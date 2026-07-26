from project import login, get_price, check_guest_access, search_for_client, check_room, check_name, check_package, check_night, check_adult, check_kid, make_guest_data


def test_login_capitalized():
    assert login("Password","password") == None
def test_login_all_uppercase():
    assert login("PASSWORD","password") == None
def test_login_nothing():
    assert login("","password") == None
def test_login_whitespace():
    assert login(" ","password") == None
def test_login_list():
    assert login([],"password") == None
def test_login_dictionary():
    assert login({},"password") == None
def test_login_integer():
    assert login(1,"password") == None
    assert login(-8,"password") == None
    assert login(0,"password") == None
def test_login_float():
    assert login(7.87,"password") == None
    assert login(-2.34,"password") == None
    assert login(0.0000,"password") == None
def test_login_set():
    assert login(set(),"password") == None
def test_login_boolean_true():
    assert login(True,"password") == None
def test_login_boolean_false():
    assert login(False,"password") == None

def test_login_correct():
    assert login("password","password") == True


def test_check_room_not_a_room():
    assert check_room("check_room_tester.txt","not a room") == None
def test_check_room_nothing():
    assert check_room("check_room_tester.txt","") == None
def test_check_room_whitespace():
    assert check_room("check_room_tester.txt"," ") == None
def test_check_rooms_list():
    assert check_room("check_room_tester.txt",[]) == None
def test_check_room_dictionary():
    assert check_room("check_room_tester.txt",{}) == None
def test_check_room_float():
    assert check_room("check_room_tester.txt",13.5) == None
    assert check_room("check_room_tester.txt",-13.5) == None
    assert check_room("check_room_tester.txt",0.000) == None
def test_check_room_set():
    assert check_room("check_room_tester.txt",set()) == None
def test_check_room_boolean_true():
    assert check_room("check_room_tester.txt",True) == None
def test_check_room_boolean_false():
    assert check_room("check_room_tester.txt",False) == None
def test_check_room_minus_1():
    assert check_room("check_room_tester.txt","-1") == None
    assert check_room("check_room_tester.txt"," -1") == None
    assert check_room("check_room_tester.txt","-1 ") == None
    assert check_room("check_room_tester.txt"," -1 ") == None
def test_check_room_minus_2():
    assert check_room("check_room_tester.txt","-2") == None
    assert check_room("check_room_tester.txt"," -2") == None
    assert check_room("check_room_tester.txt","-2 ") == None
    assert check_room("check_room_tester.txt"," -2 ") == None
def test_check_room_minus_3():
    assert check_room("check_room_tester.txt","-3") == None
    assert check_room("check_room_tester.txt"," -3") == None
    assert check_room("check_room_tester.txt","-3 ") == None
    assert check_room("check_room_tester.txt"," -3 ") == None
def test_check_room_minus_4():
    assert check_room("check_room_tester.txt","-4") == None
    assert check_room("check_room_tester.txt"," -4") == None
    assert check_room("check_room_tester.txt","-4 ") == None
    assert check_room("check_room_tester.txt"," -4 ") == None
def test_check_room_minus_400():
    assert check_room("check_room_tester.txt","-400") == None
    assert check_room("check_room_tester.txt"," -400") == None
    assert check_room("check_room_tester.txt","-400 ") == None
    assert check_room("check_room_tester.txt"," -400 ") == None

def test_check_room_incorrect_rooms_list_type_list():
    assert check_room([],"1") == None
def test_check_room_incorrect_rooms_list_type_dictionary():
    assert check_room({},"1") == None
def test_check_room_incorrect_rooms_list_type_float():
    assert check_room(4.342,"1") == None
    assert check_room(-4.342,"1") == None
    assert check_room(0.00,"1") == None
def test_check_room_incorrect_rooms_list_type_integer():
    assert check_room(7,"1") == None
    assert check_room(-7,"1") == None
    assert check_room(0,"1") == None
def test_check_room_incorrect_rooms_list_type_set():
    assert check_room(set(),"1") == None
def test_check_room_incorrect_rooms_list_type_boolean_true():
    assert check_room(True,"1") == None
def test_check_room_incorrect_rooms_list_type_boolean_false():
    assert check_room(False,"1") == None

def test_check_room_correct_1():
    assert check_room("check_room_tester.txt","1") == "correct"
    assert check_room("check_room_tester.txt"," 1") == "correct"
    assert check_room("check_room_tester.txt","1 ") == "correct"
    assert check_room("check_room_tester.txt"," 1 ") == "correct"
def test_check_room_correct_2():
    assert check_room("check_room_tester.txt","2") == "correct"
    assert check_room("check_room_tester.txt"," 2") == "correct"
    assert check_room("check_room_tester.txt","2 ") == "correct"
    assert check_room("check_room_tester.txt"," 2 ") == "correct"
def test_check_room_correct_3():
    assert check_room("check_room_tester.txt","3") == "correct"
    assert check_room("check_room_tester.txt"," 3") == "correct"
    assert check_room("check_room_tester.txt","3 ") == "correct"
    assert check_room("check_room_tester.txt"," 3 ") == "correct"
def test_check_room_correct_4():
    assert check_room("check_room_tester.txt","4") == "correct"
    assert check_room("check_room_tester.txt"," 4") == "correct"
    assert check_room("check_room_tester.txt","4 ") == "correct"
    assert check_room("check_room_tester.txt"," 4 ") == "correct"
def test_check_room_correct_5():
    assert check_room("check_room_tester.txt","5") == "correct"
    assert check_room("check_room_tester.txt"," 5") == "correct"
    assert check_room("check_room_tester.txt","5 ") == "correct"
    assert check_room("check_room_tester.txt"," 5 ") == "correct"
def test_check_room_correct_400():
    assert check_room("check_room_tester.txt","400") == "correct"
    assert check_room("check_room_tester.txt"," 400") == "correct"
    assert check_room("check_room_tester.txt","400 ") == "correct"
    assert check_room("check_room_tester.txt"," 400 ") == "correct"


