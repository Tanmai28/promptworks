## Document Analysis using LLMs with python

**Document analysis** refers to extracting, interpreting, and understanding the information contained within a document. Traditionally, this involved manual review or simple keyword-based techniques, but with the rise of Large Language Models (LLMs) like GPT and BERT, LLMs are now preferred for document analysis because they can comprehend context, generate summaries, answer questions, and identify key insights efficiently. 

For the task of document analysis using LLMs, I’ll be using a document that contains the terms of the services offered by Google.

-> You can download this document from here.
https://www.gstatic.com/policies/terms/pdf/20240522/ks8shls0/google_terms_of_service_en_in.pdf 


**Step 1: Extract Text from the PDF**

The first step in document analysis is extracting the content from a PDF file. We can use libraries like pdfplumber to open and read the text from each page of the PDF and save it into a .txt file for further analysis. 

**Step 2: Preview the Extracted Text**

After extracting the text, it’s essential to preview the content to ensure everything is correctly captured. 

**Step 3: Summarize the Document**

To get a high-level overview of the document, we can use a pre-trained summarization model like t5-small. This allows to condense large pieces of text into shorter summaries, which helps you to grasp the most important information.

The pipeline(“summarization”, model= “t5-small”) sets up the summarization model using T5-small, a pre-trained transformer model designed for text summarization. 

The document_text[:1000] specifies the portion of the text to summarize (the first 1000 characters), 

while max_length = 150 and min_length = 30 control the maximum and minimum length of the summary in tokens. 

The do_sample = False parameter ensures deterministic output, meaning the model will not randomly sample from possible summaries but will give the same result every time.

**Step 4: Split the Document into Sentences and Passages**

For more detailed analysis, like question generation, it’s important to split the document into smaller chunks. This step tokenizes the document into sentences and combines them into manageable passages for subsequent steps.

The NLTK library to split the extracted document text into individual sentences using the sent_tokenize() function. 
Then, combine these sentences into manageable passages by setting a word limit of 200 words for each passage. 
This helps ensure that each passage is of a suitable length for further processing by language models, which often have token limits. 
If the current passage exceeds the word limit, it is appended to the passages list, and the process continues until all sentences are grouped into passages.

**Step 5: Generate Questions from the Passages Using LLMs**

The next step is to generate questions based on the document’s content. This helps in understanding key information points and can be used to check the comprehension of the document. 

Here, using a question generation model (T5-based model valhalla/t5-base-qg-hl) from the Hugging Face transformers library to automatically generate questions from text passages. The function generate_questions_pipeline() takes a text passage as input and produces a list of questions. We generate at least three questions for each passage, and if not, we split the passage into smaller parts and generate additional questions. This approach guarantees comprehensive question generation for each passage, and we print the questions along with the corresponding passage for review. 

**Step 6: Answer the Generated Questions Using a QA Model**

After generating the questions, we can use a pre-trained question-answering (QA) model to find the answers within the text. The deepset/roberta-base-squad2 model extracts answers based on the context of the passage. 

Used a question-answering (QA) pipeline with the deepset/roberta-base-squad2 model to answer questions generated from the document passages. The function answer_unique_questions() tracks unique questions in a set to ensure it answers each question only once. As the code processes each passage, it checks whether it has already answered a question; if not, it generates an answer based on the passage’s context. This avoids answering duplicate questions and ensures efficient processing of all relevant queries. 
