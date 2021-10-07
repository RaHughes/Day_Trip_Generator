import random

dests = ['Enid', 'Oklahoma City', 'Dubai', 'The North Pole', 'Chicago', 'New York City', 'The Lost City of Atlantis']
rests = ['McDonalds', 'Chilis', 'El Patio', 'Burger King', 'Longhorn Steakhouse', 'Applebeas', 'Buffalo Wild Wings']
transpos = ['Car', 'Boat', 'Plane', 'Shoe Lace Express', 'Imagination', 'Hitch Hike', 'Space Ship']
ents = ['Movie Theatre', 'Gun Range', 'Nerd Store', 'Book Store', 'Swimming Pool']

def get_trip(list1, list2, list3, list4):
    destination = list1[random.randrange(0, (len(list1)))]
    transportation = list2[random.randrange(0, (len(list2)))]
    restaurant = list3[random.randrange(0, (len(list3)))]
    entertainment = list4[random.randrange(0, (len(list4)))]
    print(f'Your Day Trip will be to {destination}, You will get there by {transportation}, You will eat at {restaurant}, and then you will go to a {entertainment}')
    trip = [destination, transportation, restaurant, entertainment]
    return trip

trip = get_trip(dests, transpos, rests, ents)

def is_satisfied(trip, list1, list2, list3, list4):   
    satisfied = input('Is there anything you would like to change? Yes or No: ').upper()
    if satisfied == 'YES':
        change_this = input('Would you like to change your Destination, Restaurant, Transportation, or Entertainment?: ').lower()
        if change_this == 'destination':
            change_this_thing(trip[0], trip, list1, change_this)
        elif change_this == 'transportation':
            change_this_thing(trip[1], trip, list2, change_this)
        elif change_this == 'restaurant':
            change_this_thing(trip[2], trip, list3, change_this)
        elif change_this == 'entertainment':
            change_this_thing(trip[3], trip, list4, change_this)
        else:
            print('Im sorry, it appears you didnt type that in correctly. Lets try that again!')
            loop_this()
        loop_this()                
    elif satisfied == 'NO':
        confirm_trip(trip)
        return


def change_this_thing(this, trip, list, thing):
    new_this = list[random.randrange(0, (len(list)))]
    while new_this == trip[trip.index(this)]:
        new_this = list[random.randrange(0, (len(list)))]
    trip[trip.index(this)] = new_this
    print(f'Your new {thing.capitalize()} is {new_this}!')


def loop_this():
    is_satisfied(trip, dests, transpos, rests, ents)


def confirm_trip(trip):
    confirm = input('Is your Day Trip Complete? Yes or No: ').upper()
    if confirm == 'YES':
        print('Congratulations! Your Day Trip has been confirmed!')
        print(f'Your Trip - Destination: {trip[0]}, Transportation: {trip[1]}, Restaurant: {trip[2]}, Entertainment: {trip[3]}')
    elif confirm == 'NO':
        print('Were so sorry to hear that. Plan your own Day Trip.')
    else:
        print('Im sorry, this is a Yes or No question. Lets try that again.')
        confirm_trip(trip)


is_satisfied(trip, dests, transpos, rests, ents)