def test_check_name_nothing():
    assert check_name("guest_list_for_testing.csv","") == None
def test_check_name_whitespaces():
    assert check_name("guest_list_for_testing.csv","   ") == None
def test_check_name_list():
    assert check_name("guest_list_for_testing.csv",[]) == None
def test_check_name_dictionary():
    assert check_name("guest_list_for_testing.csv",{}) == None
def test_check_name_float():
    assert check_name("guest_list_for_testing.csv","3.1415") == None
    assert check_name("guest_list_for_testing.csv","-1.11111") == None
    assert check_name("guest_list_for_testing.csv","0.0000") == None
def test_check_name_integer():
    assert check_name("guest_list_for_testing.csv","2") == None
    assert check_name("guest_list_for_testing.csv","-2") == None
    assert check_name("guest_list_for_testing.csv","0") == None
    assert check_name("guest_list_for_testing.csv","22355") == None
def test_check_name_set():
    assert check_name("guest_list_for_testing.csv",set()) == None
def test_check_name_boolean_true():
    assert check_name("guest_list_for_testing.csv",True) == None
def test_check_name_boolean_false():
    assert check_name("guest_list_for_testing.csv",False) == None
def test_check_name_existing_guest_Veteran_Guest():
    assert check_name("guest_list_for_testing.csv","Veteran Guest") == None
def test_check_name_existing_guest_New_Guest():
    assert check_name("guest_list_for_testing.csv","New Guest") == None
def test_check_name_existing_guest_Tall_Guest():
    assert check_name("guest_list_for_testing.csv","Tall Guest") == None
def test_check_name_existing_guest_Short_Guest():
    assert check_name("guest_list_for_testing.csv","Short Guest") == None
def test_check_name_existing_guest_Funny_Guest():
    assert check_name("guest_list_for_testing.csv","Funny Guest") == None

def test_check_name_incorrect_guests_list_type_list():
    assert check_name([],"happy guest") == None
def test_check_name_incorrect_guests_list_type_dictionary():
    assert check_name({},"happy guest") == None
def test_check_name_incorrect_guests_list_type_float():
    assert check_name(4.444,"happy guest") == None
    assert check_name(-4.444,"happy guest") == None
    assert check_name(0,"happy guest") == None
def test_check_name_incorrect_guests_list_type_integer():
    assert check_name(2,"happy guest") == None
    assert check_name(-2,"happy guest") == None
    assert check_name(0,"happy guest") == None
def test_check_name_incorrect_guests_list_type_set():
    assert check_name(set(),"happy guest") == None
def test_check_name_incorrect_guests_list_type_boolean_ture():
    assert check_name(True,"happy guest") == None
def test_check_name_incorrect_guests_list_type_boolean_false():
    assert check_name(False,"happy guest") == None

def test_check_name_wrong_formated_not_titled_happy_Guest():
    assert check_name("guest_list_for_testing.csv","happy guest") == "correct"
def test_check_name_wrong_formated_not_titled_happy_Guest1():
    assert check_name("guest_list_for_testing.csv","Happy guest") == "correct"
def test_check_name_wrong_formated_not_titled_happy_Guest2():
    assert check_name("guest_list_for_testing.csv","happy Guest") == "correct"
def test_check_name_wrong_formated_not_titled_happy_Guest3():
    assert check_name("guest_list_for_testing.csv","Happy Guest") == "correct"
def test_check_name_wrong_formated_not_titled_happy_Guest4():
    assert check_name("guest_list_for_testing.csv","   hAppY gUeSt   ") == "correct"
def test_check_name_wrong_formated_incorrect_adult_number_Sporty_Guest():
    assert check_name("guest_list_for_testing.csv","sporty guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Sporty guest") == "correct"
    assert check_name("guest_list_for_testing.csv","sporty Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Sporty Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","   spoRty guEsT   ") == "correct"
def test_check_name_wrong_formated_incorrect_kid_number_Traveler_Guest():
    assert check_name("guest_list_for_testing.csv","traveler guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Traveler guest") == "correct"
    assert check_name("guest_list_for_testing.csv","traveler Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Traveler Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","   trAVeler GUest   ") == "correct"
def test_check_name_wrong_formated_incorrect_package_Tired_Guest():
    assert check_name("guest_list_for_testing.csv","tired guest") == "correct"
    assert check_name("guest_list_for_testing.csv","tired Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Tired guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Tired Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","   TIRed gueSt   ") == "correct"
def test_check_name_wrong_formated_incorrect_night_number_Motivating_Guest():
    assert check_name("guest_list_for_testing.csv","motivating guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Motivating guest") == "correct"
    assert check_name("guest_list_for_testing.csv","motivating Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Motivating Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","   MOtiVating GuEst   ") == "correct"
def test_check_name_wrong_formated_incorrect_room_number_Dancer_Guest():
    assert check_name("guest_list_for_testing.csv","dancer guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Dancer guest") == "correct"
    assert check_name("guest_list_for_testing.csv","dancer Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","Dancer Guest") == "correct"
    assert check_name("guest_list_for_testing.csv","   DANcer gUest   ") == "correct"


def test_check_package_not_a_package():
    assert check_package("not a package") == None
def test_check_package_nothing():
    assert check_package("") == None
def test_check_package_whitespace():
    assert check_package(" ") == None
def test_check_package_list():
    assert check_package([]) == None
def test_check_package_dictionary():
    assert check_package({}) == None
def test_check_package_float():
    assert check_package(1.234) == None
    assert check_package(-1.234) == None
    assert check_package(0.000) == None
def test_check_package_set():
    assert check_package(set()) == None
def test_check_package_boolean_true():
    assert check_package(True) == None
def test_check_package_boolean_false():
    assert check_package(False) == None

