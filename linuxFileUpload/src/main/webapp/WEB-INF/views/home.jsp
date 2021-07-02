<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<h1>리눅스 서버에 파일 업로드</h1>
<hr>

<form method ="POST" enctype="multipart/form-data">
	<input type="file" name="file">
	<input type="submit" value="전송">
</form>

<c:if test="${not empty uploadFileName }">
	<img src="${uploadFileName }">
</c:if>

</body>
</html>