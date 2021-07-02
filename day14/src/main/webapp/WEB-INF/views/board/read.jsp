<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<div class="main">
<table>
	<tr>
		<th>글번호</th>
		<td>${dto.idx }</td>
	</tr>
	<tr>
		<th>제목</th>
		<td>${dto.title }</td>
	</tr>
	<tr>
		<th>작성자</th>
		<td>${dto.writer }</td>
	</tr>
	<tr>
		<th>조회수</th>
		<td>${dto.viewCount }</td>
	</tr>
	<tr>
		<th>작성날짜</th>
		<td>${dto.wdate }</td>
	</tr>
	<tr>
		<th>내용</th>
		<td>${dto.content }</td>
	</tr>
	<tr>
		<th>첨부이미지</th>
		<td><img src="${cpath }/upload/${dto.uploadFile}" width="200px"></td>
	</tr>
</table>
</div>
</body>
</html>