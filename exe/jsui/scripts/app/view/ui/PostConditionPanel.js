// ===========================================================================
// eXe
// Copyright 2012, Pedro Peña Pérez, Open Phoenix IT
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//===========================================================================



Ext.define('eXe.view.ui.PostConditionPanel', {
    extend: 'Ext.panel.Panel',
    alias: 'widget.postconditionpanel',


    initComponent: function() {
        var me = this;

        var store =  Ext.data.StoreManager.lookup('combostore');
        var checkboxs = [];

        var te_textfield = {
            xtype: 'helpcontainer',
								item: {
									xtype: 'textfield',
                                    id: 'stuTimer',
									inputId: 'editorMode',
									dirtyCls: 'property-form-dirty',
									labelWidth: 150,
                                    margin: 10,
									fieldLabel: _('Time to study on this page'),
								},
								margin: 10,
								help: _('Enter time for learner to stay on this page after next page to be available')
        };
        checkboxs.push(te_textfield);

        store.load(function(){
            var outlineTreePanel1 = eXe.app.getController("Outline").getOutlineTreePanel();
            var selected1 = outlineTreePanel1.getSelectionModel().getSelection();

            if (selected1 != 0)
                var nodeid = selected1[0].data.id;

            store.each(function(records){
                //var nodeidd = nodeid;
                if (nodeid == records.index){
                    var texrStr = records.get('text');
                    if(texrStr.indexOf('Quiz') !== -1){

                        var unQuizz = parseInt(texrStr.charAt(texrStr.indexOf("Quiz")-2));
                        for(i = 1; i<=unQuizz;i++){
                            var boxlab = "Pass the " + i.toString() + " Quiz";
                            var boxid  = i.toString() + "Quiz";
                            var checked = {
                                xtype : 'checkbox',
                                boxLabel : boxlab, // field from store
                                id : boxid,   // field from store
                                toggleGroup : 'combostore',
                                margin: '0 5 3 5'
                            };
                            checkboxs.push(checked);
                        }
                    }
                }
            }); // end store.each

            var content = {
                title: 'Timmer and sequencing',
                xtype: 'fieldset',
                items: checkboxs // <---- object

            };
            me.insert(content); // this is necessary  to show your buttons in your panel
            me.doLayout();

        });
        me.callParent(arguments);
    }
});