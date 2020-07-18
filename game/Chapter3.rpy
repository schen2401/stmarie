label Chapter3:
# Key: [] implies a single text box. [Menu] means that a specific menu is needed. In the first row immediately following the [, the necessary sprite to be shown as well as starting/stopping different sound tracks. Background changes will be shown at the end, in the row preceding the ].
# BG means image background. BGS means background sound, either an ambient track or music.
# NEW FORMATTING: BLANK FIRST ROW = NO SPRITE. MC SPRITE IS ALWAYS IN THE BOTTOM LEFT.

    narrator """
    After eating my fill and helping Aunt Mildred with the dishes, I bid her goodnight and make my way towards my room for the evening.
    """
    scene bg b_mcroom
    
    narrator """
    Opening the door to the guest room down the hall from Aunt Mildred’s, I flip on the light switch and drop my travel bag near the door.
    
    The room almost untouched from when I had last seen it, I spend some time wiping off a thin layer of dust and cobwebs that had piled onto most of its surfaces. It was clear that this room hadn’t been used for a long time.
    
    Opening the closet to hang up the few changes of clothes I brought with me, I notice the floor is cluttered with boxes, buckets, and worn fishing equipment.
    
    Growing up, this room doubled as a bedroom of sorts for whenever my parents let me stay the night. Now, I guess it was used as a sort of extra storage space for whatever my aunt or uncle had needed.
    
    Feeling settled in, I change into a more comfortable set of clothes and turn off the lights before slipping under the covers, a cool ocean breeze beginning to drift into the room.
    """
    scene bg b_mcroom_dark
    
    narrator """
    Turning on my side to face the nearby window, its thin drapes held open by the passing wind, I’m met with the moon’s silver light as it begins to hover over the ocean’s shore.
    
    And as I stare off towards the horizon, my eyes growing heavy at the sight of crashing waves and the thought of old memories, I hear the heavy ring of a distant clocktower compelling me to sleep.
    """
    play music clocktowersounds-short

    # [TIMESKIP]

    narrator "I wake up to a loud knocking coming from my bedroom door, the muffled voice of Aunt Mildred calling me down for breakfast."
    
    scene bg b_mcroom

    mc "\"I’ll be right there!\""
    
    narrator """
    Yawning, I take a long stretch before kicking away the bedsheets and jumping onto my feet.

    My eyes squinting from sleep in their attempts to adjust to the searing sunlight flooding the room.

    Slamming the window shut and closing the blinds, I take a few minutes to get dressed before walking to the bathroom across the hall to freshen up.
    """

    scene bg b_house_interior
    
    narrator """
    Now fully awake, I bound down the wooden steps into the living room and am met with the smell of freshly cooked bacon and warm bread.
    
    Stepping into the kitchen I can see Aunt Mildred by the stove, sliding a pair of fried eggs onto an open plate.
    
    Wiping the sweat off her brow and wiping her hands on a nearby rag, she turns around and pushes the plate into my hands with a smile. She was fully dressed.
    """
    mc "\"You going somewhere, Aunt Millie?\""
    [
    Aunt Mildred:
    “Yeah I have a doctor’s appointment over in Jackson in about an hour. I wanted to let you sleep in but any longer and you would’ve missed breakfast.”
    ]
    [
    MC:
    “Really? What time is it?”
    ]
    [
    Aunt Mildred:
    “It was almost three the last time I checked. You must’ve really been tired.”
    ]
    [
    MC:
    “Yeah I guess. But, wait a minute. Isn’t the car still broken? Jackson’s like ten miles away. How are you going to make it in time?
    ]
    [
    Aunt Mildred:
    “Well, I was planning on taking the bus at first but then a friend of your uncle’s called and said he was willing to take me. He was going up there anyway for some business so it all works out, I’ll just have to wait for him.”
    ]
    [
    As if on cue, a loud honking from the driveway cuts our conversation short. Jumping a little in surprise, Aunt Mildred looks out the dining room window to make sure it’s her ride before reaching for her purse.
    ]
    [
    Aunt Mildred:
    “I’m going to be out for most of the day so don’t worry about waiting for me. I left some money on the counter in case you need it, and you have my number so if something comes up just call me. I’ll be home soon, okay?”
    ]
    [
    Giving me a small hug and a kiss on the cheek, Aunt Mildred makes her way towards the door and waves me goodbye.
    ]
    [
    Setting my plate down on the dining room table, I follow her to the front door to see the two of them off, waving at them as they drive down the road.
    ]
    [
    Having the house for myself, I sit down for a quick breakfast. Although later than I hoped it would be, there’s still enough time for me to do something productive before the day comes to an end,
    ]
    [
    and as I scrape up the last bits of egg yolk with a warm piece of toast, listening to the anxious clucking of the nearby chicken coop, I can’t help but wonder.
    ]
    [
    What do I want to do today?
    ]
    [MENU]
    [EXPLORE THE FOREST: CHECK OUT THAT HOUSE FROM YESTERDAY]

    [HEAD INTO TOWN: VISIT THE MECHANIC AND LOOK INTO GETTING THE CAR FIXED]

    [HEAD DOWN TO THE SHORE: GET YOUR UNCLE’S SHOP OPEN FOR BUSINESS]
    % NOTE TO SEAN: make sure to grey out and make the second and third choice unselectable.
    [MENU]


    [
    Remembering that weird building that I saw the other day on our drive back home, I set my dishes down in the nearby sink and resolve to investigate it.
    ]
    [

    Packing up my travel bag and filling it with snacks and any supplies I might need, I grab a set of spare keys from the counter and head out the back, making sure to lock the door behind me.
    BG CHANGE TO FOREST1]
    [
    Setting out into the woods, I start following one of the hiking trails that my aunt and I used to frequent when I was younger, a small dirt road lined with wooden posts that led straight into the heart of the forest.
    BG CHANGE TO FOREST1(BLACK AND WHITE)]
    [
    Whenever my uncle was out at sea for longer than expected, my aunt would take me out for long hikes through the woods, the large shadows of the trees looming overhead giving the whole place an air of mystery.
    ]
    [
    Aunt Mildred would spend this time telling me stories and feeding into my childish wonderment.
    ]
    [
    She would tell me about creatures as old as the earth itself, of troublesome fairies and their dealings with foolish men,
    ]
    [
    and most important of all, she would tell me of “Old Red Eyes” and the horrors that lay in wait between the trees.
    ]
    [
    Each trip the stories would always be the same, and although forgetting the details I do remember always liking it whenever Aunt Mildred told me them.
    ]
    [
    By the time she would finish, we would have already reached our destination.
    ]
    [
    Following the hiking trail, we would be met by a clearing with a large pond, its cool surface littered with lilypads, teeming with signs of life.
    ]
    [
    We would often sit here to eat, catch our breaths, and watch as the small frogs and glittering dragonflies scittered across the large pond reeds and onto the water’s surface.
    ]
    [
    Then, once our snacks were depleted, the two of us would pack up our things and make our way further down the hiking trail, the road looping back near to where we had started.
    BG CHANGE TO FOREST1]
    [
    Yet, as I squeeze my way past the wooden posts that line the main road, I realize that following it back would do nothing to help me reach my destination.
    ]
    [
    I had seen the building the other day while we were driving back home, meaning that if I were to find it, I would need to head towards the northern parts of the forest, near where the road had looped around into Main Street and the rest of St. Marie.
    ]
    [
    Given how the trail towards the pond had already brought me to the forest’s center, the trek towards the forest’s northern end wouldn’t be much farther, I’d just need to make sure I didn’t lose my path on the way home.
    ]
    [
    Keeping a small compass ready just in case, I strengthen my resolve and start walking deeper and deeper into the forest, batting aside stray branches as my boots crunch up the foliage piling up on the floor underneath.
    BG CHANGE TO FOREST2, ]
    [
    After thirty minutes of walking I finally arrive at my destination, the building once again almost hidden behind an endless sea of trees.
    BG CHANGE TO CHATEAU_EXTERIOR]
    [
    Now able to take a closer look at it, I not only notice the sheer size of the building, akin to that of an old mansion or plantation, but notice that the building is old, really old.
    ]
    [
    Judging from its architecture it could have been around for a century or two, with the entire building’s sweeping curves and extensive foundations giving it a sense of ornateness despite its decrepit nature.
    ]
    [
    Stepping up to its front porch, the soft wood creaking under the weight of my feet, I notice the faintest hints of a road leading away from the front porch and into the forest behind me, its appearance eroded and lost to time.
    ]
    [
    Based off my intuition, I could guess that this road was meant to lead back into town somehow, but as for why it had been abandoned for so long alongside the rest of the house, I really had no answer.
    ]
    [
    Met with a large pair of wooden double doors and a rusted iron lock, I think to myself for several moments before placing a hand upon the cool wooden surface.
    ]
    [
    With every push I can hear the soft squeaking of the wood, its weakened hinges beginning to give way until finally with a loud snap one of the doors caves in and gives me enough space to make my way inside.
    BG CHANGE TO CHATEAU_INTERIOR]
    [
    To my surprise, unlike the rest of the house, which was rotting and unkempt on the outside, its interior was clean and verently decorated.
    ]
    [
    As I walk further and further into the house and begin to ascend the large staircase adorning the center of the room, I slowly take out a pocket knife that I had brought with me, unsure of who or what thing I could stumble across.
    ]
    [
    Reaching the top of the stairs, I look up and notice a large and ornate looking grandfather clock, my face casting a reflection upon its freshly polished surface.
    ]
    [
    Upon either side of the clock I see a series of candelabras adorning the walls, their small flames serving as the only source of light within the room.
    ]
    [
    Looking closer at the candles, I notice that the wax is still relatively new, as if the candles had been replaced fairly recently.
    ]
    [
    But, wait, isn’t this place abandoned?
    ]
    [
    My eyes drawn back towards the grandfather clock, almost entranced by its surface and the soft sound of its ticking hands, I swear I can hear the faintest sounds of music coming from further down the hall.
    ]
    [
    There was someone living in this house.
    ]
    [VAMPIRE SPRITE
    ???:
    “H-Hello…?”
    ]
    [
    Hearing a voice, I immediately snap out of my thoughts and unclasp my pocket knife.
    ]
    [
    Turning around in a panic, I bump into the grandfather clock and am met with the face of a young woman staring back at me from a crack in a doorway, her eyes flinching as the clock comes crashing down behind me.
    ]
    [VAMPIRE SPRITE
    Seeing my knife, her eyes grow wide as she closes the door, leaving me with the sound of fumbling locks. Realizing my mistake, I quickly stuff my knife back into my pocket and make my way towards the door.
    ]
    [VAMPIRE SPRITE
    MC:
    “No, no! Wait! I’m sorry about the knife! I didn’t think there’d be anyone living here, I thought you’d be like some sort of animal or something.”
    ]
    [
    Stepping on a stray shard of glass and crushing it under my shoe, I wince and look over to the grandfather clock. There was no telling how expensive that thing was.
    ]
    [VAMPIRE SPRITE
    MC:
    “Uh...I’m really sorry about the clock. I can buy you a new on—oh, wait, it’s probably really old huh? I-I’ll fix it for you though! You know, if you want me too…”
    ]
    [
    I’m lying. I don’t know jack shit about fixing clocks. But I mean, it couldn’t hurt to try right?
    ]
    [
    Man I’m stupid, I just barged into this lady’s house, broke some of her things and then whipped out a knife on her. I’ll be lucky if she doesn’t call the cops on me.
    ]
    [
    MC:
    “I’ll uh, I guess I’ll be going then. Once again I’m just, really, really sorry about everything. I’ll leave some money down near the door.”
    [
    MC:
    “It’s, well it’s not much but I’m sure it’d be enough to fix some of the damages. Maybe get a new one? Y-Yeah…”
    ]
    [
    Met with complete silence, I awkwardly take out my wallet and set down some cash by the foot of the door.
    ]
    [
    Still feeling guilty but at a loss for what to say, I start walking down the hall when I hear the sound of shuffling locks, the wooden door creaking on its hinges as it’s pried open.
    ]
    [???:
    “Wait…! Don’t go just yet...”
    ]
    [
    The voice from before is soft, timid, yet tinged with a sense of loneliness. As she calls out to me I can’t help but hear the desperation in her voice, causing me to wonder why or how she got here.
    ]
    [
    This house was in the middle of nowhere. I turn around to face her...
    ]
    [Vampire CG  # 1, Gymnopedie 1 plays]
    [VAMPIRE SPRITE
    ???:
    “Y-You don’t have to worry about the clock or anything...it was already quite old…”
    ]
    [CG ends]
    [
    I see the girl step out of the doorway with trepidation, fidgeting nervously with the sleeves of her dress as she glances down at her feet.
    ]
    [
    Finally getting the chance to see her better as she steps out into the candlelight, I find myself having to fight the urge to just stand there and stare at her.
    ]
    [
    She looks like she just came out of a halloween party. Dressed in a long and frilled dress, its style feeling rather fitting for a home as old as this, her face is framed on either side by long rivulets of silvery-white hair.
    ]
    [
    Catching the candlelight’s glow, her hair glistens like moonlight, her pale skin giving way to even the smallest of blush as she continues shifting in place, seemingly unaware of what to do with the unexpected company.
    ]
    [
    As her eyes dart from place to place either glued to the floor or some other fixture, always making a conscious effort not to make eye contact, I catch the glimpse of crimson red eyes.
    ]
    [
    Contacts? Is that her real hair too or is it a wig? Wait, I guess she could be an albino but, albinos don’t have red eyes do they?
    ]
    [
    Why would she be dressed like this in the middle of nowhere too? How long has she been living here? Where did she come from?
    ]
    [
    Is she from Jackson? Actually, wait, that would make sense. People from Jackson were always a little weird.
    ]
    [VAMPIRE SPRITE
    ???:
    “U-Um...are you okay?”
    ]
    [VAMPIRE SPRITE
    MC:
    “Huh? Yeah, yeah I’m fine.”
    ]
    [VAMPIRE SPRITE
    Snapping out of it, I return to my senses to see the young girl staring at me in confusion, her head tilted to the side.
    ]
    [VAMPIRE SPRITE
    MC:
    “ I’m sorry, I just didn’t really know what to expect for someone who lived here...You do live here right?”
    ]
    [VAMPIRE SPRITE
    ???:
    “...”
    ]
    [VAMPIRE SPRITE
    Not responding, the girl takes a step back, her brow furrowing slightly as she looks to the side as if unsure of how to respond.
    ]
    [VAMPIRE SPRITE
    MC:
    “That was a weird thing to ask wasn’t it?”
    ]



    [VAMPIRE SPRITE
    Scratching the back of my head for a few moments while I try to think of what to say, I shrug and reach out with an outstretched hand while making sure to give the girl some space.
    ]
    [VAMPIRE SPRITE
    MC:
    “Well...it might be a little too late but I might as well introduce myself. My name’s[insert player name: John]...Uh, what’s yours?”
    ]
    [VAMPIRE SPRITE
    ???:
    “...”
    ]
    [VAMPIRE SPRITE
    MC:
    “Only if you’re comfortable telling me of course. I know we just met so if you’re willing to hold off that’d make sense—”
    ]
    [VAMPIRE SPRITE
    ???:
    “Claire…”
    ]
    [VAMPIRE SPRITE
    MC:
    “Come again?”
    ]
    [VAMPIRE SPRITE
    ???:
    “C-Claire du Clarimonde...it’s my name…”
    ]
    [VAMPIRE SPRITE
    Her voice as close as possible to a whisper, she looks up at me with an air of nervous content. As for her name, well, her last name definitely didn’t sound like any of the ones I was used to seeing in St. Maire.
    ]
    [VAMPIRE SPRITE
    But for some reason, I just can’t help but find it familiar.
    ]
    [VAMPIRE SPRITE
    Slowly making her way towards the door, her steps hidden by the long hem of her dress, the dense fabric gliding along the wooden floorboards, she opens it and meekly steps aside.
    ]
    [VAMPIRE SPRITE
    The room is filled with a much softer and brighter light than the rest of the house, and I can catch a glimpse of a bed and some lavish furniture. It was probably her room.
    ]
    [VAMPIRE SPRITE
    Claire:
    “Would you like some tea…?”
    ]
    [VAMPIRE SPRITE
    MC:
    “Uh, sure."
    ]
    [VAMPIRE SPRITE
    To be honest I didn’t really care much for tea, but after essentially breaking into her house I thought it was the least I could do to try and make up for it.
    ]
    [
    Following her into the room, I’m led past a series of towering bookcases, their frames almost reaching up to the ceiling and chock full of leather-bound contents.
    ]
    [
    Reaching a set of chairs separated by a glass coffee table, I notice a small plushie of a rabbit nestled in one of the chairs, a small tea set placed right in front of it.
    ]
    [
    Suddenly, Claire rushes forward and scoops the rabbit out of the chair, turning to hide it from me as she walks off and settles it into a closet of sorts.
    ]
    [
    Rushing back, her face nearly red from embarrassment, she motions towards one of the chairs.
    ]
    [VAMPIRE SPRITE
    Claire:
    “I-I’m sorry about that. P-Please, sit!”
    ]
    [VAMPIRE SPRITE
    Shrugging, I follow her lead and sit down on the chair across from her. Breathing a sigh of relief, Claire starts pouring out a few cups of tea and hands one of them to me.
    ]
    [VAMPIRE SPRITE
    MC:
    “Thanks.”
    ]
    [VAMPIRE SPRITE
    Taking a small sip, my face scrunches up. It tastes like dirt water.
    ]
    [VAMPIRE SPRITE
    Claire:
    “Would you like any sugar?”
    ]
    [VAMPIRE SPRITE
    MC:
    “Right. Yes, please. Some sugar would be nice.”
    ]
    [VAMPIRE SPRITE
    Smiling a little and stifling a laugh, Claire grabs a hold of my cup and drops in a few sugarcubes. Taking a few moments to stir and wait for it to settle, she hands me back the cup before getting to work preparing her own.
    ]
    [VAMPIRE SPRITE
    MC:
    “Thank you.”
    ]
    [
    Taking another sip, I do a better job at hiding my distaste. It still tastes like dirt, now with just a bit of sugar mixed in.
    ]
    [
    Man, maybe tea just really isn’t meant for me after all. Setting the cup down onto a tiny dish, I look over to Claire and see her taking a long drink.
    ]
    [
    Her eyes closed and her whole demeanor put at ease, it seemed like the tea did a good job at calming her nerves.
    ]
    [VAMPIRE SPRITE
    MC:
    “So was that rabbit yours?”
    ]
    [VAMPIRE SPRITE BLUSH
    And almost instantly, any peace of mind that the tea had given Claire was thrown out the window as I decided to open my big mouth.
    ]
    [VAMPIRE SPRITE BLUSH
    Her skin beginning to take on a hue similar to her widening eyes, Claire quickly sets down her teacup.
    ]
    [VAMPIRE SPRITE BLUSH
    Reaching out for a handkerchief, she turns away from me as she wipes her mouth and fights back a cough.
    ]
    [VAMPIRE SPRITE BLUSH
    MC:
    “Shit! I’m sorry, do you need water or something?”
    ]
    [VAMPIRE SPRITE BLUSH
    I get up to try and help her but Claire shakes her head and holds up a finger. Settling back down into my seat, she places a hand to her chest and clears her throat.
    ]
    [VAMPIRE SPRITE
    Claire:
    “I-I’m sorry, I wasn’t really expecting that question. Yes, the rabbit is mine.”
    ]
    [VAMPIRE SPRITE
    Folding her hands in her lap, she gently rocks her feet back and forth, her eyes gaining a rather downcast look.
    ]
    [VAMPIRE SPRITE
    After sitting there in silence for a few moments, and after my taking of a few more painful sips of tea, she looks up at me, her crimson eyes soft with worry.
    ]
    [VAMPIRE SPRITE
    Claire:
    “It’s...a little strange, isn’t it? Still playing with toys at this age...”
    ]
    [VAMPIRE SPRITE
    MC:
    “No, no! Not at all! I mean, like, everyone’s got something they’re into right? Like hobbies or that sort of thing.”
    [VAMPIRE SPRITE
    MC:
    “And besides, having a stuffed animal wouldn’t even be that weird. I’m sure there are people out there who are into things that are much weirder.”
    ]
    [VAMPIRE SPRITE
    What am I even saying? Judging from her expression, I wasn’t doing a very good job at alleviating her fears.
    ]
    [VAMPIRE SPRITE
    Claire:
    “...”
    ]
    [VAMPIRE SPRITE
    Now I’ve done it. As I kept rambling on, Claire’s face had grown more and more downtrodden.
    ]
    [
    Her gaze never parting from her lap and her fidgeting hands, I sigh as I resolve to ask something stupid.
    ]
    [VAMPIRE SPRITE
    MC:
    “What’s the rabbit’s name? If you don’t mind me asking.”
    ]
    [VAMPIRE SPRITE
    Claire:
    “...”
    ]
    [VAMPIRE SPRITE
    With a small pause of her hands she slowly looks up at me, her crimson eyes having grown a little puffy around the edges..
    ]
    [VAMPIRE SPRITE
    Claire:
    “Elly...her name is Elly.”
    ]
    [VAMPIRE SPRITE
    MC:
    “That’s a nice name. You know you don’t have to hide her if you don’t want to, it sounds like she means a lot to you.”
    ]
    [VAMPIRE SPRITE
    Claire:
    “A-Are you sure? Wouldn’t it bother you?”
    ]
    [VAMPIRE SPRITE
    MC:
    “Really, it’s fine. If it makes you feel more at ease then by all means, go ahead.”
    ]
    [
    Her lips curling into a tiny smile, I watch as Claire hops up from her seat and runs off towards the closet.
    ]
    [
    In only a few moments she’s back with the small stuffed rabbit cradled in her arms, its black tufts of fur a fitting match to her dress.
    ]
    [
    Seeing it more up close, I notice a few bits and pieces of brown fabric sewn into different parts of the plush, one of the rabbit’s eyes consisting of a different colored and much newer button than the other.
    ]
    [
    It was clear that the rabbit plush had seen its fair share of years.
    ]
    [
    But whether the rabbit was old or not didn’t seem to matter much to Claire. Sitting across from me, her rabbit nestled in her lap, Claire looks calm, or at least calmer than she had ever been in speaking with me.
    ]
    [
    MC:
    “How long have you had Elly?”
    ]
    [VAMPIRE SPRITE
    Claire:
    “Oh, I’ve had her for a long, long time...she was a gift from a friend.”
    ]
    [VAMPIRE SPRITE
    MC:
    “Oh wow, that’s really nice of them! Is she supposed to be coming over today? You know because you have tea and all these things set up. I’m not intruding or anything am I?”
    ]
    [VAMPIRE SPRITE SAD
    Claire:
    “N-No! No, don’t worry about that. She, uh, I-I mean I—we moved! My family I mean. We...we lived overseas. I wasn’t from this town originally.”
    ]
    [VAMPIRE SPRITE SAD
    Yeah, that would make some sense.
    ]
    [VAMPIRE SPRITE SAD
    MC:
    “Really? How long ago did you move into St. Marie? Or, the woods I guess?”
    ]
    [VAMPIRE SPRITE SAD
    Claire:
    “Oh, we’ve been living here for quite some time. However if you’d ask me when I...I’m afraid I’m not capable of being very specific.”
    ]
    [VAMPIRE SPRITE SAD
    MC:
    “No worries, I was just curious. But yeah about your family, are they coming home anytime soon? I think I really need to talk to them.”
    ]
    [VAMPIRE SPRITE SAD
    MC:
    “I kinda messed up the door on my way in, and then you know there’s that smashed clock outside. I don’t want them to think that someone broke in to hurt you, nor would I want you to get the blame for it either. What do you think I should do?”
    ]
    [VAMPIRE SPRITE SAD
    The small rabbit hugged close to her chest, its floppy ears coming up to her chin, Claire sits quietly for a few moments as she looks down at the empty cups of tea adorning the table in front of her.
    ]
    [VAMPIRE SPRITE SAD
    Sighing, she looks at a nearby window and out towards the woods, the leafy boughs of the nearby trees now a dark black as the sun dips beneath the horizon.
    ]
    [VAMPIRE SPRITE SAD
    Claire:
    “They’re gone, my family. They don’t live here anymore…”
    ]
    [VAMPIRE SPRITE SAD
    MC:
    “Wait, you mean you live here on your own?”
    ]
    [VAMPIRE SPRITE SAD
    Claire nods, her gaze far away as she ponders my questions.
    ]
    [
    The first slivers of moonlight begin to break through from the sea of trees outside, and as they flood into the room and shine onto Claire’s face they give her pale hair and skin an unnatural glow, causing her crimson eyes to become more pronounced.
    ]
    [
    Yet despite her outlandish appearance, I get the feeling of something familiar. It was there in the way she talked, in her willingness to treat and confide in a complete stranger.
    ]
    [
    It was something that I had lived with for years, having a home and a family yet feeling as though I had been living with complete strangers underneath the same roof.
    ]
    [
    It was something that had only worsened over time after the news of my uncle’s death, forcing me to look for a place I considered home, a place where I belonged.
    ]
    [
    As Claire stares out towards the window, her face growing stoic and unreadable, I can see it in the faint twitch of her eyes, the quivering of her bottom lip as she stifles a cry driven from a painful memory. Claire was lonely.
    ]
    [
    MC:
    “So that’s why you invited me in…”
    ]
    [VAMPIRE SPRITE SAD
    Claire:
    “Huh?”
    ]
    [VAMPIRE SPRITE
    Hearing my voice, Claire loses her train of thought and looks over at me in confusion.
    ]
    [
    MC:
    “It’s...nothing. I was just thinking. So when was the last time you ever had someone visit your house? You seemed more surprised than scared when you saw me.”
    ]
    [VAMPIRE SPRITE
    Claire:
    “O-Oh, right...To be honest I can’t seem to remember. It’s been so long…”
    ]
    [VAMPIRE SPRITE
    MC:
    “Do you still go out sometimes?”
    ]
    [VAMPIRE SPRITE
    Claire:
    “No! Well, I mean yes—but only sometimes! Although, I can’t really be around people for too long. Things can get a little awkward…”
    ]
    [VAMPIRE SPRITE
    MC:
    “Well you’ve been around me, and if it means anything I don’t think you’re awkward. A little shy yeah, but you’ve been able to talk to me for like, what? A few hours now?”
    ]
    [VAMPIRE SPRITE
    MC:
    “I just think you could use some more practice talking to people, maybe try getting out a little more?”
    ]
    [VAMPIRE SPRITE
    Claire:
    “I see...That’s very kind of you to say. I don’t mean to impose, but maybe you cou—”
    ]
    [VAMPIRE SPRITE
    Before having a chance to properly respond, Claire’s voice is drowned out by the heavy toll of a clocktower.
    BGS CLOCKTOWER]
    [
    Looking down at my phone to check the time my eyes widen and I immediately jump to my feet, startling the young girl.
    ]
    [VAMPIRE SPRITE
    MC:
    “Damn,  I guess I just lost track of time. I have some family waiting at home and I promised that I’d be home by now, any later and I won’t be able to hear the end of it.”
    ]
    [
    With a nervous laugh, I ready my bag and start making my way towards the door, but upon catching a glimpse of Claire’s face,
    ]
    [
    the same face that she had donned earlier when thinking of her parents, I stop and turn around to face her.
    ]
    [
    MC:
    “I’ll be back tomorrow. I was planning on bringing some supplies to try and get your clock fixed, maybe some stuff for your door too. Is that okay with you?”
    ]
    [
    Upon hearing this I notice Claire’s face brighten up, the corners of her lips curled upwards into a tiny smile as she nods.
    ]
    [VAMPIRE SPRITE
    Claire:
    “Y-Yes, that would be fine.”
    ]
    [
    MC:
    “Alright then, I’ll see you tomorrow.”
    ]
    [
    With a smile and a wave, I close the door shut behind me and make my way down the hall and past the grand staircase.
    ]
    [
    Reaching the front doors and leaving Claire’s house the same way I had entered it, I’m met with a cool summer wind and the darkness of a forest night.
    BG CHANGE TO CHATEAU_EXTERIOR]
    [
    Taking a moment to take out a flashlight from my bag and to zip up my jacket, I start making the trek back home, hoping that I could make it in time before Aunt Mildred does.
    BG FOREST2 then BG FOREST1 then BG HOUSE_EXTERIOR, then BG MCROOM(dark)]

    [MINI TIMESKIP]

    [
    Laying on my back, the thick walls of Aunt Mildred’s house trapping in the sweltering summer heat and causing me to kick off the covers, I find myself having trouble sleeping.
    ]
    [
    I had returned home a few minutes before my aunt did, some issue with traffic causing her to return much later than she thought she would.
    ]
    [
    After having a quick dinner of leftover meatloaf and ingesting her first dosage of medication, Aunt Mildred had grown really tired and had decided to return to her room for the day, her eyelids already heavy with sleep as she walked her way down the hall.
    ]
    [
    Figuring that I didn’t really have anything better to do, I decided to follow her lead by heading towards my room.
    ]
    [
    Yet, despite my best efforts, there are simply too many things going through my head in order for me to sleep properly.
    ]
    [
    Suddenly, hearing a bunch of noises coming from outside my window towards the back of the house, my eyes begin to widen.
    ]
    [
    Unsure of what person or what thing could be lurking out in the shadows, I get out of bed and grab ahold of the nearest weapon I can find, a thin golf club that my uncle had seemingly left stored with the rest of his things.
    ]
    [
    Heading towards the front door with a spare set of keys that I snatch up from the kitchen counter, I take careful steps to make sure that Aunt Mildred doesn’t wake up,
    worried at what sleep deprivation would do to her health.
    ]
    [
    As I step outside, I stop for a moment to try and listen, my heart beating against my chest in nervous anticipation.
    ]
    [
    The rustling of the nearby trees and bushes is loud, much too loud to have been from any sort of raccoon or smaller animal.
    ]
    [
    With a flashlight in one hand and the golf club in the other, I gently close the front door to reduce any noise and hesitate before flicking on the flashlight.
    BG CHANGE TO FOREST_FROM_HOUSE]
    [
    Pointing my flashlight towards the source of the noise, I come across a pair of glowing red eyes, the light glinting off of them and giving them an air of intensity.
    ]
    [
    The eyes sharpening as if in surprise, they stare at me while frozen in place.
    ]
    [
    Even with the flashlight shining directly onto them, the source of the eyes is unintelligible, the low hanging branches of the trees and the dense foliage of the nearby berry bushes causing the creature to be obscured by darkness.
    ]
    [
    Caught in a staring match with the unknown beast, the silence is drowned out by the sound of my heartbeat pounding in my ears.
    ]
    [
    I can’t move. As I’m forced to stare back at this unknown presence, I can’t help but notice the hunger in its eyes as it watches me, telling me that with one wrong move and it would all be over.
    ]
    [
    Gritting my teeth, I tighten the grip of my golf club and resign myself to my fate. Yet as I ready my weapon the pair of eyes suddenly run off from whence they came, their heavy footfalls echoing from between the dense forest trees.
    ]
    [
    Unsure of what to make of the situation, but feeling a little relieved, I take a few steps back and decide that it would be best to return to the house for now.
    ]
    [
    Once again making sure that the door closes quietly, I set down the set of keys and the flashlight on the nearby countertop and make a trip towards each of the doors,
    ]
    [
    making sure that each is locked in case whatever thing I saw outside was smart enough to try and enter the house.
    ]
    [
    Feeling a bit more satisfied, I take a moment to check on Aunt Mildred as she sleeps to ensure that she doesn’t need anything before heading back to bed.
    ]
    [
    Plopping down onto the firm mattress with a sigh, my eyelids grow heavy as my mind races to piece together the events that had just happened, my head growing increasingly groggy as I begin to drift off into a deep sleep.
    ]
    [
    The sound of the nearby clock tower welcoming me to a night filled with whatever my dreams have in store.
    ]
return
