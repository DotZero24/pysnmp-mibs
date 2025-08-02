_K='zyStackingSlotInfoSlot'
_J='zyStackingSlotCurrentSlotId'
_I='zyStackingSlotChannelInfoChannnel'
_H='read-write'
_G='zyStackingTrapInfoMsg'
_F='not-accessible'
_E='Integer32'
_D='zyStackingSlotChannelInfoSlot'
_C='read-only'
_B='ZYXEL-STACKING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelStacking=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,97))
_ZyxelStackingSetup_ObjectIdentity=ObjectIdentity
zyxelStackingSetup=_ZyxelStackingSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,97,1))
class _ZyStackingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_ZyStackingPriority_Type.__name__=_E
_ZyStackingPriority_Object=MibScalar
zyStackingPriority=_ZyStackingPriority_Object((1,3,6,1,4,1,890,1,15,3,97,1,1),_ZyStackingPriority_Type())
zyStackingPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:zyStackingPriority.setStatus(_A)
_ZyStackingForceMasterModeState_Type=EnabledStatus
_ZyStackingForceMasterModeState_Object=MibScalar
zyStackingForceMasterModeState=_ZyStackingForceMasterModeState_Object((1,3,6,1,4,1,890,1,15,3,97,1,2),_ZyStackingForceMasterModeState_Type())
zyStackingForceMasterModeState.setMaxAccess(_H)
if mibBuilder.loadTexts:zyStackingForceMasterModeState.setStatus(_A)
_ZyxelStackingSlotTable_Object=MibTable
zyxelStackingSlotTable=_ZyxelStackingSlotTable_Object((1,3,6,1,4,1,890,1,15,3,97,1,3))
if mibBuilder.loadTexts:zyxelStackingSlotTable.setStatus(_A)
_ZyxelStackingSlotEntry_Object=MibTableRow
zyxelStackingSlotEntry=_ZyxelStackingSlotEntry_Object((1,3,6,1,4,1,890,1,15,3,97,1,3,1))
zyxelStackingSlotEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:zyxelStackingSlotEntry.setStatus(_A)
_ZyStackingSlotCurrentSlotId_Type=Integer32
_ZyStackingSlotCurrentSlotId_Object=MibTableColumn
zyStackingSlotCurrentSlotId=_ZyStackingSlotCurrentSlotId_Object((1,3,6,1,4,1,890,1,15,3,97,1,3,1,1),_ZyStackingSlotCurrentSlotId_Type())
zyStackingSlotCurrentSlotId.setMaxAccess(_F)
if mibBuilder.loadTexts:zyStackingSlotCurrentSlotId.setStatus(_A)
class _ZyStackingSlotActiveSlotIdAfterReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('auto',0),('slotId1',1),('slotId2',2),('slotId3',3),('slotId4',4),('slotId5',5),('slotId6',6),('slotId7',7),('slotId8',8)))
_ZyStackingSlotActiveSlotIdAfterReboot_Type.__name__=_E
_ZyStackingSlotActiveSlotIdAfterReboot_Object=MibTableColumn
zyStackingSlotActiveSlotIdAfterReboot=_ZyStackingSlotActiveSlotIdAfterReboot_Object((1,3,6,1,4,1,890,1,15,3,97,1,3,1,2),_ZyStackingSlotActiveSlotIdAfterReboot_Type())
zyStackingSlotActiveSlotIdAfterReboot.setMaxAccess(_H)
if mibBuilder.loadTexts:zyStackingSlotActiveSlotIdAfterReboot.setStatus(_A)
_ZyStackingSlotIdFreeze_Type=EnabledStatus
_ZyStackingSlotIdFreeze_Object=MibScalar
zyStackingSlotIdFreeze=_ZyStackingSlotIdFreeze_Object((1,3,6,1,4,1,890,1,15,3,97,1,4),_ZyStackingSlotIdFreeze_Type())
zyStackingSlotIdFreeze.setMaxAccess(_H)
if mibBuilder.loadTexts:zyStackingSlotIdFreeze.setStatus(_A)
_ZyxelStackingStatus_ObjectIdentity=ObjectIdentity
zyxelStackingStatus=_ZyxelStackingStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,97,2))
_ZyxelStackingSlotInfoTable_Object=MibTable
zyxelStackingSlotInfoTable=_ZyxelStackingSlotInfoTable_Object((1,3,6,1,4,1,890,1,15,3,97,2,1))
if mibBuilder.loadTexts:zyxelStackingSlotInfoTable.setStatus(_A)
_ZyxelStackingSlotInfoEntry_Object=MibTableRow
zyxelStackingSlotInfoEntry=_ZyxelStackingSlotInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1))
zyxelStackingSlotInfoEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:zyxelStackingSlotInfoEntry.setStatus(_A)
_ZyStackingSlotInfoSlot_Type=Integer32
_ZyStackingSlotInfoSlot_Object=MibTableColumn
zyStackingSlotInfoSlot=_ZyStackingSlotInfoSlot_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,1),_ZyStackingSlotInfoSlot_Type())
zyStackingSlotInfoSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zyStackingSlotInfoSlot.setStatus(_A)
class _ZyStackingSlotInfoStackingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('inactive',0),('init',1),('active',2)))
_ZyStackingSlotInfoStackingStatus_Type.__name__=_E
_ZyStackingSlotInfoStackingStatus_Object=MibTableColumn
zyStackingSlotInfoStackingStatus=_ZyStackingSlotInfoStackingStatus_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,2),_ZyStackingSlotInfoStackingStatus_Type())
zyStackingSlotInfoStackingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoStackingStatus.setStatus(_A)
_ZyStackingSlotInfoForceMasterMode_Type=EnabledStatus
_ZyStackingSlotInfoForceMasterMode_Object=MibTableColumn
zyStackingSlotInfoForceMasterMode=_ZyStackingSlotInfoForceMasterMode_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,3),_ZyStackingSlotInfoForceMasterMode_Type())
zyStackingSlotInfoForceMasterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoForceMasterMode.setStatus(_A)
_ZyStackingSlotInfoPriority_Type=Integer32
_ZyStackingSlotInfoPriority_Object=MibTableColumn
zyStackingSlotInfoPriority=_ZyStackingSlotInfoPriority_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,4),_ZyStackingSlotInfoPriority_Type())
zyStackingSlotInfoPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoPriority.setStatus(_A)
class _ZyStackingSlotInfoRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('master',1),('backup',2),('linecard',3)))
_ZyStackingSlotInfoRole_Type.__name__=_E
_ZyStackingSlotInfoRole_Object=MibTableColumn
zyStackingSlotInfoRole=_ZyStackingSlotInfoRole_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,5),_ZyStackingSlotInfoRole_Type())
zyStackingSlotInfoRole.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoRole.setStatus(_A)
_ZyStackingSlotInfoMacAddress_Type=OctetString
_ZyStackingSlotInfoMacAddress_Object=MibTableColumn
zyStackingSlotInfoMacAddress=_ZyStackingSlotInfoMacAddress_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,6),_ZyStackingSlotInfoMacAddress_Type())
zyStackingSlotInfoMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoMacAddress.setStatus(_A)
_ZyStackingSlotInfoUptime_Type=TimeTicks
_ZyStackingSlotInfoUptime_Object=MibTableColumn
zyStackingSlotInfoUptime=_ZyStackingSlotInfoUptime_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,7),_ZyStackingSlotInfoUptime_Type())
zyStackingSlotInfoUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoUptime.setStatus(_A)
_ZyStackingSlotInfoFirmwareVersionRunning_Type=OctetString
_ZyStackingSlotInfoFirmwareVersionRunning_Object=MibTableColumn
zyStackingSlotInfoFirmwareVersionRunning=_ZyStackingSlotInfoFirmwareVersionRunning_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,8),_ZyStackingSlotInfoFirmwareVersionRunning_Type())
zyStackingSlotInfoFirmwareVersionRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoFirmwareVersionRunning.setStatus(_A)
_ZyStackingSlotInfoFirmwareVersionFlash1_Type=OctetString
_ZyStackingSlotInfoFirmwareVersionFlash1_Object=MibTableColumn
zyStackingSlotInfoFirmwareVersionFlash1=_ZyStackingSlotInfoFirmwareVersionFlash1_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,9),_ZyStackingSlotInfoFirmwareVersionFlash1_Type())
zyStackingSlotInfoFirmwareVersionFlash1.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoFirmwareVersionFlash1.setStatus(_A)
_ZyStackingSlotInfoFirmwareVersionFlash2_Type=OctetString
_ZyStackingSlotInfoFirmwareVersionFlash2_Object=MibTableColumn
zyStackingSlotInfoFirmwareVersionFlash2=_ZyStackingSlotInfoFirmwareVersionFlash2_Object((1,3,6,1,4,1,890,1,15,3,97,2,1,1,10),_ZyStackingSlotInfoFirmwareVersionFlash2_Type())
zyStackingSlotInfoFirmwareVersionFlash2.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotInfoFirmwareVersionFlash2.setStatus(_A)
_ZyxelStackingSlotChannelInfoTable_Object=MibTable
zyxelStackingSlotChannelInfoTable=_ZyxelStackingSlotChannelInfoTable_Object((1,3,6,1,4,1,890,1,15,3,97,2,2))
if mibBuilder.loadTexts:zyxelStackingSlotChannelInfoTable.setStatus(_A)
_ZyxelStackingSlotChannelInfoEntry_Object=MibTableRow
zyxelStackingSlotChannelInfoEntry=_ZyxelStackingSlotChannelInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,97,2,2,1))
zyxelStackingSlotChannelInfoEntry.setIndexNames((0,_B,_D),(0,_B,_I))
if mibBuilder.loadTexts:zyxelStackingSlotChannelInfoEntry.setStatus(_A)
_ZyStackingSlotChannelInfoSlot_Type=Integer32
_ZyStackingSlotChannelInfoSlot_Object=MibTableColumn
zyStackingSlotChannelInfoSlot=_ZyStackingSlotChannelInfoSlot_Object((1,3,6,1,4,1,890,1,15,3,97,2,2,1,1),_ZyStackingSlotChannelInfoSlot_Type())
zyStackingSlotChannelInfoSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zyStackingSlotChannelInfoSlot.setStatus(_A)
_ZyStackingSlotChannelInfoChannnel_Type=Integer32
_ZyStackingSlotChannelInfoChannnel_Object=MibTableColumn
zyStackingSlotChannelInfoChannnel=_ZyStackingSlotChannelInfoChannnel_Object((1,3,6,1,4,1,890,1,15,3,97,2,2,1,2),_ZyStackingSlotChannelInfoChannnel_Type())
zyStackingSlotChannelInfoChannnel.setMaxAccess(_F)
if mibBuilder.loadTexts:zyStackingSlotChannelInfoChannnel.setStatus(_A)
class _ZyStackingSlotChannelInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ZyStackingSlotChannelInfoStatus_Type.__name__=_E
_ZyStackingSlotChannelInfoStatus_Object=MibTableColumn
zyStackingSlotChannelInfoStatus=_ZyStackingSlotChannelInfoStatus_Object((1,3,6,1,4,1,890,1,15,3,97,2,2,1,3),_ZyStackingSlotChannelInfoStatus_Type())
zyStackingSlotChannelInfoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotChannelInfoStatus.setStatus(_A)
_ZyStackingSlotChannelInfoPorts_Type=PortList
_ZyStackingSlotChannelInfoPorts_Object=MibTableColumn
zyStackingSlotChannelInfoPorts=_ZyStackingSlotChannelInfoPorts_Object((1,3,6,1,4,1,890,1,15,3,97,2,2,1,4),_ZyStackingSlotChannelInfoPorts_Type())
zyStackingSlotChannelInfoPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotChannelInfoPorts.setStatus(_A)
_ZyStackingSlotChannelInfoNeighbor_Type=Integer32
_ZyStackingSlotChannelInfoNeighbor_Object=MibTableColumn
zyStackingSlotChannelInfoNeighbor=_ZyStackingSlotChannelInfoNeighbor_Object((1,3,6,1,4,1,890,1,15,3,97,2,2,1,5),_ZyStackingSlotChannelInfoNeighbor_Type())
zyStackingSlotChannelInfoNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotChannelInfoNeighbor.setStatus(_A)
class _ZyStackingSlotChannelInfoSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('speed_10G',1),('speed_12G',2),('speed_20G',3)))
_ZyStackingSlotChannelInfoSpeed_Type.__name__=_E
_ZyStackingSlotChannelInfoSpeed_Object=MibTableColumn
zyStackingSlotChannelInfoSpeed=_ZyStackingSlotChannelInfoSpeed_Object((1,3,6,1,4,1,890,1,15,3,97,2,2,1,6),_ZyStackingSlotChannelInfoSpeed_Type())
zyStackingSlotChannelInfoSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingSlotChannelInfoSpeed.setStatus(_A)
class _ZyStackingTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chain',1),('ring',2)))
_ZyStackingTopology_Type.__name__=_E
_ZyStackingTopology_Object=MibScalar
zyStackingTopology=_ZyStackingTopology_Object((1,3,6,1,4,1,890,1,15,3,97,2,3),_ZyStackingTopology_Type())
zyStackingTopology.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStackingTopology.setStatus(_A)
_ZyxelStackingTrapInfoObjects_ObjectIdentity=ObjectIdentity
zyxelStackingTrapInfoObjects=_ZyxelStackingTrapInfoObjects_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,97,3))
_ZyStackingTrapInfoMsg_Type=OctetString
_ZyStackingTrapInfoMsg_Object=MibScalar
zyStackingTrapInfoMsg=_ZyStackingTrapInfoMsg_Object((1,3,6,1,4,1,890,1,15,3,97,3,1),_ZyStackingTrapInfoMsg_Type())
zyStackingTrapInfoMsg.setMaxAccess(_F)
if mibBuilder.loadTexts:zyStackingTrapInfoMsg.setStatus(_A)
_ZyxelStackingNotifications_ObjectIdentity=ObjectIdentity
zyxelStackingNotifications=_ZyxelStackingNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,97,4))
zyStackingChannelUp=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,1))
zyStackingChannelUp.setObjects(*((_B,_D),(_B,_I)))
if mibBuilder.loadTexts:zyStackingChannelUp.setStatus(_A)
zyStackingChannelDown=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,2))
zyStackingChannelDown.setObjects(*((_B,_D),(_B,_I)))
if mibBuilder.loadTexts:zyStackingChannelDown.setStatus(_A)
zyStackingSlotAttach=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,3))
zyStackingSlotAttach.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingSlotAttach.setStatus(_A)
zyStackingSlotDetach=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,4))
zyStackingSlotDetach.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingSlotDetach.setStatus(_A)
zyStackingNewMaster=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,5))
zyStackingNewMaster.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingNewMaster.setStatus(_A)
zyStackingUpgradeFirmwareFail=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,6))
zyStackingUpgradeFirmwareFail.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingUpgradeFirmwareFail.setStatus(_A)
zyStackingNewBackup=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,7))
zyStackingNewBackup.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingNewBackup.setStatus(_A)
zyStackingBackupTakeover=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,8))
zyStackingBackupTakeover.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingBackupTakeover.setStatus(_A)
zyStackingNewMasterFromTakeover=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,9))
zyStackingNewMasterFromTakeover.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingNewMasterFromTakeover.setStatus(_A)
zyStackingSyncConfFail=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,10))
zyStackingSyncConfFail.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingSyncConfFail.setStatus(_A)
zyStackingSysRestoreConfFail=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,11))
zyStackingSysRestoreConfFail.setObjects((_B,_D))
if mibBuilder.loadTexts:zyStackingSysRestoreConfFail.setStatus(_A)
zyStackingSlotInitFail=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,12))
zyStackingSlotInitFail.setObjects((_B,_G))
if mibBuilder.loadTexts:zyStackingSlotInitFail.setStatus(_A)
zyStackingSlotChangeIndex=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,13))
zyStackingSlotChangeIndex.setObjects((_B,_G))
if mibBuilder.loadTexts:zyStackingSlotChangeIndex.setStatus(_A)
zyStackingPriorityChange=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,14))
zyStackingPriorityChange.setObjects((_B,_G))
if mibBuilder.loadTexts:zyStackingPriorityChange.setStatus(_A)
zyStackingTopologyChange=NotificationType((1,3,6,1,4,1,890,1,15,3,97,4,15))
zyStackingTopologyChange.setObjects((_B,_G))
if mibBuilder.loadTexts:zyStackingTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelStacking':zyxelStacking,'zyxelStackingSetup':zyxelStackingSetup,'zyStackingPriority':zyStackingPriority,'zyStackingForceMasterModeState':zyStackingForceMasterModeState,'zyxelStackingSlotTable':zyxelStackingSlotTable,'zyxelStackingSlotEntry':zyxelStackingSlotEntry,_J:zyStackingSlotCurrentSlotId,'zyStackingSlotActiveSlotIdAfterReboot':zyStackingSlotActiveSlotIdAfterReboot,'zyStackingSlotIdFreeze':zyStackingSlotIdFreeze,'zyxelStackingStatus':zyxelStackingStatus,'zyxelStackingSlotInfoTable':zyxelStackingSlotInfoTable,'zyxelStackingSlotInfoEntry':zyxelStackingSlotInfoEntry,_K:zyStackingSlotInfoSlot,'zyStackingSlotInfoStackingStatus':zyStackingSlotInfoStackingStatus,'zyStackingSlotInfoForceMasterMode':zyStackingSlotInfoForceMasterMode,'zyStackingSlotInfoPriority':zyStackingSlotInfoPriority,'zyStackingSlotInfoRole':zyStackingSlotInfoRole,'zyStackingSlotInfoMacAddress':zyStackingSlotInfoMacAddress,'zyStackingSlotInfoUptime':zyStackingSlotInfoUptime,'zyStackingSlotInfoFirmwareVersionRunning':zyStackingSlotInfoFirmwareVersionRunning,'zyStackingSlotInfoFirmwareVersionFlash1':zyStackingSlotInfoFirmwareVersionFlash1,'zyStackingSlotInfoFirmwareVersionFlash2':zyStackingSlotInfoFirmwareVersionFlash2,'zyxelStackingSlotChannelInfoTable':zyxelStackingSlotChannelInfoTable,'zyxelStackingSlotChannelInfoEntry':zyxelStackingSlotChannelInfoEntry,_D:zyStackingSlotChannelInfoSlot,_I:zyStackingSlotChannelInfoChannnel,'zyStackingSlotChannelInfoStatus':zyStackingSlotChannelInfoStatus,'zyStackingSlotChannelInfoPorts':zyStackingSlotChannelInfoPorts,'zyStackingSlotChannelInfoNeighbor':zyStackingSlotChannelInfoNeighbor,'zyStackingSlotChannelInfoSpeed':zyStackingSlotChannelInfoSpeed,'zyStackingTopology':zyStackingTopology,'zyxelStackingTrapInfoObjects':zyxelStackingTrapInfoObjects,_G:zyStackingTrapInfoMsg,'zyxelStackingNotifications':zyxelStackingNotifications,'zyStackingChannelUp':zyStackingChannelUp,'zyStackingChannelDown':zyStackingChannelDown,'zyStackingSlotAttach':zyStackingSlotAttach,'zyStackingSlotDetach':zyStackingSlotDetach,'zyStackingNewMaster':zyStackingNewMaster,'zyStackingUpgradeFirmwareFail':zyStackingUpgradeFirmwareFail,'zyStackingNewBackup':zyStackingNewBackup,'zyStackingBackupTakeover':zyStackingBackupTakeover,'zyStackingNewMasterFromTakeover':zyStackingNewMasterFromTakeover,'zyStackingSyncConfFail':zyStackingSyncConfFail,'zyStackingSysRestoreConfFail':zyStackingSysRestoreConfFail,'zyStackingSlotInitFail':zyStackingSlotInitFail,'zyStackingSlotChangeIndex':zyStackingSlotChangeIndex,'zyStackingPriorityChange':zyStackingPriorityChange,'zyStackingTopologyChange':zyStackingTopologyChange})