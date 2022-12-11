import matplotlib.pyplot as plt
import os
import csv

base_dir = os.path.join(os.getcwd(), "graph-data")

figures_folder = os.path.join(os.getcwd(), "figures")

####
## Bar/column graph that depicts the average compound sentiment for year range
####
def fig1():
    # open the csv file
    with open(os.path.join(base_dir, "compound.csv"), "r") as f:
        csv_data = csv.reader(f, delimiter=',', quotechar='"')

        title = "Average compound sentiment score for each year range"

        for row in csv_data:
            if csv_data.line_num == 62:
                _2010_2014 = float(row[5])
                _2015_2017 = float(row[6])
                _2018_2020 = float(row[7])
                _2021_on   = float(row[8])

                labels = ["2010-2014", "2015-2017", "2018-2020", "2021-present"]

                plt.figure(figsize=(7,5))
                data = [_2010_2014, _2015_2017, _2018_2020, _2021_on]

                plt.bar(labels, data, width=0.3, color="red")

                plt.xlabel("Year Ranges")
                plt.ylabel("Average Compound Sentiment Score")
                plt.ylim(top=0.8)
                plt.title(title)
                plt.savefig(os.path.join(figures_folder, f"{title}.png"))


####
## Bar/column graph that depicts the average positive sentiment for year range
####
def fig2():
    # open the csv file
    with open(os.path.join(base_dir, "positive.csv"), "r") as f:
        csv_data = csv.reader(f, delimiter=',', quotechar='"')

        title = "Average positive sentiment score for each year range"
        for row in csv_data:
            if csv_data.line_num == 62:
                _2010_2014 = float(row[5])
                _2015_2017 = float(row[6])
                _2018_2020 = float(row[7])
                _2021_on   = float(row[8])

                labels = ["2010-2014", "2015-2017", "2018-2020", "2021-present"]

                plt.figure(figsize=(7,5))
                data = [_2010_2014, _2015_2017, _2018_2020, _2021_on]

                plt.bar(labels, data, width=0.3, color="orange")

                plt.xlabel("Year Ranges")
                plt.ylabel("Average Positive Sentiment Score")
                plt.ylim(top=0.8)
                plt.title(title)
                plt.savefig(os.path.join(figures_folder, f"{title}.png"))


####
## Bar/column graph that depicts the average negative sentiment for year range
####
def fig3():
    # open the csv file
    with open(os.path.join(base_dir, "negative.csv"), "r") as f:
        csv_data = csv.reader(f, delimiter=',', quotechar='"')

        title = "Average negative sentiment score for each year range"
        for row in csv_data:
            if csv_data.line_num == 62:
                _2010_2014 = float(row[5])
                _2015_2017 = float(row[6])
                _2018_2020 = float(row[7])
                _2021_on   = float(row[8])

                labels = ["2010-2014", "2015-2017", "2018-2020", "2021-present"]

                plt.figure(figsize=(7,5))
                data = [_2010_2014, _2015_2017, _2018_2020, _2021_on]

                plt.bar(labels, data, width=0.3, color="green")

                plt.xlabel("Year Ranges")
                plt.ylabel("Average Negative Sentiment Score")
                plt.ylim(top=0.8)
                
                plt.title(title)
                plt.savefig(os.path.join(figures_folder, f"{title}.png"))


####
## Bar/column graph that depicts the average neutral sentiment for year range
####
def fig4():
    # open the csv file
    with open(os.path.join(base_dir, "neutral.csv"), "r") as f:
        csv_data = csv.reader(f, delimiter=',', quotechar='"')
        
        title = "Average neutral sentiment score for each year range"
        for row in csv_data:
            if csv_data.line_num == 62:
                _2010_2014 = float(row[5])
                _2015_2017 = float(row[6])
                _2018_2020 = float(row[7])
                _2021_on   = float(row[8])

                labels = ["2010-2014", "2015-2017", "2018-2020", "2021-present"]

                plt.figure(figsize=(7,5))
                data = [_2010_2014, _2015_2017, _2018_2020, _2021_on]

                plt.bar(labels, data, width=0.3, color="blue")

                plt.xlabel("Year Ranges")
                plt.ylabel("Average Neutral Sentiment Score")
                plt.ylim(top=0.8)
                plt.title(title)
                plt.savefig(os.path.join(figures_folder, f"{title}.png"))

####
# Bar/column graph that depicts the Difference in Average
#   Compound Score between Adjacent Year Ranges
####
def fig5():
    # open the csv file
    with open(os.path.join(base_dir, "compound.csv"), "r") as f:
        csv_data = csv.reader(f, delimiter=',', quotechar='"')

        title = "Difference in average compound sentiment score between adjacent year ranges"
        for row in csv_data:
            if csv_data.line_num == 62:
                _2010_2014 = float(row[9])
                _2015_2017 = float(row[10])
                _2018_2020 = float(row[11])

                labels = ["2010-2014 / 2015-2017", "2015-2017 / 2018-2020", "2018-2020/2021-present"]

                plt.figure(figsize=(7,5))
                data = [_2010_2014, _2015_2017, _2018_2020]

                plt.bar(labels, data, width=0.3, color="purple")

                plt.xlabel("Year Ranges")
                plt.ylabel("Difference in Average Compound Sentiment Score")
                plt.ylim(top=0.1, bottom=-0.1)
                plt.title(title)
                plt.savefig(os.path.join(figures_folder, f"{title}.png"))


####
# Graph that depicts the Mean Difference in Average
#   Compound Score between Adjacent Years,
#   Separated by Classification Change 
####
def fig6():
    # open the csv file
    with open(os.path.join(base_dir, "compound.csv"), "r") as f:
        csv_data = csv.reader(f, delimiter=',', quotechar='"')

        for row in csv_data:
            if csv_data.line_num == 62:
                _2010_2014 = float(row[5])
                _2015_2017 = float(row[6])
                _2018_2020 = float(row[7])
                _2021_on   = float(row[8])

                labels = ["2010-2014", "2015-2017", "2018-2020", "2021-present"]

                plt.figure(figsize=(7,5))
                data = [_2010_2014, _2015_2017, _2018_2020, _2021_on]

                plt.bar(labels, data, width=0.3)

                plt.xlabel("Year Ranges")
                plt.ylabel("")
                plt.ylim(top=0.8)
                plt.title("")
                plt.savefig(os.path.join(figures_folder, "fig6.png"))


fig1()
fig2()
fig3()
fig4()
fig5()
