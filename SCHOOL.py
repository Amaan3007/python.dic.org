sample={
    "name" : "Amaan",
    "Age" : 11,
    "City" : "London"
}

print(sample["name"])
print(sample["Age"])
print(sample["City"])

sample_list=["Amaan", 11, "London"]

print(sample_list[0])
print(sample.keys())

if "age"in sample:
    print ("Yes")
else:
    print ("NO")