def test_check_package_normal():
    assert check_package("normal") == "correct"
    assert check_package(" normal") == "correct"
    assert check_package("normal ") == "correct"
    assert check_package(" normal ") == "correct"
def test_check_package_premium():
    assert check_package("premium") == "correct"
    assert check_package(" premium") == "correct"
    assert check_package("premium ") == "correct"
    assert check_package(" premium ") == "correct"
def test_check_package_luxury():
    assert check_package("luxury") == "correct"
    assert check_package(" luxury") == "correct"
    assert check_package("luxury ") == "correct"
    assert check_package(" luxury ") == "correct"


def test_check_night_not_a_room():
    assert check_night("not a room") == None
def test_check_night_nothing():
    assert check_night("") == None
def test_check_night_whitespace():
    assert check_night(" ") == None
def test_check_night_list():
    assert check_night([]) == None
def test_check_night_dictionary():
    assert check_night({}) == None
def test_check_night_float():
    assert check_night(13.5) == None
    assert check_night(-13.5) == None
    assert check_night(0.000) == None
def test_check_night_set():
    assert check_night(set()) == None
def test_check_night_boolean_true():
    assert check_night(True) == None
def test_check_night_boolean_false():
    assert check_night(False) == None
def test_check_night_incorrect_negative():
    assert check_night("-1") == None
    assert check_night("-14") == None
    assert check_night(-1) == None
    assert check_night(-14) == None
def test_check_night_incorrect_zero():
    assert check_night("0") == None
    assert check_night(0) == None
def test_check_night_incorrect_positive():
    assert check_night(1) == None
    assert check_night(1.45) == None
    assert check_night("1.45") == None

def test_check_night_correct():
    assert check_night("1") == "correct"
    assert check_night(" 1") == "correct"
    assert check_night("1 ") == "correct"
    assert check_night(" 1 ") == "correct"
    assert check_night("2") == "correct"
    assert check_night(" 2") == "correct"
    assert check_night("2 ") == "correct"
    assert check_night(" 2 ") == "correct"
    assert check_night("4") == "correct"
    assert check_night(" 4") == "correct"
    assert check_night("4 ") == "correct"
    assert check_night(" 4" ) == "correct"
    assert check_night("5") == "correct"
    assert check_night(" 5") == "correct"
    assert check_night("5 ") == "correct"
    assert check_night(" 5 ") == "correct"
    assert check_night("8") == "correct"
    assert check_night(" 8") == "correct"
    assert check_night("8 ") == "correct"
    assert check_night(" 8 ") == "correct"


def test_check_adult_not_a_room():
    assert check_adult("not a room") == None
def test_check_adult_nothing():
    assert check_adult("") == None
def test_check_adult_whitespace():
    assert check_adult(" ") == None
def test_check_adult_list():
    assert check_adult([]) == None
def test_check_adult_dictionary():
    assert check_adult({}) == None
def test_check_adult_float():
    assert check_adult(78.6) == None
    assert check_adult(-7.865) == None
    assert check_adult(0.000) == None
def test_check_adult_set():
    assert check_adult(set()) == None
def test_check_adult_boolean_true():
    assert check_adult(True) == None
def test_check_adult_boolean_false():
    assert check_adult(False) == None
def test_check_adult_incorrect_negative():
    assert check_adult("-1") == None
    assert check_adult("-14") == None
    assert check_adult(-1) == None
    assert check_adult(-14) == None
def test_check_adult_incorrect_zero():
    assert check_adult("0") == None
    assert check_adult(0) == None
def test_check_adult_incorrect_positive():
    assert check_adult(1) == None
    assert check_adult("1.45") == None
    assert check_adult(1.45) == None

def test_check_adult_correct():
    assert check_adult("1") == "correct"
    assert check_adult(" 1") == "correct"
    assert check_adult("1 ") == "correct"
    assert check_adult(" 1 ") == "correct"
    assert check_adult("2") == "correct"
    assert check_adult(" 2") == "correct"
    assert check_adult("2 ") == "correct"
    assert check_adult(" 2 ") == "correct"
    assert check_adult("100") == "correct"
    assert check_adult(" 100") == "correct"
    assert check_adult("100 ") == "correct"
    assert check_adult(" 100 ") == "correct"


def test_check_kid_not_a_room():
    assert check_kid("not a room") == None
def test_check_kid_nothing():
    assert check_kid("") == None
def test_check_kid_whitespace():
    assert check_kid(" ") == None
def test_check_kid_list():
    assert check_kid([]) == None
def test_check_kid_dictionary():
    assert check_kid({}) == None
def test_check_kid_float():
    assert check_kid(45.65) == None
    assert check_kid(-4.3333) == None
    assert check_kid(0.0000) == None
def test_check_kid_set():
    assert check_kid(set()) == None
def test_check_kid_boolean_true():
    assert check_kid(True) == None
def test_check_kid_boolean_false():
    assert check_kid(False) == None
def test_check_kid_incorrect_negative():
    assert check_kid("-1") == None
    assert check_kid("-1.45") == None
    assert check_kid("-14") == None
    assert check_kid("-14.34") == None
    assert check_kid(-1) == None
    assert check_kid(-1.64) == None
    assert check_kid(-14) == None
    assert check_kid(-14.87) == None
def test_check_kid_incorrect_zero():
    assert check_kid(0) == None

def test_check_kid_correct_zero():
    assert check_kid("0") == "correct"
    assert check_kid(" 0") == "correct"
    assert check_kid("0 ") == "correct"
    assert check_kid(" 0 ") == "correct"
def test_check_kid_incorrect_positive():
    assert check_kid(1) == None
    assert check_kid("1.45") == None
    assert check_kid(1.45) == None
