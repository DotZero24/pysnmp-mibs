_d='hh3cMirrorRaidUuid'
_c='hh3cMirrorDistLvIndex'
_b='hh3cMirrorLvIndex'
_a='hh3cSafeCacheRaidUuid'
_Z='hh3cSafeCacheDistLvIndex'
_Y='hh3cSafeCacheLvIndex'
_X='hh3cCDRRaidUuid'
_W='hh3cCDRDistLvIndex'
_V='hh3cCDRLvIndex'
_U='resume'
_T='hh3cTimeViewStamp'
_S='hh3cSAExpRaidUuid'
_R='hh3cRepLocalLvIndex'
_Q='suspend'
_P='sync'
_O='hh3cTimeMarkStamp'
_N='stop'
_M='Hh3cStorageEnableState'
_L='Hh3cExtendSelectPolicy'
_K='OctetString'
_J='read-write'
_I='none'
_H='hh3cSnapLvIndex'
_G='not-accessible'
_F='MB'
_E='Integer32'
_D='HH3C-STORAGE-SNAP-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex')
Hh3cExtendSelectPolicy,Hh3cLvIDType,Hh3cRaidIDType,Hh3cStorageActionType,Hh3cStorageEnableState,Hh3cStorageOnlineState,hh3cStorageRef=mibBuilder.importSymbols('HH3C-STORAGE-REF-MIB',_L,'Hh3cLvIDType','Hh3cRaidIDType','Hh3cStorageActionType',_M,'Hh3cStorageOnlineState','hh3cStorageRef')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hh3cStorageSnap=ModuleIdentity((1,3,6,1,4,1,25506,10,2))
_Hh3cSnapMibObjects_ObjectIdentity=ObjectIdentity
hh3cSnapMibObjects=_Hh3cSnapMibObjects_ObjectIdentity((1,3,6,1,4,1,25506,10,2,1))
_Hh3cGlobalSnapSettingsObject_ObjectIdentity=ObjectIdentity
hh3cGlobalSnapSettingsObject=_Hh3cGlobalSnapSettingsObject_ObjectIdentity((1,3,6,1,4,1,25506,10,2,1,1))
_Hh3cAddtionalSpaceMaxSize_Type=Integer32
_Hh3cAddtionalSpaceMaxSize_Object=MibScalar
hh3cAddtionalSpaceMaxSize=_Hh3cAddtionalSpaceMaxSize_Object((1,3,6,1,4,1,25506,10,2,1,1,1),_Hh3cAddtionalSpaceMaxSize_Type())
hh3cAddtionalSpaceMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cAddtionalSpaceMaxSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cAddtionalSpaceMaxSize.setUnits('TB')
_Hh3cSnapConfigTable_Object=MibTable
hh3cSnapConfigTable=_Hh3cSnapConfigTable_Object((1,3,6,1,4,1,25506,10,2,1,2))
if mibBuilder.loadTexts:hh3cSnapConfigTable.setStatus(_A)
_Hh3cSnapConfigEntry_Object=MibTableRow
hh3cSnapConfigEntry=_Hh3cSnapConfigEntry_Object((1,3,6,1,4,1,25506,10,2,1,2,1))
hh3cSnapConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hh3cSnapConfigEntry.setStatus(_A)
_Hh3cSnapLvIndex_Type=Hh3cLvIDType
_Hh3cSnapLvIndex_Object=MibTableColumn
hh3cSnapLvIndex=_Hh3cSnapLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,2,1,1),_Hh3cSnapLvIndex_Type())
hh3cSnapLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSnapLvIndex.setStatus(_A)
_Hh3cSnapAreaId_Type=Hh3cLvIDType
_Hh3cSnapAreaId_Object=MibTableColumn
hh3cSnapAreaId=_Hh3cSnapAreaId_Object((1,3,6,1,4,1,25506,10,2,1,2,1,2),_Hh3cSnapAreaId_Type())
hh3cSnapAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapAreaId.setStatus(_A)
class _Hh3cSnapAreaAutoExpand_Type(Hh3cStorageEnableState):defaultValue=2
_Hh3cSnapAreaAutoExpand_Type.__name__=_M
_Hh3cSnapAreaAutoExpand_Object=MibTableColumn
hh3cSnapAreaAutoExpand=_Hh3cSnapAreaAutoExpand_Object((1,3,6,1,4,1,25506,10,2,1,2,1,3),_Hh3cSnapAreaAutoExpand_Type())
hh3cSnapAreaAutoExpand.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapAreaAutoExpand.setStatus(_A)
class _Hh3cSnapAreaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hh3cSnapAreaThreshold_Type.__name__=_E
_Hh3cSnapAreaThreshold_Object=MibTableColumn
hh3cSnapAreaThreshold=_Hh3cSnapAreaThreshold_Object((1,3,6,1,4,1,25506,10,2,1,2,1,4),_Hh3cSnapAreaThreshold_Type())
hh3cSnapAreaThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapAreaThreshold.setStatus(_A)
_Hh3cSnapAreaIncSize_Type=Integer32
_Hh3cSnapAreaIncSize_Object=MibTableColumn
hh3cSnapAreaIncSize=_Hh3cSnapAreaIncSize_Object((1,3,6,1,4,1,25506,10,2,1,2,1,5),_Hh3cSnapAreaIncSize_Type())
hh3cSnapAreaIncSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapAreaIncSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSnapAreaIncSize.setUnits(_F)
_Hh3cSnapAreaMaxSize_Type=Integer32
_Hh3cSnapAreaMaxSize_Object=MibTableColumn
hh3cSnapAreaMaxSize=_Hh3cSnapAreaMaxSize_Object((1,3,6,1,4,1,25506,10,2,1,2,1,6),_Hh3cSnapAreaMaxSize_Type())
hh3cSnapAreaMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapAreaMaxSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSnapAreaMaxSize.setUnits(_F)
class _Hh3cSnapAreaFullDeleteTM_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rotative',1),(_I,2)))
_Hh3cSnapAreaFullDeleteTM_Type.__name__=_E
_Hh3cSnapAreaFullDeleteTM_Object=MibTableColumn
hh3cSnapAreaFullDeleteTM=_Hh3cSnapAreaFullDeleteTM_Object((1,3,6,1,4,1,25506,10,2,1,2,1,7),_Hh3cSnapAreaFullDeleteTM_Type())
hh3cSnapAreaFullDeleteTM.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapAreaFullDeleteTM.setStatus(_A)
_Hh3cSnapAreaNotify_Type=Hh3cStorageEnableState
_Hh3cSnapAreaNotify_Object=MibTableColumn
hh3cSnapAreaNotify=_Hh3cSnapAreaNotify_Object((1,3,6,1,4,1,25506,10,2,1,2,1,8),_Hh3cSnapAreaNotify_Type())
hh3cSnapAreaNotify.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapAreaNotify.setStatus(_A)
_Hh3cSnapAreaStatus_Type=Hh3cStorageOnlineState
_Hh3cSnapAreaStatus_Object=MibTableColumn
hh3cSnapAreaStatus=_Hh3cSnapAreaStatus_Object((1,3,6,1,4,1,25506,10,2,1,2,1,9),_Hh3cSnapAreaStatus_Type())
hh3cSnapAreaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapAreaStatus.setStatus(_A)
_Hh3cSnapRaidUuid_Type=Hh3cRaidIDType
_Hh3cSnapRaidUuid_Object=MibTableColumn
hh3cSnapRaidUuid=_Hh3cSnapRaidUuid_Object((1,3,6,1,4,1,25506,10,2,1,2,1,10),_Hh3cSnapRaidUuid_Type())
hh3cSnapRaidUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapRaidUuid.setStatus(_A)
_Hh3cSnapRaidSize_Type=Integer32
_Hh3cSnapRaidSize_Object=MibTableColumn
hh3cSnapRaidSize=_Hh3cSnapRaidSize_Object((1,3,6,1,4,1,25506,10,2,1,2,1,11),_Hh3cSnapRaidSize_Type())
hh3cSnapRaidSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapRaidSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSnapRaidSize.setUnits(_F)
class _Hh3cSnapRaidSelectPolicy_Type(Hh3cExtendSelectPolicy):defaultValue=4
_Hh3cSnapRaidSelectPolicy_Type.__name__=_L
_Hh3cSnapRaidSelectPolicy_Object=MibTableColumn
hh3cSnapRaidSelectPolicy=_Hh3cSnapRaidSelectPolicy_Object((1,3,6,1,4,1,25506,10,2,1,2,1,12),_Hh3cSnapRaidSelectPolicy_Type())
hh3cSnapRaidSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapRaidSelectPolicy.setStatus(_A)
_Hh3cSnapAreaTotalSize_Type=Integer32
_Hh3cSnapAreaTotalSize_Object=MibTableColumn
hh3cSnapAreaTotalSize=_Hh3cSnapAreaTotalSize_Object((1,3,6,1,4,1,25506,10,2,1,2,1,13),_Hh3cSnapAreaTotalSize_Type())
hh3cSnapAreaTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapAreaTotalSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSnapAreaTotalSize.setUnits(_F)
_Hh3cSnapAreaFreeSize_Type=Integer32
_Hh3cSnapAreaFreeSize_Object=MibTableColumn
hh3cSnapAreaFreeSize=_Hh3cSnapAreaFreeSize_Object((1,3,6,1,4,1,25506,10,2,1,2,1,14),_Hh3cSnapAreaFreeSize_Type())
hh3cSnapAreaFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapAreaFreeSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSnapAreaFreeSize.setUnits(_F)
_Hh3cSnapExtendTimes_Type=Integer32
_Hh3cSnapExtendTimes_Object=MibTableColumn
hh3cSnapExtendTimes=_Hh3cSnapExtendTimes_Object((1,3,6,1,4,1,25506,10,2,1,2,1,15),_Hh3cSnapExtendTimes_Type())
hh3cSnapExtendTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapExtendTimes.setStatus(_A)
_Hh3cSnapRowStatus_Type=RowStatus
_Hh3cSnapRowStatus_Object=MibTableColumn
hh3cSnapRowStatus=_Hh3cSnapRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,2,1,16),_Hh3cSnapRowStatus_Type())
hh3cSnapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapRowStatus.setStatus(_A)
_Hh3cSnapExpandTable_Object=MibTable
hh3cSnapExpandTable=_Hh3cSnapExpandTable_Object((1,3,6,1,4,1,25506,10,2,1,3))
if mibBuilder.loadTexts:hh3cSnapExpandTable.setStatus(_A)
_Hh3cSnapExpandEntry_Object=MibTableRow
hh3cSnapExpandEntry=_Hh3cSnapExpandEntry_Object((1,3,6,1,4,1,25506,10,2,1,3,1))
hh3cSnapExpandEntry.setIndexNames((0,_D,_H),(0,_D,_S))
if mibBuilder.loadTexts:hh3cSnapExpandEntry.setStatus(_A)
_Hh3cSAExpRaidUuid_Type=Hh3cRaidIDType
_Hh3cSAExpRaidUuid_Object=MibTableColumn
hh3cSAExpRaidUuid=_Hh3cSAExpRaidUuid_Object((1,3,6,1,4,1,25506,10,2,1,3,1,1),_Hh3cSAExpRaidUuid_Type())
hh3cSAExpRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSAExpRaidUuid.setStatus(_A)
_Hh3cSAExpSize_Type=Integer32
_Hh3cSAExpSize_Object=MibTableColumn
hh3cSAExpSize=_Hh3cSAExpSize_Object((1,3,6,1,4,1,25506,10,2,1,3,1,2),_Hh3cSAExpSize_Type())
hh3cSAExpSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSAExpSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSAExpSize.setUnits(_F)
_Hh3cSAExpRaidSize_Type=Integer32
_Hh3cSAExpRaidSize_Object=MibTableColumn
hh3cSAExpRaidSize=_Hh3cSAExpRaidSize_Object((1,3,6,1,4,1,25506,10,2,1,3,1,3),_Hh3cSAExpRaidSize_Type())
hh3cSAExpRaidSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSAExpRaidSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSAExpRaidSize.setUnits(_F)
_Hh3cSnapAreaExpRowStatus_Type=RowStatus
_Hh3cSnapAreaExpRowStatus_Object=MibTableColumn
hh3cSnapAreaExpRowStatus=_Hh3cSnapAreaExpRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,3,1,4),_Hh3cSnapAreaExpRowStatus_Type())
hh3cSnapAreaExpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSnapAreaExpRowStatus.setStatus(_A)
_Hh3cSnapCopyTable_Object=MibTable
hh3cSnapCopyTable=_Hh3cSnapCopyTable_Object((1,3,6,1,4,1,25506,10,2,1,4))
if mibBuilder.loadTexts:hh3cSnapCopyTable.setStatus(_A)
_Hh3cSnapCopyEntry_Object=MibTableRow
hh3cSnapCopyEntry=_Hh3cSnapCopyEntry_Object((1,3,6,1,4,1,25506,10,2,1,4,1))
hh3cSnapCopyEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hh3cSnapCopyEntry.setStatus(_A)
_Hh3cSnapCopyLvIndex_Type=Hh3cLvIDType
_Hh3cSnapCopyLvIndex_Object=MibTableColumn
hh3cSnapCopyLvIndex=_Hh3cSnapCopyLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,4,1,1),_Hh3cSnapCopyLvIndex_Type())
hh3cSnapCopyLvIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cSnapCopyLvIndex.setStatus(_A)
class _Hh3cSnapCopyPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hh3cSnapCopyPercentage_Type.__name__=_E
_Hh3cSnapCopyPercentage_Object=MibTableColumn
hh3cSnapCopyPercentage=_Hh3cSnapCopyPercentage_Object((1,3,6,1,4,1,25506,10,2,1,4,1,2),_Hh3cSnapCopyPercentage_Type())
hh3cSnapCopyPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapCopyPercentage.setStatus(_A)
_Hh3cSnapCopyStartTime_Type=DateAndTime
_Hh3cSnapCopyStartTime_Object=MibTableColumn
hh3cSnapCopyStartTime=_Hh3cSnapCopyStartTime_Object((1,3,6,1,4,1,25506,10,2,1,4,1,3),_Hh3cSnapCopyStartTime_Type())
hh3cSnapCopyStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSnapCopyStartTime.setStatus(_A)
class _Hh3cSnapCopySwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),(_N,2),(_I,3)))
_Hh3cSnapCopySwitch_Type.__name__=_E
_Hh3cSnapCopySwitch_Object=MibTableColumn
hh3cSnapCopySwitch=_Hh3cSnapCopySwitch_Object((1,3,6,1,4,1,25506,10,2,1,4,1,4),_Hh3cSnapCopySwitch_Type())
hh3cSnapCopySwitch.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cSnapCopySwitch.setStatus(_A)
_Hh3cTimeMarkConfigTable_Object=MibTable
hh3cTimeMarkConfigTable=_Hh3cTimeMarkConfigTable_Object((1,3,6,1,4,1,25506,10,2,1,5))
if mibBuilder.loadTexts:hh3cTimeMarkConfigTable.setStatus(_A)
_Hh3cTimeMarkConfigEntry_Object=MibTableRow
hh3cTimeMarkConfigEntry=_Hh3cTimeMarkConfigEntry_Object((1,3,6,1,4,1,25506,10,2,1,5,1))
hh3cTimeMarkConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hh3cTimeMarkConfigEntry.setStatus(_A)
class _Hh3cTimeMarkCounts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hh3cTimeMarkCounts_Type.__name__=_E
_Hh3cTimeMarkCounts_Object=MibTableColumn
hh3cTimeMarkCounts=_Hh3cTimeMarkCounts_Object((1,3,6,1,4,1,25506,10,2,1,5,1,1),_Hh3cTimeMarkCounts_Type())
hh3cTimeMarkCounts.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cTimeMarkCounts.setStatus(_A)
_Hh3cTimeMarkInitializeTime_Type=DateAndTime
_Hh3cTimeMarkInitializeTime_Object=MibTableColumn
hh3cTimeMarkInitializeTime=_Hh3cTimeMarkInitializeTime_Object((1,3,6,1,4,1,25506,10,2,1,5,1,2),_Hh3cTimeMarkInitializeTime_Type())
hh3cTimeMarkInitializeTime.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cTimeMarkInitializeTime.setStatus(_A)
_Hh3cTimeMarkInterval_Type=Integer32
_Hh3cTimeMarkInterval_Object=MibTableColumn
hh3cTimeMarkInterval=_Hh3cTimeMarkInterval_Object((1,3,6,1,4,1,25506,10,2,1,5,1,3),_Hh3cTimeMarkInterval_Type())
hh3cTimeMarkInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cTimeMarkInterval.setStatus(_A)
_Hh3cTimeMarkLastTime_Type=DateAndTime
_Hh3cTimeMarkLastTime_Object=MibTableColumn
hh3cTimeMarkLastTime=_Hh3cTimeMarkLastTime_Object((1,3,6,1,4,1,25506,10,2,1,5,1,4),_Hh3cTimeMarkLastTime_Type())
hh3cTimeMarkLastTime.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cTimeMarkLastTime.setStatus(_A)
_Hh3cTimeMarkTotal_Type=Integer32
_Hh3cTimeMarkTotal_Object=MibTableColumn
hh3cTimeMarkTotal=_Hh3cTimeMarkTotal_Object((1,3,6,1,4,1,25506,10,2,1,5,1,5),_Hh3cTimeMarkTotal_Type())
hh3cTimeMarkTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTimeMarkTotal.setStatus(_A)
_Hh3cTimeMarkSwitch_Type=Hh3cStorageEnableState
_Hh3cTimeMarkSwitch_Object=MibTableColumn
hh3cTimeMarkSwitch=_Hh3cTimeMarkSwitch_Object((1,3,6,1,4,1,25506,10,2,1,5,1,6),_Hh3cTimeMarkSwitch_Type())
hh3cTimeMarkSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTimeMarkSwitch.setStatus(_A)
_Hh3cTimeMarkCreateTable_Object=MibTable
hh3cTimeMarkCreateTable=_Hh3cTimeMarkCreateTable_Object((1,3,6,1,4,1,25506,10,2,1,6))
if mibBuilder.loadTexts:hh3cTimeMarkCreateTable.setStatus(_A)
_Hh3cTimeMarkCreateEntry_Object=MibTableRow
hh3cTimeMarkCreateEntry=_Hh3cTimeMarkCreateEntry_Object((1,3,6,1,4,1,25506,10,2,1,6,1))
hh3cTimeMarkCreateEntry.setIndexNames((0,_D,_H),(0,_D,_O))
if mibBuilder.loadTexts:hh3cTimeMarkCreateEntry.setStatus(_A)
_Hh3cTimeMarkStamp_Type=DateAndTime
_Hh3cTimeMarkStamp_Object=MibTableColumn
hh3cTimeMarkStamp=_Hh3cTimeMarkStamp_Object((1,3,6,1,4,1,25506,10,2,1,6,1,1),_Hh3cTimeMarkStamp_Type())
hh3cTimeMarkStamp.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cTimeMarkStamp.setStatus(_A)
_Hh3cTimeMarkComment_Type=OctetString
_Hh3cTimeMarkComment_Object=MibTableColumn
hh3cTimeMarkComment=_Hh3cTimeMarkComment_Object((1,3,6,1,4,1,25506,10,2,1,6,1,2),_Hh3cTimeMarkComment_Type())
hh3cTimeMarkComment.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTimeMarkComment.setStatus(_A)
_Hh3cTimeMarkSize_Type=Integer32
_Hh3cTimeMarkSize_Object=MibTableColumn
hh3cTimeMarkSize=_Hh3cTimeMarkSize_Object((1,3,6,1,4,1,25506,10,2,1,6,1,3),_Hh3cTimeMarkSize_Type())
hh3cTimeMarkSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTimeMarkSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cTimeMarkSize.setUnits('KB')
_Hh3cTimeMarkRowStatus_Type=RowStatus
_Hh3cTimeMarkRowStatus_Object=MibTableColumn
hh3cTimeMarkRowStatus=_Hh3cTimeMarkRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,6,1,4),_Hh3cTimeMarkRowStatus_Type())
hh3cTimeMarkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTimeMarkRowStatus.setStatus(_A)
_Hh3cTimeMarkCopyTable_Object=MibTable
hh3cTimeMarkCopyTable=_Hh3cTimeMarkCopyTable_Object((1,3,6,1,4,1,25506,10,2,1,7))
if mibBuilder.loadTexts:hh3cTimeMarkCopyTable.setStatus(_A)
_Hh3cTimeMarkCopyEntry_Object=MibTableRow
hh3cTimeMarkCopyEntry=_Hh3cTimeMarkCopyEntry_Object((1,3,6,1,4,1,25506,10,2,1,7,1))
hh3cTimeMarkCopyEntry.setIndexNames((0,_D,_H),(0,_D,_O))
if mibBuilder.loadTexts:hh3cTimeMarkCopyEntry.setStatus(_A)
_Hh3cTMCopyDestLvId_Type=Hh3cLvIDType
_Hh3cTMCopyDestLvId_Object=MibTableColumn
hh3cTMCopyDestLvId=_Hh3cTMCopyDestLvId_Object((1,3,6,1,4,1,25506,10,2,1,7,1,1),_Hh3cTMCopyDestLvId_Type())
hh3cTMCopyDestLvId.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTMCopyDestLvId.setStatus(_A)
class _Hh3cTMCopyPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hh3cTMCopyPercentage_Type.__name__=_E
_Hh3cTMCopyPercentage_Object=MibTableColumn
hh3cTMCopyPercentage=_Hh3cTMCopyPercentage_Object((1,3,6,1,4,1,25506,10,2,1,7,1,2),_Hh3cTMCopyPercentage_Type())
hh3cTMCopyPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTMCopyPercentage.setStatus(_A)
_Hh3cTMCopyStartTime_Type=DateAndTime
_Hh3cTMCopyStartTime_Object=MibTableColumn
hh3cTMCopyStartTime=_Hh3cTMCopyStartTime_Object((1,3,6,1,4,1,25506,10,2,1,7,1,3),_Hh3cTMCopyStartTime_Type())
hh3cTMCopyStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTMCopyStartTime.setStatus(_A)
class _Hh3cTMCopySwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),(_N,2),(_I,3)))
_Hh3cTMCopySwitch_Type.__name__=_E
_Hh3cTMCopySwitch_Object=MibTableColumn
hh3cTMCopySwitch=_Hh3cTMCopySwitch_Object((1,3,6,1,4,1,25506,10,2,1,7,1,4),_Hh3cTMCopySwitch_Type())
hh3cTMCopySwitch.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cTMCopySwitch.setStatus(_A)
_Hh3cTimeMarkRollbackTable_Object=MibTable
hh3cTimeMarkRollbackTable=_Hh3cTimeMarkRollbackTable_Object((1,3,6,1,4,1,25506,10,2,1,8))
if mibBuilder.loadTexts:hh3cTimeMarkRollbackTable.setStatus(_A)
_Hh3cTimeMarkRollbackEntry_Object=MibTableRow
hh3cTimeMarkRollbackEntry=_Hh3cTimeMarkRollbackEntry_Object((1,3,6,1,4,1,25506,10,2,1,8,1))
hh3cTimeMarkRollbackEntry.setIndexNames((0,_D,_H),(0,_D,_O))
if mibBuilder.loadTexts:hh3cTimeMarkRollbackEntry.setStatus(_A)
class _Hh3cTMRollbackPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hh3cTMRollbackPercentage_Type.__name__=_E
_Hh3cTMRollbackPercentage_Object=MibTableColumn
hh3cTMRollbackPercentage=_Hh3cTMRollbackPercentage_Object((1,3,6,1,4,1,25506,10,2,1,8,1,1),_Hh3cTMRollbackPercentage_Type())
hh3cTMRollbackPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTMRollbackPercentage.setStatus(_A)
_Hh3cTMRollbackStartTime_Type=DateAndTime
_Hh3cTMRollbackStartTime_Object=MibTableColumn
hh3cTMRollbackStartTime=_Hh3cTMRollbackStartTime_Object((1,3,6,1,4,1,25506,10,2,1,8,1,2),_Hh3cTMRollbackStartTime_Type())
hh3cTMRollbackStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTMRollbackStartTime.setStatus(_A)
_Hh3cTMRollbackSwitch_Type=Hh3cStorageActionType
_Hh3cTMRollbackSwitch_Object=MibTableColumn
hh3cTMRollbackSwitch=_Hh3cTMRollbackSwitch_Object((1,3,6,1,4,1,25506,10,2,1,8,1,3),_Hh3cTMRollbackSwitch_Type())
hh3cTMRollbackSwitch.setMaxAccess(_J)
if mibBuilder.loadTexts:hh3cTMRollbackSwitch.setStatus(_A)
_Hh3cTimeViewTable_Object=MibTable
hh3cTimeViewTable=_Hh3cTimeViewTable_Object((1,3,6,1,4,1,25506,10,2,1,9))
if mibBuilder.loadTexts:hh3cTimeViewTable.setStatus(_A)
_Hh3cTimeViewEntry_Object=MibTableRow
hh3cTimeViewEntry=_Hh3cTimeViewEntry_Object((1,3,6,1,4,1,25506,10,2,1,9,1))
hh3cTimeViewEntry.setIndexNames((0,_D,_H),(0,_D,_T))
if mibBuilder.loadTexts:hh3cTimeViewEntry.setStatus(_A)
_Hh3cTimeViewStamp_Type=DateAndTime
_Hh3cTimeViewStamp_Object=MibTableColumn
hh3cTimeViewStamp=_Hh3cTimeViewStamp_Object((1,3,6,1,4,1,25506,10,2,1,9,1,1),_Hh3cTimeViewStamp_Type())
hh3cTimeViewStamp.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cTimeViewStamp.setStatus(_A)
_Hh3cTimeViewID_Type=Hh3cLvIDType
_Hh3cTimeViewID_Object=MibTableColumn
hh3cTimeViewID=_Hh3cTimeViewID_Object((1,3,6,1,4,1,25506,10,2,1,9,1,2),_Hh3cTimeViewID_Type())
hh3cTimeViewID.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTimeViewID.setStatus(_A)
_Hh3cTimeViewName_Type=OctetString
_Hh3cTimeViewName_Object=MibTableColumn
hh3cTimeViewName=_Hh3cTimeViewName_Object((1,3,6,1,4,1,25506,10,2,1,9,1,3),_Hh3cTimeViewName_Type())
hh3cTimeViewName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTimeViewName.setStatus(_A)
_Hh3cTimeViewRowStatus_Type=RowStatus
_Hh3cTimeViewRowStatus_Object=MibTableColumn
hh3cTimeViewRowStatus=_Hh3cTimeViewRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,9,1,4),_Hh3cTimeViewRowStatus_Type())
hh3cTimeViewRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTimeViewRowStatus.setStatus(_A)
_Hh3cReplicaConfigTable_Object=MibTable
hh3cReplicaConfigTable=_Hh3cReplicaConfigTable_Object((1,3,6,1,4,1,25506,10,2,1,10))
if mibBuilder.loadTexts:hh3cReplicaConfigTable.setStatus(_A)
_Hh3cReplicaConfigEntry_Object=MibTableRow
hh3cReplicaConfigEntry=_Hh3cReplicaConfigEntry_Object((1,3,6,1,4,1,25506,10,2,1,10,1))
hh3cReplicaConfigEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:hh3cReplicaConfigEntry.setStatus(_A)
_Hh3cRepLocalLvIndex_Type=Hh3cLvIDType
_Hh3cRepLocalLvIndex_Object=MibTableColumn
hh3cRepLocalLvIndex=_Hh3cRepLocalLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,10,1,1),_Hh3cRepLocalLvIndex_Type())
hh3cRepLocalLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cRepLocalLvIndex.setStatus(_A)
class _Hh3cLvRepLocalWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outgoing',1),('incoming',2)))
_Hh3cLvRepLocalWay_Type.__name__=_E
_Hh3cLvRepLocalWay_Object=MibTableColumn
hh3cLvRepLocalWay=_Hh3cLvRepLocalWay_Object((1,3,6,1,4,1,25506,10,2,1,10,1,2),_Hh3cLvRepLocalWay_Type())
hh3cLvRepLocalWay.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvRepLocalWay.setStatus(_A)
_Hh3cRepLocalServerIP_Type=InetAddress
_Hh3cRepLocalServerIP_Object=MibTableColumn
hh3cRepLocalServerIP=_Hh3cRepLocalServerIP_Object((1,3,6,1,4,1,25506,10,2,1,10,1,3),_Hh3cRepLocalServerIP_Type())
hh3cRepLocalServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepLocalServerIP.setStatus(_A)
_Hh3cRepLocalServerIPType_Type=InetAddressType
_Hh3cRepLocalServerIPType_Object=MibTableColumn
hh3cRepLocalServerIPType=_Hh3cRepLocalServerIPType_Object((1,3,6,1,4,1,25506,10,2,1,10,1,4),_Hh3cRepLocalServerIPType_Type())
hh3cRepLocalServerIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepLocalServerIPType.setStatus(_A)
_Hh3cRepLocalServerName_Type=OctetString
_Hh3cRepLocalServerName_Object=MibTableColumn
hh3cRepLocalServerName=_Hh3cRepLocalServerName_Object((1,3,6,1,4,1,25506,10,2,1,10,1,5),_Hh3cRepLocalServerName_Type())
hh3cRepLocalServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cRepLocalServerName.setStatus(_A)
class _Hh3cRepLocalServerUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Hh3cRepLocalServerUsername_Type.__name__=_K
_Hh3cRepLocalServerUsername_Object=MibTableColumn
hh3cRepLocalServerUsername=_Hh3cRepLocalServerUsername_Object((1,3,6,1,4,1,25506,10,2,1,10,1,6),_Hh3cRepLocalServerUsername_Type())
hh3cRepLocalServerUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepLocalServerUsername.setStatus(_A)
class _Hh3cRepLocalServerPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_Hh3cRepLocalServerPassword_Type.__name__=_K
_Hh3cRepLocalServerPassword_Object=MibTableColumn
hh3cRepLocalServerPassword=_Hh3cRepLocalServerPassword_Object((1,3,6,1,4,1,25506,10,2,1,10,1,7),_Hh3cRepLocalServerPassword_Type())
hh3cRepLocalServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepLocalServerPassword.setStatus(_A)
_Hh3cRepRemoteServerIP_Type=InetAddress
_Hh3cRepRemoteServerIP_Object=MibTableColumn
hh3cRepRemoteServerIP=_Hh3cRepRemoteServerIP_Object((1,3,6,1,4,1,25506,10,2,1,10,1,8),_Hh3cRepRemoteServerIP_Type())
hh3cRepRemoteServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepRemoteServerIP.setStatus(_A)
_Hh3cRepRemoteServerIPType_Type=InetAddressType
_Hh3cRepRemoteServerIPType_Object=MibTableColumn
hh3cRepRemoteServerIPType=_Hh3cRepRemoteServerIPType_Object((1,3,6,1,4,1,25506,10,2,1,10,1,9),_Hh3cRepRemoteServerIPType_Type())
hh3cRepRemoteServerIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepRemoteServerIPType.setStatus(_A)
_Hh3cRepRemoteServerName_Type=OctetString
_Hh3cRepRemoteServerName_Object=MibTableColumn
hh3cRepRemoteServerName=_Hh3cRepRemoteServerName_Object((1,3,6,1,4,1,25506,10,2,1,10,1,10),_Hh3cRepRemoteServerName_Type())
hh3cRepRemoteServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cRepRemoteServerName.setStatus(_A)
class _Hh3cRepRemoteServerUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Hh3cRepRemoteServerUsername_Type.__name__=_K
_Hh3cRepRemoteServerUsername_Object=MibTableColumn
hh3cRepRemoteServerUsername=_Hh3cRepRemoteServerUsername_Object((1,3,6,1,4,1,25506,10,2,1,10,1,11),_Hh3cRepRemoteServerUsername_Type())
hh3cRepRemoteServerUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepRemoteServerUsername.setStatus(_A)
class _Hh3cRepRemoteServerPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_Hh3cRepRemoteServerPassword_Type.__name__=_K
_Hh3cRepRemoteServerPassword_Object=MibTableColumn
hh3cRepRemoteServerPassword=_Hh3cRepRemoteServerPassword_Object((1,3,6,1,4,1,25506,10,2,1,10,1,12),_Hh3cRepRemoteServerPassword_Type())
hh3cRepRemoteServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepRemoteServerPassword.setStatus(_A)
_Hh3cRepRemoteLvIndex_Type=Hh3cLvIDType
_Hh3cRepRemoteLvIndex_Object=MibTableColumn
hh3cRepRemoteLvIndex=_Hh3cRepRemoteLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,10,1,13),_Hh3cRepRemoteLvIndex_Type())
hh3cRepRemoteLvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cRepRemoteLvIndex.setStatus(_A)
class _Hh3cReplicaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('adaptive',1),('remote',2),(_I,3)))
_Hh3cReplicaMode_Type.__name__=_E
_Hh3cReplicaMode_Object=MibTableColumn
hh3cReplicaMode=_Hh3cReplicaMode_Object((1,3,6,1,4,1,25506,10,2,1,10,1,14),_Hh3cReplicaMode_Type())
hh3cReplicaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaMode.setStatus(_A)
_Hh3cReplicaWatermark_Type=Integer32
_Hh3cReplicaWatermark_Object=MibTableColumn
hh3cReplicaWatermark=_Hh3cReplicaWatermark_Object((1,3,6,1,4,1,25506,10,2,1,10,1,15),_Hh3cReplicaWatermark_Type())
hh3cReplicaWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaWatermark.setStatus(_A)
if mibBuilder.loadTexts:hh3cReplicaWatermark.setUnits(_F)
_Hh3cReplicaWatermarkRetry_Type=Integer32
_Hh3cReplicaWatermarkRetry_Object=MibTableColumn
hh3cReplicaWatermarkRetry=_Hh3cReplicaWatermarkRetry_Object((1,3,6,1,4,1,25506,10,2,1,10,1,16),_Hh3cReplicaWatermarkRetry_Type())
hh3cReplicaWatermarkRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaWatermarkRetry.setStatus(_A)
_Hh3cReplicaInitializeTime_Type=DateAndTime
_Hh3cReplicaInitializeTime_Object=MibTableColumn
hh3cReplicaInitializeTime=_Hh3cReplicaInitializeTime_Object((1,3,6,1,4,1,25506,10,2,1,10,1,17),_Hh3cReplicaInitializeTime_Type())
hh3cReplicaInitializeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaInitializeTime.setStatus(_A)
_Hh3cReplicaInterval_Type=Integer32
_Hh3cReplicaInterval_Object=MibTableColumn
hh3cReplicaInterval=_Hh3cReplicaInterval_Object((1,3,6,1,4,1,25506,10,2,1,10,1,18),_Hh3cReplicaInterval_Type())
hh3cReplicaInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaInterval.setStatus(_A)
class _Hh3cReplicaEncrypt_Type(Hh3cStorageEnableState):defaultValue=2
_Hh3cReplicaEncrypt_Type.__name__=_M
_Hh3cReplicaEncrypt_Object=MibTableColumn
hh3cReplicaEncrypt=_Hh3cReplicaEncrypt_Object((1,3,6,1,4,1,25506,10,2,1,10,1,19),_Hh3cReplicaEncrypt_Type())
hh3cReplicaEncrypt.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaEncrypt.setStatus(_A)
class _Hh3cReplicaCompress_Type(Hh3cStorageEnableState):defaultValue=2
_Hh3cReplicaCompress_Type.__name__=_M
_Hh3cReplicaCompress_Object=MibTableColumn
hh3cReplicaCompress=_Hh3cReplicaCompress_Object((1,3,6,1,4,1,25506,10,2,1,10,1,20),_Hh3cReplicaCompress_Type())
hh3cReplicaCompress.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaCompress.setStatus(_A)
class _Hh3cReplicaUseExistTM_Type(Hh3cStorageEnableState):defaultValue=2
_Hh3cReplicaUseExistTM_Type.__name__=_M
_Hh3cReplicaUseExistTM_Object=MibTableColumn
hh3cReplicaUseExistTM=_Hh3cReplicaUseExistTM_Object((1,3,6,1,4,1,25506,10,2,1,10,1,21),_Hh3cReplicaUseExistTM_Type())
hh3cReplicaUseExistTM.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaUseExistTM.setStatus(_A)
class _Hh3cReplicaProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('rudp',2)))
_Hh3cReplicaProtocol_Type.__name__=_E
_Hh3cReplicaProtocol_Object=MibTableColumn
hh3cReplicaProtocol=_Hh3cReplicaProtocol_Object((1,3,6,1,4,1,25506,10,2,1,10,1,22),_Hh3cReplicaProtocol_Type())
hh3cReplicaProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaProtocol.setStatus(_A)
_Hh3cReplicaScanDiff_Type=TruthValue
_Hh3cReplicaScanDiff_Object=MibTableColumn
hh3cReplicaScanDiff=_Hh3cReplicaScanDiff_Object((1,3,6,1,4,1,25506,10,2,1,10,1,23),_Hh3cReplicaScanDiff_Type())
hh3cReplicaScanDiff.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaScanDiff.setStatus(_A)
class _Hh3cReplicaStatSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('promte',1),(_P,2),('scan',3),('reversal',4),(_N,5),(_Q,6),(_U,7),(_I,8)))
_Hh3cReplicaStatSwitch_Type.__name__=_E
_Hh3cReplicaStatSwitch_Object=MibTableColumn
hh3cReplicaStatSwitch=_Hh3cReplicaStatSwitch_Object((1,3,6,1,4,1,25506,10,2,1,10,1,24),_Hh3cReplicaStatSwitch_Type())
hh3cReplicaStatSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaStatSwitch.setStatus(_A)
_Hh3cReplicaRowStatus_Type=RowStatus
_Hh3cReplicaRowStatus_Object=MibTableColumn
hh3cReplicaRowStatus=_Hh3cReplicaRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,10,1,25),_Hh3cReplicaRowStatus_Type())
hh3cReplicaRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cReplicaRowStatus.setStatus(_A)
_Hh3cReplicaStateTable_Object=MibTable
hh3cReplicaStateTable=_Hh3cReplicaStateTable_Object((1,3,6,1,4,1,25506,10,2,1,11))
if mibBuilder.loadTexts:hh3cReplicaStateTable.setStatus(_A)
_Hh3cReplicaStateEntry_Object=MibTableRow
hh3cReplicaStateEntry=_Hh3cReplicaStateEntry_Object((1,3,6,1,4,1,25506,10,2,1,11,1))
hh3cReplicaStateEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:hh3cReplicaStateEntry.setStatus(_A)
_Hh3cReplicaDelta_Type=Integer32
_Hh3cReplicaDelta_Object=MibTableColumn
hh3cReplicaDelta=_Hh3cReplicaDelta_Object((1,3,6,1,4,1,25506,10,2,1,11,1,1),_Hh3cReplicaDelta_Type())
hh3cReplicaDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cReplicaDelta.setStatus(_A)
if mibBuilder.loadTexts:hh3cReplicaDelta.setUnits(_F)
_Hh3cReplicaLastSyncTime_Type=DateAndTime
_Hh3cReplicaLastSyncTime_Object=MibTableColumn
hh3cReplicaLastSyncTime=_Hh3cReplicaLastSyncTime_Object((1,3,6,1,4,1,25506,10,2,1,11,1,2),_Hh3cReplicaLastSyncTime_Type())
hh3cReplicaLastSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cReplicaLastSyncTime.setStatus(_A)
_Hh3cReplicaNextSyncTime_Type=DateAndTime
_Hh3cReplicaNextSyncTime_Object=MibTableColumn
hh3cReplicaNextSyncTime=_Hh3cReplicaNextSyncTime_Object((1,3,6,1,4,1,25506,10,2,1,11,1,3),_Hh3cReplicaNextSyncTime_Type())
hh3cReplicaNextSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cReplicaNextSyncTime.setStatus(_A)
_Hh3cReplicaSyncTotalSize_Type=Integer32
_Hh3cReplicaSyncTotalSize_Object=MibTableColumn
hh3cReplicaSyncTotalSize=_Hh3cReplicaSyncTotalSize_Object((1,3,6,1,4,1,25506,10,2,1,11,1,4),_Hh3cReplicaSyncTotalSize_Type())
hh3cReplicaSyncTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cReplicaSyncTotalSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cReplicaSyncTotalSize.setUnits(_F)
_Hh3cReplicaSyncCurPercentage_Type=Integer32
_Hh3cReplicaSyncCurPercentage_Object=MibTableColumn
hh3cReplicaSyncCurPercentage=_Hh3cReplicaSyncCurPercentage_Object((1,3,6,1,4,1,25506,10,2,1,11,1,5),_Hh3cReplicaSyncCurPercentage_Type())
hh3cReplicaSyncCurPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cReplicaSyncCurPercentage.setStatus(_A)
_Hh3cReplicaSyncPerformance_Type=Integer32
_Hh3cReplicaSyncPerformance_Object=MibTableColumn
hh3cReplicaSyncPerformance=_Hh3cReplicaSyncPerformance_Object((1,3,6,1,4,1,25506,10,2,1,11,1,6),_Hh3cReplicaSyncPerformance_Type())
hh3cReplicaSyncPerformance.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cReplicaSyncPerformance.setStatus(_A)
class _Hh3cReplicaRunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),('idle',2),(_N,3),(_P,4),('scan',5)))
_Hh3cReplicaRunStatus_Type.__name__=_E
_Hh3cReplicaRunStatus_Object=MibTableColumn
hh3cReplicaRunStatus=_Hh3cReplicaRunStatus_Object((1,3,6,1,4,1,25506,10,2,1,11,1,7),_Hh3cReplicaRunStatus_Type())
hh3cReplicaRunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cReplicaRunStatus.setStatus(_A)
_Hh3cCDRConfigTable_Object=MibTable
hh3cCDRConfigTable=_Hh3cCDRConfigTable_Object((1,3,6,1,4,1,25506,10,2,1,12))
if mibBuilder.loadTexts:hh3cCDRConfigTable.setStatus(_A)
_Hh3cCDRConfigEntry_Object=MibTableRow
hh3cCDRConfigEntry=_Hh3cCDRConfigEntry_Object((1,3,6,1,4,1,25506,10,2,1,12,1))
hh3cCDRConfigEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:hh3cCDRConfigEntry.setStatus(_A)
_Hh3cCDRLvIndex_Type=Hh3cLvIDType
_Hh3cCDRLvIndex_Object=MibTableColumn
hh3cCDRLvIndex=_Hh3cCDRLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,12,1,1),_Hh3cCDRLvIndex_Type())
hh3cCDRLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cCDRLvIndex.setStatus(_A)
_Hh3cCDRID_Type=Integer32
_Hh3cCDRID_Object=MibTableColumn
hh3cCDRID=_Hh3cCDRID_Object((1,3,6,1,4,1,25506,10,2,1,12,1,2),_Hh3cCDRID_Type())
hh3cCDRID.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cCDRID.setStatus(_A)
_Hh3cCDRStatus_Type=Hh3cStorageOnlineState
_Hh3cCDRStatus_Object=MibTableColumn
hh3cCDRStatus=_Hh3cCDRStatus_Object((1,3,6,1,4,1,25506,10,2,1,12,1,3),_Hh3cCDRStatus_Type())
hh3cCDRStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cCDRStatus.setStatus(_A)
_Hh3cCDRTotalSize_Type=Integer32
_Hh3cCDRTotalSize_Object=MibTableColumn
hh3cCDRTotalSize=_Hh3cCDRTotalSize_Object((1,3,6,1,4,1,25506,10,2,1,12,1,4),_Hh3cCDRTotalSize_Type())
hh3cCDRTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cCDRTotalSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cCDRTotalSize.setUnits(_F)
_Hh3cCDRFreeSize_Type=Integer32
_Hh3cCDRFreeSize_Object=MibTableColumn
hh3cCDRFreeSize=_Hh3cCDRFreeSize_Object((1,3,6,1,4,1,25506,10,2,1,12,1,5),_Hh3cCDRFreeSize_Type())
hh3cCDRFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cCDRFreeSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cCDRFreeSize.setUnits(_F)
class _Hh3cCDRSelectPolicy_Type(Hh3cExtendSelectPolicy):defaultValue=4
_Hh3cCDRSelectPolicy_Type.__name__=_L
_Hh3cCDRSelectPolicy_Object=MibTableColumn
hh3cCDRSelectPolicy=_Hh3cCDRSelectPolicy_Object((1,3,6,1,4,1,25506,10,2,1,12,1,6),_Hh3cCDRSelectPolicy_Type())
hh3cCDRSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cCDRSelectPolicy.setStatus(_A)
_Hh3cCDRRowStatus_Type=RowStatus
_Hh3cCDRRowStatus_Object=MibTableColumn
hh3cCDRRowStatus=_Hh3cCDRRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,12,1,7),_Hh3cCDRRowStatus_Type())
hh3cCDRRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cCDRRowStatus.setStatus(_A)
_Hh3cCDRDistributeTable_Object=MibTable
hh3cCDRDistributeTable=_Hh3cCDRDistributeTable_Object((1,3,6,1,4,1,25506,10,2,1,13))
if mibBuilder.loadTexts:hh3cCDRDistributeTable.setStatus(_A)
_Hh3cCDRDistributeEntry_Object=MibTableRow
hh3cCDRDistributeEntry=_Hh3cCDRDistributeEntry_Object((1,3,6,1,4,1,25506,10,2,1,13,1))
hh3cCDRDistributeEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:hh3cCDRDistributeEntry.setStatus(_A)
_Hh3cCDRDistLvIndex_Type=Hh3cLvIDType
_Hh3cCDRDistLvIndex_Object=MibTableColumn
hh3cCDRDistLvIndex=_Hh3cCDRDistLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,13,1,1),_Hh3cCDRDistLvIndex_Type())
hh3cCDRDistLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cCDRDistLvIndex.setStatus(_A)
_Hh3cCDRRaidUuid_Type=Hh3cRaidIDType
_Hh3cCDRRaidUuid_Object=MibTableColumn
hh3cCDRRaidUuid=_Hh3cCDRRaidUuid_Object((1,3,6,1,4,1,25506,10,2,1,13,1,2),_Hh3cCDRRaidUuid_Type())
hh3cCDRRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cCDRRaidUuid.setStatus(_A)
_Hh3cCDRRaidSize_Type=Integer32
_Hh3cCDRRaidSize_Object=MibTableColumn
hh3cCDRRaidSize=_Hh3cCDRRaidSize_Object((1,3,6,1,4,1,25506,10,2,1,13,1,3),_Hh3cCDRRaidSize_Type())
hh3cCDRRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cCDRRaidSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cCDRRaidSize.setUnits(_F)
_Hh3cCDRExtRowStatus_Type=RowStatus
_Hh3cCDRExtRowStatus_Object=MibTableColumn
hh3cCDRExtRowStatus=_Hh3cCDRExtRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,13,1,4),_Hh3cCDRExtRowStatus_Type())
hh3cCDRExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cCDRExtRowStatus.setStatus(_A)
_Hh3cSafeCacheConfigTable_Object=MibTable
hh3cSafeCacheConfigTable=_Hh3cSafeCacheConfigTable_Object((1,3,6,1,4,1,25506,10,2,1,14))
if mibBuilder.loadTexts:hh3cSafeCacheConfigTable.setStatus(_A)
_Hh3cSafeCacheConfigEntry_Object=MibTableRow
hh3cSafeCacheConfigEntry=_Hh3cSafeCacheConfigEntry_Object((1,3,6,1,4,1,25506,10,2,1,14,1))
hh3cSafeCacheConfigEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:hh3cSafeCacheConfigEntry.setStatus(_A)
_Hh3cSafeCacheLvIndex_Type=Hh3cLvIDType
_Hh3cSafeCacheLvIndex_Object=MibTableColumn
hh3cSafeCacheLvIndex=_Hh3cSafeCacheLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,14,1,1),_Hh3cSafeCacheLvIndex_Type())
hh3cSafeCacheLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSafeCacheLvIndex.setStatus(_A)
_Hh3cSafeCacheID_Type=Integer32
_Hh3cSafeCacheID_Object=MibTableColumn
hh3cSafeCacheID=_Hh3cSafeCacheID_Object((1,3,6,1,4,1,25506,10,2,1,14,1,2),_Hh3cSafeCacheID_Type())
hh3cSafeCacheID.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSafeCacheID.setStatus(_A)
_Hh3cSafeCacheStatus_Type=Hh3cStorageOnlineState
_Hh3cSafeCacheStatus_Object=MibTableColumn
hh3cSafeCacheStatus=_Hh3cSafeCacheStatus_Object((1,3,6,1,4,1,25506,10,2,1,14,1,3),_Hh3cSafeCacheStatus_Type())
hh3cSafeCacheStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSafeCacheStatus.setStatus(_A)
_Hh3cSafeCacheTotalSize_Type=Integer32
_Hh3cSafeCacheTotalSize_Object=MibTableColumn
hh3cSafeCacheTotalSize=_Hh3cSafeCacheTotalSize_Object((1,3,6,1,4,1,25506,10,2,1,14,1,4),_Hh3cSafeCacheTotalSize_Type())
hh3cSafeCacheTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSafeCacheTotalSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSafeCacheTotalSize.setUnits(_F)
_Hh3cSafeCacheFreeSize_Type=Integer32
_Hh3cSafeCacheFreeSize_Object=MibTableColumn
hh3cSafeCacheFreeSize=_Hh3cSafeCacheFreeSize_Object((1,3,6,1,4,1,25506,10,2,1,14,1,5),_Hh3cSafeCacheFreeSize_Type())
hh3cSafeCacheFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSafeCacheFreeSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cSafeCacheFreeSize.setUnits(_F)
class _Hh3cSafeCacheSelectPolicy_Type(Hh3cExtendSelectPolicy):defaultValue=4
_Hh3cSafeCacheSelectPolicy_Type.__name__=_L
_Hh3cSafeCacheSelectPolicy_Object=MibTableColumn
hh3cSafeCacheSelectPolicy=_Hh3cSafeCacheSelectPolicy_Object((1,3,6,1,4,1,25506,10,2,1,14,1,6),_Hh3cSafeCacheSelectPolicy_Type())
hh3cSafeCacheSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheSelectPolicy.setStatus(_A)
class _Hh3cSafeCacheThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hh3cSafeCacheThreshold_Type.__name__=_E
_Hh3cSafeCacheThreshold_Object=MibTableColumn
hh3cSafeCacheThreshold=_Hh3cSafeCacheThreshold_Object((1,3,6,1,4,1,25506,10,2,1,14,1,7),_Hh3cSafeCacheThreshold_Type())
hh3cSafeCacheThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheThreshold.setStatus(_A)
_Hh3cSafeCacheFlushTime_Type=Integer32
_Hh3cSafeCacheFlushTime_Object=MibTableColumn
hh3cSafeCacheFlushTime=_Hh3cSafeCacheFlushTime_Object((1,3,6,1,4,1,25506,10,2,1,14,1,8),_Hh3cSafeCacheFlushTime_Type())
hh3cSafeCacheFlushTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheFlushTime.setStatus(_A)
class _Hh3cSafeCacheFlushCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Hh3cSafeCacheFlushCommand_Type.__name__=_E
_Hh3cSafeCacheFlushCommand_Object=MibTableColumn
hh3cSafeCacheFlushCommand=_Hh3cSafeCacheFlushCommand_Object((1,3,6,1,4,1,25506,10,2,1,14,1,9),_Hh3cSafeCacheFlushCommand_Type())
hh3cSafeCacheFlushCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheFlushCommand.setStatus(_A)
class _Hh3cSafeCacheSkipDupWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_Hh3cSafeCacheSkipDupWrite_Type.__name__=_E
_Hh3cSafeCacheSkipDupWrite_Object=MibTableColumn
hh3cSafeCacheSkipDupWrite=_Hh3cSafeCacheSkipDupWrite_Object((1,3,6,1,4,1,25506,10,2,1,14,1,10),_Hh3cSafeCacheSkipDupWrite_Type())
hh3cSafeCacheSkipDupWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheSkipDupWrite.setStatus(_A)
class _Hh3cSafeCacheRunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('run',1),(_Q,2)))
_Hh3cSafeCacheRunStatus_Type.__name__=_E
_Hh3cSafeCacheRunStatus_Object=MibTableColumn
hh3cSafeCacheRunStatus=_Hh3cSafeCacheRunStatus_Object((1,3,6,1,4,1,25506,10,2,1,14,1,11),_Hh3cSafeCacheRunStatus_Type())
hh3cSafeCacheRunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSafeCacheRunStatus.setStatus(_A)
class _Hh3cSafeCacheSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_U,2),(_I,3)))
_Hh3cSafeCacheSwitch_Type.__name__=_E
_Hh3cSafeCacheSwitch_Object=MibTableColumn
hh3cSafeCacheSwitch=_Hh3cSafeCacheSwitch_Object((1,3,6,1,4,1,25506,10,2,1,14,1,12),_Hh3cSafeCacheSwitch_Type())
hh3cSafeCacheSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheSwitch.setStatus(_A)
_Hh3cSafeCacheRowStatus_Type=RowStatus
_Hh3cSafeCacheRowStatus_Object=MibTableColumn
hh3cSafeCacheRowStatus=_Hh3cSafeCacheRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,14,1,13),_Hh3cSafeCacheRowStatus_Type())
hh3cSafeCacheRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheRowStatus.setStatus(_A)
_Hh3cSafeCacheDistributeTable_Object=MibTable
hh3cSafeCacheDistributeTable=_Hh3cSafeCacheDistributeTable_Object((1,3,6,1,4,1,25506,10,2,1,15))
if mibBuilder.loadTexts:hh3cSafeCacheDistributeTable.setStatus(_A)
_Hh3cSafeCacheDistributeEntry_Object=MibTableRow
hh3cSafeCacheDistributeEntry=_Hh3cSafeCacheDistributeEntry_Object((1,3,6,1,4,1,25506,10,2,1,15,1))
hh3cSafeCacheDistributeEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:hh3cSafeCacheDistributeEntry.setStatus(_A)
_Hh3cSafeCacheDistLvIndex_Type=Hh3cLvIDType
_Hh3cSafeCacheDistLvIndex_Object=MibTableColumn
hh3cSafeCacheDistLvIndex=_Hh3cSafeCacheDistLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,15,1,1),_Hh3cSafeCacheDistLvIndex_Type())
hh3cSafeCacheDistLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSafeCacheDistLvIndex.setStatus(_A)
_Hh3cSafeCacheRaidUuid_Type=Hh3cRaidIDType
_Hh3cSafeCacheRaidUuid_Object=MibTableColumn
hh3cSafeCacheRaidUuid=_Hh3cSafeCacheRaidUuid_Object((1,3,6,1,4,1,25506,10,2,1,15,1,2),_Hh3cSafeCacheRaidUuid_Type())
hh3cSafeCacheRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSafeCacheRaidUuid.setStatus(_A)
_Hh3cSafeCacheRaidSize_Type=Integer32
_Hh3cSafeCacheRaidSize_Object=MibTableColumn
hh3cSafeCacheRaidSize=_Hh3cSafeCacheRaidSize_Object((1,3,6,1,4,1,25506,10,2,1,15,1,3),_Hh3cSafeCacheRaidSize_Type())
hh3cSafeCacheRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheRaidSize.setStatus(_A)
_Hh3cSafeCacheExtRowStatus_Type=RowStatus
_Hh3cSafeCacheExtRowStatus_Object=MibTableColumn
hh3cSafeCacheExtRowStatus=_Hh3cSafeCacheExtRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,15,1,4),_Hh3cSafeCacheExtRowStatus_Type())
hh3cSafeCacheExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSafeCacheExtRowStatus.setStatus(_A)
_Hh3cMirrorConfigTable_Object=MibTable
hh3cMirrorConfigTable=_Hh3cMirrorConfigTable_Object((1,3,6,1,4,1,25506,10,2,1,16))
if mibBuilder.loadTexts:hh3cMirrorConfigTable.setStatus(_A)
_Hh3cMirrorConfigEntry_Object=MibTableRow
hh3cMirrorConfigEntry=_Hh3cMirrorConfigEntry_Object((1,3,6,1,4,1,25506,10,2,1,16,1))
hh3cMirrorConfigEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:hh3cMirrorConfigEntry.setStatus(_A)
_Hh3cMirrorLvIndex_Type=Hh3cLvIDType
_Hh3cMirrorLvIndex_Object=MibTableColumn
hh3cMirrorLvIndex=_Hh3cMirrorLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,16,1,1),_Hh3cMirrorLvIndex_Type())
hh3cMirrorLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cMirrorLvIndex.setStatus(_A)
class _Hh3cMirrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('async',2),(_I,3)))
_Hh3cMirrorType_Type.__name__=_E
_Hh3cMirrorType_Object=MibTableColumn
hh3cMirrorType=_Hh3cMirrorType_Object((1,3,6,1,4,1,25506,10,2,1,16,1,2),_Hh3cMirrorType_Type())
hh3cMirrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cMirrorType.setStatus(_A)
_Hh3cMirrorStatus_Type=Hh3cStorageOnlineState
_Hh3cMirrorStatus_Object=MibTableColumn
hh3cMirrorStatus=_Hh3cMirrorStatus_Object((1,3,6,1,4,1,25506,10,2,1,16,1,3),_Hh3cMirrorStatus_Type())
hh3cMirrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cMirrorStatus.setStatus(_A)
_Hh3cMirrorName_Type=OctetString
_Hh3cMirrorName_Object=MibTableColumn
hh3cMirrorName=_Hh3cMirrorName_Object((1,3,6,1,4,1,25506,10,2,1,16,1,4),_Hh3cMirrorName_Type())
hh3cMirrorName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorName.setStatus(_A)
class _Hh3cMirrorSyncPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hh3cMirrorSyncPercentage_Type.__name__=_E
_Hh3cMirrorSyncPercentage_Object=MibTableColumn
hh3cMirrorSyncPercentage=_Hh3cMirrorSyncPercentage_Object((1,3,6,1,4,1,25506,10,2,1,16,1,5),_Hh3cMirrorSyncPercentage_Type())
hh3cMirrorSyncPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cMirrorSyncPercentage.setStatus(_A)
class _Hh3cMirrorSyncPerformance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hh3cMirrorSyncPerformance_Type.__name__=_E
_Hh3cMirrorSyncPerformance_Object=MibTableColumn
hh3cMirrorSyncPerformance=_Hh3cMirrorSyncPerformance_Object((1,3,6,1,4,1,25506,10,2,1,16,1,6),_Hh3cMirrorSyncPerformance_Type())
hh3cMirrorSyncPerformance.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cMirrorSyncPerformance.setStatus(_A)
_Hh3cMirrorDelta_Type=Integer32
_Hh3cMirrorDelta_Object=MibTableColumn
hh3cMirrorDelta=_Hh3cMirrorDelta_Object((1,3,6,1,4,1,25506,10,2,1,16,1,7),_Hh3cMirrorDelta_Type())
hh3cMirrorDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cMirrorDelta.setStatus(_A)
if mibBuilder.loadTexts:hh3cMirrorDelta.setUnits(_F)
class _Hh3cMirrorRaidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('virtual',1),('serviceEnable',2),(_I,3)))
_Hh3cMirrorRaidType_Type.__name__=_E
_Hh3cMirrorRaidType_Object=MibTableColumn
hh3cMirrorRaidType=_Hh3cMirrorRaidType_Object((1,3,6,1,4,1,25506,10,2,1,16,1,8),_Hh3cMirrorRaidType_Type())
hh3cMirrorRaidType.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorRaidType.setStatus(_A)
class _Hh3cMirrorSelectPolicy_Type(Hh3cExtendSelectPolicy):defaultValue=4
_Hh3cMirrorSelectPolicy_Type.__name__=_L
_Hh3cMirrorSelectPolicy_Object=MibTableColumn
hh3cMirrorSelectPolicy=_Hh3cMirrorSelectPolicy_Object((1,3,6,1,4,1,25506,10,2,1,16,1,9),_Hh3cMirrorSelectPolicy_Type())
hh3cMirrorSelectPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorSelectPolicy.setStatus(_A)
class _Hh3cMirrorSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('swap',2),('promote',3),(_I,4)))
_Hh3cMirrorSwitch_Type.__name__=_E
_Hh3cMirrorSwitch_Object=MibTableColumn
hh3cMirrorSwitch=_Hh3cMirrorSwitch_Object((1,3,6,1,4,1,25506,10,2,1,16,1,10),_Hh3cMirrorSwitch_Type())
hh3cMirrorSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorSwitch.setStatus(_A)
_Hh3cMirrorExtendRaidUuid_Type=Hh3cRaidIDType
_Hh3cMirrorExtendRaidUuid_Object=MibTableColumn
hh3cMirrorExtendRaidUuid=_Hh3cMirrorExtendRaidUuid_Object((1,3,6,1,4,1,25506,10,2,1,16,1,11),_Hh3cMirrorExtendRaidUuid_Type())
hh3cMirrorExtendRaidUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorExtendRaidUuid.setStatus(_A)
_Hh3cMirrorRowStatus_Type=RowStatus
_Hh3cMirrorRowStatus_Object=MibTableColumn
hh3cMirrorRowStatus=_Hh3cMirrorRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,16,1,12),_Hh3cMirrorRowStatus_Type())
hh3cMirrorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorRowStatus.setStatus(_A)
_Hh3cMirrorDistributeTable_Object=MibTable
hh3cMirrorDistributeTable=_Hh3cMirrorDistributeTable_Object((1,3,6,1,4,1,25506,10,2,1,17))
if mibBuilder.loadTexts:hh3cMirrorDistributeTable.setStatus(_A)
_Hh3cMirrorDistributeEntry_Object=MibTableRow
hh3cMirrorDistributeEntry=_Hh3cMirrorDistributeEntry_Object((1,3,6,1,4,1,25506,10,2,1,17,1))
hh3cMirrorDistributeEntry.setIndexNames((0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:hh3cMirrorDistributeEntry.setStatus(_A)
_Hh3cMirrorDistLvIndex_Type=Hh3cLvIDType
_Hh3cMirrorDistLvIndex_Object=MibTableColumn
hh3cMirrorDistLvIndex=_Hh3cMirrorDistLvIndex_Object((1,3,6,1,4,1,25506,10,2,1,17,1,1),_Hh3cMirrorDistLvIndex_Type())
hh3cMirrorDistLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cMirrorDistLvIndex.setStatus(_A)
_Hh3cMirrorRaidUuid_Type=Hh3cRaidIDType
_Hh3cMirrorRaidUuid_Object=MibTableColumn
hh3cMirrorRaidUuid=_Hh3cMirrorRaidUuid_Object((1,3,6,1,4,1,25506,10,2,1,17,1,2),_Hh3cMirrorRaidUuid_Type())
hh3cMirrorRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cMirrorRaidUuid.setStatus(_A)
_Hh3cMirrorRaidSize_Type=Integer32
_Hh3cMirrorRaidSize_Object=MibTableColumn
hh3cMirrorRaidSize=_Hh3cMirrorRaidSize_Object((1,3,6,1,4,1,25506,10,2,1,17,1,3),_Hh3cMirrorRaidSize_Type())
hh3cMirrorRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorRaidSize.setStatus(_A)
_Hh3cMirrorExtRowStatus_Type=RowStatus
_Hh3cMirrorExtRowStatus_Object=MibTableColumn
hh3cMirrorExtRowStatus=_Hh3cMirrorExtRowStatus_Object((1,3,6,1,4,1,25506,10,2,1,17,1,4),_Hh3cMirrorExtRowStatus_Type())
hh3cMirrorExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cMirrorExtRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hh3cStorageSnap':hh3cStorageSnap,'hh3cSnapMibObjects':hh3cSnapMibObjects,'hh3cGlobalSnapSettingsObject':hh3cGlobalSnapSettingsObject,'hh3cAddtionalSpaceMaxSize':hh3cAddtionalSpaceMaxSize,'hh3cSnapConfigTable':hh3cSnapConfigTable,'hh3cSnapConfigEntry':hh3cSnapConfigEntry,_H:hh3cSnapLvIndex,'hh3cSnapAreaId':hh3cSnapAreaId,'hh3cSnapAreaAutoExpand':hh3cSnapAreaAutoExpand,'hh3cSnapAreaThreshold':hh3cSnapAreaThreshold,'hh3cSnapAreaIncSize':hh3cSnapAreaIncSize,'hh3cSnapAreaMaxSize':hh3cSnapAreaMaxSize,'hh3cSnapAreaFullDeleteTM':hh3cSnapAreaFullDeleteTM,'hh3cSnapAreaNotify':hh3cSnapAreaNotify,'hh3cSnapAreaStatus':hh3cSnapAreaStatus,'hh3cSnapRaidUuid':hh3cSnapRaidUuid,'hh3cSnapRaidSize':hh3cSnapRaidSize,'hh3cSnapRaidSelectPolicy':hh3cSnapRaidSelectPolicy,'hh3cSnapAreaTotalSize':hh3cSnapAreaTotalSize,'hh3cSnapAreaFreeSize':hh3cSnapAreaFreeSize,'hh3cSnapExtendTimes':hh3cSnapExtendTimes,'hh3cSnapRowStatus':hh3cSnapRowStatus,'hh3cSnapExpandTable':hh3cSnapExpandTable,'hh3cSnapExpandEntry':hh3cSnapExpandEntry,_S:hh3cSAExpRaidUuid,'hh3cSAExpSize':hh3cSAExpSize,'hh3cSAExpRaidSize':hh3cSAExpRaidSize,'hh3cSnapAreaExpRowStatus':hh3cSnapAreaExpRowStatus,'hh3cSnapCopyTable':hh3cSnapCopyTable,'hh3cSnapCopyEntry':hh3cSnapCopyEntry,'hh3cSnapCopyLvIndex':hh3cSnapCopyLvIndex,'hh3cSnapCopyPercentage':hh3cSnapCopyPercentage,'hh3cSnapCopyStartTime':hh3cSnapCopyStartTime,'hh3cSnapCopySwitch':hh3cSnapCopySwitch,'hh3cTimeMarkConfigTable':hh3cTimeMarkConfigTable,'hh3cTimeMarkConfigEntry':hh3cTimeMarkConfigEntry,'hh3cTimeMarkCounts':hh3cTimeMarkCounts,'hh3cTimeMarkInitializeTime':hh3cTimeMarkInitializeTime,'hh3cTimeMarkInterval':hh3cTimeMarkInterval,'hh3cTimeMarkLastTime':hh3cTimeMarkLastTime,'hh3cTimeMarkTotal':hh3cTimeMarkTotal,'hh3cTimeMarkSwitch':hh3cTimeMarkSwitch,'hh3cTimeMarkCreateTable':hh3cTimeMarkCreateTable,'hh3cTimeMarkCreateEntry':hh3cTimeMarkCreateEntry,_O:hh3cTimeMarkStamp,'hh3cTimeMarkComment':hh3cTimeMarkComment,'hh3cTimeMarkSize':hh3cTimeMarkSize,'hh3cTimeMarkRowStatus':hh3cTimeMarkRowStatus,'hh3cTimeMarkCopyTable':hh3cTimeMarkCopyTable,'hh3cTimeMarkCopyEntry':hh3cTimeMarkCopyEntry,'hh3cTMCopyDestLvId':hh3cTMCopyDestLvId,'hh3cTMCopyPercentage':hh3cTMCopyPercentage,'hh3cTMCopyStartTime':hh3cTMCopyStartTime,'hh3cTMCopySwitch':hh3cTMCopySwitch,'hh3cTimeMarkRollbackTable':hh3cTimeMarkRollbackTable,'hh3cTimeMarkRollbackEntry':hh3cTimeMarkRollbackEntry,'hh3cTMRollbackPercentage':hh3cTMRollbackPercentage,'hh3cTMRollbackStartTime':hh3cTMRollbackStartTime,'hh3cTMRollbackSwitch':hh3cTMRollbackSwitch,'hh3cTimeViewTable':hh3cTimeViewTable,'hh3cTimeViewEntry':hh3cTimeViewEntry,_T:hh3cTimeViewStamp,'hh3cTimeViewID':hh3cTimeViewID,'hh3cTimeViewName':hh3cTimeViewName,'hh3cTimeViewRowStatus':hh3cTimeViewRowStatus,'hh3cReplicaConfigTable':hh3cReplicaConfigTable,'hh3cReplicaConfigEntry':hh3cReplicaConfigEntry,_R:hh3cRepLocalLvIndex,'hh3cLvRepLocalWay':hh3cLvRepLocalWay,'hh3cRepLocalServerIP':hh3cRepLocalServerIP,'hh3cRepLocalServerIPType':hh3cRepLocalServerIPType,'hh3cRepLocalServerName':hh3cRepLocalServerName,'hh3cRepLocalServerUsername':hh3cRepLocalServerUsername,'hh3cRepLocalServerPassword':hh3cRepLocalServerPassword,'hh3cRepRemoteServerIP':hh3cRepRemoteServerIP,'hh3cRepRemoteServerIPType':hh3cRepRemoteServerIPType,'hh3cRepRemoteServerName':hh3cRepRemoteServerName,'hh3cRepRemoteServerUsername':hh3cRepRemoteServerUsername,'hh3cRepRemoteServerPassword':hh3cRepRemoteServerPassword,'hh3cRepRemoteLvIndex':hh3cRepRemoteLvIndex,'hh3cReplicaMode':hh3cReplicaMode,'hh3cReplicaWatermark':hh3cReplicaWatermark,'hh3cReplicaWatermarkRetry':hh3cReplicaWatermarkRetry,'hh3cReplicaInitializeTime':hh3cReplicaInitializeTime,'hh3cReplicaInterval':hh3cReplicaInterval,'hh3cReplicaEncrypt':hh3cReplicaEncrypt,'hh3cReplicaCompress':hh3cReplicaCompress,'hh3cReplicaUseExistTM':hh3cReplicaUseExistTM,'hh3cReplicaProtocol':hh3cReplicaProtocol,'hh3cReplicaScanDiff':hh3cReplicaScanDiff,'hh3cReplicaStatSwitch':hh3cReplicaStatSwitch,'hh3cReplicaRowStatus':hh3cReplicaRowStatus,'hh3cReplicaStateTable':hh3cReplicaStateTable,'hh3cReplicaStateEntry':hh3cReplicaStateEntry,'hh3cReplicaDelta':hh3cReplicaDelta,'hh3cReplicaLastSyncTime':hh3cReplicaLastSyncTime,'hh3cReplicaNextSyncTime':hh3cReplicaNextSyncTime,'hh3cReplicaSyncTotalSize':hh3cReplicaSyncTotalSize,'hh3cReplicaSyncCurPercentage':hh3cReplicaSyncCurPercentage,'hh3cReplicaSyncPerformance':hh3cReplicaSyncPerformance,'hh3cReplicaRunStatus':hh3cReplicaRunStatus,'hh3cCDRConfigTable':hh3cCDRConfigTable,'hh3cCDRConfigEntry':hh3cCDRConfigEntry,_V:hh3cCDRLvIndex,'hh3cCDRID':hh3cCDRID,'hh3cCDRStatus':hh3cCDRStatus,'hh3cCDRTotalSize':hh3cCDRTotalSize,'hh3cCDRFreeSize':hh3cCDRFreeSize,'hh3cCDRSelectPolicy':hh3cCDRSelectPolicy,'hh3cCDRRowStatus':hh3cCDRRowStatus,'hh3cCDRDistributeTable':hh3cCDRDistributeTable,'hh3cCDRDistributeEntry':hh3cCDRDistributeEntry,_W:hh3cCDRDistLvIndex,_X:hh3cCDRRaidUuid,'hh3cCDRRaidSize':hh3cCDRRaidSize,'hh3cCDRExtRowStatus':hh3cCDRExtRowStatus,'hh3cSafeCacheConfigTable':hh3cSafeCacheConfigTable,'hh3cSafeCacheConfigEntry':hh3cSafeCacheConfigEntry,_Y:hh3cSafeCacheLvIndex,'hh3cSafeCacheID':hh3cSafeCacheID,'hh3cSafeCacheStatus':hh3cSafeCacheStatus,'hh3cSafeCacheTotalSize':hh3cSafeCacheTotalSize,'hh3cSafeCacheFreeSize':hh3cSafeCacheFreeSize,'hh3cSafeCacheSelectPolicy':hh3cSafeCacheSelectPolicy,'hh3cSafeCacheThreshold':hh3cSafeCacheThreshold,'hh3cSafeCacheFlushTime':hh3cSafeCacheFlushTime,'hh3cSafeCacheFlushCommand':hh3cSafeCacheFlushCommand,'hh3cSafeCacheSkipDupWrite':hh3cSafeCacheSkipDupWrite,'hh3cSafeCacheRunStatus':hh3cSafeCacheRunStatus,'hh3cSafeCacheSwitch':hh3cSafeCacheSwitch,'hh3cSafeCacheRowStatus':hh3cSafeCacheRowStatus,'hh3cSafeCacheDistributeTable':hh3cSafeCacheDistributeTable,'hh3cSafeCacheDistributeEntry':hh3cSafeCacheDistributeEntry,_Z:hh3cSafeCacheDistLvIndex,_a:hh3cSafeCacheRaidUuid,'hh3cSafeCacheRaidSize':hh3cSafeCacheRaidSize,'hh3cSafeCacheExtRowStatus':hh3cSafeCacheExtRowStatus,'hh3cMirrorConfigTable':hh3cMirrorConfigTable,'hh3cMirrorConfigEntry':hh3cMirrorConfigEntry,_b:hh3cMirrorLvIndex,'hh3cMirrorType':hh3cMirrorType,'hh3cMirrorStatus':hh3cMirrorStatus,'hh3cMirrorName':hh3cMirrorName,'hh3cMirrorSyncPercentage':hh3cMirrorSyncPercentage,'hh3cMirrorSyncPerformance':hh3cMirrorSyncPerformance,'hh3cMirrorDelta':hh3cMirrorDelta,'hh3cMirrorRaidType':hh3cMirrorRaidType,'hh3cMirrorSelectPolicy':hh3cMirrorSelectPolicy,'hh3cMirrorSwitch':hh3cMirrorSwitch,'hh3cMirrorExtendRaidUuid':hh3cMirrorExtendRaidUuid,'hh3cMirrorRowStatus':hh3cMirrorRowStatus,'hh3cMirrorDistributeTable':hh3cMirrorDistributeTable,'hh3cMirrorDistributeEntry':hh3cMirrorDistributeEntry,_c:hh3cMirrorDistLvIndex,_d:hh3cMirrorRaidUuid,'hh3cMirrorRaidSize':hh3cMirrorRaidSize,'hh3cMirrorExtRowStatus':hh3cMirrorExtRowStatus})