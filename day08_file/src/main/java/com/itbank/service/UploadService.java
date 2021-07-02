package com.itbank.service;

import java.io.File;
import java.io.IOException;
import java.sql.ResultSet;
import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.itbank.model.GalleryDAO;
import com.itbank.model.GalleryDTO;

@Service
public class UploadService {

	@Autowired private GalleryDAO dao;
	
	private final String uploadPath ="D:\\upload"; //윈도우일 경우

	public UploadService() {
		File dir = new File(uploadPath);
		if(dir.exists() == false) {
			dir.mkdirs();	// mkdir -p [경로] : 상위 경로가 없으면 상위경로도 같이 만들어라
		}
	}
	
	public List<String> getList(){
		File dir = new File(uploadPath);
		if(dir.exists()) {
//			dir.listFiles(); 						// 지정한 디렉토리 내부의 [파일 객체] 을 [파일 배열] 형태로 반환하는 메서
			String[] fileNames =  dir.list();		//지정한 디렉토리 내부의 [파일 이름]을 [문자열 배열] 형태로 반환하는 메서드
			List<String> list = Arrays.asList(fileNames);	// 배열을 리스트로 (add는 작동안함)
			return list;
			}
		return null;
	}
	
	public boolean upload(MultipartFile uploadFile) {
		
		File target = new File(uploadPath, uploadFile.getOriginalFilename());
		// 사용자가 업로드한 파일을 서버의 지정한 위치에 만들 객체
		
		if(uploadFile.getContentType().contains("image")) { // 조건을 만족하면
			try {
				uploadFile.transferTo(target); // 입력받은 파일을 대상 위치에 전송(복사)
				return true;
			} catch (IllegalStateException | IOException e) {
				e.printStackTrace();
			}
		}
		return target.exists();	// if를 수행했으면, 파일이 존재하므로 true
	}

	public int insert(GalleryDTO dto) {
		int row=0;
		if(dto.ready()) {
			File target = new File(uploadPath, dto.getStoredFileName());	// 객체가 생성되어도 파일이 있다는 보장은 없다.
			try {
				dto.getUploadFile().transferTo(target);
				
			} catch (IllegalStateException | IOException e) {
				e.printStackTrace();
			}
			
			row= dao.insert(dto);
		}
		return row;
	}

	public List<GalleryDTO> getGalleryList() {
		
		
		return dao.selectGalleryList();
	}




	
	
	
	
}
