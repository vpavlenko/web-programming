(function() {
    "use strict";

    function makeDraggable($handle, $base) {
        $handle.draggable({
            containment: $base,
            scroll: false,
            axis: "x"
        });
    }

    function map(x, in_min, in_max, out_min, out_max) {
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    }

    function RangeSlider(selector, params) {
        this.$element = $(selector);
        this.$base = $('<div class="range-slider-base">');
        this.$leftHandle = $('<div class="range-slider-handle range-slider-handle-left">L');
        this.$rightHandle = $('<div class="range-slider-handle range-slider-handle-right">R');

        this.$base.append(this.$leftHandle).append(this.$rightHandle);
        this.$element.append(this.$base);

        makeDraggable(this.$leftHandle, this.$base);
        makeDraggable(this.$rightHandle, this.$base);

        this.range = params.range;
        this.value(params.start);
    }

    RangeSlider.prototype.value = function(value) {
        if (value) {
            this.$leftHandle.css('left', map(value[0], this.range[0], this.range[1], 0, this.$base.width()));
            this.$rightHandle.css('right', map(value[1], this.range[0], this.range[1], this.$base.width(), 0));
            return this;
        } else {
            return this.value;
        }
    };

    window.RangeSlider = RangeSlider;
})();