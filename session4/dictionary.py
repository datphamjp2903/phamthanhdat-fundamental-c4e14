#tuananh = ["Tuan Anh", 22, "Moc Chau", 2, True, 4, 20]

# tuananh = {
#
# }
#dictionary

# tuananh = {
#     "name": "Tuan Anh"
# }
#"key"(str):"value"

tuananh = {
    "name": "Tuan Anh",
    "age": 22,
    "home": "Moc Chau",
    "in_relationship": True
}
print(tuananh["name"])
#update
tuananh["age"] = 23
tuananh["age"] += 1

tuananh["projects"] = 4#create
print(tuananh)

del tuananh["in_relationship"]#delete
print(tuananh)
