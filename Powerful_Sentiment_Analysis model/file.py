# **POWERFUL SENTIMENT ANALYSIS MODEL**

# This model can take any sentence you give it and tell you if it’s POSITIVE or NEGATIVE. Utilized the impressive Transformers library from Hugging Face to obtain a state-of-the-art model without requiring any training.

#STEP 1: The Setup

!pip install gradio
!pip install transformers

#STEP 2: The Code

import gradio as gr
from transformers import pipeline

# load the pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# define the function that will wrap our model
def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    # gradio works best with dictionary outputs
    return {result['label']: result['score']}

# create the Gradio Interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Enter a sentence here..."),
    outputs="label",
    title="Sentiment Analysis Bot",
    description="Type in a sentence and see if the model thinks it's POSITIVE or NEGATIVE. Built with Gradio and Hugging Face Transformers."
)

# launch the app!
iface.launch()
