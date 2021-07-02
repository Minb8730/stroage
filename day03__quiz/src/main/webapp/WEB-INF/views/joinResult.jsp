<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>가입 신청 결과</h1>
<hr>
<b>jstl</b>
<h2>${newbie }</h2>
<hr>
<b>request</b>
<h2><%=request.getAttribute("newbie") %></h2>
<hr>
<b>out.print</b>
<h3><% out.print(request.getAttribute("newbie")); %></h3>
<hr>
<b>response</b>
<h4><% response.getWriter().append(request.getAttribute("newbie").toString()); %></h4>
<!-- 모두 같은 결과 -->
</body>
</html>