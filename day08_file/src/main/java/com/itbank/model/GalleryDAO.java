package com.itbank.model;

import java.util.List;

public interface GalleryDAO {

	int insert(GalleryDTO dto);

	List<GalleryDTO> selectGalleryList();



}
