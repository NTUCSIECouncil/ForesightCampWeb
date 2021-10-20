function clock() {
  hour = document.getElementById("hour");
  h = new Date().getHours();
  if (h < 10)
    hour.innerHTML = '0' + h;
  else
    hour.innerHTML = h;
  minute = document.getElementById("minute");
  m = new Date().getMinutes();
  if (m < 10)
    minute.innerHTML = '0' + m;
  else
    minute.innerHTML = m;
  second = document.getElementById("second");
  s = new Date().getSeconds();
  if (s < 10)
    second.innerHTML = '0' + s;
  else
    second.innerHTML = s;
}
setInterval(clock, 0.1);

