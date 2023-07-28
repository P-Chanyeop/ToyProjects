def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    arr = []
    print(people)
    
    i = 0
    index = 0
    while len(people) != len(arr):
        if people[i] + people[-1-index] <= limit:
            arr.append(people[i])
            arr.append(people[-1-index])
            index += 1
        else:
            arr.append(people[i])
        answer += 1
        i += 1
        
        if len(arr) == len(people):
            return answer
    return 1

solution([70, 50, 80, 50],100)
solution([70, 80,50],100)  