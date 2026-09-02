#Please enter name:

from datetime import datetime
prompt = ""
PrePrompt = input("Please enter prompt:")
for i in range(len(PrePrompt)):
    letter = PrePrompt[i]
    letter = letter.lower()
    prompt += letter
if prompt.__contains__("hello"):
    print("Hi there, how are you?")
elif prompt.__contains__("name"):
    print("My name is ExamBot, how can I help?")
elif prompt.__contains__("time"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
elif prompt.__contains__("weather"):
    print("it is always sunny in Ireland")
else:
    print("I am sorry, I do not know that one")
