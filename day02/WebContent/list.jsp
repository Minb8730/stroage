<%@page import="java.util.List"%>
<%@page import="day02.BoardDTO"%>
<%@page import="day02.TestDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>   
<c:set var ="dao" value ="<%=TestDAO.getInstance() %>"></c:set>
<jsp:useBean id="dao" class = "day02.TestDAO"/>
<!DOCTYPE html> 
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	List<BoardDTO> list = dao.selectList();
%>
<c:set var ="list" value ="${dao.selectList() }"></c:set>

	<table align = "center" border = "1" width = 800>
		<thead>
			<tr>
				<td>글번호</td>
				<td>제목</td>
				<td>작성자</td>
				<td>내용</td>
				<td>작성날짜</td>
				<td>조회수</td>
				<td>작성자IP</td>
			</tr>
		</thead>
	<%for(BoardDTO dto : list ){%>
			<tr>
				<td><%=dto.getIdx()%></td>
				<td><%=dto.getTitle()%></td>
				<td><%=dto.getWriter()%></td>
				<td><%=dto.getContent()%></td>
				<td><%=dto.getWdate()%></td>
				<td><%=dto.getVcnt()%></td>
				<td><%=dto.getIpaddr()%></td>
			</tr>
	
	
<% }
%>
		
		
	</table>
</body>
</html>