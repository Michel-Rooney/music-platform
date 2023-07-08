

const pause = document.getElementById('pause');
const play = document.getElementById('play')
const audio = document.getElementById('audio1');
pause.style.display = 'none';

const musicSound = document.getElementById('music-sound');
console.log(musicSound)


function playMusic() {
  play.style.display = 'none';
  pause.style.display = 'block';
  audio.play();
}

function pauseMusic() {
  play.style.display = 'block';
  pause.style.display = 'none';
  audio.pause();
}