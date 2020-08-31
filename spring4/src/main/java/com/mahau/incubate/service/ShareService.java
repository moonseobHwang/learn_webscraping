package com.mahau.incubate.service;

import java.util.List;

public interface ShareService {

	public List<Object> getList(Object sqlMapId, Object dataMap);

	public Object getObject(Object sqlMapId, Object dataMap);

	public Object saveObject(Object sqlMapId, Object dataMap);

	public Object deleteObject(Object sqlMapId, Object dataMap);
	
	public Object updateObject(Object sqlMapId, Object dataMap);	
}
