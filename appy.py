from flask import Flask, render_template, request
import pygal

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("home.html")


@app.route("/belugagraph", methods=['GET'])
def belugagraph():
	line_out_data = []
	line_chart = pygal.Line()
	line_chart.title = "Adidas Yeezy Boost 350 V2 Beluga"
	line_chart.x_labels = ['Time']
	line_chart.y_labels = ['$']
	hilcsv = open("beluga.csv", "r")
	mega = hilcsv.read()
	hell = mega.split("\n")
	listme = []
	hell.pop(0)
	for i in hell:
		i = i.split(',')
		try:
			listme.append(float(i[0]))
		except ValueError:
			print('hi')
	line_chart.add("Shoe", listme)
	line_chart_data = line_chart.render_data_uri()
	line_out_data.append(line_chart_data)
	return render_template("belugagraph.html", line_out_data=line_out_data)

@app.route("/boostgraph", methods=['GET'])
def boostgraph():
	line_out_data = []
	line_chart = pygal.Line()
	line_chart.title = "Adidas Ultra Boost 4.0 Triple Black"
	line_chart.x_labels = ['Time']
	line_chart.y_labels = ['$']
	hilcsv = open("boost.csv", "r")
	mega = hilcsv.read()
	hell = mega.split("\n")
	listme = []
	hell.pop(0)
	for i in hell:
		i = i.split(',')
		try:
			listme.append(float(i[0]))
		except ValueError:
			print('hi')
	line_chart.add("Shoe", listme)
	line_chart_data = line_chart.render_data_uri()
	line_out_data.append(line_chart_data)
	return render_template("boostgraph.html", line_out_data=line_out_data)

@app.route("/hilfiggraph", methods=['GET'])
def hilgiggraph():
    line_out_data = []
    line_chart = pygal.Line()
    line_chart.title = "Tommy Hilfiger X Kith"
    line_chart.x_labels = ['Time']
    line_chart.y_labels = ['$']
    hilcsv = open("hilfig.csv", "r")
    mega = hilcsv.read()
    hell = mega.split("\n")
    listme = []
    hell.pop(0)
    for i in hell:
        i = i.split(',')
        try:
            listme.append(float(i[0]))
        except ValueError:
            print('hi')
    line_chart.add("Shirt", listme )
    line_chart_data = line_chart.render_data_uri()
    line_out_data.append(line_chart_data)
    return render_template("hilfiggraph.html", line_out_data = line_out_data)

@app.route("/kithgraph", methods=['GET'])
def kithgraph():
	line_out_data = []
	line_chart = pygal.Line()
	line_chart.title = "Kith Tie Dye Box Logo Tee Blue"
	line_chart.x_labels = ['Time']
	line_chart.y_labels = ['$']
	hilcsv = open("kith.csv", "r")
	mega = hilcsv.read()
	hell = mega.split("\n")
	listme = []
	hell.pop(0)
	for i in hell:
		i = i.split(',')
		try:
			listme.append(float(i[0]))
		except ValueError:
			print('hi')
	line_chart.add("Shirt", listme)
	line_chart_data = line_chart.render_data_uri()
	line_out_data.append(line_chart_data)
	return render_template("kithgraph.html", line_out_data=line_out_data)


@app.route("/conversegraph", methods=['GET'])
def conversegraph():
	line_out_data = []
	line_chart = pygal.Line()
	line_chart.title = "Converse Chuck Taylor All-Star 70s Hi Off-White"
	line_chart.x_labels = ['Time']
	line_chart.y_labels = ['$']
	hilcsv = open("chucktay.csv", "r")
	mega = hilcsv.read()
	hell = mega.split("\n")
	listme = []
	hell.pop(0)
	for i in hell:
		i = i.split(',')
		try:
			listme.append(float(i[0]))
		except ValueError:
			print('hi')
	line_chart.add("Shoe", listme)
	line_chart_data = line_chart.render_data_uri()
	line_out_data.append(line_chart_data)
	return render_template("conversegraph.html", line_out_data=line_out_data)


if __name__ == "__main__":
	app.debug = True
	app.run()
