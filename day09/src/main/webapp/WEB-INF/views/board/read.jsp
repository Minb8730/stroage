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
			<a href="${cpath }/board/?type=${param.type}&search=${param.search}"><button>목록</button></a>
		</div>
		<div>
			<a href="${cpath }/board/modify/${dto.idx}"><button>수정</button></a>
			<button id="deleteBtn">삭제</button>
		</div>
	</div>
	
	<script>
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