
#### main.py

```python
#!/usr/bin/env python3
import random

kingdoms = [
    "The Ivory Bastion – A kingdom built on wisdom, lost when its scholars were taken by the void.",
    "The Crimson Crown – A warrior nation, betrayed from within and erased from history.",
    "The Sapphire Court – A city of magic, shattered when its own spells turned against it.",
    "The Ashen Empire – A land of fire and steel, burned to the ground by an unknown force.",
    "The Moonlit Dominion – A kingdom blessed by the stars, lost when the heavens went dark."
]

def get_random_kingdom():
    return random.choice(kingdoms)

def main():
    print("Welcome to Shattered Thrones!")
    print("Here is a randomly generated lost kingdom and its fate:")
    print(get_random_kingdom())

if __name__ == "__main__":
    main()
