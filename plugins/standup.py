from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template
from will import settings

class StandupPlugin(WillPlugin):

    @periodic(hour='11', minute='30', day_of_week="mon-fri")
    def standup(self):
        self.say("@all Standup! %s" % settings.WILL_ZOOM_URL)
