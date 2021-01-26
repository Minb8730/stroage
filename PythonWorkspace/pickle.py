# pickle은 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장
'''

import pickle
profile_file = open("profile.pickle", "wb") # write, 바이너리를 꼭 정해주어야 pickle을 사용할 수 있음
profile = {"이름":"박명수","나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile. profile_file) #profile 에 있는 정보를 file 에 저장
profile_file.close()
'''

# 파일에 저장된 정보, 데이터를 불러와서 파일에 있는 정보를 변수에 저장해서 계속 쓸수 있게 만들어줌
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
