_t='tmnxElmiEventGroup'
_s='tmnxElmiStatsGroup'
_r='tmnxElmiEvcConfigGroup'
_q='tmnxElmiIfConfigGroup'
_p='tmnxElmiTimeStampGroup'
_o='tmnxElmiEVCStatusChangeEvent'
_n='tmnxElmiIfStatusChangeEvent'
_m='tmnxElmiStatTxAsyncStatusMsgs'
_l='tmnxElmiStatInvRxSeqNumMsgs'
_k='tmnxElmiStatDiscardedMsgs'
_j='tmnxElmiStatTxStatusCheckTime'
_i='tmnxElmiStatRxStatusCheckTime'
_h='tmnxElmiStatTxStatusMsgs'
_g='tmnxElmiStatTxStatusMsgTime'
_f='tmnxElmiStatStatusEnqMsgTimeouts'
_e='tmnxElmiStatRxStatusEnqMsgs'
_d='tmnxElmiStatRxStatusEnqMsgTime'
_c='tmnxElmiEvcCfgStatusTimeStamp'
_b='tmnxElmiEvcCfgType'
_a='tmnxElmiEvcCfgIdentifier'
_Z='tmnxElmiIfCfgUniIdentifier'
_Y='tmnxElmiIfCfgUniType'
_X='tmnxElmiIfCfgT392'
_W='tmnxElmiIfCfgT391'
_V='tmnxElmiIfCfgN393'
_U='tmnxElmiIfCfgMode'
_T='tmnxElmiEvcCfgTableLastChanged'
_S='tmnxElmiIfConfigTableLastChanged'
_R='tmnxElmiStatEntry'
_Q='tmnxElmiIfConfigEntry'
_P='tmnxElmiEvcCfgVlanId'
_O='TmnxElmiIdentifierString'
_N='seconds'
_M='tmnxPortPortID'
_L='TIMETRA-PORT-MIB'
_K='tmnxChassisIndex'
_J='TIMETRA-CHASSIS-MIB'
_I='tmnxElmiEvcCfgStatus'
_H='tmnxElmiIfCfgStatus'
_G='Unsigned32'
_F='messages'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='TIMETRA-ELMI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
tmnxChassisIndex,=mibBuilder.importSymbols(_J,_K)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
tmnxPortEtherEntry,tmnxPortPortID=mibBuilder.importSymbols(_L,'tmnxPortEtherEntry',_M)
TmnxEncapVal,=mibBuilder.importSymbols('TIMETRA-TC-MIB','TmnxEncapVal')
tmnxElmiMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,68))
if mibBuilder.loadTexts:tmnxElmiMIBModule.setRevisions(('2008-10-23 00:00',))
class TmnxElmiIdentifierString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_TmnxElmiConformance_ObjectIdentity=ObjectIdentity
tmnxElmiConformance=_TmnxElmiConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,68))
_TmnxElmiCompliances_ObjectIdentity=ObjectIdentity
tmnxElmiCompliances=_TmnxElmiCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,68,1))
_TmnxElmiGroups_ObjectIdentity=ObjectIdentity
tmnxElmiGroups=_TmnxElmiGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,68,2))
_TmnxElmiObjs_ObjectIdentity=ObjectIdentity
tmnxElmiObjs=_TmnxElmiObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,68))
_TmnxElmiConfigurationTimeStamps_ObjectIdentity=ObjectIdentity
tmnxElmiConfigurationTimeStamps=_TmnxElmiConfigurationTimeStamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,68,0))
_TmnxElmiIfConfigTableLastChanged_Type=TimeStamp
_TmnxElmiIfConfigTableLastChanged_Object=MibScalar
tmnxElmiIfConfigTableLastChanged=_TmnxElmiIfConfigTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,68,0,1),_TmnxElmiIfConfigTableLastChanged_Type())
tmnxElmiIfConfigTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiIfConfigTableLastChanged.setStatus(_A)
_TmnxElmiEvcCfgTableLastChanged_Type=TimeStamp
_TmnxElmiEvcCfgTableLastChanged_Object=MibScalar
tmnxElmiEvcCfgTableLastChanged=_TmnxElmiEvcCfgTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,68,0,2),_TmnxElmiEvcCfgTableLastChanged_Type())
tmnxElmiEvcCfgTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiEvcCfgTableLastChanged.setStatus(_A)
_TmnxElmiConfigurations_ObjectIdentity=ObjectIdentity
tmnxElmiConfigurations=_TmnxElmiConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,68,1))
_TmnxElmiIfConfigTable_Object=MibTable
tmnxElmiIfConfigTable=_TmnxElmiIfConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1))
if mibBuilder.loadTexts:tmnxElmiIfConfigTable.setStatus(_A)
_TmnxElmiIfConfigEntry_Object=MibTableRow
tmnxElmiIfConfigEntry=_TmnxElmiIfConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1))
if mibBuilder.loadTexts:tmnxElmiIfConfigEntry.setStatus(_A)
class _TmnxElmiIfCfgMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('uniN',1),('uniC',2)))
_TmnxElmiIfCfgMode_Type.__name__=_D
_TmnxElmiIfCfgMode_Object=MibTableColumn
tmnxElmiIfCfgMode=_TmnxElmiIfCfgMode_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1,1),_TmnxElmiIfCfgMode_Type())
tmnxElmiIfCfgMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxElmiIfCfgMode.setStatus(_A)
class _TmnxElmiIfCfgStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_TmnxElmiIfCfgStatus_Type.__name__=_D
_TmnxElmiIfCfgStatus_Object=MibTableColumn
tmnxElmiIfCfgStatus=_TmnxElmiIfCfgStatus_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1,2),_TmnxElmiIfCfgStatus_Type())
tmnxElmiIfCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiIfCfgStatus.setStatus(_A)
class _TmnxElmiIfCfgN393_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_TmnxElmiIfCfgN393_Type.__name__=_G
_TmnxElmiIfCfgN393_Object=MibTableColumn
tmnxElmiIfCfgN393=_TmnxElmiIfCfgN393_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1,3),_TmnxElmiIfCfgN393_Type())
tmnxElmiIfCfgN393.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxElmiIfCfgN393.setStatus(_A)
class _TmnxElmiIfCfgT391_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_TmnxElmiIfCfgT391_Type.__name__=_G
_TmnxElmiIfCfgT391_Object=MibTableColumn
tmnxElmiIfCfgT391=_TmnxElmiIfCfgT391_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1,4),_TmnxElmiIfCfgT391_Type())
tmnxElmiIfCfgT391.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxElmiIfCfgT391.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiIfCfgT391.setUnits(_N)
class _TmnxElmiIfCfgT392_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_TmnxElmiIfCfgT392_Type.__name__=_G
_TmnxElmiIfCfgT392_Object=MibTableColumn
tmnxElmiIfCfgT392=_TmnxElmiIfCfgT392_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1,5),_TmnxElmiIfCfgT392_Type())
tmnxElmiIfCfgT392.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxElmiIfCfgT392.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiIfCfgT392.setUnits(_N)
class _TmnxElmiIfCfgUniType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notUsed',0),('allToOneBundling',1),('svcMultiplexNoBundling',2),('bundling',3)))
_TmnxElmiIfCfgUniType_Type.__name__=_D
_TmnxElmiIfCfgUniType_Object=MibTableColumn
tmnxElmiIfCfgUniType=_TmnxElmiIfCfgUniType_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1,6),_TmnxElmiIfCfgUniType_Type())
tmnxElmiIfCfgUniType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiIfCfgUniType.setStatus(_A)
class _TmnxElmiIfCfgUniIdentifier_Type(TmnxElmiIdentifierString):subtypeSpec=TmnxElmiIdentifierString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TmnxElmiIfCfgUniIdentifier_Type.__name__=_O
_TmnxElmiIfCfgUniIdentifier_Object=MibTableColumn
tmnxElmiIfCfgUniIdentifier=_TmnxElmiIfCfgUniIdentifier_Object((1,3,6,1,4,1,6527,3,1,2,68,1,1,1,7),_TmnxElmiIfCfgUniIdentifier_Type())
tmnxElmiIfCfgUniIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxElmiIfCfgUniIdentifier.setStatus(_A)
_TmnxElmiEvcConfigTable_Object=MibTable
tmnxElmiEvcConfigTable=_TmnxElmiEvcConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,68,1,2))
if mibBuilder.loadTexts:tmnxElmiEvcConfigTable.setStatus(_A)
_TmnxElmiEvcConfigEntry_Object=MibTableRow
tmnxElmiEvcConfigEntry=_TmnxElmiEvcConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,68,1,2,1))
tmnxElmiEvcConfigEntry.setIndexNames((0,_J,_K),(0,_L,_M),(0,_B,_P))
if mibBuilder.loadTexts:tmnxElmiEvcConfigEntry.setStatus(_A)
_TmnxElmiEvcCfgVlanId_Type=TmnxEncapVal
_TmnxElmiEvcCfgVlanId_Object=MibTableColumn
tmnxElmiEvcCfgVlanId=_TmnxElmiEvcCfgVlanId_Object((1,3,6,1,4,1,6527,3,1,2,68,1,2,1,1),_TmnxElmiEvcCfgVlanId_Type())
tmnxElmiEvcCfgVlanId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tmnxElmiEvcCfgVlanId.setStatus(_A)
_TmnxElmiEvcCfgIdentifier_Type=TmnxElmiIdentifierString
_TmnxElmiEvcCfgIdentifier_Object=MibTableColumn
tmnxElmiEvcCfgIdentifier=_TmnxElmiEvcCfgIdentifier_Object((1,3,6,1,4,1,6527,3,1,2,68,1,2,1,2),_TmnxElmiEvcCfgIdentifier_Type())
tmnxElmiEvcCfgIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxElmiEvcCfgIdentifier.setStatus(_A)
class _TmnxElmiEvcCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('p2p',0),('mp2mp',1)))
_TmnxElmiEvcCfgType_Type.__name__=_D
_TmnxElmiEvcCfgType_Object=MibTableColumn
tmnxElmiEvcCfgType=_TmnxElmiEvcCfgType_Object((1,3,6,1,4,1,6527,3,1,2,68,1,2,1,3),_TmnxElmiEvcCfgType_Type())
tmnxElmiEvcCfgType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiEvcCfgType.setStatus(_A)
class _TmnxElmiEvcCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('notActive',0),('newAndNotActive',1),('active',2),('newAndActive',3),('partiallyActive',4),('newAndPartiallyActive',5)))
_TmnxElmiEvcCfgStatus_Type.__name__=_D
_TmnxElmiEvcCfgStatus_Object=MibTableColumn
tmnxElmiEvcCfgStatus=_TmnxElmiEvcCfgStatus_Object((1,3,6,1,4,1,6527,3,1,2,68,1,2,1,4),_TmnxElmiEvcCfgStatus_Type())
tmnxElmiEvcCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiEvcCfgStatus.setStatus(_A)
_TmnxElmiEvcCfgStatusTimeStamp_Type=TimeStamp
_TmnxElmiEvcCfgStatusTimeStamp_Object=MibTableColumn
tmnxElmiEvcCfgStatusTimeStamp=_TmnxElmiEvcCfgStatusTimeStamp_Object((1,3,6,1,4,1,6527,3,1,2,68,1,2,1,5),_TmnxElmiEvcCfgStatusTimeStamp_Type())
tmnxElmiEvcCfgStatusTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiEvcCfgStatusTimeStamp.setStatus(_A)
_TmnxElmiStatistics_ObjectIdentity=ObjectIdentity
tmnxElmiStatistics=_TmnxElmiStatistics_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,68,2))
_TmnxElmiStatTable_Object=MibTable
tmnxElmiStatTable=_TmnxElmiStatTable_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1))
if mibBuilder.loadTexts:tmnxElmiStatTable.setStatus(_A)
_TmnxElmiStatEntry_Object=MibTableRow
tmnxElmiStatEntry=_TmnxElmiStatEntry_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1))
if mibBuilder.loadTexts:tmnxElmiStatEntry.setStatus(_A)
_TmnxElmiStatRxStatusEnqMsgTime_Type=TimeStamp
_TmnxElmiStatRxStatusEnqMsgTime_Object=MibTableColumn
tmnxElmiStatRxStatusEnqMsgTime=_TmnxElmiStatRxStatusEnqMsgTime_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,1),_TmnxElmiStatRxStatusEnqMsgTime_Type())
tmnxElmiStatRxStatusEnqMsgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatRxStatusEnqMsgTime.setStatus(_A)
_TmnxElmiStatRxStatusEnqMsgs_Type=Counter32
_TmnxElmiStatRxStatusEnqMsgs_Object=MibTableColumn
tmnxElmiStatRxStatusEnqMsgs=_TmnxElmiStatRxStatusEnqMsgs_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,2),_TmnxElmiStatRxStatusEnqMsgs_Type())
tmnxElmiStatRxStatusEnqMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatRxStatusEnqMsgs.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiStatRxStatusEnqMsgs.setUnits(_F)
_TmnxElmiStatStatusEnqMsgTimeouts_Type=Counter32
_TmnxElmiStatStatusEnqMsgTimeouts_Object=MibTableColumn
tmnxElmiStatStatusEnqMsgTimeouts=_TmnxElmiStatStatusEnqMsgTimeouts_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,3),_TmnxElmiStatStatusEnqMsgTimeouts_Type())
tmnxElmiStatStatusEnqMsgTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatStatusEnqMsgTimeouts.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiStatStatusEnqMsgTimeouts.setUnits(_F)
_TmnxElmiStatTxStatusMsgTime_Type=TimeStamp
_TmnxElmiStatTxStatusMsgTime_Object=MibTableColumn
tmnxElmiStatTxStatusMsgTime=_TmnxElmiStatTxStatusMsgTime_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,4),_TmnxElmiStatTxStatusMsgTime_Type())
tmnxElmiStatTxStatusMsgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatTxStatusMsgTime.setStatus(_A)
_TmnxElmiStatTxStatusMsgs_Type=Counter32
_TmnxElmiStatTxStatusMsgs_Object=MibTableColumn
tmnxElmiStatTxStatusMsgs=_TmnxElmiStatTxStatusMsgs_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,5),_TmnxElmiStatTxStatusMsgs_Type())
tmnxElmiStatTxStatusMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatTxStatusMsgs.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiStatTxStatusMsgs.setUnits(_F)
_TmnxElmiStatRxStatusCheckTime_Type=TimeStamp
_TmnxElmiStatRxStatusCheckTime_Object=MibTableColumn
tmnxElmiStatRxStatusCheckTime=_TmnxElmiStatRxStatusCheckTime_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,6),_TmnxElmiStatRxStatusCheckTime_Type())
tmnxElmiStatRxStatusCheckTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatRxStatusCheckTime.setStatus(_A)
_TmnxElmiStatTxStatusCheckTime_Type=TimeStamp
_TmnxElmiStatTxStatusCheckTime_Object=MibTableColumn
tmnxElmiStatTxStatusCheckTime=_TmnxElmiStatTxStatusCheckTime_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,7),_TmnxElmiStatTxStatusCheckTime_Type())
tmnxElmiStatTxStatusCheckTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatTxStatusCheckTime.setStatus(_A)
_TmnxElmiStatDiscardedMsgs_Type=Counter32
_TmnxElmiStatDiscardedMsgs_Object=MibTableColumn
tmnxElmiStatDiscardedMsgs=_TmnxElmiStatDiscardedMsgs_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,8),_TmnxElmiStatDiscardedMsgs_Type())
tmnxElmiStatDiscardedMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatDiscardedMsgs.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiStatDiscardedMsgs.setUnits(_F)
_TmnxElmiStatInvRxSeqNumMsgs_Type=Counter32
_TmnxElmiStatInvRxSeqNumMsgs_Object=MibTableColumn
tmnxElmiStatInvRxSeqNumMsgs=_TmnxElmiStatInvRxSeqNumMsgs_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,9),_TmnxElmiStatInvRxSeqNumMsgs_Type())
tmnxElmiStatInvRxSeqNumMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatInvRxSeqNumMsgs.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiStatInvRxSeqNumMsgs.setUnits(_F)
_TmnxElmiStatTxAsyncStatusMsgs_Type=Counter32
_TmnxElmiStatTxAsyncStatusMsgs_Object=MibTableColumn
tmnxElmiStatTxAsyncStatusMsgs=_TmnxElmiStatTxAsyncStatusMsgs_Object((1,3,6,1,4,1,6527,3,1,2,68,2,1,1,10),_TmnxElmiStatTxAsyncStatusMsgs_Type())
tmnxElmiStatTxAsyncStatusMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxElmiStatTxAsyncStatusMsgs.setStatus(_A)
if mibBuilder.loadTexts:tmnxElmiStatTxAsyncStatusMsgs.setUnits(_F)
_TmnxElmiNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxElmiNotifyPrefix=_TmnxElmiNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,68))
_TmnxElmiNotifications_ObjectIdentity=ObjectIdentity
tmnxElmiNotifications=_TmnxElmiNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,68,0))
tmnxPortEtherEntry.registerAugmentions((_B,_Q))
tmnxElmiIfConfigEntry.setIndexNames(*tmnxPortEtherEntry.getIndexNames())
tmnxElmiIfConfigEntry.registerAugmentions((_B,_R))
tmnxElmiStatEntry.setIndexNames(*tmnxElmiIfConfigEntry.getIndexNames())
tmnxElmiTimeStampGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,68,2,1))
tmnxElmiTimeStampGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:tmnxElmiTimeStampGroup.setStatus(_A)
tmnxElmiIfConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,68,2,2))
tmnxElmiIfConfigGroup.setObjects(*((_B,_U),(_B,_H),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:tmnxElmiIfConfigGroup.setStatus(_A)
tmnxElmiEvcConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,68,2,3))
tmnxElmiEvcConfigGroup.setObjects(*((_B,_a),(_B,_b),(_B,_I),(_B,_c)))
if mibBuilder.loadTexts:tmnxElmiEvcConfigGroup.setStatus(_A)
tmnxElmiStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,68,2,4))
tmnxElmiStatsGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:tmnxElmiStatsGroup.setStatus(_A)
tmnxElmiIfStatusChangeEvent=NotificationType((1,3,6,1,4,1,6527,3,1,3,68,0,1))
tmnxElmiIfStatusChangeEvent.setObjects((_B,_H))
if mibBuilder.loadTexts:tmnxElmiIfStatusChangeEvent.setStatus(_A)
tmnxElmiEVCStatusChangeEvent=NotificationType((1,3,6,1,4,1,6527,3,1,3,68,0,2))
tmnxElmiEVCStatusChangeEvent.setObjects((_B,_I))
if mibBuilder.loadTexts:tmnxElmiEVCStatusChangeEvent.setStatus(_A)
tmnxElmiEventGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,68,2,5))
tmnxElmiEventGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:tmnxElmiEventGroup.setStatus(_A)
tmnxElmiCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,68,1,1))
tmnxElmiCompliance.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:tmnxElmiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_O:TmnxElmiIdentifierString,'tmnxElmiMIBModule':tmnxElmiMIBModule,'tmnxElmiConformance':tmnxElmiConformance,'tmnxElmiCompliances':tmnxElmiCompliances,'tmnxElmiCompliance':tmnxElmiCompliance,'tmnxElmiGroups':tmnxElmiGroups,_p:tmnxElmiTimeStampGroup,_q:tmnxElmiIfConfigGroup,_r:tmnxElmiEvcConfigGroup,_s:tmnxElmiStatsGroup,_t:tmnxElmiEventGroup,'tmnxElmiObjs':tmnxElmiObjs,'tmnxElmiConfigurationTimeStamps':tmnxElmiConfigurationTimeStamps,_S:tmnxElmiIfConfigTableLastChanged,_T:tmnxElmiEvcCfgTableLastChanged,'tmnxElmiConfigurations':tmnxElmiConfigurations,'tmnxElmiIfConfigTable':tmnxElmiIfConfigTable,_Q:tmnxElmiIfConfigEntry,_U:tmnxElmiIfCfgMode,_H:tmnxElmiIfCfgStatus,_V:tmnxElmiIfCfgN393,_W:tmnxElmiIfCfgT391,_X:tmnxElmiIfCfgT392,_Y:tmnxElmiIfCfgUniType,_Z:tmnxElmiIfCfgUniIdentifier,'tmnxElmiEvcConfigTable':tmnxElmiEvcConfigTable,'tmnxElmiEvcConfigEntry':tmnxElmiEvcConfigEntry,_P:tmnxElmiEvcCfgVlanId,_a:tmnxElmiEvcCfgIdentifier,_b:tmnxElmiEvcCfgType,_I:tmnxElmiEvcCfgStatus,_c:tmnxElmiEvcCfgStatusTimeStamp,'tmnxElmiStatistics':tmnxElmiStatistics,'tmnxElmiStatTable':tmnxElmiStatTable,_R:tmnxElmiStatEntry,_d:tmnxElmiStatRxStatusEnqMsgTime,_e:tmnxElmiStatRxStatusEnqMsgs,_f:tmnxElmiStatStatusEnqMsgTimeouts,_g:tmnxElmiStatTxStatusMsgTime,_h:tmnxElmiStatTxStatusMsgs,_i:tmnxElmiStatRxStatusCheckTime,_j:tmnxElmiStatTxStatusCheckTime,_k:tmnxElmiStatDiscardedMsgs,_l:tmnxElmiStatInvRxSeqNumMsgs,_m:tmnxElmiStatTxAsyncStatusMsgs,'tmnxElmiNotifyPrefix':tmnxElmiNotifyPrefix,'tmnxElmiNotifications':tmnxElmiNotifications,_n:tmnxElmiIfStatusChangeEvent,_o:tmnxElmiEVCStatusChangeEvent})