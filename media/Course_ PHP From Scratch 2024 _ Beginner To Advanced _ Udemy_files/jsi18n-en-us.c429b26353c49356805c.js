(self["webpackChunkudemy_website"]=self["webpackChunkudemy_website"]||[]).push([["jsi18n-en-us"],{"./node_modules/@sentry/webpack-plugin/src/sentry-webpack.module.js":(e,t,n)=>{const i=typeof window!=="undefined"?window:typeof n.g!=="undefined"?n.g:typeof self!=="undefined"?self:{};i.SENTRY_RELEASE={id:"f00f5cd7cdcc7f873be61e8a9543c5016f7be1f2"};i.SENTRY_RELEASES=i.SENTRY_RELEASES||{};i.SENTRY_RELEASES["frontend@udemycom"]={id:"f00f5cd7cdcc7f873be61e8a9543c5016f7be1f2"}},"./src/udemy/js/utils/jsi18n-helpers.js":()=>{"use strict";window.ninterpolate=function e(t,n,i,r){let s=[i],o=false;if(r){s=r;o=true}return interpolate(ngettext(t,n,i),s,o)}},"./generated/locale/jsi18n/en-us.js":()=>{(function(){"use strict";{const e=this;const t=e.django||(e.django={});t.pluralidx=function(e){return e==1?0:1};t.catalog=t.catalog||{};if(!t.jsi18n_initialized){t.gettext=function(e){const n=t.catalog[e];if(typeof n==="undefined"){return e}else{return typeof n==="string"?n:n[0]}};t.ngettext=function(e,n,i){const r=t.catalog[e];if(typeof r==="undefined"){return i==1?e:n}else{return r.constructor===Array?r[t.pluralidx(i)]:r}};t.gettext_noop=function(e){return e};t.pgettext=function(e,n){let i=t.gettext(e+""+n);if(i.includes("")){i=n}return i};t.npgettext=function(e,n,i,r){let s=t.ngettext(e+""+n,e+""+i,r);if(s.includes("")){s=t.ngettext(n,i,r)}return s};t.interpolate=function(e,t,n){if(n){return e.replace(/%\(\w+\)s/g,(function(e){return String(t[e.slice(2,-2)])}))}else{return e.replace(/%s/g,(function(e){return String(t.shift())}))}};t.formats={DATETIME_FORMAT:"N j, Y, P",DATETIME_INPUT_FORMATS:["%Y-%m-%d %H:%M:%S","%Y-%m-%d %H:%M:%S.%f","%Y-%m-%d %H:%M","%m/%d/%Y %H:%M:%S","%m/%d/%Y %H:%M:%S.%f","%m/%d/%Y %H:%M","%m/%d/%y %H:%M:%S","%m/%d/%y %H:%M:%S.%f","%m/%d/%y %H:%M","%Y-%m-%d"],DATE_FORMAT:"N j, Y",DATE_INPUT_FORMATS:["%Y-%m-%d","%m/%d/%Y","%m/%d/%y"],DECIMAL_SEPARATOR:".",FIRST_DAY_OF_WEEK:0,MONTH_DAY_FORMAT:"F j",NUMBER_GROUPING:3,SHORT_DATETIME_FORMAT:"m/d/Y P",SHORT_DATE_FORMAT:"m/d/Y",THOUSAND_SEPARATOR:",",TIME_FORMAT:"P",TIME_INPUT_FORMATS:["%H:%M:%S","%H:%M:%S.%f","%H:%M"],YEAR_MONTH_FORMAT:"F Y"};t.get_format=function(e){const n=t.formats[e];if(typeof n==="undefined"){return e}else{return n}};e.pluralidx=t.pluralidx;e.gettext=t.gettext;e.ngettext=t.ngettext;e.gettext_noop=t.gettext_noop;e.pgettext=t.pgettext;e.npgettext=t.npgettext;e.interpolate=t.interpolate;e.get_format=t.get_format;t.jsi18n_initialized=true}}}).call(window)}},e=>{var t=t=>e(e.s=t);var n=(t("./node_modules/@sentry/webpack-plugin/src/sentry-webpack.module.js"),t("./generated/locale/jsi18n/en-us.js"),t("./src/udemy/js/utils/jsi18n-helpers.js"))}]);
//# sourceMappingURL=jsi18n-en-us.c429b26353c49356805c.js.map