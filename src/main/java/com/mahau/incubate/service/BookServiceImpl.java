package com.mahau.incubate.service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.mahau.incubate.dao.ShareDao;
import com.mahau.incubate.util.CommonUtil;

@Service("bookService")
public class BookServiceImpl implements ShareService {

	@Autowired
	private ShareDao dao;

	private String ROOT_VIEW = "/book/";

	@Override
	public List<Object> getList(Object sqlMapId, Object dataMap) {
		List<Object> result = dao.getList(sqlMapId, dataMap);
		return result;
	}

	@Override
	public Object getObject(Object sqlMapId, Object dataMap) {
		Object result = dao.getObject(sqlMapId, dataMap);
		return result;
	}

	@SuppressWarnings("unchecked")
	@Override
	public Object saveObject(Object sqlMapId, Object dataMap) {
		CommonUtil commonUtil = new CommonUtil();
		long createID = commonUtil.getIncrementUserID();

		((Map<Object, Object>) dataMap).put("BOOKID", createID);
		dao.saveObject(sqlMapId, dataMap);

		List<Object> fileInformationList = (List<Object>) ((Map<Object, Object>) dataMap)
				.get("fileList");
		Map<Object, Object> fileMap = null;

		if (fileInformationList != null && fileInformationList.size() > 0) {
			fileMap = (HashMap<Object, Object>) fileInformationList.get(0);
			fileMap.put("FILEINFORID", commonUtil.getIncrementUserID());
			fileMap.put("RELATEDID", createID);
			dao.saveObject("/fileinfor/insert", fileMap);
		}

		Object result = dao.getObject(ROOT_VIEW + "read", dataMap);
		return result;
	}

	@Override
	public Object deleteObject(Object sqlMapId, Object dataMap) {
		dao.deleteObject(ROOT_VIEW + "delete", dataMap);
		Object result = dao.getList(sqlMapId, dataMap);
		return result;
	}

	@Override
	public Object updateObject(Object sqlMapId, Object dataMap) {
		dao.saveObject(sqlMapId, dataMap);
		Object result = dao.getObject(ROOT_VIEW + "read", dataMap);
		return result;
	}

}
