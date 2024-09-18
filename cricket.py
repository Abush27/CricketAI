import random

running = True

batting = True

bowling = False

batscore = 0

tracklist = ['1', '2', '3', '4', '5', '6', '6', '5', '4']

counter = 0

score = 0

tracker = 0

var = 0

state = 'none'

complist = ['1', '2', '3', '4', '5', '6', '6', '5', '4']

bowlist = ['1', '2', '3', '4', '5', '6']

bignums = ['4', '5', '6']

smallnums = ['1', '2', '3']

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

def reset(name):
    name.clear()
    name.extend(['1', '2', '3', '4', '5', '6', '6', '5', '4'])

#---- MOST FREQUENT ITEM FINDER ---

print('You are batting')
print('')

while running:
    
    while batting:
        hit = input('What do u choose: ')
        print('')

        
            
        if state == "same":
            comphit = str(var)
        if state == "same3":
            comphit = str(var)
        elif state == "big":
            comphit = random.choice(bignums)

        elif state == "small":
            comphit = random.choice(smallnums)

        else:
            comphit = random.choice(complist)

        if hit == "quit":
            batting = False
            running = False

        elif hit == "restart":
            bowling = False
            complist.clear()
            complist.extend(['1', '2', '3', '4', '5', '6', '6', '5', '4'])
            score = 0
            tracker = 0
            counter = 0
            print('You are batting\n')
            batting = True
            
        elif comphit == hit:
        
            print(f'Out\n')
            print ('You scored ', str(score), ' runs')
            batscore = score
            complist.clear()
            complist.extend(['1', '2', '3', '4', '5', '6', '6', '5', '4'])
            score = 0
            tracker = 0
            counter = 0
            print('')
            print(f'You are bowling\n')
            bowling = True
            batting = False

        elif hit == "track":
            print(complist)

        elif hit in complist:
            complist.append(hit)
            score = score + int(hit)
            counter += 1
            tracker += 1
            if tracker == 6:
                tracker = 0
                reset(complist)
                
            if counter == 1:
                a = int(hit)
                if state == 'same3':
                    state = 'ed'
            elif counter == 2:
                b = int(hit)
            elif counter == 3:
                c = int(hit)
                if a == c:
                    state = 'same'
                    var = a

                elif state == 'small' or state == 'big':
                    state = 'yes'
            elif counter == 4:
                d = int(hit)
            elif counter == 5:
                e = int(hit)
                if state == 'same':
                    state = '3id'
            elif counter == 6:
                f = int(hit)
                counter = 0
                if a > 3 and b > 3 and c > 3 and d < 4 and e < 4:
                    state = 'big'
                elif a < 4 and b < 4 and c < 4 and d > 3 and e > 3:
                    state = 'small'

                elif a == d:
                    state = 'same3'
                    var = a
            

                
           

                    
        
                    
                
                
            
                
            print ('Runs: ', str(score))
            print('')

        else:
            print('Wrong value')


    while bowling:

        hit = input('What do u choose: ')

        print('')
        comphit = random.choice(bowlist)

        if hit == "quit":
            bowling = False
            break

        elif hit == "restart":
            bowling = False
            complist.clear()
            complist.extend(['1', '2', '3', '4', '5', '6', '6', '5', '4'])
            score = 0
            print('You are batting\n')
            batting = True
            
        elif comphit == hit:

            print('Out')
            print('')
            print ('The Computer scored', str(score), ' runs')
            print('')
            print('You scored ', str(batscore), ' runs')
            print('')
            if batscore == score:
                print(f"It was Tie, well played\n")
            elif batscore > score:
                print(f'Congratulations You Win !!\n')
            else:
                print(f'Computers Wins\n')
            complist.clear()
            complist.extend(['1', '2', '3', '4', '5', '6', '6', '5', '4'])
            score = 0
            print('')
            bowling = False
            print('You are batting\n')
            batting = True

        elif comphit in bowlist:
            score = score + int(comphit)
            print ('Computer runs: ', str(score))
            print('')

        else:
            print('Wrong value')

         
    
 
"""a b c d e f

if a < 4:

    value = value + 1

if a == b:
    ab = True"""



    
        

    
    