def test_check_kid_correct_positive():
    assert check_kid("1") == "correct"
    assert check_kid(" 1") == "correct"
    assert check_kid("1 ") == "correct"
    assert check_kid(" 1 ") == "correct"
    assert check_kid("2") == "correct"
    assert check_kid(" 2") == "correct"
    assert check_kid("2 ") == "correct"
    assert check_kid(" 2 ") == "correct"
    assert check_kid("100") == "correct"
    assert check_kid(" 100") == "correct"
    assert check_kid("100 ") == "correct"
    assert check_kid(" 100 ") == "correct"


def test_get_price_incorrect_normal():
    assert get_price(1,1,"normal",1) == None
    assert get_price(1,1,"normal","1") == None
    assert get_price(1,"1","normal",1) == None
    assert get_price(1,"1","normal","1") == None
    assert get_price("1",1,"normal",1) == None
    assert get_price("1",1,"normal","1") == None
    assert get_price("1","1","normal",1) == None
def test_get_price_incorrect_premium():
    assert get_price(1,1,"premium",1) == None
    assert get_price(1,1,"premium","1") == None
    assert get_price(1,"1","premium",1) == None
    assert get_price(1,"1","premium","1") == None
    assert get_price("1",1,"premium",1) == None
    assert get_price("1",1,"premium","1") == None
    assert get_price("1","1","premium",1) == None
def test_get_price_incorrect_luxury():
    assert get_price(1,1,"luxury",1) == None
    assert get_price(1,1,"luxury","1") == None
    assert get_price(1,"1","luxury",1) == None
    assert get_price(1,"1","luxury","1") == None
    assert get_price("1",1,"luxury",1) == None
    assert get_price("1",1,"luxury","1") == None
    assert get_price("1","1","luxury",1) == None

def test_get_price_correct_normal():
    assert get_price("1","1","normal","1") == 450
    assert get_price(" 1"," 1"," Normal"," 1") == 450
    assert get_price("1 ","1 ","norMal ","1 ") == 450
    assert get_price(" 1 "," 1 "," NORMAL "," 1 ") == 450
def test_get_price_correct_premium():
    assert get_price("2","2","premium","2") == 3600
    assert get_price(" 2"," 2"," Premium"," 2") == 3600
    assert get_price("2 ","2 ","preMium ","2 ") == 3600
    assert get_price(" 2 "," 2 "," PREMIUM "," 2 ") == 3600
def test_get_price_correct_luxury():
    assert get_price("3","3","luxury","3") == 12150
    assert get_price(" 3"," 3"," Luxury"," 3") == 12150
    assert get_price("3 ","3 ","luXury ","3 ") == 12150
    assert get_price(" 3 "," 3 "," LUXURY "," 3 ") == 12150


def test_search_for_client_not_a_guest():
    assert search_for_client("guest_list_for_testing.csv","not a guest") == ("error","\nInvlaid guest name : Not A Guest, Not A Guest is not the hotels guest")
    assert search_for_client("guest_list_for_testing.csv","NOBODY") == ("error","\nInvlaid guest name : Nobody, Nobody is not the hotels guest")
    assert search_for_client("guest_list_for_testing.csv","cat") == ("error","\nInvlaid guest name : Cat, Cat is not the hotels guest")
def test_search_for_client_nothing():
    assert search_for_client("guest_list_for_testing.csv","") == ("error","\nInvlaid guest name : None, None is not the hotels guest")
def test_search_for_client_whitespace():
    assert search_for_client("guest_list_for_testing.csv"," ") == ("error","\nInvlaid guest name : None, None is not the hotels guest")
def test_search_for_client_incorrect_type_list():
    assert search_for_client("guest_list_for_testing.csv",[]) == ("error","\nInccorect type for name : 'list', name must be a string")
def test_search_for_client_incorrect_type_dictionary():
    assert search_for_client("guest_list_for_testing.csv",{}) == ("error","\nInccorect type for name : 'dict', name must be a string")
def test_search_for_client_incorrect_type_float():
    assert search_for_client("guest_list_for_testing.csv",1.23) == ("error","\nInccorect type for name : 'float', name must be a string")
def test_search_for_client_incorrect_type_set():
    assert search_for_client("guest_list_for_testing.csv",set()) == ("error","\nInccorect type for name : 'set', name must be a string")
def test_search_for_client_incorrect_type_boolean_true():
    assert search_for_client("guest_list_for_testing.csv",True) == ("error","\nInccorect type for name : 'bool', name must be a string")
def test_search_for_client_incorrect_type_boolean_false():
    assert search_for_client("guest_list_for_testing.csv",False) == ("error","\nInccorect type for name : 'bool', name must be a string")

def test_search_for_client_invalid_guests_list_type_list():
    assert search_for_client([],"") == ("error",f"\nInvalid type for guests_list : 'list', guests_list must be string")
def test_search_for_client_invalid_guests_list_type_dictionary():
    assert search_for_client({},"") == ("error",f"\nInvalid type for guests_list : 'dict', guests_list must be string")
def test_search_for_client_invalid_guests_list_type_float():
    assert search_for_client(1.23,"") == ("error",f"\nInvalid type for guests_list : 'float', guests_list must be string")
    assert search_for_client(-1.23,"") == ("error",f"\nInvalid type for guests_list : 'float', guests_list must be string")
    assert search_for_client(0.00,"") == ("error",f"\nInvalid type for guests_list : 'float', guests_list must be string")
def test_search_for_client_invalid_guests_list_type_int():
    assert search_for_client(23,"") == ("error",f"\nInvalid type for guests_list : 'int', guests_list must be string")
    assert search_for_client(-23,"") == ("error",f"\nInvalid type for guests_list : 'int', guests_list must be string")
    assert search_for_client(0,"") == ("error",f"\nInvalid type for guests_list : 'int', guests_list must be string")
def test_search_for_client_invalid_guests_list_type_set():
    assert search_for_client(set(),"") == ("error",f"\nInvalid type for guests_list : 'set', guests_list must be string")
