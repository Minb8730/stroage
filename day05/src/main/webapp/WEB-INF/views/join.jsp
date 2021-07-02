<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ include file="header.jsp"%>

<main>
<h2>회원 가입</h2>
<div style="border: 1px solid black; padding: 10ps;">

	<form method="post">
		<p>
			<span class="input-name">유형(STYPE)</span> 
			<label><input type="radio" name="stype" value="it" required>단과반</label>
			<label><input type="radio" name="stype" value="ib" required>취업반</label>
		</p>
		<p>
			<span class="input-name">ID</span>
			<input type="text" name="id" placeholder="ID" required>
		</p>
		<p>
			<span class="input-name">Password</span>
			<input type="password" name="pw" placeholder="Password" required>
		</p>
		<p>
			<span class="input-name">학생 이름</span>
			<input type="text" name="name" placeholder="이름을 입력하세요" required>
		</p>
		<p>
			<span class="input-name">휴대폰 번호</span>
			<input type="text" name="phone" placeholder="010-0000-0000" required>
		</p>
		<p>
			<span class="input-name">생년월일 (6자리)</span>
			<input type="date" name="birth" value="2000-01-01" required>
		</p>
		<p>
			<input type="submit" value="가입신청">
		</p>
	</form>

</div>

</main>
</body>
</html>