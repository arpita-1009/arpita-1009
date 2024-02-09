from flask import *
import utm
import time
import simplekml
import random
app = Flask(__name__)

@app.route("/" , methods = ['POST','GET'])
def index(): 
    if request.method == 'POST':   
        zone = request.form.get("zone")
        counter = request.form.get("counter")
        num = int(counter)
        list = []
        for i in range(0,num):
            print("lat"+str(i))
            lat = request.form.get("lat"+str(i))
            long = request.form.get("long"+str(i))
            longlat1 = lat , long
            list.append(longlat1)
        print(list)
        """use of postman
        json_data = request.get_json()
        vert = json_data.get("count")
        a =json_data.get("latlong")
        zone = json_data.get('zone')
        b = str(a).strip(' ').split(',')
        list = []
        for i in range(0,len(b),2):
            str1 = b[i],b[i+1]
            list.append(str1)
        print(list)
        """
        latlong = []
        for l in range(0,int(counter)):
            v1 = float(list[l][0])
            v2 = float(list[l][1])
            lat1, long1 = utm.to_latlon(v1,v2, int(zone), northern=True)
            longlat1 = long1 , lat1
            latlong.append(longlat1)
        latlong.append(latlong[0])
        print(latlong,"5")
        kml = simplekml.Kml()
        lin = kml.newlinestring(name="Pathway", description="A pathway in MH",coords=latlong)
        lin.style.linestyle.color = 'ff0000ff'
        lin.style.linestyle.width= 2

        num1 = random.uniform(5, 10)
        path = 'static/'
        path_kml = f'{path}/{num1}.kml'
        kml.save(f"{path}/{num1}.kml")
        output = {"latlog":latlong}
        # from selenium import webdriver 
        # url = 'file:///Users/arpita_patel/Documents/GitHub/bhunaksha/templates/plot.html'
        # driver = webdriver.Chrome()
        # driver.get(url)
        # driver.maximize_window()
        # time.sleep(3)
        # elem = driver.find_element_by_class_name("gm-style-moc")
        # elem.screenshot(f"{path}/{num1}.png")
        # path_jpg  = f'{path}/{num1}.png'
        return render_template('plot.html',output = output , path_kml = path_kml ,)

    return render_template("test1.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)
