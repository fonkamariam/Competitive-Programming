def gradingStudents(grades):
    a=[]
    for i in range(len(grades)):
        if grades[i]>=38:
                if grades[i]%5==0:
                    a.append(grades[i])
                elif grades[i]%5>2:
                    if grades[i]%5==3:
                        a.append(grades[i]+2)
                    if grades[i]%5==4:
                        a.append(grades[i]+1)
                else:
                    a.append(grades[i])
        else:
            a.append(grades[i])
    return (a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