def test_search_for_client_invalid_guests_list_type_boolen_true():
    assert search_for_client(True,"") == ("error",f"\nInvalid type for guests_list : 'bool', guests_list must be string")
def test_search_for_client_invalid_guests_list_type_boolen_false():
    assert search_for_client(False,"") == ("error",f"\nInvalid type for guests_list : 'bool', guests_list must be string")

def test_search_for_client_alex():
    assert search_for_client("guest_list_for_testing.csv","alex") == ("correct","\nName : Alex \nPackage : normal \nNumber of adults : 3 \nNumber of kids : 3 \nNumber of staying nights : 3 \nRoom number : 3")
    assert search_for_client("guest_list_for_testing.csv","  Alex  ") == ("correct","\nName : Alex \nPackage : normal \nNumber of adults : 3 \nNumber of kids : 3 \nNumber of staying nights : 3 \nRoom number : 3")
    assert search_for_client("guest_list_for_testing.csv","  aLEx") == ("correct","\nName : Alex \nPackage : normal \nNumber of adults : 3 \nNumber of kids : 3 \nNumber of staying nights : 3 \nRoom number : 3")
    assert search_for_client("guest_list_for_testing.csv","ALEX") == ("correct","\nName : Alex \nPackage : normal \nNumber of adults : 3 \nNumber of kids : 3 \nNumber of staying nights : 3 \nRoom number : 3")
def test_search_for_client_tomas():
    assert search_for_client("guest_list_for_testing.csv","tomas") == ("correct","\nName : Tomas \nPackage : luxury \nNumber of adults : 1 \nNumber of kids : 0 \nNumber of staying nights : 5 \nRoom number : 10")
    assert search_for_client("guest_list_for_testing.csv","  Tomas  ") == ("correct","\nName : Tomas \nPackage : luxury \nNumber of adults : 1 \nNumber of kids : 0 \nNumber of staying nights : 5 \nRoom number : 10")
    assert search_for_client("guest_list_for_testing.csv","  ToMaS") == ("correct","\nName : Tomas \nPackage : luxury \nNumber of adults : 1 \nNumber of kids : 0 \nNumber of staying nights : 5 \nRoom number : 10")
    assert search_for_client("guest_list_for_testing.csv","TOMAS") == ("correct","\nName : Tomas \nPackage : luxury \nNumber of adults : 1 \nNumber of kids : 0 \nNumber of staying nights : 5 \nRoom number : 10")


def test_check_guest_access_wrong_name_type_list_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv",[],"pool") == ("error","Invalid type for name : 'list', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",[],"gym") == ("error","Invalid type for name : 'list', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",[],"dining") == ("error","Invalid type for name : 'list', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",[],"sauna") == ("error","Invalid type for name : 'list', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",[],"massage") == ("error","Invalid type for name : 'list', name must be string")
def test_check_guest_access_wrong_name_type_list_and_incorrect_service():
    assert check_guest_access("guest_list_for_testing.csv",[],"skydiving") == ("error","Invalid service : skydiving, skydiving not one of the hotel services and invalid type for name 'list', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",[],"Monster Truck Show") == ("error","Invalid service : Monster Truck Show, Monster Truck Show not one of the hotel services and invalid type for name 'list', name must be string")
def test_check_guest_access_wrong_name_type_dictionary_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv",{},"pool") == ("error","Invalid type for name : 'dict', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",{},"gym") == ("error","Invalid type for name : 'dict', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",{},"dining") == ("error","Invalid type for name : 'dict', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",{},"sauna") == ("error","Invalid type for name : 'dict', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",{},"massage") == ("error","Invalid type for name : 'dict', name must be string")
def test_check_guest_access_wrong_name_type_dictionary_and_incorrect_service():
    assert check_guest_access("guest_list_for_testing.csv",{},"skydiving") == ("error","Invalid service : skydiving, skydiving not one of the hotel services and invalid type for name 'dict', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",{},"Monster Truck Show") == ("error","Invalid service : Monster Truck Show, Monster Truck Show not one of the hotel services and invalid type for name 'dict', name must be string")
def test_check_guest_access_wrong_name_type_float_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv",1.23,"pool") == ("error","Invalid type for name : 'float', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",1.23,"gym") == ("error","Invalid type for name : 'float', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",1.23,"dining") == ("error","Invalid type for name : 'float', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",1.23,"sauna") == ("error","Invalid type for name : 'float', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",1.23,"massage") == ("error","Invalid type for name : 'float', name must be string")
def test_check_guest_access_wrong_name_type_float_and_incorrect_service():
    assert check_guest_access("guest_list_for_testing.csv",1.23,"skydiving") == ("error","Invalid service : skydiving, skydiving not one of the hotel services and invalid type for name 'float', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",1.23,"Monster Truck Show") == ("error","Invalid service : Monster Truck Show, Monster Truck Show not one of the hotel services and invalid type for name 'float', name must be string")
def test_check_guest_access_wrong_name_type_set_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv",set(),"pool") == ("error","Invalid type for name : 'set', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",set(),"gym") == ("error","Invalid type for name : 'set', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",set(),"dining") == ("error","Invalid type for name : 'set', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",set(),"sauna") == ("error","Invalid type for name : 'set', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",set(),"massage") == ("error","Invalid type for name : 'set', name must be string")
def test_check_guest_access_wrong_name_type_set_and_incorrect_service():
    assert check_guest_access("guest_list_for_testing.csv",set(),"skydiving") == ("error","Invalid service : skydiving, skydiving not one of the hotel services and invalid type for name 'set', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",set(),"Monster Truck Show") == ("error","Invalid service : Monster Truck Show, Monster Truck Show not one of the hotel services and invalid type for name 'set', name must be string")
