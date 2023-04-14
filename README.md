# Battle-for-Cyber-City

- [Battle-for-Cyber-City](#battle-for-cyber-city)
  - [The Team](#the-team)
  - [Instructions for Development](#instructions-for-development)
    - [Installing New Dependencies](#installing-new-dependencies)
    - [Github Instructions](#github-instructions)
    - [Folder Structure](#folder-structure)
  - [Design](#design)
  - [PLC Mappings](#plc-mappings)
    - [Power (10.10.10.1)](#power-1010101)
    - [Hospital (10.10.10.2)](#hospital-1010102)
    - [Police/Fire (10.10.10.3)](#policefire-1010103)
    - [Traffic (10.10.10.4)](#traffic-1010104)

## The Team

- Lead Developer 💻 `Benjamin` [@HoleInOneGolfer](https://www.github.com/HoleInOneGolfer)
- Game Developer 💻 `Rishi` [@rishih](https://www.github.com/Rishi-prog731)
- Lead Designer 🎨 `Roland`

## Instructions for Development

- Create a virtual environment in `src` using `python -m venv .venv`
- `cd` into `src`
- Activate the virtual environment using `.venv\Scripts\activate` or `.venv/bin/activate`
- Install the dependencies using `pip install -r requirements.txt`

### Installing New Dependencies

- Run `pip freeze > requirements.txt` to update the `requirements.txt` file

### Github Instructions

- Keep changes in a branch and merge into `main` when ready

### Folder Structure

- The `src` directory stores all the development files.
- The `doc` directory stores all the documentation files.

## Design

UX: [Figma.com](https://www.figma.com/file/mn40OqTiIRspf0wprOv92w/Cyber-City-Range?node-id=0%3A1&t=ArfQfiEURLy880xD-1)

Game: [Google Sheet](https://docs.google.com/spreadsheets/d/1fAyjl4c2pVBRPMtv6dN021eSeIyQtpjlF3AOrqUOK1o/edit)

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
