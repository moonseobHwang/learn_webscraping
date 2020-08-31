package com.mahau.incubate.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.mahau.incubate.dao.ShareDao;

@Service("shareService")
public class ShareServiceImpl implements ShareService {

	@Autowired
	private ShareDao dao;

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

	@Override
	public Object saveObject(Object sqlMapId, Object dataMap) {
		Object result = dao.saveObject(sqlMapId, dataMap);
		return result;
	}

	@Override
	public Object deleteObject(Object sqlMapId, Object dataMap) {
		Object result = dao.deleteObject(sqlMapId, dataMap);
		return result;
	}

	@Override
	public Object updateObject(Object sqlMapId, Object dataMap) {
		return null;
	}

}
