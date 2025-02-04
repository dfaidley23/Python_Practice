waiting_list = ["jon", "ben", "bill"]
waiting_list.sort()

for i, w in enumerate(waiting_list):
    waiting = f"{i + 1}.{w.capitalize()}"
    print(waiting)