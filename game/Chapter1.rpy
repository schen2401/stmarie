define attendant = Character("Attendant")
define aunt = Character("Aunt Mildred")
define icom = Character("Intercom")
define mc = Character('[player_name]')
define narrator = Character(None)

# The game starts here.

label Chapter1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #    show eileen happy

    # These display lines of dialogue.

    #    e "You've created a new Ren'Py game."

    #    e "Once you add a story, pictures, and music, you can release it to the world!"

    #   On the Train
    scene b_train_interior_1

    icom "\"Attention all passengers: The train will be stopping at Southshore station in just a few minutes. Please make sure to prepare all of your belongings."

    icom "An attendant will be out shortly to confirm your tickets as well as any proper form of identification. Once again, on behalf of everyone here in Travel corp, we thank you for choosing us and wish you some happy traveling!\""

    narrator """
    With a soft click, the transmission cut off, the sound of the announcer’s voice replaced by the muted rumbling of the train tracks and the soft bustling of eager passengers.

    Taking the announcer’s words to heart, I look down at the bag nestled between my feet and shift it side to side to confirm it still being there. I didn’t bring much with me, just a few changes of clothes, a laptop, and some money to hold me over if I needed it.

    Although on second thought, I probably should’ve brought some more stuff. This summer I had planned to move in with my aunt in Arcadia, a small fishing town miles and miles away from the nearest city.

    Now don’t get me wrong, from what I remember the town has quite a few shops so I’m sure I could find most if not anything I could ask for.

    But last I checked, Arcadia wasn’t the most caught up with the times, its buildings untouched for nearly a century, I wouldn’t be surprised if the latest they have in terms of technology made its debut over forty years ago.

    I had spent most of my childhood growing up in Arcadia before moving to the city with my parents almost ten years ago.

    We had lived in a small house not too far from my aunt and uncle and would help out with his fishing business on occasion, at least until my dad got a job reassignment.

    He had worked on a little startup with some friends the next town over, and it had taken off nicely enough that it allowed them to expand and relocate into the city.

    My mom wasn’t too keen about living in such a small and secluded town, much less as a fisherman’s wife, so the news of a possible relocation had got her pretty excited.

    My brother was too young at the time to really have any thoughts regarding the move, but I remember taking the news pretty hard at the time. Moving away to me meant leaving behind my uncle and all my friends, the few I had that is.

    I remember fighting with my parents for hours to try and get them to change their minds, but no matter how hard I tried it never fully panned out.
    """

    attendant "\"Excuse me, your ticket, and identification please\""

    narrator """
    The weathered voice of the train attendant snaps me out of my thoughts as I glance over to find his hand outstretched, his face warped into a tired expression.

    Digging through my pockets for my wallet, my eyes dart around the room to notice a few nosy passengers watching me. My face reddens, there was no telling how long I had kept the man waiting.

    Growing up, I had always had a bad habit of drifting off into my thoughts, something I wish I had grown out of by now as it always seemed to happen at the most inopportune times.
    """
    menu:
        "Select your gender."
        "Male":
            $ gender = "m"
            jump enter_name
        "Female":
            $ gender = "f"
            jump enter_name

    label enter_name:
        $ player_name = renpy.input("Enter your name: ")
        $ player_name = player_name.strip()

    narrator "Punching a hole into the boarding ticket and giving my identification card a quick glance-over, the attendant hands back my things and barely regards me with a tip of his cap."

    attendant "Thank you for your cooperation, have a happy rest of your trip,” as he makes his way towards the other train cars."

    narrator """
    After the quick send-off, he makes his way towards the other train cars. Letting out a deep sigh, I recline my head against the back of my seat and shut my eyes in embarrassment.

    There were still a few minutes left before our arrival, and after my small scene, I thought it best not to socialize.

    The loud trill of the train whistle pierces the relative silence of the train car as we pull ourselves up towards Southshore station. With a loud gush of wind, the train stops and opens its doors having finally reached its destination.

    The intercom once again blares to life over the excited commotion of the disembarking passengers as the announcer bids them goodbye.

    Picking up my bag and slinging it over my back, I hop up off my seat and slip into the crowd, trying my best to go with the motions as I make my way towards the door.
    """
