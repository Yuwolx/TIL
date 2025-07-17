# Branch
**When you see vim, write :q to finish**
## Advantage
    - Can keep master branch safe from risk because form independant devleop circumstance
    - Project will be more clearly and Structed

## Code
- `git branch -c victor/login`
    - `git branch -c(create) [name]/[purpose]`: [Branch name]

- `git switch [branch name]`
    - change working space

- `git merge [branch name]`
    - [branch name] merge to current user, almost master
    - fastforward merge
    - if there are addtional merge log
        - Have to make new commit 
            - Three way merge

- `git branch -d [branch name]`
    - Those branch delected

## If conflit in remote repository (workflow)
- synchlonize master version by pull from remote repository
    - merge, master to my branch 
        - resolve conflict
**or**
- pull to my branch from remote master last version
    - fix confilct
        - request merge to remote hub by push

- **last routine**
    - synchlonize master version on local circumstance from remote repository

- Orginize
    - no one revise master branch
    - master branch initial setting by common status
    - Create my branch for dev(development) branch