<%@page import="test.Member"%>
<%@page import="java.util.ArrayList"%>
<%@page import="test.MemberStroage"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>

	<%
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		String name = request.getParameter("name");
	
    	MemberStroage ms = new MemberStroage();
    	ArrayList<Member> memberList = ms.selectAll();
    	
    	for(Member m : memberList){
    		if(m != null){
	    		if(m.getId().equals(id) && m.getPw().equals(pw)){
					session.setAttribute("logId", id);
					session.setAttribute("logName", name);
					response.sendRedirect("index.jsp");
    		}else{
%>
				<script>
    			alert("���̵�� ��й�ȣ�� Ȯ���� �ּ���")
    			history.back();
    			</script>  
<%    		}
    	}
    }    			
    %>
</body>
</html>