<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>인증 메일 예제</title>
<style>
	fieldset {
		width: 500px;
		display: flex;
		flex-flow: column;
		justify-content: center;
	}
	.hidden{
		display: none;
	}

</style>
</head>
<body>

<h1>인증 메일 예제</h1>
<hr>

<form id="sendMailForm">
	<fieldset>
		<legend><h4>이메일 주소 입력</h4></legend>
		<div>
			<input type="email" name="email" placeholder="이메일 주소">
			<input type="submit" value="인증번호 전송">
		</div>
		<div id="sendMailMsg"></div>
	</fieldset>
</form>

<form id="authMailForm" class="hidden">
	<fieldset><h4>인증 번호 입력</h4>
		<div>
			<input type="text" name="auth" placeholder="인증 번호를 입력하세요">
			<input type="submit" value="인증">
		</div>
		<div id="authMailMsg"></div>
	</fieldset>
</form>

<script>

	const sendMailForm = document.forms[0]
	const sendMailMsg = document.getElementById('sendMailMsg')
	
	const sendMailHandler = function(event){
		event.preventDefault()
		const email = event.target.querySelector('input[type="email"]')
		
		const url = '${cpath}/mailto/' + email.value + '/'
		const opt = {
			method: 'get'
		}
		
		fetch(url, opt).then(resp =>resp.text())
		.then(text=> {
			// 정상처리되었다면 128자리의 해시값이 반환된다.
			console.log(text)
			if(text.length == 128){
				authMailForm.classList.remove('hidden')
				sendMailMsg.innerText = '입력한 이메일로 인증 번호를 전송했습니다.'
				sendMailMsg.style.color = 'blue'
				sendMailMsg.style.fontWeight = 'bold'
			}else{
				sendMailMsg.innerText = '이메일을 확인하지 못했습니다.'
				sendMailMsg.style.color = 'red'
				sendMailMsg.style.fontWeight = 'bold'
			}		
		})
	}
	
	sendMailForm.onsubmit = sendMailHandler


</script>

<script>

	// 인증번호를 검증
	
	const authMailForm = document.forms[1]
	const authMailMsg = document.getElementById('authMailMsg')
	let authResult;
	
	const authHandler = function(event){
		event.preventDefault()
		
		const userNumber = event.target.querySelector('input[name="auth"]')
		const url = '${cpath}/getAuthResult/' + userNumber.value
		const opt = {
				method: 'get'
		}
		fetch(url,opt).then(resp => resp.text())
		.then(text =>{
// 			console.log(text)
			authMailMsg.innerText = ''  		// 첫번째 인증이 실패했다면 메시지가 출력된 상태일 것이므로
			
			if(text == 'true'){		// text 값으로 반환되기 때문에 텍스트로 비교해준다.
				authMailMsg.innerText = '인증 성공!!'
				authMailMsg.style.color = 'blue'
				authMailMsg.style.fontWeight = 'bold'
				authResult = true
			}else{
				authMailMsg.innerText = '인증 실패!!'
				authMailMsg.style.color = 'red'
				authMailMsg.style.fontWeight = 'bold'
				authResult = false
			}
			
		})
	}
	
	authMailForm.onsubmit = authHandler


</script>


















</body>
</html>