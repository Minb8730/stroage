<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<h2>My Page</h2>

<div>
	<p>
		<span class="input-name">학생 유형</span>
		<span>${login.stype == 'ib'? '취업반' : '단과반'}</span>
	</p>
	<p>
		<span class="input-name">ID</span>
		<span>${login.id}</span>
	</p>
	<p>
		<span class="input-name">이름</span>
		<span>${login.name}</span>
	</p>
	<p>
		<span class="input-name">휴대폰 번호</span>
		<span>${login.phone}</span>
	</p>
	<p>
		<span class="input-name">생년월일</span>
		<span>${login.birth}</span>
	</p>
	<p>
		<span class="input-name">최초 등록 날짜</span>
		<span>${login.rdate}</span>
	</p>
	
	<div>
		<a href="${cpath }/update/${login.id}"><button>정보 수정</button></a>
		<%--기존 비밀번호와 신규비밀번호를 입력받아서, 기존비밀번호가 일치하면 신규비밀번호를 해시처리해서 업데이트하기 --%>
		<a href="${cpath }/updatePassword/${login.id}"><button>비밀번호 수정</button></a>
		<a><button id="deleteBtn">계정 삭제</button></a>
	</div>
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