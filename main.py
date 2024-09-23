import datetime

def print_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"The current local time is: {current_time}")
print_time()

# def print_day_of_week():
#     current_day = datetime.datetime.now().strftime("%A")
#     print(f"Today is: {current_day}")
# print_day_of_week()
