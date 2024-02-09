
from flask import *
import importlib , os , uuid 
from datetime import date, timedelta
import shutil
from werkzeug.utils import secure_filename
from flask import Flask, send_file
from logging.config import dictConfig
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'custom_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': r'C:\1_All_Websites\1_All_Python_Sites\py.proplegit.com\logs/mylog1.log'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'custom_handler']
    }
})
app = Flask(__name__)
mappings = {
    'Karnawati ClubMake Excel': ("karnawati", "karna_wati"),
    'EB5 GCCIMake Excel':("gcci","convert"),
    'EB5 GDMAMake Excel':("GDMA_main","convert"),
    'InvoiceMake Excel':('invoice','in_def'),
    'GDMA_MOMake Excel':('get_mobile','excel_no'),
    'GoaRuralMake Excel':('Goa_ws','excel'),
    'PunjabRuralMake Excel': ('punj_ws', 'excel'),
    "Himachal PradeshRuralMake Excel": ('himachal_ws', 'excel'),
    'HaryanaRuralMake Excel': ('harya_ws', 'excel'),
    'ChhattisgarhRuralMake Excel': ('chhattis_ws', 'excel'),
    'Andhra PradeshRuralMake Excel': ('ap_ws', 'excel'),
    'Andhra PradeshUrbanMake Excel':('andrapradesh_urban', 'andrapradesh'),
    'GujaratUrbanMake Excel':('gujarat_urban', 'gujarat'),
    'MadhyaPradeshUrbanMake Excel':('madhyapradesh_urban', 'madhyapradesh'),
    'TamilNaduUrbanMake Excel':('tamilnadu_urban', 'tamilnadu'),
    'TelanganaUrbanMake Excel':('telangana_urban', 'telangana'),
    'TelanganacdmaUrbanMake Excel':('telanganacdma_urban', 'telanganacdma'),

}
@app.route('/', methods=['GET', 'POST'])
def home():
    # try:
        if request.method == "POST":
            format_1 = request.form.get("Format")
            type = request.form.get("type")
            if format_1=="MasterData":
                print("master")
                state= request.form.get("State")
                area= request.form.get("Area")
                print(state, area)
                pyfile, func= mappings[state + area + type ]
                module= importlib.util.find_spec(pyfile, package=None)
                m= module.loader.load_module()
                today=date.today()
                path= f"static/{today}/{state}_{area}.xlsx"
                print(path)
                return render_template('download.html',path=path)
            else:
                print(format_1 , type)
                pyfile, func= mappings[format_1 + type]
                module = importlib.util.find_spec(pyfile, package=None)
                m = module.loader.load_module()
                function = getattr(m, func)
                pdf = function()
                print(pdf)
                path1 = pdf[0].partition('static')
                path = path1[1]+path1[2]            
                return render_template('download.html',path=path)
        return render_template('index.html')
    # except Exception as e:
    #     return("Woops,Page Not Found, that page doesnot exist on your path!")

def get_date():
    r_filename = str(uuid.uuid4())
    format_1 = request.form.get("Format")
    if format_1 == "Karnawati Club":
        name = r_filename+"/Karnawati Club"
    if format_1 == "EB5 GCCI":
        name = r_filename+"/EB5 GCCI"
    if format_1 == "EB5 GDMA":
        name = r_filename+"/EB5 GDMA"
    if format_1 == "Invoice":
        name = r_filename+"/invoice"
    today = date.today()
    print("Today's date:", today)
    yesterday_date = date.today() - timedelta(1)
    shutil.rmtree('static/'+str(yesterday_date),ignore_errors=True)
    """________________"""
    pa_th = os.path.join(os.getcwd(),'static',str(today) , name)
    os.makedirs(pa_th, exist_ok=True)
    file = request.files['file_1']
    file_name = secure_filename(file.filename)
    file.save(os.path.join(pa_th,file_name))
    filepath = os.path.join(pa_th,file_name)
    return [filepath]

@app.route("/delete_file", methods=['POST'])
def delete():
    if request.method == "POST":
        print("delete")
        today = date.today()
        delete_fol=os.path.join(os.getcwd(),'static', str(today))
        from os.path import exists
        dele_exist=exists(delete_fol)
        if dele_exist==True:
            shutil.rmtree(delete_fol)
        return redirect('/')
#####
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)