#   Leaving the Train

#   Enter the station
    scene b_train_station
    play music "audio/INTRO.mp3"

    narrator """
    The sun is almost blinding as I make my way outside, my eyes needing a few moments in order to properly readjust. Squinting, I try making out the face of my aunt amongst the crowds of moving people.

    Catching sight of a large cardboard sign with my name on it and a tiny middle-aged woman almost hidden underneath it, I grin and wave as I make my way over to her.
    """

    mc "\"Auntie Mildred! How long have you been holding that thing? It’s almost twice your size!\""

    narrator "Trying my best to stifle my laughter, I grab ahold of the sign and get ready to take it from her hands."

    show aunt

    aunt "\"Oh shut it, you! I just got here a few minutes ago, and if I don’t make it this big there’s no way you’d ever notice it! You’re a blockhead just like your father.\""

    narrator """
    Laughing at my father and I’s expense, Auntie Elle finally lets go of the massive piece of cardstock. Now face to face, we stand there for a moment in complete silence.

    I’m stunned, right in front of me is the very same aunt that I had spent so much of my childhood with, yet something was wrong.

    The faintest strands of silvery-white hair spilled from beneath the brim of her sunhat despite Auntie Elle’s best efforts to keep them tucked in; while the faint wrinkles of the laugh lines that had framed the corners of her lips were deepened from growing age and years worth of exposure to the sweltering sun.

    Compared to my parents, my aunt and uncle were older by about ten years, meaning that expecting them to look just as young as I had left them would be ridiculous. I knew this, of course I did, yet that wasn’t all.

    Auntie Mildred didn’t look old, she looked ill. There was no flush to her cheeks, her skin tinged instead with a sickly pallor that made no sense for this climate, one that she tried to conceal underneath a layer of rouge and blush.

    Her eyes, nestled underneath the shade of her sunhat, were rimmed with a glossy and yellow sheen, indicating the sickness that she tried so desperately to hide.

    Her hands, like the rest of her body, were unnaturally thin, the wiry muscle I remember her having now eroded as the skin that clung onto her bones was almost as oversized as the clothes that clung onto her body.
    """

    aunt "\"Jesus. Just look at you, feels almost like yesterday that you were runnin’ around catching bugs in my backyard, and now here you are, all grown up!\""

    narrator "Auntie Mildred’s voice snaps me back to reality as she looks up at me, her toothy grin still as strong as ever."

    mc "\"Y-Yeah, it’s been a while,” I say as I curse myself under my breath for zoning out again.\""

    narrator "I say as I curse myself under my breath for zoning out again."

    aunt "\"Ten years huh?\""

    mc "\"Yeah, something like that.\""

    narrator "I scratch my head and take a second to regain my composure before reaching out to grab ahold of Auntie Elle’s hand."

    narrator "As we make our way towards the parking lot, I ask, "

    mc "\"So uh, did you drive here, or did you take the bus?\""

    aunt "\"Bus? You kiddin’ me? Honey, with how spread out this county is you wouldn’t believe how long it’d take me to get here by bus."

    aunt "It takes twenty to thirty minutes just to drive here from Arcadia on my own, now imagine needin’ to stop and pick up some passengers every couple of minutes.\""

    hide aunt

    narrator """
    Shit, she was right. In being both the biggest town out of the entire county and having access to its very own train station, Southshore served as a sort of central hub.

    From here one could take a bus to any place they’d like, but with how long the bus routes can get in these parts, it was always preferable to have some sort of ride to pick you up.
    """

    show aunt

    mc "\"Would you like me to drive?\""

    aunt "\"No no no, don’t you worry about that honey. You’ve had a long trip so don’t you worry about a thing. I’m not that old yet, I can handle at least this much.\""

    mc "\"N-No wait I didn’t mean it like th—\""

    narrator "Sighing, I shake my head as I’m ushered into the passenger’s side of my aunt’s car. Thinking about it more rationally, I guess letting my aunt drive would be the quicker way to get to where we were going."

    hide aunt

    narrator """
    Those ten years in the city didn't do me any favors when it comes to remembering directions; and compared to just letting my aunt drive, fidgeting with a gps would be a bigger hassle since the reception wasn't always the best around these parts.

    Resigning myself with these conclusions, I just make sure to have Auntie Mildred tell me whenever she wants me to take over the wheel.

    """
