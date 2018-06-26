package com.mahau.incubate.dao;

import java.util.List;

public interface ShareDao {

	public List<Object> getList(Object sqlMapId, Object dataMap);

	public Object getObject(Object sqlMapId, Object dataMap);

	public Object saveObject(Object sqlMapId, Object dataMap);

	public Object deleteObject(Object sqlMapId, Object dataMap);
}
