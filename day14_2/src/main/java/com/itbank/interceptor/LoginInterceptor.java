package com.itbank.interceptor;

import java.util.Random;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

// 인터셉터 : 특정 주소에 대한 요청을 가로채서 사전 작업/ 사후 작업을 수행하는 객체(servlet-context.xml)
// 필터 : 모든 요청에 대해 공통 작업을 수행하는 객체(web.xml)
// web.xml 에 의해서 DispatcherServlet 으로 요청이 넘어가고, 
// preHandle : @Controller 이전에 Interceptor 작동
// postHandle : @Controller가 반환될때 Interceptor 작동
// AfterCompletion : DispatcherServlet에서 view로 반환될때 Interceptor 작동
// Interceptor는 상속받아서 사용한다.
// 필터는 web.xml 직후에 작동

public class LoginInterceptor extends HandlerInterceptorAdapter {
	
	
	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		String requestURL = request.getRequestURL().toString();
		System.out.println("preHandle : " + requestURL);
		
		HttpSession session = request.getSession();
		if(session.getAttribute("login") == null) {
			response.sendRedirect(request.getContextPath() + "/member/login");
			return false; // 컨트롤러의 메서드를 진행시키지 않는다.
		}
		return true;	// 예정대로 컨트롤러의 메서드를 진행시킨다.
	}
	
	
	@Override // controller의 메소드가 반환되었으나, viewResolver체게 전달하지 않은 상태 . 즉 함수는 실행 되었지만 화면은 안뜬 상태
	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler,
			ModelAndView modelAndView) throws Exception {
		
		String[] color = {"salmon", "burlywood", "lightgreen", "skyblue"};
		Random ran = new Random();
		int i = ran.nextInt(4);
		String bgcolor = color[i];
		modelAndView.addObject("bgcolor", bgcolor);
		
		
	}
	
	
	
	
	
	
	
	
}
