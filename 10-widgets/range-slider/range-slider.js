(function() {
    "use strict";

    function RangeSlider(selector, params) {
        this.$element = $(selector);
        this.$base = $('<div class="range-slider-base">');
        this.$leftHandle = $('<div class="range-slider-handle">');
        this.$rightHandle = $('<div class="range-slider-handle">');

        this.$base.append(this.$leftHandle).append(this.$rightHandle);
        this.$element.append(this.$base);
    }

    window.RangeSlider = RangeSlider;
})();