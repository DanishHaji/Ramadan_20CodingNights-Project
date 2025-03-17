# CLI Todo List Manager

A simple, command-line-based Todo List Manager to help you keep track of your tasks effortlessly. This tool lets you add, list, complete, and remove tasks, all from the convenience of your terminal.

---

## How It Works

This Todo List Manager uses Python's `click` library to provide a user-friendly Command Line Interface (CLI). Tasks are stored persistently in a JSON file (`todo.json`), making them available across sessions. Here's what you can do:

1. **Add tasks**: Create new tasks to keep track of what needs to be done.
2. **List tasks**: View all your tasks, with a status indicator (✅ for completed, ❌ for pending).
3. **Complete tasks**: Mark tasks as completed when you're done.
4. **Remove tasks**: Delete tasks you no longer need from your list.

---

## How to Clone and Use the Project

Follow these steps to clone this repository and start using the Todo List Manager:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DanishHaji/Ramadan_20CodingNights-Project.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd <project-directory>
    ```

3. **Install dependencies**:
    Ensure you have Python installed, then run:
    ```bash
    pip install click
    ```

4. **Run the CLI tool**:
    Use the commands below to manage your tasks:
    - Add a task:
      ```bash
      python todo.py add "Your Task Here"
      ```
    - List tasks:
      ```bash
      python todo.py list_tasks
      ```
    - Complete a task:
      ```bash
      python todo.py complete <task-number>
      ```
    - Remove a task:
      ```bash
      python todo.py remove <task-number>
      ```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to suggest improvements or fix bugs.

---

## License

This project is open-source and available under the MIT License. Feel free to use and modify it as you wish.

---

## Author

Developed by Danish.

---

