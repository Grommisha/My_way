users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
]

name = 'misha'
user_id = 1
current_users = list(filter(lambda user: user.get('id') == user_id, users))
for user in current_users:
    user['name'] = name

for user in current_users:
    print(user)