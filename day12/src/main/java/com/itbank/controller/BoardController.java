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
import com.itbank.model.Paging;
import com.itbank.model.ReplyDTO;
import com.itbank.service.BoardService;

@Controller
@RequestMapping("/board")
public class BoardController {
	
	@Autowired private BoardService bs;

	@GetMapping("/")
	public ModelAndView list(@RequestParam HashMap<String, String> param, int page) {
		
		ModelAndView mav = new ModelAndView("board/list");
		
		int boardCount = bs.selectBoardCount(param);
		
		Paging paging = new Paging(page, boardCount);
		param.put("perPage", paging.getPerPage() + "");
		param.put("offset", paging.getOffset() + "");
		
		List<BoardDTO> list = bs.selectAll(param);
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
			System.out.println("location : " + location);
			return new ModelAndView(location);
		}
		
		ModelAndView mav = new ModelAndView("board/read");
		BoardDTO dto = bs.selectOne(idx);
		
		List<ReplyDTO> replyList = bs.selectReplyList(idx);
		mav.addObject("replyList", replyList);
		
		mav.addObject("dto", dto);
		return mav;
	}
	
	@PostMapping("/read/{idx}")
	public String insertReply(ReplyDTO dto, int page) {
		int row = bs.insertReply(dto);
		return "redirect:/board/read/" + dto.getBnum() + "/?page=" + page;
	}
	
	@GetMapping("/write")
	public String write() {
		return "board/write";
	}
	
	@PostMapping("/write")
	public String write(BoardDTO dto) {
		
		int idx = bs.insertBoard(dto);
		return "redirect:/board/read/" + idx + "/?page=1";
	}
	
	@GetMapping("/delete/{idx}")
	public String delete(@PathVariable int idx, String password) {
		
		int row = bs.deleteBoard(idx, password);
		return "redirect:/board/" + "?page=1&search=";
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
		
		return "redirect:/board/read/" + dto.getIdx() + "/?page=1";
	}
	
	
	
	@GetMapping("deleteReply/{idx}")
	public String deleteReply(@PathVariable int idx, int bnum, String password) {	// reply의 idx
		System.out.println("idx : " + idx);
		System.out.println("bnum : " + bnum);
		System.out.println("password : " + password);
		System.out.println();
		
		int row= bs.deleteReply(idx, password);
		
		return "redirect:/board/read/" + bnum + "?page=1"; 
		
	}
	
	
	
	
}