# Leave Train Station

# On the Road

    scene b_road

    narrator """

    After making sure I was settled in, Auntie Mildred turns the ignition and causes the car to roar to life.

    Pulling out of the train station parking lot, she spares no time in making her way out of the town’s limits, causing the buildings to whiz by as we drive past them.

    In minutes we leave any vestiges of town-life behind as we drive through a winding forest road, the sun gleaming through the cracks between the trees.

    Having lived in the city for so long, I can’t help but roll down the window and take a deep breath of the fresh forest air.

    Closing my eyes, I smile as the wind blows through my hair and face. I stay like that for several moments, taking in all of the sounds and scents that reminded me of my childhood home before finally opening my eyes.

    My vision was spotty, dark amorphous blobs blinking in and out of view after their direct exposure to the sun. I rub my eyes, trying to get them to readjust, but as I do so I catch a glimpse of something.

    There between the endless rows of trees, its image nearly obscured by my spotted vision, I make out what looks to be some sort of building, a very, very large building.

    Catching only a glimpse of it before speeding off further down the road, I turn over to Auntie Mildred.
    """


    mc "\"Hey Auntie, is there anything around these parts?\""

    show aunt

    aunt "\"Nah honey, the closest thing is home and we're still 'bout ten minutes out. Why'd you ask?\""

    mc "\"Oh. Um, it was nothing really. I just thought I saw something in the woods.\""

    aunt "\"Oooo scary! Best make sure you're a good boy once we get to town else 'ol Red Eyes gets you~\""

    hide aunt

    narrator """
    \"Old Red Eyes\" was an urban legend originating in Saint Marie, and growing up, Auntie Mildred made sure to use it at every waking moment to scare the shit out of me.

    Having been passed around and retold for so long it was a bit difficult to make out the specifics, but a few details were always the same: a mysterious crime scene,

    a dead old man, a group of baffled cops, and a pair of red eyes watching from the forest.
    """

    show aunt

    mc "\"H-Hey I'm not a kid anymore, that sorta stuff doesn't work on me! And besides, what I saw was a building, not some, thing.\""

    narrator "Auntie Mildred looks over at my direction for a few moments and shrugs."

    aunt "\"Whole county is pretty old honey, folks don't tend to patch things up till they need to. Wouldn't be surprised if there is a building out there. Maybe one of them old plantations or somethin, we've got a few of those lyin' around."

    hide aunt

    narrator """
    Satisfied with my answer, we spend the remainder of the drive towards town trying to make up for lost time, going back and forth as we answer each other's questions.

    Auntie Mildred asks me how life in the city was like, how things were going in school, how my family was doing, the basics. Yet I could see how each question ignited a spark of life within my aunt's tired eyes, flitting between me and the road in captivated attention.

    I answer her as best as I can, trying my best to leave out some, unsavoury details. There were some things I wanted to talk about, actually a lot of things, but seeing how happy the act of just talking made her, I didn't want to ruin it.

    My problems could wait. In return I ask about the town instead, how much it had changed, what was still there, what wasn't, each tiny bit of information unearthing long forgotten memories.

    Soon enough, as we drive past the city limits and turn into Main street, I can see the answers for myself. The town had remained virtually untouched from how I had last remembered it, almost as if the forest had served as some sort of gateway into the past.
    """

    scene b_street_corner_1

    narrator """
    Almost all of Saint Marie was connected to Main street, a central road that branched off into a series of smaller streets surrounded by shops and small businesses at every corner.

    Following the road down one end would take you to a fork leading down to the docks or to a series of residential areas.

    Going down the other end would eventually lead you back into the forest itself and towards the town of Jackson, the road flanked on either side by the forest and the sea. It was this part of town where my uncle had made his home.
    """

    stop music fadeout 1.0

    # This ends the game.

jump Chapter2
