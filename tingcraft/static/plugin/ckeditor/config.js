/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    config.toolbarGroups = [
        { name: 'document', groups: [ 'mode'] }, // shows the source button
        { name: 'pbckcode' } ,                   // shows the pbckcode button
    ];
    config.extraPlugins = 'pbckcode';
    config.pbckcode = {
        modes :  [ ['C++', 'c_pp'], ['Python', 'py'] ],
        theme : 'clouds',
        highlighter : "PRETTIFY"
    };
};
