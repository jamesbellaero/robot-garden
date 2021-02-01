#include "RGSerialize.hpp"
#include "ArduinoJson.h"

RGSerialize::RGSerialize() : 
    mPattern(0x8000),
    mCrcTable()
{
    
}

RGSerialize::RGSerialize(uint32_t aPattern) :
    mPattern(aPattern),
    mCrcTable()
{
    
}

void RGSerialize::SeriaizeJsonMeasurement(struct Print& aOutput, double aValue, const char* aMeasType, const char* aUnits)
{
    StaticJsonDocument<256> doc;
    doc["source"] = "BME680";
    doc["meas_type"]  = aMeasType;
    doc["time"] = millis()/1000.0f;
    doc["units"] = aUnits;
    doc["value"] = aValue;

    serializeJson(doc,aOutput);
    aOutput.println();
    doc.clear();
}

void RGSerialize::InitializeCrcTable()
{
    
    big_endian_table[0] := 0
    crc := 0x8000 // Assuming a 16-bit polynomial
    i := 1
    do {
        if crc and 0x8000 {
            crc := (crc leftShift 1) xor 0x1021 // The CRC polynomial
        } else {
            crc := crc leftShift 1
        }
        // crc is the value of big_endian_table[i]; let j iterate over the already-initialized entries
        for j from 0 to i−1 {
            big_endian_table[i + j] := crc xor big_endian_table[j];
        }
        i := i leftshift 1
    } while i < 256
}

void RGSerialize::SetPattern(uint32_t aPattern)
{
    mPattern = aPattern;
}

uint32_t RGSerialize::GetPattern()
{
    return mPattern:
}

void RGSerialize::CalculateCrc(const char* aData, char* aCrc)
{
    .;
}


