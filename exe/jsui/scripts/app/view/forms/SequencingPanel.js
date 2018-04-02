// ===========================================================================
// eXe
// Copyright 2013, Pedro Peña Pérez, Open Phoenix IT
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
Ext.define('eXe.view.forms.SequencingPanel', {
    extend: 'Ext.form.Panel',
    alias: 'widget.sequencing',

    refs: [
        {
            selector: '#outline_treepanel',
            ref: 'outlineTreePanel'
        },

    ],

    initComponent: function () {
        var me = this;
        var lngsel = _("Available when");
        var seqTarget = null;
        Ext.applyIf(me, {
            autoScroll: true,
            trackResetOnLoad: true,
            url: 'sequencing',
            bodyPadding: 4,
            items: [{
                xtype: 'tabpanel',
                height: 310,
                activeTab: 0,
                plain: true,
                items: [
					// Tab 0
					{
						title: _('sequencing Settings'),
						bodyPadding: 10,
						items: [{
							xtype: 'container',
							layout: 'hbox',
							//layout:'column',
							border: 1,
							margin: 10,
							width: '94%',
							items: [{
							    xtype: 'combobox',
                                id: 'seqTarget',
							inputId: 'locale',
							dirtyCls: 'property-form-dirty',
							fieldLabel: _("Available when: "),
							labelWidth: 130,
							margin: 10,
							queryModel: 'local',
							displayField: 'text',
							valueField: 'value',
							store: {
								fields: ['value', 'text'],
								proxy: {
									type: 'ajax',
									url: 'sequencing',
									reader: {
										type: 'json',
										root: 'Nodes'

									}
								},

								autoLoad: true
									}
								}
							]
						}]
					},

				],
            }, {
                xtype: 'container',
                layout: 'hbox',
                style: {
					marginTop: '10px'
				},
                items: [{
                    xtype: 'button',
                    text: _('Save'),
                    handler: function (button) {
                        var formpanel = button.up('form'),
                            form = formpanel.getForm(),

                            outlineTreePanel = eXe.app.getController("Outline").getOutlineTreePanel(),
                            selected = outlineTreePanel.getSelectionModel().getSelection();
                        var targetID = Ext.getCmp('seqTarget').getValue();
                        var targetRecord = Ext.getCmp('seqTarget').findRecordByValue(targetID),
                        index = Ext.getCmp('seqTarget').getStore().indexOf(targetRecord);
                            scope: this,
                            nodeid = '0';

    	                if (selected != 0)
    		                nodeid = selected[0].data.id;

                        form.submit({
                            success: function () {
                                if (nodeid == index){
                                    Ext.Msg.alert('PLease select a valid target:');
                                }
                                else{
                                    nevow_clientToServerEvent('AddTarget',this, '', nodeid, index);
                                    form.hide();
                                }

                            },
                            failure: function (form, action) {
                                Ext.Msg.alert(_('Error'), action.result.errorMessage);
                            }
                        });
                    },
                    itemId: 'save_sequencing'
                }, {
                    xtype: 'component',
                    flex: 1
                },
				]
            }]
        });

        me.callParent(arguments);
    }

});