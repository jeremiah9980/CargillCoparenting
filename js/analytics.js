const GA_ID = "G-139L5HHEPH";

var script = document.createElement("script");
script.async = true;
script.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;

document.head.appendChild(script);

window.dataLayer = window.dataLayer || [];

function gtag(){dataLayer.push(arguments);}

gtag('js', new Date());
gtag('config', GA_ID);
