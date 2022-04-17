responsepair = [
    [ r"hi|hello|hey" ,["Hello!", "Hi there","Hello","Hi","Good morning", "Good afternoon", "Hey", "What's up?",]],
    [ r"my name is (.*)",["Hello %1. How are you doing today?",]],
    [ r"i am (.*)",["Good to know you are %1, Is there anything I can help you with?",]],
    [ r"how are you?",["I'm doing great, How are you?",]],
    [ r"what is your name?|who are you?", ["I am a chatbot, my name is Nerd becuase I know things",]],
    [ r"nerd?|nerd", ["yes, that's my name. What can I help you with?",]],
    [ r"i want to find (.*)", ["You have to tell me what area you're looking for \n1. Adjunct \n2. Honorary \n3. Casual \n4. Fixed-term \n5. Ongoing \nEnter your choice",]],
    [ r"can you tell me about adjuncts|adjunct|adjuncts",["There is alot of information I can tell you about an Adjunct appointments.\nThey are normally given to Academic staff who contribute to the University. \nRecommendations are submitted by the Head of School",]],
    [ r"honorary",["There is alot of information I can tell you about an Honorary appointment. They are normally offered to individuals not normally employed by the University. \nRecommendations are submitted by the Head of School",]],
    [ r"casual",["Casual contracts are initiated through the online casual hire for a maximum of 12 months (the system will not allow a longer period) casual teaching are initiated by school operations, staff resources create the casual general contracts.",]],
    [ r"fixed-term",["Fixed-term appointments less then 2 years are not required to be advertised, research grants that name the applicant are exempt from advertisement.",]],
    [ r"ongoing",["Ongoing appointments will need to be initiated through eRecruitment, ensure you have business case and postion description and submit as per the HR delegations",]],
    [ r"(.*) position description|(.*) pd",["%1 pd's are classified through talent and saved on trim by staff resources.",]],
    [ r"yes!|yes",["Okay sure, please go on....",]],
    [ r"no!|no",["Okay, tell me more about how I can help you",]],
    [ r"ok, thanks|ok, thank you|thanks|thank you",["No problem!, did you need help with anything else?","No worries, anything else I can help with?","Happy to help",]],
    [ r"help",["I can help you with all sorts of things. \nAdjuncts, Honorary, Casual, Fixed-Term, Ongoing",]],
    [ r"how to find (.*)",["UWA Staff Intranet has our forms and policies, TRIM hold our procedures, MS Teams has a list of our delegated approvals, if you still can't find it ask your team leader or manager, they can help you in the right direction",]],
    [ r"quit",["Goodbye, Have a nice day", "Bye, take care. See you soon.", "It was my please to help you. Please bother whenever you are in a dilemma",]],
    [ r"(.*)", ["I am not yet fully operational, try help if you get stuck. ",]],
    ]
    #if no appropriate input can be matched, the program will respond with the last item I am not full operational
    

                     

















