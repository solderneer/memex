---
title: "Droid Project"
description: "Building the hexapod simulation"
emoji: "🦿"
pubDate: "May 30 2020"
tags: ["topic/technology"]
originalPost: "https://makerforce.io/droid-project-completed-body/"
---

<iframe width="816" height="456" src="https://www.youtube.com/embed/MYIbnTOSr5M" title="Droid Project: Body IK Test" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Currently finished coupling 6 legs to a simulation body, with the leg inverse kinematics functional for all of the legs. The remaining elements to implement would be select-able individual joint controls for each leg and the body kinematics itself.

Then I completed the inverse kinematics that allows for the coupling between the body of the robot and its 6 corresponding legs (arranged with 60 degrees between each leg). I won’t bother explaining the mathematics going into these calculations in detail as they have been outlined in [Oscar Liang’s blog post](https://oscarliang.com/inverse-kinematics-implementation-hexapod-robots/) and the equations from [TogleFritz’s Lair](https://toglefritz.com/hexapod-inverse-kinematics-equations/).

The resultant equations needed a bit of tweaking, especially with the orientation of the coordinate plane and the direction of certain rotations. Additionally, the equations from TogleFritz’s Lair are unnecessarily redundant when implemented in code. I added some optimizations and loop logic to help make the equations less cumbersome to use.

```c
    void Droid::ikCalculate() {
      const float increment = M_PI/3;

      for(int i = 0; i < 6; i++) {
        vec3 bodyOffset = vec3(cos(increment * i) * legRadius, 0, sin(increment * i) * legRadius);
        vec3 legPos = vec3(
            cos(increment * i) * (DEFAULT_COXA_LEN + DEFAULT_FEMUR_LEN),
            -DEFAULT_TIBIA_LEN,
            sin(increment * i) * (DEFAULT_COXA_LEN + DEFAULT_FEMUR_LEN));

        vec3 totalPos = bodyOffset + legPos + bodyPos;

        float distToLeg = sqrt(pow(totalPos[0], 2) + pow(totalPos[2], 2));
        float angleToLeg = atan2(totalPos[2], totalPos[0]);

        float roll = tan(bodyRot[2]) * totalPos[0]; // About the Z Axis
        float pitch = tan(bodyRot[0]) * totalPos[2]; // About the X Axis

        float bodyIkX = cos(angleToLeg + bodyRot[1]) * distToLeg - totalPos[0];
        float bodyIkY = roll + pitch;
        float bodyIkZ = sin(angleToLeg + bodyRot[1]) * distToLeg - totalPos[2];

        vec3 finalLegPos = legPos + vec3(bodyIkX, bodyIkY, bodyIkZ) + bodyPos;

        // Coordinate frame transform from body to leg (rotated)
        vec3 legCordFrame = vec3(
            cos(i * increment) * finalLegPos[0] + sin(i * increment) * finalLegPos[2],
            finalLegPos[1],
            -sin(i * increment) * finalLegPos[0] + cos(i * increment) * finalLegPos[2]);

        gl::drawVector(vec3(0,0,0), legCordFrame);

        mLeg[i].moveToCoord(&legCordFrame);
      }
    }
```

With those changes and a couple of new ImGui control panels, everything is looking nice and functional!
