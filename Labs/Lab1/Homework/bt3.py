from pymongo import MongoClient
from matplotlib import pyplot

client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.get_default_database()

customers = db['customers']#get collection

customers_list = customers.find()#Get ALL, become list type

group_events = 0
group_ads = 0
group_wom = 0
for customer in customers_list:#dictionary
    for ref in customer.values():
        if ref == "events":
            group_events += 1
        if ref == "ads":
            group_ads += 1
        if ref == "wom":
            group_wom += 1
print(group_events, "customers are acquired from events.")
print(group_ads, "customers are acquired from advertisements.")
print(group_wom, "customers are acquired from word of mouth.")

labels = ['Events', 'Advertisements', ' Word of mouth']
colors = ['red', 'blue', 'yellow']
data = [group_events, group_ads, group_wom]

pyplot.pie(data, labels = labels, colors = colors, shadow = True, startangle = 90, autopct='%1.1f%%')#autopct = show percents
pyplot.axis('equal')
pyplot.show()
