#include "CrcSerialize.hpp"
#include "ArduinoJson.h"
#include <string>

CrcSerializer::CrcSerializer() : 
    mPattern(0xe792105a), // or 0x1cf2420b5 if endianness is off, 0x9960034C if hipster
    mCrcTable()
{
    
}

CrcSerializer::CrcSerializer(uint32_t aPattern) :
    mPattern(aPattern),
    mCrcTable()
{
    
}

Array<char,4> CrcSerializer::SerializeJsonMeasurement(struct Print& aOutput, double aValue, const char* aMeasType, const char* aUnits)
{
    StaticJsonDocument<256> doc;
    doc["source"] = "BME680";
    doc["meas_type"]  = aMeasType;
    doc["time"] = millis()/1000.0f;
    doc["units"] = aUnits;
    doc["value"] = aValue;

    String dataString = "";

    serializeJson(doc,dataString);

    Array<char, 4> buffer;
    CalculateCrc(dataString.c_str(), dataString.length(), buffer);

    String bufferString;
    for(int i = 0; i < 4; i++)
    {
        bufferString += buffer[i];
    }

    dataString += bufferString;
    aOutput.println(dataString);
    aOutput.println(String((int)buffer[0], DEC) + String((int)buffer[1], DEC) + String((int)buffer[2], DEC) + String((int)buffer[3], DEC));

    doc.clear();

    return buffer;
}

void CrcSerializer::InitializeCrcTable()
{
    
    mCrcTable[0] = 0;
    uint32_t crc = 1; 

    int i = 128;
    while(i>0)
    {
        if (crc & 1)
        {
            crc = (crc >> 1) ^ mPattern;
        } 
        else 
        {
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

void CrcSerializer::SetPattern(uint32_t aPattern)
{
    mPattern = aPattern;
}

uint32_t CrcSerializer::GetPattern()
{
    return mPattern;
}

void CrcSerializer::CalculateCrc(const char* aData, int aLen, Array<char,4>& aCrc)
{
    uint32_t remainder = 0;
    // A popular variant complements rem here
    for(int i = 0; i<aLen ; i++)
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
        remainder = (remainder >> 8) ^ mCrcTable[aData[i] ^ rightmost];
    }

    //LSB
    aCrc[3] = (remainder >> 24 & 0xFF);
    aCrc[2] = (remainder >> 16 & 0xFF);
    aCrc[1] = (remainder >> 8 & 0xFF);
    aCrc[0] = (remainder & 0xFF);    
}


