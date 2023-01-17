post = int(input('게시글의 총 갯수를 입력하세요 : '))
onepage = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))

import math

page = math.ceil(post / onepage) 

print(page)