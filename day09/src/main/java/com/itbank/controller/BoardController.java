package com.itbank.controller;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.BoardDTO;
import com.itbank.service.BoardService;

@Controller
@RequestMapping("/board")
public class BoardController {
	
	@Autowired private BoardService bs;

	@GetMapping("/")
	public ModelAndView list(@RequestParam HashMap<String, String> param) {
		System.out.println(param);
		System.out.println(param.size());
		
		ModelAndView mav = new ModelAndView("board/list");
		List<BoardDTO> list = bs.selectAll(param);
		System.out.println(list.size());
		mav.addObject("list", list);
		return mav;
	}
	
	@GetMapping("/read/{idx}")
	public ModelAndView read(@PathVariable int idx, boolean vc, String type, String search) {

		if(vc) {
			bs.updateViewCount(idx);
			try {
				search = URLEncoder.encode(search, "UTF-8");	// 한글 파라미터를 디스패처서블릿이 처리못하니까 직접 인코딩
			} catch (UnsupportedEncodingException e) {
				e.printStackTrace();
			}
			String location = "redirect:/board/read/" + idx + "/?type=" + type + "&search=" + search;
			System.out.println("location : " + location);
			return new ModelAndView(location);
		}
		
		ModelAndView mav = new ModelAndView("board/read");
		BoardDTO dto = bs.selectOne(idx);
		mav.addObject("dto", dto);
		return mav;
	}
	
	@GetMapping("/write")
	public String write() {
		return "board/write";
	}
	
	@PostMapping("/write")
	public String write(BoardDTO dto) {
		
		int idx = bs.insertBoard(dto);
		return "redirect:/board/read/" + idx;
	}
	
	@GetMapping("/delete/{idx}")
	public String delete(@PathVariable int idx, String password) {
		
		int row = bs.deleteBoard(idx, password);
		return "redirect:/board/";
	}
	
	@GetMapping("/modify/{idx}")
	public ModelAndView modify(@PathVariable int idx) {
		ModelAndView mav = new ModelAndView("board/modify");
		BoardDTO dto = bs.selectOne(idx);
		mav.addObject("dto", dto);
		return mav;
	}
	
	@PostMapping("/modify/{idx}")
	public String modify(BoardDTO dto) {
		
		int row = bs.modify(dto);
		
		return "redirect:/board/read/" + dto.getIdx();
	}
	
	
	
	
	
	
	
	
}
