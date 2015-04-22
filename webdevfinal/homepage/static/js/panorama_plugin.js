/**
 * Created by mhelvey on 4/21/15.
 */

(function ( $ ) {
    $.fn.panorama = function(options){
        var screen_width = screen.width;
        options = $.extend(true, {
            option: 'value'
        }, options);

        $(this).hover(function(){
            $(this).children("span").toggleClass("display-span");

        });

        //$(this).mouseenter(function(){
        //
        //    $(this).children("span").addClass("display-span");
        //
        //});

        //$(this).hover()
        //    .children("img").toggleClass("rollover", 100);
        //$(this).hover()
        //    .children("span").toggleClass("display-span");
        //
        return this;
    };
}( jQuery ));