def test_check_guest_access_wrong_name_type_boolean_true_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv",True,"pool") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",True,"gym") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",True,"dining") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",True,"sauna") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",True,"massage") == ("error","Invalid type for name : 'bool', name must be string")
def test_check_guest_access_wrong_name_type_boolean_true_and_incorrect_service():
    assert check_guest_access("guest_list_for_testing.csv",True,"skydiving") == ("error","Invalid service : skydiving, skydiving not one of the hotel services and invalid type for name 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",True,"Monster Truck Show") == ("error","Invalid service : Monster Truck Show, Monster Truck Show not one of the hotel services and invalid type for name 'bool', name must be string")
def test_check_guest_access_wrong_name_type_boolean_false_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv",False,"pool") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",False,"gym") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",False,"dining") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",False,"sauna") == ("error","Invalid type for name : 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",False,"massage") == ("error","Invalid type for name : 'bool', name must be string")
def test_check_guest_access_wrong_name_type_boolean_false_and_incorrect_service():
    assert check_guest_access("guest_list_for_testing.csv",False,"skydiving") == ("error","Invalid service : skydiving, skydiving not one of the hotel services and invalid type for name 'bool', name must be string")
    assert check_guest_access("guest_list_for_testing.csv",False,"Monster Truck Show") == ("error","Invalid service : Monster Truck Show, Monster Truck Show not one of the hotel services and invalid type for name 'bool', name must be string")

def test_check_guest_access_correct_name_and_wrong_service_type_list():
    assert check_guest_access("guest_list_for_testing.csv","alex",[]) == ("error","Invalid type for service : 'list', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," Alex",[]) == ("error","Invalid type for service : 'list', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","aLEx ",[]) == ("error","Invalid type for service : 'list', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," ALEX ",[]) == ("error","Invalid type for service : 'list', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","tomas",[]) == ("error","Invalid type for service : 'list', service must be string")
def test_check_guest_access_incorrect_name_and_wrong_service_type_list():
    assert check_guest_access("guest_list_for_testing.csv","cat",[]) == ("error","Invalid name : Cat, Cat not a hotel guest and invalid type for service 'list', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","",[]) == ("error","Invalid name : ,  not a hotel guest and invalid type for service 'list', service must be string")
def test_check_guest_access_correct_name_and_wrong_service_type_dictionary():
    assert check_guest_access("guest_list_for_testing.csv","alex",{}) == ("error","Invalid type for service : 'dict', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," Alex",{}) == ("error","Invalid type for service : 'dict', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","aLEx ",{}) == ("error","Invalid type for service : 'dict', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," ALEX ",{}) == ("error","Invalid type for service : 'dict', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","tomas",{}) == ("error","Invalid type for service : 'dict', service must be string")
def test_check_guest_access_incorrect_name_and_wrong_service_type_dictionary():
    assert check_guest_access("guest_list_for_testing.csv","cat",{}) == ("error","Invalid name : Cat, Cat not a hotel guest and invalid type for service 'dict', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","",{}) == ("error","Invalid name : ,  not a hotel guest and invalid type for service 'dict', service must be string")
def test_check_guest_access_correct_name_and_wrong_service_type_float():
    assert check_guest_access("guest_list_for_testing.csv","alex",1.23) == ("error","Invalid type for service : 'float', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," Alex",1.23) == ("error","Invalid type for service : 'float', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","aLEx ",1.23) == ("error","Invalid type for service : 'float', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," ALEX ",1.23) == ("error","Invalid type for service : 'float', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","tomas",1.23) == ("error","Invalid type for service : 'float', service must be string")
def test_check_guest_access_incorrect_name_and_wrong_service_type_float():
    assert check_guest_access("guest_list_for_testing.csv","cat",1.23) == ("error","Invalid name : Cat, Cat not a hotel guest and invalid type for service 'float', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","",1.23) == ("error","Invalid name : ,  not a hotel guest and invalid type for service 'float', service must be string")
def test_check_guest_access_correct_name_and_wrong_service_type_set():
    assert check_guest_access("guest_list_for_testing.csv","alex",set()) == ("error","Invalid type for service : 'set', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," Alex",set()) == ("error","Invalid type for service : 'set', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","aLEx ",set()) == ("error","Invalid type for service : 'set', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," ALEX ",set()) == ("error","Invalid type for service : 'set', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","tomas",set()) == ("error","Invalid type for service : 'set', service must be string")
def test_check_guest_access_incorrect_name_and_wrong_service_type_set():
    assert check_guest_access("guest_list_for_testing.csv","cat",set()) == ("error","Invalid name : Cat, Cat not a hotel guest and invalid type for service 'set', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","",set()) == ("error","Invalid name : ,  not a hotel guest and invalid type for service 'set', service must be string")
def test_check_guest_access_correct_name_and_wrong_service_type_boolean_true():
    assert check_guest_access("guest_list_for_testing.csv","alex",True) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," Alex",True) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","aLEx ",True) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," ALEX ",True) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","tomas",True) == ("error","Invalid type for service : 'bool', service must be string")
def test_check_guest_access_incorrect_name_and_wrong_service_type_boolean_true():
    assert check_guest_access("guest_list_for_testing.csv","cat",True) == ("error","Invalid name : Cat, Cat not a hotel guest and invalid type for service 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","",True) == ("error","Invalid name : ,  not a hotel guest and invalid type for service 'bool', service must be string")
def test_check_guest_access_correct_name_and_wrong_service_type_boolean_false():
    assert check_guest_access("guest_list_for_testing.csv","alex",False) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," Alex",False) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","aLEx ",False) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv"," ALEX ",False) == ("error","Invalid type for service : 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","tomas",False) == ("error","Invalid type for service : 'bool', service must be string")
def test_check_guest_access_incorrect_name_and_wrong_service_type_boolean_false():
    assert check_guest_access("guest_list_for_testing.csv","cat",False) == ("error","Invalid name : Cat, Cat not a hotel guest and invalid type for service 'bool', service must be string")
    assert check_guest_access("guest_list_for_testing.csv","",False) == ("error","Invalid name : ,  not a hotel guest and invalid type for service 'bool', service must be string")

