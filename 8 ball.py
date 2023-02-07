import random, time
print ("Welcome to the magic 8 ball.")

answers = ['Maybe.',
           'You should definately go for it.',
           'Do it!!!',
           'I cannot advise you on this.',
           'No, you must not do that.',
           'I think you need professional help.',
           'We will see.',
           'Only time will tell.',
           'May the odds be forever in your favour.']

question = input("Please ask me a question> ")

print ("Calculating")
time.sleep(2)
print (random.choice(answers))
