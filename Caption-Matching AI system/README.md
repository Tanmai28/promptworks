**Multimodal AI** - It refers to models that process and understand multiple types of data, like text, images, audio, and video, simultaneously. These models can analyze an image, read a sentence, and understand how both relate. OpenAI’s CLIP (Contrastive Language-Image Pretraining) is one of the most powerful examples. Trained on 400 million (image, text) pairs, CLIP can “see” an image and “read” text in the same semantic space, which allows you to compare the two directly.


**Built a caption-matching AI system that:**
 - Takes an input image (say, a cup of tea)
 - Compares it to a list of 70+ potential captions
 - Returns the Top 5 captions that best describe the image, using cosine similarity
   
Built all of this using Python, PyTorch, and Hugging Face Transformers.

**Step 1: Load and Preprocess the Image**

 - Used Pillow to load the image and CLIPProcessor to tokenize it for the CLIP model

**Step 2: Extract Image Embeddings with CLIP**

 - Next, used CLIPModel to extract feature embeddings from the image

**Step 3: Match the Image to the Captions**

 - Now, compared the image features to the text features of all possible captions. Here I used cosine similarity to find how closely the image vector aligns with each caption vector.

**Step 4: Wrap It All Together**

 - wrote the final function for our multimodal AI model and try it out on an image



**Sample Input Taken:**

![lotus](https://github.com/user-attachments/assets/705c0e07-6f6c-46ae-b9b3-7029fdfed77f)

**Output for the image taken:**

<img width="1919" height="784" alt="image" src="https://github.com/user-attachments/assets/2292f309-11bc-429d-b028-a1c44416da87" />


