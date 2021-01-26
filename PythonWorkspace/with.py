# with file을 열고 닫을 필요가 없음

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
# close 로 닫을 필요가 없음 자동으로 with 를 탈출 함.

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "w", encoding = "utf8") as study_file:
    print(study_file.read())