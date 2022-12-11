"""
Generates comment files from the school-lists directory using the data available in the database.
"""
from dbf import DatabaseFunctions
import os

dbf = DatabaseFunctions()


# list the out directory
for file in os.listdir("school-lists"):
    # the filename for later
    basename = file.split(".")[0].strip()
    # open the file
    with open(os.path.join('school-lists', file), "r", encoding="latin2") as f:
        lines = f.readlines()
    for line in lines:
        # school id
        sid = line.split("\t")[0]
        # school name
        name = line.split("\t")[1].replace("\n", "")
        
        # print(basename, name)
        # make directories
        if not os.path.exists('comments'):
            os.mkdir('comments')
        if not os.path.exists(os.path.join('comments', basename)):
            os.mkdir(os.path.join('comments', basename))
        if not os.path.exists(os.path.join('comments', basename, name)):
            os.mkdir(os.path.join('comments', basename, name))

        # holding comments for different date ranges
        comments_2005_2009 = []
        comments_2010_2014 = []
        comments_2015_2017 = []
        comments_2018_2020 = []
        comments_2021_onward = []


        ratings = dbf.get_school_ratings(int(sid))
        # for each rating
        for rating in ratings:
            comment = rating[15].replace("&quot;",'"').replace("&lt;", "<").replace("&gt;",">")
            # filter out nonsense
            if (comment.lower() == 'not specified.'
                or comment.lower() == 'none.'
                or comment.lower() == 'n/a'
                or comment == ':)'
                or comment.lower() == 'n.a'
                or comment == '.'
                or comment.lower() == "none"):
                continue
            # time to filter out year ranges wooo yeah exciting
            year = rating[2].year
            # 2005-2009
            if year >= 2005 and year <= 2009:
                comments_2005_2009.append(comment + "\n")
            # 2010-2014
            elif year >= 2010 and year <= 2014:
                comments_2010_2014.append(comment + "\n")
            # 2015-2017
            elif year >= 2015 and year <= 2017:
                comments_2015_2017.append(comment + "\n")
            # 2018-2020
            elif year >= 2018 and year <= 2020:
                comments_2018_2020.append(comment + "\n")
            # 2021+
            elif year >= 2021:
                comments_2021_onward.append(comment + "\n")

        base_file_dir = os.path.join('comments', basename, name)

        with open(os.path.join(base_file_dir, "2005_2009.txt"), "w") as g:
            g.writelines(comments_2005_2009)
        
        with open(os.path.join(base_file_dir, "2010_2014.txt"), "w") as g:
            g.writelines(comments_2010_2014)
        
        with open(os.path.join(base_file_dir, "2015_2017.txt"), "w") as g:
            g.writelines(comments_2015_2017)
        
        with open(os.path.join(base_file_dir, "2018_2020.txt"), "w") as g:
            g.writelines(comments_2018_2020)
        
        with open(os.path.join(base_file_dir, "2021_onward.txt"), "w") as g:
            g.writelines(comments_2021_onward)




