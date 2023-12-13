hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price #the loop iterates through prices list, calculates the sum of all prices and stores it in total_revenue

average_price = total_price/len(prices) #the average, have to use the len() on prices give the numeber of prices offered which is 7

print("Average Haircut Price: ", average_price)

new_prices = [cut - 5 for cut in prices] # creates a new list by subtracting 5 from ech price in prices list using list comprehension
print(new_prices)

total_revenue = 0 #init variable
for i in range(0, len(hairstyles)): # calculates total revenue by iterating through the haorstyles list and multiplying the price of each hairstyle (prices[i]) by the number sold last week (last_week[i]). then stores in total_revenue
  total_revenue += prices[i] * last_week[i]

print('Total Revenue: ', total_revenue )

average_daily_revenue = total_revenue / 7 #average each day
print('Average daily rev: ', average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
#range(len(new_prices)): generates a range of indices that correspond to the length of new_prices, can also told as 0 to len(new_prices) - 1
#for i in range(len(new_prices)): iterates over each index i in the range of valid indices for new_prices; allows you to acces both index and value at the index of new_prices
#hairstyles[i]: retrieves hairstyle name from hairstyles list at the same index i. Since i represents the current index being processed in the loop, hairstyles[i] gives you the name of the haorstyle that corresponds to that index
#[hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]: for each index i in the valid range, it checks the price new_price[i] of the corresponding hairstyle less than 30. If the condition is met, it includes the name of that haorstyle hairstyle[i] in the cuts_under_30