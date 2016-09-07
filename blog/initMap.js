if (jQuery != undefined) {
    var django = {
        'jQuery': jQuery,
    }
}

$(document).ready(function() {
      var latlng = new google.maps.LatLng("{{ latitude }}", "{{ longitude }}");
      var mapOptions = {
          zoom: 15,
          center: latlng,
          mapTypeControl: false,
          navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL},
          mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      map = new google.maps.Map($('.map')[0], mapOptions);

      var marker = new google.maps.Marker({
          position: latlng,
          map: map,
          title:"Jesteś tutaj"
      });

          latlng = new google.maps.LatLng("{{ post.position[0] }}", "{{ post.position[1] }}");
          new google.maps.Marker({
              position: latlng,
              map: map,
              title:"{{ shop.name }}"
          });
  });(django.jQuery);
