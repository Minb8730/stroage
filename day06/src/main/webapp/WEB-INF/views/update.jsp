<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<h2>내 정보 수정하기</h2>

<div>
	<form method="post">
	<input type="hidden" name="id" value="${dto.id }">
			<p>
				<span class="input-name">학생 유형</span>
				<span>${dto.stype == 'ib'? '취업반' : '단과반'}</span>
			</p>
			<p>
				<span class="input-name">ID</span>
				<span>${dto.id}</span>
			</p>
			<p>
				<span class="input-name">이름</span>
				<span><input type="text" name="name" value="${dto.name}"></span>
			</p>
			<p>
				<span class="input-name">휴대폰 번호</span>
				<span><span><input type="text" name="phone" value="${dto.phone}"></span>
			</p>
			<p>
				<span class="input-name">생년월일</span>
				<span><span><input type="text" name="birth" value="${dto.birth}"></span>
			</p>
			<p>
				<span class="input-name">최초 등록 날짜</span>
				<span>${dto.rdate}</span>
			</p>
		<div>
			<input type="submit" value="정보수정">
		</div>
	</form>	
</div>

<script>
	document.getElementById('deleteBtn').onclick = function(){
		const flag = confirm("정말 계정을 삭제하시겠습니까?");
		if(flag){
			location.replace("${cpath}/delete/${login.id}");
		}
	}

</script>



</body>
</html>