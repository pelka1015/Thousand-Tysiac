# 🃏 Thousand (Tysiąc) – Python Card Game

Thousand (Tysiąc) is a Python-based version of the classic Polish card game.
Designed for 2 or 3 players, it’s a game that blends elements of strategy, bidding, and precise point management.

This project was created as a learning exercise to understand the basics of object-oriented programming (OOP) in Python, while also exploring how game logic and user interaction can be structured in an object-oriented way.
## 💡 Features

- Fully text-based console interface.
  
- Support for 2-player and 3-player modes.
  
- Randomized deck and shuffling.
  
- Basic meld and scoring system.
  
- Object-oriented design using Python classes and inheritance.

  
## 🧩 Game Flow

- Dealing – Each player receives their hand of cards.

- Bidding – Players take turns increasing the bid.

- Talon (Musik) – The bidding winner takes extra cards and discards as needed.

- Declaration – Players announce the number of points they aim to reach.

- Play – Players play rounds, compare cards, and collect points.

- Results – Scores are compared and the winner is announced.


## 🧱 Code Structure

- Card – represents an individual playing card.

- PileOfCards – manages collections of cards (hands, talon).

- Player – extends PileOfCards with player-specific data such as points, bids, and declarations.

- Game Functions – handle dealing, bidding, meld detection, and scoring logic.

- Main Menu – provides a simple navigation interface for choosing game modes.



## 🚧 Notes & Limitations

- The game is fully interactive via console input() — there is no AI opponent.

- Input validation is basic; invalid entries may cause unexpected behavior.

- The implementation follows simplified Thousand rules for learning purposes.

- Designed primarily as an educational project, not a polished commercial game.

## ✒️ Authors

- Patryk Pełka
  
- Filip Gertner
