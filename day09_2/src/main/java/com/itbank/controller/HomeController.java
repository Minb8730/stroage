package com.itbank.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.BoardDTO;
import com.itbank.service.BoardService;

@Controller
public class HomeController {
	
	@Autowired private BoardService bs;
	
	
	@RequestMapping("/")
	public String home() {
		return "home";
	}
	
	@GetMapping("list")
	public ModelAndView list(ModelAndView mav) {
		
		List<BoardDTO> list = bs.selectAll();
		mav.addObject("list", list);
		mav.setViewName("list");
		
		return mav;
	}
	
	@GetMapping("write")
	public String write() {
		return "write";
	}
	
	@PostMapping("write")
	public ModelAndView write(BoardDTO dto) {
		ModelAndView mav = new ModelAndView("redirect:/list/");
		int row = bs.insert(dto);
		return mav;
	}
	
	@GetMapping("delete/{title}")
	public ModelAndView delete(@PathVariable int idx ) {
		ModelAndView mav = new ModelAndView("redirect:/list/");
		int row = bs.delete(idx);
		String msg = "게시글 삭제가 되지 않았습니다.";
//		mav.setViewName("alert");
		if(row==1) {
			msg = "게시글이 삭제되었습니다.";
			mav.addObject("msg", msg);
			return mav;
		}
		mav.addObject("msg", msg);
		return mav;
	}
	
	@GetMapping("read/{idx}")
	public ModelAndView read(@PathVariable int idx ) {
		ModelAndView mav = new ModelAndView();
		BoardDTO dto = bs.selectOne(idx);
		mav.addObject("dto", dto);
		mav.setViewName("read");
		return mav;
	}
	
	@GetMapping("update/{idx}")
	public ModelAndView update(@PathVariable int idx) {
		ModelAndView mav = new ModelAndView();
		BoardDTO dto = bs.selectOne(idx);
		mav.addObject("dto", dto);
		mav.setViewName("update");
		return mav;
	}
	@PostMapping("update/{idx}")
	public String update(@PathVariable int idx, @PathVariable String content) {
		int row = bs.update(idx, content);
		if(row == 1) {
			return "read/" + idx;
		}
		return "update";
	}
	
	@GetMapping("find")
	public String find() {
		return "find";
	}
	
	@PostMapping("find")
	public ModelAndView find(String findArticle) {
		ModelAndView mav = new ModelAndView();
		
		return mav;
	}
	
}
