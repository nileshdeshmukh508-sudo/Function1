from functools import reduce

#Here we take the list of student name and there marks inside the tuple
marks=[("Nilesh",81),("Rohit",33),("Samay",24),("Ram",55),("Sneha",88),("Omkar",87),("Anuj",80)] 


#filter funtion used for filteration where above 40 marks are filtered 
passed=list(filter(lambda x: x[1]>=40,marks))

#map used for operation on the individual element
updated=list(map(lambda x:(x[0],x[1]+5),passed))

#reduce used for  ultimately "reducing" that sequence into a single cumulative value
total=reduce(lambda a,b:a+b,updated)

print(marks)
print(updated)
print(passed)
print(total)
