import os

for filename in os.listdir("3_static/"):
	os.rename("3_static/"+filename, "3_static/"+filename[:4]+".gif")