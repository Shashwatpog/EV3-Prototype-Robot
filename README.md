# EV3-Prototype-Robot (Now Archived - Team 188 Spring 2022 ENED 1120 project)
EV3 robot - prototype for warehouse box management robot
<br>
A prototype of a robot used in warehouse facilities to move boxes to specified positions using bar codes for better inventory management

## About

### We broke down the problem into different pieces and tackled each part one by one:
* Robot needed to navigate through the warehouse
* Stop at a given location
* Scan barcode on the box and identify drop off location based on the barcode
* Lift the box and drop it off at the location matched through the barcode
<img width="479" alt="image" src="https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/98c0bf5d-933b-4e1c-b215-7f11c7fde861">

### For each part we developed the following functionalities :

#### 1. Navigation
For Navigation, we used two motors. 
After running tests, we found the best speed at which the robot did not drift and get off the track due to friction. 
The tests also helped us determine if the robot was not going in a straight line.

#### 2. Stopping at a Box
We used an ultrasonic sensor to stop near a box.
The ultrasonic sensor was programmed to sense if there was an object near the robot. 
If yes, then the robot stops and initiates the barcode scanning function.

#### 3. Barcode Scanning
<img width="415" alt="image" src="https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/50a56f02-ab7e-49a9-857f-832024309dae">

To scan the barcode, a light sensor was used.
As the barcodes are combinations of black and white lines, the light sensors were programmed to sense the color on barcode.
White returns 0, Black returns 1.
These numbers were stored in an array and after successful scanning, the array was referenced to already existing barcode arrays for specified drop locations of each box.

#### 4. Lifting and drop off
A forklift mechanism was used to pick up the box and drop it at the specified location.

## How To Use

To run this application, you will need the python-ev3dev2 module installed : 
```bash
# In the command line
$ pip install python-ev3dev2
```

```
#include the following comment at the beginning of each ev3dev2 python file:
#!/usr/bin/env python3
import ev3dev2
```
## Additional pictures + Design Notebook

<img align = center height = "200" width="400" alt="image" src="https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/d44f7be9-6003-45dd-8726-68f8fad19a3f">
<img align = center height = "200" width="303" alt="image" src="https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/af426566-2655-4be0-a932-ab6c872e746d">
<br>
<img align = center height = "200 "width="255" alt="image" src="https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/602301a7-792b-4f2b-9be4-fabe6526f995">
<img align = center height = "200" width="338" alt="image" src="https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/309d0102-1ef3-4331-86bb-9b29054e08a6">
<br>
<img align = center height = "400" width="400" src = "https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/315fc55a-4825-42a2-81d5-b5c6c42f913b">
<img align = center height = "400" width="400" src = "https://github.com/Shashwatpog/EV3-Prototype-Robot/assets/141262519/f7615d53-519c-4616-bf54-935e3cd8f7a3">





> **Note**
> <br>
> If using VS code make sure to change from CRLF to LF <br>
> Ev3dev2 docs -> [Documentation](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/spec.html)<br>
> Download EV3dev2 extension package on VS code <br>
> [Ev3dev2 Support and Config file](https://drive.google.com/file/d/14C0nthxZp0Bdg3hHogh25fNWywiaQqdh/view?usp=sharing)


## License

MIT

---
> GitHub [@Shashwatpog](https://github.com/Shashwatpog)



