(function($) {
            $(document).ready(function() {
		    CKEDITOR.disableAutoInline = true;
		    //CKEDITOR.replace('id_data');
		    //CKEDITOR.replace( 'id_data', {
             //  		 extraPlugins: 'mathjax',
	   	 //    	 height: 350
	   	 //   });

			$("textarea").each(function(index,val){
				CKEDITOR.replace( $(val).attr('id'),
					{extraPlugins: 'mathjax'}
				);
			});
	   })	
        })(django.jQuery);
