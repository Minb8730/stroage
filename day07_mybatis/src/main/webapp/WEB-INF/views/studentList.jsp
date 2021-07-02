<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>


<h2>student 테이블의 목록</h2>
<hr>
${list }

<ul>
<c:forEach var="dto" items="${list }">
	<li>${dto.id } | ${dto.name } | ${dto.stype } | ${dto.status }</li>
</c:forEach>
</ul>

</body>
</html>
