<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h1>글 읽기</h1>

	<p>제목 : ${dto.title }</p>
	<p>아이디 : ${dto.writer }</p>
	<p>${dto.content }</p>
	<p>비밀번호 : <input type="password" name="password" placeholder="비밀번호 입력" required></p>

	<p><a href ="${cpath }/update/${dto.idx}"><button id="udateBtn">수정하기</button></a></p>
	
	<script>
	document.getElementById('updateBtn').onclick = function() {
		if(dto.password.equals(getElementById('password'))){
			location.replace("${cpath}/delete/${login.id}");
			}else{
				alert("비밀번호가 일치하지 않습니다.");
			}
	};
</script>
	
</body>
</html>