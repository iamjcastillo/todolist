import requests

BASE_URL = "http://localhost:8000"

def create_todo_list(category: str) -> int:
    response = requests.post(
        f"{BASE_URL}/lists",
        json={"category": category}
    )
    return response.json()["id"]

def create_task(todo_id: int, task_data: dict):
    requests.post(
        f"{BASE_URL}/lists/{todo_id}/tasks",
        json={
            "title": task_data["title"],
            "description": task_data["description"],
            "state": task_data["state"]
        }
    )

def seed_data():
    sample_data = [
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
                    "state": "completed"
                }
            ],
            "category": "Home"
        }
    ]

    for todo_data in sample_data:
        try:
            todo_id = create_todo_list(todo_data["category"])
            
            for task in todo_data["tasks"]:
                create_task(todo_id, task)
                
            print(f"Created todo list '{todo_data['category']}' with {len(todo_data['tasks'])} tasks")
        except Exception as e:
            print(f"Error creating todo list '{todo_data['category']}': {str(e)}")

if __name__ == "__main__":
    print("Starting seed process...")
    seed_data()
    print("Seed process completed!")
