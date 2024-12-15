from CrocoBot3 import history, user_ids

def view_history(user):
    print(user.username + ' - history')
    for i in history[user_ids[user]]:
        print(i.message.text)