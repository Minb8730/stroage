<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<h2>비밀번호 변경</h2>

<form method="post">
	<input type="hidden" name="phone" value="${login.phone }">
	<input type="hidden" name="name" value="${login.name }">
	<input type="hidden" name="id" value="${login.id }">

	<p><input type="password" name="currentPw" placeholder="현재 비밀번호" required></p>
	<p><input type="password" name="pw" placeholder="신규 비밀번호" required></p>
	<p><input type="password" name="pw2" placeholder="비밀번호 확인" required></p>
	
	<p><input type="submit" value="변경"></p>
</form>

<script>
	// 대표적인 이벤트 함수 : onclick, onsubmit, onkeyup(실시간으로 하나하나 타이핑할때)
	const form = document.forms[0]; // forms 는 jsp 내의 전체 form을 배열로 가져온다.
	form.onsubmit = function(event) {	// => document.forms[0].fonsubmit
		event.preventDefault(); // 기본 이벤트 작동을 막는다.
								// a 태그라면 링크에 의한 이동을 막는다.
								// form 태그라면 데이터 제출을 막는다.
		console.log(event.target);						
		const pw1 = event.target.querySelector('input[name="pw"]').value;
		const pw2 = event.target.querySelector('input[name="pw2"]').value;
		console.log(pw1, pw2);
		
		if(pw1 == pw2){
			event.target.submit();
		}else{
			alert('신규 비밀번호가 서로 일치하지 않습니다.');
		}
//	event.target.submit();		// 원하는 시점에서 현재 폼을 제출할 수 있다.		
	};
	
</script>


</body>
</html>