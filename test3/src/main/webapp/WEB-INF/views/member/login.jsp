<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<h2>로그인</h2>
<form method="post">
	<div>
		<p>ID : <input type="text" name="userId" placeholder="아이디입력" required></p>
		<p>PW : <input type="password" name="userPw" placeholder="비밀번호입력" required></p>
		<p>
			<input type="submit" value="로그인">
			<a href="${cpath}/member/insert"><input type="button" value="회원가입"></a>
		</p>
	</div>
</form>



</body>
</html>