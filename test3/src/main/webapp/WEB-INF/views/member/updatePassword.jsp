<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<h2>비밀번호 변경</h2>

<form method="post">
	<input type="hidden" name="userId" value="${login.userId }">

	<p><input type="password" name="userPw" placeholder="현재 비밀번호" required></p>
	<p><input type="password" name="pw" placeholder="신규 비밀번호" required></p>
	<p><input type="password" name="pw2" placeholder="비밀번호 확인" required></p>
	
	<p><input type="submit" value="변경"></p>
</form>




<script>

	const form = document.forms[0]; 
	form.onsubmit = function(event) {	
		event.preventDefault(); 
		console.log(event.target);						
		const pw1 = event.target.querySelector('input[name="pw"]').value;
		const pw2 = event.target.querySelector('input[name="pw2"]').value;
		console.log(pw1, pw2);
		
		if(pw1 == pw2){
			event.target.submit();
		}else{
			alert('신규 비밀번호가 서로 일치하지 않습니다.');
		}
	};
	
</script>

</body>
</html>