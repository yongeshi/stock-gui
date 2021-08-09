eel.py_function("what up")

eel.expose(js_function)
function js_function(x) {
    console.log("eyy {}".replace("{}", x))
}
