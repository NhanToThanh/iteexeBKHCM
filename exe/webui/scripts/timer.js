var hours;
var mins;
var secs;
var counting;

function stopCounting() {
	counting = false;
}

function setMaxTimeAllow(total_sec) {
	counting = true;
	hours = Math.floor(total_sec / 3600);
	mins = Math.floor((total_sec % 3600) / 60);
	secs = Math.floor((total_sec % 3600) % 60) + 1;
	redo();	  
}


function RecordTest(){
        scorm.SetCompletionStatus('completed');
        scorm.SetSuccessStatus('passed');
        scorm.save()
    }

function redo() {
	if(counting == false) {
		return;
	}
	
	secs--;
	if(secs == -1) {
		secs = 59;
		mins--;
	}
	if (mins == -1) {
		mins = 59;
		hours--;
	}

	if (hours == 0) {
		if (mins == 0) {
			if (secs == 0) {
				RecordTest();
			} else {
				cd = setTimeout("redo()",1000);
			}
		} else {
			cd = setTimeout("redo()",1000);
		}
	} else {
		cd = setTimeout("redo()",1000);
	}
}