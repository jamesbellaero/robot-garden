EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "AS7341 Breakout Board"
Date "2020-07-27"
Rev "v1.0"
Comp ""
Comment1 ""
Comment2 "creativecommons.org/licenses/by/4.0/"
Comment3 "License: CC BY 4.0"
Comment4 "Author: James Bell"
$EndDescr
$Comp
L power:VDD #PWR05
U 1 1 5F204209
P 6100 3200
F 0 "#PWR05" H 6100 3050 50  0001 C CNN
F 1 "VDD" H 6115 3373 50  0000 C CNN
F 2 "" H 6100 3200 50  0001 C CNN
F 3 "" H 6100 3200 50  0001 C CNN
	1    6100 3200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 5F1FF013
P 6300 4200
F 0 "R3" H 6230 4154 50  0000 R CNN
F 1 "R" H 6230 4245 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 6230 4200 50  0001 C CNN
F 3 "~" H 6300 4200 50  0001 C CNN
	1    6300 4200
	-1   0    0    1   
$EndComp
$Comp
L Device:R R2
U 1 1 5F1FEC6D
P 6000 4200
F 0 "R2" H 5930 4154 50  0000 R CNN
F 1 "R" H 5930 4245 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5930 4200 50  0001 C CNN
F 3 "~" H 6000 4200 50  0001 C CNN
	1    6000 4200
	-1   0    0    1   
$EndComp
$Comp
L power:VDD #PWR04
U 1 1 5F20B48A
P 6000 4350
F 0 "#PWR04" H 6000 4200 50  0001 C CNN
F 1 "VDD" H 6015 4523 50  0000 C CNN
F 2 "" H 6000 4350 50  0001 C CNN
F 3 "" H 6000 4350 50  0001 C CNN
	1    6000 4350
	-1   0    0    1   
$EndComp
$Comp
L power:VDD #PWR06
U 1 1 5F20C015
P 6300 4350
F 0 "#PWR06" H 6300 4200 50  0001 C CNN
F 1 "VDD" H 6315 4523 50  0000 C CNN
F 2 "" H 6300 4350 50  0001 C CNN
F 3 "" H 6300 4350 50  0001 C CNN
	1    6300 4350
	-1   0    0    1   
$EndComp
$Comp
L power:VDD #PWR03
U 1 1 5F20CC4C
P 6000 2650
F 0 "#PWR03" H 6000 2500 50  0001 C CNN
F 1 "VDD" H 6015 2823 50  0000 C CNN
F 2 "" H 6000 2650 50  0001 C CNN
F 3 "" H 6000 2650 50  0001 C CNN
	1    6000 2650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5F1FD9ED
P 6000 2800
F 0 "R1" H 5930 2754 50  0000 R CNN
F 1 "R" H 5930 2845 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5930 2800 50  0001 C CNN
F 3 "~" H 6000 2800 50  0001 C CNN
	1    6000 2800
	-1   0    0    1   
$EndComp
$Comp
L AS7341-~Symbol~Library:AS7341 U1
U 1 1 5F1FC45E
P 5950 3500
F 0 "U1" H 6178 3521 50  0000 L CNN
F 1 "AS7341" H 6178 3430 50  0000 L CNN
F 2 "AS7341- Breakout Library:AS7341" V 5950 3500 50  0001 C CNN
F 3 "" V 5950 3500 50  0001 C CNN
	1    5950 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 3200 6000 3000
Wire Wire Line
	6100 4050 6300 4050
$Comp
L power:GND #PWR01
U 1 1 5F20E2B8
P 5800 3850
F 0 "#PWR01" H 5800 3600 50  0001 C CNN
F 1 "GND" H 5805 3677 50  0000 C CNN
F 2 "" H 5800 3850 50  0001 C CNN
F 3 "" H 5800 3850 50  0001 C CNN
	1    5800 3850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 5F20EB29
P 5900 3200
F 0 "#PWR02" H 5900 2950 50  0001 C CNN
F 1 "GND" H 5905 3027 50  0000 C CNN
F 2 "" H 5900 3200 50  0001 C CNN
F 3 "" H 5900 3200 50  0001 C CNN
	1    5900 3200
	-1   0    0    1   
$EndComp
$Comp
L Device:LED D1
U 1 1 5F20F3A5
P 5450 3050
F 0 "D1" H 5443 2795 50  0000 C CNN
F 1 "LED" H 5443 2886 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm" H 5450 3050 50  0001 C CNN
F 3 "~" H 5450 3050 50  0001 C CNN
	1    5450 3050
	-1   0    0    1   
$EndComp
Wire Wire Line
	5600 3050 5800 3050
Wire Wire Line
	5800 3050 5800 3200
$Comp
L power:GND #PWR0101
U 1 1 5F212E6D
P 5300 3050
F 0 "#PWR0101" H 5300 2800 50  0001 C CNN
F 1 "GND" H 5305 2877 50  0000 C CNN
F 2 "" H 5300 3050 50  0001 C CNN
F 3 "" H 5300 3050 50  0001 C CNN
	1    5300 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	6950 3300 7050 3300
Wire Wire Line
	7000 3400 7050 3400
Wire Wire Line
	6900 3200 7050 3200
Wire Wire Line
	6900 3100 7050 3100
Wire Wire Line
	6000 3850 6000 4000
Wire Wire Line
	6100 3850 6100 4050
$Comp
L Connector_Generic:Conn_01x06 J1
U 1 1 5F21700B
P 7250 3200
F 0 "J1" H 7330 3192 50  0000 L CNN
F 1 "Conn_01x06" H 7330 3101 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 7250 3200 50  0001 C CNN
F 3 "~" H 7250 3200 50  0001 C CNN
	1    7250 3200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F224E48
P 7050 3000
F 0 "#PWR?" H 7050 2750 50  0001 C CNN
F 1 "GND" H 7055 2827 50  0000 C CNN
F 2 "" H 7050 3000 50  0001 C CNN
F 3 "" H 7050 3000 50  0001 C CNN
	1    7050 3000
	-1   0    0    1   
$EndComp
$Comp
L power:VDD #PWR?
U 1 1 5F2256D0
P 6900 3200
F 0 "#PWR?" H 6900 3050 50  0001 C CNN
F 1 "VDD" V 6915 3327 50  0000 L CNN
F 2 "" H 6900 3200 50  0001 C CNN
F 3 "" H 6900 3200 50  0001 C CNN
	1    6900 3200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6000 3000 6900 3000
Wire Wire Line
	6900 3000 6900 3100
Connection ~ 6000 3000
Wire Wire Line
	6000 3000 6000 2950
Wire Wire Line
	6300 4050 6950 4050
Wire Wire Line
	6950 4050 6950 3300
Connection ~ 6300 4050
Wire Wire Line
	6000 4000 7000 4000
Wire Wire Line
	7000 4000 7000 3400
Connection ~ 6000 4000
Wire Wire Line
	6000 4000 6000 4050
Wire Wire Line
	7050 3850 7050 3500
Wire Wire Line
	5900 3850 7050 3850
$EndSCHEMATC