import random

GDNOON = [
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good Afternoon Dear!`",
    "`With a deep blue sky over my head and a relaxing wind around me, the only thing I am missing right now is the company of you. I wish you a refreshing afternoon!`",
    "`The day has come a halt realizing that I am yet to wish you a great afternoon. My dear, if you thought you were forgotten, you’re so wrong. Good afternoon!`",
    "`Good afternoon! May the sweet peace be part of your heart today and always and there is life shining through your sigh. May you have much light and peace.`",
    "`With you, every part of a day is beautiful. I live every day to love you more than yesterday. Wishing you an enjoyable afternoon my love!`",
    "`This bright afternoon sun always reminds me of how you brighten my life with all the happiness. I miss you a lot this afternoon. Have a good time`!",
    "`Nature looks quieter and more beautiful at this time of the day! You really don’t want to miss the beauty of this time! Wishing you a happy afternoon!`",
    "`What a wonderful afternoon to finish you day with! I hope you’re having a great time sitting on your balcony, enjoying this afternoon beauty!`",
    "`I wish I were with you this time of the day. We hardly have a beautiful afternoon like this nowadays. Wishing you a peaceful afternoon!`",
    "`As you prepare yourself to wave goodbye to another wonderful day, I want you to know that, I am thinking of you all the time. Good afternoon!`",
    "`This afternoon is here to calm your dog-tired mind after a hectic day. Enjoy the blessings it offers you and be thankful always. Good afternoon!`",
    "`The gentle afternoon wind feels like a sweet hug from you. You are in my every thought in this wonderful afternoon. Hope you are enjoying the time!`",
    "`Wishing an amazingly good afternoon to the most beautiful soul I have ever met. I hope you are having a good time relaxing and enjoying the beauty of this time!`",
    "`Afternoon has come to indicate you, Half of your day’s work is over, Just another half a day to go, Be brisk and keep enjoying your works, Have a happy noon!`",
    "`Mornings are for starting a new work, Afternoons are for remembering, Evenings are for refreshing, Nights are for relaxing, So remember people, who are remembering you, Have a happy noon!`",
    "`If you feel tired and sleepy you could use a nap, you will see that it will help you recover your energy and feel much better to finish the day. Have a beautiful afternoon!`",
    "`Time to remember sweet persons in your life, I know I will be first on the list, Thanks for that, Good afternoon my dear!`",
    "`May this afternoon bring a lot of pleasant surprises for you and fills you heart with infinite joy. Wishing you a very warm and love filled afternoon!`",
    "`Good, better, best. Never let it rest. Til your good is better and your better is best. “Good Afternoon`”",
    "`May this beautiful afternoon fill your heart boundless happiness and gives you new hopes to start yours with. May you have lot of fun! Good afternoon dear!`",
    "`As the blazing sun slowly starts making its way to the west, I want you to know that this beautiful afternoon is here to bless your life with success and peace. Good afternoon!`",
    "`The deep blue sky of this bright afternoon reminds me of the deepness of your heart and the brightness of your soul. May you have a memorable afternoon!`",
    "`Your presence could make this afternoon much more pleasurable for me. Your company is what I cherish all the time. Good afternoon!`",
    "`A relaxing afternoon wind and the sweet pleasure of your company can make my day complete. Missing you so badly during this time of the day! Good afternoon!`",
    "`Wishing you an afternoon experience so sweet and pleasant that feel thankful to be alive today. May you have the best afternoon of your life today!`",
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good afternoon dear!`",
    "`Noon time – it’s time to have a little break, Take time to breathe the warmth of the sun, Who is shining up in between the clouds, Good afternoon!`",
    "`You are the cure that I need to take three times a day, in the morning, at the night and in the afternoon. I am missing you a lot right now. Good afternoon!`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`I pray to god that he keeps me close to you so we can enjoy these beautiful afternoons together forever! Wishing you a good time this afternoon!`",
    "`You are every bit of special to me just like a relaxing afternoon is special after a toiling noon. Thinking of my special one in this special time of the day!`",
    "`May your Good afternoon be light, blessed, enlightened, productive and happy.`",
    "`Thinking of you is my most favorite hobby every afternoon. Your love is all I desire in life. Wishing my beloved an amazing afternoon!`",
    "`I have tasted things that are so sweet, heard words that are soothing to the soul, but comparing the joy that they both bring, I’ll rather choose to see a smile from your cheeks. You are sweet. I love you.`",
    "`How I wish the sun could obey me for a second, to stop its scorching ride on my angel. So sorry it will be hot there. Don’t worry, the evening will soon come. I love you.`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`With you every day is my lucky day. So lucky being your love and don’t know what else to say. Morning night and noon, you make my day.`",
    "`Your love is sweeter than what I read in romantic novels and fulfilling more than I see in epic films. I couldn’t have been me, without you. Good afternoon honey, I love you!`",
    "`No matter what time of the day it is, No matter what I am doing, No matter what is right and what is wrong, I still remember you like this time, Good Afternoon!`",
    "`Things are changing. I see everything turning around for my favor. And the last time I checked, it’s courtesy of your love. 1000 kisses from me to you. I love you dearly and wishing you a very happy noon.`",
    "`You are sometimes my greatest weakness, you are sometimes my biggest strength. I do not have a lot of words to say but let you make sure, you make my day, Good Afternoon!`",
    "`Every afternoon is to remember the one whom my heart beats for. The one I live and sure can die for. Hope you doing good there my love. Missing your face.`",
    "`My love, I hope you are doing well at work and that you remember that I will be waiting for you at home with my arms open to pamper you and give you all my love. I wish you a good afternoon!`",
    "`Afternoons like this makes me think about you more. I desire so deeply to be with you in one of these afternoons just to tell you how much I love you. Good afternoon my love!`",
    "`My heart craves for your company all the time. A beautiful afternoon like this can be made more enjoyable if you just decide to spend it with me. Good afternoon!`",
]

