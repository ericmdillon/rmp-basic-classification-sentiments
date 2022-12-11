from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Class that handles all sentiment analysis 
class Sentiment_Score():

    #initializing the sentiment analzyer that is used to analyze every comment
    sid_obj = SentimentIntensityAnalyzer()

    def __init__(self, sentence:str) -> None:
        self.sentiment_dict:dict = self.sid_obj.polarity_scores(sentence)
        self.negative = self.negative_sentiment()
        self.positive = self.positive_sentiment()
        self.neutral = self.neutral_sentiment()
        self.compound = self.compound_sentiment()
        return

    #Used to evaluate the sentiment of a singular comment for testing purposes. Not used for the multi file processing. 
    def sentiment_scores(self, sentence):
        sentiment_dict:dict = self.sid_obj.polarity_scores(sentence)
        
        print("Overall sentiment dictionary is : ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
        print("Sentence Overall Rated As", end = " ")
    
        #Decides the sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05 :
            print("Positive")
    
        elif sentiment_dict['compound'] <= -0.05 :
            print("Negative")
    
        else :
            print("Neutral")
        return
    
    #Finds the negative sentiment score of the string passed to it and returns it as a float
    def negative_sentiment(self) -> float:
        return self.sentiment_dict['neg']

    #Finds the positive sentiment score of the string passed to it and returns it as a float
    def positive_sentiment(self) -> float:
        return self.sentiment_dict['pos']

    #Finds the neutral sentiment score of the string passed to it and returns it as a float
    def neutral_sentiment(self) -> float:
        return self.sentiment_dict['neu']

    #Finds the compound sentiment score of the string passed to it and returns it as a float
    def compound_sentiment(self) -> float:
        return self.sentiment_dict['compound']

    #ToString method for Sentiment class
    def __repr__(self) -> str:
        return f"Positive:{self.positive}, Negative:{self.negative}, Neutral:{self.neutral}"

# Driver code
if __name__ == "__main__" :

    #Running counter to see total amount of comments parsed through within a university
    total_comment_count = 0
    
    #First set of average sentiment scores for years 2010-2014
    average_positive1 = 0
    average_negative1 = 0
    average_neutral1 = 0
    average_compound1 = 0
    
    #Parses through first file for univeristy comments. From year 2010-2014
    file_path1 = r"C:\\comments\MastersSmall\Walla Walla University\2010_2014.txt"
    with open(file_path1, 'r', encoding='ISO-8859-1') as file:
        lines:list[str] = file.readlines()
        num_of_lines:int = len(lines)
        total_comment_count += num_of_lines

        for line in lines:
            #Clean line of any unnecessary characters
            line = line.strip()

            #Check for empty lines
            if not len(line) > 0:
                num_of_lines -= 1

            #Runs sentiment analysis on the line currently being read
            line_score = Sentiment_Score(line)
            print(line_score)

            #Tally all scores
            average_positive1 += line_score.positive
            average_negative1 += line_score.negative
            average_neutral1 += line_score.neutral         
            average_compound1 += line_score.compound

        #If there are zero reviews at all, default to 0 for all scores
        if num_of_lines == 0:
            average_positive1 = 0
            average_negative1 = 0
            average_neutral1 = 0
            average_compound1 = 0

        else:
            #Average out tallies
            average_positive1 = average_positive1 / num_of_lines
            average_negative1 = average_negative1 / num_of_lines
            average_neutral1 = average_neutral1 / num_of_lines
            average_compound1 = average_compound1 / num_of_lines
        
        #Adds all averaged scores to a list that will be used to print to the final output
        averages_2010_2014 =["Positive: ",str(average_positive1),"\n","Negative: ",str(average_negative1),"\n", "Neutral: ",str(average_neutral1),"\n", "Compound: ",str(average_compound1),"\n"]

        #Prints everything evaluated for testing purposes 
        print(f"For 2010-2014 -- Total Average Positive:{average_positive1}, Negative:{average_negative1}, Neutral:{average_neutral1}, Compound:{average_compound1}")
        print("-----------------",total_comment_count,"-----------------") 

    #Second set of average sentiment scores for years 2015-2017
    average_positive2 = 0
    average_negative2 = 0
    average_neutral2 = 0
    average_compound2 = 0

    #Parses through second file for univeristy comments. From year 2015-2017
    file_path2 = r"C:\\comments\MastersSmall\Walla Walla University\2015_2017.txt"
    with open(file_path2, 'r', encoding='ISO-8859-1') as file:
        lines:list[str] = file.readlines()
        num_of_lines:int = len(lines)
        total_comment_count += num_of_lines

        for line in lines:
            #Clean line of any unnecessary characters
            line = line.strip()

            #Check for empty lines
            if not len(line) > 0:
                num_of_lines -= 1

            #Runs sentiment analysis on the line currently being read
            line_score = Sentiment_Score(line)
            print(line_score)

            #Tally all scores
            average_positive2 += line_score.positive
            average_negative2 += line_score.negative
            average_neutral2 += line_score.neutral         
            average_compound2 += line_score.compound
        
        #If there are zero reviews at all, default to 0 for all scores
        if num_of_lines == 0:
            average_positive2 = 0
            average_negative2 = 0
            average_neutral2 = 0
            average_compound2 = 0

        else:
            #Average out tallies
            average_positive2 = average_positive2 / num_of_lines
            average_negative2 = average_negative2 / num_of_lines
            average_neutral2 = average_neutral2 / num_of_lines
            average_compound2 = average_compound2 / num_of_lines
        
        #Adds all averaged scores to a list that will be used to print to the final output
        averages_2015_2017 =["Positive: ",str(average_positive2),"\n","Negative: ",str(average_negative2),"\n", "Neutral: ",str(average_neutral2),"\n", "Compound: ",str(average_compound2),"\n"]

        #Prints everything evaluated for testing purposes 
        print(f"For 2015-2017 -- Total Average Positive:{average_positive2}, Negative:{average_negative2}, Neutral:{average_neutral2}, Compound:{average_compound2}")
        print("-----------------",total_comment_count,"-----------------")

    #Third set of average sentiment scores for years 2018-2020
    average_positive3 = 0
    average_negative3 = 0
    average_neutral3 = 0
    average_compound3 = 0

    #Parses through third file for univeristy comments. From year 2018-2020
    file_path3 = r"C:\\comments\MastersSmall\Walla Walla University\2018_2020.txt"
    with open(file_path3, 'r', encoding='ISO-8859-1') as file:
        lines:list[str] = file.readlines()
        num_of_lines:int = len(lines)
        total_comment_count += num_of_lines

        for line in lines:
            #Clean line of any unnecessary characters
            line = line.strip()

            #Check for empty lines
            if not len(line) > 0:
                num_of_lines -= 1

            #Runs sentiment analysis on the line currently being read
            line_score = Sentiment_Score(line)
            print(line_score)

            #Tally all scores
            average_positive3 += line_score.positive
            average_negative3 += line_score.negative
            average_neutral3 += line_score.neutral         
            average_compound3 += line_score.compound
        
        #If there are zero reviews at all, default to 0 for all scores
        if num_of_lines == 0:
            average_positive3 = 0
            average_negative3 = 0
            average_neutral3 = 0
            average_compound3 = 0

        else:
            #Average out tallies
            average_positive3 = average_positive3 / num_of_lines
            average_negative3 = average_negative3 / num_of_lines
            average_neutral3 = average_neutral3 / num_of_lines
            average_compound3 = average_compound3 / num_of_lines

        #Adds all averaged scores to a list that will be used to print to the final output
        averages_2018_2020 =["Positive: ",str(average_positive3),"\n","Negative: ",str(average_negative3),"\n", "Neutral: ",str(average_neutral3),"\n", "Compound: ",str(average_compound3),"\n"]

        #Prints everything evaluated for testing purposes
        print(f"For 2018-2020 -- Total Average Positive:{average_positive3}, Negative:{average_negative3}, Neutral:{average_neutral3}, Compound:{average_compound3}")
        print("-----------------",total_comment_count,"-----------------")

    #Fourth set of average sentiment scores for years 2021+
    average_positive4 = 0
    average_negative4 = 0
    average_neutral4 = 0
    average_compound4 = 0

    #Parses through fourth file for univeristy comments. From year 2021+
    file_path4 = r"C:\\comments\MastersSmall\Walla Walla University\2021_onward.txt"
    with open(file_path4, 'r', encoding='ISO-8859-1') as file:
        lines:list[str] = file.readlines()
        num_of_lines:int = len(lines)
        total_comment_count += num_of_lines

        for line in lines:
            #Clean line of any unnecessary characters
            line = line.strip()

            #Check for empty lines
            if not len(line) > 0:
                num_of_lines -= 1

            #Runs sentiment analysis on the line currently being read
            line_score = Sentiment_Score(line)
            print(line_score)

            #Tally all scores
            average_positive4 += line_score.positive
            average_negative4 += line_score.negative
            average_neutral4 += line_score.neutral         
            average_compound4 += line_score.compound
        
        #If there are zero reviews at all, default to 0 for all scores
        if num_of_lines == 0:
            average_positive4 = 0
            average_negative4 = 0
            average_neutral4 = 0
            average_compound4 = 0

        else:
            #Average out tallies
            average_positive4 = average_positive4 / num_of_lines
            average_negative4 = average_negative4 / num_of_lines
            average_neutral4 = average_neutral4 / num_of_lines
            average_compound4 = average_compound4 / num_of_lines
        
        #Adds all averaged scores to a list that will be used to print to the final output
        averages_2021_onward = ["Positive: ",str(average_positive4),"\n","Negative: ",str(average_negative4),"\n", "Neutral: ",str(average_neutral4),"\n", "Compound: ",str(average_compound4),"\n"]

        #Prints everything evaluated for testing purposes
        print(f"For 2021 and onward -- Total Average Positive:{average_positive4}, Negative:{average_negative4}, Neutral:{average_neutral4}, Compound:{average_compound4}")
        print("-----------------",total_comment_count,"-----------------")

    #Tallies up the average sentiments of ALL reviews over all time
    univ_avg_pos = (average_positive1 + average_positive2 + average_positive3 + average_positive4) / 4
    univ_avg_neg = (average_negative1 + average_negative2 + average_negative3 + average_negative4) / 4
    univ_avg_neu = (average_neutral1 + average_neutral2 + average_neutral3 + average_neutral4) / 4
    univ_avg_comp = (average_compound1 + average_compound2 + average_compound3 + average_compound4) / 4
    univ_total_avg = ["Positive: ",str(univ_avg_pos),"\n","Negative: ",str(univ_avg_neg),"\n", "Neutral: ",str(univ_avg_neu),"\n", "Compound: ",str(univ_avg_comp),"\n"]

    #Writes the output file
    output_file = r"C:\\comments\MastersSmall\Walla Walla University\All_Averages.txt"
    with open(output_file, 'w', encoding='ISO-8859-1') as file:
        #Writes the 4 different averaged sentiment scores from 2010-2014
        file.write("Averages for 2010-2014: \n")
        file.writelines(averages_2010_2014)
        file.write("********\n")

        #Writes the 4 different averaged sentiment scores from 2015-2017
        file.write("Averages for 2015-2017: \n")
        file.writelines(averages_2015_2017)
        file.write("********\n")

        #Writes the 4 different averaged sentiment scores from 2018-2020
        file.write("Averages for 2018-2020: \n")
        file.writelines(averages_2018_2020)
        file.write("********\n")

        #Writes the 4 different averaged sentiment scores from 2021 and onward
        file.write("Averages for 2021 and onward: \n")
        file.writelines(averages_2021_onward)
        file.write("********\n")

        #Writes the 4 different averaged sentiment scores for the university over all time
        file.write("Averages for university over all time: \n")
        file.writelines(univ_total_avg)
        file.write("********\n")

        #Writes the total number of reviews analyzed over all time
        file.write("Total number of reviews analyzed: ")
        file.write(str(total_comment_count))

        file.close()


    
