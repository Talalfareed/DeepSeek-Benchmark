# Import ollama and time modules
from ollama import chat
import time

Question = ["What is 45 + 67", "Subtract 89 from 150", 
            "Multiply 12 by 15", "Divide 144 by 12", 
            "What is 25 percent of 200", "Convert 3/4 to a decimal", 
            "What is 0.6 as a percentage", "Simplify: 5 + 3 × 2", 
            "What is the square root of 64", "Calculate 2³ + 4²"]

totalTime = 0

model = ["llama3.1", 'deepseek-r1:8b', 'deepseek-r1:7b', 'deepseek-r1:1.5b']

selectedModel = model[0]
print("Using model:", selectedModel)

for q in Question:
  messages = [
    {
      'role': 'user',
      'content': q,
    },
  ]

 

  start = time.time()
  response = chat(selectedModel, messages=messages)
  end = time.time()

  print("The time of execution for answer of question (", q, ") is:", 
        (end-start) * 10**3, "ms")
  #print(response['message']['content'])
  totalTime += (end-start)

print("The average time of execution for model " + selectedModel + " is:", totalTime/10)
