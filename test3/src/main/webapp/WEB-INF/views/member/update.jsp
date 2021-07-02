<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>

<h2>나의 정보 수정</h2>
<div>
	<form method="post">
		<p>
			<span class="input-name">ID</span>
			<span>${login.userId}</span>
		</p>
		<p>
			<span class="input-name">회원 이름</span>
			<span><input type="text" name="userName" value="${login.userName}"></span>
		</p>
		<p>
			<span class="input-name">생년월일</span>
			<span><input type="text" name="birth" value="${dto.birth}" maxlength="6"></span>
		</p>
		<p>
			<span class="input-name">email</span>
			<span><input type="text" name="email" value="${dto.email}"></span>
		</p>
		<p>
			<span class="input-name">성별</span>
			<span>
				<input type="radio" name="gender" value="m" ${dto.gender == 'm' ? 'required' : ''}>남성
				<input type="radio" name="gender" value="f" ${dto.gender == 'f' ? 'required' : ''}>여성
			</span>
		</p>
		<p>
			<span class="input-name">주소</span>
			<span><input type="text" name="address" value="${dto.address}"></span>
		</p>
		<div>
			<p>
				<input type="submit" value="정보 수정">
				<a><button id="deleteBtn">계정 삭제</button></a>
			</p>
		</div>
		
	<%-- 		<a href="${cpath }/updatePassword/${dto.userId}"><button>비밀번호 수정</button></a> --%>
	</form>


</div>

<script>
 	document.getElementById('deleteBtn').onclick = function(){ 
 		const flag = confirm("정말 계정을 삭제하시겠습니까?"); -->
 		if(flag){ 
			location.replace("${cpath }/member/delete/${dto.userId}");
 		} 
 	} 

</script>


</body>
</html>