# Ultimate Football Quiz 2022

A simple Python-based quiz application that demonstrates modular programming, input validation, console interaction, and basic data structures. This project showcases skills useful for Python development, including function decomposition, global variable management, and user interaction in the terminal.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies & Concepts Demonstrated](#technologies--concepts-demonstrated)
- [License](#license)

---

## Overview
The Ultimate Football Quiz 2022 allows multiple players to register and answer football-related questions. Scores are tracked, and the winners are displayed at the end. The project emphasizes clean code, modular design, and interactive console applications.

---

## Features
- Multiple player registration with input validation.
- Modular Python files separating concerns:
  - Console clearing
  - Sleep timing functions
  - Messaging
  - Player addition
  - Questioning and scoring
- Interactive terminal interface with feedback for correct/incorrect answers.
- Scoreboard and winner determination.


---

## Project Structure

ultimate-football-quiz/
├── quiz.py # Main entry point to run the quiz
├── clear_function.py # Clears the console across operating systems
├── sleep_function.py # Contains delay functions (1s and 2s)
├── message.py # Displays welcome and starting messages
├── player_addition.py # Handles player registration and input validation
└── questioning.py # Contains quiz questions, answers, scoring, and winner determination

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ultimate-football-quiz.git
   cd ultimate-football-quiz
Ensure you have Python 3.x installed.

Run the quiz:

python quiz.py
