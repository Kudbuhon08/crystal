
const toggle_question = (el,img) => {
  el.style.height = el.style.height =='150px'?'40px':'150px'
  img.style.transform == 'rotate(0deg)'?img.style.transform='rotate(-90deg)':img.style.transform='rotate(0deg)'
};

const allQE = document.querySelectorAll(".questions_item ")
const allQEImg = document.querySelectorAll(".questions_item img")


for(let i =0;i<allQE.length;i++){
    allQE[i].onclick = ()=>toggle_question(allQE[i],allQEImg[i])
}


//   .addEventListener("click", toggle_question);
// ACCORDION END
