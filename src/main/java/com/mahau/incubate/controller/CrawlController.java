/**
 * It's Designed For incubated Center
 * @author      Oh Sanghun
 * @version     %I%, %G%
 * @since       1.0
 */
package com.mahau.incubate.controller;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.mahau.incubate.service.CrawlService;
import com.mahau.incubate.service.ShareService;

@Controller
public class CrawlController {

	@Resource(name = "shareService")
	private ShareService service;

	@Autowired
	private CrawlService crawlService;

	private String ROOT_VIEW = "/crawl/";

	// Receive Parameters from Html Using @RequestParam Map with @PathVariable
	@SuppressWarnings("unchecked")
	@RequestMapping(value = "/crawl/{action}", method = { RequestMethod.GET,
			RequestMethod.POST })
	public ModelAndView doRequest(@RequestParam Map<Object, Object> paramMap,
			@PathVariable String action, ModelAndView modelandView) {

		List<Object> resultList = null;
		Map<Object, Object> resultMap = new HashMap<Object, Object>();
		String viewName = ROOT_VIEW + action;

		try {
			resultList = (List<Object>) crawlService.processPage(paramMap);
		} catch (IOException e) {
			e.printStackTrace();
		}

		viewName = ROOT_VIEW + "list";

		modelandView.addObject("resultList", resultList);
		modelandView.addObject("resultMap", resultMap);
		modelandView.addObject("paramMap", paramMap);
		modelandView.setViewName(viewName);
		return modelandView;
	}

}