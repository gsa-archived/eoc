function shorten(s, max){
    s = s.split(' ');
    cut = '';
    while (cut.length<=max && s.length){
        cut += s.shift() + ' ';
    }
    if (s.length) cut = cut.substring(0,cut.length-1) + '...'
    return cut
}
//let s = "Readability: the readability of the title is so-so. Having a dash (-) and pipe (|)in the title tag decreases readability. On top of that, the title is truncated which hurts the readability as well. Relevant keywords: the title tag is not very relevant - what does “Canada’s Top Business Law Firm” have to do with your search query? Besides, the keyword usage in the title tag is not good - the applicable keywords are at the end"
// s = shorten(s,60)
// console.log(s);

let origin = 'https://federalist-a1f29504-db06-4d32-992e-c2dadbfe82f2.sites.pages.cloud.gov';

let fullUrl = 'https://federalist-a1f29504-db06-4d32-992e-c2dadbfe82f2.sites.pages.cloud.gov/preview/gsa/eoc/feature/OMB-3-Release2.0-Demo/evidenceportal/ongoing/';

let index = fullUrl.indexOf(origin) + origin.length;
console.log(fullUrl.substring(index,fullUrl.length));