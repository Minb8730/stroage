<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	a {
		text-decoration: none;
		color: inherit;
		cursor: pointer;
	}
	a:hover {
		text-decoration: underline;
	}
	nav {
		display: flex;
		justify-content: flex-end;
	}
	nav > ul {
		display: flex;
		right: 20px;
		list-style: none;
		padding: 0;
		width: 50%;
		justify-content: space-between;
	}
	nav > ul > li {
		text-align: center;
		width: 100px;
		font-weight: bold;
		font-size: 20px;
	}
	.hidden {
		display: none;
	}
</style>
</head>
<body>

<header>
	<h1><a href="${cpath }/">AJAX 연습</a></h1>
	<nav>
		<ul>
			<li><a class="insert" title="가입">가입</a></li>
			<li><a class="search" title="검색">검색</a></li>
			<li><a class="update" title="수정">수정</a></li>
			<li><a class="delete" title="탈퇴">탈퇴</a></li>
		</ul>
	</nav>
</header>
<hr>
<div class="list main">
	<h2>회원 목록</h2>
	
</div>

<div class="insert main hidden">
	<h2>가입</h2>
	<form id="insertForm" method="POST">
		<p>
			<input type="text" name="userid" placeholder="ID" required autofocus>
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

<div class="search main hidden">
	<h2>검색</h2>
	<form id="searchForm">
		<input type="text" name="userid" placeholder ="검색할 ID를 입력하세요">
		<input type="submit" value="검색">
	</form>
</div>




<div class="update main hidden">
	<h2>수정</h2>
	<input type="text" name="userid" placeholder="수정할 ID를 입력">
	<button id="updateIdBtn">찾기</button>
	<form id="updateForm">
		<p>
	</form>
</div>


<div class="delete main hidden">
	<h2>탈퇴</h2>
	<form id="deleteForm">
	
		<p><input type="text" name="userid" placeholder="탈퇴 처리할 계정을 입력하세요"></p>
		<p><input type="submit" value="탈퇴처리"></p>
	</form>
	<div id="deleteMsg"></div>
</div>

<script>
	// update
	// 1) userid를 입력받아서 관련 결과(GET,SELECT)를 화면에 출력한다.
	// 2) 불러온 결과는 form의 형식으로 화면에 출력한다.
	// 3) 사용자가 내용을 수정(PUT,UPDATE)한 후 submit 하면 body를 넣어서 서버에 전송하고 결과를 숫자로 받는다.
	// 4) 숫자에 따라서 메시지를 출력한다.
	const updateForm = document.getElementById('updateForm')
	
	const loadTarget = function(userid){		// 수정할 대상을 불러오는 함수
		const url= '${cpath}/member/' + userid
		const opt= {method: 'get'}
		fetch(url, opt).then(resp => resp.json())
		.then(json =>{
			updateForm.innerHTML = ''
			for(key in json){
				const div = document.createElement('div')
				const input = document.createElement('input')
			
				switch(key){
				case 'userid' : input.type = 'hidden';break;
				case 'userpw' : input.type = 'password'; break;
				case 'birth'  : input.type = 'date'; break;
				default	 	  : input.type = 'text';
				
				}
				
				input.name = key
				input.value = json[key]
				div.appendChild(input)
				updateForm.appendChild(div)
			}
			if(json != null){
				const submit = document.createElement('input')	
				submit.type = 'submit'
				submit.value = '수정'
				updateForm.appendChild(document.createElement('div').appendChild(submit))
			}
			else {
				const h3 = document.createElement('h3')
				h3.innerText = '계정을 찾을 수 없습니다.'
				updateForm.appendChild(h3)
			}
		})
		
	}

	const updateSubmitHandler = function(event) {		// updateForm 이 submit 되면 호출할 함수
		event.preventDefault()
		const formData = new FormData(event.target)  // formData는 내부 속성이 없다.
		const ob = {}
		for (key of formData.keys()){
			ob[key] = formData.get(key)		// formData에서 key가 name에 해당한다. key를 전달하여 value를 받는다.
		}
		console.log(JSON.stringify(ob))
		const url = '${cpath}/member/'
		const opt ={
				method : 'put',
				body: JSON.stringify(ob),
				headers: {
					'Content-Type' : 'application/json; charset=utf-8' // GET, POST 에서만 사용 가능
			}
		}
		fetch(url, opt)
		.then(resp =>resp.text())
		.then(text =>{
			console.log('update :' + text)
			if(text == 1){
				location.href = '${cpath}'
			}
		})
	}
	
	updateForm.onsubmit = updateSubmitHandler
	
	document.getElementById('updateIdBtn').onclick = function(event){
		const userid = event.target.previousElementSibling.value	// 같은 노드 안에서만 적용. 태그 순서대로 했을 때 한단계 이전의 요소(Element) 를 가져온다.
		loadTarget(userid)
		event.target.previousElementSibling.readOnly = 'readonly'
	}
	
	

</script>



<script>
	// delete member2 where userid=?
	// 계정을 선택(select)하고, 검색된 계정이 있으면 탈퇴를 진행한다.
	
	document.getElementById('deleteForm').onsubmit = function(event){
		event.preventDefault()
		const url = '${cpath}/member/' + event.target.querySelector('input[name="userid"]').value
		const opt ={
				method: 'DELETE'		// @DeleteMapping(url, opt)
		}
		fetch(url, opt)
		.then(resp => resp.text())
		.then(text => {
// 			console.log(typeof text) 	// int 로 반환되도 형변환 되어서 String(text) 으로 받아진다.
			if(text == 1){ // 문자열을 받아도, 자바스크립트는 == 이면 값만 비교한다. === 이면 타입도 비교한다.  ex) 1 == '1' : true
				document.getElementById('deleteMsg').innerText = '탈퇴 처리되었습니다.'
			}
			else{
				alert('요청받은 계정을 찾을 수 없습니다.')
// 				document.getElementById('deleteMsg').innerText = '요청받은 계정을 찾을 수 없습니다.'
			}
		})
	}
