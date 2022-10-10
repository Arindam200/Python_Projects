logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print('*******************Welcome To Online Auction***********************')

bids={}

bidding_finished=False

def find_highest_bidder(bidding_record):

    highest_bid = 0

    for bidder in bidding_record:

        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid :

            highest_bid = bid_amount

            winner = bidder
            
    print(f'The Winner Is "{winner}" With A Bid Amount Of "{highest_bid}"')
            
while not bidding_finished:

    name=input('What is your name ?: ')

    price=int(input('What is your Bid ? ₹: '))

    bids[name] = price

    should_continue =input('Are there any other bidders ? Type YES/NO ').lower()

    if should_continue == 'no':
        
        bidding_finished = True

        find_highest_bidder(bids)

    elif should_continue == 'yes':

        pass
