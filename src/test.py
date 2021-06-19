import spacy
nlp = spacy.load("en_core_web_md")

#Ask question and store input answer
inp_str = input("Commercial real estate investor purchased a property for $12 million dollars in Los Angleles, CA in January 2021, loan matures in January 2031. Amortization for this loans is for 30 years. \n")
inp = nlp(inp_str)

#Correct answer
ans = nlp("Marketing automation is technology that manages marketing processes and multifunctional campaigns, across multiple channels, automatically.")

#Parse answer and store keywords
# keywords = []
# for token in ans:
#     if ans.similarity(nlp(token.lemma_)) > 0.65 and token.lemma_ not in keywords:
#         keywords.append(token.lemma_)

keywords = ['balloon', 'payment', 'reduced', 'refinance', 'full', 'short', 'term', 'capital']

#Parse input and count how many keywords
counter = 0
for token in inp:
    if token.lemma_ in keywords:
        counter += 1

#Write content to report
file = open("report.txt", "w")
file.write("Candidate answer: " + inp_str + "\n")
# file.write("Recorded answer: Marketing automation is technology that manages marketing processes and multifunctional campaigns, across multiple channels, automatically.\n")
# file.write("Similarity of candidate answer to recorded answer: " + str(ans.similarity(inp)) + "\n")
file.write("Keywords in recorded answer: " + str(keywords) + "\n")
file.write("Number of keywords in candidate answer: " + str(counter) + "/" + str(len(keywords)))
file.close()
