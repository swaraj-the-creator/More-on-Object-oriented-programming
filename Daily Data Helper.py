class DayMese:
    def __init__(self):
        self.message = ""
    def get_message(self):
        self.message = input("Enter today's message: ")
    def print_message(self):
        print("Message in uppercase:", self.message.upper())
daily_text = DayMese()
daily_text.get_message()
daily_text.print_message()
class HrSn:
    def __init__(self):
        print("Daily Data Helper session created")
    def __del__(self):
        print("Daily Data Helper session ended")
def create_session():
    print("Making helper session...")
    session = HrSn()
    print("Session is ready,")
    return session
print("")
session_obj = create_session()
class PairFer:
 
    def find_pair(self, numbers, target):
        lookup = {}
        for index, number in enumerate(numbers):
            needed_number = target - number
 
            if needed_number in lookup:
                return (lookup[needed_number], index)
 
            lookup[number] = index
 
        return None

numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,747,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,1010,2010,30100,400011,50000011,510,401,9001,2300)
i = 0
while i < 999999:
    try: 
        target_value = int(input("Enter target sum to search: "))
 
        result = PairFer().find_pair(numbers, target_value)
 
        if result is not None:
            print(" %d + %d + 2 = {}".format(target_value)  % result)
            break
        else:
            print("No matching pair found.")
    except ValueError:
        target_value = "########## "
        print(f"{target_value} is an inappropriate VALUUUUE!!! for computer!")
del session_obj
print("Program End")
