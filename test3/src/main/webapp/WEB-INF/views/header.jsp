<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>

<c:set var="cpath" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
	h, html, body, div, span, ul, ol, li, a, table, td, th, form {
		margin: 0;
		padding: 0;
 		box-sizing: border-box;	 /*	 테두리를 포함한 너비나 높이를 만들어준다 */
	}
	a {
		text-decoration: none;
		color: inherit;
	}
	.input-name{
		display : inline-block;
		width: 150px;
	}
	main, main > form {
		width: 80%;
		display: flex;
		flex-flow: column;
		justify-content: center;
		align-items: center;
		margin: 20px auto;
	}
	main > form  {
		width: 100%;
	}
	#boardList {
		width: 100%;
		max-width: 1000px;
		border: 2px solid #dadada;
	}
	#boardList > .board-top {
		user-select: none;
		border-bottom: 2px solid black;
		background-color: #5a5a5a;
		color: white;
		font-weight: 900;
		cursor: pointer;
	}
	#boardList > .board-content {
		border-bottom: 2px solid black;
		cursor: pointer;
	}
	#boardList > .board-content:hover {
		background-color: #dadada;
		font-weight: bold;
	}
	#boardList > div > span {
		font-size: 16px;
		display: inline-block;
		padding: 5px;
		text-align: center;
	}
	.board-idx, 
	.board-writer, 
	.board-viewCount, 
	.board-wdate,
	.board-ipaddr {
		width: 8%;
	}
	.board-wdate {
		width: 15%;
	}
	.board-title {
		text-align: left !important;
		width: 40%;
	}
	.board-title > a {
		display: block;
	}
	.sb {
		width: 100%;
		max-width: 1000px;
		padding: 10px 0px;
		display: flex;
		justify-content: space-between;
	}
	main .read {
		border: 2px solid #dadada;
		max-width: 1000px;
		width: 100%;
		margin: auto;
		padding: 20px;
	}
	.sb pre,
	.write-area {
		border: 0;
		width: 100%;
		min-height: 200px;
		text-align: left;
		font-size: 16px;
		resize: none;
	}
	.reply-area {
		border: 2px solid black;
		width: 100%;
		min-height: 50px;
		text-align: left;
		font-size: 14px;
		resize: none;
	}
	input[type="text"],
	input[type="password"] {
		all: unset;
		border: 0;
		border-bottom: 2px solid black;
		padding: 5px;
		width: 220px;
	}
	input[type="button"],
	input[type="submit"],
	button,
	.btn {
/* 		all: unset; */
		border: 0;
		display: inline-block;
		font-size: 16px;
		font-weight: 900;
		width: 110px;
		height: 35px;
		line-height: 35px;
		text-align: center;
		background-color: #5a5a5a;
		color: white;
		padding: 0px 15px;
		border-radius: 5px;
		cursor: pointer;
	}
	input[type="button"]:hover,
	input[type="submit"]:hover,
	button:hover,
	.btn:hover {
		background-color: black;
	}
	.reply {
		background-color: #dadada;
		border-radius: 10px;
		width: 800px;
		min-height: 50px;
		text-align: left;
		font-size: 14px;
		margin: 10px auto;
		padding: 5px 20px;
	}
	
</style>
<title>홈페이지</title>
</head>
<body>
<header style="background-color : ${bgcolor };">
	<h1><a href="${cpath }">홈으로</a></h1>
	<hr>
	<div id="log_check">
		<c:if test="${not empty login }">
			<p>환영합니다. ${login.userName }님
			<a href="${cpath }/member/logout"><input type="button" value="로그아웃"></a>
			<a href = "${cpath }/member/mypage"><input type="button" value="myPage"></a>
			</p> 
		</c:if>
	</div>

</header>




