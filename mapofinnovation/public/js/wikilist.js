var type_filter = document.getElementById('filter_type').value;
var name_filter = document.getElementById('filter_name').value;
var name_f = name_filter.replace("+"," ");
$.get('/searchapi/findSpacesByType',{'type':type_filter,'name':name_f}, function(spaces) {
	if(spaces!="")
	{
   for (i=0; i<spaces.length; ++i) {	
		var spaceitem = spaces[i];
		$('#wiki-list-content ul').append(
    $('<li>').append(
        $('<a>').attr('href',spaceitem["wiki"]).append(
            $('<span>').attr('class', 'tab').append(spaceitem["name"])
))); 
		}
   	}
	  else {
	 $('#wiki-list-content ul').append(
    $('<li>').append(
            $('<span>').attr('class', 'tab').append("There are no spaces with these details")
));
}
});