def test_check_guest_access_incorrect_guests_list_type_list():
    assert check_guest_access([],"tomas","pool") == ("error",f"Invalid type for guests_list : 'list', guests_list must be string")
def test_check_guest_access_incorrect_guests_list_type_dictionary():
    assert check_guest_access({},"tomas","pool") == ("error",f"Invalid type for guests_list : 'dict', guests_list must be string")
def test_check_guest_access_incorrect_guests_list_type_float():
    assert check_guest_access(4.242,"tomas","pool") == ("error",f"Invalid type for guests_list : 'float', guests_list must be string")
    assert check_guest_access(-4.242,"tomas","pool") == ("error",f"Invalid type for guests_list : 'float', guests_list must be string")
    assert check_guest_access(0.000000,"tomas","pool") == ("error",f"Invalid type for guests_list : 'float', guests_list must be string")
def test_check_guest_access_incorrect_guests_list_type_integer():
    assert check_guest_access(3,"tomas","pool") == ("error",f"Invalid type for guests_list : 'int', guests_list must be string")
    assert check_guest_access(-3,"tomas","pool") == ("error",f"Invalid type for guests_list : 'int', guests_list must be string")
    assert check_guest_access(0,"tomas","pool") == ("error",f"Invalid type for guests_list : 'int', guests_list must be string")
def test_check_guest_access_incorrect_guests_list_type_set():
    assert check_guest_access(set(),"tomas","pool") == ("error",f"Invalid type for guests_list : 'set', guests_list must be string")
def test_check_guest_access_incorrect_guests_list_type_boolean_true():
    assert check_guest_access(True,"tomas","pool") == ("error",f"Invalid type for guests_list : 'bool', guests_list must be string")
def test_check_guest_access_incorrect_guests_list_type_boolean_false():
    assert check_guest_access(False,"tomas","pool") == ("error",f"Invalid type for guests_list : 'bool', guests_list must be string")

def test_check_guest_access_wrong_name_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv","wrong name","pool") == ("error","\nincorrect guest name : Wrong Name")
    assert check_guest_access("guest_list_for_testing.csv","not a name","gym") == ("error","\nincorrect guest name : Not A Name")
    assert check_guest_access("guest_list_for_testing.csv","INCORRECT NAME","dining") == ("error","\nincorrect guest name : Incorrect Name")
    assert check_guest_access("guest_list_for_testing.csv","just name","sauna") == ("error","\nincorrect guest name : Just Name")
    assert check_guest_access("guest_list_for_testing.csv","wrong","massage") ==("error","\nincorrect guest name : Wrong")
def test_check_guest_access_correct_name_and_wrong_service():
    assert check_guest_access("guest_list_for_testing.csv","alex","wrong service") == ("error","\nincorrect service name : wrong service")
    assert check_guest_access("guest_list_for_testing.csv","  Alex  ","not a service") == ("error","\nincorrect service name : not a service")
    assert check_guest_access("guest_list_for_testing.csv"," aLEx","INCORRECT SERVICE") == ("error","\nincorrect service name : incorrect service")
    assert check_guest_access("guest_list_for_testing.csv","ALEX","just service") == ("error","\nincorrect service name : just service")
    assert check_guest_access("guest_list_for_testing.csv","tomas","wrong") == ("error","\nincorrect service name : wrong")
def test_check_guest_access_wrong_name_and_wrong_service():
    assert check_guest_access("guest_list_for_testing.csv","wrong name","wrong service") == ("error","\nincorrect guest and service name : Wrong Name, wrong service")
    assert check_guest_access("guest_list_for_testing.csv","not a name","not a service") == ("error","\nincorrect guest and service name : Not A Name, not a service")
    assert check_guest_access("guest_list_for_testing.csv","INCORRECT NAME","INCORRECT SERVICE") == ("error","\nincorrect guest and service name : Incorrect Name, incorrect service")
    assert check_guest_access("guest_list_for_testing.csv","just name","just service") == ("error","\nincorrect guest and service name : Just Name, just service")
    assert check_guest_access("guest_list_for_testing.csv","wrong","wrong") == ("error","\nincorrect guest and service name : Wrong, wrong")
def test_check_guest_access_none_name_and_correct_service():
    assert check_guest_access("guest_list_for_testing.csv","","pool") == ("error","\nincorrect guest name : None")
    assert check_guest_access("guest_list_for_testing.csv","     ","gym") == ("error","\nincorrect guest name : None")
    assert check_guest_access("guest_list_for_testing.csv","","dining") == ("error","\nincorrect guest name : None")
    assert check_guest_access("guest_list_for_testing.csv"," ","sauna") == ("error","\nincorrect guest name : None")
    assert check_guest_access("guest_list_for_testing.csv","","massage") == ("error","\nincorrect guest name : None")
def test_check_guest_access_correct_name_and_none_service():
    assert check_guest_access("guest_list_for_testing.csv","alex","") == ("error","\nincorrect service name : None")
    assert check_guest_access("guest_list_for_testing.csv","  Alex  ","   ") == ("error","\nincorrect service name : None")
    assert check_guest_access("guest_list_for_testing.csv"," aLEx","") == ("error","\nincorrect service name : None")
    assert check_guest_access("guest_list_for_testing.csv","ALEX"," ") == ("error","\nincorrect service name : None")
    assert check_guest_access("guest_list_for_testing.csv","tomas","") == ("error","\nincorrect service name : None")
def test_check_guest_access_none_name_and_none_service():
    assert check_guest_access("guest_list_for_testing.csv","","") == ("error","\nincorrect guest and service name : None")
    assert check_guest_access("guest_list_for_testing.csv","      ","      ") == ("error","\nincorrect guest and service name : None")
    assert check_guest_access("guest_list_for_testing.csv"," "," ") == ("error","\nincorrect guest and service name : None")
