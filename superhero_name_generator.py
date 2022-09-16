import guizero 

def make_event():
    output.value = f"You are.. The {adjective.value.title()} {colour.value.title()} {animal.value.title()}"

app = guizero.App(title="Superhero Name Generator")
guizero.Text(app, text="Superhero Name Generator!", size=50)

guizero.Text(app, text="Input an adjective")
adjective = guizero.ButtonGroup(app, options=["Amazing", "Cool", "Epic", "Insane"])

guizero.Text(app, text="Input a colour")
colour = guizero.TextBox(app)

guizero.Text(app, text="Input an animal")
animal = guizero.Combo(app, options=sorted(["Cat", "Dog", "Dolphin", "Elephant", "Ant"]))

make_name = guizero.PushButton(app, text="Make me a superhero", command=make_event)

output = guizero.Text(app, text="")

app.display()