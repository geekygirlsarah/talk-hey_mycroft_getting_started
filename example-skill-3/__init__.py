from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'geekygirlsarah/Sarah Withee'
LOGGER = getLogger(__name__)

class KnockKnockSkill(MycroftSkill):

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    @intent_handler(IntentBuilder("").require("knock.knock"))
    def handle_knock_knock_intent(self, message):
        # They said "knock knock"

        # You say "who's there?"
        # Get the next line
        noun = self.get_user_response("whos.there")

        # They said noun
        # You say "noun who?"
        self.speak(noun)
        self.get_user_response("who")

        # They said a punchline
        # You laugh in return
        self.speak_dialog("laugh")

def create_skill():
    return KnockKnockSkill()


