from sys import exit
from csv import DictReader, DictWriter
from termcolor import cprint


login_password = "1234"
hotel_room_limit = 10
empty_rooms = []
hotel_guests = []


def main():
    try:
        print("\nWelcome !\n")
        for login_tries in range(3):
            if login(input("Please enter the password : ").strip(),login_password):
                break
            elif login_tries == 2:
                cprint("\nToo many incorrect tries, access denied\n","red")
                exit()
            else:
                cprint(f"\nincorrect password, you have {3-(login_tries+1)} tries left !\n","red")
        cprint("\naccess granted !","green")
        while True:
            handle_empty_rooms()
            handle_hotel_guests()
            choice()
    except KeyboardInterrupt:
        print()
        cprint("\nThe program force quit\n","red")
        exit()


def choice():
    if len(empty_rooms) == 0:
        try:
            for function_tries in range(3):
                print("\nPlease choose a function:\n  check guest access: press number 2\n  search for guest: press number 3\n  remove guest: press number 4\n  logout: press number 5\n")
                choice = input("Function number: ")
                try:
                    choice = int(choice.strip())
                except ValueError:
                    if function_tries == 2:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    cprint(f"\nincorrect function number : {choice}, you have {3-(function_tries+1)} tries left, please choose one of these : | 2 || 3 || 4 || 5 |","red" )
                else:
                    if choice in [2,3,4,5]:
                        break
                    elif function_tries == 2:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    if choice not in [2,3,4,5]:
                        cprint(f"\nincorrect function number : {choice}, you have {3-(function_tries+1)} tries left, please choose one of these : | 2 || 3 || 4 || 5 |","red" )
            match choice:
                case 2:
                    for check_access_tries in range(3):
                        name = input("\nWhose access would you like to check : ")
                        service = input("Wich service : ")
                        if check_guest_access("hotel_guests_list.csv",name,service)[0] == "error":
                            cprint(f"{check_guest_access('hotel_guests_list.csv',name,service)[1]}, you have {3-(check_access_tries+1)} tries left","red")
                        else:
                            if check_guest_access("hotel_guests_list.csv",name,service)[0] == "denied":
                                cprint(check_guest_access('hotel_guests_list.csv',name,service)[1],"red")
                                break
                            else:
                                cprint(check_guest_access('hotel_guests_list.csv',name,service)[1],"green")
                                break

                case 3:
                    for search_client_tries in range(3):
                        guest = input("\nWhose information would you like ? ")
                        if search_for_client("hotel_guests_list.csv",guest)[0] == "error":
                            cprint(f"{search_for_client('hotel_guests_list.csv',guest)[1]}, you have {3-(search_client_tries+1)} tries left","red")
                        else:
                            print(search_for_client("hotel_guests_list.csv",guest)[1])
                            break
                case 4:
                    for remove_tries in range(3):
                        hotel_guests_name = []
                        for h_g in hotel_guests:
                            hotel_guests_name.append(h_g["name"])
                        guest_name = input("\nThe guest name who you want to remove : ").strip().lower().title()
                        if guest_name in hotel_guests_name:
                            for guest in hotel_guests:
                                if guest["name"] == guest_name:
                                    manage_room("add",int(guest["room"]))
                                    break
                            remove_guest(guest_name)
                            cprint(f"\nGuest {guest_name} is succesfully removed","green")
                            break
                        else:
                            cprint(f"\nInvalid guest name : {guest_name}, {guest_name} is not a hotel guest, you have {3-(remove_tries+1)} tries left","red")

                case 5:
                    for logout_tries in range(3):
                        logout_choice = input("\nDo you want to logout: 'yes'/'no' ").strip().lower()
                        if logout_choice == "yes":
                            logout()
                        elif logout_choice == "no":
                            break
                        else:
                            cprint(f"\nInvalid response {logout_choice}, please respond with 'yes' or 'no', you have {3-(logout_tries+1)} tries left","red")

        except KeyboardInterrupt:
            print()
            for exit_tries in range(3):
                exit_choice = input("\nDo you want to force quit (not recommened) ? yes/no : ").strip().lower()
                if exit_choice == "yes":
                    cprint("\nThe program force quit\n","red")
                    exit()
                elif exit_choice == "no":
                    break
                else:
                    cprint(f"\nInvalid response : {exit_choice}, please respond with 'yes' or 'no', you have {3-(exit_tries+1)} tries left","red")


    elif len(hotel_guests) == 0:
        try:
            for function_tries in range(3):
                print("\nPlease choose a function:\n  add guest: press number 1\n  logout: press number 5\n")
                choice = input("Function number: ")
                try:
                    choice = int(choice.strip())
                except ValueError:
                    if function_tries == 2:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    cprint(f"\nincorrect function number : {choice}, you have {3-(function_tries+1)} tries left, please choose one of these : | 1 || 5 |","red" )
                else:
                    if choice in [1,5]:
                        break
                    elif function_tries == 2:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    if choice not in [1,5]:
                        cprint(f"\nincorrect function number : {choice}, you have {3-(function_tries+1)} tries left, please choose one of these : | 1 || 5 |","red" )
            match choice:
                case 1:
                    last_correct_data = None
                    print("\nHere are the empty rooms : ",end="")
                    for e_r in empty_rooms:
                        print(f"| {e_r} |",end="")
                    print()
                    for room_tries in range(3):
                        room = input("\nWhich one would you like ? ")
                        if check_room("empty_rooms_list.txt",room) == "correct":
                            last_correct_data = "room"
                            break
                        else:
                            cprint(f"\nIncorrect room number : {room}, you have {3-(room_tries+1)} tries left, please choose one of these rooms : ","red",end="")
                            for e_r in empty_rooms:
                                print(f"| {e_r} |",end="")
                            print()
                    if last_correct_data == "room":
                        for name_tries in range(3):
                            name = input("\nAt which name would you like to get the room ? ")
                            if check_name("hotel_guests_list.csv",name) == "correct":
                                last_correct_data = "name"
                                break
                            else:
                                cprint(f"\nInvalid name : {name}, you have {3-(name_tries+1)} tries left","red")
                    if last_correct_data == "name":
                        for package_tries in range(3):
                            package = input("\nWhich package would you like ? ")
                            if check_package(package) == "correct":
                                last_correct_data = "package"
                                break
                            else:
                                cprint(f"\nIncorrect package : {package}, you have {3-(package_tries+1)} tries left, please choose one of these packages : 'normal', 'premium', 'luxury'","red")
                    if last_correct_data == "package":
                        for night_tries in range(3):
                            night = input("\nHow many nights would you like to stay ? ")
                            if check_night(night) == "correct":
                                last_correct_data = "night"
                                break
                            else:
                                cprint(f"\nIncorrect number of nights : {night}, you have {3-(night_tries+1)} tries left, please choose a number greater than 0","red")
                    if last_correct_data == "night":
                        for adult_tries in range(3):
                            adult = input("\nHow many adult would like to stay ? ")
                            if check_adult(adult) == "correct":
                                last_correct_data = "adult"
                                break
                            else:
                                cprint(f"\nIncorrect number of adults: {adult}, you have {3-(adult_tries+1)} tries left, please choose a number greater than 0","red")
                    if last_correct_data == "adult":
                        for kid_tries in range(3):
                            kid = input("\nHow many kids would like to stay ? ")
                            if check_kid(kid) == "correct":
                                last_correct_data = "kid"
                                break
                            else:
                                cprint(f"\nIncorrect number of kids : {kid}, you have {3-(kid_tries+1)} tries left, please choose a number greater or equal to 0","red")
                    if last_correct_data == "kid":
                        guest_data = make_guest_data(name,adult,kid,package,night,room)
                        cprint(f"\nThats will be ${get_price(adult,kid,package,night):,}\n","yellow",end="")
                        for pay_tries in range(3):
                            response = input("\nDid the guest paid ? yes/no ").strip().lower()
                            if response == "yes":
                                manage_room("remove",guest_data["room"])
                                add_guest(guest_data)
                                cprint(f"\nGuest {guest_data['name']} is succesfully added","green")
                                break
                            elif response == "no":
                                cprint(f"\nSorry but without paying the hotel can't provide any service","red")
                                break
                            else:
                                cprint(f"\nInvalid input : {response}, you have {3-(pay_tries+1)} tries left, please respond with yes or no","red")

                case 5:
                    for logout_tries in range(3):
                        logout_choice = input("\nDo you want to logout: 'yes'/'no' ").strip().lower()
                        if logout_choice == "yes":
                            logout()
                        elif logout_choice == "no":
                            break
                        else:
                            cprint(f"\nInvalid response {logout_choice}, please respond with 'yes' or 'no', you have {3-(logout_tries+1)} tries left","red")

        except KeyboardInterrupt:
            print()
            for exit_tries in range(3):
                exit_choice = input("\nDo you want to force quit (not recommened) ? yes/no : ").strip().lower()
                if exit_choice == "yes":
                    cprint("\nThe program force quit\n","red")
                    exit()
                elif exit_choice == "no":
                    break
                else:
                    cprint(f"\nInvalid response : {exit_choice}, please respond with 'yes' or 'no', you have {3-(exit_tries+1)} tries left","red")


    else:
        try:
            for function_tries in range(3):
                print("\nPlease choose a function:\n  add guest: press number 1\n  check guest access: press number 2\n  search for guest: press number 3\n  remove guest: press number 4\n  logout: press number 5\n")
                choice = input("Function number: ")
                try:
                    choice = int(choice.strip())
                except ValueError:
                    if function_tries == 2:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    cprint(f"\nincorrect function number : {choice}, you have {3-(function_tries+1)} tries left, please choose one of these : | 1 || 2 || 3 || 4 || 5 |","red" )
                else:
                    if choice in [1,2,3,4,5]:
                        break
                    elif function_tries == 2:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    if choice not in [1,2,3,4,5]:
                        cprint(f"\nincorrect function number : {choice}, you have {3-(function_tries+1)} tries left, please choose one of these : | 1 || 2 || 3 || 4 || 5 |","red" )
            match choice:
                case 1:
                    last_correct_data = None
                    print("\nHere are the empty rooms : ",end="")
                    for e_r in empty_rooms:
                        print(f"| {e_r} |",end="")
                    print()
                    for room_tries in range(3):
                        room = input("\nWhich one would you like ? ")
                        if check_room("empty_rooms_list.txt",room) == "correct":
                            last_correct_data = "room"
                            break
                        else:
                            cprint(f"\nIncorrect room number : {room}, you have {3-(room_tries+1)} tries left, please choose one of these rooms : ","red",end="")
                            for e_r in empty_rooms:
                                print(f"| {e_r} |",end="")
                            print()
                    if last_correct_data == "room":
                        for name_tries in range(3):
                            name = input("\nAt which name would you like to get the room ? ")
                            if check_name("hotel_guests_list.csv",name) == "correct":
                                last_correct_data = "name"
                                break
                            else:
                                cprint(f"\nInvalid name : {name}, you have {3-(name_tries+1)} tries left","red")
                    if last_correct_data == "name":
                        for package_tries in range(3):
                            package = input("\nWhich package would you like ? ")
                            if check_package(package) == "correct":
                                last_correct_data = "package"
                                break
                            else:
                                cprint(f"\nIncorrect package : {package}, you have {3-(package_tries+1)} tries left, please choose one of these packages : 'normal', 'premium', 'luxury'","red")
                    if last_correct_data == "package":
                        for night_tries in range(3):
                            night = input("\nHow many nights would you like to stay ? ")
                            if check_night(night) == "correct":
                                last_correct_data = "night"
                                break
                            else:
                                cprint(f"\nIncorrect number of nights : {night}, you have {3-(night_tries+1)} tries left, please choose a number greater than 0","red")
                    if last_correct_data == "night":
                        for adult_tries in range(3):
                            adult = input("\nHow many adult would like to stay ? ")
                            if check_adult(adult) == "correct":
                                last_correct_data = "adult"
                                break
                            else:
                                cprint(f"\nIncorrect number of adults: {adult}, you have {3-(adult_tries+1)} tries left, please choose a number greater than 0","red")
                    if last_correct_data == "adult":
                        for kid_tries in range(3):
                            kid = input("\nHow many kids would like to stay ? ")
                            if check_kid(kid) == "correct":
                                last_correct_data = "kid"
                                break
                            else:
                                cprint(f"\nIncorrect number of kids : {kid}, you have {3-(kid_tries+1)} tries left, please choose a number greater or equal to 0","red")
                    if last_correct_data == "kid":
                        guest_data = make_guest_data(name,adult,kid,package,night,room)
                        cprint(f"\nThats will be ${get_price(adult,kid,package,night):,}\n","yellow",end="")
                        for pay_tries in range(3):
                            response = input("\nDid the guest paid ? yes/no ").strip().lower()
                            if response == "yes":
                                manage_room("remove",guest_data["room"])
                                add_guest(guest_data)
                                cprint(f"\nGuest {guest_data['name']} is succesfully added","green")
                                break
                            elif response == "no":
                                cprint(f"\nSorry but without paying the hotel can't provide any service","red")
                                break
                            else:
                                cprint(f"\nInvalid input : {response}, you have {3-(pay_tries+1)} tries left, please respond with yes or no","red")

                case 2:
                    for check_access_tries in range(3):
                        name = input("\nWhose access would you like to check : ")
                        service = input("Wich service : ")
                        if check_guest_access("hotel_guests_list.csv",name,service)[0] == "error":
                            cprint(f"{check_guest_access('hotel_guests_list.csv',name,service)[1]}, you have {3-(check_access_tries+1)} tries left","red")
                        else:
                            if check_guest_access("hotel_guests_list.csv",name,service)[0] == "denied":
                                cprint(check_guest_access('hotel_guests_list.csv',name,service)[1],"red")
                                break
                            else:
                                cprint(check_guest_access('hotel_guests_list.csv',name,service)[1],"green")
                                break

                case 3:
                    for search_client_tries in range(3):
                        guest = input("\nWhose information would you like ? ")
                        if search_for_client("hotel_guests_list.csv",guest)[0] == "error":
                            cprint(f"{search_for_client('hotel_guests_list.csv',guest)[1]}, you have {3-(search_client_tries+1)} tries left","red")
                        else:
                            print(search_for_client("hotel_guests_list.csv",guest)[1])
                            break

                case 4:
                    for remove_tries in range(3):
                        hotel_guests_name = []
                        for h_g in hotel_guests:
                            hotel_guests_name.append(h_g["name"])
                        guest_name = input("\nThe guest name who you want to remove : ").strip().lower().title()
                        if guest_name in hotel_guests_name:
                            for guest in hotel_guests:
                                if guest["name"] == guest_name:
                                    manage_room("add",int(guest["room"]))
                                    break
                            remove_guest(guest_name)
                            cprint(f"\nGuest {guest_name} is succesfully removed","green")
                            break
                        else:
                            cprint(f"\nInvalid guest name : {guest_name}, {guest_name} is not a hotel guest, you have {3-(remove_tries+1)} tries left","red")

                case 5:
                    for logout_tries in range(3):
                        logout_choice = input("\nDo you want to logout: 'yes'/'no' ").strip().lower()
                        if logout_choice == "yes":
                            logout()
                        elif logout_choice == "no":
                            break
                        else:
                            cprint(f"\nInvalid response {logout_choice}, please respond with 'yes' or 'no', you have {3-(logout_tries+1)} tries left","red")

        except KeyboardInterrupt:
            print()
            for exit_tries in range(3):
                exit_choice = input("\nDo you want to force quit (not recommened) ? yes/no : ").strip().lower()
                if exit_choice == "yes":
                    cprint("\nThe program force quit\n","red")
                    exit()
                elif exit_choice == "no":
                    break
                else:
                    cprint(f"\nInvalid response : {exit_choice}, please respond with 'yes' or 'no', you have {3-(exit_tries+1)} tries left","red")



