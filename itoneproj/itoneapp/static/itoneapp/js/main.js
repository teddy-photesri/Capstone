
// Start Range Scale

let input_intensity = document.querySelector('#input_intensity')
let label_intensity = document.querySelector('#label_intensity')
let change_emotion = document.getElementById('change_emotion')
input_intensity.addEventListener('input', function() {
  // label_intensity.innerText = 'Intensity: ' + input_intensity.value
  label_intensity.innerText = input_intensity.value
})
// End Range Scale



let emos = document.querySelectorAll('.emo_icon')
let emotions = ['Joy', 'Love', 'Surprise', 'Anger', 'Sadness', 'Fear']
// console.log(emos)
for (let i=0; i<emos.length; ++i) {
  emos[i].addEventListener('click', function() {

    change_emotion.value = emotions[i]
    console.log(emos[i].dataset.name)
    for (let j=0; j<emos.length; ++j) {
      if (emos[j] != this) {
        emos[j].style.opacity = 0.2
      } else {
        emos[j].style.opacity = 1
      }
    }
  })
}
