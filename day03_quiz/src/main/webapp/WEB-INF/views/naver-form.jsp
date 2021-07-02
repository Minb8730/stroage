<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원가입</title>
</head>
<body>
<form method="post">
<div><h1>회원가입</h1></div>
<div>
	<p>아이디</p>
	<input type="text" name ="id" placeholder ="ID">
	<p>비밀번호</p>
	<input type="password" name ="pw" placeholder = "PASSWORD">
	<p>이름</p>
	<input type="text" name ="name" placeholder = "이름">
	<p>생년월일</p>
	<input type="text" name ="birth1" placeholder = "년(4자)">
	<input type="text" name ="birth2" placeholder = "예시(05)" >
	<input type="text" name ="birth3" placeholder = "예시(07)">
	<p>이메일</p>
	<input type="text" name ="email">
	<input type="submit">


</div>

</form>

</body>
</html>