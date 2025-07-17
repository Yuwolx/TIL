# Command Line Interface
- 명령어를 써서 컴퓨터와 상호작용 한다
- GUI
    - 그래픽을 통해 상호작용 하는 것
        - 폴더 열기 등

- Unix 운영체제에서 이 형태로 작동이 된다.
    - 써야 할 일이 있을 것이다.
    - AWS 할 때: 배포 할 때, CLI 명령어를 써야 한다.

- . 의 역할
    - . 
        - 현재 디렉토리
        - 현재 폴더에 있는 다른 파일 찾기 위해서는 현재 디렉토리를 본다.
    - ..
        - 현재의 상위 디렉토리(부모 폴더)

### Bagic Grammer
- touch
    - make file
    - `touch [file_name].txt`

- mkdir (make directory)
    - make folder
    - `mkdir [folder_name]`

- ls
    - print all folder in current working directory
    - `ls -al`

- cd
    - change current working directory location
    - `cd ..`
        - and `makdir [folder_name]` then make new file in new location
    - `cd ../01_git/`
        - go to 01_git in parent folder
    - `cd ../0 [tap][tap]`
        - Can see other folder name that start 0
    - `cd ../02[Tap]`
        - Auto complete

- start
    - open file/folder
    - open by VS code

- remove
    - `rm [file_name]`
    - Can delete file
        - Can't restore
    - `rm [file_name] [file_name2]`
        - delete all files in code split by space
    - `rm -r [forder_name]`
        - If want delete folder, use `-r`
            - That mean recursive funtion

- `git init`
    - Commit, Use current location for directory controled git

- `git add 00_startcamp/01_git/markdown.md`
    - Convey to staging area

- `git commit -m "insert message"`
 - Convet repository

- `git config --global user.email "you@example.com"`
- `git config --global user.name "Your Name"`
    - Enroll your information before initial try commit
    - Saved in computer 
    - If use local instead gloabl, then information setting for only local circumstance
        - `code ~/.gitconfig`
            - Can fix your information where information wrtitted location

- `git log`
    - Can check commit log

- `echo "# TIL" >> README.md`
    - Create 'README.md' file with "# TIL" on first line

- `git remote add origin https://github.com/Yuwolx/TIL.git`
    - add remote storage [name] is 'origin' that mean remote sever representative name

- `git push -u origin master`
    - Push to remote repository current git

- `git diff`
    - Show differenct between current file and last commit
    - **`git difftool` is better
        - Show display more efficiently

- `git diff [commit id]`
    - you can find commit id by use `git log --online --all`
    - Can compare current commit and id commit


### 문법 및 활용
- 절대 경로
    - 모든 경로 표시, '/'로 구분

- 상대 경로
    - 상대적 위치로 작성
    - 대부분 상대경로로 얘기 함
