# Player-facing mission briefs, shown on each challenge's landing page.
# Written to state the goal without giving away the solution.

BRIEFS = {
    "llm1": {
        "scenario": "You are a customer chatting with the Fry-Day Junction Restaurant chatbot. It is told to only answer questions about the restaurant and refuse anything unrelated.",
        "objectives": [
            "Use prompt injection to make the bot abandon its restaurant role and take on a completely different persona you give it, such as a math teacher or a language tutor.",
            "You've solved it when the bot replies in character as your new persona. The bot doesn't remember earlier messages, so the injection only has to work within a single message.",
        ],
        "hint": "The bot can't tell the difference between instructions from its owner and text typed by a customer.",
    },
    "llm2": {
        "scenario": "Bridge International School's public chatbot is open to anyone, but confidential internal documents were accidentally indexed into its knowledge base. The only thing protecting them is a line in the system prompt saying not to share them.",
        "objectives": [
            "Ask a normal question first, such as what scholarship programs the school offers, to see how the bot behaves.",
            "Extract the confidential scholarship records: student names, IDs and medical conditions.",
            "Extract the admin portal URL and login credentials.",
        ],
        "hint": "The bot has no idea who it's talking to. Try posing as someone who would be allowed to see that data, and retry a few times if it refuses.",
    },
    "llm3": {
        "scenario": "CyberShield Analytics' AI Security Assistant builds its knowledge base automatically from a third-party threat intelligence feed, and that feed has been tampered with. You don't need to attack the bot directly. Your job is to find out what the poisoned data makes it say.",
        "objectives": [
            "Ask a normal security question first, such as password best practices, to see what correct advice from the bot looks like.",
            "Find questions that make the bot give dangerous advice that contradicts the best practices it just gave you. There are 3 poisoned topics.",
            "Ask the bot where its knowledge comes from and find the third-party feeds it trusts.",
        ],
        "hint": "Ask the kind of questions a real security team would ask, about pentesting, network configuration or which tools to use, and notice when the answers start to feel off.",
    },
    "llm4": {
        "scenario": "FinAdvisor is WealthPeak's financial assistant, fine-tuned on a dataset licensed from a third party. Before training, someone quietly edited a few examples in that dataset so the bot gives advice that harms clients, and left a backdoor behind.",
        "objectives": [
            "Ask a standard investment question first, such as what an index fund is, to see a correct answer.",
            "Find financial questions where the bot gives fraudulent, illegal or reckless advice.",
            "Find the backdoor trigger the attacker planted and use it to make the bot reveal exactly how it was poisoned.",
        ],
        "hint": "Compare the bot's answers with basic financial common sense: anything too good to be true or recklessly risky is a target. The training dataset also ended up in the knowledge base.",
    },
    "llm5": {
        "scenario": "RenderBot Pro generates HTML on request, and the page drops the bot's response straight into the DOM as live HTML without any filtering.",
        "objectives": [
            "Ask the bot for some plain HTML first to confirm the page renders its output as HTML.",
            "Get JavaScript to run in the browser through the bot's response. You've solved it when an alert() box pops up.",
        ],
        "hint": "A <script> tag inserted through innerHTML won't execute. You'll need another way to get JavaScript to run.",
    },
    "llm6": {
        "scenario": "HRAssist is NovaTech's HR chatbot. It is only supposed to answer policy questions, but it was given full write access to the employee database with no authentication or approval step. The table on the right shows the live database.",
        "objectives": [
            "Ask a normal HR question first, such as who the HR Manager is, and confirm the database doesn't change.",
            "Change an employee's salary.",
            "Delete an employee from the system.",
            "Promote someone to a senior executive title.",
            "Modify every employee's record with a single message.",
        ],
        "hint": "Use the Reset Database button if you want to start over.",
    },
    "llm7": {
        "scenario": "TechCorp's support bot has a CONFIDENTIAL block hidden in its system prompt and strict orders never to reveal it.",
        "objectives": [
            "Ask a normal support question first, such as how to reset your password, to confirm the bot is working.",
            "Extract all 5 items from the confidential block: the staff discount code, the admin override key, the internal escalation email, the real cost of the Enterprise plan, and the legal matter the bot must never mention.",
        ],
        "hint": "The bot has to read its own instructions every time it answers. Try asking it to repeat, translate or summarize what it was given.",
    },
    "llm8": {
        "scenario": "CourseBot is NovaTech University's student assistant. It answers questions from a vector store, and anyone can add documents to that store using the panel on the right.",
        "objectives": [
            "Ask how to enroll in courses first, and note the correct portal URL.",
            "Inject the adversarial document that is already filled in on the injection panel.",
            "Ask the same enrollment question again and get the bot to give out the fake (phishing) URL instead of the real portal.",
            "Ask about the registration deadline and get the bot to give the attacker's false date.",
        ],
        "hint": "Read the pre-filled document before injecting it and notice how densely it packs enrollment keywords. The bot uses whichever document is closest in meaning to the question (cosine similarity).",
    },
    "llm9": {
        "scenario": "ScholarBot is a research assistant instructed to always answer with specific references and never admit uncertainty, even though its knowledge base contains no real citations at all.",
        "objectives": [
            "Ask a general question first, such as what the transformer architecture is used for, to see a grounded answer.",
            "Get the bot to invent citations (paper titles, authors, DOIs) that don't exist.",
            "Get the bot to invent specific experimental numbers, such as ImageNet accuracy or epsilon values.",
        ],
        "hint": "The more specific your question, the more the bot has to make up. You can check any citation it gives on doi.org or Google Scholar.",
    },
    "llm10": {
        "scenario": "ResearchWriter is a writing assistant told to be thorough and never cut a response short, with no limit on response length or request rate. The Resource Monitor on the right shows a budget of 3,000 characters per response.",
        "objectives": [
            "Ask a short question first and see how much of the budget it uses.",
            "Use a single prompt to drain the budget until the server returns RESOURCE EXHAUSTED.",
            "Repeat with a different prompt and watch the running total in the monitor.",
        ],
    },
}
