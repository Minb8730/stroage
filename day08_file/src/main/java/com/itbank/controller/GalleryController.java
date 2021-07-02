package com.itbank.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.GalleryDTO;
import com.itbank.service.UploadService;

@Controller
@RequestMapping("/gallery")
public class GalleryController {

	@Autowired private UploadService us;
	
	@GetMapping({"/", ""})
	public ModelAndView index(ModelAndView mav) {
		mav.addObject("list", us.getGalleryList());
		// controller -> service -> dao -> mapper -> DB
		mav.setViewName("index");
		return mav;
	}
	
	@PostMapping({"/",""})
	public String upload(GalleryDTO dto) {
		int row= us.insert(dto);
		return  "redirect:/gallery";
	}
	
}
