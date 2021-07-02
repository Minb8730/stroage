package com.itbank.model;

// 매번 객체를 새로 생성해서, 객체마다 서로 다른 값을 가져야 한다면, 스프링 빈으로 등록하지 않는다 (dto와 비슷하게)
// 객체가 하나만 존재하고, 자동 의존 주입으로 객체간의 참조를 구현하려면, 스프링 빈으로 등록한다 (@Component)

public class Paging {
	// 사용자 요청에 담긴 페이지 요청번호(?page=1)에 따라서, 내부에  페이징 정보를 담고 있는 객체를 생성한다
	
	private final int perPage = 10;
	private int page;				// 사용자가 요청한 페이지 번호
	private int boardCount;
	private int pageCount;
	private int offset;				// 첫번째 글에서 몇개의 글을 건너뛸지 결정하는 개수
	
	private final int perSection = 10;
	private int begin;
	private int end;
	private int section;			// <c:if test="${true }">
	
	private boolean prev;
	private boolean next;
	
	public Paging(int page, int boardCount) {
		this.page = page;
		this.boardCount = boardCount;
		
		offset = (page - 1) * perPage;
		
		pageCount = boardCount / perPage;
		pageCount += (boardCount % perPage == 0) ? 0 : 1; 
		
		section = (page - 1) / perSection;	//  0,  1,  2,  3 ...
		begin = perSection * section + 1;	//  1, 11, 21, 31 ...
		end = begin + perSection - 1;		// 10, 20, 30, 40 ...
		end = (end < pageCount) ? end : pageCount;	// 둘 중 작은 값을 end로 처리한다
		
		prev = section != 0;
		next = boardCount > perPage * end;
		
//		System.out.printf("select * from board where deleted = 'n' order by idx desc "
//				+ "offset %d rows fetch first %d rows only\n", offset, perPage);
	}
	
	
	public int getPage() {
		return page;
	}
	public void setPage(int page) {
		this.page = page;
	}
	public int getBoardCount() {
		return boardCount;
	}
	public void setBoardCount(int boardCount) {
		this.boardCount = boardCount;
	}
	public int getOffset() {
		return offset;
	}
	public void setOffset(int offset) {
		this.offset = offset;
	}
	public int getBegin() {
		return begin;
	}
	public void setBegin(int begin) {
		this.begin = begin;
	}
	public int getEnd() {
		return end;
	}
	public void setEnd(int end) {
		this.end = end;
	}
	public int getSection() {
		return section;
	}
	public void setSection(int section) {
		this.section = section;
	}
	public boolean isPrev() {
		return prev;
	}
	public void setPrev(boolean prev) {
		this.prev = prev;
	}
	public boolean isNext() {
		return next;
	}
	public void setNext(boolean next) {
		this.next = next;
	}
	public int getPerPage() {
		return perPage;
	}
	public int getPerSection() {
		return perSection;
	}
	
	
}
