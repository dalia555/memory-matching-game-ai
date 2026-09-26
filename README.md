# Memory Matching Game with AI

A memory matching game that combines a traditional card-matching gameplay experience with an AI opponent.

The project demonstrates game logic, state management, graphical user interface development, and AI decision-making.

## Project Overview

The game consists of a set of hidden cards arranged on a board. Players reveal cards and attempt to find matching pairs.

An AI opponent also participates in the game and uses previously revealed card information to make decisions.

## Features

- 🃏 Card matching gameplay
- 🤖 AI opponent
- 🧠 AI memory of previously revealed cards
- 🎮 Interactive gameplay
- 🖥️ Graphical user interface
- 🔄 Game state management
- 🏆 Score tracking
- 🎯 Matching-pair detection

## AI Component

The AI opponent keeps track of information it has observed during the game.

When cards are revealed, the AI can use this information when making future selections.

The general process is:

```text
Cards are revealed
       ↓
AI observes card information
       ↓
Information is stored
       ↓
AI checks known card pairs
       ↓
AI selects a card
       ↓
Game continues
