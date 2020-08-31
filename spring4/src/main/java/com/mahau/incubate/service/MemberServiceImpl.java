package com.mahau.incubate.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.mahau.incubate.dao.ShareDao;
import com.mahau.incubate.util.CommonUtil;

@Service("memberService")
public class MemberServiceImpl implements ShareService {

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

	@SuppressWarnings("unchecked")
	@Override
	public Object saveObject(Object sqlMapId, Object dataMap) {
		CommonUtil commonUtil = new CommonUtil();
		
		((Map<Object, Object>) dataMap).put("MEMBERID", commonUtil.getIncrementUserID());
		dao.saveObject(sqlMapId, dataMap);
		Object result = dao.getObject("/member/read", dataMap);
		return result;
	}

	@Override
	public Object deleteObject(Object sqlMapId, Object dataMap) {
		dao.deleteObject("/member/delete", dataMap);
		Object result = dao.getList(sqlMapId, dataMap);
		return result;
	}

	@Override
	public Object updateObject(Object sqlMapId, Object dataMap) {
		dao.saveObject(sqlMapId, dataMap);
		Object result = dao.getObject("/member/read", dataMap);
		return result;
	}

}