def test_check_guest_access_none_name_and_wrong_service():
    assert check_guest_access("guest_list_for_testing.csv","","wrong service") == ("error","\nincorrect guest and service name : None, wrong service")
    assert check_guest_access("guest_list_for_testing.csv","      ","not a service") == ("error","\nincorrect guest and service name : None, not a service")
    assert check_guest_access("guest_list_for_testing.csv","","INCORRECT SERVICE") == ("error","\nincorrect guest and service name : None, incorrect service")
    assert check_guest_access("guest_list_for_testing.csv"," ","just service") == ("error","\nincorrect guest and service name : None, just service")
    assert check_guest_access("guest_list_for_testing.csv","","wrong") == ("error","\nincorrect guest and service name : None, wrong")
def test_check_guest_access_wrong_name_and_none_service():
    assert check_guest_access("guest_list_for_testing.csv","wrong name","") == ("error","\nincorrect guest and service name : Wrong Name, None")
    assert check_guest_access("guest_list_for_testing.csv","not a name","      ") == ("error","\nincorrect guest and service name : Not A Name, None")
    assert check_guest_access("guest_list_for_testing.csv","INCORRECT NAME","") == ("error","\nincorrect guest and service name : Incorrect Name, None")
    assert check_guest_access("guest_list_for_testing.csv","just name"," ") == ("error","\nincorrect guest and service name : Just Name, None")
    assert check_guest_access("guest_list_for_testing.csv","wrong","") == ("error","\nincorrect guest and service name : Wrong, None")

def test_check_guest_access_normal():
    assert check_guest_access("guest_list_for_testing.csv","peter","pool") == ("denied","\naccess denied, normal package which Peter bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv","  Peter  ","gym") == ("denied","\naccess denied, normal package which Peter bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv","PETER  ","dining") == ("denied","\naccess denied, normal package which Peter bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv"," PeTeR ","sauna") == ("denied","\naccess denied, normal package which Peter bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv","Peter","massage") == ("denied","\naccess denied, normal package which Peter bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv","alex","pool") == ("denied","\naccess denied, normal package which Alex bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv"," Alex  ","gym") == ("denied","\naccess denied, normal package which Alex bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv"," ALEX","dining") == ("denied","\naccess denied, normal package which Alex bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv"," aLEX ","sauna") == ("denied","\naccess denied, normal package which Alex bought dont include any service")
    assert check_guest_access("guest_list_for_testing.csv","Alex","massage") == ("denied","\naccess denied, normal package which Alex bought dont include any service")
def test_check_guest_access_premium():
    assert check_guest_access("guest_list_for_testing.csv","robert","pool") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","  Robert  ","gym") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","ROBERT  ","dining") == ("denied","\naccess denied, premium package which Robert bought dont include dining")
    assert check_guest_access("guest_list_for_testing.csv"," RoBeRT ","sauna") == ("denied","\naccess denied, premium package which Robert bought dont include sauna")
    assert check_guest_access("guest_list_for_testing.csv","Robert","massage") == ("denied","\naccess denied, premium package which Robert bought dont include massage")
def test_check_guest_access_luxury():
    assert check_guest_access("guest_list_for_testing.csv","scott","pool") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","  Scott  ","gym") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","SCOTT  ","dining") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv"," ScOTT ","sauna") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","Scott","massage") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","tomas","pool") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","  Tomas  ","gym") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","TOMAS  ","dining") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv"," tOMAs ","sauna") == ("granted","\naccess granted")
    assert check_guest_access("guest_list_for_testing.csv","Tomas","massage") == ("granted","\naccess granted")


def test_make_guest_data_not_correct_data_string():
    assert make_guest_data("not correct data","not correct data","not correct data","not correct data","not correct data","not correct data") == None
def test_make_guest_data_nothing():
    assert make_guest_data("","","","","","") == None
def test_make_guest_data_whitespaces():
    assert make_guest_data("    "," "," "," "," "," ") == None
def test_make_guest_data_list():
    assert make_guest_data([],[],[],[],[],[]) == None
def test_make_guest_data_dictionary():
    assert make_guest_data({},{},{},{},{},{}) == None
def test_make_guest_data_float():
    assert make_guest_data(3.453,-14.34,0.000,45.151,151.515,-1551.51) == None
def test_make_guest_data_integer():
    assert make_guest_data(3,-14,0,45,151,-1551) == None
def test_make_guest_data_set():
    assert make_guest_data(set(),set(),set(),set(),set(),set()) == None
def test_make_guest_data_boolean_true():
    assert make_guest_data(True,True,True,True,True,True) == None
def test_make_guest_data_boolean_false():
    assert make_guest_data(False,False,False,False,False,False) == None

def test_make_guest_data_correct1():
    assert make_guest_data("brave guest","1","0"," normal","1","1") == {"name": "Brave Guest", "adult": 1, "kid": 0, "package": "normal", "night": 1, "room": 1}
def test_make_guest_data_correct2():
    assert make_guest_data("Moody guest","2","0","premium ","2","6") == {"name": "Moody Guest", "adult": 2, "kid": 0, "package": "premium", "night": 2, "room": 6}
def test_make_guest_data_correct3():
    assert make_guest_data("smart Guest","2","1"," Luxury ","3","5") == {"name": "Smart Guest", "adult": 2, "kid": 1, "package": "luxury", "night": 3, "room": 5}
def test_make_guest_data_correct4():
    assert make_guest_data("Picky Guest","2","2","normal","4","23") == {"name": "Picky Guest", "adult": 2, "kid": 2, "package": "normal", "night": 4, "room": 23}
def test_make_guest_data_correct5():
    assert make_guest_data(" Techguru Guest ","3","4"," prEmiUm ","6","123") == {"name": "Techguru Guest", "adult": 3, "kid": 4, "package": "premium", "night": 6, "room": 123}