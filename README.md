# Sitemap-monitor

Monitor changes to Sitemaps over time. A command line tool that compares URLs from a live Sitemap with that of a previous capture.

Examples show the tool detecting changes in - https://www.theguardian.com/sitemaps/news.xml / https://www.theguardian.com/sitemaps/video.xml.


## Usage

```
sitemap-monitor --sitemap <Sitemap URL>
```
On initial run, if the tool does not find a previous capture of a Sitemap, it will ask the user if they'd like to create one -

![Sitemap-monitor screenshot](/images/sitemap-monitor1.png)

Thereafter, the tool will compare the live Sitemap with the previous Sitemap capture. It will give the option of updating the previous capture to the latest Sitemap each time the tool is run.

Here is the tool running approximately 30 minutes after previous capture of Sitemap -

![Sitemap-monitor screenshot](/images/sitemap-monitor.gif)

```
sitemap-monitor --sitemap <Sitemap URL> -on -Outputs new URLs found to terminal

sitemap-monitor --sitemap <Sitemap URL> -or -Outputs removed URLs found to terminal

sitemap-monitor --sitemap <Sitemap URL> -f <keywords> -Outputs URLs that contain keywords
```

Sitemap captures are stored in sitemap_memory.json - this will be created in the same directory as sitemap_monitor.py. The file can be deleted in order to reset the tool.