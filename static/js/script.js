
$(document).ready(function() {
    $(".popoverTrigger").on("mouseenter", function() {
        var popoverId = $(this).data("popover-id");
        $("#popover-" + popoverId).show().position({
            my: "right top",
            at: "right+150 top",
            of: this
        });
    }).on("mouseleave", function() {
        var popoverId = $(this).data("popover-id");
        $("#popover-" + popoverId).hide();
    });
});
