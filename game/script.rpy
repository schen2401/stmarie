define attendant = Character("Attendant")
define aunt = Character("Aunt Mildred")
define icom = Character("Intercom")
define mc = Character('[player_name]', image='mc')
define narrator = Character(None)
define mystery = Character("???")
define vamp = Character("Claire")

# flag that sets disabled choices to still show
define config.menu_include_disabled = True

init python:
    if not hasattr(renpy.store, 'gender'):
        gender = "m"
    mc_scale = 0.2 # how much the mc sprites get scaled down
    v_scale = 0.4 # how much the vampire sprites get scaled down

    demo = True # flag if game is a demo or not

# defining sprites

image aunt = "aunt_sprite.png"

image mmc = im.FactorScale("mmc_neutral.png", mc_scale)
image fmc = im.FactorScale("fmc_neutral.png", mc_scale)
image mmc embarassed = im.FactorScale("mmc_embarassed.png", mc_scale)
image fmc embarassed = im.FactorScale("fmc_embarassed.png", mc_scale)
image mmc fear = im.FactorScale("mmc_fear.png", mc_scale)
image fmc fear = im.FactorScale("fmc_fear.png", mc_scale)
image mmc happy = im.FactorScale("mmc_happy.png", mc_scale)
image fmc happy = im.FactorScale("fmc_happy.png", mc_scale)
image mmc surprised = im.FactorScale("mmc_surprised.png", mc_scale)
image fmc surprised = im.FactorScale("fmc_surprised.png", mc_scale)

# side mc images appear in bottom left corner
image side mc:
    ConditionSwitch("gender == 'm'", "mmc",
                            "True", "fmc")

image side mc embarassed = ConditionSwitch("gender == 'm'", "mmc embarassed",
                            "True", "fmc embarassed")

image side mc fear = ConditionSwitch("gender == 'm'", "mmc fear",
                            "True", "fmc fear")

image side mc happy = ConditionSwitch("gender == 'm'", "mmc happy",
                            "True", "fmc happy")

image side mc surprised = ConditionSwitch("gender == 'm'", "mmc surprised",
                            "True", "fmcsurprised")


image vamp = im.FactorScale("v_neutral.png", v_scale)
image vamp embarassed = im.FactorScale("v_embarassed.png", v_scale)
image vamp happy = im.FactorScale("v_happy.png", v_scale)
image vamp sad = im.FactorScale("v_sad.png", v_scale)
image vamp doki = im.FactorScale("v_doki.png", v_scale)

# defining animations
transform pan_up:
    yalign 0.6
    # lerp from y = 1 to y = 0 in 2.5 seconds
    linear 2.5 yalign 0.0

image vamp cg1:
    im.FactorScale("v_cg_1.png", 0.5)

    pan_up


# The game starts here.

label start:

    #jump sprite_test
    jump Chapter1
    return
