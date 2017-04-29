from instapy import InstaPy
import os

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder

friend_list = ['friend1', 'friend2', 'friend3']
like_list = ['#design', '#fashionillustration', '#illustration', '#fashionweek', '#textiles', '#patterndesign', '#art', '#fashiondesign', '#illustrator', '#Fashionillustrator', '#creativedirector', '#artdirection',  '#pattern', '#designer', '#creative', '#textiledesigner', '#DIGITALART', '#illustrationoftheday', '#fashionblogger']
# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

InstaPy())\
  .login()\
  .set_upper_follower_count(limit = 3000) \
  .set_lower_follower_count(limit = 200) \
  .set_do_comment(True, percentage=1) \
  .set_comments(['so great!' 'love it!']) \
  .like_by_tags(like_list, amount=100) \
  .end()
