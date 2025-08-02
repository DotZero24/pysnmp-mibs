_b='cie1000AlarmTrapStatusDelInfoGroup'
_a='cie1000AlarmTrapStatusModInfoGroup'
_Z='cie1000AlarmTrapStatusAddInfoGroup'
_Y='cie1000AlarmControlTableInfoGroup'
_X='cie1000AlarmStatusInfoGroup'
_W='cie1000AlarmConfigTableRowEditorInfoGroup'
_V='cie1000AlarmConfigTableInfoGroup'
_U='cie1000AlarmTrapStatusDel'
_T='cie1000AlarmTrapStatusMod'
_S='cie1000AlarmTrapStatusAdd'
_R='cie1000AlarmControlSuppress'
_Q='cie1000AlarmConfigTableRowEditorAction'
_P='cie1000AlarmConfigTableRowEditorExpression'
_O='cie1000AlarmConfigTableRowEditorAlarmName'
_N='cie1000AlarmConfigAction'
_M='cie1000AlarmConfigExpression'
_L='cie1000AlarmControlAlarmName'
_K='read-only'
_J='accessible-for-notify'
_I='cie1000AlarmConfigAlarmName'
_H='cie1000AlarmStatusExposedActive'
_G='cie1000AlarmStatusActive'
_F='cie1000AlarmStatusSuppressed'
_E='cie1000AlarmStatusAlarmName'
_D='read-write'
_C='CIE1000DisplayString'
_B='current'
_A='CIE1000-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CIE1000DisplayString,CIE1000RowEditorState=mibBuilder.importSymbols('CIE1000-TC',_C,'CIE1000RowEditorState')
cie1000SwitchMgmt,=mibBuilder.importSymbols('CISCO-IE1000-MIB','cie1000SwitchMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cie1000AlarmMib=ModuleIdentity((1,3,6,1,4,1,9,9,832,1,136))
if mibBuilder.loadTexts:cie1000AlarmMib.setRevisions(('2016-02-08 00:00',))
_Cie1000AlarmMibObjects_ObjectIdentity=ObjectIdentity
cie1000AlarmMibObjects=_Cie1000AlarmMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,1))
_Cie1000AlarmConfig_ObjectIdentity=ObjectIdentity
cie1000AlarmConfig=_Cie1000AlarmConfig_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,1,2))
_Cie1000AlarmConfigTable_Object=MibTable
cie1000AlarmConfigTable=_Cie1000AlarmConfigTable_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,1))
if mibBuilder.loadTexts:cie1000AlarmConfigTable.setStatus(_B)
_Cie1000AlarmConfigEntry_Object=MibTableRow
cie1000AlarmConfigEntry=_Cie1000AlarmConfigEntry_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,1,1))
cie1000AlarmConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:cie1000AlarmConfigEntry.setStatus(_B)
class _Cie1000AlarmConfigAlarmName_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Cie1000AlarmConfigAlarmName_Type.__name__=_C
_Cie1000AlarmConfigAlarmName_Object=MibTableColumn
cie1000AlarmConfigAlarmName=_Cie1000AlarmConfigAlarmName_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,1,1,1),_Cie1000AlarmConfigAlarmName_Type())
cie1000AlarmConfigAlarmName.setMaxAccess(_J)
if mibBuilder.loadTexts:cie1000AlarmConfigAlarmName.setStatus(_B)
class _Cie1000AlarmConfigExpression_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_Cie1000AlarmConfigExpression_Type.__name__=_C
_Cie1000AlarmConfigExpression_Object=MibTableColumn
cie1000AlarmConfigExpression=_Cie1000AlarmConfigExpression_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,1,1,2),_Cie1000AlarmConfigExpression_Type())
cie1000AlarmConfigExpression.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000AlarmConfigExpression.setStatus(_B)
_Cie1000AlarmConfigAction_Type=CIE1000RowEditorState
_Cie1000AlarmConfigAction_Object=MibTableColumn
cie1000AlarmConfigAction=_Cie1000AlarmConfigAction_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,1,1,100),_Cie1000AlarmConfigAction_Type())
cie1000AlarmConfigAction.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000AlarmConfigAction.setStatus(_B)
_Cie1000AlarmConfigTableRowEditor_ObjectIdentity=ObjectIdentity
cie1000AlarmConfigTableRowEditor=_Cie1000AlarmConfigTableRowEditor_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,1,2,2))
class _Cie1000AlarmConfigTableRowEditorAlarmName_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Cie1000AlarmConfigTableRowEditorAlarmName_Type.__name__=_C
_Cie1000AlarmConfigTableRowEditorAlarmName_Object=MibScalar
cie1000AlarmConfigTableRowEditorAlarmName=_Cie1000AlarmConfigTableRowEditorAlarmName_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,2,1),_Cie1000AlarmConfigTableRowEditorAlarmName_Type())
cie1000AlarmConfigTableRowEditorAlarmName.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000AlarmConfigTableRowEditorAlarmName.setStatus(_B)
class _Cie1000AlarmConfigTableRowEditorExpression_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_Cie1000AlarmConfigTableRowEditorExpression_Type.__name__=_C
_Cie1000AlarmConfigTableRowEditorExpression_Object=MibScalar
cie1000AlarmConfigTableRowEditorExpression=_Cie1000AlarmConfigTableRowEditorExpression_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,2,2),_Cie1000AlarmConfigTableRowEditorExpression_Type())
cie1000AlarmConfigTableRowEditorExpression.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000AlarmConfigTableRowEditorExpression.setStatus(_B)
_Cie1000AlarmConfigTableRowEditorAction_Type=CIE1000RowEditorState
_Cie1000AlarmConfigTableRowEditorAction_Object=MibScalar
cie1000AlarmConfigTableRowEditorAction=_Cie1000AlarmConfigTableRowEditorAction_Object((1,3,6,1,4,1,9,9,832,1,136,1,2,2,100),_Cie1000AlarmConfigTableRowEditorAction_Type())
cie1000AlarmConfigTableRowEditorAction.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000AlarmConfigTableRowEditorAction.setStatus(_B)
_Cie1000AlarmStatus_ObjectIdentity=ObjectIdentity
cie1000AlarmStatus=_Cie1000AlarmStatus_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,1,3))
_Cie1000AlarmStatusTable_Object=MibTable
cie1000AlarmStatusTable=_Cie1000AlarmStatusTable_Object((1,3,6,1,4,1,9,9,832,1,136,1,3,1))
if mibBuilder.loadTexts:cie1000AlarmStatusTable.setStatus(_B)
_Cie1000AlarmStatusEntry_Object=MibTableRow
cie1000AlarmStatusEntry=_Cie1000AlarmStatusEntry_Object((1,3,6,1,4,1,9,9,832,1,136,1,3,1,1))
cie1000AlarmStatusEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:cie1000AlarmStatusEntry.setStatus(_B)
class _Cie1000AlarmStatusAlarmName_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Cie1000AlarmStatusAlarmName_Type.__name__=_C
_Cie1000AlarmStatusAlarmName_Object=MibTableColumn
cie1000AlarmStatusAlarmName=_Cie1000AlarmStatusAlarmName_Object((1,3,6,1,4,1,9,9,832,1,136,1,3,1,1,1),_Cie1000AlarmStatusAlarmName_Type())
cie1000AlarmStatusAlarmName.setMaxAccess(_J)
if mibBuilder.loadTexts:cie1000AlarmStatusAlarmName.setStatus(_B)
_Cie1000AlarmStatusSuppressed_Type=TruthValue
_Cie1000AlarmStatusSuppressed_Object=MibTableColumn
cie1000AlarmStatusSuppressed=_Cie1000AlarmStatusSuppressed_Object((1,3,6,1,4,1,9,9,832,1,136,1,3,1,1,2),_Cie1000AlarmStatusSuppressed_Type())
cie1000AlarmStatusSuppressed.setMaxAccess(_K)
if mibBuilder.loadTexts:cie1000AlarmStatusSuppressed.setStatus(_B)
_Cie1000AlarmStatusActive_Type=TruthValue
_Cie1000AlarmStatusActive_Object=MibTableColumn
cie1000AlarmStatusActive=_Cie1000AlarmStatusActive_Object((1,3,6,1,4,1,9,9,832,1,136,1,3,1,1,3),_Cie1000AlarmStatusActive_Type())
cie1000AlarmStatusActive.setMaxAccess(_K)
if mibBuilder.loadTexts:cie1000AlarmStatusActive.setStatus(_B)
_Cie1000AlarmStatusExposedActive_Type=TruthValue
_Cie1000AlarmStatusExposedActive_Object=MibTableColumn
cie1000AlarmStatusExposedActive=_Cie1000AlarmStatusExposedActive_Object((1,3,6,1,4,1,9,9,832,1,136,1,3,1,1,4),_Cie1000AlarmStatusExposedActive_Type())
cie1000AlarmStatusExposedActive.setMaxAccess(_K)
if mibBuilder.loadTexts:cie1000AlarmStatusExposedActive.setStatus(_B)
_Cie1000AlarmControl_ObjectIdentity=ObjectIdentity
cie1000AlarmControl=_Cie1000AlarmControl_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,1,4))
_Cie1000AlarmControlTable_Object=MibTable
cie1000AlarmControlTable=_Cie1000AlarmControlTable_Object((1,3,6,1,4,1,9,9,832,1,136,1,4,1))
if mibBuilder.loadTexts:cie1000AlarmControlTable.setStatus(_B)
_Cie1000AlarmControlEntry_Object=MibTableRow
cie1000AlarmControlEntry=_Cie1000AlarmControlEntry_Object((1,3,6,1,4,1,9,9,832,1,136,1,4,1,1))
cie1000AlarmControlEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:cie1000AlarmControlEntry.setStatus(_B)
class _Cie1000AlarmControlAlarmName_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Cie1000AlarmControlAlarmName_Type.__name__=_C
_Cie1000AlarmControlAlarmName_Object=MibTableColumn
cie1000AlarmControlAlarmName=_Cie1000AlarmControlAlarmName_Object((1,3,6,1,4,1,9,9,832,1,136,1,4,1,1,1),_Cie1000AlarmControlAlarmName_Type())
cie1000AlarmControlAlarmName.setMaxAccess(_J)
if mibBuilder.loadTexts:cie1000AlarmControlAlarmName.setStatus(_B)
_Cie1000AlarmControlSuppress_Type=TruthValue
_Cie1000AlarmControlSuppress_Object=MibTableColumn
cie1000AlarmControlSuppress=_Cie1000AlarmControlSuppress_Object((1,3,6,1,4,1,9,9,832,1,136,1,4,1,1,2),_Cie1000AlarmControlSuppress_Type())
cie1000AlarmControlSuppress.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000AlarmControlSuppress.setStatus(_B)
_Cie1000AlarmTrap_ObjectIdentity=ObjectIdentity
cie1000AlarmTrap=_Cie1000AlarmTrap_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,1,6))
_Cie1000AlarmMibConformance_ObjectIdentity=ObjectIdentity
cie1000AlarmMibConformance=_Cie1000AlarmMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,2))
_Cie1000AlarmMibCompliances_ObjectIdentity=ObjectIdentity
cie1000AlarmMibCompliances=_Cie1000AlarmMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,2,1))
_Cie1000AlarmMibGroups_ObjectIdentity=ObjectIdentity
cie1000AlarmMibGroups=_Cie1000AlarmMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,136,2,2))
cie1000AlarmConfigTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,136,2,2,1))
cie1000AlarmConfigTableInfoGroup.setObjects(*((_A,_I),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cie1000AlarmConfigTableInfoGroup.setStatus(_B)
cie1000AlarmConfigTableRowEditorInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,136,2,2,2))
cie1000AlarmConfigTableRowEditorInfoGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:cie1000AlarmConfigTableRowEditorInfoGroup.setStatus(_B)
cie1000AlarmStatusInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,136,2,2,3))
cie1000AlarmStatusInfoGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cie1000AlarmStatusInfoGroup.setStatus(_B)
cie1000AlarmControlTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,136,2,2,4))
cie1000AlarmControlTableInfoGroup.setObjects(*((_A,_L),(_A,_R)))
if mibBuilder.loadTexts:cie1000AlarmControlTableInfoGroup.setStatus(_B)
cie1000AlarmTrapStatusAdd=NotificationType((1,3,6,1,4,1,9,9,832,1,136,1,6,1))
cie1000AlarmTrapStatusAdd.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cie1000AlarmTrapStatusAdd.setStatus(_B)
cie1000AlarmTrapStatusMod=NotificationType((1,3,6,1,4,1,9,9,832,1,136,1,6,2))
cie1000AlarmTrapStatusMod.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cie1000AlarmTrapStatusMod.setStatus(_B)
cie1000AlarmTrapStatusDel=NotificationType((1,3,6,1,4,1,9,9,832,1,136,1,6,3))
cie1000AlarmTrapStatusDel.setObjects((_A,_E))
if mibBuilder.loadTexts:cie1000AlarmTrapStatusDel.setStatus(_B)
cie1000AlarmTrapStatusAddInfoGroup=NotificationGroup((1,3,6,1,4,1,9,9,832,1,136,2,2,5))
cie1000AlarmTrapStatusAddInfoGroup.setObjects((_A,_S))
if mibBuilder.loadTexts:cie1000AlarmTrapStatusAddInfoGroup.setStatus(_B)
cie1000AlarmTrapStatusModInfoGroup=NotificationGroup((1,3,6,1,4,1,9,9,832,1,136,2,2,6))
cie1000AlarmTrapStatusModInfoGroup.setObjects((_A,_T))
if mibBuilder.loadTexts:cie1000AlarmTrapStatusModInfoGroup.setStatus(_B)
cie1000AlarmTrapStatusDelInfoGroup=NotificationGroup((1,3,6,1,4,1,9,9,832,1,136,2,2,7))
cie1000AlarmTrapStatusDelInfoGroup.setObjects((_A,_U))
if mibBuilder.loadTexts:cie1000AlarmTrapStatusDelInfoGroup.setStatus(_B)
cie1000AlarmMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,832,1,136,2,1,1))
cie1000AlarmMibCompliance.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cie1000AlarmMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cie1000AlarmMib':cie1000AlarmMib,'cie1000AlarmMibObjects':cie1000AlarmMibObjects,'cie1000AlarmConfig':cie1000AlarmConfig,'cie1000AlarmConfigTable':cie1000AlarmConfigTable,'cie1000AlarmConfigEntry':cie1000AlarmConfigEntry,_I:cie1000AlarmConfigAlarmName,_M:cie1000AlarmConfigExpression,_N:cie1000AlarmConfigAction,'cie1000AlarmConfigTableRowEditor':cie1000AlarmConfigTableRowEditor,_O:cie1000AlarmConfigTableRowEditorAlarmName,_P:cie1000AlarmConfigTableRowEditorExpression,_Q:cie1000AlarmConfigTableRowEditorAction,'cie1000AlarmStatus':cie1000AlarmStatus,'cie1000AlarmStatusTable':cie1000AlarmStatusTable,'cie1000AlarmStatusEntry':cie1000AlarmStatusEntry,_E:cie1000AlarmStatusAlarmName,_F:cie1000AlarmStatusSuppressed,_G:cie1000AlarmStatusActive,_H:cie1000AlarmStatusExposedActive,'cie1000AlarmControl':cie1000AlarmControl,'cie1000AlarmControlTable':cie1000AlarmControlTable,'cie1000AlarmControlEntry':cie1000AlarmControlEntry,_L:cie1000AlarmControlAlarmName,_R:cie1000AlarmControlSuppress,'cie1000AlarmTrap':cie1000AlarmTrap,_S:cie1000AlarmTrapStatusAdd,_T:cie1000AlarmTrapStatusMod,_U:cie1000AlarmTrapStatusDel,'cie1000AlarmMibConformance':cie1000AlarmMibConformance,'cie1000AlarmMibCompliances':cie1000AlarmMibCompliances,'cie1000AlarmMibCompliance':cie1000AlarmMibCompliance,'cie1000AlarmMibGroups':cie1000AlarmMibGroups,_V:cie1000AlarmConfigTableInfoGroup,_W:cie1000AlarmConfigTableRowEditorInfoGroup,_X:cie1000AlarmStatusInfoGroup,_Y:cie1000AlarmControlTableInfoGroup,_Z:cie1000AlarmTrapStatusAddInfoGroup,_a:cie1000AlarmTrapStatusModInfoGroup,_b:cie1000AlarmTrapStatusDelInfoGroup})