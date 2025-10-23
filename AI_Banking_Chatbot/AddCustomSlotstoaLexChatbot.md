## Add Custom Slots to a Lex Chatbot 
              - The goal is to get BankerBot to check users' bank account balance.


### STEP 1: **Create a custom slot for account types**

<img width="2082" height="933" alt="image" src="https://github.com/user-attachments/assets/0b5df732-8036-4406-b029-63a0a198f8dc" />

- Slots are pieces of information that a chatbot needs to complete a user's request. Think of them as blanks that need to be filled in a form. For example, if the intent is to book a table at a restaurant, the chatbot needs specific details like: restaurant name, date, time, number of people.
- Amazon Lex provides many ready-to-use slot types for common information, like dates and times, but you can also create your own custom slot types to fit your specific needs. That's what we're about to do.

<img width="1062" height="507" alt="image" src="https://github.com/user-attachments/assets/ebe2a5b8-1da4-4768-99e9-a3728915ce5c" />
<img width="1409" height="473" alt="image" src="https://github.com/user-attachments/assets/b210f140-6d3e-40bc-9b43-c635b5393b80" />

- Selecting Restrict to slot values makes sure that only the values that you specify will count as a valid accountType! Otherwise, Amazon Lex might use machine learning to accept other values that it frequently encounters from users.
- In our case, we don't want Lex to use machine learning to accept other values. We have a set list of bank account types that we offer - Checking, Savings, and Credit accounts - and we don't offer any other bank account types.
- If Lex starts accepting other values outside of these three, users could end up having conversations about bank account types we don't actually offer! To prevent that from happening, we'll restrict Lex to only acknowledge the bank account types we set up here.


- In this project, we're setting up a new intent that lets users check their bank account balance. Our BankerBot will need to know what bank account type the user is wanting to check, so BankerBot will have to ask for the user's bank account type in the conversation.
- By entering specific slot type values, we make sure that our BankerBot only recognizes and accepts the bank account types we offer—Checking, Savings, and Credit. This prevents any confusion or misunderstandings with the user, as the chatbot won't suggest or accept account types that aren't available.

<img width="1405" height="941" alt="image" src="https://github.com/user-attachments/assets/20521a69-8650-4d91-8622-27172676292b" />


### STEP 2: **Create the CheckBalance intent**

<img width="1052" height="502" alt="image" src="https://github.com/user-attachments/assets/753553f8-5b5e-40da-9a53-3cbd5637725a" />
<img width="1052" height="502" alt="image" src="https://github.com/user-attachments/assets/6e0e73e5-cf02-4628-8c30-a044aba1f4e7" />


💡 **Why do some of the utterances have the text {accountType}?**
- This means that Amazon Lex is now prepared to look for slot values from the user's input.
- If a word fits what's expected for the accountType slot, Lex will automatically fill in that information and won't need to prompt the user for their accountType anymore (saving time for the user)!

<img width="1051" height="660" alt="image" src="https://github.com/user-attachments/assets/0b9f8b44-06c2-4686-9da2-2ab08d3dc661" />
<img width="1052" height="659" alt="image" src="https://github.com/user-attachments/assets/cf4312bd-7a9b-46ed-9d82-26a233dd7a8a" />

**Testing**

<img width="658" height="926" alt="image" src="https://github.com/user-attachments/assets/a6ed3a22-1645-4964-9f5a-8bf044a005ac" />


💡 **Why does my bot say 'Intent CheckBalance fulfilled'?**
- that means your bot has successfully taken in the user's details, but it doesn't actually know how to calculate the bank balance yet.
- Because of this, it just returns the generic closing response to tell you it's finished running the intent.

  <img width="768" height="690" alt="image" src="https://github.com/user-attachments/assets/0ec19605-9e00-4417-bbe5-a78b51083876" />
  








