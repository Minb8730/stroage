<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }"></c:set>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<c:forEach var="str" items="${list }">
	<h2>${str }</h2>
</c:forEach>

<a href="${cpath }/studentList"><button>student 전체 목록 불러오기</button></a>
<a href="${cpath }/studentList2"><button>student 전체 목록 불러오기(매퍼 자동 주입)</button></a>


</body>
</html>