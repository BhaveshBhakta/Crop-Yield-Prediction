gsap.registerPlugin(ScrollTrigger);

const splitTypes = document.querySelectorAll('#reveal-type');

splitTypes.forEach((char) => {
  
    const text = char.innerText.split("").map((letter) => {
        const span = document.createElement('span');
        span.innerText = letter;
        return span;
    });

 
    char.innerHTML = '';
    text.forEach((span) => char.appendChild(span));

 
    gsap.from(char.children, {
        scrollTrigger: {
            trigger: char,        
            start: 'top 80%',      
            end: 'top 20%',        
            scrub: 2,            
            markers: false           
        },
        opacity: 0.2,             
        stagger: 0.3,
    });
});






const lenis = new Lenis()

lenis.on('scroll', (e) => {
  console.log(e)
})

function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}

requestAnimationFrame(raf)

