{% block extra_js %}
    <script>
        $(document).ready(function () {
            $('#myStaticDatatable').DataTable({

            'columns':[
               {'data1':'labels'},
               {'data1':'data'},
               ]
            });
        });
    $.fn.DataTable.ext.errMode='throw';
    </script>
{% endblock %}