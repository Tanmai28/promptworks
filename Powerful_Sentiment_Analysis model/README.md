## Built a live app for a powerful sentiment analysis model

This model can take any sentence you give it and tell you if it’s POSITIVE or NEGATIVE. Utilized the impressive Transformers library from Hugging Face to obtain a state-of-the-art model without requiring any training.

**Gradio**. It’s a pure Python library that lets you build and share a web UI for any ML model with just a few lines of code. It’s designed by and for the ML community, which means it understands exactly what we need: speed and simplicity.
It's like a UI wrapper for Python function. You give it a function (your model’s prediction logic), tell it what the inputs and outputs look like (e.g., an image input, text output), and it does all the heavy lifting of creating an interactive web app.

**Step 1: The Setup**

First, let’s install the two necessary libraries - gradio and transformers

**Step 2: Writing The Code**

 - Used a pipeline(“sentiment-analysis”) to load a powerful, pre-trained model from Hugging Face in one line. No training required!
 - Created analyze_sentiment(text). This function is the heart of our app. It takes text as input, passes it to our model, and formats the output into a simple dictionary.

The **gr.Interface(…)** call is where everything happens. We tell it:

 - fn = analyze_sentiment: Use our function to do the work.
 - inputs = gr.Textbox(…): The user should get a text box to type in.
 - outputs = “label”: The output should be displayed as a clean label.
 - title & description: Some nice text to make our app look professional.
 - iface.launch(): starts the web server.

**Step 3: Run it and Share it Globally**

Output when run it in google colab:

<img width="1919" height="1064" alt="image" src="https://github.com/user-attachments/assets/6917a5a8-bf9f-4e00-90e2-85de7d2ba439" />


The app is live! 🚀 You can check it out here: https://1c056bb2c14bff0200.gradio.live/
