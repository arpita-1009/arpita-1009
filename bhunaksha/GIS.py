
# import utm
# vert = 4
# zone = 43

# a  = "719995.45032 , 2341252.05111, 719990.58156 , 2341206.31953, 720102.46426 , 2341183.07976, 720121.69282 , 2341289.73417"
# b = a.strip(' ').split(',')
# list = []
# for i in range(0,len(b),2):

#     str1 = b[i],b[i+1]
#     list.append(str1)

# print(list)

# latlong = []
# for l in range(0,int(vert)):
#     v1 = float(list[l][0])
#     v2 = float(list[l][1])
#     lat1, long1 = utm.to_latlon(v1,v2, zone, northern=True)
#     longlat1 = long1 , lat1
#     latlong.append(longlat1)



# latlong.append(latlong[0])
# print(latlong)


latlong =[('77.16928' ,'31.80324'), ('77.16953','31.8032'),('77.16933','31.80324'), ('77.16957','31.80322'),('77.16958' ,'31.80322'),(' 77.16961' ,'31.80324'),('77.1693' ,'31.80324'),('77.16953' ,'31.80321'),('77.16928' ,'31.80324')]
import simplekml
kml = simplekml.Kml()
lin = kml.newlinestring(name="Pathway", description="A pathway in MH",coords=latlong)
lin.style.linestyle.color = 'ff0000ff'
lin.style.linestyle.width= 2
path = 'static/'
kml.save(f"{path}Plot.kml")


# 720121.00486 , 2341289.44560
# 720102.46887 , 2341733.24527
# 719990.59871 , 2341206.14267
# 719995.17819 , 2342852.37362


# import utm
# vert = input("Enter Total Vertices:")
# zone = int(input("Enter zone :"))
# for l in range(0,int(vert)):
#     for i in range(0,1):
#         v1 = float(input("Enter Value v1:"))
#         v2 = float(input("Enter value v2:"))
#         lat, long = utm.to_latlon(v1,v2, zone, northern=True)
#         print(lat,long)

# import simplekml
# kml = simplekml.Kml()
# for k in range(0,2*int(vert)+2):
#     lat = float(input("Enter value lat:"))
#     long = float(input("Enter value long:"))
# lin = kml.newlinestring(name="Pathway", description="A pathway in MH",coords=[(float(lat)),(float(long))])

# lin.style.linestyle.color = 'ff0000ff' # COLOR - Red

# lin.style.linestyle.width= 2 # Line Width

# kml.save(f"Plot.kml")

