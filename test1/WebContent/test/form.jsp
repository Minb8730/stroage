<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>회원가입</title>
</head>
<body>
	<h2>회원가입</h2>
	<form action = "form_check.jsp" method="post">
		<div>
			이름 : <input type="text" name ="name"><br>
			id : <input type="text" name ="id"><br>
			pw : <input type="password" name ="pw"><br>
			<input type="submit" value="가입">
			<input type="reset" value="취소">
		</div>
	</form>
</body>
</html>