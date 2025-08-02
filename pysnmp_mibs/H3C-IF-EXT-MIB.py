_AE='h3cIfPfcDot1pInPpsThreshold'
_AD='h3cIfPfcDot1pInPps'
_AC='h3cIfPfcDot1pOutPpsThreshold'
_AB='h3cIfPfcDot1pOutPps'
_AA='h3cIfDiscardPktRateUpperLimit'
_A9='h3cIfDiscardPktRate'
_A8='h3cIfBandwidthUpperLimit'
_A7='h3cIfBandwidthRate'
_A6='h3cIfUsingIndex'
_A5='h3cIfPortTypeIndex'
_A4='h3cIfLinkModeIndex'
_A3='h3cRTSubIfOrdinal'
_A2='h3cRTSubIfParentIfIndex'
_A1='h3cRTParentIfIndex'
_A0='h3cIfMonTxPauseFrameInterval'
_z='h3cIfMonTxPauseFrameStatistics'
_y='h3cIfMonTxPauseFrameLowThres'
_x='h3cIfMonTxPauseFrameHighThres'
_w='h3cIfMonPauseFrameInterval'
_v='h3cIfMonPauseFrameStatistics'
_u='h3cIfMonPauseFrameLowThres'
_t='h3cIfMonPauseFrameHighThres'
_s='h3cIfMonCRCErrType'
_r='h3cIfMonCRCErrorInterval'
_q='h3cIfMonCRCErrorStatistics'
_p='h3cIfMonCRCErrorLowThres'
_o='h3cIfMonCRCErrorHighThres'
_n='h3cIfMonSdhB2ErrorInterval'
_m='h3cIfMonSdhB2ErrorStatistics'
_l='h3cIfMonSdhB2ErrorHighThres'
_k='h3cIfMonSdhB2ErrorLowThres'
_j='h3cIfMonSdhB1ErrorInterval'
_i='h3cIfMonSdhB1ErrorStatistics'
_h='h3cIfMonSdhB1ErrorHighThres'
_g='h3cIfMonSdhB1ErrorLowThres'
_f='h3cIfMonSdhErrorInterval'
_e='h3cIfMonSdhErrorStatistics'
_d='h3cIfMonSdhErrorHighThres'
_c='h3cIfMonSdhErrorLowThres'
_b='h3cIfMonOutputErrorAlarmInterval'
_a='h3cIfMonOutputErrorAlarmStatistics'
_Z='h3cIfMonOutputErrorAlarmLowThres'
_Y='h3cIfMonOutputErrorAlarmHighThres'
_X='h3cIfMonInputErrorAlarmInterval'
_W='h3cIfMonInputErrorAlarmStatistics'
_V='h3cIfMonInputErrorAlarmLowThres'
_U='h3cIfMonInputErrorAlarmHighThres'
_T='h3cIfMonOutputRateStatistics'
_S='h3cIfMonOutputRateHighThres'
_R='h3cIfMonOutputRateLowThres'
_Q='h3cIfMonInputRateStatistics'
_P='h3cIfMonInputRateHighThres'
_O='h3cIfMonInputRateLowThres'
_N='DisplayString'
_M='h3cIfPfcDot1pValue'
_L='seconds'
_K='not-accessible'
_J='TruthValue'
_I='Integer32'
_H='Unsigned32'
_G='ifDescr'
_F='ifIndex'
_E='read-only'
_D='read-write'
_C='IF-MIB'
_B='H3C-IF-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_C,'InterfaceIndex',_G,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','TextualConvention',_J)
h3cIfExt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,40))
if mibBuilder.loadTexts:h3cIfExt.setRevisions(('2018-02-07 00:00','2018-01-09 00:00','2017-12-13 18:20','2017-07-13 10:40','2016-12-05 18:00','2016-07-01 17:00','2015-12-10 10:00','2015-04-02 04:58','2014-11-20 08:00','2009-05-06 19:36','2004-11-13 19:36'))
_H3cIfExtScalarGroup_ObjectIdentity=ObjectIdentity
h3cIfExtScalarGroup=_H3cIfExtScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,1))
_H3cIfStatGlobalFlowInterval_Type=Integer32
_H3cIfStatGlobalFlowInterval_Object=MibScalar
h3cIfStatGlobalFlowInterval=_H3cIfStatGlobalFlowInterval_Object((1,3,6,1,4,1,2011,10,2,40,1,1),_H3cIfStatGlobalFlowInterval_Type())
h3cIfStatGlobalFlowInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfStatGlobalFlowInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cIfStatGlobalFlowInterval.setUnits(_L)
_H3cIfShutDownInterval_Type=Integer32
_H3cIfShutDownInterval_Object=MibScalar
h3cIfShutDownInterval=_H3cIfShutDownInterval_Object((1,3,6,1,4,1,2011,10,2,40,1,2),_H3cIfShutDownInterval_Type())
h3cIfShutDownInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfShutDownInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cIfShutDownInterval.setUnits(_L)
_H3cIfThroughputInKbps_Type=CounterBasedGauge64
_H3cIfThroughputInKbps_Object=MibScalar
h3cIfThroughputInKbps=_H3cIfThroughputInKbps_Object((1,3,6,1,4,1,2011,10,2,40,1,3),_H3cIfThroughputInKbps_Type())
h3cIfThroughputInKbps.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfThroughputInKbps.setStatus(_A)
_H3cIfThroughputOutKbps_Type=CounterBasedGauge64
_H3cIfThroughputOutKbps_Object=MibScalar
h3cIfThroughputOutKbps=_H3cIfThroughputOutKbps_Object((1,3,6,1,4,1,2011,10,2,40,1,4),_H3cIfThroughputOutKbps_Type())
h3cIfThroughputOutKbps.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfThroughputOutKbps.setStatus(_A)
_H3cIfExtGroup_ObjectIdentity=ObjectIdentity
h3cIfExtGroup=_H3cIfExtGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,2))
_H3cIfStat_ObjectIdentity=ObjectIdentity
h3cIfStat=_H3cIfStat_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,2,1))
_H3cIfStatScalarGroup_ObjectIdentity=ObjectIdentity
h3cIfStatScalarGroup=_H3cIfStatScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,2,1,1))
_H3cIfStatTable_ObjectIdentity=ObjectIdentity
h3cIfStatTable=_H3cIfStatTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,2,1,2))
_H3cIfFlowStatTable_Object=MibTable
h3cIfFlowStatTable=_H3cIfFlowStatTable_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1))
if mibBuilder.loadTexts:h3cIfFlowStatTable.setStatus(_A)
_H3cIfStatEntry_Object=MibTableRow
h3cIfStatEntry=_H3cIfStatEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1))
h3cIfStatEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfStatEntry.setStatus(_A)
_H3cIfStatFlowInterval_Type=Integer32
_H3cIfStatFlowInterval_Object=MibTableColumn
h3cIfStatFlowInterval=_H3cIfStatFlowInterval_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1,1),_H3cIfStatFlowInterval_Type())
h3cIfStatFlowInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfStatFlowInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cIfStatFlowInterval.setUnits(_L)
_H3cIfStatFlowInBits_Type=Unsigned32
_H3cIfStatFlowInBits_Object=MibTableColumn
h3cIfStatFlowInBits=_H3cIfStatFlowInBits_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1,2),_H3cIfStatFlowInBits_Type())
h3cIfStatFlowInBits.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowInBits.setStatus(_A)
_H3cIfStatFlowOutBits_Type=Unsigned32
_H3cIfStatFlowOutBits_Object=MibTableColumn
h3cIfStatFlowOutBits=_H3cIfStatFlowOutBits_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1,3),_H3cIfStatFlowOutBits_Type())
h3cIfStatFlowOutBits.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowOutBits.setStatus(_A)
_H3cIfStatFlowInPkts_Type=Unsigned32
_H3cIfStatFlowInPkts_Object=MibTableColumn
h3cIfStatFlowInPkts=_H3cIfStatFlowInPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1,4),_H3cIfStatFlowInPkts_Type())
h3cIfStatFlowInPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowInPkts.setStatus(_A)
_H3cIfStatFlowOutPkts_Type=Unsigned32
_H3cIfStatFlowOutPkts_Object=MibTableColumn
h3cIfStatFlowOutPkts=_H3cIfStatFlowOutPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1,5),_H3cIfStatFlowOutPkts_Type())
h3cIfStatFlowOutPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowOutPkts.setStatus(_A)
_H3cIfStatFlowInBytes_Type=Unsigned32
_H3cIfStatFlowInBytes_Object=MibTableColumn
h3cIfStatFlowInBytes=_H3cIfStatFlowInBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1,6),_H3cIfStatFlowInBytes_Type())
h3cIfStatFlowInBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowInBytes.setStatus(_A)
_H3cIfStatFlowOutBytes_Type=Unsigned32
_H3cIfStatFlowOutBytes_Object=MibTableColumn
h3cIfStatFlowOutBytes=_H3cIfStatFlowOutBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,1,1,7),_H3cIfStatFlowOutBytes_Type())
h3cIfStatFlowOutBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowOutBytes.setStatus(_A)
_H3cIfSpeedStatTable_Object=MibTable
h3cIfSpeedStatTable=_H3cIfSpeedStatTable_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,2))
if mibBuilder.loadTexts:h3cIfSpeedStatTable.setStatus(_A)
_H3cIfSpeedStatEntry_Object=MibTableRow
h3cIfSpeedStatEntry=_H3cIfSpeedStatEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,2,1))
h3cIfSpeedStatEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfSpeedStatEntry.setStatus(_A)
_H3cIfSpeedStatInterval_Type=Integer32
_H3cIfSpeedStatInterval_Object=MibTableColumn
h3cIfSpeedStatInterval=_H3cIfSpeedStatInterval_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,2,1,1),_H3cIfSpeedStatInterval_Type())
h3cIfSpeedStatInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfSpeedStatInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cIfSpeedStatInterval.setUnits(_L)
_H3cIfSpeedStatInPkts_Type=Unsigned32
_H3cIfSpeedStatInPkts_Object=MibTableColumn
h3cIfSpeedStatInPkts=_H3cIfSpeedStatInPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,2,1,2),_H3cIfSpeedStatInPkts_Type())
h3cIfSpeedStatInPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatInPkts.setStatus(_A)
_H3cIfSpeedStatOutPkts_Type=Unsigned32
_H3cIfSpeedStatOutPkts_Object=MibTableColumn
h3cIfSpeedStatOutPkts=_H3cIfSpeedStatOutPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,2,1,3),_H3cIfSpeedStatOutPkts_Type())
h3cIfSpeedStatOutPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatOutPkts.setStatus(_A)
_H3cIfSpeedStatInBytes_Type=Unsigned32
_H3cIfSpeedStatInBytes_Object=MibTableColumn
h3cIfSpeedStatInBytes=_H3cIfSpeedStatInBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,2,1,4),_H3cIfSpeedStatInBytes_Type())
h3cIfSpeedStatInBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatInBytes.setStatus(_A)
_H3cIfSpeedStatOutBytes_Type=Unsigned32
_H3cIfSpeedStatOutBytes_Object=MibTableColumn
h3cIfSpeedStatOutBytes=_H3cIfSpeedStatOutBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,2,1,5),_H3cIfSpeedStatOutBytes_Type())
h3cIfSpeedStatOutBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatOutBytes.setStatus(_A)
_H3cIfHCFlowStatTable_Object=MibTable
h3cIfHCFlowStatTable=_H3cIfHCFlowStatTable_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3))
if mibBuilder.loadTexts:h3cIfHCFlowStatTable.setStatus(_A)
_H3cIfHCFlowStatEntry_Object=MibTableRow
h3cIfHCFlowStatEntry=_H3cIfHCFlowStatEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3,1))
h3cIfHCFlowStatEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfHCFlowStatEntry.setStatus(_A)
_H3cIfStatFlowHCInBits_Type=CounterBasedGauge64
_H3cIfStatFlowHCInBits_Object=MibTableColumn
h3cIfStatFlowHCInBits=_H3cIfStatFlowHCInBits_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3,1,1),_H3cIfStatFlowHCInBits_Type())
h3cIfStatFlowHCInBits.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowHCInBits.setStatus(_A)
_H3cIfStatFlowHCOutBits_Type=CounterBasedGauge64
_H3cIfStatFlowHCOutBits_Object=MibTableColumn
h3cIfStatFlowHCOutBits=_H3cIfStatFlowHCOutBits_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3,1,2),_H3cIfStatFlowHCOutBits_Type())
h3cIfStatFlowHCOutBits.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowHCOutBits.setStatus(_A)
_H3cIfStatFlowHCInPkts_Type=CounterBasedGauge64
_H3cIfStatFlowHCInPkts_Object=MibTableColumn
h3cIfStatFlowHCInPkts=_H3cIfStatFlowHCInPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3,1,3),_H3cIfStatFlowHCInPkts_Type())
h3cIfStatFlowHCInPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowHCInPkts.setStatus(_A)
_H3cIfStatFlowHCOutPkts_Type=CounterBasedGauge64
_H3cIfStatFlowHCOutPkts_Object=MibTableColumn
h3cIfStatFlowHCOutPkts=_H3cIfStatFlowHCOutPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3,1,4),_H3cIfStatFlowHCOutPkts_Type())
h3cIfStatFlowHCOutPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowHCOutPkts.setStatus(_A)
_H3cIfStatFlowHCInBytes_Type=CounterBasedGauge64
_H3cIfStatFlowHCInBytes_Object=MibTableColumn
h3cIfStatFlowHCInBytes=_H3cIfStatFlowHCInBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3,1,5),_H3cIfStatFlowHCInBytes_Type())
h3cIfStatFlowHCInBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowHCInBytes.setStatus(_A)
_H3cIfStatFlowHCOutBytes_Type=CounterBasedGauge64
_H3cIfStatFlowHCOutBytes_Object=MibTableColumn
h3cIfStatFlowHCOutBytes=_H3cIfStatFlowHCOutBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,3,1,6),_H3cIfStatFlowHCOutBytes_Type())
h3cIfStatFlowHCOutBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowHCOutBytes.setStatus(_A)
_H3cIfHCSpeedStatTable_Object=MibTable
h3cIfHCSpeedStatTable=_H3cIfHCSpeedStatTable_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,4))
if mibBuilder.loadTexts:h3cIfHCSpeedStatTable.setStatus(_A)
_H3cIfHCSpeedStatEntry_Object=MibTableRow
h3cIfHCSpeedStatEntry=_H3cIfHCSpeedStatEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,4,1))
h3cIfHCSpeedStatEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfHCSpeedStatEntry.setStatus(_A)
_H3cIfSpeedStatHCInPkts_Type=CounterBasedGauge64
_H3cIfSpeedStatHCInPkts_Object=MibTableColumn
h3cIfSpeedStatHCInPkts=_H3cIfSpeedStatHCInPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,4,1,1),_H3cIfSpeedStatHCInPkts_Type())
h3cIfSpeedStatHCInPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatHCInPkts.setStatus(_A)
_H3cIfSpeedStatHCOutPkts_Type=CounterBasedGauge64
_H3cIfSpeedStatHCOutPkts_Object=MibTableColumn
h3cIfSpeedStatHCOutPkts=_H3cIfSpeedStatHCOutPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,4,1,2),_H3cIfSpeedStatHCOutPkts_Type())
h3cIfSpeedStatHCOutPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatHCOutPkts.setStatus(_A)
_H3cIfSpeedStatHCInBytes_Type=CounterBasedGauge64
_H3cIfSpeedStatHCInBytes_Object=MibTableColumn
h3cIfSpeedStatHCInBytes=_H3cIfSpeedStatHCInBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,4,1,3),_H3cIfSpeedStatHCInBytes_Type())
h3cIfSpeedStatHCInBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatHCInBytes.setStatus(_A)
_H3cIfSpeedStatHCOutBytes_Type=CounterBasedGauge64
_H3cIfSpeedStatHCOutBytes_Object=MibTableColumn
h3cIfSpeedStatHCOutBytes=_H3cIfSpeedStatHCOutBytes_Object((1,3,6,1,4,1,2011,10,2,40,2,1,2,4,1,4),_H3cIfSpeedStatHCOutBytes_Type())
h3cIfSpeedStatHCOutBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatHCOutBytes.setStatus(_A)
_H3cIfControl_ObjectIdentity=ObjectIdentity
h3cIfControl=_H3cIfControl_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,2,2))
_H3cRTParentIfTable_Object=MibTable
h3cRTParentIfTable=_H3cRTParentIfTable_Object((1,3,6,1,4,1,2011,10,2,40,2,2,1))
if mibBuilder.loadTexts:h3cRTParentIfTable.setStatus(_A)
_H3cRTParentIfEntry_Object=MibTableRow
h3cRTParentIfEntry=_H3cRTParentIfEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,2,1,1))
h3cRTParentIfEntry.setIndexNames((0,_B,_A1))
if mibBuilder.loadTexts:h3cRTParentIfEntry.setStatus(_A)
class _H3cRTParentIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cRTParentIfIndex_Type.__name__=_I
_H3cRTParentIfIndex_Object=MibTableColumn
h3cRTParentIfIndex=_H3cRTParentIfIndex_Object((1,3,6,1,4,1,2011,10,2,40,2,2,1,1,1),_H3cRTParentIfIndex_Type())
h3cRTParentIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRTParentIfIndex.setStatus(_A)
_H3cRTMinSubIfOrdinal_Type=Integer32
_H3cRTMinSubIfOrdinal_Object=MibTableColumn
h3cRTMinSubIfOrdinal=_H3cRTMinSubIfOrdinal_Object((1,3,6,1,4,1,2011,10,2,40,2,2,1,1,2),_H3cRTMinSubIfOrdinal_Type())
h3cRTMinSubIfOrdinal.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRTMinSubIfOrdinal.setStatus(_A)
_H3cRTMaxSubIfOrdinal_Type=Integer32
_H3cRTMaxSubIfOrdinal_Object=MibTableColumn
h3cRTMaxSubIfOrdinal=_H3cRTMaxSubIfOrdinal_Object((1,3,6,1,4,1,2011,10,2,40,2,2,1,1,3),_H3cRTMaxSubIfOrdinal_Type())
h3cRTMaxSubIfOrdinal.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRTMaxSubIfOrdinal.setStatus(_A)
_H3cRTSubIfTable_Object=MibTable
h3cRTSubIfTable=_H3cRTSubIfTable_Object((1,3,6,1,4,1,2011,10,2,40,2,2,2))
if mibBuilder.loadTexts:h3cRTSubIfTable.setStatus(_A)
_H3cRTSubIfEntry_Object=MibTableRow
h3cRTSubIfEntry=_H3cRTSubIfEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,2,2,1))
h3cRTSubIfEntry.setIndexNames((0,_B,_A2),(0,_B,_A3))
if mibBuilder.loadTexts:h3cRTSubIfEntry.setStatus(_A)
class _H3cRTSubIfParentIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cRTSubIfParentIfIndex_Type.__name__=_I
_H3cRTSubIfParentIfIndex_Object=MibTableColumn
h3cRTSubIfParentIfIndex=_H3cRTSubIfParentIfIndex_Object((1,3,6,1,4,1,2011,10,2,40,2,2,2,1,1),_H3cRTSubIfParentIfIndex_Type())
h3cRTSubIfParentIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRTSubIfParentIfIndex.setStatus(_A)
class _H3cRTSubIfOrdinal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cRTSubIfOrdinal_Type.__name__=_I
_H3cRTSubIfOrdinal_Object=MibTableColumn
h3cRTSubIfOrdinal=_H3cRTSubIfOrdinal_Object((1,3,6,1,4,1,2011,10,2,40,2,2,2,1,2),_H3cRTSubIfOrdinal_Type())
h3cRTSubIfOrdinal.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRTSubIfOrdinal.setStatus(_A)
_H3cRTSubIfSubIfIndex_Type=Integer32
_H3cRTSubIfSubIfIndex_Object=MibTableColumn
h3cRTSubIfSubIfIndex=_H3cRTSubIfSubIfIndex_Object((1,3,6,1,4,1,2011,10,2,40,2,2,2,1,3),_H3cRTSubIfSubIfIndex_Type())
h3cRTSubIfSubIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRTSubIfSubIfIndex.setStatus(_A)
class _H3cRTSubIfSubIfDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cRTSubIfSubIfDesc_Type.__name__=_N
_H3cRTSubIfSubIfDesc_Object=MibTableColumn
h3cRTSubIfSubIfDesc=_H3cRTSubIfSubIfDesc_Object((1,3,6,1,4,1,2011,10,2,40,2,2,2,1,4),_H3cRTSubIfSubIfDesc_Type())
h3cRTSubIfSubIfDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRTSubIfSubIfDesc.setStatus(_A)
_H3cRTSubIfRowStatus_Type=RowStatus
_H3cRTSubIfRowStatus_Object=MibTableColumn
h3cRTSubIfRowStatus=_H3cRTSubIfRowStatus_Object((1,3,6,1,4,1,2011,10,2,40,2,2,2,1,5),_H3cRTSubIfRowStatus_Type())
h3cRTSubIfRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:h3cRTSubIfRowStatus.setStatus(_A)
_H3cIfLinkModeTable_Object=MibTable
h3cIfLinkModeTable=_H3cIfLinkModeTable_Object((1,3,6,1,4,1,2011,10,2,40,2,2,3))
if mibBuilder.loadTexts:h3cIfLinkModeTable.setStatus(_A)
_H3cIfLinkModeEntry_Object=MibTableRow
h3cIfLinkModeEntry=_H3cIfLinkModeEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,2,3,1))
h3cIfLinkModeEntry.setIndexNames((0,_B,_A4))
if mibBuilder.loadTexts:h3cIfLinkModeEntry.setStatus(_A)
class _H3cIfLinkModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIfLinkModeIndex_Type.__name__=_I
_H3cIfLinkModeIndex_Object=MibTableColumn
h3cIfLinkModeIndex=_H3cIfLinkModeIndex_Object((1,3,6,1,4,1,2011,10,2,40,2,2,3,1,1),_H3cIfLinkModeIndex_Type())
h3cIfLinkModeIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cIfLinkModeIndex.setStatus(_A)
class _H3cIfLinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridgeMode',1),('routeMode',2)))
_H3cIfLinkMode_Type.__name__=_I
_H3cIfLinkMode_Object=MibTableColumn
h3cIfLinkMode=_H3cIfLinkMode_Object((1,3,6,1,4,1,2011,10,2,40,2,2,3,1,2),_H3cIfLinkMode_Type())
h3cIfLinkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfLinkMode.setStatus(_A)
_H3cIfLinkModeSwitchSupport_Type=TruthValue
_H3cIfLinkModeSwitchSupport_Object=MibTableColumn
h3cIfLinkModeSwitchSupport=_H3cIfLinkModeSwitchSupport_Object((1,3,6,1,4,1,2011,10,2,40,2,2,3,1,3),_H3cIfLinkModeSwitchSupport_Type())
h3cIfLinkModeSwitchSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfLinkModeSwitchSupport.setStatus(_A)
_H3cIfPortTypeTable_Object=MibTable
h3cIfPortTypeTable=_H3cIfPortTypeTable_Object((1,3,6,1,4,1,2011,10,2,40,2,2,4))
if mibBuilder.loadTexts:h3cIfPortTypeTable.setStatus(_A)
_H3cIfPortTypeEntry_Object=MibTableRow
h3cIfPortTypeEntry=_H3cIfPortTypeEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,2,4,1))
h3cIfPortTypeEntry.setIndexNames((0,_B,_A5))
if mibBuilder.loadTexts:h3cIfPortTypeEntry.setStatus(_A)
_H3cIfPortTypeIndex_Type=InterfaceIndex
_H3cIfPortTypeIndex_Object=MibTableColumn
h3cIfPortTypeIndex=_H3cIfPortTypeIndex_Object((1,3,6,1,4,1,2011,10,2,40,2,2,4,1,1),_H3cIfPortTypeIndex_Type())
h3cIfPortTypeIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cIfPortTypeIndex.setStatus(_A)
class _H3cIfPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('ethernet',2),('fc',3)))
_H3cIfPortType_Type.__name__=_I
_H3cIfPortType_Object=MibTableColumn
h3cIfPortType=_H3cIfPortType_Object((1,3,6,1,4,1,2011,10,2,40,2,2,4,1,2),_H3cIfPortType_Type())
h3cIfPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfPortType.setStatus(_A)
_H3cIfPfcDot1pTable_Object=MibTable
h3cIfPfcDot1pTable=_H3cIfPfcDot1pTable_Object((1,3,6,1,4,1,2011,10,2,40,2,2,5))
if mibBuilder.loadTexts:h3cIfPfcDot1pTable.setStatus(_A)
_H3cIfPfcDot1pEntry_Object=MibTableRow
h3cIfPfcDot1pEntry=_H3cIfPfcDot1pEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,2,5,1))
h3cIfPfcDot1pEntry.setIndexNames((0,_C,_F),(0,_B,_M))
if mibBuilder.loadTexts:h3cIfPfcDot1pEntry.setStatus(_A)
class _H3cIfPfcDot1pValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('pri0',1),('pri1',2),('pri2',3),('pri3',4),('pri4',5),('pri5',6),('pri6',7),('pri7',8)))
_H3cIfPfcDot1pValue_Type.__name__=_I
_H3cIfPfcDot1pValue_Object=MibTableColumn
h3cIfPfcDot1pValue=_H3cIfPfcDot1pValue_Object((1,3,6,1,4,1,2011,10,2,40,2,2,5,1,1),_H3cIfPfcDot1pValue_Type())
h3cIfPfcDot1pValue.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfPfcDot1pValue.setStatus(_A)
_H3cIfPfcDot1pInPps_Type=Unsigned32
_H3cIfPfcDot1pInPps_Object=MibTableColumn
h3cIfPfcDot1pInPps=_H3cIfPfcDot1pInPps_Object((1,3,6,1,4,1,2011,10,2,40,2,2,5,1,2),_H3cIfPfcDot1pInPps_Type())
h3cIfPfcDot1pInPps.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfPfcDot1pInPps.setStatus(_A)
_H3cIfPfcDot1pOutPps_Type=Unsigned32
_H3cIfPfcDot1pOutPps_Object=MibTableColumn
h3cIfPfcDot1pOutPps=_H3cIfPfcDot1pOutPps_Object((1,3,6,1,4,1,2011,10,2,40,2,2,5,1,3),_H3cIfPfcDot1pOutPps_Type())
h3cIfPfcDot1pOutPps.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfPfcDot1pOutPps.setStatus(_A)
_H3cIfPfcDot1pInPpsThreshold_Type=Unsigned32
_H3cIfPfcDot1pInPpsThreshold_Object=MibTableColumn
h3cIfPfcDot1pInPpsThreshold=_H3cIfPfcDot1pInPpsThreshold_Object((1,3,6,1,4,1,2011,10,2,40,2,2,5,1,4),_H3cIfPfcDot1pInPpsThreshold_Type())
h3cIfPfcDot1pInPpsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfPfcDot1pInPpsThreshold.setStatus(_A)
_H3cIfPfcDot1pOutPpsThreshold_Type=Unsigned32
_H3cIfPfcDot1pOutPpsThreshold_Object=MibTableColumn
h3cIfPfcDot1pOutPpsThreshold=_H3cIfPfcDot1pOutPpsThreshold_Object((1,3,6,1,4,1,2011,10,2,40,2,2,5,1,5),_H3cIfPfcDot1pOutPpsThreshold_Type())
h3cIfPfcDot1pOutPpsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfPfcDot1pOutPpsThreshold.setStatus(_A)
_H3cIfInterfaces_ObjectIdentity=ObjectIdentity
h3cIfInterfaces=_H3cIfInterfaces_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,2,3))
_H3cIfPhysicalNumber_Type=Integer32
_H3cIfPhysicalNumber_Object=MibScalar
h3cIfPhysicalNumber=_H3cIfPhysicalNumber_Object((1,3,6,1,4,1,2011,10,2,40,2,3,1),_H3cIfPhysicalNumber_Type())
h3cIfPhysicalNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfPhysicalNumber.setStatus(_A)
_H3cIfTable_Object=MibTable
h3cIfTable=_H3cIfTable_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2))
if mibBuilder.loadTexts:h3cIfTable.setStatus(_A)
_H3cIfEntry_Object=MibTableRow
h3cIfEntry=_H3cIfEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1))
h3cIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfEntry.setStatus(_A)
_H3cIfUpDownTimes_Type=Integer32
_H3cIfUpDownTimes_Object=MibTableColumn
h3cIfUpDownTimes=_H3cIfUpDownTimes_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,1),_H3cIfUpDownTimes_Type())
h3cIfUpDownTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfUpDownTimes.setStatus(_A)
_H3cIfMtu_Type=Integer32
_H3cIfMtu_Object=MibTableColumn
h3cIfMtu=_H3cIfMtu_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,2),_H3cIfMtu_Type())
h3cIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMtu.setStatus(_A)
class _H3cIfBandwidthRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cIfBandwidthRate_Type.__name__=_I
_H3cIfBandwidthRate_Object=MibTableColumn
h3cIfBandwidthRate=_H3cIfBandwidthRate_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,3),_H3cIfBandwidthRate_Type())
h3cIfBandwidthRate.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfBandwidthRate.setStatus(_A)
class _H3cIfDiscardPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cIfDiscardPktRate_Type.__name__=_I
_H3cIfDiscardPktRate_Object=MibTableColumn
h3cIfDiscardPktRate=_H3cIfDiscardPktRate_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,4),_H3cIfDiscardPktRate_Type())
h3cIfDiscardPktRate.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfDiscardPktRate.setStatus(_A)
_H3cIfStatusKeepTime_Type=TimeTicks
_H3cIfStatusKeepTime_Object=MibTableColumn
h3cIfStatusKeepTime=_H3cIfStatusKeepTime_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,5),_H3cIfStatusKeepTime_Type())
h3cIfStatusKeepTime.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatusKeepTime.setStatus(_A)
_H3cIfInNUcastPkts_Type=Counter64
_H3cIfInNUcastPkts_Object=MibTableColumn
h3cIfInNUcastPkts=_H3cIfInNUcastPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,6),_H3cIfInNUcastPkts_Type())
h3cIfInNUcastPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfInNUcastPkts.setStatus(_A)
_H3cIfOutNUcastPkts_Type=Counter64
_H3cIfOutNUcastPkts_Object=MibTableColumn
h3cIfOutNUcastPkts=_H3cIfOutNUcastPkts_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,7),_H3cIfOutNUcastPkts_Type())
h3cIfOutNUcastPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfOutNUcastPkts.setStatus(_A)
_H3cIfIsPoe_Type=TruthValue
_H3cIfIsPoe_Object=MibTableColumn
h3cIfIsPoe=_H3cIfIsPoe_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,8),_H3cIfIsPoe_Type())
h3cIfIsPoe.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfIsPoe.setStatus(_A)
class _H3cIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('admindown',4)))
_H3cIfOperStatus_Type.__name__=_I
_H3cIfOperStatus_Object=MibTableColumn
h3cIfOperStatus=_H3cIfOperStatus_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,9),_H3cIfOperStatus_Type())
h3cIfOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfOperStatus.setStatus(_A)
_H3cIfDownTimes_Type=Integer32
_H3cIfDownTimes_Object=MibTableColumn
h3cIfDownTimes=_H3cIfDownTimes_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,10),_H3cIfDownTimes_Type())
h3cIfDownTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfDownTimes.setStatus(_A)
class _H3cIfPfcStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),('auto',3)))
_H3cIfPfcStatus_Type.__name__=_I
_H3cIfPfcStatus_Object=MibTableColumn
h3cIfPfcStatus=_H3cIfPfcStatus_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,11),_H3cIfPfcStatus_Type())
h3cIfPfcStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfPfcStatus.setStatus(_A)
class _H3cIfPfcDot1pNoDrop_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('pri0',0),('pri1',1),('pri2',2),('pri3',3),('pri4',4),('pri5',5),('pri6',6),('pri7',7)))
_H3cIfPfcDot1pNoDrop_Type.__name__='Bits'
_H3cIfPfcDot1pNoDrop_Object=MibTableColumn
h3cIfPfcDot1pNoDrop=_H3cIfPfcDot1pNoDrop_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,12),_H3cIfPfcDot1pNoDrop_Type())
h3cIfPfcDot1pNoDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfPfcDot1pNoDrop.setStatus(_A)
class _H3cIfDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIfDescription_Type.__name__=_N
_H3cIfDescription_Object=MibTableColumn
h3cIfDescription=_H3cIfDescription_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,13),_H3cIfDescription_Type())
h3cIfDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfDescription.setStatus(_A)
_H3cIfFwdErrDiscards_Type=Unsigned32
_H3cIfFwdErrDiscards_Object=MibTableColumn
h3cIfFwdErrDiscards=_H3cIfFwdErrDiscards_Object((1,3,6,1,4,1,2011,10,2,40,2,3,2,1,14),_H3cIfFwdErrDiscards_Type())
h3cIfFwdErrDiscards.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfFwdErrDiscards.setStatus(_A)
_H3cIfUsingTable_Object=MibTable
h3cIfUsingTable=_H3cIfUsingTable_Object((1,3,6,1,4,1,2011,10,2,40,2,3,3))
if mibBuilder.loadTexts:h3cIfUsingTable.setStatus(_A)
_H3cIfUsingEntry_Object=MibTableRow
h3cIfUsingEntry=_H3cIfUsingEntry_Object((1,3,6,1,4,1,2011,10,2,40,2,3,3,1))
h3cIfUsingEntry.setIndexNames((0,_B,_A6))
if mibBuilder.loadTexts:h3cIfUsingEntry.setStatus(_A)
class _H3cIfUsingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIfUsingIndex_Type.__name__=_I
_H3cIfUsingIndex_Object=MibTableColumn
h3cIfUsingIndex=_H3cIfUsingIndex_Object((1,3,6,1,4,1,2011,10,2,40,2,3,3,1,1),_H3cIfUsingIndex_Type())
h3cIfUsingIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cIfUsingIndex.setStatus(_A)
_H3cIfUsingSupportType_Type=Integer32
_H3cIfUsingSupportType_Object=MibTableColumn
h3cIfUsingSupportType=_H3cIfUsingSupportType_Object((1,3,6,1,4,1,2011,10,2,40,2,3,3,1,2),_H3cIfUsingSupportType_Type())
h3cIfUsingSupportType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfUsingSupportType.setStatus(_A)
class _H3cIfUsingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('noUsing',0),('using10GE',1),('using20GE',2),('using40GE',3),('using100GE',4),('using25GE',5),('using50GE',6)))
_H3cIfUsingType_Type.__name__=_I
_H3cIfUsingType_Object=MibTableColumn
h3cIfUsingType=_H3cIfUsingType_Object((1,3,6,1,4,1,2011,10,2,40,2,3,3,1,3),_H3cIfUsingType_Type())
h3cIfUsingType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfUsingType.setStatus(_A)
class _H3cIfUsingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noUsing',0),('needReboot',1)))
_H3cIfUsingStatus_Type.__name__=_I
_H3cIfUsingStatus_Object=MibTableColumn
h3cIfUsingStatus=_H3cIfUsingStatus_Object((1,3,6,1,4,1,2011,10,2,40,2,3,3,1,4),_H3cIfUsingStatus_Type())
h3cIfUsingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfUsingStatus.setStatus(_A)
_H3cIfExtTrap_ObjectIdentity=ObjectIdentity
h3cIfExtTrap=_H3cIfExtTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,3))
_H3cIfExtTrapPrex_ObjectIdentity=ObjectIdentity
h3cIfExtTrapPrex=_H3cIfExtTrapPrex_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,3,0))
_H3cIfExtTrapObject_ObjectIdentity=ObjectIdentity
h3cIfExtTrapObject=_H3cIfExtTrapObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,3,1))
_H3cIfExtTrapCfgTable_Object=MibTable
h3cIfExtTrapCfgTable=_H3cIfExtTrapCfgTable_Object((1,3,6,1,4,1,2011,10,2,40,3,1,1))
if mibBuilder.loadTexts:h3cIfExtTrapCfgTable.setStatus(_A)
_H3cIfExtTrapCfgEntry_Object=MibTableRow
h3cIfExtTrapCfgEntry=_H3cIfExtTrapCfgEntry_Object((1,3,6,1,4,1,2011,10,2,40,3,1,1,1))
h3cIfExtTrapCfgEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfExtTrapCfgEntry.setStatus(_A)
class _H3cIfBandwidthUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cIfBandwidthUpperLimit_Type.__name__=_I
_H3cIfBandwidthUpperLimit_Object=MibTableColumn
h3cIfBandwidthUpperLimit=_H3cIfBandwidthUpperLimit_Object((1,3,6,1,4,1,2011,10,2,40,3,1,1,1,1),_H3cIfBandwidthUpperLimit_Type())
h3cIfBandwidthUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfBandwidthUpperLimit.setStatus(_A)
class _H3cIfDiscardPktRateUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cIfDiscardPktRateUpperLimit_Type.__name__=_I
_H3cIfDiscardPktRateUpperLimit_Object=MibTableColumn
h3cIfDiscardPktRateUpperLimit=_H3cIfDiscardPktRateUpperLimit_Object((1,3,6,1,4,1,2011,10,2,40,3,1,1,1,2),_H3cIfDiscardPktRateUpperLimit_Type())
h3cIfDiscardPktRateUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfDiscardPktRateUpperLimit.setStatus(_A)
_H3cIfMonScalarGroup_ObjectIdentity=ObjectIdentity
h3cIfMonScalarGroup=_H3cIfMonScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,4))
_H3cIfMonGroup_ObjectIdentity=ObjectIdentity
h3cIfMonGroup=_H3cIfMonGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,5))
_H3cIfMonStat_ObjectIdentity=ObjectIdentity
h3cIfMonStat=_H3cIfMonStat_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,5,1))
_H3cIfMonStatTable_Object=MibTable
h3cIfMonStatTable=_H3cIfMonStatTable_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1))
if mibBuilder.loadTexts:h3cIfMonStatTable.setStatus(_A)
_H3cIfMonStatEntry_Object=MibTableRow
h3cIfMonStatEntry=_H3cIfMonStatEntry_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1))
h3cIfMonStatEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfMonStatEntry.setStatus(_A)
_H3cIfMonInputRateStatistics_Type=Counter64
_H3cIfMonInputRateStatistics_Object=MibTableColumn
h3cIfMonInputRateStatistics=_H3cIfMonInputRateStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,1),_H3cIfMonInputRateStatistics_Type())
h3cIfMonInputRateStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonInputRateStatistics.setStatus(_A)
_H3cIfMonOutputRateStatistics_Type=Counter64
_H3cIfMonOutputRateStatistics_Object=MibTableColumn
h3cIfMonOutputRateStatistics=_H3cIfMonOutputRateStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,2),_H3cIfMonOutputRateStatistics_Type())
h3cIfMonOutputRateStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonOutputRateStatistics.setStatus(_A)
_H3cIfMonInputErrorAlarmStatistics_Type=Counter64
_H3cIfMonInputErrorAlarmStatistics_Object=MibTableColumn
h3cIfMonInputErrorAlarmStatistics=_H3cIfMonInputErrorAlarmStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,3),_H3cIfMonInputErrorAlarmStatistics_Type())
h3cIfMonInputErrorAlarmStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonInputErrorAlarmStatistics.setStatus(_A)
_H3cIfMonOutputErrorAlarmStatistics_Type=Counter64
_H3cIfMonOutputErrorAlarmStatistics_Object=MibTableColumn
h3cIfMonOutputErrorAlarmStatistics=_H3cIfMonOutputErrorAlarmStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,4),_H3cIfMonOutputErrorAlarmStatistics_Type())
h3cIfMonOutputErrorAlarmStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonOutputErrorAlarmStatistics.setStatus(_A)
_H3cIfMonSdhErrorStatistics_Type=Counter64
_H3cIfMonSdhErrorStatistics_Object=MibTableColumn
h3cIfMonSdhErrorStatistics=_H3cIfMonSdhErrorStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,5),_H3cIfMonSdhErrorStatistics_Type())
h3cIfMonSdhErrorStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonSdhErrorStatistics.setStatus(_A)
_H3cIfMonSdhB1ErrorStatistics_Type=Counter64
_H3cIfMonSdhB1ErrorStatistics_Object=MibTableColumn
h3cIfMonSdhB1ErrorStatistics=_H3cIfMonSdhB1ErrorStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,6),_H3cIfMonSdhB1ErrorStatistics_Type())
h3cIfMonSdhB1ErrorStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonSdhB1ErrorStatistics.setStatus(_A)
_H3cIfMonSdhB2ErrorStatistics_Type=Counter64
_H3cIfMonSdhB2ErrorStatistics_Object=MibTableColumn
h3cIfMonSdhB2ErrorStatistics=_H3cIfMonSdhB2ErrorStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,7),_H3cIfMonSdhB2ErrorStatistics_Type())
h3cIfMonSdhB2ErrorStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonSdhB2ErrorStatistics.setStatus(_A)
_H3cIfMonCRCErrorStatistics_Type=Counter64
_H3cIfMonCRCErrorStatistics_Object=MibTableColumn
h3cIfMonCRCErrorStatistics=_H3cIfMonCRCErrorStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,8),_H3cIfMonCRCErrorStatistics_Type())
h3cIfMonCRCErrorStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonCRCErrorStatistics.setStatus(_A)
_H3cIfMonPauseFrameStatistics_Type=Counter64
_H3cIfMonPauseFrameStatistics_Object=MibTableColumn
h3cIfMonPauseFrameStatistics=_H3cIfMonPauseFrameStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,9),_H3cIfMonPauseFrameStatistics_Type())
h3cIfMonPauseFrameStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonPauseFrameStatistics.setStatus(_A)
_H3cIfMonTxPauseFrameStatistics_Type=Counter64
_H3cIfMonTxPauseFrameStatistics_Object=MibTableColumn
h3cIfMonTxPauseFrameStatistics=_H3cIfMonTxPauseFrameStatistics_Object((1,3,6,1,4,1,2011,10,2,40,5,1,1,1,10),_H3cIfMonTxPauseFrameStatistics_Type())
h3cIfMonTxPauseFrameStatistics.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMonTxPauseFrameStatistics.setStatus(_A)
_H3cIfMonControl_ObjectIdentity=ObjectIdentity
h3cIfMonControl=_H3cIfMonControl_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,5,2))
_H3cIfMonThresholdTable_Object=MibTable
h3cIfMonThresholdTable=_H3cIfMonThresholdTable_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1))
if mibBuilder.loadTexts:h3cIfMonThresholdTable.setStatus(_A)
_H3cIfMonThresholdEntry_Object=MibTableRow
h3cIfMonThresholdEntry=_H3cIfMonThresholdEntry_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1))
h3cIfMonThresholdEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfMonThresholdEntry.setStatus(_A)
class _H3cIfMonInputRateLowThres_Type(Unsigned32):defaultValue=80
_H3cIfMonInputRateLowThres_Type.__name__=_H
_H3cIfMonInputRateLowThres_Object=MibTableColumn
h3cIfMonInputRateLowThres=_H3cIfMonInputRateLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,1),_H3cIfMonInputRateLowThres_Type())
h3cIfMonInputRateLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonInputRateLowThres.setStatus(_A)
class _H3cIfMonInputRateHighThres_Type(Unsigned32):defaultValue=90
_H3cIfMonInputRateHighThres_Type.__name__=_H
_H3cIfMonInputRateHighThres_Object=MibTableColumn
h3cIfMonInputRateHighThres=_H3cIfMonInputRateHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,2),_H3cIfMonInputRateHighThres_Type())
h3cIfMonInputRateHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonInputRateHighThres.setStatus(_A)
class _H3cIfMonOutputRateLowThres_Type(Unsigned32):defaultValue=80
_H3cIfMonOutputRateLowThres_Type.__name__=_H
_H3cIfMonOutputRateLowThres_Object=MibTableColumn
h3cIfMonOutputRateLowThres=_H3cIfMonOutputRateLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,3),_H3cIfMonOutputRateLowThres_Type())
h3cIfMonOutputRateLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonOutputRateLowThres.setStatus(_A)
class _H3cIfMonOutputRateHighThres_Type(Unsigned32):defaultValue=90
_H3cIfMonOutputRateHighThres_Type.__name__=_H
_H3cIfMonOutputRateHighThres_Object=MibTableColumn
h3cIfMonOutputRateHighThres=_H3cIfMonOutputRateHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,4),_H3cIfMonOutputRateHighThres_Type())
h3cIfMonOutputRateHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonOutputRateHighThres.setStatus(_A)
class _H3cIfMonInputErrorAlarmLowThres_Type(Unsigned32):defaultValue=100
_H3cIfMonInputErrorAlarmLowThres_Type.__name__=_H
_H3cIfMonInputErrorAlarmLowThres_Object=MibTableColumn
h3cIfMonInputErrorAlarmLowThres=_H3cIfMonInputErrorAlarmLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,5),_H3cIfMonInputErrorAlarmLowThres_Type())
h3cIfMonInputErrorAlarmLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonInputErrorAlarmLowThres.setStatus(_A)
class _H3cIfMonInputErrorAlarmHighThres_Type(Unsigned32):defaultValue=1000
_H3cIfMonInputErrorAlarmHighThres_Type.__name__=_H
_H3cIfMonInputErrorAlarmHighThres_Object=MibTableColumn
h3cIfMonInputErrorAlarmHighThres=_H3cIfMonInputErrorAlarmHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,6),_H3cIfMonInputErrorAlarmHighThres_Type())
h3cIfMonInputErrorAlarmHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonInputErrorAlarmHighThres.setStatus(_A)
class _H3cIfMonInputErrorAlarmInterval_Type(Unsigned32):defaultValue=10
_H3cIfMonInputErrorAlarmInterval_Type.__name__=_H
_H3cIfMonInputErrorAlarmInterval_Object=MibTableColumn
h3cIfMonInputErrorAlarmInterval=_H3cIfMonInputErrorAlarmInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,7),_H3cIfMonInputErrorAlarmInterval_Type())
h3cIfMonInputErrorAlarmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonInputErrorAlarmInterval.setStatus(_A)
class _H3cIfMonOutputErrorAlarmLowThres_Type(Unsigned32):defaultValue=100
_H3cIfMonOutputErrorAlarmLowThres_Type.__name__=_H
_H3cIfMonOutputErrorAlarmLowThres_Object=MibTableColumn
h3cIfMonOutputErrorAlarmLowThres=_H3cIfMonOutputErrorAlarmLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,8),_H3cIfMonOutputErrorAlarmLowThres_Type())
h3cIfMonOutputErrorAlarmLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonOutputErrorAlarmLowThres.setStatus(_A)
class _H3cIfMonOutputErrorAlarmHighThres_Type(Unsigned32):defaultValue=1000
_H3cIfMonOutputErrorAlarmHighThres_Type.__name__=_H
_H3cIfMonOutputErrorAlarmHighThres_Object=MibTableColumn
h3cIfMonOutputErrorAlarmHighThres=_H3cIfMonOutputErrorAlarmHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,9),_H3cIfMonOutputErrorAlarmHighThres_Type())
h3cIfMonOutputErrorAlarmHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonOutputErrorAlarmHighThres.setStatus(_A)
class _H3cIfMonOutputErrorAlarmInterval_Type(Unsigned32):defaultValue=10
_H3cIfMonOutputErrorAlarmInterval_Type.__name__=_H
_H3cIfMonOutputErrorAlarmInterval_Object=MibTableColumn
h3cIfMonOutputErrorAlarmInterval=_H3cIfMonOutputErrorAlarmInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,10),_H3cIfMonOutputErrorAlarmInterval_Type())
h3cIfMonOutputErrorAlarmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonOutputErrorAlarmInterval.setStatus(_A)
class _H3cIfMonSdhErrorLowThres_Type(Unsigned32):defaultValue=100
_H3cIfMonSdhErrorLowThres_Type.__name__=_H
_H3cIfMonSdhErrorLowThres_Object=MibTableColumn
h3cIfMonSdhErrorLowThres=_H3cIfMonSdhErrorLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,11),_H3cIfMonSdhErrorLowThres_Type())
h3cIfMonSdhErrorLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhErrorLowThres.setStatus(_A)
class _H3cIfMonSdhErrorHighThres_Type(Unsigned32):defaultValue=1000
_H3cIfMonSdhErrorHighThres_Type.__name__=_H
_H3cIfMonSdhErrorHighThres_Object=MibTableColumn
h3cIfMonSdhErrorHighThres=_H3cIfMonSdhErrorHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,12),_H3cIfMonSdhErrorHighThres_Type())
h3cIfMonSdhErrorHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhErrorHighThres.setStatus(_A)
class _H3cIfMonSdhErrorInterval_Type(Unsigned32):defaultValue=10
_H3cIfMonSdhErrorInterval_Type.__name__=_H
_H3cIfMonSdhErrorInterval_Object=MibTableColumn
h3cIfMonSdhErrorInterval=_H3cIfMonSdhErrorInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,13),_H3cIfMonSdhErrorInterval_Type())
h3cIfMonSdhErrorInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhErrorInterval.setStatus(_A)
_H3cIfMonSdhB1ErrorLowThres_Type=Unsigned32
_H3cIfMonSdhB1ErrorLowThres_Object=MibTableColumn
h3cIfMonSdhB1ErrorLowThres=_H3cIfMonSdhB1ErrorLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,14),_H3cIfMonSdhB1ErrorLowThres_Type())
h3cIfMonSdhB1ErrorLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB1ErrorLowThres.setStatus(_A)
class _H3cIfMonSdhB1ErrorHighThres_Type(Unsigned32):defaultValue=1000
_H3cIfMonSdhB1ErrorHighThres_Type.__name__=_H
_H3cIfMonSdhB1ErrorHighThres_Object=MibTableColumn
h3cIfMonSdhB1ErrorHighThres=_H3cIfMonSdhB1ErrorHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,15),_H3cIfMonSdhB1ErrorHighThres_Type())
h3cIfMonSdhB1ErrorHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB1ErrorHighThres.setStatus(_A)
class _H3cIfMonSdhB1ErrorInterval_Type(Unsigned32):defaultValue=10
_H3cIfMonSdhB1ErrorInterval_Type.__name__=_H
_H3cIfMonSdhB1ErrorInterval_Object=MibTableColumn
h3cIfMonSdhB1ErrorInterval=_H3cIfMonSdhB1ErrorInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,16),_H3cIfMonSdhB1ErrorInterval_Type())
h3cIfMonSdhB1ErrorInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB1ErrorInterval.setStatus(_A)
_H3cIfMonSdhB2ErrorLowThres_Type=Unsigned32
_H3cIfMonSdhB2ErrorLowThres_Object=MibTableColumn
h3cIfMonSdhB2ErrorLowThres=_H3cIfMonSdhB2ErrorLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,17),_H3cIfMonSdhB2ErrorLowThres_Type())
h3cIfMonSdhB2ErrorLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB2ErrorLowThres.setStatus(_A)
class _H3cIfMonSdhB2ErrorHighThres_Type(Unsigned32):defaultValue=1000
_H3cIfMonSdhB2ErrorHighThres_Type.__name__=_H
_H3cIfMonSdhB2ErrorHighThres_Object=MibTableColumn
h3cIfMonSdhB2ErrorHighThres=_H3cIfMonSdhB2ErrorHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,18),_H3cIfMonSdhB2ErrorHighThres_Type())
h3cIfMonSdhB2ErrorHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB2ErrorHighThres.setStatus(_A)
class _H3cIfMonSdhB2ErrorInterval_Type(Unsigned32):defaultValue=10
_H3cIfMonSdhB2ErrorInterval_Type.__name__=_H
_H3cIfMonSdhB2ErrorInterval_Object=MibTableColumn
h3cIfMonSdhB2ErrorInterval=_H3cIfMonSdhB2ErrorInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,19),_H3cIfMonSdhB2ErrorInterval_Type())
h3cIfMonSdhB2ErrorInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB2ErrorInterval.setStatus(_A)
_H3cIfMonCRCErrorLowThres_Type=Unsigned32
_H3cIfMonCRCErrorLowThres_Object=MibTableColumn
h3cIfMonCRCErrorLowThres=_H3cIfMonCRCErrorLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,20),_H3cIfMonCRCErrorLowThres_Type())
h3cIfMonCRCErrorLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonCRCErrorLowThres.setStatus(_A)
_H3cIfMonCRCErrorHighThres_Type=Unsigned32
_H3cIfMonCRCErrorHighThres_Object=MibTableColumn
h3cIfMonCRCErrorHighThres=_H3cIfMonCRCErrorHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,21),_H3cIfMonCRCErrorHighThres_Type())
h3cIfMonCRCErrorHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonCRCErrorHighThres.setStatus(_A)
class _H3cIfMonCRCErrorInterval_Type(Unsigned32):defaultValue=10
_H3cIfMonCRCErrorInterval_Type.__name__=_H
_H3cIfMonCRCErrorInterval_Object=MibTableColumn
h3cIfMonCRCErrorInterval=_H3cIfMonCRCErrorInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,22),_H3cIfMonCRCErrorInterval_Type())
h3cIfMonCRCErrorInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonCRCErrorInterval.setStatus(_A)
class _H3cIfMonCRCErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absolute',1),('ratio',2)))
_H3cIfMonCRCErrType_Type.__name__=_I
_H3cIfMonCRCErrType_Object=MibTableColumn
h3cIfMonCRCErrType=_H3cIfMonCRCErrType_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,23),_H3cIfMonCRCErrType_Type())
h3cIfMonCRCErrType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonCRCErrType.setStatus(_A)
_H3cIfMonPauseFrameLowThres_Type=Unsigned32
_H3cIfMonPauseFrameLowThres_Object=MibTableColumn
h3cIfMonPauseFrameLowThres=_H3cIfMonPauseFrameLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,24),_H3cIfMonPauseFrameLowThres_Type())
h3cIfMonPauseFrameLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonPauseFrameLowThres.setStatus(_A)
_H3cIfMonPauseFrameHighThres_Type=Unsigned32
_H3cIfMonPauseFrameHighThres_Object=MibTableColumn
h3cIfMonPauseFrameHighThres=_H3cIfMonPauseFrameHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,25),_H3cIfMonPauseFrameHighThres_Type())
h3cIfMonPauseFrameHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonPauseFrameHighThres.setStatus(_A)
_H3cIfMonPauseFrameInterval_Type=Unsigned32
_H3cIfMonPauseFrameInterval_Object=MibTableColumn
h3cIfMonPauseFrameInterval=_H3cIfMonPauseFrameInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,26),_H3cIfMonPauseFrameInterval_Type())
h3cIfMonPauseFrameInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonPauseFrameInterval.setStatus(_A)
class _H3cIfMonTxPauseFrameLowThres_Type(Unsigned32):defaultValue=100
_H3cIfMonTxPauseFrameLowThres_Type.__name__=_H
_H3cIfMonTxPauseFrameLowThres_Object=MibTableColumn
h3cIfMonTxPauseFrameLowThres=_H3cIfMonTxPauseFrameLowThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,27),_H3cIfMonTxPauseFrameLowThres_Type())
h3cIfMonTxPauseFrameLowThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonTxPauseFrameLowThres.setStatus(_A)
class _H3cIfMonTxPauseFrameHighThres_Type(Unsigned32):defaultValue=500
_H3cIfMonTxPauseFrameHighThres_Type.__name__=_H
_H3cIfMonTxPauseFrameHighThres_Object=MibTableColumn
h3cIfMonTxPauseFrameHighThres=_H3cIfMonTxPauseFrameHighThres_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,28),_H3cIfMonTxPauseFrameHighThres_Type())
h3cIfMonTxPauseFrameHighThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonTxPauseFrameHighThres.setStatus(_A)
class _H3cIfMonTxPauseFrameInterval_Type(Unsigned32):defaultValue=10
_H3cIfMonTxPauseFrameInterval_Type.__name__=_H
_H3cIfMonTxPauseFrameInterval_Object=MibTableColumn
h3cIfMonTxPauseFrameInterval=_H3cIfMonTxPauseFrameInterval_Object((1,3,6,1,4,1,2011,10,2,40,5,2,1,1,29),_H3cIfMonTxPauseFrameInterval_Type())
h3cIfMonTxPauseFrameInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonTxPauseFrameInterval.setStatus(_A)
_H3cIfMonAlarmDownEnableTable_Object=MibTable
h3cIfMonAlarmDownEnableTable=_H3cIfMonAlarmDownEnableTable_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2))
if mibBuilder.loadTexts:h3cIfMonAlarmDownEnableTable.setStatus(_A)
_H3cIfMonAlarmDownEnableEntry_Object=MibTableRow
h3cIfMonAlarmDownEnableEntry=_H3cIfMonAlarmDownEnableEntry_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1))
h3cIfMonAlarmDownEnableEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cIfMonAlarmDownEnableEntry.setStatus(_A)
class _H3cIfMonInputRateEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonInputRateEnableDown_Type.__name__=_J
_H3cIfMonInputRateEnableDown_Object=MibTableColumn
h3cIfMonInputRateEnableDown=_H3cIfMonInputRateEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,1),_H3cIfMonInputRateEnableDown_Type())
h3cIfMonInputRateEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonInputRateEnableDown.setStatus(_A)
class _H3cIfMonOutputRateEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonOutputRateEnableDown_Type.__name__=_J
_H3cIfMonOutputRateEnableDown_Object=MibTableColumn
h3cIfMonOutputRateEnableDown=_H3cIfMonOutputRateEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,2),_H3cIfMonOutputRateEnableDown_Type())
h3cIfMonOutputRateEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonOutputRateEnableDown.setStatus(_A)
class _H3cIfMonInputErrorAlarmEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonInputErrorAlarmEnableDown_Type.__name__=_J
_H3cIfMonInputErrorAlarmEnableDown_Object=MibTableColumn
h3cIfMonInputErrorAlarmEnableDown=_H3cIfMonInputErrorAlarmEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,3),_H3cIfMonInputErrorAlarmEnableDown_Type())
h3cIfMonInputErrorAlarmEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonInputErrorAlarmEnableDown.setStatus(_A)
class _H3cIfMonOutputErrorAlarmEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonOutputErrorAlarmEnableDown_Type.__name__=_J
_H3cIfMonOutputErrorAlarmEnableDown_Object=MibTableColumn
h3cIfMonOutputErrorAlarmEnableDown=_H3cIfMonOutputErrorAlarmEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,4),_H3cIfMonOutputErrorAlarmEnableDown_Type())
h3cIfMonOutputErrorAlarmEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonOutputErrorAlarmEnableDown.setStatus(_A)
class _H3cIfMonSdhErrorEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonSdhErrorEnableDown_Type.__name__=_J
_H3cIfMonSdhErrorEnableDown_Object=MibTableColumn
h3cIfMonSdhErrorEnableDown=_H3cIfMonSdhErrorEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,5),_H3cIfMonSdhErrorEnableDown_Type())
h3cIfMonSdhErrorEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhErrorEnableDown.setStatus(_A)
class _H3cIfMonSdhB1ErrorEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonSdhB1ErrorEnableDown_Type.__name__=_J
_H3cIfMonSdhB1ErrorEnableDown_Object=MibTableColumn
h3cIfMonSdhB1ErrorEnableDown=_H3cIfMonSdhB1ErrorEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,6),_H3cIfMonSdhB1ErrorEnableDown_Type())
h3cIfMonSdhB1ErrorEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB1ErrorEnableDown.setStatus(_A)
class _H3cIfMonSdhB2ErrorEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonSdhB2ErrorEnableDown_Type.__name__=_J
_H3cIfMonSdhB2ErrorEnableDown_Object=MibTableColumn
h3cIfMonSdhB2ErrorEnableDown=_H3cIfMonSdhB2ErrorEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,7),_H3cIfMonSdhB2ErrorEnableDown_Type())
h3cIfMonSdhB2ErrorEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonSdhB2ErrorEnableDown.setStatus(_A)
class _H3cIfMonCRCErrorEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonCRCErrorEnableDown_Type.__name__=_J
_H3cIfMonCRCErrorEnableDown_Object=MibTableColumn
h3cIfMonCRCErrorEnableDown=_H3cIfMonCRCErrorEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,8),_H3cIfMonCRCErrorEnableDown_Type())
h3cIfMonCRCErrorEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonCRCErrorEnableDown.setStatus(_A)
class _H3cIfMonPauseFrameEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonPauseFrameEnableDown_Type.__name__=_J
_H3cIfMonPauseFrameEnableDown_Object=MibTableColumn
h3cIfMonPauseFrameEnableDown=_H3cIfMonPauseFrameEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,9),_H3cIfMonPauseFrameEnableDown_Type())
h3cIfMonPauseFrameEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonPauseFrameEnableDown.setStatus(_A)
class _H3cIfMonTxPauseFrameEnableDown_Type(TruthValue):defaultValue=2
_H3cIfMonTxPauseFrameEnableDown_Type.__name__=_J
_H3cIfMonTxPauseFrameEnableDown_Object=MibTableColumn
h3cIfMonTxPauseFrameEnableDown=_H3cIfMonTxPauseFrameEnableDown_Object((1,3,6,1,4,1,2011,10,2,40,5,2,2,1,10),_H3cIfMonTxPauseFrameEnableDown_Type())
h3cIfMonTxPauseFrameEnableDown.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIfMonTxPauseFrameEnableDown.setStatus(_A)
_H3cIfMonTrap_ObjectIdentity=ObjectIdentity
h3cIfMonTrap=_H3cIfMonTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,6))
_H3cIfMonTrapPrex_ObjectIdentity=ObjectIdentity
h3cIfMonTrapPrex=_H3cIfMonTrapPrex_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,6,0))
_H3cIfMonTrapObject_ObjectIdentity=ObjectIdentity
h3cIfMonTrapObject=_H3cIfMonTrapObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,40,6,1))
h3cIfBandwidthUsageHigh=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,1))
h3cIfBandwidthUsageHigh.setObjects(*((_C,_G),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:h3cIfBandwidthUsageHigh.setStatus(_A)
h3cIfDiscardPktRateHigh=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,2))
h3cIfDiscardPktRateHigh.setObjects(*((_C,_G),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:h3cIfDiscardPktRateHigh.setStatus(_A)
h3cIfDampeningSuppressed=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,3))
h3cIfDampeningSuppressed.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cIfDampeningSuppressed.setStatus(_A)
h3cIfDampeningNotSuppressed=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,4))
h3cIfDampeningNotSuppressed.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cIfDampeningNotSuppressed.setStatus(_A)
h3cIfPortUp=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,5))
h3cIfPortUp.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cIfPortUp.setStatus(_A)
h3cIfPortDown=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,6))
h3cIfPortDown.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cIfPortDown.setStatus(_A)
h3cIfPfcOutRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,7))
h3cIfPfcOutRising.setObjects(*((_C,_F),(_C,_G),(_B,_M),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:h3cIfPfcOutRising.setStatus(_A)
h3cIfPfcInRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,3,0,8))
h3cIfPfcInRising.setObjects(*((_C,_F),(_C,_G),(_B,_M),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:h3cIfPfcInRising.setStatus(_A)
h3cIfMonInputRateRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,1))
h3cIfMonInputRateRising.setObjects(*((_C,_F),(_C,_G),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cIfMonInputRateRising.setStatus(_A)
h3cIfMonInputRateResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,2))
h3cIfMonInputRateResume.setObjects(*((_C,_F),(_C,_G),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cIfMonInputRateResume.setStatus(_A)
h3cIfMonOutputRateRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,3))
h3cIfMonOutputRateRising.setObjects(*((_C,_F),(_C,_G),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:h3cIfMonOutputRateRising.setStatus(_A)
h3cIfMonOutputRateResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,4))
h3cIfMonOutputRateResume.setObjects(*((_C,_F),(_C,_G),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:h3cIfMonOutputRateResume.setStatus(_A)
h3cIfMonInputErrorAlarmRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,5))
h3cIfMonInputErrorAlarmRising.setObjects(*((_C,_F),(_C,_G),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:h3cIfMonInputErrorAlarmRising.setStatus(_A)
h3cIfMonInputErrorAlarmResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,6))
h3cIfMonInputErrorAlarmResume.setObjects(*((_C,_F),(_C,_G),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:h3cIfMonInputErrorAlarmResume.setStatus(_A)
h3cIfMonOutputErrorAlarmRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,7))
h3cIfMonOutputErrorAlarmRising.setObjects(*((_C,_F),(_C,_G),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:h3cIfMonOutputErrorAlarmRising.setStatus(_A)
h3cIfMonOutputErrorAlarmResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,8))
h3cIfMonOutputErrorAlarmResume.setObjects(*((_C,_F),(_C,_G),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:h3cIfMonOutputErrorAlarmResume.setStatus(_A)
h3cIfMonSdhErrorRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,9))
h3cIfMonSdhErrorRising.setObjects(*((_C,_F),(_C,_G),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:h3cIfMonSdhErrorRising.setStatus(_A)
h3cIfMonSdhErrorResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,10))
h3cIfMonSdhErrorResume.setObjects(*((_C,_F),(_C,_G),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:h3cIfMonSdhErrorResume.setStatus(_A)
h3cIfMonSdhB1ErrorRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,11))
h3cIfMonSdhB1ErrorRising.setObjects(*((_C,_F),(_C,_G),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:h3cIfMonSdhB1ErrorRising.setStatus(_A)
h3cIfMonSdhB1ErrorResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,12))
h3cIfMonSdhB1ErrorResume.setObjects(*((_C,_F),(_C,_G),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:h3cIfMonSdhB1ErrorResume.setStatus(_A)
h3cIfMonSdhB2ErrorRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,13))
h3cIfMonSdhB2ErrorRising.setObjects(*((_C,_F),(_C,_G),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:h3cIfMonSdhB2ErrorRising.setStatus(_A)
h3cIfMonSdhB2ErrorResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,14))
h3cIfMonSdhB2ErrorResume.setObjects(*((_C,_F),(_C,_G),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:h3cIfMonSdhB2ErrorResume.setStatus(_A)
h3cIfMonCRCErrorRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,15))
h3cIfMonCRCErrorRising.setObjects(*((_C,_F),(_C,_G),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:h3cIfMonCRCErrorRising.setStatus(_A)
h3cIfMonCRCErrorResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,16))
h3cIfMonCRCErrorResume.setObjects(*((_C,_F),(_C,_G),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:h3cIfMonCRCErrorResume.setStatus(_A)
h3cIfMonPauseFrameRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,17))
h3cIfMonPauseFrameRising.setObjects(*((_C,_F),(_C,_G),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:h3cIfMonPauseFrameRising.setStatus(_A)
h3cIfMonPauseFrameResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,18))
h3cIfMonPauseFrameResume.setObjects(*((_C,_F),(_C,_G),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:h3cIfMonPauseFrameResume.setStatus(_A)
h3cIfMonTxPauseFrameRising=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,19))
h3cIfMonTxPauseFrameRising.setObjects(*((_C,_F),(_C,_G),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:h3cIfMonTxPauseFrameRising.setStatus(_A)
h3cIfMonTxPauseFrameResume=NotificationType((1,3,6,1,4,1,2011,10,2,40,6,0,20))
h3cIfMonTxPauseFrameResume.setObjects(*((_C,_F),(_C,_G),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:h3cIfMonTxPauseFrameResume.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cIfExt':h3cIfExt,'h3cIfExtScalarGroup':h3cIfExtScalarGroup,'h3cIfStatGlobalFlowInterval':h3cIfStatGlobalFlowInterval,'h3cIfShutDownInterval':h3cIfShutDownInterval,'h3cIfThroughputInKbps':h3cIfThroughputInKbps,'h3cIfThroughputOutKbps':h3cIfThroughputOutKbps,'h3cIfExtGroup':h3cIfExtGroup,'h3cIfStat':h3cIfStat,'h3cIfStatScalarGroup':h3cIfStatScalarGroup,'h3cIfStatTable':h3cIfStatTable,'h3cIfFlowStatTable':h3cIfFlowStatTable,'h3cIfStatEntry':h3cIfStatEntry,'h3cIfStatFlowInterval':h3cIfStatFlowInterval,'h3cIfStatFlowInBits':h3cIfStatFlowInBits,'h3cIfStatFlowOutBits':h3cIfStatFlowOutBits,'h3cIfStatFlowInPkts':h3cIfStatFlowInPkts,'h3cIfStatFlowOutPkts':h3cIfStatFlowOutPkts,'h3cIfStatFlowInBytes':h3cIfStatFlowInBytes,'h3cIfStatFlowOutBytes':h3cIfStatFlowOutBytes,'h3cIfSpeedStatTable':h3cIfSpeedStatTable,'h3cIfSpeedStatEntry':h3cIfSpeedStatEntry,'h3cIfSpeedStatInterval':h3cIfSpeedStatInterval,'h3cIfSpeedStatInPkts':h3cIfSpeedStatInPkts,'h3cIfSpeedStatOutPkts':h3cIfSpeedStatOutPkts,'h3cIfSpeedStatInBytes':h3cIfSpeedStatInBytes,'h3cIfSpeedStatOutBytes':h3cIfSpeedStatOutBytes,'h3cIfHCFlowStatTable':h3cIfHCFlowStatTable,'h3cIfHCFlowStatEntry':h3cIfHCFlowStatEntry,'h3cIfStatFlowHCInBits':h3cIfStatFlowHCInBits,'h3cIfStatFlowHCOutBits':h3cIfStatFlowHCOutBits,'h3cIfStatFlowHCInPkts':h3cIfStatFlowHCInPkts,'h3cIfStatFlowHCOutPkts':h3cIfStatFlowHCOutPkts,'h3cIfStatFlowHCInBytes':h3cIfStatFlowHCInBytes,'h3cIfStatFlowHCOutBytes':h3cIfStatFlowHCOutBytes,'h3cIfHCSpeedStatTable':h3cIfHCSpeedStatTable,'h3cIfHCSpeedStatEntry':h3cIfHCSpeedStatEntry,'h3cIfSpeedStatHCInPkts':h3cIfSpeedStatHCInPkts,'h3cIfSpeedStatHCOutPkts':h3cIfSpeedStatHCOutPkts,'h3cIfSpeedStatHCInBytes':h3cIfSpeedStatHCInBytes,'h3cIfSpeedStatHCOutBytes':h3cIfSpeedStatHCOutBytes,'h3cIfControl':h3cIfControl,'h3cRTParentIfTable':h3cRTParentIfTable,'h3cRTParentIfEntry':h3cRTParentIfEntry,_A1:h3cRTParentIfIndex,'h3cRTMinSubIfOrdinal':h3cRTMinSubIfOrdinal,'h3cRTMaxSubIfOrdinal':h3cRTMaxSubIfOrdinal,'h3cRTSubIfTable':h3cRTSubIfTable,'h3cRTSubIfEntry':h3cRTSubIfEntry,_A2:h3cRTSubIfParentIfIndex,_A3:h3cRTSubIfOrdinal,'h3cRTSubIfSubIfIndex':h3cRTSubIfSubIfIndex,'h3cRTSubIfSubIfDesc':h3cRTSubIfSubIfDesc,'h3cRTSubIfRowStatus':h3cRTSubIfRowStatus,'h3cIfLinkModeTable':h3cIfLinkModeTable,'h3cIfLinkModeEntry':h3cIfLinkModeEntry,_A4:h3cIfLinkModeIndex,'h3cIfLinkMode':h3cIfLinkMode,'h3cIfLinkModeSwitchSupport':h3cIfLinkModeSwitchSupport,'h3cIfPortTypeTable':h3cIfPortTypeTable,'h3cIfPortTypeEntry':h3cIfPortTypeEntry,_A5:h3cIfPortTypeIndex,'h3cIfPortType':h3cIfPortType,'h3cIfPfcDot1pTable':h3cIfPfcDot1pTable,'h3cIfPfcDot1pEntry':h3cIfPfcDot1pEntry,_M:h3cIfPfcDot1pValue,_AD:h3cIfPfcDot1pInPps,_AB:h3cIfPfcDot1pOutPps,_AE:h3cIfPfcDot1pInPpsThreshold,_AC:h3cIfPfcDot1pOutPpsThreshold,'h3cIfInterfaces':h3cIfInterfaces,'h3cIfPhysicalNumber':h3cIfPhysicalNumber,'h3cIfTable':h3cIfTable,'h3cIfEntry':h3cIfEntry,'h3cIfUpDownTimes':h3cIfUpDownTimes,'h3cIfMtu':h3cIfMtu,_A7:h3cIfBandwidthRate,_A9:h3cIfDiscardPktRate,'h3cIfStatusKeepTime':h3cIfStatusKeepTime,'h3cIfInNUcastPkts':h3cIfInNUcastPkts,'h3cIfOutNUcastPkts':h3cIfOutNUcastPkts,'h3cIfIsPoe':h3cIfIsPoe,'h3cIfOperStatus':h3cIfOperStatus,'h3cIfDownTimes':h3cIfDownTimes,'h3cIfPfcStatus':h3cIfPfcStatus,'h3cIfPfcDot1pNoDrop':h3cIfPfcDot1pNoDrop,'h3cIfDescription':h3cIfDescription,'h3cIfFwdErrDiscards':h3cIfFwdErrDiscards,'h3cIfUsingTable':h3cIfUsingTable,'h3cIfUsingEntry':h3cIfUsingEntry,_A6:h3cIfUsingIndex,'h3cIfUsingSupportType':h3cIfUsingSupportType,'h3cIfUsingType':h3cIfUsingType,'h3cIfUsingStatus':h3cIfUsingStatus,'h3cIfExtTrap':h3cIfExtTrap,'h3cIfExtTrapPrex':h3cIfExtTrapPrex,'h3cIfBandwidthUsageHigh':h3cIfBandwidthUsageHigh,'h3cIfDiscardPktRateHigh':h3cIfDiscardPktRateHigh,'h3cIfDampeningSuppressed':h3cIfDampeningSuppressed,'h3cIfDampeningNotSuppressed':h3cIfDampeningNotSuppressed,'h3cIfPortUp':h3cIfPortUp,'h3cIfPortDown':h3cIfPortDown,'h3cIfPfcOutRising':h3cIfPfcOutRising,'h3cIfPfcInRising':h3cIfPfcInRising,'h3cIfExtTrapObject':h3cIfExtTrapObject,'h3cIfExtTrapCfgTable':h3cIfExtTrapCfgTable,'h3cIfExtTrapCfgEntry':h3cIfExtTrapCfgEntry,_A8:h3cIfBandwidthUpperLimit,_AA:h3cIfDiscardPktRateUpperLimit,'h3cIfMonScalarGroup':h3cIfMonScalarGroup,'h3cIfMonGroup':h3cIfMonGroup,'h3cIfMonStat':h3cIfMonStat,'h3cIfMonStatTable':h3cIfMonStatTable,'h3cIfMonStatEntry':h3cIfMonStatEntry,_Q:h3cIfMonInputRateStatistics,_T:h3cIfMonOutputRateStatistics,_W:h3cIfMonInputErrorAlarmStatistics,_a:h3cIfMonOutputErrorAlarmStatistics,_e:h3cIfMonSdhErrorStatistics,_i:h3cIfMonSdhB1ErrorStatistics,_m:h3cIfMonSdhB2ErrorStatistics,_q:h3cIfMonCRCErrorStatistics,_v:h3cIfMonPauseFrameStatistics,_z:h3cIfMonTxPauseFrameStatistics,'h3cIfMonControl':h3cIfMonControl,'h3cIfMonThresholdTable':h3cIfMonThresholdTable,'h3cIfMonThresholdEntry':h3cIfMonThresholdEntry,_O:h3cIfMonInputRateLowThres,_P:h3cIfMonInputRateHighThres,_R:h3cIfMonOutputRateLowThres,_S:h3cIfMonOutputRateHighThres,_V:h3cIfMonInputErrorAlarmLowThres,_U:h3cIfMonInputErrorAlarmHighThres,_X:h3cIfMonInputErrorAlarmInterval,_Z:h3cIfMonOutputErrorAlarmLowThres,_Y:h3cIfMonOutputErrorAlarmHighThres,_b:h3cIfMonOutputErrorAlarmInterval,_c:h3cIfMonSdhErrorLowThres,_d:h3cIfMonSdhErrorHighThres,_f:h3cIfMonSdhErrorInterval,_g:h3cIfMonSdhB1ErrorLowThres,_h:h3cIfMonSdhB1ErrorHighThres,_j:h3cIfMonSdhB1ErrorInterval,_k:h3cIfMonSdhB2ErrorLowThres,_l:h3cIfMonSdhB2ErrorHighThres,_n:h3cIfMonSdhB2ErrorInterval,_p:h3cIfMonCRCErrorLowThres,_o:h3cIfMonCRCErrorHighThres,_r:h3cIfMonCRCErrorInterval,_s:h3cIfMonCRCErrType,_u:h3cIfMonPauseFrameLowThres,_t:h3cIfMonPauseFrameHighThres,_w:h3cIfMonPauseFrameInterval,_y:h3cIfMonTxPauseFrameLowThres,_x:h3cIfMonTxPauseFrameHighThres,_A0:h3cIfMonTxPauseFrameInterval,'h3cIfMonAlarmDownEnableTable':h3cIfMonAlarmDownEnableTable,'h3cIfMonAlarmDownEnableEntry':h3cIfMonAlarmDownEnableEntry,'h3cIfMonInputRateEnableDown':h3cIfMonInputRateEnableDown,'h3cIfMonOutputRateEnableDown':h3cIfMonOutputRateEnableDown,'h3cIfMonInputErrorAlarmEnableDown':h3cIfMonInputErrorAlarmEnableDown,'h3cIfMonOutputErrorAlarmEnableDown':h3cIfMonOutputErrorAlarmEnableDown,'h3cIfMonSdhErrorEnableDown':h3cIfMonSdhErrorEnableDown,'h3cIfMonSdhB1ErrorEnableDown':h3cIfMonSdhB1ErrorEnableDown,'h3cIfMonSdhB2ErrorEnableDown':h3cIfMonSdhB2ErrorEnableDown,'h3cIfMonCRCErrorEnableDown':h3cIfMonCRCErrorEnableDown,'h3cIfMonPauseFrameEnableDown':h3cIfMonPauseFrameEnableDown,'h3cIfMonTxPauseFrameEnableDown':h3cIfMonTxPauseFrameEnableDown,'h3cIfMonTrap':h3cIfMonTrap,'h3cIfMonTrapPrex':h3cIfMonTrapPrex,'h3cIfMonInputRateRising':h3cIfMonInputRateRising,'h3cIfMonInputRateResume':h3cIfMonInputRateResume,'h3cIfMonOutputRateRising':h3cIfMonOutputRateRising,'h3cIfMonOutputRateResume':h3cIfMonOutputRateResume,'h3cIfMonInputErrorAlarmRising':h3cIfMonInputErrorAlarmRising,'h3cIfMonInputErrorAlarmResume':h3cIfMonInputErrorAlarmResume,'h3cIfMonOutputErrorAlarmRising':h3cIfMonOutputErrorAlarmRising,'h3cIfMonOutputErrorAlarmResume':h3cIfMonOutputErrorAlarmResume,'h3cIfMonSdhErrorRising':h3cIfMonSdhErrorRising,'h3cIfMonSdhErrorResume':h3cIfMonSdhErrorResume,'h3cIfMonSdhB1ErrorRising':h3cIfMonSdhB1ErrorRising,'h3cIfMonSdhB1ErrorResume':h3cIfMonSdhB1ErrorResume,'h3cIfMonSdhB2ErrorRising':h3cIfMonSdhB2ErrorRising,'h3cIfMonSdhB2ErrorResume':h3cIfMonSdhB2ErrorResume,'h3cIfMonCRCErrorRising':h3cIfMonCRCErrorRising,'h3cIfMonCRCErrorResume':h3cIfMonCRCErrorResume,'h3cIfMonPauseFrameRising':h3cIfMonPauseFrameRising,'h3cIfMonPauseFrameResume':h3cIfMonPauseFrameResume,'h3cIfMonTxPauseFrameRising':h3cIfMonTxPauseFrameRising,'h3cIfMonTxPauseFrameResume':h3cIfMonTxPauseFrameResume,'h3cIfMonTrapObject':h3cIfMonTrapObject})