<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<main>
	<h2>대문 페이지 입니다.</h2>
</main>

	<table>
		<tr>
			<th>IDX</th>
			<th>STYPE</th>
			<th>ID</th>
			<th>PW</th>
			<th>NAME</th>
			<th>PHONE</th>
			<th>BIRTH</th>
			<th>RDATE</th>
			<th>DUE</th>
			<th>SFUND</th>
			<th>PAYMENT</th>
			<th>STATUS</th>
		</tr>
		<c:forEach var="dto" items="${list }">
		<tr>
			<th>${dto.idx}</th>
			<th>${dto.stype}</th>
			<th>${dto.id}</th>
			<th>${dto.pw}</th>
			<th>${dto.name}</th>
			<th>${dto.phone}</th>
			<th>${dto.birth}</th>
			<th>${dto.rdate}</th>
			<th>${dto.due}</th>
			<th>${dto.sfund}</th>
			<th>${dto.payment}</th>
			<th>${dto.status}</th>
		</tr>
		
		

		</c:forEach>
	</table>


</body>
</html>


