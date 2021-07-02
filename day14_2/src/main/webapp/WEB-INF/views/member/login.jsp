<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<div class="main">
	<h2>로그인</h2>
	<form method="POST">
		<p><input type="text" name="userid" placeholder="ID" required autofocus></p>
		<p><input type="password" name="userpw" placeholder="Password" required></p>
		<p><input type="submit" value="로그인"></p>
	</form>
	
	<br><br>
	
	<div>
		<a href="${cpath }/member/join">회원가입</a> <b>|</b> 
		<a href="${cpath }/member/findId">ID찾기</a> <b>|</b>
		<a href="${cpath }/member/findPw">비밀번호 재발급</a> 
	</div>
</div>
</body>
</html>