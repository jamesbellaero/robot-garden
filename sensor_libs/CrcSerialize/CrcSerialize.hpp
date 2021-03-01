#ifndef CRCSERIALIZE_H
#define CRCSERIALIZE_H

#include "Arduino.h"

#include <Array.h>

// https://en.wikipedia.org/wiki/Computation_of_cyclic_redundancy_checks#Multi-bit_computation

class CrcSerializer
{
public:
    CrcSerializer();
    CrcSerializer(uint32_t aPattern);      
    
    Array<char,4> SerializeJsonMeasurement(struct Print& aOutput, double aValue, const char* aMeasType, const char* aUnits);
    void InitializeCrcTable();
    void SetPattern(uint32_t aPattern);
    uint32_t GetPattern();
    void CalculateCrc(const char* aData, int aLen, Array<char,4>& aCrc);

protected:
    uint32_t mPattern;
    // Define big endian crc lookup table here
    uint8_t mCrcTable[256];

};


#endif // CRCSERIALIZE_H