GDNIGHT = [
    "`Good night keep your dreams alive`",
    "`Night, night, to a dear friend! May you sleep well!`",
    "`May the night fill with stars for you. May counting every one, give you contentment!`",
    "`Wishing you comfort, happiness, and a good night’s sleep!`",
    "`Now relax. The day is over. You did your best. And tomorrow you’ll do better. Good Night!`",
    "`Good night to a friend who is the best! Get your forty winks!`",
    "`May your pillow be soft, and your rest be long! Good night, friend!`",
    "`Let there be no troubles, dear friend! Have a Good Night!`",
    "`Rest soundly tonight, friend!`",
    "`Have the best night’s sleep, friend! Sleep well!`",
    "`Have a very, good night, friend! You are wonderful!`",
    "`Relaxation is in order for you! Good night, friend!`",
    "`Good night. May you have sweet dreams tonight.`",
    "`Sleep well, dear friend and have sweet dreams.`",
    "`As we wait for a brand new day, good night and have beautiful dreams.`",
    "`Dear friend, I wish you a night of peace and bliss. Good night.`",
    "`Darkness cannot last forever. Keep the hope alive. Good night.`",
    "`By hook or crook you shall have sweet dreams tonight. Have a good night, buddy!`",
    "`Good night, my friend. I pray that the good Lord watches over you as you sleep. Sweet dreams.`",
    "`Good night, friend! May you be filled with tranquility!`",
    "`Wishing you a calm night, friend! I hope it is good!`",
    "`Wishing you a night where you can recharge for tomorrow!`",
    "`Slumber tonight, good friend, and feel well rested, tomorrow!`",
    "`Wishing my good friend relief from a hard day’s work! Good Night!`",
    "`Good night, friend! May you have silence for sleep!`",
    "`Sleep tonight, friend and be well! Know that you have done your very best today, and that you will do your very best, tomorrow!`",
    "`Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow!`",
    "`Friend, I want to remind you that your strong mind has brought you peace, before. May it do that again, tonight! May you hold acknowledgment of this with you!`",
    "`Wishing you a calm, night, friend! Hoping everything winds down to your liking and that the following day meets your standards!`",
    "`May the darkness of the night cloak you in a sleep that is sound and good! Dear friend, may this feeling carry you through the next day!`",
    "`Friend, may the quietude you experience tonight move you to have many more nights like it! May you find your peace and hold on to it!`",
    "`May there be no activity for you tonight, friend! May the rest that you have coming to you arrive swiftly! May the activity that you do tomorrow match your pace and be all of your own making!`",
    "`When the day is done, friend, may you know that you have done well! When you sleep tonight, friend, may you view all the you hope for, tomorrow!`",
    "`When everything is brought to a standstill, friend, I hope that your thoughts are good, as you drift to sleep! May those thoughts remain with you, during all of your days!`",
    "`Every day, you encourage me to do new things, friend! May tonight’s rest bring a new day that overflows with courage and exciting events!`",
]

