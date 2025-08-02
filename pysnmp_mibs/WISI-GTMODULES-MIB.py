_d='gtModulesBasicNotificationsGroup'
_c='gtModulesSetGroup'
_b='gtModulesTrapGroup'
_a='gtModulesStatsGroup'
_Z='gtModulesSystemGroup'
_Y='gtModulesV1Group'
_X='gtModulesNotifyPlugout'
_W='gtModulesNotifyPlugin'
_V='gtNumCapabilities'
_U='gtModuleLifetime'
_T='gtModuleUptime'
_S='gtOutputsTableIdx'
_R='gtInputsTableIdx'
_Q='gtChannel'
_P='gtModuleSerNo'
_O='gtModuleFWID'
_N='gtModuleHWID'
_M='gtModuleName'
_L='gtThisModuleSlot'
_K='gtCapability'
_J='DisplayString'
_I='Integer32'
_H='gtNumModules'
_G='read-write'
_F='not-accessible'
_E='gtModule'
_D='Unsigned32'
_C='read-only'
_B='WISI-GTMODULES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
gtUnit,=mibBuilder.importSymbols('WISI-TANGRAM-MIB','gtUnit')
gtModulesMIB=ModuleIdentity((1,3,6,1,4,1,7465,20,2,9,1,2))
if mibBuilder.loadTexts:gtModulesMIB.setRevisions(('2016-09-08 00:00','2016-06-08 00:00','2015-06-16 00:00','2013-07-29 00:00','2013-06-26 00:00','2012-10-31 00:00','2011-12-13 00:00','2011-09-08 00:00','2011-04-01 00:00'))
_GtModulesNotifications_ObjectIdentity=ObjectIdentity
gtModulesNotifications=_GtModulesNotifications_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,2,0))
_GtModulesObjects_ObjectIdentity=ObjectIdentity
gtModulesObjects=_GtModulesObjects_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,2,1))
class _GtThisModuleSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_GtThisModuleSlot_Type.__name__=_D
_GtThisModuleSlot_Object=MibScalar
gtThisModuleSlot=_GtThisModuleSlot_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,1),_GtThisModuleSlot_Type())
gtThisModuleSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:gtThisModuleSlot.setStatus(_A)
class _GtNumModules_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_GtNumModules_Type.__name__=_D
_GtNumModules_Object=MibScalar
gtNumModules=_GtNumModules_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,2),_GtNumModules_Type())
gtNumModules.setMaxAccess(_C)
if mibBuilder.loadTexts:gtNumModules.setStatus(_A)
_GtModulesTable_Object=MibTable
gtModulesTable=_GtModulesTable_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3))
if mibBuilder.loadTexts:gtModulesTable.setStatus(_A)
_GtModulesEntry_Object=MibTableRow
gtModulesEntry=_GtModulesEntry_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1))
gtModulesEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:gtModulesEntry.setStatus(_A)
class _GtModule_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_GtModule_Type.__name__=_D
_GtModule_Object=MibTableColumn
gtModule=_GtModule_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,1),_GtModule_Type())
gtModule.setMaxAccess(_F)
if mibBuilder.loadTexts:gtModule.setStatus(_A)
_GtModuleName_Type=DisplayString
_GtModuleName_Object=MibTableColumn
gtModuleName=_GtModuleName_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,2),_GtModuleName_Type())
gtModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleName.setStatus(_A)
_GtModuleHWID_Type=DisplayString
_GtModuleHWID_Object=MibTableColumn
gtModuleHWID=_GtModuleHWID_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,3),_GtModuleHWID_Type())
gtModuleHWID.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleHWID.setStatus(_A)
_GtModuleFWID_Type=DisplayString
_GtModuleFWID_Object=MibTableColumn
gtModuleFWID=_GtModuleFWID_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,4),_GtModuleFWID_Type())
gtModuleFWID.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleFWID.setStatus(_A)
_GtModuleSerNo_Type=DisplayString
_GtModuleSerNo_Object=MibTableColumn
gtModuleSerNo=_GtModuleSerNo_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,5),_GtModuleSerNo_Type())
gtModuleSerNo.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleSerNo.setStatus(_A)
_GtModuleUptime_Type=Counter32
_GtModuleUptime_Object=MibTableColumn
gtModuleUptime=_GtModuleUptime_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,6),_GtModuleUptime_Type())
gtModuleUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleUptime.setStatus(_A)
if mibBuilder.loadTexts:gtModuleUptime.setUnits('s')
_GtModuleLifetime_Type=Counter32
_GtModuleLifetime_Object=MibTableColumn
gtModuleLifetime=_GtModuleLifetime_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,7),_GtModuleLifetime_Type())
gtModuleLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleLifetime.setStatus(_A)
if mibBuilder.loadTexts:gtModuleLifetime.setUnits('s')
class _GtModulePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_GtModulePower_Type.__name__=_I
_GtModulePower_Object=MibTableColumn
gtModulePower=_GtModulePower_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,8),_GtModulePower_Type())
gtModulePower.setMaxAccess(_G)
if mibBuilder.loadTexts:gtModulePower.setStatus(_A)
_GtModuleMode_Type=DisplayString
_GtModuleMode_Object=MibTableColumn
gtModuleMode=_GtModuleMode_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,9),_GtModuleMode_Type())
gtModuleMode.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleMode.setStatus(_A)
_GtModuleStatus_Type=DisplayString
_GtModuleStatus_Object=MibTableColumn
gtModuleStatus=_GtModuleStatus_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,10),_GtModuleStatus_Type())
gtModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleStatus.setStatus(_A)
class _GtModuleSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_GtModuleSlot_Type.__name__=_D
_GtModuleSlot_Object=MibTableColumn
gtModuleSlot=_GtModuleSlot_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,11),_GtModuleSlot_Type())
gtModuleSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleSlot.setStatus('deprecated')
_GtModuleFWIDUploaded_Type=DisplayString
_GtModuleFWIDUploaded_Object=MibTableColumn
gtModuleFWIDUploaded=_GtModuleFWIDUploaded_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,12),_GtModuleFWIDUploaded_Type())
gtModuleFWIDUploaded.setMaxAccess(_C)
if mibBuilder.loadTexts:gtModuleFWIDUploaded.setStatus(_A)
class _GtModuleReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('running',0),('reboot',1)))
_GtModuleReboot_Type.__name__=_I
_GtModuleReboot_Object=MibTableColumn
gtModuleReboot=_GtModuleReboot_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,3,1,13),_GtModuleReboot_Type())
gtModuleReboot.setMaxAccess(_G)
if mibBuilder.loadTexts:gtModuleReboot.setStatus(_A)
class _GtNumCapabilities_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_GtNumCapabilities_Type.__name__=_D
_GtNumCapabilities_Object=MibScalar
gtNumCapabilities=_GtNumCapabilities_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,4),_GtNumCapabilities_Type())
gtNumCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:gtNumCapabilities.setStatus(_A)
_GtCapabilitiesTable_Object=MibTable
gtCapabilitiesTable=_GtCapabilitiesTable_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,5))
if mibBuilder.loadTexts:gtCapabilitiesTable.setStatus(_A)
_GtCapabilitiesEntry_Object=MibTableRow
gtCapabilitiesEntry=_GtCapabilitiesEntry_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,5,1))
gtCapabilitiesEntry.setIndexNames((0,_B,_E),(0,_B,_Q),(0,_B,_K))
if mibBuilder.loadTexts:gtCapabilitiesEntry.setStatus(_A)
class _GtChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_GtChannel_Type.__name__=_D
_GtChannel_Object=MibTableColumn
gtChannel=_GtChannel_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,5,1,1),_GtChannel_Type())
gtChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:gtChannel.setStatus(_A)
class _GtCapability_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_GtCapability_Type.__name__=_D
_GtCapability_Object=MibTableColumn
gtCapability=_GtCapability_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,5,1,2),_GtCapability_Type())
gtCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:gtCapability.setStatus(_A)
_GtInputsTable_Object=MibTable
gtInputsTable=_GtInputsTable_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,7))
if mibBuilder.loadTexts:gtInputsTable.setStatus(_A)
_GtInputsEntry_Object=MibTableRow
gtInputsEntry=_GtInputsEntry_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,7,1))
gtInputsEntry.setIndexNames((0,_B,_E),(0,_B,_R))
if mibBuilder.loadTexts:gtInputsEntry.setStatus(_A)
class _GtInputsTableIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_GtInputsTableIdx_Type.__name__=_D
_GtInputsTableIdx_Object=MibTableColumn
gtInputsTableIdx=_GtInputsTableIdx_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,7,1,1),_GtInputsTableIdx_Type())
gtInputsTableIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:gtInputsTableIdx.setStatus(_A)
_GtInputChannel_Type=ObjectIdentifier
_GtInputChannel_Object=MibTableColumn
gtInputChannel=_GtInputChannel_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,7,1,2),_GtInputChannel_Type())
gtInputChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:gtInputChannel.setStatus(_A)
class _GtInputName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_GtInputName_Type.__name__=_J
_GtInputName_Object=MibTableColumn
gtInputName=_GtInputName_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,7,1,3),_GtInputName_Type())
gtInputName.setMaxAccess(_G)
if mibBuilder.loadTexts:gtInputName.setStatus(_A)
_GtOutputsTable_Object=MibTable
gtOutputsTable=_GtOutputsTable_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,8))
if mibBuilder.loadTexts:gtOutputsTable.setStatus(_A)
_GtOutputsEntry_Object=MibTableRow
gtOutputsEntry=_GtOutputsEntry_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,8,1))
gtOutputsEntry.setIndexNames((0,_B,_E),(0,_B,_S))
if mibBuilder.loadTexts:gtOutputsEntry.setStatus(_A)
class _GtOutputsTableIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_GtOutputsTableIdx_Type.__name__=_D
_GtOutputsTableIdx_Object=MibTableColumn
gtOutputsTableIdx=_GtOutputsTableIdx_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,8,1,1),_GtOutputsTableIdx_Type())
gtOutputsTableIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:gtOutputsTableIdx.setStatus(_A)
_GtOutputChannel_Type=ObjectIdentifier
_GtOutputChannel_Object=MibTableColumn
gtOutputChannel=_GtOutputChannel_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,8,1,2),_GtOutputChannel_Type())
gtOutputChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:gtOutputChannel.setStatus(_A)
class _GtOutputName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_GtOutputName_Type.__name__=_J
_GtOutputName_Object=MibTableColumn
gtOutputName=_GtOutputName_Object((1,3,6,1,4,1,7465,20,2,9,1,2,1,8,1,3),_GtOutputName_Type())
gtOutputName.setMaxAccess(_G)
if mibBuilder.loadTexts:gtOutputName.setStatus(_A)
_GtModulesConformance_ObjectIdentity=ObjectIdentity
gtModulesConformance=_GtModulesConformance_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,2,2))
_GtModulesCompliances_ObjectIdentity=ObjectIdentity
gtModulesCompliances=_GtModulesCompliances_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,2,2,1))
_GtModulesGroups_ObjectIdentity=ObjectIdentity
gtModulesGroups=_GtModulesGroups_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,2,2,2))
_GtModulesTrapGroup_ObjectIdentity=ObjectIdentity
gtModulesTrapGroup=_GtModulesTrapGroup_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,2,2,2,4))
_GtModulesSetGroup_ObjectIdentity=ObjectIdentity
gtModulesSetGroup=_GtModulesSetGroup_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,2,2,2,5))
gtModulesV1Group=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,2,2,2,1))
gtModulesV1Group.setObjects(*((_B,_L),(_B,_H),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:gtModulesV1Group.setStatus(_A)
gtModulesSystemGroup=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,2,2,2,2))
gtModulesSystemGroup.setObjects(*((_B,_L),(_B,_H),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_K)))
if mibBuilder.loadTexts:gtModulesSystemGroup.setStatus(_A)
gtModulesStatsGroup=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,2,2,2,3))
gtModulesStatsGroup.setObjects(*((_B,_H),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:gtModulesStatsGroup.setStatus(_A)
gtModulesNotifyPlugin=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,2,0,1))
if mibBuilder.loadTexts:gtModulesNotifyPlugin.setStatus(_A)
gtModulesNotifyPlugout=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,2,0,2))
if mibBuilder.loadTexts:gtModulesNotifyPlugout.setStatus(_A)
gtModulesNotifyFailure=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,2,0,3))
if mibBuilder.loadTexts:gtModulesNotifyFailure.setStatus(_A)
gtModulesNotifyRedundancy=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,2,0,4))
if mibBuilder.loadTexts:gtModulesNotifyRedundancy.setStatus(_A)
gtModulesNotifyRedundancyClear=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,2,0,5))
if mibBuilder.loadTexts:gtModulesNotifyRedundancyClear.setStatus(_A)
gtModulesNotifyFailureClear=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,2,0,6))
if mibBuilder.loadTexts:gtModulesNotifyFailureClear.setStatus(_A)
gtModulesBasicNotificationsGroup=NotificationGroup((1,3,6,1,4,1,7465,20,2,9,1,2,2,2,6))
gtModulesBasicNotificationsGroup.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:gtModulesBasicNotificationsGroup.setStatus(_A)
gtModulesMIBCompliance=ModuleCompliance((1,3,6,1,4,1,7465,20,2,9,1,2,2,1,1))
gtModulesMIBCompliance.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:gtModulesMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gtModulesMIB':gtModulesMIB,'gtModulesNotifications':gtModulesNotifications,_W:gtModulesNotifyPlugin,_X:gtModulesNotifyPlugout,'gtModulesNotifyFailure':gtModulesNotifyFailure,'gtModulesNotifyRedundancy':gtModulesNotifyRedundancy,'gtModulesNotifyRedundancyClear':gtModulesNotifyRedundancyClear,'gtModulesNotifyFailureClear':gtModulesNotifyFailureClear,'gtModulesObjects':gtModulesObjects,_L:gtThisModuleSlot,_H:gtNumModules,'gtModulesTable':gtModulesTable,'gtModulesEntry':gtModulesEntry,_E:gtModule,_M:gtModuleName,_N:gtModuleHWID,_O:gtModuleFWID,_P:gtModuleSerNo,_T:gtModuleUptime,_U:gtModuleLifetime,'gtModulePower':gtModulePower,'gtModuleMode':gtModuleMode,'gtModuleStatus':gtModuleStatus,'gtModuleSlot':gtModuleSlot,'gtModuleFWIDUploaded':gtModuleFWIDUploaded,'gtModuleReboot':gtModuleReboot,_V:gtNumCapabilities,'gtCapabilitiesTable':gtCapabilitiesTable,'gtCapabilitiesEntry':gtCapabilitiesEntry,_Q:gtChannel,_K:gtCapability,'gtInputsTable':gtInputsTable,'gtInputsEntry':gtInputsEntry,_R:gtInputsTableIdx,'gtInputChannel':gtInputChannel,'gtInputName':gtInputName,'gtOutputsTable':gtOutputsTable,'gtOutputsEntry':gtOutputsEntry,_S:gtOutputsTableIdx,'gtOutputChannel':gtOutputChannel,'gtOutputName':gtOutputName,'gtModulesConformance':gtModulesConformance,'gtModulesCompliances':gtModulesCompliances,'gtModulesMIBCompliance':gtModulesMIBCompliance,'gtModulesGroups':gtModulesGroups,_Y:gtModulesV1Group,_Z:gtModulesSystemGroup,_a:gtModulesStatsGroup,_b:gtModulesTrapGroup,_c:gtModulesSetGroup,_d:gtModulesBasicNotificationsGroup})