## Creating a new bot from scratch on Amazon Lex.


### STEP 1: **Set up the Lex Chatbot**


<img width="2021" height="927" alt="image" src="https://github.com/user-attachments/assets/e74bbc1f-1b1a-457c-8071-7fbda7cec460" />
<img width="951" height="834" alt="image" src="https://github.com/user-attachments/assets/fc2aa78a-490d-4faa-80e8-8b085f16f140" />
<img width="951" height="834" alt="image" src="https://github.com/user-attachments/assets/638e99a0-e8ed-4d5f-943e-63e9a35fbc31" />

 - Amazon Lex needs the permission to call other AWS services on your behalf, later in this project series you'll be integrating Lex with another service called Lambda!
 - Amazon Lex will only maintain a session for a set length of time. If the user is idle and doesn't add any input for 5 minutes, their session will end.

<img width="1754" height="1430" alt="image" src="https://github.com/user-attachments/assets/c7467c2d-e314-49a5-a1ec-e5b77558476d" />

- These voices are borrowed from Amazon Polly, which is another AWS service all about turning your text into speech!
- When you're using Amazon Lex to build a chatbot, this intent classification confidence score threshold is like a minimum score for your chatbot to confidently understand what the user is trying to say. Setting this to 0.4 means that your chatbot needs to be at least 40% confident that it understands what the user is asking to be able to give a response. So if a user's input is ambiguous and your chatbot's confidence score is below 0.4, it'll throw an error message.


### STEP 2: **Creating the first intent**

- When your bot is created, you will automatically see a page called Intent: NewIntent.
- An intent is what the user is trying to achieve in their conversation with the chatbot. For example, checking a bank account balance; booking a flight; ordering food. In Amazon Lex, you build your chatbot by defining and categorising different intents. If you set up different intents, one single chatbot can manage a bunch of requests that are usually related to each other.

<img width="1212" height="861" alt="image" src="https://github.com/user-attachments/assets/b7847a82-ddb3-493b-adb8-bea6219a0e88" />
<img width="1178" height="483" alt="image" src="https://github.com/user-attachments/assets/23ec4ff5-744c-4da3-bf41-18f8bc15749b" />
<img width="1613" height="976" alt="image" src="https://github.com/user-attachments/assets/ac9abf50-5359-4de9-ac8d-265f96289402" />
<img width="1389" height="627" alt="image" src="https://github.com/user-attachments/assets/4d65a942-ade8-401f-b350-d23987494bbc" />
<img width="867" height="1227" alt="image" src="https://github.com/user-attachments/assets/865e36d2-5f93-464d-ba0f-ecac4910b225" />
<img width="590" height="1002" alt="image" src="https://github.com/user-attachments/assets/6a41c441-f279-417d-8e39-45a0789d5104" />

💡 **How does my chatbot respond to these user inputs?**
 - The first three are successfully recognized - Amazon Lex is able to use its ML techniques to match what you have said against your utterances.
 - But the last two fail, resulting in an Intent FallbackIntent is fulfilled response - meaning Amazon Lex doesn't quite recognize your utterance. We'll learn what FallbackIntent means in the next step.



### STEP 3: **Manage FallbackIntent**

💡 **What is FallbackIntent?**
 - Remember the intent classification confidence score threshold, and how it's been set to 0.4? If your chatbot has a confidence score below 40% for all the intents you've defined (in our case, it's just the WelcomeIntent for now), the FallbackIntent is triggered.
 - Think of it as a custom error message that your chatbot will use to tell the user it doesn't understand their input.

<img width="2703" height="931" alt="image" src="https://github.com/user-attachments/assets/8a159733-9768-4fd0-b1e9-04a589d90067" />
<img width="1420" height="866" alt="image" src="https://github.com/user-attachments/assets/c15d7796-9907-4b49-907f-e7a28c771f2c" />

 - Variations are literally variations of the same Message in the main Message box. When Amazon Lex needs to return a Fallback response, it will randomly choose a message from the group and return that.
 - Variations will give your users a dynamic range of responses, making them sound more conversational!


<img width="620" height="774" alt="image" src="https://github.com/user-attachments/assets/a93d49d3-aa3c-4830-babb-0ca310f4533e" />





