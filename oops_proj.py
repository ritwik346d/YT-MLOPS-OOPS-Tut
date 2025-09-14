class chatbook:
    def __init__(self):
        self.__name   = "Default User"
        self.user_id = 0
        self.user_id += 1 
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

def get_name(self):
    return self.__name

def set_name(self, value):
    self.__name = value

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like t proceed?" 
                     1. Press 1 to signup
                     2. Press 2 to login
                     3. Press 3 to write a post
                     4. Press 4 to message a friend
                     5. Press any other key to exit""")
        
        if user_input == '1':
           self.signup()
           pass
        elif user_input == '2':
           self.signin()
        elif user_input == '3':
           self.my_post() 
        elif user_input == '4':
           self.sendmsg()
        else:
            exit() 

    def signup(self):
        email = input("enter your email here -> ")      
        pwd = input("setup your password here -> ")  
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please sign up first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("enter your password here -> ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input corrext credentials")   
            print("\n")
            self.menu() 

    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to sign in first to post something...")
            print("\n")
            self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            friend = input("Enter your friend's email/username here -> ")
            msg = input("Enter your message here -> ")
            print(f"Following message has been sent to {friend} -> {msg}")
        else:
            print("You need to sign in first to send a message...")
            print("\n")
            self.menu()                   



    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? ->  ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to sign in first to post something...")
            print("\n")
            self.menu()

#user1 = chatbook()
