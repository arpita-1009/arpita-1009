from flask import *
import importlib

app = Flask(__name__)

mappings = {
    'Desktop1': ("desktoppage", "desktop"),
    'Mobile2':("mobilepage","mobile"),
}

@app.route('/url', methods=['POST'])
def pdf():
    type = request.form.get("type")
    if type == "Desktop":
        num = "1"
    else:
        num = "2" 
    print(type , num) 
    pyfile, func= mappings[type  + num]
    module = importlib.util.find_spec(pyfile, package=None)
    m = module.loader.load_module()
    function = getattr(m, func)
    pdf = function()
    return render_template('pdfsave.html', pdf=pdf , type = type)
    
def upload_file():
    url = request.form['url']
    return url

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return("Woops,Page Not Found, that page doesnot exist on your path!")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
    