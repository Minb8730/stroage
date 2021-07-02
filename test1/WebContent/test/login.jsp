<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>로그인</title>
</head>
<body>
	<form action = "login_check.jsp" method = "post">
		<div>
			아이디 : <input type="text" name = "id"><br>
			비밀번호 : <input type="password" name = "pw"><br>
			<input type="submit" value="확인">
			<input type="reset" value="취소">
		</div>
	</form>	
	
</body>
</html>