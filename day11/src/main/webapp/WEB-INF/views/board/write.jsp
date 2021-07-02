<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>
<main>
	<form method="POST" enctype="multipart/form-data">
	<input type="hidden" name="ipaddr" value="${pageContext.request.remoteAddr }">
	<div class="sb">
		<div>
			<p><input type="text" name="title" placeholder="제목을 입력하세요" required style="width: 300px" autofocus></p>
			<p><input type="text" name="writer" placeholder="이름을 입력하세요" required></p>
			<p><input type="password" name="password" placeholder="비밀번호를 입력하세요" required></p>
		</div>
		<div>
		</div>
	</div>
	
	<div class="sb read">
		<textarea class="write-area" name="content" required></textarea>
	</div>
	
	<div class="sb" style="border-bottom: 2px solid black; padding-bottom: 20px; margin-bottom: 20px;">
		<input type="file" name="file">
	</div>
	
	<div class="sb">
		<div>
			<a class="btn" onclick="history.go(-1)">뒤로가기</a>
		</div>
		<div>
			<button>작성완료</button>
		</div>
	</div>
	</form>
</main>
</body>
</html>