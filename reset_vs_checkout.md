# `git reset` vs `git checkout -- <file>`

### Commands for Managing Changes:

1. **Unstage a File:**
    - If you have staged a file but want to unstage it (move it from the staging area back to the working directory), use:
        
        `git reset <file>`
        
2. **Discard Local Changes (Working Directory):**
    - To discard changes in your working directory and revert the file to the state of the last commit, use:
        
        `git checkout -- <file>`
        

### Combined Usage:

1. **Unstage and Discard Changes:**
    - If you’ve staged changes and decide you want to discard them completely, first unstage the file and then discard the changes:
        
        ```bash
        # Unstage the file
        git reset HEAD <file>
        
        # Discard changes and revert to last commit
        git checkout -- <file>
        ```
        

### Important Notes:

- **`git checkout -- <file>`**: This command discards all changes made to the file since the last commit. Be cautious with this command because it irreversibly removes changes.
- **Use Cases:**
    - **Unstage Only:** If you only want to unstage the file but keep the changes for later review or modification, use `git reset`.
    - **Discard All Changes:** If you want to discard all changes to a file and revert it to its last committed state, use `git checkout --`.

### Summary

- **`git reset <file>`**: Moves a file from the staging area back to the working directory, keeping your changes.
- **`git checkout -- <file>`**: Reverts the file in your working directory to the state of the last commit, discarding all local changes.