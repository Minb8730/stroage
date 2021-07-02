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
	</div>

</main>
</body>
</html>