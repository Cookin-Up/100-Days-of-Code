# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

bids = {}
auction_running = True
winning_bid = 0
winning_name = ""

while auction_running:

    name_value = input("What is your name? \n")
    bid_value = int(input("What is your bid? in $\n"))
    bids[name_value] = bid_value
    over = input("Has everyone bid? (Y/N) \n").lower()
    if over == "n":
        print("\n" * 20)
    if over == "y":
        auction_running = False
        for key in bids:
            if bids[key] > winning_bid:
                winning_bid = bids[key]
                winning_name = key
        print(f"Bid winner is {winning_name} who bid {winning_bid}")