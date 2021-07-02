<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<div class="login">
	<h2>login</h2>
	<div>
		<form method="post" id="loginForm">
			<p>
				<input type="text" name="userid" placeholder="ID">
			</p>
			<p>
				<input type="password" name="userpw" placeholder="Password" autocomplete="off">
			</p>
			<p>
				<input type="submit" value="로그인">
			</p>
		</form>
	</div>
</div>


<script>


const form = document.getElementById('loginForm')
const URL = document.getElementById('URL')
form.onsubmit=function(event){
	event.preventDefault()
	const formData = new FormData(event.target)
	const ob = {}
	for(key of formData.keys()){
		ob[key] = formData.get(key) 
	}
	const url = '${cpath}/login'
	const opt = {
			method : "POST",
			body : JSON.stringify(ob), 
			headers: { 
				'Content-Type' : 'application/json; charset=utf-8',
			}
	}
	fetch(url,opt).then(resp => resp.text())
	.then(text => {
		console.log(text)
		if(text== 'true'){
			alert('로그인에 성공하셨습니다');
			location.href='${cpath}/'
		}else{
			alert('로그인에 실패하셨습니다.')
		}
	})
}


</script>
</body>
</html>