var jQuery = require('jquery');
jQuery(function(){
  jQuery(".hello-btn").click(function(){
    alert("hello");
    return false;
  });
});
