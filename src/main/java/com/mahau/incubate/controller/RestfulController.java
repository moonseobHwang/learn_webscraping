/**
 * It's Designed For incubated Center
 * @author      Oh Sanghun
 * @version     %I%, %G%
 * @since       1.0
 */
package com.mahau.incubate.controller;

import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.mahau.incubate.service.ShareService;

@Controller
public class RestfulController {

	@Resource(name = "shareService")
	private ShareService service;

	@RequestMapping(value = "/restfulMap", method = { RequestMethod.POST,
			RequestMethod.GET })
	public @ResponseBody List<Object> doRestful(
			@RequestParam Map<Object, Object> paramMap) {
		List<Object> resultList = service.getList(paramMap.get("viewName"),
				paramMap);
		return resultList;

	}

}