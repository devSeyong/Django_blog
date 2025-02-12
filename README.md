# 📌 Django 블로그 프로젝트

## 📝 프로젝트 소개
**Django 기반의 블로그 플랫폼**  
사용자가 게시글을 작성하고 댓글을 통해 소통할 수 있는 블로그 서비스입니다.



## 📅 프로젝트 기간
- 2025년 2월 5일 ~ 2월 11일



## 🛠 기술 스택
- **Backend**: Python 3.13, Django 5.1, SQLite3  
- **Frontend**: Django Template, Bootstrap, HTML/CSS, JavaScript  
- **Library**: django-widget-tweaks(폼 렌더링), Pillow(이미지 처리)



## 💡 구현된 기능
### 1️⃣ 사용자 관리 (`accounts` 앱)
- **회원가입 (`SignUpView`)**  
  - `UserCreationForm`을 확장하여 회원가입 기능 구현  
  - 아이디(`username`), 이메일(`email`) 중복 검사  

- **로그인 (`CustomLoginView`)**
  - 로그인 실패 시 오류 메시지 제공

- **로그아웃 (`CustomLogoutView`)**  
  - Django 기본 `LogoutView` 사용

- **프로필 관리**  
  - **프로필 조회 (`ProfileView`)** → 본인 프로필 및 작성한 게시글 목록 표시  
  - **다른 유저의 프로필 조회 (`UserProfileView`)** → 특정 사용자의 프로필 조회 가능  
  - **프로필 수정 (`ProfileEditView`)** → `ProfileUpdateForm`을 사용하여 프로필 사진, 자기소개 수정 가능  

- **비밀번호 찾기**  
  - **아이디 찾기 (`FindUsernameView`)** → 이름과 이메일을 입력하여 가입된 아이디 확인 가능  
  - **비밀번호 재설정 요청 (`PasswordResetRequestView`)**
    - 인증코드 발송 후 비밀번호 변경 가능  
    - Google SMTP 서버(Gmail) 사용하여 인증 코드 이메일 전송
  - **비밀번호 변경 (`PasswordResetView`)** → 인증코드 확인 후 새로운 비밀번호 설정  

### 2️⃣ 블로그 기능 (`blog` 앱)
- **게시글 관리**  
  - **게시글 목록 조회 (`PostListView`)**  
    - 전체 게시글을 최신순으로 정렬하여 조회
    - 검색 기능(`title`, `author.username`) 제공  
  - **게시글 상세 조회 (`PostDetailView`)**  
    - 게시글 정보 및 작성된 댓글 목록 표시  
  - **게시글 작성 (`PostCreateView`)**  
    - 로그인한 사용자만 작성 가능 (`LoginRequiredMixin` 적용)  
    - 작성자 자동 지정  
  - **게시글 수정 (`PostUpdateView`)**  
    - 본인이 작성한 글만 수정 가능  
  - **게시글 삭제 (`PostDeleteView`)**  
    - 본인이 작성한 글만 삭제 가능  

- **댓글 관리**  
  - **댓글 작성 (`AddCommentView`)**  
    - 로그인한 사용자만 댓글 작성 가능
    - Ajax 요청을 받아 JSON 형태로 응답 반환
  - **댓글 수정 (`EditCommentView`)**  
    - 본인이 작성한 댓글만 수정 가능
  - **댓글 삭제 (`DeleteCommentView`)**  
    - 본인이 작성한 댓글만 삭제 가능

---

## 📁 프로젝트 구조
```
📂 프로젝트 루트
│── config/                  # Django 프로젝트 설정
│── accounts/                # 사용자 관리 (회원가입, 로그인, 프로필)
│── blog/                    # 블로그 기능 (게시글, 댓글)
│── static/                  # 정적 파일 (CSS, 이미지)
│── templates/               # 템플릿 파일 (HTML)
│── media/                   # 업로드된 이미지 저장
│── manage.py                # Django 관리 스크립트
```

## ⚙️ 설치 및 실행 방법
### 1️⃣ 저장소 클론
```bash
git clone https://github.com/devSeyong/Django_blog.git
cd Django_blog
```
### 2️⃣ 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3️⃣ 패키지 설치
```bash
pip install -r requirements.txt
```
### 4️⃣ 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ 서버 실행
```bash
python manage.py runserver
```
---

