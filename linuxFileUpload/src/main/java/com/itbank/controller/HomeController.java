package com.itbank.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.service.UploadService;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.SftpException;

@Controller
public class HomeController {

	@Autowired private UploadService uploadService;
	
	@GetMapping("/")
	public String home() {
		return "home";
	}
	
	@PostMapping("/")
	public ModelAndView upload(MultipartFile file) throws IllegalStateException, JSchException, IOException, SftpException {
		ModelAndView mav = new ModelAndView("home");
		String uploadFileName = uploadService.upload(file);
		mav.addObject("uploadFileName", uploadFileName);
		return mav;
	}
}
