<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

    
<c:if test="${empty login }">
	<h1><a href="${cpath}/member/login ">홈페이지 들어가기</a></h1>
	<hr>
</c:if>

<c:if test="${not empty login }">
	<h1><a href="${cpath}/board/list?page=1&type=&search=">홈페이지 들어가기</a></h1>
</c:if>
</body>
</html>