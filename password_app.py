import guizero 

app = guizero.App(title="Password app")

def button_press():
    if password1.value != password2.value:
        guizero.info("Password error", "Your passwords do not match")
        password1.value = ""
        password2.value = ""
        return 
    guizero.info(title="Success", text="Passwords match")

guizero.Text(app, text="Password Checker tool!!!!", size=30, color="red")

guizero.Picture(app, image="download.png")

guizero.Text(app, text="Enter your password")
password1 = guizero.TextBox(app)

guizero.Text(app, text="Enter your password again")
password2 = guizero.TextBox(app)

guizero.PushButton(app, command=button_press, text="Submit passwords")

app.display()