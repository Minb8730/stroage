<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ex02 - EL,JSTL</title>
</head>
<body>
<%-- 변수 선언, 내장객체에 attribute를 선언 --%>
<%-- pageContext.setAttribute("test1", "이지은"); --%>
<c:set var ="test1" value = "이지은" scope = "page"/>
<%-- session.setAttribute("test2","홍진호"); --%>
<c:set var = "test2">홍진호</c:set>

<p>${test1 }</p>
<%-- pageContext.getAttribute("test1").toString() --%>
<%-- EL Tag는 scope를 명시하지 않으면, pageContext -> request ->session -> application --%>
${test2.toString() }

<c:set var ="flag" value="${test2 }" />
<c:if test = "${flag == '이지은' }">
	<h3>이지은님 안녕하세요</h3>
</c:if>

<c:if test = "${flag == '홍진호' }">
	<h3>콩은 까야 제맛</h3>
</c:if>


</body>
</html>




