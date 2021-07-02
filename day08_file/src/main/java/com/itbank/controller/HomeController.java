package com.itbank.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartRequest;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.service.UploadService;

@Controller
public class HomeController{
	
	@Autowired private UploadService us;
	
	@GetMapping("/")
	public ModelAndView home() {
		ModelAndView mav = new ModelAndView("home");
		mav.addObject("list", us.getList());
		return mav;
	}
	
	@PostMapping("/")
//  public String home(HttpServletRequest request) { 	// 파라미터를 받기 위한 request
//	public String home(MultipartFile uploadFile) {  // file 외에 다른것을 받을 일이 없을 경우, 파일을 단일 객체로
//	public String home(MultipartRequest mpRequest) {	// file 외에 다른것도 받을 경우 ex)text 등,  파일을 담고 있는 MultipartRequest 
	public String home(MultipartHttpServletRequest mpRequest) { // 파라미터와 파일을 동시에
																// MultipartFile을 포함하는 커맨드 객체 사용 가능
		// Controller에서 request를 받아도, Service는 웹에 종속적이지 않은 코드를 작성하므로
		// request를 Service 에 넘기지 않도록 주의할 것
		
		MultipartFile uploadFile = mpRequest.getFile("uploadFile");
	
		// HttpServletRequest <=> MultipartRequest
		System.out.println(((HttpServletRequest)mpRequest).getParameter("name"));
		System.out.println((mpRequest).getParameter("name"));
		
		System.out.println(uploadFile.getContentType());
		System.out.println(uploadFile.getContentType().contains("image"));
		System.out.println(uploadFile.getName());
		System.out.println(uploadFile.getOriginalFilename());
		System.out.println(uploadFile.getSize());
		System.out.println();
		
		boolean flag = us.upload(uploadFile);
		
		
		return "redirect:/";
	}
	
	
	
	
	
	
}