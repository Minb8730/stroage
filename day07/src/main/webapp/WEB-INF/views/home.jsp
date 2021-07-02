<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<%-- <h2>${header.referer }</h2> --%>
<%-- <h2>accept-Language : <%= request.getHeader("accept-language") %></h2> --%>
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
			<th>${dto.stype == 'it' ? '단과반' : '취업반'}</th>
			<th>${dto.id}</th>
			<th>${dto.pw}</th>
			<th>${dto.name}</th>
			<th>${dto.phone}</th>
			<th>${dto.birth}</th>
			<th>${dto.rdate}</th>
			<th>
				<fmt:formatNumber type="currency" value="${dto.due }" />
			</th>
			<th>
				<fmt:formatNumber type="currency" value="${dto.sfund}"/>	
			</th>
			<th>
				<fmt:formatNumber type="currency" value="${dto.payment}"/>	
			</th>
			<th>${dto.status}</th>
		</tr>
		
		

		</c:forEach>
	</table>

<script>
	const url='${cpath}/popup';
	const opt = 'width=350, height=250, member=no, status=no, toolbar=no, resizable=no';
	//window.open(url,'아이유 한번 보고 가세요',opt);
</script>
</body>
</html>


