S = input().strip()

def chat_room(S):
    count=0
    for i in S:
        if count==0 and i=="h":
            count=1
        elif count==1 and i=="e":
            count=2
        elif count==2 and i=="l":
            count=3
        elif count==3 and i=="l":
            count=4
        elif count==4 and i=="o":
            return "YES"
    return "NO"

print(chat_room(S))
