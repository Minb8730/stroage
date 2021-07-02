<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>
<main>
	<div id="boardList">
		<div class="board-top">
			<span class="board-idx">글번호</span>
			<span class="board-title">제목</span>
			<span class="board-writer">작성자</span>
			<span class="board-viewCount">조회수</span>
			<span class="board-wdate">작성일자</span>
			<span class="board-ipaddr">IP</span>
		</div>
		<c:forEach var="dto" items="${list }">
		<div class="board-content">
			<span class="board-idx">${dto.idx }</span>
			<span class="board-title">
				<a href="${cpath }/board/read/${dto.idx}?page=${param.page }&type=${param.type }&search=${param.search }&vc=true">
					${fn:length(dto.title) gt 20 ? fn:substring(dto.title, 0, 20) : dto.title }
					${fn:length(dto.title) gt 20 ? '...' : ''}
				</a>
			</span>
			<span class="board-writer">${dto.writer }</span>
			<span class="board-viewCount">${dto.viewCount }</span>
			<span class="board-wdate">${dto.wdate }</span>
			<span class="board-ipaddr">${dto.ipaddr }</span>
		</div>
		</c:forEach>
	</div>
	<div class="sb">
		<div>
			<form>
				<input type="hidden" name="page" value="1">
				<select name="type">
					<option ${param.type == 'title' ? 'selected' : '' } value="title">제목으로 검색</option>
					<option ${param.type == 'writer' ? 'selected' : '' } value="writer">작성자로 검색</option>
					<option ${param.type == 'content' ? 'selected' : '' } value="content">내용으로 검색</option>
				</select>
				<input type="text" name="search" value="${param.search }" placeholder="검색어를 입력하세요">
				<input type="submit" value="검색">
			</form>
		</div>
		<div>
			<a href="${cpath }/board/write"><button>새 글 작성</button></a>
		</div>
	</div>
	
	<div>
		<c:if test="${paging.prev }">
			<a href="${cpath }/board/?page=${paging.begin - 1}&type=${param.type}&search=${param.search}">[이전]</a>
		</c:if>
		
		<c:forEach var="i" begin="${paging.begin }" end="${paging.end }">
			<a href="${cpath }/board/?page=${i}&type=${param.type}&search=${param.search}">
			${param.page == i ? '<b>' : '' }
			[${i }]
			${param.page == i ? '</b>' : '' }
			</a>
		</c:forEach>
		
		<c:if test="${paging.next }">
			<a href="${cpath }/board/?page=${paging.end + 1}&type=${param.type}&search=${param.search}">[다음]</a>
		</c:if>
	</div>
	
	
</main>
</body>
</html>


