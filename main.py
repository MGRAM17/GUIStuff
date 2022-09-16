import guizero

app = guizero.App(title="This is my first GUI!")

message = guizero.Text(app, text="GUIs are cool", color="red")
secondMessage = guizero.Text(app, text="BIGGER TEXT", size=50, color="white", bg="black")

app.display()