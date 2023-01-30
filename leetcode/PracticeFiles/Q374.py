n = 10
def guess(number):
    correct = 6
    if number > correct:
        return -1
    elif number < correct:
        return 1
    else:
        return 0



start = 1
end = n
pick = (end-start)//2 + start



while(True):
    if (guess(pick)== 1):
        start = pick +1
        pick = (end-start)//2 + start
    
    elif (guess(pick)== -1):
        end = pick -1
        pick = (end-start)//2 + start
    else:
        break

print(pick)


