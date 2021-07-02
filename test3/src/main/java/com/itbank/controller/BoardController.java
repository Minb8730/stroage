package com.itbank.controller;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.List;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.Board2DTO;
import com.itbank.model.Paging;
import com.itbank.service.Board2Service;

@Controller
@RequestMapping("/board")
public class BoardController {


	@Autowired Board2Service bs;
	
	@GetMapping("/list")
	public ModelAndView list(@RequestParam HashMap<String, String> param, int page) {
		
		ModelAndView mav = new ModelAndView("board/list");
		
		int boardCount = bs.selectBoardCount(param);
		
		Paging paging = new Paging(page, boardCount);
		param.put("perPage", paging.getPerPage() + "");
		param.put("offset", paging.getOffset() + "");
		
		List<Board2DTO> list = bs.selectAll(param);
		mav.addObject("list", list);
		mav.addObject("paging", paging);
		return mav;
	}
	
	@GetMapping("/read/{idx}")
	public ModelAndView read(@PathVariable int idx, boolean vc, String type, String search, int page) {
		
		if(vc) {
			bs.updateViewCount(idx);
			try {
				search = URLEncoder.encode(search, "UTF-8");	// 한글 파라미터를 디스패처서블릿이 처리못하니까 직접 인코딩
			} catch (UnsupportedEncodingException e) {
				e.printStackTrace();
			}
			String location = "redirect:/board/read/" + idx + "/?page=" + page + "&type=" + type + "&search=" + search;
			return new ModelAndView(location);
		}
		
		ModelAndView mav = new ModelAndView("board/read");
		Board2DTO dto = bs.selectOne(idx);
		
		mav.addObject("dto", dto);
		return mav;
	}
	
}
