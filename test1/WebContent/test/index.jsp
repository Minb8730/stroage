<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>�ε���</title>
</head>
<body>
<%
	String name = (String)session.getAttribute("logId");
	String id = (String)session.getAttribute("logName");
	if(name != null){
%>	
	<div>
		<a href="form.jsp">ȸ������</a>
		<a href="logout.jsp">�α׾ƿ�</a>
		<a href="#">ȸ�����</a>
	</div>
	<h4>ID : <%=id %></h4>
	<h4>�̸� : <%=name %></h4>
<% 	}else{
%>
	<div>
		<a href="form.jsp">ȸ������</a>
		<a href="login.jsp">�α���</a>
		<a href="#">ȸ�����</a>
	</div>
<%} %>	
</body>
</html>