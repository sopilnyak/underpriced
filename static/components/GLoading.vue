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
            $(document).ready(function() {
            function runAnimation() {
                let loadingLeft = $('.loading-1');
                loadingLeft.animate({opacity:'1'}, 600);
                loadingLeft.animate({opacity:'0.5'}, 600, runAnimation);
            setTimeout(function() {
                let loadingCenter = $('.loading-2');
                loadingCenter.animate({opacity: '1'}, 600);
                loadingCenter.animate({opacity: '0.5'}, 600, runAnimation);
                }, 300);
            setTimeout(function() {
                let loadingRight = $('.loading-3');
                loadingRight.animate({opacity: '1'}, 600);
                loadingRight.animate({opacity: '0.5'}, 600, runAnimation);
                }, 600);
            }
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
    }

    .loading-2 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(55,80,132,1.0);
        opacity: 0.5;
    }

    .loading-3 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(55,80,132,1.0);
        opacity: 0.3;
    }

    .loading {
        margin: 50px auto;
        width: 100%;
        text-align: center;
    }
</style>
