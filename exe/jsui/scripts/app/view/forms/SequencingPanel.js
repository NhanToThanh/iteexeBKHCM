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
    requires: [
        'eXe.view.ui.PostConditionPanel',
        'eXe.view.ui.PreConditionPanel',
    ],
    alias: 'widget.sequencing',

    refs: [
        {
            selector: '#outline_treepanel',
            ref: 'outlineTreePanel'
        },
    ],

    initComponent: function () {
        var me = this;
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
                        title: _('Preconditions'),
                        //bodyPadding: 10,
                        items: [{
                            bodyPadding: 10,
                            xtype: 'preconditionpanel'
                        }]

                    },//Tab Precondition

                    { //Tab Postcondition
                        title: _('Postconditions'),
                        items: [{
                            bodyPadding: 10,
                            xtype: 'postconditionpanel'
                        }]
                    },//Tab Postcondition

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
                        var studyTimer = Ext.getCmp('stuTimer').getValue();
                        var checkSome = false;
                        var checkAny = false;
                        var quizArray = [];
                        if (Ext.getCmp('anycon')) {
                            //checkAny = true;
                            if (Ext.getCmp('anycon').getValue()) {
                                checkAny = true;
                                quizArray[0] = 1;
                                for (j = 1; j <= 10; j++) {
                                    var box_id = j.toString() + "Quiz";
                                    if (Ext.getCmp(box_id))
                                        quizArray[j] = 1;
                                    else
                                        break;

                                }
                            } else {
                                //kiem tra dieu kien some
                                for (k = 1; k < 10; k++) {
                                    var sbox_id = k.toString() + "Quiz";
                                    if (Ext.getCmp(sbox_id)) {
                                        if (Ext.getCmp(sbox_id).getValue())
                                            checkSome = true;
                                    }
                                    else
                                        break;

                                }// end checkSome

                                if (checkSome) {
                                    quizArray[0] = 0;
                                    for (j = 1; j <= 10; j++) {
                                        var box_id = j.toString() + "Quiz";
                                        if (Ext.getCmp(box_id)) {
                                            if (Ext.getCmp(box_id).getValue()) {
                                                quizArray[j] = 1;
                                            } else
                                                quizArray[j] = 0;

                                        } else
                                            break;
                                    }//for
                                }

                            }
                        }
                        else {
                            if (!checkAny)
                                quizArray[0] = 3;
                            else
                                quizArray[0] = 2;
                        }


                        //var isQuizPass = Ext.getCmp('isQuizz').getValue();

                        var nodeid = '0';

                        if (selected != 0)
                            nodeid = selected[0].data.id;
                        index = (index == -1) ? 0 : index;
                        studyTimer = (studyTimer == "") ? "0" : studyTimer;
                        //isQuizPassstr = (isQuizPass != 0)?isQuizPass:0;

                        form.submit({
                            success: function () {
                                if (nodeid == index) {
                                    Ext.Msg.alert('Seclect another target', 'PLease selected another target node!');
                                }
                                else {

                                nevow_clientToServerEvent('AddTarget', this, '', nodeid, index, studyTimer, quizArray);



                                    Ext.getCmp('sequencingwin').doClose();
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