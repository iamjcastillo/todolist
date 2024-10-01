import requests

url = "http://localhost:8000/lists"

seed_data = [
    {
        "tasks": [
            {
                "title": "Task 1",
                "description": "First task description",
                "state": "pending"
            },
            {
                "title": "Task 2",
                "description": "Second task description",
                "state": "completed"
            }
        ],
        "category": "Work"
    },
    {
        "tasks": [
            {
                "title": "Task 3",
                "description": "Third task description",
                "state": "pending"
            }
        ],
        "category": "Personal"
    },
    {
        "tasks": [
            {
                "title": "Task 4",
                "description": "Fourth task description",
                "state": "pending"
            },
            {
                "title": "Task 5",
                "description": "Fifth task description",
                "state": "pending"
            }
        ],
        "category": "Chores"
    },
    {
        "tasks": [
            {
                "title": "Task 6",
                "description": "Sixth task description",
                "state": "completed"
            }
        ],
        "category": "Fitness"
    },
    {
        "tasks": [
            {
                "title": "Task 7",
                "description": "Seventh task description",
                "state": "pending"
            },
            {
                "title": "Task 8",
                "description": "Eighth task description",
                "state": "completed"
            }
        ],
        "category": "Study"
    },
    {
        "tasks": [
            {
                "title": "Task 9",
                "description": "Ninth task description",
                "state": "pending"
            }
        ],
        "category": "Hobbies"
    },
    {
        "tasks": [
            {
                "title": "Task 10",
                "description": "Tenth task description",
                "state": "completed"
            },
            {
                "title": "Task 11",
                "description": "Eleventh task description",
                "state": "completed"
            }
        ],
        "category": "Shopping"
    },
    {
        "tasks": [
            {
                "title": "Task 12",
                "description": "Twelfth task description",
                "state": "pending"
            }
        ],
        "category": "Errands"
    },
    {
        "tasks": [
            {
                "title": "Task 13",
                "description": "Thirteenth task description",
                "state": "completed"
            },
            {
                "title": "Task 14",
                "description": "Fourteenth task description",
                "state": "pending"
            }
        ],
        "category": "Work"
    },
    {
        "tasks": [
            {
                "title": "Task 15",
                "description": "Fifteenth task description",
                "state": "completed"
            }
        ],
        "category": "Learning"
    }
]

for data in seed_data:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Data seeded successfully: {data}")
    else:
        print(f"Failed to seed data: {data}")
        print(f"Status Code: {response.status_code}, Response: {response.text}")
