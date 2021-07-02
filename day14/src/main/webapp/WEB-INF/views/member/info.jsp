<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<div class="main">
	<h2>마이 페이지</h2><br>
	
	<table border="1" cellpadding="10" cellspacing="0" align="center">
		<tr><th>ID</th>		<td>${login.userid }</td></tr>
		<tr><th>PW</th>		<td>********</td></tr>
		<tr><th>NAME</th>		<td>${login.username }</td></tr>
		<tr><th>BIRTH</th>		<td>${login.birth }</td></tr>
		<tr><th>EMAIL</th>		<td>${login.email }</td></tr>
		<tr><th>GENDER</th>		<td>${login.gender }</td></tr>
		<tr><th>ADDRESS</th>		<td>${login.address }</td></tr>
	</table>
</div>

<div class="ce">
	<a href="${cpath }/member/update"><button>정보 수정</button></a>
	<a href="${cpath }/member/changePw"><button>비밀번호 변경</button></a>
	<button id="deleteBtn">회원 탈퇴</button>
</div>

<script>
	document.getElementById('deleteBtn').onclick = function(event) {
		if(confirm('정말 사이트에서 탈퇴하시겠습니까?')) {
			location.href = '${cpath }/member/delete'
		}
	}
</script>

</body>
</html>






