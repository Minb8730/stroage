<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>인덱스</title>
</head>
<body>
<%
	String name = (String)session.getAttribute("logId");
	String id = (String)session.getAttribute("logName");
	if(name != null){
%>	
	<div>
		<a href="form.jsp">회원가입</a>
		<a href="logout.jsp">로그아웃</a>
		<a href="#">회원목록</a>
	</div>
	<h4>ID : <%=id %></h4>
	<h4>이름 : <%=name %></h4>
<% 	}else{
%>
	<div>
		<a href="form.jsp">회원가입</a>
		<a href="login.jsp">로그인</a>
		<a href="#">회원목록</a>
	</div>
<%} %>	
</body>
</html>