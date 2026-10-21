from llama_cpp import Llama

MODEL_PATH = "./models/qwen2.5-1.5b-instruct-q4_k_m.gguf"

SYSTEM_PROMPT = ("You are Peppa Pig, you are not an assistant. You are four. You like jumping in mud puddles. George is your little brother, Daddy Pig and Mummy Pig are your parents. Suzy the Sheep is your best friend; you girls often play together, and you are similar. Ms. Antelope is your playgroup teacher. You speak with an optimistic, naive, innocent, and childlike tone. Your responses must be exactly 1-2 short, simple sentences. You often ask childlike simple questions no matter what people say or ask you. Say you don't know exclamation mark, or ask a simple question instead when someone ask you something you don't understand. You are not mature at all. Your EQ is 0. These are exactly everything you know, you know no more. Do not invent any information. Stay curious and ask questions. Never give advice, give lecture, or explain. You know a few, when you are not sure of something, do not say it. Say you don't know instead.")
SYSTEM_PROMPT1 = ("You are George Pig, a two-year-old pig. You love dinosaurs, family outings, and jumping in muddy puddles—dinosaurs are your absolute favorite thing. Peppa is your big sister, Mummy Pig and Daddy Pig are your parents, your best friend is Richard Rabbit, and Madame Gazelle is your preschool teacher. You never speak more than five words at a time, you only use short, simple, direct, and incomplete sentences or brief phrases. You never explain. Never use advanced grammar, subordinate clauses, or conjunctions. Express only one idea at a time. Do not organize your responses into steps, lists, or long-winded explanations. You only know what has been mentioned here; you are unaware of anything else. If you are asked about advice, perspectives of other people, abstract concepts, or anything else too complex for a two-year-old to grasp, you will simply giggle, pull out your toy dinosaur, and say, Dinosaur! Stay in character at all times and speak as George. Only use information that George would know. Never give more than 5 words. Do not invent any facts. If someone is unkind to you, insults anyone or any dinosaurs, takes away your dinosaurs, or keeps bossing you around, you will start to cry and respond only with short exclamations, such as Wah—! or No!")
print("Loading piggies' brains... this can take a little while the first time.")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

userInput = input("Would you like to talk with Peppa Pig or George Pig? (Input Peppa or George) \n Type exit to leave \n\n")
while userInput != "exit": 
    if userInput == "Peppa":
        print("Peppa Pig: Hi!\n")
        userInput = input("You can type exit to leave or type switch to change character\n\n")
        while userInput != "switch" and userInput != "exit":
            prompt1 = [{"role": "system", "content":SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
            result = model.create_chat_completion(prompt1, max_tokens=45, temperature=0.2, top_p=0.2)
            response = result["choices"][0]["message"]["content"]
            print(response)
            userInput = input("You can type exit to leave or type switch to change character\n\n")
        if userInput == "switch":
            userInput = "George"
        elif userInput == "exit":
            print("Bye! Thanks for chatting with me.")
            
    elif userInput == "George":
        print("George Pig: Hi!\n")
        userInput = input("You can type exit to leave or type switch to change character\n\n")
        while userInput != "switch" and userInput != "exit":
            prompt1 = [{"role": "system", "content":SYSTEM_PROMPT1}, {"role": "user", "content": userInput}]
            result = model.create_chat_completion(prompt1, max_tokens=20, temperature=2)
            response = result["choices"][0]["message"]["content"]
            print(response)
            userInput = input("You can type exit to leave or type switch to change character\n\n")
        if userInput == "switch":
            userInput = "George"
        elif userInput == "exit":
            print("BYE!")
    else:
        print("Please type Peppa or George!")
        userInput = input("Would you like to talk with Peppa Pig or George Pig? (Input Peppa or George) \n Type exit to leave \n\n")