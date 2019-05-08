animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
number_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']

keep_going = True

while keep_going:
    place = raw_input('Which place do you want to check?')
    
    if place.isdigit():
        print animals[int(place)]
        again = raw_input("Keep going?")
        if again != 'yes':
            keep_going = False
        
    else:
        print animals[number_list.index(place)]
        again = raw_input("Keep going?")
        if again != 'yes':
            keep_going = False
        