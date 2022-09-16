import guizero 

app = guizero.App(title="My second GUI!")

def button_event(message_type=1):

    def event_changed():
        if message_type == 1:
            guizero.info("Greetings", f"Hello, {name_input.value}, you like {like_input.value}")
        elif message_type == 2:
            guizero.info("Greetings", f"Hi, your name is {name_input.value} and you like {like_input.value}")
    
    return event_changed

guizero.Text(app, text="Enter your name below")
name_input = guizero.TextBox(app)

guizero.Text(app, "Add something you like!")
like_input = guizero.TextBox(app)

button = guizero.PushButton(app, command=button_event(1), text="Greet")
button2 = guizero.PushButton(app, command=button_event(2), text="Alternate Greeting")


app.display()