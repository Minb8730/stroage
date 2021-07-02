<%@page import="java.util.Arrays"%>
<%@page import="java.util.ArrayList"%>
<%@page import="test1.Account"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%! 
	List<Account> accountList = new ArrayList<Account>(Arrays.asList(new Account[]{
			new Account("test", "1234", "테스트"),
			new Account("itbank", "it", "아이티뱅크"),
			new Account("admin", "1", "관리자"),
	}));
	// 1) 매개변수 생성자를 통해서 각각의 계정 객체를 생성한다
	// 2) 똑같은 자료형의 객체가 여러개이므로, 배열로 묶는다.
	// 3) 배열은 데이터 추가 및 삭제가 번거로우니까 List형태로 변경한다.
	// 4) List 타입에서는 add가 있지만 정상적으로 작동하지 않는다 (미구현)
	// 5) ArrayList 타입에서는 add가 정상적으로 작동한다.
	// 6) 목록을 받은 페이지 혹은 코드에서, 추가를 허용하려면 ArrayList형태로 반환 / 추가를 막으려면 List 형태로 반환
%>
<%
	request.setCharacterEncoding("utf-8");	// web.xml 인코딩 필터적용하면 굳이 적용하지 않아도 된다. -> AJAX이면 지정해야한다.
	if(application.getAttribute("accountList") == null){ 	// Object이지만 null은 자료형에 상관없다.
		application.setAttribute("accountList", accountList);
		System.out.println("계정 목록 추가!!"); // 이 코드는 딱 한번만 작동된다.
	}
%>
<jsp:useBean id = "inputData" class= "test1.Account"/>
<jsp:setProperty property="*" name="inputData"/>
<%-- \
	test1.Account inputData = new test.Account();
	
	inputData.setId(request.getParameter("id"));
	inputData.setPw(request.getParameter("pw"));
	
	pageContext.setAttribute("inputData", inputData); 와 같다
 --%>
<%
	List<Account> list = (List<Account>)application.getAttribute("accountList"); // 위의 코드가 한번만 작동하기 때문에 다시 가져온다.
	for(Account acc : list){
		if(acc.equals(inputData)){ // id와 pw만 비교하기 위해 오버라이딩한 메소드를 사용
			session.setAttribute("login", acc);
			session.setMaxInactiveInterval(600);
		}
	}
	response.sendRedirect(request.getContextPath());  // 프로젝트 최상위 문서 경로 -> index.jsp
	// post를 처리하고 나면 반드시 redirect를 이용하여 페이지를 이동시키자. 이 과정을 거치지 않으면 DB에 데이터가 계속 쌓이고 팝업이 뜬다.
%>
 
 
</body>
</html>