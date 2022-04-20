from dhooks import Webhook
import readchar

Password = input("Enter Files Password: ")
RealPassword = "Y4cwZKuNDD97PL"
if(Password == RealPassword):
    try:
        hook = Webhook(input("Please Enter webhook link: "))
    except Exception:
        print("somethink is wrong, please try again")
        print("Press Any Key To Exit")
        k = readchar.readchar()
    try:
        text = input("Enter text: ")
        times = input("Enter times you want to send this message: ")
    except Exception:
        print("somethink is wrong, please try again")
        print("Press Any Key To Exit")
        k = readchar.readchar()
    else:
        for val in range(int(times)):
            hook.send(text)
else:
    print("Password is wrong")
    print("Press Any Key To Exit")
    k = readchar.readchar()