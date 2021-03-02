import tweepy
import re
#Function for emoji
def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                               "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
#Authentication
api_key = '' #my api key
api_secret_key = '' #my api secret key
access_token = '' #my access token
access_token_secret = '' #my access token secret

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
screenname = input("Screen Nameee")
stuff = api.user_timeline(screenname, count=10, include_rts=True)


#Dimiourgia listas
tweet = str(stuff)
list = []
x = ""
for info in stuff[:]:
    for i in str(info.text):
        if i==" ":
            list.append(x)
            x=""
        else:
            x = x + i

list.sort(reverse=True)
XwrisEmoji = []
for i in range(len(list)):
    lexeis = list[i]
    XwrisEmoji.append(deEmojify(lexeis))
list = XwrisEmoji
AritmosTweets=["1","2","3","4","5","6","7","8","9","0"]
for i in range(u-1,-1,-1):
    keimenakio = list[y]
    if ("." in text) or ("," in text) or ("!" in text) or ("@" in text) or ("£" in text) or ("#" in text) or ("$" in text) or ("€" in text)  or ("%" in text) or ("^" in text)  or ("&" in text)  or ("*" in text)  or ("(" in text) or (")"in text)or ("["in text)or ("]"in text)or ("{"in text)or ("}"in text) or (":"in text) or (";"in text) or ("<"in text) or ("/"in text) or ("?"in text) or ("|"in text)or (">"in text)or ("-"in text)or ("+"in text)or ("="in text)or ("http"in text):
        list.pop(y)
    elif True:
         for q in range(10):
                if Numbers[q] in list[y]:
                    list.pop(y)
print("Οι μεγαλυτερες λεξεις ειναι")
for i in range(5):
    print(list[-i])
print("Οι μικροτερες λεξεις ειναι")
for i in range(5):
    print(list[i-1])
