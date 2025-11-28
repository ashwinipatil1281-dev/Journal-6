import sys
if len(sys.argv) < 2:
    print("Usage : python scores-main.py <s1> <s2> ...")
    sys.exit(1)

scores = [float(x) for x in sys.argv[1:]]
total = sum(scores)
avg = total / len(scores)

print("Scores :", scores)
print("Sum :", total)
print("Average :", avg)