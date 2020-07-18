define attendant = Character("Attendant")
define aunt = Character("Aunt Mildred")
define icom = Character("Intercom")
define mc = Character('[player_name]')
define narrator = Character(None)

# The game starts here.

label start:
    jump Chapter1
    return
