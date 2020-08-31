package com.mahau.incubate.dao;

import java.util.List;
import java.util.Map;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class ShareDaoImpl implements ShareDao {

	@Autowired
	private SqlSessionTemplate sqlSession;

	@Override
	public List<Object> getList(Object sqlMapId, Object dataMap) {
		List<Object> result = sqlSession.selectList((String) sqlMapId, dataMap);

		return result;
	}

	@Override
	public Object getObject(Object sqlMapId, Object dataMap) {
		Map<Object, Object> result = sqlSession.selectOne((String) sqlMapId, dataMap);
		return result;
	}

	@Override
	public Object saveObject(Object sqlMapId, Object dataMap) {
		Integer result = sqlSession.insert((String)sqlMapId, dataMap);
		return result;
	}

	@Override
	public Object deleteObject(Object sqlMapId, Object dataMap) {
		Integer result = sqlSession.delete((String) sqlMapId,dataMap);
		return result;
	}

}
