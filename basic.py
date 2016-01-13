from flask import Flask, request, jsonify
app = Flask(__name__, static_url_path='/static') # This just defines our "app"

todo = [] # The list of items "to do"

@app.route("/") # App routes tell flask which function to call when you request a page in your browser
def root():
    return app.send_static_file('index.html')

@app.route("/add", methods=["POST"])
def add():
    todo.append(request.get_json(force=True)) # Add to the list from the browser request
    return "Added an item"

@app.route("/remove", methods=["POST"])
def remove():
    todo.remove(request.get_json(force=True)) # Remove from the list 
    return "Removed an item"

@app.route("/show")
def show():
    return jsonify(items=todo) # Convert the list into something the browser can interpret

if __name__ == "__main__":
    app.run()
