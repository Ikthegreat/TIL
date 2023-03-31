# Navigation Bar
- Bootstrap Navbar Component 에서 불러와 동일하게 구현하였으나, 각 부분의 색을 바꾸는 과정에서 이해가 어려웠다
- 처음에는 data-bs-theme="dark" 로 생각하였으나, 버튼의 색이 다른 것을 확인
- navbar-dark, navbar-bg-dark 활용하여 색상을 맞추니 Sample 과 동일하게 구현이 가능했다.

# Footer
- Navbar 를 활용할지 고민하다, position-fixed bottom-0 w-100 text-center 활용하여 고정하였음
- 이후 2, 3 번 Home, Community 화면 구현 중 글씨가 다른 Box 뒤로 가는 현상을 발견하였다.
- Fixed-bottom 활용하여 수정

# Home/Header
- 이미지를 최소 3장 이상 사용하여 자동 전환 기능을 구글링해보니 JS 또는 JQuery 사용한 케이스만 볼 수 있어서 당황
- 요구사항을 다시 잘 읽어보니 Bootstrap Carousel Component 로 구성
- 해당 기능을 사용해보니 신기했다.

# Home/Section
- 스크린 샷 예시를 참고하며 row-cols-1 row-cols-md-3 g-4 클래스 활용하여 반응형 구현

# Community
- 가장 고생했던 부분
- Display Property (Bootstrap 웹 페이지) 를 보고 px 사이즈에 따라 숨기거나 보이게 하는 반응형 구현이 가능함을 알게 되었다.
- `d-none d-lg-block large` : hide on screens smaller than lg
- Grid
- col-lg-10 (Screen 이 large 이상인 경우 10/12 칸 차지하도록 (열 기준))

## 느낀 점
- Bootstrap 사용 시 각 클래스에 해당하는 부분이 무엇을 의미하는지 숙달이 필요함을 느꼈다.
- navbar-expand-lg 가 무엇을 의미하는지 한참을 찾아 헤매었다
- Navbars require a wrapping .navbar with .navbar-expand{-sm|-md|-lg|-xl|-xxl} for responsive collapsing and color scheme classes.
- width 에 따라 반응하는 기능을 의미하는 클래스였다.