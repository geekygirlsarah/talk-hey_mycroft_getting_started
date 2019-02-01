from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
import twitter

LOGGER = getLogger(__name__)

class ReadHashtag(MycroftSkill):

    @intent_handler(IntentBuilder("").require("readhashtag"))
    def handle_read_hashtag(self, message):

        LOGGER.info("Trying to create Twitter API connection")

        # Feel these in with your Twitter Developer account keys

        consumer_key    = "..."
        consumer_secret = "..."
        token_key       = "..."
        token_secret    = "..."

        api = twitter.Api(consumer_key,
            consumer_secret,
            token_key,
            token_secret)

        LOGGER.info("Validating user")
        current_user = api.VerifyCredentials()
        LOGGER.info("User id: " + str(current_user.id) + "   Username: " + current_user.screen_name)

        LOGGER.info("Looking up tweets with #MycroftAtNDC")

        raw_tweets = api.GetSearch(term="#MycroftAtNDC",count=5,result_type="recent")
        tweet_text = ""
        for t in raw_tweets:
            tweet_text += t.user.screen_name + " tweeted: " + t.text + ". \n  "

        LOGGER.info("Tweets returned are: \n" + tweet_text)

        self.speak("Here are the last 5 tweets with the hashtag mycroft at N D C")
        self.speak(tweet_text)


def create_skill():
    return ReadHashtag()
