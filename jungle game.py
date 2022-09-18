import random

print('hello welcome to animal war ')

while True:
   
    print('choose your animal from down list and enter the name of your animal')
    print('list of animal -> [line ,cheetah ,tiger ,wolf ,haskidag ,bear]')
    print('you can exit with type exit or khooruj')

    # creat a class to name Animal
    class Animal():
        def __init__(self,name,power,color):
            self.live = 'Jungle'
            self.power = power
            self.name = name
            self.color = color

    # creat 2 classes to names Cats and Dags and these classes inheritance from Animal

    class Cats(Animal):
        group = 'cats'

        def __init__(self, name, power,color):
            super().__init__(name, power,color)

    class Dags(Animal):
        group = 'dags'

        def __init__(self, name, power,color):
            super().__init__(name, power,color)

    # creat some objects from Cats and Dags
    
    line = Cats('line',10,'yellow')
    cheetah = Cats('cheetah',6,'yellow and black circle')
    tiger = Cats('tiger',9,'yellow and black line')
    wolf = Dags('wolf',8,'dark brown')
    haskidog = Dags('haski dog',5,'gray')
    bear = Dags('bear',9.5,'brown')

    # creat a list of objects
    choices = [line,cheetah,tiger,wolf,haskidog,bear]

    # choice random from list(choices) for computer
    computer = random.choice(choices)

    # get value from user
    user_input = input('choose from list and then enter:')
    
    # make a way for exit from ring with break
    if user_input == 'exit' or user_input == 'khooruj':
        break    

    # creat 1 dictiouneries from objects Property and make a loop by while for when value of user not in choices
    

    responses_for_originality ={'line' : line, 
                'cheetah' : cheetah,
                'tiger' : tiger,
                'wolf' : wolf,
                'haskidag' : haskidog,
                'bear':bear
                }
    while True:
        if user_input not in responses_for_originality:
            print('sorry i think you enter the name of your animal wrong please enter again name of your animal')
            print('list of animal -> [line ,cheetah ,tiger ,wolf ,haskidag ,bear]')
            user_input = input('choose from list and then enter:')
        else:
            break

#for when value of user in choices    
    for user_inout in responses_for_originality.keys():
        user_originality = responses_for_originality[user_input]

#creat Variables for acces to properties

    user_color = user_originality.color
    
    user_power = user_originality.power

    user_name = user_originality.name

    computer_group = computer.group

    user_group = user_originality.group

#  creat a function for Verdict between user and computer
    def juge():
       
        print('computer group :',computer_group,'vs user group :',user_group)

        print('computer:',computer.color,computer.name,'vs you:',user_color,user_input)

# creat if for when value of computer and value of user the same
        if computer.power==user_power:
            print('both of you choice one animal ')
        
        else:
            if computer.power>user_power:
                print('computer is win')
            else :
                print('yess!!!! you are win')

    juge()

