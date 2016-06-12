import csv 
import math
from stop_words import get_stop_words

stop_words = get_stop_words('english')

category_d = {}
wordscategory_d = {}	

def train (category,text): 
	each_word(text,category)
	increment_cat(category)

def each_word(text,category):

	words = text.lower().split() 

	if not category in wordscategory_d:
		wordscategory_d[category] = {}

	for word in words:
		if not word in stop_words:
			if not word in wordscategory_d[category]:
				wordscategory_d[category][word] = 1
			else:
				wordscategory_d[category][word] += 1	

def increment_cat(category):
	if not category in category_d:
		category_d[category] = 1
	else:
		category_d[category] += 1	

def classify (text):
	print("Classifying: ", text)
	for category in category_d:
		words = text.lower().split() 
		text_probability = 0
		for word in words:
			if not word in stop_words:
				if word in wordscategory_d[category]:
					text_probability = text_probability + math.log((wordscategory_d[category][word]+1)/number_word_category[category])
				else:
					text_probability = text_probability + math.log(1 / number_word_category[category])
		print (category, -text_probability - math.log(category_d[category]/total_category))


categories = ["Setup : Positive","Setup : Negative","Stablity: Good","Stability : Poor", "Performance : Fast","Performance : Slow","Coverage : Good","Coverage : Bad"]
# categories = ["Animal","Color"]
with open('Training_Set.csv',encoding='latin1') as trainingfile:
	reader = csv.DictReader(trainingfile)
	for row in reader:
		text = row["Text"]
		for category in categories:
			if row[category] == "1":
				train(category,text); 

total_category = 0

for category in category_d:
	total_category = total_category + category_d[category]

number_word_category = {}

for category in wordscategory_d:
	if not category in number_word_category:
		number_word_category[category] = 0 	
	for word in wordscategory_d[category]:
		number_word_category[category] = number_word_category[category] + wordscategory_d[category][word]

print (number_word_category)

def classify (text):
	print("Classifying: ", text)
	for category in category_d:
		words = text.lower().split() 
		text_probability = 0
		for word in words:
			if not word in stop_words:
				if word in wordscategory_d[category]:
					text_probability = text_probability + math.log((wordscategory_d[category][word]+1)/number_word_category[category])
				else:
					text_probability = text_probability + math.log(1 / number_word_category[category])
		print (category, text_probability - math.log(category_d[category]/total_category))

print(classify("i have 8 access points covering a 3300 sqft house, with two outbuildings, and the throughput is drastically slower than my asus ac system (2 aps)."))
