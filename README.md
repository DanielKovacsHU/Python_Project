




# Hotel Management System
## [![Hotel Management System](<img width="1024" height="576" alt="hms" src="https://github.com/user-attachments/assets/bf6cb027-2671-490f-933a-cc2e1b0526d5" />
)](https://github.com/user-attachments/assets/90280530-19e4-4121-add1-2e62498eac24)   





# Introduction
Welcome, in the introduction I explain what’s my [CS50P](https://pll.harvard.edu/course/cs50s-introduction-programming-python) final project is, the original use case and some do and don’t-s.

## Idea
My original idea is that I create a “simple” add-remove system for hotel management with some additional features like a function that simulate a sort of electric barrier gate at the front of certain services like pools, saunas or at gym door.
I tried to find a balance between short/compactness and how well functions can be imported.

## Usecase
The program is designed to be used similar to the following:

The receptionist login to the computer and waiting for the guests.
If a new client arrives, after asking a couple of questions, like if they have any room preference or which package would they like, they will be in the hotels system after paying. Now they can access any service of the hotel that’s been paid for.

If a guest can’t access any of their paid services, that they can ask the receptionist to check why they got denied. With a function that is designed for this, after asking for the name, the program shows all the saved data of the specified guest, they can check if the mistake is made on the hotel’s or client’s side.

Before leaving the receptionist asks the clients for their name, if the name is correct (actual guest not a made-up name), they can leave without anything further to do.

## Do's and Don'ts
There are couple things to keep in mind when using the program:
It’s my first more complex project so it will be far from perfect, but I think for the average user, in this case a receptionist it’s get the job done. There could be a lot of further optimizations or features added in the future, feel free to modify it.

The program writes and reads from sensitive files in case of the hotel’s standpoint, maybe someone who has knowlede in cyber security can be asked to [encrypt](https://en.wikipedia.org/wiki/Encryption) those files to only be accessible if somebody knows the password to these files.

The program has one known flaw so it must be corrected first! If somebody access the computer files and add him/herself to  **hotel_guests_list.csv** and remove their room from  **empty_rooms_list.txt** after logout, then it’s almost impossible to detect the act, because the program will handle them as a regular guest. It can be countered by cameras, or another file where the paid user’s transaction ID is stored so it can be check if every user have paid, if not then alert the corresponding person who handle these situations.

Another safety tip is to logout every time the user leaves the computer so outsider can access the hotels system. Also it's a good idea to only use a freshly installed, licensed operating system with nothing else, but the required files running on the computer so it minimizes the remote attack surface.

The program shows error messages pretty user friendly if not imported, if it is, than a programmer will understand it quite well, if need more information than I recommend to check the Function part of this guide below.

# Functions

## Pre requirements to run the program
* from sys import exit
* from csv import DictReader, DictWriter
* install [termcolor](https://pypi.org/project/termcolor/)
* from termcolor import cprint
* login_password = "the hotels password goes here" (recommened a [strong password](https://security.harvard.edu/use-strong-passwords))
* hotel_room_limit = number of the hotel's room capacity (type integer)
* empty_rooms = []
* hotel_guests = []

## main() -> None:
It contains 2 parts: **Pre Login, After login**

### Pre login
The program welcomes the user and waiting for a password prompt
that formatted by str.strip() so whitespaces don’t cause problems.
If the password is incorrect an error message is shown. At the first 2 times
the user got another prompt if it is the third time the program exit
with sys.exit().

### After login
If the login was successful,  there is an infinite loop that has
3 functions:

**handle_empty_rooms()** and **handle_hotel_guests()** which as their
name says it handles the file that contain
the empty rooms (**empty_rooms_list.txt**) and hotel guests
(**hotel_guests_list.csv**). The third function is **choice()**, which is the second
biggest function after **main()**. It contains the remaining function that are not
listed here, also it’s the “heart” of the program.
There is also an error handling that shows a message to the user and exits the
program when a [Keyboard Interrupt](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt) is detected. Here it’s immediately exit
the program, because there is no need to ask if it was intentional or not, no
changes have made in the program and/or files.

## choice() -> None:
It has 3 main parts for different  situations:

1.  there is no empty room in
the hotel,
2. there is no guest in the hotel
3. in between the two

Let’s go through each of them.
### There is no empty room
This part starts with a conditional that checks if the number of the available
rooms are equal to zero, then the user needs to choose a function number, if it’s not correct she/he get
prompt again 2 more times before the program exit. If the function
number is correct than it jumps to one of the match-case  pairs.

#### Function 2
It meant to simulate a sort electric barrier gate system that only let through a guest if
she/he bought the package that contains the service. If a correct name and
service is given than it either shows a “granted” or “denied” message, if
3 times incorrect data is given than it returns to the function selecting menu

#### Function 3
This is part what’s meant to hopefully solving a problem by helping to decide,
when a guest cant access a service is either her/him that not bought a package
or it’s the hotel who has an error in their system. This part if a valid guest name
is given than it returns all of the recorded data. If 3 times invalid input is given
than the program goes back to the function menu

#### Function 4
If any guest wants to leave the hotel permanently first, they must be removed
from the hotels system. They gave their name to the receptionist who use this
function. It not only removes the guest from the guests list, but it also frees up
the room they stayed in. If 3 incorrect names are given, then the program goes
back to the main, function selecting menu

#### Function 5
If the user/receptionist want to leave the computer for a longer period of time, she/he must logout. This part is ensuring that there is no missing or excess room
and/or guest in the database. If 3 incorrect responses given to the logout
conformation or the response is no, then the program goes back to the main
menu.

In any match-cases, if any time a [Keyboard Interrupt](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt) is given, than the program asks
the user if it was intentional or not, if it was then it force quit without the logout
database check. If it wasn’t or 3 incorrect responses given, then the it goes
back to function menu.

### There is no hotel guest
It starts with the  same **function_tries** loop with some changes. It not only
has less function (2 instead of 4), but one of them is missing from the
no empty rooms loop. The reasons are the following: in the first big loop
there was no empty room, so there is no need for an **add_guest()**.
In the second big loop there is no guest, so we can’t check if a guest has
access to a service or not, what information does she/he has, we can’t
even remove them, so there is no need for these functions.

#### Function 1
This part has a variable **last_correct_data**, it’s propose is to update each
time if a correct response is given. The correctness of the response is
determined by the **check…()** functions. If all the responses are correct
which equal to **last_correct_data = “kid”**, then a dictionary of all the guest
data is created by **make_guest_data()**. If she/he paid than the program
adds her/him to the guests list, and remove the room she/he choose form
empty rooms list. If any time during the data collection 3 wrong inputs
is given for the same question or the guest not paid, then the program exits
back to the function choosing menu.

Every part that I not specifically mentioned in **no hotel guest** are exactly the
same as in the **no empty room** part, which also true for **in between** loop,
which is the combination of the two loop (excluding the similar parts). The program use the **in between loop** if there is at least 1 guest, but the hotel is not full and if there is at least one room available, but the hotel not empty.

## handle_empty_rooms() -> None:
This function is designed to read all the data in **empty_rooms_list.txt**
and filter those out that are not zero or positive integer. It starts by defining
a global variable **empty_rooms**. It needed to be global, because other
functions will need to use and modify it. Then program check if the line, striped from the “\n” newline is a decimal character or not. If it is, than its get added to
**empty_rooms_set** first to avoid room duplicates. After opening the file in
“write” mode to overwrite all the data, in a sorted loop each number
converted to a string to be able to write it to a file, then a “\n” newline is
added to each line's end so the next room written in a newline. The last line of
the function is making sure that empty_rooms is in an ascending order.

## handle_hotel_guests() -> None:
This  is one of the more complex function, so it’s better to split it to 3 big parts
based on filtering.

### Part 1
After opening **hotel_guests_list.csv** the first filter is only accepts guests that:
* not already in hotel_guests,
* the name is title cased,
* the number of adults is greater/equal to 1,
* the number of the kids is a non-negative whole number,
* the package they  bought is either “normal”, “premium” or “luxury”,
* the number of the night they stay is at least 1,
* their room number is not in empty_rooms.

Only if all conditional is met can a guest pass the first filter

### Part 2
It's name duplicate filter that is executed if a name in **hotel_guests_name** have
at least one duplicate. First the program lists all the guests who has been
registered under the same name with an “index” number (**number_of_the_guest**). Then it got stored inside a list **guest_with_number** as
a dictionary where the first value is the “index”, the second is the guest.

After that the program asks the user to choose which one is the
correct. If the response is a valid guests “index” (**number_of_the_guest**),
then the in a loop it checks which guests has that “index” and save it as
**correct_guest**. There is a while loop that has the function of deleting 1
duplicate guest form **hotel_guests** (has the same name, but not
**correct_guest**). It also removes 1 name-room pair from
**hotel_guests_name** and **hotel_guests_room** if:
* the name is correct, but the room is not same to **corret_guest**’s room.
* the name and room are equal to the correct **AND** there is at least 1 duplicate of the **correct_guest**s’s room.

The latter conditional is needed if there is more than one guest who has the same name and room, but some of its data is differ, for example the package she/he bought. Here is an example:

1st guest: name: Tom, package: normal, room: 10

2nd guest: name: Tom, package: premium, room: 10

They booth got stored as Tom/10 pair in **hotel_guests_name** and **hotel_guests_room**. The first conditional won’t do anything if the room is same as the **correct_guest**, so there will be remaining 2 pairs of Tom/10. In similar cases we can check if there is any duplicates of the correct name or room remaining (I choose room for no good reason). If name and room are correct (Tom/10) and there is more than 1 room duplicate (of 10), than it removes 1 Tom/10. In hotel_guests there is no need for this, if it's not the same what the user chooses, then it get removed.


If there is only one name-room pair left, the loop ends.

while it seems that it may sort out any guest at first glance, we need 1 additional part in case where there is at least 2 guests
with different name and same room in **hotel_guests_list.csv**.

### Part 3
The first loop starts if there is any room in **hotel_guests_room** that has at least 1 duplicate. If there is than as in **Part 2** all guests will be saved with an “index”
that has the same room as specified. Then the user got asked which is the
correct guest’s number/index. if a valid input has given, like in **Part 2**, the
correct guest got saved as **correct_guest**. The last while loop is similar, but
it not checks the number of name, but the number of room duplicates.
The loop removes 1 guest who has the same room as the specified duplicate
and not the **correct_guest** form **hotel_guests**. The other loop removes
1 name-room pair that has the same room as the **correct_guest**, but
the name is differ from it.

If 3 wrong inputs is given to any prompt during the last 2 filter or a [Keyboard Interrupt](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt) is raised, the program exit without any modification

Lastly the function opens **hotel_guests_list.csv** in “write” mode so only
the correct, filtered guests are remains in it.

## login(password_entered: str, actual_password: str) -> bool:
Very simple program, compares 2 string and if they match, return
True. In the login phase at main(), actual_password is at the top of the file, so it's very easy to modify it.

## check_room(room_list: str, room: str) -> str:
This function needs a **room_list** string, which is a file name where the rooms
are stored. The file needs to have only 1 number per line to function
properly. if the input **room** is in the list, it returns a “correct” string. Exception handling can changed if desired.

## check_name(guests_list: str, name: str) -> str:
It searches for the name that has given as input argument in the file
**guest_list**. If the file contains the name, it returns “correct”.

## check_package(package: str) -> str:
Check if the input argument **package** is either “normal”, “premium” or “luxury”. if it is than returns “correct”.

## check_night(night: str) -> str:
Return correct if **night** greater than 0.

## check_adult(adult: str) -> str:
If **adult** greater than 0, returns “correct”.

## check_kid(kid: str) -> str:
When the number of **kid** is at least 0, return “correct”

## make_guest_data(name: str, adult: str, kid: str, package: str, night: str, room: str) -> dict:
Returns a dictionary where each argument is formatted, so **name** is title cased, **adult, kid, night, room** is an integer and **package** is lower cased. Each of them is striped form whitespaces.

## get_price(adult: str, kid: str, package: str, night: str) -> int:
It calculate the price of the staying based on the arguments. Returns the price as integer.

## manage_room(mode: str,  room: int) -> None:
This function has 2 modes: "remove" and "add"

* In “remove” mode, it iterates over each room in **empty_rooms**, if the
actual room is equal to **room**, then it deletes it form the list. After then
it writes back the sorted and shortened **empty_rooms** to **empty_rooms_list.txt**.

* In “add” mode, the function just appends **room** to **empty_rooms**
and as in “remove” mode, writes the sorted and extended **empty_rooms** to
**empty_rooms_list.txt**.

## add_guest(guest: dict) -> None:
It appends **guest** to **hotel_guests**, then it write back the name sorted and
extended **hotel_guests** to **hotel_guests_list.csv**.

## check_guest_access(guests_list: str, name: str, service: str) -> tuple:
First the function check if **name** in **hotel_guests_name** and **service** is
in **luxury** (it has all the services). If booth is true, then in match-case
if the package is “normal”, the response is “denied” (it doesn’t include any
service), if it’s "premium" and the **service** is in the premium list, then
the access is “granted” else “denied”. In case of "luxury", it contains all the services so
the response is “granted” every time. If there is an error in either at
the **name** or at the **service**, the functions return “error” as the first part
of the tuple followed by a somewhat detailed message why the error
occurred.

## search_for_client(guests_list: str, name: str) -> tuple:
This function is simply check if **name** is in **hotel_guests_name**.
If it is then return a tuple with “correct” str at index 0 and a
format string at index 1, which has all of the data of a guest who's name is **name**. If it isn't in **hotel_guests_name**, return an error tuple.

## remove_guest(name: str) -> None:
If **name** is one of **hotel_guests** name, then the function deletes this guest.
After that, it writes back the sorted and shortened **hotel_guests** to
**hotel_guests_list.csv**.

## logout() -> None:
It has 3 different scenarios :

* if the sum of the guests and rooms are equal to hotel limit, then there
is no excess or missing data.

* if the sum is less than the limit, there are missing rooms or guests.

* If the sum is greater than the limit, there are excess rooms or guests in
the database.

# Final thoughts
## sources
* [python docmentations](https://docs.python.org/3/) for official informations about python, like functions, errors, i/o and so on
* [stack overflow](https://stackoverflow.com/) for common questions that occurred during programing
* [edx's CS50P's](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python) lectures and notes for everything else

## notes
* for a better user experience maximize the terminal window size

* some functions are lot harder to unit-test than others: those add or remove elements from file, so have no return value. Maybe someone more experienced can do test for those, but for me it’s outside of my capabilities.

* every **check_somethig** works the same, gets an input, decides if its correct, if it is than return "correct" else, return nothing. In case of any error, the message is in main/choice/function 1. The return value can be edited to show an error message with except SomethingError: return "this text", but for this programs use case its not necessary

* **handle_hotel_guests()** only accept and the program only adds title cased names, so if there is any name that’s not, it must be malicious (if the program not modified).


* for testing proposes please don’t change **guest_list_for_testing.csv** and **check_room_tester.txt**, they made only for testing proposes to demonstrate that if a file given than how the program will behave, if someone want to test different scenarios don’t forget, the assertions need to change too


* there is a couple of tests in the original idea of **logout()**, but because in my program there is no possible way to cause the problem listed, i can't test it and be sure that its working correctly without editing my program to be faulty on purpose, which is not in my intentions. These are what i think could happen before redo my program to sort these out:

  * there aren’t any  multiplied rooms in empty room or guests in hotel guests list
  * if there is a not normal empty room like: negative, zero, or not int type,
  * if there is a not complete guest in hotel guest list
  * if there is a guest with the same number as in empty rooms (room don’t get removed)
  * if the room get added, but guest still in list (guest not removed, same as room dint get removed)
  * if the guest removed, but the room not shown (room not added)
  * if there isn’t a guest with the removed room, but the room get removed (guest don’t get added)

* in choice/function 1 (add guest) there is no error checking for wrong file type for **guests_list** or **rooms_list** arguments, they are "hardcoded" in the program which works correctly, no need to check for errors there. If later needed it can be edited to return a value instead of a passing at exception handling in **check_name()** and **check_room()**







