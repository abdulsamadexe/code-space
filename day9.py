# student_scores={
#     "harry":91,
#     "ben":76,
#     "ahmed":80,
#     "neville":64,
#     "draco":75,
# }
# final_student_score={}
# for key in student_scores:
#     score=student_scores[key] 
#     if score>90 and score<=100:
#         score="A"
#         final_student_score[key]=score
#     elif score>80 and score<=90:
#         score="B"
#         final_student_score[key]=score
#     elif score>70 and score<=80:
#         score="C"
#         final_student_score[key]=score
#     elif score>60 and score<=70:
#         score="D"
#         final_student_score[key]=score
# print(final_student_score)

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]
# def add_new_country(country,total_visits,cities_visited):
#     new_dictionary={
#         "country":country,
#         "total visits":total_visits,
#         "cities_visited":cities_visited
#         }
#     travel_log.append(new_dictionary)
# add_new_country("Russia",2,["Moscow","saint pearl"])
# print(travel_log)

print( '''
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
''')
bid_list={}
name=input("what is your name?")
bids=int(input("what is your bid? $"))
def bid(name,bid):
    bid_list[name]=bid
bid(name,bids)
chk=input("Are ther any other biiders?type YES or NO")
chk.lower
while chk!="yes" and chk!="no":
    print("invalid input")
    chk=input("Are ther any other biiders?type YES or NO")
if chk=="yes":
    while chk=="yes":
        name=input("what is your name?")
        bids=int(input("what is your bid? $"))
        bid(name,bids)
        chk=input("Are ther any other biders?type YES or NO")
        chk.lower
def highest_record(bidding_record):
    highest_bid=0
    highest_bidder="0"
    for name in bid_list:
        bid=bid_list[name]
        if bid>highest_bid:
            highest_bid=bid
            highest_bidder=name
    print(f"{highest_bidder} won the silent bid with a bid of ${highest_bid}")

highest_record(bid_list)


    

