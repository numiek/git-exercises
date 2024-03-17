"""
Problem Description:
    You are assigned the task of implementing the 'get_short_state_command' function, which should return the Git command 
    needed to retrieve shortened information about the current state of the repository.
"""


def get_short_state_command():
    return "git status -s"
