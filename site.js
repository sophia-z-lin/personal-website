/* Progressive enhancement: links and content work without JavaScript. */
const progress=document.querySelector('.reading-progress');
let queued=false;
function updateProgress(){const range=document.documentElement.scrollHeight-innerHeight;progress.style.width=`${range>0?Math.min(100,scrollY/range*100):0}%`;queued=false;}
addEventListener('scroll',()=>{if(!queued){queued=true;requestAnimationFrame(updateProgress)}},{passive:true});
addEventListener('resize',updateProgress);updateProgress();
document.querySelectorAll('[data-video] .video-cover').forEach(link=>link.addEventListener('click',event=>{
  if(event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
  event.preventDefault();const container=link.parentElement;
  const frame=document.createElement('iframe');
  frame.src=`https://www.youtube-nocookie.com/embed/${container.dataset.video}?autoplay=1&rel=0`;
  frame.title=link.getAttribute('aria-label');frame.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';frame.allowFullscreen=true;
  frame.referrerPolicy='strict-origin-when-cross-origin';container.replaceChildren(frame);frame.focus();
}));
