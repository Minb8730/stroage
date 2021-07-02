<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>


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

</table>



<!-- 	<div class="sb"> -->
<%-- 		<div>No. ${dto.idx } | <b>${dto.title }</b> | ${dto.writer }</div> --%>
<%-- 		<div>${dto.wdate } | ${dto.ipaddr } | 조회수 : ${dto.viewCount }</div> --%>
<!-- 	</div> -->
	
<!-- 	<div class="sb read" style="flex-flow: column;"> -->
<%-- 		<c:if test="${not empty dto.uploadFile }"> --%>
<%-- 			<div><img src="${cpath }/upload/${dto.uploadFile }" height="300px"></div> --%>
<%-- 		</c:if> --%>
<%-- 		<pre>${dto.content }</pre> --%>
<!-- 	</div> -->
	
<!-- 	<div class="sb">  -->
<!-- 		<div> -->
<%-- 			<a href="${cpath }/board/?page=${param.page }&type=${param.type}&search=${param.search}"><button>목록</button></a> --%>
<!-- 		</div> -->
<!-- 		<div> -->
<%-- 			<a href="${cpath }/board/modify/${dto.idx}"><button>수정</button></a> --%>
<!-- 			<button id="deleteBtn">삭제</button> -->
<!-- 		</div> -->
<!-- 	</div> -->
	
</body>
</html>