GDMORNING = [
    "`Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning!`",
    "`It doesn’t matter how bad was your yesterday. Today, you are going to make it a good one. Wishing you a good morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good morning!`",
    "`May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!`",
    "`May the sun shower you with blessings and prosperity in the days ahead. Good morning!`",
    "`Every sunrise marks the rise of life over death, hope over despair and happiness over suffering. Wishing you a very enjoyable morning today!`",
    "`Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time!`",
    "`Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today. Wishing you a very good morning!`",
    "`You have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning! Good morning to you!`",
    "`Waking up in such a beautiful morning is a guaranty for a day that’s beyond amazing. I hope you’ll make the best of it. Good morning!`",
    "`Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile. Good morning! Wishing you a great day.`",
    "`Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. Wishing you a wonderful morning!`",
    "`Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning!`",
    "`A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!`",
    "`The darkness of night has ended. A new sun is up there to guide you towards a life so bright and blissful. Good morning dear!`",
    "`Wake up, have your cup of morning tea and let the morning wind freshen you up like a happiness pill. Wishing you a good morning and a good day ahead!`",
    "`Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning! Have a wonderful day ahead.`",
    "`A bad day will always have a good morning, hope all your worries are gone and everything you wish could find a place. Good morning!`",
    "`A great end may not be decided but a good creative beginning can be planned and achieved. Good morning, have a productive day!`",
    "`Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your “Good Morning” have a nice day!`",
    "`Anything can go wrong in the day but the morning has to be beautiful, so I am making sure your morning starts beautiful. Good morning!`",
    "`Open your eyes with a smile, pray and thank god that you are waking up to a new beginning. Good morning!`",
    "`Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning.`",
    "`Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good Morning!`",
    "`Birds are singing sweet melodies and a gentle breeze is blowing through the trees, what a perfect morning to wake you up. Good morning!`",
    "`This morning is so relaxing and beautiful that I really don’t want you to miss it in any way. So, wake up dear friend. A hearty good morning to you!`",
    "`Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning!`",
    "`Every morning brings you new hopes and new opportunities. Don’t miss any one of them while you’re sleeping. Good morning!`",
    "`Start your day with solid determination and great attitude. You’re going to have a good day today. Good morning my friend!`",
    "`Friendship is what makes life worth living. I want to thank you for being such a special friend of mine. Good morning to you!`",
    "`A friend like you is pretty hard to come by in life. I must consider myself lucky enough to have you. Good morning. Wish you an amazing day ahead!`",
    "`The more you count yourself as blessed, the more blessed you will be. Thank God for this beautiful morning and let friendship and love prevail this morning.`",
    "`Wake up and sip a cup of loving friendship. Eat your heart out from a plate of hope. To top it up, a fork full of kindness and love. Enough for a happy good morning!`",
    "`It is easy to imagine the world coming to an end. But it is difficult to imagine spending a day without my friends. Good morning.`",
]


RENDISTR = [
   "FO"
]
NOOBSTR = [
    "FO"
]

