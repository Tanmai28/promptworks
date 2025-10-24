## Connect Amazon Lex with Lambda
          - The goal is to get BankerBot to check users' bank account balance and return a random bank balance.
                 
### STEP 1: **Create Your AWS Lambda Function**

 - Lex doesn't come with the smarts to calculate bank balances on its own, but luckily it doesn't have to.
 - We'll be using another AWS service, AWS Lambda, to generate a random number on the fly (whenever a user asks for their balance). You can think of Lex as the interface that the user sees and chats with, while Lambda is the calculator that's out of sight but works in the background.
 - Easy peasy, there's no experience with Lambda required to do this. 

**AWS Lambda** is a service that lets you run code in the cloud without needing to manage any computers/servers - Lambda will manage them for you.
Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second - all you need to do is supply your code in one of the languages that Lambda supports.


<img width="1829" height="1062" alt="image" src="https://github.com/user-attachments/assets/88fb0cc0-915c-4a91-93e4-fe32f86b7ffb" />




https://storage.googleapis.com/nextwork_course_resources/courses/aws/AWS%20Project%20People%20projects/Project%3A%20Create%20a%20chatbot%20with%20Amazon%20Lex%20/BankingBotEnglish%20NextWork.py

 - This Python script helps the chatbot give users quick answers about their account balances.
 - When someone asks about their account balance to your chatbot, Lex will ask your Lambda function to run this code, which will pick a random number to pretend it's the balance.
 - Lambda will pass this random number to Lex, who will then push the bank balance figure to the user through your chatbot.


<img width="1543" height="757" alt="image" src="https://github.com/user-attachments/assets/384c1245-088d-4f01-9de7-7d520a2c205e" />




### STEP 2: **Connect AWS Lambda with Amazon Lex**


**💡 What are aliases, why are we using them?**
 - Think of an alias in Amazon Lex as a pointer for a specific version of your bot.
 - So when you're connecting Lex with other AWS services or your custom applications, those external resources will connect to an alias, which will point to the specific version of your bot that you want to use.
 - Now, instead of always updating your apps to connect to the newest version of the bot, you can just update the alias to point to that new version. All your apps will automatically start using the updated bot without needing any changes on their end - this saves developers a TON of time and reduces the risk of errors!


**💡 What is TestBotAlias?**
 - TestBotAlias is a default version of your bot that's made for testing or development.
 - This is the playground version of your bot that you'll use to make sure everything works smoothly before rolling out changes!

<img width="1108" height="781" alt="image" src="https://github.com/user-attachments/assets/3ff3bfcd-c3a8-4e79-9637-85b16b195699" />


**💡 What does $LATEST mean?**
Using the $LATEST version means you're directing your alias to always use the most up to date version of this Lambda function. This setup is a time saver that lets you immediately test any changes in your function.




### STEP 3: **Connect your CheckBalance intent with your Lambda function**

**💡 What is fulfilment?**
- In Amazon Lex, fulfilment means completing the intent. With your BankingBot, after a user tells your bot:
    - The account they want to check, and
    - Their birthday for verification
- The bot has all the information it needs and moves to fulfilment. This is where it will use the Lambda function to get the account balance and pass it back to the user.


**💡 What are code hooks?**
 - Code hooks help you connect your chatbot to custom Lambda functions for doing specific tasks during a conversation.
 - They're used to handle more complex actions that the basic chatbot setup can't do on its own, like checking data from a database or making decisions based on past conversations.
 - Essentially, code hooks make your chatbot smarter and more useful by allowing it to perform these extra steps seamlessly during chats.


<img width="1093" height="436" alt="image" src="https://github.com/user-attachments/assets/0be14464-f94b-4a3b-a25f-8f2d74ffa27e" />



**Testing**

<img width="532" height="709" alt="image" src="https://github.com/user-attachments/assets/e4272727-574e-44a5-8e39-0971f7545fd5" />




