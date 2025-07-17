### What is git
- **Version Control System**
    - version control is tracking and recording changing points
    - Git saves only revised things on each version

- **Distributed version control system**
     - Save and control version each copied storage
        - Can keep copied versions when one storage broked
        - If each user make diffrent revise thing, Can check only different points, when conbine verisons


    - If use centralized system
        - Careless of risk
        - Difficurty of revising by multiple user

- **3 Divided area**
    - Working directory
        - current using directory
         - Control by Git

    - Staging Area
        - Middle prepare area(Tempolary files, But physically exist) 
        - Tracking changed, prepared file in working directory before commit
            ``` 
            The staging area is a place where Git keeps track of changes that are marked to be included in the next commit. It allows you to group specific updates together before finalizing them.
            ```

    - Repository
        - Commit every verion and file perminent
        - Storage controled Git

### Remote Repository
- **Save codes on web like software**

### Reset git config
    - delete git config --global setting
        - `code ~/.gitconfig` [enter]
        - remove your all information
    - find `win+자격증명` -> 자격증명 관리자 -> delete github and gitlap accounts information 
    