/**
 * It's Designed For incubated Center
 * @author      Oh Sanghun
 * @version     %I%, %G%
 * @since       1.0
 */
package com.mahau.incubate.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.mahau.incubate.service.ShareService;

@Controller
public class MemberController {

	@Resource(name="memberService")
	private ShareService service;

	private String ROOT_VIEW = "/member/";

	// Receive Parameters from Html Using @RequestParam Map with @PathVariable
	@SuppressWarnings("unchecked")
	@RequestMapping(value = "/member/{action}", method = { RequestMethod.GET, RequestMethod.POST })
	public ModelAndView doRequest(@RequestParam Map<Object, Object> paramMap, @PathVariable String action,
			ModelAndView modelandView) {

		List<Object> resultList = null;
		Map<Object, Object> resultMap = new HashMap<Object, Object>() ;
		String viewName = ROOT_VIEW + action;

		// delete 
		if ("delete".equals(action)) {
			service.deleteObject(viewName, paramMap);
			viewName = ROOT_VIEW + "list";
			resultList = service.getList(viewName, paramMap);

			// update
		} else if ("update".equals(action)) {
			resultMap = (Map<Object, Object>) service.updateObject(viewName, paramMap);			
			viewName = ROOT_VIEW + "read";

			// insert
		} else if ("insert".equals(action)) {
			resultMap = (Map<Object, Object>) service.saveObject(viewName, paramMap);
			viewName = ROOT_VIEW + "read";

			// read
		} else if ("read".equals(action)) {
			resultMap = (Map<Object, Object>) service.getObject(viewName, paramMap);

			// edit by pass
		} else if ("edit".equals(action)) {
			String userid = (String) paramMap.get("MEMBERID");
			if(userid == null){
				resultMap.put("forword", "insert");
			} else {
				resultMap = (Map<Object, Object>) service.getObject(ROOT_VIEW + "read", paramMap);
				resultMap.put("forword", "update");
			}

			// list
		} else if ("list".equals(action)) {
			resultList = service.getList(viewName, paramMap);

			// forward exception page
		} 

		modelandView.addObject("resultList", resultList);
		modelandView.addObject("resultMap", resultMap);
		modelandView.addObject("paramMap", paramMap);
		modelandView.setViewName(viewName);
		return modelandView;

	}
}