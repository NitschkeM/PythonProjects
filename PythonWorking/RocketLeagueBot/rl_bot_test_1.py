
# This will configure Rocket League with the default parameters that come with RLGym.
# The make function comes with a number of optional parameters, list here:
#   https://rlgym.org/docs-page.html#introduction

#import rlgym
#env = rlgym.make()

# Configuring RLGym Environments using 3 Basic Configuration Objects.
# 1. A Reward Function Object               Singular?   Restricted to a Single Reward Function Object(RFO)?
#                                                           - A Single Reward Function per RFO?
# 2. An Observation Builder Object          Singluar?   Limited to Only One Observation Bulder Object?
# 3. A List of Terminal Condition Objects   Plural      Multiple Terminal Condition Objects



# How does the bot play now and how can I change how it plays?
#   How to describe how the bot plays?
#     Looking for, describing and programming its Tendencies and Patterns.

# The Doubt and Hessitation seems to stem from/be related to ideas such as:
#   - I dont have enough Time and Processing Power to create a really good bot.
#         A revolutionary bot?
#           In what way?
# Perhaps the honest statement would be: I don't know what is possible.
#   I would prefer that to limiting beliefs without basis in reality.

# Was a little discouraged by the idea of using learning algorithms created by others / [official algorithms / well known algorithms]:
#   Wants to rely as little as possible on others?
#     Wants to be as idependent as possible?
#   The question:
#       Is there really anything I can do to improve the performance of a bot trained with a well known algorithm?
#         A1: I don't know. 
#         A2: I don't know - yet.     (Seems More Active and Less Passive, Seems More Forward Moving/Looking)
#               --> I wonder how others have done it.
#                       Wants to see examples to learn from.


import rlgym

env = rlgym.make(game_speed=4)

while True:
    obs = env.reset()
    done = False

    while not done:
      #Here we sample a random action. If you have an agent, you would get an action from it here.
      action = env.action_space.sample()
      
      next_obs, reward, done, gameinfo = env.step(action)
      
      obs = next_obs


# How do one store the bots progress?
# How is the bot's learning stored?
# I do not want to see myself as a bot - therefore I do not referr to myself as a bot.
#   - Thats exactly what a bot would say!
#   - Also You!
#   - And You!
# Reddit Forums?
################################
#   Let's be Explicit, Concrete and Precise:
#	This is not a Reddit Forum.
#	This is not Rocket League.
################################
#	This is Visual Studio Code.
################################


