import numpy as np
import pandas as pd
import PyPDF2 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
filename = 'NLP.pdf' 
#open allows you to read the binary file
pdfFileObj = open(filename,'rb')
#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
# To check if the doc is a scanned PDF or not
if text != "":
   text = text
# import this library so as to split the data as per our requirements i.e only alphabets   
import re   
words= re.sub('[^a-zA-Z]',' ',text)
words = words.lower()
words = words.split()
key_words = [word for word in words if not word in set(stopwords.words('english'))]
df = pd.DataFrame(key_words)
imp_words = (df[0].value_counts())
finalize = imp_words[:499]

# FINALISE is the top 500 words. However at the end there are a number of 1's that can't be differenticated on the basis of repetitive importance

