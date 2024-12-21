#lambda function to reverse the number
reverse = lambda s : s[::-1]
print(reverse ("Disha"))

#lambda with tupple sorting
students = [("Disha" , 20), ("Priya" , 22) , ("Riya" , 25)]

sorted_student = sorted(students , key=lambda x : x[1])
print(sorted_student)