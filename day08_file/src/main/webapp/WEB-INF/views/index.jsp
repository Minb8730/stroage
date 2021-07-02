<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>DB Gallery</h1>
<hr>
<div style="display : flex; justify-content: center; width:100%;">
	<form method="post" enctype="multipart/form-data">
		<input type="file" name="uploadFile">
		<input type="submit" value="업로드">
	</form>
</div>
<hr>
<div style="display:flex; flex-flow:wrap; width: 600px;">
	<c:forEach var="img" items="${list }">
	<div style="width: 170px; border:2px solid #5a5a5a; padding: 5px;">
		<img src="${cpath }/upload/${img.storedFileName }" width="150px">
	</div>
	</c:forEach>
	
</div>



</body>
</html>