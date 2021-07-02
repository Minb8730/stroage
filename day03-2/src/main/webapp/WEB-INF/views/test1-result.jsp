<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<%-- <h1>${name }님은 ${age }살이고, ${age >=20 ? '성인' : '미성년자' }입니다.</h1> --%>
<!-- 	requestScope.name == name   requestScope.age == age  -->
<h1>${mem.name }님은 ${mem.age }살이고, ${mem.age >=20 ? '성인' : '미성년자' }입니다.</h1>
<!-- Member로 받는다면 mem.name == requestScope.mem.name 	mem.age == requestScope.mem.age -->

<button onclick ="history.go(-1)">이전으로</button>

</body>
</html>