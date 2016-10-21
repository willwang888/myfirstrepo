# https://www.careercup.com/question?id=5723093194506240

def getCompleteTime(tasks, waitBetweenRepeatedTask):
	time = 0	# clock
	record = {}	# record[t] represents last time t is done
	for t in tasks:
		if t in record and time - record[t] < waitBetweenRepeatedTask:
			# wait the cooldown
			time = record[t] + waitBetweenRepeatedTask
		# execute t
		time += 1
		# update record
		record[t] = time
	return time

# tests
tasks = [1, 2, 3, 4]
k = 3
print(tasks, k)
print(getCompleteTime(tasks, k))

tasks = [1, 2, 1, 4]
k = 3
print(tasks, k)
print(getCompleteTime(tasks, k))

tasks = [1, 1, 1, 1]
k = 3
print(tasks, k)
print(getCompleteTime(tasks, k))

tasks = [1, 2, 3, 1, 3, 2, 4, 1]
k = 4
print(tasks, k)
print(getCompleteTime(tasks, k))



