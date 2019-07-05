#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-06-18 15:51:27
# Project: YouXin

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        'proxy': 'HB33WL15KSV4H8RD:F88EC4F8F9E7E049@http-dyn.abuyun.com:9020',
        'itag': 'v004',
    }


    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.xin.com/guangzhou/s/?channel=a49b117c44837d110753e751863f53', callback=self.index_page, validate_cert=False,fetch_type='js')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('li > .across > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js',validate_cert=False)
        next = response.doc('.con-page.search_page_link a:last-child').attr.href
        self.crawl(next, callback=self.index_page,fetch_type='js', validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "标题": response.doc('.cd_m_info_it2 > .cd_m_h.cd_m_h_zjf > .cd_m_h_tit').text(),
            "原价": response.doc('.new-noline').text(),
            "现价": response.doc('.cd_m_info_jg b').text(),
            "排放标准": response.doc('.cd_m_i_pz > dl:nth-child(1) > dd:nth-child(1) > span:nth-child(2)').text(),
            "表显里程": response.doc('.cd_m_i_pz > dl:nth-child(1) > dd:nth-child(2) > span:nth-child(2) > a').text(),
            "使用性质": response.doc('.cd_m_i_pz > dl:nth-child(1) > dd:nth-child(3) > span:nth-child(2)').text(),
            "年检到期": response.doc('.cd_m_i_pz > dl:nth-child(1) > dd:nth-child(4) > span:nth-child(2)').text(),
            "保险到期": response.doc('.cd_m_i_pz > dl:nth-child(1) > dd:nth-child(5) > span:nth-child(2)').text(),
            "保养情况": response.doc('.cd_m_i_pz > dl:nth-child(1) > dd:nth-child(6) > span:nth-child(2)').text(),
            "车辆厂商": response.doc('.cd_m_i_pz > dl:nth-child(2) > dd:nth-child(1) > span:nth-child(2) > a').text(),
            "车辆级别": response.doc('.cd_m_i_pz > dl:nth-child(2) > dd:nth-child(2) > span:nth-child(2) > a').text(),
            "车辆颜色": response.doc('.cd_m_i_pz > dl:nth-child(2) > dd:nth-child(3) > span:nth-child(2) > a').text(),
            "车身结构": response.doc('.cd_m_i_pz > dl:nth-child(2) > dd:nth-child(4) > span:nth-child(2) > a').text(),
            "整备质量": response.doc('.cd_m_i_pz > dl:nth-child(2) > dd:nth-child(5) > span:nth-child(2)').text(),
            "轴距": response.doc('.cd_m_i_pz > dl:nth-child(2) > dd:nth-child(6) > span:nth-child(2)').text(),
            "发动机": response.doc('.cd_m_i_pz > dl:nth-child(3) > dd:nth-child(1) > span:nth-child(2)').text(),
            "变速器": response.doc('.cd_m_i_pz > dl:nth-child(3) > dd:nth-child(2) > span:nth-child(2) > a').text(),
            "排量": response.doc('.cd_m_i_pz > dl:nth-child(3) > dd:nth-child(3) > span:nth-child(2) > a').text(),
            "燃料类型": response.doc('.cd_m_i_pz > dl:nth-child(3) > dd:nth-child(4) > span:nth-child(2)').text(),
            "驱动方式": response.doc('.cd_m_i_pz > dl:nth-child(3) > dd:nth-child(5) > span:nth-child(2)').text(),
            "综合油耗": response.doc('.cd_m_i_pz > dl:nth-child(3) > dd:nth-child(6) > span:nth-child(2)').text(),
        }
