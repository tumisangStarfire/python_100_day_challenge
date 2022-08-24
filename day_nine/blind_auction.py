from art import logo
print(logo)
bids = []

def add_new_bid(name= "", bid = 0):
    bid = { "name" : name, "bid" : bid}
    bids.append(bid)
    return bids

def calculate_highest_bid(bids = {}): 
    max_bid = 0
    winner = ""
    print(bids)
    for key in bids:  
        bid_amount = key["bid"]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = key["name"]
    message = f"The winner is { winner } with a bid of {max_bid }"
    return message
            
        
next_bid = True 

while next_bid:
    name = input("What is your name..?\n")
    bid = int(input("What is your bid..? $\n"))
    total_bids = add_new_bid(name,bid) 
    promt_user = input("Are they are any other bidders..? Type 'yes' or 'no' \n").lower()

    if promt_user == "yes":
        print("\033c")
    if promt_user == "no":
        next_bid = False
        result = calculate_highest_bid(total_bids)
        print(result)