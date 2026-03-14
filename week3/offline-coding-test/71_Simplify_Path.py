"""
/week1/basic
/week1/basic/.. -> week1
/week1/basic///// -> week1/basic
/week1/basic
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        # '/'를 기준으로 문자열 자르기
        # 리스트엔 '/'의 자리에 공백이 들어가게 된다
        cmd_list = path.split('/')

        # 반환할 주소 리스트
        simple_path = []

        for cmd in cmd_list:
            # '/' 대신 들어간 공백, 현재 디렉토리로 취급해야 하는 '.'은 담지 않고 넘어간다 
            if cmd == "" or cmd == ".":
                continue
            # 이전 상위 디렉토리로 취급해야 하는 '..'은 pop으로 이전 상위 디렉토리 주소만 남긴다
            elif cmd == "..":
                if simple_path:
                    simple_path.pop()
            # 그 외 다른 디렉토리 이름 및 문자들은 주소로 반환한다
            else:
                simple_path.append(cmd)
        
        # 무조건 루트 디렉토리 '/' 문자 포함
        ## 리스트로 저장했기 때문에 .join 메소드 활용해서 리스트 문자열들을 하나로 합쳐주며 디렉토리 사이 '/'문자를 추가해준다
        simple_path = "/" + "/".join(simple_path)
        return simple_path

        # ------------------------ 내가 풀었던 풀이
        # path_list = list(path.split('/'))
        
        # print(path_list)
        
        # simple_path = []

        # # 경로 첫 시작은 무조건 /
        # #simple_path.append('/')

        # # 받아온 경로를 처음부터 끝까지 순회 
        # for i in range(len(path_list)):
        #     # 일단 디렉토리 요소들 다 push 해줌
        #     simple_path.append(path_list[i])

        #     if path_list[i] == "":
        #         continue

        #     # . 은 현재 디렉토리
        #     elif path_list[i] == ".":
        #         # = . pop 해서 디렉토리 현재 이름만 남기기 
        #         simple_path.pop()
            
        #     # ..은 이전 상위 디렉토리 
        #     elif path_list[i] == "..":
        #         # 첫번째 pop으로 .. 지우고
        #         simple_path.pop()
        #         # 두번째 pop으로 상위 디렉토리 이름만 남기기
        #         simple_path.pop()

        #         # # i가 마지막 디렉터리가 아니라면
        #         # if not i == len(path_list) - 1:
        #         #     # 디렉터리 이름 뒤 슬래시 붙이기
        #         #     simple_path.append('/')    

        # # elif 
        # # / 슬래시 여러 개는 어쩌지
        # simple_path = "/".join(simple_path)
        # #simple_path = "".join(simple_path)

        # for c in simple_path:
        #     if simple_path[i] == len(simple_path) - 1:
                
        # print(simple_path)
        
        # return simple_path
