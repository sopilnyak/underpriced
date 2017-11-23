<template>
    <div id="main" class="content">
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
    html {
        height: 100%;
    }

    body {
        position: relative;
        min-height: 100%;
        margin: 0;
        color: #313334;
        font-family: "Open Sans", Helvetica;
        font-size: 14px;
        background-color: #EDEFF1;
        min-width: 1250px;
    }

    .content {
        padding-bottom: 30px;
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
        padding: 20px 0 20px 40px;
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
        border: 1px solid #375084;
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

    *:focus {
    outline: none;
        border: 1px solid #010B20;
    }

    .button {
        -webkit-box-shadow: 1px 1px 5px 0 rgba(0,0,0,0.35);
        -moz-box-shadow: 1px 1px 5px 0 rgba(0,0,0,0.35);
        box-shadow: 1px 1px 5px 0 rgba(0,0,0,0.35);
        -webkit-border-radius: 2px;
        background-color: #375084;
        border: 1px solid #375084;
        color: #EDEFF1;
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
        border: 1px solid #375084;
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
        margin: 20px 30px 20px 0;
        border: 1px solid #375084;
        -webkit-border-radius: 2px;
        padding: 20px 30px;
    }

    .entry:hover {
        background-color: rgba(171,181,202,0.25);
        border-color: #010B20;
    }

    .image-column {
        float: left;
        width: 250px;
        margin-right: 30px;
    }

    .flat-image {
        width: 250px;
        height: 120px;
        background-position: center center;
        background-repeat: no-repeat;
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

    .predicted-price {
        font-size: 30px;
        color: #424445;
    }

    .predicted-price-hint {
        color: gray;
        font-size: 18px;
        margin-left: 2px;
    }

    .actual-price-title {
        color: gray;
        font-size: inherit;
    }

    .actual-price-hint {
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

    .sort-container {
        display: inline-block;
        padding: 0.3em 0 0 0.5em;
        height: 2em;
        font-weight: bold;
        cursor: pointer;
    }

    .filter {
        padding: 3px;
        font-size: 13px;
    }

    .pagination-block {
        width: 100%;
        overflow: hidden;
    }

    .shareFB {
        float: right;
        margin-right: 30px;
    }

    .shareVK {
        float: right;
        margin-right: 10px;
    }

    .dropdown-hidden {
        display: none;
    }

    .dropdown {
        display: block;
        position: absolute;
        margin-top: 5px;
    }

    .dropdown-entry {
        width: 16.3em;
        padding: 5px 10px;
        background-color: rgba(217,219,221,0.70);
    }

    .dropdown-entry:hover {
        background-color: #8C9AB6;
        color: #ffffff;
    }

    .filter-underground {
        width: 8em;
    }

    .filter-distance {
        width: 8em;
    }

    .filter-distance-type {
        margin-left: 0.7em;
    }

</style>
