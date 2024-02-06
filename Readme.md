# Chat Explanations

## Chat 1
[Chat 1 Link](https://chat.openai.com/share/1c306f68-4ef4-420b-966a-f4e981e9d28f) <br>
![Chat 1 Question Image](/Users/aditya/Project/cot1q.png)

**Summary:**
<details>
  <summary style="color: #008080; font-size: 1.2em;">In this chat, I asked ChatGPT to come up with a math expression using some given numbers, just once, using the rules of BODMAS, to get a total of 13. If it couldn't find one, I gave it four steps. First, it had to set up a stack. Then, it could use different math operations and pick equations to throw on the stack. This process had to go on until all the equations were used up.</summary>
</details>

**Key Points:**
<ul style="list-style-type: square; color: #006400;">
  <li>Initialization of Stack</li>
  <li>BODMAS Operations and Stack Modification</li>
  <li>Iterative Search for Solution</li>
</ul>

![Chat 1 Answer Image](/Users/aditya/Project/cot1a.png)

**Summary:**
<details>
  <summary style="color: #008080; font-size: 1.2em;">For the given set of numbers (5, 5, 2, 1), there is no combination of BODMAS operations that results in the value 13. The attempt to find such a combination using various operations and iterating through the possibilities did not yield the desired result. Therefore, the solution is summarized as 'NA' (Not Available).</summary>
</details>


**Insights:**
<blockquote style="background-color: #f0f0f0; padding: 10px; border-left: 5px solid #008080; color: #333;">
  This method of writing Prompt is called as Chain of Thought (CoT)
  
</blockquote>

## Chat 1.1
[Chat 1.1 Link](https://chat.openai.com/share/52fec345-5f19-4782-bbd3-b1b47393aa24) <br>
![Chat 1.1 Question Image](/Users/aditya/Project/cot1-1q.png)

**Summary:**
<details>
  <summary style="color: #008080; font-size: 1em;">In this chat, I made a change in the third step by replacing "Select the result of any equation and append in the stack" with "Select the result of equation which you think can be combined with the remaining numbers of the stack to reach 13." which changed it's approach from taking any equation to selecting a eqn which the GPT thought would fit best</summary>
</details>

**Key Points:**
<ul style="list-style-type: square; color: #006400;">
  <li>Initialization of Stack</li>
  <li>BODMAS Operations and Stack Modification</li>
  <li>Iterative Search for Solution</li>
</ul>

![Chat 1.1 Answer Image](/Users/aditya/Project/cot1-1a.png)

**Summary:**
<details>
  <summary style="color: #008080; font-size: 1em;">For the given set of numbers (5, 5, 2, 1), Combine them using addition and multiplication to get 13. Start with 5 + 5, then add 2 and 1. The equation is 5 + 5 + 2 + 1 = 13.</summary>
</details>


**Insights:**
<blockquote style="background-color: #f0f0f0; padding: 10px; border-left: 5px solid #008080; color: #333;">
By altering the thought process of the LLM we can get our desired result
  
</blockquote>


## Chat 2
![Chat 2 Image](path/to/chat2/image.png)

**Summary:**
<details>
  <summary style="color: #008080; font-size: 1.2em;">Provide a summary of the main content and context of this chat.</summary>
  <p style="color: #333;">Add any personal reflections or observations related to this chat.</p>
</details>

**Key Takeaways:**
<ol style="list-style-type: decimal; color: #800080;">
  <li>Takeaway 1</li>
  <li>Takeaway 2</li>
  <li>Takeaway 3</li>
</ol>

**Reflection:**
<blockquote style="background-color: #f0f0f0; padding: 10px; border-left: 5px solid #800080; color: #333;">
  Share any personal reflections or observations related to this chat.
</blockquote>

## Chat 3
![Chat 3 Image](path/to/chat3/image.png)

**Overview:**
<details>
  <summary style="color: #008080; font-size: 1.2em;">Give an overview of the themes, questions, or information exchanged in this chat.</summary>
  <p style="color: #333;">Share any new information or insights gained from this conversation.</p>
</details>

**Significant Details:**
<ul style="list-style-type: square; color: #800000;">
  <li>Detail 1</li>
  <li>Detail 2</li>
  <li>Detail 3</li>
</ul>

**Learnings:**
<blockquote style="background-color: #f0f0f0; padding: 10px; border-left: 5px solid #800000; color: #333;">
  Share any new information or insights gained from this conversation.
</blockquote>

...
