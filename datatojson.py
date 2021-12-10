
import json

filename = 'rtankiejerk.txt'
start_id = 13000
labels = {
    "11": "Appeal to authority",                                     # Stating that a claim is true because a valid authority or expert on the issue said it was true, without any other supporting evidence offered. We consider the special case in which the reference is not an authority or an expert as part of this technique, although it is referred to as Testimonial in the literature.
    "5": "Appeal to fear/prejudice",                                # Seeking to build support for an idea by instilling anxiety and/or panic in the population towards an alternative. In some cases, the support is built based on preconceived judgments.
    "13": "Black-and-white Fallacy/Dictatorship",                    # Presenting two alternative options as the only possibilities, when in fact more possibilities exist. As an extreme case, tell the audience exactly what actions to take, eliminating any other possible choices (Dictatorship).
    "10": "Causal Oversimplification",                               # Assuming a single cause or reason, when there are actually multiple causes for an issue. It includes transferring blame to one person or group of people without investigating the actual complexities of the issue.
    "3": "Doubt",                                                   # Questioning the credibility of someone or something.
    "4": "Exaggeration/Minimisation",                               # Either representing something in an excessive manner, e.g., making things larger, better, worse (“the best of the best”, “quality guaranteed”), or making something seem less important or smaller than it really is, e.g., saying that an insult was just a joke.
    "8": "Flag-waving",                                             # Playing on strong national feeling (or positive feelings toward any group, e.g., based on race, gender, political preference) to justify or promote an action or idea.
    "20": "Glittering generalities (Virtue)",                        # These are words or symbols in the value system of the target audience that produce a positive image when attached to a person or an issue.
    "1": "Loaded Language",                                         # Using specific words and phrases with strong emotional implications (either positive or negative) to influence an audience
    "9": "Misrepresentation of Someone's Position (Straw Man)",    # When an opponent’s proposition is substituted with a similar one, which is then refuted in place of the original proposition.
    "2": "Name calling/Labeling",                                  # Labeling the object of the propaganda campaign as either something the target audience fears, hates, finds undesirable, or loves, praises.
    "16": "Obfuscation, Intentional vagueness, Confusion",          # Using words that are deliberately not clear, so that the audience can have their own interpretations.
    "17": "Presenting Irrelevant Data (Red Herring)",               # Introducing irrelevant material to the issue being discussed, so that everyone’s attention is diverted away from the points made.
    "14": "Reductio ad hitlerum",                                   # Persuading an audience to disapprove of an action or an idea by suggesting that the idea is popular with groups that are hated or in contempt by the target audience. It can refer to any person or concept with a negative connotation.
    "15": "Repetition",                                             # Repeating the same message over and over again, so that the audience will eventually accept it.
    "6": "Slogans",                                                # A brief and striking phrase that may include labeling and stereotyping. Slogans tend to act as emotional appeals.
    "19": "Smears",                                                 # A smear is an effort to damage or call into question someone’s reputation, by propounding negative propaganda. It can be applied to individuals or groups.
    "12": "Thought-terminating cliché",                             # Words or phrases that discourage critical thought and meaningful discussion about a given topic. They are typically short, generic sentences that offer seemingly simple answers to complex questions or that distract the attention away from other lines of thought.
    "7": "Whataboutism",                                           # A technique that attempts to discredit an opponent’s position by charging them with hypocrisy without directly disproving their argument.
    "18": "Bandwagon"                                               # Attempting to persuade the target audience to join in and take the course of action because “everyone else is taking the same action.”
}

datalist = []
meme_id = start_id
line_action = 0

lines = []
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

i = 0
meme_id = start_id
while i < len(lines) - 1:
    #print(i)
    dataobj = {}
    dataobj["id"] = str(meme_id)

    labelnums = lines[i].split()
    #print(labelnums)
    labellist = [labels[num] for num in labelnums]
    labellist.sort()
    dataobj["labels"] = labellist

    dataobj["text"] = lines[i + 1]

    datalist.append(dataobj)
    i += 2
    meme_id += 1

jsondata = json.dumps(datalist, indent=4)
print(jsondata)




