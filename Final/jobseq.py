n = int(input())
p = list(map(int, input().split()))
d = list(map(int, input().split()))
jobs = sorted(zip(p, d), reverse=True)
slots = [False] * max(d)
profit = 0
for pr, dl in jobs:
    for i in range(min(dl, len(slots)) - 1, -1, -1):
        if not slots[i]:
            slots[i] = True
            profit += pr
            break
print(profit)

##########################################################################################

def job_sequencing(n, profits, deadlines):
    jobs = sorted(zip(profits, deadlines), reverse=True)  # Sort by profit descending
    max_deadline = max(deadlines)
    slots = [False] * max_deadline
    profit = 0

    for pr, dl in jobs:
        for i in range(min(dl, max_deadline) - 1, -1, -1):  # Find a free slot before deadline
            if not slots[i]:
                slots[i] = True
                profit += pr
                break
    return profit

if __name__ == "__main__":
    n = int(input("Enter number of jobs: "))
    profits = list(map(int, input("Enter the profits of the jobs: ").split()))
    deadlines = list(map(int, input("Enter the deadlines of the jobs: ").split()))
    
    result = job_sequencing(n, profits, deadlines)
    print("Maximum Profit:", result)
