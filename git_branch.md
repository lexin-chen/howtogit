# git branch commands

`git branch` is useful to create feature branches so you can have an independent line of development that is separated from master. You can work on your feature without causing traffic in the master branch. It is closely related to `git checkout` and `git merge`.

- `git branch` list all the branches in the repo.
- `git branch <feature-branch>` creates a new branch. However this is different from `git checkout -b <feature-branch>`. **First one does not switch from working branch to that branch but the second one does.**
- `git branch -d <feature-branch>` delete the feature branch. However, it does not delete if it has unmerged changes.
- `git branch -D <feature-branch>` force delete the specified branch, even if it has unmerged changes. It will **permanently** throw away all the commits with that branch
- `git branch -m <feature-branch>` rename
- `git branch -a` list all remote branches