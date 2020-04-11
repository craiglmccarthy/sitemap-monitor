```
  _____ _ _                               __  __             _ _
 / ____(_) |                             |  \/  |           (_) |
| (___  _| |_ ___ _ __ ___   __ _ _ __   | \  / | ___  _ __  _| |_ ___  _ __
 \___ \| | __/ _ \ '_ ` _ \ / _` | '_ \  | |\/| |/ _ \| '_ \| | __/ _ \| '__|
 ____) | | ||  __/ | | | | | (_| | |_) | | |  | | (_) | | | | | || (_) | |
|_____/|_|\__\___|_| |_| |_|\__,_| .__/  |_|  |_|\___/|_| |_|_|\__\___/|_|
                                 | |
                                 |_|
```

Monitor changes to Sitemaps over time. A command line tool that compares URLs from a live Sitemap with that of a previous state.

Examples show the tool detecting changes in - https://www.theguardian.com/sitemaps/news.xml / https://www.theguardian.com/sitemaps/video.xml.

## Usage

```
sitemap-monitor.py --sitemap <Sitemap URL>
```

On initial run, if the tool does not find a previous capture of a Sitemap, it will ask the user if they'd like to create one -

![Sitemap-monitor screenshot](/images/sitemap-monitor1.gif)

Thereafter, the tool will compare the live Sitemap with the previous Sitemap state. It will give the option of updating the previous state to the latest Sitemap if changes are detected.

Here is the tool running approximately 30 minutes after previous capture of Sitemap -

![Sitemap-monitor screenshot](/images/sitemap-monitor2.gif)

```
sitemap-monitor.py --sitemap <Sitemap URL> -on -Outputs new URLs

sitemap-monitor.py --sitemap <Sitemap URL> -or -Outputs removed URLs

sitemap-monitor.py --sitemap <Sitemap URL> -fa <keywords> -Outputs new URLs that contain all keywords given

sitemap-monitor.py --sitemap <Sitemap URL> -fo <keywords> -Outputs new URLs that contains at least 1 of the keywords given
```

Sitemap captures are stored in sitemap_memory.json - this will be created in the same directory as sitemap_monitor.py. The file can be deleted in order to reset the tool.
