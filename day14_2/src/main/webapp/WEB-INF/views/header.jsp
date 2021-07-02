<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Series 2</title>
<style>
	div, span, body, ul, ol, li, h2, h3 {
		margin: 0;
		padding: 0;
	}
	body {
		width: 100%;
		overflow-x: hidden; 
	}
	header {
		position: relative;
		z-index: 5;
		background-color: skyblue;
		color: white;
		padding: 10px 50px;
	}
	a {
		text-decoration: none;
		color: inherit;
	}
	a:hover {
		text-decoration: underline;
	}
	nav {
		position: sticky;
		top: 0;
		width: 100%;
		display: flex;
		justify-content: center;
	}
	nav > ul {
		display: flex;
		list-style: none;
	}
	nav > ul > li {
		width: 120px;
		height: 50px;
		display: flex;
		justify-content: center;
		align-items: center;
		border: 2px solid white;
		margin-right: -2px;
	}
	nav > ul > li > a {
		display: block;
		width: 100%;
		height: 100%;
		text-align: center;
		line-height: 50px;
		font-size: 20px;
		font-weight: 900;
	}
	nav > ul > li > a:hover {
		text-decoration: none;
		background-color: white;
		color: skyblue;
	}
	.index-bg {
		position: relative;
		background-image: url('http://221.164.9.222/img/iu.jpg');
		background-size: 100%;
		background-repeat: no-repeat;
		background-position: center;
		width: 100%;
		height: 80vh;
		opacity: 0.8;
	}
	.loginInfo {
		display: flex;
		width: 100%;
		justify-content: flex-end;
		font-weight: bold;
		height: 30px;
	}
	.main {
		width: 100%;
		display: flex;
		flex-flow: column;
		align-items: center;
		padding-top: 50px;
	}
	input[type="text"],
	input[type="email"],
	input[type="password"] {
		all: unset;
		border: 0;
		border-bottom: 2px solid black;
		padding: 5px 10px;
	}
	.ce, .fs, .fe, .sb {
		margin: 20px 0;
		display: flex;
	}
	.ce { justify-content: center; 			}	/*   가운데  	 */
	.fs { justify-content: flex-start; 		}	/* 왼쪽		 */
	.fe { justify-content: flex-end; 		}	/* 		오른쪽  */
	.sb { justify-content: space-between; 	}	/* 양	      쪽  */
	
</style>
</head>
<body>

<header>
	<h1><a href="${cpath }">Series 2</a></h1>
	<div class="loginInfo">
		<c:if test="${not empty login }">
			<h3><a href="${cpath }/member/info">${login.username } (${login.userid })</a></h3>
		</c:if>
	</div>
	<nav>
		<ul>
			<li>
				<a href="${cpath }/member/${not empty login ? 'logout' : 'login'}">
					${not empty login ? '로그아웃' : '로그인' }
				</a>
			</li>
			<li><a href="${cpath }/board/">게시판</a></li>
		</ul>
	</nav>
</header>
