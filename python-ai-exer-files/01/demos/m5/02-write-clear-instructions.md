# Write Clear Instructions

## Include Details in Your Query to Get More Relevant Answers
Including details in your query is a good strategy for creating more effective prompts because it provides contextual clarity, helping the model understand the context of your request thus making it easier to generate relevant answers. Additionally, these details allow specifying the requirements more precisely which reduces misinterpretation, tailoring the responses to your specific preferences or criteria... improving the quality of the responses. This is particularly important when dealing with domain-specific questoins or topics.

### Execute This Prompt

User
```
What is an LLM?
```

### Now Try Again with a User Role

User
```
Respond only in the context of machine learning, artificial intelligence and GPTs
```

User
```
What is an LLM?
```

Now the answer is better, but with several options.

### Even Clearer

User
```
Respond only on topics that are related to GPT models and not other fields.
```

User
```
What is an LLM?
```

Now the answer is better.


## Ask the Model to Adopt a Persona and Specify Desired Length
Use the system message to specify the persona used by the model in its replies. Also, indicate the desired length of the response.

### Write a Thank You Note

User
```
Write a thank you message in to my neighbor for helping me with my car last night.
```

It is a little bit long and not with the tone I would like to use.

### Try This

System
```
Your response will be a text overflowing with euphoric comments, each paragraph resonating with intense and vivid human emotions
```

User
```
Write a thank you message to my neighbor for helping me with my car last night. Your response should be at a maximum two paragraphs.
```

## Use Delimiters to Clearly Indicate Distinct Parts of the Input

User
```
Get keywords from text delimited by triple quotes.

"""
Large language models, such as OpenAI's GPT-3, play a crucial role in advancing natural language processing and enabling a wide range of applications. These models are important because they demonstrate an unprecedented ability to generate human-like text, comprehend nuanced language, and provide accurate and context-aware responses to queries. By training on vast amounts of data, large language models capture the complexities of language, making them valuable tools for improving automated writing, chatbots, content creation, translation, and many other language-based tasks. Moreover, they inspire further research in AI and foster innovation in various industries, driving us closer to more efficient and effective ways of communicating with computers.
"""
```

## Specify the Steps Required to Complete a Task

System
```
Use the following step-by-step instructions to respond to user inputs.

Step 1 - The user will provide you with text in triple quotes. Get the keywords from this text with a prefix that says "Keywords: ".

Step 2 - Translate the summary from Step 1 into Spanish, and French, with a prefix that says "Translation: ".
```

User
```
"""
Large language models, such as OpenAI's GPT-3, play a crucial role in advancing natural language processing and enabling a wide range of applications. These models are important because they demonstrate an unprecedented ability to generate human-like text, comprehend nuanced language, and provide accurate and context-aware responses to queries. By training on vast amounts of data, large language models capture the complexities of language, making them valuable tools for improving automated writing, chatbots, content creation, translation, and many other language-based tasks. Moreover, they inspire further research in AI and foster innovation in various industries, driving us closer to more efficient and effective ways of communicating with computers.
"""
```
 
 