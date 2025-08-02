_d='h3cMirrorRaidUuid'
_c='h3cMirrorDistLvIndex'
_b='h3cMirrorLvIndex'
_a='h3cSafeCacheRaidUuid'
_Z='h3cSafeCacheDistLvIndex'
_Y='h3cSafeCacheLvIndex'
_X='h3cCDRRaidUuid'
_W='h3cCDRDistLvIndex'
_V='h3cCDRLvIndex'
_U='resume'
_T='h3cTimeViewStamp'
_S='h3cSAExpRaidUuid'
_R='h3cRepLocalLvIndex'
_Q='suspend'
_P='sync'
_O='h3cTimeMarkStamp'
_N='stop'
_M='H3cStorageEnableState'
_L='H3cExtendSelectPolicy'
_K='OctetString'
_J='read-write'
_I='none'
_H='h3cSnapLvIndex'
_G='not-accessible'
_F='MB'
_E='Integer32'
_D='H3C-STORAGE-SNAP-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex')
H3cExtendSelectPolicy,H3cLvIDType,H3cRaidIDType,H3cStorageActionType,H3cStorageEnableState,H3cStorageOnlineState,h3cStorageRef=mibBuilder.importSymbols('H3C-STORAGE-REF-MIB',_L,'H3cLvIDType','H3cRaidIDType','H3cStorageActionType',_M,'H3cStorageOnlineState','h3cStorageRef')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cStorageSnap=ModuleIdentity((1,3,6,1,4,1,2011,10,10,2))
_H3cSnapMibObjects_ObjectIdentity=ObjectIdentity
h3cSnapMibObjects=_H3cSnapMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,10,2,1))
_H3cGlobalSnapSettingsObject_ObjectIdentity=ObjectIdentity
h3cGlobalSnapSettingsObject=_H3cGlobalSnapSettingsObject_ObjectIdentity((1,3,6,1,4,1,2011,10,10,2,1,1))
_H3cAddtionalSpaceMaxSize_Type=Integer32
_H3cAddtionalSpaceMaxSize_Object=MibScalar
h3cAddtionalSpaceMaxSize=_H3cAddtionalSpaceMaxSize_Object((1,3,6,1,4,1,2011,10,10,2,1,1,1),_H3cAddtionalSpaceMaxSize_Type())
h3cAddtionalSpaceMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cAddtionalSpaceMaxSize.setStatus(_A)
if mibBuilder.loadTexts:h3cAddtionalSpaceMaxSize.setUnits('TB')
_H3cSnapConfigTable_Object=MibTable
h3cSnapConfigTable=_H3cSnapConfigTable_Object((1,3,6,1,4,1,2011,10,10,2,1,2))
if mibBuilder.loadTexts:h3cSnapConfigTable.setStatus(_A)
_H3cSnapConfigEntry_Object=MibTableRow
h3cSnapConfigEntry=_H3cSnapConfigEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1))
h3cSnapConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cSnapConfigEntry.setStatus(_A)
_H3cSnapLvIndex_Type=H3cLvIDType
_H3cSnapLvIndex_Object=MibTableColumn
h3cSnapLvIndex=_H3cSnapLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,1),_H3cSnapLvIndex_Type())
h3cSnapLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSnapLvIndex.setStatus(_A)
_H3cSnapAreaId_Type=H3cLvIDType
_H3cSnapAreaId_Object=MibTableColumn
h3cSnapAreaId=_H3cSnapAreaId_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,2),_H3cSnapAreaId_Type())
h3cSnapAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapAreaId.setStatus(_A)
class _H3cSnapAreaAutoExpand_Type(H3cStorageEnableState):defaultValue=2
_H3cSnapAreaAutoExpand_Type.__name__=_M
_H3cSnapAreaAutoExpand_Object=MibTableColumn
h3cSnapAreaAutoExpand=_H3cSnapAreaAutoExpand_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,3),_H3cSnapAreaAutoExpand_Type())
h3cSnapAreaAutoExpand.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapAreaAutoExpand.setStatus(_A)
class _H3cSnapAreaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cSnapAreaThreshold_Type.__name__=_E
_H3cSnapAreaThreshold_Object=MibTableColumn
h3cSnapAreaThreshold=_H3cSnapAreaThreshold_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,4),_H3cSnapAreaThreshold_Type())
h3cSnapAreaThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapAreaThreshold.setStatus(_A)
_H3cSnapAreaIncSize_Type=Integer32
_H3cSnapAreaIncSize_Object=MibTableColumn
h3cSnapAreaIncSize=_H3cSnapAreaIncSize_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,5),_H3cSnapAreaIncSize_Type())
h3cSnapAreaIncSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapAreaIncSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSnapAreaIncSize.setUnits(_F)
_H3cSnapAreaMaxSize_Type=Integer32
_H3cSnapAreaMaxSize_Object=MibTableColumn
h3cSnapAreaMaxSize=_H3cSnapAreaMaxSize_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,6),_H3cSnapAreaMaxSize_Type())
h3cSnapAreaMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapAreaMaxSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSnapAreaMaxSize.setUnits(_F)
class _H3cSnapAreaFullDeleteTM_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rotative',1),(_I,2)))
_H3cSnapAreaFullDeleteTM_Type.__name__=_E
_H3cSnapAreaFullDeleteTM_Object=MibTableColumn
h3cSnapAreaFullDeleteTM=_H3cSnapAreaFullDeleteTM_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,7),_H3cSnapAreaFullDeleteTM_Type())
h3cSnapAreaFullDeleteTM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapAreaFullDeleteTM.setStatus(_A)
_H3cSnapAreaNotify_Type=H3cStorageEnableState
_H3cSnapAreaNotify_Object=MibTableColumn
h3cSnapAreaNotify=_H3cSnapAreaNotify_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,8),_H3cSnapAreaNotify_Type())
h3cSnapAreaNotify.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapAreaNotify.setStatus(_A)
_H3cSnapAreaStatus_Type=H3cStorageOnlineState
_H3cSnapAreaStatus_Object=MibTableColumn
h3cSnapAreaStatus=_H3cSnapAreaStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,9),_H3cSnapAreaStatus_Type())
h3cSnapAreaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapAreaStatus.setStatus(_A)
_H3cSnapRaidUuid_Type=H3cRaidIDType
_H3cSnapRaidUuid_Object=MibTableColumn
h3cSnapRaidUuid=_H3cSnapRaidUuid_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,10),_H3cSnapRaidUuid_Type())
h3cSnapRaidUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapRaidUuid.setStatus(_A)
_H3cSnapRaidSize_Type=Integer32
_H3cSnapRaidSize_Object=MibTableColumn
h3cSnapRaidSize=_H3cSnapRaidSize_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,11),_H3cSnapRaidSize_Type())
h3cSnapRaidSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapRaidSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSnapRaidSize.setUnits(_F)
class _H3cSnapRaidSelectPolicy_Type(H3cExtendSelectPolicy):defaultValue=4
_H3cSnapRaidSelectPolicy_Type.__name__=_L
_H3cSnapRaidSelectPolicy_Object=MibTableColumn
h3cSnapRaidSelectPolicy=_H3cSnapRaidSelectPolicy_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,12),_H3cSnapRaidSelectPolicy_Type())
h3cSnapRaidSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapRaidSelectPolicy.setStatus(_A)
_H3cSnapAreaTotalSize_Type=Integer32
_H3cSnapAreaTotalSize_Object=MibTableColumn
h3cSnapAreaTotalSize=_H3cSnapAreaTotalSize_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,13),_H3cSnapAreaTotalSize_Type())
h3cSnapAreaTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapAreaTotalSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSnapAreaTotalSize.setUnits(_F)
_H3cSnapAreaFreeSize_Type=Integer32
_H3cSnapAreaFreeSize_Object=MibTableColumn
h3cSnapAreaFreeSize=_H3cSnapAreaFreeSize_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,14),_H3cSnapAreaFreeSize_Type())
h3cSnapAreaFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapAreaFreeSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSnapAreaFreeSize.setUnits(_F)
_H3cSnapExtendTimes_Type=Integer32
_H3cSnapExtendTimes_Object=MibTableColumn
h3cSnapExtendTimes=_H3cSnapExtendTimes_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,15),_H3cSnapExtendTimes_Type())
h3cSnapExtendTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapExtendTimes.setStatus(_A)
_H3cSnapRowStatus_Type=RowStatus
_H3cSnapRowStatus_Object=MibTableColumn
h3cSnapRowStatus=_H3cSnapRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,2,1,16),_H3cSnapRowStatus_Type())
h3cSnapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapRowStatus.setStatus(_A)
_H3cSnapExpandTable_Object=MibTable
h3cSnapExpandTable=_H3cSnapExpandTable_Object((1,3,6,1,4,1,2011,10,10,2,1,3))
if mibBuilder.loadTexts:h3cSnapExpandTable.setStatus(_A)
_H3cSnapExpandEntry_Object=MibTableRow
h3cSnapExpandEntry=_H3cSnapExpandEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,3,1))
h3cSnapExpandEntry.setIndexNames((0,_D,_H),(0,_D,_S))
if mibBuilder.loadTexts:h3cSnapExpandEntry.setStatus(_A)
_H3cSAExpRaidUuid_Type=H3cRaidIDType
_H3cSAExpRaidUuid_Object=MibTableColumn
h3cSAExpRaidUuid=_H3cSAExpRaidUuid_Object((1,3,6,1,4,1,2011,10,10,2,1,3,1,1),_H3cSAExpRaidUuid_Type())
h3cSAExpRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSAExpRaidUuid.setStatus(_A)
_H3cSAExpSize_Type=Integer32
_H3cSAExpSize_Object=MibTableColumn
h3cSAExpSize=_H3cSAExpSize_Object((1,3,6,1,4,1,2011,10,10,2,1,3,1,2),_H3cSAExpSize_Type())
h3cSAExpSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSAExpSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSAExpSize.setUnits(_F)
_H3cSAExpRaidSize_Type=Integer32
_H3cSAExpRaidSize_Object=MibTableColumn
h3cSAExpRaidSize=_H3cSAExpRaidSize_Object((1,3,6,1,4,1,2011,10,10,2,1,3,1,3),_H3cSAExpRaidSize_Type())
h3cSAExpRaidSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSAExpRaidSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSAExpRaidSize.setUnits(_F)
_H3cSnapAreaExpRowStatus_Type=RowStatus
_H3cSnapAreaExpRowStatus_Object=MibTableColumn
h3cSnapAreaExpRowStatus=_H3cSnapAreaExpRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,3,1,4),_H3cSnapAreaExpRowStatus_Type())
h3cSnapAreaExpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnapAreaExpRowStatus.setStatus(_A)
_H3cSnapCopyTable_Object=MibTable
h3cSnapCopyTable=_H3cSnapCopyTable_Object((1,3,6,1,4,1,2011,10,10,2,1,4))
if mibBuilder.loadTexts:h3cSnapCopyTable.setStatus(_A)
_H3cSnapCopyEntry_Object=MibTableRow
h3cSnapCopyEntry=_H3cSnapCopyEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,4,1))
h3cSnapCopyEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cSnapCopyEntry.setStatus(_A)
_H3cSnapCopyLvIndex_Type=H3cLvIDType
_H3cSnapCopyLvIndex_Object=MibTableColumn
h3cSnapCopyLvIndex=_H3cSnapCopyLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,4,1,1),_H3cSnapCopyLvIndex_Type())
h3cSnapCopyLvIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSnapCopyLvIndex.setStatus(_A)
class _H3cSnapCopyPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cSnapCopyPercentage_Type.__name__=_E
_H3cSnapCopyPercentage_Object=MibTableColumn
h3cSnapCopyPercentage=_H3cSnapCopyPercentage_Object((1,3,6,1,4,1,2011,10,10,2,1,4,1,2),_H3cSnapCopyPercentage_Type())
h3cSnapCopyPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapCopyPercentage.setStatus(_A)
_H3cSnapCopyStartTime_Type=DateAndTime
_H3cSnapCopyStartTime_Object=MibTableColumn
h3cSnapCopyStartTime=_H3cSnapCopyStartTime_Object((1,3,6,1,4,1,2011,10,10,2,1,4,1,3),_H3cSnapCopyStartTime_Type())
h3cSnapCopyStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSnapCopyStartTime.setStatus(_A)
class _H3cSnapCopySwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),(_N,2),(_I,3)))
_H3cSnapCopySwitch_Type.__name__=_E
_H3cSnapCopySwitch_Object=MibTableColumn
h3cSnapCopySwitch=_H3cSnapCopySwitch_Object((1,3,6,1,4,1,2011,10,10,2,1,4,1,4),_H3cSnapCopySwitch_Type())
h3cSnapCopySwitch.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSnapCopySwitch.setStatus(_A)
_H3cTimeMarkConfigTable_Object=MibTable
h3cTimeMarkConfigTable=_H3cTimeMarkConfigTable_Object((1,3,6,1,4,1,2011,10,10,2,1,5))
if mibBuilder.loadTexts:h3cTimeMarkConfigTable.setStatus(_A)
_H3cTimeMarkConfigEntry_Object=MibTableRow
h3cTimeMarkConfigEntry=_H3cTimeMarkConfigEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,5,1))
h3cTimeMarkConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cTimeMarkConfigEntry.setStatus(_A)
class _H3cTimeMarkCounts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cTimeMarkCounts_Type.__name__=_E
_H3cTimeMarkCounts_Object=MibTableColumn
h3cTimeMarkCounts=_H3cTimeMarkCounts_Object((1,3,6,1,4,1,2011,10,10,2,1,5,1,1),_H3cTimeMarkCounts_Type())
h3cTimeMarkCounts.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTimeMarkCounts.setStatus(_A)
_H3cTimeMarkInitializeTime_Type=DateAndTime
_H3cTimeMarkInitializeTime_Object=MibTableColumn
h3cTimeMarkInitializeTime=_H3cTimeMarkInitializeTime_Object((1,3,6,1,4,1,2011,10,10,2,1,5,1,2),_H3cTimeMarkInitializeTime_Type())
h3cTimeMarkInitializeTime.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTimeMarkInitializeTime.setStatus(_A)
_H3cTimeMarkInterval_Type=Integer32
_H3cTimeMarkInterval_Object=MibTableColumn
h3cTimeMarkInterval=_H3cTimeMarkInterval_Object((1,3,6,1,4,1,2011,10,10,2,1,5,1,3),_H3cTimeMarkInterval_Type())
h3cTimeMarkInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTimeMarkInterval.setStatus(_A)
_H3cTimeMarkLastTime_Type=DateAndTime
_H3cTimeMarkLastTime_Object=MibTableColumn
h3cTimeMarkLastTime=_H3cTimeMarkLastTime_Object((1,3,6,1,4,1,2011,10,10,2,1,5,1,4),_H3cTimeMarkLastTime_Type())
h3cTimeMarkLastTime.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTimeMarkLastTime.setStatus(_A)
_H3cTimeMarkTotal_Type=Integer32
_H3cTimeMarkTotal_Object=MibTableColumn
h3cTimeMarkTotal=_H3cTimeMarkTotal_Object((1,3,6,1,4,1,2011,10,10,2,1,5,1,5),_H3cTimeMarkTotal_Type())
h3cTimeMarkTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTimeMarkTotal.setStatus(_A)
_H3cTimeMarkSwitch_Type=H3cStorageEnableState
_H3cTimeMarkSwitch_Object=MibTableColumn
h3cTimeMarkSwitch=_H3cTimeMarkSwitch_Object((1,3,6,1,4,1,2011,10,10,2,1,5,1,6),_H3cTimeMarkSwitch_Type())
h3cTimeMarkSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTimeMarkSwitch.setStatus(_A)
_H3cTimeMarkCreateTable_Object=MibTable
h3cTimeMarkCreateTable=_H3cTimeMarkCreateTable_Object((1,3,6,1,4,1,2011,10,10,2,1,6))
if mibBuilder.loadTexts:h3cTimeMarkCreateTable.setStatus(_A)
_H3cTimeMarkCreateEntry_Object=MibTableRow
h3cTimeMarkCreateEntry=_H3cTimeMarkCreateEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,6,1))
h3cTimeMarkCreateEntry.setIndexNames((0,_D,_H),(0,_D,_O))
if mibBuilder.loadTexts:h3cTimeMarkCreateEntry.setStatus(_A)
_H3cTimeMarkStamp_Type=DateAndTime
_H3cTimeMarkStamp_Object=MibTableColumn
h3cTimeMarkStamp=_H3cTimeMarkStamp_Object((1,3,6,1,4,1,2011,10,10,2,1,6,1,1),_H3cTimeMarkStamp_Type())
h3cTimeMarkStamp.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cTimeMarkStamp.setStatus(_A)
_H3cTimeMarkComment_Type=OctetString
_H3cTimeMarkComment_Object=MibTableColumn
h3cTimeMarkComment=_H3cTimeMarkComment_Object((1,3,6,1,4,1,2011,10,10,2,1,6,1,2),_H3cTimeMarkComment_Type())
h3cTimeMarkComment.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTimeMarkComment.setStatus(_A)
_H3cTimeMarkSize_Type=Integer32
_H3cTimeMarkSize_Object=MibTableColumn
h3cTimeMarkSize=_H3cTimeMarkSize_Object((1,3,6,1,4,1,2011,10,10,2,1,6,1,3),_H3cTimeMarkSize_Type())
h3cTimeMarkSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTimeMarkSize.setStatus(_A)
if mibBuilder.loadTexts:h3cTimeMarkSize.setUnits('KB')
_H3cTimeMarkRowStatus_Type=RowStatus
_H3cTimeMarkRowStatus_Object=MibTableColumn
h3cTimeMarkRowStatus=_H3cTimeMarkRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,6,1,4),_H3cTimeMarkRowStatus_Type())
h3cTimeMarkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTimeMarkRowStatus.setStatus(_A)
_H3cTimeMarkCopyTable_Object=MibTable
h3cTimeMarkCopyTable=_H3cTimeMarkCopyTable_Object((1,3,6,1,4,1,2011,10,10,2,1,7))
if mibBuilder.loadTexts:h3cTimeMarkCopyTable.setStatus(_A)
_H3cTimeMarkCopyEntry_Object=MibTableRow
h3cTimeMarkCopyEntry=_H3cTimeMarkCopyEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,7,1))
h3cTimeMarkCopyEntry.setIndexNames((0,_D,_H),(0,_D,_O))
if mibBuilder.loadTexts:h3cTimeMarkCopyEntry.setStatus(_A)
_H3cTMCopyDestLvId_Type=H3cLvIDType
_H3cTMCopyDestLvId_Object=MibTableColumn
h3cTMCopyDestLvId=_H3cTMCopyDestLvId_Object((1,3,6,1,4,1,2011,10,10,2,1,7,1,1),_H3cTMCopyDestLvId_Type())
h3cTMCopyDestLvId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTMCopyDestLvId.setStatus(_A)
class _H3cTMCopyPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cTMCopyPercentage_Type.__name__=_E
_H3cTMCopyPercentage_Object=MibTableColumn
h3cTMCopyPercentage=_H3cTMCopyPercentage_Object((1,3,6,1,4,1,2011,10,10,2,1,7,1,2),_H3cTMCopyPercentage_Type())
h3cTMCopyPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTMCopyPercentage.setStatus(_A)
_H3cTMCopyStartTime_Type=DateAndTime
_H3cTMCopyStartTime_Object=MibTableColumn
h3cTMCopyStartTime=_H3cTMCopyStartTime_Object((1,3,6,1,4,1,2011,10,10,2,1,7,1,3),_H3cTMCopyStartTime_Type())
h3cTMCopyStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTMCopyStartTime.setStatus(_A)
class _H3cTMCopySwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),(_N,2),(_I,3)))
_H3cTMCopySwitch_Type.__name__=_E
_H3cTMCopySwitch_Object=MibTableColumn
h3cTMCopySwitch=_H3cTMCopySwitch_Object((1,3,6,1,4,1,2011,10,10,2,1,7,1,4),_H3cTMCopySwitch_Type())
h3cTMCopySwitch.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTMCopySwitch.setStatus(_A)
_H3cTimeMarkRollbackTable_Object=MibTable
h3cTimeMarkRollbackTable=_H3cTimeMarkRollbackTable_Object((1,3,6,1,4,1,2011,10,10,2,1,8))
if mibBuilder.loadTexts:h3cTimeMarkRollbackTable.setStatus(_A)
_H3cTimeMarkRollbackEntry_Object=MibTableRow
h3cTimeMarkRollbackEntry=_H3cTimeMarkRollbackEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,8,1))
h3cTimeMarkRollbackEntry.setIndexNames((0,_D,_H),(0,_D,_O))
if mibBuilder.loadTexts:h3cTimeMarkRollbackEntry.setStatus(_A)
class _H3cTMRollbackPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cTMRollbackPercentage_Type.__name__=_E
_H3cTMRollbackPercentage_Object=MibTableColumn
h3cTMRollbackPercentage=_H3cTMRollbackPercentage_Object((1,3,6,1,4,1,2011,10,10,2,1,8,1,1),_H3cTMRollbackPercentage_Type())
h3cTMRollbackPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTMRollbackPercentage.setStatus(_A)
_H3cTMRollbackStartTime_Type=DateAndTime
_H3cTMRollbackStartTime_Object=MibTableColumn
h3cTMRollbackStartTime=_H3cTMRollbackStartTime_Object((1,3,6,1,4,1,2011,10,10,2,1,8,1,2),_H3cTMRollbackStartTime_Type())
h3cTMRollbackStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTMRollbackStartTime.setStatus(_A)
_H3cTMRollbackSwitch_Type=H3cStorageActionType
_H3cTMRollbackSwitch_Object=MibTableColumn
h3cTMRollbackSwitch=_H3cTMRollbackSwitch_Object((1,3,6,1,4,1,2011,10,10,2,1,8,1,3),_H3cTMRollbackSwitch_Type())
h3cTMRollbackSwitch.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTMRollbackSwitch.setStatus(_A)
_H3cTimeViewTable_Object=MibTable
h3cTimeViewTable=_H3cTimeViewTable_Object((1,3,6,1,4,1,2011,10,10,2,1,9))
if mibBuilder.loadTexts:h3cTimeViewTable.setStatus(_A)
_H3cTimeViewEntry_Object=MibTableRow
h3cTimeViewEntry=_H3cTimeViewEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,9,1))
h3cTimeViewEntry.setIndexNames((0,_D,_H),(0,_D,_T))
if mibBuilder.loadTexts:h3cTimeViewEntry.setStatus(_A)
_H3cTimeViewStamp_Type=DateAndTime
_H3cTimeViewStamp_Object=MibTableColumn
h3cTimeViewStamp=_H3cTimeViewStamp_Object((1,3,6,1,4,1,2011,10,10,2,1,9,1,1),_H3cTimeViewStamp_Type())
h3cTimeViewStamp.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cTimeViewStamp.setStatus(_A)
_H3cTimeViewID_Type=H3cLvIDType
_H3cTimeViewID_Object=MibTableColumn
h3cTimeViewID=_H3cTimeViewID_Object((1,3,6,1,4,1,2011,10,10,2,1,9,1,2),_H3cTimeViewID_Type())
h3cTimeViewID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTimeViewID.setStatus(_A)
_H3cTimeViewName_Type=OctetString
_H3cTimeViewName_Object=MibTableColumn
h3cTimeViewName=_H3cTimeViewName_Object((1,3,6,1,4,1,2011,10,10,2,1,9,1,3),_H3cTimeViewName_Type())
h3cTimeViewName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTimeViewName.setStatus(_A)
_H3cTimeViewRowStatus_Type=RowStatus
_H3cTimeViewRowStatus_Object=MibTableColumn
h3cTimeViewRowStatus=_H3cTimeViewRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,9,1,4),_H3cTimeViewRowStatus_Type())
h3cTimeViewRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTimeViewRowStatus.setStatus(_A)
_H3cReplicaConfigTable_Object=MibTable
h3cReplicaConfigTable=_H3cReplicaConfigTable_Object((1,3,6,1,4,1,2011,10,10,2,1,10))
if mibBuilder.loadTexts:h3cReplicaConfigTable.setStatus(_A)
_H3cReplicaConfigEntry_Object=MibTableRow
h3cReplicaConfigEntry=_H3cReplicaConfigEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1))
h3cReplicaConfigEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:h3cReplicaConfigEntry.setStatus(_A)
_H3cRepLocalLvIndex_Type=H3cLvIDType
_H3cRepLocalLvIndex_Object=MibTableColumn
h3cRepLocalLvIndex=_H3cRepLocalLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,1),_H3cRepLocalLvIndex_Type())
h3cRepLocalLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cRepLocalLvIndex.setStatus(_A)
class _H3cLvRepLocalWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outgoing',1),('incoming',2)))
_H3cLvRepLocalWay_Type.__name__=_E
_H3cLvRepLocalWay_Object=MibTableColumn
h3cLvRepLocalWay=_H3cLvRepLocalWay_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,2),_H3cLvRepLocalWay_Type())
h3cLvRepLocalWay.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvRepLocalWay.setStatus(_A)
_H3cRepLocalServerIP_Type=InetAddress
_H3cRepLocalServerIP_Object=MibTableColumn
h3cRepLocalServerIP=_H3cRepLocalServerIP_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,3),_H3cRepLocalServerIP_Type())
h3cRepLocalServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepLocalServerIP.setStatus(_A)
_H3cRepLocalServerIPType_Type=InetAddressType
_H3cRepLocalServerIPType_Object=MibTableColumn
h3cRepLocalServerIPType=_H3cRepLocalServerIPType_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,4),_H3cRepLocalServerIPType_Type())
h3cRepLocalServerIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepLocalServerIPType.setStatus(_A)
_H3cRepLocalServerName_Type=OctetString
_H3cRepLocalServerName_Object=MibTableColumn
h3cRepLocalServerName=_H3cRepLocalServerName_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,5),_H3cRepLocalServerName_Type())
h3cRepLocalServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRepLocalServerName.setStatus(_A)
class _H3cRepLocalServerUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cRepLocalServerUsername_Type.__name__=_K
_H3cRepLocalServerUsername_Object=MibTableColumn
h3cRepLocalServerUsername=_H3cRepLocalServerUsername_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,6),_H3cRepLocalServerUsername_Type())
h3cRepLocalServerUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepLocalServerUsername.setStatus(_A)
class _H3cRepLocalServerPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cRepLocalServerPassword_Type.__name__=_K
_H3cRepLocalServerPassword_Object=MibTableColumn
h3cRepLocalServerPassword=_H3cRepLocalServerPassword_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,7),_H3cRepLocalServerPassword_Type())
h3cRepLocalServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepLocalServerPassword.setStatus(_A)
_H3cRepRemoteServerIP_Type=InetAddress
_H3cRepRemoteServerIP_Object=MibTableColumn
h3cRepRemoteServerIP=_H3cRepRemoteServerIP_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,8),_H3cRepRemoteServerIP_Type())
h3cRepRemoteServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepRemoteServerIP.setStatus(_A)
_H3cRepRemoteServerIPType_Type=InetAddressType
_H3cRepRemoteServerIPType_Object=MibTableColumn
h3cRepRemoteServerIPType=_H3cRepRemoteServerIPType_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,9),_H3cRepRemoteServerIPType_Type())
h3cRepRemoteServerIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepRemoteServerIPType.setStatus(_A)
_H3cRepRemoteServerName_Type=OctetString
_H3cRepRemoteServerName_Object=MibTableColumn
h3cRepRemoteServerName=_H3cRepRemoteServerName_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,10),_H3cRepRemoteServerName_Type())
h3cRepRemoteServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRepRemoteServerName.setStatus(_A)
class _H3cRepRemoteServerUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cRepRemoteServerUsername_Type.__name__=_K
_H3cRepRemoteServerUsername_Object=MibTableColumn
h3cRepRemoteServerUsername=_H3cRepRemoteServerUsername_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,11),_H3cRepRemoteServerUsername_Type())
h3cRepRemoteServerUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepRemoteServerUsername.setStatus(_A)
class _H3cRepRemoteServerPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cRepRemoteServerPassword_Type.__name__=_K
_H3cRepRemoteServerPassword_Object=MibTableColumn
h3cRepRemoteServerPassword=_H3cRepRemoteServerPassword_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,12),_H3cRepRemoteServerPassword_Type())
h3cRepRemoteServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepRemoteServerPassword.setStatus(_A)
_H3cRepRemoteLvIndex_Type=H3cLvIDType
_H3cRepRemoteLvIndex_Object=MibTableColumn
h3cRepRemoteLvIndex=_H3cRepRemoteLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,13),_H3cRepRemoteLvIndex_Type())
h3cRepRemoteLvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRepRemoteLvIndex.setStatus(_A)
class _H3cReplicaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('adaptive',1),('remote',2),(_I,3)))
_H3cReplicaMode_Type.__name__=_E
_H3cReplicaMode_Object=MibTableColumn
h3cReplicaMode=_H3cReplicaMode_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,14),_H3cReplicaMode_Type())
h3cReplicaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaMode.setStatus(_A)
_H3cReplicaWatermark_Type=Integer32
_H3cReplicaWatermark_Object=MibTableColumn
h3cReplicaWatermark=_H3cReplicaWatermark_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,15),_H3cReplicaWatermark_Type())
h3cReplicaWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaWatermark.setStatus(_A)
if mibBuilder.loadTexts:h3cReplicaWatermark.setUnits(_F)
_H3cReplicaWatermarkRetry_Type=Integer32
_H3cReplicaWatermarkRetry_Object=MibTableColumn
h3cReplicaWatermarkRetry=_H3cReplicaWatermarkRetry_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,16),_H3cReplicaWatermarkRetry_Type())
h3cReplicaWatermarkRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaWatermarkRetry.setStatus(_A)
_H3cReplicaInitializeTime_Type=DateAndTime
_H3cReplicaInitializeTime_Object=MibTableColumn
h3cReplicaInitializeTime=_H3cReplicaInitializeTime_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,17),_H3cReplicaInitializeTime_Type())
h3cReplicaInitializeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaInitializeTime.setStatus(_A)
_H3cReplicaInterval_Type=Integer32
_H3cReplicaInterval_Object=MibTableColumn
h3cReplicaInterval=_H3cReplicaInterval_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,18),_H3cReplicaInterval_Type())
h3cReplicaInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaInterval.setStatus(_A)
class _H3cReplicaEncrypt_Type(H3cStorageEnableState):defaultValue=2
_H3cReplicaEncrypt_Type.__name__=_M
_H3cReplicaEncrypt_Object=MibTableColumn
h3cReplicaEncrypt=_H3cReplicaEncrypt_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,19),_H3cReplicaEncrypt_Type())
h3cReplicaEncrypt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaEncrypt.setStatus(_A)
class _H3cReplicaCompress_Type(H3cStorageEnableState):defaultValue=2
_H3cReplicaCompress_Type.__name__=_M
_H3cReplicaCompress_Object=MibTableColumn
h3cReplicaCompress=_H3cReplicaCompress_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,20),_H3cReplicaCompress_Type())
h3cReplicaCompress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaCompress.setStatus(_A)
class _H3cReplicaUseExistTM_Type(H3cStorageEnableState):defaultValue=2
_H3cReplicaUseExistTM_Type.__name__=_M
_H3cReplicaUseExistTM_Object=MibTableColumn
h3cReplicaUseExistTM=_H3cReplicaUseExistTM_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,21),_H3cReplicaUseExistTM_Type())
h3cReplicaUseExistTM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaUseExistTM.setStatus(_A)
class _H3cReplicaProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('rudp',2)))
_H3cReplicaProtocol_Type.__name__=_E
_H3cReplicaProtocol_Object=MibTableColumn
h3cReplicaProtocol=_H3cReplicaProtocol_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,22),_H3cReplicaProtocol_Type())
h3cReplicaProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaProtocol.setStatus(_A)
_H3cReplicaScanDiff_Type=TruthValue
_H3cReplicaScanDiff_Object=MibTableColumn
h3cReplicaScanDiff=_H3cReplicaScanDiff_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,23),_H3cReplicaScanDiff_Type())
h3cReplicaScanDiff.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaScanDiff.setStatus(_A)
class _H3cReplicaStatSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('promte',1),(_P,2),('scan',3),('reversal',4),(_N,5),(_Q,6),(_U,7),(_I,8)))
_H3cReplicaStatSwitch_Type.__name__=_E
_H3cReplicaStatSwitch_Object=MibTableColumn
h3cReplicaStatSwitch=_H3cReplicaStatSwitch_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,24),_H3cReplicaStatSwitch_Type())
h3cReplicaStatSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaStatSwitch.setStatus(_A)
_H3cReplicaRowStatus_Type=RowStatus
_H3cReplicaRowStatus_Object=MibTableColumn
h3cReplicaRowStatus=_H3cReplicaRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,10,1,25),_H3cReplicaRowStatus_Type())
h3cReplicaRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cReplicaRowStatus.setStatus(_A)
_H3cReplicaStateTable_Object=MibTable
h3cReplicaStateTable=_H3cReplicaStateTable_Object((1,3,6,1,4,1,2011,10,10,2,1,11))
if mibBuilder.loadTexts:h3cReplicaStateTable.setStatus(_A)
_H3cReplicaStateEntry_Object=MibTableRow
h3cReplicaStateEntry=_H3cReplicaStateEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1))
h3cReplicaStateEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:h3cReplicaStateEntry.setStatus(_A)
_H3cReplicaDelta_Type=Integer32
_H3cReplicaDelta_Object=MibTableColumn
h3cReplicaDelta=_H3cReplicaDelta_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1,1),_H3cReplicaDelta_Type())
h3cReplicaDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cReplicaDelta.setStatus(_A)
if mibBuilder.loadTexts:h3cReplicaDelta.setUnits(_F)
_H3cReplicaLastSyncTime_Type=DateAndTime
_H3cReplicaLastSyncTime_Object=MibTableColumn
h3cReplicaLastSyncTime=_H3cReplicaLastSyncTime_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1,2),_H3cReplicaLastSyncTime_Type())
h3cReplicaLastSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cReplicaLastSyncTime.setStatus(_A)
_H3cReplicaNextSyncTime_Type=DateAndTime
_H3cReplicaNextSyncTime_Object=MibTableColumn
h3cReplicaNextSyncTime=_H3cReplicaNextSyncTime_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1,3),_H3cReplicaNextSyncTime_Type())
h3cReplicaNextSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cReplicaNextSyncTime.setStatus(_A)
_H3cReplicaSyncTotalSize_Type=Integer32
_H3cReplicaSyncTotalSize_Object=MibTableColumn
h3cReplicaSyncTotalSize=_H3cReplicaSyncTotalSize_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1,4),_H3cReplicaSyncTotalSize_Type())
h3cReplicaSyncTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cReplicaSyncTotalSize.setStatus(_A)
if mibBuilder.loadTexts:h3cReplicaSyncTotalSize.setUnits(_F)
_H3cReplicaSyncCurPercentage_Type=Integer32
_H3cReplicaSyncCurPercentage_Object=MibTableColumn
h3cReplicaSyncCurPercentage=_H3cReplicaSyncCurPercentage_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1,5),_H3cReplicaSyncCurPercentage_Type())
h3cReplicaSyncCurPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cReplicaSyncCurPercentage.setStatus(_A)
_H3cReplicaSyncPerformance_Type=Integer32
_H3cReplicaSyncPerformance_Object=MibTableColumn
h3cReplicaSyncPerformance=_H3cReplicaSyncPerformance_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1,6),_H3cReplicaSyncPerformance_Type())
h3cReplicaSyncPerformance.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cReplicaSyncPerformance.setStatus(_A)
class _H3cReplicaRunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),('idle',2),(_N,3),(_P,4),('scan',5)))
_H3cReplicaRunStatus_Type.__name__=_E
_H3cReplicaRunStatus_Object=MibTableColumn
h3cReplicaRunStatus=_H3cReplicaRunStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,11,1,7),_H3cReplicaRunStatus_Type())
h3cReplicaRunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cReplicaRunStatus.setStatus(_A)
_H3cCDRConfigTable_Object=MibTable
h3cCDRConfigTable=_H3cCDRConfigTable_Object((1,3,6,1,4,1,2011,10,10,2,1,12))
if mibBuilder.loadTexts:h3cCDRConfigTable.setStatus(_A)
_H3cCDRConfigEntry_Object=MibTableRow
h3cCDRConfigEntry=_H3cCDRConfigEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1))
h3cCDRConfigEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:h3cCDRConfigEntry.setStatus(_A)
_H3cCDRLvIndex_Type=H3cLvIDType
_H3cCDRLvIndex_Object=MibTableColumn
h3cCDRLvIndex=_H3cCDRLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1,1),_H3cCDRLvIndex_Type())
h3cCDRLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cCDRLvIndex.setStatus(_A)
_H3cCDRID_Type=Integer32
_H3cCDRID_Object=MibTableColumn
h3cCDRID=_H3cCDRID_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1,2),_H3cCDRID_Type())
h3cCDRID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCDRID.setStatus(_A)
_H3cCDRStatus_Type=H3cStorageOnlineState
_H3cCDRStatus_Object=MibTableColumn
h3cCDRStatus=_H3cCDRStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1,3),_H3cCDRStatus_Type())
h3cCDRStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCDRStatus.setStatus(_A)
_H3cCDRTotalSize_Type=Integer32
_H3cCDRTotalSize_Object=MibTableColumn
h3cCDRTotalSize=_H3cCDRTotalSize_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1,4),_H3cCDRTotalSize_Type())
h3cCDRTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCDRTotalSize.setStatus(_A)
if mibBuilder.loadTexts:h3cCDRTotalSize.setUnits(_F)
_H3cCDRFreeSize_Type=Integer32
_H3cCDRFreeSize_Object=MibTableColumn
h3cCDRFreeSize=_H3cCDRFreeSize_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1,5),_H3cCDRFreeSize_Type())
h3cCDRFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCDRFreeSize.setStatus(_A)
if mibBuilder.loadTexts:h3cCDRFreeSize.setUnits(_F)
class _H3cCDRSelectPolicy_Type(H3cExtendSelectPolicy):defaultValue=4
_H3cCDRSelectPolicy_Type.__name__=_L
_H3cCDRSelectPolicy_Object=MibTableColumn
h3cCDRSelectPolicy=_H3cCDRSelectPolicy_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1,6),_H3cCDRSelectPolicy_Type())
h3cCDRSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cCDRSelectPolicy.setStatus(_A)
_H3cCDRRowStatus_Type=RowStatus
_H3cCDRRowStatus_Object=MibTableColumn
h3cCDRRowStatus=_H3cCDRRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,12,1,7),_H3cCDRRowStatus_Type())
h3cCDRRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cCDRRowStatus.setStatus(_A)
_H3cCDRDistributeTable_Object=MibTable
h3cCDRDistributeTable=_H3cCDRDistributeTable_Object((1,3,6,1,4,1,2011,10,10,2,1,13))
if mibBuilder.loadTexts:h3cCDRDistributeTable.setStatus(_A)
_H3cCDRDistributeEntry_Object=MibTableRow
h3cCDRDistributeEntry=_H3cCDRDistributeEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,13,1))
h3cCDRDistributeEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:h3cCDRDistributeEntry.setStatus(_A)
_H3cCDRDistLvIndex_Type=H3cLvIDType
_H3cCDRDistLvIndex_Object=MibTableColumn
h3cCDRDistLvIndex=_H3cCDRDistLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,13,1,1),_H3cCDRDistLvIndex_Type())
h3cCDRDistLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cCDRDistLvIndex.setStatus(_A)
_H3cCDRRaidUuid_Type=H3cRaidIDType
_H3cCDRRaidUuid_Object=MibTableColumn
h3cCDRRaidUuid=_H3cCDRRaidUuid_Object((1,3,6,1,4,1,2011,10,10,2,1,13,1,2),_H3cCDRRaidUuid_Type())
h3cCDRRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cCDRRaidUuid.setStatus(_A)
_H3cCDRRaidSize_Type=Integer32
_H3cCDRRaidSize_Object=MibTableColumn
h3cCDRRaidSize=_H3cCDRRaidSize_Object((1,3,6,1,4,1,2011,10,10,2,1,13,1,3),_H3cCDRRaidSize_Type())
h3cCDRRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cCDRRaidSize.setStatus(_A)
if mibBuilder.loadTexts:h3cCDRRaidSize.setUnits(_F)
_H3cCDRExtRowStatus_Type=RowStatus
_H3cCDRExtRowStatus_Object=MibTableColumn
h3cCDRExtRowStatus=_H3cCDRExtRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,13,1,4),_H3cCDRExtRowStatus_Type())
h3cCDRExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cCDRExtRowStatus.setStatus(_A)
_H3cSafeCacheConfigTable_Object=MibTable
h3cSafeCacheConfigTable=_H3cSafeCacheConfigTable_Object((1,3,6,1,4,1,2011,10,10,2,1,14))
if mibBuilder.loadTexts:h3cSafeCacheConfigTable.setStatus(_A)
_H3cSafeCacheConfigEntry_Object=MibTableRow
h3cSafeCacheConfigEntry=_H3cSafeCacheConfigEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1))
h3cSafeCacheConfigEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:h3cSafeCacheConfigEntry.setStatus(_A)
_H3cSafeCacheLvIndex_Type=H3cLvIDType
_H3cSafeCacheLvIndex_Object=MibTableColumn
h3cSafeCacheLvIndex=_H3cSafeCacheLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,1),_H3cSafeCacheLvIndex_Type())
h3cSafeCacheLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSafeCacheLvIndex.setStatus(_A)
_H3cSafeCacheID_Type=Integer32
_H3cSafeCacheID_Object=MibTableColumn
h3cSafeCacheID=_H3cSafeCacheID_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,2),_H3cSafeCacheID_Type())
h3cSafeCacheID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSafeCacheID.setStatus(_A)
_H3cSafeCacheStatus_Type=H3cStorageOnlineState
_H3cSafeCacheStatus_Object=MibTableColumn
h3cSafeCacheStatus=_H3cSafeCacheStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,3),_H3cSafeCacheStatus_Type())
h3cSafeCacheStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSafeCacheStatus.setStatus(_A)
_H3cSafeCacheTotalSize_Type=Integer32
_H3cSafeCacheTotalSize_Object=MibTableColumn
h3cSafeCacheTotalSize=_H3cSafeCacheTotalSize_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,4),_H3cSafeCacheTotalSize_Type())
h3cSafeCacheTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSafeCacheTotalSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSafeCacheTotalSize.setUnits(_F)
_H3cSafeCacheFreeSize_Type=Integer32
_H3cSafeCacheFreeSize_Object=MibTableColumn
h3cSafeCacheFreeSize=_H3cSafeCacheFreeSize_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,5),_H3cSafeCacheFreeSize_Type())
h3cSafeCacheFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSafeCacheFreeSize.setStatus(_A)
if mibBuilder.loadTexts:h3cSafeCacheFreeSize.setUnits(_F)
class _H3cSafeCacheSelectPolicy_Type(H3cExtendSelectPolicy):defaultValue=4
_H3cSafeCacheSelectPolicy_Type.__name__=_L
_H3cSafeCacheSelectPolicy_Object=MibTableColumn
h3cSafeCacheSelectPolicy=_H3cSafeCacheSelectPolicy_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,6),_H3cSafeCacheSelectPolicy_Type())
h3cSafeCacheSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheSelectPolicy.setStatus(_A)
class _H3cSafeCacheThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cSafeCacheThreshold_Type.__name__=_E
_H3cSafeCacheThreshold_Object=MibTableColumn
h3cSafeCacheThreshold=_H3cSafeCacheThreshold_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,7),_H3cSafeCacheThreshold_Type())
h3cSafeCacheThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheThreshold.setStatus(_A)
_H3cSafeCacheFlushTime_Type=Integer32
_H3cSafeCacheFlushTime_Object=MibTableColumn
h3cSafeCacheFlushTime=_H3cSafeCacheFlushTime_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,8),_H3cSafeCacheFlushTime_Type())
h3cSafeCacheFlushTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheFlushTime.setStatus(_A)
class _H3cSafeCacheFlushCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cSafeCacheFlushCommand_Type.__name__=_E
_H3cSafeCacheFlushCommand_Object=MibTableColumn
h3cSafeCacheFlushCommand=_H3cSafeCacheFlushCommand_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,9),_H3cSafeCacheFlushCommand_Type())
h3cSafeCacheFlushCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheFlushCommand.setStatus(_A)
class _H3cSafeCacheSkipDupWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_H3cSafeCacheSkipDupWrite_Type.__name__=_E
_H3cSafeCacheSkipDupWrite_Object=MibTableColumn
h3cSafeCacheSkipDupWrite=_H3cSafeCacheSkipDupWrite_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,10),_H3cSafeCacheSkipDupWrite_Type())
h3cSafeCacheSkipDupWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheSkipDupWrite.setStatus(_A)
class _H3cSafeCacheRunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('run',1),(_Q,2)))
_H3cSafeCacheRunStatus_Type.__name__=_E
_H3cSafeCacheRunStatus_Object=MibTableColumn
h3cSafeCacheRunStatus=_H3cSafeCacheRunStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,11),_H3cSafeCacheRunStatus_Type())
h3cSafeCacheRunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSafeCacheRunStatus.setStatus(_A)
class _H3cSafeCacheSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_U,2),(_I,3)))
_H3cSafeCacheSwitch_Type.__name__=_E
_H3cSafeCacheSwitch_Object=MibTableColumn
h3cSafeCacheSwitch=_H3cSafeCacheSwitch_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,12),_H3cSafeCacheSwitch_Type())
h3cSafeCacheSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheSwitch.setStatus(_A)
_H3cSafeCacheRowStatus_Type=RowStatus
_H3cSafeCacheRowStatus_Object=MibTableColumn
h3cSafeCacheRowStatus=_H3cSafeCacheRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,14,1,13),_H3cSafeCacheRowStatus_Type())
h3cSafeCacheRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheRowStatus.setStatus(_A)
_H3cSafeCacheDistributeTable_Object=MibTable
h3cSafeCacheDistributeTable=_H3cSafeCacheDistributeTable_Object((1,3,6,1,4,1,2011,10,10,2,1,15))
if mibBuilder.loadTexts:h3cSafeCacheDistributeTable.setStatus(_A)
_H3cSafeCacheDistributeEntry_Object=MibTableRow
h3cSafeCacheDistributeEntry=_H3cSafeCacheDistributeEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,15,1))
h3cSafeCacheDistributeEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:h3cSafeCacheDistributeEntry.setStatus(_A)
_H3cSafeCacheDistLvIndex_Type=H3cLvIDType
_H3cSafeCacheDistLvIndex_Object=MibTableColumn
h3cSafeCacheDistLvIndex=_H3cSafeCacheDistLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,15,1,1),_H3cSafeCacheDistLvIndex_Type())
h3cSafeCacheDistLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSafeCacheDistLvIndex.setStatus(_A)
_H3cSafeCacheRaidUuid_Type=H3cRaidIDType
_H3cSafeCacheRaidUuid_Object=MibTableColumn
h3cSafeCacheRaidUuid=_H3cSafeCacheRaidUuid_Object((1,3,6,1,4,1,2011,10,10,2,1,15,1,2),_H3cSafeCacheRaidUuid_Type())
h3cSafeCacheRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSafeCacheRaidUuid.setStatus(_A)
_H3cSafeCacheRaidSize_Type=Integer32
_H3cSafeCacheRaidSize_Object=MibTableColumn
h3cSafeCacheRaidSize=_H3cSafeCacheRaidSize_Object((1,3,6,1,4,1,2011,10,10,2,1,15,1,3),_H3cSafeCacheRaidSize_Type())
h3cSafeCacheRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheRaidSize.setStatus(_A)
_H3cSafeCacheExtRowStatus_Type=RowStatus
_H3cSafeCacheExtRowStatus_Object=MibTableColumn
h3cSafeCacheExtRowStatus=_H3cSafeCacheExtRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,15,1,4),_H3cSafeCacheExtRowStatus_Type())
h3cSafeCacheExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSafeCacheExtRowStatus.setStatus(_A)
_H3cMirrorConfigTable_Object=MibTable
h3cMirrorConfigTable=_H3cMirrorConfigTable_Object((1,3,6,1,4,1,2011,10,10,2,1,16))
if mibBuilder.loadTexts:h3cMirrorConfigTable.setStatus(_A)
_H3cMirrorConfigEntry_Object=MibTableRow
h3cMirrorConfigEntry=_H3cMirrorConfigEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1))
h3cMirrorConfigEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:h3cMirrorConfigEntry.setStatus(_A)
_H3cMirrorLvIndex_Type=H3cLvIDType
_H3cMirrorLvIndex_Object=MibTableColumn
h3cMirrorLvIndex=_H3cMirrorLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,1),_H3cMirrorLvIndex_Type())
h3cMirrorLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMirrorLvIndex.setStatus(_A)
class _H3cMirrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('async',2),(_I,3)))
_H3cMirrorType_Type.__name__=_E
_H3cMirrorType_Object=MibTableColumn
h3cMirrorType=_H3cMirrorType_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,2),_H3cMirrorType_Type())
h3cMirrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMirrorType.setStatus(_A)
_H3cMirrorStatus_Type=H3cStorageOnlineState
_H3cMirrorStatus_Object=MibTableColumn
h3cMirrorStatus=_H3cMirrorStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,3),_H3cMirrorStatus_Type())
h3cMirrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMirrorStatus.setStatus(_A)
_H3cMirrorName_Type=OctetString
_H3cMirrorName_Object=MibTableColumn
h3cMirrorName=_H3cMirrorName_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,4),_H3cMirrorName_Type())
h3cMirrorName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorName.setStatus(_A)
class _H3cMirrorSyncPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cMirrorSyncPercentage_Type.__name__=_E
_H3cMirrorSyncPercentage_Object=MibTableColumn
h3cMirrorSyncPercentage=_H3cMirrorSyncPercentage_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,5),_H3cMirrorSyncPercentage_Type())
h3cMirrorSyncPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMirrorSyncPercentage.setStatus(_A)
class _H3cMirrorSyncPerformance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cMirrorSyncPerformance_Type.__name__=_E
_H3cMirrorSyncPerformance_Object=MibTableColumn
h3cMirrorSyncPerformance=_H3cMirrorSyncPerformance_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,6),_H3cMirrorSyncPerformance_Type())
h3cMirrorSyncPerformance.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMirrorSyncPerformance.setStatus(_A)
_H3cMirrorDelta_Type=Integer32
_H3cMirrorDelta_Object=MibTableColumn
h3cMirrorDelta=_H3cMirrorDelta_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,7),_H3cMirrorDelta_Type())
h3cMirrorDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMirrorDelta.setStatus(_A)
if mibBuilder.loadTexts:h3cMirrorDelta.setUnits(_F)
class _H3cMirrorRaidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('virtual',1),('serviceEnable',2),(_I,3)))
_H3cMirrorRaidType_Type.__name__=_E
_H3cMirrorRaidType_Object=MibTableColumn
h3cMirrorRaidType=_H3cMirrorRaidType_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,8),_H3cMirrorRaidType_Type())
h3cMirrorRaidType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorRaidType.setStatus(_A)
class _H3cMirrorSelectPolicy_Type(H3cExtendSelectPolicy):defaultValue=4
_H3cMirrorSelectPolicy_Type.__name__=_L
_H3cMirrorSelectPolicy_Object=MibTableColumn
h3cMirrorSelectPolicy=_H3cMirrorSelectPolicy_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,9),_H3cMirrorSelectPolicy_Type())
h3cMirrorSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorSelectPolicy.setStatus(_A)
class _H3cMirrorSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('swap',2),('promote',3),(_I,4)))
_H3cMirrorSwitch_Type.__name__=_E
_H3cMirrorSwitch_Object=MibTableColumn
h3cMirrorSwitch=_H3cMirrorSwitch_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,10),_H3cMirrorSwitch_Type())
h3cMirrorSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorSwitch.setStatus(_A)
_H3cMirrorExtendRaidUuid_Type=H3cRaidIDType
_H3cMirrorExtendRaidUuid_Object=MibTableColumn
h3cMirrorExtendRaidUuid=_H3cMirrorExtendRaidUuid_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,11),_H3cMirrorExtendRaidUuid_Type())
h3cMirrorExtendRaidUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorExtendRaidUuid.setStatus(_A)
_H3cMirrorRowStatus_Type=RowStatus
_H3cMirrorRowStatus_Object=MibTableColumn
h3cMirrorRowStatus=_H3cMirrorRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,16,1,12),_H3cMirrorRowStatus_Type())
h3cMirrorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorRowStatus.setStatus(_A)
_H3cMirrorDistributeTable_Object=MibTable
h3cMirrorDistributeTable=_H3cMirrorDistributeTable_Object((1,3,6,1,4,1,2011,10,10,2,1,17))
if mibBuilder.loadTexts:h3cMirrorDistributeTable.setStatus(_A)
_H3cMirrorDistributeEntry_Object=MibTableRow
h3cMirrorDistributeEntry=_H3cMirrorDistributeEntry_Object((1,3,6,1,4,1,2011,10,10,2,1,17,1))
h3cMirrorDistributeEntry.setIndexNames((0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:h3cMirrorDistributeEntry.setStatus(_A)
_H3cMirrorDistLvIndex_Type=H3cLvIDType
_H3cMirrorDistLvIndex_Object=MibTableColumn
h3cMirrorDistLvIndex=_H3cMirrorDistLvIndex_Object((1,3,6,1,4,1,2011,10,10,2,1,17,1,1),_H3cMirrorDistLvIndex_Type())
h3cMirrorDistLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMirrorDistLvIndex.setStatus(_A)
_H3cMirrorRaidUuid_Type=H3cRaidIDType
_H3cMirrorRaidUuid_Object=MibTableColumn
h3cMirrorRaidUuid=_H3cMirrorRaidUuid_Object((1,3,6,1,4,1,2011,10,10,2,1,17,1,2),_H3cMirrorRaidUuid_Type())
h3cMirrorRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMirrorRaidUuid.setStatus(_A)
_H3cMirrorRaidSize_Type=Integer32
_H3cMirrorRaidSize_Object=MibTableColumn
h3cMirrorRaidSize=_H3cMirrorRaidSize_Object((1,3,6,1,4,1,2011,10,10,2,1,17,1,3),_H3cMirrorRaidSize_Type())
h3cMirrorRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorRaidSize.setStatus(_A)
_H3cMirrorExtRowStatus_Type=RowStatus
_H3cMirrorExtRowStatus_Object=MibTableColumn
h3cMirrorExtRowStatus=_H3cMirrorExtRowStatus_Object((1,3,6,1,4,1,2011,10,10,2,1,17,1,4),_H3cMirrorExtRowStatus_Type())
h3cMirrorExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMirrorExtRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cStorageSnap':h3cStorageSnap,'h3cSnapMibObjects':h3cSnapMibObjects,'h3cGlobalSnapSettingsObject':h3cGlobalSnapSettingsObject,'h3cAddtionalSpaceMaxSize':h3cAddtionalSpaceMaxSize,'h3cSnapConfigTable':h3cSnapConfigTable,'h3cSnapConfigEntry':h3cSnapConfigEntry,_H:h3cSnapLvIndex,'h3cSnapAreaId':h3cSnapAreaId,'h3cSnapAreaAutoExpand':h3cSnapAreaAutoExpand,'h3cSnapAreaThreshold':h3cSnapAreaThreshold,'h3cSnapAreaIncSize':h3cSnapAreaIncSize,'h3cSnapAreaMaxSize':h3cSnapAreaMaxSize,'h3cSnapAreaFullDeleteTM':h3cSnapAreaFullDeleteTM,'h3cSnapAreaNotify':h3cSnapAreaNotify,'h3cSnapAreaStatus':h3cSnapAreaStatus,'h3cSnapRaidUuid':h3cSnapRaidUuid,'h3cSnapRaidSize':h3cSnapRaidSize,'h3cSnapRaidSelectPolicy':h3cSnapRaidSelectPolicy,'h3cSnapAreaTotalSize':h3cSnapAreaTotalSize,'h3cSnapAreaFreeSize':h3cSnapAreaFreeSize,'h3cSnapExtendTimes':h3cSnapExtendTimes,'h3cSnapRowStatus':h3cSnapRowStatus,'h3cSnapExpandTable':h3cSnapExpandTable,'h3cSnapExpandEntry':h3cSnapExpandEntry,_S:h3cSAExpRaidUuid,'h3cSAExpSize':h3cSAExpSize,'h3cSAExpRaidSize':h3cSAExpRaidSize,'h3cSnapAreaExpRowStatus':h3cSnapAreaExpRowStatus,'h3cSnapCopyTable':h3cSnapCopyTable,'h3cSnapCopyEntry':h3cSnapCopyEntry,'h3cSnapCopyLvIndex':h3cSnapCopyLvIndex,'h3cSnapCopyPercentage':h3cSnapCopyPercentage,'h3cSnapCopyStartTime':h3cSnapCopyStartTime,'h3cSnapCopySwitch':h3cSnapCopySwitch,'h3cTimeMarkConfigTable':h3cTimeMarkConfigTable,'h3cTimeMarkConfigEntry':h3cTimeMarkConfigEntry,'h3cTimeMarkCounts':h3cTimeMarkCounts,'h3cTimeMarkInitializeTime':h3cTimeMarkInitializeTime,'h3cTimeMarkInterval':h3cTimeMarkInterval,'h3cTimeMarkLastTime':h3cTimeMarkLastTime,'h3cTimeMarkTotal':h3cTimeMarkTotal,'h3cTimeMarkSwitch':h3cTimeMarkSwitch,'h3cTimeMarkCreateTable':h3cTimeMarkCreateTable,'h3cTimeMarkCreateEntry':h3cTimeMarkCreateEntry,_O:h3cTimeMarkStamp,'h3cTimeMarkComment':h3cTimeMarkComment,'h3cTimeMarkSize':h3cTimeMarkSize,'h3cTimeMarkRowStatus':h3cTimeMarkRowStatus,'h3cTimeMarkCopyTable':h3cTimeMarkCopyTable,'h3cTimeMarkCopyEntry':h3cTimeMarkCopyEntry,'h3cTMCopyDestLvId':h3cTMCopyDestLvId,'h3cTMCopyPercentage':h3cTMCopyPercentage,'h3cTMCopyStartTime':h3cTMCopyStartTime,'h3cTMCopySwitch':h3cTMCopySwitch,'h3cTimeMarkRollbackTable':h3cTimeMarkRollbackTable,'h3cTimeMarkRollbackEntry':h3cTimeMarkRollbackEntry,'h3cTMRollbackPercentage':h3cTMRollbackPercentage,'h3cTMRollbackStartTime':h3cTMRollbackStartTime,'h3cTMRollbackSwitch':h3cTMRollbackSwitch,'h3cTimeViewTable':h3cTimeViewTable,'h3cTimeViewEntry':h3cTimeViewEntry,_T:h3cTimeViewStamp,'h3cTimeViewID':h3cTimeViewID,'h3cTimeViewName':h3cTimeViewName,'h3cTimeViewRowStatus':h3cTimeViewRowStatus,'h3cReplicaConfigTable':h3cReplicaConfigTable,'h3cReplicaConfigEntry':h3cReplicaConfigEntry,_R:h3cRepLocalLvIndex,'h3cLvRepLocalWay':h3cLvRepLocalWay,'h3cRepLocalServerIP':h3cRepLocalServerIP,'h3cRepLocalServerIPType':h3cRepLocalServerIPType,'h3cRepLocalServerName':h3cRepLocalServerName,'h3cRepLocalServerUsername':h3cRepLocalServerUsername,'h3cRepLocalServerPassword':h3cRepLocalServerPassword,'h3cRepRemoteServerIP':h3cRepRemoteServerIP,'h3cRepRemoteServerIPType':h3cRepRemoteServerIPType,'h3cRepRemoteServerName':h3cRepRemoteServerName,'h3cRepRemoteServerUsername':h3cRepRemoteServerUsername,'h3cRepRemoteServerPassword':h3cRepRemoteServerPassword,'h3cRepRemoteLvIndex':h3cRepRemoteLvIndex,'h3cReplicaMode':h3cReplicaMode,'h3cReplicaWatermark':h3cReplicaWatermark,'h3cReplicaWatermarkRetry':h3cReplicaWatermarkRetry,'h3cReplicaInitializeTime':h3cReplicaInitializeTime,'h3cReplicaInterval':h3cReplicaInterval,'h3cReplicaEncrypt':h3cReplicaEncrypt,'h3cReplicaCompress':h3cReplicaCompress,'h3cReplicaUseExistTM':h3cReplicaUseExistTM,'h3cReplicaProtocol':h3cReplicaProtocol,'h3cReplicaScanDiff':h3cReplicaScanDiff,'h3cReplicaStatSwitch':h3cReplicaStatSwitch,'h3cReplicaRowStatus':h3cReplicaRowStatus,'h3cReplicaStateTable':h3cReplicaStateTable,'h3cReplicaStateEntry':h3cReplicaStateEntry,'h3cReplicaDelta':h3cReplicaDelta,'h3cReplicaLastSyncTime':h3cReplicaLastSyncTime,'h3cReplicaNextSyncTime':h3cReplicaNextSyncTime,'h3cReplicaSyncTotalSize':h3cReplicaSyncTotalSize,'h3cReplicaSyncCurPercentage':h3cReplicaSyncCurPercentage,'h3cReplicaSyncPerformance':h3cReplicaSyncPerformance,'h3cReplicaRunStatus':h3cReplicaRunStatus,'h3cCDRConfigTable':h3cCDRConfigTable,'h3cCDRConfigEntry':h3cCDRConfigEntry,_V:h3cCDRLvIndex,'h3cCDRID':h3cCDRID,'h3cCDRStatus':h3cCDRStatus,'h3cCDRTotalSize':h3cCDRTotalSize,'h3cCDRFreeSize':h3cCDRFreeSize,'h3cCDRSelectPolicy':h3cCDRSelectPolicy,'h3cCDRRowStatus':h3cCDRRowStatus,'h3cCDRDistributeTable':h3cCDRDistributeTable,'h3cCDRDistributeEntry':h3cCDRDistributeEntry,_W:h3cCDRDistLvIndex,_X:h3cCDRRaidUuid,'h3cCDRRaidSize':h3cCDRRaidSize,'h3cCDRExtRowStatus':h3cCDRExtRowStatus,'h3cSafeCacheConfigTable':h3cSafeCacheConfigTable,'h3cSafeCacheConfigEntry':h3cSafeCacheConfigEntry,_Y:h3cSafeCacheLvIndex,'h3cSafeCacheID':h3cSafeCacheID,'h3cSafeCacheStatus':h3cSafeCacheStatus,'h3cSafeCacheTotalSize':h3cSafeCacheTotalSize,'h3cSafeCacheFreeSize':h3cSafeCacheFreeSize,'h3cSafeCacheSelectPolicy':h3cSafeCacheSelectPolicy,'h3cSafeCacheThreshold':h3cSafeCacheThreshold,'h3cSafeCacheFlushTime':h3cSafeCacheFlushTime,'h3cSafeCacheFlushCommand':h3cSafeCacheFlushCommand,'h3cSafeCacheSkipDupWrite':h3cSafeCacheSkipDupWrite,'h3cSafeCacheRunStatus':h3cSafeCacheRunStatus,'h3cSafeCacheSwitch':h3cSafeCacheSwitch,'h3cSafeCacheRowStatus':h3cSafeCacheRowStatus,'h3cSafeCacheDistributeTable':h3cSafeCacheDistributeTable,'h3cSafeCacheDistributeEntry':h3cSafeCacheDistributeEntry,_Z:h3cSafeCacheDistLvIndex,_a:h3cSafeCacheRaidUuid,'h3cSafeCacheRaidSize':h3cSafeCacheRaidSize,'h3cSafeCacheExtRowStatus':h3cSafeCacheExtRowStatus,'h3cMirrorConfigTable':h3cMirrorConfigTable,'h3cMirrorConfigEntry':h3cMirrorConfigEntry,_b:h3cMirrorLvIndex,'h3cMirrorType':h3cMirrorType,'h3cMirrorStatus':h3cMirrorStatus,'h3cMirrorName':h3cMirrorName,'h3cMirrorSyncPercentage':h3cMirrorSyncPercentage,'h3cMirrorSyncPerformance':h3cMirrorSyncPerformance,'h3cMirrorDelta':h3cMirrorDelta,'h3cMirrorRaidType':h3cMirrorRaidType,'h3cMirrorSelectPolicy':h3cMirrorSelectPolicy,'h3cMirrorSwitch':h3cMirrorSwitch,'h3cMirrorExtendRaidUuid':h3cMirrorExtendRaidUuid,'h3cMirrorRowStatus':h3cMirrorRowStatus,'h3cMirrorDistributeTable':h3cMirrorDistributeTable,'h3cMirrorDistributeEntry':h3cMirrorDistributeEntry,_c:h3cMirrorDistLvIndex,_d:h3cMirrorRaidUuid,'h3cMirrorRaidSize':h3cMirrorRaidSize,'h3cMirrorExtRowStatus':h3cMirrorExtRowStatus})