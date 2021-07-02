<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<h1>글 쓰기</h1>
<form method="post" enctype="multipart/form-data">
	<input type="hidden" name="ipaddr" value=${pageContext.request.remoteAddr }>
	<p>제목 : <input type="text" name="title" placeholder="제목" required></p>
	<p><input type="file" name="uploadFile"></p>
	<p>아이디 : <input type="text" name="writer" placeholder="아이디 입력" required></p>
	<p><textarea cols="200" rows="10"" name="content" placeholder="내용 입력"></textarea></p>
	<p>비밀번호 : <input type="password" name="password" placeholder="비밀번호 입력" required></p>
	<p><input type="submit" value="저장"></p>
</form>

<body>

</body>
</html>