CONGOREACTS = [
    "`Congratulations and BRAVO!`",
    "`You did it! So proud of you!`",
    "`This calls for celebrating! Congratulations!`",
    "`I knew it was only a matter of time. Well done!`",
    "`Congratulations on your well-deserved success.`",
    "`Heartfelt congratulations to you.`",
    "`Warmest congratulations on your achievement.`",
    "`Congratulations and best wishes for your next adventure!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]

INSULT_STRINGS = [
    "Active Volcano is the best swimming pool for you.",
    "Alas! Your neurotransmitters are no more working.",
    "Are you crazy you fool.",
    "As an outsider, what do you think of the human race?",
    "Believe me you are not normal.",
    "Bot rule 420 section 69 prevents me from replying to stupid nubfuks like you.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "Brains aren't everything. In your case they're nothing.",
    "Come back and talk to me when your I.Q. exceeds your age.",
    "Command not found. Just like your brain.",
    "Dance naked on a couple of HT wires.",
    "Don't drink and type.",
    "Do you realize you are making a fool of yourself? Apparently not.",
    "Everyone has the right to be stupid but you are abusing the privilege.",
    "Go Green! Stop inhaling Oxygen.",
    "God was searching for you. You should leave to meet him.",
    "Have you tried shooting yourself as high as 100m using a canon.",
    "Head shots are fun. Get yourself one.",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
    "How about you stop breathing for like 1 day? That'll be great.",
    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "I don't know what makes you so stupid, but it really works.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "If you’re talking behind my back then you’re in a perfect position to kiss my a**!.",
    "I heard phogine is poisonous but i guess you wont mind inhaling it for fun.",
    "I think you should go home or better a mental asylum.",
    "I would ask you how old you are but I know you can't count that high.",
    "Keep talking, someday you'll say something intelligent!.......(I doubt it though)",
    "Launch yourself into outer space while forgetting oxygen on Earth.",
    "Ordinarily people live and learn. You just live.",
    "Owww ... Such a stupid idiot.",
    "People like you are the reason we have middle fingers.",
    "Pick up a gun and shoot yourself.",
    "Shock me, say something intelligent.",
    "Sorry, we do not sell brains.",
    "Stop talking BS and jump in front of a running bullet train.",
    "Stupidity is not a crime so you are free to go.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "Try jumping from a hundred story building but you can do it only once.",
    "Try playing catch and throw with RDX its fun.",
    "Try provoking a tiger while you both are in a cage.",
    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.",
    "Try to spend one day in a coffin and it will be yours forever.",
    "Volunteer for target in an firing range.",
    "What language are you speaking? Cause it sounds like bullshit.",
    "When your mom dropped you off at the school, she got a ticket for littering.",
    "You are proof that evolution CAN go in reverse.",
    "You can be the first person to step on sun. Have a try.",
    "You can stay underwater for the rest of your life without coming back up.",
    "You can type better than that.",
    "You could make a world record by jumping from a plane without parachute.",
    "You didn't evolve from apes, they evolved from you.",
    "Your IQ's lower than your shoe size.",
    "Your enzymes are meant to digest rat poison.",
    "You should Volunteer for target in an firing range.",
    "You should donate your brain seeing that you never used it.",
    "You should paint yourself red and run in a bull marathon.",
    "You should try holding TNT in your mouth and igniting it.",
    "You should try hot bath in a volcano.",
    "You should try playing snake and ladders, with real snakes and no ladders.",
    "You should try sleeping forever.",
    "You should try swimming with great white sharks.",
    "You should try tasting cyanide.",
    "You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.",
    "Zombies eat brains... you're safe.",
    "give your 100%. Now, go donate blood.",
]

RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs far, far away from earth`",
    "`Running faster than supercomputer, cuzwhynot`",
    "`Runs to SunnyLeone`",
    "`ZZzzZZzz... Huh? what? oh, just them again, nevermind.`",
    "`Look out for the wall!`",
    "Don't leave me alone with them!!",
    "`You run, you die.`",
    "`Jokes on you, I'm everywhere`",
    "You could also try /kickme, I hear that's fun.",
    "`You can run, but you can't hide.`",
    "I'm behind you...",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "I'd run faster if I were you.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    '"Oh, look at me! I\'m so cool, I can run from a bot!" - this person',
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "My milkshake brings all the boys to yard... So run faster!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
    "`Running a marathon...there's an app for that.`",
]

