<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>


<div class="main">
	<h2>회원 가입</h2>
	<form method="POST">
		<p><input type="text" name="userid" placeholder="ID" required autofocus>
			<input id="checkId" type="button" value="중복 확인">
		</p>
		<div id="msg"></div>
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

<script>
	const msg = document.getElementById('msg')				// 서버와 통신 이후, 출력 메시지를 담을 div
	const checkIdBtn = document.getElementById('checkId')	// 클릭에 의해 이벤트를 발생시킬 버튼

	const checkHandler = function(event){					// 이벤트를 어떻게 처리할지 함수를 정의
		const id = document.querySelector('input[name="userid"]').value	// 입력값 불러오기
		const url = '${cpath}/ajax/checkId';			// 서버에게 요청할 주소 (인터셉터에 의해 방해받지 않도록 하자!!)
		const opt = {									// 요청에 대한 옵션
			method : 'POST',							// HTTP Method (GET, POST, PUT, DELETE, PATCH)
			body: JSON.stringify({id: id}),				// POST, PUT, PATCH 의 경우 데이터를 전달할 수 있다. (GET은 안됨. 서버에게 요구하는 작업이기 때문에)
			headers: {
				'Content-Type' : 'application/json'		// 내가 보내는 컨텐트의 타입은 JSON이다 명시를 해준다.
				// JSON : JavaScript Object Notation
			}
		}
		// 자바스크립트 객체를 JSON으로 파싱한 결과를 콘솔창에 출력(웹 브라우저 개발자 도구 F12 - Console)
// 		console.log(JSON.stringify({
// 			id: id,
// 			age: 29,
// 			name: '이지은'
// 			}))
		
		// 가장 최근의 자바스크립트에서 AJAX를 편리하게 구현할 수 있도록 준비된 라이브러리, 표준
		fetch(url, opt)	// url 에 어떠한 작업을 적용
		.then(resp => resp.text()) // 받아온 응답을 어떻게 처리할 것인지. 이 경우는 text
		.then(text => {
			msg.innerText = text;	// div 테그 안쪽에 text 를 집어넣겠다.
			const flag = text == '사용 가능한 ID입니다.'
			msg.style.color = flag ? 'blue' : 'red';
			msg.style.fontWeight = 'bold'
			if(flag == false) {
				document.querySelector('input[name="userid"]').select()	// focus 는 커서, select는 문자열을 선택해준다.
			}
			else{
				document.querySelector('input[name="userpw"]').focus()
			}
		}) 
	}
	checkIdBtn.onclick = checkHandler;
	
</script>
