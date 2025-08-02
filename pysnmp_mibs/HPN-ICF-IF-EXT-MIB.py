_U='hpnicfIfDiscardPktRateUpperLimit'
_T='hpnicfIfDiscardPktRate'
_S='hpnicfIfBandwidthUpperLimit'
_R='hpnicfIfBandwidthRate'
_Q='noUsing'
_P='hpnicfIfUsingIndex'
_O='hpnicfIfLinkModeIndex'
_N='hpnicfRTSubIfOrdinal'
_M='hpnicfRTSubIfParentIfIndex'
_L='hpnicfRTParentIfIndex'
_K='DisplayString'
_J='seconds'
_I='not-accessible'
_H='ifDescr'
_G='ifIndex'
_F='read-write'
_E='HPN-ICF-IF-EXT-MIB'
_D='IF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_H,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfIfExt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40))
if mibBuilder.loadTexts:hpnicfIfExt.setRevisions(('2009-05-06 19:36','2004-11-13 19:36'))
_HpnicfIfExtScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfIfExtScalarGroup=_HpnicfIfExtScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,1))
_HpnicfIfStatGlobalFlowInterval_Type=Integer32
_HpnicfIfStatGlobalFlowInterval_Object=MibScalar
hpnicfIfStatGlobalFlowInterval=_HpnicfIfStatGlobalFlowInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,1,1),_HpnicfIfStatGlobalFlowInterval_Type())
hpnicfIfStatGlobalFlowInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfStatGlobalFlowInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfIfStatGlobalFlowInterval.setUnits(_J)
_HpnicfIfShutDownInterval_Type=Integer32
_HpnicfIfShutDownInterval_Object=MibScalar
hpnicfIfShutDownInterval=_HpnicfIfShutDownInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,1,2),_HpnicfIfShutDownInterval_Type())
hpnicfIfShutDownInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfShutDownInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfIfShutDownInterval.setUnits(_J)
_HpnicfIfExtGroup_ObjectIdentity=ObjectIdentity
hpnicfIfExtGroup=_HpnicfIfExtGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,2))
_HpnicfIfStat_ObjectIdentity=ObjectIdentity
hpnicfIfStat=_HpnicfIfStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1))
_HpnicfIfStatScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfIfStatScalarGroup=_HpnicfIfStatScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,1))
_HpnicfIfStatTable_ObjectIdentity=ObjectIdentity
hpnicfIfStatTable=_HpnicfIfStatTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2))
_HpnicfIfFlowStatTable_Object=MibTable
hpnicfIfFlowStatTable=_HpnicfIfFlowStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1))
if mibBuilder.loadTexts:hpnicfIfFlowStatTable.setStatus(_A)
_HpnicfIfFlowStatEntry_Object=MibTableRow
hpnicfIfFlowStatEntry=_HpnicfIfFlowStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1))
hpnicfIfFlowStatEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfIfFlowStatEntry.setStatus(_A)
_HpnicfIfStatFlowInterval_Type=Integer32
_HpnicfIfStatFlowInterval_Object=MibTableColumn
hpnicfIfStatFlowInterval=_HpnicfIfStatFlowInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1,1),_HpnicfIfStatFlowInterval_Type())
hpnicfIfStatFlowInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfStatFlowInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfIfStatFlowInterval.setUnits(_J)
_HpnicfIfStatFlowInBits_Type=Unsigned32
_HpnicfIfStatFlowInBits_Object=MibTableColumn
hpnicfIfStatFlowInBits=_HpnicfIfStatFlowInBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1,2),_HpnicfIfStatFlowInBits_Type())
hpnicfIfStatFlowInBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowInBits.setStatus(_A)
_HpnicfIfStatFlowOutBits_Type=Unsigned32
_HpnicfIfStatFlowOutBits_Object=MibTableColumn
hpnicfIfStatFlowOutBits=_HpnicfIfStatFlowOutBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1,3),_HpnicfIfStatFlowOutBits_Type())
hpnicfIfStatFlowOutBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowOutBits.setStatus(_A)
_HpnicfIfStatFlowInPkts_Type=Unsigned32
_HpnicfIfStatFlowInPkts_Object=MibTableColumn
hpnicfIfStatFlowInPkts=_HpnicfIfStatFlowInPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1,4),_HpnicfIfStatFlowInPkts_Type())
hpnicfIfStatFlowInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowInPkts.setStatus(_A)
_HpnicfIfStatFlowOutPkts_Type=Unsigned32
_HpnicfIfStatFlowOutPkts_Object=MibTableColumn
hpnicfIfStatFlowOutPkts=_HpnicfIfStatFlowOutPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1,5),_HpnicfIfStatFlowOutPkts_Type())
hpnicfIfStatFlowOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowOutPkts.setStatus(_A)
_HpnicfIfStatFlowInBytes_Type=Unsigned32
_HpnicfIfStatFlowInBytes_Object=MibTableColumn
hpnicfIfStatFlowInBytes=_HpnicfIfStatFlowInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1,6),_HpnicfIfStatFlowInBytes_Type())
hpnicfIfStatFlowInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowInBytes.setStatus(_A)
_HpnicfIfStatFlowOutBytes_Type=Unsigned32
_HpnicfIfStatFlowOutBytes_Object=MibTableColumn
hpnicfIfStatFlowOutBytes=_HpnicfIfStatFlowOutBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,1,1,7),_HpnicfIfStatFlowOutBytes_Type())
hpnicfIfStatFlowOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowOutBytes.setStatus(_A)
_HpnicfIfSpeedStatTable_Object=MibTable
hpnicfIfSpeedStatTable=_HpnicfIfSpeedStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,2))
if mibBuilder.loadTexts:hpnicfIfSpeedStatTable.setStatus(_A)
_HpnicfIfSpeedStatEntry_Object=MibTableRow
hpnicfIfSpeedStatEntry=_HpnicfIfSpeedStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,2,1))
hpnicfIfSpeedStatEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfIfSpeedStatEntry.setStatus(_A)
_HpnicfIfSpeedStatInterval_Type=Integer32
_HpnicfIfSpeedStatInterval_Object=MibTableColumn
hpnicfIfSpeedStatInterval=_HpnicfIfSpeedStatInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,2,1,1),_HpnicfIfSpeedStatInterval_Type())
hpnicfIfSpeedStatInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfSpeedStatInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfIfSpeedStatInterval.setUnits(_J)
_HpnicfIfSpeedStatInPkts_Type=Unsigned32
_HpnicfIfSpeedStatInPkts_Object=MibTableColumn
hpnicfIfSpeedStatInPkts=_HpnicfIfSpeedStatInPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,2,1,2),_HpnicfIfSpeedStatInPkts_Type())
hpnicfIfSpeedStatInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfSpeedStatInPkts.setStatus(_A)
_HpnicfIfSpeedStatOutPkts_Type=Unsigned32
_HpnicfIfSpeedStatOutPkts_Object=MibTableColumn
hpnicfIfSpeedStatOutPkts=_HpnicfIfSpeedStatOutPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,2,1,3),_HpnicfIfSpeedStatOutPkts_Type())
hpnicfIfSpeedStatOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfSpeedStatOutPkts.setStatus(_A)
_HpnicfIfSpeedStatInBytes_Type=Unsigned32
_HpnicfIfSpeedStatInBytes_Object=MibTableColumn
hpnicfIfSpeedStatInBytes=_HpnicfIfSpeedStatInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,2,1,4),_HpnicfIfSpeedStatInBytes_Type())
hpnicfIfSpeedStatInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfSpeedStatInBytes.setStatus(_A)
_HpnicfIfSpeedStatOutBytes_Type=Unsigned32
_HpnicfIfSpeedStatOutBytes_Object=MibTableColumn
hpnicfIfSpeedStatOutBytes=_HpnicfIfSpeedStatOutBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,2,1,5),_HpnicfIfSpeedStatOutBytes_Type())
hpnicfIfSpeedStatOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfSpeedStatOutBytes.setStatus(_A)
_HpnicfIfHCFlowStatTable_Object=MibTable
hpnicfIfHCFlowStatTable=_HpnicfIfHCFlowStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3))
if mibBuilder.loadTexts:hpnicfIfHCFlowStatTable.setStatus(_A)
_HpnicfIfHCFlowStatEntry_Object=MibTableRow
hpnicfIfHCFlowStatEntry=_HpnicfIfHCFlowStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3,1))
hpnicfIfHCFlowStatEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfIfHCFlowStatEntry.setStatus(_A)
_HpnicfIfStatFlowHCInBits_Type=CounterBasedGauge64
_HpnicfIfStatFlowHCInBits_Object=MibTableColumn
hpnicfIfStatFlowHCInBits=_HpnicfIfStatFlowHCInBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3,1,1),_HpnicfIfStatFlowHCInBits_Type())
hpnicfIfStatFlowHCInBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowHCInBits.setStatus(_A)
_HpnicfIfStatFlowHCOutBits_Type=CounterBasedGauge64
_HpnicfIfStatFlowHCOutBits_Object=MibTableColumn
hpnicfIfStatFlowHCOutBits=_HpnicfIfStatFlowHCOutBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3,1,2),_HpnicfIfStatFlowHCOutBits_Type())
hpnicfIfStatFlowHCOutBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowHCOutBits.setStatus(_A)
_HpnicfIfStatFlowHCInPkts_Type=CounterBasedGauge64
_HpnicfIfStatFlowHCInPkts_Object=MibTableColumn
hpnicfIfStatFlowHCInPkts=_HpnicfIfStatFlowHCInPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3,1,3),_HpnicfIfStatFlowHCInPkts_Type())
hpnicfIfStatFlowHCInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowHCInPkts.setStatus(_A)
_HpnicfIfStatFlowHCOutPkts_Type=CounterBasedGauge64
_HpnicfIfStatFlowHCOutPkts_Object=MibTableColumn
hpnicfIfStatFlowHCOutPkts=_HpnicfIfStatFlowHCOutPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3,1,4),_HpnicfIfStatFlowHCOutPkts_Type())
hpnicfIfStatFlowHCOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowHCOutPkts.setStatus(_A)
_HpnicfIfStatFlowHCInBytes_Type=CounterBasedGauge64
_HpnicfIfStatFlowHCInBytes_Object=MibTableColumn
hpnicfIfStatFlowHCInBytes=_HpnicfIfStatFlowHCInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3,1,5),_HpnicfIfStatFlowHCInBytes_Type())
hpnicfIfStatFlowHCInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowHCInBytes.setStatus(_A)
_HpnicfIfStatFlowHCOutBytes_Type=CounterBasedGauge64
_HpnicfIfStatFlowHCOutBytes_Object=MibTableColumn
hpnicfIfStatFlowHCOutBytes=_HpnicfIfStatFlowHCOutBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,1,2,3,1,6),_HpnicfIfStatFlowHCOutBytes_Type())
hpnicfIfStatFlowHCOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatFlowHCOutBytes.setStatus(_A)
_HpnicfIfControl_ObjectIdentity=ObjectIdentity
hpnicfIfControl=_HpnicfIfControl_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2))
_HpnicfRTParentIfTable_Object=MibTable
hpnicfRTParentIfTable=_HpnicfRTParentIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,1))
if mibBuilder.loadTexts:hpnicfRTParentIfTable.setStatus(_A)
_HpnicfRTParentIfEntry_Object=MibTableRow
hpnicfRTParentIfEntry=_HpnicfRTParentIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,1,1))
hpnicfRTParentIfEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hpnicfRTParentIfEntry.setStatus(_A)
class _HpnicfRTParentIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfRTParentIfIndex_Type.__name__=_C
_HpnicfRTParentIfIndex_Object=MibTableColumn
hpnicfRTParentIfIndex=_HpnicfRTParentIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,1,1,1),_HpnicfRTParentIfIndex_Type())
hpnicfRTParentIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRTParentIfIndex.setStatus(_A)
_HpnicfRTMinSubIfOrdinal_Type=Integer32
_HpnicfRTMinSubIfOrdinal_Object=MibTableColumn
hpnicfRTMinSubIfOrdinal=_HpnicfRTMinSubIfOrdinal_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,1,1,2),_HpnicfRTMinSubIfOrdinal_Type())
hpnicfRTMinSubIfOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTMinSubIfOrdinal.setStatus(_A)
_HpnicfRTMaxSubIfOrdinal_Type=Integer32
_HpnicfRTMaxSubIfOrdinal_Object=MibTableColumn
hpnicfRTMaxSubIfOrdinal=_HpnicfRTMaxSubIfOrdinal_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,1,1,3),_HpnicfRTMaxSubIfOrdinal_Type())
hpnicfRTMaxSubIfOrdinal.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTMaxSubIfOrdinal.setStatus(_A)
_HpnicfRTSubIfTable_Object=MibTable
hpnicfRTSubIfTable=_HpnicfRTSubIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,2))
if mibBuilder.loadTexts:hpnicfRTSubIfTable.setStatus(_A)
_HpnicfRTSubIfEntry_Object=MibTableRow
hpnicfRTSubIfEntry=_HpnicfRTSubIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,2,1))
hpnicfRTSubIfEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:hpnicfRTSubIfEntry.setStatus(_A)
class _HpnicfRTSubIfParentIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfRTSubIfParentIfIndex_Type.__name__=_C
_HpnicfRTSubIfParentIfIndex_Object=MibTableColumn
hpnicfRTSubIfParentIfIndex=_HpnicfRTSubIfParentIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,2,1,1),_HpnicfRTSubIfParentIfIndex_Type())
hpnicfRTSubIfParentIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRTSubIfParentIfIndex.setStatus(_A)
class _HpnicfRTSubIfOrdinal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfRTSubIfOrdinal_Type.__name__=_C
_HpnicfRTSubIfOrdinal_Object=MibTableColumn
hpnicfRTSubIfOrdinal=_HpnicfRTSubIfOrdinal_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,2,1,2),_HpnicfRTSubIfOrdinal_Type())
hpnicfRTSubIfOrdinal.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRTSubIfOrdinal.setStatus(_A)
_HpnicfRTSubIfSubIfIndex_Type=Integer32
_HpnicfRTSubIfSubIfIndex_Object=MibTableColumn
hpnicfRTSubIfSubIfIndex=_HpnicfRTSubIfSubIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,2,1,3),_HpnicfRTSubIfSubIfIndex_Type())
hpnicfRTSubIfSubIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTSubIfSubIfIndex.setStatus(_A)
class _HpnicfRTSubIfSubIfDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfRTSubIfSubIfDesc_Type.__name__=_K
_HpnicfRTSubIfSubIfDesc_Object=MibTableColumn
hpnicfRTSubIfSubIfDesc=_HpnicfRTSubIfSubIfDesc_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,2,1,4),_HpnicfRTSubIfSubIfDesc_Type())
hpnicfRTSubIfSubIfDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRTSubIfSubIfDesc.setStatus(_A)
_HpnicfRTSubIfRowStatus_Type=RowStatus
_HpnicfRTSubIfRowStatus_Object=MibTableColumn
hpnicfRTSubIfRowStatus=_HpnicfRTSubIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,2,1,5),_HpnicfRTSubIfRowStatus_Type())
hpnicfRTSubIfRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfRTSubIfRowStatus.setStatus(_A)
_HpnicfIfLinkModeTable_Object=MibTable
hpnicfIfLinkModeTable=_HpnicfIfLinkModeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,3))
if mibBuilder.loadTexts:hpnicfIfLinkModeTable.setStatus(_A)
_HpnicfIfLinkModeEntry_Object=MibTableRow
hpnicfIfLinkModeEntry=_HpnicfIfLinkModeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,3,1))
hpnicfIfLinkModeEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hpnicfIfLinkModeEntry.setStatus(_A)
class _HpnicfIfLinkModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIfLinkModeIndex_Type.__name__=_C
_HpnicfIfLinkModeIndex_Object=MibTableColumn
hpnicfIfLinkModeIndex=_HpnicfIfLinkModeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,3,1,1),_HpnicfIfLinkModeIndex_Type())
hpnicfIfLinkModeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfLinkModeIndex.setStatus(_A)
class _HpnicfIfLinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridgeMode',1),('routeMode',2)))
_HpnicfIfLinkMode_Type.__name__=_C
_HpnicfIfLinkMode_Object=MibTableColumn
hpnicfIfLinkMode=_HpnicfIfLinkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,3,1,2),_HpnicfIfLinkMode_Type())
hpnicfIfLinkMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfLinkMode.setStatus(_A)
_HpnicfIfLinkModeSwitchSupport_Type=TruthValue
_HpnicfIfLinkModeSwitchSupport_Object=MibTableColumn
hpnicfIfLinkModeSwitchSupport=_HpnicfIfLinkModeSwitchSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,2,3,1,3),_HpnicfIfLinkModeSwitchSupport_Type())
hpnicfIfLinkModeSwitchSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfLinkModeSwitchSupport.setStatus(_A)
_HpnicfIfInterfaces_ObjectIdentity=ObjectIdentity
hpnicfIfInterfaces=_HpnicfIfInterfaces_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3))
_HpnicfIfPhysicalNumber_Type=Integer32
_HpnicfIfPhysicalNumber_Object=MibScalar
hpnicfIfPhysicalNumber=_HpnicfIfPhysicalNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,1),_HpnicfIfPhysicalNumber_Type())
hpnicfIfPhysicalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfPhysicalNumber.setStatus(_A)
_HpnicfIfTable_Object=MibTable
hpnicfIfTable=_HpnicfIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2))
if mibBuilder.loadTexts:hpnicfIfTable.setStatus(_A)
_HpnicfIfEntry_Object=MibTableRow
hpnicfIfEntry=_HpnicfIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1))
hpnicfIfEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfIfEntry.setStatus(_A)
_HpnicfIfUpDownTimes_Type=Integer32
_HpnicfIfUpDownTimes_Object=MibTableColumn
hpnicfIfUpDownTimes=_HpnicfIfUpDownTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,1),_HpnicfIfUpDownTimes_Type())
hpnicfIfUpDownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfUpDownTimes.setStatus(_A)
_HpnicfIfMtu_Type=Integer32
_HpnicfIfMtu_Object=MibTableColumn
hpnicfIfMtu=_HpnicfIfMtu_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,2),_HpnicfIfMtu_Type())
hpnicfIfMtu.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfMtu.setStatus(_A)
class _HpnicfIfBandwidthRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfIfBandwidthRate_Type.__name__=_C
_HpnicfIfBandwidthRate_Object=MibTableColumn
hpnicfIfBandwidthRate=_HpnicfIfBandwidthRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,3),_HpnicfIfBandwidthRate_Type())
hpnicfIfBandwidthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfBandwidthRate.setStatus(_A)
class _HpnicfIfDiscardPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfIfDiscardPktRate_Type.__name__=_C
_HpnicfIfDiscardPktRate_Object=MibTableColumn
hpnicfIfDiscardPktRate=_HpnicfIfDiscardPktRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,4),_HpnicfIfDiscardPktRate_Type())
hpnicfIfDiscardPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfDiscardPktRate.setStatus(_A)
_HpnicfIfStatusKeepTime_Type=TimeTicks
_HpnicfIfStatusKeepTime_Object=MibTableColumn
hpnicfIfStatusKeepTime=_HpnicfIfStatusKeepTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,5),_HpnicfIfStatusKeepTime_Type())
hpnicfIfStatusKeepTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfStatusKeepTime.setStatus(_A)
_HpnicfIfInNUcastPkts_Type=Counter64
_HpnicfIfInNUcastPkts_Object=MibTableColumn
hpnicfIfInNUcastPkts=_HpnicfIfInNUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,6),_HpnicfIfInNUcastPkts_Type())
hpnicfIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfInNUcastPkts.setStatus(_A)
_HpnicfIfOutNUcastPkts_Type=Counter64
_HpnicfIfOutNUcastPkts_Object=MibTableColumn
hpnicfIfOutNUcastPkts=_HpnicfIfOutNUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,7),_HpnicfIfOutNUcastPkts_Type())
hpnicfIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfOutNUcastPkts.setStatus(_A)
_HpnicfIfIsPoe_Type=TruthValue
_HpnicfIfIsPoe_Object=MibTableColumn
hpnicfIfIsPoe=_HpnicfIfIsPoe_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,8),_HpnicfIfIsPoe_Type())
hpnicfIfIsPoe.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfIsPoe.setStatus(_A)
class _HpnicfIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('admindown',4)))
_HpnicfIfOperStatus_Type.__name__=_C
_HpnicfIfOperStatus_Object=MibTableColumn
hpnicfIfOperStatus=_HpnicfIfOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,9),_HpnicfIfOperStatus_Type())
hpnicfIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfOperStatus.setStatus(_A)
_HpnicfIfDownTimes_Type=Integer32
_HpnicfIfDownTimes_Object=MibTableColumn
hpnicfIfDownTimes=_HpnicfIfDownTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,2,1,10),_HpnicfIfDownTimes_Type())
hpnicfIfDownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfDownTimes.setStatus(_A)
_HpnicfIfUsingTable_Object=MibTable
hpnicfIfUsingTable=_HpnicfIfUsingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,3))
if mibBuilder.loadTexts:hpnicfIfUsingTable.setStatus(_A)
_HpnicfIfUsingEntry_Object=MibTableRow
hpnicfIfUsingEntry=_HpnicfIfUsingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,3,1))
hpnicfIfUsingEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hpnicfIfUsingEntry.setStatus(_A)
class _HpnicfIfUsingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIfUsingIndex_Type.__name__=_C
_HpnicfIfUsingIndex_Object=MibTableColumn
hpnicfIfUsingIndex=_HpnicfIfUsingIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,3,1,1),_HpnicfIfUsingIndex_Type())
hpnicfIfUsingIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfUsingIndex.setStatus(_A)
_HpnicfIfUsingSupportType_Type=Integer32
_HpnicfIfUsingSupportType_Object=MibTableColumn
hpnicfIfUsingSupportType=_HpnicfIfUsingSupportType_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,3,1,2),_HpnicfIfUsingSupportType_Type())
hpnicfIfUsingSupportType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfUsingSupportType.setStatus(_A)
class _HpnicfIfUsingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_Q,0),('using10GE',1),('using20GE',2),('using40GE',3),('using100GE',4)))
_HpnicfIfUsingType_Type.__name__=_C
_HpnicfIfUsingType_Object=MibTableColumn
hpnicfIfUsingType=_HpnicfIfUsingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,3,1,3),_HpnicfIfUsingType_Type())
hpnicfIfUsingType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfUsingType.setStatus(_A)
class _HpnicfIfUsingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('needReboot',1)))
_HpnicfIfUsingStatus_Type.__name__=_C
_HpnicfIfUsingStatus_Object=MibTableColumn
hpnicfIfUsingStatus=_HpnicfIfUsingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,2,3,3,1,4),_HpnicfIfUsingStatus_Type())
hpnicfIfUsingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfUsingStatus.setStatus(_A)
_HpnicfIfExtTrap_ObjectIdentity=ObjectIdentity
hpnicfIfExtTrap=_HpnicfIfExtTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,3))
_HpnicfIfExtTrapPrex_ObjectIdentity=ObjectIdentity
hpnicfIfExtTrapPrex=_HpnicfIfExtTrapPrex_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,3,0))
_HpnicfIfExtTrapObject_ObjectIdentity=ObjectIdentity
hpnicfIfExtTrapObject=_HpnicfIfExtTrapObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,40,3,1))
_HpnicfIfExtTrapCfgTable_Object=MibTable
hpnicfIfExtTrapCfgTable=_HpnicfIfExtTrapCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,3,1,1))
if mibBuilder.loadTexts:hpnicfIfExtTrapCfgTable.setStatus(_A)
_HpnicfIfExtTrapCfgEntry_Object=MibTableRow
hpnicfIfExtTrapCfgEntry=_HpnicfIfExtTrapCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,3,1,1,1))
hpnicfIfExtTrapCfgEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfIfExtTrapCfgEntry.setStatus(_A)
class _HpnicfIfBandwidthUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfIfBandwidthUpperLimit_Type.__name__=_C
_HpnicfIfBandwidthUpperLimit_Object=MibTableColumn
hpnicfIfBandwidthUpperLimit=_HpnicfIfBandwidthUpperLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,3,1,1,1,1),_HpnicfIfBandwidthUpperLimit_Type())
hpnicfIfBandwidthUpperLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfBandwidthUpperLimit.setStatus(_A)
class _HpnicfIfDiscardPktRateUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfIfDiscardPktRateUpperLimit_Type.__name__=_C
_HpnicfIfDiscardPktRateUpperLimit_Object=MibTableColumn
hpnicfIfDiscardPktRateUpperLimit=_HpnicfIfDiscardPktRateUpperLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,40,3,1,1,1,2),_HpnicfIfDiscardPktRateUpperLimit_Type())
hpnicfIfDiscardPktRateUpperLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfDiscardPktRateUpperLimit.setStatus(_A)
hpnicfIfBandwidthUsageHigh=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,40,3,0,1))
hpnicfIfBandwidthUsageHigh.setObjects(*((_D,_H),(_E,_R),(_E,_S)))
if mibBuilder.loadTexts:hpnicfIfBandwidthUsageHigh.setStatus(_A)
hpnicfIfDiscardPktRateHigh=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,40,3,0,2))
hpnicfIfDiscardPktRateHigh.setObjects(*((_D,_H),(_E,_T),(_E,_U)))
if mibBuilder.loadTexts:hpnicfIfDiscardPktRateHigh.setStatus(_A)
hpnicfIfDampeningSuppressed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,40,3,0,3))
hpnicfIfDampeningSuppressed.setObjects(*((_D,_G),(_D,_H)))
if mibBuilder.loadTexts:hpnicfIfDampeningSuppressed.setStatus(_A)
hpnicfIfDampeningNotSuppressed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,40,3,0,4))
hpnicfIfDampeningNotSuppressed.setObjects(*((_D,_G),(_D,_H)))
if mibBuilder.loadTexts:hpnicfIfDampeningNotSuppressed.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfIfExt':hpnicfIfExt,'hpnicfIfExtScalarGroup':hpnicfIfExtScalarGroup,'hpnicfIfStatGlobalFlowInterval':hpnicfIfStatGlobalFlowInterval,'hpnicfIfShutDownInterval':hpnicfIfShutDownInterval,'hpnicfIfExtGroup':hpnicfIfExtGroup,'hpnicfIfStat':hpnicfIfStat,'hpnicfIfStatScalarGroup':hpnicfIfStatScalarGroup,'hpnicfIfStatTable':hpnicfIfStatTable,'hpnicfIfFlowStatTable':hpnicfIfFlowStatTable,'hpnicfIfFlowStatEntry':hpnicfIfFlowStatEntry,'hpnicfIfStatFlowInterval':hpnicfIfStatFlowInterval,'hpnicfIfStatFlowInBits':hpnicfIfStatFlowInBits,'hpnicfIfStatFlowOutBits':hpnicfIfStatFlowOutBits,'hpnicfIfStatFlowInPkts':hpnicfIfStatFlowInPkts,'hpnicfIfStatFlowOutPkts':hpnicfIfStatFlowOutPkts,'hpnicfIfStatFlowInBytes':hpnicfIfStatFlowInBytes,'hpnicfIfStatFlowOutBytes':hpnicfIfStatFlowOutBytes,'hpnicfIfSpeedStatTable':hpnicfIfSpeedStatTable,'hpnicfIfSpeedStatEntry':hpnicfIfSpeedStatEntry,'hpnicfIfSpeedStatInterval':hpnicfIfSpeedStatInterval,'hpnicfIfSpeedStatInPkts':hpnicfIfSpeedStatInPkts,'hpnicfIfSpeedStatOutPkts':hpnicfIfSpeedStatOutPkts,'hpnicfIfSpeedStatInBytes':hpnicfIfSpeedStatInBytes,'hpnicfIfSpeedStatOutBytes':hpnicfIfSpeedStatOutBytes,'hpnicfIfHCFlowStatTable':hpnicfIfHCFlowStatTable,'hpnicfIfHCFlowStatEntry':hpnicfIfHCFlowStatEntry,'hpnicfIfStatFlowHCInBits':hpnicfIfStatFlowHCInBits,'hpnicfIfStatFlowHCOutBits':hpnicfIfStatFlowHCOutBits,'hpnicfIfStatFlowHCInPkts':hpnicfIfStatFlowHCInPkts,'hpnicfIfStatFlowHCOutPkts':hpnicfIfStatFlowHCOutPkts,'hpnicfIfStatFlowHCInBytes':hpnicfIfStatFlowHCInBytes,'hpnicfIfStatFlowHCOutBytes':hpnicfIfStatFlowHCOutBytes,'hpnicfIfControl':hpnicfIfControl,'hpnicfRTParentIfTable':hpnicfRTParentIfTable,'hpnicfRTParentIfEntry':hpnicfRTParentIfEntry,_L:hpnicfRTParentIfIndex,'hpnicfRTMinSubIfOrdinal':hpnicfRTMinSubIfOrdinal,'hpnicfRTMaxSubIfOrdinal':hpnicfRTMaxSubIfOrdinal,'hpnicfRTSubIfTable':hpnicfRTSubIfTable,'hpnicfRTSubIfEntry':hpnicfRTSubIfEntry,_M:hpnicfRTSubIfParentIfIndex,_N:hpnicfRTSubIfOrdinal,'hpnicfRTSubIfSubIfIndex':hpnicfRTSubIfSubIfIndex,'hpnicfRTSubIfSubIfDesc':hpnicfRTSubIfSubIfDesc,'hpnicfRTSubIfRowStatus':hpnicfRTSubIfRowStatus,'hpnicfIfLinkModeTable':hpnicfIfLinkModeTable,'hpnicfIfLinkModeEntry':hpnicfIfLinkModeEntry,_O:hpnicfIfLinkModeIndex,'hpnicfIfLinkMode':hpnicfIfLinkMode,'hpnicfIfLinkModeSwitchSupport':hpnicfIfLinkModeSwitchSupport,'hpnicfIfInterfaces':hpnicfIfInterfaces,'hpnicfIfPhysicalNumber':hpnicfIfPhysicalNumber,'hpnicfIfTable':hpnicfIfTable,'hpnicfIfEntry':hpnicfIfEntry,'hpnicfIfUpDownTimes':hpnicfIfUpDownTimes,'hpnicfIfMtu':hpnicfIfMtu,_R:hpnicfIfBandwidthRate,_T:hpnicfIfDiscardPktRate,'hpnicfIfStatusKeepTime':hpnicfIfStatusKeepTime,'hpnicfIfInNUcastPkts':hpnicfIfInNUcastPkts,'hpnicfIfOutNUcastPkts':hpnicfIfOutNUcastPkts,'hpnicfIfIsPoe':hpnicfIfIsPoe,'hpnicfIfOperStatus':hpnicfIfOperStatus,'hpnicfIfDownTimes':hpnicfIfDownTimes,'hpnicfIfUsingTable':hpnicfIfUsingTable,'hpnicfIfUsingEntry':hpnicfIfUsingEntry,_P:hpnicfIfUsingIndex,'hpnicfIfUsingSupportType':hpnicfIfUsingSupportType,'hpnicfIfUsingType':hpnicfIfUsingType,'hpnicfIfUsingStatus':hpnicfIfUsingStatus,'hpnicfIfExtTrap':hpnicfIfExtTrap,'hpnicfIfExtTrapPrex':hpnicfIfExtTrapPrex,'hpnicfIfBandwidthUsageHigh':hpnicfIfBandwidthUsageHigh,'hpnicfIfDiscardPktRateHigh':hpnicfIfDiscardPktRateHigh,'hpnicfIfDampeningSuppressed':hpnicfIfDampeningSuppressed,'hpnicfIfDampeningNotSuppressed':hpnicfIfDampeningNotSuppressed,'hpnicfIfExtTrapObject':hpnicfIfExtTrapObject,'hpnicfIfExtTrapCfgTable':hpnicfIfExtTrapCfgTable,'hpnicfIfExtTrapCfgEntry':hpnicfIfExtTrapCfgEntry,_S:hpnicfIfBandwidthUpperLimit,_U:hpnicfIfDiscardPktRateUpperLimit})