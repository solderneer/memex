---
title: "EdiPlane board"
description: "Building an Intel Edison based flight controller"
emoji: "✈️"
pubDate: "Jan 16 2016"
tags: ["topic/technology", "type/young-shan"]
originalPost: "https://makerforce.io/an-edison-based-flight-controller/"
---

#### Introduction

The quadcopter industry has been booming recently and along with that has come a surge of new flight controllers. Along with the popular APM and Naza platforms, flight controllers like the Naze 32 are also taking front stage. Recently, I decided to build an autonomous quad from scratch and I found myself stuck. I simply could not find a capable flight platform for a fully autonomous flight platform with a vision system. All the flight controllers today required some form of seperate computer like the Raspberry Pi to carry out vision robotics. So, I decided to do myself a favor and go make a fully autonomous quad platform.

#### The EdiPlane board

The EdiPlane board is Edison-Arduino integrated board which is intended for use in a fully autonomous drone/rover platform. It takes the ATMEL ATMEGA 328 chip and combines it with the computing power of the Intel Edison to get a perfect combination of computing power and I/O pins.

![](https://makerforce.io/content/images/2016/01/Edison-image.jpg)

#### How it works

The EdiPlane is simply a board which allows an Edison to be plugged into a "arduino board" and allows for serial UART communciation between the ATMEGA328 and the Edison. This means that the control part of the quadcopter is controlled by the ATMEGA328 while the Edison acts as the high level processor doing vision processing and sending commands to the ATMEGA328. This ecosystem allows for the workload to be split and for the flight controller to perform intensive computational tasks.

The full SMD nature of the board also makes it very compact and allows for the board to only span 5cm\*5cm. However, since this was intended to be a completely autonomous platform it does not have receiver inputs. Instead manual override and control is given through Wifi and SSH into the Edison.

![](https://makerforce.io/content/images/2016/01/Board-rev-6.PNG)

#### Conclusion

This board is intended for the serious robotics enthusiast and hobbyist and allows them to implement it in any platform they could possibly want-rover,ship or drone. I will be posting a follow up on this to outline the use-cases of this board and also taking a look at the viability and usefulness of the board.
