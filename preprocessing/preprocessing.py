import pandas as pd

df = pd.read_csv('help_service_data.csv')

df = df[df['Name'].isnull()==False]

df = df.reset_index(drop = True)

for each in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Public Holidays']:
    df.at[53, each] = 'Check with the website'

Accommodation = ['Accommodation', 'Food']
health = ['Health Services / Pharmacy', 'Hospitals / Emergency']
essential = ['Clothes and Blankets', 'Showers / Laundry']
hotlines = ['Helpful website', 'Helpful phone number']
legal_fin = ['Legal / Financial Advice']
others = ['Drug and Alcohol', 'Needle Exchange', 'Counselling and Psychiatric Services', 'Employment Assistance',
        'Travel Assistance', 'Tenancy Assistance']

def clean(x):
    return x.replace('\n', ' ')

data = {}
df = df.fillna('Unknown')

def insert_acc(data, df):
    temp = []
    for i in range(len(df)):
        if df['Category 1'][i] in Accommodation or df['Category 2'][i] in Accommodation or df['Category 3'][i] in Accommodation or df['Category 4'][i] in Accommodation or df['Category 5'][i] in Accommodation:
                tmp = {}
                tmp['id_'] = i+1 #set unique id for each service
                tmp['Name'] = df['Name'][i]
                tmp['What'] = clean(df['What'][i])
                tmp['Who'] = clean(df['Who'][i])
                if df['Address 1'][i] != 'Unknown':
                    tmp['Address'] = df['Address 1'][i]
                elif df['Address 2'][i] != 'Unknown':
                    tmp['Address'] = df['Address 2'][i]
                else:
                    tmp['Address'] = 'Unknown'
                if df['Phone'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone'][i]
                elif df['Phone 2'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone 2'][i]
                else:
                    tmp['Phone'] = df['Free Call'][i]
                tmp['Email'] = df['Email'][i]
                tmp['Website'] = df['Website'][i]
                tmp['Longitude'] = df['Longitude'][i]
                tmp['Latitude'] = df['Latitude'][i]
                tmp['Geocoded Location'] = df['Geocoded Location'][i]
                tmp['Suburb'] = df['Suburb'][i]
                hours = {}
                if df['Monday'][i] != 'Unknown':
                    hours['Monday'] = df['Monday'][i]
                if df['Tuesday'][i] != 'Unknown':
                    hours['Tuesday'] = df['Tuesday'][i]
                if df['Wednesday'][i] != 'Unknown':
                    hours['Wednesday'] = df['Wednesday'][i]
                if df['Thursday'][i] != 'Unknown':
                    hours['Thursday'] = df['Thursday'][i]
                if df['Friday'][i] != 'Unknown':
                    hours['Friday'] = df['Friday'][i]  
                if df['Saturday'][i] != 'Unknown':
                    hours['Saturday'] = df['Saturday'][i]   
                if df['Sunday'][i] != 'Unknown':
                    hours['Sunday'] = df['Sunday'][i]    
                if df['Public Holidays'][i] != 'Unknown':
                    hours['Public Holidays'] = df['Public Holidays'][i]
                tmp['Opening Hours'] = hours
                temp.append(tmp)
    data = temp
    return data


def insert_health(data, df):
    temp = []
    for i in range(len(df)):
        if df['Category 1'][i] in health or df['Category 2'][i] in health or df['Category 3'][i] in health or df['Category 4'][i] in health or df['Category 5'][i] in health:
                tmp = {}
                tmp['id_'] = i+1 #set unique id for each service
                tmp['Name'] = df['Name'][i]
                tmp['What'] = clean(df['What'][i])
                tmp['Who'] = clean(df['Who'][i])
                if df['Address 1'][i] != 'Unknown':
                    tmp['Address'] = df['Address 1'][i]
                elif df['Address 2'][i] != 'Unknown':
                    tmp['Address'] = df['Address 2'][i]
                else:
                    tmp['Address'] = 'Unknown'
                if df['Phone'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone'][i]
                elif df['Phone 2'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone 2'][i]
                else:
                    tmp['Phone'] = df['Free Call'][i]
                tmp['Email'] = df['Email'][i]
                tmp['Website'] = df['Website'][i]
                tmp['Longitude'] = df['Longitude'][i]
                tmp['Latitude'] = df['Latitude'][i]
                tmp['Geocoded Location'] = df['Geocoded Location'][i]
                tmp['Suburb'] = df['Suburb'][i]
                hours = {}
                if df['Monday'][i] != 'Unknown':
                    hours['Monday'] = df['Monday'][i]
                if df['Tuesday'][i] != 'Unknown':
                    hours['Tuesday'] = df['Tuesday'][i]
                if df['Wednesday'][i] != 'Unknown':
                    hours['Wednesday'] = df['Wednesday'][i]
                if df['Thursday'][i] != 'Unknown':
                    hours['Thursday'] = df['Thursday'][i]
                if df['Friday'][i] != 'Unknown':
                    hours['Friday'] = df['Friday'][i]  
                if df['Saturday'][i] != 'Unknown':
                    hours['Saturday'] = df['Saturday'][i]   
                if df['Sunday'][i] != 'Unknown':
                    hours['Sunday'] = df['Sunday'][i]    
                if df['Public Holidays'][i] != 'Unknown':
                    hours['Public Holidays'] = df['Public Holidays'][i]
                tmp['Opening Hours'] = hours
                temp.append(tmp)
    data = temp
    return data


def insert_essential(data, df):
    temp = []
    for i in range(len(df)):
        if df['Category 1'][i] in essential or df['Category 2'][i] in essential or df['Category 3'][i] in essential or df['Category 4'][i] in essential or df['Category 5'][i] in essential:
                tmp = {}
                tmp['id_'] = i+1 #set unique id for each service
                tmp['Name'] = df['Name'][i]
                tmp['What'] = clean(df['What'][i])
                tmp['Who'] = clean(df['Who'][i])
                if df['Address 1'][i] != 'Unknown':
                    tmp['Address'] = df['Address 1'][i]
                elif df['Address 2'][i] != 'Unknown':
                    tmp['Address'] = df['Address 2'][i]
                else:
                    tmp['Address'] = 'Unknown'
                if df['Phone'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone'][i]
                elif df['Phone 2'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone 2'][i]
                else:
                    tmp['Phone'] = df['Free Call'][i]
                tmp['Email'] = df['Email'][i]
                tmp['Website'] = df['Website'][i]
                tmp['Longitude'] = df['Longitude'][i]
                tmp['Latitude'] = df['Latitude'][i]
                tmp['Geocoded Location'] = df['Geocoded Location'][i]
                tmp['Suburb'] = df['Suburb'][i]
                hours = {}
                if df['Monday'][i] != 'Unknown':
                    hours['Monday'] = df['Monday'][i]
                if df['Tuesday'][i] != 'Unknown':
                    hours['Tuesday'] = df['Tuesday'][i]
                if df['Wednesday'][i] != 'Unknown':
                    hours['Wednesday'] = df['Wednesday'][i]
                if df['Thursday'][i] != 'Unknown':
                    hours['Thursday'] = df['Thursday'][i]
                if df['Friday'][i] != 'Unknown':
                    hours['Friday'] = df['Friday'][i]  
                if df['Saturday'][i] != 'Unknown':
                    hours['Saturday'] = df['Saturday'][i]   
                if df['Sunday'][i] != 'Unknown':
                    hours['Sunday'] = df['Sunday'][i]    
                if df['Public Holidays'][i] != 'Unknown':
                    hours['Public Holidays'] = df['Public Holidays'][i]
                tmp['Opening Hours'] = hours
                temp.append(tmp)
    data = temp
    return data


def insert_legal_fin(data, df):
    temp = []
    for i in range(len(df)):
        if df['Category 1'][i] in legal_fin or df['Category 2'][i] in legal_fin or df['Category 3'][i] in legal_fin or df['Category 4'][i] in legal_fin or df['Category 5'][i] in legal_fin:
                tmp = {}
                tmp['id_'] = i+1
                tmp['Name'] = df['Name'][i]
                tmp['What'] = clean(df['What'][i])
                tmp['Who'] = clean(df['Who'][i])
                if df['Address 1'][i] != 'Unknown':
                    tmp['Address'] = df['Address 1'][i]
                elif df['Address 2'][i] != 'Unknown':
                    tmp['Address'] = df['Address 2'][i]
                else:
                    tmp['Address'] = 'Unknown'
                if df['Phone'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone'][i]
                elif df['Phone 2'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone 2'][i]
                else:
                    tmp['Phone'] = df['Free Call'][i]
                tmp['Email'] = df['Email'][i]
                tmp['Website'] = df['Website'][i]
                tmp['Longitude'] = df['Longitude'][i]
                tmp['Latitude'] = df['Latitude'][i]
                tmp['Geocoded Location'] = df['Geocoded Location'][i]
                tmp['Suburb'] = df['Suburb'][i]
                hours = {}
                if df['Monday'][i] != 'Unknown':
                    hours['Monday'] = df['Monday'][i]
                if df['Tuesday'][i] != 'Unknown':
                    hours['Tuesday'] = df['Tuesday'][i]
                if df['Wednesday'][i] != 'Unknown':
                    hours['Wednesday'] = df['Wednesday'][i]
                if df['Thursday'][i] != 'Unknown':
                    hours['Thursday'] = df['Thursday'][i]
                if df['Friday'][i] != 'Unknown':
                    hours['Friday'] = df['Friday'][i]  
                if df['Saturday'][i] != 'Unknown':
                    hours['Saturday'] = df['Saturday'][i]   
                if df['Sunday'][i] != 'Unknown':
                    hours['Sunday'] = df['Sunday'][i]    
                if df['Public Holidays'][i] != 'Unknown':
                    hours['Public Holidays'] = df['Public Holidays'][i]
                tmp['Opening Hours'] = hours
                temp.append(tmp)
    data = temp
    return data



def insert_hotlines(data, df):
    temp = []
    for i in range(len(df)):
        if df['Category 1'][i] in hotlines or df['Category 2'][i] in hotlines or df['Category 3'][i] in hotlines or df['Category 4'][i] in hotlines or df['Category 5'][i] in hotlines:
                tmp = {}
                tmp['id_'] = i+1
                tmp['Name'] = df['Name'][i]
                tmp['What'] = clean(df['What'][i])
                tmp['Who'] = clean(df['Who'][i])
                if df['Phone'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone'][i]
                elif df['Phone 2'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone 2'][i]
                else:
                    tmp['Phone'] = df['Free Call'][i]
                tmp['Email'] = df['Email'][i]
                tmp['Website'] = df['Website'][i]
                hours = {}
                if df['Monday'][i] != 'Unknown':
                    hours['Monday'] = df['Monday'][i]
                if df['Tuesday'][i] != 'Unknown':
                    hours['Tuesday'] = df['Tuesday'][i]
                if df['Wednesday'][i] != 'Unknown':
                    hours['Wednesday'] = df['Wednesday'][i]
                if df['Thursday'][i] != 'Unknown':
                    hours['Thursday'] = df['Thursday'][i]
                if df['Friday'][i] != 'Unknown':
                    hours['Friday'] = df['Friday'][i]  
                if df['Saturday'][i] != 'Unknown':
                    hours['Saturday'] = df['Saturday'][i]   
                if df['Sunday'][i] != 'Unknown':
                    hours['Sunday'] = df['Sunday'][i]    
                if df['Public Holidays'][i] != 'Unknown':
                    hours['Public Holidays'] = df['Public Holidays'][i]
                tmp['Opening Hours'] = hours
                temp.append(tmp)
    data = temp
    return data



def insert_others(data, df):
    temp = []
    for i in range(len(df)):
        if df['Category 1'][i] in others or df['Category 2'][i] in others or df['Category 3'][i] in others or df['Category 4'][i] in others or df['Category 5'][i] in others:
                tmp = {}
                tmp['id_'] = i+1 #set unique id for each service
                tmp['Name'] = df['Name'][i]
                tmp['What'] = clean(df['What'][i])
                tmp['Who'] = clean(df['Who'][i])
                if df['Address 1'][i] != 'Unknown':
                    tmp['Address'] = df['Address 1'][i]
                elif df['Address 2'][i] != 'Unknown':
                    tmp['Address'] = df['Address 2'][i]
                else:
                    tmp['Address'] = 'Unknown'
                if df['Phone'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone'][i]
                elif df['Phone 2'][i] != 'Unknown':
                    tmp['Phone'] = df['Phone 2'][i]
                else:
                    tmp['Phone'] = df['Free Call'][i]
                tmp['Email'] = df['Email'][i]
                tmp['Website'] = df['Website'][i]
                tmp['Longitude'] = df['Longitude'][i]
                tmp['Latitude'] = df['Latitude'][i]
                tmp['Geocoded Location'] = df['Geocoded Location'][i]
                tmp['Suburb'] = df['Suburb'][i]
                hours = {}
                if df['Monday'][i] != 'Unknown':
                    hours['Monday'] = df['Monday'][i]
                if df['Tuesday'][i] != 'Unknown':
                    hours['Tuesday'] = df['Tuesday'][i]
                if df['Wednesday'][i] != 'Unknown':
                    hours['Wednesday'] = df['Wednesday'][i]
                if df['Thursday'][i] != 'Unknown':
                    hours['Thursday'] = df['Thursday'][i]
                if df['Friday'][i] != 'Unknown':
                    hours['Friday'] = df['Friday'][i]  
                if df['Saturday'][i] != 'Unknown':
                    hours['Saturday'] = df['Saturday'][i]   
                if df['Sunday'][i] != 'Unknown':
                    hours['Sunday'] = df['Sunday'][i]    
                if df['Public Holidays'][i] != 'Unknown':
                    hours['Public Holidays'] = df['Public Holidays'][i]
                tmp['Opening Hours'] = hours
                temp.append(tmp)
    data = temp
    return data


data = {}
# data = insert_others(data,df)
nameList = ['accommodation', 'health', 'essential', 'legal', 'hotlines', 'others']
dtList = [data_acc, data_health, data_essential,  data_legal, data_hotlines, data_others]

for i in range(len(nameList)):
    data[nameList[i]] = dtList[i]

tmp = []
for key, value in data.items():
    for each in value:
        each['Type'] = key
        tmp.append(each)

for each in tmp:
    each['Rating'] = []

from pymongo import MongoClient

cloud = False

if cloud:
	uri = 'mongodb://lenomongo:kzUR8Q9x2b0CSbxp8A0lpVpXPIl07VEnwhCDlrKZLv7imd7Ik0B6O5tpZk6khUemBbDqH8OgdTaAxQxFdtrRdw==@lenomongo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
	client = MongoClient(uri)
	db = client.IE
	services = db.Services
	try:
    		services.insert_many(tmp)
	except Exception:
    		raise Exception("it is not json file")
        
	client.close()
else:
	client = MongoClient()
        db = client.IE
        services = db.Services
        try:
                services.insert_many(tmp)
        except Exception:
                raise Exception("it is not json file")

        client.close()

data = tmp.copy()

id_list = []
text_list = []

for document in data:
    key = str(document['_id'])
    try: 
        document['Address']
        value = document['Name']+' '+document['What']+' '+document['Who']+' '+document['Address']+' '+document['Suburb']+' '+document['Phone']
    except:
        value = document['Name']+' '+document['What']+' '+document['Who']+' '+document['Phone']
    id_list.append(key)
    text_list.append(value)


import re
import nltk

# create an array for replace some contractions
replace_patterns = [
('(A|a)in\'t', 'is not'),
('(C|c)an\'t', 'can not'),
('(H|h)ow\'s', 'how is'),
('(H|h)ow\'d', 'how did'), 
('(H|h)ow\'d\'y', 'how do you'),
('(H|h)ere\'s', 'here is'),
('(I|i)t\'s', 'it is'),
('(I|i)\'m', 'i am'),
('f(u\*|\*c)k', 'fuck'),    
('(L|l)et\'s', 'let us'),
('(M|m)a\'am', 'madam'),
('sh\*t', 'shit'),
('(S|s)han\'t', 'shall not'), 
('(S|s)ha\'n\'t', 'shall not'), 
('(S|s)o\'s', 'so as'),    
('(T|t)his\'s', 'this is'),
('(T|t)here\'s', 'there is'),
('(W|w)on\'t', 'will not'),
('(W|w)hat\'s', 'what is'),    
('(W|w)hatis', 'what is'),
('(W|w)hen\'s', 'when is'), 
('(W|w)here\'d', 'where did'), 
('(W|w)here\'s', 'where is'), 
('(W|w)ho\'s', 'who is'), 
('(W|w)hy\'s', 'why is'),     
('(Y|y)\'all', 'you all'), 
('o\'clock', 'of the clock'),
('\'cause', 'because'),  
('(\w+)\'ve', '\g<1> have'),
('(\w+)\'ll', '\g<1> will'),
('(\w+)n\'t', '\g<1> not'),
('(\w+)\'re', '\g<1> are'),
('(\w+)\'d', '\g<1> would')]
# function for clean contractions
def clean_contraction(x):    
    x = str(x)    
    for punct in "’‘":
        if punct in x:
            x = x.replace(punct, "'") 
    for pattern, repl in replace_patterns:
        if re.search(pattern,x):
            x = re.sub(pattern, repl, x)
    return x


# unify the expression of time
check_pm = re.compile(r'[0-9]+p[.]?m[.]?')
check_PM = re.compile(r'[0-9]+P[.]?M[.]?')
check_am = re.compile(r'[0-9]+a[.]?m[.]?')
check_AM = re.compile(r'[0-9]+A[.]?M$[.]?')
# write the function 
def fix_time(x):  
    x = str(x)
    if re.search(check_pm, x):
        x = re.sub('p.m', ' PM', x)
    if re.search(check_PM, x):
        x = re.sub('P.M', ' PM', x)
    if re.search(check_am, x):
        x = re.sub('a.m', ' AM', x)
    if re.search(check_AM, x):
        x = re.sub('A.M', ' AM', x)       
    return x



# fix duplication of letters
goood = re.compile(r'g+(o)\1{2,}(d)+') # replace gooodddd by good
check_duplicate = re.compile(r'\w*(\S)\1{2,}\w*') # replace words such as fantasticccccc by fantastic
# fix duplications and clean some puncs
def clean_punc(x):
    x = str(x)
    if re.search(goood,x): # we can treat goood and goooood in the same way
        x = re.sub(goood, 'good', x)
    if re.findall(check_duplicate,x): # we replace other duplicate characters
        x = re.sub(r'(\D)\1{2,}', r'\1', x)
    if re.search('(\[.*math).+(math\])',x): # dealing with math functions(borrowed from kaggle)
        x = re.sub('(\[.*math).+(math\])', '[latex formula]', x)
    if "'s " in x:
        x = x.replace("'s "," ")
    if "'" in x:
        x = x.replace("'", '')
    if "_" in x:
        x = x.replace("_", ' and ')
    for each in ",.!?()/":
        x = x.replace(each, '')
    return x


# we fix common wrong spellings in our specific document context
mispell_dict = {    'colour':'color',
                    'centre':'center',
                    'didnt':'did not',
                    'Didnt':'Did not',
                    'Doesnt':'Does not',
                    'Couldnt':'Could not',
                    'doesnt':'does not',
                    'isnt':'is not',
                    'shouldnt':'should not',
                    'flavour':'flavor',
                    'flavours':'flavors',
                    'wasnt':'was not',
                    'cancelled':'canceled',
                    'neighbourhood':'neighborhood',
                    'neighbour':'neighbor',
                    'theatre':'theater',
                    'grey':'gray',
                    'favourites':'favorites',
                    'favourite':'favorite',
                    'flavoured':'flavored',
                    'acknowledgement':'acknowledgment',
                    'judgement':'judgment',
                    'speciality':'specialty',
                    'favour':'favor',
                    'colours':'colors',
                    'coloured':'colored',
                    'theatres':'theaters',
                    'behaviour':'behavior',
                    'travelling':'traveling',
                    'colouring':'coloring',
                    'labelled':'labeled',
                    'cancelling':'canceling',
                    'waitedand': 'waited and',
                    'whisky':'Whisky',
                    'tastey':'tasty',
                    'goodbut': 'good but',
                    'sushis':'sushi',
                    'disapoointed': 'disappointed',
                    'disapointed':'disappointed',
                    'disapointment':'disappointment',
                    'Amzing':'Amazing',
                    'bAd':'bad',
                    'fantastics':'fatastic',
                    'flavuorful':'flavorful',
                    'infomation':'information',
                    'informaiton':'information',
                    'eveeyone':'everyone',
                    'Hsppy':'Happy',
                    'waygu':'wagyu',
                    'unflavorful':'untasty',
                    'fiancÃ©':'fiance',
                    'jalapeÃ±o':'jalapeno',
                    'jalapeÃ±os':'jalapenos',
                    'sautÃ©ed':'sauteed',
                    'CafÃ©':'Cafe',
                    'cafÃ©':'cafe',
                    'entrÃ©e':'entree',
                    'brÃ»lÃ©e':'brulee',
                    'entrÃ©es':'entrees',
                    'MontrÃ©al':'Montreal',
                    'crÃ¨me':'creme',
                    'JalapeÃ±o':'jalapeno',
                    'crÃªpe':'crepe',
                    'CrÃªpe':'Crepe',
                    'Flavortown': 'Flavor Town',
                    '\u200b': ' ',
                    'fck':'fuck',
                    'wi-fi':'wifi',
                    'ayce':'all you can eat',
                    'appriceiate':'appriciate',
                    'worest':'worst'}
def correct_spelling(x):
    x = str(x)
    for word in mispell_dict.keys():
        if word in x:
            x = x.replace(word, mispell_dict[word])
    return x

# seperate words, numbers and some unremoved punctuations such as ,.?!
def seperate_word(x):
    for pattern, repl in [('[\W]',lambda p:' '+p.group()+' '),('[0-9]{1,}',lambda p:' '+p.group()+' ')]:
        if re.search(pattern,x):   
            x = re.sub(pattern, repl, x)
    return x

from nltk.stem import SnowballStemmer
sb = SnowballStemmer("english")


# tokenize text
def tokenizeRawData(text):
    if isinstance(text, list):
        output = []
        for document in text:
            document = clean_contraction(document)
            document = clean_punc(document)
            document = fix_time(document)
            document = correct_spelling(document)
            document = seperate_word(document)
            document = document.lower()
            tokens = document.split()
            for i in range(len(tokens)):
                token = tokens[i]
                tokens[i] = sb.stem(token)
            output.append(tokens)
        assert len(output) == len(text)
        return output
    elif isinstance(text, str):
        text = clean_contraction(text)
        text = clean_punc(text)
        text = fix_time(text)
        text = correct_spelling(text)
        text = seperate_word(text)
        text = text.lower()
        output = text.split()
        for i in range(len(output)):
                token = output[i]
                output[i] = sb.stem(token)
        return output

tokenized_txt = tokenizeRawData(text_list)
assert len(tokenized_txt) == len(text_list)
assert len(id_list) == len(tokenized_txt)
tokenized_dict = {}
for i in range(len(id_list)):
    tokenized_dict[id_list[i]] =  tokenized_txt[i]

if cloud:
    client = MongoClient(uri)
    db = client.IE
    tokenizedDoc = db.tokenizedDoc
    try:
        tokenizedDoc.insert(tokenized_dict)
    except Exception:
        raise Exception("it is not json file")
    client.close()
else:
    client = MongoClient()
    db = client.IE
    tokenizedDoc = db.tokenizedDoc
    try:
        tokenizedDoc.insert(tokenized_dict)
    except Exception:
        raise Exception("it is not json file")
    client.close()








