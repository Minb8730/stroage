<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	tabel{
		border-collapse: collapse;
		border: 1px solid black;
	}
	td, th {
		border : 1px solid black;
		padding : 5px 10px;
	}
</style>
</head>
<body>
<h1>Snackbar 상품 목록</h1>
<hr>
<form method="post">
	<p><input type="text" name="name" placeholder="상품명" required autocomplete="off"></p>
	<p><input type="number" name="price" placeholder="단품가격" required></p>
	<p><input type="submit" value="등록"></p>
<!-- 	action 의 대상이 없으면 현재 페이지에서 처리한다. -->
</form>

<table>
	<tr>
		<th>상품코드</th>
		<th>상품명</th>
		<th>가격</th>
		<th>수량</th>
		<th>수정</th>
		<th>삭제</th>
	</tr>
	<c:set var="cpath" value="${pageContext.request.contextPath }"/>
	<c:forEach var="dto" items="${list }">
	<tr>
		<td>${dto.idx }</td>
		<td>${dto.name }</td>
		<td>${dto.price }</td>
		<td>${dto.cnt }</td>
		<td><a href="${cpath }/snackbar/update/${dto.idx}"><button>수정</button></a>
		<td><button class="deleteBtn" 
					data-idx="${dto.idx }"
					data-name="${dto.name }">삭제</button></td> 
	</tr>
	</c:forEach>
	
</table>
<script type="text/javascript">
	//document.querySelectorAll('.deleteBtn').forEach(btn => console.log(btn.dataset.name));
	document.querySelectorAll('.deleteBtn').forEach(btn => {
		btn.onclick = (event) => { // (event) => 로 function(event) 써도 괜찮다.
			const idx = event.target.dataset.idx;
			const name = event.target.dataset.name;
			const flag= confirm('[' + idx + '-' + name + '] : 정말 삭제하시겠습니까?' );
			if(flag){
				location.href = '${cpath}/snackbar/delete/' + idx;	// 주소가 바뀌면 새로운 request
			}
		}
	});
	
</script>

</body>
</html>