def handle_empty_rooms():
    global empty_rooms
    empty_rooms = []
    empty_rooms_set = set()
    with open("empty_rooms_list.txt") as file:
            for line in file.readlines():
                if line.rstrip().isdecimal() == True:
                    empty_rooms_set.add(int(line.rstrip()))
    for room in empty_rooms_set:
        empty_rooms.append(room)
    with open("empty_rooms_list.txt","w") as file:
            for e_r in sorted(empty_rooms):
                file.write(f"{str(e_r)}\n")
    empty_rooms = sorted(empty_rooms)


def handle_hotel_guests():
    global hotel_guests
    hotel_guests = []
    hotel_guests_name = []
    hotel_guests_room = []

    with open("hotel_guests_list.csv") as file:
            for guest in DictReader(file):
                try:
                    if guest not in hotel_guests and guest["name"].istitle() and guest["adult"].isdecimal() and (int(guest["adult"]) >= 1) and guest["kid"].isdecimal() and (int(guest["kid"]) >= 0) and guest["package"] in ["normal","premium","luxury"] and guest["night"].isdecimal() and (int(guest["night"]) >= 1) and guest["room"].isdecimal() and (int(guest["room"]) not in empty_rooms):
                        hotel_guests.append(guest)
                except AttributeError:
                    pass
    for append_guest_data in hotel_guests:
        hotel_guests_name.append(append_guest_data["name"])
        hotel_guests_room.append(append_guest_data["room"])

    for name in set(hotel_guests_name):
        if hotel_guests_name.count(name) > 1:
            cprint(f"\nThere are multiple guests with the same name : {name}, please choose which one is the CORRECT !","red")
            guest_with_number = []
            number_of_the_guest = 0
            for hg in hotel_guests:
                if hg["name"] == name:
                    number_of_the_guest += 1
                    print(f"Number : {number_of_the_guest}    Name : {hg['name']}, Adult : {hg['adult']}, Kid : {hg['kid']}, Package : {hg['package']}. Night : {hg['night']}, Room : {hg['room']}")
                    guest_with_number.append({"number_of_the_guest" : number_of_the_guest, "guest" : hg})

            for name_tries in range(3):
                try:
                    correct_guest_number = int(input("\nThe number of the CORRECT guest : ").strip())
                except ValueError :
                    if name_tries != 2:
                        cprint(f"\nInvalid number : Not a Number, please choose a number displayed after the 'Number' text, you have {3-(name_tries+1)} tries left","red")
                        for gwn in guest_with_number:
                            print(f"Number : {gwn['number_of_the_guest']}    Name : {gwn['guest']['name']}, Adult : {gwn['guest']['adult']}, Kid : {gwn['guest']['kid']}, Package : {gwn['guest']['package']}. Night : {gwn['guest']['night']}, Room : {gwn['guest']['room']}")
                    else:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                else:
                    if ((correct_guest_number < 1) or (correct_guest_number > number_of_the_guest)) and (name_tries == 2):
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    elif ((correct_guest_number < 1) or (correct_guest_number > number_of_the_guest)):
                        cprint(f"\nInvalid number : {correct_guest_number}, please choose a number displayed after the 'Number' text, you have {3-(name_tries+1)} tries left","red")
                        for gwn in guest_with_number:
                            print(f"Number : {gwn['number_of_the_guest']}    Name : {gwn['guest']['name']}, Adult : {gwn['guest']['adult']}, Kid : {gwn['guest']['kid']}, Package : {gwn['guest']['package']}. Night : {gwn['guest']['night']}, Room : {gwn['guest']['room']}")
                    else:
                        for g_w_n in guest_with_number:
                            if g_w_n["number_of_the_guest"] == correct_guest_number:
                                correct_guest = g_w_n["guest"]
                                break
                        break

            while hotel_guests_name.count(name) > 1:
                for h_g_index in range(len(hotel_guests)):
                    if (hotel_guests[h_g_index]["name"] == name) and (hotel_guests[h_g_index] != correct_guest):
                        del hotel_guests[h_g_index]
                        break
                for hgn_index in range(len(hotel_guests_name)):
                    if (hotel_guests_name[hgn_index] == name) and (hotel_guests_room[hgn_index] != correct_guest["room"]):
                        del hotel_guests_name[hgn_index]
                        del hotel_guests_room[hgn_index]
                        break
                    elif (hotel_guests_name[hgn_index] == name) and (hotel_guests_room[hgn_index] == correct_guest["room"]) and (hotel_guests_room.count(correct_guest["room"]) > 1):
                        del hotel_guests_name[hgn_index]
                        del hotel_guests_room[hgn_index]
                        break

    for room in set(hotel_guests_room):
        if hotel_guests_room.count(room) > 1:
            cprint(f"\nThere are multiple guests with the same room : {room}, please choose which one is the CORRECT !","red")
            guest_with_number = []
            number_of_the_guest = 0
            for h_guest in hotel_guests:
                if h_guest["room"] == room:
                    number_of_the_guest += 1
                    print(f"Number : {number_of_the_guest}    Name : {h_guest['name']}, Adult : {h_guest['adult']}, Kid : {h_guest['kid']}, Package : {h_guest['package']}. Night : {h_guest['night']}, Room : {h_guest['room']}")
                    guest_with_number.append({"number_of_the_guest" : number_of_the_guest, "guest" : h_guest})

            for room_tries in range(3):
                try:
                    correct_room_number = int(input("\nThe number of the CORRECT guest : ").strip())
                except ValueError :
                    if room_tries != 2:
                        cprint(f"\nInvalid number : Not a Number, please choose a number displayed after the 'Number' text, you have {3-(room_tries+1)} tries left","red")
                        for gwn in guest_with_number:
                            print(f"Number : {gwn['number_of_the_guest']}    Name : {gwn['guest']['name']}, Adult : {gwn['guest']['adult']}, Kid : {gwn['guest']['kid']}, Package : {gwn['guest']['package']}. Night : {gwn['guest']['night']}, Room : {gwn['guest']['room']}")
                    else:
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                else:
                    if ((correct_room_number < 1) or (correct_room_number > number_of_the_guest)) and (room_tries == 2):
                        cprint(f"\nInvalid number : {correct_room_number}, please choose a number displayed after the 'Number' text, you have {3-(room_tries+1)} tries left","red")
                        for gwn in guest_with_number:
                            print(f"Number : {gwn['number_of_the_guest']}    Name : {gwn['guest']['name']}, Adult : {gwn['guest']['adult']}, Kid : {gwn['guest']['kid']}, Package : {gwn['guest']['package']}. Night : {gwn['guest']['night']}, Room : {gwn['guest']['room']}")
                    elif ((correct_room_number < 1) or (correct_room_number > number_of_the_guest)):
                        cprint("\nToo many incorrect tries, the program closes itself\n","red")
                        exit()
                    else:
                        for g_w_n in guest_with_number:
                            if g_w_n["number_of_the_guest"] == correct_room_number:
                                correct_guest = g_w_n["guest"]
                                break
                        break

            while hotel_guests_room.count(room) > 1:
                for hg_index in range(len(hotel_guests)):
                    if (hotel_guests[hg_index]["room"] == room) and (hotel_guests[hg_index] != correct_guest):
                        del hotel_guests[hg_index]
                        break
                for hgr_index in range(len(hotel_guests_room)):
                    if (hotel_guests_room[hgr_index] == room) and (hotel_guests_name[hgr_index] != correct_guest["name"]):
                        del hotel_guests_room[hgr_index]
                        del hotel_guests_name[hgr_index]
                        break

    with open("hotel_guests_list.csv","w") as file:
        writer = DictWriter(file, fieldnames=["name","adult","kid","package","night","room"])
        writer.writeheader()
        for write_guest in sorted(hotel_guests, key=lambda guest: guest["name"]):
            writer.writerow(write_guest)