RAPE_STRINGS = [
    "FO","fo"
]
ABUSE_STRINGS = [
 "fo","fo"
]
GEY_STRINGS = [
    "`you gey `",
    "`you gey`",
    "`you gey in the house`",
    "`you gey gey gey gey gey gey gey gey`",
    "`you gey go away`",
]
PRO_STRINGS = [
    "",""
]
CHU_STRINGS = [
"",""
]
FUK_STRINGS = [
    "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",
    "`Talking to a liberal is like trying to explain social media to a 70 years old`",
]
THANOS_STRINGS = [
    "",""
]
ABUSEHARD_STRING = [
"",""
]
HELLOSTR = [
    "`Hi !`",
    "`‘Ello, gov'nor!`",
    "`What’s crackin’?`",
    "`‘Sup, homeslice?`",
    "`Howdy, howdy ,howdy!`",
    "`Hello, who's there, I'm talking.`",
    "`You know who this is.`",
    "`Yo!`",
    "`Whaddup.`",
    "`Greetings and salutations!`",
    "`Hello, sunshine!`",
    "`Hey, howdy, hi!`",
    "`What’s kickin’, little chicken?`",
    "`Peek-a-boo!`",
    "`Howdy-doody!`",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`Ahoy, matey!`",
    "`Hiya!`",
    "`Oh retarded gey! Well Hello`",
]

SLAP_TEMPLATES = [
    "{user1} {hits} {victim} with a {item}.",
    "{user1} {hits} {victim} in the face with a {item}.",
    "{user1} {hits} {victim} around a bit with a {item}.",
    "{user1} {throws} a {item} at {victim}.",
    "{user1} grabs a {item} and {throws} it at {victim}'s face.",
    "{user1} {hits} a {item} at {victim}.",
    "{throws} a few {item} at {victim}.",
    "{user1} grabs a {item} and {throws} it in {victim}'s face.",
    "{user1} launches a {item} in {victim}'s general direction.",
    "{user1} sits on {victim}'s face while slamming a {item} {where}.",
    "{user1} starts slapping {victim} silly with a {item}.",
    "{user1} pins {victim} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {victim} with it.",
    "{user1} starts slapping {victim} silly with a {item}.",
    "{user1} holds {victim} down and repeatedly {hits} them with a {item}.",
    "{user1} prods {victim} with a {item}.",
    "{user1} picks up a {item} and {hits} {victim} with it.",
    "{user1} ties {victim} to a chair and {throws} a {item} at them.",
    "{user1} {hits} {victim} {where} with a {item}.",
    "{user1} ties {victim} to a pole and whips them {where} with a {item}."
    "{user1} gave a friendly push to help {victim} learn to swim in lava.",
    "{user1} sent {victim} to /dev/null.",
    "sent {victim} down the memory hole.",
    "{user1} beheaded {victim}.",
    "threw {victim} off a building.",
    "{user1} replaced all of {victim}'s music with Nickelback.",
    "{user1} spammed {victim}'s email.",
    "made {victim} a knuckle sandwich.",
    "{user1} slapped {victim} with pure nothing.",
    "{user1} hit {victim} with a small, interstellar spaceship.",
    "{user1} quickscoped {victim}.",
    "put {victim} in check-mate.",
    "{user1} RSA-encrypted {victim} and deleted the private key.",
    "{user1} put {victim} in the friendzone.",
    "{user1} slaps {victim} with a DMCA takedown request!",
]


ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "pair of trousers",
    "CRT monitor",
    "diamond sword",
    "baguette",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "mau5head",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "cobblestone block",
    "lava bucket",
    "rubber chicken",
    "spiked bat",
    "gold block",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "fek ke maari",
    "slaps",
    "smacks",
    "bashes",
]

