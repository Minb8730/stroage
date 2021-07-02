<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h1>글 수정</h1>
	<form method="post">
		<input type="hidden" value="${dto.idx }">
		<p>제목 : <input type="text" name="title" placeholder="제목" required value = "${dto.title }"></p>
		<p>아이디 : ${dto.writer }</p>
		<p><textarea cols="200" rows="10"" name="content" placeholder="내용 입력">${dto.content }</textarea></p>
		<p>비밀번호 : <input type="password" name="password" placeholder="비밀번호 입력" required></p>
		<p><a><button id="updateBtn" data-password="${dto.password }">수정하기</button></a></p>
	</form>
	
	
</body>
</html>