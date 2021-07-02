<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<h2>ID 찾기</h2>
<%-- <c:if test="${empty msg }"> --%>
<form method="post">
	<p><input type="text" name="name" placeholder="이름을 입력하세요"></p>
	<p><input type="text" name="phone" placeholder="전화번호를 입력하세요"></p>
	<p><input type="submit" value="찾기"></p>
</form>
<%-- </c:if> --%>

<c:if test="${not empty msg }">
	<fieldset>
		<h2>${msg }</h2>
		<a href="${cpath }/login"><button>로그인</button></a>
		<a href="${cpath }/renewPw"><button>비밀번호 재발급</button></a>
	</fieldset>
</c:if>


</body>
</html>