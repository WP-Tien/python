# Phân tách strings
s = "This is a text string"

words = s.split(" ")
print(words) # ['This', 'is', 'a', 'text', 'string']
s = " ".join(words)

print(s) # This is a text string

# Format thông thường
name = 'Jack'
city = 'New York'
print("{} is from {}".format(name, city)) # Jack is from New York

# Format khi một biến được dùng lại nhiều lần
number = 5
print("{0} times {0} is equal to {1}". format(number, number ** 2)) # 5 times 5 is equal to 25

# Padding and alignment
# > Aligned to the right
# < Aligned to the left
# ^ Centered

male = 20
female = 30
total = male + female
percent_male = round(male * 100 / total, 2)

print("Number of male students: {:>10}".format(male))
print("Number of female students: {:>10}".format(female))
print("Percentage of male students: {:>10}%".format(percent_male))

# Truncate long strings
name = "Barrack Very Long Obama"
print("{:.5}".format(name))

# Format số nguyên
month_1 = 5
month_2 = 12

print("Month 1: {:02d}".format(month_1)) # Month 1: 05
print("Month 2: {:02d}".format(month_2)) # Month 2: 12

# Format số thực
print("{:.2f}".format(10 / 3)) # 3.33