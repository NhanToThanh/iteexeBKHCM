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

        Ext.applyIf(me, {
        				height: 309,
						items: [
							// Document Format
							{
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
							},
                            {
								xtype: 'helpcontainer',
								item: {
									xtype: 'checkbox',
                                    id: 'isQuizz',
                                    boxLabel: 'Pass the Quiz: ',
                                    name: 'isQuiz',
                                    checked: false,
                                    inputValue: 'isQuiz',
									dirtyCls: 'property-form-dirty',
									labelWidth: 325,
								},
								margin: 10,
								help: _('Learner must pass the quiz to move to next page')
							}]
        });

        me.callParent(arguments);
    }
});