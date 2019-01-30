from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class WelcomeNDCLondon(MycroftSkill):

    @intent_handler(IntentBuilder("").require("welcomendc"))
    def handle_welcome_ndc_intent(self, message):
        self.speak_dialog("welcomendc")

def create_skill():
    return WelcomeNDCLondon()
