import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
import random
import time
from datetime import datetime, timedelta

class GitTutorialGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Mastery Tutorial & Practice")
        self.root.geometry("1400x900")
        self.root.configure(bg='#1e1e1e')
        
        # Tutorial system
        self.tutorials = self.setup_tutorials()
        self.current_tutorial = None
        self.current_step = 0
        
        # Initialize complex git state
        self.setup_complex_repository()
        self.setup_gui()
        self.update_visualization()
    
    def setup_tutorials(self):
        return {
            'beginner': [
                {
                    'title': '1. Git Basics: Your First Commit',
                    'description': 'Learn the basic Git workflow',
                    'steps': [
                        {
                            'action': 'Check your current status',
                            'command': 'git status',
                            'explanation': 'git status shows your current branch and what files are changed, staged, or untracked.',
                            'expected_output': 'On branch main with some modified files'
                        },
                        {
                            'action': 'Stage your changes',
                            'command': 'git add .',
                            'explanation': 'git add . stages ALL changes. Use git add <file> to stage specific files.',
                            'expected_output': 'Changes are now staged for commit'
                        },
                        {
                            'action': 'Commit your changes',
                            'command': 'git commit -m',
                            'explanation': 'Commits save your staged changes with a message. Write clear, descriptive messages!',
                            'expected_output': 'New commit created with your message'
                        }
                    ]
                },
                {
                    'title': '2. Working with Branches',
                    'description': 'Learn to create and switch branches',
                    'steps': [
                        {
                            'action': 'See all branches',
                            'command': 'git branch',
                            'explanation': 'Shows all branches. The * indicates your current branch.',
                            'expected_output': 'List of branches with current marked'
                        },
                        {
                            'action': 'Create and switch to new branch',
                            'command': 'git checkout -b',
                            'explanation': 'Creates a new branch and switches to it. Perfect for working on new features!',
                            'expected_output': 'Switched to new branch'
                        }
                    ]
                }
            ],
            'intermediate': [
                {
                    'title': '3. Merge vs Rebase',
                    'description': 'Understand when to use merge vs rebase',
                    'steps': [
                        {
                            'action': 'Merge a branch',
                            'command': 'git merge',
                            'explanation': 'Merging combines branch histories and creates a merge commit. Use when you want to preserve the complete history.',
                            'expected_output': 'Branch merged (may have conflicts)'
                        },
                        {
                            'action': 'Rebase onto main',
                            'command': 'git rebase',
                            'explanation': 'Rebasing replays your commits on top of another branch. Creates cleaner history but rewrites commits.',
                            'expected_output': 'Rebase started (may have conflicts)'
                        }
                    ]
                },
                {
                    'title': '4. Stashing Changes',
                    'description': 'Temporarily save work without committing',
                    'steps': [
                        {
                            'action': 'Stash your changes',
                            'command': 'git stash',
                            'explanation': 'Use when you need to switch branches but arent ready to commit. Saves your work safely.',
                            'expected_output': 'Working directory cleaned'
                        },
                        {
                            'action': 'Restore stashed changes',
                            'command': 'git stash pop',
                            'explanation': 'Restores your most recent stash and removes it from the stash list.',
                            'expected_output': 'Changes restored from stash'
                        }
                    ]
                }
            ],
            'advanced': [
                {
                    'title': '5. Fixing Mistakes',
                    'description': 'Recover from common Git mistakes',
                    'steps': [
                        {
                            'action': 'Unstage changes',
                            'command': 'git reset',
                            'explanation': 'git reset (mixed) unstages changes but keeps them in working directory. Use --hard to discard changes completely.',
                            'expected_output': 'Changes unstaged'
                        },
                        {
                            'action': 'Amend last commit',
                            'command': 'git commit --amend',
                            'explanation': 'Use to fix the most recent commit message or add forgotten changes. NEVER amend public commits!',
                            'expected_output': 'Commit amended successfully'
                        },
                        {
                            'action': 'View recovery history',
                            'command': 'git reflog',
                            'explanation': 'reflog shows ALL your actions. Use it to find lost commits or recover from bad operations.',
                            'expected_output': 'History of your Git actions'
                        }
                    ]
                },
                {
                    'title': '6. Advanced Scenarios',
                    'description': 'Handle complex Git situations',
                    'steps': [
                        {
                            'action': 'Cherry-pick a commit',
                            'command': 'git cherry-pick',
                            'explanation': 'Apply a specific commit from another branch to your current branch. Useful for hotfixes.',
                            'expected_output': 'Commit applied (may have conflicts)'
                        },
                        {
                            'action': 'Find when a bug was introduced',
                            'command': 'git bisect',
                            'explanation': 'Binary search through history to find which commit introduced a bug. Powerful debugging tool!',
                            'expected_output': 'Bisect session started'
                        }
                    ]
                }
            ],
            'conflict_resolution': [
                {
                    'title': '7. Merge Conflict Mastery',
                    'description': 'Learn to resolve conflicts like a pro',
                    'steps': [
                        {
                            'action': 'Create a practice conflict',
                            'command': 'Create Conflict',
                            'explanation': 'Well create a simulated conflict so you can practice resolution.',
                            'expected_output': 'Conflict created in a file'
                        },
                        {
                            'action': 'Edit the conflicted file',
                            'command': 'Edit Files (VI Sim)',
                            'explanation': 'Open the file and resolve conflicts by choosing which changes to keep.',
                            'expected_output': 'File opened for editing'
                        },
                        {
                            'action': 'Mark conflict as resolved',
                            'command': 'git add .',
                            'explanation': 'After fixing conflicts, stage the files to mark them as resolved.',
                            'expected_output': 'File staged (conflict marked resolved)'
                        },
                        {
                            'action': 'Complete the operation',
                            'command': 'git commit -m',
                            'explanation': 'Commit to finish the merge/rebase operation.',
                            'expected_output': 'Operation completed successfully'
                        }
                    ]
                }
            ]
        }
    
    def setup_complex_repository(self):
        # Complex initial state with multiple branches and history
        self.branches = {
            'main': ['c0ff33', 'd3adb33f', 'f4c3b00k'],
            'develop': ['c0ff33', 'd3adb33f', 'f3374tur3'],
            'feature/login': ['c0ff33', 'd3adb33f', 'l06in1'],
            'feature/payment': ['c0ff33', 'p4ym3nt']
        }
        
        self.current_branch = 'main'
        self.remote_branches = {
            'origin/main': ['c0ff33', 'd3adb33f', 'f4c3b00k', 'r3m0t3c0mm1t'],
            'origin/develop': ['c0ff33', 'd3adb33f', 'f3374tur3']
        }
        
        self.commits = [
            {'hash': 'c0ff33', 'message': 'Initial commit', 'branch': 'main', 
             'author': 'Alice <alice@dev.com>', 'date': self.random_past_date(30),
             'files': ['README.md', 'main.py']},
            {'hash': 'd3adb33f', 'message': 'Add core functionality', 'branch': 'main',
             'author': 'Bob <bob@dev.com>', 'date': self.random_past_date(25),
             'files': ['main.py', 'utils.py', 'config.json']},
            {'hash': 'f4c3b00k', 'message': 'Fix authentication bug', 'branch': 'main',
             'author': 'Alice <alice@dev.com>', 'date': self.random_past_date(20),
             'files': ['auth.py', 'main.py']},
            {'hash': 'f3374tur3', 'message': 'Add new API endpoints', 'branch': 'develop',
             'author': 'Charlie <charlie@dev.com>', 'date': self.random_past_date(15),
             'files': ['api.py', 'models.py', 'requirements.txt']},
            {'hash': 'l06in1', 'message': 'Implement login UI', 'branch': 'feature/login',
             'author': 'Alice <alice@dev.com>', 'date': self.random_past_date(10),
             'files': ['templates/login.html', 'static/css/login.css', 'auth.py']},
            {'hash': 'p4ym3nt', 'message': 'Payment system setup', 'branch': 'feature/payment',
             'author': 'Bob <bob@dev.com>', 'date': self.random_past_date(5),
             'files': ['payment.py', 'models.py']},
            {'hash': 'r3m0t3c0mm1t', 'message': 'Remote changes', 'branch': 'origin/main',
             'author': 'Team <team@company.com>', 'date': self.random_past_date(2),
             'files': ['main.py', 'deploy.py']}
        ]
        
        self.staged_files = []
        self.unstaged_files = ['auth.py', 'main.py', 'config.json']
        self.untracked_files = ['new_feature.py', 'test_temp.py']
        self.stash_list = []
        self.reflog = []
        self.commit_count = 7
        self.conflict_files = {}
        
        # File content simulation
        self.file_contents = {
            'main.py': 'def main():\n    print("Hello World")\n    auth_user()',
            'auth.py': 'def auth_user():\n    return True\n\n# Conflict marker here',
            'utils.py': 'import os\n\ndef helper():\n    pass',
            'config.json': '{"debug": true, "port": 8000}'
        }
    
    def random_past_date(self, days_ago):
        return datetime.now() - timedelta(days=days_ago)
    
    def setup_gui(self):
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#2d2d30')
        style.configure('TLabel', background='#2d2d30', foreground='#cccccc')
        style.configure('TLabelFrame', background='#2d2d30', foreground='#569cd6')
        style.configure('TButton', background='#0e639c', foreground='white')
        style.configure('TEntry', fieldbackground='#3c3c3c', foreground='white')
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Left panel - Tutorials and Commands
        left_frame = ttk.LabelFrame(main_frame, text="Git Tutorial & Commands", padding="10")
        left_frame.grid(row=0, column=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Tutorial selector
        ttk.Label(left_frame, text="Select Tutorial:", font=('Arial', 10, 'bold')).pack(pady=(0, 5), anchor=tk.W)
        
        tutorial_frame = ttk.Frame(left_frame)
        tutorial_frame.pack(fill=tk.X, pady=5)
        
        self.tutorial_var = tk.StringVar()
        tutorial_combo = ttk.Combobox(tutorial_frame, textvariable=self.tutorial_var, state='readonly')
        tutorial_combo['values'] = [
            '🎯 Beginner: Basic Workflow',
            '🎯 Beginner: Branch Management', 
            '🚀 Intermediate: Merge vs Rebase',
            '🚀 Intermediate: Stashing',
            '⚡ Advanced: Fixing Mistakes',
            '⚡ Advanced: Complex Scenarios',
            '🔥 Expert: Conflict Resolution'
        ]
        tutorial_combo.pack(fill=tk.X)
        tutorial_combo.bind('<<ComboboxSelected>>', self.start_tutorial)
        
        # Current tutorial info
        self.tutorial_info = scrolledtext.ScrolledText(left_frame, height=8, width=35, 
                                                      bg='#2d3748', fg='#e2e8f0', 
                                                      font=('Arial', 9))
        self.tutorial_info.pack(fill=tk.X, pady=10)
        
        # Tutorial navigation
        nav_frame = ttk.Frame(left_frame)
        nav_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(nav_frame, text="◀ Previous", command=self.previous_step, width=10).pack(side=tk.LEFT)
        ttk.Button(nav_frame, text="Next ▶", command=self.next_step, width=10).pack(side=tk.RIGHT)
        ttk.Button(nav_frame, text="Skip Tutorial", command=self.skip_tutorial, width=12).pack(side=tk.RIGHT, padx=5)
        
        # Command categories notebook
        notebook = ttk.Notebook(left_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Basic commands tab
        basic_frame = ttk.Frame(notebook, padding="5")
        notebook.add(basic_frame, text="Basic")
        
        basic_commands = [
            ("git status", self.git_status),
            ("git add .", self.git_add_all),
            ("git commit -m", self.git_commit),
            ("git log", self.git_log),
            ("git branch", self.git_branch),
            ("git checkout", self.git_checkout),
            ("git push", self.git_push),
            ("git pull", self.git_pull)
        ]
        
        for i, (text, command) in enumerate(basic_commands):
            btn = ttk.Button(basic_frame, text=text, command=command, width=18)
            btn.grid(row=i//2, column=i%2, pady=2, padx=2, sticky=tk.W)
        
        # Advanced commands tab
        advanced_frame = ttk.Frame(notebook, padding="5")
        notebook.add(advanced_frame, text="Advanced")
        
        advanced_commands = [
            ("git rebase", self.git_rebase),
            ("git merge", self.git_merge),
            ("git reset", self.git_reset),
            ("git show", self.git_show),
            ("git diff", self.git_diff),
            ("git stash", self.git_stash),
            ("git stash pop", self.git_stash_pop),
            ("git blame", self.git_blame)
        ]
        
        for i, (text, command) in enumerate(advanced_commands):
            btn = ttk.Button(advanced_frame, text=text, command=command, width=18)
            btn.grid(row=i//2, column=i%2, pady=2, padx=2, sticky=tk.W)
        
        # Expert commands tab
        expert_frame = ttk.Frame(notebook, padding="5")
        notebook.add(expert_frame, text="Expert")
        
        expert_commands = [
            ("git bisect", self.git_bisect),
            ("git commit --amend", self.git_commit_amend),
            ("git reflog", self.git_reflog),
            ("git cherry-pick", self.git_cherry_pick),
            ("Create Conflict", self.create_conflict),
            ("Edit Files (VI Sim)", self.edit_files_sim),
            ("git log --oneline", self.git_log_oneline),
            ("git remote -v", self.git_remote_v)
        ]
        
        for i, (text, command) in enumerate(expert_commands):
            btn = ttk.Button(expert_frame, text=text, command=command, width=18)
            btn.grid(row=i//2, column=i%2, pady=2, padx=2, sticky=tk.W)
        
        # Custom command input
        ttk.Label(left_frame, text="Custom Command:").pack(pady=(10, 5), anchor=tk.W)
        
        cmd_frame = ttk.Frame(left_frame)
        cmd_frame.pack(fill=tk.X, pady=5)
        
        self.command_var = tk.StringVar()
        command_entry = ttk.Entry(cmd_frame, textvariable=self.command_var, width=20)
        command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        command_entry.bind('<Return>', self.execute_custom_command)
        
        ttk.Button(cmd_frame, text="Execute", command=self.execute_custom_command).pack(side=tk.RIGHT, padx=(5, 0))
        
        # Right panel - Terminal output
        right_frame = ttk.LabelFrame(main_frame, text="Terminal Output", padding="10")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        self.terminal_output = scrolledtext.ScrolledText(right_frame, height=20, width=80, 
                                                        bg='black', fg='#00ff00', 
                                                        font=('Consolas', 10), insertbackground='green')
        self.terminal_output.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Visualization panel
        viz_frame = ttk.LabelFrame(main_frame, text="Repository Visualization", padding="10")
        viz_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        viz_frame.columnconfigure(0, weight=1)
        viz_frame.rowconfigure(0, weight=1)
        
        self.viz_canvas = tk.Canvas(viz_frame, bg='#1e1e1e', height=400, highlightthickness=0)
        self.viz_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Welcome message
        self.print_to_terminal("🚀 Git Mastery Tutorial & Practice")
        self.print_to_terminal("💡 Select a tutorial from the dropdown to get started!")
        self.print_to_terminal("📚 Learn when and how to use each Git command properly\n")
    
    # TUTORIAL SYSTEM
    def start_tutorial(self, event=None):
        selection = self.tutorial_var.get()
        tutorial_map = {
            '🎯 Beginner: Basic Workflow': ('beginner', 0),
            '🎯 Beginner: Branch Management': ('beginner', 1),
            '🚀 Intermediate: Merge vs Rebase': ('intermediate', 0),
            '🚀 Intermediate: Stashing': ('intermediate', 1),
            '⚡ Advanced: Fixing Mistakes': ('advanced', 0),
            '⚡ Advanced: Complex Scenarios': ('advanced', 1),
            '🔥 Expert: Conflict Resolution': ('conflict_resolution', 0)
        }
        
        if selection in tutorial_map:
            category, index = tutorial_map[selection]
            self.current_tutorial = self.tutorials[category][index]
            self.current_step = 0
            self.show_current_step()
    
    def show_current_step(self):
        if not self.current_tutorial:
            return
            
        self.tutorial_info.delete('1.0', tk.END)
        
        # Show tutorial title and description
        self.tutorial_info.insert(tk.END, f"📖 {self.current_tutorial['title']}\n", 'title')
        self.tutorial_info.insert(tk.END, f"{self.current_tutorial['description']}\n\n", 'subtitle')
        
        if self.current_step < len(self.current_tutorial['steps']):
            step = self.current_tutorial['steps'][self.current_step]
            
            # Show current step
            self.tutorial_info.insert(tk.END, f"Step {self.current_step + 1}: {step['action']}\n", 'step')
            self.tutorial_info.insert(tk.END, f"Command: {step['command']}\n\n", 'command')
            self.tutorial_info.insert(tk.END, "💡 Explanation:\n", 'heading')
            self.tutorial_info.insert(tk.END, f"{step['explanation']}\n\n")
            self.tutorial_info.insert(tk.END, "📋 Expected:\n", 'heading')
            self.tutorial_info.insert(tk.END, f"{step['expected_output']}\n")
            
            # Configure text tags for formatting
            self.tutorial_info.tag_config('title', foreground='#569cd6', font=('Arial', 11, 'bold'))
            self.tutorial_info.tag_config('subtitle', foreground='#9cdcfe', font=('Arial', 10, 'italic'))
            self.tutorial_info.tag_config('step', foreground='#4ec9b0', font=('Arial', 10, 'bold'))
            self.tutorial_info.tag_config('command', foreground='#ce9178', font=('Consolas', 9))
            self.tutorial_info.tag_config('heading', foreground='#dcdcaa', font=('Arial', 9, 'bold'))
            
            # Auto-execute the command for the user in tutorial mode
            self.print_to_terminal(f"\n🎯 TUTORIAL: {step['action']}", "cyan")
            self.print_to_terminal(f"💡 Running: {step['command']}", "yellow")
            
            # Map command strings to actual methods
            command_map = {
                'git status': self.git_status,
                'git add .': self.git_add_all,
                'git commit -m': self.git_commit,
                'git branch': self.git_branch,
                'git checkout -b': self.git_checkout_b,
                'git merge': self.git_merge,
                'git rebase': self.git_rebase,
                'git stash': self.git_stash,
                'git stash pop': self.git_stash_pop,
                'git reset': self.git_reset,
                'git commit --amend': self.git_commit_amend,
                'git reflog': self.git_reflog,
                'git cherry-pick': self.git_cherry_pick,
                'git bisect': self.git_bisect,
                'Create Conflict': self.create_conflict,
                'Edit Files (VI Sim)': self.edit_files_sim
            }
            
            if step['command'] in command_map:
                # Execute the command
                command_map[step['command']]()
    
    def next_step(self):
        if self.current_tutorial and self.current_step < len(self.current_tutorial['steps']) - 1:
            self.current_step += 1
            self.show_current_step()
        else:
            self.print_to_terminal("🎉 Tutorial completed! Great job!", "green")
            self.current_tutorial = None
    
    def previous_step(self):
        if self.current_tutorial and self.current_step > 0:
            self.current_step -= 1
            self.show_current_step()
    
    def skip_tutorial(self):
        self.current_tutorial = None
        self.tutorial_info.delete('1.0', tk.END)
        self.tutorial_info.insert(tk.END, "💡 Select a tutorial from the dropdown to start learning!")
        self.print_to_terminal("Tutorial skipped. Feel free to explore commands on your own!", "yellow")
    
    # GIT COMMAND IMPLEMENTATIONS
    def print_to_terminal(self, text, color=None):
        tag = None
        if color:
            tag = f"color_{color}"
            self.terminal_output.tag_config(tag, foreground=color)
        
        if tag:
            self.terminal_output.insert(tk.END, text + '\n', tag)
        else:
            self.terminal_output.insert(tk.END, text + '\n')
        self.terminal_output.see(tk.END)
    
    def git_status(self):
        self.print_to_terminal(f"$ git status")
        self.print_to_terminal(f"On branch {self.current_branch}")
        if self.current_branch in self.remote_branches.get(f'origin/{self.current_branch}', []):
            self.print_to_terminal("Your branch is up to date with 'origin/main'.")
        
        self.print_to_terminal("\nChanges not staged for commit:")
        for file in self.unstaged_files:
            self.print_to_terminal(f"  modified:   {file}")
        
        self.print_to_terminal("\nUntracked files:")
        for file in self.untracked_files:
            self.print_to_terminal(f"  {file}")
        
        self.print_to_terminal("\nChanges to be committed:")
        for file in self.staged_files:
            self.print_to_terminal(f"  new file:   {file}")
        
        if self.conflict_files:
            self.print_to_terminal("\nUnmerged paths:", "red")
            for file in self.conflict_files:
                self.print_to_terminal(f"  both modified: {file}", "red")
        self.update_visualization()
    
    def git_add_all(self):
        self.print_to_terminal(f"$ git add .")
        if self.unstaged_files:
            self.staged_files.extend(self.unstaged_files)
            self.unstaged_files = []
            self.print_to_terminal("Staged all changes for commit")
        else:
            self.print_to_terminal("No changes to stage")
        self.update_visualization()
    
    def git_commit(self):
        self.print_to_terminal(f"$ git commit -m")
        if self.staged_files:
            self.commit_count += 1
            commit_hash = f"{random.choice(['a1b2c', 'd4e5f', '67890'])}{self.commit_count:02d}"
            commit_msg = simpledialog.askstring("Commit Message", "Enter commit message:")
            if not commit_msg:
                commit_msg = f"Commit #{self.commit_count}"
            
            new_commit = {
                'hash': commit_hash,
                'message': commit_msg,
                'branch': self.current_branch,
                'author': 'You <you@dev.com>',
                'date': datetime.now(),
                'files': self.staged_files.copy()
            }
            
            self.commits.append(new_commit)
            self.branches[self.current_branch].append(commit_hash)
            self.staged_files = []
            self.unstaged_files = [f"file{self.commit_count + 1}.txt"]
            
            self.print_to_terminal(f"[{self.current_branch} {commit_hash}] {commit_msg}")
            self.print_to_terminal(f" {len(new_commit['files'])} files changed")
            self.add_to_reflog(f"commit: {commit_msg}")
        else:
            self.print_to_terminal("No changes staged for commit")
        self.update_visualization()
    
    def git_log(self):
        self.print_to_terminal(f"$ git log")
        self.print_to_terminal("Commit history:")
        for commit in reversed(self.commits[-10:]):  # Show last 10 commits
            author = commit['author'].split('<')[0].strip()
            date_str = commit['date'].strftime("%Y-%m-%d %H:%M")
            self.print_to_terminal(f"commit {commit['hash']}")
            self.print_to_terminal(f"Author: {commit['author']}")
            self.print_to_terminal(f"Date:   {date_str}")
            self.print_to_terminal("")
            self.print_to_terminal(f"    {commit['message']}")
            self.print_to_terminal("")
    
    def git_branch(self):
        self.print_to_terminal(f"$ git branch")
        self.print_to_terminal("Available branches:")
        for branch in self.branches:
            marker = "* " if branch == self.current_branch else "  "
            self.print_to_terminal(f"{marker}{branch}")
    
    def git_checkout(self):
        target = simpledialog.askstring("Checkout", "Branch or commit to checkout:")
        if target:
            self.print_to_terminal(f"$ git checkout {target}")
            if target in self.branches:
                self.current_branch = target
                self.print_to_terminal(f"Switched to branch '{target}'")
                self.add_to_reflog(f"checkout: moving to {target}")
            else:
                # Try to find commit
                commit = next((c for c in self.commits if c['hash'].startswith(target)), None)
                if commit:
                    self.print_to_terminal(f"Note: checking out '{target}'")
                    self.print_to_terminal("You are in 'detached HEAD' state.")
                    self.current_branch = f"detached-{target[:7]}"
                    self.add_to_reflog(f"checkout: moving to {target}")
                else:
                    self.print_to_terminal(f"error: pathspec '{target}' did not match any file(s) known to git")
        self.update_visualization()
    
    def git_checkout_b(self):
        new_branch = f"feature-{len(self.branches)}"
        self.branches[new_branch] = self.branches[self.current_branch].copy()
        self.current_branch = new_branch
        self.print_to_terminal(f"Switched to new branch '{new_branch}'")
        self.update_visualization()
    
    def git_push(self):
        self.print_to_terminal(f"$ git push")
        if self.current_branch in ['main', 'develop']:
            self.print_to_terminal(f"Pushing to origin/{self.current_branch}")
            # Simulate push rejection due to conflicts
            if random.random() < 0.4:
                self.print_to_terminal("! [rejected]        main -> main (non-fast-forward)", "red")
                self.print_to_terminal("error: failed to push some refs", "red")
                self.print_to_terminal("hint: Updates were rejected because the remote contains work...")
                self.print_to_terminal("hint: Use 'git pull' to integrate the remote changes.")
            else:
                self.print_to_terminal("Everything up-to-date")
        else:
            self.print_to_terminal(f"Pushing feature branch {self.current_branch}")
            self.print_to_terminal("Would set upstream branch")
        self.add_to_reflog("push: origin")
    
    def git_pull(self):
        self.print_to_terminal(f"$ git pull")
        self.print_to_terminal("Pulling from origin...")
        # Simulate merge during pull
        if random.random() < 0.3:
            self.print_to_terminal("Auto-merging main.py")
            self.print_to_terminal("CONFLICT (content): Merge conflict in main.py", "red")
            self.conflict_files['main.py'] = True
        else:
            self.print_to_terminal("Already up to date.")
        self.add_to_reflog("pull: origin")
        self.update_visualization()
    
    def git_rebase(self):
        target_branch = simpledialog.askstring("Rebase", "Rebase onto which branch?", initialvalue="develop")
        if target_branch and target_branch in self.branches:
            self.print_to_terminal(f"$ git rebase {target_branch}")
            self.print_to_terminal(f"Rebasing {self.current_branch} onto {target_branch}")
            
            # Simulate rebase process
            target_commits = self.branches[target_branch]
            current_commits = self.branches[self.current_branch]
            
            # Find common ancestor
            common_ancestor = None
            for commit in reversed(current_commits):
                if commit in target_commits:
                    common_ancestor = commit
                    break
            
            if common_ancestor:
                # Replay commits after common ancestor
                commits_to_replay = current_commits[current_commits.index(common_ancestor)+1:]
                self.print_to_terminal(f"Replaying {len(commits_to_replay)} commits...")
                
                for commit_hash in commits_to_replay:
                    commit = next(c for c in self.commits if c['hash'] == commit_hash)
                    self.print_to_terminal(f"Applying: {commit['message']}")
                    # Simulate potential conflicts
                    if random.random() < 0.3:
                        conflict_file = random.choice(['main.py', 'auth.py', 'utils.py'])
                        self.print_to_terminal(f"CONFLICT in {conflict_file}", "red")
                        self.conflict_files[conflict_file] = True
                
                if self.conflict_files:
                    self.print_to_terminal("Rebase paused due to conflicts. Resolve and run 'git rebase --continue'", "red")
                else:
                    self.print_to_terminal("Rebase completed successfully!")
                    self.branches[self.current_branch] = target_commits + commits_to_replay
            self.add_to_reflog(f"rebase: onto {target_branch}")
        self.update_visualization()
    
    def git_merge(self):
        source_branch = simpledialog.askstring("Merge", "Branch to merge from:")
        if source_branch and source_branch in self.branches:
            self.print_to_terminal(f"$ git merge {source_branch}")
            self.print_to_terminal(f"Merging {source_branch} into {self.current_branch}")
            
            # Simulate different merge scenarios
            merge_type = random.choice(['fast-forward', '3-way', 'conflict'])
            
            if merge_type == 'fast-forward':
                self.print_to_terminal("Fast-forward merge - no merge commit created")
                self.branches[self.current_branch].extend(
                    self.branches[source_branch][len(self.branches[self.current_branch]):]
                )
            elif merge_type == 'conflict':
                conflict_file = random.choice(['main.py', 'auth.py'])
                self.print_to_terminal(f"CONFLICT (content): Merge conflict in {conflict_file}", "red")
                self.conflict_files[conflict_file] = True
                self.print_to_terminal("Automatic merge failed; fix conflicts and then commit the result.")
            else:
                # Create a merge commit
                merge_hash = f"merge{random.randint(1000,9999)}"
                merge_commit = {
                    'hash': merge_hash,
                    'message': f"Merge branch '{source_branch}' into {self.current_branch}",
                    'branch': self.current_branch,
                    'author': 'You <you@dev.com>',
                    'date': datetime.now(),
                    'files': ['merged_files.txt']
                }
                self.commits.append(merge_commit)
                self.branches[self.current_branch].append(merge_hash)
                self.print_to_terminal("Merge made by the 'ort' strategy.")
            
            self.add_to_reflog(f"merge: {source_branch}")
            self.update_visualization()
    
    def git_reset(self):
        reset_type = simpledialog.askstring("Reset", "Reset type (soft/mixed/hard):", initialvalue="mixed")
        if reset_type:
            self.print_to_terminal(f"$ git reset --{reset_type}")
            if reset_type == "hard":
                self.unstaged_files.extend(self.staged_files)
                self.staged_files = []
                self.print_to_terminal("Hard reset - discarded all changes")
            elif reset_type == "soft":
                self.print_to_terminal("Soft reset - changes preserved in staging")
            else:  # mixed
                self.unstaged_files.extend(self.staged_files)
                self.staged_files = []
                self.print_to_terminal("Mixed reset - changes preserved but unstaged")
            self.add_to_reflog(f"reset: {reset_type}")
        self.update_visualization()
    
    def git_show(self):
        self.print_to_terminal(f"$ git show")
        if self.commits:
            latest_commit = self.commits[-1]
            self.print_to_terminal(f"commit {latest_commit['hash']}")
            self.print_to_terminal(f"Author: {latest_commit['author']}")
            self.print_to_terminal(f"Date:   {latest_commit['date']}")
            self.print_to_terminal("")
            self.print_to_terminal(f"    {latest_commit['message']}")
            self.print_to_terminal("")
            self.print_to_terminal("Files changed:")
            for file in latest_commit.get('files', []):
                self.print_to_terminal(f"    {file}")
    
    def git_diff(self):
        self.print_to_terminal(f"$ git diff")
        if self.unstaged_files or self.staged_files:
            self.print_to_terminal("diff --git a/file.txt b/file.txt")
            self.print_to_terminal("index 1234567..89abcde 100644")
            self.print_to_terminal("--- a/file.txt")
            self.print_to_terminal("+++ b/file.txt")
            self.print_to_terminal("@@ -1,3 +1,4 @@")
            self.print_to_terminal(" def main():")
            self.print_to_terminal("-    print(\"Old code\")")
            self.print_to_terminal("+    print(\"New code\")")
            self.print_to_terminal("+    # New feature added")
            self.print_to_terminal("     return True")
        else:
            self.print_to_terminal("No changes to show")
    
    def git_stash(self):
        self.print_to_terminal(f"$ git stash")
        if self.unstaged_files or self.staged_files:
            stash_id = f"stash@{{{len(self.stash_list)}}}"
            stash_content = {
                'id': stash_id,
                'branch': self.current_branch,
                'files': self.unstaged_files + self.staged_files,
                'message': f"WIP on {self.current_branch}"
            }
            self.stash_list.append(stash_content)
            self.unstaged_files = []
            self.staged_files = []
            self.print_to_terminal(f"Saved working directory and index state {stash_id}")
            self.add_to_reflog(f"stash: {stash_content['message']}")
        else:
            self.print_to_terminal("No local changes to save")
        self.update_visualization()
    
    def git_stash_pop(self):
        self.print_to_terminal(f"$ git stash pop")
        if self.stash_list:
            stash = self.stash_list.pop()
            self.unstaged_files = stash['files']
            self.print_to_terminal(f"Restored changes from {stash['id']}")
            self.add_to_reflog(f"stash pop: {stash['id']}")
        else:
            self.print_to_terminal("No stash entries found.")
        self.update_visualization()
    
    def git_blame(self):
        file_to_blame = simpledialog.askstring("Blame", "File to blame:", initialvalue="main.py")
        if file_to_blame:
            self.print_to_terminal(f"$ git blame {file_to_blame}")
            self.print_to_terminal(f"Blame for {file_to_blame}:")
            self.print_to_terminal("a1b2c01 (Alice Dev    2024-01-15 1) def main():")
            self.print_to_terminal("d3adb33 (Bob Coder    2024-01-20 2)     print('Hello')")
            self.print_to_terminal("f4c3b00 (Alice Dev    2024-01-25 3)     return True")
    
    def git_bisect(self):
        self.print_to_terminal(f"$ git bisect start")
        self.print_to_terminal("Starting bisect session...")
        self.print_to_terminal("Mark commits as 'good' or 'bad' to find the breaking change")
        self.print_to_terminal("Commands: git bisect good, git bisect bad")
        self.print_to_terminal("Current commit: d3adb33 - 'Add core functionality'")
        self.print_to_terminal("Bisecting: 3 revisions left to test")
        self.add_to_reflog("bisect: start")
    
    def git_commit_amend(self):
        self.print_to_terminal(f"$ git commit --amend")
        if any(self.staged_files or self.unstaged_files):
            new_msg = simpledialog.askstring("Amend Commit", "New commit message:", 
                                           initialvalue="Amended commit")
            if new_msg:
                if self.commits:
                    self.commits[-1]['message'] = new_msg
                    self.commits[-1]['date'] = datetime.now()
                self.print_to_terminal("Commit amended successfully")
                self.add_to_reflog("commit (amend)")
        else:
            self.print_to_terminal("No changes to amend with")
        self.update_visualization()
    
    def git_reflog(self):
        self.print_to_terminal(f"$ git reflog")
        self.print_to_terminal("Reference log:")
        for entry in reversed(self.reflog[-10:]):  # Show last 10 entries
            self.print_to_terminal(entry)
    
    def git_cherry_pick(self):
        commit_hash = simpledialog.askstring("Cherry-pick", "Commit hash to cherry-pick:")
        if commit_hash:
            self.print_to_terminal(f"$ git cherry-pick {commit_hash}")
            commit_to_pick = next((c for c in self.commits if c['hash'] == commit_hash), None)
            if commit_to_pick:
                self.print_to_terminal(f"Applying: {commit_to_pick['message']}")
                # Simulate potential conflicts
                if random.random() < 0.4:
                    conflict_file = random.choice(commit_to_pick.get('files', ['main.py']))
                    self.print_to_terminal(f"CONFLICT in {conflict_file}", "red")
                    self.conflict_files[conflict_file] = True
                    self.print_to_terminal("Cherry-pick paused due to conflicts. Resolve and run 'git cherry-pick --continue'")
                else:
                    new_hash = f"cherry{random.randint(1000,9999)}"
                    new_commit = commit_to_pick.copy()
                    new_commit['hash'] = new_hash
                    new_commit['branch'] = self.current_branch
                    self.commits.append(new_commit)
                    self.branches[self.current_branch].append(new_hash)
                    self.print_to_terminal(f"Cherry-pick completed: {new_hash}")
                self.add_to_reflog(f"cherry-pick: {commit_hash}")
            else:
                self.print_to_terminal(f"Error: Commit {commit_hash} not found", "red")
        self.update_visualization()
    
    def create_conflict(self):
        self.print_to_terminal(f"$ # Creating practice conflict...")
        """Simulate creating a merge conflict for practice"""
        conflict_file = random.choice(['main.py', 'auth.py', 'utils.py'])
        self.conflict_files[conflict_file] = True
        self.print_to_terminal(f"🎯 Created simulated conflict in {conflict_file}", "yellow")
        self.print_to_terminal("Practice resolving with:")
        self.print_to_terminal("  - Edit the file manually")
        self.print_to_terminal("  - git add <file> to mark as resolved")
        self.print_to_terminal("  - git commit to complete the merge")
        self.update_visualization()
    
    def edit_files_sim(self):
        self.print_to_terminal(f"$ # Opening file editor...")
        """Simulate VI editor for file editing"""
        if not self.unstaged_files:
            self.unstaged_files = ['main.py', 'config.json']
        
        file_to_edit = simpledialog.askstring("VI Simulator", "File to edit:", 
                                            initialvalue=self.unstaged_files[0])
        if file_to_edit:
            self.print_to_terminal(f"📝 Opening {file_to_edit} in VI simulator...")
            self.print_to_terminal("VI Commands: i (insert), ESC (command mode), :wq (save & quit)")
            self.print_to_terminal("Current content:")
            
            # Show current file content
            content = self.file_contents.get(file_to_edit, "# New file\n# Start editing here...")
            for line in content.split('\n'):
                self.print_to_terminal(f"  {line}")
            
            # Simulate editing
            new_content = simpledialog.askstring("Edit File", f"New content for {file_to_edit}:", 
                                               initialvalue=content)
            if new_content:
                self.file_contents[file_to_edit] = new_content
                if file_to_edit not in self.unstaged_files:
                    self.unstaged_files.append(file_to_edit)
                self.print_to_terminal("💾 File saved. Changes are unstaged.")
                self.print_to_terminal("Run 'git add <file>' to stage changes")
        self.update_visualization()
    
    def git_log_oneline(self):
        self.print_to_terminal(f"$ git log --oneline")
        self.print_to_terminal("Commit history (oneline):")
        for commit in reversed(self.commits[-10:]):  # Show last 10 commits
            branch_indicator = "*" if commit['branch'] == self.current_branch else " "
            self.print_to_terminal(f"{commit['hash'][:7]} {branch_indicator} {commit['message']}")
    
    def git_remote_v(self):
        self.print_to_terminal(f"$ git remote -v")
        self.print_to_terminal("Remote repositories:")
        self.print_to_terminal("origin  https://github.com/user/repo.git (fetch)")
        self.print_to_terminal("origin  https://github.com/user/repo.git (push)")
    
    def add_to_reflog(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.reflog.append(f"{self.current_branch}@{{0}} {timestamp}: {action}")
    
    def execute_custom_command(self, event=None):
        command = self.command_var.get().strip()
        self.command_var.set("")
        
        self.print_to_terminal(f"$ {command}")
        
        if command == 'help':
            self.show_help()
        elif command.startswith('git '):
            cmd_parts = command[4:].split()
            if cmd_parts[0] == 'rebase':
                if len(cmd_parts) > 1:
                    self.git_rebase()
            elif cmd_parts[0] == 'reset':
                self.git_reset()
            elif cmd_parts[0] == 'stash':
                if len(cmd_parts) > 1 and cmd_parts[1] == 'pop':
                    self.git_stash_pop()
                else:
                    self.git_stash()
            else:
                self.print_to_terminal(f"Executed: {command}")
                self.add_to_reflog(f"command: {command}")
        else:
            self.print_to_terminal(f"Command not recognized: {command}")
    
    def show_help(self):
        self.print_to_terminal("Available Git Commands:", "cyan")
        self.print_to_terminal("Basic: status, add, commit, log, branch, checkout, push, pull")
        self.print_to_terminal("Advanced: rebase, merge, reset, show, diff, stash, blame")
        self.print_to_terminal("Expert: bisect, commit --amend, reflog, cherry-pick")
        self.print_to_terminal("")
        self.print_to_terminal("💡 Pro Tips:", "yellow")
        self.print_to_terminal("• Use tutorials to learn when to use each command")
        self.print_to_terminal("• Practice conflict resolution")
        self.print_to_terminal("• Learn the difference between merge and rebase")
        self.print_to_terminal("• Master git stash for context switching")
    
    def update_visualization(self):
        self.viz_canvas.delete("all")
        
        # Colors
        colors = {
            'main': '#48bb78',
            'develop': '#4299e1', 
            'feature/login': '#ed8936',
            'feature/payment': '#9f7aea',
            'origin/main': '#e53e3e',
            'default': '#a0aec0'
        }
        
        # Draw commits and branches
        x, y = 50, 80
        commit_radius = 15
        
        # Group commits by branch for better visualization
        branch_commits = {}
        for branch in self.branches:
            branch_commits[branch] = [c for c in self.commits if c['hash'] in self.branches[branch]]
        
        # Draw each branch as a separate line
        branch_y_positions = {}
        for i, branch in enumerate(self.branches.keys()):
            branch_y = y + i * 80
            branch_y_positions[branch] = branch_y
            
            # Draw branch label
            color = colors.get(branch, colors['default'])
            current_indicator = "➤ " if branch == self.current_branch else ""
            self.viz_canvas.create_text(20, branch_y, text=f"{current_indicator}{branch}", 
                                      anchor='w', font=('Consolas', 10, 'bold'), fill=color)
            
            # Draw commits for this branch
            for j, commit_hash in enumerate(self.branches[branch]):
                commit_x = 200 + j * 60
                commit = next(c for c in self.commits if c['hash'] == commit_hash)
                
                # Draw commit circle
                fill_color = color
                outline_color = '#ffffff' if branch == self.current_branch else '#718096'
                self.viz_canvas.create_oval(commit_x, branch_y-commit_radius, 
                                          commit_x+commit_radius*2, branch_y+commit_radius, 
                                          fill=fill_color, outline=outline_color, width=2)
                
                # Draw commit hash (abbreviated)
                self.viz_canvas.create_text(commit_x+commit_radius, branch_y, 
                                          text=commit_hash[:6], font=('Consolas', 7), 
                                          fill='white')
                
                # Draw connecting line to next commit
                if j < len(self.branches[branch]) - 1:
                    next_x = commit_x + commit_radius*2 + 10
                    self.viz_canvas.create_line(commit_x+commit_radius*2, branch_y, 
                                              next_x, branch_y, 
                                              fill=color, width=2, arrow=tk.LAST)
        
        # Draw current state info
        info_y = 20
        self.viz_canvas.create_text(20, info_y, 
                                  text=f"Current Branch: {self.current_branch}", 
                                  anchor='w', font=('Consolas', 12, 'bold'), fill='#569cd6')
        
        # Draw staging area and working directory
        self.draw_workflow_areas(500, 350)
    
    def draw_workflow_areas(self, start_x, start_y):
        """Draw staging area and working directory status"""
        # Staging Area
        self.viz_canvas.create_rectangle(start_x, start_y, start_x+200, start_y+120, 
                                       outline='#4a5568', width=2, fill='#2d3748')
        self.viz_canvas.create_text(start_x+100, start_y-15, text="Staging Area", 
                                  font=('Arial', 9, 'bold'), fill='#90cdf4')
        
        for i, file in enumerate(self.staged_files[:4]):
            self.viz_canvas.create_text(start_x+10, start_y+20 + i*20, text=f"✓ {file}", 
                                      anchor='w', font=('Consolas', 8), fill='#68d391')
        
        # Working Directory
        work_y = start_y + 140
        self.viz_canvas.create_rectangle(start_x, work_y, start_x+200, work_y+120, 
                                       outline='#4a5568', width=2, fill='#2d3748')
        self.viz_canvas.create_text(start_x+100, work_y-15, text="Working Directory", 
                                  font=('Arial', 9, 'bold'), fill='#90cdf4')
        
        for i, file in enumerate(self.unstaged_files[:4]):
            self.viz_canvas.create_text(start_x+10, work_y+20 + i*20, text=f"• {file}", 
                                      anchor='w', font=('Consolas', 8), fill='#fbb6ce')
        
        # Conflicts
        if self.conflict_files:
            conflict_y = work_y + 140
            self.viz_canvas.create_rectangle(start_x, conflict_y, start_x+200, conflict_y+60, 
                                           outline='#e53e3e', width=2, fill='#742a2a')
            self.viz_canvas.create_text(start_x+100, conflict_y-15, text="Conflicts", 
                                      font=('Arial', 9, 'bold'), fill='#fc8181')
            
            for i, file in enumerate(list(self.conflict_files.keys())[:2]):
                self.viz_canvas.create_text(start_x+10, conflict_y+20 + i*20, text=f"⚡ {file}", 
                                          anchor='w', font=('Consolas', 8), fill='#fed7d7')

def main():
    root = tk.Tk()
    app = GitTutorialGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()