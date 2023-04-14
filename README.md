# Battle-for-Cyber-City

Cyber City stradegy game for [SAMSAT](https://www.samsat.org/)

- [Battle-for-Cyber-City](#battle-for-cyber-city)
  - [Folder Stucture](#folder-structure)
  - [Instructions for Development](#instructions-for-development)
  - [The Team](#the-team)
  - [PLC Mappings](#plc-mappings)
    - [Power (10.10.10.1)](#power-1010101)
    - [Hospital (10.10.10.2)](#hospital-1010102)
    - [Police/Fire (10.10.10.3)](#policefire-1010103)
    - [Traffic (10.10.10.4)](#traffic-1010104)
  - [Design](#design)

## Folder Structure

* The `src` directory stores all the development files.
* The `doc` directory stores all the documentation files.

## Instructions for Development

* create a python virtual environment in the `src` folder
* use pip to install requirements.txt
* if you install a package add it to requirements.txt by using pip freeze into the file
* make sure you keep the files organized and follow standard coding conventions
* don't work on the main branch, create a development branch for you and make pull requests

## The Team

* Lead Developer 💻 `Benjamin` [@HoleInOneGolfer](https://www.github.com/HoleInOneGolfer)
* Game Developer 💻 `Rishi` [@rishih](https://www.github.com/Rishi-prog731)
* Lead Designer 🎨 `Roland`

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
UX: [Figma.com](https://www.figma.com/file/mn40OqTiIRspf0wprOv92w/Cyber-City-Range?node-id=0%3A1&t=ArfQfiEURLy880xD-1)

Game: [Google Sheet](https://docs.google.com/spreadsheets/d/1fAyjl4c2pVBRPMtv6dN021eSeIyQtpjlF3AOrqUOK1o/edit)