<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<main>
	<div class="sb">
		<div>No. ${dto.idx } | <b>${dto.title }</b> | ${dto.writer }</div>
		<div>${dto.wdate } | ${dto.ipaddr } | 조회수 : ${dto.viewCount }</div>
	</div>
	
	<div class="sb read" style="flex-flow: column;">
		<c:if test="${not empty dto.uploadFile }">
			<div><img src="${cpath }/upload/${dto.uploadFile }" height="300px"></div>
		</c:if>
		<pre>${dto.content }</pre>
	</div>
	
	<div class="sb"> 
		<div>
			<a href="${cpath }/board/?page=${param.page }&type=${param.type}&search=${param.search}"><button>목록</button></a>
		</div>
		<div>
			<a href="${cpath }/board/modify/${dto.idx}"><button>수정</button></a>
			<button id="deleteBtn">삭제</button>
		</div>
	</div>
	
	<div class="sb" style="justify-content: center; width: 1000px">
		<form method="POST" style="width: 800px;">
		<input type="hidden" name="page" value="${param.page }">
		<input type="hidden" name="bnum" value="${dto.idx }">
		<p>
			<input type="text" name="writer" placeholder="작성자 이름" required>
			<input type="password" name="password" placeholder="댓글 비밀번호" required>
		</p>
		<p>
			<textarea class="reply-area" name="content" placeholder="바르고 고운말을 사용합시다" required></textarea>
			<input type="submit" value="댓글 작성">
		</p>
		</form>
	</div>
	
	<c:forEach var="reply" items="${replyList }">
	<div class="reply">
		<div class="sb" style="width: 750px;">
			<div><b>${reply.writer }</b></div>
			<div>
				<a href="">수정</a>&nbsp;<b>|</b>
				<a class="deleteReplyBtn" data-idx="${reply.idx }" href="">삭제</a>
			</div>
		</div>
		<div><pre>${reply.content }</pre></div>
	</div>
	</c:forEach>
	
	<script>
		// 댓글 삭제
		const deleteReplyURL = '${cpath}/board/deleteReply/';
		
		const deleteReplyBtnList = document.querySelectorAll('.deleteReplyBtn');
		
		const deleteReplyHandler = function(event) {
			//기본 event 를 날려야 이 event 와 중복되어 오작동 하지 않는다
			event.preventDefault(); // prevent 로 기본 이벤트를 방지한다. 그렇지 않으면 서로 번갈아 가면서 작동한다.
			
			//클릭하면 idx를 불러와서 비밀번호를 물어보고 삭제 처리
			const idx = event.target.dataset.idx;
			const password = prompt('댓글을 삭제하려면 비밀번호를 입력하세요.');
			location.href = deleteReplyURL + idx + '?password=' + password + '&bnum=${dto.idx}';
// 			게시글은 하나밖에 없어서 바로 참조할 수 있지만 forEach로 받은 댓글은 바로 받지 못하기 때문에 data-idx 로 나누어 받아준다.
		};
		
		deleteReplyBtnList.forEach(function(btn) {
			btn.onclick = deleteReplyHandler;
		});
	
	
		// 게시글 삭제
		const deleteUrl = '${cpath }/board/delete/${dto.idx}';
		document.getElementById('deleteBtn').onclick = function(event) {
			const answer = prompt('${dto.idx}번 글을 삭제하려면 비밀번호를 입력하세요');
			if(answer) {
				location.href = deleteUrl + '?password=' + answer;
			}
		}
	</script>
	
</main>
</body>
</html>