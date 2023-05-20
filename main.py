import re
import long_responses as long



def messaga_probability(user_message, recognised_word, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_word:
            message_certainty += 1

    #percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_word))


    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = messaga_probability(message, list_of_words, single_response, required_words)


    # Response------------------------------------------
    response('Hello', ['hello', 'hi','sup', 'hey'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you' ,'doing'], required_words=['how'])
    response('Thank you!', ['i','love', 'code', 'palace'], required_words=['code', 'palace'])
    

    response(long.R_EATING, ['what','you', 'eat'], required_words=['you', 'eat'])



    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list) print the highest probability of the word by the bot

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_reponse(user_input):
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        response = check_all_messages(split_message)
        return response


#Testing the reponses
while True:
    print('Bot: ' + get_reponse(input('You: ')))