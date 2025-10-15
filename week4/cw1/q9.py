users = [
    {'name': 'Ali', 'email': 'ali@example.com', 'status': 'active'},
    {'name': 'Sara', 'email': 'sara@example.com', 'status': 'inactive'},
    {'name': 'Reza', 'email': 'reza@example.com', 'status': 'active'},
    {'name': 'Maryam', 'email': 'maryam@example.com', 'status': 'active'},
    {'name': 'Nima', 'email': 'nima@example.com', 'status': 'inactive'}
]

welcome_message = list(map(lambda user: f"Dear {user['name']}, welcome back!", filter(lambda user: user['status'] == 'active', users)))

print(welcome_message)