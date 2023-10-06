# EV3-Prototype-Robot
EV3 robot - prototype for warehouse box management robot

<h1 align="center">
  <br>

<h4 align="center">A prototype of a robot used in warehouse facilities to move boxes to specified positions using bar codes for better inventory management</h4>



## About

### We broke down the problem into different pieces and tackled each part one by one:
* Robot needed to navigate through the warehouse
* Stop at given location
* Scan barcode on the box and identify drop off location based on the barcode
* Lift the box and drop it off at the location matched through the barcode

### For each part we developed the following functionalities : 
#### Navigation
For Navigation, we used two motors. 
After running tests, we found the best speed at which the robot did not drift and get off the track due to friction. 
The tests also helped us determine if the robot was not going in a straight line.
#### Stopping at a Box
We used an ultrasonic sensor to stop near a box.
The ultrasonic sensor was programmed to sense if there was an object near the robot. 
If yes, then the robot stops and initiates the barcode scanning function.
#### Barcode Scanning
To scan the barcode, a light sensor was used.
As the barcodes are combinations of black and white lines, the light sensors were programmed to sense the color on barcode.
White returns 0, Black returns 1.
These numbers were stored in an array and after successful scanning, the array was referenced to already existing barcode arrays for specified drop locations of each box.
#### Lifting and drop off
A forklift mechanism was used to pick up the box and drop it at the specified location.

## How To Use

To run this application, you will need the python-ev3dev2 module installed : 
```bash
# In the command line
$ pip install python-ev3dev2
```

```
# in the python code
import ev3
```

> **Note**
> If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.


## Download

You can [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) the latest installable version of Markdownify for Windows, macOS and Linux.

## Emailware

Markdownify is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <bullredeyes@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## Credits

This software uses the following open source packages:

- [Electron](http://electron.atom.io/)
- [Node.js](https://nodejs.org/)
- [Marked - a markdown parser](https://github.com/chjj/marked)
- [showdown](http://showdownjs.github.io/showdown/)
- [CodeMirror](http://codemirror.net/)
- Emojis are taken from [here](https://github.com/arvida/emoji-cheat-sheet.com)
- [highlight.js](https://highlightjs.org/)

## Related

[markdownify-web](https://github.com/amitmerchant1990/markdownify-web) - Web version of Markdownify

## Support

<a href="https://www.buymeacoffee.com/5Zn8Xh3l9" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/amitmerchant">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## You may also like...

- [Pomolectron](https://github.com/amitmerchant1990/pomolectron) - A pomodoro app
- [Correo](https://github.com/amitmerchant1990/correo) - A menubar/taskbar Gmail App for Windows and macOS

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)


