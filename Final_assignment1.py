##assignment1
i = int(input())
if (i >= 2000) and (i <= 3200) and (i % 7 == 0) and (i % 5 != 0):
    print ("The number " + str(i) + " meets the requirement",end = ' ')
else:
    print("The number " + str(i) + " does not meet the requirement")