def login(password_entered,actual_password):
    if password_entered == actual_password:
        return True


def check_room(rooms_list,room):
    empty_rooms_set = set()
    try:
        rooms_list = rooms_list.strip()
    except AttributeError:
        pass
    else:
        with open(rooms_list) as file:
                for line in file.readlines():
                    if line.rstrip().isdecimal() == True:
                        empty_rooms_set.add(int(line.rstrip()))
    try:
        if int(room.strip()) in empty_rooms_set:
            return "correct"
    except (ValueError, AttributeError, TypeError):
        pass


def check_name(guests_list,name):
    hotel_guests=[]
    try:
        guests_list = guests_list.strip()
        name = name.strip().lower().title()
    except AttributeError:
        pass
    else:
        with open(guests_list) as file:
                    for guest in DictReader(file):
                        try:
                            if guest not in hotel_guests and guest["name"].istitle() and guest["adult"].isdecimal() and (int(guest["adult"]) >= 1) and guest["kid"].isdecimal() and (int(guest["kid"]) >= 0) and guest["package"] in ["normal","premium","luxury"] and guest["night"].isdecimal() and (int(guest["night"]) >= 1) and guest["room"].isdecimal():
                                hotel_guests.append(guest)
                        except AttributeError:
                            pass
        hotel_guest_names=[]
        for guest in hotel_guests:
            hotel_guest_names.append(guest["name"])
        if name not in hotel_guest_names and name.istitle():
            return "correct"


