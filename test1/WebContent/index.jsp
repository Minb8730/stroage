<%@page import="java.util.Date"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>로그인 샘플</title>
</head>
<body>

	<h1>내장 객체를 활용한 로그인</h1>
	<hr>
	<div style = "width : 100%; text-align: right">
		<h3>
			${not empty login ? login.id : ''}
			${not empty login ? '(' : '' }
			${not empty login ? login.name : ''}
			${not empty login ? ')' : ''}
		</h3>
	</div>
<%
	if(session.getAttribute("login") == null){%>
		<form method = "post" action = "login.jsp">
			<p><input type="text" name = "id" placeholder = "ID" autofocus></p>
			<p><input type="password" name = "pw" placeholder = "Password" required></p>
			<p><input type="submit" value = "로그인"></p>
		</form>
<% }else{%>
		<a href = "logout.jsp"><button>로그아웃</button></a>
<% }
%>
	
</body>
</html>