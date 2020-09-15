# Dictionary full of info
my_info = {"name": "Jeremy Greenwald",
           "age": 42,
           "hobbies": ["reading", "TV", "YouTube", "complaining"],
           "wake-up": {"Mon": 8, "Friday": 9, "Saturday": 7, "Sunday": 9}}

# Print out results are stored in the dictionary
print(f'Hello I am {my_info["name"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On the weekend I get up at {my_info["wake-up"]["Saturday"]}')
