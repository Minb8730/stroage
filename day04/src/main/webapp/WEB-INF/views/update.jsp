<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<h1>상품 정보 수정</h1>
<!-- index는 pathVariable 로 전달되기 때문에 굳이 index를 지정하지 않는다 -->
<form method="post">
	<p><input type="text" name="name" value="${dto.name }"></p>
	<p><input type="number" name="price" value="${dto.price }"></p>
	<p><input type="number" name="cnt" value="${dto.cnt }"></p>
	<p><input type="submit" value="수정"></p>	
	
</form>

</body>
</html>