def askYesNoQuestion(question):
  YesNoAnswer = input(question)
  if YesNoAnswer == "who is my dream girl" or YesNoAnswer == "where she resides" or YesNoAnswer == "what is her date of birth":
     return YesNoAnswer
  else:
      print('She is missing you')
      return askYesNoQuestion(question)


a= askYesNoQuestion("Ask anthing : ")
if a == "who is my dream girl":
  print("Mini is your dream girl")
  b = askYesNoQuestion("do you want know more about her : ")
  if b == "where she resides":
    print("she resides in goregaon, mumbai")
    c = askYesNoQuestion("Any specific details you want to know about your dream girl  : ")
    if c == "what is her date of birth":
      print("Her DOB is 3rd December")
      d = askYesNoQuestion("Want to know something else about your dream girl  : ")
      if d == "what she is doing":
        print("She is missing you")
else:
  print("Thank You")
  