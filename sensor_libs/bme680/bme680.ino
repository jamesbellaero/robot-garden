#include "bme680.h"
#include "bme680_defs.h"
#include "Wire.h"
#include "ArduinoJson.h"
#include "string.h"

#include "CrcSerialize.hpp"


uint16_t meas_period;
struct bme680_dev gas_sensor;
TwoWire *bmeWire = NULL;


/** Type definitions */
/*!
 * Generic communication function pointer
 * @param[in] dev_id: Place holder to store the id of the device structure
 *                    Can be used to store the index of the Chip select or
 *                    I2C address of the device.
 * @param[in] reg_addr:  Used to select the register the where data needs to
 *                      be read from or written to.
 * @param[in/out] reg_data: Data array to read/write
 * @param[in] len: Length of the data array
 */
//typedef int8_t (*bme680_com_fptr_t)(uint8_t dev_id, uint8_t reg_addr, uint8_t *data, uint16_t len);

int8_t readI2CPin(uint8_t dev_id, uint8_t reg_addr, uint8_t *reg_data, uint16_t len)
{
  //https://www.arduino.cc/en/Tutorial/LibraryExamples/MasterReader
  bmeWire->beginTransmission((uint8_t)dev_id);
  bmeWire->write((uint8_t)reg_addr);
  bmeWire->endTransmission();
  
  if (len != bmeWire->requestFrom((uint8_t)dev_id, (byte)len)) {
    return 1;
  }
  while (len--) {
    *reg_data = (uint8_t)bmeWire->read();
    reg_data++;
  }
  return 0;
}

int8_t writeI2CPin(uint8_t dev_id, uint8_t reg_addr, uint8_t *reg_data, uint16_t len)
{
  //https://www.arduino.cc/en/Tutorial/LibraryExamples/MasterWriter
  bmeWire->beginTransmission((uint8_t)dev_id);
  bmeWire->write((uint8_t)reg_addr);
  while (len--) {
    bmeWire->write(*reg_data);
    reg_data++;
  }
  bmeWire->endTransmission();
  
  return 0;
}

static int8_t null_ptr_check(const struct bme680_dev *dev)
{
  int8_t rslt;

  if ((dev == NULL) || (dev->read == NULL) || (dev->write == NULL) || (dev->delay_ms == NULL)) {
    /* Device structure pointer is not valid */
    rslt = BME680_E_NULL_PTR;
  } else {
    /* Device structure is fine */
    rslt = BME680_OK;
  }

  return rslt;
}

static void delay_msec(uint32_t ms) { delay(ms); }

void setup() {
  Serial.begin(9600);
  bmeWire = &Wire;
  bmeWire->begin();
  
  // Suggested defaults from Bosch  
  gas_sensor.dev_id = BME680_I2C_ADDR_PRIMARY;
  gas_sensor.intf = BME680_I2C_INTF;
  gas_sensor.read = &readI2CPin;
  gas_sensor.write = &writeI2CPin;
  gas_sensor.delay_ms = &delay_msec; 
  // amb_temp can be set to 25 prior to configuring the gas sensor 
  // or by performing a few temperature readings without operating the gas sensor.
   
  gas_sensor.amb_temp = 21;

  gas_sensor.tph_sett.os_hum = BME680_OS_2X;
  gas_sensor.tph_sett.os_pres = BME680_OS_4X;
  gas_sensor.tph_sett.os_temp = BME680_OS_8X;
  gas_sensor.tph_sett.filter = BME680_FILTER_SIZE_3;
  
  // Set the remaining gas sensor settings and link the heating profile 
  //gas_sensor.gas_sett.run_gas = BME680_ENABLE_GAS_MEAS;
  // Create a ramp heat waveform in 3 steps 
  gas_sensor.gas_sett.heatr_temp = 320; // degree Celsius 
  gas_sensor.gas_sett.heatr_dur = 150; // milliseconds 
  
  // Select the power mode 
  // Must be set before writing the sensor configuration 
  gas_sensor.power_mode = BME680_FORCED_MODE; 
  
  
  int8_t rslt = BME680_OK;
  Serial.print(null_ptr_check(&gas_sensor));
  Serial.print("Initializing...\n");
  
  rslt = bme680_init(&gas_sensor);
  Serial.print("Result: ");
  Serial.println(rslt);
  
  uint16_t meas_period;
  bme680_get_profile_dur(&meas_period, &gas_sensor);

  
  // Set the required sensor settings needed 
  uint8_t set_required_settings = BME680_OST_SEL | BME680_OSP_SEL | BME680_OSH_SEL | BME680_FILTER_SEL 
      | BME680_GAS_SENSOR_SEL;
  
  // Set the desired sensor configuration 
  rslt = bme680_set_sensor_settings(set_required_settings,&gas_sensor);
  
  // Set the power mode 
  rslt = bme680_set_sensor_mode(&gas_sensor);
}

void loop() {
  
  // More Bosch code
  delay(meas_period); // Delay till the measurement is ready 

  struct bme680_field_data data;
  int8_t rslt = bme680_get_sensor_data(&data, &gas_sensor);

  serializeJsonMeasurement(Serial, data.temperature/100.0f,"Temperature","Celsius");
  serializeJsonMeasurement(Serial, data.pressure*10.0f,"Pressure","Pascals"); // divide by 100 to get hPa
  serializeJsonMeasurement(Serial, data.humidity/1000.0f,"Humidity","Relative Humidity");
  
  if(data.status & BME680_GASM_VALID_MSK)
  {
    serializeJsonMeasurement(Serial, data.gas_resistance,"Gas Resistance","Ohms");
  }
  
  if (gas_sensor.power_mode == BME680_FORCED_MODE) {
      rslt = bme680_set_sensor_mode(&gas_sensor);
  }
}
