# `git rebase`

Rebasing alters the history of a repository, changing the parent of one or more commits.

Rebasing has two main purposes.

1. To merge a branch without creating an “extra” merge commit.
2. To clean up a local branch with **git rebase -i** where you’ve made a bunch of small commits.
- To merge a local branch into master without an extra commit:

- checkout the local branch

- **git rebase master**

- To push local master changes to the shared repository without an extra commit:

- **git pull --rebase**