def check_package(package):
    try:
        if package.strip().lower() in ["normal","premium","luxury"]:
            return "correct"
    except AttributeError:
        pass


def check_night(night):
        try:
            if int(night.strip()) > 0:
                return "correct"
        except (ValueError, AttributeError):
            pass


def check_adult(adult):
        try:
            if int(adult.strip()) > 0:
                return "correct"
        except (ValueError, AttributeError):
            pass


def check_kid(kid):
    try:
        if int(kid.strip()) >= 0:
            return "correct"
    except (ValueError, AttributeError):
        pass


def make_guest_data(name,adult,kid,package,night,room):
    try:
        return {"name": name.strip().lower().title(), "adult": int(adult.strip()), "kid": int(kid.strip()), "package": package.strip().lower(), "night": int(night.strip()), "room": int(room.strip())}
    except (ValueError, AttributeError):
        pass


def get_price(adult,kid,package,night):
    try:
        match package.strip().lower():
            case "normal":
                return (int(adult.strip())*300 + int(kid.strip())*150)*int(night.strip())
            case "premium":
                return (int(adult.strip())*600 + int(kid.strip())*300)*int(night.strip())
            case "luxury":
                return (int(adult.strip())*900 + int(kid.strip())*450)*int(night.strip())
    except (ValueError, AttributeError):
        pass


