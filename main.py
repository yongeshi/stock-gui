import eel

eel.init("static")

@eel.expose
def py_function(x):
    print(f"sup {x}")

eel.js_function("brrr")

eel.start("index.html", size=(200, 150))