<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>
<div class="main">
<table>
<tr>
	<th>글번호</th>
	<th>제목</th>
	<th>작성자</th>
	<th>조회수</th>
	<th>작성날짜</th>
</tr>

<c:forEach var="dto" items="${list }">
<tr>
	<td>${dto.idx }</td>
	<td><a href="${cpath }/board/read/${dto.idx}">${dto.title }</a></td>
	<td>${dto.writer }</td>
	<td>${dto.viewCount }</td>
	<td>${dto.wdate }</td>
</tr>
</c:forEach>

</table>

<a href="${cpath }/board/write">새 글 작성</a>
<a href=""></a>
</div>

</body>
</html>