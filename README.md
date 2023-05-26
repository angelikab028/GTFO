# GTFO
G.T.F.O. (General Turret For Occupants) Security System 

Team Members: Taneesha Sharma, Cody Kurpanek, Yuchen Zhu, & Angelika Bermudez

## Use Case
	Home security is a serious concern that if improved, could prevent theft and assault amongst other crimes. Currently, there exist security systems such as Ring, ADT, or Nest that work as doorbell/camera systems. However the measures that these systems take to prevent home invasion are mostly dependent on user action. For example, a user must lock the house and turn on the security system for it to trigger an alarm from attempts at opening a door. This alarm sounds a loud siren and asks the user if police intervention is needed. A potential issue with these types of systems is only having this protection when it is enabled, which is what our product wants to solve.
    G.T.F.O. Security System’s goal is to improve the state of current home security and decrease the amount of necessary user interference. In order to do this, G.T.F.O. uses facial recognition to detect intruders at an entrance of a home. When an intruder is detected, the system will notify the homeowner through their phone. If the intruder manages to break into the home, a turret will be waiting for the uninvited guest to defend the home and call the authorities. The biggest challenges that we will encounter when implementing this system include facial recognition accuracy and turret aim accuracy by which both must be calculated quickly as well. Another issue that extends from facial recognition is permitting the ability for the user to add “familiar” facial scans so that new faces that are not intruders are not detected as one.

## Network Diagrams
![alt text](https://github.com/angelikab028/GTFO/blob/main/networkdiagram1.png?raw=true)

![alt text](https://github.com/angelikab028/GTFO/blob/main/networkdiagram2.png?raw=true)


## Device Catalog
    - Jetson Nano #1, Facial Recognition:
        - Angetube 1080P HD Webcam is plugged into a 4G Jetson Nano through the USB Port.
        - 4G Jetson Nano Remains on and stays plugged using a 2.5A micro usb power supply.
            - ARMv8 4 core processor
            - 128-core NVIDIA GPU
            - 1.43 GHz Clock Speed

    - Laptop Server, Middleware:
        - Dell XPS 13 Laptop remains plugged in through the usb c power cord.
            - Core i7-1165G7 4 core processor 
            - 32 G RAM
            - 3.7GHz Clock Speed

    - Jetson Nano #2, Turret:
        - Logitech C270 Webcam is plugged into the 4G Jetson Nano through the USB Port.
        - Arduino Uno R3 is plugged into the 4G Jetson Nano through the USB Port.
        - 4G Jetson Nano Remains on and stays plugged using a DC5V 4A power supply.
            - ARMv8 4 core processor
            - 128-core NVIDIA GPU
            - 1.43 GHz Clock Speed

    - Google Servers, Cloud Storage:
        - Data is sent to the Google Servers through the Cloud Storage API
        - Computational Resources decided by the Cloud Storage API



