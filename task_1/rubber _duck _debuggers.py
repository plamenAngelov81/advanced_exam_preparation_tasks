from collections import deque


def get_reward(num, some_dict):
    for i in some_dict:
        if num in some_dict[i][0]:
            return i


def get_stats(programmers, tasks, my_dict):
    max_points = 241
    decrease_tasks = 2
    while programmers and tasks:
        task_time = programmers.popleft()
        task = tasks.pop()
        time = task_time * task

        if time >= max_points:
            task -= decrease_tasks
            programmers.append(task_time)
            tasks.append(task)
        else:
            my_dict[get_reward(time, my_dict)][1] += 1


time_to_complete_task = deque(int(x) for x in input().split(' '))
number_of_tasks = [int(y) for y in input().split(' ')]

ducky_dict = {
    'Darth Vader Ducky': [range(0, 61), 0],
    'Thor Ducky': [range(61, 121), 0],
    'Big Blue Rubber Ducky': [range(121, 181), 0],
    'Small Yellow Rubber Ducky': [range(181, 241), 0],
}

get_stats(time_to_complete_task, number_of_tasks, ducky_dict)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for element in ducky_dict:
    print(f'{element}: {ducky_dict[element][1]}')
