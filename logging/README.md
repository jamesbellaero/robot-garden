This small python library is setup to read data from multiple ports and log it to files.

Requires the following python modules:
```pyserial```
```getopt```
```json``` (3.8- only)

An overview for how this program runs is:
1. The user runs ```garden_logging.py``` 
2. The ArgumentParser determines which ports should be opened
3. A PortReader manages ports and reads packets delineated by newline characters
4. A DataParser turns those packets from JSON into Python objects
5. A DataLogger writes that data to a different directories and files depending on the source and data type, respectively 

To interface with it, two things are required.
- First, you have to be sending data in the form of JSON packets over a network. 
- Second, you have to tell this program what those ports are for it to talk to them.

Lastly, the JSON data should take on the following format:

```json
{
    "source" : "Whatever the source name is",
    "meas_type" : "Type of measurement coming from the source",
    "time" : 0,
    "value" : 1
}
```

This could easily be improved upon by having all measurements of a given source come in the same JSON block. That may come with time.

Default call: python garden_logging.py -p "COM3" -d "testing-files" -P "prefix" -S "suffix"
