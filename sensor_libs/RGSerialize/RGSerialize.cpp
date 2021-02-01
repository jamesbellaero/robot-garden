#include "RGSerialize.hpp"
#include "ArduinoJson.h"

RGSerialize::RGSerialize() : 
    mPattern(0x4C036099), // or 0x9960034C if endianness is off
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
    
    mCrcTable[0] = 0;
    uint32_t crc = 1; 

    int i = 128;
    while(i>0)
    {
        if crc & 1 {
            crc = (crc >> 1) ^ mPattern;
        } else {
            crc = crc >> 1;
        }
        // crc is the value of big_endian_table[i]; let j iterate over the already-initialized entries
        for(int j = 0; j<256;j+= 2*i)
        {
            mCrcTable[i + j] = crc ^ mCrcTable[j];
        }
        i = i >> 1;
    } 
}

void RGSerialize::SetPattern(uint32_t aPattern)
{
    mPattern = aPattern;
}

uint32_t RGSerialize::GetPattern()
{
    return mPattern:
}

void RGSerialize::CalculateCrc(const char* aData, int aLen, char* aCrc)
{
        uint32_t remainder = 0;
        // A popular variant complements rem here
        for(int i = 0; i<len ; i++)
        {
            remainder  = remainder ^ aData[i];
            // for j from 1 to 8 {   // Assuming 8 bits per byte
            //     if rem and 0x0001 {   // if rightmost (most significant) bit is set
            //         rem  := (rem rightShift 1) ^ mPattern
            //     } else {
            //         rem  := rem rightShift 1
            //     }
            // }
            uint8_t rightmost = (uint8_t)(remainder & 255);
            remmainder = (remainder >> 8) ^ mCrcTable[aData[i] ^ rightmost];
        }
        // A popular variant complements rem here
        return remainder;
    }
}


