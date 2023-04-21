import re

def Bot_Response(message, response_array, response):

    # Splits the message and the punctuation into an array

    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message

    score = 0

    for word in list_message:

        if word in response_array:

            score = score + 1

    # Returns the response and the score of the response

    # print(score, response)

    return [score, response]

def get_response(message):

    # Add your custom responses here

    response_list = [

        Bot_Response(message, ['selam', 'merhaba', 'sa', 'sea',],

                     'merhaba ve aleyküm selam '),

        Bot_Response(message, ['bb', 'by', 'gidiyorum', 'gittim', 'çıkıyorum', 'gittim', 'kaçtım',], 'selametle'),

        Bot_Response(message, ['naber',], 'iyidir senden'),

        Bot_Response(message, ['nasılsın',],

                     'iyiyim sen'),

        # new

        Bot_Response(message, ['nerelisin',],

                     'Sana neresi lazım 🤭'),

        # Name

        Bot_Response(message, ['kimsin',],

                     'geveze ben🤝'),
        Bot_Response(message, ['yaş',], 'ѕαиα кα¢̧ ℓαzıм'),
                   

        # Help

        Bot_Response(message, ['mamaklı',],

                     'vefalı Mamaklı'),

        # Website

        Bot_Response(message, ['link', 'grup', ], '@vefaasohbet'),

        # Song

        Bot_Response(message, ['play', 'song', ],

                     'https://youtu.be/edzt82nC45k'),

        # Notes

        Bot_Response(message, ['not', ],

                     '🍻'),

        Bot_Response(message, ['socials', 'socials', ],

                     'Here you Go\n /socials'),

        Bot_Response(message, ['source', 'code', ], 'bilmiyom'),

        Bot_Response(message, ['günaydın',], 'günün aydın olsun'),

      

        # Nude Joke Lol

        Bot_Response(message, [

                     'nude', 'nudes', ], '🤫'),

        # When Querry

        Bot_Response(message, ['when', '?', 'query', 'question', 'inform',

                     'developer'], 'Inquire with the developer about this. @amrohan'),

        # When Website

        Bot_Response(message, ['website', 'amrohan', 'web', 'developer'],

                     'https://www.rohan.ml'),

        # When Projects

        Bot_Response(message, ['projects', 'project', 'proj','pro','projec', 'proje'],

                     'Here you Go\n /projects'),

    ]

    # Checks all of the response scores and returns the best matching response

    response_scores = []

    for response in response_list:

        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable

    winning_response = max(response_scores)

Bot_Response(message, ['kurucukim,kurucu',],

                     '@Cengonuzz'),
  

  matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user

    if winning_response == 0:

        score = score + 1

    else:

        bot_response = matching_response[1]

    print('Bot response:', bot_response)

    return bot_response
