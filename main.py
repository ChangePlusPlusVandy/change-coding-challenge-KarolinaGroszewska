import tweepy
import random

# Variables that contains the credentials to access Twitter API. Unique to Karolina Groszewska, and the
# TwitterTinkerChange++ app
# Populate with own data
ACCESS_TOKEN = 'INSERT HERE'
ACCESS_SECRET = 'INSERT HERE'
CONSUMER_KEY = 'INSERT HERE'
CONSUMER_SECRET = 'INSERT HERE'
# Access to user's consumer key and consumer secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# Access to user's access key and access secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# Calling api
api = tweepy.API(auth)
# declares and initializes empty arrays for tweets
tweet1Array = []
tweet2Array = []
# declares and initializes selectedTweet string
selectedTweet = ""
# declares and initializes number of tweets and the point system
numberOfTweets = 0
points = 0

# Function to extract tweets
def get_tweets(username):
    # 3200 tweets to be extracted
    number_of_tweets = 3200
    # checks for the username passed into the function, excludes replies and retweets
    try:
        tweets = api.user_timeline(screen_name=username, exclude_replies=True, include_rts=False)
    except:
        raise Exception("An invalid username was entered")

    # declares and initializes empty array for temporary tweet collection
    tmp = []

    # create array of tweet information: text, tweet link
    tweetArray = [tweet.text for tweet in tweets]
    for t in tweetArray:
        #final check for any @s
        if "@" in t:
            # tweet excluded for featuring an @"
            print("tweet excluded for featuring an @")
        else:
            # appending tweets to the empty array tmp
            tmp.append(t)

    #return temporary array to save
    return tmp

# MAIN METHOD #
if __name__ == '__main__':
    #intro comments
    print("Welcome to Twitter Tinker! Created by Karolina for the Change++ 2020 application.")
    print("*********************************************************************************")
    # person one
    val1 = input("Enter your value for user number one following this format – 'kanyewest' (no quotes) : ")
    # if left blank assume kanye
    if val1 == "":
        val1 = "kanyewest"
    # person two
    val2 = input("Enter your value for user number one following this format – 'elonmusk' (no quotes) : ")
    # if left blank assume elon
    if val2 == "":
        val2 = "elonmusk"
    # tweet arrays are initialized
    tweet1Array = get_tweets(val1)
    tweet2Array = get_tweets(val2)
    # tweet array lengths are initialized
    num1 = len(tweet1Array)
    num2 = len(tweet2Array)
    # loop for playing
    userValue = ""
    while userValue != "quit":
        #random number generator to determine person
        selection = random.randint(1, 2)
        if selection == 1:
            # random number generator to determine tweet
            randomTweet = random.randint(0, num1-1)
            selectedTweet = tweet1Array[randomTweet]
            print("The text of your selected tweet is : " + selectedTweet)
            guess = input("Do you think this tweet belongs to " + val1 + " or to " + val2 + "? ")
            if guess == val1:
                print("Congrats! You have gained one point.")
                points += 1
                numberOfTweets += 1
            else:
                print("Sorry! You have gained no points")
                numberOfTweets += 1
        else:
            # random number generator to determine tweet
            randomTweet = random.randint(0, num2-1)
            selectedTweet = tweet2Array[randomTweet]
            print("The text of your selected tweet is : " + selectedTweet)
            guess = input("Do you think this tweet belongs to " + val1 + " or to " + val2 + "? ")
            if guess == val2:
                print("Congrats! You have gained one point.")
                points += 1
                numberOfTweets += 1
            else:
                print("Sorry! You have gained no points")
                numberOfTweets += 1
        # exiting loop
        userValue = input("Type in 'quit' to exit. Otherwise, press enter to continue. ")
        # easter egg
        if userValue == "Karolina":
            print("Caffeine brain go brrrrrr")
    #ending comments
    print("Thanks for playing TwitterTinker!")
    print("*********************************")
    #point prints because grammar is important
    if points == 1:
        print("Your score was " + str(points) + " point. You played " + str(numberOfTweets) + " rounds.")
    elif numberOfTweets == 1:
        print("Your score was " + str(points) + " points. You played " + str(numberOfTweets) + " round.")
    elif points == 1 & numberOfTweets == 1:
        print("Your score was " + str(points) + " point. You played " + str(numberOfTweets) + " round.")
    else:
        print("Your score was " + str(points) + " points. You played " + str(numberOfTweets) + " rounds.")








