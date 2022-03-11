var lock = false;
function submit_check(f){
	if (lock) {
		alert("waiting..");
		return false;
	}
	lock = true;
	var key = f.key.value;
	if (key == "") {
		alert("please fill the input box.");
		lock = false;
		return false;
	}

	submit(key);

	return false;
}

function submit(key){
	$.ajax({
		type : "POST",
		async : false,
		url : "./index.php",
		data : {json:JSON.stringify({key: key})},
		dataType : 'json'
	}).done(function(result){
		if (result['code'] == true) {
			document.write("Congratulations! flag is " + result['flag']);
		} else {
			alert("nope...");
		}
		lock = false;
	});
}
