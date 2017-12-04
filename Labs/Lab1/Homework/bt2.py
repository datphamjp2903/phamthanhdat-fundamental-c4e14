from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.get_default_database()

posts = db['posts']
new_post = {
    "title": "プログラミング",
    "author": "達人",
    "content": "僕は長年で日本語・日本文化を勉強していたが、新しい分野を勉強してみたいので、科学情報を選んだ。そのため、このコースに参加してみたわけである。将来、IT技術者になるかまだ決めていないが、一応頑張っている！"
}

posts.insert_one(new_post)
