import requests

from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template


class ServicesPlugin(WillPlugin):

    @periodic(second='36')
    def github_is_up(self):
        r = requests.get("https://status.github.com/api/last-message.json")
        last_status = self.load("last_github_status")
        if r.json()["status"] != last_status:
            if r.json()["status"] != "good":
                self.say("FYI everyone, github is having trouble: %s" % r.json()["body"])
            else:
                self.say("Looks like github's back up!")
            self.save("last_github_status", r.json()["status"])

    @periodic(second='46')
    def heroku_is_up(self):
        r = requests.get("https://status.heroku.com/api/v3/current-status")
        last_status = self.load("last_heroku_status")
        if r.json()["status"] != last_status:
            if r.json()["status"]["Production"] != "green":
                self.say("FYI everyone, heroku is having trouble: %s. \n http://status.heroku.com" % r.json()["issues"][0]["title"])
            else:
                self.say("Looks like heroku's back up!")
            self.save("last_heroku_status", r.json()["status"])
