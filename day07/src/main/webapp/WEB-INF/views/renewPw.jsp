<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<h2>비밀번호 재발급</h2>
<form method="post">
	<p><input type="text" name="id" placeholder="ID를 입력하세요."></p>
	<p><input type="text" name="name" placeholder="이름을 입력하세요."></p>
	<p><input type="text" name="phone" placeholder="핸드폰 번호를 입력하세요."></p>
	<p><input type="submit" value="재발급 요청"></p>
</form>

<c:if test="${pageContext.request.method=='POST' }">
<fieldset>
	<c:if test="${not empty newPw }"><h2>새로 발급된 임시 비밀번호는 [${newPw}]입니다.</h2></c:if>
	<c:if test="${empty newPw }"><h2>정보가 일치하지 않습니다.</h2></c:if>
	<a href="${cpath }/login"><button>로그인</button></a>
</fieldset>
</c:if>
</body>
</html>