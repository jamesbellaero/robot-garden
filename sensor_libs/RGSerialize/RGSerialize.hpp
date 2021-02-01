#ifndef RGSERIALIZE_H
#define RGSERIALIZE_H

#include "Arduino.h"

// https://en.wikipedia.org/wiki/Computation_of_cyclic_redundancy_checks#Multi-bit_computation

class RGSerializer
{
public:
    RGSerializer();
    RGSerializer(uint32_t aPattern);      
    
    uint32_t SerializeJsonMeasurement(struct Print& aOutput, double aValue, const char* aMeasType, const char* aUnits)
    void InitializeCrcTable();
    void SetPattern(uint32_t aPattern);
    uint32_t GetPattern();
    void CalculateCrc(const char* aData, char* aCrc);

protected:
    uint32_t mPattern;
    // Define big endian crc lookup table here
    uint8_t mCrcTable[256];

};


#endif // RGSERIALIZE_H