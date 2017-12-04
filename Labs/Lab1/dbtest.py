from pymongo import MongoClient

#1. Connect to database
client = MongoClient("mongodb://admin:admin@ds129156.mlab.com:29156/c4e14-dat")

#2. Get default database
db = client.get_default_database()

#3. Get collection
blog = db['blog']

#4. Insert document
# new_post = {
#     'title': "Hom nay troi mua",
#     'content': "Coding"
# }
#
# blog.insert_one(new_post)

posts = blog.find()#GET ALL posts in blog
#print(posts[0])
for post in posts:
    print(post)
