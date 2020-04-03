# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# print(email_one)

#Point 2

def censor(censor_word, text):
    censor_str = "["
    for i in range(0, len(censor_word)):
        censor_str += "-"
    censor_str += "]"

    return text.replace(censor_word, censor_str)



# print(censor("learning algorithms", email_one))

#Point 3

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
# print(email_two)

def censor2(censor_lst, text):
    censored_text = text
    censor_lst_cap = []
    for word in censor_lst:
        censor_lst_cap.append(word.capitalize())
    censor_lst_updated = censor_lst + censor_lst_cap

    for word in censor_lst_updated:
        censor_str = "["
        for i in range(0, len(word)):
            censor_str += "-"
        censor_str += "]"
        censored_text = censored_text.replace(word, censor_str)
    return censored_text

# print(censor2(proprietary_terms, email_two))

#Point 4

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]




def censor3(censor_lst, negative_lst, text):
    negative_lst_cap = []
    for str in negative_lst:
        negative_lst_cap.append([str, str.capitalize()])
    print(negative_lst_cap)
    censored_text = censor2(censor_lst, text)
    counter = 0
    for neg_word in negative_lst_cap:
        for word in neg_word:
            counter += text.count(word)
    return counter

print(censor3(proprietary_terms, negative_words, email_three))
