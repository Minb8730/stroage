package com.itbank.model;

import java.util.List;

// repository annotation 을 붙이지 않는다.
public interface StudentDAO2 {

	List<StudentDTO> selectStudentList2();

}
