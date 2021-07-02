<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../header.jsp" %>


<h2>나의 정보</h2>

<div>
	<p>
		<span class="input-name">회원 이름</span>
		<span>${login.userName}</span>
	</p>
	<p>
		<span class="input-name">ID</span>
		<span>${login.userId}</span>
	</p>
	<p>
		<span class="input-name">생년월일</span>
		<span>${login.birth}</span>
	</p>
	<p>
		<span class="input-name">email</span>
		<span>${login.email}</span>
	</p>
	<p>
		<span class="input-name">성별</span>
		<span>${login.gender}</span>
	</p>
	<p>
		<span class="input-name">주소</span>
		<span>${login.address}</span>
	</p>

	
	 <div>
		<a href="${cpath }/member/update/${login.userId}"><button>정보 수정</button></a>
		<a href="${cpath }/member/updatePassword/${login.userId}"><button>비밀번호 수정</button></a>
		<a><button id="deleteBtn">계정 삭제</button></a>
	</div> 
</div>


<script>
	document.getElementById('deleteBtn').onclick = function(){
		const flag = confirm("정말 계정을 삭제하시겠습니까?");
		if(flag){
			location.replace("${cpath}/member/delete/${login.userId}");
		}
	}

</script>








</body>
</html>