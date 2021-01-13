#include "bme680.h"

void setup() {
  


  
  // Suggested defaults from Bosch
  struct bme680_dev gas_sensor;
  
  gas_sensor.dev_id = BME680_I2C_ADDR_PRIMARY;
  gas_sensor.intf = BME680_I2C_INTF;
  gas_sensor.read = ;
  gas_sensor.write = user_i2c_write;
  gas_sensor.delay_ms = 100; //100 ms
  /* amb_temp can be set to 25 prior to configuring the gas sensor 
   * or by performing a few temperature readings without operating the gas sensor.
   */
  gas_sensor.amb_temp = 25;
  
  
  int8_t rslt = BME680_OK;
  rslt = bme680_init(&gas_sensor);

  uint16_t meas_period;
  bme680_get_profile_dur(&meas_period, &gas_sensor);

  gas_sensor.tph_sett.os_hum = BME680_OS_2X;
  gas_sensor.tph_sett.os_pres = BME680_OS_4X;
  gas_sensor.tph_sett.os_temp = BME680_OS_8X;
  gas_sensor.tph_sett.filter = BME680_FILTER_SIZE_3;
  
  /* Set the remaining gas sensor settings and link the heating profile */
  gas_sensor.gas_sett.run_gas = BME680_ENABLE_GAS_MEAS;
  /* Create a ramp heat waveform in 3 steps */
  gas_sensor.gas_sett.heatr_temp = 320; /* degree Celsius */
  gas_sensor.gas_sett.heatr_dur = 150; /* milliseconds */
  
  /* Select the power mode */
  /* Must be set before writing the sensor configuration */
  gas_sensor.power_mode = BME680_FORCED_MODE; 
  
  /* Set the required sensor settings needed */
  set_required_settings = BME680_OST_SEL | BME680_OSP_SEL | BME680_OSH_SEL | BME680_FILTER_SEL 
      | BME680_GAS_SENSOR_SEL;
  
  /* Set the desired sensor configuration */
  rslt = bme680_set_sensor_settings(set_required_settings,&gas_sensor);
  
  /* Set the power mode */
  rslt = bme680_set_sensor_mode(&gas_sensor);

}

void loop() {
  // More Bosch code
  delay(meas_period); /* Delay till the measurement is ready */

  rslt = bme680_get_sensor_data(&data, &gas_sensor);

  printf("T: %.2f degC, P: %.2f hPa, H %.2f %%rH ", data.temperature / 100.0f,
      data.pressure / 100.0f, data.humidity / 1000.0f );
  /* Avoid using measurements from an unstable heating setup */
  if(data.status & BME680_GASM_VALID_MSK)
      printf(", G: %d ohms", data.gas_resistance);

  printf("\r\n");

  /* Trigger the next measurement if you would like to read data out continuously */
  if (gas_sensor.power_mode == BME680_FORCED_MODE) {
      rslt = bme680_set_sensor_mode(&gas_sensor);
  }
}