_q='fsPimStdNbrSecAddress'
_p='fsPimStdNbrSecAddressPrimary'
_o='fsPimStdNbrSecAddressType'
_n='fsPimStdNbrSecAddressIfIndex'
_m='fsPimStdComponentBSRAddrType'
_l='fsPimStdComponentBSRIndex'
_k='fsPimStdComponentIndex'
_j='fsPimStdCandidateRPGroupMaskLen'
_i='fsPimStdCandidateRPGroupAddress'
_h='fsPimStdCandidateRPAddrType'
_g='fsPimStdRPSetAddress'
_f='fsPimStdRPSetGroupMaskLen'
_e='fsPimStdRPSetGroupAddress'
_d='fsPimStdRPSetAddrType'
_c='fsPimStdRPSetComponent'
_b='fsPimStdRPAddress'
_a='fsPimStdRPGroupAddress'
_Z='fsPimStdRPAddrType'
_Y='fsPimStdIpMRouteNextHopAddress'
_X='fsPimStdIpMRouteNextHopIfIndex'
_W='fsPimStdIpMRouteNextHopSourceMaskLen'
_V='fsPimStdIpMRouteNextHopSource'
_U='fsPimStdIpMRouteNextHopGroup'
_T='fsPimStdIpMRouteNextHopAddrType'
_S='fsPimStdIpMRouteSourceMaskLen'
_R='fsPimStdIpMRouteSource'
_Q='fsPimStdIpMRouteGroup'
_P='fsPimStdIpMRouteAddrType'
_O='fsPimStdNeighborAddress'
_N='fsPimStdNeighborAddrType'
_M='sparse'
_L='fsPimStdInterfaceAddrType'
_K='fsPimStdInterfaceIfIndex'
_J='read-write'
_I='InetAddress'
_H='seconds'
_G='deprecated'
_F='read-create'
_E='Integer32'
_D='read-only'
_C='not-accessible'
_B='SUPERMICRO-PIMCMN2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsPimStdMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,114))
if mibBuilder.loadTexts:fsPimStdMIB.setRevisions(('2012-09-05 00:00',))
_FsPimStdMIBObjects_ObjectIdentity=ObjectIdentity
fsPimStdMIBObjects=_FsPimStdMIBObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,114,1))
_FsPimStdScalars_ObjectIdentity=ObjectIdentity
fsPimStdScalars=_FsPimStdScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,1,114,1,1))
_FsPimStdJoinPruneInterval_Type=Integer32
_FsPimStdJoinPruneInterval_Object=MibScalar
fsPimStdJoinPruneInterval=_FsPimStdJoinPruneInterval_Object((1,3,6,1,4,1,10876,101,1,114,1,1,1),_FsPimStdJoinPruneInterval_Type())
fsPimStdJoinPruneInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:fsPimStdJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimStdJoinPruneInterval.setUnits(_H)
_FsPimStdTables_ObjectIdentity=ObjectIdentity
fsPimStdTables=_FsPimStdTables_ObjectIdentity((1,3,6,1,4,1,10876,101,1,114,1,2))
_FsPimStdInterfaceTable_Object=MibTable
fsPimStdInterfaceTable=_FsPimStdInterfaceTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1))
if mibBuilder.loadTexts:fsPimStdInterfaceTable.setStatus(_A)
_FsPimStdInterfaceEntry_Object=MibTableRow
fsPimStdInterfaceEntry=_FsPimStdInterfaceEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1))
fsPimStdInterfaceEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:fsPimStdInterfaceEntry.setStatus(_A)
class _FsPimStdInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimStdInterfaceIfIndex_Type.__name__=_E
_FsPimStdInterfaceIfIndex_Object=MibTableColumn
fsPimStdInterfaceIfIndex=_FsPimStdInterfaceIfIndex_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,1),_FsPimStdInterfaceIfIndex_Type())
fsPimStdInterfaceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdInterfaceIfIndex.setStatus(_A)
_FsPimStdInterfaceAddrType_Type=InetAddressType
_FsPimStdInterfaceAddrType_Object=MibTableColumn
fsPimStdInterfaceAddrType=_FsPimStdInterfaceAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,2),_FsPimStdInterfaceAddrType_Type())
fsPimStdInterfaceAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdInterfaceAddrType.setStatus(_A)
_FsPimStdInterfaceAddress_Type=InetAddress
_FsPimStdInterfaceAddress_Object=MibTableColumn
fsPimStdInterfaceAddress=_FsPimStdInterfaceAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,3),_FsPimStdInterfaceAddress_Type())
fsPimStdInterfaceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdInterfaceAddress.setStatus(_A)
_FsPimStdInterfaceNetMaskLen_Type=Integer32
_FsPimStdInterfaceNetMaskLen_Object=MibTableColumn
fsPimStdInterfaceNetMaskLen=_FsPimStdInterfaceNetMaskLen_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,4),_FsPimStdInterfaceNetMaskLen_Type())
fsPimStdInterfaceNetMaskLen.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdInterfaceNetMaskLen.setStatus(_A)
class _FsPimStdInterfaceMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dense',1),(_M,2),('sparseDense',3)))
_FsPimStdInterfaceMode_Type.__name__=_E
_FsPimStdInterfaceMode_Object=MibTableColumn
fsPimStdInterfaceMode=_FsPimStdInterfaceMode_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,5),_FsPimStdInterfaceMode_Type())
fsPimStdInterfaceMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdInterfaceMode.setStatus(_A)
_FsPimStdInterfaceDR_Type=InetAddress
_FsPimStdInterfaceDR_Object=MibTableColumn
fsPimStdInterfaceDR=_FsPimStdInterfaceDR_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,6),_FsPimStdInterfaceDR_Type())
fsPimStdInterfaceDR.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdInterfaceDR.setStatus(_A)
class _FsPimStdInterfaceHelloInterval_Type(Integer32):defaultValue=30
_FsPimStdInterfaceHelloInterval_Type.__name__=_E
_FsPimStdInterfaceHelloInterval_Object=MibTableColumn
fsPimStdInterfaceHelloInterval=_FsPimStdInterfaceHelloInterval_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,7),_FsPimStdInterfaceHelloInterval_Type())
fsPimStdInterfaceHelloInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdInterfaceHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimStdInterfaceHelloInterval.setUnits(_H)
_FsPimStdInterfaceStatus_Type=RowStatus
_FsPimStdInterfaceStatus_Object=MibTableColumn
fsPimStdInterfaceStatus=_FsPimStdInterfaceStatus_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,8),_FsPimStdInterfaceStatus_Type())
fsPimStdInterfaceStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdInterfaceStatus.setStatus(_A)
_FsPimStdInterfaceJoinPruneInterval_Type=Integer32
_FsPimStdInterfaceJoinPruneInterval_Object=MibTableColumn
fsPimStdInterfaceJoinPruneInterval=_FsPimStdInterfaceJoinPruneInterval_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,9),_FsPimStdInterfaceJoinPruneInterval_Type())
fsPimStdInterfaceJoinPruneInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdInterfaceJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:fsPimStdInterfaceJoinPruneInterval.setUnits(_H)
class _FsPimStdInterfaceCBSRPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_FsPimStdInterfaceCBSRPreference_Type.__name__=_E
_FsPimStdInterfaceCBSRPreference_Object=MibTableColumn
fsPimStdInterfaceCBSRPreference=_FsPimStdInterfaceCBSRPreference_Object((1,3,6,1,4,1,10876,101,1,114,1,2,1,1,10),_FsPimStdInterfaceCBSRPreference_Type())
fsPimStdInterfaceCBSRPreference.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdInterfaceCBSRPreference.setStatus(_A)
_FsPimStdNeighborTable_Object=MibTable
fsPimStdNeighborTable=_FsPimStdNeighborTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2))
if mibBuilder.loadTexts:fsPimStdNeighborTable.setStatus(_A)
_FsPimStdNeighborEntry_Object=MibTableRow
fsPimStdNeighborEntry=_FsPimStdNeighborEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2,1))
fsPimStdNeighborEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:fsPimStdNeighborEntry.setStatus(_A)
_FsPimStdNeighborAddrType_Type=InetAddressType
_FsPimStdNeighborAddrType_Object=MibTableColumn
fsPimStdNeighborAddrType=_FsPimStdNeighborAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2,1,1),_FsPimStdNeighborAddrType_Type())
fsPimStdNeighborAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdNeighborAddrType.setStatus(_A)
_FsPimStdNeighborAddress_Type=InetAddress
_FsPimStdNeighborAddress_Object=MibTableColumn
fsPimStdNeighborAddress=_FsPimStdNeighborAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2,1,2),_FsPimStdNeighborAddress_Type())
fsPimStdNeighborAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdNeighborAddress.setStatus(_A)
_FsPimStdNeighborIfIndex_Type=Integer32
_FsPimStdNeighborIfIndex_Object=MibTableColumn
fsPimStdNeighborIfIndex=_FsPimStdNeighborIfIndex_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2,1,3),_FsPimStdNeighborIfIndex_Type())
fsPimStdNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdNeighborIfIndex.setStatus(_A)
_FsPimStdNeighborUpTime_Type=TimeTicks
_FsPimStdNeighborUpTime_Object=MibTableColumn
fsPimStdNeighborUpTime=_FsPimStdNeighborUpTime_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2,1,4),_FsPimStdNeighborUpTime_Type())
fsPimStdNeighborUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdNeighborUpTime.setStatus(_A)
_FsPimStdNeighborExpiryTime_Type=TimeTicks
_FsPimStdNeighborExpiryTime_Object=MibTableColumn
fsPimStdNeighborExpiryTime=_FsPimStdNeighborExpiryTime_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2,1,5),_FsPimStdNeighborExpiryTime_Type())
fsPimStdNeighborExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdNeighborExpiryTime.setStatus(_A)
class _FsPimStdNeighborMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),(_M,2)))
_FsPimStdNeighborMode_Type.__name__=_E
_FsPimStdNeighborMode_Object=MibTableColumn
fsPimStdNeighborMode=_FsPimStdNeighborMode_Object((1,3,6,1,4,1,10876,101,1,114,1,2,2,1,6),_FsPimStdNeighborMode_Type())
fsPimStdNeighborMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdNeighborMode.setStatus(_G)
_FsPimStdIpMRouteTable_Object=MibTable
fsPimStdIpMRouteTable=_FsPimStdIpMRouteTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3))
if mibBuilder.loadTexts:fsPimStdIpMRouteTable.setStatus(_A)
_FsPimStdIpMRouteEntry_Object=MibTableRow
fsPimStdIpMRouteEntry=_FsPimStdIpMRouteEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1))
fsPimStdIpMRouteEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:fsPimStdIpMRouteEntry.setStatus(_A)
_FsPimStdIpMRouteAddrType_Type=InetAddressType
_FsPimStdIpMRouteAddrType_Object=MibTableColumn
fsPimStdIpMRouteAddrType=_FsPimStdIpMRouteAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,2),_FsPimStdIpMRouteAddrType_Type())
fsPimStdIpMRouteAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteAddrType.setStatus(_A)
_FsPimStdIpMRouteGroup_Type=InetAddress
_FsPimStdIpMRouteGroup_Object=MibTableColumn
fsPimStdIpMRouteGroup=_FsPimStdIpMRouteGroup_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,3),_FsPimStdIpMRouteGroup_Type())
fsPimStdIpMRouteGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteGroup.setStatus(_A)
_FsPimStdIpMRouteSource_Type=InetAddress
_FsPimStdIpMRouteSource_Object=MibTableColumn
fsPimStdIpMRouteSource=_FsPimStdIpMRouteSource_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,4),_FsPimStdIpMRouteSource_Type())
fsPimStdIpMRouteSource.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteSource.setStatus(_A)
class _FsPimStdIpMRouteSourceMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimStdIpMRouteSourceMaskLen_Type.__name__=_E
_FsPimStdIpMRouteSourceMaskLen_Object=MibTableColumn
fsPimStdIpMRouteSourceMaskLen=_FsPimStdIpMRouteSourceMaskLen_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,5),_FsPimStdIpMRouteSourceMaskLen_Type())
fsPimStdIpMRouteSourceMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteSourceMaskLen.setStatus(_A)
_FsPimStdIpMRouteUpstreamAssertTimer_Type=TimeTicks
_FsPimStdIpMRouteUpstreamAssertTimer_Object=MibTableColumn
fsPimStdIpMRouteUpstreamAssertTimer=_FsPimStdIpMRouteUpstreamAssertTimer_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,6),_FsPimStdIpMRouteUpstreamAssertTimer_Type())
fsPimStdIpMRouteUpstreamAssertTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdIpMRouteUpstreamAssertTimer.setStatus(_A)
_FsPimStdIpMRouteAssertMetric_Type=Integer32
_FsPimStdIpMRouteAssertMetric_Object=MibTableColumn
fsPimStdIpMRouteAssertMetric=_FsPimStdIpMRouteAssertMetric_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,7),_FsPimStdIpMRouteAssertMetric_Type())
fsPimStdIpMRouteAssertMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdIpMRouteAssertMetric.setStatus(_A)
_FsPimStdIpMRouteAssertMetricPref_Type=Integer32
_FsPimStdIpMRouteAssertMetricPref_Object=MibTableColumn
fsPimStdIpMRouteAssertMetricPref=_FsPimStdIpMRouteAssertMetricPref_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,8),_FsPimStdIpMRouteAssertMetricPref_Type())
fsPimStdIpMRouteAssertMetricPref.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdIpMRouteAssertMetricPref.setStatus(_A)
_FsPimStdIpMRouteAssertRPTBit_Type=TruthValue
_FsPimStdIpMRouteAssertRPTBit_Object=MibTableColumn
fsPimStdIpMRouteAssertRPTBit=_FsPimStdIpMRouteAssertRPTBit_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,9),_FsPimStdIpMRouteAssertRPTBit_Type())
fsPimStdIpMRouteAssertRPTBit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdIpMRouteAssertRPTBit.setStatus(_A)
class _FsPimStdIpMRouteFlags_Type(Bits):namedValues=NamedValues(*(('rpt',0),('spt',1)))
_FsPimStdIpMRouteFlags_Type.__name__='Bits'
_FsPimStdIpMRouteFlags_Object=MibTableColumn
fsPimStdIpMRouteFlags=_FsPimStdIpMRouteFlags_Object((1,3,6,1,4,1,10876,101,1,114,1,2,3,1,10),_FsPimStdIpMRouteFlags_Type())
fsPimStdIpMRouteFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdIpMRouteFlags.setStatus(_A)
_FsPimStdIpMRouteNextHopTable_Object=MibTable
fsPimStdIpMRouteNextHopTable=_FsPimStdIpMRouteNextHopTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4))
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopTable.setStatus(_A)
_FsPimStdIpMRouteNextHopEntry_Object=MibTableRow
fsPimStdIpMRouteNextHopEntry=_FsPimStdIpMRouteNextHopEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1))
fsPimStdIpMRouteNextHopEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopEntry.setStatus(_A)
_FsPimStdIpMRouteNextHopAddrType_Type=InetAddressType
_FsPimStdIpMRouteNextHopAddrType_Object=MibTableColumn
fsPimStdIpMRouteNextHopAddrType=_FsPimStdIpMRouteNextHopAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1,2),_FsPimStdIpMRouteNextHopAddrType_Type())
fsPimStdIpMRouteNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopAddrType.setStatus(_A)
_FsPimStdIpMRouteNextHopGroup_Type=InetAddress
_FsPimStdIpMRouteNextHopGroup_Object=MibTableColumn
fsPimStdIpMRouteNextHopGroup=_FsPimStdIpMRouteNextHopGroup_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1,3),_FsPimStdIpMRouteNextHopGroup_Type())
fsPimStdIpMRouteNextHopGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopGroup.setStatus(_A)
_FsPimStdIpMRouteNextHopSource_Type=InetAddress
_FsPimStdIpMRouteNextHopSource_Object=MibTableColumn
fsPimStdIpMRouteNextHopSource=_FsPimStdIpMRouteNextHopSource_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1,4),_FsPimStdIpMRouteNextHopSource_Type())
fsPimStdIpMRouteNextHopSource.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopSource.setStatus(_A)
class _FsPimStdIpMRouteNextHopSourceMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimStdIpMRouteNextHopSourceMaskLen_Type.__name__=_E
_FsPimStdIpMRouteNextHopSourceMaskLen_Object=MibTableColumn
fsPimStdIpMRouteNextHopSourceMaskLen=_FsPimStdIpMRouteNextHopSourceMaskLen_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1,5),_FsPimStdIpMRouteNextHopSourceMaskLen_Type())
fsPimStdIpMRouteNextHopSourceMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopSourceMaskLen.setStatus(_A)
class _FsPimStdIpMRouteNextHopIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPimStdIpMRouteNextHopIfIndex_Type.__name__=_E
_FsPimStdIpMRouteNextHopIfIndex_Object=MibTableColumn
fsPimStdIpMRouteNextHopIfIndex=_FsPimStdIpMRouteNextHopIfIndex_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1,6),_FsPimStdIpMRouteNextHopIfIndex_Type())
fsPimStdIpMRouteNextHopIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopIfIndex.setStatus(_A)
_FsPimStdIpMRouteNextHopAddress_Type=InetAddress
_FsPimStdIpMRouteNextHopAddress_Object=MibTableColumn
fsPimStdIpMRouteNextHopAddress=_FsPimStdIpMRouteNextHopAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1,7),_FsPimStdIpMRouteNextHopAddress_Type())
fsPimStdIpMRouteNextHopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopAddress.setStatus(_A)
class _FsPimStdIpMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('prune',2),('assert',3)))
_FsPimStdIpMRouteNextHopPruneReason_Type.__name__=_E
_FsPimStdIpMRouteNextHopPruneReason_Object=MibTableColumn
fsPimStdIpMRouteNextHopPruneReason=_FsPimStdIpMRouteNextHopPruneReason_Object((1,3,6,1,4,1,10876,101,1,114,1,2,4,1,8),_FsPimStdIpMRouteNextHopPruneReason_Type())
fsPimStdIpMRouteNextHopPruneReason.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdIpMRouteNextHopPruneReason.setStatus(_A)
_FsPimStdRPTable_Object=MibTable
fsPimStdRPTable=_FsPimStdRPTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5))
if mibBuilder.loadTexts:fsPimStdRPTable.setStatus(_G)
_FsPimStdRPEntry_Object=MibTableRow
fsPimStdRPEntry=_FsPimStdRPEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1))
fsPimStdRPEntry.setIndexNames((0,_B,_Z),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:fsPimStdRPEntry.setStatus(_G)
_FsPimStdRPAddrType_Type=InetAddressType
_FsPimStdRPAddrType_Object=MibTableColumn
fsPimStdRPAddrType=_FsPimStdRPAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1,1),_FsPimStdRPAddrType_Type())
fsPimStdRPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPAddrType.setStatus(_A)
_FsPimStdRPGroupAddress_Type=InetAddress
_FsPimStdRPGroupAddress_Object=MibTableColumn
fsPimStdRPGroupAddress=_FsPimStdRPGroupAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1,2),_FsPimStdRPGroupAddress_Type())
fsPimStdRPGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPGroupAddress.setStatus(_G)
_FsPimStdRPAddress_Type=InetAddress
_FsPimStdRPAddress_Object=MibTableColumn
fsPimStdRPAddress=_FsPimStdRPAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1,3),_FsPimStdRPAddress_Type())
fsPimStdRPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPAddress.setStatus(_G)
class _FsPimStdRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsPimStdRPState_Type.__name__=_E
_FsPimStdRPState_Object=MibTableColumn
fsPimStdRPState=_FsPimStdRPState_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1,4),_FsPimStdRPState_Type())
fsPimStdRPState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdRPState.setStatus(_G)
_FsPimStdRPStateTimer_Type=TimeTicks
_FsPimStdRPStateTimer_Object=MibTableColumn
fsPimStdRPStateTimer=_FsPimStdRPStateTimer_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1,5),_FsPimStdRPStateTimer_Type())
fsPimStdRPStateTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdRPStateTimer.setStatus(_G)
_FsPimStdRPLastChange_Type=TimeTicks
_FsPimStdRPLastChange_Object=MibTableColumn
fsPimStdRPLastChange=_FsPimStdRPLastChange_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1,6),_FsPimStdRPLastChange_Type())
fsPimStdRPLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdRPLastChange.setStatus(_G)
_FsPimStdRPRowStatus_Type=RowStatus
_FsPimStdRPRowStatus_Object=MibTableColumn
fsPimStdRPRowStatus=_FsPimStdRPRowStatus_Object((1,3,6,1,4,1,10876,101,1,114,1,2,5,1,7),_FsPimStdRPRowStatus_Type())
fsPimStdRPRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdRPRowStatus.setStatus(_G)
_FsPimStdRPSetTable_Object=MibTable
fsPimStdRPSetTable=_FsPimStdRPSetTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6))
if mibBuilder.loadTexts:fsPimStdRPSetTable.setStatus(_A)
_FsPimStdRPSetEntry_Object=MibTableRow
fsPimStdRPSetEntry=_FsPimStdRPSetEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1))
fsPimStdRPSetEntry.setIndexNames((0,_B,_c),(0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:fsPimStdRPSetEntry.setStatus(_A)
_FsPimStdRPSetAddrType_Type=InetAddressType
_FsPimStdRPSetAddrType_Object=MibTableColumn
fsPimStdRPSetAddrType=_FsPimStdRPSetAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,1),_FsPimStdRPSetAddrType_Type())
fsPimStdRPSetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPSetAddrType.setStatus(_A)
_FsPimStdRPSetGroupAddress_Type=InetAddress
_FsPimStdRPSetGroupAddress_Object=MibTableColumn
fsPimStdRPSetGroupAddress=_FsPimStdRPSetGroupAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,2),_FsPimStdRPSetGroupAddress_Type())
fsPimStdRPSetGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPSetGroupAddress.setStatus(_A)
class _FsPimStdRPSetGroupMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimStdRPSetGroupMaskLen_Type.__name__=_E
_FsPimStdRPSetGroupMaskLen_Object=MibTableColumn
fsPimStdRPSetGroupMaskLen=_FsPimStdRPSetGroupMaskLen_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,3),_FsPimStdRPSetGroupMaskLen_Type())
fsPimStdRPSetGroupMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPSetGroupMaskLen.setStatus(_A)
_FsPimStdRPSetAddress_Type=InetAddress
_FsPimStdRPSetAddress_Object=MibTableColumn
fsPimStdRPSetAddress=_FsPimStdRPSetAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,4),_FsPimStdRPSetAddress_Type())
fsPimStdRPSetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPSetAddress.setStatus(_A)
class _FsPimStdRPSetHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimStdRPSetHoldTime_Type.__name__=_E
_FsPimStdRPSetHoldTime_Object=MibTableColumn
fsPimStdRPSetHoldTime=_FsPimStdRPSetHoldTime_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,5),_FsPimStdRPSetHoldTime_Type())
fsPimStdRPSetHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdRPSetHoldTime.setStatus(_A)
if mibBuilder.loadTexts:fsPimStdRPSetHoldTime.setUnits(_H)
_FsPimStdRPSetExpiryTime_Type=TimeTicks
_FsPimStdRPSetExpiryTime_Object=MibTableColumn
fsPimStdRPSetExpiryTime=_FsPimStdRPSetExpiryTime_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,6),_FsPimStdRPSetExpiryTime_Type())
fsPimStdRPSetExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdRPSetExpiryTime.setStatus(_A)
class _FsPimStdRPSetComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimStdRPSetComponent_Type.__name__=_E
_FsPimStdRPSetComponent_Object=MibTableColumn
fsPimStdRPSetComponent=_FsPimStdRPSetComponent_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,7),_FsPimStdRPSetComponent_Type())
fsPimStdRPSetComponent.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdRPSetComponent.setStatus(_A)
class _FsPimStdRPSetPimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dm',1),('sm',2),('ssm',3),('bidir',4)))
_FsPimStdRPSetPimMode_Type.__name__=_E
_FsPimStdRPSetPimMode_Object=MibTableColumn
fsPimStdRPSetPimMode=_FsPimStdRPSetPimMode_Object((1,3,6,1,4,1,10876,101,1,114,1,2,6,1,11),_FsPimStdRPSetPimMode_Type())
fsPimStdRPSetPimMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdRPSetPimMode.setStatus(_A)
_FsPimStdCandidateRPTable_Object=MibTable
fsPimStdCandidateRPTable=_FsPimStdCandidateRPTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,7))
if mibBuilder.loadTexts:fsPimStdCandidateRPTable.setStatus(_A)
_FsPimStdCandidateRPEntry_Object=MibTableRow
fsPimStdCandidateRPEntry=_FsPimStdCandidateRPEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,7,1))
fsPimStdCandidateRPEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:fsPimStdCandidateRPEntry.setStatus(_A)
_FsPimStdCandidateRPAddrType_Type=InetAddressType
_FsPimStdCandidateRPAddrType_Object=MibTableColumn
fsPimStdCandidateRPAddrType=_FsPimStdCandidateRPAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,7,1,1),_FsPimStdCandidateRPAddrType_Type())
fsPimStdCandidateRPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdCandidateRPAddrType.setStatus(_A)
_FsPimStdCandidateRPGroupAddress_Type=InetAddress
_FsPimStdCandidateRPGroupAddress_Object=MibTableColumn
fsPimStdCandidateRPGroupAddress=_FsPimStdCandidateRPGroupAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,7,1,2),_FsPimStdCandidateRPGroupAddress_Type())
fsPimStdCandidateRPGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdCandidateRPGroupAddress.setStatus(_A)
class _FsPimStdCandidateRPGroupMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPimStdCandidateRPGroupMaskLen_Type.__name__=_E
_FsPimStdCandidateRPGroupMaskLen_Object=MibTableColumn
fsPimStdCandidateRPGroupMaskLen=_FsPimStdCandidateRPGroupMaskLen_Object((1,3,6,1,4,1,10876,101,1,114,1,2,7,1,3),_FsPimStdCandidateRPGroupMaskLen_Type())
fsPimStdCandidateRPGroupMaskLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdCandidateRPGroupMaskLen.setStatus(_A)
_FsPimStdCandidateRPAddress_Type=InetAddress
_FsPimStdCandidateRPAddress_Object=MibTableColumn
fsPimStdCandidateRPAddress=_FsPimStdCandidateRPAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,7,1,4),_FsPimStdCandidateRPAddress_Type())
fsPimStdCandidateRPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdCandidateRPAddress.setStatus(_A)
_FsPimStdCandidateRPRowStatus_Type=RowStatus
_FsPimStdCandidateRPRowStatus_Object=MibTableColumn
fsPimStdCandidateRPRowStatus=_FsPimStdCandidateRPRowStatus_Object((1,3,6,1,4,1,10876,101,1,114,1,2,7,1,5),_FsPimStdCandidateRPRowStatus_Type())
fsPimStdCandidateRPRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdCandidateRPRowStatus.setStatus(_A)
_FsPimStdComponentTable_Object=MibTable
fsPimStdComponentTable=_FsPimStdComponentTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,8))
if mibBuilder.loadTexts:fsPimStdComponentTable.setStatus(_A)
_FsPimStdComponentEntry_Object=MibTableRow
fsPimStdComponentEntry=_FsPimStdComponentEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,8,1))
fsPimStdComponentEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:fsPimStdComponentEntry.setStatus(_A)
class _FsPimStdComponentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimStdComponentIndex_Type.__name__=_E
_FsPimStdComponentIndex_Object=MibTableColumn
fsPimStdComponentIndex=_FsPimStdComponentIndex_Object((1,3,6,1,4,1,10876,101,1,114,1,2,8,1,1),_FsPimStdComponentIndex_Type())
fsPimStdComponentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdComponentIndex.setStatus(_A)
_FsPimStdComponentBSRExpiryTime_Type=TimeTicks
_FsPimStdComponentBSRExpiryTime_Object=MibTableColumn
fsPimStdComponentBSRExpiryTime=_FsPimStdComponentBSRExpiryTime_Object((1,3,6,1,4,1,10876,101,1,114,1,2,8,1,2),_FsPimStdComponentBSRExpiryTime_Type())
fsPimStdComponentBSRExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdComponentBSRExpiryTime.setStatus(_A)
class _FsPimStdComponentCRPHoldTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPimStdComponentCRPHoldTime_Type.__name__=_E
_FsPimStdComponentCRPHoldTime_Object=MibTableColumn
fsPimStdComponentCRPHoldTime=_FsPimStdComponentCRPHoldTime_Object((1,3,6,1,4,1,10876,101,1,114,1,2,8,1,3),_FsPimStdComponentCRPHoldTime_Type())
fsPimStdComponentCRPHoldTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdComponentCRPHoldTime.setStatus(_A)
if mibBuilder.loadTexts:fsPimStdComponentCRPHoldTime.setUnits(_H)
_FsPimStdComponentStatus_Type=RowStatus
_FsPimStdComponentStatus_Object=MibTableColumn
fsPimStdComponentStatus=_FsPimStdComponentStatus_Object((1,3,6,1,4,1,10876,101,1,114,1,2,8,1,4),_FsPimStdComponentStatus_Type())
fsPimStdComponentStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPimStdComponentStatus.setStatus(_A)
_FsPimStdComponentScopeZoneName_Type=DisplayString
_FsPimStdComponentScopeZoneName_Object=MibTableColumn
fsPimStdComponentScopeZoneName=_FsPimStdComponentScopeZoneName_Object((1,3,6,1,4,1,10876,101,1,114,1,2,8,1,5),_FsPimStdComponentScopeZoneName_Type())
fsPimStdComponentScopeZoneName.setMaxAccess(_J)
if mibBuilder.loadTexts:fsPimStdComponentScopeZoneName.setStatus(_A)
_FsPimStdComponentBSRTable_Object=MibTable
fsPimStdComponentBSRTable=_FsPimStdComponentBSRTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,9))
if mibBuilder.loadTexts:fsPimStdComponentBSRTable.setStatus(_A)
_FsPimStdComponentBSREntry_Object=MibTableRow
fsPimStdComponentBSREntry=_FsPimStdComponentBSREntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,9,1))
fsPimStdComponentBSREntry.setIndexNames((0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:fsPimStdComponentBSREntry.setStatus(_A)
class _FsPimStdComponentBSRIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsPimStdComponentBSRIndex_Type.__name__=_E
_FsPimStdComponentBSRIndex_Object=MibTableColumn
fsPimStdComponentBSRIndex=_FsPimStdComponentBSRIndex_Object((1,3,6,1,4,1,10876,101,1,114,1,2,9,1,1),_FsPimStdComponentBSRIndex_Type())
fsPimStdComponentBSRIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdComponentBSRIndex.setStatus(_A)
_FsPimStdComponentBSRAddrType_Type=InetAddressType
_FsPimStdComponentBSRAddrType_Object=MibTableColumn
fsPimStdComponentBSRAddrType=_FsPimStdComponentBSRAddrType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,9,1,2),_FsPimStdComponentBSRAddrType_Type())
fsPimStdComponentBSRAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdComponentBSRAddrType.setStatus(_A)
_FsPimStdComponentBSRAddress_Type=InetAddress
_FsPimStdComponentBSRAddress_Object=MibTableColumn
fsPimStdComponentBSRAddress=_FsPimStdComponentBSRAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,9,1,3),_FsPimStdComponentBSRAddress_Type())
fsPimStdComponentBSRAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdComponentBSRAddress.setStatus(_A)
_FsPimStdNbrSecAddressTable_Object=MibTable
fsPimStdNbrSecAddressTable=_FsPimStdNbrSecAddressTable_Object((1,3,6,1,4,1,10876,101,1,114,1,2,10))
if mibBuilder.loadTexts:fsPimStdNbrSecAddressTable.setStatus(_A)
_FsPimStdNbrSecAddressEntry_Object=MibTableRow
fsPimStdNbrSecAddressEntry=_FsPimStdNbrSecAddressEntry_Object((1,3,6,1,4,1,10876,101,1,114,1,2,10,1))
fsPimStdNbrSecAddressEntry.setIndexNames((0,_B,_n),(0,_B,_o),(0,_B,_p),(0,_B,_q))
if mibBuilder.loadTexts:fsPimStdNbrSecAddressEntry.setStatus(_A)
_FsPimStdNbrSecAddressIfIndex_Type=InterfaceIndex
_FsPimStdNbrSecAddressIfIndex_Object=MibTableColumn
fsPimStdNbrSecAddressIfIndex=_FsPimStdNbrSecAddressIfIndex_Object((1,3,6,1,4,1,10876,101,1,114,1,2,10,1,1),_FsPimStdNbrSecAddressIfIndex_Type())
fsPimStdNbrSecAddressIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdNbrSecAddressIfIndex.setStatus(_A)
_FsPimStdNbrSecAddressType_Type=InetAddressType
_FsPimStdNbrSecAddressType_Object=MibTableColumn
fsPimStdNbrSecAddressType=_FsPimStdNbrSecAddressType_Object((1,3,6,1,4,1,10876,101,1,114,1,2,10,1,2),_FsPimStdNbrSecAddressType_Type())
fsPimStdNbrSecAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdNbrSecAddressType.setStatus(_A)
class _FsPimStdNbrSecAddressPrimary_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_FsPimStdNbrSecAddressPrimary_Type.__name__=_I
_FsPimStdNbrSecAddressPrimary_Object=MibTableColumn
fsPimStdNbrSecAddressPrimary=_FsPimStdNbrSecAddressPrimary_Object((1,3,6,1,4,1,10876,101,1,114,1,2,10,1,3),_FsPimStdNbrSecAddressPrimary_Type())
fsPimStdNbrSecAddressPrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPimStdNbrSecAddressPrimary.setStatus(_A)
class _FsPimStdNbrSecAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_FsPimStdNbrSecAddress_Type.__name__=_I
_FsPimStdNbrSecAddress_Object=MibTableColumn
fsPimStdNbrSecAddress=_FsPimStdNbrSecAddress_Object((1,3,6,1,4,1,10876,101,1,114,1,2,10,1,4),_FsPimStdNbrSecAddress_Type())
fsPimStdNbrSecAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPimStdNbrSecAddress.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsPimStdMIB':fsPimStdMIB,'fsPimStdMIBObjects':fsPimStdMIBObjects,'fsPimStdScalars':fsPimStdScalars,'fsPimStdJoinPruneInterval':fsPimStdJoinPruneInterval,'fsPimStdTables':fsPimStdTables,'fsPimStdInterfaceTable':fsPimStdInterfaceTable,'fsPimStdInterfaceEntry':fsPimStdInterfaceEntry,_K:fsPimStdInterfaceIfIndex,_L:fsPimStdInterfaceAddrType,'fsPimStdInterfaceAddress':fsPimStdInterfaceAddress,'fsPimStdInterfaceNetMaskLen':fsPimStdInterfaceNetMaskLen,'fsPimStdInterfaceMode':fsPimStdInterfaceMode,'fsPimStdInterfaceDR':fsPimStdInterfaceDR,'fsPimStdInterfaceHelloInterval':fsPimStdInterfaceHelloInterval,'fsPimStdInterfaceStatus':fsPimStdInterfaceStatus,'fsPimStdInterfaceJoinPruneInterval':fsPimStdInterfaceJoinPruneInterval,'fsPimStdInterfaceCBSRPreference':fsPimStdInterfaceCBSRPreference,'fsPimStdNeighborTable':fsPimStdNeighborTable,'fsPimStdNeighborEntry':fsPimStdNeighborEntry,_N:fsPimStdNeighborAddrType,_O:fsPimStdNeighborAddress,'fsPimStdNeighborIfIndex':fsPimStdNeighborIfIndex,'fsPimStdNeighborUpTime':fsPimStdNeighborUpTime,'fsPimStdNeighborExpiryTime':fsPimStdNeighborExpiryTime,'fsPimStdNeighborMode':fsPimStdNeighborMode,'fsPimStdIpMRouteTable':fsPimStdIpMRouteTable,'fsPimStdIpMRouteEntry':fsPimStdIpMRouteEntry,_P:fsPimStdIpMRouteAddrType,_Q:fsPimStdIpMRouteGroup,_R:fsPimStdIpMRouteSource,_S:fsPimStdIpMRouteSourceMaskLen,'fsPimStdIpMRouteUpstreamAssertTimer':fsPimStdIpMRouteUpstreamAssertTimer,'fsPimStdIpMRouteAssertMetric':fsPimStdIpMRouteAssertMetric,'fsPimStdIpMRouteAssertMetricPref':fsPimStdIpMRouteAssertMetricPref,'fsPimStdIpMRouteAssertRPTBit':fsPimStdIpMRouteAssertRPTBit,'fsPimStdIpMRouteFlags':fsPimStdIpMRouteFlags,'fsPimStdIpMRouteNextHopTable':fsPimStdIpMRouteNextHopTable,'fsPimStdIpMRouteNextHopEntry':fsPimStdIpMRouteNextHopEntry,_T:fsPimStdIpMRouteNextHopAddrType,_U:fsPimStdIpMRouteNextHopGroup,_V:fsPimStdIpMRouteNextHopSource,_W:fsPimStdIpMRouteNextHopSourceMaskLen,_X:fsPimStdIpMRouteNextHopIfIndex,_Y:fsPimStdIpMRouteNextHopAddress,'fsPimStdIpMRouteNextHopPruneReason':fsPimStdIpMRouteNextHopPruneReason,'fsPimStdRPTable':fsPimStdRPTable,'fsPimStdRPEntry':fsPimStdRPEntry,_Z:fsPimStdRPAddrType,_a:fsPimStdRPGroupAddress,_b:fsPimStdRPAddress,'fsPimStdRPState':fsPimStdRPState,'fsPimStdRPStateTimer':fsPimStdRPStateTimer,'fsPimStdRPLastChange':fsPimStdRPLastChange,'fsPimStdRPRowStatus':fsPimStdRPRowStatus,'fsPimStdRPSetTable':fsPimStdRPSetTable,'fsPimStdRPSetEntry':fsPimStdRPSetEntry,_d:fsPimStdRPSetAddrType,_e:fsPimStdRPSetGroupAddress,_f:fsPimStdRPSetGroupMaskLen,_g:fsPimStdRPSetAddress,'fsPimStdRPSetHoldTime':fsPimStdRPSetHoldTime,'fsPimStdRPSetExpiryTime':fsPimStdRPSetExpiryTime,_c:fsPimStdRPSetComponent,'fsPimStdRPSetPimMode':fsPimStdRPSetPimMode,'fsPimStdCandidateRPTable':fsPimStdCandidateRPTable,'fsPimStdCandidateRPEntry':fsPimStdCandidateRPEntry,_h:fsPimStdCandidateRPAddrType,_i:fsPimStdCandidateRPGroupAddress,_j:fsPimStdCandidateRPGroupMaskLen,'fsPimStdCandidateRPAddress':fsPimStdCandidateRPAddress,'fsPimStdCandidateRPRowStatus':fsPimStdCandidateRPRowStatus,'fsPimStdComponentTable':fsPimStdComponentTable,'fsPimStdComponentEntry':fsPimStdComponentEntry,_k:fsPimStdComponentIndex,'fsPimStdComponentBSRExpiryTime':fsPimStdComponentBSRExpiryTime,'fsPimStdComponentCRPHoldTime':fsPimStdComponentCRPHoldTime,'fsPimStdComponentStatus':fsPimStdComponentStatus,'fsPimStdComponentScopeZoneName':fsPimStdComponentScopeZoneName,'fsPimStdComponentBSRTable':fsPimStdComponentBSRTable,'fsPimStdComponentBSREntry':fsPimStdComponentBSREntry,_l:fsPimStdComponentBSRIndex,_m:fsPimStdComponentBSRAddrType,'fsPimStdComponentBSRAddress':fsPimStdComponentBSRAddress,'fsPimStdNbrSecAddressTable':fsPimStdNbrSecAddressTable,'fsPimStdNbrSecAddressEntry':fsPimStdNbrSecAddressEntry,_n:fsPimStdNbrSecAddressIfIndex,_o:fsPimStdNbrSecAddressType,_p:fsPimStdNbrSecAddressPrimary,_q:fsPimStdNbrSecAddress})