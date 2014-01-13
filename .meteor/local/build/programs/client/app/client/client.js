(function(){Template.hello.events({
"click #submit" : function(e) {
	var csv = CSVToArray(document.getElementById("data").value);
	document.getElementById("data").value = "";
	for(var i = 0; i < csv.length; i++) {
		var array = csv[i];
		if(array[1].indexOf("@") == -1) {
			array[1] = array[1] + "@uw.edu";
		}
		if(array.length != 4 || array[1].indexOf("@") == -1 || array[2].search(/\d/) == -1) {
			console.log("Something was wrong with params: " + csv[i]);
		} else {
			Meteor.call(	'sendEmail',
            				array[1],
					"cse331-staff@cs.washington.edu",
            				"Late Days Requested: " + array[2],
            				"Hi, you requested " + array[2] + " lateday(s).");
			console.log("Success: " + array[1] + ": " + array[2]);
		}
	}
}
});

})();
