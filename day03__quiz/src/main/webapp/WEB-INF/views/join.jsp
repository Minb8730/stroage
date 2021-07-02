<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<form method = "POST">
		<div>아이디<br><input type="text" name = "id" placeholder="ID"></div>
		<div>비밀번호<br><input type="password" name ="pw" placeholder="Password"></div>
		<div>비밀번호 재확인<br><input type="password" name ="pw2" placeholder="Confirm Password"></div>
		<div>이름<br><input type="text" name="name" placeholder ="Name"></div>
		
		<div>
			생년월일<br>
			연<input type="number" name="year" min="1900" max="2021" placeholder="연도(4자리)">
			월
			<select name ="month">
				<c:forEach var="i" begin="1" end="12">
					<option value = "${i }">${i }월</option>
				</c:forEach>
			</select>
			<input type="number" name="date" min="1" max="31" placeholder="일">
		</div>
		
		<div>
			성별<br>
			<select name="gender">
				<option>남자</option>	
				<option>여자</option>	
				<option>선택 안함</option>	
			</select>
		</div>
		
		<div>이메일<br><input name="email" placeholder="foo@bar.com"></div>
		<div>전화번호<br><input name="phone" placeholder="010-0000-0000"></div>
		<div>
			<p><input type="submit" value ="가입신청"></p>
		</div>
		
	</form>

</body>
</html>