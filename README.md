# Repository for Code the Dream Python 100 Homework

Before using this repository, you should install Python.  

If you are using the VSCode editor, you should also have installed the Python extension.  (You may use a different editor, such as JetBrains Pycharm, but the instructions here describe the use of VSCode.)  If you are on Windows, you should configure VSCode to use Git Bash for your terminal session.  This is done from the command palette `Terminal: Select Default Profile`.  

  You should also have done the command:
```shell
pip install virtualenv
```

To use this repository:

1. Fork this repository, to create a copy in your Github account.
2. On your laptop, clone your fork.  (Do not clone the original repository!)
3. Change to the python_homework directory.  Enter the following commands:
```shell
pip -m venv .venv
code .
```
4. Important: Open the VSCode command pallette (ctrl-shift P).  In the `Python: Select Interpreter` option, choose the one with `.venv`.  If you have any terminal sessions open, close them, and open a new one.  You will see `(venv)` in your terminal prompt.
5. From the VSCode terminal session, enter the command:
```shell
pip install -r requirements_dev.txt
```

Once this is done, you are ready to create your lesson1 git branch.  You create a separate branch for each lesson.  The lesson2 branch is created when the lesson1 branch is active, so that the lessons build on one another.

Create the programs for lesson 1.  These are to be created in the root of your python_homework repository, unless the lesson specifies otherwise.  In some cases, you will need to install additional pip packages to complete the lesson.

When you have completed the lesson, add and commit your changes and push them to your fork of this repository.  Then create a pull request. **Be careful here!**  The target for your pull request must be the main branch of YOUR repository.  The default target that comes up when you create the pull request is this repository in the Code The Dream School account. **You don't want to use the default target.** Many students make this error.

Once you have created the pull request, include a link for the pull request in your homework submission.  Your reviewer will be notified, and will approve your request or ask for rework.  **Do not merge your pull request until your reviewer has approved it.**

Good luck with the class!