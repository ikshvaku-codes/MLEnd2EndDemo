# MLEnd2EndDemo
This is the end to end demo project. It helps you to understand how to deploay a Machine Learning Project.

Requirements
1. GitHub repository
2. AWS account
3. VS Code
4. Git CLI

Steps to follow:
1. Create Repo in GitHub
2. Clone repository on System
3. Open Cloned repository in VSCode
4. Open Terminal in VS Code and run in Git Bash Mode.

* We link Cloud infra with git pipeline and make sure everything is updated accordingly.


![Archetecture](d:/Downloads/My%20First%20Board.jpg)


Whenever we made a change in the code we need to commit changes to the branch on github.
Steps to commit changes to the branch:
1. Commands for stageing
    1. git status :- To check the status of the files
    2. git add . or git add <filename> filename to add a specific file and . to add all the changes
    3. git log to get the logs of all the existing versions
2. Commit the changes
    git commit -m "message"
3. Push the changes to the git repository
    git push origin <branchname>