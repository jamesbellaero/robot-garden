# AS7341 Breakout Board

This board is meant to enable the user to access the pins on the AS7341. To get it printed, upload the .kicad_pcb file to Oshpark's website.

There is no guarantee this board will work. I'm not even an electrical engineer. Don't blame me if you fry or break your stuff using this.

## Required components

* 3x 4.7k Ohm Resistors
* 1x 3 mm LED bulb (Like this one: https://www.sparkfun.com/products/533)
* 1x 1 by 6 Pin Header with 2.54 mm pitch

## Setup

Note that I've yet to actually receive all of the necessary components and, as a result, cannot verify this works even when done right.

<b>Warning</b>: Do not let the soldering iron exceed 260 Celsius (requirement from AS7341 documentation)

1. Using a really thin head, figure out a way to solder the AS7341 to the board. Be sure to match the pads correctly (there's a corner missing on the VDD pin).
2. Proceed to solder the resistors, cutting off the excess metal wires on each.
3. Solder the LED, cutting off the excess metal wire.
4. Solder the pin header

## Pinout

Sorry these are so mixed up. I wanted to use only one side of the board to reduce costs, which necessitated a weird ordering.

1 - GND
2 - SCL
3 - VDD (1.8 volts)
4 - SDA
5 - INT
6 - GPIO

## Software

Software to actually use this is not completed yet. Refer to the AS7341 documentation or find some other software online in the meantime.


