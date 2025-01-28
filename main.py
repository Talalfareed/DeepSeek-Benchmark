# Import ollama and time modules
from ollama import chat
import matplotlib.pyplot as plt
import time
import sys
import numpy as np

def test(model, Questions) -> float:
  totalTime = 0

  for q in Questions:
    messages = [
      {
        'role': 'user',
        'content': q,
      },
    ]

  

    start = time.time()
    response = chat(model, messages=messages)
    end = time.time()

    print("The time of execution for answer of question (", q, ") is:", 
          (end-start) * 10**3, "ms")
    #print(response['message']['content'])
    totalTime += (end-start)

  print("The average time of execution for model ", model, " is:", totalTime/10)
  return totalTime/10

def main() -> int:
  Questions = ["What is 45 + 67", "Subtract 89 from 150", 
            "Multiply 12 by 15", "Divide 144 by 12", 
            "What is 25 percent of 200", "Convert 3/4 to a decimal", 
            "What is 0.6 as a percentage", "Simplify: 5 + 3 × 2", 
            "What is the square root of 64", "Calculate 2³ + 4²"]

  # Names of the models
  models= ["llama3.1", 'deepseek-r1:1.5b', 'deepseek-r1:7b', 'deepseek-r1:8b']

  results = []

  # Calculate avg time for test
  for model in models:
    print("Using model:", model)
    avg_time = test(model, Questions)
    results.append(avg_time)

  y_pos = np.arange(len(models))

  # Create bars
  plt.bar(y_pos, results)

  # Create names on the x-axis, y-axis
  plt.xticks(y_pos, models)
  plt.ylabel("Time in Secs")

  # Save 
  plt.savefig('benchmarks/result1.png')
  # Show graphic
  plt.show()

  return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit