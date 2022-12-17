# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
b_m_i: float = weight / (height ** 2)
print(round(b_m_i))
# if we want to round to two decimal place
print(round(b_m_i, 2))
# if we just want the integer and cut off all the decimal place while dividing we can diretcly use flow divion
div_ison = weight // height
print(div_ison)
# if we want to do a cumilitative divison or additon we can use short hand
result = 4 / 2
result /= 2
print(result)
score = 78
score += 2
print(score)
# f string
print("your score is " + str(score))
isWinning = True
print(F'your score is {score}, your  height is {height}, you are winning is {isWinning})')