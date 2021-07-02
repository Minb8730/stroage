<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %> 
<c:set var="cpth" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link type="text/css" rel="stylesheet" href="resources/css/stype.css">
</head>
<body>

<h1>Hello, world !!</h1>
<h2>${cpth }/resources/css/style.css</h2>
<h2><c:url value="/resources/css/style.css"/></h2>

</body>
</html>