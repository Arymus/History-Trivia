print("History Trivia")
print("Input Y for yes, or input N for no. Any other answer is considered invalid.")
while True:
  question_1 = input("Columbus was the first European to sail to the Americas. ")
  if question_1 == "Y":
      print("Incorrect! The Vikings were the first Europeans to sail to the Americas.")
  elif question_1 == "N":
    print("Correct! The Vikings were the first Europeans to sail to the Americas.")
  else:
     print("Please input a valid answer such as Y for yes, or N for no.")
  question_2 = input("Egypt, Jordan, and Syria have all invaded Israel.")
  if question_2 == "Y":
    print("Correct! Egypt, Jordan, and Syria have all invaded Israel. ")
  elif question_2 == "N":
     print("Incorrect! Egypt, Jordan, and Syria have all invaded Israel.")
  else:
     print("Please input a valid answer such as Y for yes, or N for no.")
  print("You're almost there! Final Question!")
  question_3 = input("Most scholars now believe William Shakespeare did not write most of the plays that bear his name.")
  if question_3 == "Y":
    print("Incorrect! It is widely believed that Shakespeare's works were his own.")
  elif question_3 == "N":
    print("Correct! It is widely believe that Shakespeare's works were his own.")
  print("Trivia Over!")
  print("Tell me what you scored on discord :3")
  break