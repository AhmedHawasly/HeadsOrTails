import random

def coin_toss():
    return "Heads" if random.choice([True, False]) else "Tails"

def main():
    name = input("Who are you?\n> ")
    print(f"Hello, {name}!")
    print("Tossing a coin...")
    heads_count = 0
    tails_count = 0
    for round_num in range(1, 4):
        result = coin_toss()
        print(f"Round {round_num}: {result}")
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    print(f"Heads: {heads_count}, Tails: {tails_count}")

if __name__ == "__main__":
    main()
