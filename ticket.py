passenger_name = "ahmed"
destination = "madrid"
num_of_tickets = 3
cost_of_1= 12

total_ticket_cost= num_of_tickets * cost_of_1



coach_price = 25.50
train_price= 14.00



if train_price < coach_price:
    print("the train is cheaper than the coach")
else:
    print("the coach is cheaper than the train")



train_price,coach_price=coach_price,train_price

print(train_price,coach_price)