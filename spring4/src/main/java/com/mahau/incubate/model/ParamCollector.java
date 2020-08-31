package com.mahau.incubate.model;

import java.util.HashMap;
import java.util.Map;

public class ParamCollector{

    Map<Object, Object> map = new HashMap<Object, Object>();

    public String get(Object key){
        return (String) map.get(key);
    }

    public void put(Object key, Object value){
        map.put(key, value);
    }
    
    public Map<Object, Object> getMap(){
    	return this.map;
    }

    public String toString() {
        return map.toString();
    }
}