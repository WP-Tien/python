student_scores = [12, 13, 55, 88, 334, 123, 32, 67, 32, 11, 49, 299]

# total_exam_score = sum(student_scores)
# print( total_exam_score 

# sum = 0
# for score in student_scores:
#     sum += score 
# print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)