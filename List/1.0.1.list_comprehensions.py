friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)
print(friends is starts_s)
print("Friends: ", id(friends), "starts_s:", id(starts_s)) # Friends:  4503996736 starts_s: 4503998528
