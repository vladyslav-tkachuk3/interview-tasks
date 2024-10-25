def maximize_value(tasks, available_time):
    # Sorting tasks in descending order of value to duration ratio
    tasks.sort(key=lambda x: x['value'] / x['duration'], reverse=True)
    
    total_value = 0
    selected_tasks = []
    
    for task in tasks:
        if available_time >= task['duration']:
            available_time -= task['duration']
            total_value += task['value']
            selected_tasks.append(task)
    
    return selected_tasks, total_value

# Test case 1
tasks1 = [
    {'duration': 1, 'value': 1},
    {'duration': 3, 'value': 2},
    {'duration': 4, 'value': 3}
]
available_time1 = 7
selected_tasks1, total_value1 = maximize_value(tasks1, available_time1)
print(f"Selected tasks: {selected_tasks1}, Total value: {total_value1}")

# Test case 2
tasks2 = [
    {'duration': 1, 'value': 1},
    {'duration': 2, 'value': 3},
    {'duration': 3, 'value': 4}
]
available_time2 = 5
selected_tasks2, total_value2 = maximize_value(tasks2, available_time2)
print(f"Selected tasks: {selected_tasks2}, Total value: {total_value2}")