def manage_room(mode,room):
    global empty_rooms

    try:
        mode = mode.strip().lower()
    except AttributeError:
        pass
    else:
        if mode == "remove":
            for index in range(len(empty_rooms)):
                if empty_rooms[index] == room:
                    del empty_rooms[index]
                    break
            with open("empty_rooms_list.txt","w") as file:
                for room in sorted(empty_rooms):
                    file.write(f"{str(room)}\n")
        elif mode == "add":
            empty_rooms.append(room)
            with open("empty_rooms_list.txt","w") as file:
                for e_r in sorted(empty_rooms):
                    file.write(f"{str(e_r)}\n")


def add_guest(guest):
    global hotel_guests

    hotel_guests.append(guest)
    with open("hotel_guests_list.csv","w") as file:
        writer = DictWriter(file, fieldnames=["name","adult","kid","package","night","room"])
        writer.writeheader()
        for h_g in sorted(hotel_guests, key=lambda guest: guest["name"]):
            writer.writerow(h_g)


def check_guest_access(guests_list,name,service):
    premium = ["pool","gym"]
    luxury = ["pool","gym","dining","massage","sauna"]
    hotel_guests_name = []
    hotel_guests = []

    try:
        guests_list = guests_list.strip()
    except AttributeError:
        return "error",f"Invalid type for guests_list : {str(type(guests_list)).split(' ')[1].rstrip('>')}, guests_list must be string"
    else:
        with open(guests_list) as file:
            for guest in DictReader(file):
                try:
                    if guest not in hotel_guests and guest["name"].istitle() and guest["adult"].isdecimal() and (int(guest["adult"]) >= 1) and guest["kid"].isdecimal() and (int(guest["kid"]) >= 0) and guest["package"] in ["normal","premium","luxury"] and guest["night"].isdecimal() and (int(guest["night"]) >= 1) and guest["room"].isdecimal():
                        hotel_guests.append(guest)
                except AttributeError:
                    pass
        for h_g in hotel_guests:
            hotel_guests_name.append(h_g["name"])

    try:
        name = name.strip().lower().title()
        service = service.strip().lower()
    except AttributeError:
        if type(name) != str and type(service) != str:
            return "error",f"Invalid type for name and service : {str(type(name)).split(' ')[1].rstrip('>')} and {str(type(service)).split(' ')[1].rstrip('>')}, name and service must be string"
        elif type(name) == str and type(service) != str:
            if name in hotel_guests_name:
                return "error",f"Invalid type for service : {str(type(service)).split(' ')[1].rstrip('>')}, service must be string"
            else:
                return "error",f"Invalid name : {name}, {name} not a hotel guest and invalid type for service {str(type(service)).split(' ')[1].rstrip('>')}, service must be string"
        else:
            if service in luxury:
                return "error",f"Invalid type for name : {str(type(name)).split(' ')[1].rstrip('>')}, name must be string"
            else:
                return "error",f"Invalid service : {service}, {service} not one of the hotel services and invalid type for name {str(type(name)).split(' ')[1].rstrip('>')}, name must be string"
    else:
        if (name in hotel_guests_name) and (service in luxury):
            for hg in hotel_guests:
                if hg["name"] == name:
                    match hg["package"]:
                        case "normal":
                            return "denied",f"\naccess denied, normal package which {name} bought dont include any service"
                        case "premium":
                            if service in premium:
                                return "granted","\naccess granted"
                            else:
                                return "denied",f"\naccess denied, premium package which {name} bought dont include {service}"
                        case "luxury":
                            return "granted","\naccess granted"
        else:
            if (name not in hotel_guests_name) and (service in luxury):
                if name == "":
                    return "error","\nincorrect guest name : None"
                else:
                    return "error",f"\nincorrect guest name : {name}"
            elif (service not in luxury) and (name in hotel_guests_name):
                if service == "":
                    return "error","\nincorrect service name : None"
                else:
                    return "error",f"\nincorrect service name : {service}"
            else:
                if name == "" and service == "":
                    return "error","\nincorrect guest and service name : None"
                elif name == "":
                    return "error",f"\nincorrect guest and service name : None, {service}"
                elif service == "":
                    return "error",f"\nincorrect guest and service name : {name}, None"
                else:
                    return "error",f"\nincorrect guest and service name : {name}, {service}"


