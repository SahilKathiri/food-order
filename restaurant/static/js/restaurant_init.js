$(document).ready(function() {

    $(".button-collapse").sideNav({
    	menuWidth: 300,
    	edge:'left',
    });

    $(".dropdown-button").dropdown();

    $("#table_search").keyup(function () {
        var value = this.value.toLowerCase().trim();

        $("#search_table tr").each(function (index) {
            if (!index) return;
            $(this).find("td").each(function () {
                var id = $(this).text().toLowerCase().trim();
                var not_found = (id.indexOf(value) == -1);
                $(this).closest('tr').toggle(!not_found);
                return not_found;
            });
        });
    });
});
