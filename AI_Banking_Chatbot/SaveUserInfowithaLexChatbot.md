## Save User Info with a Lex Chatbot


### STEP 1: **Remember information stored in CheckBalance**

<img width="1041" height="585" alt="image" src="https://github.com/user-attachments/assets/cf3a824f-34a1-4f74-a953-221cf338a1db" />


**💡 What are context tags?**
 - Context tags in Amazon Lex are used to store and check for specific information across different parts of a conversation. They help save the user from having to repeat certain information
 - There are two types of context tags in Amazon Lex:
       - Output context tag: This tells the chatbot to remember certain details after an intent is finished, so other parts of the conversation can use this stored information later. For example, the account type from BalanceCheck could be saved and reused.
       - Input context tag: This checks if specific details are already available before an intent activates. For example, FollowupCheckBalance will check if this conversation already has the user's date of birth saved somewhere, so it won't need to ask for that information again.


<img width="828" height="447" alt="image" src="https://github.com/user-attachments/assets/f0661ca6-e831-40f2-8e52-6f947450150a" />


### STEP 2: **Create the FollowupCheckBalance intent**

 1. Choose Add intent.
 2. Choose Add empty intent.
 3. Under the Intent details pane, use the following properties to set up your next intent:
            Name: FollowupCheckBalance
            Description: Intent to allow a follow-up balance check request without authentication.

Under the Contexts pane, select contextCheckBalance from the Input context:


<img width="638" height="276" alt="image" src="https://github.com/user-attachments/assets/85d8c7d7-3897-4569-8bfd-f13ea1662902" />

**Add a new slot:**

  Name: accountType
  
  Prompt: For which account would you like your balance?
  
  Slot type: accountType


**Add another new slot:**

  Name: dateOfBirth
  
  Prompt: For verification purposes, what is your date of birth?
  
  Slot type: AMAZON.Date


### STEP 3: **Finishing Touches for FollowupCheckBalance**


<img width="1153" height="554" alt="image" src="https://github.com/user-attachments/assets/c69b2042-cebb-4f36-9864-83cff06bc89d" />

This tells Amazon Lex that the input context contextCheckBalance should have the value of dateOfBirth in CheckBalance.

<img width="1181" height="1048" alt="image" src="https://github.com/user-attachments/assets/04d383bf-10b2-4186-b8fb-c10b09622690" />



<img width="602" height="1034" alt="image" src="https://github.com/user-attachments/assets/b13c74ed-5f39-42b4-a474-b781ee9f0777" />




   