![ERD](https://github.com/user-attachments/assets/f4a1b168-6fc4-43e4-8549-2cb3c4cb1407)

---

## 🔍 API 명세
### 사용자 관리 API
| 메서드 | URL 패턴 | 기능 | 인증 필요 |
|--------|------------------|-------------|-------------|
| POST | /accounts/signup/ | 회원가입 | X |
| POST | /accounts/login/ | 로그인 | X |
| POST | /accounts/logout/ | 로그아웃 | O |
| GET/POST | /accounts/profile/ | 프로필 조회/수정 | O |
| GET | /accounts/profile/<int:pk>/ | 다른 사용자 프로필 조회 | O |
| POST | /accounts/change_password/ | 비밀번호 변경 | O |

### 게시글 API
| 메서드 | URL 패턴 | 기능 | 인증 필요 |
|--------|------------------|-------------|-------------|
| GET | / | 게시글 목록 조회 | X |
| GET | /post/<int:pk>/ | 게시글 상세 조회 | X |
| GET | /post/create/ | 게시글 작성 폼 | O |
| POST | /post/create/ | 게시글 작성 | O |
| GET | /post/<int:pk>/edit/ | 게시글 수정 폼 | O |
| POST | /post/<int:pk>/edit/ | 게시글 수정 | O |
| DELETE | /post/<int:pk>/delete/ | 게시글 삭제 | O |

### 댓글 API
| 메서드 | URL 패턴 | 기능 | 인증 필요 |
|--------|--------------------------|-------------|-------------|
| POST | /post/<int:post_pk>/comment/ | 댓글 작성 | O |
| POST | /comment/<int:comment_id>/edit/ | 댓글 수정 | O |
| POST | /comment/<int:comment_id>/delete/ | 댓글 삭제 | O |

### 검색 API
| 메서드 | URL 패턴 | 기능 | 인증 필요 |
|--------|------------------|-------------|-------------|
| GET | /?q=검색어 | 검색 기능 | X |

---

## 작업 진행 상황 (WBS)

### 기획 및 개발 준비 (2월 5일)
- [✅] 요구사항 정의
- [✅] DB 설계 (모델 정의)
- [✅] Django 프로젝트 및 앱 생성
- [✅] URL 구조 설계

### 회원 관리 기능 (2월 6일 ~ 2월 7일)
- [✅] 회원가입 기능 개발 (SignUpView, Form, Model)
- [✅] 로그인/로그아웃 기능 개발 (CustomLoginView, CustomLogoutView)
- [✅] 프로필 조회 (ProfileView, UserProfileView) 기능 개발
- [✅] 프로필 수정 (ProfileEditView) 기능 개발
- [✅] 비밀번호 찾기 기능 추가 (FindUsernameView, PasswordResetRequestView, PasswordResetView)
- [✅] Google SMTP를 활용한 이메일 인증 코드 전송

### 게시글 기능 (2월 8일 ~ 2월 9일)
- [✅] 게시글 작성 (PostCreateView) 기능 개발
- [✅] 게시글 목록 조회 (PostListView) 기능 개발
- [✅] 검색 기능 (title, author.username) 추가
- [✅] 게시글 상세 조회 (PostDetailView) 기능 개발
- [✅] 게시글 수정 (PostUpdateView) 기능 개발
- [✅] 게시글 삭제 (PostDeleteView) 기능 개발

### 댓글 기능 (2월 9일)
- [✅] 댓글 작성 (AddCommentView) 기능 개발 (Ajax 기반)
- [✅] 댓글 수정 (EditCommentView) 기능 개발 (Ajax 기반)
- [✅] 댓글 삭제 (DeleteCommentView) 기능 개발 (Ajax 기반)

### UI 구현 (2월 10일 ~ 2월 11일)
- [✅] 기본 템플릿 구조 설계 (HTML)
- [✅] 부트스트랩을 활용한 스타일링

### 테스트 및 마무리 (2월 11일)
- [✅] 기능 테스트 및 최종 점검
- [✅] 발표 자료 정리

![WBS최종본](https://github.com/user-attachments/assets/223b9d29-54c8-4eb2-a49e-192a2c7fc93d)

---

ERD
![ERD](https://github.com/user-attachments/assets/eae75d2e-4a2a-45bb-ac6a-ddd8b8c276cf)






