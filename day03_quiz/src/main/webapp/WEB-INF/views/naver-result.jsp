<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원가입 완료</title>
</head>
<body>
<div><h1>회원가입 완료</h1></div>
<div>
	<p>아이디 : ${mem.id }</p>
	<p>비밀번호 : ${mem.pw }</p>
	<p>이름 : ${mem.name }</p>
	<p>생년월일 : ${mem.birth1 }년  ${mem.birth2 }월  ${mem.birth3 }일</p>
	<p>이메일 : ${mem.email }</p>

	<button onclick ="history.go(-1)">이전으로</button>
</div>
</body>
</html>