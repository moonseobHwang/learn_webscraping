package com.mahau.incubate.util;

import java.util.Date;

import org.springframework.stereotype.Component;

@Component
public class CommonUtil {
    public long getIncrementUserID() {
    	long longTime = new Long(new Date().getTime());
        return longTime;
    }
}
