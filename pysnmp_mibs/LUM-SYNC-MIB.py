_A_='syncSourceGroupV6'
_Az='syncSourceGroupV5'
_Ay='syncSourceGroupV4'
_Ax='syncSubrackGroupV2'
_Aw='syncSubrackGroup'
_Av='syncGroupGroupV7'
_Au='syncGroupGroupV2'
_At='syncGeneralGroup'
_As='syncGroupSourceChanged'
_Ar='syncSourceLocalId'
_Aq='syncSourceUpPortId'
_Ap='syncSourceIfNo'
_Ao='syncGroupQualityLevelSelectionMode'
_An='syncGroupHoldover'
_Am='syncGroupSourceSwitchType'
_Al='syncGroupSourceSwitch'
_Ak='syncBoardToDomainBoardName'
_Aj='syncBoardToDomainBoardIndex'
_Ai='syncBoardToDomainDomainName'
_Ah='syncBoardToDomainDomainIndex'
_Ag='syncBoardToDomainName'
_Af='syncBusStaticMasterIndex'
_Ae='syncBusStaticMasterSlot'
_Ad='syncBusDomainIndex'
_Ac='syncBusDomain'
_Ab='syncBusSubrack'
_Aa='syncBusName'
_AZ='syncDomainAssociateBoard'
_AY='syncDomainQuality'
_AX='syncDomainSource'
_AW='syncDomainHoldOff'
_AV='syncDomainWaitToRestore'
_AU='syncDomainQualityLevelSelectionMode'
_AT='syncDomainNumber'
_AS='syncDomainName'
_AR='syncSubrackGroupMasterBusB'
_AQ='syncSubrackGroupMasterBusA'
_AP='syncGeneralSyncSubrackTableSize'
_AO='syncGeneralSyncSourceTableSize'
_AN='syncGeneralSyncGroupTableSize'
_AM='SyncSourceMode'
_AL='MgmtNameString'
_AK='BoardOrInterfaceAdminStatus'
_AJ='AdminStatus'
_AI='syncGroupGroupV8'
_AH='syncGroupGroupV4'
_AG='syncGroupGroup'
_AF='syncSourceNonSyncEClock'
_AE='syncSourceClockWanderExceeded'
_AD='syncGroupStatus'
_AC='syncSubrackConfigureLocalBus'
_AB='syncSubrackMasterBusB'
_AA='syncSubrackMasterBusA'
_A9='syncSubrackName'
_A8='syncSubrackSubrack'
_A7='syncGeneralStateLastChangeTime'
_A6='syncBoardToDomainIndex'
_A5='syncBusIndex'
_A4='syncDomainIndex'
_A3='enabled'
_A2='disabled'
_A1='BoardOrInterfaceOperStatus'
_A0='syncBoardToDomainGroup'
_z='syncBusGroup'
_y='syncDomainGroup'
_x='syncGroupGroupV9'
_w='syncGroupGroupV6'
_v='syncSourceGroupV2'
_u='syncGroupGroupV3'
_t='syncSourceFilterState'
_s='syncSourceStaticQuality'
_r='syncGroupConfigurationMode'
_q='syncGeneralLastChangeTime'
_p='syncSubrackIndex'
_o='PortNumber'
_n='syncSourceGroup'
_m='syncGroupManualSourceName'
_l='syncGroupLocalOscActive'
_k='syncSourceAlwaysSendDoNotUse'
_j='syncGroupLocalOscActiveW2C'
_i='syncSourceId'
_h='syncGroupLastChangeTime'
_g='syncGroupRingMode'
_f='syncSourceIsSelected'
_e='syncSourceOperStatus'
_d='syncSourceAdminStatus'
_c='syncSourcePriority'
_b='syncSourceType'
_a='syncSourceTxPort'
_Z='syncSourceRxPort'
_Y='syncSourceGroupV3'
_X='syncGroupOperStatus'
_W='syncGroupAdminStatus'
_V='syncSourceQuality'
_U='syncSourceName'
_T='syncSourceIndex'
_S='syncGeneralGroupV3'
_R='syncGeneralGroupV2'
_Q='syncGroupQuality'
_P='syncGroupManualSource'
_O='syncGroupMode'
_N='syncGroupSlot'
_M='syncGroupSubrack'
_L='syncGroupSelectedSource'
_K='syncGroupName'
_J='syncGroupIndex'
_I='Integer32'
_H='syncNotificationGroup'
_G='read-create'
_F='read-write'
_E='Unsigned32'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-SYNC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumSyncMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumSyncMIB')
AdminStatus,BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,CommandString,FaultStatus,MgmtNameString,PortNumber,SlotNumber,SubrackNumber,SyncSourceMode,SyncSourceState=mibBuilder.importSymbols('LUM-TC',_AJ,_AK,_A1,'CommandString','FaultStatus',_AL,_o,'SlotNumber','SubrackNumber',_AM,'SyncSourceState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
lumSyncMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,17))
if mibBuilder.loadTexts:lumSyncMIBModule.setRevisions(('2018-01-25 00:00','2017-09-01 00:00','2017-06-15 00:00','2016-02-01 00:00','2015-01-14 00:00','2012-12-25 12:00','2011-05-31 00:00','2007-11-12 00:00','2002-12-11 00:00','2002-11-20 00:00','2002-05-16 00:00'))
_LumSyncConfs_ObjectIdentity=ObjectIdentity
lumSyncConfs=_LumSyncConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,16,1))
_LumSyncGroups_ObjectIdentity=ObjectIdentity
lumSyncGroups=_LumSyncGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,16,1,1))
_LumSyncCompl_ObjectIdentity=ObjectIdentity
lumSyncCompl=_LumSyncCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,16,1,2))
_LumSyncMIBObjects_ObjectIdentity=ObjectIdentity
lumSyncMIBObjects=_LumSyncMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2))
_SyncGeneral_ObjectIdentity=ObjectIdentity
syncGeneral=_SyncGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,1))
_SyncGeneralLastChangeTime_Type=DateAndTime
_SyncGeneralLastChangeTime_Object=MibScalar
syncGeneralLastChangeTime=_SyncGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,16,2,1,1),_SyncGeneralLastChangeTime_Type())
syncGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralLastChangeTime.setStatus(_B)
_SyncGeneralStateLastChangeTime_Type=DateAndTime
_SyncGeneralStateLastChangeTime_Object=MibScalar
syncGeneralStateLastChangeTime=_SyncGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,16,2,1,2),_SyncGeneralStateLastChangeTime_Type())
syncGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralStateLastChangeTime.setStatus(_B)
_SyncGeneralSyncGroupTableSize_Type=Unsigned32
_SyncGeneralSyncGroupTableSize_Object=MibScalar
syncGeneralSyncGroupTableSize=_SyncGeneralSyncGroupTableSize_Object((1,3,6,1,4,1,8708,2,16,2,1,3),_SyncGeneralSyncGroupTableSize_Type())
syncGeneralSyncGroupTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralSyncGroupTableSize.setStatus(_B)
_SyncGeneralSyncSourceTableSize_Type=Unsigned32
_SyncGeneralSyncSourceTableSize_Object=MibScalar
syncGeneralSyncSourceTableSize=_SyncGeneralSyncSourceTableSize_Object((1,3,6,1,4,1,8708,2,16,2,1,4),_SyncGeneralSyncSourceTableSize_Type())
syncGeneralSyncSourceTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralSyncSourceTableSize.setStatus(_B)
_SyncGeneralSyncSubrackTableSize_Type=Unsigned32
_SyncGeneralSyncSubrackTableSize_Object=MibScalar
syncGeneralSyncSubrackTableSize=_SyncGeneralSyncSubrackTableSize_Object((1,3,6,1,4,1,8708,2,16,2,1,5),_SyncGeneralSyncSubrackTableSize_Type())
syncGeneralSyncSubrackTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralSyncSubrackTableSize.setStatus(_D)
_SyncGeneralSyncDomainTableSize_Type=Unsigned32
_SyncGeneralSyncDomainTableSize_Object=MibScalar
syncGeneralSyncDomainTableSize=_SyncGeneralSyncDomainTableSize_Object((1,3,6,1,4,1,8708,2,16,2,1,6),_SyncGeneralSyncDomainTableSize_Type())
syncGeneralSyncDomainTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralSyncDomainTableSize.setStatus(_B)
_SyncGeneralSyncBusTableSize_Type=Unsigned32
_SyncGeneralSyncBusTableSize_Object=MibScalar
syncGeneralSyncBusTableSize=_SyncGeneralSyncBusTableSize_Object((1,3,6,1,4,1,8708,2,16,2,1,7),_SyncGeneralSyncBusTableSize_Type())
syncGeneralSyncBusTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralSyncBusTableSize.setStatus(_B)
_SyncGeneralSyncBoardToDomainTableSize_Type=Unsigned32
_SyncGeneralSyncBoardToDomainTableSize_Object=MibScalar
syncGeneralSyncBoardToDomainTableSize=_SyncGeneralSyncBoardToDomainTableSize_Object((1,3,6,1,4,1,8708,2,16,2,1,8),_SyncGeneralSyncBoardToDomainTableSize_Type())
syncGeneralSyncBoardToDomainTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGeneralSyncBoardToDomainTableSize.setStatus(_B)
_SyncGroups_ObjectIdentity=ObjectIdentity
syncGroups=_SyncGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,2))
_SyncGroupTable_Object=MibTable
syncGroupTable=_SyncGroupTable_Object((1,3,6,1,4,1,8708,2,16,2,2,1))
if mibBuilder.loadTexts:syncGroupTable.setStatus(_B)
_SyncGroupEntry_Object=MibTableRow
syncGroupEntry=_SyncGroupEntry_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1))
syncGroupEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:syncGroupEntry.setStatus(_B)
_SyncGroupIndex_Type=Unsigned32
_SyncGroupIndex_Object=MibTableColumn
syncGroupIndex=_SyncGroupIndex_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,1),_SyncGroupIndex_Type())
syncGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupIndex.setStatus(_B)
_SyncGroupName_Type=MgmtNameString
_SyncGroupName_Object=MibTableColumn
syncGroupName=_SyncGroupName_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,2),_SyncGroupName_Type())
syncGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupName.setStatus(_B)
_SyncGroupSubrack_Type=SubrackNumber
_SyncGroupSubrack_Object=MibTableColumn
syncGroupSubrack=_SyncGroupSubrack_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,3),_SyncGroupSubrack_Type())
syncGroupSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupSubrack.setStatus(_B)
_SyncGroupSlot_Type=SlotNumber
_SyncGroupSlot_Object=MibTableColumn
syncGroupSlot=_SyncGroupSlot_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,4),_SyncGroupSlot_Type())
syncGroupSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupSlot.setStatus(_B)
class _SyncGroupMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('auto',2)))
_SyncGroupMode_Type.__name__=_I
_SyncGroupMode_Object=MibTableColumn
syncGroupMode=_SyncGroupMode_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,5),_SyncGroupMode_Type())
syncGroupMode.setMaxAccess(_F)
if mibBuilder.loadTexts:syncGroupMode.setStatus(_B)
class _SyncGroupManualSource_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SyncGroupManualSource_Type.__name__=_E
_SyncGroupManualSource_Object=MibTableColumn
syncGroupManualSource=_SyncGroupManualSource_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,6),_SyncGroupManualSource_Type())
syncGroupManualSource.setMaxAccess(_G)
if mibBuilder.loadTexts:syncGroupManualSource.setStatus(_B)
_SyncGroupSelectedSource_Type=MgmtNameString
_SyncGroupSelectedSource_Object=MibTableColumn
syncGroupSelectedSource=_SyncGroupSelectedSource_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,7),_SyncGroupSelectedSource_Type())
syncGroupSelectedSource.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupSelectedSource.setStatus(_B)
class _SyncGroupQuality_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SyncGroupQuality_Type.__name__=_E
_SyncGroupQuality_Object=MibTableColumn
syncGroupQuality=_SyncGroupQuality_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,8),_SyncGroupQuality_Type())
syncGroupQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupQuality.setStatus(_B)
_SyncGroupLocalOscActiveW2C_Type=FaultStatus
_SyncGroupLocalOscActiveW2C_Object=MibTableColumn
syncGroupLocalOscActiveW2C=_SyncGroupLocalOscActiveW2C_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,9),_SyncGroupLocalOscActiveW2C_Type())
syncGroupLocalOscActiveW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupLocalOscActiveW2C.setStatus(_D)
_SyncGroupLocalOscActive_Type=FaultStatus
_SyncGroupLocalOscActive_Object=MibTableColumn
syncGroupLocalOscActive=_SyncGroupLocalOscActive_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,10),_SyncGroupLocalOscActive_Type())
syncGroupLocalOscActive.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupLocalOscActive.setStatus(_B)
class _SyncGroupAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_SyncGroupAdminStatus_Type.__name__=_AK
_SyncGroupAdminStatus_Object=MibTableColumn
syncGroupAdminStatus=_SyncGroupAdminStatus_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,11),_SyncGroupAdminStatus_Type())
syncGroupAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:syncGroupAdminStatus.setStatus(_B)
class _SyncGroupOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_SyncGroupOperStatus_Type.__name__=_A1
_SyncGroupOperStatus_Object=MibTableColumn
syncGroupOperStatus=_SyncGroupOperStatus_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,12),_SyncGroupOperStatus_Type())
syncGroupOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupOperStatus.setStatus(_B)
class _SyncGroupRingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_SyncGroupRingMode_Type.__name__=_I
_SyncGroupRingMode_Object=MibTableColumn
syncGroupRingMode=_SyncGroupRingMode_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,13),_SyncGroupRingMode_Type())
syncGroupRingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:syncGroupRingMode.setStatus(_D)
_SyncGroupLastChangeTime_Type=DateAndTime
_SyncGroupLastChangeTime_Object=MibTableColumn
syncGroupLastChangeTime=_SyncGroupLastChangeTime_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,14),_SyncGroupLastChangeTime_Type())
syncGroupLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupLastChangeTime.setStatus(_B)
class _SyncGroupManualSourceName_Type(MgmtNameString):defaultValue=OctetString('')
_SyncGroupManualSourceName_Type.__name__=_AL
_SyncGroupManualSourceName_Object=MibTableColumn
syncGroupManualSourceName=_SyncGroupManualSourceName_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,15),_SyncGroupManualSourceName_Type())
syncGroupManualSourceName.setMaxAccess(_F)
if mibBuilder.loadTexts:syncGroupManualSourceName.setStatus(_B)
class _SyncGroupConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('neverUseTrunc',1),('uniDirRingSatellite',2),('standardG707',3)))
_SyncGroupConfigurationMode_Type.__name__=_I
_SyncGroupConfigurationMode_Object=MibTableColumn
syncGroupConfigurationMode=_SyncGroupConfigurationMode_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,16),_SyncGroupConfigurationMode_Type())
syncGroupConfigurationMode.setMaxAccess(_F)
if mibBuilder.loadTexts:syncGroupConfigurationMode.setStatus(_B)
class _SyncGroupStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('holdover',2)))
_SyncGroupStatus_Type.__name__=_I
_SyncGroupStatus_Object=MibTableColumn
syncGroupStatus=_SyncGroupStatus_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,17),_SyncGroupStatus_Type())
syncGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupStatus.setStatus(_B)
_SyncGroupSourceSwitch_Type=CommandString
_SyncGroupSourceSwitch_Object=MibTableColumn
syncGroupSourceSwitch=_SyncGroupSourceSwitch_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,18),_SyncGroupSourceSwitch_Type())
syncGroupSourceSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupSourceSwitch.setStatus(_B)
class _SyncGroupSourceSwitchType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('manual',2),('forced',3)))
_SyncGroupSourceSwitchType_Type.__name__=_I
_SyncGroupSourceSwitchType_Object=MibTableColumn
syncGroupSourceSwitchType=_SyncGroupSourceSwitchType_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,19),_SyncGroupSourceSwitchType_Type())
syncGroupSourceSwitchType.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupSourceSwitchType.setStatus(_B)
_SyncGroupHoldover_Type=FaultStatus
_SyncGroupHoldover_Object=MibTableColumn
syncGroupHoldover=_SyncGroupHoldover_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,20),_SyncGroupHoldover_Type())
syncGroupHoldover.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupHoldover.setStatus(_B)
class _SyncGroupQualityLevelSelectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A2,1),(_A3,2)))
_SyncGroupQualityLevelSelectionMode_Type.__name__=_I
_SyncGroupQualityLevelSelectionMode_Object=MibTableColumn
syncGroupQualityLevelSelectionMode=_SyncGroupQualityLevelSelectionMode_Object((1,3,6,1,4,1,8708,2,16,2,2,1,1,21),_SyncGroupQualityLevelSelectionMode_Type())
syncGroupQualityLevelSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:syncGroupQualityLevelSelectionMode.setStatus(_B)
_SyncSources_ObjectIdentity=ObjectIdentity
syncSources=_SyncSources_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,3))
_SyncSourceTable_Object=MibTable
syncSourceTable=_SyncSourceTable_Object((1,3,6,1,4,1,8708,2,16,2,3,1))
if mibBuilder.loadTexts:syncSourceTable.setStatus(_B)
_SyncSourceEntry_Object=MibTableRow
syncSourceEntry=_SyncSourceEntry_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1))
syncSourceEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:syncSourceEntry.setStatus(_B)
class _SyncSourceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000000000))
_SyncSourceIndex_Type.__name__=_E
_SyncSourceIndex_Object=MibTableColumn
syncSourceIndex=_SyncSourceIndex_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,1),_SyncSourceIndex_Type())
syncSourceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceIndex.setStatus(_B)
_SyncSourceName_Type=MgmtNameString
_SyncSourceName_Object=MibTableColumn
syncSourceName=_SyncSourceName_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,2),_SyncSourceName_Type())
syncSourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceName.setStatus(_B)
class _SyncSourceId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SyncSourceId_Type.__name__=_E
_SyncSourceId_Object=MibTableColumn
syncSourceId=_SyncSourceId_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,3),_SyncSourceId_Type())
syncSourceId.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSourceId.setStatus(_B)
class _SyncSourceRxPort_Type(PortNumber):defaultValue=0
_SyncSourceRxPort_Type.__name__=_o
_SyncSourceRxPort_Object=MibTableColumn
syncSourceRxPort=_SyncSourceRxPort_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,4),_SyncSourceRxPort_Type())
syncSourceRxPort.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSourceRxPort.setStatus(_B)
class _SyncSourceTxPort_Type(PortNumber):defaultValue=0
_SyncSourceTxPort_Type.__name__=_o
_SyncSourceTxPort_Object=MibTableColumn
syncSourceTxPort=_SyncSourceTxPort_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,5),_SyncSourceTxPort_Type())
syncSourceTxPort.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSourceTxPort.setStatus(_B)
class _SyncSourceType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oscillator',1),('signal',2),('external',3),('bus',4)))
_SyncSourceType_Type.__name__=_I
_SyncSourceType_Object=MibTableColumn
syncSourceType=_SyncSourceType_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,6),_SyncSourceType_Type())
syncSourceType.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSourceType.setStatus(_B)
class _SyncSourceQuality_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18))
_SyncSourceQuality_Type.__name__=_E
_SyncSourceQuality_Object=MibTableColumn
syncSourceQuality=_SyncSourceQuality_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,7),_SyncSourceQuality_Type())
syncSourceQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceQuality.setStatus(_B)
class _SyncSourcePriority_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SyncSourcePriority_Type.__name__=_E
_SyncSourcePriority_Object=MibTableColumn
syncSourcePriority=_SyncSourcePriority_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,8),_SyncSourcePriority_Type())
syncSourcePriority.setMaxAccess(_F)
if mibBuilder.loadTexts:syncSourcePriority.setStatus(_B)
class _SyncSourceAdminStatus_Type(AdminStatus):defaultValue=1
_SyncSourceAdminStatus_Type.__name__=_AJ
_SyncSourceAdminStatus_Object=MibTableColumn
syncSourceAdminStatus=_SyncSourceAdminStatus_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,9),_SyncSourceAdminStatus_Type())
syncSourceAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:syncSourceAdminStatus.setStatus(_B)
class _SyncSourceOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_SyncSourceOperStatus_Type.__name__=_A1
_SyncSourceOperStatus_Object=MibTableColumn
syncSourceOperStatus=_SyncSourceOperStatus_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,10),_SyncSourceOperStatus_Type())
syncSourceOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceOperStatus.setStatus(_B)
_SyncSourceIsSelected_Type=TruthValue
_SyncSourceIsSelected_Object=MibTableColumn
syncSourceIsSelected=_SyncSourceIsSelected_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,11),_SyncSourceIsSelected_Type())
syncSourceIsSelected.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceIsSelected.setStatus(_B)
class _SyncSourceAlwaysSendDoNotUse_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A2,1),(_A3,2)))
_SyncSourceAlwaysSendDoNotUse_Type.__name__=_I
_SyncSourceAlwaysSendDoNotUse_Object=MibTableColumn
syncSourceAlwaysSendDoNotUse=_SyncSourceAlwaysSendDoNotUse_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,12),_SyncSourceAlwaysSendDoNotUse_Type())
syncSourceAlwaysSendDoNotUse.setMaxAccess(_F)
if mibBuilder.loadTexts:syncSourceAlwaysSendDoNotUse.setStatus(_B)
class _SyncSourceStaticQuality_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SyncSourceStaticQuality_Type.__name__=_E
_SyncSourceStaticQuality_Object=MibTableColumn
syncSourceStaticQuality=_SyncSourceStaticQuality_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,13),_SyncSourceStaticQuality_Type())
syncSourceStaticQuality.setMaxAccess(_F)
if mibBuilder.loadTexts:syncSourceStaticQuality.setStatus(_B)
_SyncSourceFilterState_Type=SyncSourceState
_SyncSourceFilterState_Object=MibTableColumn
syncSourceFilterState=_SyncSourceFilterState_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,14),_SyncSourceFilterState_Type())
syncSourceFilterState.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceFilterState.setStatus(_B)
class _SyncSourceMode_Type(SyncSourceMode):defaultValue=0
_SyncSourceMode_Type.__name__=_AM
_SyncSourceMode_Object=MibTableColumn
syncSourceMode=_SyncSourceMode_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,15),_SyncSourceMode_Type())
syncSourceMode.setMaxAccess(_F)
if mibBuilder.loadTexts:syncSourceMode.setStatus(_B)
_SyncSourceClearWaitToRestore_Type=CommandString
_SyncSourceClearWaitToRestore_Object=MibTableColumn
syncSourceClearWaitToRestore=_SyncSourceClearWaitToRestore_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,16),_SyncSourceClearWaitToRestore_Type())
syncSourceClearWaitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceClearWaitToRestore.setStatus(_B)
_SyncSourceClockWanderExceeded_Type=FaultStatus
_SyncSourceClockWanderExceeded_Object=MibTableColumn
syncSourceClockWanderExceeded=_SyncSourceClockWanderExceeded_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,17),_SyncSourceClockWanderExceeded_Type())
syncSourceClockWanderExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceClockWanderExceeded.setStatus(_B)
_SyncSourceNonSyncEClock_Type=FaultStatus
_SyncSourceNonSyncEClock_Object=MibTableColumn
syncSourceNonSyncEClock=_SyncSourceNonSyncEClock_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,18),_SyncSourceNonSyncEClock_Type())
syncSourceNonSyncEClock.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSourceNonSyncEClock.setStatus(_B)
class _SyncSourceIfNo_Type(PortNumber):defaultValue=1
_SyncSourceIfNo_Type.__name__=_o
_SyncSourceIfNo_Object=MibTableColumn
syncSourceIfNo=_SyncSourceIfNo_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,19),_SyncSourceIfNo_Type())
syncSourceIfNo.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSourceIfNo.setStatus(_B)
class _SyncSourceUpPortId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_SyncSourceUpPortId_Type.__name__=_I
_SyncSourceUpPortId_Object=MibTableColumn
syncSourceUpPortId=_SyncSourceUpPortId_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,20),_SyncSourceUpPortId_Type())
syncSourceUpPortId.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSourceUpPortId.setStatus(_B)
class _SyncSourceLocalId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_SyncSourceLocalId_Type.__name__=_I
_SyncSourceLocalId_Object=MibTableColumn
syncSourceLocalId=_SyncSourceLocalId_Object((1,3,6,1,4,1,8708,2,16,2,3,1,1,21),_SyncSourceLocalId_Type())
syncSourceLocalId.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSourceLocalId.setStatus(_B)
_LumentisSyncNotifications_ObjectIdentity=ObjectIdentity
lumentisSyncNotifications=_LumentisSyncNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,4))
_SyncNotifyPrefix_ObjectIdentity=ObjectIdentity
syncNotifyPrefix=_SyncNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,4,0))
_SyncSubracks_ObjectIdentity=ObjectIdentity
syncSubracks=_SyncSubracks_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,5))
_SyncSubrackTable_Object=MibTable
syncSubrackTable=_SyncSubrackTable_Object((1,3,6,1,4,1,8708,2,16,2,5,1))
if mibBuilder.loadTexts:syncSubrackTable.setStatus(_D)
_SyncSubrackEntry_Object=MibTableRow
syncSubrackEntry=_SyncSubrackEntry_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1))
syncSubrackEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:syncSubrackEntry.setStatus(_D)
_SyncSubrackIndex_Type=Unsigned32
_SyncSubrackIndex_Object=MibTableColumn
syncSubrackIndex=_SyncSubrackIndex_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,1),_SyncSubrackIndex_Type())
syncSubrackIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSubrackIndex.setStatus(_D)
_SyncSubrackName_Type=MgmtNameString
_SyncSubrackName_Object=MibTableColumn
syncSubrackName=_SyncSubrackName_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,2),_SyncSubrackName_Type())
syncSubrackName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSubrackName.setStatus(_D)
_SyncSubrackSubrack_Type=SubrackNumber
_SyncSubrackSubrack_Object=MibTableColumn
syncSubrackSubrack=_SyncSubrackSubrack_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,3),_SyncSubrackSubrack_Type())
syncSubrackSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSubrackSubrack.setStatus(_D)
_SyncSubrackMasterBusA_Type=SlotNumber
_SyncSubrackMasterBusA_Object=MibTableColumn
syncSubrackMasterBusA=_SyncSubrackMasterBusA_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,4),_SyncSubrackMasterBusA_Type())
syncSubrackMasterBusA.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSubrackMasterBusA.setStatus(_D)
_SyncSubrackMasterBusB_Type=SlotNumber
_SyncSubrackMasterBusB_Object=MibTableColumn
syncSubrackMasterBusB=_SyncSubrackMasterBusB_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,5),_SyncSubrackMasterBusB_Type())
syncSubrackMasterBusB.setMaxAccess(_G)
if mibBuilder.loadTexts:syncSubrackMasterBusB.setStatus(_D)
_SyncSubrackConfigureLocalBus_Type=CommandString
_SyncSubrackConfigureLocalBus_Object=MibTableColumn
syncSubrackConfigureLocalBus=_SyncSubrackConfigureLocalBus_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,6),_SyncSubrackConfigureLocalBus_Type())
syncSubrackConfigureLocalBus.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSubrackConfigureLocalBus.setStatus(_D)
_SyncSubrackGroupMasterBusA_Type=DisplayString
_SyncSubrackGroupMasterBusA_Object=MibTableColumn
syncSubrackGroupMasterBusA=_SyncSubrackGroupMasterBusA_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,7),_SyncSubrackGroupMasterBusA_Type())
syncSubrackGroupMasterBusA.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSubrackGroupMasterBusA.setStatus(_D)
_SyncSubrackGroupMasterBusB_Type=DisplayString
_SyncSubrackGroupMasterBusB_Object=MibTableColumn
syncSubrackGroupMasterBusB=_SyncSubrackGroupMasterBusB_Object((1,3,6,1,4,1,8708,2,16,2,5,1,1,8),_SyncSubrackGroupMasterBusB_Type())
syncSubrackGroupMasterBusB.setMaxAccess(_C)
if mibBuilder.loadTexts:syncSubrackGroupMasterBusB.setStatus(_D)
_SyncDomains_ObjectIdentity=ObjectIdentity
syncDomains=_SyncDomains_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,6))
_SyncDomainTable_Object=MibTable
syncDomainTable=_SyncDomainTable_Object((1,3,6,1,4,1,8708,2,16,2,6,1))
if mibBuilder.loadTexts:syncDomainTable.setStatus(_B)
_SyncDomainEntry_Object=MibTableRow
syncDomainEntry=_SyncDomainEntry_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1))
syncDomainEntry.setIndexNames((0,_A,_A4))
if mibBuilder.loadTexts:syncDomainEntry.setStatus(_B)
_SyncDomainIndex_Type=Unsigned32
_SyncDomainIndex_Object=MibTableColumn
syncDomainIndex=_SyncDomainIndex_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,1),_SyncDomainIndex_Type())
syncDomainIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:syncDomainIndex.setStatus(_B)
_SyncDomainNumber_Type=Unsigned32
_SyncDomainNumber_Object=MibTableColumn
syncDomainNumber=_SyncDomainNumber_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,2),_SyncDomainNumber_Type())
syncDomainNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:syncDomainNumber.setStatus(_B)
_SyncDomainName_Type=MgmtNameString
_SyncDomainName_Object=MibTableColumn
syncDomainName=_SyncDomainName_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,3),_SyncDomainName_Type())
syncDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncDomainName.setStatus(_B)
class _SyncDomainQualityLevelSelectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A2,1),(_A3,2)))
_SyncDomainQualityLevelSelectionMode_Type.__name__=_I
_SyncDomainQualityLevelSelectionMode_Object=MibTableColumn
syncDomainQualityLevelSelectionMode=_SyncDomainQualityLevelSelectionMode_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,4),_SyncDomainQualityLevelSelectionMode_Type())
syncDomainQualityLevelSelectionMode.setMaxAccess(_F)
if mibBuilder.loadTexts:syncDomainQualityLevelSelectionMode.setStatus(_B)
class _SyncDomainWaitToRestore_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_SyncDomainWaitToRestore_Type.__name__=_E
_SyncDomainWaitToRestore_Object=MibTableColumn
syncDomainWaitToRestore=_SyncDomainWaitToRestore_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,5),_SyncDomainWaitToRestore_Type())
syncDomainWaitToRestore.setMaxAccess(_F)
if mibBuilder.loadTexts:syncDomainWaitToRestore.setStatus(_B)
class _SyncDomainHoldOff_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SyncDomainHoldOff_Type.__name__=_E
_SyncDomainHoldOff_Object=MibTableColumn
syncDomainHoldOff=_SyncDomainHoldOff_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,6),_SyncDomainHoldOff_Type())
syncDomainHoldOff.setMaxAccess(_F)
if mibBuilder.loadTexts:syncDomainHoldOff.setStatus(_B)
_SyncDomainSource_Type=MgmtNameString
_SyncDomainSource_Object=MibTableColumn
syncDomainSource=_SyncDomainSource_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,7),_SyncDomainSource_Type())
syncDomainSource.setMaxAccess(_C)
if mibBuilder.loadTexts:syncDomainSource.setStatus(_B)
class _SyncDomainQuality_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SyncDomainQuality_Type.__name__=_E
_SyncDomainQuality_Object=MibTableColumn
syncDomainQuality=_SyncDomainQuality_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,8),_SyncDomainQuality_Type())
syncDomainQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:syncDomainQuality.setStatus(_B)
_SyncDomainAssociateBoard_Type=CommandString
_SyncDomainAssociateBoard_Object=MibTableColumn
syncDomainAssociateBoard=_SyncDomainAssociateBoard_Object((1,3,6,1,4,1,8708,2,16,2,6,1,1,9),_SyncDomainAssociateBoard_Type())
syncDomainAssociateBoard.setMaxAccess(_C)
if mibBuilder.loadTexts:syncDomainAssociateBoard.setStatus(_B)
_SyncBuses_ObjectIdentity=ObjectIdentity
syncBuses=_SyncBuses_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,7))
_SyncBusTable_Object=MibTable
syncBusTable=_SyncBusTable_Object((1,3,6,1,4,1,8708,2,16,2,7,1))
if mibBuilder.loadTexts:syncBusTable.setStatus(_B)
_SyncBusEntry_Object=MibTableRow
syncBusEntry=_SyncBusEntry_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1))
syncBusEntry.setIndexNames((0,_A,_A5))
if mibBuilder.loadTexts:syncBusEntry.setStatus(_B)
_SyncBusIndex_Type=Unsigned32
_SyncBusIndex_Object=MibTableColumn
syncBusIndex=_SyncBusIndex_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1,1),_SyncBusIndex_Type())
syncBusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:syncBusIndex.setStatus(_B)
_SyncBusName_Type=MgmtNameString
_SyncBusName_Object=MibTableColumn
syncBusName=_SyncBusName_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1,2),_SyncBusName_Type())
syncBusName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncBusName.setStatus(_B)
_SyncBusSubrack_Type=Unsigned32
_SyncBusSubrack_Object=MibTableColumn
syncBusSubrack=_SyncBusSubrack_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1,3),_SyncBusSubrack_Type())
syncBusSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:syncBusSubrack.setStatus(_B)
class _SyncBusDomain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,160))
_SyncBusDomain_Type.__name__=_E
_SyncBusDomain_Object=MibTableColumn
syncBusDomain=_SyncBusDomain_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1,4),_SyncBusDomain_Type())
syncBusDomain.setMaxAccess(_F)
if mibBuilder.loadTexts:syncBusDomain.setStatus(_B)
class _SyncBusDomainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SyncBusDomainIndex_Type.__name__=_E
_SyncBusDomainIndex_Object=MibTableColumn
syncBusDomainIndex=_SyncBusDomainIndex_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1,5),_SyncBusDomainIndex_Type())
syncBusDomainIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:syncBusDomainIndex.setStatus(_B)
_SyncBusStaticMasterSlot_Type=SlotNumber
_SyncBusStaticMasterSlot_Object=MibTableColumn
syncBusStaticMasterSlot=_SyncBusStaticMasterSlot_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1,6),_SyncBusStaticMasterSlot_Type())
syncBusStaticMasterSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:syncBusStaticMasterSlot.setStatus(_B)
class _SyncBusStaticMasterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SyncBusStaticMasterIndex_Type.__name__=_E
_SyncBusStaticMasterIndex_Object=MibTableColumn
syncBusStaticMasterIndex=_SyncBusStaticMasterIndex_Object((1,3,6,1,4,1,8708,2,16,2,7,1,1,7),_SyncBusStaticMasterIndex_Type())
syncBusStaticMasterIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:syncBusStaticMasterIndex.setStatus(_B)
_SyncBoardToDomain_ObjectIdentity=ObjectIdentity
syncBoardToDomain=_SyncBoardToDomain_ObjectIdentity((1,3,6,1,4,1,8708,2,16,2,8))
_SyncBoardToDomainTable_Object=MibTable
syncBoardToDomainTable=_SyncBoardToDomainTable_Object((1,3,6,1,4,1,8708,2,16,2,8,1))
if mibBuilder.loadTexts:syncBoardToDomainTable.setStatus(_B)
_SyncBoardToDomainEntry_Object=MibTableRow
syncBoardToDomainEntry=_SyncBoardToDomainEntry_Object((1,3,6,1,4,1,8708,2,16,2,8,1,1))
syncBoardToDomainEntry.setIndexNames((0,_A,_A6))
if mibBuilder.loadTexts:syncBoardToDomainEntry.setStatus(_B)
_SyncBoardToDomainIndex_Type=Unsigned32
_SyncBoardToDomainIndex_Object=MibTableColumn
syncBoardToDomainIndex=_SyncBoardToDomainIndex_Object((1,3,6,1,4,1,8708,2,16,2,8,1,1,1),_SyncBoardToDomainIndex_Type())
syncBoardToDomainIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:syncBoardToDomainIndex.setStatus(_B)
_SyncBoardToDomainName_Type=MgmtNameString
_SyncBoardToDomainName_Object=MibTableColumn
syncBoardToDomainName=_SyncBoardToDomainName_Object((1,3,6,1,4,1,8708,2,16,2,8,1,1,2),_SyncBoardToDomainName_Type())
syncBoardToDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncBoardToDomainName.setStatus(_B)
class _SyncBoardToDomainDomainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SyncBoardToDomainDomainIndex_Type.__name__=_E
_SyncBoardToDomainDomainIndex_Object=MibTableColumn
syncBoardToDomainDomainIndex=_SyncBoardToDomainDomainIndex_Object((1,3,6,1,4,1,8708,2,16,2,8,1,1,3),_SyncBoardToDomainDomainIndex_Type())
syncBoardToDomainDomainIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:syncBoardToDomainDomainIndex.setStatus(_B)
_SyncBoardToDomainDomainName_Type=MgmtNameString
_SyncBoardToDomainDomainName_Object=MibTableColumn
syncBoardToDomainDomainName=_SyncBoardToDomainDomainName_Object((1,3,6,1,4,1,8708,2,16,2,8,1,1,4),_SyncBoardToDomainDomainName_Type())
syncBoardToDomainDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncBoardToDomainDomainName.setStatus(_B)
class _SyncBoardToDomainBoardIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SyncBoardToDomainBoardIndex_Type.__name__=_E
_SyncBoardToDomainBoardIndex_Object=MibTableColumn
syncBoardToDomainBoardIndex=_SyncBoardToDomainBoardIndex_Object((1,3,6,1,4,1,8708,2,16,2,8,1,1,5),_SyncBoardToDomainBoardIndex_Type())
syncBoardToDomainBoardIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:syncBoardToDomainBoardIndex.setStatus(_B)
_SyncBoardToDomainBoardName_Type=MgmtNameString
_SyncBoardToDomainBoardName_Object=MibTableColumn
syncBoardToDomainBoardName=_SyncBoardToDomainBoardName_Object((1,3,6,1,4,1,8708,2,16,2,8,1,1,6),_SyncBoardToDomainBoardName_Type())
syncBoardToDomainBoardName.setMaxAccess(_C)
if mibBuilder.loadTexts:syncBoardToDomainBoardName.setStatus(_B)
syncGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,1))
syncGeneralGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:syncGeneralGroup.setStatus(_D)
syncGroupGroup=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,2))
syncGroupGroup.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_j)))
if mibBuilder.loadTexts:syncGroupGroup.setStatus(_D)
syncSourceGroup=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,3))
syncSourceGroup.setObjects(*((_A,_T),(_A,_U),(_A,_Z),(_A,_a),(_A,_b),(_A,_V),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:syncSourceGroup.setStatus(_B)
syncGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,4))
syncGeneralGroupV2.setObjects(*((_A,_q),(_A,_A7)))
if mibBuilder.loadTexts:syncGeneralGroupV2.setStatus(_D)
syncGroupGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,5))
syncGroupGroupV2.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_j),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:syncGroupGroupV2.setStatus(_D)
syncGroupGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,6))
syncGroupGroupV3.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_j),(_A,_W),(_A,_X),(_A,_g)))
if mibBuilder.loadTexts:syncGroupGroupV3.setStatus(_D)
syncSourceGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,7))
syncSourceGroupV2.setObjects(*((_A,_T),(_A,_i),(_A,_U),(_A,_Z),(_A,_a),(_A,_b),(_A,_V),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:syncSourceGroupV2.setStatus(_D)
syncGroupGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,9))
syncGroupGroupV4.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_j),(_A,_W),(_A,_X),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:syncGroupGroupV4.setStatus(_D)
syncSourceGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,10))
syncSourceGroupV3.setObjects(*((_A,_T),(_A,_i),(_A,_U),(_A,_Z),(_A,_a),(_A,_b),(_A,_V),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_k)))
if mibBuilder.loadTexts:syncSourceGroupV3.setStatus(_D)
syncGroupGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,12))
syncGroupGroupV6.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_l),(_A,_W),(_A,_X),(_A,_g),(_A,_h),(_A,_m)))
if mibBuilder.loadTexts:syncGroupGroupV6.setStatus(_D)
syncGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,13))
syncGeneralGroupV3.setObjects(*((_A,_q),(_A,_A7),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:syncGeneralGroupV3.setStatus(_B)
syncGroupGroupV7=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,14))
syncGroupGroupV7.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_l),(_A,_W),(_A,_X),(_A,_g),(_A,_h),(_A,_m),(_A,_r)))
if mibBuilder.loadTexts:syncGroupGroupV7.setStatus(_D)
syncSubrackGroup=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,15))
syncSubrackGroup.setObjects(*((_A,_p),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:syncSubrackGroup.setStatus(_D)
syncGroupGroupV8=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,16))
syncGroupGroupV8.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_l),(_A,_W),(_A,_X),(_A,_g),(_A,_h),(_A,_m),(_A,_r),(_A,_AD)))
if mibBuilder.loadTexts:syncGroupGroupV8.setStatus(_B)
syncSubrackGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,17))
syncSubrackGroupV2.setObjects(*((_A,_p),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:syncSubrackGroupV2.setStatus(_B)
syncSourceGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,18))
syncSourceGroupV4.setObjects(*((_A,_T),(_A,_i),(_A,_U),(_A,_Z),(_A,_a),(_A,_b),(_A,_V),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_k),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:syncSourceGroupV4.setStatus(_D)
syncDomainGroup=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,19))
syncDomainGroup.setObjects(*((_A,_A4),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:syncDomainGroup.setStatus(_B)
syncBusGroup=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,20))
syncBusGroup.setObjects(*((_A,_A5),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:syncBusGroup.setStatus(_B)
syncBoardToDomainGroup=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,21))
syncBoardToDomainGroup.setObjects(*((_A,_A6),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:syncBoardToDomainGroup.setStatus(_B)
syncGroupGroupV9=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,22))
syncGroupGroupV9.setObjects(*((_A,_J),(_A,_M),(_A,_N),(_A,_K),(_A,_O),(_A,_P),(_A,_L),(_A,_Q),(_A,_l),(_A,_W),(_A,_X),(_A,_g),(_A,_h),(_A,_m),(_A,_r),(_A,_AD),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:syncGroupGroupV9.setStatus(_B)
syncSourceGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,23))
syncSourceGroupV5.setObjects(*((_A,_T),(_A,_i),(_A,_U),(_A,_Z),(_A,_a),(_A,_b),(_A,_V),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_k),(_A,_s),(_A,_t),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:syncSourceGroupV5.setStatus(_D)
syncSourceGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,16,1,1,24))
syncSourceGroupV6.setObjects(*((_A,_T),(_A,_i),(_A,_U),(_A,_Z),(_A,_a),(_A,_b),(_A,_V),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_k),(_A,_s),(_A,_t),(_A,_AE),(_A,_AF),(_A,_Ap),(_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:syncSourceGroupV6.setStatus(_B)
syncGroupSourceChanged=NotificationType((1,3,6,1,4,1,8708,2,16,2,4,0,1))
syncGroupSourceChanged.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_U),(_A,_h),(_A,_V)))
if mibBuilder.loadTexts:syncGroupSourceChanged.setStatus(_B)
syncNotificationGroup=NotificationGroup((1,3,6,1,4,1,8708,2,16,1,1,8))
syncNotificationGroup.setObjects((_A,_As))
if mibBuilder.loadTexts:syncNotificationGroup.setStatus(_B)
lumSyncBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,1))
lumSyncBasicComplV1.setObjects(*((_A,_At),(_A,_AG),(_A,_n)))
if mibBuilder.loadTexts:lumSyncBasicComplV1.setStatus(_D)
lumSyncBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,2))
lumSyncBasicComplV2.setObjects(*((_A,_R),(_A,_AG),(_A,_n)))
if mibBuilder.loadTexts:lumSyncBasicComplV2.setStatus(_D)
lumSyncBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,3))
lumSyncBasicComplV3.setObjects(*((_A,_R),(_A,_Au),(_A,_n)))
if mibBuilder.loadTexts:lumSyncBasicComplV3.setStatus(_D)
lumSyncBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,4))
lumSyncBasicComplV4.setObjects(*((_A,_R),(_A,_u),(_A,_n)))
if mibBuilder.loadTexts:lumSyncBasicComplV4.setStatus(_D)
lumSyncBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,5))
lumSyncBasicComplV5.setObjects(*((_A,_R),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:lumSyncBasicComplV5.setStatus(_D)
lumSyncBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,6))
lumSyncBasicComplV6.setObjects(*((_A,_R),(_A,_u),(_A,_v),(_A,_H)))
if mibBuilder.loadTexts:lumSyncBasicComplV6.setStatus(_D)
lumSyncBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,7))
lumSyncBasicComplV7.setObjects(*((_A,_R),(_A,_AH),(_A,_v),(_A,_H)))
if mibBuilder.loadTexts:lumSyncBasicComplV7.setStatus(_D)
lumSyncBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,8))
lumSyncBasicComplV8.setObjects(*((_A,_R),(_A,_AH),(_A,_Y),(_A,_H)))
if mibBuilder.loadTexts:lumSyncBasicComplV8.setStatus(_D)
lumSyncBasicComplV9=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,9))
lumSyncBasicComplV9.setObjects(*((_A,_R),(_A,_w),(_A,_Y),(_A,_H)))
if mibBuilder.loadTexts:lumSyncBasicComplV9.setStatus(_D)
lumSyncBasicComplV10=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,10))
lumSyncBasicComplV10.setObjects(*((_A,_S),(_A,_w),(_A,_Y),(_A,_H)))
if mibBuilder.loadTexts:lumSyncBasicComplV10.setStatus(_D)
lumSyncBasicComplV11=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,11))
lumSyncBasicComplV11.setObjects(*((_A,_S),(_A,_w),(_A,_Y),(_A,_H)))
if mibBuilder.loadTexts:lumSyncBasicComplV11.setStatus(_D)
lumSyncBasicComplV12=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,12))
lumSyncBasicComplV12.setObjects(*((_A,_S),(_A,_Av),(_A,_Y),(_A,_H)))
if mibBuilder.loadTexts:lumSyncBasicComplV12.setStatus(_D)
lumSyncBasicComplV13=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,13))
lumSyncBasicComplV13.setObjects(*((_A,_S),(_A,_AI),(_A,_Y),(_A,_H),(_A,_Aw)))
if mibBuilder.loadTexts:lumSyncBasicComplV13.setStatus(_D)
lumSyncBasicComplV14=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,14))
lumSyncBasicComplV14.setObjects(*((_A,_S),(_A,_AI),(_A,_Y),(_A,_H),(_A,_Ax)))
if mibBuilder.loadTexts:lumSyncBasicComplV14.setStatus(_D)
lumSyncBasicComplV15=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,15))
lumSyncBasicComplV15.setObjects(*((_A,_S),(_A,_x),(_A,_Ay),(_A,_H),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:lumSyncBasicComplV15.setStatus(_D)
lumSyncBasicComplV16=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,16))
lumSyncBasicComplV16.setObjects(*((_A,_S),(_A,_x),(_A,_Az),(_A,_H),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:lumSyncBasicComplV16.setStatus(_B)
lumSyncBasicComplV17=ModuleCompliance((1,3,6,1,4,1,8708,2,16,1,2,17))
lumSyncBasicComplV17.setObjects(*((_A,_S),(_A,_x),(_A,_A_),(_A,_H),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:lumSyncBasicComplV17.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumSyncMIBModule':lumSyncMIBModule,'lumSyncConfs':lumSyncConfs,'lumSyncGroups':lumSyncGroups,_At:syncGeneralGroup,_AG:syncGroupGroup,_n:syncSourceGroup,_R:syncGeneralGroupV2,_Au:syncGroupGroupV2,_u:syncGroupGroupV3,_v:syncSourceGroupV2,_H:syncNotificationGroup,_AH:syncGroupGroupV4,_Y:syncSourceGroupV3,_w:syncGroupGroupV6,_S:syncGeneralGroupV3,_Av:syncGroupGroupV7,_Aw:syncSubrackGroup,_AI:syncGroupGroupV8,_Ax:syncSubrackGroupV2,_Ay:syncSourceGroupV4,_y:syncDomainGroup,_z:syncBusGroup,_A0:syncBoardToDomainGroup,_x:syncGroupGroupV9,_Az:syncSourceGroupV5,_A_:syncSourceGroupV6,'lumSyncCompl':lumSyncCompl,'lumSyncBasicComplV1':lumSyncBasicComplV1,'lumSyncBasicComplV2':lumSyncBasicComplV2,'lumSyncBasicComplV3':lumSyncBasicComplV3,'lumSyncBasicComplV4':lumSyncBasicComplV4,'lumSyncBasicComplV5':lumSyncBasicComplV5,'lumSyncBasicComplV6':lumSyncBasicComplV6,'lumSyncBasicComplV7':lumSyncBasicComplV7,'lumSyncBasicComplV8':lumSyncBasicComplV8,'lumSyncBasicComplV9':lumSyncBasicComplV9,'lumSyncBasicComplV10':lumSyncBasicComplV10,'lumSyncBasicComplV11':lumSyncBasicComplV11,'lumSyncBasicComplV12':lumSyncBasicComplV12,'lumSyncBasicComplV13':lumSyncBasicComplV13,'lumSyncBasicComplV14':lumSyncBasicComplV14,'lumSyncBasicComplV15':lumSyncBasicComplV15,'lumSyncBasicComplV16':lumSyncBasicComplV16,'lumSyncBasicComplV17':lumSyncBasicComplV17,'lumSyncMIBObjects':lumSyncMIBObjects,'syncGeneral':syncGeneral,_q:syncGeneralLastChangeTime,_A7:syncGeneralStateLastChangeTime,_AN:syncGeneralSyncGroupTableSize,_AO:syncGeneralSyncSourceTableSize,_AP:syncGeneralSyncSubrackTableSize,'syncGeneralSyncDomainTableSize':syncGeneralSyncDomainTableSize,'syncGeneralSyncBusTableSize':syncGeneralSyncBusTableSize,'syncGeneralSyncBoardToDomainTableSize':syncGeneralSyncBoardToDomainTableSize,'syncGroups':syncGroups,'syncGroupTable':syncGroupTable,'syncGroupEntry':syncGroupEntry,_J:syncGroupIndex,_K:syncGroupName,_M:syncGroupSubrack,_N:syncGroupSlot,_O:syncGroupMode,_P:syncGroupManualSource,_L:syncGroupSelectedSource,_Q:syncGroupQuality,_j:syncGroupLocalOscActiveW2C,_l:syncGroupLocalOscActive,_W:syncGroupAdminStatus,_X:syncGroupOperStatus,_g:syncGroupRingMode,_h:syncGroupLastChangeTime,_m:syncGroupManualSourceName,_r:syncGroupConfigurationMode,_AD:syncGroupStatus,_Al:syncGroupSourceSwitch,_Am:syncGroupSourceSwitchType,_An:syncGroupHoldover,_Ao:syncGroupQualityLevelSelectionMode,'syncSources':syncSources,'syncSourceTable':syncSourceTable,'syncSourceEntry':syncSourceEntry,_T:syncSourceIndex,_U:syncSourceName,_i:syncSourceId,_Z:syncSourceRxPort,_a:syncSourceTxPort,_b:syncSourceType,_V:syncSourceQuality,_c:syncSourcePriority,_d:syncSourceAdminStatus,_e:syncSourceOperStatus,_f:syncSourceIsSelected,_k:syncSourceAlwaysSendDoNotUse,_s:syncSourceStaticQuality,_t:syncSourceFilterState,'syncSourceMode':syncSourceMode,'syncSourceClearWaitToRestore':syncSourceClearWaitToRestore,_AE:syncSourceClockWanderExceeded,_AF:syncSourceNonSyncEClock,_Ap:syncSourceIfNo,_Aq:syncSourceUpPortId,_Ar:syncSourceLocalId,'lumentisSyncNotifications':lumentisSyncNotifications,'syncNotifyPrefix':syncNotifyPrefix,_As:syncGroupSourceChanged,'syncSubracks':syncSubracks,'syncSubrackTable':syncSubrackTable,'syncSubrackEntry':syncSubrackEntry,_p:syncSubrackIndex,_A9:syncSubrackName,_A8:syncSubrackSubrack,_AA:syncSubrackMasterBusA,_AB:syncSubrackMasterBusB,_AC:syncSubrackConfigureLocalBus,_AQ:syncSubrackGroupMasterBusA,_AR:syncSubrackGroupMasterBusB,'syncDomains':syncDomains,'syncDomainTable':syncDomainTable,'syncDomainEntry':syncDomainEntry,_A4:syncDomainIndex,_AT:syncDomainNumber,_AS:syncDomainName,_AU:syncDomainQualityLevelSelectionMode,_AV:syncDomainWaitToRestore,_AW:syncDomainHoldOff,_AX:syncDomainSource,_AY:syncDomainQuality,_AZ:syncDomainAssociateBoard,'syncBuses':syncBuses,'syncBusTable':syncBusTable,'syncBusEntry':syncBusEntry,_A5:syncBusIndex,_Aa:syncBusName,_Ab:syncBusSubrack,_Ac:syncBusDomain,_Ad:syncBusDomainIndex,_Ae:syncBusStaticMasterSlot,_Af:syncBusStaticMasterIndex,'syncBoardToDomain':syncBoardToDomain,'syncBoardToDomainTable':syncBoardToDomainTable,'syncBoardToDomainEntry':syncBoardToDomainEntry,_A6:syncBoardToDomainIndex,_Ag:syncBoardToDomainName,_Ah:syncBoardToDomainDomainIndex,_Ai:syncBoardToDomainDomainName,_Aj:syncBoardToDomainBoardIndex,_Ak:syncBoardToDomainBoardName})