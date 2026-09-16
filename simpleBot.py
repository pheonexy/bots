def support_bot():
    faqs = {
        "hours": "We are open Monday to Friday, 9 AM to 6 PM.",
        "when": "We are open Monday to Friday, 9 AM to 6 PM.",
        "location": "Our office is located in Tangier, Morocco.",
        "where" : "Our office is located in Tangier, Morocco.",
        "contact": "You can reach us at support@example.com.",
        "Who": "You can reach us at support@example.com."
    }
    
    while True:
        user = input("You: ").lower()
        if user == "hi":
            print("Bot: Hello")
        elif user in faqs:
            print("Bot:", faqs[user])
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don’t have that information.")