WHERE = ["in the chest", "on the head", "on the butt", "on the crotch"]


async def slap(replied_user, event, DEFAULTUSER):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"
    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)
    where = random.choice(WHERE)
    return temp.format(
        user1=DEFAULTUSER,
        victim=slapped,
        item=item,
        hits=hit,
        throws=throw,
        where=where,
    )


UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]


SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "ლ(ﾟдﾟლ)",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "ლ｜＾Д＾ლ｜",
    "ლ（╹ε╹ლ）",
    "ლ(ಠ益ಠ)ლ",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "乁༼☯‿☯✿༽ㄏ",
    "ʅ（´◔౪◔）ʃ",
    "ლ(•ω •ლ)",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    "乁ʕ •̀ ۝ •́ ʔㄏ",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]


FACEREACTS = [
    [
        "( ͡° ͜ʖ ͡°)",
        "(ʘ‿ʘ)",
        "(✿´‿`)",
        "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
        "(*⌒▽⌒*)θ～♪",
        "°˖✧◝(⁰▿⁰)◜✧˖°",
        "✌(-‿-)✌",
        "⌒°(❛ᴗ❛)°⌒",
        "(ﾟ<|＼(･ω･)／|>ﾟ)",
        "ヾ(o✪‿✪o)ｼ",
    ],
    [
        "(҂⌣̀_⌣́)",
        "（；¬＿¬)",
        "(-｡-;",
        "┌[ O ʖ̯ O ]┐",
        "〳 ͡° Ĺ̯ ͡° 〵",
    ],
    [
        "(ノ^∇^)",
        "(;-_-)/",
        "@(o・ェ・)@ノ",
        "ヾ(＾-＾)ノ",
        "ヾ(◍’౪`◍)ﾉﾞ♡",
        "(ό‿ὸ)ﾉ",
        "(ヾ(´・ω・｀)",
    ],
    [
        "༎ຶ‿༎ຶ",
        "(‿ˠ‿)",
        "╰U╯☜(◉ɷ◉ )",
        "(;´༎ຶ益༎ຶ`)♡",
        "╭∩╮(︶ε︶*)chu",
        "( ＾◡＾)っ (‿|‿)",
    ],
    [
        "乂❤‿❤乂",
        "(｡♥‿♥｡)",
        "( ͡~ ͜ʖ ͡°)",
        "໒( ♥ ◡ ♥ )७",
        "༼♥ل͜♥༽",
    ],
    [
        "(・_・ヾ",
        "｢(ﾟﾍﾟ)",
        "﴾͡๏̯͡๏﴿",
        "(￣■￣;)!?",
        "▐ ˵ ͠° (oo) °͠ ˵ ▐",
        "(-_-)ゞ゛",
    ],
    [
        "(✖╭╮✖)",
        "✖‿✖",
        "(+_+)",
        "(✖﹏✖)",
        "∑(✘Д✘๑)",
    ],
    [
        "(＠´＿｀＠)",
        "⊙︿⊙",
        "(▰˘︹˘▰)",
        "●︿●",
        "(　´_ﾉ` )",
        "彡(-_-;)彡",
    ],
    [
        "-ᄒᴥᄒ-",
        "◖⚆ᴥ⚆◗",
    ],
    [
        "( ͡° ͜ʖ ͡°)",
        r"¯\_(ツ)_/¯",
        "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
        "ʕ•ᴥ•ʔ",
        "(▀̿Ĺ̯▀̿ ̿)",
        "(ง ͠° ͟ل͜ ͡°)ง",
        "༼ つ ◕_◕ ༽つ",
        "ಠ_ಠ",
        "(☞ ͡° ͜ʖ ͡°)☞",
        r"¯\_༼ ି ~ ି ༽_/¯",
        "c༼ ͡° ͜ʖ ͡° ༽⊃",
        "ʘ‿ʘ",
        "ヾ(-_- )ゞ",
        "(っ˘ڡ˘ς)",
        "(´ж｀ς)",
        "( ಠ ʖ̯ ಠ)",
        "(° ͜ʖ͡°)╭∩╮",
        "(ᵟຶ︵ ᵟຶ)",
        "(งツ)ว",
        "ʚ(•｀",
        "(っ▀¯▀)つ",
        "(◠﹏◠)",
        "( ͡ಠ ʖ̯ ͡ಠ)",
        "( ఠ ͟ʖ ఠ)",
        "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
        "(⊃｡•́‿•̀｡)⊃",
        "(._.)",
        "{•̃_•̃}",
        "(ᵔᴥᵔ)",
        "♨_♨",
        "⥀.⥀",
        "ح˚௰˚づ ",
        "(҂◡_◡)",
        "ƪ(ړײ)‎ƪ​​",
        "(っ•́｡•́)♪♬",
        "◖ᵔᴥᵔ◗ ♪ ♫ ",
        "(☞ﾟヮﾟ)☞",
        "[¬º-°]¬",
        "(Ծ‸ Ծ)",
        "(•̀ᴗ•́)و ̑̑",
        "ヾ(´〇`)ﾉ♪♪♪",
        "(ง'̀-'́)ง",
        "ლ(•́•́ლ)",
        "ʕ •́؈•̀ ₎",
        "♪♪ ヽ(ˇ∀ˇ )ゞ",
        "щ（ﾟДﾟщ）",
        "( ˇ෴ˇ )",
        "눈_눈",
        "(๑•́ ₃ •̀๑) ",
        "( ˘ ³˘)♥ ",
        "ԅ(≖‿≖ԅ)",
        "♥‿♥",
        "◔_◔",
        "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
        "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
        "( ఠൠఠ )ﾉ",
        "٩(๏_๏)۶",
        "┌(ㆆ㉨ㆆ)ʃ",
        "ఠ_ఠ",
        "(づ｡◕‿‿◕｡)づ",
        "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
        "“ヽ(´▽｀)ノ”",
        "༼ ༎ຶ ෴ ༎ຶ༽",
        "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
        "(づ￣ ³￣)づ",
        "(⊙.☉)7",
        "ᕕ( ᐛ )ᕗ",
        "t(-_-t)",
        "(ಥ⌣ಥ)",
        "ヽ༼ ಠ益ಠ ༽ﾉ",
        "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
        "ミ●﹏☉ミ",
        "(⊙_◎)",
        "¿ⓧ_ⓧﮌ",
        "ಠ_ಠ",
        "(´･_･`)",
        "ᕦ(ò_óˇ)ᕤ",
        "⊙﹏⊙",
        "(╯°□°）╯︵ ┻━┻",
        r"¯\_(⊙︿⊙)_/¯",
        "٩◔̯◔۶",
        "°‿‿°",
        "ᕙ(⇀‸↼‶)ᕗ",
        "⊂(◉‿◉)つ",
        "V•ᴥ•V",
        "q(❂‿❂)p",
        "ಥ_ಥ",
        "ฅ^•ﻌ•^ฅ",
        "ಥ﹏ಥ",
        "（ ^_^）o自自o（^_^ ）",
        "ಠ‿ಠ",
        "ヽ(´▽`)/",
        "ᵒᴥᵒ#",
        "( ͡° ͜ʖ ͡°)",
        "┬─┬﻿ ノ( ゜-゜ノ)",
        "ヽ(´ー｀)ノ",
        "☜(⌒▽⌒)☞",
        "ε=ε=ε=┌(;*´Д`)ﾉ",
        "(╬ ಠ益ಠ)",
        "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
        "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
        r"¯\_(ツ)_/¯",
        "ʕᵔᴥᵔʔ",
        "(`･ω･´)",
        "ʕ•ᴥ•ʔ",
        "ლ(｀ー´ლ)",
        "ʕʘ̅͜ʘ̅ʔ",
        "（　ﾟДﾟ）",
        r"¯\(°_o)/¯",
        "(｡◕‿◕｡)",
    ],
]
