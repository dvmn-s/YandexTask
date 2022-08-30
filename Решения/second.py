
job_to_vacancies_amount = dict([input().split(',') for i in range(int(input()))])

participants = [input().split(',') for i in range(int(input()))]
sorted_participants = sorted(participants, key=lambda x: (-int(x[2]), int(x[3])))

job_to_participants = {}

for participant in sorted_participants:
    job = participant[1]
    if job in job_to_participants:
        job_to_participants[job].append(participant[0])
    else:
        job_to_participants[job] = [participant[0]]


accepted_patricipents = []

for job, vacancies_amount in job_to_vacancies_amount.items():
    accepted_patricipents += job_to_participants[job][0:int(vacancies_amount)]

accepted_patricipents.sort()
print(*accepted_patricipents, sep='\n')

