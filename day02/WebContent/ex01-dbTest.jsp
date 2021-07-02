<%@page import="day02.TestDAO"%>
<%@page import="java.sql.ResultSetMetaData"%>
<%@page import="java.sql.DriverManager"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.Statement" %>
<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.ResultSet" %>
<%
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	String user = "c##itbank2";
	String password = "it";		
	String sql = "select * from v$version";
	String result = null;
	
	Class.forName(driver);
	Connection conn = DriverManager.getConnection(url, user, password);
	Statement stmt = conn.createStatement();  // Statcement vs PreparedStatement
	ResultSet rs = stmt.executeQuery(sql);
	ResultSetMetaData rsmd = rs.getMetaData(); // Developer 가 사용하는 값들 -> ResultSet 안에 결과를 표시하는 모든 것들이 포함되어 있다.
	
	while(rs.next()){
		result = rs.getString(1);
	}
	rs.close();		// 접속에 사용된 객체가
	stmt.close();	// 데이터 통신에 사용했던 스트림을
	conn.close();	// 개방의 역순으로 닫아준다.
	// 커넥션을 닫지 않는다면 접속할때 마다 객체는 생성되지만 소멸이 되지 않기 때문에 생성이 쌓이면 어느 순간부터 접속 불가능
%>
<h1>ex01 - dbTest</h1>
<hr>
<h2>result : <%=result %></h2>
<%=rsmd.getColumnCount() %>
<hr>
<%=TestDAO.getInstance().test() %>


</body>
</html>

