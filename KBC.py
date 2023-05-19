questions =[ 
             ["Who is the father of computer science?","Alan Turing","Charles Babbage","Ada Lovelace","John McCarthy","B"],
             ["Who is the captain of Pakistan cricket team?","Babar Azam","Sarfaraz Ahmed","Shoaib Malik","Imad Wasim","A"],
             ["Who is the president of Pakistan?","Imran Khan","Arif Alvi","Asad Umar","Shah Mehmood Qureshi","B"],
             ["who is the No.1 odi batsman?","Virat Kohli","Rohit Sharma","Babar Azam","Kane Williamson","C"],
             ["Who is the No.1 odi bowler?","Josh Hazelwod","Trent Boult","Kagiso Rabada","Pat Cummins","A"],
             ["Who is the No.1 t20 batsman?","Babar Azam","Aaron Finch","Virat Kohli","Rohit Sharma","A"],
             ["Who is the No.1 t20 bowler?","Rashid Khan","Mujeeb Ur Rehman","Imad Wasim","Shadab Khan","A"],
]
levels = [10000,20000,30000,40000,50000,600000,7000000]
for i in range(0,len(questions)):
    print("Question",i+1,":",questions[i][0])
    print("A.",questions[i][1])
    print("B.",questions[i][2])
    print("C.",questions[i][3])
    print("D.",questions[i][4])
    ans = input("Enter your answer: ")
    if ans == questions[i][5]:
        print("Congratulations! You have won Rs.",levels[i])
    else:
        print("Wrong Answer And Sorry! You have lost the game")
        break
    print("Your total winning amount is Rs.",levels[i])