</script>



<script>
	document.getElementById('searchForm').onsubmit = function(event){
		event.preventDefault()
		const url = '${cpath}/member/' + event.target.querySelector('input[name="userid"]').value
		const opt = {
			method: 'get'
		}
		
		fetch(url, opt)
		.then(function(resp) { return resp.json() })
		.then(function(json){

			const div = document.createElement('div') 	// <div></div>
			div.classList.add('searchResult')		// <div class = "searchResult"></div>
			
			for(key in json){		// {} 형식의 객체에 대해서 멤버(속성) 이름을 가져오려면 for ~ in 형식 사용, key 변수 대신 아무거나 사용 가능
				const childDiv = document.createElement('div')
				childDiv.innerText = key + ' : ' + json[key]
				div.appendChild(childDiv)
			}
			
			if(json == null){
				div.innerText = '검색 결과가 없습니다.'
			}
			
			if(document.querySelector('div.searchResult') != null){
				document.querySelector('div.searchResult').remove()
			}
			document.querySelector('div.search').appendChild(div)
		})
	}
</script>


<script>
	// 1) 서버에 목록을 요청하는 코드 작성하기
	const url = "${cpath}/member/"
	const opt = {
			method: 'get'
	}
// 	.then(resp => resp.json())
// 	.then(json =>{
	fetch(url, opt)
	.then(function(resp) {return resp.json()})
	.then(function(json) {
// 		console.log(json)
// 		console.log(json instanceof Array)
		
	// HTML 요소를 만들고 값을 채워넣어서 화면에 반영하기
	const ul = document.createElement('ul')
	for(let i = 0; i < json.length; i++){
		const li = document.createElement('li') // 새로운 HTML 요소를 만들어준다.
		const userid = json[i].USERID
		const username = json[i].USERNAME
		const email = json[i].EMAIL
		li.innerText = userid + ' / ' + username + ' / ' + email
		ul.appendChild(li) // HTML 요소를 자식 요소로써 부모 요소에게 추가한다.  ul 안에 자식 요소로 넣어주겠다.
	}
	document.querySelector('div.list').appendChild(ul)	
		})
</script>

<script>
	document.querySelectorAll('nav > ul > li > a').forEach(a => a.onclick = function(event) {
		const className = event.target.className
		document.querySelectorAll('.main').forEach(div => div.classList.add('hidden'))
		document.querySelector('div.' + className).classList.remove('hidden')
	})
	
	document.getElementById('checkId').onclick = function(event) {
// 		console.log('이벤트 함수 호출 !!')
		const userid = document.querySelector('input[name="userid"]').value
		const url = '${cpath}/member/' + userid		//member/{userid}		
		const opt ={
				method: 'GET',	// HTTP Method GET 에서는 body 를 작성하지 않는다.
		}
		fetch(url, opt)					// JSON.stringify(object) : object를 json형식의 string 으로 변환
		.then(resp => resp.json())		// JSON.parse(string) : 객체형식의 string을 object 형식으로 변환      //fetch 에서 resp.json() 이 string 을 자동으로 객체로 변환시켜줌
		.then(json => {
// 			console.log('json : ' , {'json' : json})	
			if( json == null ){
				document.getElementById('msg').innerText = '사용 가능한 ID입니다.'
				document.getElementById('msg').style.color = 'blue'
				document.querySelector('input[name="userpw"]').focus()
				
			}else{
				document.getElementById('msg').innerText = '이미 사용중인 ID입니다.'
				document.getElementById('msg').style.color = 'red'
				document.querySelector('input[name="userid"]').select()

			}
				document.getElementById('msg').style.fontWeight = 'bold'
		})
	}
		
	
</script>

<script>
	// 회원가입 처리
	document.getElementById('insertForm').onsubmit = function(event){	//form을 submit하면 
		event.preventDefault();								// 기본 작동을 막고

		
/* 		const formData = new FormData(event.target)			// submit 된 form을 기반으로 formData를 생성
		const ent = formData.entries();						// formData 의 엔트리를 불러와서
		let ob = {};										// 비어있는 객체 생성
		while(true){
			next = ent.next();								
			if(next.done) break;							// 만약, 엔트리 순회가 끝났으면 break;
			ob[next.value[0]] = next.value[1];				// 엔트리의 0번째는 key, 엔트리의 1번째는 value
		}
		const json = JSON.stringify(ob)						// ob를 json으로 변경
		console.log(json)									// 화면에 출력
		
		// 여기서부터 ajax
		const url = '${cpath}/member/'
		const opt = {
				method: 'post',
				body: json,
				headers:{
					'Content-Type' : 'application/json; charset=utf-8'
				}
		}	
		// formData를 직접 전송할 때는 headers에 Content-Type을 명시하지 말자
		// form을 이용하여 multipart/form-data 형식으로 전송 할 때도, 컨텐트 타입을 명시하지 않는다.
		// Content-Type 은 text/plain이 아닌 정보를 전송하는 경우
		*/
		
		const formData = new FormData(event.target)			
		const url = '${cpath}/member/'
		const opt = {
				method: 'post',
				body: formData,
		}

		fetch(url, opt)
		.then(resp => resp.text())
		.then(text => {
			console.log(text)
			if(+text == 1){ 	// 변수 앞에 + 를 붙이면 정수형으로 변환
				event.target.reset();
				document.getElementById('msg').innerText = '';
				alert('회원 가입 성공!!');
			}else{
				alert('회원 가입 실패...');
			}
		})
	}
	
	
</script>
</body>
</html>