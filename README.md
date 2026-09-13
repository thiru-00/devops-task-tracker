# DevOps Task Tracker

A beginner-friendly Python CLI project created to practice **Python programming, Git, GitHub, branching, commits, merging, and basic DevOps workflow**.

The project is being developed incrementally while learning Git and DevOps concepts through hands-on practice.

## 📌 Project Overview

DevOps Task Tracker is a command-line task management application written in Python.

The application allows users to:

* Add new tasks
* Edit task status
* List existing tasks
* Mark tasks as completed
* Delete tasks
* Exit the application

Tasks are currently stored in a Python dictionary during program execution.

## 🛠️ Technologies Used

* Python
* Git
* GitHub
* Linux/Unix command line

## 📂 Current Features

### 1. Add Task

Users can create a new task.

Example:

```text
Enter your task: Learn Git
Task added successfully!
```

New tasks are initially assigned the status:

```text
pending
```

### 2. Edit Task

Users can select an existing task and update its status.

Supported status concepts include:

* pending
* inprogress
* completed

### 3. List Tasks

Displays the tasks currently stored in the application along with their status.

### 4. Complete Task

Users can select a task and mark it as:

```text
Completed
```

### 5. Delete Task

Users can remove an existing task from the task list.

### 6. Exit

The application exits when the user selects option `5`.

## 🖥️ Application Menu

```text
===============================
       DEVOPS TASK TRACKER
===============================

        1. Add Task
        2. List Tasks
        3. Complete Task
        4. Delete Task
        5. Exit
```

## 🧠 Python Concepts Practiced

This project is being used to practice:

* Classes and objects
* `__init__()`
* Instance variables
* Dictionaries
* Conditional statements
* `if / elif / else`
* `while` loops
* `for` loops
* Functions/methods
* User input
* Dictionary operations
* Basic error handling and validation

## 🔧 Git Concepts Practiced

Git is an important part of this project.

The project is used to practice:

```text
git init
git status
git add
git commit
git log
git branch
git checkout
git merge
git diff
git reset
git rm
git clone
git push
```

### Git Workflow

The basic workflow used while developing the project is:

```text
Modify Code
    ↓
git status
    ↓
git add
    ↓
git commit
    ↓
Create / Switch Branch
    ↓
Develop Feature
    ↓
Merge Feature
    ↓
Push to GitHub
```

## 🌿 Branching Practice

Different branches are used to practice Git branching and merging.

Example branches:

```text
main
testing
demo_run
```

The project is also being used to understand how changes made in different branches can be merged back into the main branch.

## 📈 Development Roadmap

The project will be developed progressively.

### Phase 1 — Python CLI

* [x] Create CLI menu
* [x] Add task
* [x] Edit task status
* [x] List tasks
* [x] Complete task
* [x] Delete task
* [x] Exit option
* [ ] Improve input validation
* [ ] Improve task display

### Phase 2 — Git & GitHub

* [x] Initialize Git repository
* [x] Track changes
* [x] Create commits
* [x] Create branches
* [x] Switch branches
* [x] Merge branches
* [x] Push changes to GitHub
* [ ] Practice pull requests
* [ ] Practice merge conflicts
* [ ] Improve commit history

### Phase 3 — Persistent Storage

* [ ] Store tasks in JSON
* [ ] Load tasks when application starts
* [ ] Save tasks when application exits

### Phase 4 — Testing

* [ ] Add unit tests
* [ ] Test task creation
* [ ] Test task completion
* [ ] Test task deletion
* [ ] Test invalid inputs

### Phase 5 — CI/CD

* [ ] Add GitHub Actions
* [ ] Automatically run tests
* [ ] Add CI workflow
* [ ] Build application automatically

### Phase 6 — Containerization

* [ ] Create Dockerfile
* [ ] Build Docker image
* [ ] Run application using Docker
* [ ] Push image to container registry

### Phase 7 — Cloud Deployment

* [ ] Deploy application to AWS
* [ ] Configure cloud infrastructure
* [ ] Monitor application
* [ ] Document deployment process

## 🎯 Learning Objectives

The main purpose of this project is to gain practical experience with:

1. Python programming
2. Git version control
3. GitHub repository management
4. Branch-based development
5. Feature development workflow
6. Testing
7. CI/CD
8. Docker
9. Cloud deployment

The project is intentionally being developed step-by-step so that each new feature introduces a new technical concept.

## 🚀 Future Architecture

The long-term goal is to evolve the project from a simple CLI application into a small DevOps-oriented application:

```text
Python Application
       ↓
Git
       ↓
GitHub
       ↓
GitHub Actions
       ↓
Automated Tests
       ↓
Docker
       ↓
Container Registry
       ↓
AWS
       ↓
Monitoring
```

## 📚 Learning Approach

This project is being developed through hands-on implementation rather than copying a complete solution.

Each feature is implemented, tested, committed to Git, and progressively integrated into the main branch.

## 👨‍💻 Author

**Thirumalai K**

DevOps / Cloud Engineer

GitHub: https://github.com/thiru-00
