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
<style>
.top_nav{
	display: flex;
	clear: both;

}
.top_nav > h2{
  width:50%;
  margin:0 auto;
  
}
a:link{
	text-decoration: none;
	color: black;
}
a:visited{
	color: black;
}
a:hover {
	background-color: black;
	color: white;
}
.login{
	width:200px; margin: 0 auto;
}
.name{
	float: right;
	
}
</style>
<body>

<h1><a href="${cpath }/">AjaxLogin</a></h1>
<div>
	<div class="name">
		<c:if test="${empty login }">
			<b>응시자: 민성기</b>
		</c:if>
		<c:if test="${not empty login }">
			<b>로그인 : ${login.userid } ${login.username }</b>
		</c:if>
	</div>
	<div class="top_nav">
		<c:if test="${empty login }">
			<h2><span><a href="${cpath }/login">LOGIN</a></span></h2>
		</c:if>
		<c:if test="${not empty login }">
			<h2><span><a href="${cpath }/logout">LOGOUT</a></span></h2>
		</c:if>
	
		<h2><span><a href="${cpath }/board">BOARD</a></span></h2>
		<h2><span><a href="${cpath }/review">REVIEW</a></span></h2>
		<h2><span><a href="${cpath }/gallery">GALLERY</a></span></h2>
	</div>
</div>
<hr>