## **git**

버전 관리 프로그램

---

### 명령어

- `git init`
	- git Repository 만들기
- `git add {파일 이름}`
	- Staging area에 추가
- `git commit -m '{message}'`
	- Commit(기록) 남기기
- `git status`
	- 상태 확인
- `git log`
	- Commit 확인
	- `git log --oneline`
- `git remote add origin {url}`
	- 원격 연결
- `git push origin master`
	- 업로드
	- `git push -u origin master`
- `git config --global user.name {name}`
- `git config --global user.email {email}`

- `git clone {url}`
	- 깃허브에 있는 깃 새로 가져오기
- `git pull origin master`
	- 이미 연결된 상태에서 당겨오기
- `git commit --amend`
	- 커밋 수정
	- vim 에디터가 나옴
		- i => insert 모드
		- esc => 모드 나가기
		- :wq => 저장 후 나가기
- `.gitignore`
	- git에서 관리하지 않는 파일/폴더의 모음
	- gitignore.io 사용