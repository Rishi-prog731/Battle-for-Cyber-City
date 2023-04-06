# Battle-for-Cyber-City

Cyber City stradegy game for [SAMSAT](https://www.samsat.org/)

- [Battle-for-Cyber-City](#battle-for-cyber-city)
  - [Instructions](#instructions)
  - [The Team](#the-team)
  - [PLC Mappings](#plc-mappings)
    - [Power (10.10.10.1)](#power-1010101)
    - [Hospital (10.10.10.2)](#hospital-1010102)
    - [Police/Fire (10.10.10.3)](#policefire-1010103)
    - [Traffic (10.10.10.4)](#traffic-1010104)
  - [Design](#design)
  
## Instructions

* The src directory stores all the development files.
* create a python virtual environment in the src folder
* install requirements.txt
* if you install a package add it to requirements.txt
* make sure you keep the files organized and follow standard coding conventions

## The Team

* Lead Developer 💻 `Benjamin Bowles`
* Developer 💻 `??`
* Lead Designer 🎨 `Roland Catapia`

## PLC Mappings

### Power (10.10.10.1)
| Coil | Mapping           |
| ---- | ----------------- |
| 0    | Business District |
| 1    | Hospital          |
| 2    | Police / Fire     |
| 3    | Industrial Area   |
| 4    | University        |
| 5    | Residential       |

### Hospital (10.10.10.2)

| Coil | Mapping           |
| ---- | ----------------- |
| 0    | Power             |
| 1    | Generator Running |

### Police/Fire (10.10.10.3)

| Coil | Mapping           |
| ---- | ----------------- |
| 0    | Power             |
| 1    | Generator Running |

### Traffic (10.10.10.4)

| Coil | Mapping         |
| ---- | --------------- |
| 0    | Green Light NS  |
| 1    | Yellow Light NS |
| 2    | Red Light NS    |
| 3    | Green Light EW  |
| 4    | Yellow Light EW |
| 5    | Red Light EW    |

## Design
[Figma.com](https://www.figma.com/file/mn40OqTiIRspf0wprOv92w/Cyber-City-Range?node-id=0%3A1&t=ArfQfiEURLy880xD-1)
