<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
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
	
</style>
</head>
<body>

<header>
	<h1>학생 관리 프로그램</h1>
	<div class="login-info">
		로그인 계정(로그인 이름)
	</div>
	<nav>
		<ul>
			<li><a href="${cpath }/join">학생등록</a></li>
			<li><a href="${cpath }/login">로그인</a></li>
		</ul>
	</nav>
</header>
<hr>
