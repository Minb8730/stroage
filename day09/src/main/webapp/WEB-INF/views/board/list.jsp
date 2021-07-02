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
				<a href="${cpath }/board/read/${dto.idx}?type=${param.type }&search=${param.search }&vc=true">
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
	
	
</main>
</body>
</html>