import requests
import time

from plugins.server.mixins import GithubMixin
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template

class TimeboxerPlugin(GithubMixin, WillPlugin):

    def _check_branches(self):
        #print self.get_github_branches()[0]
        print self.get_github_branches()[0].branches[0].branch_obj
        print dir(self.get_github_branches()[0].branches[0].branch_obj)
        print self.get_github_branches()[0].branches[0].branch_obj.ratelimit_remaining
        print self.get_github_branches()[0].branches[0].branch_obj.commit
        print dir(self.get_github_branches()[0].branches[0].branch_obj.commit)
        print self.get_github_branches()[0].branches[0].branch_obj.commit.committer
        print dir(self.get_github_branches()[0].branches[0].branch_obj.commit.committer)


    @periodic(day='1')
    def check_for_stale_branches(self):
        self._check_branches()

    @respond_to("^test timeboxer", multiline=True)
    def test_timeboxer(self, message):
        self._check_branches()