def search_for_client(guests_list,name):
    hotel_guests = []

    try:
        guests_list = guests_list.strip()
    except AttributeError:
        return "error",f"\nInvalid type for guests_list : {str(type(guests_list)).split(' ')[1].rstrip('>')}, guests_list must be string"
    else:
        with open(guests_list) as file:
                for guest in DictReader(file):
                    try:
                        if guest not in hotel_guests and guest["name"].istitle() and guest["adult"].isdecimal() and (int(guest["adult"]) >= 1) and guest["kid"].isdecimal() and (int(guest["kid"]) >= 0) and guest["package"] in ["normal","premium","luxury"] and guest["night"].isdecimal() and (int(guest["night"]) >= 1) and guest["room"].isdecimal():
                            hotel_guests.append(guest)
                    except AttributeError:
                        pass

    try:
        name = name.strip().lower().title()
    except AttributeError:
        return "error",f"\nInccorect type for name : {str(type(name)).split(' ')[1].rstrip('>')}, name must be a string"
    else:
        hotel_guests_name = []
        for h_g in hotel_guests:
            hotel_guests_name.append(h_g["name"])
        if name in hotel_guests_name:
            for hg in hotel_guests:
                if name == hg["name"]:
                    return "correct",f"\nName : {hg['name']} \nPackage : {hg['package']} \nNumber of adults : {hg['adult']} \nNumber of kids : {hg['kid']} \nNumber of staying nights : {hg['night']} \nRoom number : {hg['room']}"
        else:
            if name == "":
                return "error","\nInvlaid guest name : None, None is not the hotels guest"
            else:
                return "error",f"\nInvlaid guest name : {name}, {name} is not the hotels guest"


def remove_guest(name):
    global hotel_guests

    try:
        name = name.strip().lower().title()
    except AttributeError:
        pass
    else:
        for index in range(len(hotel_guests)):
            if hotel_guests[index]["name"] == name:
                del hotel_guests[index]
                break
        with open("hotel_guests_list.csv","w") as file:
            writer = DictWriter(file, fieldnames=["name","adult","kid","package","night","room"])
            writer.writeheader()
            for guest in sorted(hotel_guests, key=lambda guest: guest["name"]):
                writer.writerow(guest)



def logout():
    if (len(hotel_guests) + len(empty_rooms)) == hotel_room_limit:
        cprint("\nThere is no missing or excess data in the database","green")
    elif (len(hotel_guests) + len(empty_rooms)) < hotel_room_limit:
        cprint(f"\nThere is {hotel_room_limit - (len(hotel_guests) + len(empty_rooms))} missing room in empty rooms list or guests in hotel guests list","red")
    else:
        cprint(f"\nThere is {(len(hotel_guests) + len(empty_rooms)) - hotel_room_limit} more room or guest in the database","red")
    exit("")

if __name__=="__main__":
     main()