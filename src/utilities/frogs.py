import random


def getFrog():
    x = random.randint(0, 4)
    frogs = {
        0: """
         @..@         /===================\\
        (\\--/)        |     Welcome to    |
       (.>__<.)       |       Pocket      |
       ^^^  ^^^       \\===================/
   \n""",
        1: """      
         @..@         /===================\\
        (____)        |     Welcome to    |
       (>____<)       |       Pocket      |
        ^^~~^^        \\===================/
    \n""",
        2: """
         00           /===================\\
        (--)          |     Welcome to    |
       ( || )         |       Pocket      |
       ^^~~^^         \\===================/
   \n""",
        3: """
       (0) (0)        /===================\\
      ( ----- )       |     Welcome to    |
       [ | | ]        |       Pocket      |
      ~^~   ~^~       \\===================/
    \n""",
        4: """
       \\@--@/         /===================\\
      [ .~~. ]        |     Welcome to    |
       ||  ||         |       Pocket      |
      ~~~  ~~~        \\===================/

    \n"""
    }
    return(frogs.get(x))
