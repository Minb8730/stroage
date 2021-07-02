<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>day09 - 비회원 기본 게시판</title>
<!-- 작성중인 css는 style 태그 내에 작성하고, 완성된 시점에서 별도의 .css 파일로 분리하자. -->
<link rel="stylesheet" href="${cpath }/resources/css/style.css">
<style>
	html, body, div, span, ul, ol, li, a, table, td, th, form{
		margin: 20px;
		padding: 30px;
 		box-sizing: border-box;  /* 테두리를 포함한 너비나 높이를 만들어준다. */
	}
	a{
		text-decoration: none;
		color: inherit;
	}
	
</style>
</head>
<body>

<header>
	<a href="${cpath }/"><h1>게시판</h1></a>
	<div><a href="${cpath }/list">[목록]</a> 
	<a href="${cpath }/write">[글 쓰기]</a>
	<a href="${cpath }/find">[검색]</a>
	
<!-- 	[목록] - [글 읽기] - [작성] - [삭제] - [수정] - [조회수 증가] - [검색] -->
	</div>
</header>
<hr>
<!-- <div style="box-sizing: content-box; width: 200px; height: 100px; border: 3px solid red;"></div> -->
<!-- <div style="box-sizing: border-box; width: 200px; height: 100px; border: 3px solid blue;"></div> -->
<!-- <div style="border: 5px solid green; width: 200px; height: 100px;"></div> -->

