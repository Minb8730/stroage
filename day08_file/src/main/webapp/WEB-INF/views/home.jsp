<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    
<c:set var="cpath" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>파일 업로드 연습</title>
</head>
<body>

<h1><a style="text-decoration: none; color: inherit;"
		href="${cpath }">파일 업로드</a></h1>
<hr>
<a href="${cpath }/gallery" style="text-decoration: none;">
	<button style="all: unset; background-color: black;
			color: white; width:250px; height: 50px;
			padding: 5px 20px; text-align: center;
			font-size: 20px; font-weight:900;
			position: absolute; right:50px;">	
		DB에 업로드되는 갤러리
	</button>
</a>
<div style="display:flex; width: 500px; height: 300px;
			justify-content: center; align-items: center;
			border: 2px solid black; padding: 20px;">
			
	<form method="post" enctype="multipart/form-data">
		<p><input type="file" name="uploadFile"></p>
		<p><input type="submit" value="업로드"></p>
	</form>
</div>

<div style="width: 700px; display: flex; flex-flow: wrap; border: 3px solid #dadada;
		justify-content: flex-start; align-items: center;
		margin: 20px auto; over-flow-x: hidden; overflow-y: auto;">			 
	<c:forEach var="img" items="${list }">
	<div style = "margin:10px;">
		<a href="${cpath }/upload/${img}" target="_blank">
			<img src="${cpath }/upload/${img}" width="200px">
		</a>
	</div>
	</c:forEach>
</div>
</body>
</html>