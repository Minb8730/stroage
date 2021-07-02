<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
	
	
<table>
	<tr>
		<th>IDX</th>
		<th>TITLE</th>
		<th>WRITER</th>
		<th>WDATE</th>
		<th>IPADDR</th>
		<th>VIEWCOUNT</th>
		<th>DELETED</th>
	</tr>
	<c:forEach var="dto" items="${list }">
	<tr>
		<th>${dto.idx}</th>
		<th><a href="${cpath }/read/${dto.idx}">${dto.title}</a></th>
		<th>${dto.writer}</th>
		<th>${dto.wdate}</th>
		<th>${dto.ipaddr}</th>
		<th>${dto.viewCount}</th>
		<th>
			<a><button class="deleteBtn" data-idx="${dto.idx }">삭제하기</button></a>
		</th>
	</tr>
	</c:forEach>
</table>

<script>
	document.querySelectorAll('.deleteBtn').forEach(function(btn) {
		btn.onclick = function(event){
			const flag = confirm("게시물을 삭제하시겠습니까?");
			if(flag){
				location.replace("${cpath}/delete/" + event.target.dataset.idx);
			}
		}
	});

</script>

</body>
</html>