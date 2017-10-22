<template>
    <div id="main">
        <g-header></g-header>
        <list-header></list-header>
        <router-view></router-view>
        <g-footer></g-footer>
    </div>
</template>

<script>
    import GHeader from './GHeader.vue'
    import GFooter from './GFooter.vue'
    import GLoading from './GLoading.vue'
    import ListHeader from './ListHeader.vue'

    export default {
        name: 'main',
        components: {
            GHeader,
            ListHeader,
            GFooter,
            GLoading
        }
    }
</script>

<style>
    body {
        margin: 0;
        color: #313334;
        font-family: "Open Sans";
        font-size: 14px;
        background-color: #f3faec;
        min-width: 1000px;
    }

    .number {
        display: inline;
        margin: 4px 4px;
    }

    .left-arrow {
        display: inline;
        margin: 4px 4px;
        text-decoration: underline;
    }

    .right-arrow {
        display: inline;
        margin: 4px 4px;
        text-decoration: underline;
    }

    .left-arrow.disabled {
        display: none;
    }
    .right-arrow.disabled {
        display: none;
    }

    .left-arrow:hover {
        cursor: pointer;
    }

    .right-arrow:hover {
        cursor: pointer;
    }

    .number:not(.active) {
        text-decoration: underline;
    }

    .number:hover:not(.active) {
        cursor: pointer;
    }

    ul {
        margin: 0;
        padding: 0;
    }

    .underpriced {
        width: 100%;
    }

    .filters {
        padding: 20px 40px;
    }

    select {
        -webkit-appearance: button;
        -webkit-border-radius: 2px;
        -webkit-padding-end: 20px;
        -webkit-padding-start: 2px;
        -webkit-user-select: none;
        background-image: url(http://i62.tinypic.com/15xvbd5.png);
        background-color: #FFFFFF;
        background-position: 97% center;
        background-repeat: no-repeat;
        border: 1px solid #00ACC1;
        color: #555;
        font-size: 15px;
        overflow: hidden;
        padding: 5px 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 160px;
        margin-right: 10px;
    }

    select:hover {
        cursor: pointer;
    }

    .button {
        -webkit-appearance: button;
        -webkit-border-radius: 2px;
        background-color: #E0F7FA;
        border: 1px solid #00ACC1;
        color: #555;
        overflow: hidden;
        padding: 5px 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: inline-block;
        text-decoration: none;
        margin-top: 10px;
    }

    .button:hover {
        cursor: pointer;
    }

    input {
        -webkit-border-radius: 2px;
        padding: 5px 10px;
        border: 1px solid #00ACC1;
        color: #555;
        font-size: 15px;
        overflow: hidden;
        padding: 5px 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 160px;
        margin-right: 10px;
    }

    .entry {
        display: block;
        margin: 20px 0;
        border: 1px solid #00ACC1;
        -webkit-border-radius: 2px;
        padding: 20px 30px;
    }

    .entry:hover {
        background-color: #B2EBF2;
        border-color: #00838F;
    }

    .image-column {
        float: left;
        width: 250px;
        margin-right: 30px;
    }

    .flat-image {
        width: 250px;
    }

    .first-column {
        float: left;
        width: 20%;
    }

    .second-column {
        float: left;
        width: 30%;
    }

    .third-column {
        float: right;
        text-align: right;
    }

    br {
        clear: both;
    }

    .actual-price {
        font-size: 30px;
        color: #424445;
    }

    .actual-price-hint {
        color: gray;
        font-size: 18px;
        margin-left: 2px;
    }

    .predicted-price-title {
        color: gray;
        font-size: inherit;
    }

    .predicted-price-hint {
        color: gray;
        font-size: 15px;
    }

    .source {
        font-size: 10px;
        color: gray;
        text-decoration: none;
    }

    .subway {
        font-weight: bold;
    }

    .location {
        font-size: 12px;
    }

    .district {
        display: block;
        margin-top: 5px;
    }

    .rooms {

    }

    .rooms-hint {
        color: gray;
    }

    .area {

    }

    .area-hint {
        color: gray;
    }

    .floor {

    }

    .external {
        display: block;
        margin-top: 3px;
    }

</style>
