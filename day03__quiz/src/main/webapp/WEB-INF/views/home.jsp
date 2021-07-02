<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value ="${pageContext.request.contextPath }"/>
<html>
<head>
<meta charset="UTF-8">
<title>간단 회원 가입 예제(파라미터 처리)</title>
<style>
	a {
		text-decoration : none;
		color : inherit;
		}
	a:hover {
		text-decoration : underline;
		}
	
</style>
</head>
<body>

<h1>간단 회원 가입 예제(파라미터 처리)</h1>
<hr>

<ul>
	<li><a href = "${cpath }/join">회원가입</a></li>
</ul>

</body>
</html>