# Sitemap-monitor

Monitor changes to Sitemaps over time. A command line tool that compares URLs from a live Sitemap with a previous capture.

Examples show the tool detecting changes in - https://www.theguardian.com/sitemaps/news.xml / https://www.theguardian.com/sitemaps/video.xml.


## Usage

```
sitemap-monitor --sitemap <sitemap URL>
```
On first running the tool, if it does not find a previous capture of a Sitemap, it will ask for the user if they'd like to create one -

![Sitemap-monitor screenshot](/images/sitemap-monitor1.png)

Thereafter the tool will compare the live Sitemap with the previous Sitemap capture. It will give the option of updating the previous capture each time the tool is run.

![Sitemap-monitor screenshot](/images/sitemap-monitor.gif)

Sitemap captures are stored in sitemap_memory.JSON - it will be created in the same directory as sitemap_monitor.py. The file can be deleted in order to reset the tool.