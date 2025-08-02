_K='pfLabelsLblIndex'
_J='pfAltqQueueIndex'
_I='pfTablesAddrIndex'
_H='pfTablesTblIndex'
_G='pfInterfacesIfIndex'
_F='1/100th of a Second'
_E='not-accessible'
_D='BEGEMOT-PF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
begemotPf=ModuleIdentity((1,3,6,1,4,1,12325,1,200))
if mibBuilder.loadTexts:begemotPf.setRevisions(('2010-03-18 00:00','2009-12-05 00:00','2005-01-24 00:00'))
_BegemotPfObjects_ObjectIdentity=ObjectIdentity
begemotPfObjects=_BegemotPfObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1))
_PfStatus_ObjectIdentity=ObjectIdentity
pfStatus=_PfStatus_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,1))
_PfStatusRunning_Type=TruthValue
_PfStatusRunning_Object=MibScalar
pfStatusRunning=_PfStatusRunning_Object((1,3,6,1,4,1,12325,1,200,1,1,1),_PfStatusRunning_Type())
pfStatusRunning.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStatusRunning.setStatus(_A)
_PfStatusRuntime_Type=TimeTicks
_PfStatusRuntime_Object=MibScalar
pfStatusRuntime=_PfStatusRuntime_Object((1,3,6,1,4,1,12325,1,200,1,1,2),_PfStatusRuntime_Type())
pfStatusRuntime.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStatusRuntime.setStatus(_A)
if mibBuilder.loadTexts:pfStatusRuntime.setUnits(_F)
class _PfStatusDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('urgent',1),('misc',2),('loud',3)))
_PfStatusDebug_Type.__name__=_C
_PfStatusDebug_Object=MibScalar
pfStatusDebug=_PfStatusDebug_Object((1,3,6,1,4,1,12325,1,200,1,1,3),_PfStatusDebug_Type())
pfStatusDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStatusDebug.setStatus(_A)
_PfStatusHostId_Type=OctetString
_PfStatusHostId_Object=MibScalar
pfStatusHostId=_PfStatusHostId_Object((1,3,6,1,4,1,12325,1,200,1,1,4),_PfStatusHostId_Type())
pfStatusHostId.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStatusHostId.setStatus(_A)
_PfCounter_ObjectIdentity=ObjectIdentity
pfCounter=_PfCounter_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,2))
_PfCounterMatch_Type=Counter64
_PfCounterMatch_Object=MibScalar
pfCounterMatch=_PfCounterMatch_Object((1,3,6,1,4,1,12325,1,200,1,2,1),_PfCounterMatch_Type())
pfCounterMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:pfCounterMatch.setStatus(_A)
_PfCounterBadOffset_Type=Counter64
_PfCounterBadOffset_Object=MibScalar
pfCounterBadOffset=_PfCounterBadOffset_Object((1,3,6,1,4,1,12325,1,200,1,2,2),_PfCounterBadOffset_Type())
pfCounterBadOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:pfCounterBadOffset.setStatus(_A)
_PfCounterFragment_Type=Counter64
_PfCounterFragment_Object=MibScalar
pfCounterFragment=_PfCounterFragment_Object((1,3,6,1,4,1,12325,1,200,1,2,3),_PfCounterFragment_Type())
pfCounterFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:pfCounterFragment.setStatus(_A)
_PfCounterShort_Type=Counter64
_PfCounterShort_Object=MibScalar
pfCounterShort=_PfCounterShort_Object((1,3,6,1,4,1,12325,1,200,1,2,4),_PfCounterShort_Type())
pfCounterShort.setMaxAccess(_B)
if mibBuilder.loadTexts:pfCounterShort.setStatus(_A)
_PfCounterNormalize_Type=Counter64
_PfCounterNormalize_Object=MibScalar
pfCounterNormalize=_PfCounterNormalize_Object((1,3,6,1,4,1,12325,1,200,1,2,5),_PfCounterNormalize_Type())
pfCounterNormalize.setMaxAccess(_B)
if mibBuilder.loadTexts:pfCounterNormalize.setStatus(_A)
_PfCounterMemDrop_Type=Counter64
_PfCounterMemDrop_Object=MibScalar
pfCounterMemDrop=_PfCounterMemDrop_Object((1,3,6,1,4,1,12325,1,200,1,2,6),_PfCounterMemDrop_Type())
pfCounterMemDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:pfCounterMemDrop.setStatus(_A)
_PfStateTable_ObjectIdentity=ObjectIdentity
pfStateTable=_PfStateTable_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,3))
_PfStateTableCount_Type=Unsigned32
_PfStateTableCount_Object=MibScalar
pfStateTableCount=_PfStateTableCount_Object((1,3,6,1,4,1,12325,1,200,1,3,1),_PfStateTableCount_Type())
pfStateTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStateTableCount.setStatus(_A)
_PfStateTableSearches_Type=Counter64
_PfStateTableSearches_Object=MibScalar
pfStateTableSearches=_PfStateTableSearches_Object((1,3,6,1,4,1,12325,1,200,1,3,2),_PfStateTableSearches_Type())
pfStateTableSearches.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStateTableSearches.setStatus(_A)
_PfStateTableInserts_Type=Counter64
_PfStateTableInserts_Object=MibScalar
pfStateTableInserts=_PfStateTableInserts_Object((1,3,6,1,4,1,12325,1,200,1,3,3),_PfStateTableInserts_Type())
pfStateTableInserts.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStateTableInserts.setStatus(_A)
_PfStateTableRemovals_Type=Counter64
_PfStateTableRemovals_Object=MibScalar
pfStateTableRemovals=_PfStateTableRemovals_Object((1,3,6,1,4,1,12325,1,200,1,3,4),_PfStateTableRemovals_Type())
pfStateTableRemovals.setMaxAccess(_B)
if mibBuilder.loadTexts:pfStateTableRemovals.setStatus(_A)
_PfSrcNodes_ObjectIdentity=ObjectIdentity
pfSrcNodes=_PfSrcNodes_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,4))
_PfSrcNodesCount_Type=Unsigned32
_PfSrcNodesCount_Object=MibScalar
pfSrcNodesCount=_PfSrcNodesCount_Object((1,3,6,1,4,1,12325,1,200,1,4,1),_PfSrcNodesCount_Type())
pfSrcNodesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:pfSrcNodesCount.setStatus(_A)
_PfSrcNodesSearches_Type=Counter64
_PfSrcNodesSearches_Object=MibScalar
pfSrcNodesSearches=_PfSrcNodesSearches_Object((1,3,6,1,4,1,12325,1,200,1,4,2),_PfSrcNodesSearches_Type())
pfSrcNodesSearches.setMaxAccess(_B)
if mibBuilder.loadTexts:pfSrcNodesSearches.setStatus(_A)
_PfSrcNodesInserts_Type=Counter64
_PfSrcNodesInserts_Object=MibScalar
pfSrcNodesInserts=_PfSrcNodesInserts_Object((1,3,6,1,4,1,12325,1,200,1,4,3),_PfSrcNodesInserts_Type())
pfSrcNodesInserts.setMaxAccess(_B)
if mibBuilder.loadTexts:pfSrcNodesInserts.setStatus(_A)
_PfSrcNodesRemovals_Type=Counter64
_PfSrcNodesRemovals_Object=MibScalar
pfSrcNodesRemovals=_PfSrcNodesRemovals_Object((1,3,6,1,4,1,12325,1,200,1,4,4),_PfSrcNodesRemovals_Type())
pfSrcNodesRemovals.setMaxAccess(_B)
if mibBuilder.loadTexts:pfSrcNodesRemovals.setStatus(_A)
_PfLimits_ObjectIdentity=ObjectIdentity
pfLimits=_PfLimits_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,5))
_PfLimitsStates_Type=Unsigned32
_PfLimitsStates_Object=MibScalar
pfLimitsStates=_PfLimitsStates_Object((1,3,6,1,4,1,12325,1,200,1,5,1),_PfLimitsStates_Type())
pfLimitsStates.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLimitsStates.setStatus(_A)
_PfLimitsSrcNodes_Type=Unsigned32
_PfLimitsSrcNodes_Object=MibScalar
pfLimitsSrcNodes=_PfLimitsSrcNodes_Object((1,3,6,1,4,1,12325,1,200,1,5,2),_PfLimitsSrcNodes_Type())
pfLimitsSrcNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLimitsSrcNodes.setStatus(_A)
_PfLimitsFrags_Type=Unsigned32
_PfLimitsFrags_Object=MibScalar
pfLimitsFrags=_PfLimitsFrags_Object((1,3,6,1,4,1,12325,1,200,1,5,3),_PfLimitsFrags_Type())
pfLimitsFrags.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLimitsFrags.setStatus(_A)
_PfTimeouts_ObjectIdentity=ObjectIdentity
pfTimeouts=_PfTimeouts_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,6))
_PfTimeoutsTcpFirst_Type=Integer32
_PfTimeoutsTcpFirst_Object=MibScalar
pfTimeoutsTcpFirst=_PfTimeoutsTcpFirst_Object((1,3,6,1,4,1,12325,1,200,1,6,1),_PfTimeoutsTcpFirst_Type())
pfTimeoutsTcpFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsTcpFirst.setStatus(_A)
_PfTimeoutsTcpOpening_Type=Integer32
_PfTimeoutsTcpOpening_Object=MibScalar
pfTimeoutsTcpOpening=_PfTimeoutsTcpOpening_Object((1,3,6,1,4,1,12325,1,200,1,6,2),_PfTimeoutsTcpOpening_Type())
pfTimeoutsTcpOpening.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsTcpOpening.setStatus(_A)
_PfTimeoutsTcpEstablished_Type=Integer32
_PfTimeoutsTcpEstablished_Object=MibScalar
pfTimeoutsTcpEstablished=_PfTimeoutsTcpEstablished_Object((1,3,6,1,4,1,12325,1,200,1,6,3),_PfTimeoutsTcpEstablished_Type())
pfTimeoutsTcpEstablished.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsTcpEstablished.setStatus(_A)
_PfTimeoutsTcpClosing_Type=Integer32
_PfTimeoutsTcpClosing_Object=MibScalar
pfTimeoutsTcpClosing=_PfTimeoutsTcpClosing_Object((1,3,6,1,4,1,12325,1,200,1,6,4),_PfTimeoutsTcpClosing_Type())
pfTimeoutsTcpClosing.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsTcpClosing.setStatus(_A)
_PfTimeoutsTcpFinWait_Type=Integer32
_PfTimeoutsTcpFinWait_Object=MibScalar
pfTimeoutsTcpFinWait=_PfTimeoutsTcpFinWait_Object((1,3,6,1,4,1,12325,1,200,1,6,5),_PfTimeoutsTcpFinWait_Type())
pfTimeoutsTcpFinWait.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsTcpFinWait.setStatus(_A)
_PfTimeoutsTcpClosed_Type=Integer32
_PfTimeoutsTcpClosed_Object=MibScalar
pfTimeoutsTcpClosed=_PfTimeoutsTcpClosed_Object((1,3,6,1,4,1,12325,1,200,1,6,6),_PfTimeoutsTcpClosed_Type())
pfTimeoutsTcpClosed.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsTcpClosed.setStatus(_A)
_PfTimeoutsUdpFirst_Type=Integer32
_PfTimeoutsUdpFirst_Object=MibScalar
pfTimeoutsUdpFirst=_PfTimeoutsUdpFirst_Object((1,3,6,1,4,1,12325,1,200,1,6,7),_PfTimeoutsUdpFirst_Type())
pfTimeoutsUdpFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsUdpFirst.setStatus(_A)
_PfTimeoutsUdpSingle_Type=Integer32
_PfTimeoutsUdpSingle_Object=MibScalar
pfTimeoutsUdpSingle=_PfTimeoutsUdpSingle_Object((1,3,6,1,4,1,12325,1,200,1,6,8),_PfTimeoutsUdpSingle_Type())
pfTimeoutsUdpSingle.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsUdpSingle.setStatus(_A)
_PfTimeoutsUdpMultiple_Type=Integer32
_PfTimeoutsUdpMultiple_Object=MibScalar
pfTimeoutsUdpMultiple=_PfTimeoutsUdpMultiple_Object((1,3,6,1,4,1,12325,1,200,1,6,9),_PfTimeoutsUdpMultiple_Type())
pfTimeoutsUdpMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsUdpMultiple.setStatus(_A)
_PfTimeoutsIcmpFirst_Type=Integer32
_PfTimeoutsIcmpFirst_Object=MibScalar
pfTimeoutsIcmpFirst=_PfTimeoutsIcmpFirst_Object((1,3,6,1,4,1,12325,1,200,1,6,10),_PfTimeoutsIcmpFirst_Type())
pfTimeoutsIcmpFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsIcmpFirst.setStatus(_A)
_PfTimeoutsIcmpError_Type=Integer32
_PfTimeoutsIcmpError_Object=MibScalar
pfTimeoutsIcmpError=_PfTimeoutsIcmpError_Object((1,3,6,1,4,1,12325,1,200,1,6,11),_PfTimeoutsIcmpError_Type())
pfTimeoutsIcmpError.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsIcmpError.setStatus(_A)
_PfTimeoutsOtherFirst_Type=Integer32
_PfTimeoutsOtherFirst_Object=MibScalar
pfTimeoutsOtherFirst=_PfTimeoutsOtherFirst_Object((1,3,6,1,4,1,12325,1,200,1,6,12),_PfTimeoutsOtherFirst_Type())
pfTimeoutsOtherFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsOtherFirst.setStatus(_A)
_PfTimeoutsOtherSingle_Type=Integer32
_PfTimeoutsOtherSingle_Object=MibScalar
pfTimeoutsOtherSingle=_PfTimeoutsOtherSingle_Object((1,3,6,1,4,1,12325,1,200,1,6,13),_PfTimeoutsOtherSingle_Type())
pfTimeoutsOtherSingle.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsOtherSingle.setStatus(_A)
_PfTimeoutsOtherMultiple_Type=Integer32
_PfTimeoutsOtherMultiple_Object=MibScalar
pfTimeoutsOtherMultiple=_PfTimeoutsOtherMultiple_Object((1,3,6,1,4,1,12325,1,200,1,6,14),_PfTimeoutsOtherMultiple_Type())
pfTimeoutsOtherMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsOtherMultiple.setStatus(_A)
_PfTimeoutsFragment_Type=Integer32
_PfTimeoutsFragment_Object=MibScalar
pfTimeoutsFragment=_PfTimeoutsFragment_Object((1,3,6,1,4,1,12325,1,200,1,6,15),_PfTimeoutsFragment_Type())
pfTimeoutsFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsFragment.setStatus(_A)
_PfTimeoutsInterval_Type=Integer32
_PfTimeoutsInterval_Object=MibScalar
pfTimeoutsInterval=_PfTimeoutsInterval_Object((1,3,6,1,4,1,12325,1,200,1,6,16),_PfTimeoutsInterval_Type())
pfTimeoutsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsInterval.setStatus(_A)
_PfTimeoutsAdaptiveStart_Type=Integer32
_PfTimeoutsAdaptiveStart_Object=MibScalar
pfTimeoutsAdaptiveStart=_PfTimeoutsAdaptiveStart_Object((1,3,6,1,4,1,12325,1,200,1,6,17),_PfTimeoutsAdaptiveStart_Type())
pfTimeoutsAdaptiveStart.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsAdaptiveStart.setStatus(_A)
_PfTimeoutsAdaptiveEnd_Type=Integer32
_PfTimeoutsAdaptiveEnd_Object=MibScalar
pfTimeoutsAdaptiveEnd=_PfTimeoutsAdaptiveEnd_Object((1,3,6,1,4,1,12325,1,200,1,6,18),_PfTimeoutsAdaptiveEnd_Type())
pfTimeoutsAdaptiveEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsAdaptiveEnd.setStatus(_A)
_PfTimeoutsSrcNode_Type=Integer32
_PfTimeoutsSrcNode_Object=MibScalar
pfTimeoutsSrcNode=_PfTimeoutsSrcNode_Object((1,3,6,1,4,1,12325,1,200,1,6,19),_PfTimeoutsSrcNode_Type())
pfTimeoutsSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTimeoutsSrcNode.setStatus(_A)
_PfLogInterface_ObjectIdentity=ObjectIdentity
pfLogInterface=_PfLogInterface_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,7))
_PfLogInterfaceName_Type=OctetString
_PfLogInterfaceName_Object=MibScalar
pfLogInterfaceName=_PfLogInterfaceName_Object((1,3,6,1,4,1,12325,1,200,1,7,1),_PfLogInterfaceName_Type())
pfLogInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceName.setStatus(_A)
_PfLogInterfaceIp4BytesIn_Type=Counter64
_PfLogInterfaceIp4BytesIn_Object=MibScalar
pfLogInterfaceIp4BytesIn=_PfLogInterfaceIp4BytesIn_Object((1,3,6,1,4,1,12325,1,200,1,7,2),_PfLogInterfaceIp4BytesIn_Type())
pfLogInterfaceIp4BytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp4BytesIn.setStatus(_A)
_PfLogInterfaceIp4BytesOut_Type=Counter64
_PfLogInterfaceIp4BytesOut_Object=MibScalar
pfLogInterfaceIp4BytesOut=_PfLogInterfaceIp4BytesOut_Object((1,3,6,1,4,1,12325,1,200,1,7,3),_PfLogInterfaceIp4BytesOut_Type())
pfLogInterfaceIp4BytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp4BytesOut.setStatus(_A)
_PfLogInterfaceIp4PktsInPass_Type=Counter64
_PfLogInterfaceIp4PktsInPass_Object=MibScalar
pfLogInterfaceIp4PktsInPass=_PfLogInterfaceIp4PktsInPass_Object((1,3,6,1,4,1,12325,1,200,1,7,4),_PfLogInterfaceIp4PktsInPass_Type())
pfLogInterfaceIp4PktsInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp4PktsInPass.setStatus(_A)
_PfLogInterfaceIp4PktsInDrop_Type=Counter64
_PfLogInterfaceIp4PktsInDrop_Object=MibScalar
pfLogInterfaceIp4PktsInDrop=_PfLogInterfaceIp4PktsInDrop_Object((1,3,6,1,4,1,12325,1,200,1,7,5),_PfLogInterfaceIp4PktsInDrop_Type())
pfLogInterfaceIp4PktsInDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp4PktsInDrop.setStatus(_A)
_PfLogInterfaceIp4PktsOutPass_Type=Counter64
_PfLogInterfaceIp4PktsOutPass_Object=MibScalar
pfLogInterfaceIp4PktsOutPass=_PfLogInterfaceIp4PktsOutPass_Object((1,3,6,1,4,1,12325,1,200,1,7,6),_PfLogInterfaceIp4PktsOutPass_Type())
pfLogInterfaceIp4PktsOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp4PktsOutPass.setStatus(_A)
_PfLogInterfaceIp4PktsOutDrop_Type=Counter64
_PfLogInterfaceIp4PktsOutDrop_Object=MibScalar
pfLogInterfaceIp4PktsOutDrop=_PfLogInterfaceIp4PktsOutDrop_Object((1,3,6,1,4,1,12325,1,200,1,7,7),_PfLogInterfaceIp4PktsOutDrop_Type())
pfLogInterfaceIp4PktsOutDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp4PktsOutDrop.setStatus(_A)
_PfLogInterfaceIp6BytesIn_Type=Counter64
_PfLogInterfaceIp6BytesIn_Object=MibScalar
pfLogInterfaceIp6BytesIn=_PfLogInterfaceIp6BytesIn_Object((1,3,6,1,4,1,12325,1,200,1,7,8),_PfLogInterfaceIp6BytesIn_Type())
pfLogInterfaceIp6BytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp6BytesIn.setStatus(_A)
_PfLogInterfaceIp6BytesOut_Type=Counter64
_PfLogInterfaceIp6BytesOut_Object=MibScalar
pfLogInterfaceIp6BytesOut=_PfLogInterfaceIp6BytesOut_Object((1,3,6,1,4,1,12325,1,200,1,7,9),_PfLogInterfaceIp6BytesOut_Type())
pfLogInterfaceIp6BytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp6BytesOut.setStatus(_A)
_PfLogInterfaceIp6PktsInPass_Type=Counter64
_PfLogInterfaceIp6PktsInPass_Object=MibScalar
pfLogInterfaceIp6PktsInPass=_PfLogInterfaceIp6PktsInPass_Object((1,3,6,1,4,1,12325,1,200,1,7,10),_PfLogInterfaceIp6PktsInPass_Type())
pfLogInterfaceIp6PktsInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp6PktsInPass.setStatus(_A)
_PfLogInterfaceIp6PktsInDrop_Type=Counter64
_PfLogInterfaceIp6PktsInDrop_Object=MibScalar
pfLogInterfaceIp6PktsInDrop=_PfLogInterfaceIp6PktsInDrop_Object((1,3,6,1,4,1,12325,1,200,1,7,11),_PfLogInterfaceIp6PktsInDrop_Type())
pfLogInterfaceIp6PktsInDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp6PktsInDrop.setStatus(_A)
_PfLogInterfaceIp6PktsOutPass_Type=Counter64
_PfLogInterfaceIp6PktsOutPass_Object=MibScalar
pfLogInterfaceIp6PktsOutPass=_PfLogInterfaceIp6PktsOutPass_Object((1,3,6,1,4,1,12325,1,200,1,7,12),_PfLogInterfaceIp6PktsOutPass_Type())
pfLogInterfaceIp6PktsOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp6PktsOutPass.setStatus(_A)
_PfLogInterfaceIp6PktsOutDrop_Type=Counter64
_PfLogInterfaceIp6PktsOutDrop_Object=MibScalar
pfLogInterfaceIp6PktsOutDrop=_PfLogInterfaceIp6PktsOutDrop_Object((1,3,6,1,4,1,12325,1,200,1,7,13),_PfLogInterfaceIp6PktsOutDrop_Type())
pfLogInterfaceIp6PktsOutDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLogInterfaceIp6PktsOutDrop.setStatus(_A)
_PfInterfaces_ObjectIdentity=ObjectIdentity
pfInterfaces=_PfInterfaces_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,8))
_PfInterfacesIfNumber_Type=Integer32
_PfInterfacesIfNumber_Object=MibScalar
pfInterfacesIfNumber=_PfInterfacesIfNumber_Object((1,3,6,1,4,1,12325,1,200,1,8,1),_PfInterfacesIfNumber_Type())
pfInterfacesIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIfNumber.setStatus(_A)
_PfInterfacesIfTable_Object=MibTable
pfInterfacesIfTable=_PfInterfacesIfTable_Object((1,3,6,1,4,1,12325,1,200,1,8,2))
if mibBuilder.loadTexts:pfInterfacesIfTable.setStatus(_A)
_PfInterfacesIfEntry_Object=MibTableRow
pfInterfacesIfEntry=_PfInterfacesIfEntry_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1))
pfInterfacesIfEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:pfInterfacesIfEntry.setStatus(_A)
class _PfInterfacesIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PfInterfacesIfIndex_Type.__name__=_C
_PfInterfacesIfIndex_Object=MibTableColumn
pfInterfacesIfIndex=_PfInterfacesIfIndex_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,1),_PfInterfacesIfIndex_Type())
pfInterfacesIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pfInterfacesIfIndex.setStatus(_A)
_PfInterfacesIfDescr_Type=OctetString
_PfInterfacesIfDescr_Object=MibTableColumn
pfInterfacesIfDescr=_PfInterfacesIfDescr_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,2),_PfInterfacesIfDescr_Type())
pfInterfacesIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIfDescr.setStatus(_A)
class _PfInterfacesIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('group',0),('instance',1),('detached',2)))
_PfInterfacesIfType_Type.__name__=_C
_PfInterfacesIfType_Object=MibTableColumn
pfInterfacesIfType=_PfInterfacesIfType_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,3),_PfInterfacesIfType_Type())
pfInterfacesIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIfType.setStatus(_A)
_PfInterfacesIfTZero_Type=TimeTicks
_PfInterfacesIfTZero_Object=MibTableColumn
pfInterfacesIfTZero=_PfInterfacesIfTZero_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,4),_PfInterfacesIfTZero_Type())
pfInterfacesIfTZero.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIfTZero.setStatus(_A)
if mibBuilder.loadTexts:pfInterfacesIfTZero.setUnits(_F)
_PfInterfacesIfRefsState_Type=Unsigned32
_PfInterfacesIfRefsState_Object=MibTableColumn
pfInterfacesIfRefsState=_PfInterfacesIfRefsState_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,5),_PfInterfacesIfRefsState_Type())
pfInterfacesIfRefsState.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIfRefsState.setStatus(_A)
_PfInterfacesIfRefsRule_Type=Unsigned32
_PfInterfacesIfRefsRule_Object=MibTableColumn
pfInterfacesIfRefsRule=_PfInterfacesIfRefsRule_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,6),_PfInterfacesIfRefsRule_Type())
pfInterfacesIfRefsRule.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIfRefsRule.setStatus(_A)
_PfInterfacesIf4BytesInPass_Type=Counter64
_PfInterfacesIf4BytesInPass_Object=MibTableColumn
pfInterfacesIf4BytesInPass=_PfInterfacesIf4BytesInPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,7),_PfInterfacesIf4BytesInPass_Type())
pfInterfacesIf4BytesInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4BytesInPass.setStatus(_A)
_PfInterfacesIf4BytesInBlock_Type=Counter64
_PfInterfacesIf4BytesInBlock_Object=MibTableColumn
pfInterfacesIf4BytesInBlock=_PfInterfacesIf4BytesInBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,8),_PfInterfacesIf4BytesInBlock_Type())
pfInterfacesIf4BytesInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4BytesInBlock.setStatus(_A)
_PfInterfacesIf4BytesOutPass_Type=Counter64
_PfInterfacesIf4BytesOutPass_Object=MibTableColumn
pfInterfacesIf4BytesOutPass=_PfInterfacesIf4BytesOutPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,9),_PfInterfacesIf4BytesOutPass_Type())
pfInterfacesIf4BytesOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4BytesOutPass.setStatus(_A)
_PfInterfacesIf4BytesOutBlock_Type=Counter64
_PfInterfacesIf4BytesOutBlock_Object=MibTableColumn
pfInterfacesIf4BytesOutBlock=_PfInterfacesIf4BytesOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,10),_PfInterfacesIf4BytesOutBlock_Type())
pfInterfacesIf4BytesOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4BytesOutBlock.setStatus(_A)
_PfInterfacesIf4PktsInPass_Type=Counter64
_PfInterfacesIf4PktsInPass_Object=MibTableColumn
pfInterfacesIf4PktsInPass=_PfInterfacesIf4PktsInPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,11),_PfInterfacesIf4PktsInPass_Type())
pfInterfacesIf4PktsInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4PktsInPass.setStatus(_A)
_PfInterfacesIf4PktsInBlock_Type=Counter64
_PfInterfacesIf4PktsInBlock_Object=MibTableColumn
pfInterfacesIf4PktsInBlock=_PfInterfacesIf4PktsInBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,12),_PfInterfacesIf4PktsInBlock_Type())
pfInterfacesIf4PktsInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4PktsInBlock.setStatus(_A)
_PfInterfacesIf4PktsOutPass_Type=Counter64
_PfInterfacesIf4PktsOutPass_Object=MibTableColumn
pfInterfacesIf4PktsOutPass=_PfInterfacesIf4PktsOutPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,13),_PfInterfacesIf4PktsOutPass_Type())
pfInterfacesIf4PktsOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4PktsOutPass.setStatus(_A)
_PfInterfacesIf4PktsOutBlock_Type=Counter64
_PfInterfacesIf4PktsOutBlock_Object=MibTableColumn
pfInterfacesIf4PktsOutBlock=_PfInterfacesIf4PktsOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,14),_PfInterfacesIf4PktsOutBlock_Type())
pfInterfacesIf4PktsOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf4PktsOutBlock.setStatus(_A)
_PfInterfacesIf6BytesInPass_Type=Counter64
_PfInterfacesIf6BytesInPass_Object=MibTableColumn
pfInterfacesIf6BytesInPass=_PfInterfacesIf6BytesInPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,15),_PfInterfacesIf6BytesInPass_Type())
pfInterfacesIf6BytesInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6BytesInPass.setStatus(_A)
_PfInterfacesIf6BytesInBlock_Type=Counter64
_PfInterfacesIf6BytesInBlock_Object=MibTableColumn
pfInterfacesIf6BytesInBlock=_PfInterfacesIf6BytesInBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,16),_PfInterfacesIf6BytesInBlock_Type())
pfInterfacesIf6BytesInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6BytesInBlock.setStatus(_A)
_PfInterfacesIf6BytesOutPass_Type=Counter64
_PfInterfacesIf6BytesOutPass_Object=MibTableColumn
pfInterfacesIf6BytesOutPass=_PfInterfacesIf6BytesOutPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,17),_PfInterfacesIf6BytesOutPass_Type())
pfInterfacesIf6BytesOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6BytesOutPass.setStatus(_A)
_PfInterfacesIf6BytesOutBlock_Type=Counter64
_PfInterfacesIf6BytesOutBlock_Object=MibTableColumn
pfInterfacesIf6BytesOutBlock=_PfInterfacesIf6BytesOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,18),_PfInterfacesIf6BytesOutBlock_Type())
pfInterfacesIf6BytesOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6BytesOutBlock.setStatus(_A)
_PfInterfacesIf6PktsInPass_Type=Counter64
_PfInterfacesIf6PktsInPass_Object=MibTableColumn
pfInterfacesIf6PktsInPass=_PfInterfacesIf6PktsInPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,19),_PfInterfacesIf6PktsInPass_Type())
pfInterfacesIf6PktsInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6PktsInPass.setStatus(_A)
_PfInterfacesIf6PktsInBlock_Type=Counter64
_PfInterfacesIf6PktsInBlock_Object=MibTableColumn
pfInterfacesIf6PktsInBlock=_PfInterfacesIf6PktsInBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,20),_PfInterfacesIf6PktsInBlock_Type())
pfInterfacesIf6PktsInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6PktsInBlock.setStatus(_A)
_PfInterfacesIf6PktsOutPass_Type=Counter64
_PfInterfacesIf6PktsOutPass_Object=MibTableColumn
pfInterfacesIf6PktsOutPass=_PfInterfacesIf6PktsOutPass_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,21),_PfInterfacesIf6PktsOutPass_Type())
pfInterfacesIf6PktsOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6PktsOutPass.setStatus(_A)
_PfInterfacesIf6PktsOutBlock_Type=Counter64
_PfInterfacesIf6PktsOutBlock_Object=MibTableColumn
pfInterfacesIf6PktsOutBlock=_PfInterfacesIf6PktsOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,8,2,1,22),_PfInterfacesIf6PktsOutBlock_Type())
pfInterfacesIf6PktsOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfInterfacesIf6PktsOutBlock.setStatus(_A)
_PfTables_ObjectIdentity=ObjectIdentity
pfTables=_PfTables_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,9))
_PfTablesTblNumber_Type=Integer32
_PfTablesTblNumber_Object=MibScalar
pfTablesTblNumber=_PfTablesTblNumber_Object((1,3,6,1,4,1,12325,1,200,1,9,1),_PfTablesTblNumber_Type())
pfTablesTblNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblNumber.setStatus(_A)
_PfTablesTblTable_Object=MibTable
pfTablesTblTable=_PfTablesTblTable_Object((1,3,6,1,4,1,12325,1,200,1,9,2))
if mibBuilder.loadTexts:pfTablesTblTable.setStatus(_A)
_PfTablesTblEntry_Object=MibTableRow
pfTablesTblEntry=_PfTablesTblEntry_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1))
pfTablesTblEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:pfTablesTblEntry.setStatus(_A)
class _PfTablesTblIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PfTablesTblIndex_Type.__name__=_C
_PfTablesTblIndex_Object=MibTableColumn
pfTablesTblIndex=_PfTablesTblIndex_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,1),_PfTablesTblIndex_Type())
pfTablesTblIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pfTablesTblIndex.setStatus(_A)
_PfTablesTblDescr_Type=OctetString
_PfTablesTblDescr_Object=MibTableColumn
pfTablesTblDescr=_PfTablesTblDescr_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,2),_PfTablesTblDescr_Type())
pfTablesTblDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblDescr.setStatus(_A)
_PfTablesTblCount_Type=Integer32
_PfTablesTblCount_Object=MibTableColumn
pfTablesTblCount=_PfTablesTblCount_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,3),_PfTablesTblCount_Type())
pfTablesTblCount.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblCount.setStatus(_A)
_PfTablesTblTZero_Type=TimeTicks
_PfTablesTblTZero_Object=MibTableColumn
pfTablesTblTZero=_PfTablesTblTZero_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,4),_PfTablesTblTZero_Type())
pfTablesTblTZero.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblTZero.setStatus(_A)
if mibBuilder.loadTexts:pfTablesTblTZero.setUnits(_F)
_PfTablesTblRefsAnchor_Type=Integer32
_PfTablesTblRefsAnchor_Object=MibTableColumn
pfTablesTblRefsAnchor=_PfTablesTblRefsAnchor_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,5),_PfTablesTblRefsAnchor_Type())
pfTablesTblRefsAnchor.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblRefsAnchor.setStatus(_A)
_PfTablesTblRefsRule_Type=Integer32
_PfTablesTblRefsRule_Object=MibTableColumn
pfTablesTblRefsRule=_PfTablesTblRefsRule_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,6),_PfTablesTblRefsRule_Type())
pfTablesTblRefsRule.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblRefsRule.setStatus(_A)
_PfTablesTblEvalMatch_Type=Counter64
_PfTablesTblEvalMatch_Object=MibTableColumn
pfTablesTblEvalMatch=_PfTablesTblEvalMatch_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,7),_PfTablesTblEvalMatch_Type())
pfTablesTblEvalMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblEvalMatch.setStatus(_A)
_PfTablesTblEvalNoMatch_Type=Counter64
_PfTablesTblEvalNoMatch_Object=MibTableColumn
pfTablesTblEvalNoMatch=_PfTablesTblEvalNoMatch_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,8),_PfTablesTblEvalNoMatch_Type())
pfTablesTblEvalNoMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblEvalNoMatch.setStatus(_A)
_PfTablesTblBytesInPass_Type=Counter64
_PfTablesTblBytesInPass_Object=MibTableColumn
pfTablesTblBytesInPass=_PfTablesTblBytesInPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,9),_PfTablesTblBytesInPass_Type())
pfTablesTblBytesInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblBytesInPass.setStatus(_A)
_PfTablesTblBytesInBlock_Type=Counter64
_PfTablesTblBytesInBlock_Object=MibTableColumn
pfTablesTblBytesInBlock=_PfTablesTblBytesInBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,10),_PfTablesTblBytesInBlock_Type())
pfTablesTblBytesInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblBytesInBlock.setStatus(_A)
_PfTablesTblBytesInXPass_Type=Counter64
_PfTablesTblBytesInXPass_Object=MibTableColumn
pfTablesTblBytesInXPass=_PfTablesTblBytesInXPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,11),_PfTablesTblBytesInXPass_Type())
pfTablesTblBytesInXPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblBytesInXPass.setStatus(_A)
_PfTablesTblBytesOutPass_Type=Counter64
_PfTablesTblBytesOutPass_Object=MibTableColumn
pfTablesTblBytesOutPass=_PfTablesTblBytesOutPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,12),_PfTablesTblBytesOutPass_Type())
pfTablesTblBytesOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblBytesOutPass.setStatus(_A)
_PfTablesTblBytesOutBlock_Type=Counter64
_PfTablesTblBytesOutBlock_Object=MibTableColumn
pfTablesTblBytesOutBlock=_PfTablesTblBytesOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,13),_PfTablesTblBytesOutBlock_Type())
pfTablesTblBytesOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblBytesOutBlock.setStatus(_A)
_PfTablesTblBytesOutXPass_Type=Counter64
_PfTablesTblBytesOutXPass_Object=MibTableColumn
pfTablesTblBytesOutXPass=_PfTablesTblBytesOutXPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,14),_PfTablesTblBytesOutXPass_Type())
pfTablesTblBytesOutXPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblBytesOutXPass.setStatus(_A)
_PfTablesTblPktsInPass_Type=Counter64
_PfTablesTblPktsInPass_Object=MibTableColumn
pfTablesTblPktsInPass=_PfTablesTblPktsInPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,15),_PfTablesTblPktsInPass_Type())
pfTablesTblPktsInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblPktsInPass.setStatus(_A)
_PfTablesTblPktsInBlock_Type=Counter64
_PfTablesTblPktsInBlock_Object=MibTableColumn
pfTablesTblPktsInBlock=_PfTablesTblPktsInBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,16),_PfTablesTblPktsInBlock_Type())
pfTablesTblPktsInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblPktsInBlock.setStatus(_A)
_PfTablesTblPktsInXPass_Type=Counter64
_PfTablesTblPktsInXPass_Object=MibTableColumn
pfTablesTblPktsInXPass=_PfTablesTblPktsInXPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,17),_PfTablesTblPktsInXPass_Type())
pfTablesTblPktsInXPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblPktsInXPass.setStatus(_A)
_PfTablesTblPktsOutPass_Type=Counter64
_PfTablesTblPktsOutPass_Object=MibTableColumn
pfTablesTblPktsOutPass=_PfTablesTblPktsOutPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,18),_PfTablesTblPktsOutPass_Type())
pfTablesTblPktsOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblPktsOutPass.setStatus(_A)
_PfTablesTblPktsOutBlock_Type=Counter64
_PfTablesTblPktsOutBlock_Object=MibTableColumn
pfTablesTblPktsOutBlock=_PfTablesTblPktsOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,19),_PfTablesTblPktsOutBlock_Type())
pfTablesTblPktsOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblPktsOutBlock.setStatus(_A)
_PfTablesTblPktsOutXPass_Type=Counter64
_PfTablesTblPktsOutXPass_Object=MibTableColumn
pfTablesTblPktsOutXPass=_PfTablesTblPktsOutXPass_Object((1,3,6,1,4,1,12325,1,200,1,9,2,1,20),_PfTablesTblPktsOutXPass_Type())
pfTablesTblPktsOutXPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesTblPktsOutXPass.setStatus(_A)
_PfTablesAddrTable_Object=MibTable
pfTablesAddrTable=_PfTablesAddrTable_Object((1,3,6,1,4,1,12325,1,200,1,9,3))
if mibBuilder.loadTexts:pfTablesAddrTable.setStatus(_A)
_PfTablesAddrEntry_Object=MibTableRow
pfTablesAddrEntry=_PfTablesAddrEntry_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1))
pfTablesAddrEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:pfTablesAddrEntry.setStatus(_A)
class _PfTablesAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PfTablesAddrIndex_Type.__name__=_C
_PfTablesAddrIndex_Object=MibTableColumn
pfTablesAddrIndex=_PfTablesAddrIndex_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,1),_PfTablesAddrIndex_Type())
pfTablesAddrIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pfTablesAddrIndex.setStatus(_A)
_PfTablesAddrNetType_Type=InetAddressType
_PfTablesAddrNetType_Object=MibTableColumn
pfTablesAddrNetType=_PfTablesAddrNetType_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,2),_PfTablesAddrNetType_Type())
pfTablesAddrNetType.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrNetType.setStatus(_A)
_PfTablesAddrNet_Type=InetAddress
_PfTablesAddrNet_Object=MibTableColumn
pfTablesAddrNet=_PfTablesAddrNet_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,3),_PfTablesAddrNet_Type())
pfTablesAddrNet.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrNet.setStatus(_A)
_PfTablesAddrPrefix_Type=InetAddressPrefixLength
_PfTablesAddrPrefix_Object=MibTableColumn
pfTablesAddrPrefix=_PfTablesAddrPrefix_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,4),_PfTablesAddrPrefix_Type())
pfTablesAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrPrefix.setStatus(_A)
_PfTablesAddrTZero_Type=TimeTicks
_PfTablesAddrTZero_Object=MibTableColumn
pfTablesAddrTZero=_PfTablesAddrTZero_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,5),_PfTablesAddrTZero_Type())
pfTablesAddrTZero.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrTZero.setStatus(_A)
if mibBuilder.loadTexts:pfTablesAddrTZero.setUnits(_F)
_PfTablesAddrBytesInPass_Type=Counter64
_PfTablesAddrBytesInPass_Object=MibTableColumn
pfTablesAddrBytesInPass=_PfTablesAddrBytesInPass_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,6),_PfTablesAddrBytesInPass_Type())
pfTablesAddrBytesInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrBytesInPass.setStatus(_A)
_PfTablesAddrBytesInBlock_Type=Counter64
_PfTablesAddrBytesInBlock_Object=MibTableColumn
pfTablesAddrBytesInBlock=_PfTablesAddrBytesInBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,7),_PfTablesAddrBytesInBlock_Type())
pfTablesAddrBytesInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrBytesInBlock.setStatus(_A)
_PfTablesAddrBytesOutPass_Type=Counter64
_PfTablesAddrBytesOutPass_Object=MibTableColumn
pfTablesAddrBytesOutPass=_PfTablesAddrBytesOutPass_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,8),_PfTablesAddrBytesOutPass_Type())
pfTablesAddrBytesOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrBytesOutPass.setStatus(_A)
_PfTablesAddrBytesOutBlock_Type=Counter64
_PfTablesAddrBytesOutBlock_Object=MibTableColumn
pfTablesAddrBytesOutBlock=_PfTablesAddrBytesOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,9),_PfTablesAddrBytesOutBlock_Type())
pfTablesAddrBytesOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrBytesOutBlock.setStatus(_A)
_PfTablesAddrPktsInPass_Type=Counter64
_PfTablesAddrPktsInPass_Object=MibTableColumn
pfTablesAddrPktsInPass=_PfTablesAddrPktsInPass_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,10),_PfTablesAddrPktsInPass_Type())
pfTablesAddrPktsInPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrPktsInPass.setStatus(_A)
_PfTablesAddrPktsInBlock_Type=Counter64
_PfTablesAddrPktsInBlock_Object=MibTableColumn
pfTablesAddrPktsInBlock=_PfTablesAddrPktsInBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,11),_PfTablesAddrPktsInBlock_Type())
pfTablesAddrPktsInBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrPktsInBlock.setStatus(_A)
_PfTablesAddrPktsOutPass_Type=Counter64
_PfTablesAddrPktsOutPass_Object=MibTableColumn
pfTablesAddrPktsOutPass=_PfTablesAddrPktsOutPass_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,12),_PfTablesAddrPktsOutPass_Type())
pfTablesAddrPktsOutPass.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrPktsOutPass.setStatus(_A)
_PfTablesAddrPktsOutBlock_Type=Counter64
_PfTablesAddrPktsOutBlock_Object=MibTableColumn
pfTablesAddrPktsOutBlock=_PfTablesAddrPktsOutBlock_Object((1,3,6,1,4,1,12325,1,200,1,9,3,1,13),_PfTablesAddrPktsOutBlock_Type())
pfTablesAddrPktsOutBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:pfTablesAddrPktsOutBlock.setStatus(_A)
_PfAltq_ObjectIdentity=ObjectIdentity
pfAltq=_PfAltq_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,10))
_PfAltqQueueNumber_Type=Unsigned32
_PfAltqQueueNumber_Object=MibScalar
pfAltqQueueNumber=_PfAltqQueueNumber_Object((1,3,6,1,4,1,12325,1,200,1,10,1),_PfAltqQueueNumber_Type())
pfAltqQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pfAltqQueueNumber.setStatus(_A)
_PfAltqQueueTable_Object=MibTable
pfAltqQueueTable=_PfAltqQueueTable_Object((1,3,6,1,4,1,12325,1,200,1,10,2))
if mibBuilder.loadTexts:pfAltqQueueTable.setStatus(_A)
_PfAltqQueueEntry_Object=MibTableRow
pfAltqQueueEntry=_PfAltqQueueEntry_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1))
pfAltqQueueEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:pfAltqQueueEntry.setStatus(_A)
class _PfAltqQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PfAltqQueueIndex_Type.__name__=_C
_PfAltqQueueIndex_Object=MibTableColumn
pfAltqQueueIndex=_PfAltqQueueIndex_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1,1),_PfAltqQueueIndex_Type())
pfAltqQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pfAltqQueueIndex.setStatus(_A)
_PfAltqQueueDescr_Type=OctetString
_PfAltqQueueDescr_Object=MibTableColumn
pfAltqQueueDescr=_PfAltqQueueDescr_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1,2),_PfAltqQueueDescr_Type())
pfAltqQueueDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:pfAltqQueueDescr.setStatus(_A)
_PfAltqQueueParent_Type=OctetString
_PfAltqQueueParent_Object=MibTableColumn
pfAltqQueueParent=_PfAltqQueueParent_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1,3),_PfAltqQueueParent_Type())
pfAltqQueueParent.setMaxAccess(_B)
if mibBuilder.loadTexts:pfAltqQueueParent.setStatus(_A)
class _PfAltqQueueScheduler_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,8,11)));namedValues=NamedValues(*(('cbq',1),('hfsc',8),('priq',11)))
_PfAltqQueueScheduler_Type.__name__=_C
_PfAltqQueueScheduler_Object=MibTableColumn
pfAltqQueueScheduler=_PfAltqQueueScheduler_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1,4),_PfAltqQueueScheduler_Type())
pfAltqQueueScheduler.setMaxAccess(_B)
if mibBuilder.loadTexts:pfAltqQueueScheduler.setStatus(_A)
_PfAltqQueueBandwidth_Type=Unsigned32
_PfAltqQueueBandwidth_Object=MibTableColumn
pfAltqQueueBandwidth=_PfAltqQueueBandwidth_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1,5),_PfAltqQueueBandwidth_Type())
pfAltqQueueBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:pfAltqQueueBandwidth.setStatus(_A)
_PfAltqQueuePriority_Type=Integer32
_PfAltqQueuePriority_Object=MibTableColumn
pfAltqQueuePriority=_PfAltqQueuePriority_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1,6),_PfAltqQueuePriority_Type())
pfAltqQueuePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:pfAltqQueuePriority.setStatus(_A)
_PfAltqQueueLimit_Type=Integer32
_PfAltqQueueLimit_Object=MibTableColumn
pfAltqQueueLimit=_PfAltqQueueLimit_Object((1,3,6,1,4,1,12325,1,200,1,10,2,1,7),_PfAltqQueueLimit_Type())
pfAltqQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:pfAltqQueueLimit.setStatus(_A)
_PfLabels_ObjectIdentity=ObjectIdentity
pfLabels=_PfLabels_ObjectIdentity((1,3,6,1,4,1,12325,1,200,1,11))
_PfLabelsLblNumber_Type=Integer32
_PfLabelsLblNumber_Object=MibScalar
pfLabelsLblNumber=_PfLabelsLblNumber_Object((1,3,6,1,4,1,12325,1,200,1,11,1),_PfLabelsLblNumber_Type())
pfLabelsLblNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLabelsLblNumber.setStatus(_A)
_PfLabelsLblTable_Object=MibTable
pfLabelsLblTable=_PfLabelsLblTable_Object((1,3,6,1,4,1,12325,1,200,1,11,2))
if mibBuilder.loadTexts:pfLabelsLblTable.setStatus(_A)
_PfLabelsLblEntry_Object=MibTableRow
pfLabelsLblEntry=_PfLabelsLblEntry_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1))
pfLabelsLblEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:pfLabelsLblEntry.setStatus(_A)
class _PfLabelsLblIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PfLabelsLblIndex_Type.__name__=_C
_PfLabelsLblIndex_Object=MibTableColumn
pfLabelsLblIndex=_PfLabelsLblIndex_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1,1),_PfLabelsLblIndex_Type())
pfLabelsLblIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pfLabelsLblIndex.setStatus(_A)
_PfLabelsLblName_Type=OctetString
_PfLabelsLblName_Object=MibTableColumn
pfLabelsLblName=_PfLabelsLblName_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1,2),_PfLabelsLblName_Type())
pfLabelsLblName.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLabelsLblName.setStatus(_A)
_PfLabelsLblEvals_Type=Counter64
_PfLabelsLblEvals_Object=MibTableColumn
pfLabelsLblEvals=_PfLabelsLblEvals_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1,3),_PfLabelsLblEvals_Type())
pfLabelsLblEvals.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLabelsLblEvals.setStatus(_A)
_PfLabelsLblBytesIn_Type=Counter64
_PfLabelsLblBytesIn_Object=MibTableColumn
pfLabelsLblBytesIn=_PfLabelsLblBytesIn_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1,4),_PfLabelsLblBytesIn_Type())
pfLabelsLblBytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLabelsLblBytesIn.setStatus(_A)
_PfLabelsLblBytesOut_Type=Counter64
_PfLabelsLblBytesOut_Object=MibTableColumn
pfLabelsLblBytesOut=_PfLabelsLblBytesOut_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1,5),_PfLabelsLblBytesOut_Type())
pfLabelsLblBytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLabelsLblBytesOut.setStatus(_A)
_PfLabelsLblPktsIn_Type=Counter64
_PfLabelsLblPktsIn_Object=MibTableColumn
pfLabelsLblPktsIn=_PfLabelsLblPktsIn_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1,6),_PfLabelsLblPktsIn_Type())
pfLabelsLblPktsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLabelsLblPktsIn.setStatus(_A)
_PfLabelsLblPktsOut_Type=Counter64
_PfLabelsLblPktsOut_Object=MibTableColumn
pfLabelsLblPktsOut=_PfLabelsLblPktsOut_Object((1,3,6,1,4,1,12325,1,200,1,11,2,1,7),_PfLabelsLblPktsOut_Type())
pfLabelsLblPktsOut.setMaxAccess(_B)
if mibBuilder.loadTexts:pfLabelsLblPktsOut.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'begemotPf':begemotPf,'begemotPfObjects':begemotPfObjects,'pfStatus':pfStatus,'pfStatusRunning':pfStatusRunning,'pfStatusRuntime':pfStatusRuntime,'pfStatusDebug':pfStatusDebug,'pfStatusHostId':pfStatusHostId,'pfCounter':pfCounter,'pfCounterMatch':pfCounterMatch,'pfCounterBadOffset':pfCounterBadOffset,'pfCounterFragment':pfCounterFragment,'pfCounterShort':pfCounterShort,'pfCounterNormalize':pfCounterNormalize,'pfCounterMemDrop':pfCounterMemDrop,'pfStateTable':pfStateTable,'pfStateTableCount':pfStateTableCount,'pfStateTableSearches':pfStateTableSearches,'pfStateTableInserts':pfStateTableInserts,'pfStateTableRemovals':pfStateTableRemovals,'pfSrcNodes':pfSrcNodes,'pfSrcNodesCount':pfSrcNodesCount,'pfSrcNodesSearches':pfSrcNodesSearches,'pfSrcNodesInserts':pfSrcNodesInserts,'pfSrcNodesRemovals':pfSrcNodesRemovals,'pfLimits':pfLimits,'pfLimitsStates':pfLimitsStates,'pfLimitsSrcNodes':pfLimitsSrcNodes,'pfLimitsFrags':pfLimitsFrags,'pfTimeouts':pfTimeouts,'pfTimeoutsTcpFirst':pfTimeoutsTcpFirst,'pfTimeoutsTcpOpening':pfTimeoutsTcpOpening,'pfTimeoutsTcpEstablished':pfTimeoutsTcpEstablished,'pfTimeoutsTcpClosing':pfTimeoutsTcpClosing,'pfTimeoutsTcpFinWait':pfTimeoutsTcpFinWait,'pfTimeoutsTcpClosed':pfTimeoutsTcpClosed,'pfTimeoutsUdpFirst':pfTimeoutsUdpFirst,'pfTimeoutsUdpSingle':pfTimeoutsUdpSingle,'pfTimeoutsUdpMultiple':pfTimeoutsUdpMultiple,'pfTimeoutsIcmpFirst':pfTimeoutsIcmpFirst,'pfTimeoutsIcmpError':pfTimeoutsIcmpError,'pfTimeoutsOtherFirst':pfTimeoutsOtherFirst,'pfTimeoutsOtherSingle':pfTimeoutsOtherSingle,'pfTimeoutsOtherMultiple':pfTimeoutsOtherMultiple,'pfTimeoutsFragment':pfTimeoutsFragment,'pfTimeoutsInterval':pfTimeoutsInterval,'pfTimeoutsAdaptiveStart':pfTimeoutsAdaptiveStart,'pfTimeoutsAdaptiveEnd':pfTimeoutsAdaptiveEnd,'pfTimeoutsSrcNode':pfTimeoutsSrcNode,'pfLogInterface':pfLogInterface,'pfLogInterfaceName':pfLogInterfaceName,'pfLogInterfaceIp4BytesIn':pfLogInterfaceIp4BytesIn,'pfLogInterfaceIp4BytesOut':pfLogInterfaceIp4BytesOut,'pfLogInterfaceIp4PktsInPass':pfLogInterfaceIp4PktsInPass,'pfLogInterfaceIp4PktsInDrop':pfLogInterfaceIp4PktsInDrop,'pfLogInterfaceIp4PktsOutPass':pfLogInterfaceIp4PktsOutPass,'pfLogInterfaceIp4PktsOutDrop':pfLogInterfaceIp4PktsOutDrop,'pfLogInterfaceIp6BytesIn':pfLogInterfaceIp6BytesIn,'pfLogInterfaceIp6BytesOut':pfLogInterfaceIp6BytesOut,'pfLogInterfaceIp6PktsInPass':pfLogInterfaceIp6PktsInPass,'pfLogInterfaceIp6PktsInDrop':pfLogInterfaceIp6PktsInDrop,'pfLogInterfaceIp6PktsOutPass':pfLogInterfaceIp6PktsOutPass,'pfLogInterfaceIp6PktsOutDrop':pfLogInterfaceIp6PktsOutDrop,'pfInterfaces':pfInterfaces,'pfInterfacesIfNumber':pfInterfacesIfNumber,'pfInterfacesIfTable':pfInterfacesIfTable,'pfInterfacesIfEntry':pfInterfacesIfEntry,_G:pfInterfacesIfIndex,'pfInterfacesIfDescr':pfInterfacesIfDescr,'pfInterfacesIfType':pfInterfacesIfType,'pfInterfacesIfTZero':pfInterfacesIfTZero,'pfInterfacesIfRefsState':pfInterfacesIfRefsState,'pfInterfacesIfRefsRule':pfInterfacesIfRefsRule,'pfInterfacesIf4BytesInPass':pfInterfacesIf4BytesInPass,'pfInterfacesIf4BytesInBlock':pfInterfacesIf4BytesInBlock,'pfInterfacesIf4BytesOutPass':pfInterfacesIf4BytesOutPass,'pfInterfacesIf4BytesOutBlock':pfInterfacesIf4BytesOutBlock,'pfInterfacesIf4PktsInPass':pfInterfacesIf4PktsInPass,'pfInterfacesIf4PktsInBlock':pfInterfacesIf4PktsInBlock,'pfInterfacesIf4PktsOutPass':pfInterfacesIf4PktsOutPass,'pfInterfacesIf4PktsOutBlock':pfInterfacesIf4PktsOutBlock,'pfInterfacesIf6BytesInPass':pfInterfacesIf6BytesInPass,'pfInterfacesIf6BytesInBlock':pfInterfacesIf6BytesInBlock,'pfInterfacesIf6BytesOutPass':pfInterfacesIf6BytesOutPass,'pfInterfacesIf6BytesOutBlock':pfInterfacesIf6BytesOutBlock,'pfInterfacesIf6PktsInPass':pfInterfacesIf6PktsInPass,'pfInterfacesIf6PktsInBlock':pfInterfacesIf6PktsInBlock,'pfInterfacesIf6PktsOutPass':pfInterfacesIf6PktsOutPass,'pfInterfacesIf6PktsOutBlock':pfInterfacesIf6PktsOutBlock,'pfTables':pfTables,'pfTablesTblNumber':pfTablesTblNumber,'pfTablesTblTable':pfTablesTblTable,'pfTablesTblEntry':pfTablesTblEntry,_H:pfTablesTblIndex,'pfTablesTblDescr':pfTablesTblDescr,'pfTablesTblCount':pfTablesTblCount,'pfTablesTblTZero':pfTablesTblTZero,'pfTablesTblRefsAnchor':pfTablesTblRefsAnchor,'pfTablesTblRefsRule':pfTablesTblRefsRule,'pfTablesTblEvalMatch':pfTablesTblEvalMatch,'pfTablesTblEvalNoMatch':pfTablesTblEvalNoMatch,'pfTablesTblBytesInPass':pfTablesTblBytesInPass,'pfTablesTblBytesInBlock':pfTablesTblBytesInBlock,'pfTablesTblBytesInXPass':pfTablesTblBytesInXPass,'pfTablesTblBytesOutPass':pfTablesTblBytesOutPass,'pfTablesTblBytesOutBlock':pfTablesTblBytesOutBlock,'pfTablesTblBytesOutXPass':pfTablesTblBytesOutXPass,'pfTablesTblPktsInPass':pfTablesTblPktsInPass,'pfTablesTblPktsInBlock':pfTablesTblPktsInBlock,'pfTablesTblPktsInXPass':pfTablesTblPktsInXPass,'pfTablesTblPktsOutPass':pfTablesTblPktsOutPass,'pfTablesTblPktsOutBlock':pfTablesTblPktsOutBlock,'pfTablesTblPktsOutXPass':pfTablesTblPktsOutXPass,'pfTablesAddrTable':pfTablesAddrTable,'pfTablesAddrEntry':pfTablesAddrEntry,_I:pfTablesAddrIndex,'pfTablesAddrNetType':pfTablesAddrNetType,'pfTablesAddrNet':pfTablesAddrNet,'pfTablesAddrPrefix':pfTablesAddrPrefix,'pfTablesAddrTZero':pfTablesAddrTZero,'pfTablesAddrBytesInPass':pfTablesAddrBytesInPass,'pfTablesAddrBytesInBlock':pfTablesAddrBytesInBlock,'pfTablesAddrBytesOutPass':pfTablesAddrBytesOutPass,'pfTablesAddrBytesOutBlock':pfTablesAddrBytesOutBlock,'pfTablesAddrPktsInPass':pfTablesAddrPktsInPass,'pfTablesAddrPktsInBlock':pfTablesAddrPktsInBlock,'pfTablesAddrPktsOutPass':pfTablesAddrPktsOutPass,'pfTablesAddrPktsOutBlock':pfTablesAddrPktsOutBlock,'pfAltq':pfAltq,'pfAltqQueueNumber':pfAltqQueueNumber,'pfAltqQueueTable':pfAltqQueueTable,'pfAltqQueueEntry':pfAltqQueueEntry,_J:pfAltqQueueIndex,'pfAltqQueueDescr':pfAltqQueueDescr,'pfAltqQueueParent':pfAltqQueueParent,'pfAltqQueueScheduler':pfAltqQueueScheduler,'pfAltqQueueBandwidth':pfAltqQueueBandwidth,'pfAltqQueuePriority':pfAltqQueuePriority,'pfAltqQueueLimit':pfAltqQueueLimit,'pfLabels':pfLabels,'pfLabelsLblNumber':pfLabelsLblNumber,'pfLabelsLblTable':pfLabelsLblTable,'pfLabelsLblEntry':pfLabelsLblEntry,_K:pfLabelsLblIndex,'pfLabelsLblName':pfLabelsLblName,'pfLabelsLblEvals':pfLabelsLblEvals,'pfLabelsLblBytesIn':pfLabelsLblBytesIn,'pfLabelsLblBytesOut':pfLabelsLblBytesOut,'pfLabelsLblPktsIn':pfLabelsLblPktsIn,'pfLabelsLblPktsOut':pfLabelsLblPktsOut})