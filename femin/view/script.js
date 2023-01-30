function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

function isi_tabel(arr, keys, table) {
	let cell
	for (let i = 0; i < arr[keys[0]].length; i++) {
		row = table.insertRow(i+2);
		cell = row.insertCell(0)
		cell.style.textAlign = "center";
		//cell1.className = "alignRight"
		cell.innerHTML = (i+1);
		for (let j = 0; j < keys.length; j++) {
			cell = row.insertCell(j+1)
			cell.style.textAlign = "center";
			cell.innerHTML = arr[keys[j]][i]
		}
	}
}

function tableHist(hist_arr, hist_keys, ax_arr, ax_keys, hist_table){
  let valueHist = [[],[],[],[],[],[],[],[],[],[]];
  for (let keys = 0; keys < hist_keys.length; keys++){
    switch (hist_keys[keys].substring(0, hist_keys[keys].length - 2)){
      case "time":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[0].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "burnup":
        for (let bvalue = 0; bvalue < hist_arr[hist_keys[keys]].length; bvalue++){
          valueHist[1].push(hist_arr[hist_keys[keys]][bvalue]);
        }
        break;
      case "lhr":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[2].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "coolTemp":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[3].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "coolPress":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[4].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "nFlux":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[5].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "coolVelocity":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[6].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "iTime opt":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[7].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "iPrint opt":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[8].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
      case "iState opt":
        for (let value = 0; value < hist_arr[hist_keys[keys]].length; value++){
          valueHist[9].push(hist_arr[hist_keys[keys]][value]);
        }
        break;
    }
  }

  /* Creating Table */
  for (let i = 0; i < valueHist[1].length; i++){
    row = hist_table.insertRow(i+1);
    for (let j = 0; j < 10; j++){
      cell = row.insertCell(j)
      if (valueHist[j][i] === undefined){
        cell.style.textAlign = "center";
        cell.innerHTML = "--"
      } else {
        cell.style.textAlign = "right";
        cell.innerHTML = valueHist[j][i]
      }
    }
  }
}

function table_pwrprofile(ax_keys, ax, table_pwr){
  row = table_pwr.insertRow(1)
  for(let k=0; k< ax_keys.length;k++){
    cell = row.insertCell(k);
    cell.style.textAlign = "center";
    cell.innerHTML = (k+1)
  }
  for(let j = 0; j < ax[ax_keys[0]].length; j++){
    row = table_pwr.insertRow(j+2);
    cell = row.insertCell(0);
    cell.style.textAlign = "center";
    cell.innerHTML = (j+1);
    for(let i=0; i < (ax_keys.length); i++){
      cell = row.insertCell(i+1);
      cell.style.textAlign = "right";
      cell.innerHTML = ax[ax_keys[i]][j];
    } 
  }
  row = table_pwr.insertRow(ax[ax_keys[0].length + 2])
  cell = row.insertCell(0);
  cell.style.textAlign = "center";
  cell.innerHTML = "Avg Segment"
  for(let i=0; i<ax_keys.length; i++){
    cell = row.insertCell(i+1);
    cell.style.textAlign = "right";
    decimal = ax[ax_keys[i]].reduce((a, b) => a.length > b.length ? a : b);
    console.log(decimal.length);
    cell.innerHTML = ((ax[ax_keys[i]].map(Number).reduce((a,b) => a+b)) / ax[ax_keys[i]].length).toFixed(decimal.length-2);
  }
}
document.querySelector(".active").click();