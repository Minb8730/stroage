<%@page import="test.MemberStroage"%>
<%@page import="test.Member"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>

    <%
    	String name = request.getParameter("name");
    	String id = request.getParameter("id");
    	String pw = request.getParameter("pw");
    	
    	MemberStroage ms = new MemberStroage();
    	ArrayList<Member> memberList = ms.selectAll();
    	for(Member m : memberList){
    		if(m.getId().equals(id)){
%>
				<script>
					alert("�̹� �����ϴ� ���̵� �Դϴ�.");
					history.back();
				</script>    			
<%   		}else{
				m.setId(id);
				m.setPw(pw);
				m.setName(name);
				if(ms.addMember(m)){
%>	
				<script>
					alert("ȸ�����Կ� ����");
					location.href="login.jsp";			
				</script>
<%				}else{%>
				<script>
					alert("ȸ�����Կ� ����");
					history.back();			
				</script>		
<%}
			}
    	}
    			
    %>