
$(document).ready(function() {
    $(".popoverTrigger").on("mouseenter", function() {
        var popoverId = $(this).data("popover-id");
        $("#popover-" + popoverId).show().position({
            my: "center top",
            at: "center top+40",
            of: this
        });
    }).on("mouseleave", function() {
        var popoverId = $(this).data("popover-id");
        $("#popover-" + popoverId).hide();
    });
});
