# SW-AI 컴퓨팅 사고로의 전환 - 레포지토리 템플릿 (Week 2~5)


## 📂 폴더 구조

```
SW_AI-W02-05-TEMPLATE/
├── week2/
│   ├── basic/              # 기본 개념 학습 (10개 문제)
│   │   ├── 01_python_dict.py
│   │   ├── 02_array.py
│   │   └── ...
│   │   └── check.py        # 로컬 테스트 스크립트
│   └── problem-solving/    # 알고리즘 문제 풀이 (20개 문제)
│       ├── 난이도하_파이썬문법_최댓값_브론즈3.py
│       ├── 난이도중_백트래킹_NQueen_골드4.py
│       └── ...
├── week3/
│   ├── basic/
│   └── problem-solving/
├── week4/
│   ├── basic/
│   └── problem-solving/
├── week5/
│   ├── basic/
│   └── problem-solving/
├── problems set.md         # 문제 목록 및 링크
└── README.md               # 본 문서
```

## ⚙️ 저장소 설정하기

이 템플릿을 본인의 GitHub 저장소로 복사합니다:

```bash
# 템플릿 클론 후 새 저장소로 초기화 
git clone <템플릿-저장소-URL> 
cd <템플릿-저장소-URL> 
rm -rf .git
git init
git remote add origin <본인-저장소-URL>
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

```

```bash
# 경로 이동
cd /{드라이브}/{폴더}

# 현재 위치에 새 폴더 없이 저장소 클론
# 반드시 현재 위치(폴더)가 비어있어야 클론 가능
git clone {템플릿-저장소-URL} .
 
```

## ✏️ 작업 내역 반영하기 
```bash
# file 들의 tracking 상태 보기
git status

# 저장소 최신 작업 내역 가지고 오기
# pull을 먼저 진행하지 않으면 나의 로컬 작업 내역을 push 할 수 없음 
git pull

# 커밋할 파일 추가하기
git add <filenName>

# 작업 내역 커밋하기
git commit -m "코멘트"

# 저장소에 작업 내역 반영하기
git push
```

## 그 외 유용한 명령어
```bash
# 한 줄로 그래프 형태로 commit 히스토리 보기
git log --oneline --graph

# remote origin의 development branch merge
git merge origin/development

# remote에서 삭제된 brach를 local 에서도 깔끔하게 삭제
git fetch origin --prune
```

## 📝 문제 풀이 방법

### Basic (로컬 테스트)

각 주차의 `basic` 폴더에는 `check.py` 자동 채점 스크립트가 있습니다.

#### 모든 문제 한 번에 테스트

```bash
# Week 2 기본 문제 전체 테스트
cd week2/basic
python3 check.py --all

# Week 3 기본 문제 전체 테스트
cd week3/basic
python3 check.py --all

# Week 4 기본 문제 전체 테스트
cd week4/basic
python3 check.py --all

# Week 5 기본 문제 전체 테스트
cd week5/basic
python3 check.py --all
```

#### 특정 문제만 테스트

```bash
# 예시: Week 2의 01_python_dict.py만 테스트
cd week2/basic
python3 check.py 01_python_dict.py

# 예시: Week 3의 03_quick_sort.py만 테스트
cd week3/basic
python3 check.py 03_quick_sort.py
```

### problem-solving

실제 문제는 문제링크를 통해 접속한 사이트(백준, LeetCode)에서 풉니다.
각 문제 파일을 열어 풀이 코드를 기록합니다.

```
week2/problem-solving/난이도하_파이썬문법_최댓값_브론즈3.py
```

각 파일에는 문제 링크가 주석으로 포함되어 있습니다:
```python
# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

# 여기에 코드 작성
```
