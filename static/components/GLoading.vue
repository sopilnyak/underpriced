<template>
    <div class="loading">
        <span class="loading-1"></span>
        <span class="loading-2"></span>
        <span class="loading-3"></span>
        <br>
        Пожалуйста, подождите...
    </div>
</template>

<script>
    export default {
        name: 'GLoading',
        mounted() {
            let animationDuration = 700;
            $(document).ready(function() {
                let loadingLeft = $('.loading-1');
                let loadingCenter = $('.loading-2');
                let loadingRight = $('.loading-3');
                function runAnimation() {
                    loadingLeft.animate({opacity:'1'}, animationDuration);
                    loadingLeft.animate({opacity:'0.5'}, animationDuration, runAnimation);
                    loadingCenter.animate({opacity: '1'}, animationDuration);
                    loadingCenter.animate({opacity: '0.5'}, animationDuration, runAnimation);
                    loadingRight.animate({opacity: '1'}, animationDuration);
                    loadingRight.animate({opacity: '0.5'}, animationDuration, runAnimation);
                }
                loadingLeft.animate({opacity: '1'}, animationDuration);
                loadingLeft.animate({opacity:'0.5'}, animationDuration, runAnimation);
                loadingCenter.delay(animationDuration / 3).animate({opacity: '1'}, animationDuration);
                loadingCenter.animate({opacity: '0.5'}, animationDuration, runAnimation);
                loadingRight.delay(animationDuration * 2 / 3).animate({opacity: '1'}, animationDuration);
                loadingRight.animate({opacity: '0.5'}, animationDuration, runAnimation);
                runAnimation();
            });
        }
    }
</script>

<style scoped>

    .loading-1 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(55,80,132,1.0);
        opacity: 0.5;
    }

    .loading-2 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(55,80,132,1.0);
        opacity: 0.75;
    }

    .loading-3 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(55,80,132,1.0);
        opacity: 0.8;
    }

    .loading {
        margin: 50px auto;
        width: 100%;
        text-align: center;
    }
</style>
