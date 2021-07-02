<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<main>
	<h2>로그인</h2>
	<div style="border : 1px solid black; padding : 20px">
		<form method="post">
			<p><input type="text" name="id" placeholder="ID" required autofocus></p>
			<p><input type="password" name="pw" placeholder="Password" required></p>
			<p><input type="submit" value="로그인"></p>
		</form>
	<%--이름과 전화번호가 일치하면 ID 알려주기 --%>
	<a href="${cpath }/findID"><button>ID 찾기</button></a>
	
	<%--이름과 전화번호와 ID가 일치하면 새로 발급해주기 --%>
	<%-- 랜덤한 문자열을 만들어서, 새로 알려주고, 비밀번호 업데이트하기 --%>
	<%-- java.util.Random / java.util.UUID --%>
	<%=java.util.UUID.randomUUID().toString().split("-")[0] %>
	<a href="renewPw"><button>비밀번호 재발급</button></a>
	</div>
</main>
</body>
</html>