<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>


<div class="main">
	<h2>회원 가입</h2>
	<form method="POST">
		<p><input type="text" name="userid" placeholder="ID" required autofocus></p>
		<p><input type="password" name="userpw" placeholder="Password" required ></p>
		<p><input type="text" name="username" placeholder="이름" required ></p>
		<p><input type="email" name="email" placeholder="foo@bar.com" required ></p>
		<p><input type="text" name="address" placeholder="주소를 입력하세요" required ></p>
		<p>
			<label><input type="radio" name="gender" value="남" required>남성</label>
			<label><input type="radio" name="gender" value="여" required>여성</label>
		</p>
		<p>
			<b>생년월일</b><br>
			<input type="date" name="birth" required >
		</p>
		<p><input type="submit" value="가입신청"></p>
	</form>
</div>

</body>
</html>