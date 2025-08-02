_Ac='tmnxSasSapQosV2v0Group'
_Ab='tmnxSapGlobalV1v0Group'
_Aa='svcVplssvcBoundToIESSvc'
_AZ='svcVplsId'
_AY='sapIngQosMeterOperCIR'
_AX='sapIngQosMeterOperPIR'
_AW='sapIngQosMeterRateMode'
_AV='sapIngQosMeterAdminCIR'
_AU='sapIngQosMeterAdminPIR'
_AT='sapIngQosMeterPIRAdaptation'
_AS='sapIngQosMeterCIRAdaptation'
_AR='sapIngQosMeterAdminMBS'
_AQ='sapIngQosMeterAdminCBS'
_AP='sapIngQosMeterOverrideFlags'
_AO='sapIngQosMeterLastMgmtChange'
_AN='sapIngQosMeterRowStatus'
_AM='sapBaseInfoIngressAggShaperRatePIR'
_AL='sapBaseInfoIngressAggShaperRateCIR'
_AK='sapBaseInfoEthRingShgEnable'
_AJ='sapBaseInfoIngressFabricPath'
_AI='sapBaseInfoIngressCounterType'
_AH='svcEpipeType'
_AG='sapBaseInfoIngressStatsEnable'
_AF='sapBaseInfoEgressStatsEnable'
_AE='sapIngQosQueueStatsOutprofDroOcts'
_AD='sapIngQosQueueStatsOutprofDroPkts'
_AC='sapIngQosQueueStatsInprofDroOcts'
_AB='sapIngQosQueueStatsInprofDroPkts'
_AA='sapIngQosQueueStatsFwdOcts'
_A9='sapIngQosQueueStatsFwdPkts'
_A8='sapEgrQosQueueStatsOutprofDroOcts'
_A7='sapEgrQosQueueStatsOutprofDroPkts'
_A6='sapEgrQosQueueStatsInprofDroOcts'
_A5='sapEgrQosQueueStatsInprofDroPkts'
_A4='sapEgrQosQueueStatsFwdOcts'
_A3='sapEgrQosQueueStatsFwdPkts'
_A2='svcBaseInfoExtnEntry'
_A1='sapIngQosQueueInfoExtnEntry'
_A0='sapIngQosQueueStatsExtnEntry'
_z='sapEgrQosQueueStatsExtnEntry'
_y='sapBaseInfoExtnEntry'
_x='sapBaseStatsExtnEntry'
_w='accessible-for-notify'
_v='kilo bytes'
_u='sapIngQosMeterOvId'
_t='read-write'
_s='TSapAggShaperRatePIRsize'
_r='TSapAggShaperRateCIRsize'
_q='TSapIngressAggShaperRatePIRsize'
_p='TSapIngressAggShaperRateCIRsize'
_o='TSapIngressAggrMeterBurstSize'
_n='TWeight'
_m='TNamedItem'
_l='TLevelOrDefault'
_k='iesIfIndex'
_j='TMeterRateMode'
_i='sapPortId'
_h='sapEncapValue'
_g='sapBaseStatsIngressExtraTagDroppedOctets'
_f='sapBaseStatsIngressExtraTagDroppedPackets'
_e='sapBaseStatsEgressForwardedOctets'
_d='sapBaseStatsEgressForwardedPackets'
_c='sapBaseStatsIngressForwardedOctets'
_b='sapBaseStatsIngressForwardedPackets'
_a='svcCustomerVid'
_Z='svcUplinkType'
_Y='svcSapType'
_X='svcMtuCheck'
_W='sapBaseInfoIngressExtraTagDropCount'
_V='sapBaseInfoIngressWithAggregateMeter'
_U='sapBaseInfoIngressAggregateMeterBurst'
_T='sapBaseInfoIngressAggregateMeterRate'
_S='sapBaseInfoIngressCounterMode'
_R='sapBaseInfoEgressStatsPktsMode'
_Q='sapBaseStatsQosMetersUsed'
_P='sapBaseStatsQosClassifiersUsed'
_O='undefined'
_N='TAdaptationRule'
_M='TIMETRA-SERV-MIB'
_L='TIngressPIRRate'
_K='TIngressCIRRate'
_J='TIngressBurstSize'
_I='TIMETRA-SAP-MIB'
_H='kilo bits per second'
_G='kbps'
_F='TruthValue'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='TIMETRA-SAS-SERV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_F)
sapBaseInfoEntry,sapBaseStatsEntry,sapEgrQosQueueStatsEntry,sapEncapValue,sapIngQosQueueInfoEntry,sapIngQosQueueStatsEntry,sapPortId=mibBuilder.importSymbols(_I,'sapBaseInfoEntry','sapBaseStatsEntry','sapEgrQosQueueStatsEntry',_h,'sapIngQosQueueInfoEntry','sapIngQosQueueStatsEntry',_i)
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
TIngressBurstSize,TIngressCIRRate,TIngressPIRRate,TMeterMode,TMeterRateMode=mibBuilder.importSymbols('TIMETRA-SAS-QOS-MIB',_J,_K,_L,'TMeterMode',_j)
iesIfIndex,svcBaseInfoEntry,svcId=mibBuilder.importSymbols(_M,_k,'svcBaseInfoEntry','svcId')
TAdaptationRule,TLevelOrDefault,TNamedItem,TSapIngressMeterId,TWeight,TmnxServId=mibBuilder.importSymbols('TN-TC-MIB',_N,_l,_m,'TSapIngressMeterId',_n,'TmnxServId')
timetraSASServicesMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,9))
if mibBuilder.loadTexts:timetraSASServicesMIBModule.setRevisions(('1909-07-07 00:00',))
class TSapIngressAggrMeterBurstSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(4,2146959))
class TSapIngressAggShaperRateCIRsize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,20000000))
class TSapIngressAggShaperRatePIRsize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,20000000))
class TSapAggShaperRateCIRsize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,20000000))
class TSapAggShaperRatePIRsize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,20000000))
class TQosMeterAttribute(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('cbs',0),('cir',1),('cirAdaptRule',2),('mbs',3),('pir',4),('pirAdaptRule',5),('rateMode',6),('colorMode',7)))
_TmnxSASServConformance_ObjectIdentity=ObjectIdentity
tmnxSASServConformance=_TmnxSASServConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,5))
_TmnxSASSapConformance_ObjectIdentity=ObjectIdentity
tmnxSASSapConformance=_TmnxSASSapConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,5,1))
_TmnxSASSapCompliances_ObjectIdentity=ObjectIdentity
tmnxSASSapCompliances=_TmnxSASSapCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,5,1,1))
_TmnxSASSapGroups_ObjectIdentity=ObjectIdentity
tmnxSASSapGroups=_TmnxSASSapGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,5,1,2))
_TmnxSASServGroups_ObjectIdentity=ObjectIdentity
tmnxSASServGroups=_TmnxSASServGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,5,2))
_TmnxSASServObjs_ObjectIdentity=ObjectIdentity
tmnxSASServObjs=_TmnxSASServObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,8))
_TmnxSASSapObjs_ObjectIdentity=ObjectIdentity
tmnxSASSapObjs=_TmnxSASSapObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,8,1))
_SapBaseStatsExtnTable_Object=MibTable
sapBaseStatsExtnTable=_SapBaseStatsExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1))
if mibBuilder.loadTexts:sapBaseStatsExtnTable.setStatus(_A)
_SapBaseStatsExtnEntry_Object=MibTableRow
sapBaseStatsExtnEntry=_SapBaseStatsExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1))
if mibBuilder.loadTexts:sapBaseStatsExtnEntry.setStatus(_A)
_SapBaseStatsQosClassifiersUsed_Type=Unsigned32
_SapBaseStatsQosClassifiersUsed_Object=MibTableColumn
sapBaseStatsQosClassifiersUsed=_SapBaseStatsQosClassifiersUsed_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,1),_SapBaseStatsQosClassifiersUsed_Type())
sapBaseStatsQosClassifiersUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsQosClassifiersUsed.setStatus(_A)
_SapBaseStatsQosMetersUsed_Type=Unsigned32
_SapBaseStatsQosMetersUsed_Object=MibTableColumn
sapBaseStatsQosMetersUsed=_SapBaseStatsQosMetersUsed_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,2),_SapBaseStatsQosMetersUsed_Type())
sapBaseStatsQosMetersUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsQosMetersUsed.setStatus(_A)
_SapBaseStatsIngressForwardedPackets_Type=Counter64
_SapBaseStatsIngressForwardedPackets_Object=MibTableColumn
sapBaseStatsIngressForwardedPackets=_SapBaseStatsIngressForwardedPackets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,3),_SapBaseStatsIngressForwardedPackets_Type())
sapBaseStatsIngressForwardedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsIngressForwardedPackets.setStatus(_A)
_SapBaseStatsIngressForwardedOctets_Type=Counter64
_SapBaseStatsIngressForwardedOctets_Object=MibTableColumn
sapBaseStatsIngressForwardedOctets=_SapBaseStatsIngressForwardedOctets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,4),_SapBaseStatsIngressForwardedOctets_Type())
sapBaseStatsIngressForwardedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsIngressForwardedOctets.setStatus(_A)
_SapBaseStatsEgressForwardedPackets_Type=Counter64
_SapBaseStatsEgressForwardedPackets_Object=MibTableColumn
sapBaseStatsEgressForwardedPackets=_SapBaseStatsEgressForwardedPackets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,5),_SapBaseStatsEgressForwardedPackets_Type())
sapBaseStatsEgressForwardedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsEgressForwardedPackets.setStatus(_A)
_SapBaseStatsEgressForwardedOctets_Type=Counter64
_SapBaseStatsEgressForwardedOctets_Object=MibTableColumn
sapBaseStatsEgressForwardedOctets=_SapBaseStatsEgressForwardedOctets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,6),_SapBaseStatsEgressForwardedOctets_Type())
sapBaseStatsEgressForwardedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsEgressForwardedOctets.setStatus(_A)
_SapBaseStatsIngressExtraTagDroppedPackets_Type=Counter64
_SapBaseStatsIngressExtraTagDroppedPackets_Object=MibTableColumn
sapBaseStatsIngressExtraTagDroppedPackets=_SapBaseStatsIngressExtraTagDroppedPackets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,7),_SapBaseStatsIngressExtraTagDroppedPackets_Type())
sapBaseStatsIngressExtraTagDroppedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsIngressExtraTagDroppedPackets.setStatus(_A)
_SapBaseStatsIngressExtraTagDroppedOctets_Type=Counter64
_SapBaseStatsIngressExtraTagDroppedOctets_Object=MibTableColumn
sapBaseStatsIngressExtraTagDroppedOctets=_SapBaseStatsIngressExtraTagDroppedOctets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,8),_SapBaseStatsIngressExtraTagDroppedOctets_Type())
sapBaseStatsIngressExtraTagDroppedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsIngressExtraTagDroppedOctets.setStatus(_A)
_SapBaseStatsIngressDroppedPackets_Type=Counter64
_SapBaseStatsIngressDroppedPackets_Object=MibTableColumn
sapBaseStatsIngressDroppedPackets=_SapBaseStatsIngressDroppedPackets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,9),_SapBaseStatsIngressDroppedPackets_Type())
sapBaseStatsIngressDroppedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsIngressDroppedPackets.setStatus(_A)
_SapBaseStatsIngressDroppedOctets_Type=Counter64
_SapBaseStatsIngressDroppedOctets_Object=MibTableColumn
sapBaseStatsIngressDroppedOctets=_SapBaseStatsIngressDroppedOctets_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,1,1,10),_SapBaseStatsIngressDroppedOctets_Type())
sapBaseStatsIngressDroppedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:sapBaseStatsIngressDroppedOctets.setStatus(_A)
_SapBaseInfoExtnTable_Object=MibTable
sapBaseInfoExtnTable=_SapBaseInfoExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2))
if mibBuilder.loadTexts:sapBaseInfoExtnTable.setStatus(_A)
_SapBaseInfoExtnEntry_Object=MibTableRow
sapBaseInfoExtnEntry=_SapBaseInfoExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1))
if mibBuilder.loadTexts:sapBaseInfoExtnEntry.setStatus(_A)
class _SapBaseInfoEgressStatsPktsMode_Type(TruthValue):defaultValue=2
_SapBaseInfoEgressStatsPktsMode_Type.__name__=_F
_SapBaseInfoEgressStatsPktsMode_Object=MibTableColumn
sapBaseInfoEgressStatsPktsMode=_SapBaseInfoEgressStatsPktsMode_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,1),_SapBaseInfoEgressStatsPktsMode_Type())
sapBaseInfoEgressStatsPktsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoEgressStatsPktsMode.setStatus(_A)
class _SapBaseInfoIngressCounterMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('packet',1),('octet',2)))
_SapBaseInfoIngressCounterMode_Type.__name__=_E
_SapBaseInfoIngressCounterMode_Object=MibTableColumn
sapBaseInfoIngressCounterMode=_SapBaseInfoIngressCounterMode_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,2),_SapBaseInfoIngressCounterMode_Type())
sapBaseInfoIngressCounterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressCounterMode.setStatus(_A)
class _SapBaseInfoIngressAggregateMeterRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,20000000))
_SapBaseInfoIngressAggregateMeterRate_Type.__name__=_E
_SapBaseInfoIngressAggregateMeterRate_Object=MibTableColumn
sapBaseInfoIngressAggregateMeterRate=_SapBaseInfoIngressAggregateMeterRate_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,3),_SapBaseInfoIngressAggregateMeterRate_Type())
sapBaseInfoIngressAggregateMeterRate.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressAggregateMeterRate.setStatus(_A)
class _SapBaseInfoIngressAggregateMeterBurst_Type(TSapIngressAggrMeterBurstSize):defaultValue=-1
_SapBaseInfoIngressAggregateMeterBurst_Type.__name__=_o
_SapBaseInfoIngressAggregateMeterBurst_Object=MibTableColumn
sapBaseInfoIngressAggregateMeterBurst=_SapBaseInfoIngressAggregateMeterBurst_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,4),_SapBaseInfoIngressAggregateMeterBurst_Type())
sapBaseInfoIngressAggregateMeterBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressAggregateMeterBurst.setStatus(_A)
class _SapBaseInfoIngressWithAggregateMeter_Type(TruthValue):defaultValue=2
_SapBaseInfoIngressWithAggregateMeter_Type.__name__=_F
_SapBaseInfoIngressWithAggregateMeter_Object=MibTableColumn
sapBaseInfoIngressWithAggregateMeter=_SapBaseInfoIngressWithAggregateMeter_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,5),_SapBaseInfoIngressWithAggregateMeter_Type())
sapBaseInfoIngressWithAggregateMeter.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressWithAggregateMeter.setStatus(_A)
class _SapBaseInfoIngressExtraTagDropCount_Type(TruthValue):defaultValue=2
_SapBaseInfoIngressExtraTagDropCount_Type.__name__=_F
_SapBaseInfoIngressExtraTagDropCount_Object=MibTableColumn
sapBaseInfoIngressExtraTagDropCount=_SapBaseInfoIngressExtraTagDropCount_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,6),_SapBaseInfoIngressExtraTagDropCount_Type())
sapBaseInfoIngressExtraTagDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressExtraTagDropCount.setStatus(_A)
class _SapBaseInfoEgressStatsEnable_Type(TruthValue):defaultValue=2
_SapBaseInfoEgressStatsEnable_Type.__name__=_F
_SapBaseInfoEgressStatsEnable_Object=MibTableColumn
sapBaseInfoEgressStatsEnable=_SapBaseInfoEgressStatsEnable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,7),_SapBaseInfoEgressStatsEnable_Type())
sapBaseInfoEgressStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoEgressStatsEnable.setStatus(_A)
class _SapBaseInfoIngressStatsEnable_Type(TruthValue):defaultValue=2
_SapBaseInfoIngressStatsEnable_Type.__name__=_F
_SapBaseInfoIngressStatsEnable_Object=MibTableColumn
sapBaseInfoIngressStatsEnable=_SapBaseInfoIngressStatsEnable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,8),_SapBaseInfoIngressStatsEnable_Type())
sapBaseInfoIngressStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressStatsEnable.setStatus(_A)
class _SapBaseInfoIngressCounterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in-out-profile-count',1),('forward-drop-count',2)))
_SapBaseInfoIngressCounterType_Type.__name__=_E
_SapBaseInfoIngressCounterType_Object=MibTableColumn
sapBaseInfoIngressCounterType=_SapBaseInfoIngressCounterType_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,9),_SapBaseInfoIngressCounterType_Type())
sapBaseInfoIngressCounterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressCounterType.setStatus(_A)
class _SapBaseInfoIngressFabricPath_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SapBaseInfoIngressFabricPath_Type.__name__=_E
_SapBaseInfoIngressFabricPath_Object=MibTableColumn
sapBaseInfoIngressFabricPath=_SapBaseInfoIngressFabricPath_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,10),_SapBaseInfoIngressFabricPath_Type())
sapBaseInfoIngressFabricPath.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressFabricPath.setStatus(_A)
class _SapBaseInfoEthRingShgEnable_Type(TruthValue):defaultValue=2
_SapBaseInfoEthRingShgEnable_Type.__name__=_F
_SapBaseInfoEthRingShgEnable_Object=MibTableColumn
sapBaseInfoEthRingShgEnable=_SapBaseInfoEthRingShgEnable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,11),_SapBaseInfoEthRingShgEnable_Type())
sapBaseInfoEthRingShgEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoEthRingShgEnable.setStatus(_A)
class _SapBaseInfoIngressAggShaperRateCIR_Type(TSapIngressAggShaperRateCIRsize):defaultValue=0
_SapBaseInfoIngressAggShaperRateCIR_Type.__name__=_p
_SapBaseInfoIngressAggShaperRateCIR_Object=MibTableColumn
sapBaseInfoIngressAggShaperRateCIR=_SapBaseInfoIngressAggShaperRateCIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,12),_SapBaseInfoIngressAggShaperRateCIR_Type())
sapBaseInfoIngressAggShaperRateCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressAggShaperRateCIR.setStatus(_A)
if mibBuilder.loadTexts:sapBaseInfoIngressAggShaperRateCIR.setUnits(_G)
class _SapBaseInfoIngressAggShaperRatePIR_Type(TSapIngressAggShaperRatePIRsize):defaultValue=-1
_SapBaseInfoIngressAggShaperRatePIR_Type.__name__=_q
_SapBaseInfoIngressAggShaperRatePIR_Object=MibTableColumn
sapBaseInfoIngressAggShaperRatePIR=_SapBaseInfoIngressAggShaperRatePIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,13),_SapBaseInfoIngressAggShaperRatePIR_Type())
sapBaseInfoIngressAggShaperRatePIR.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoIngressAggShaperRatePIR.setStatus(_A)
if mibBuilder.loadTexts:sapBaseInfoIngressAggShaperRatePIR.setUnits(_G)
class _SapBaseInfoEgressAggShaperRateCIR_Type(TSapAggShaperRateCIRsize):defaultValue=0
_SapBaseInfoEgressAggShaperRateCIR_Type.__name__=_r
_SapBaseInfoEgressAggShaperRateCIR_Object=MibTableColumn
sapBaseInfoEgressAggShaperRateCIR=_SapBaseInfoEgressAggShaperRateCIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,14),_SapBaseInfoEgressAggShaperRateCIR_Type())
sapBaseInfoEgressAggShaperRateCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoEgressAggShaperRateCIR.setStatus(_A)
if mibBuilder.loadTexts:sapBaseInfoEgressAggShaperRateCIR.setUnits(_G)
class _SapBaseInfoEgressAggShaperRatePIR_Type(TSapAggShaperRatePIRsize):defaultValue=-1
_SapBaseInfoEgressAggShaperRatePIR_Type.__name__=_s
_SapBaseInfoEgressAggShaperRatePIR_Object=MibTableColumn
sapBaseInfoEgressAggShaperRatePIR=_SapBaseInfoEgressAggShaperRatePIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,15),_SapBaseInfoEgressAggShaperRatePIR_Type())
sapBaseInfoEgressAggShaperRatePIR.setMaxAccess(_C)
if mibBuilder.loadTexts:sapBaseInfoEgressAggShaperRatePIR.setStatus(_A)
if mibBuilder.loadTexts:sapBaseInfoEgressAggShaperRatePIR.setUnits(_G)
class _SapEgressAggRateLimitCIR_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_SapEgressAggRateLimitCIR_Type.__name__=_E
_SapEgressAggRateLimitCIR_Object=MibTableColumn
sapEgressAggRateLimitCIR=_SapEgressAggRateLimitCIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,16),_SapEgressAggRateLimitCIR_Type())
sapEgressAggRateLimitCIR.setMaxAccess(_t)
if mibBuilder.loadTexts:sapEgressAggRateLimitCIR.setStatus(_A)
class _SapEgressAggRateLimitPIR_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,10000000))
_SapEgressAggRateLimitPIR_Type.__name__=_E
_SapEgressAggRateLimitPIR_Object=MibTableColumn
sapEgressAggRateLimitPIR=_SapEgressAggRateLimitPIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,2,1,17),_SapEgressAggRateLimitPIR_Type())
sapEgressAggRateLimitPIR.setMaxAccess(_t)
if mibBuilder.loadTexts:sapEgressAggRateLimitPIR.setStatus(_A)
_SapEgrQosQueueStatsExtnTable_Object=MibTable
sapEgrQosQueueStatsExtnTable=_SapEgrQosQueueStatsExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3))
if mibBuilder.loadTexts:sapEgrQosQueueStatsExtnTable.setStatus(_A)
_SapEgrQosQueueStatsExtnEntry_Object=MibTableRow
sapEgrQosQueueStatsExtnEntry=_SapEgrQosQueueStatsExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3,1))
if mibBuilder.loadTexts:sapEgrQosQueueStatsExtnEntry.setStatus(_A)
_SapEgrQosQueueStatsFwdPkts_Type=Counter64
_SapEgrQosQueueStatsFwdPkts_Object=MibTableColumn
sapEgrQosQueueStatsFwdPkts=_SapEgrQosQueueStatsFwdPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3,1,1),_SapEgrQosQueueStatsFwdPkts_Type())
sapEgrQosQueueStatsFwdPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapEgrQosQueueStatsFwdPkts.setStatus(_A)
_SapEgrQosQueueStatsFwdOcts_Type=Counter64
_SapEgrQosQueueStatsFwdOcts_Object=MibTableColumn
sapEgrQosQueueStatsFwdOcts=_SapEgrQosQueueStatsFwdOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3,1,2),_SapEgrQosQueueStatsFwdOcts_Type())
sapEgrQosQueueStatsFwdOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapEgrQosQueueStatsFwdOcts.setStatus(_A)
_SapEgrQosQueueStatsInprofDroPkts_Type=Counter64
_SapEgrQosQueueStatsInprofDroPkts_Object=MibTableColumn
sapEgrQosQueueStatsInprofDroPkts=_SapEgrQosQueueStatsInprofDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3,1,3),_SapEgrQosQueueStatsInprofDroPkts_Type())
sapEgrQosQueueStatsInprofDroPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapEgrQosQueueStatsInprofDroPkts.setStatus(_A)
_SapEgrQosQueueStatsInprofDroOcts_Type=Counter64
_SapEgrQosQueueStatsInprofDroOcts_Object=MibTableColumn
sapEgrQosQueueStatsInprofDroOcts=_SapEgrQosQueueStatsInprofDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3,1,4),_SapEgrQosQueueStatsInprofDroOcts_Type())
sapEgrQosQueueStatsInprofDroOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapEgrQosQueueStatsInprofDroOcts.setStatus(_A)
_SapEgrQosQueueStatsOutprofDroPkts_Type=Counter64
_SapEgrQosQueueStatsOutprofDroPkts_Object=MibTableColumn
sapEgrQosQueueStatsOutprofDroPkts=_SapEgrQosQueueStatsOutprofDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3,1,5),_SapEgrQosQueueStatsOutprofDroPkts_Type())
sapEgrQosQueueStatsOutprofDroPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapEgrQosQueueStatsOutprofDroPkts.setStatus(_A)
_SapEgrQosQueueStatsOutprofDroOcts_Type=Counter64
_SapEgrQosQueueStatsOutprofDroOcts_Object=MibTableColumn
sapEgrQosQueueStatsOutprofDroOcts=_SapEgrQosQueueStatsOutprofDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,3,1,6),_SapEgrQosQueueStatsOutprofDroOcts_Type())
sapEgrQosQueueStatsOutprofDroOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapEgrQosQueueStatsOutprofDroOcts.setStatus(_A)
_SapIngQosQueueStatsExtnTable_Object=MibTable
sapIngQosQueueStatsExtnTable=_SapIngQosQueueStatsExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4))
if mibBuilder.loadTexts:sapIngQosQueueStatsExtnTable.setStatus(_A)
_SapIngQosQueueStatsExtnEntry_Object=MibTableRow
sapIngQosQueueStatsExtnEntry=_SapIngQosQueueStatsExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4,1))
if mibBuilder.loadTexts:sapIngQosQueueStatsExtnEntry.setStatus(_A)
_SapIngQosQueueStatsFwdPkts_Type=Counter64
_SapIngQosQueueStatsFwdPkts_Object=MibTableColumn
sapIngQosQueueStatsFwdPkts=_SapIngQosQueueStatsFwdPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4,1,1),_SapIngQosQueueStatsFwdPkts_Type())
sapIngQosQueueStatsFwdPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosQueueStatsFwdPkts.setStatus(_A)
_SapIngQosQueueStatsFwdOcts_Type=Counter64
_SapIngQosQueueStatsFwdOcts_Object=MibTableColumn
sapIngQosQueueStatsFwdOcts=_SapIngQosQueueStatsFwdOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4,1,2),_SapIngQosQueueStatsFwdOcts_Type())
sapIngQosQueueStatsFwdOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosQueueStatsFwdOcts.setStatus(_A)
_SapIngQosQueueStatsInprofDroPkts_Type=Counter64
_SapIngQosQueueStatsInprofDroPkts_Object=MibTableColumn
sapIngQosQueueStatsInprofDroPkts=_SapIngQosQueueStatsInprofDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4,1,3),_SapIngQosQueueStatsInprofDroPkts_Type())
sapIngQosQueueStatsInprofDroPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosQueueStatsInprofDroPkts.setStatus(_A)
_SapIngQosQueueStatsInprofDroOcts_Type=Counter64
_SapIngQosQueueStatsInprofDroOcts_Object=MibTableColumn
sapIngQosQueueStatsInprofDroOcts=_SapIngQosQueueStatsInprofDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4,1,4),_SapIngQosQueueStatsInprofDroOcts_Type())
sapIngQosQueueStatsInprofDroOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosQueueStatsInprofDroOcts.setStatus(_A)
_SapIngQosQueueStatsOutprofDroPkts_Type=Counter64
_SapIngQosQueueStatsOutprofDroPkts_Object=MibTableColumn
sapIngQosQueueStatsOutprofDroPkts=_SapIngQosQueueStatsOutprofDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4,1,5),_SapIngQosQueueStatsOutprofDroPkts_Type())
sapIngQosQueueStatsOutprofDroPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosQueueStatsOutprofDroPkts.setStatus(_A)
_SapIngQosQueueStatsOutprofDroOcts_Type=Counter64
_SapIngQosQueueStatsOutprofDroOcts_Object=MibTableColumn
sapIngQosQueueStatsOutprofDroOcts=_SapIngQosQueueStatsOutprofDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,4,1,6),_SapIngQosQueueStatsOutprofDroOcts_Type())
sapIngQosQueueStatsOutprofDroOcts.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosQueueStatsOutprofDroOcts.setStatus(_A)
_SapIngQosMeterInfoTable_Object=MibTable
sapIngQosMeterInfoTable=_SapIngQosMeterInfoTable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5))
if mibBuilder.loadTexts:sapIngQosMeterInfoTable.setStatus(_A)
_SapIngQosMeterInfoEntry_Object=MibTableRow
sapIngQosMeterInfoEntry=_SapIngQosMeterInfoEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1))
sapIngQosMeterInfoEntry.setIndexNames((0,_M,'svcId'),(0,_I,_i),(0,_I,_h),(0,_B,_u))
if mibBuilder.loadTexts:sapIngQosMeterInfoEntry.setStatus(_A)
_SapIngQosMeterOvId_Type=TSapIngressMeterId
_SapIngQosMeterOvId_Object=MibTableColumn
sapIngQosMeterOvId=_SapIngQosMeterOvId_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,1),_SapIngQosMeterOvId_Type())
sapIngQosMeterOvId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:sapIngQosMeterOvId.setStatus(_A)
_SapIngQosMeterRowStatus_Type=RowStatus
_SapIngQosMeterRowStatus_Object=MibTableColumn
sapIngQosMeterRowStatus=_SapIngQosMeterRowStatus_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,2),_SapIngQosMeterRowStatus_Type())
sapIngQosMeterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterRowStatus.setStatus(_A)
_SapIngQosMeterLastMgmtChange_Type=TimeStamp
_SapIngQosMeterLastMgmtChange_Object=MibTableColumn
sapIngQosMeterLastMgmtChange=_SapIngQosMeterLastMgmtChange_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,3),_SapIngQosMeterLastMgmtChange_Type())
sapIngQosMeterLastMgmtChange.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosMeterLastMgmtChange.setStatus(_A)
_SapIngQosMeterOverrideFlags_Type=TQosMeterAttribute
_SapIngQosMeterOverrideFlags_Object=MibTableColumn
sapIngQosMeterOverrideFlags=_SapIngQosMeterOverrideFlags_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,4),_SapIngQosMeterOverrideFlags_Type())
sapIngQosMeterOverrideFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterOverrideFlags.setStatus(_A)
class _SapIngQosMeterAdminCBS_Type(TIngressBurstSize):defaultValue=-1
_SapIngQosMeterAdminCBS_Type.__name__=_J
_SapIngQosMeterAdminCBS_Object=MibTableColumn
sapIngQosMeterAdminCBS=_SapIngQosMeterAdminCBS_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,5),_SapIngQosMeterAdminCBS_Type())
sapIngQosMeterAdminCBS.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterAdminCBS.setStatus(_A)
if mibBuilder.loadTexts:sapIngQosMeterAdminCBS.setUnits(_v)
class _SapIngQosMeterAdminMBS_Type(TIngressBurstSize):defaultValue=-1
_SapIngQosMeterAdminMBS_Type.__name__=_J
_SapIngQosMeterAdminMBS_Object=MibTableColumn
sapIngQosMeterAdminMBS=_SapIngQosMeterAdminMBS_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,6),_SapIngQosMeterAdminMBS_Type())
sapIngQosMeterAdminMBS.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterAdminMBS.setStatus(_A)
if mibBuilder.loadTexts:sapIngQosMeterAdminMBS.setUnits(_v)
class _SapIngQosMeterCIRAdaptation_Type(TAdaptationRule):defaultValue=3
_SapIngQosMeterCIRAdaptation_Type.__name__=_N
_SapIngQosMeterCIRAdaptation_Object=MibTableColumn
sapIngQosMeterCIRAdaptation=_SapIngQosMeterCIRAdaptation_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,7),_SapIngQosMeterCIRAdaptation_Type())
sapIngQosMeterCIRAdaptation.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterCIRAdaptation.setStatus(_A)
class _SapIngQosMeterPIRAdaptation_Type(TAdaptationRule):defaultValue=3
_SapIngQosMeterPIRAdaptation_Type.__name__=_N
_SapIngQosMeterPIRAdaptation_Object=MibTableColumn
sapIngQosMeterPIRAdaptation=_SapIngQosMeterPIRAdaptation_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,8),_SapIngQosMeterPIRAdaptation_Type())
sapIngQosMeterPIRAdaptation.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterPIRAdaptation.setStatus(_A)
class _SapIngQosMeterAdminPIR_Type(TIngressPIRRate):defaultValue=-1
_SapIngQosMeterAdminPIR_Type.__name__=_L
_SapIngQosMeterAdminPIR_Object=MibTableColumn
sapIngQosMeterAdminPIR=_SapIngQosMeterAdminPIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,9),_SapIngQosMeterAdminPIR_Type())
sapIngQosMeterAdminPIR.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterAdminPIR.setStatus(_A)
if mibBuilder.loadTexts:sapIngQosMeterAdminPIR.setUnits(_H)
class _SapIngQosMeterAdminCIR_Type(TIngressCIRRate):defaultValue=-1
_SapIngQosMeterAdminCIR_Type.__name__=_K
_SapIngQosMeterAdminCIR_Object=MibTableColumn
sapIngQosMeterAdminCIR=_SapIngQosMeterAdminCIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,10),_SapIngQosMeterAdminCIR_Type())
sapIngQosMeterAdminCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterAdminCIR.setStatus(_A)
if mibBuilder.loadTexts:sapIngQosMeterAdminCIR.setUnits(_H)
class _SapIngQosMeterRateMode_Type(TMeterRateMode):defaultValue=3
_SapIngQosMeterRateMode_Type.__name__=_j
_SapIngQosMeterRateMode_Object=MibTableColumn
sapIngQosMeterRateMode=_SapIngQosMeterRateMode_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,11),_SapIngQosMeterRateMode_Type())
sapIngQosMeterRateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterRateMode.setStatus(_A)
class _SapIngQosMeterOperPIR_Type(TIngressPIRRate):defaultValue=-1
_SapIngQosMeterOperPIR_Type.__name__=_L
_SapIngQosMeterOperPIR_Object=MibTableColumn
sapIngQosMeterOperPIR=_SapIngQosMeterOperPIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,12),_SapIngQosMeterOperPIR_Type())
sapIngQosMeterOperPIR.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosMeterOperPIR.setStatus(_A)
if mibBuilder.loadTexts:sapIngQosMeterOperPIR.setUnits(_H)
class _SapIngQosMeterOperCIR_Type(TIngressCIRRate):defaultValue=-1
_SapIngQosMeterOperCIR_Type.__name__=_K
_SapIngQosMeterOperCIR_Object=MibTableColumn
sapIngQosMeterOperCIR=_SapIngQosMeterOperCIR_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,13),_SapIngQosMeterOperCIR_Type())
sapIngQosMeterOperCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:sapIngQosMeterOperCIR.setStatus(_A)
if mibBuilder.loadTexts:sapIngQosMeterOperCIR.setUnits(_H)
class _SapIngQosMeterRateColorMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('color-aware',1),('color-blind',2)))
_SapIngQosMeterRateColorMode_Type.__name__=_E
_SapIngQosMeterRateColorMode_Object=MibTableColumn
sapIngQosMeterRateColorMode=_SapIngQosMeterRateColorMode_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,5,1,14),_SapIngQosMeterRateColorMode_Type())
sapIngQosMeterRateColorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosMeterRateColorMode.setStatus(_A)
_SapIngQosQueueInfoExtnTable_Object=MibTable
sapIngQosQueueInfoExtnTable=_SapIngQosQueueInfoExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,6))
if mibBuilder.loadTexts:sapIngQosQueueInfoExtnTable.setStatus(_A)
_SapIngQosQueueInfoExtnEntry_Object=MibTableRow
sapIngQosQueueInfoExtnEntry=_SapIngQosQueueInfoExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,6,1))
if mibBuilder.loadTexts:sapIngQosQueueInfoExtnEntry.setStatus(_A)
class _SapIngQosQPolicyName_Type(TNamedItem):defaultValue=OctetString('default')
_SapIngQosQPolicyName_Type.__name__=_m
_SapIngQosQPolicyName_Object=MibTableColumn
sapIngQosQPolicyName=_SapIngQosQPolicyName_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,6,1,1),_SapIngQosQPolicyName_Type())
sapIngQosQPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosQPolicyName.setStatus(_A)
class _SapIngQosQPIRWeight_Type(TWeight):defaultValue=1
_SapIngQosQPIRWeight_Type.__name__=_n
_SapIngQosQPIRWeight_Object=MibTableColumn
sapIngQosQPIRWeight=_SapIngQosQPIRWeight_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,6,1,2),_SapIngQosQPIRWeight_Type())
sapIngQosQPIRWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosQPIRWeight.setStatus(_A)
class _SapIngQosQCIRLevel_Type(TLevelOrDefault):defaultValue=0
_SapIngQosQCIRLevel_Type.__name__=_l
_SapIngQosQCIRLevel_Object=MibTableColumn
sapIngQosQCIRLevel=_SapIngQosQCIRLevel_Object((1,3,6,1,4,1,6527,6,2,2,2,8,1,6,1,3),_SapIngQosQCIRLevel_Type())
sapIngQosQCIRLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sapIngQosQCIRLevel.setStatus(_A)
_TmnxSASSvcObjs_ObjectIdentity=ObjectIdentity
tmnxSASSvcObjs=_TmnxSASSvcObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,8,2))
_SvcBaseInfoExtnTable_Object=MibTable
svcBaseInfoExtnTable=_SvcBaseInfoExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1))
if mibBuilder.loadTexts:svcBaseInfoExtnTable.setStatus(_A)
_SvcBaseInfoExtnEntry_Object=MibTableRow
svcBaseInfoExtnEntry=_SvcBaseInfoExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1))
if mibBuilder.loadTexts:svcBaseInfoExtnEntry.setStatus(_A)
class _SvcMtuCheck_Type(TruthValue):defaultValue=1
_SvcMtuCheck_Type.__name__=_F
_SvcMtuCheck_Object=MibTableColumn
svcMtuCheck=_SvcMtuCheck_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1,1),_SvcMtuCheck_Type())
svcMtuCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:svcMtuCheck.setStatus(_A)
class _SvcSapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_O,0),('null-star',1),('dot1q',2),('dot1q-preserve',3),('any',4),('dot1q-range',5),('qinq-inner-tag-preserve',6)))
_SvcSapType_Type.__name__=_E
_SvcSapType_Object=MibTableColumn
svcSapType=_SvcSapType_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1,2),_SvcSapType_Type())
svcSapType.setMaxAccess(_C)
if mibBuilder.loadTexts:svcSapType.setStatus(_A)
class _SvcUplinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('l2',1),('mpls',2)))
_SvcUplinkType_Type.__name__=_E
_SvcUplinkType_Object=MibTableColumn
svcUplinkType=_SvcUplinkType_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1,3),_SvcUplinkType_Type())
svcUplinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:svcUplinkType.setStatus(_A)
class _SvcCustomerVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SvcCustomerVid_Type.__name__=_E
_SvcCustomerVid_Object=MibTableColumn
svcCustomerVid=_SvcCustomerVid_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1,4),_SvcCustomerVid_Type())
svcCustomerVid.setMaxAccess(_C)
if mibBuilder.loadTexts:svcCustomerVid.setStatus(_A)
class _SvcEpipeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('pbbepipe',2)))
_SvcEpipeType_Type.__name__=_E
_SvcEpipeType_Object=MibTableColumn
svcEpipeType=_SvcEpipeType_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1,5),_SvcEpipeType_Type())
svcEpipeType.setMaxAccess(_C)
if mibBuilder.loadTexts:svcEpipeType.setStatus(_A)
class _SvcAllowL2ptXstpBpdu_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('enable',1),('disable',2)))
_SvcAllowL2ptXstpBpdu_Type.__name__=_E
_SvcAllowL2ptXstpBpdu_Object=MibTableColumn
svcAllowL2ptXstpBpdu=_SvcAllowL2ptXstpBpdu_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1,6),_SvcAllowL2ptXstpBpdu_Type())
svcAllowL2ptXstpBpdu.setMaxAccess(_C)
if mibBuilder.loadTexts:svcAllowL2ptXstpBpdu.setStatus(_A)
class _SvcbVplsVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SvcbVplsVid_Type.__name__=_E
_SvcbVplsVid_Object=MibTableColumn
svcbVplsVid=_SvcbVplsVid_Object((1,3,6,1,4,1,6527,6,2,2,2,8,2,1,1,7),_SvcbVplsVid_Type())
svcbVplsVid.setMaxAccess(_C)
if mibBuilder.loadTexts:svcbVplsVid.setStatus(_A)
_TmnxSASSvcTraps_ObjectIdentity=ObjectIdentity
tmnxSASSvcTraps=_TmnxSASSvcTraps_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,8,3))
_TmnxSASSvcNotifyObjs_ObjectIdentity=ObjectIdentity
tmnxSASSvcNotifyObjs=_TmnxSASSvcNotifyObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,8,4))
_SvcVplsId_Type=TmnxServId
_SvcVplsId_Object=MibScalar
svcVplsId=_SvcVplsId_Object((1,3,6,1,4,1,6527,6,2,2,2,8,4,1),_SvcVplsId_Type())
svcVplsId.setMaxAccess(_w)
if mibBuilder.loadTexts:svcVplsId.setStatus(_A)
_SvcIesId_Type=TmnxServId
_SvcIesId_Object=MibScalar
svcIesId=_SvcIesId_Object((1,3,6,1,4,1,6527,6,2,2,2,8,4,2),_SvcIesId_Type())
svcIesId.setMaxAccess(_w)
if mibBuilder.loadTexts:svcIesId.setStatus(_A)
sapBaseStatsEntry.registerAugmentions((_B,_x))
sapBaseStatsExtnEntry.setIndexNames(*sapBaseStatsEntry.getIndexNames())
sapBaseInfoEntry.registerAugmentions((_B,_y))
sapBaseInfoExtnEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
sapEgrQosQueueStatsEntry.registerAugmentions((_B,_z))
sapEgrQosQueueStatsExtnEntry.setIndexNames(*sapEgrQosQueueStatsEntry.getIndexNames())
sapIngQosQueueStatsEntry.registerAugmentions((_B,_A0))
sapIngQosQueueStatsExtnEntry.setIndexNames(*sapIngQosQueueStatsEntry.getIndexNames())
sapIngQosQueueInfoEntry.registerAugmentions((_B,_A1))
sapIngQosQueueInfoExtnEntry.setIndexNames(*sapIngQosQueueInfoEntry.getIndexNames())
svcBaseInfoEntry.registerAugmentions((_B,_A2))
svcBaseInfoExtnEntry.setIndexNames(*svcBaseInfoEntry.getIndexNames())
tmnxSapGlobalV1v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,5,1,2,28))
tmnxSapGlobalV1v0Group.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:tmnxSapGlobalV1v0Group.setStatus(_A)
tmnxSasSapQosV2v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,5,1,2,29))
tmnxSasSapQosV2v0Group.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:tmnxSasSapQosV2v0Group.setStatus(_A)
tmnxSapGlobalV3v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,5,1,2,30))
tmnxSapGlobalV3v0Group.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_AF),(_B,_AG),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_AH),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:tmnxSapGlobalV3v0Group.setStatus(_A)
tmnxSapGlobalV4v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,5,1,2,31))
tmnxSapGlobalV4v0Group.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:tmnxSapGlobalV4v0Group.setStatus(_A)
tmnxSapGlobalV5v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,5,1,2,32))
tmnxSapGlobalV5v0Group.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:tmnxSapGlobalV5v0Group.setStatus(_A)
svcVplssvcBoundToIESSvc=NotificationType((1,3,6,1,4,1,6527,6,2,2,2,8,3,1))
svcVplssvcBoundToIESSvc.setObjects(*((_B,_AZ),(_B,'svcIesId'),(_M,_k)))
if mibBuilder.loadTexts:svcVplssvcBoundToIESSvc.setStatus(_A)
tmnxSASSvcNotifyGroup=NotificationGroup((1,3,6,1,4,1,6527,6,2,2,1,5,2,1))
tmnxSASSvcNotifyGroup.setObjects((_B,_Aa))
if mibBuilder.loadTexts:tmnxSASSvcNotifyGroup.setStatus(_A)
tmnxSap72100V1v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,6,2,2,1,5,1,1,1))
tmnxSap72100V1v0Compliance.setObjects(*((_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:tmnxSap72100V1v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_o:TSapIngressAggrMeterBurstSize,_p:TSapIngressAggShaperRateCIRsize,_q:TSapIngressAggShaperRatePIRsize,_r:TSapAggShaperRateCIRsize,_s:TSapAggShaperRatePIRsize,'TQosMeterAttribute':TQosMeterAttribute,'timetraSASServicesMIBModule':timetraSASServicesMIBModule,'tmnxSASServConformance':tmnxSASServConformance,'tmnxSASSapConformance':tmnxSASSapConformance,'tmnxSASSapCompliances':tmnxSASSapCompliances,'tmnxSap72100V1v0Compliance':tmnxSap72100V1v0Compliance,'tmnxSASSapGroups':tmnxSASSapGroups,_Ab:tmnxSapGlobalV1v0Group,_Ac:tmnxSasSapQosV2v0Group,'tmnxSapGlobalV3v0Group':tmnxSapGlobalV3v0Group,'tmnxSapGlobalV4v0Group':tmnxSapGlobalV4v0Group,'tmnxSapGlobalV5v0Group':tmnxSapGlobalV5v0Group,'tmnxSASServGroups':tmnxSASServGroups,'tmnxSASSvcNotifyGroup':tmnxSASSvcNotifyGroup,'tmnxSASServObjs':tmnxSASServObjs,'tmnxSASSapObjs':tmnxSASSapObjs,'sapBaseStatsExtnTable':sapBaseStatsExtnTable,_x:sapBaseStatsExtnEntry,_P:sapBaseStatsQosClassifiersUsed,_Q:sapBaseStatsQosMetersUsed,_b:sapBaseStatsIngressForwardedPackets,_c:sapBaseStatsIngressForwardedOctets,_d:sapBaseStatsEgressForwardedPackets,_e:sapBaseStatsEgressForwardedOctets,_f:sapBaseStatsIngressExtraTagDroppedPackets,_g:sapBaseStatsIngressExtraTagDroppedOctets,'sapBaseStatsIngressDroppedPackets':sapBaseStatsIngressDroppedPackets,'sapBaseStatsIngressDroppedOctets':sapBaseStatsIngressDroppedOctets,'sapBaseInfoExtnTable':sapBaseInfoExtnTable,_y:sapBaseInfoExtnEntry,_R:sapBaseInfoEgressStatsPktsMode,_S:sapBaseInfoIngressCounterMode,_T:sapBaseInfoIngressAggregateMeterRate,_U:sapBaseInfoIngressAggregateMeterBurst,_V:sapBaseInfoIngressWithAggregateMeter,_W:sapBaseInfoIngressExtraTagDropCount,_AF:sapBaseInfoEgressStatsEnable,_AG:sapBaseInfoIngressStatsEnable,_AI:sapBaseInfoIngressCounterType,_AJ:sapBaseInfoIngressFabricPath,_AK:sapBaseInfoEthRingShgEnable,_AL:sapBaseInfoIngressAggShaperRateCIR,_AM:sapBaseInfoIngressAggShaperRatePIR,'sapBaseInfoEgressAggShaperRateCIR':sapBaseInfoEgressAggShaperRateCIR,'sapBaseInfoEgressAggShaperRatePIR':sapBaseInfoEgressAggShaperRatePIR,'sapEgressAggRateLimitCIR':sapEgressAggRateLimitCIR,'sapEgressAggRateLimitPIR':sapEgressAggRateLimitPIR,'sapEgrQosQueueStatsExtnTable':sapEgrQosQueueStatsExtnTable,_z:sapEgrQosQueueStatsExtnEntry,_A3:sapEgrQosQueueStatsFwdPkts,_A4:sapEgrQosQueueStatsFwdOcts,_A5:sapEgrQosQueueStatsInprofDroPkts,_A6:sapEgrQosQueueStatsInprofDroOcts,_A7:sapEgrQosQueueStatsOutprofDroPkts,_A8:sapEgrQosQueueStatsOutprofDroOcts,'sapIngQosQueueStatsExtnTable':sapIngQosQueueStatsExtnTable,_A0:sapIngQosQueueStatsExtnEntry,_A9:sapIngQosQueueStatsFwdPkts,_AA:sapIngQosQueueStatsFwdOcts,_AB:sapIngQosQueueStatsInprofDroPkts,_AC:sapIngQosQueueStatsInprofDroOcts,_AD:sapIngQosQueueStatsOutprofDroPkts,_AE:sapIngQosQueueStatsOutprofDroOcts,'sapIngQosMeterInfoTable':sapIngQosMeterInfoTable,'sapIngQosMeterInfoEntry':sapIngQosMeterInfoEntry,_u:sapIngQosMeterOvId,_AN:sapIngQosMeterRowStatus,_AO:sapIngQosMeterLastMgmtChange,_AP:sapIngQosMeterOverrideFlags,_AQ:sapIngQosMeterAdminCBS,_AR:sapIngQosMeterAdminMBS,_AS:sapIngQosMeterCIRAdaptation,_AT:sapIngQosMeterPIRAdaptation,_AU:sapIngQosMeterAdminPIR,_AV:sapIngQosMeterAdminCIR,_AW:sapIngQosMeterRateMode,_AX:sapIngQosMeterOperPIR,_AY:sapIngQosMeterOperCIR,'sapIngQosMeterRateColorMode':sapIngQosMeterRateColorMode,'sapIngQosQueueInfoExtnTable':sapIngQosQueueInfoExtnTable,_A1:sapIngQosQueueInfoExtnEntry,'sapIngQosQPolicyName':sapIngQosQPolicyName,'sapIngQosQPIRWeight':sapIngQosQPIRWeight,'sapIngQosQCIRLevel':sapIngQosQCIRLevel,'tmnxSASSvcObjs':tmnxSASSvcObjs,'svcBaseInfoExtnTable':svcBaseInfoExtnTable,_A2:svcBaseInfoExtnEntry,_X:svcMtuCheck,_Y:svcSapType,_Z:svcUplinkType,_a:svcCustomerVid,_AH:svcEpipeType,'svcAllowL2ptXstpBpdu':svcAllowL2ptXstpBpdu,'svcbVplsVid':svcbVplsVid,'tmnxSASSvcTraps':tmnxSASSvcTraps,_Aa:svcVplssvcBoundToIESSvc,'tmnxSASSvcNotifyObjs':tmnxSASSvcNotifyObjs,_AZ:svcVplsId,'svcIesId':svcIesId})