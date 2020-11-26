import random
def main():
    score = random.randint(0,100)
    print(final(score))
def final(score):
    out_file = open('results.txt', 'w')
    if score < 0 or score > 100:
        print("Invalid score",file=out_file)
    elif score >= 90:
        print("Execelent",file=out_file)
    elif score >= 50:
        print("Passable",file=out_file)
    else:
        print("Bad",file=out_file)
    out_file.close()
main()
