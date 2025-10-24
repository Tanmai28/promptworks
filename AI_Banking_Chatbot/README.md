## AI BankerBot

### In this project, I am creating a chatbot called **BankerBot**, designed for an imaginary banking service. This bot will greet users and be ready to handle conversations through voice or text.


To wrap things up, I've learnt how to:

🚞 Configure multiple slots with a shared slot type: You set up two different slots, sourceAccountType and targetAccountType, that both utilize the same underlying accountType slot. This streamlines data handling in your bot.

👍 Implement a confirmation prompt: You've added a confirmation prompt that repeats the transaction details back to the user for verification.

🎨 Use the conversation flow and visual builder: You've cracked open two awesome features that you could bring into the next time you create a Lex chatbot!

☁️ Automate bot deployment with CloudFormation: You used AWS CloudFormation to automate the deployment of your banking bot. This not only saved time but also made sure all resources were correctly configured and linked! Awesome work deploying infrastructure using code.




**Overview of all the parts:**

🥳 In **Part 1** (WelcomeIntent, FallbackIntent),


- Define a basic intent.
- Create lists of utterances.
- Handling failures i.e. FallbackIntent.
- Define a MessageGroup to provide a semi-random response.
- Build and test your bot using text and speech.
  

🤩 In **Part 2** (CheckBalance), 


- Define a custom slot type.
- Associate custom and built-in slots to your intent.
- Parse slot values from the initial utterance.
  

🤯 In **Part 3** (Lambda function), 


- Set up a Lambda function
- Integrate the Lambda function with your chatbot's alias.
- Use code hooks to perform the final fulfilment step of the intent.

🤪 In **Part 4** (FollowupCheckBalance), 

- Set up context carryover of slot values from one intent to the next.


🤩 In **Part 5** (Deployment), 

- AWS CloudFormation
