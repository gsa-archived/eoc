// Add your custom javascript here
console.log("Hi from Federalist");

(function(){
    let forcedUrl = null;
    let lockActive = false;
    function buildForcedUrl(href){
      href = href.trim();
      if(href.indexOf(window.location.origin) === 0)return href;
      return window.location.origin+href;
    }
    const originalAssign = window.location.assign;
    const originalReplace = window.location.replace;
    const originalPushState = history.pushState;
    const originalReplaceState = history.replaceState;
    window.location.assign = function(url){
      if(lockActive)return;
      forcedUrl = buildForcedUrl(url);
      lockActive = true;
      originalReplace.call(window.location,forcedUrl);
    };
    window.location.replace = function(url){
      if(lockActive)return;
      forcedUrl = buildForcedUrl(url);
      lockActive = true;
      originalReplace.call(window.location,forcedUrl);
    };
    try{
      const proto = Object.getPrototypeOf(window.location);
      const desc = Object.getOwnPropertyDescriptor(proto,"href");
      if(desc && desc.configurable){
        Object.defineProperty(proto,"href",{
          set: function(val){
            if(lockActive)return;
            forcedUrl = buildForcedUrl(val);
            lockActive = true;
            originalReplace.call(window.location,forcedUrl);
          },
          get: desc.get,
          configurable: false,
          enumerable: true
        });
      }
    }catch(e){}
    history.pushState = function(state,title,url){
      if(lockActive)return;
      if(url){
        forcedUrl = buildForcedUrl(url);
        lockActive = true;
        originalReplace.call(window.location,forcedUrl);
      } else {
        originalPushState.apply(history,arguments);
      }
    };
    history.replaceState = function(state,title,url){
      if(lockActive)return;
      if(url){
        forcedUrl = buildForcedUrl(url);
        lockActive = true;
        originalReplace.call(window.location,forcedUrl);
      } else {
        originalReplaceState.apply(history,arguments);
      }
    };
    const origAddEventListener = EventTarget.prototype.addEventListener;
    EventTarget.prototype.addEventListener = function(type,listener,options){
      if(type==='click'){
        const wrapped = function(e){
          if(lockActive){
            e.stopImmediatePropagation();
            return;
          }
          return listener.apply(this,arguments);
        };
        return origAddEventListener.call(this,type,wrapped,options);
      }
      return origAddEventListener.call(this,type,listener,options);
    };
    document.addEventListener('click',function(e){
      if(lockActive){
        e.stopImmediatePropagation();
        return;
      }
      let el = e.target;
      while(el && el!==document){
        if(el.tagName==='A'){
          const href = el.getAttribute('href');
          if(href && !href.startsWith('javascript:')){
            e.preventDefault();
            e.stopImmediatePropagation();
            forcedUrl = buildForcedUrl(href);
            lockActive = true;
            originalReplace.call(window.location,forcedUrl);
          }
          break;
        }
        el = el.parentElement;
      }
    },true);
    ['mousedown','mouseup','touchstart','touchend'].forEach(function(type){
      document.addEventListener(type,function(e){
        if(lockActive)e.stopImmediatePropagation();
      },true);
    });
    const observer = new MutationObserver(function(mutations){
      if(lockActive && forcedUrl && window.location.href!==forcedUrl){
        originalReplace.call(window.location,forcedUrl);
      }
      mutations.forEach(function(mutation){
        if(mutation.type==='childList'){
          Array.from(mutation.addedNodes).forEach(function(node){
            if(node.nodeType===Node.ELEMENT_NODE && node.tagName==='META'){
              if(node.getAttribute('http-equiv') && node.getAttribute('http-equiv').toLowerCase()==='refresh'){
                node.parentNode && node.parentNode.removeChild(node);
              }
            }
          });
        }
      });
    });
    observer.observe(document.documentElement,{childList:true,subtree:true,attributes:true});
    window.addEventListener('popstate',function(){
      if(lockActive && forcedUrl && window.location.href!==forcedUrl){
        originalReplace.call(window.location,forcedUrl);
      }
    });
    window.addEventListener('hashchange',function(){
      if(lockActive && forcedUrl && window.location.href!==forcedUrl){
        originalReplace.call(window.location,forcedUrl);
      }
    });
    setInterval(function(){
      if(lockActive && forcedUrl && window.location.href!==forcedUrl){
        originalReplace.call(window.location,forcedUrl);
      }
    },10);
  })();
  
  

// Add a new class for all of the external anchor tags
$("a").each(function(index, element) {
    if (!$(element).attr("href").startsWith('https://www.evaluation.gov' && 'javascript:void(0)')
        && !$(element).hasClass('usa-link--external')
        && !$(element).hasClass('external-link-off')
        && this.host !== location.host){
        if ($(element).hasClass('usa-link--external-white'))
            $(element).addClass("usa-link--external-white");
        else
            $(element).addClass("usa-link--external");
        }
});

jQuery(document).ready(function ($) {
    // Agencies page.
    // Slide toggle Annual Evaluation Plan.
    $('a.eval-plan-link').on('click', function() {
        $(this).toggleClass('expanded');
        $('.eval-plan').slideToggle('fast');
        return false;
    });

    // Hide Evaluation plan links on click.
    $(document).on("click", function(event){
        if(!$(event.target).closest(".eval-plan").length){
            if($(".eval-plan").is(":visible")){
                $(".eval-plan").slideUp('fast');
                $('a.eval-plan-link').removeClass('expanded');
            }
        }
    });
});
