<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<div>
	<h3>회원가입</h3>
	<div>
		<form method="post">
			<p><input type="text" name="userId" placeholder="ID 입력" required autofocus></p>
			<p><input type="password" name="userPw" placeholder="Password 입력" required></p>
			<p><input type="text" name="userName" placeholder="이름" required></p>
			<p><input type="text" name="birth" placeholder="주민등록번호 6자리" maxlength="6" required></p>
			<p><input type="text" name="email" placeholder="이메일"></p>
			<p><input type="text" name="address" placeholder="주소"></p>
			<p><input type="radio" name="gender" value="m" checked>남성<input type="radio" name="gender" value="f" >여성</p>
			<p><input type="submit" value="회원가입"><a href="${cpath }/"><input type="button" value="취소"></a></p>
		</form>
	
	</div>
</div>



</body>
</html>