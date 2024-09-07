# `git reset` vs. `git revert`

Nutshell, reset is commits before pushes and revert is commits after pushes. One unstages one undoes after pushing

### `git reset`

**Purpose:** `git reset` is used to move the HEAD pointer and optionally modify the index (staging area) and working directory to match a specific commit. It is typically used to undo changes in your commit history.

**Usage:**

- **To Unstage Files:** If you've added files to the staging area (`git add`), but haven't committed them yet, you can use `git reset` to unstage those files:
    
    ```bash
    git reset <file>
    ```
    
    most straightforward way to see what files are in the staging area is `git status`.
    
- **To Undo Local Commits:** You can use `git reset` to undo local commits and move the HEAD pointer to a previous commit. This can be done in three modes:
    - **Soft Reset:** Keeps changes in the working directory and index, allowing you to re-commit them:
        
        ```bash
        git reset --soft <commit>
        ```
        
    - **Mixed Reset (default):** Keeps changes in the working directory but unstages them:
        
        ```bash
        git reset <commit>
        ```
        
    - **Hard Reset:** Discards changes in both the working directory and the index, effectively reverting to the specified commit:
        
        ```bash
        git reset --hard <commit>
        ```
        

**When to Use:**

- When you want to adjust your local commit history.
- When you need to unstage changes or remove commits that haven’t been pushed to a remote repository.
- Be cautious with `-hard` as it will permanently delete changes in your working directory and index.

### `git revert`

**Purpose:** `git revert` is used to create a new commit that undoes the changes introduced by a previous commit. It is a way to "undo" changes while preserving the commit history.

**Usage:**

- To revert a specific commit:
    
    ```bash
    git revert <commit>
    ```
    

**When to Use:**

- When you need to undo a commit that has already been pushed to a remote repository, especially if you want to maintain a clear history.
- When working in a shared repository where rewriting commit history (with `git reset`) could cause issues for others.

### Summary:

- **Use `git reset`** for local changes and to modify your commit history before sharing it. It’s useful for fixing mistakes before commits are shared with others.
- **Use `git revert`** for undoing changes in a commit that has already been shared with others, as it adds a new commit to reverse the changes rather than altering history.

Each tool has its place depending on whether you’re working with local changes or collaborating with others.

In the context of Git and version control, "sharing with others" generally refers to the act of pushing your changes to a remote repository that other collaborators have access to. This means that your changes become part of a shared codebase that others may rely on.