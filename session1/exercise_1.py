def minion_game(string):
    vowels = 'AEIOU'
    an_score = 0
    minh_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            minh_score += len(string) - i
        else:
            an_score += len(string) - i
    if an_score > minh_score:
        print('An', an_score)
    elif minh_score > an_score:
        print('Minh', minh_score)
    else:
        print('Draw')

string = input("Enter upper string: ")
minion_game(string)
