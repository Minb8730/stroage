package com.itbank.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.SnackDTO;
import com.itbank.service.SnackbarService;

@Controller
@RequestMapping("snackbar")
public class SnackbarController {

	@Autowired
	private SnackbarService ss;
	
	@GetMapping("")			// 등록된 상품의 목록을 띄우는 페이지
	public ModelAndView index() {
		ModelAndView mav = new ModelAndView("index");	//index.jsp를 지정해둔다.
		List<SnackDTO> list = ss.getSnackList();		//서비스 -> DAO를 통해 상품 목록을 가져온다.
		mav.addObject("list", list);					// 가져온 리스트를 view에 넘긴다.
		return mav;										// 메서드 종료 -> view로 이동
	}
	
	@PostMapping("") 	// postmapping 시에 데이터를 처리하고 나서 원래 페이지로 redirect를 걸어주자!!
	public String insert(SnackDTO dto) {
		System.out.println(dto.getName());
		System.out.println(dto.getPrice());
		
		int row = ss.insertSnack(dto);
		System.out.println(row == 1 ? "성공" : "실패");
		return "redirect:/snackbar";	// jsp주소가 아니라, 브라우저 주소창에 찍히는 주소, 요청주소이다.
	}
	
	@GetMapping("update/{idx}")
	public ModelAndView update(@PathVariable int idx) {		// 쿼리스트링 형식 대신, 주소에 포함되는 문자열이나 숫자를 처리하는 어노테이션
		System.out.println("idx : " +idx);
		//idx를 전달받아서, 상품 정보를 모두 가져온 후에, form 형식에 값이 채워진채로 화면을 띄운다.
		ModelAndView mav = new ModelAndView("update");
		SnackDTO dto = ss.selectOne(idx);
		mav.addObject("dto", dto);
		return mav;
	}
	
	@PostMapping("update/{idx}")
	public String update(@PathVariable int idx, SnackDTO dto) { // 위의 update와 변수가 같으면 오버로딩이 안된다.
		dto.setIdx(idx);
		int row = ss.update(dto);
		System.out.println(row == 1? "수정 성공!!" : "수정 실패!!");
		return "redirect:/snackbar";
	}
	
	@GetMapping("delete/{idx}")
	public String delete(@PathVariable int idx) {
		int row = ss.delete(idx);
		return "redirect:/snackbar";
	}
	
}
