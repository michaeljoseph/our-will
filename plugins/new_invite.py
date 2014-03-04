from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template


class NewInvitePlugin(WillPlugin):

    @route("/new-invite/")
    def new_invite_listener(self):
        new_invite_html = rendered_template("new_invite.html", self.request.query)
        self.say(new_invite_html, html=True)
        return ""