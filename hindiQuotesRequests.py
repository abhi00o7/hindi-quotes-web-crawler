import json
import urllib.request
import requests
from bs4 import BeautifulSoup

# hindi quotes website आज का सुविचार
r = requests.get('https://aajkasuvichar.com/aaj-ka-suvichar/')

html_doc = '''

<!doctype html>
<!--[if IE 8]><html class="ie8" lang="en"> <![endif]-->
<!--[if IE 9]><html class="ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!-->
<html lang="en-US" prefix="og: https://ogp.me/ns#">
<!--<![endif]-->

<head>
    <link media="all"
        href="https://aajkasuvichar.com/wp-content/cache/autoptimize/css/autoptimize_3911836228d18944ce8de8d6bc5046e0.css"
        rel="stylesheet" />
    <title>Aaj Ka Suvichar 2021 |आज का सुविचार - Aaj Ka Suvichar</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="pingback" href="https://aajkasuvichar.com/xmlrpc.php" />
    <script type="text/javascript">
        ! function (e) {
            var n = {};

            function t(r) {
                if (n[r]) return n[r].exports;
                var o = n[r] = {
                    i: r,
                    l: !1,
                    exports: {}
                };
                return e[r].call(o.exports, o, o.exports, t), o.l = !0, o.exports
            }
            t.m = e, t.c = n, t.d = function (e, n, r) {
                t.o(e, n) || Object.defineProperty(e, n, {
                    enumerable: !0,
                    get: r
                })
            }, t.r = function (e) {
                "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                    value: "Module"
                }), Object.defineProperty(e, "__esModule", {
                    value: !0
                })
            }, t.t = function (e, n) {
                if (1 & n && (e = t(e)), 8 & n) return e;
                if (4 & n && "object" == typeof e && e && e.__esModule) return e;
                var r = Object.create(null);
                if (t.r(r), Object.defineProperty(r, "default", {
                        enumerable: !0,
                        value: e
                    }), 2 & n && "string" != typeof e)
                    for (var o in e) t.d(r, o, function (n) {
                        return e[n]
                    }.bind(null, o));
                return r
            }, t.n = function (e) {
                var n = e && e.__esModule ? function () {
                    return e.default
                } : function () {
                    return e
                };
                return t.d(n, "a", n), n
            }, t.o = function (e, n) {
                return Object.prototype.hasOwnProperty.call(e, n)
            }, t.p = "", t(t.s = 0)
        }([function (e, n, t) {
            (function (e) {
                ! function (n) {
                    var t = n.ampUrl,
                        r = n.isCustomizePreview,
                        o = n.isAmpDevMode,
                        i = n.noampQueryVarName,
                        a = n.noampQueryVarValue,
                        u = n.disabledStorageKey,
                        s = n.mobileUserAgents,
                        c = n.regexRegex;
                    if ("undefined" != typeof sessionStorage) {
                        var f = new RegExp(c);
                        if (s.some((function (e) {
                                var n = e.match(f);
                                return !(!n || !new RegExp(n[1], n[2]).test(navigator.userAgent)) ||
                                    navigator.userAgent.includes(e)
                            }))) {
                            e.addEventListener("DOMContentLoaded", (function () {
                                var e = document.getElementById("amp-mobile-version-switcher");
                                if (e) {
                                    e.hidden = !1;
                                    var n = e.querySelector("a[href]");
                                    n && n.addEventListener("click", (function () {
                                        sessionStorage.removeItem(u)
                                    }))
                                }
                            }));
                            var d = o && ["paired-browsing-non-amp", "paired-browsing-amp"].includes(window
                                .name);
                            if (!(sessionStorage.getItem(u) || r || d)) {
                                var l = new URL(location.href),
                                    p = new URL(t);
                                p.hash = l.hash, l.searchParams.has(i) && a === l.searchParams.get(i) ?
                                    sessionStorage.setItem(u, "1") : p.href !== l.href && (window.stop(),
                                        location.replace(p.href))
                            }
                        }
                    }
                }({
                    "ampUrl": "https:\/\/aajkasuvichar.com\/aaj-ka-suvichar\/?amp",
                    "noampQueryVarName": "noamp",
                    "noampQueryVarValue": "mobile",
                    "disabledStorageKey": "amp_mobile_redirect_disabled",
                    "mobileUserAgents": ["Mobile", "Android", "Silk\/", "Kindle", "BlackBerry",
                        "Opera Mini", "Opera Mobi"
                    ],
                    "regexRegex": "^\\/((?:.|\n)+)\\/([i]*)$",
                    "isCustomizePreview": false,
                    "isAmpDevMode": false
                })
            }).call(this, t(1))
        }, function (e, n) {
            var t;
            t = function () {
                return this
            }();
            try {
                t = t || new Function("return this")()
            } catch (e) {
                "object" == typeof window && (t = window)
            }
            e.exports = t
        }]);
    </script>
    <link rel="icon" type="image/png"
        href="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_180,h_180/https://aajkasuvichar.com/wp-content/uploads/2020/08/AajKaSuvichar.png">
    <meta name="description"
        content="Aaj Ka Suvichar 2020 |आज का सुविचार:- वे विचार या महान लोगों के कथन, जो हमारे जीवन पर सकारात्मक प्रभाव डालते हैं। उन्हें ही सुविचार कहाँ जाता है। सुविचारों" />
    <meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large" />
    <link rel="canonical" href="https://aajkasuvichar.com/aaj-ka-suvichar/" />
    <meta property="og:locale" content="en_US" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="Aaj Ka Suvichar 2021 |आज का सुविचार - Aaj Ka Suvichar" />
    <meta property="og:description"
        content="Aaj Ka Suvichar 2020 |आज का सुविचार:- वे विचार या महान लोगों के कथन, जो हमारे जीवन पर सकारात्मक प्रभाव डालते हैं। उन्हें ही सुविचार कहाँ जाता है। सुविचारों" />
    <meta property="og:url" content="https://aajkasuvichar.com/aaj-ka-suvichar/" />
    <meta property="og:site_name" content="Aaj Ka Suvichar" />
    <meta property="article:publisher" content="https://www.facebook.com/SuVichar24/" />
    <meta property="article:tag" content="aaj ka shubh vichar" />
    <meta property="article:tag" content="aaj ka suvichar 2021" />
    <meta property="article:tag" content="aaj ka suvichar batao" />
    <meta property="article:tag" content="aaj ka suvichar good morning" />
    <meta property="article:tag" content="aaj ka suvichar hindi" />
    <meta property="article:tag" content="aaj ka suvichar hindi me" />
    <meta property="article:tag" content="aaj ka suvichar hindi mein" />
    <meta property="article:tag" content="Aaj Ka Suvichar in Hindi" />
    <meta property="article:tag" content="aaj ka suvichar in hindi 2021" />
    <meta property="article:tag" content="aaj ka suvichar in hindi for students" />
    <meta property="article:tag" content="aaj ka suvichar in hindi text" />
    <meta property="article:tag" content="aaj ka suvichar kya ha" />
    <meta property="article:tag" content="aaj ka suvichar latest" />
    <meta property="article:tag" content="aaj ka vichar in hindi for whatsapp" />
    <meta property="article:tag" content="आज का सुविचार" />
    <meta property="article:section" content="Hindi Quotes" />
    <meta property="og:updated_time" content="2021-02-20T13:35:00+00:00" />
    <meta property="og:image" content="https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg" />
    <meta property="og:image:secure_url" content="https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg" />
    <meta property="og:image:width" content="640" />
    <meta property="og:image:height" content="360" />
    <meta property="og:image:alt" content="Aaj Ka suvichar in hindi" />
    <meta property="og:image:type" content="image/jpeg" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Aaj Ka Suvichar 2021 |आज का सुविचार - Aaj Ka Suvichar" />
    <meta name="twitter:description"
        content="Aaj Ka Suvichar 2020 |आज का सुविचार:- वे विचार या महान लोगों के कथन, जो हमारे जीवन पर सकारात्मक प्रभाव डालते हैं। उन्हें ही सुविचार कहाँ जाता है। सुविचारों" />
    <meta name="twitter:image" content="https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg" />
    <script type="application/ld+json" class="rank-math-schema">
        {
            "@context": "https://schema.org",
            "@graph": [{
                "@type": ["Organization", "Person"],
                "@id": "https://aajkasuvichar.com/#person",
                "name": "AajKaSuvichar",
                "url": "https://aajkasuvichar.com",
                "logo": {
                    "@type": "ImageObject",
                    "@id": "https://aajkasuvichar.com/#logo",
                    "url": "https://aajkasuvichar.com/wp-content/uploads/2020/08/AajKaSuvichar.png",
                    "caption": "AajKaSuvichar",
                    "inLanguage": "en-US",
                    "width": "600",
                    "height": "600"
                },
                "image": {
                    "@id": "https://aajkasuvichar.com/#logo"
                }
            }, {
                "@type": "WebSite",
                "@id": "https://aajkasuvichar.com/#website",
                "url": "https://aajkasuvichar.com",
                "name": "AajKaSuvichar",
                "publisher": {
                    "@id": "https://aajkasuvichar.com/#person"
                },
                "inLanguage": "en-US"
            }, {
                "@type": "ImageObject",
                "@id": "https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg",
                "url": "https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg",
                "width": "640",
                "height": "360",
                "caption": "Aaj Ka suvichar in hindi",
                "inLanguage": "en-US"
            }, {
                "@type": "Person",
                "@id": "https://aajkasuvichar.com/author/AajKaSuvichar/",
                "name": "AajKaSuvichar",
                "url": "https://aajkasuvichar.com/author/AajKaSuvichar/",
                "image": {
                    "@type": "ImageObject",
                    "@id": "https://secure.gravatar.com/avatar/d30991ca73ad0e2b85a32aef80f71c3a?s=96&amp;r=g",
                    "url": "https://secure.gravatar.com/avatar/d30991ca73ad0e2b85a32aef80f71c3a?s=96&amp;r=g",
                    "caption": "AajKaSuvichar",
                    "inLanguage": "en-US"
                },
                "sameAs": ["https://aajkasuvichar.com"]
            }, {
                "@type": "WebPage",
                "@id": "https://aajkasuvichar.com/aaj-ka-suvichar/#webpage",
                "url": "https://aajkasuvichar.com/aaj-ka-suvichar/",
                "name": "Aaj Ka Suvichar 2021 |\u0906\u091c \u0915\u093e \u0938\u0941\u0935\u093f\u091a\u093e\u0930 - Aaj Ka Suvichar",
                "datePublished": "2018-10-19T09:32:00+00:00",
                "dateModified": "2021-02-20T13:35:00+00:00",
                "author": {
                    "@id": "https://aajkasuvichar.com/author/AajKaSuvichar/"
                },
                "isPartOf": {
                    "@id": "https://aajkasuvichar.com/#website"
                },
                "primaryImageOfPage": {
                    "@id": "https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg"
                },
                "inLanguage": "en-US"
            }, {
                "@type": "BlogPosting",
                "headline": "Aaj Ka Suvichar 2021 |\u0906\u091c \u0915\u093e \u0938\u0941\u0935\u093f\u091a\u093e\u0930 - Aaj Ka Suvichar",
                "datePublished": "2018-10-19T09:32:00+00:00",
                "dateModified": "2021-02-20T13:35:00+00:00",
                "author": {
                    "@type": "Person",
                    "name": "AajKaSuvichar"
                },
                "publisher": {
                    "@id": "https://aajkasuvichar.com/#person"
                },
                "description": "Aaj Ka Suvichar 2020 |\u0906\u091c \u0915\u093e \u0938\u0941\u0935\u093f\u091a\u093e\u0930:- \u0935\u0947 \u0935\u093f\u091a\u093e\u0930 \u092f\u093e \u092e\u0939\u093e\u0928 \u0932\u094b\u0917\u094b\u0902 \u0915\u0947 \u0915\u0925\u0928, \u091c\u094b \u0939\u092e\u093e\u0930\u0947 \u091c\u0940\u0935\u0928 \u092a\u0930 \u0938\u0915\u093e\u0930\u093e\u0924\u094d\u092e\u0915 \u092a\u094d\u0930\u092d\u093e\u0935 \u0921\u093e\u0932\u0924\u0947 \u0939\u0948\u0902\u0964 \u0909\u0928\u094d\u0939\u0947\u0902 \u0939\u0940 \u0938\u0941\u0935\u093f\u091a\u093e\u0930 \u0915\u0939\u093e\u0901 \u091c\u093e\u0924\u093e \u0939\u0948\u0964 \u0938\u0941\u0935\u093f\u091a\u093e\u0930\u094b\u0902",
                "name": "Aaj Ka Suvichar 2021 |\u0906\u091c \u0915\u093e \u0938\u0941\u0935\u093f\u091a\u093e\u0930 - Aaj Ka Suvichar",
                "@id": "https://aajkasuvichar.com/aaj-ka-suvichar/#richSnippet",
                "isPartOf": {
                    "@id": "https://aajkasuvichar.com/aaj-ka-suvichar/#webpage"
                },
                "image": {
                    "@id": "https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg"
                },
                "inLanguage": "en-US",
                "mainEntityOfPage": {
                    "@id": "https://aajkasuvichar.com/aaj-ka-suvichar/#webpage"
                }
            }]
        }
    </script>
    <link rel='dns-prefetch' href='//www.googletagmanager.com' />
    <link rel='dns-prefetch' href='//fonts.googleapis.com' />
    <link rel='dns-prefetch' href='//s.w.org' />
    <link rel='dns-prefetch' href='//pagead2.googlesyndication.com' />
    <link href='https://cdn.shortpixel.ai' rel='preconnect' />
    <link rel="alternate" type="application/rss+xml" title="Aaj Ka Suvichar &raquo; Feed"
        href="https://aajkasuvichar.com/feed/" />
    <link rel="alternate" type="application/rss+xml" title="Aaj Ka Suvichar &raquo; Comments Feed"
        href="https://aajkasuvichar.com/comments/feed/" />
    <link rel="alternate" type="application/rss+xml"
        title="Aaj Ka Suvichar &raquo; Aaj Ka Suvichar 2021 |आज का सुविचार Comments Feed"
        href="https://aajkasuvichar.com/aaj-ka-suvichar/feed/" />
    <script type="text/javascript">
        window._wpemojiSettings = {
            "baseUrl": "https:\/\/s.w.org\/images\/core\/emoji\/13.0.1\/72x72\/",
            "ext": ".png",
            "svgUrl": "https:\/\/s.w.org\/images\/core\/emoji\/13.0.1\/svg\/",
            "svgExt": ".svg",
            "source": {
                "concatemoji": "https:\/\/aajkasuvichar.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.7.2"
            }
        };
        ! function (e, a, t) {
            var n, r, o, i = a.createElement("canvas"),
                p = i.getContext && i.getContext("2d");

            function s(e, t) {
                var a = String.fromCharCode;
                p.clearRect(0, 0, i.width, i.height), p.fillText(a.apply(this, e), 0, 0);
                e = i.toDataURL();
                return p.clearRect(0, 0, i.width, i.height), p.fillText(a.apply(this, t), 0, 0), e === i.toDataURL()
            }

            function c(e) {
                var t = a.createElement("script");
                t.src = e, t.defer = t.type = "text/javascript", a.getElementsByTagName("head")[0].appendChild(t)
            }
            for (o = Array("flag", "emoji"), t.supports = {
                    everything: !0,
                    everythingExceptFlag: !0
                }, r = 0; r < o.length; r++) t.supports[o[r]] = function (e) {
                if (!p || !p.fillText) return !1;
                switch (p.textBaseline = "top", p.font = "600 32px Arial", e) {
                    case "flag":
                        return s([127987, 65039, 8205, 9895, 65039], [127987, 65039, 8203, 9895, 65039]) ? !1 : !s([
                            55356, 56826, 55356, 56819
                        ], [55356, 56826, 8203, 55356, 56819]) && !s([55356, 57332, 56128, 56423, 56128, 56418,
                            56128, 56421, 56128, 56430, 56128, 56423, 56128, 56447
                        ], [55356, 57332, 8203, 56128, 56423, 8203, 56128, 56418, 8203, 56128, 56421, 8203,
                            56128, 56430, 8203, 56128, 56423, 8203, 56128, 56447
                        ]);
                    case "emoji":
                        return !s([55357, 56424, 8205, 55356, 57212], [55357, 56424, 8203, 55356, 57212])
                }
                return !1
            }(o[r]), t.supports.everything = t.supports.everything && t.supports[o[r]], "flag" !== o[r] && (t
                .supports.everythingExceptFlag = t.supports.everythingExceptFlag && t.supports[o[r]]);
            t.supports.everythingExceptFlag = t.supports.everythingExceptFlag && !t.supports.flag, t.DOMReady = !1, t
                .readyCallback = function () {
                    t.DOMReady = !0
                }, t.supports.everything || (n = function () {
                    t.readyCallback()
                }, a.addEventListener ? (a.addEventListener("DOMContentLoaded", n, !1), e.addEventListener("load",
                    n, !1)) : (e.attachEvent("onload", n), a.attachEvent("onreadystatechange", function () {
                    "complete" === a.readyState && t.readyCallback()
                })), (n = t.source || {}).concatemoji ? c(n.concatemoji) : n.wpemoji && n.twemoji && (c(n.twemoji),
                    c(n.wpemoji)))
        }(window, document, window._wpemojiSettings);
    </script>
    <link crossorigin="anonymous" rel='stylesheet' id='google-fonts-style-css'
        href='https://fonts.googleapis.com/css?family=Open+Sans%3A400%2C600%2C700%2C300%7CRoboto%3A400%2C500%2C700%2C300&#038;display=swap&#038;ver=11'
        type='text/css' media='all' />
    <link rel='stylesheet' id='a3a3_lazy_load-css'
        href='//aajkasuvichar.com/wp-content/uploads/sass/a3_lazy_load.min.css?ver=1608802179' type='text/css'
        media='all' />
    <script type='text/javascript' src='https://aajkasuvichar.com/wp-includes/js/jquery/jquery.min.js?ver=3.5.1'
        id='jquery-core-js'></script>
    <script type='text/javascript' src='https://www.googletagmanager.com/gtag/js?id=UA-127456986-1'
        id='google_gtagjs-js' async></script>
    <script type='text/javascript' id='google_gtagjs-js-after'>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('set', 'linker', {
            "domains": ["aajkasuvichar.com"]
        });
        gtag("js", new Date());
        gtag("set", "developer_id.dZTNiMT", true);
        gtag("config", "UA-127456986-1", {
            "anonymize_ip": true
        });
    </script>
    <link rel="https://api.w.org/" href="https://aajkasuvichar.com/wp-json/" />
    <link rel="alternate" type="application/json" href="https://aajkasuvichar.com/wp-json/wp/v2/posts/56" />
    <link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://aajkasuvichar.com/xmlrpc.php?rsd" />
    <link rel="wlwmanifest" type="application/wlwmanifest+xml"
        href="https://aajkasuvichar.com/wp-includes/wlwmanifest.xml" />
    <meta name="generator" content="WordPress 5.7.2" />
    <link rel='shortlink' href='https://aajkasuvichar.com/?p=56' />
    <link rel="alternate" type="application/json+oembed"
        href="https://aajkasuvichar.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Faajkasuvichar.com%2Faaj-ka-suvichar%2F" />
    <link rel="alternate" type="text/xml+oembed"
        href="https://aajkasuvichar.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Faajkasuvichar.com%2Faaj-ka-suvichar%2F&#038;format=xml" />
    <meta name="generator" content="Site Kit by Google 1.35.0" />
    <!--[if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script><![endif]-->
    <script>
        window.tdb_globals = {
            "wpRestNonce": "86771c7fd1",
            "wpRestUrl": "https:\/\/aajkasuvichar.com\/wp-json\/",
            "permalinkStructure": "\/%postname%\/",
            "isAjax": false,
            "isAdminBarShowing": false,
            "autoloadScrollPercent": 20,
            "postAutoloadStatus": "on",
            "origPostEditUrl": null
        };
    </script>
    <script>
        window.tdwGlobal = {
            "adminUrl": "https:\/\/aajkasuvichar.com\/wp-admin\/",
            "wpRestNonce": "86771c7fd1",
            "wpRestUrl": "https:\/\/aajkasuvichar.com\/wp-json\/",
            "permalinkStructure": "\/%postname%\/"
        };
    </script>
    <script>
        window.tdaGlobal = {
            "adminUrl": "https:\/\/aajkasuvichar.com\/wp-admin\/",
            "wpRestNonce": "86771c7fd1",
            "wpRestUrl": "https:\/\/aajkasuvichar.com\/wp-json\/",
            "permalinkStructure": "\/%postname%\/",
            "postId": 56
        };
    </script>
    <link rel="amphtml" href="https://aajkasuvichar.com/aaj-ka-suvichar/?amp">
    <script id="google_gtagjs" src="https://www.googletagmanager.com/gtag/js?id=UA-127456986-1" async="async"
        type="text/javascript"></script>
    <script id="google_gtagjs-inline" type="text/javascript">
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('set', 'linker', {
            "domains": ["aajkasuvichar.com"]
        });
        gtag('js', new Date());
        gtag('config', 'UA-127456986-1', {});
    </script>
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({
            "google_ad_client": "ca-pub-6453827096557789",
            "enable_page_level_ads": true,
            "tag_partner": "site_kit"
        });
    </script>
    <script>
        (function (w, d, s, l, i) {
            w[l] = w[l] || [];
            w[l].push({
                'gtm.start': new Date().getTime(),
                event: 'gtm.js'
            });
            var f = d.getElementsByTagName(s)[0],
                j = d.createElement(s),
                dl = l != 'dataLayer' ? '&l=' + l : '';
            j.async = true;
            j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
            f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer', 'GTM-PHM577N');
    </script>
    <link rel="alternate" type="text/html" media="only screen and (max-width: 640px)"
        href="https://aajkasuvichar.com/aaj-ka-suvichar/?amp">
    <script>
        var tdBlocksArray = []; //here we store all the items for the current page

        //td_block class - each ajax block uses a object of this class for requests
        function tdBlock() {
            this.id = '';
            this.block_type = 1; //block type id (1-234 etc)
            this.atts = '';
            this.td_column_number = '';
            this.td_current_page = 1; //
            this.post_count = 0; //from wp
            this.found_posts = 0; //from wp
            this.max_num_pages = 0; //from wp
            this.td_filter_value = ''; //current live filter value
            this.is_ajax_running = false;
            this.td_user_action = ''; // load more or infinite loader (used by the animation)
            this.header_color = '';
            this.ajax_pagination_infinite_stop = ''; //show load more at page x
        }


        // td_js_generator - mini detector
        (function () {
            var htmlTag = document.getElementsByTagName("html")[0];

            if (navigator.userAgent.indexOf("MSIE 10.0") > -1) {
                htmlTag.className += ' ie10';
            }

            if (!!navigator.userAgent.match(/Trident.*rv\:11\./)) {
                htmlTag.className += ' ie11';
            }

            if (navigator.userAgent.indexOf("Edge") > -1) {
                htmlTag.className += ' ieEdge';
            }

            if (/(iPad|iPhone|iPod)/g.test(navigator.userAgent)) {
                htmlTag.className += ' td-md-is-ios';
            }

            var user_agent = navigator.userAgent.toLowerCase();
            if (user_agent.indexOf("android") > -1) {
                htmlTag.className += ' td-md-is-android';
            }

            if (-1 !== navigator.userAgent.indexOf('Mac OS X')) {
                htmlTag.className += ' td-md-is-os-x';
            }

            if (/chrom(e|ium)/.test(navigator.userAgent.toLowerCase())) {
                htmlTag.className += ' td-md-is-chrome';
            }

            if (-1 !== navigator.userAgent.indexOf('Firefox')) {
                htmlTag.className += ' td-md-is-firefox';
            }

            if (-1 !== navigator.userAgent.indexOf('Safari') && -1 === navigator.userAgent.indexOf('Chrome')) {
                htmlTag.className += ' td-md-is-safari';
            }

            if (-1 !== navigator.userAgent.indexOf('IEMobile')) {
                htmlTag.className += ' td-md-is-iemobile';
            }

        })();




        var tdLocalCache = {};

        (function () {
            "use strict";

            tdLocalCache = {
                data: {},
                remove: function (resource_id) {
                    delete tdLocalCache.data[resource_id];
                },
                exist: function (resource_id) {
                    return tdLocalCache.data.hasOwnProperty(resource_id) && tdLocalCache.data[
                        resource_id] !== null;
                },
                get: function (resource_id) {
                    return tdLocalCache.data[resource_id];
                },
                set: function (resource_id, cachedData) {
                    tdLocalCache.remove(resource_id);
                    tdLocalCache.data[resource_id] = cachedData;
                }
            };
        })();



        var td_viewport_interval_list = [{
            "limitBottom": 767,
            "sidebarWidth": 228
        }, {
            "limitBottom": 1018,
            "sidebarWidth": 300
        }, {
            "limitBottom": 1140,
            "sidebarWidth": 324
        }];
        var td_animation_stack_effect = "type0";
        var tds_animation_stack = true;
        var td_animation_stack_specific_selectors = ".entry-thumb, img, .td-lazy-img";
        var td_animation_stack_general_selectors =
            ".td-animation-stack img, .td-animation-stack .entry-thumb, .post img, .td-animation-stack .td-lazy-img";
        var tds_general_modal_image = "yes";
        var tdc_is_installed = "yes";
        var td_ajax_url = "https:\/\/aajkasuvichar.com\/wp-admin\/admin-ajax.php?td_theme_name=Newspaper&v=11";
        var td_get_template_directory_uri =
            "https:\/\/aajkasuvichar.com\/wp-content\/plugins\/td-composer\/legacy\/common";
        var tds_snap_menu = "snap";
        var tds_logo_on_sticky = "show";
        var tds_header_style = "3";
        var td_please_wait = "Please wait...";
        var td_email_user_pass_incorrect = "User or password incorrect!";
        var td_email_user_incorrect = "Email or username incorrect!";
        var td_email_incorrect = "Email incorrect!";
        var tds_more_articles_on_post_enable = "";
        var tds_more_articles_on_post_time_to_wait = "";
        var tds_more_articles_on_post_pages_distance_from_top = 0;
        var tds_theme_color_site_wide = "#ff6d00";
        var tds_smart_sidebar = "";
        var tdThemeName = "Newspaper";
        var td_magnific_popup_translation_tPrev = "Previous (Left arrow key)";
        var td_magnific_popup_translation_tNext = "Next (Right arrow key)";
        var td_magnific_popup_translation_tCounter = "%curr% of %total%";
        var td_magnific_popup_translation_ajax_tError = "The content from %url% could not be loaded.";
        var td_magnific_popup_translation_image_tError = "The image #%curr% could not be loaded.";
        var tdBlockNonce = "c4259db548";
        var tdDateNamesI18n = {
            "month_names": ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                "October", "November", "December"
            ],
            "month_names_short": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                "Dec"],
            "day_names": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "day_names_short": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        };
        var td_ad_background_click_link = "";
        var td_ad_background_click_target = "";
    </script>
    <style>
        .td-header-wrap .black-menu .sf-menu>.current-menu-item>a,
        .td-header-wrap .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>.current-category-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>li>a:hover,
        .td-header-wrap .black-menu .sf-menu>.sfHover>a,
        .sf-menu>.current-menu-item>a:after,
        .sf-menu>.current-menu-ancestor>a:after,
        .sf-menu>.current-category-ancestor>a:after,
        .sf-menu>li:hover>a:after,
        .sf-menu>.sfHover>a:after,
        .header-search-wrap .td-drop-down-search:after,
        .header-search-wrap .td-drop-down-search .btn:hover,
        input[type=submit]:hover,
        .td-read-more a,
        .td-post-category:hover,
        .td_top_authors .td-active .td-author-post-count,
        .td_top_authors .td-active .td-author-comments-count,
        .td_top_authors .td_mod_wrap:hover .td-author-post-count,
        .td_top_authors .td_mod_wrap:hover .td-author-comments-count,
        .td-404-sub-sub-title a:hover,
        .td-search-form-widget .wpb_button:hover,
        .td-rating-bar-wrap div,
        .dropcap,
        .td_wrapper_video_playlist .td_video_controls_playlist_wrapper,
        .wpb_default,
        .wpb_default:hover,
        .td-left-smart-list:hover,
        .td-right-smart-list:hover,
        #bbpress-forums button:hover,
        .bbp_widget_login .button:hover,
        .td-footer-wrapper .td-post-category,
        .td-footer-wrapper .widget_product_search input[type="submit"]:hover,
        .single-product .product .summary .cart .button:hover,
        .td-next-prev-wrap a:hover,
        .td-load-more-wrap a:hover,
        .td-post-small-box a:hover,
        .page-nav .current,
        .page-nav:first-child>div,
        #bbpress-forums .bbp-pagination .current,
        #bbpress-forums #bbp-single-user-details #bbp-user-navigation li.current a,
        .td-theme-slider:hover .slide-meta-cat a,
        a.vc_btn-black:hover,
        .td-trending-now-wrapper:hover .td-trending-now-title,
        .td-scroll-up,
        .td-smart-list-button:hover,
        .td-weather-information:before,
        .td-weather-week:before,
        .td_block_exchange .td-exchange-header:before,
        .td-pulldown-syle-2 .td-subcat-dropdown ul:after,
        .td_block_template_9 .td-block-title:after,
        .td_block_template_15 .td-block-title:before,
        div.wpforms-container .wpforms-form div.wpforms-submit-container button[type=submit],
        .td-close-video-fixed {
            background-color: #ff6d00;
        }

        .td_block_template_4 .td-related-title .td-cur-simple-item:before {
            border-color: #ff6d00 transparent transparent transparent !important;
        }


        .td_block_template_4 .td-related-title .td-cur-simple-item,
        .td_block_template_3 .td-related-title .td-cur-simple-item,
        .td_block_template_9 .td-related-title:after {
            background-color: #ff6d00;
        }

        a,
        cite a:hover,
        .td-page-content blockquote p,
        .td-post-content blockquote p,
        .mce-content-body blockquote p,
        .comment-content blockquote p,
        .wpb_text_column blockquote p,
        .td_block_text_with_title blockquote p,
        .td_module_wrap:hover .entry-title a,
        .td-subcat-filter .td-subcat-list a:hover,
        .td-subcat-filter .td-subcat-dropdown a:hover,
        .td_quote_on_blocks,
        .dropcap2,
        .dropcap3,
        .td_top_authors .td-active .td-authors-name a,
        .td_top_authors .td_mod_wrap:hover .td-authors-name a,
        .td-post-next-prev-content a:hover,
        .author-box-wrap .td-author-social a:hover,
        .td-author-name a:hover,
        .td-author-url a:hover,
        .comment-reply-link:hover,
        .logged-in-as a:hover,
        #cancel-comment-reply-link:hover,
        .td-search-query,
        .widget a:hover,
        .td_wp_recentcomments a:hover,
        .archive .widget_archive .current,
        .archive .widget_archive .current a,
        .widget_calendar tfoot a:hover,
        #bbpress-forums li.bbp-header .bbp-reply-content span a:hover,
        #bbpress-forums .bbp-forum-freshness a:hover,
        #bbpress-forums .bbp-topic-freshness a:hover,
        #bbpress-forums .bbp-forums-list li a:hover,
        #bbpress-forums .bbp-forum-title:hover,
        #bbpress-forums .bbp-topic-permalink:hover,
        #bbpress-forums .bbp-topic-started-by a:hover,
        #bbpress-forums .bbp-topic-started-in a:hover,
        #bbpress-forums .bbp-body .super-sticky li.bbp-topic-title .bbp-topic-permalink,
        #bbpress-forums .bbp-body .sticky li.bbp-topic-title .bbp-topic-permalink,
        .widget_display_replies .bbp-author-name,
        .widget_display_topics .bbp-author-name,
        .td-subfooter-menu li a:hover,
        a.vc_btn-black:hover,
        .td-smart-list-dropdown-wrap .td-smart-list-button:hover,
        .td-instagram-user a,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-display-option:hover,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-display-option:hover i,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-link:hover,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-item .td-cur-simple-item,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more i,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more i,
        .td_block_template_2 .td-related-title .td-cur-simple-item,
        .td_block_template_5 .td-related-title .td-cur-simple-item,
        .td_block_template_6 .td-related-title .td-cur-simple-item,
        .td_block_template_7 .td-related-title .td-cur-simple-item,
        .td_block_template_8 .td-related-title .td-cur-simple-item,
        .td_block_template_9 .td-related-title .td-cur-simple-item,
        .td_block_template_10 .td-related-title .td-cur-simple-item,
        .td_block_template_11 .td-related-title .td-cur-simple-item,
        .td_block_template_12 .td-related-title .td-cur-simple-item,
        .td_block_template_13 .td-related-title .td-cur-simple-item,
        .td_block_template_14 .td-related-title .td-cur-simple-item,
        .td_block_template_15 .td-related-title .td-cur-simple-item,
        .td_block_template_16 .td-related-title .td-cur-simple-item,
        .td_block_template_17 .td-related-title .td-cur-simple-item,
        .td-theme-wrap .sf-menu ul .td-menu-item>a:hover,
        .td-theme-wrap .sf-menu ul .sfHover>a,
        .td-theme-wrap .sf-menu ul .current-menu-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-category-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-menu-item>a,
        .td_outlined_btn,
        .td_block_categories_tags .td-ct-item:hover {
            color: #ff6d00;
        }

        a.vc_btn-black.vc_btn_square_outlined:hover,
        a.vc_btn-black.vc_btn_outlined:hover {
            color: #ff6d00 !important;
        }

        .td-next-prev-wrap a:hover,
        .td-load-more-wrap a:hover,
        .td-post-small-box a:hover,
        .page-nav .current,
        .page-nav:first-child>div,
        #bbpress-forums .bbp-pagination .current,
        .post .td_quote_box,
        .page .td_quote_box,
        a.vc_btn-black:hover,
        .td_block_template_5 .td-block-title>*,
        .td_outlined_btn {
            border-color: #ff6d00;
        }

        .td_wrapper_video_playlist .td_video_currently_playing:after {
            border-color: #ff6d00 !important;
        }

        .header-search-wrap .td-drop-down-search:before {
            border-color: transparent transparent #ff6d00 transparent;
        }

        .block-title>span,
        .block-title>a,
        .block-title>label,
        .widgettitle,
        .widgettitle:after,
        body .td-trending-now-title,
        .td-trending-now-wrapper:hover .td-trending-now-title,
        .wpb_tabs li.ui-tabs-active a,
        .wpb_tabs li:hover a,
        .vc_tta-container .vc_tta-color-grey.vc_tta-tabs-position-top.vc_tta-style-classic .vc_tta-tabs-container .vc_tta-tab.vc_active>a,
        .vc_tta-container .vc_tta-color-grey.vc_tta-tabs-position-top.vc_tta-style-classic .vc_tta-tabs-container .vc_tta-tab:hover>a,
        .td_block_template_1 .td-related-title .td-cur-simple-item,
        .td-subcat-filter .td-subcat-dropdown:hover .td-subcat-more,
        .td_3D_btn,
        .td_shadow_btn,
        .td_default_btn,
        .td_round_btn,
        .td_outlined_btn:hover {
            background-color: #ff6d00;
        }

        .block-title,
        .td_block_template_1 .td-related-title,
        .wpb_tabs .wpb_tabs_nav,
        .vc_tta-container .vc_tta-color-grey.vc_tta-tabs-position-top.vc_tta-style-classic .vc_tta-tabs-container {
            border-color: #ff6d00;
        }

        .td_block_wrap .td-subcat-item a.td-cur-simple-item {
            color: #ff6d00;
        }



        .td-grid-style-4 .entry-title {
            background-color: rgba(255, 109, 0, 0.7);
        }



        @media (max-width: 767px) {
            body .td-header-wrap .td-header-main-menu {
                background-color: #b5123d !important;
            }
        }



        .td-menu-background:before,
        .td-search-background:before {
            background: rgba(0, 0, 0, 0.5);
            background: -moz-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(0, 0, 0, 0.5)), color-stop(100%, rgba(0, 0, 0, 0.6)));
            background: -webkit-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: -o-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: -ms-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='rgba(0,0,0,0.5)', endColorstr='rgba(0,0,0,0.6)', GradientType=0);
        }


        .td-mobile-content .current-menu-item>a,
        .td-mobile-content .current-menu-ancestor>a,
        .td-mobile-content .current-category-ancestor>a,
        #td-mobile-nav .td-menu-login-section a:hover,
        #td-mobile-nav .td-register-section a:hover,
        #td-mobile-nav .td-menu-socials-wrap a:hover i,
        .td-search-close a:hover i {
            color: #00aae2;
        }


        .white-popup-block:before {
            background-image: url('https://hindilins.com/wp-content/uploads/2021/03/login-mod.jpg');
        }

        .td-header-style-12 .td-header-menu-wrap-full,
        .td-header-style-12 .td-affix,
        .td-grid-style-1.td-hover-1 .td-big-grid-post:hover .td-post-category,
        .td-grid-style-5.td-hover-1 .td-big-grid-post:hover .td-post-category,
        .td_category_template_3 .td-current-sub-category,
        .td_category_template_8 .td-category-header .td-category a.td-current-sub-category,
        .td_category_template_4 .td-category-siblings .td-category a:hover,
        .td_block_big_grid_9.td-grid-style-1 .td-post-category,
        .td_block_big_grid_9.td-grid-style-5 .td-post-category,
        .td-grid-style-6.td-hover-1 .td-module-thumb:after,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>li>a:hover,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.sfHover>a {
            background-color: #ff6d00;
        }

        .td_mega_menu_sub_cats .cur-sub-cat,
        .td-mega-span h3 a:hover,
        .td_mod_mega_menu:hover .entry-title a,
        .header-search-wrap .result-msg a:hover,
        .td-header-top-menu .td-drop-down-search .td_module_wrap:hover .entry-title a,
        .td-header-top-menu .td-icon-search:hover,
        .td-header-wrap .result-msg a:hover,
        .top-header-menu li a:hover,
        .top-header-menu .current-menu-item>a,
        .top-header-menu .current-menu-ancestor>a,
        .top-header-menu .current-category-ancestor>a,
        .td-social-icon-wrap>a:hover,
        .td-header-sp-top-widget .td-social-icon-wrap a:hover,
        .td_mod_related_posts:hover h3>a,
        .td-post-template-11 .td-related-title .td-related-left:hover,
        .td-post-template-11 .td-related-title .td-related-right:hover,
        .td-post-template-11 .td-related-title .td-cur-simple-item,
        .td-post-template-11 .td_block_related_posts .td-next-prev-wrap a:hover,
        .td-category-header .td-pulldown-category-filter-link:hover,
        .td-category-siblings .td-subcat-dropdown a:hover,
        .td-category-siblings .td-subcat-dropdown a.td-current-sub-category,
        .footer-text-wrap .footer-email-wrap a,
        .footer-social-wrap a:hover,
        .td_module_17 .td-read-more a:hover,
        .td_module_18 .td-read-more a:hover,
        .td_module_19 .td-post-author-name a:hover,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more i,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more i,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.sfHover>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>li>a:hover {
            color: #ff6d00;
        }

        .td-mega-menu-page .wpb_content_element ul li a:hover,
        .td-theme-wrap .td-aj-search-results .td_module_wrap:hover .entry-title a,
        .td-theme-wrap .header-search-wrap .result-msg a:hover {
            color: #ff6d00 !important;
        }

        .td_category_template_8 .td-category-header .td-category a.td-current-sub-category,
        .td_category_template_4 .td-category-siblings .td-category a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>li>a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.sfHover>a {
            border-color: #ff6d00;
        }





        .td-header-wrap .td-header-menu-wrap-full,
        .td-header-menu-wrap.td-affix,
        .td-header-style-3 .td-header-main-menu,
        .td-header-style-3 .td-affix .td-header-main-menu,
        .td-header-style-4 .td-header-main-menu,
        .td-header-style-4 .td-affix .td-header-main-menu,
        .td-header-style-8 .td-header-menu-wrap.td-affix,
        .td-header-style-8 .td-header-top-menu-full {
            background-color: #1ac117;
        }

        .td-boxed-layout .td-header-style-3 .td-header-menu-wrap,
        .td-boxed-layout .td-header-style-4 .td-header-menu-wrap,
        .td-header-style-3 .td_stretch_content .td-header-menu-wrap,
        .td-header-style-4 .td_stretch_content .td-header-menu-wrap {
            background-color: #1ac117 !important;
        }

        @media (min-width: 1019px) {

            .td-header-style-1 .td-header-sp-recs,
            .td-header-style-1 .td-header-sp-logo {
                margin-bottom: 28px;
            }
        }

        @media (min-width: 768px) and (max-width: 1018px) {

            .td-header-style-1 .td-header-sp-recs,
            .td-header-style-1 .td-header-sp-logo {
                margin-bottom: 14px;
            }
        }

        .td-header-style-7 .td-header-top-menu {
            border-bottom: none;
        }


        .sf-menu>.current-menu-item>a:after,
        .sf-menu>.current-menu-ancestor>a:after,
        .sf-menu>.current-category-ancestor>a:after,
        .sf-menu>li:hover>a:after,
        .sf-menu>.sfHover>a:after,
        .td_block_mega_menu .td-next-prev-wrap a:hover,
        .td-mega-span .td-post-category:hover,
        .td-header-wrap .black-menu .sf-menu>li>a:hover,
        .td-header-wrap .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>.sfHover>a,
        .td-header-wrap .black-menu .sf-menu>.current-menu-item>a,
        .td-header-wrap .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>li>a:hover,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.sfHover>a {
            background-color: #b5123d;
        }

        .td_block_mega_menu .td-next-prev-wrap a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>li>a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.sfHover>a {
            border-color: #b5123d;
        }

        .header-search-wrap .td-drop-down-search:before {
            border-color: transparent transparent #b5123d transparent;
        }

        .td_mega_menu_sub_cats .cur-sub-cat,
        .td_mod_mega_menu:hover .entry-title a,
        .td-theme-wrap .sf-menu ul .td-menu-item>a:hover,
        .td-theme-wrap .sf-menu ul .sfHover>a,
        .td-theme-wrap .sf-menu ul .current-menu-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-category-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>li>a:hover,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.sfHover>a {
            color: #b5123d;
        }



        .td-header-menu-wrap.td-affix,
        .td-header-style-3 .td-affix .td-header-main-menu,
        .td-header-style-4 .td-affix .td-header-main-menu,
        .td-header-style-8 .td-header-menu-wrap.td-affix {
            background-color: #1ac117;
        }



        .td-affix .sf-menu>.current-menu-item>a:after,
        .td-affix .sf-menu>.current-menu-ancestor>a:after,
        .td-affix .sf-menu>.current-category-ancestor>a:after,
        .td-affix .sf-menu>li:hover>a:after,
        .td-affix .sf-menu>.sfHover>a:after,
        .td-header-wrap .td-affix .black-menu .sf-menu>li>a:hover,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .td-affix .black-menu .sf-menu>.sfHover>a,
        .td-affix .header-search-wrap .td-drop-down-search:after,
        .td-affix .header-search-wrap .td-drop-down-search .btn:hover,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-menu-item>a,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>li>a:hover,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.sfHover>a {
            background-color: #b5123d;
        }

        .td-affix .header-search-wrap .td-drop-down-search:before {
            border-color: transparent transparent #b5123d transparent;
        }

        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>li>a:hover,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.sfHover>a {
            border-color: #b5123d;
        }

        .td-theme-wrap .td-affix .sf-menu ul .td-menu-item>a:hover,
        .td-theme-wrap .td-affix .sf-menu ul .sfHover>a,
        .td-theme-wrap .td-affix .sf-menu ul .current-menu-ancestor>a,
        .td-theme-wrap .td-affix .sf-menu ul .current-category-ancestor>a,
        .td-theme-wrap .td-affix .sf-menu ul .current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>li>a:hover,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.sfHover>a {
            color: #b5123d;
        }

        .td-header-wrap .td-header-menu-social .td-social-icon-wrap a {
            color: #ffffff;
        }

        .td-footer-wrapper,
        .td-footer-wrapper .td_block_template_7 .td-block-title>*,
        .td-footer-wrapper .td_block_template_17 .td-block-title,
        .td-footer-wrapper .td-block-title-wrap .td-wrapper-pulldown-filter {
            background-color: #333333;
        }


        .td-footer-wrapper::before {
            background-repeat: repeat-x;
        }

        .td-header-wrap .black-menu .sf-menu>.current-menu-item>a,
        .td-header-wrap .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>.current-category-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>li>a:hover,
        .td-header-wrap .black-menu .sf-menu>.sfHover>a,
        .sf-menu>.current-menu-item>a:after,
        .sf-menu>.current-menu-ancestor>a:after,
        .sf-menu>.current-category-ancestor>a:after,
        .sf-menu>li:hover>a:after,
        .sf-menu>.sfHover>a:after,
        .header-search-wrap .td-drop-down-search:after,
        .header-search-wrap .td-drop-down-search .btn:hover,
        input[type=submit]:hover,
        .td-read-more a,
        .td-post-category:hover,
        .td_top_authors .td-active .td-author-post-count,
        .td_top_authors .td-active .td-author-comments-count,
        .td_top_authors .td_mod_wrap:hover .td-author-post-count,
        .td_top_authors .td_mod_wrap:hover .td-author-comments-count,
        .td-404-sub-sub-title a:hover,
        .td-search-form-widget .wpb_button:hover,
        .td-rating-bar-wrap div,
        .dropcap,
        .td_wrapper_video_playlist .td_video_controls_playlist_wrapper,
        .wpb_default,
        .wpb_default:hover,
        .td-left-smart-list:hover,
        .td-right-smart-list:hover,
        #bbpress-forums button:hover,
        .bbp_widget_login .button:hover,
        .td-footer-wrapper .td-post-category,
        .td-footer-wrapper .widget_product_search input[type="submit"]:hover,
        .single-product .product .summary .cart .button:hover,
        .td-next-prev-wrap a:hover,
        .td-load-more-wrap a:hover,
        .td-post-small-box a:hover,
        .page-nav .current,
        .page-nav:first-child>div,
        #bbpress-forums .bbp-pagination .current,
        #bbpress-forums #bbp-single-user-details #bbp-user-navigation li.current a,
        .td-theme-slider:hover .slide-meta-cat a,
        a.vc_btn-black:hover,
        .td-trending-now-wrapper:hover .td-trending-now-title,
        .td-scroll-up,
        .td-smart-list-button:hover,
        .td-weather-information:before,
        .td-weather-week:before,
        .td_block_exchange .td-exchange-header:before,
        .td-pulldown-syle-2 .td-subcat-dropdown ul:after,
        .td_block_template_9 .td-block-title:after,
        .td_block_template_15 .td-block-title:before,
        div.wpforms-container .wpforms-form div.wpforms-submit-container button[type=submit],
        .td-close-video-fixed {
            background-color: #ff6d00;
        }

        .td_block_template_4 .td-related-title .td-cur-simple-item:before {
            border-color: #ff6d00 transparent transparent transparent !important;
        }


        .td_block_template_4 .td-related-title .td-cur-simple-item,
        .td_block_template_3 .td-related-title .td-cur-simple-item,
        .td_block_template_9 .td-related-title:after {
            background-color: #ff6d00;
        }

        a,
        cite a:hover,
        .td-page-content blockquote p,
        .td-post-content blockquote p,
        .mce-content-body blockquote p,
        .comment-content blockquote p,
        .wpb_text_column blockquote p,
        .td_block_text_with_title blockquote p,
        .td_module_wrap:hover .entry-title a,
        .td-subcat-filter .td-subcat-list a:hover,
        .td-subcat-filter .td-subcat-dropdown a:hover,
        .td_quote_on_blocks,
        .dropcap2,
        .dropcap3,
        .td_top_authors .td-active .td-authors-name a,
        .td_top_authors .td_mod_wrap:hover .td-authors-name a,
        .td-post-next-prev-content a:hover,
        .author-box-wrap .td-author-social a:hover,
        .td-author-name a:hover,
        .td-author-url a:hover,
        .comment-reply-link:hover,
        .logged-in-as a:hover,
        #cancel-comment-reply-link:hover,
        .td-search-query,
        .widget a:hover,
        .td_wp_recentcomments a:hover,
        .archive .widget_archive .current,
        .archive .widget_archive .current a,
        .widget_calendar tfoot a:hover,
        #bbpress-forums li.bbp-header .bbp-reply-content span a:hover,
        #bbpress-forums .bbp-forum-freshness a:hover,
        #bbpress-forums .bbp-topic-freshness a:hover,
        #bbpress-forums .bbp-forums-list li a:hover,
        #bbpress-forums .bbp-forum-title:hover,
        #bbpress-forums .bbp-topic-permalink:hover,
        #bbpress-forums .bbp-topic-started-by a:hover,
        #bbpress-forums .bbp-topic-started-in a:hover,
        #bbpress-forums .bbp-body .super-sticky li.bbp-topic-title .bbp-topic-permalink,
        #bbpress-forums .bbp-body .sticky li.bbp-topic-title .bbp-topic-permalink,
        .widget_display_replies .bbp-author-name,
        .widget_display_topics .bbp-author-name,
        .td-subfooter-menu li a:hover,
        a.vc_btn-black:hover,
        .td-smart-list-dropdown-wrap .td-smart-list-button:hover,
        .td-instagram-user a,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-display-option:hover,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-display-option:hover i,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-link:hover,
        .td-block-title-wrap .td-wrapper-pulldown-filter .td-pulldown-filter-item .td-cur-simple-item,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more i,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more i,
        .td_block_template_2 .td-related-title .td-cur-simple-item,
        .td_block_template_5 .td-related-title .td-cur-simple-item,
        .td_block_template_6 .td-related-title .td-cur-simple-item,
        .td_block_template_7 .td-related-title .td-cur-simple-item,
        .td_block_template_8 .td-related-title .td-cur-simple-item,
        .td_block_template_9 .td-related-title .td-cur-simple-item,
        .td_block_template_10 .td-related-title .td-cur-simple-item,
        .td_block_template_11 .td-related-title .td-cur-simple-item,
        .td_block_template_12 .td-related-title .td-cur-simple-item,
        .td_block_template_13 .td-related-title .td-cur-simple-item,
        .td_block_template_14 .td-related-title .td-cur-simple-item,
        .td_block_template_15 .td-related-title .td-cur-simple-item,
        .td_block_template_16 .td-related-title .td-cur-simple-item,
        .td_block_template_17 .td-related-title .td-cur-simple-item,
        .td-theme-wrap .sf-menu ul .td-menu-item>a:hover,
        .td-theme-wrap .sf-menu ul .sfHover>a,
        .td-theme-wrap .sf-menu ul .current-menu-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-category-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-menu-item>a,
        .td_outlined_btn,
        .td_block_categories_tags .td-ct-item:hover {
            color: #ff6d00;
        }

        a.vc_btn-black.vc_btn_square_outlined:hover,
        a.vc_btn-black.vc_btn_outlined:hover {
            color: #ff6d00 !important;
        }

        .td-next-prev-wrap a:hover,
        .td-load-more-wrap a:hover,
        .td-post-small-box a:hover,
        .page-nav .current,
        .page-nav:first-child>div,
        #bbpress-forums .bbp-pagination .current,
        .post .td_quote_box,
        .page .td_quote_box,
        a.vc_btn-black:hover,
        .td_block_template_5 .td-block-title>*,
        .td_outlined_btn {
            border-color: #ff6d00;
        }

        .td_wrapper_video_playlist .td_video_currently_playing:after {
            border-color: #ff6d00 !important;
        }

        .header-search-wrap .td-drop-down-search:before {
            border-color: transparent transparent #ff6d00 transparent;
        }

        .block-title>span,
        .block-title>a,
        .block-title>label,
        .widgettitle,
        .widgettitle:after,
        body .td-trending-now-title,
        .td-trending-now-wrapper:hover .td-trending-now-title,
        .wpb_tabs li.ui-tabs-active a,
        .wpb_tabs li:hover a,
        .vc_tta-container .vc_tta-color-grey.vc_tta-tabs-position-top.vc_tta-style-classic .vc_tta-tabs-container .vc_tta-tab.vc_active>a,
        .vc_tta-container .vc_tta-color-grey.vc_tta-tabs-position-top.vc_tta-style-classic .vc_tta-tabs-container .vc_tta-tab:hover>a,
        .td_block_template_1 .td-related-title .td-cur-simple-item,
        .td-subcat-filter .td-subcat-dropdown:hover .td-subcat-more,
        .td_3D_btn,
        .td_shadow_btn,
        .td_default_btn,
        .td_round_btn,
        .td_outlined_btn:hover {
            background-color: #ff6d00;
        }

        .block-title,
        .td_block_template_1 .td-related-title,
        .wpb_tabs .wpb_tabs_nav,
        .vc_tta-container .vc_tta-color-grey.vc_tta-tabs-position-top.vc_tta-style-classic .vc_tta-tabs-container {
            border-color: #ff6d00;
        }

        .td_block_wrap .td-subcat-item a.td-cur-simple-item {
            color: #ff6d00;
        }



        .td-grid-style-4 .entry-title {
            background-color: rgba(255, 109, 0, 0.7);
        }



        @media (max-width: 767px) {
            body .td-header-wrap .td-header-main-menu {
                background-color: #b5123d !important;
            }
        }



        .td-menu-background:before,
        .td-search-background:before {
            background: rgba(0, 0, 0, 0.5);
            background: -moz-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(0, 0, 0, 0.5)), color-stop(100%, rgba(0, 0, 0, 0.6)));
            background: -webkit-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: -o-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: -ms-linear-gradient(top, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.6) 100%);
            filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='rgba(0,0,0,0.5)', endColorstr='rgba(0,0,0,0.6)', GradientType=0);
        }


        .td-mobile-content .current-menu-item>a,
        .td-mobile-content .current-menu-ancestor>a,
        .td-mobile-content .current-category-ancestor>a,
        #td-mobile-nav .td-menu-login-section a:hover,
        #td-mobile-nav .td-register-section a:hover,
        #td-mobile-nav .td-menu-socials-wrap a:hover i,
        .td-search-close a:hover i {
            color: #00aae2;
        }


        .white-popup-block:before {
            background-image: url('https://hindilins.com/wp-content/uploads/2021/03/login-mod.jpg');
        }

        .td-header-style-12 .td-header-menu-wrap-full,
        .td-header-style-12 .td-affix,
        .td-grid-style-1.td-hover-1 .td-big-grid-post:hover .td-post-category,
        .td-grid-style-5.td-hover-1 .td-big-grid-post:hover .td-post-category,
        .td_category_template_3 .td-current-sub-category,
        .td_category_template_8 .td-category-header .td-category a.td-current-sub-category,
        .td_category_template_4 .td-category-siblings .td-category a:hover,
        .td_block_big_grid_9.td-grid-style-1 .td-post-category,
        .td_block_big_grid_9.td-grid-style-5 .td-post-category,
        .td-grid-style-6.td-hover-1 .td-module-thumb:after,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>li>a:hover,
        .tdm-menu-active-style5 .td-header-menu-wrap .sf-menu>.sfHover>a {
            background-color: #ff6d00;
        }

        .td_mega_menu_sub_cats .cur-sub-cat,
        .td-mega-span h3 a:hover,
        .td_mod_mega_menu:hover .entry-title a,
        .header-search-wrap .result-msg a:hover,
        .td-header-top-menu .td-drop-down-search .td_module_wrap:hover .entry-title a,
        .td-header-top-menu .td-icon-search:hover,
        .td-header-wrap .result-msg a:hover,
        .top-header-menu li a:hover,
        .top-header-menu .current-menu-item>a,
        .top-header-menu .current-menu-ancestor>a,
        .top-header-menu .current-category-ancestor>a,
        .td-social-icon-wrap>a:hover,
        .td-header-sp-top-widget .td-social-icon-wrap a:hover,
        .td_mod_related_posts:hover h3>a,
        .td-post-template-11 .td-related-title .td-related-left:hover,
        .td-post-template-11 .td-related-title .td-related-right:hover,
        .td-post-template-11 .td-related-title .td-cur-simple-item,
        .td-post-template-11 .td_block_related_posts .td-next-prev-wrap a:hover,
        .td-category-header .td-pulldown-category-filter-link:hover,
        .td-category-siblings .td-subcat-dropdown a:hover,
        .td-category-siblings .td-subcat-dropdown a.td-current-sub-category,
        .footer-text-wrap .footer-email-wrap a,
        .footer-social-wrap a:hover,
        .td_module_17 .td-read-more a:hover,
        .td_module_18 .td-read-more a:hover,
        .td_module_19 .td-post-author-name a:hover,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-2 .td-subcat-dropdown:hover .td-subcat-more i,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more span,
        .td-pulldown-syle-3 .td-subcat-dropdown:hover .td-subcat-more i,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.sfHover>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>li>a:hover {
            color: #ff6d00;
        }

        .td-mega-menu-page .wpb_content_element ul li a:hover,
        .td-theme-wrap .td-aj-search-results .td_module_wrap:hover .entry-title a,
        .td-theme-wrap .header-search-wrap .result-msg a:hover {
            color: #ff6d00 !important;
        }

        .td_category_template_8 .td-category-header .td-category a.td-current-sub-category,
        .td_category_template_4 .td-category-siblings .td-category a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>li>a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.sfHover>a {
            border-color: #ff6d00;
        }





        .td-header-wrap .td-header-menu-wrap-full,
        .td-header-menu-wrap.td-affix,
        .td-header-style-3 .td-header-main-menu,
        .td-header-style-3 .td-affix .td-header-main-menu,
        .td-header-style-4 .td-header-main-menu,
        .td-header-style-4 .td-affix .td-header-main-menu,
        .td-header-style-8 .td-header-menu-wrap.td-affix,
        .td-header-style-8 .td-header-top-menu-full {
            background-color: #1ac117;
        }

        .td-boxed-layout .td-header-style-3 .td-header-menu-wrap,
        .td-boxed-layout .td-header-style-4 .td-header-menu-wrap,
        .td-header-style-3 .td_stretch_content .td-header-menu-wrap,
        .td-header-style-4 .td_stretch_content .td-header-menu-wrap {
            background-color: #1ac117 !important;
        }

        @media (min-width: 1019px) {

            .td-header-style-1 .td-header-sp-recs,
            .td-header-style-1 .td-header-sp-logo {
                margin-bottom: 28px;
            }
        }

        @media (min-width: 768px) and (max-width: 1018px) {

            .td-header-style-1 .td-header-sp-recs,
            .td-header-style-1 .td-header-sp-logo {
                margin-bottom: 14px;
            }
        }

        .td-header-style-7 .td-header-top-menu {
            border-bottom: none;
        }


        .sf-menu>.current-menu-item>a:after,
        .sf-menu>.current-menu-ancestor>a:after,
        .sf-menu>.current-category-ancestor>a:after,
        .sf-menu>li:hover>a:after,
        .sf-menu>.sfHover>a:after,
        .td_block_mega_menu .td-next-prev-wrap a:hover,
        .td-mega-span .td-post-category:hover,
        .td-header-wrap .black-menu .sf-menu>li>a:hover,
        .td-header-wrap .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>.sfHover>a,
        .td-header-wrap .black-menu .sf-menu>.current-menu-item>a,
        .td-header-wrap .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .black-menu .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>li>a:hover,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap .sf-menu>.sfHover>a {
            background-color: #b5123d;
        }

        .td_block_mega_menu .td-next-prev-wrap a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .sf-menu>li>a:hover,
        .tdm-menu-active-style4 .tdm-header .sf-menu>.sfHover>a {
            border-color: #b5123d;
        }

        .header-search-wrap .td-drop-down-search:before {
            border-color: transparent transparent #b5123d transparent;
        }

        .td_mega_menu_sub_cats .cur-sub-cat,
        .td_mod_mega_menu:hover .entry-title a,
        .td-theme-wrap .sf-menu ul .td-menu-item>a:hover,
        .td-theme-wrap .sf-menu ul .sfHover>a,
        .td-theme-wrap .sf-menu ul .current-menu-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-category-ancestor>a,
        .td-theme-wrap .sf-menu ul .current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>li>a:hover,
        .tdm-menu-active-style3 .tdm-header.td-header-wrap .sf-menu>.sfHover>a {
            color: #b5123d;
        }



        .td-header-menu-wrap.td-affix,
        .td-header-style-3 .td-affix .td-header-main-menu,
        .td-header-style-4 .td-affix .td-header-main-menu,
        .td-header-style-8 .td-header-menu-wrap.td-affix {
            background-color: #1ac117;
        }



        .td-affix .sf-menu>.current-menu-item>a:after,
        .td-affix .sf-menu>.current-menu-ancestor>a:after,
        .td-affix .sf-menu>.current-category-ancestor>a:after,
        .td-affix .sf-menu>li:hover>a:after,
        .td-affix .sf-menu>.sfHover>a:after,
        .td-header-wrap .td-affix .black-menu .sf-menu>li>a:hover,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .td-affix .black-menu .sf-menu>.sfHover>a,
        .td-affix .header-search-wrap .td-drop-down-search:after,
        .td-affix .header-search-wrap .td-drop-down-search .btn:hover,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-menu-item>a,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-menu-ancestor>a,
        .td-header-wrap .td-affix .black-menu .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>li>a:hover,
        .tdm-menu-active-style5 .tdm-header .td-header-menu-wrap.td-affix .sf-menu>.sfHover>a {
            background-color: #b5123d;
        }

        .td-affix .header-search-wrap .td-drop-down-search:before {
            border-color: transparent transparent #b5123d transparent;
        }

        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>li>a:hover,
        .tdm-menu-active-style4 .tdm-header .td-affix .sf-menu>.sfHover>a {
            border-color: #b5123d;
        }

        .td-theme-wrap .td-affix .sf-menu ul .td-menu-item>a:hover,
        .td-theme-wrap .td-affix .sf-menu ul .sfHover>a,
        .td-theme-wrap .td-affix .sf-menu ul .current-menu-ancestor>a,
        .td-theme-wrap .td-affix .sf-menu ul .current-category-ancestor>a,
        .td-theme-wrap .td-affix .sf-menu ul .current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.current-menu-item>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.current-menu-ancestor>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.current-category-ancestor>a,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>li>a:hover,
        .tdm-menu-active-style3 .tdm-header .td-affix .sf-menu>.sfHover>a {
            color: #b5123d;
        }

        .td-header-wrap .td-header-menu-social .td-social-icon-wrap a {
            color: #ffffff;
        }

        .td-footer-wrapper,
        .td-footer-wrapper .td_block_template_7 .td-block-title>*,
        .td-footer-wrapper .td_block_template_17 .td-block-title,
        .td-footer-wrapper .td-block-title-wrap .td-wrapper-pulldown-filter {
            background-color: #333333;
        }


        .td-footer-wrapper::before {
            background-repeat: repeat-x;
        }
    </style>
    <script type="application/ld+json">
        {
            "@context": "http://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [{
                    "@type": "ListItem",
                    "position": 1,
                    "item": {
                        "@type": "WebSite",
                        "@id": "https://aajkasuvichar.com/",
                        "name": "Home"
                    }
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "item": {
                        "@type": "WebPage",
                        "@id": "https://aajkasuvichar.com/hindi-quotes/",
                        "name": "Hindi Quotes"
                    }
                }, {
                    "@type": "ListItem",
                    "position": 3,
                    "item": {
                        "@type": "WebPage",
                        "@id": "https://aajkasuvichar.com/aaj-ka-suvichar/",
                        "name": "Aaj Ka Suvichar 2021 |आज का सुविचार"
                    }
                }
            ]
        }
    </script>
</head>

<body
    class="post-template-default single single-post postid-56 single-format-standard td-standard-pack aaj-ka-suvichar global-block-template-8 single_template_1 td-animation-stack-type0 td-full-layout"
    itemscope="itemscope" itemtype="https://schema.org/WebPage">
    <div class="td-scroll-up  td-hide-scroll-up-on-mob" style="display:none;"><i class="td-icon-menu-up"></i></div>
    <div class="td-menu-background"></div>
    <div id="td-mobile-nav">
        <div class="td-mobile-container">
            <div class="td-menu-socials-wrap">
                <div class="td-menu-socials"> <span class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                            href="https://www.facebook.com/SuvicharHindiMe" title="Facebook"> <i
                                class="td-icon-font td-icon-facebook"></i> </a> </span> <span
                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                            href="https://www.instagram.com/suvicharhindime/" title="Instagram"> <i
                                class="td-icon-font td-icon-instagram"></i> </a> </span> <span
                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                            href="https://mix.com/aajkasuvichar" title="Mix"> <i
                                class="td-icon-font td-icon-stumbleupon"></i> </a> </span> <span
                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                            href="https://in.pinterest.com/AajKaSuvichar" title="Pinterest"> <i
                                class="td-icon-font td-icon-pinterest"></i> </a> </span> <span
                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow" href="https://t.me/AajKaSuvichar"
                            title="Telegram"> <i class="td-icon-font td-icon-telegram"></i> </a> </span> <span
                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                            href="https://twitter.com/suvicharhindime" title="Twitter"> <i
                                class="td-icon-font td-icon-twitter"></i> </a> </span></div>
                <div class="td-mobile-close"> <a href="#" aria-label="Close"><i class="td-icon-close-mobile"></i></a>
                </div>
            </div>
            <div class="td-mobile-content">
                <div class="menu-main-menu-container">
                    <ul id="menu-main-menu" class="td-mobile-main-menu">
                        <li id="menu-item-1500"
                            class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-first menu-item-1500">
                            <a href="https://aajkasuvichar.com/">Home</a></li>
                        <li id="menu-item-1492"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-1492">
                            <a href="https://aajkasuvichar.com/hindi-quotes/">Hindi Quotes</a></li>
                        <li id="menu-item-1495"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1495"><a
                                href="https://aajkasuvichar.com/wishes/">Wishes</a></li>
                        <li id="menu-item-1493"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1493"><a
                                href="https://aajkasuvichar.com/hindi-story/">Hindi Story</a></li>
                        <li id="menu-item-1494"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1494"><a
                                href="https://aajkasuvichar.com/knowledge/">Knowledge</a></li>
                        <li id="menu-item-1496"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1496"><a
                                href="https://aajkasuvichar.com/jokes/">Jokes</a></li>
                        <li id="menu-item-1498"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1498"><a
                                href="https://aajkasuvichar.com/hindi-poem/">Hindi Poem</a></li>
                        <li id="menu-item-1601"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1601"><a
                                href="https://aajkasuvichar.com/hindi-biography/">Hindi Biography</a></li>
                        <li id="menu-item-1499"
                            class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1499"><a
                                href="https://aajkasuvichar.com/health-tips/">Health Tips</a></li>
                        <li id="menu-item-1534"
                            class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1534">
                            <a href="#">More<i class="td-icon-menu-right td-element-after"></i></a>
                            <ul class="sub-menu">
                                <li id="menu-item-1497"
                                    class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1497">
                                    <a href="https://aajkasuvichar.com/chanakya-niti-in-hindi/">Chanakya Niti in
                                        Hindi</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <div class="td-search-background"></div>
    <div class="td-search-wrap-mob">
        <div class="td-drop-down-search">
            <form method="get" class="td-search-form" action="https://aajkasuvichar.com/">
                <div class="td-search-close"> <a href="#"><i class="td-icon-close-mobile"></i></a></div>
                <div role="search" class="td-search-input"> <span>Search</span> <input id="td-header-search-mob"
                        type="text" value="" name="s" autocomplete="off" /></div>
            </form>
            <div id="td-aj-search-mob" class="td-ajax-search-flex"></div>
        </div>
    </div>
    <div id="td-outer-wrap" class="td-theme-wrap">
        <div class="tdc-header-wrap ">
            <div class="td-header-wrap td-header-style-3 ">
                <div class="td-header-top-menu-full td-container-wrap td_stretch_content">
                    <div class="td-container td-header-row td-header-top-menu">
                        <div id="login-form" class="white-popup-block mfp-hide mfp-with-anim">
                            <div class="td-login-wrap"> <a href="#" aria-label="Back" class="td-back-button"><i
                                        class="td-icon-modal-back"></i></a>
                                <div id="td-login-div" class="td-login-form-div td-display-block">
                                    <div class="td-login-panel-title">Sign in</div>
                                    <div class="td-login-panel-descr">Welcome! Log into your account</div>
                                    <div class="td_display_err"></div>
                                    <form action="#" method="post">
                                        <div class="td-login-inputs"><input class="td-login-input"
                                                autocomplete="username" type="text" name="login_email" id="login_email"
                                                value="" required><label for="login_email">your username</label></div>
                                        <div class="td-login-inputs"><input class="td-login-input"
                                                autocomplete="current-password" type="password" name="login_pass"
                                                id="login_pass" value="" required><label for="login_pass">your
                                                password</label></div> <input type="button" name="login_button"
                                            id="login_button" class="wpb_button btn td-login-button" value="Login">
                                    </form>
                                    <div class="td-login-info-text"><a href="#" id="forgot-pass-link">Forgot your
                                            password? Get help</a></div>
                                    <div class="td-login-info-text"><a class="privacy-policy-link"
                                            href="https://aajkasuvichar.com/privacy-policy-2/">Privacy Policy</a></div>
                                </div>
                                <div id="td-forgot-pass-div" class="td-login-form-div td-display-none">
                                    <div class="td-login-panel-title">Password recovery</div>
                                    <div class="td-login-panel-descr">Recover your password</div>
                                    <div class="td_display_err"></div>
                                    <div class="td-login-inputs"><input class="td-login-input" type="text"
                                            name="forgot_email" id="forgot_email" value="" required><label
                                            for="forgot_email">your email</label></div> <input type="button"
                                        name="forgot_button" id="forgot_button" class="wpb_button btn td-login-button"
                                        value="Send My Password">
                                    <div class="td-login-info-text">A password will be e-mailed to you.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="td-banner-wrap-full td-container-wrap ">
                    <div class="td-container td-header-row td-header-header">
                        <div class="td-header-sp-logo"> <a class="td-main-logo" href="https://aajkasuvichar.com/">
                                <noscript><img class="td-retina-data"
                                        data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                        src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                        alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar" width="554"
                                        height="116" /></noscript><img class="lazyload td-retina-data"
                                    data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                    src='https://cdn.shortpixel.ai/client/q_lqip,ret_wait,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png'
                                    data-src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                    alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar" width="554" height="116" /> <span
                                    class="td-visual-hidden">Aaj Ka Suvichar</span> </a></div>
                    </div>
                </div>
                <div class="td-header-menu-wrap-full td-container-wrap td_stretch_content">
                    <div class="td-header-menu-wrap ">
                        <div class="td-container td-header-row td-header-main-menu black-menu">
                            <div id="td-header-menu" role="navigation">
                                <div id="td-top-mobile-toggle"><a href="#"><i
                                            class="td-icon-font td-icon-mobile"></i></a></div>
                                <div class="td-main-menu-logo td-logo-in-header"> <a
                                        class="td-mobile-logo td-sticky-mobile" href="https://aajkasuvichar.com/">
                                        <noscript><img class="td-retina-data"
                                                data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                                src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                                alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar" width="554"
                                                height="116" /></noscript><img class="lazyload td-retina-data"
                                            data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                            src='https://cdn.shortpixel.ai/client/q_lqip,ret_wait,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png'
                                            data-src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                            alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar" width="554" height="116" />
                                    </a> <a class="td-header-logo td-sticky-mobile" href="https://aajkasuvichar.com/">
                                        <noscript><img class="td-retina-data"
                                                data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                                src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                                alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar" width="554"
                                                height="116" /></noscript><img class="lazyload td-retina-data"
                                            data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                            src='https://cdn.shortpixel.ai/client/q_lqip,ret_wait,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png'
                                            data-src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554,h_116/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                            alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar" width="554" height="116" />
                                    </a></div>
                                <div class="menu-main-menu-container">
                                    <ul id="menu-main-menu-1" class="sf-menu">
                                        <li
                                            class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-first td-menu-item td-normal-menu menu-item-1500">
                                            <a href="https://aajkasuvichar.com/">Home</a></li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent td-menu-item td-mega-menu menu-item-1492">
                                            <a href="https://aajkasuvichar.com/hindi-quotes/">Hindi Quotes</a>
                                            <ul class="sub-menu">
                                                <li id="menu-item-0" class="menu-item-0">
                                                    <div class="td-container-border">
                                                        <div class="td-mega-grid">
                                                            <div class="td_block_wrap td_block_mega_menu tdi_1 td-no-subcats td_with_ajax_pagination td-pb-border-top td_block_template_8"
                                                                data-td-block-uid="tdi_1">
                                                                <script>
                                                                    var block_tdi_1 = new tdBlock();
                                                                    block_tdi_1.id = "tdi_1";
                                                                    block_tdi_1.atts =
                                                                        '{"limit":"5","td_column_number":3,"ajax_pagination":"next_prev","category_id":"36","show_child_cat":30,"td_ajax_filter_type":"td_category_ids_filter","td_ajax_preloading":"","block_type":"td_block_mega_menu","block_template_id":"","header_color":"","ajax_pagination_infinite_stop":"","offset":"","td_filter_default_txt":"","td_ajax_filter_ids":"","el_class":"","color_preset":"","border_top":"","css":"","tdc_css":"","class":"tdi_1","tdc_css_class":"tdi_1","tdc_css_class_style":"tdi_1_rand_style"}';
                                                                    block_tdi_1.td_column_number = "3";
                                                                    block_tdi_1.block_type = "td_block_mega_menu";
                                                                    block_tdi_1.post_count = "5";
                                                                    block_tdi_1.found_posts = "22";
                                                                    block_tdi_1.header_color = "";
                                                                    block_tdi_1.ajax_pagination_infinite_stop = "";
                                                                    block_tdi_1.max_num_pages = "5";
                                                                    tdBlocksArray.push(block_tdi_1);
                                                                </script>
                                                                <div id=tdi_1 class="td_block_inner">
                                                                    <div class="td-mega-row">
                                                                        <div class="td-mega-span">
                                                                            <div
                                                                                class="td_module_mega_menu td-animation-stack td_mod_mega_menu">
                                                                                <div class="td-module-image">
                                                                                    <div class="td-module-thumb"><a
                                                                                            href="https://aajkasuvichar.com/dhirubhai-ambani-quotes-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            class="td-image-wrap "
                                                                                            title="Dhirubhai Ambani Quotes in Hindi | धीरूभाई अंबानी के अनमोल विचार"><img
                                                                                                class="entry-thumb"
                                                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                                                alt="Dhirubhai Ambani Quotes in Hindi"
                                                                                                title="Dhirubhai Ambani Quotes in Hindi | धीरूभाई अंबानी के अनमोल विचार"
                                                                                                data-type="image_tag"
                                                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2021/01/dhirubhai-ambani-quotes-in-hindi.jpg"
                                                                                                width="218"
                                                                                                height="122" /></a>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="item-details">
                                                                                    <h3
                                                                                        class="entry-title td-module-title">
                                                                                        <a href="https://aajkasuvichar.com/dhirubhai-ambani-quotes-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            title="Dhirubhai Ambani Quotes in Hindi | धीरूभाई अंबानी के अनमोल विचार">Dhirubhai
                                                                                            Ambani Quotes in Hindi |
                                                                                            धीरूभाई अंबानी के अनमोल
                                                                                            विचार</a></h3>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="td-mega-span">
                                                                            <div
                                                                                class="td_module_mega_menu td-animation-stack td_mod_mega_menu">
                                                                                <div class="td-module-image">
                                                                                    <div class="td-module-thumb"><a
                                                                                            href="https://aajkasuvichar.com/shaheed-bhagat-singh-quotes-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            class="td-image-wrap "
                                                                                            title="Shaheed Bhagat Singh Quotes in Hindi |शहीद भगत सिंह के क्रांतिकारी विचार"><img
                                                                                                class="entry-thumb"
                                                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                                                alt="Shaheed Bhagat Singh Quotes in Hindi"
                                                                                                title="Shaheed Bhagat Singh Quotes in Hindi |शहीद भगत सिंह के क्रांतिकारी विचार"
                                                                                                data-type="image_tag"
                                                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/09/Sheed-Bhagat-Singh.jpg"
                                                                                                width="218"
                                                                                                height="121" /></a>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="item-details">
                                                                                    <h3
                                                                                        class="entry-title td-module-title">
                                                                                        <a href="https://aajkasuvichar.com/shaheed-bhagat-singh-quotes-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            title="Shaheed Bhagat Singh Quotes in Hindi |शहीद भगत सिंह के क्रांतिकारी विचार">Shaheed
                                                                                            Bhagat Singh Quotes in Hindi
                                                                                            |शहीद भगत सिंह के
                                                                                            क्रांतिकारी&#8230;</a></h3>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="td-mega-span">
                                                                            <div
                                                                                class="td_module_mega_menu td-animation-stack td_mod_mega_menu">
                                                                                <div class="td-module-image">
                                                                                    <div class="td-module-thumb"><a
                                                                                            href="https://aajkasuvichar.com/aaj-ka-mukhya-suvichar/"
                                                                                            rel="bookmark"
                                                                                            class="td-image-wrap "
                                                                                            title="Aaj Ka Mukhya Suvichar 2020 | प्रेरणादायक सुविचार"><img
                                                                                                class="entry-thumb"
                                                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                                                alt="Aaj Ka Mukhya Suvichar"
                                                                                                title="Aaj Ka Mukhya Suvichar 2020 | प्रेरणादायक सुविचार"
                                                                                                data-type="image_tag"
                                                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Mukhya-Suvichar-1.jpg"
                                                                                                width="179"
                                                                                                height="150" /></a>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="item-details">
                                                                                    <h3
                                                                                        class="entry-title td-module-title">
                                                                                        <a href="https://aajkasuvichar.com/aaj-ka-mukhya-suvichar/"
                                                                                            rel="bookmark"
                                                                                            title="Aaj Ka Mukhya Suvichar 2020 | प्रेरणादायक सुविचार">Aaj
                                                                                            Ka Mukhya Suvichar 2020 |
                                                                                            प्रेरणादायक सुविचार</a></h3>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="td-mega-span">
                                                                            <div
                                                                                class="td_module_mega_menu td-animation-stack td_mod_mega_menu">
                                                                                <div class="td-module-image">
                                                                                    <div class="td-module-thumb"><a
                                                                                            href="https://aajkasuvichar.com/bill-gates-biography-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            class="td-image-wrap "
                                                                                            title="Bill Gates Biography in Hindi | बिल गेट्स की सफलता की कहानी"><img
                                                                                                class="entry-thumb"
                                                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                                                alt="Bill-Gates-Biography-in-Hindi"
                                                                                                title="Bill Gates Biography in Hindi | बिल गेट्स की सफलता की कहानी"
                                                                                                data-type="image_tag"
                                                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/07/Bill-Gates-Biography-in-Hindi.jpg"
                                                                                                width="218"
                                                                                                height="109" /></a>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="item-details">
                                                                                    <h3
                                                                                        class="entry-title td-module-title">
                                                                                        <a href="https://aajkasuvichar.com/bill-gates-biography-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            title="Bill Gates Biography in Hindi | बिल गेट्स की सफलता की कहानी">Bill
                                                                                            Gates Biography in Hindi |
                                                                                            बिल गेट्स की सफलता
                                                                                            की&#8230;</a></h3>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="td-mega-span">
                                                                            <div
                                                                                class="td_module_mega_menu td-animation-stack td_mod_mega_menu">
                                                                                <div class="td-module-image">
                                                                                    <div class="td-module-thumb"><a
                                                                                            href="https://aajkasuvichar.com/narendra-modi-quotes-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            class="td-image-wrap "
                                                                                            title="Narendra Modi Quotes in Hindi |नरेन्द्र मोदी के प्रेरक कथन"><img
                                                                                                class="entry-thumb"
                                                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                                                alt="Narendra Modi Quotes In Hindi"
                                                                                                title="Narendra Modi Quotes in Hindi |नरेन्द्र मोदी के प्रेरक कथन"
                                                                                                data-type="image_tag"
                                                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/02/Narendra-Modi-Quotes-In-Hindi.jpg"
                                                                                                width="218"
                                                                                                height="136" /></a>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="item-details">
                                                                                    <h3
                                                                                        class="entry-title td-module-title">
                                                                                        <a href="https://aajkasuvichar.com/narendra-modi-quotes-in-hindi/"
                                                                                            rel="bookmark"
                                                                                            title="Narendra Modi Quotes in Hindi |नरेन्द्र मोदी के प्रेरक कथन">Narendra
                                                                                            Modi Quotes in Hindi
                                                                                            |नरेन्द्र मोदी के प्रेरक
                                                                                            कथन</a></h3>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="td-next-prev-wrap"><a href="#"
                                                                        class="td-ajax-prev-page ajax-page-disabled"
                                                                        aria-label="prev-page" id="prev-page-tdi_1"
                                                                        data-td_block_id="tdi_1"><i
                                                                            class="td-next-prev-icon td-icon-font td-icon-menu-left"></i></a><a
                                                                        href="#" class="td-ajax-next-page"
                                                                        aria-label="next-page" id="next-page-tdi_1"
                                                                        data-td_block_id="tdi_1"><i
                                                                            class="td-next-prev-icon td-icon-font td-icon-menu-right"></i></a>
                                                                </div>
                                                                <div class="clearfix"></div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1495">
                                            <a href="https://aajkasuvichar.com/wishes/">Wishes</a></li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1493">
                                            <a href="https://aajkasuvichar.com/hindi-story/">Hindi Story</a></li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1494">
                                            <a href="https://aajkasuvichar.com/knowledge/">Knowledge</a></li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1496">
                                            <a href="https://aajkasuvichar.com/jokes/">Jokes</a></li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1498">
                                            <a href="https://aajkasuvichar.com/hindi-poem/">Hindi Poem</a></li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1601">
                                            <a href="https://aajkasuvichar.com/hindi-biography/">Hindi Biography</a>
                                        </li>
                                        <li
                                            class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1499">
                                            <a href="https://aajkasuvichar.com/health-tips/">Health Tips</a></li>
                                        <li
                                            class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children td-menu-item td-normal-menu menu-item-1534">
                                            <a href="#">More</a>
                                            <ul class="sub-menu">
                                                <li
                                                    class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-1497">
                                                    <a href="https://aajkasuvichar.com/chanakya-niti-in-hindi/">Chanakya
                                                        Niti in Hindi</a></li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="header-search-wrap">
                                <div class="td-search-btns-wrap"> <a id="td-header-search-button" href="#" role="button"
                                        class="dropdown-toggle " data-toggle="dropdown"><i
                                            class="td-icon-search"></i></a> <a id="td-header-search-button-mob" href="#"
                                        class="dropdown-toggle " data-toggle="dropdown"><i
                                            class="td-icon-search"></i></a></div>
                                <div class="td-drop-down-search" aria-labelledby="td-header-search-button">
                                    <form method="get" class="td-search-form" action="https://aajkasuvichar.com/">
                                        <div role="search" class="td-head-form-search-wrap"> <input
                                                id="td-header-search" type="text" value="" name="s"
                                                autocomplete="off" /><input class="wpb_button wpb_btn-inverse btn"
                                                type="submit" id="td-header-search-top" value="Search" /></div>
                                    </form>
                                    <div id="td-aj-search"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="td-main-content-wrap td-container-wrap">
            <div class="td-container td-post-template-1 ">
                <div class="td-crumb-container">
                    <div class="entry-crumbs"><span><a title="" class="entry-crumb"
                                href="https://aajkasuvichar.com/">Home</a></span> <i
                            class="td-icon-right td-bread-sep"></i> <span><a title="View all posts in Hindi Quotes"
                                class="entry-crumb" href="https://aajkasuvichar.com/hindi-quotes/">Hindi
                                Quotes</a></span> <i class="td-icon-right td-bread-sep td-bred-no-url-last"></i> <span
                            class="td-bred-no-url-last">Aaj Ka Suvichar 2021 |आज का सुविचार</span></div>
                </div>
                <div class="td-pb-row">
                    <div class="td-pb-span8 td-main-content" role="main">
                        <div class="td-ss-main-content">
                            <article id="post-56"
                                class="post-56 post type-post status-publish format-standard has-post-thumbnail category-hindi-quotes tag-aaj-ka-shubh-vichar tag-aaj-ka-suvichar-2021 tag-aaj-ka-suvichar-batao tag-aaj-ka-suvichar-good-morning tag-aaj-ka-suvichar-hindi tag-aaj-ka-suvichar-hindi-me tag-aaj-ka-suvichar-hindi-mein tag-aaj-ka-suvichar-in-hindi tag-aaj-ka-suvichar-in-hindi-2021 tag-aaj-ka-suvichar-in-hindi-for-students tag-aaj-ka-suvichar-in-hindi-text tag-aaj-ka-suvichar-kya-ha tag-aaj-ka-suvichar-latest tag-aaj-ka-vichar-in-hindi-for-whatsapp tag-282"
                                itemscope itemtype="https://schema.org/Article">
                                <div class="td-post-header">
                                    <header class="td-post-title">
                                        <h1 class="entry-title">Aaj Ka Suvichar 2021 |आज का सुविचार</h1>
                                        <div class="td-module-meta-info">
                                            <div class="td-post-views"><i class="td-icon-views"></i><span
                                                    class="td-nr-views-56">2408</span></div>
                                        </div>
                                    </header>
                                </div>
                                <div class="td-post-sharing-top">
                                    <div id="td_social_sharing_article_top"
                                        class="td-post-sharing td-ps-border td-ps-border-grey td-ps-icon-arrow td-ps-icon-bg td-ps-text-color td-post-sharing-style19 ">
                                        <div class="td-post-sharing-visible"><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-facebook"
                                                href="https://www.facebook.com/sharer.php?u=https%3A%2F%2Faajkasuvichar.com%2Faaj-ka-suvichar%2F"
                                                title="Facebook">
                                                <div class="td-social-but-icon"><i class="td-icon-facebook"></i></div>
                                                <div class="td-social-but-text">Facebook</div>
                                            </a><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-twitter"
                                                href="https://twitter.com/intent/tweet?text=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0&url=https%3A%2F%2Faajkasuvichar.com%2Faaj-ka-suvichar%2F&via=Aaj+Ka+Suvichar"
                                                title="Twitter">
                                                <div class="td-social-but-icon"><i class="td-icon-twitter"></i></div>
                                                <div class="td-social-but-text">Twitter</div>
                                            </a><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-pinterest"
                                                href="https://pinterest.com/pin/create/button/?url=https://aajkasuvichar.com/aaj-ka-suvichar/&amp;media=https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg&description=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                title="Pinterest">
                                                <div class="td-social-but-icon"><i class="td-icon-pinterest"></i></div>
                                                <div class="td-social-but-text">Pinterest</div>
                                            </a><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-whatsapp"
                                                href="https://api.whatsapp.com/send?text=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0 %0A%0A https://aajkasuvichar.com/aaj-ka-suvichar/"
                                                title="WhatsApp">
                                                <div class="td-social-but-icon"><i class="td-icon-whatsapp"></i></div>
                                                <div class="td-social-but-text">WhatsApp</div>
                                            </a><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-linkedin"
                                                href="https://www.linkedin.com/shareArticle?mini=true&url=https://aajkasuvichar.com/aaj-ka-suvichar/&title=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                title="Linkedin">
                                                <div class="td-social-but-icon"><i class="td-icon-linkedin"></i></div>
                                                <div class="td-social-but-text">Linkedin</div>
                                            </a><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-telegram"
                                                href="https://telegram.me/share/url?url=https://aajkasuvichar.com/aaj-ka-suvichar/&text=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                title="Telegram">
                                                <div class="td-social-but-icon"><i class="td-icon-telegram"></i></div>
                                                <div class="td-social-but-text">Telegram</div>
                                            </a><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-reddit"
                                                href="https://reddit.com/submit?url=https://aajkasuvichar.com/aaj-ka-suvichar/&title=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                title="ReddIt">
                                                <div class="td-social-but-icon"><i class="td-icon-reddit"></i></div>
                                                <div class="td-social-but-text">ReddIt</div>
                                            </a><a
                                                class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-tumblr"
                                                href="https://www.tumblr.com/share/link?url=https://aajkasuvichar.com/aaj-ka-suvichar/&name=Aaj Ka Suvichar 2021 |आज का सुविचार"
                                                title="Tumblr">
                                                <div class="td-social-but-icon"><i class="td-icon-tumblr"></i></div>
                                                <div class="td-social-but-text">Tumblr</div>
                                            </a></div>
                                        <div class="td-social-sharing-hidden">
                                            <ul class="td-pulldown-filter-list"></ul><a
                                                class="td-social-sharing-button td-social-handler td-social-expand-tabs"
                                                href="#" data-block-uid="td_social_sharing_article_top" title="More">
                                                <div class="td-social-but-icon"><i
                                                        class="td-icon-plus td-social-expand-tabs-icon"></i></div>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="td-post-content tagdiv-type">
                                    <div class="td-featured-image-rec"></div>
                                    <p><strong>Aaj Ka <a href="https://aajkasuvichar.com/tag/suvichar/"
                                                class="st_tag internal_tag" rel="tag"
                                                title="Posts tagged with suvichar">Suvichar</a> 2020 |<a
                                                href="https://in.pinterest.com/AajKaSuvichar/aaj-ka-suvichar/"
                                                target="_blank" aria-label="आज का सुविचार (opens in a new tab)"
                                                rel="noreferrer noopener" class="rank-math-link">आज का
                                                सुविचार</a>:-</strong> वे विचार या महान लोगों के कथन, जो हमारे जीवन पर
                                        सकारात्मक प्रभाव डालते हैं। उन्हें ही सुविचार कहाँ जाता है। सुविचारों में इतनी
                                        ताकत होती है। जिसके सुनने मात्र से ही मनुष्य अपना जीवन बदल सकता है। प्रतिदिन कम
                                        से कम एक सुविचार अवश्य पढ़े और उसे अपने जीवन लागू करने का प्रयास भी अवश्य करे।
                                        कुछ समय के पश्चात आप अपनी ज़िन्दगी में कुछ न कुछ बदलाव अवश्य पाएंगे तो चलिए
                                        पढ़ते है, कुछ महान लोगों के कथन जो आपकी ज़िन्दगी को बदल देंगे और आप के अंदर एक
                                        नयी चेतना और समझ का विकास करेंगे।</p>
                                    <figure class="wp-block-image size-large"><noscript><img width="640" height="360"
                                                src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640,h_360/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg"
                                                alt="Aaj Ka Suvichar" class="wp-image-677" title="Aaj Ka Suvichar"
                                                srcset="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg 640w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_300/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks-300x169.jpg 300w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_386/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks-386x217.jpg 386w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_20/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks-20x11.jpg 20w"
                                                sizes="(max-width: 640px) 100vw, 640px" /></noscript><img width="640"
                                            height="360"
                                            src='https://cdn.shortpixel.ai/client/q_lqip,ret_wait,w_640,h_360/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg'
                                            data-src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640,h_360/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg"
                                            alt="Aaj Ka Suvichar" class="lazyload wp-image-677" title="Aaj Ka Suvichar"
                                            data-srcset="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg 640w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_300/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks-300x169.jpg 300w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_386/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks-386x217.jpg 386w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_20/https://aajkasuvichar.com/wp-content/uploads/2020/09/aks-20x11.jpg 20w"
                                            data-sizes="(max-width: 640px) 100vw, 640px" /></figure>
                                    <h2>Best Collection of <a href="https://aajkasuvichar.com/tag/aaj-ka-suvichar/"
                                            class="st_tag internal_tag" rel="tag"
                                            title="Posts tagged with Aaj Ka Suvichar">Aaj Ka Suvichar</a> |<a
                                            href="https://aajkasuvichar.com/tag/%e0%a4%86%e0%a4%9c-%e0%a4%95%e0%a4%be-%e0%a4%b8%e0%a5%81%e0%a4%b5%e0%a4%bf%e0%a4%9a%e0%a4%be%e0%a4%b0/"
                                            class="st_tag internal_tag" rel="tag"
                                            title="Posts tagged with आज का सुविचार">आज का सुविचार</a>:-</h2>
                                    <blockquote class="wp-block-quote">
                                        <p>ज़िंदेगी मे इतनी तेज़ी से आगे दौड़ो की लोगो के बुराई के धागे आपके पैरो मे ही
                                            आकर टूट जाए।</p>
                                    </blockquote>
                                    <figure class="wp-block-image size-large"><noscript><img width="640" height="640"
                                                src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640,h_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar.jpg"
                                                alt="Aaj Ka Suvichar" class="wp-image-678" title="Aaj Ka Suvichar"
                                                srcset="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar.jpg 640w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_300/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-300x300.jpg 300w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_150/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-150x150.jpg 150w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_386/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-386x386.jpg 386w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_80/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-80x80.jpg 80w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_20/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-20x20.jpg 20w"
                                                sizes="(max-width: 640px) 100vw, 640px" /></noscript><img width="640"
                                            height="640"
                                            src='https://cdn.shortpixel.ai/client/q_lqip,ret_wait,w_640,h_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar.jpg'
                                            data-src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640,h_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar.jpg"
                                            alt="Aaj Ka Suvichar" class="lazyload wp-image-678" title="Aaj Ka Suvichar"
                                            data-srcset="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar.jpg 640w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_300/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-300x300.jpg 300w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_150/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-150x150.jpg 150w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_386/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-386x386.jpg 386w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_80/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-80x80.jpg 80w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_20/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvichar-20x20.jpg 20w"
                                            data-sizes="(max-width: 640px) 100vw, 640px" /></figure>
                                    <blockquote class="wp-block-quote">
                                        <p>अच्छे काम करते रहिये, चाहे लोग तारीफ करे या न करे ,आधे से ज्यादा दुनिआ सोती
                                            रहती है तब सूरज निकलता है |</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>कुछ भी असंभव नहीं . जो सोच सकते है, वो कर सकते है, और वो भी सोच सकते है जो आज
                                            तक नहीं किया।&nbsp;</p>
                                    </blockquote>
                                    <figure class="wp-block-image size-large"><noscript><img width="640" height="640"
                                                src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640,h_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1.jpg"
                                                alt="Aaj Ka Suvichar" class="wp-image-679" title="Aaj Ka Suvichar"
                                                srcset="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1.jpg 640w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_300/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-300x300.jpg 300w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_150/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-150x150.jpg 150w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_386/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-386x386.jpg 386w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_80/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-80x80.jpg 80w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_20/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-20x20.jpg 20w"
                                                sizes="(max-width: 640px) 100vw, 640px" /></noscript><img width="640"
                                            height="640"
                                            src='https://cdn.shortpixel.ai/client/q_lqip,ret_wait,w_640,h_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1.jpg'
                                            data-src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640,h_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1.jpg"
                                            alt="Aaj Ka Suvichar" class="lazyload wp-image-679" title="Aaj Ka Suvichar"
                                            data-srcset="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_640/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1.jpg 640w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_300/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-300x300.jpg 300w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_150/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-150x150.jpg 150w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_386/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-386x386.jpg 386w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_80/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-80x80.jpg 80w, https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_20/https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Suvicha1-20x20.jpg 20w"
                                            data-sizes="(max-width: 640px) 100vw, 640px" /></figure>
                                    <blockquote class="wp-block-quote">
                                        <p>दुसरो के अनुभवों से लाभ उठाना ही बुद्धिमानी है |</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जिंदगी आसान नहीं होती, इसे आसान बनाना पड़ता है…! कुछ ‘अंदाज’ से, कुछ ‘नजर
                                            अंदाज ‘से……!</p>
                                    </blockquote>
                                    <p><strong><a href="https://aajkasuvichar.com/tag/aaj-ka-suvichar-latest/"
                                                class="st_tag internal_tag" rel="tag"
                                                title="Posts tagged with aaj ka suvichar latest">Aaj ka Suvichar
                                                Latest</a></strong></p>
                                    <blockquote class="wp-block-quote">
                                        <p>जो खुद खुश रहते है उनसे दुनिया खुश रहती है&nbsp;।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>&nbsp;ज़िंदगीआगे बढ़ने&nbsp; का नाम है, रुकने का नही</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>भीड़ हमेशा आसन रस्ते पर चलती है, जरुरी नहीं वो सही है | अपने रस्ते खुद चुनिए,
                                            आपको आपसे बेहतर और कोई नहीं जनता।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>परेशानी में कोई सलाह मांगे, तो सलाह के साथ अपना साथ भी देना, क्योकि सलाह गलत
                                            हो सकती है, साथ नहीं..</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>दुसरो की गलतियों से सीखे, आप कभी इतना लम्बा नही जी सकते की सारी गलतियाँ खुद
                                            करने का मौका मिले</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>प्यार से भागना आपको चोट से नहीं बचाता, वो दर असल प्यार पाने से रोकता है।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>डिग्री ना होना फायदेमंद भी है, डिग्री वाले एक ही काम करते है| जिनके पास
                                            डिग्री नहीं वो कुछ भी कर सकते है।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जो सबका मित्र &nbsp;होता है, वो दरअसल &nbsp;किसी का मित्र नहीं होता।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>बीच रास्ते से लौटने का कोई फायदा नहीं, लौटने पर भी उतनी ही दूरी तय करनी पड़ेगी
                                            जितनी दूरी तय कर लक्ष्य तक पहुच सकते है।</p>
                                    </blockquote>
                                    <p><strong><a href="https://aajkasuvichar.com/tag/aaj-ka-suvichar-good-morning/"
                                                class="st_tag internal_tag" rel="tag"
                                                title="Posts tagged with aaj ka suvichar good morning">Aaj ka Suvichar
                                                Good Morning</a></strong></p>
                                    <blockquote class="wp-block-quote">
                                        <p>&nbsp;कुछ भी असंभव नहीं जो सोच सकते है वो कर सकते है| और वो भी सोच सकते है जो
                                            आज तक नहीं किया।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>बेहतर काम न करने की वजह या वक्त न होने का बहाना मत बनाइयें, आपका दिन भी २४
                                            घंटे का ही होता है और सफल लोगो का भी।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जो आपके साथ दिल से बात करता हो, उनको कभी दिमाग से जवाब मत देना।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>&nbsp;सफलता की ख़ुशी मानना अच्छा है पर उससे ज़रूरीहै अपनी असफलता से सीख
                                            लेना&nbsp;..</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>पछ्तावे से आच्छा है, कोशिश करके फेल हो जाना&nbsp;</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>&nbsp;किसी के पैरों में गिरकर कामयाबीपाने से बेहतर है अपने पैरों पर चलकर कुछ
                                            बनने की ठान लो।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>समझनी है ज़िन्दगी तो पीछे देखो, जीनी है ज़िन्दगी तो आगे देखो ।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जब तुम पैदा हुए थे तो तुम रोए थे जबकि पूरी दुनिया ने जश्न मनाया था| अपना जीवन
                                            ऐसे जियो कि तुम्हारी मौत पर पूरी दुनिया रोए और तुम जश्न मनाओ</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>भीड़ हमेशा उस रास्ते पर चलती है जो रास्ता आसान लगता है, लेकिन इसका मतलब यह
                                            नहीं की भीड़ हमेशा सही रास्ते पर चलती है| अपने रास्ते खुद चुनिए क्योंकि आपको
                                            आपसे बेहतर और कोई नहीं जानता|</p>
                                    </blockquote>
                                    <h3><span class="ez-toc-section" id="Life_Best_Aaj_Ka_Suvichar_in_HIndi"></span>Life
                                        Best Aaj Ka <a href="https://in.pinterest.com/AajKaSuvichar/suvichar/"
                                            target="_blank" aria-label="Suvichar (opens in a new tab)"
                                            rel="noreferrer noopener nofollow" class="rank-math-link">Suvichar</a> in
                                        HIndi<span class="ez-toc-section-end"></span></h3>
                                    <blockquote class="wp-block-quote">
                                        <p>मुसीबतों से भागना, नयी मुसीबतों को निमंत्रण देने के समान है| जीवन में समय-समय
                                            पर चुनौतियों एंव मुसीबतों का सामना करना पड़ता है एंव यही जीवन का सत्य
                                            है|&nbsp;एक शांत समुन्द्र में नाविक कभी भी कुशल नहीं बन पाता</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>किसी डिग्री का ना होन दरअसल फायेदेमंद है, अगर आप इंजिनियर या डाक्टर हैं तब आप
                                            एक ही काम कर सकते हैं| पर यदि आपके पास कोई डिग्री नहीं है, तो आप कुछ भी कर
                                            सकते हैं|</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जीवन में&nbsp;कठिनाइयाँ हमे बर्बाद करने नहीं आती है, बल्कि यह हमारी छुपी
                                            हुई&nbsp;सामर्थ्य और शक्तियों को बाहर निकलने में हमारी मदद करती है|
                                            कठिनाइयों को यह जान लेने दो की आप उससे भी ज्यादा कठिन हो।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>सच्चे लोगों को कभी प्रशंसा की आवश्यकता नहीं होती और असली फूलों को कभी इत्र
                                            लगाने की जरूरत नहीं पड़ती है ।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जुबान में हड्डी नहीं होती लेकिन हड्डी तुडवाने की ताकद जरुर होती है।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>अगर सफल होने की इच्छा प्रबल है, तो लाखों असफलताएं भी आपको सफलता की ओर ही
                                            धकेलती हैं।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>&nbsp;जीवन का एक ही नियम हैं “जो झुकता हैं वो प्राप्तकरता हैं” वैसे ही जैसे
                                            कुए में उतरने वाली बाल्टी झुकती है तो भरकर बाहर निकलती है।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>&nbsp;जो मनुष्यआपके बुरे समय में आपका साथ नहीं देता, उसे आपके अच्छे वक्त में
                                            भी साथ रहने का कोई अधिकार नहीं है। पहले पाप करके बाद में प्रायचित्त करना वो
                                            कीचड़ में पैर डालके फिर धोने के समान हैं।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>शिक्षा सबसे अच्छी मित्र है. हर शिक्षित व्यक्ति हर जगह सम्मान ही पता है.</p>
                                    </blockquote>
                                    <p><strong>Aaj ka <a href="https://aajkasuvichar.com/tag/suvichar-in-hindi/"
                                                class="st_tag internal_tag" rel="tag"
                                                title="Posts tagged with suvichar in Hindi">Suvichar in Hindi</a> for
                                            Students</strong></p>
                                    <blockquote class="wp-block-quote">
                                        <p>शिक्षा सौंदर्य और यौवन को परास्त कर देती है।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जब आप सपने देखना छोड़ देते हैं आप जीना छोड़ देते हैं।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>एक मनुष्य को कठिनाइयों की जरूरत होती है क्योंकि तभी वह सफलता का आनंद ले सकता
                                            है।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>आप वो बन जाते हैं जो आप सोचते हैं कि आप हैं।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जब आपको अपने लक्ष्य के आलावा जीवन में कुछ भी दिखाई नहीं देता तो आप अपने
                                            लक्ष्य को आसानी से प्राप्त कर सकोंगे।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जीवन में गिरना बहुत जरुरी हैं क्योकि जब तक आप गिरते नहीं तब तक आपको पाता नहीं
                                            चलेंगा की आप कितने मजबूत हो।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>दूसरों पर अपनी असफलता का दोष मढ़ने वाले जिंदगी में कभी आगे नहीं बढ़ पाते हैं।
                                        </p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>अगर आप कुछ बड़ा पाना की सोच रहे है, तो आपकी जिवन आसान नहीं होगा. क्योंकि बड़ी
                                            सफलता आसानी से नहीं मिलती है।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जो इन्सान यह जानते हुए भी कि सही रास्ता कौन सा है, गलत रास्ते पर आगे बढ़ता जा
                                            रहा हो…. भगवान भी उसका भला नहीं कर सकते हैं।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>इतने मजबूत बनिए, कि कोई भी छोटी-छोटी बातें आपको प्रभावित न कर सकें।</p>
                                    </blockquote>
                                    <p><a href="https://aajkasuvichar.com/tag/aaj-ka-suvichar-kya-ha/"
                                            class="st_tag internal_tag" rel="tag"
                                            title="Posts tagged with aaj ka suvichar kya ha">Aaj ka Suvichar Kya Ha</a>
                                    </p>
                                    <blockquote class="wp-block-quote">
                                        <p>जो बातें नज़रअंदाज़ करने लायक हैं, आपको उन बातों को नज़रअंदाज़ ही करना चाहिए।
                                        </p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>अगर आपके बिना भी दूसरे का काम हो सकता है, तो दूसरे के कामों में शामिल न हों।
                                        </p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>आपको अच्छे विचार तब तक पता नहीं चलेंगे, जब तक आप कुछ बुरे विचारों पर काम नहीं
                                            करते।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>अगर किसी चीज को हासिल करना चाहते हो, तो स्वयं को उस के काबिल बनाओ. ऐसी स्थिति
                                            मत आने दो कि तुम्हें दूसरे के आगे मजबूर होना पड़े।</p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>जब आप अपने इस वक्त को बर्बाद करते हैं, तो दूसरे लोग आपके भविष्य का निर्धारण
                                            करते हैं। क्योंकि वर्तमान को&nbsp;इस बात से मतलब नहीं है की तुम कितनी धीरे
                                            चलते हो जब तक की तुम रुकते नहीं</p>
                                    </blockquote>
                                    <p><strong><a href="https://aajkasuvichar.com/tag/aaj-ka-vichar/"
                                                class="st_tag internal_tag" rel="tag"
                                                title="Posts tagged with Aaj Ka Vichar">Aaj ka Vichar</a> in Hindi for
                                            Whatsapp</strong></p>
                                    <blockquote class="wp-block-quote">
                                        <p>कोई भी मूर्ख आलोचना,निंदा, और शिकायत कर सकता है– और ज्यादातर मूर्ख करते हैं.
                                        </p>
                                    </blockquote>
                                    <blockquote class="wp-block-quote">
                                        <p>&nbsp;खुद के लिए और अपनी मौजूदा स्थिति के लिए अफ़सोस करना , ना केवल उर्जा की
                                            बर्बादी है बल्कि शायद ये सबसे बुरी आदत है जो आपके अन्दर हो सकती है.</p>
                                    </blockquote>
                                    <h4><span class="ez-toc-section" id="Reda_More"></span>Reda More:-<span
                                            class="ez-toc-section-end"></span></h4>
                                    <p><a aria-label="Suvichar in Hindi-501 सुविचार (opens in a new tab)"
                                            href="https://aajkasuvichar.com/suvichar-in-hindi/"
                                            rel="noreferrer noopener nofollow" target="_blank"
                                            class="rank-math-link">Suvichar in Hindi-501 सुविचार</a></p>
                                    <p><a href="https://aajkasuvichar.com/happy-birthday-wishes-in-hindi/"
                                            target="_blank" aria-label=" (opens in a new tab)"
                                            rel="noreferrer noopener nofollow" class="rank-math-link">Happy Birthday
                                            Wishes in Hindi</a></p>
                                    <p><a href="https://aajkasuvichar.com/hindi-jokes-collection/" target="_blank"
                                            aria-label=" (opens in a new tab)" rel="noreferrer noopener nofollow"
                                            class="rank-math-link">Hindi Jokes Collection</a></p>
                                    <h5><span class="ez-toc-section"
                                            id="i"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                        <span class="ez-toc-section-end"></span></h5>
                                    <p><strong>Final Words:-</strong></p>
                                    <p>आशा करते हैं कि आपको यहाँ पर दिए गए&nbsp;<strong><a
                                                href="https://in.pinterest.com/tourzman/aaj-ka-suvichaar/"
                                                target="_blank" aria-label=" (opens in a new tab)"
                                                rel="noreferrer noopener nofollow" class="rank-math-link">Aaj Ka
                                                Suvichar</a>&nbsp;सुविचार इन हिंदी</strong>&nbsp;काफ़ी पसंद आये होंगे।
                                        आप इसे अपने दोस्तों तथा जानने वाले लोगो के साथ शेयर करना ना भूलें। इसके साथ ही
                                        आपको यहाँ पर दिए गए सभी सुविचार कैसे लगे ये हमे कमेंट कर के जरूर बताएं। वहीं अगर
                                        आपके पास इससे जुड़े कुछ ज़रूरी सुझाव और सलाह हो तो वो भी हमें कमेंट के माध्यम से
                                        जरूर बताएं।</p>
                                </div>
                                <footer>
                                    <div class="td-post-source-tags"></div>
                                    <div class="td-post-sharing-bottom">
                                        <div class="td-post-sharing-classic"><iframe frameBorder="0"
                                                src="https://www.facebook.com/plugins/like.php?href=https://aajkasuvichar.com/aaj-ka-suvichar/&amp;layout=button_count&amp;show_faces=false&amp;width=105&amp;action=like&amp;colorscheme=light&amp;height=21"
                                                style="border:none; overflow:hidden; width:auto; height:21px; background-color:transparent;"></iframe>
                                        </div>
                                        <div id="td_social_sharing_article_bottom"
                                            class="td-post-sharing td-ps-border td-ps-border-grey td-ps-icon-arrow td-ps-icon-bg td-ps-text-color td-post-sharing-style19 ">
                                            <div class="td-post-sharing-visible"><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-facebook"
                                                    href="https://www.facebook.com/sharer.php?u=https%3A%2F%2Faajkasuvichar.com%2Faaj-ka-suvichar%2F"
                                                    title="Facebook">
                                                    <div class="td-social-but-icon"><i class="td-icon-facebook"></i>
                                                    </div>
                                                    <div class="td-social-but-text">Facebook</div>
                                                </a><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-twitter"
                                                    href="https://twitter.com/intent/tweet?text=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0&url=https%3A%2F%2Faajkasuvichar.com%2Faaj-ka-suvichar%2F&via=Aaj+Ka+Suvichar"
                                                    title="Twitter">
                                                    <div class="td-social-but-icon"><i class="td-icon-twitter"></i>
                                                    </div>
                                                    <div class="td-social-but-text">Twitter</div>
                                                </a><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-pinterest"
                                                    href="https://pinterest.com/pin/create/button/?url=https://aajkasuvichar.com/aaj-ka-suvichar/&amp;media=https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg&description=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                    title="Pinterest">
                                                    <div class="td-social-but-icon"><i class="td-icon-pinterest"></i>
                                                    </div>
                                                    <div class="td-social-but-text">Pinterest</div>
                                                </a><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-whatsapp"
                                                    href="https://api.whatsapp.com/send?text=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0 %0A%0A https://aajkasuvichar.com/aaj-ka-suvichar/"
                                                    title="WhatsApp">
                                                    <div class="td-social-but-icon"><i class="td-icon-whatsapp"></i>
                                                    </div>
                                                    <div class="td-social-but-text">WhatsApp</div>
                                                </a><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-linkedin"
                                                    href="https://www.linkedin.com/shareArticle?mini=true&url=https://aajkasuvichar.com/aaj-ka-suvichar/&title=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                    title="Linkedin">
                                                    <div class="td-social-but-icon"><i class="td-icon-linkedin"></i>
                                                    </div>
                                                    <div class="td-social-but-text">Linkedin</div>
                                                </a><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-telegram"
                                                    href="https://telegram.me/share/url?url=https://aajkasuvichar.com/aaj-ka-suvichar/&text=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                    title="Telegram">
                                                    <div class="td-social-but-icon"><i class="td-icon-telegram"></i>
                                                    </div>
                                                    <div class="td-social-but-text">Telegram</div>
                                                </a><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-reddit"
                                                    href="https://reddit.com/submit?url=https://aajkasuvichar.com/aaj-ka-suvichar/&title=Aaj+Ka+Suvichar+2021+%7C%E0%A4%86%E0%A4%9C+%E0%A4%95%E0%A4%BE+%E0%A4%B8%E0%A5%81%E0%A4%B5%E0%A4%BF%E0%A4%9A%E0%A4%BE%E0%A4%B0"
                                                    title="ReddIt">
                                                    <div class="td-social-but-icon"><i class="td-icon-reddit"></i></div>
                                                    <div class="td-social-but-text">ReddIt</div>
                                                </a><a
                                                    class="td-social-sharing-button td-social-sharing-button-js td-social-network td-social-tumblr"
                                                    href="https://www.tumblr.com/share/link?url=https://aajkasuvichar.com/aaj-ka-suvichar/&name=Aaj Ka Suvichar 2021 |आज का सुविचार"
                                                    title="Tumblr">
                                                    <div class="td-social-but-icon"><i class="td-icon-tumblr"></i></div>
                                                    <div class="td-social-but-text">Tumblr</div>
                                                </a></div>
                                            <div class="td-social-sharing-hidden">
                                                <ul class="td-pulldown-filter-list"></ul><a
                                                    class="td-social-sharing-button td-social-handler td-social-expand-tabs"
                                                    href="#" data-block-uid="td_social_sharing_article_bottom"
                                                    title="More">
                                                    <div class="td-social-but-icon"><i
                                                            class="td-icon-plus td-social-expand-tabs-icon"></i></div>
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="td-block-row td-post-next-prev">
                                        <div class="td-block-span6 td-post-prev-post">
                                            <div class="td-post-next-prev-content"><span>Previous article</span><a
                                                    href="https://aajkasuvichar.com/friend-advice/">Friend Advice-मित्र
                                                    की सलाह</a></div>
                                        </div>
                                        <div class="td-next-prev-separator"></div>
                                        <div class="td-block-span6 td-post-next-post">
                                            <div class="td-post-next-prev-content"><span>Next article</span><a
                                                    href="https://aajkasuvichar.com/aaj-ka-thought-in-hindi/">Aaj Ka
                                                    Thought in Hindi-आज का विचार</a></div>
                                        </div>
                                    </div>
                                    <div class="td-author-name vcard author" style="display: none"><span class="fn"><a
                                                href="https://aajkasuvichar.com/author/AajKaSuvichar/">AajKaSuvichar</a></span>
                                    </div> <span class="td-page-meta" itemprop="author" itemscope
                                        itemtype="https://schema.org/Person">
                                        <meta itemprop="name" content="AajKaSuvichar"></span>
                                    <meta itemprop="datePublished" content="2018-10-19T09:32:00+00:00">
                                    <meta itemprop="dateModified" content="2021-02-20T13:35:00+00:00">
                                    <meta itemscope itemprop="mainEntityOfPage" itemType="https://schema.org/WebPage"
                                        itemid="https://aajkasuvichar.com/aaj-ka-suvichar/" /><span class="td-page-meta"
                                        itemprop="publisher" itemscope itemtype="https://schema.org/Organization"><span
                                            class="td-page-meta" itemprop="logo" itemscope
                                            itemtype="https://schema.org/ImageObject">
                                            <meta itemprop="url"
                                                content="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png">
                                            </span>
                                        <meta itemprop="name" content="Aaj Ka Suvichar"></span>
                                    <meta itemprop="headline " content="Aaj Ka Suvichar 2021 |आज का सुविचार"><span
                                        class="td-page-meta" itemprop="image" itemscope
                                        itemtype="https://schema.org/ImageObject">
                                        <meta itemprop="url"
                                            content="https://aajkasuvichar.com/wp-content/uploads/2020/09/aks.jpg">
                                        <meta itemprop="width" content="640">
                                        <meta itemprop="height" content="360"></span>
                                </footer>
                            </article>
                            <div class="td_block_wrap td_block_related_posts tdi_4 td_with_ajax_pagination td-pb-border-top td_block_template_8"
                                data-td-block-uid="tdi_4">
                                <script>
                                    var block_tdi_4 = new tdBlock();
                                    block_tdi_4.id = "tdi_4";
                                    block_tdi_4.atts =
                                        '{"limit":6,"ajax_pagination":"next_prev","live_filter":"cur_post_same_categories","td_ajax_filter_type":"td_custom_related","class":"tdi_4","td_column_number":3,"block_type":"td_block_related_posts","live_filter_cur_post_id":56,"live_filter_cur_post_author":"1","block_template_id":"","header_color":"","ajax_pagination_infinite_stop":"","offset":"","td_ajax_preloading":"","td_filter_default_txt":"","td_ajax_filter_ids":"","el_class":"","color_preset":"","border_top":"","css":"","tdc_css":"","tdc_css_class":"tdi_4","tdc_css_class_style":"tdi_4_rand_style"}';
                                    block_tdi_4.td_column_number = "3";
                                    block_tdi_4.block_type = "td_block_related_posts";
                                    block_tdi_4.post_count = "6";
                                    block_tdi_4.found_posts = "21";
                                    block_tdi_4.header_color = "";
                                    block_tdi_4.ajax_pagination_infinite_stop = "";
                                    block_tdi_4.max_num_pages = "4";
                                    tdBlocksArray.push(block_tdi_4);
                                </script>
                                <h4 class="td-related-title td-block-title"><a id="tdi_5"
                                        class="td-related-left td-cur-simple-item" data-td_filter_value=""
                                        data-td_block_id="tdi_4" href="#">RELATED ARTICLES</a><a id="tdi_6"
                                        class="td-related-right" data-td_filter_value="td_related_more_from_author"
                                        data-td_block_id="tdi_4" href="#">MORE FROM AUTHOR</a></h4>
                                <div id=tdi_4 class="td_block_inner">
                                    <div class="td-related-row">
                                        <div class="td-related-span4">
                                            <div
                                                class="td_module_related_posts td-animation-stack td_mod_related_posts">
                                                <div class="td-module-image">
                                                    <div class="td-module-thumb"><a
                                                            href="https://aajkasuvichar.com/dhirubhai-ambani-quotes-in-hindi/"
                                                            rel="bookmark" class="td-image-wrap "
                                                            title="Dhirubhai Ambani Quotes in Hindi | धीरूभाई अंबानी के अनमोल विचार"><img
                                                                class="entry-thumb"
                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                alt="Dhirubhai Ambani Quotes in Hindi"
                                                                title="Dhirubhai Ambani Quotes in Hindi | धीरूभाई अंबानी के अनमोल विचार"
                                                                data-type="image_tag"
                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2021/01/dhirubhai-ambani-quotes-in-hindi.jpg"
                                                                width="218" height="122" /></a></div>
                                                </div>
                                                <div class="item-details">
                                                    <h3 class="entry-title td-module-title"><a
                                                            href="https://aajkasuvichar.com/dhirubhai-ambani-quotes-in-hindi/"
                                                            rel="bookmark"
                                                            title="Dhirubhai Ambani Quotes in Hindi | धीरूभाई अंबानी के अनमोल विचार">Dhirubhai
                                                            Ambani Quotes in Hindi | धीरूभाई अंबानी के अनमोल विचार</a>
                                                    </h3>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="td-related-span4">
                                            <div
                                                class="td_module_related_posts td-animation-stack td_mod_related_posts">
                                                <div class="td-module-image">
                                                    <div class="td-module-thumb"><a
                                                            href="https://aajkasuvichar.com/shaheed-bhagat-singh-quotes-in-hindi/"
                                                            rel="bookmark" class="td-image-wrap "
                                                            title="Shaheed Bhagat Singh Quotes in Hindi |शहीद भगत सिंह के क्रांतिकारी विचार"><img
                                                                class="entry-thumb"
                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                alt="Shaheed Bhagat Singh Quotes in Hindi"
                                                                title="Shaheed Bhagat Singh Quotes in Hindi |शहीद भगत सिंह के क्रांतिकारी विचार"
                                                                data-type="image_tag"
                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/09/Sheed-Bhagat-Singh.jpg"
                                                                width="218" height="121" /></a></div>
                                                </div>
                                                <div class="item-details">
                                                    <h3 class="entry-title td-module-title"><a
                                                            href="https://aajkasuvichar.com/shaheed-bhagat-singh-quotes-in-hindi/"
                                                            rel="bookmark"
                                                            title="Shaheed Bhagat Singh Quotes in Hindi |शहीद भगत सिंह के क्रांतिकारी विचार">Shaheed
                                                            Bhagat Singh Quotes in Hindi |शहीद भगत सिंह के क्रांतिकारी
                                                            विचार</a></h3>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="td-related-span4">
                                            <div
                                                class="td_module_related_posts td-animation-stack td_mod_related_posts">
                                                <div class="td-module-image">
                                                    <div class="td-module-thumb"><a
                                                            href="https://aajkasuvichar.com/aaj-ka-mukhya-suvichar/"
                                                            rel="bookmark" class="td-image-wrap "
                                                            title="Aaj Ka Mukhya Suvichar 2020 | प्रेरणादायक सुविचार"><img
                                                                class="entry-thumb"
                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                alt="Aaj Ka Mukhya Suvichar"
                                                                title="Aaj Ka Mukhya Suvichar 2020 | प्रेरणादायक सुविचार"
                                                                data-type="image_tag"
                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/09/Aaj-Ka-Mukhya-Suvichar-1.jpg"
                                                                width="179" height="150" /></a></div>
                                                </div>
                                                <div class="item-details">
                                                    <h3 class="entry-title td-module-title"><a
                                                            href="https://aajkasuvichar.com/aaj-ka-mukhya-suvichar/"
                                                            rel="bookmark"
                                                            title="Aaj Ka Mukhya Suvichar 2020 | प्रेरणादायक सुविचार">Aaj
                                                            Ka Mukhya Suvichar 2020 | प्रेरणादायक सुविचार</a></h3>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="td-related-row">
                                        <div class="td-related-span4">
                                            <div
                                                class="td_module_related_posts td-animation-stack td_mod_related_posts">
                                                <div class="td-module-image">
                                                    <div class="td-module-thumb"><a
                                                            href="https://aajkasuvichar.com/bill-gates-biography-in-hindi/"
                                                            rel="bookmark" class="td-image-wrap "
                                                            title="Bill Gates Biography in Hindi | बिल गेट्स की सफलता की कहानी"><img
                                                                class="entry-thumb"
                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                alt="Bill-Gates-Biography-in-Hindi"
                                                                title="Bill Gates Biography in Hindi | बिल गेट्स की सफलता की कहानी"
                                                                data-type="image_tag"
                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/07/Bill-Gates-Biography-in-Hindi.jpg"
                                                                width="218" height="109" /></a></div>
                                                </div>
                                                <div class="item-details">
                                                    <h3 class="entry-title td-module-title"><a
                                                            href="https://aajkasuvichar.com/bill-gates-biography-in-hindi/"
                                                            rel="bookmark"
                                                            title="Bill Gates Biography in Hindi | बिल गेट्स की सफलता की कहानी">Bill
                                                            Gates Biography in Hindi | बिल गेट्स की सफलता की कहानी</a>
                                                    </h3>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="td-related-span4">
                                            <div
                                                class="td_module_related_posts td-animation-stack td_mod_related_posts">
                                                <div class="td-module-image">
                                                    <div class="td-module-thumb"><a
                                                            href="https://aajkasuvichar.com/narendra-modi-quotes-in-hindi/"
                                                            rel="bookmark" class="td-image-wrap "
                                                            title="Narendra Modi Quotes in Hindi |नरेन्द्र मोदी के प्रेरक कथन"><img
                                                                class="entry-thumb"
                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                alt="Narendra Modi Quotes In Hindi"
                                                                title="Narendra Modi Quotes in Hindi |नरेन्द्र मोदी के प्रेरक कथन"
                                                                data-type="image_tag"
                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/02/Narendra-Modi-Quotes-In-Hindi.jpg"
                                                                width="218" height="136" /></a></div>
                                                </div>
                                                <div class="item-details">
                                                    <h3 class="entry-title td-module-title"><a
                                                            href="https://aajkasuvichar.com/narendra-modi-quotes-in-hindi/"
                                                            rel="bookmark"
                                                            title="Narendra Modi Quotes in Hindi |नरेन्द्र मोदी के प्रेरक कथन">Narendra
                                                            Modi Quotes in Hindi |नरेन्द्र मोदी के प्रेरक कथन</a></h3>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="td-related-span4">
                                            <div
                                                class="td_module_related_posts td-animation-stack td_mod_related_posts">
                                                <div class="td-module-image">
                                                    <div class="td-module-thumb"><a
                                                            href="https://aajkasuvichar.com/life-quotes-in-hindi/"
                                                            rel="bookmark" class="td-image-wrap "
                                                            title="Life Quotes in Hindi |जीवन के प्रेरणादायक  सुविचार"><img
                                                                class="entry-thumb"
                                                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAACWAQMAAACCSQSPAAAAA1BMVEWurq51dlI4AAAAAXRSTlMmkutdmwAAABpJREFUWMPtwQENAAAAwiD7p7bHBwwAAAAg7RD+AAGXD7BoAAAAAElFTkSuQmCC"
                                                                alt="Life Quots in Hindi"
                                                                title="Life Quotes in Hindi |जीवन के प्रेरणादायक  सुविचार"
                                                                data-type="image_tag"
                                                                data-img-url="https://aajkasuvichar.com/wp-content/uploads/2020/02/Life-Quotes-In-Hindi.jpg"
                                                                width="218" height="145" /></a></div>
                                                </div>
                                                <div class="item-details">
                                                    <h3 class="entry-title td-module-title"><a
                                                            href="https://aajkasuvichar.com/life-quotes-in-hindi/"
                                                            rel="bookmark"
                                                            title="Life Quotes in Hindi |जीवन के प्रेरणादायक  सुविचार">Life
                                                            Quotes in Hindi |जीवन के प्रेरणादायक सुविचार</a></h3>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="td-next-prev-wrap"><a href="#" class="td-ajax-prev-page ajax-page-disabled"
                                        aria-label="prev-page" id="prev-page-tdi_4" data-td_block_id="tdi_4"><i
                                            class="td-next-prev-icon td-icon-font td-icon-menu-left"></i></a><a href="#"
                                        class="td-ajax-next-page" aria-label="next-page" id="next-page-tdi_4"
                                        data-td_block_id="tdi_4"><i
                                            class="td-next-prev-icon td-icon-font td-icon-menu-right"></i></a></div>
                            </div>
                            <div id="disqus_thread"></div>
                        </div>
                    </div>
                    <div class="td-pb-span4 td-main-sidebar" role="complementary">
                        <div class="td-ss-main-sidebar"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="td-main-content-wrap td-footer-instagram-container td-container-wrap td_stretch_content">
            <div class="td-instagram-user">
                <h4 class="td-footer-instagram-title"> Follow us on Instagram <a class="td-footer-instagram-user-link"
                        href="https://www.instagram.com/suvicharhindime" target="_blank">@suvicharhindime</a></h4>
            </div>
            <div class="td_block_wrap td_block_instagram tdi_7 td-pb-border-top td_block_template_8"
                data-td-block-uid="tdi_7">
                <div class="td-block-title-wrap"></div>
                <div id=tdi_7 class="td-instagram-wrap td_block_inner td-column-1">
                    <div class="td-instagram-main td-images-on-row-6">
                        <div class="td-instagram-element"> <a class="td-instagram-image"
                                href="https://www.instagram.com/p/CRCHoBoBauA/" aria-label="instagram-image"
                                target="_blank"
                                style="background-image: url(https://scontent-lhr8-1.cdninstagram.com/v/t51.29350-15/213007430_190974722974680_8503814877064569941_n.jpg?_nc_cat=108&ccb=1-3&_nc_sid=8ae9d6&_nc_ohc=DWKHIfiC_wcAX-LHDaf&_nc_ht=scontent-lhr8-1.cdninstagram.com&oh=382bdf5105a3b0689a4ffc35c33e7f25&oe=60ECC430)">
                            </a></div>
                        <div class="td-instagram-element"> <a class="td-instagram-image"
                                href="https://www.instagram.com/p/CRCHmHVhCSl/" aria-label="instagram-image"
                                target="_blank"
                                style="background-image: url(https://scontent-lhr8-1.cdninstagram.com/v/t51.29350-15/212643949_337181514445084_3590203799648346571_n.jpg?_nc_cat=103&ccb=1-3&_nc_sid=8ae9d6&_nc_ohc=PsnvBqExbm0AX8ZETEF&_nc_ht=scontent-lhr8-1.cdninstagram.com&oh=1e2b07817fbfa3ff08bae340dee9c2a7&oe=60ECCBCB)">
                            </a></div>
                        <div class="td-instagram-element"> <a class="td-instagram-image"
                                href="https://www.instagram.com/p/CRCHkQjBKIB/" aria-label="instagram-image"
                                target="_blank"
                                style="background-image: url(https://scontent-lhr8-1.cdninstagram.com/v/t51.29350-15/213766800_507688863648407_2790648657335932182_n.jpg?_nc_cat=111&ccb=1-3&_nc_sid=8ae9d6&_nc_ohc=nd_1i-RNe40AX9cT1VM&_nc_ht=scontent-lhr8-1.cdninstagram.com&oh=3f5e924ee68db7dcd24535a2c2715372&oe=60EB759A)">
                            </a></div>
                        <div class="td-instagram-element"> <a class="td-instagram-image"
                                href="https://www.instagram.com/p/CRCHhQaB-B8/" aria-label="instagram-image"
                                target="_blank"
                                style="background-image: url(https://scontent-lhr8-2.cdninstagram.com/v/t51.29350-15/211272159_4827569850592220_3953839212039064420_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=8ae9d6&_nc_ohc=AUqebBPKM4UAX9DqJZ8&_nc_ht=scontent-lhr8-2.cdninstagram.com&oh=107d31518f4f76264b60251f97a22725&oe=60EC43D3)">
                            </a></div>
                        <div class="td-instagram-element"> <a class="td-instagram-image"
                                href="https://www.instagram.com/p/CRCHfnHhLUB/" aria-label="instagram-image"
                                target="_blank"
                                style="background-image: url(https://scontent-lhr8-1.cdninstagram.com/v/t51.29350-15/211225981_3050794975245873_2862996175906653218_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=8ae9d6&_nc_ohc=Vu4_0YTjYHUAX8VN4f3&_nc_ht=scontent-lhr8-1.cdninstagram.com&oh=cba8842082fa1e29c0ec77d032aebe83&oe=60EC288C)">
                            </a></div>
                        <div class="td-instagram-element"> <a class="td-instagram-image"
                                href="https://www.instagram.com/p/CRCHdFjBVWq/" aria-label="instagram-image"
                                target="_blank"
                                style="background-image: url(https://scontent-lhr8-1.cdninstagram.com/v/t51.29350-15/212545526_553437058986060_8605091228193092749_n.jpg?_nc_cat=103&ccb=1-3&_nc_sid=8ae9d6&_nc_ohc=57vyfdnJKMkAX-5WdsD&_nc_ht=scontent-lhr8-1.cdninstagram.com&oh=8e221fa38ee05e133a5a2f15a5f9631b&oe=60ECC2DF)">
                            </a></div>
                        <div class="clearfix"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="tdc-footer-wrap ">
            <div class="td-footer-wrapper td-footer-container td-container-wrap td_stretch_content">
                <div class="td-container">
                    <div class="td-pb-row">
                        <div class="td-pb-span12"></div>
                    </div>
                    <div class="td-pb-row">
                        <div class="td-pb-span4"></div>
                        <div class="td-pb-span4"></div>
                        <div class="td-pb-span4"></div>
                    </div>
                </div>
                <div class="td-footer-bottom-full">
                    <div class="td-container">
                        <div class="td-pb-row">
                            <div class="td-pb-span3">
                                <aside class="footer-logo-wrap"><a href="https://aajkasuvichar.com/"><noscript><img
                                                class="td-retina-data"
                                                src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                                data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                                alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar"
                                                width="554" /></noscript><img class="lazyload td-retina-data"
                                            src='https://cdn.shortpixel.ai/client/q_lqip,ret_wait,w_554/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png'
                                            data-src="https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_554/https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                            data-retina="https://aajkasuvichar.com/wp-content/uploads/2020/09/AKS-Blue.png"
                                            alt="Aaj Ka Suvichar" title="Aaj Ka Suvichar" width="554" /></a></aside>
                            </div>
                            <div class="td-pb-span5">
                                <aside class="footer-text-wrap">
                                    <div class="block-title"><span>ABOUT US</span></div>
                                    <div class="footer-email-wrap">Contact us: <a
                                            href="/cdn-cgi/l/email-protection#a7d3c8c3c6ded4d2d1cec4cfc6d5e7c0cac6cecb89c4c8ca"><span
                                                class="__cf_email__"
                                                data-cfemail="aedac1cacfd7dddbd8c7cdc6cfdceec9c3cfc7c280cdc1c3">[email&#160;protected]</span></a>
                                    </div>
                                </aside>
                            </div>
                            <div class="td-pb-span4">
                                <aside class="footer-social-wrap td-social-style-2">
                                    <div class="block-title"><span>FOLLOW US</span></div> <span
                                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                                            href="https://www.facebook.com/SuvicharHindiMe" title="Facebook"> <i
                                                class="td-icon-font td-icon-facebook"></i> </a> </span> <span
                                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                                            href="https://www.instagram.com/suvicharhindime/" title="Instagram"> <i
                                                class="td-icon-font td-icon-instagram"></i> </a> </span> <span
                                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                                            href="https://mix.com/aajkasuvichar" title="Mix"> <i
                                                class="td-icon-font td-icon-stumbleupon"></i> </a> </span> <span
                                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                                            href="https://in.pinterest.com/AajKaSuvichar" title="Pinterest"> <i
                                                class="td-icon-font td-icon-pinterest"></i> </a> </span> <span
                                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                                            href="https://t.me/AajKaSuvichar" title="Telegram"> <i
                                                class="td-icon-font td-icon-telegram"></i> </a> </span> <span
                                        class="td-social-icon-wrap"> <a target="_blank" rel="nofollow"
                                            href="https://twitter.com/suvicharhindime" title="Twitter"> <i
                                                class="td-icon-font td-icon-twitter"></i> </a> </span>
                                </aside>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="td-sub-footer-container td-container-wrap td_stretch_content">
                <div class="td-container">
                    <div class="td-pb-row">
                        <div class="td-pb-span td-sub-footer-menu">
                            <div class="menu-footer-menu-container">
                                <ul id="menu-footer-menu" class="td-subfooter-menu">
                                    <li id="menu-item-447"
                                        class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-first td-menu-item td-normal-menu menu-item-447">
                                        <a href="https://aajkasuvichar.com/">Home</a></li>
                                    <li id="menu-item-427"
                                        class="menu-item menu-item-type-post_type menu-item-object-page td-menu-item td-normal-menu menu-item-427">
                                        <a href="https://aajkasuvichar.com/about/">About</a></li>
                                    <li id="menu-item-428"
                                        class="menu-item menu-item-type-post_type menu-item-object-page td-menu-item td-normal-menu menu-item-428">
                                        <a href="https://aajkasuvichar.com/contact/">Contact</a></li>
                                    <li id="menu-item-429"
                                        class="menu-item menu-item-type-post_type menu-item-object-page td-menu-item td-normal-menu menu-item-429">
                                        <a href="https://aajkasuvichar.com/disclaimer/">Disclaimer</a></li>
                                    <li id="menu-item-382"
                                        class="menu-item menu-item-type-post_type menu-item-object-page td-menu-item td-normal-menu menu-item-382">
                                        <a href="https://aajkasuvichar.com/guest-posting/">Guest Posting</a></li>
                                    <li id="menu-item-383"
                                        class="menu-item menu-item-type-post_type menu-item-object-page menu-item-privacy-policy td-menu-item td-normal-menu menu-item-383">
                                        <a href="https://aajkasuvichar.com/privacy-policy-2/">Privacy Policy</a></li>
                                    <li id="menu-item-448"
                                        class="menu-item menu-item-type-post_type menu-item-object-page td-menu-item td-normal-menu menu-item-448">
                                        <a href="https://aajkasuvichar.com/cookies-policy/">Cookies Policy</a></li>
                                    <li id="menu-item-449"
                                        class="menu-item menu-item-type-post_type menu-item-object-page td-menu-item td-normal-menu menu-item-449">
                                        <a href="https://aajkasuvichar.com/terms-and-conditions/">Terms and
                                            Conditions</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="td-pb-span td-sub-footer-copy"> &copy;</div>
                    </div>
                </div>
            </div>
        </div>
    </div> <noscript>
        <style>
            .lazyload {
                display: none;
            }
        </style>
    </noscript>
    <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>
    <script data-noptimize="1">
        window.lazySizesConfig = window.lazySizesConfig || {};
        window.lazySizesConfig.loadMode = 1;
    </script>
    <script async data-noptimize="1"
        src='https://aajkasuvichar.com/wp-content/plugins/autoptimize/classes/external/js/lazysizes.min.js?ao_version=2.8.4'>
    </script>
    <script data-noptimize="1">
        function c_img(a, b) {
            src = "avif" == b ?
                "data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADybWV0YQAAAAAAAAAoaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAAAAADnBpdG0AAAAAAAEAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAABoAAAAoaWluZgAAAAAAAQAAABppbmZlAgAAAAABAABhdjAxQ29sb3IAAAAAamlwcnAAAABLaXBjbwAAABRpc3BlAAAAAAAAAAEAAAABAAAAEHBpeGkAAAAAAwgICAAAAAxhdjFDgQ0MAAAAABNjb2xybmNseAACAAIAAYAAAAAXaXBtYQAAAAAAAAABAAEEAQKDBAAAACJtZGF0EgAKCBgADsgQEAwgMgwf8AAAWAAAAACvJ+o=" :
                "data:image/webp;base64,UklGRhoAAABXRUJQVlA4TA0AAAAvAAAAEAcQERGIiP4HAA==";
            var c = new Image;
            c.onload = function () {
                var d = 0 < c.width && 0 < c.height;
                a(d, b)
            }, c.onerror = function () {
                a(!1, b)
            }, c.src = src
        }

        function s_img(a, b) {
            w = window, "avif" == b ? !1 == a ? c_img(s_img, "webp") : w.ngImg = "avif" : !1 == a ? w.ngImg = !1 : w
                .ngImg = "webp"
        }
        c_img(s_img, "avif");
        document.addEventListener("lazybeforeunveil", function ({
            target: a
        }) {
            window.ngImg && ["data-src", "data-srcset"].forEach(function (b) {
                attr = a.getAttribute(b), null !== attr && -1 == attr.indexOf("/client/to_") && a
                    .setAttribute(b, attr.replace(/\/client\//, "/client/to_" + window.ngImg + ","))
            })
        });
    </script> <noscript> <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PHM577N" height="0" width="0"
            style="display:none;visibility:hidden"></iframe> </noscript>
    <div id="amp-mobile-version-switcher" hidden> <a rel="amphtml"
            href="https://aajkasuvichar.com/aaj-ka-suvichar/?amp"> Go to mobile version </a></div>
    <script type='text/javascript'
        src='https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill.min.js?ver=7.4.4' id='wp-polyfill-js'>
    </script>
    <script type='text/javascript' id='wp-polyfill-js-after'>
        ('fetch' in window) || document.write(
            '<script src="https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill-fetch.min.js?ver=3.0.0"></scr' +
            'ipt>');
        (document.contains) || document.write(
            '<script src="https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill-node-contains.min.js?ver=3.42.0"></scr' +
            'ipt>');
        (window.DOMRect) || document.write(
            '<script src="https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill-dom-rect.min.js?ver=3.42.0"></scr' +
            'ipt>');
        (window.URL && window.URL.prototype && window.URLSearchParams) || document.write(
            '<script src="https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill-url.min.js?ver=3.6.4"></scr' +
            'ipt>');
        (window.FormData && window.FormData.prototype.keys) || document.write(
            '<script src="https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill-formdata.min.js?ver=3.0.12"></scr' +
            'ipt>');
        (Element.prototype.matches && Element.prototype.closest) || document.write(
            '<script src="https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill-element-closest.min.js?ver=2.0.2"></scr' +
            'ipt>');
        ('objectFit' in document.documentElement.style) || document.write(
            '<script src="https://aajkasuvichar.com/wp-includes/js/dist/vendor/wp-polyfill-object-fit.min.js?ver=2.3.4"></scr' +
            'ipt>');
    </script>
    <script type='text/javascript' id='contact-form-7-js-extra'>
        var wpcf7 = {
            "api": {
                "root": "https:\/\/aajkasuvichar.com\/wp-json\/",
                "namespace": "contact-form-7\/v1"
            }
        };
    </script>
    <script type='text/javascript' id='disqus_count-js-extra'>
        var countVars = {
            "disqusShortname": "aajkasuvichar"
        };
    </script>
    <script type='text/javascript' id='disqus_embed-js-extra'>
        var embedVars = {
            "disqusConfig": {
                "integration": "wordpress 3.0.22"
            },
            "disqusIdentifier": "56 https:\/\/aajkasuvichar.com\/2018\/10\/19\/aaj-ka-suvichar-%e0%a4%86%e0%a4%9c-%e0%a4%95%e0%a4%be-%e0%a4%b8%e0%a5%81%e0%a4%b5%e0%a4%bf%e0%a4%9a%e0%a4%be%e0%a4%b0\/",
            "disqusShortname": "aajkasuvichar",
            "disqusTitle": "Aaj Ka Suvichar 2021 |\u0906\u091c \u0915\u093e \u0938\u0941\u0935\u093f\u091a\u093e\u0930",
            "disqusUrl": "https:\/\/aajkasuvichar.com\/aaj-ka-suvichar\/",
            "postId": "56"
        };
    </script>
    <script type='text/javascript' id='aicp-js-extra'>
        var AICP = {
            "ajaxurl": "https:\/\/aajkasuvichar.com\/wp-admin\/admin-ajax.php",
            "nonce": "d0655e0f7e",
            "ip": "182.69.204.45",
            "clickLimit": "3",
            "clickCounterCookieExp": "3",
            "banDuration": "7",
            "countryBlockCheck": "No",
            "banCountryList": ""
        };
    </script>
    <script type='text/javascript' id='jquery-lazyloadxt-js-extra'>
        var a3_lazyload_params = {
            "apply_images": "",
            "apply_videos": "1"
        };
    </script>
    <script type='text/javascript' id='jquery-lazyloadxt-extend-js-extra'>
        var a3_lazyload_extend_params = {
            "edgeY": "0",
            "horizontal_container_classnames": ""
        };
    </script>
    <script type='text/javascript' id='ez-toc-js-js-extra'>
        var ezTOC = {
            "smooth_scroll": "1",
            "visibility_hide_by_default": "1",
            "width": "auto",
            "scroll_offset": "30"
        };
    </script>
    <script></script>
    <script defer
        src="https://aajkasuvichar.com/wp-content/cache/autoptimize/js/autoptimize_65dfb38ca93789aa92c8c566b5ed3e12.js">
    </script>
</body>

</html>
'''
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.body)
# print(soup.head.title)
# print(soup.findAll('p'))
print(r.status_code)
# print(pAll)
# print(r.text)
# print(read_content)
# print(soup)
# print(dir(r))
# print(help(r))
print(soup.find(class_='td-post-content tagdiv-type').get_text())


