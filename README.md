# Character Weapon Strategy System

This Python project demonstrates the Strategy design pattern through a character-based weapon system. Different character types can use interchangeable weapons, allowing dynamic changes to their behavior. Each weapon encapsulates unique attack behavior, which can be swapped as needed, providing flexibility and modularity.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Overview](#project-overview)
4. [Key Features](#key-features)
5. [Purpose and Lessons Learned](#purpose-and-lessons-learned)

## Installation

To set up and run this project locally:

1. **Clone the Repository:**  
```bash
git clone https://github.com/alex-nin/strategy-design-pattern.git
cd strategy-design-pattern
```

2. **Install Dependencies:** Ensure you have Python 3.x installed.

## Usage

To run the program, execute the following command in your terminal in the program directory, depending on your environment:

```bash
python strategy.py
```
or
```bash
python3 strategy.py
```

## Project Overview

The main components include:
- **WeaponBehavior Interface**: Defines a `use_weapon` method for different weapon behaviors.
- **Concrete Weapons**: Specific weapon behaviors, including `KnifeBehavior`, `AxeBehavior`, `BowAndArrowBehavior`, and `SwordBehavior`, each implementing unique attack actions.
- **Character Base Class**: An abstract class representing characters with a default weapon and the ability to change weapons dynamically. It includes a `fight` method that delegates attack behavior to the current weapon.
- **Character Types**: Concrete character classes like `King`, `Queen`, `Knight`, and `Troll`, each initialized with a specific weapon but capable of changing weapons dynamically.

## Key Features

1. **Interchangeable Behaviors**: Different weapon behaviors can be assigned to characters, allowing flexible changes to attack methods without altering character classes.
2. **Dynamic Behavior Changes**: Characters can switch weapons at runtime, enabling varied attack strategies within a single execution.
3. **Encapsulation of Algorithms**: Each weapon encapsulates its specific behavior, promoting modularity and separation of concerns.
4. **Extended Flexibility**: New weapons or character types can be added without modifying existing code, enhancing scalability.

## Purpose and Lessons Learned

This project helped me understand the Strategy design pattern by implementing it in a character-weapon context. By separating weapon behaviors from character classes, I saw how the Strategy pattern improves flexibility, allowing characters to switch attack methods without modifying their underlying code. This modular approach reinforced how the Strategy pattern can adapt behaviors dynamically, emphasizing its value in creating adaptable, maintainable, and reusable code structures.
