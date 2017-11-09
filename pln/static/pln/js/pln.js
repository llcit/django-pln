  // closeall
  $(document).on('click', '.closeall', function(e){
  $('.app > .panel-collapse.in').collapse('hide');
  $('.app > .panel-heading span.clickable').removeClass('panel-collapsed');
  $('.app > .panel-heading span.clickable').find('i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
  });
  // openall
  $(document).on('click', '.openall', function(e){
  $('.app > .panel-collapse:not(".in")').collapse('show');
  $('.app > .panel-heading span.clickable').addClass('panel-collapsed');
  $('.app > .panel-heading span.clickable').find('i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
  });
  // app clickable panel-heading
  $(document).on('click', '.app .panel-heading span.clickable', function(e){
    var $this = $(this);
  if(!$this.hasClass('panel-collapsed')) {
  	$this.addClass('panel-collapsed');
  	$this.find('i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
  } else {
  	$this.removeClass('panel-collapsed');
  	$this.find('i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
  }
  });
  // filter clickable panel-heading
  $(document).on('click', '.filter .panel-heading span.clickable', function(e){
    var $this = $(this);
  if(!$this.hasClass('panel-collapsed')) {
  	$this.addClass('panel-collapsed');
  	$this.find('i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
  } else {
  	$this.removeClass('panel-collapsed');
  	$this.find('i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
  }
  });
  // filter collapse on small devices
  $(document).ready(function(){
  var windowWidth = $(window).width();
  if(windowWidth <= 1024)
     $('.filter > .panel > .panel-collapse').removeClass('in')
  });
  $(window).resize(function(){
  var windowWidth = $(window).width();
  if(windowWidth <= 777) $('.filter > .panel > .panel-collapse').removeClass('in')
  if(windowWidth > 777) $('.filter > .panel > .panel-collapse').addClass('in')
  });
  // Filtering
  var $filterCheckboxes = $('input[type="checkbox"]');
  $filterCheckboxes.on('change', function() {
    var selectedFilters = {};
    $filterCheckboxes.filter(':checked').each(function() {
    if (!selectedFilters.hasOwnProperty(this.name)) {
        selectedFilters[this.name] = [];
    }
        selectedFilters[this.name].push(this.value);
    });
    var $filteredResults = $('.app');
    $.each(selectedFilters, function(name, filterValues) {
        $filteredResults = $filteredResults.filter(function() {
            var matched = false, currentFilterValues = $(this).data('category').split(' ');
            $.each(currentFilterValues, function(_, currentFilterValue) {
                if ($.inArray(currentFilterValue, filterValues) != -1) {
                    matched = true;
                    return false;
                }
            });
            return matched;
        });
    });
    $('.app').hide().filter($filteredResults).show();
  });
