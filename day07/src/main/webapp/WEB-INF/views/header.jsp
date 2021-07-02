<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<c:set var="cpath" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>학생 관리 프로그램</title>
<style>
	a{
		text-decoration: none;
		color : inherit;
	}
	a:hover{
		text-decoration: underline;
	}
	.login-info {
		height: 50px;
		text-align : right;
	}
	table{
		width : 100%;
		word-break : none;
		table-layout: fixed;
		border-collapse: collapse;
	}
	td,th{
		border : 1px solid black;
		padding : 5px 10px;
	}
	.input-name{
		display : inline-block;
		width: 150px;
	}
	th:nth-child(4) {
		width : 100px;
		overflow : hidden;
	}
	header{
		position: sticky; /* static, absolute, relative, fixed, sticky*/
		top: 20px;
		background-color : white;
		border-bottom: 3px solid black;
	}
	nav > ul{
		list-style: none;
		padding : 0;
		display: flex;
	}
	nav > ul > li{
		width: 120px;
		font-size: 20px;
		margin: 0;
		margin-right: -3px;
		border : 3px solid #dadada;
		text-align: center;
	}
</style>
</head>
<body>

<header>
	<a href="${cpath }"><h1>학생 관리 프로그램</h1></a>
	<div class="login-info">
		<c:if test="${not empty login }">
			${login.name } (${login.id })
		</c:if>
	</div>
	<nav>
		<ul>
			<%-- 로그인 안되어 있으면 노출되는 메뉴 --%>
			<c:if test="${empty login }">
				<li><a href="${cpath }/join">회원가입</a></li>
				<li><a href="${cpath }/login">로그인</a></li>
			</c:if>
			
			<%-- 로그인 되어 있으면 노출되는 메뉴 --%>
			<c:if test="${not empty login }">
				<li><a href="${cpath }/mypage">마이페이지</a></li>
				<li><a href="${cpath }/logout">로그아웃</a></li>
				<li><a href="${cpath }/payment">결제</a></li>
			</c:if>
			
		</ul>
	</nav>
</header>
