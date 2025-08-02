_S='h3cIfDiscardPktRateUpperLimit'
_R='h3cIfDiscardPktRate'
_Q='h3cIfBandwidthUpperLimit'
_P='h3cIfBandwidthRate'
_O='h3cIfLinkModeIndex'
_N='h3cRTSubIfOrdinal'
_M='h3cRTSubIfParentIfIndex'
_L='h3cRTParentIfIndex'
_K='DisplayString'
_J='seconds'
_I='ifDescr'
_H='not-accessible'
_G='Integer32'
_F='ifIndex'
_E='read-write'
_D='IF-MIB'
_C='A3COM-HUAWEI-IF-EXT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_I,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cIfExt=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,40))
if mibBuilder.loadTexts:h3cIfExt.setRevisions(('2009-05-06 19:36','2004-11-13 19:36'))
_H3cIfExtScalarGroup_ObjectIdentity=ObjectIdentity
h3cIfExtScalarGroup=_H3cIfExtScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,1))
_H3cIfStatGlobalFlowInterval_Type=Integer32
_H3cIfStatGlobalFlowInterval_Object=MibScalar
h3cIfStatGlobalFlowInterval=_H3cIfStatGlobalFlowInterval_Object((1,3,6,1,4,1,43,45,1,10,2,40,1,1),_H3cIfStatGlobalFlowInterval_Type())
h3cIfStatGlobalFlowInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatGlobalFlowInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cIfStatGlobalFlowInterval.setUnits(_J)
_H3cIfExtGroup_ObjectIdentity=ObjectIdentity
h3cIfExtGroup=_H3cIfExtGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,2))
_H3cIfStat_ObjectIdentity=ObjectIdentity
h3cIfStat=_H3cIfStat_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,2,1))
_H3cIfStatScalarGroup_ObjectIdentity=ObjectIdentity
h3cIfStatScalarGroup=_H3cIfStatScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,2,1,1))
_H3cIfStatTable_ObjectIdentity=ObjectIdentity
h3cIfStatTable=_H3cIfStatTable_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2))
_H3cIfFlowStatTable_Object=MibTable
h3cIfFlowStatTable=_H3cIfFlowStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1))
if mibBuilder.loadTexts:h3cIfFlowStatTable.setStatus(_A)
_H3cIfStatEntry_Object=MibTableRow
h3cIfStatEntry=_H3cIfStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1))
h3cIfStatEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cIfStatEntry.setStatus(_A)
_H3cIfStatFlowInterval_Type=Integer32
_H3cIfStatFlowInterval_Object=MibTableColumn
h3cIfStatFlowInterval=_H3cIfStatFlowInterval_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1,1),_H3cIfStatFlowInterval_Type())
h3cIfStatFlowInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfStatFlowInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cIfStatFlowInterval.setUnits(_J)
_H3cIfStatFlowInBits_Type=Unsigned32
_H3cIfStatFlowInBits_Object=MibTableColumn
h3cIfStatFlowInBits=_H3cIfStatFlowInBits_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1,2),_H3cIfStatFlowInBits_Type())
h3cIfStatFlowInBits.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowInBits.setStatus(_A)
_H3cIfStatFlowOutBits_Type=Unsigned32
_H3cIfStatFlowOutBits_Object=MibTableColumn
h3cIfStatFlowOutBits=_H3cIfStatFlowOutBits_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1,3),_H3cIfStatFlowOutBits_Type())
h3cIfStatFlowOutBits.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowOutBits.setStatus(_A)
_H3cIfStatFlowInPkts_Type=Unsigned32
_H3cIfStatFlowInPkts_Object=MibTableColumn
h3cIfStatFlowInPkts=_H3cIfStatFlowInPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1,4),_H3cIfStatFlowInPkts_Type())
h3cIfStatFlowInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowInPkts.setStatus(_A)
_H3cIfStatFlowOutPkts_Type=Unsigned32
_H3cIfStatFlowOutPkts_Object=MibTableColumn
h3cIfStatFlowOutPkts=_H3cIfStatFlowOutPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1,5),_H3cIfStatFlowOutPkts_Type())
h3cIfStatFlowOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowOutPkts.setStatus(_A)
_H3cIfStatFlowInBytes_Type=Unsigned32
_H3cIfStatFlowInBytes_Object=MibTableColumn
h3cIfStatFlowInBytes=_H3cIfStatFlowInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1,6),_H3cIfStatFlowInBytes_Type())
h3cIfStatFlowInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowInBytes.setStatus(_A)
_H3cIfStatFlowOutBytes_Type=Unsigned32
_H3cIfStatFlowOutBytes_Object=MibTableColumn
h3cIfStatFlowOutBytes=_H3cIfStatFlowOutBytes_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,1,1,7),_H3cIfStatFlowOutBytes_Type())
h3cIfStatFlowOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowOutBytes.setStatus(_A)
_H3cIfSpeedStatTable_Object=MibTable
h3cIfSpeedStatTable=_H3cIfSpeedStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,2))
if mibBuilder.loadTexts:h3cIfSpeedStatTable.setStatus(_A)
_H3cIfSpeedStatEntry_Object=MibTableRow
h3cIfSpeedStatEntry=_H3cIfSpeedStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,2,1))
h3cIfSpeedStatEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cIfSpeedStatEntry.setStatus(_A)
_H3cIfSpeedStatInterval_Type=Integer32
_H3cIfSpeedStatInterval_Object=MibTableColumn
h3cIfSpeedStatInterval=_H3cIfSpeedStatInterval_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,2,1,1),_H3cIfSpeedStatInterval_Type())
h3cIfSpeedStatInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfSpeedStatInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cIfSpeedStatInterval.setUnits(_J)
_H3cIfSpeedStatInPkts_Type=Unsigned32
_H3cIfSpeedStatInPkts_Object=MibTableColumn
h3cIfSpeedStatInPkts=_H3cIfSpeedStatInPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,2,1,2),_H3cIfSpeedStatInPkts_Type())
h3cIfSpeedStatInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfSpeedStatInPkts.setStatus(_A)
_H3cIfSpeedStatOutPkts_Type=Unsigned32
_H3cIfSpeedStatOutPkts_Object=MibTableColumn
h3cIfSpeedStatOutPkts=_H3cIfSpeedStatOutPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,2,1,3),_H3cIfSpeedStatOutPkts_Type())
h3cIfSpeedStatOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfSpeedStatOutPkts.setStatus(_A)
_H3cIfSpeedStatInBytes_Type=Unsigned32
_H3cIfSpeedStatInBytes_Object=MibTableColumn
h3cIfSpeedStatInBytes=_H3cIfSpeedStatInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,2,1,4),_H3cIfSpeedStatInBytes_Type())
h3cIfSpeedStatInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfSpeedStatInBytes.setStatus(_A)
_H3cIfSpeedStatOutBytes_Type=Unsigned32
_H3cIfSpeedStatOutBytes_Object=MibTableColumn
h3cIfSpeedStatOutBytes=_H3cIfSpeedStatOutBytes_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,2,1,5),_H3cIfSpeedStatOutBytes_Type())
h3cIfSpeedStatOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfSpeedStatOutBytes.setStatus(_A)
_H3cIfHCFlowStatTable_Object=MibTable
h3cIfHCFlowStatTable=_H3cIfHCFlowStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3))
if mibBuilder.loadTexts:h3cIfHCFlowStatTable.setStatus(_A)
_H3cIfHCFlowStatEntry_Object=MibTableRow
h3cIfHCFlowStatEntry=_H3cIfHCFlowStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3,1))
h3cIfHCFlowStatEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cIfHCFlowStatEntry.setStatus(_A)
_H3cIfStatFlowHCInBits_Type=CounterBasedGauge64
_H3cIfStatFlowHCInBits_Object=MibTableColumn
h3cIfStatFlowHCInBits=_H3cIfStatFlowHCInBits_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3,1,1),_H3cIfStatFlowHCInBits_Type())
h3cIfStatFlowHCInBits.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowHCInBits.setStatus(_A)
_H3cIfStatFlowHCOutBits_Type=CounterBasedGauge64
_H3cIfStatFlowHCOutBits_Object=MibTableColumn
h3cIfStatFlowHCOutBits=_H3cIfStatFlowHCOutBits_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3,1,2),_H3cIfStatFlowHCOutBits_Type())
h3cIfStatFlowHCOutBits.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowHCOutBits.setStatus(_A)
_H3cIfStatFlowHCInPkts_Type=CounterBasedGauge64
_H3cIfStatFlowHCInPkts_Object=MibTableColumn
h3cIfStatFlowHCInPkts=_H3cIfStatFlowHCInPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3,1,3),_H3cIfStatFlowHCInPkts_Type())
h3cIfStatFlowHCInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowHCInPkts.setStatus(_A)
_H3cIfStatFlowHCOutPkts_Type=CounterBasedGauge64
_H3cIfStatFlowHCOutPkts_Object=MibTableColumn
h3cIfStatFlowHCOutPkts=_H3cIfStatFlowHCOutPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3,1,4),_H3cIfStatFlowHCOutPkts_Type())
h3cIfStatFlowHCOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowHCOutPkts.setStatus(_A)
_H3cIfStatFlowHCInBytes_Type=CounterBasedGauge64
_H3cIfStatFlowHCInBytes_Object=MibTableColumn
h3cIfStatFlowHCInBytes=_H3cIfStatFlowHCInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3,1,5),_H3cIfStatFlowHCInBytes_Type())
h3cIfStatFlowHCInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowHCInBytes.setStatus(_A)
_H3cIfStatFlowHCOutBytes_Type=CounterBasedGauge64
_H3cIfStatFlowHCOutBytes_Object=MibTableColumn
h3cIfStatFlowHCOutBytes=_H3cIfStatFlowHCOutBytes_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,1,2,3,1,6),_H3cIfStatFlowHCOutBytes_Type())
h3cIfStatFlowHCOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatFlowHCOutBytes.setStatus(_A)
_H3cIfControl_ObjectIdentity=ObjectIdentity
h3cIfControl=_H3cIfControl_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,2,2))
_H3cRTParentIfTable_Object=MibTable
h3cRTParentIfTable=_H3cRTParentIfTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,1))
if mibBuilder.loadTexts:h3cRTParentIfTable.setStatus(_A)
_H3cRTParentIfEntry_Object=MibTableRow
h3cRTParentIfEntry=_H3cRTParentIfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,1,1))
h3cRTParentIfEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:h3cRTParentIfEntry.setStatus(_A)
_H3cRTParentIfIndex_Type=Integer32
_H3cRTParentIfIndex_Object=MibTableColumn
h3cRTParentIfIndex=_H3cRTParentIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,1,1,1),_H3cRTParentIfIndex_Type())
h3cRTParentIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cRTParentIfIndex.setStatus(_A)
_H3cRTMinSubIfOrdinal_Type=Integer32
_H3cRTMinSubIfOrdinal_Object=MibTableColumn
h3cRTMinSubIfOrdinal=_H3cRTMinSubIfOrdinal_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,1,1,2),_H3cRTMinSubIfOrdinal_Type())
h3cRTMinSubIfOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRTMinSubIfOrdinal.setStatus(_A)
_H3cRTMaxSubIfOrdinal_Type=Integer32
_H3cRTMaxSubIfOrdinal_Object=MibTableColumn
h3cRTMaxSubIfOrdinal=_H3cRTMaxSubIfOrdinal_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,1,1,3),_H3cRTMaxSubIfOrdinal_Type())
h3cRTMaxSubIfOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRTMaxSubIfOrdinal.setStatus(_A)
_H3cRTSubIfTable_Object=MibTable
h3cRTSubIfTable=_H3cRTSubIfTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,2))
if mibBuilder.loadTexts:h3cRTSubIfTable.setStatus(_A)
_H3cRTSubIfEntry_Object=MibTableRow
h3cRTSubIfEntry=_H3cRTSubIfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,2,1))
h3cRTSubIfEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:h3cRTSubIfEntry.setStatus(_A)
_H3cRTSubIfParentIfIndex_Type=Integer32
_H3cRTSubIfParentIfIndex_Object=MibTableColumn
h3cRTSubIfParentIfIndex=_H3cRTSubIfParentIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,2,1,1),_H3cRTSubIfParentIfIndex_Type())
h3cRTSubIfParentIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cRTSubIfParentIfIndex.setStatus(_A)
_H3cRTSubIfOrdinal_Type=Integer32
_H3cRTSubIfOrdinal_Object=MibTableColumn
h3cRTSubIfOrdinal=_H3cRTSubIfOrdinal_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,2,1,2),_H3cRTSubIfOrdinal_Type())
h3cRTSubIfOrdinal.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cRTSubIfOrdinal.setStatus(_A)
_H3cRTSubIfSubIfIndex_Type=Integer32
_H3cRTSubIfSubIfIndex_Object=MibTableColumn
h3cRTSubIfSubIfIndex=_H3cRTSubIfSubIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,2,1,3),_H3cRTSubIfSubIfIndex_Type())
h3cRTSubIfSubIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRTSubIfSubIfIndex.setStatus(_A)
class _H3cRTSubIfSubIfDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cRTSubIfSubIfDesc_Type.__name__=_K
_H3cRTSubIfSubIfDesc_Object=MibTableColumn
h3cRTSubIfSubIfDesc=_H3cRTSubIfSubIfDesc_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,2,1,4),_H3cRTSubIfSubIfDesc_Type())
h3cRTSubIfSubIfDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRTSubIfSubIfDesc.setStatus(_A)
_H3cRTSubIfRowStatus_Type=RowStatus
_H3cRTSubIfRowStatus_Object=MibTableColumn
h3cRTSubIfRowStatus=_H3cRTSubIfRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,2,1,5),_H3cRTSubIfRowStatus_Type())
h3cRTSubIfRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:h3cRTSubIfRowStatus.setStatus(_A)
_H3cIfLinkModeTable_Object=MibTable
h3cIfLinkModeTable=_H3cIfLinkModeTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,3))
if mibBuilder.loadTexts:h3cIfLinkModeTable.setStatus(_A)
_H3cIfLinkModeEntry_Object=MibTableRow
h3cIfLinkModeEntry=_H3cIfLinkModeEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,3,1))
h3cIfLinkModeEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:h3cIfLinkModeEntry.setStatus(_A)
_H3cIfLinkModeIndex_Type=Integer32
_H3cIfLinkModeIndex_Object=MibTableColumn
h3cIfLinkModeIndex=_H3cIfLinkModeIndex_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,3,1,1),_H3cIfLinkModeIndex_Type())
h3cIfLinkModeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIfLinkModeIndex.setStatus(_A)
class _H3cIfLinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridgeMode',1),('routeMode',2)))
_H3cIfLinkMode_Type.__name__=_G
_H3cIfLinkMode_Object=MibTableColumn
h3cIfLinkMode=_H3cIfLinkMode_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,3,1,2),_H3cIfLinkMode_Type())
h3cIfLinkMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfLinkMode.setStatus(_A)
_H3cIfLinkModeSwitchSupport_Type=TruthValue
_H3cIfLinkModeSwitchSupport_Object=MibTableColumn
h3cIfLinkModeSwitchSupport=_H3cIfLinkModeSwitchSupport_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,2,3,1,3),_H3cIfLinkModeSwitchSupport_Type())
h3cIfLinkModeSwitchSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfLinkModeSwitchSupport.setStatus(_A)
_H3cIfInterfaces_ObjectIdentity=ObjectIdentity
h3cIfInterfaces=_H3cIfInterfaces_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,2,3))
_H3cIfPhysicalNumber_Type=Integer32
_H3cIfPhysicalNumber_Object=MibScalar
h3cIfPhysicalNumber=_H3cIfPhysicalNumber_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,1),_H3cIfPhysicalNumber_Type())
h3cIfPhysicalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfPhysicalNumber.setStatus(_A)
_H3cIfTable_Object=MibTable
h3cIfTable=_H3cIfTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2))
if mibBuilder.loadTexts:h3cIfTable.setStatus(_A)
_H3cIfEntry_Object=MibTableRow
h3cIfEntry=_H3cIfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1))
h3cIfEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cIfEntry.setStatus(_A)
_H3cIfUpDownTimes_Type=Integer32
_H3cIfUpDownTimes_Object=MibTableColumn
h3cIfUpDownTimes=_H3cIfUpDownTimes_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,1),_H3cIfUpDownTimes_Type())
h3cIfUpDownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfUpDownTimes.setStatus(_A)
_H3cIfMtu_Type=Integer32
_H3cIfMtu_Object=MibTableColumn
h3cIfMtu=_H3cIfMtu_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,2),_H3cIfMtu_Type())
h3cIfMtu.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfMtu.setStatus(_A)
class _H3cIfBandwidthRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cIfBandwidthRate_Type.__name__=_G
_H3cIfBandwidthRate_Object=MibTableColumn
h3cIfBandwidthRate=_H3cIfBandwidthRate_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,3),_H3cIfBandwidthRate_Type())
h3cIfBandwidthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfBandwidthRate.setStatus(_A)
class _H3cIfDiscardPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cIfDiscardPktRate_Type.__name__=_G
_H3cIfDiscardPktRate_Object=MibTableColumn
h3cIfDiscardPktRate=_H3cIfDiscardPktRate_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,4),_H3cIfDiscardPktRate_Type())
h3cIfDiscardPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfDiscardPktRate.setStatus(_A)
_H3cIfStatusKeepTime_Type=TimeTicks
_H3cIfStatusKeepTime_Object=MibTableColumn
h3cIfStatusKeepTime=_H3cIfStatusKeepTime_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,5),_H3cIfStatusKeepTime_Type())
h3cIfStatusKeepTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfStatusKeepTime.setStatus(_A)
_H3cIfInNUcastPkts_Type=Counter64
_H3cIfInNUcastPkts_Object=MibTableColumn
h3cIfInNUcastPkts=_H3cIfInNUcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,6),_H3cIfInNUcastPkts_Type())
h3cIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfInNUcastPkts.setStatus(_A)
_H3cIfOutNUcastPkts_Type=Counter64
_H3cIfOutNUcastPkts_Object=MibTableColumn
h3cIfOutNUcastPkts=_H3cIfOutNUcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,7),_H3cIfOutNUcastPkts_Type())
h3cIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfOutNUcastPkts.setStatus(_A)
_H3cIfIsPoe_Type=TruthValue
_H3cIfIsPoe_Object=MibTableColumn
h3cIfIsPoe=_H3cIfIsPoe_Object((1,3,6,1,4,1,43,45,1,10,2,40,2,3,2,1,8),_H3cIfIsPoe_Type())
h3cIfIsPoe.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfIsPoe.setStatus(_A)
_H3cIfExtTrap_ObjectIdentity=ObjectIdentity
h3cIfExtTrap=_H3cIfExtTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,3))
_H3cIfExtTrapPrex_ObjectIdentity=ObjectIdentity
h3cIfExtTrapPrex=_H3cIfExtTrapPrex_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,3,0))
_H3cIfExtTrapObject_ObjectIdentity=ObjectIdentity
h3cIfExtTrapObject=_H3cIfExtTrapObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,40,3,1))
_H3cIfExtTrapCfgTable_Object=MibTable
h3cIfExtTrapCfgTable=_H3cIfExtTrapCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,40,3,1,1))
if mibBuilder.loadTexts:h3cIfExtTrapCfgTable.setStatus(_A)
_H3cIfExtTrapCfgEntry_Object=MibTableRow
h3cIfExtTrapCfgEntry=_H3cIfExtTrapCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,40,3,1,1,1))
h3cIfExtTrapCfgEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cIfExtTrapCfgEntry.setStatus(_A)
class _H3cIfBandwidthUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cIfBandwidthUpperLimit_Type.__name__=_G
_H3cIfBandwidthUpperLimit_Object=MibTableColumn
h3cIfBandwidthUpperLimit=_H3cIfBandwidthUpperLimit_Object((1,3,6,1,4,1,43,45,1,10,2,40,3,1,1,1,1),_H3cIfBandwidthUpperLimit_Type())
h3cIfBandwidthUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfBandwidthUpperLimit.setStatus(_A)
class _H3cIfDiscardPktRateUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cIfDiscardPktRateUpperLimit_Type.__name__=_G
_H3cIfDiscardPktRateUpperLimit_Object=MibTableColumn
h3cIfDiscardPktRateUpperLimit=_H3cIfDiscardPktRateUpperLimit_Object((1,3,6,1,4,1,43,45,1,10,2,40,3,1,1,1,2),_H3cIfDiscardPktRateUpperLimit_Type())
h3cIfDiscardPktRateUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIfDiscardPktRateUpperLimit.setStatus(_A)
h3cIfBandwidthUsageHigh=NotificationType((1,3,6,1,4,1,43,45,1,10,2,40,3,0,1))
h3cIfBandwidthUsageHigh.setObjects(*((_D,_I),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:h3cIfBandwidthUsageHigh.setStatus(_A)
h3cIfDiscardPktRateHigh=NotificationType((1,3,6,1,4,1,43,45,1,10,2,40,3,0,2))
h3cIfDiscardPktRateHigh.setObjects(*((_D,_I),(_C,_R),(_C,_S)))
if mibBuilder.loadTexts:h3cIfDiscardPktRateHigh.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cIfExt':h3cIfExt,'h3cIfExtScalarGroup':h3cIfExtScalarGroup,'h3cIfStatGlobalFlowInterval':h3cIfStatGlobalFlowInterval,'h3cIfExtGroup':h3cIfExtGroup,'h3cIfStat':h3cIfStat,'h3cIfStatScalarGroup':h3cIfStatScalarGroup,'h3cIfStatTable':h3cIfStatTable,'h3cIfFlowStatTable':h3cIfFlowStatTable,'h3cIfStatEntry':h3cIfStatEntry,'h3cIfStatFlowInterval':h3cIfStatFlowInterval,'h3cIfStatFlowInBits':h3cIfStatFlowInBits,'h3cIfStatFlowOutBits':h3cIfStatFlowOutBits,'h3cIfStatFlowInPkts':h3cIfStatFlowInPkts,'h3cIfStatFlowOutPkts':h3cIfStatFlowOutPkts,'h3cIfStatFlowInBytes':h3cIfStatFlowInBytes,'h3cIfStatFlowOutBytes':h3cIfStatFlowOutBytes,'h3cIfSpeedStatTable':h3cIfSpeedStatTable,'h3cIfSpeedStatEntry':h3cIfSpeedStatEntry,'h3cIfSpeedStatInterval':h3cIfSpeedStatInterval,'h3cIfSpeedStatInPkts':h3cIfSpeedStatInPkts,'h3cIfSpeedStatOutPkts':h3cIfSpeedStatOutPkts,'h3cIfSpeedStatInBytes':h3cIfSpeedStatInBytes,'h3cIfSpeedStatOutBytes':h3cIfSpeedStatOutBytes,'h3cIfHCFlowStatTable':h3cIfHCFlowStatTable,'h3cIfHCFlowStatEntry':h3cIfHCFlowStatEntry,'h3cIfStatFlowHCInBits':h3cIfStatFlowHCInBits,'h3cIfStatFlowHCOutBits':h3cIfStatFlowHCOutBits,'h3cIfStatFlowHCInPkts':h3cIfStatFlowHCInPkts,'h3cIfStatFlowHCOutPkts':h3cIfStatFlowHCOutPkts,'h3cIfStatFlowHCInBytes':h3cIfStatFlowHCInBytes,'h3cIfStatFlowHCOutBytes':h3cIfStatFlowHCOutBytes,'h3cIfControl':h3cIfControl,'h3cRTParentIfTable':h3cRTParentIfTable,'h3cRTParentIfEntry':h3cRTParentIfEntry,_L:h3cRTParentIfIndex,'h3cRTMinSubIfOrdinal':h3cRTMinSubIfOrdinal,'h3cRTMaxSubIfOrdinal':h3cRTMaxSubIfOrdinal,'h3cRTSubIfTable':h3cRTSubIfTable,'h3cRTSubIfEntry':h3cRTSubIfEntry,_M:h3cRTSubIfParentIfIndex,_N:h3cRTSubIfOrdinal,'h3cRTSubIfSubIfIndex':h3cRTSubIfSubIfIndex,'h3cRTSubIfSubIfDesc':h3cRTSubIfSubIfDesc,'h3cRTSubIfRowStatus':h3cRTSubIfRowStatus,'h3cIfLinkModeTable':h3cIfLinkModeTable,'h3cIfLinkModeEntry':h3cIfLinkModeEntry,_O:h3cIfLinkModeIndex,'h3cIfLinkMode':h3cIfLinkMode,'h3cIfLinkModeSwitchSupport':h3cIfLinkModeSwitchSupport,'h3cIfInterfaces':h3cIfInterfaces,'h3cIfPhysicalNumber':h3cIfPhysicalNumber,'h3cIfTable':h3cIfTable,'h3cIfEntry':h3cIfEntry,'h3cIfUpDownTimes':h3cIfUpDownTimes,'h3cIfMtu':h3cIfMtu,_P:h3cIfBandwidthRate,_R:h3cIfDiscardPktRate,'h3cIfStatusKeepTime':h3cIfStatusKeepTime,'h3cIfInNUcastPkts':h3cIfInNUcastPkts,'h3cIfOutNUcastPkts':h3cIfOutNUcastPkts,'h3cIfIsPoe':h3cIfIsPoe,'h3cIfExtTrap':h3cIfExtTrap,'h3cIfExtTrapPrex':h3cIfExtTrapPrex,'h3cIfBandwidthUsageHigh':h3cIfBandwidthUsageHigh,'h3cIfDiscardPktRateHigh':h3cIfDiscardPktRateHigh,'h3cIfExtTrapObject':h3cIfExtTrapObject,'h3cIfExtTrapCfgTable':h3cIfExtTrapCfgTable,'h3cIfExtTrapCfgEntry':h3cIfExtTrapCfgEntry,_Q:h3cIfBandwidthUpperLimit,_S:h3cIfDiscardPktRateUpperLimit})