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
        censored_text = censored_text.replace(word, "###")
    return censored_text

print(censor2(proprietary_terms, email_two))
