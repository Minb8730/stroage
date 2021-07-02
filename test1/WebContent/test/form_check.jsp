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
					alert("이미 존재하는 아이디 입니다.");
					history.back();
				</script>    			
<%   		}else{
				m.setId(id);
				m.setPw(pw);
				m.setName(name);
				if(ms.addMember(m)){
%>	
				<script>
					alert("회원가입에 성공");
					location.href="login.jsp";			
				</script>
<%				}else{%>
				<script>
					alert("회원가입에 실패");
					history.back();			
				</script>		
<%}
			}
    	}
    			
    %>