<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<div class="main">
	<h2>새 글 작성</h2>
	
	<form method="POST" enctype="multipart/form-data">
		<p><input type="text" name="title" placeholder="제목을 입력하세요" required></p>
		<p><input type="text" name="writer" value="${login.userid }" readonly></p>
		<p><textarea name="content" placeholder="내용을 입력하세요" required></textarea></p>
		<p><input type="file" name="file"></p>
		<p><input type="submit" value="작성"></p>
	</form>
</div>

</body>
</html>