# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.intent is not None:
            return
        
        # set_intent tells the bot what it's trying to do
        if self.kickoff_flag:

            self.set_intent(kickoff())
            return
        
        if self.is_in_front_of_ball:
            self.set_intent(goto(self.friend_goal.location))
            return
        
        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        hits = find_hits(self, targets)
        if len(hits['at_oppenent_goal']) > 0:
            self.set_intent(hits['at_oppoenent_goal'][0])
            return
        if len(hits['away_from_our_net']) > 0:
            self.set_intent(hits['away_from_our_net'])
            return
        if self.me.boost > 99:
            self.set_intent(short_shot(self.foe.location))
            return
        closest_boost = self.get_closest_large_boost()
        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))
            return
        



       
