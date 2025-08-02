_AC='cPimDenseV2MIBGroup'
_AB='cPimV2CRPMIBGroup'
_AA='cPimV2MIBGroup'
_A9='cPimNbrLoss'
_A8='cPimInetMRouteAssertRPTBit'
_A7='cPimInetMRouteAssertMetricPref'
_A6='cPimInetMRouteAssertMetric'
_A5='cPimInetMRouteNextHopPruneReason'
_A4='cPimCRPRowStatus'
_A3='cPimCRPAddress'
_A2='cPimInetMRouteUpstreamAssertTime'
_A1='cPimInetMRouteFlags'
_A0='cPimComponentStatus'
_z='cPimComponentCRPHoldTime'
_y='cPimComponentBSRExpiryTime'
_x='cPimComponentBSRAddress'
_w='cPimComponentBSRAddrType'
_v='cPimRPMapExpiryTime'
_u='cPimRPMapHoldTime'
_t='cPimIfCBSRPreference'
_s='cPimIfJoinPruneInterval'
_r='cPimIfAddressType'
_q='cPimJoinPruneInterval'
_p='cPimComponentIndex'
_o='cPimCRPGroupMask'
_n='cPimCRPGroupAddress'
_m='cPimCRPAddrType'
_l='cPimRPMapAddress'
_k='cPimRPMapGroupMask'
_j='cPimRPMapGroupAddress'
_i='cPimRPMapAddrType'
_h='cPimRPMapComponent'
_g='cPimNbrAddress'
_f='cPimNbrAddressType'
_e='cPimNbrIfIndex'
_d='cPimIfInetVersion'
_c='cPimIfIndex'
_b='cIpMRouteSourceMask'
_a='cIpMRouteSource'
_Z='cIpMRouteNextHopSourceMask'
_Y='cIpMRouteNextHopSource'
_X='cIpMRouteNextHopIfIndex'
_W='cIpMRouteNextHopGroup'
_V='cIpMRouteNextHopAddress'
_U='cIpMRouteNextHopAddrType'
_T='cIpMRouteGroup'
_S='cIpMRouteAddrType'
_R='cPimIfMode'
_Q='cPimIfStatus'
_P='cPimIfHelloInterval'
_O='cPimIfDR'
_N='cPimIfNetMask'
_M='cPimIfAddress'
_L='cPimNbrExpiryTime'
_K='cPimNbrUpTime'
_J='Integer32'
_I='seconds'
_H='InetAddress'
_G='Unsigned32'
_F='CISCO-IETF-IPMROUTE-MIB'
_E='read-only'
_D='read-create'
_C='not-accessible'
_B='CISCO-IETF-PIM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cIpMRouteAddrType,cIpMRouteGroup,cIpMRouteNextHopAddrType,cIpMRouteNextHopAddress,cIpMRouteNextHopGroup,cIpMRouteNextHopIfIndex,cIpMRouteNextHopSource,cIpMRouteNextHopSourceMask,cIpMRouteSource,cIpMRouteSourceMask=mibBuilder.importSymbols(_F,_S,_T,_U,_V,_W,_X,_Y,_Z,_a,_b)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType,InetVersion=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,'InetAddressPrefixLength','InetAddressType','InetVersion')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoIetfPimMIB=ModuleIdentity((1,3,6,1,4,1,9,10,119))
if mibBuilder.loadTexts:ciscoIetfPimMIB.setRevisions(('2005-02-22 00:00',))
_CPimNotifs_ObjectIdentity=ObjectIdentity
cPimNotifs=_CPimNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,119,0))
_CPimMIBObjects_ObjectIdentity=ObjectIdentity
cPimMIBObjects=_CPimMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,119,1))
_CPim_ObjectIdentity=ObjectIdentity
cPim=_CPim_ObjectIdentity((1,3,6,1,4,1,9,10,119,1,1))
class _CPimJoinPruneInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CPimJoinPruneInterval_Type.__name__=_G
_CPimJoinPruneInterval_Object=MibScalar
cPimJoinPruneInterval=_CPimJoinPruneInterval_Object((1,3,6,1,4,1,9,10,119,1,1,1),_CPimJoinPruneInterval_Type())
cPimJoinPruneInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:cPimJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:cPimJoinPruneInterval.setUnits(_I)
_CPimIfTable_Object=MibTable
cPimIfTable=_CPimIfTable_Object((1,3,6,1,4,1,9,10,119,1,1,2))
if mibBuilder.loadTexts:cPimIfTable.setStatus(_A)
_CPimIfEntry_Object=MibTableRow
cPimIfEntry=_CPimIfEntry_Object((1,3,6,1,4,1,9,10,119,1,1,2,1))
cPimIfEntry.setIndexNames((0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:cPimIfEntry.setStatus(_A)
_CPimIfIndex_Type=InterfaceIndex
_CPimIfIndex_Object=MibTableColumn
cPimIfIndex=_CPimIfIndex_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,1),_CPimIfIndex_Type())
cPimIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimIfIndex.setStatus(_A)
_CPimIfInetVersion_Type=InetVersion
_CPimIfInetVersion_Object=MibTableColumn
cPimIfInetVersion=_CPimIfInetVersion_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,2),_CPimIfInetVersion_Type())
cPimIfInetVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimIfInetVersion.setStatus(_A)
_CPimIfAddressType_Type=InetAddressType
_CPimIfAddressType_Object=MibTableColumn
cPimIfAddressType=_CPimIfAddressType_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,3),_CPimIfAddressType_Type())
cPimIfAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimIfAddressType.setStatus(_A)
class _CPimIfAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimIfAddress_Type.__name__=_H
_CPimIfAddress_Object=MibTableColumn
cPimIfAddress=_CPimIfAddress_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,4),_CPimIfAddress_Type())
cPimIfAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimIfAddress.setStatus(_A)
_CPimIfNetMask_Type=InetAddressPrefixLength
_CPimIfNetMask_Object=MibTableColumn
cPimIfNetMask=_CPimIfNetMask_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,5),_CPimIfNetMask_Type())
cPimIfNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimIfNetMask.setStatus(_A)
class _CPimIfMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dense',1),('sparse',2),('sparseDense',3)))
_CPimIfMode_Type.__name__=_J
_CPimIfMode_Object=MibTableColumn
cPimIfMode=_CPimIfMode_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,6),_CPimIfMode_Type())
cPimIfMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimIfMode.setStatus(_A)
class _CPimIfDR_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimIfDR_Type.__name__=_H
_CPimIfDR_Object=MibTableColumn
cPimIfDR=_CPimIfDR_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,7),_CPimIfDR_Type())
cPimIfDR.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimIfDR.setStatus(_A)
class _CPimIfHelloInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CPimIfHelloInterval_Type.__name__=_G
_CPimIfHelloInterval_Object=MibTableColumn
cPimIfHelloInterval=_CPimIfHelloInterval_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,8),_CPimIfHelloInterval_Type())
cPimIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:cPimIfHelloInterval.setUnits(_I)
class _CPimIfJoinPruneInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CPimIfJoinPruneInterval_Type.__name__=_G
_CPimIfJoinPruneInterval_Object=MibTableColumn
cPimIfJoinPruneInterval=_CPimIfJoinPruneInterval_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,9),_CPimIfJoinPruneInterval_Type())
cPimIfJoinPruneInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimIfJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:cPimIfJoinPruneInterval.setUnits(_I)
class _CPimIfCBSRPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CPimIfCBSRPreference_Type.__name__=_J
_CPimIfCBSRPreference_Object=MibTableColumn
cPimIfCBSRPreference=_CPimIfCBSRPreference_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,10),_CPimIfCBSRPreference_Type())
cPimIfCBSRPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimIfCBSRPreference.setStatus(_A)
_CPimIfStatus_Type=RowStatus
_CPimIfStatus_Object=MibTableColumn
cPimIfStatus=_CPimIfStatus_Object((1,3,6,1,4,1,9,10,119,1,1,2,1,11),_CPimIfStatus_Type())
cPimIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimIfStatus.setStatus(_A)
_CPimNbrTable_Object=MibTable
cPimNbrTable=_CPimNbrTable_Object((1,3,6,1,4,1,9,10,119,1,1,3))
if mibBuilder.loadTexts:cPimNbrTable.setStatus(_A)
_CPimNbrEntry_Object=MibTableRow
cPimNbrEntry=_CPimNbrEntry_Object((1,3,6,1,4,1,9,10,119,1,1,3,1))
cPimNbrEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:cPimNbrEntry.setStatus(_A)
_CPimNbrIfIndex_Type=InterfaceIndex
_CPimNbrIfIndex_Object=MibTableColumn
cPimNbrIfIndex=_CPimNbrIfIndex_Object((1,3,6,1,4,1,9,10,119,1,1,3,1,1),_CPimNbrIfIndex_Type())
cPimNbrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimNbrIfIndex.setStatus(_A)
_CPimNbrAddressType_Type=InetAddressType
_CPimNbrAddressType_Object=MibTableColumn
cPimNbrAddressType=_CPimNbrAddressType_Object((1,3,6,1,4,1,9,10,119,1,1,3,1,2),_CPimNbrAddressType_Type())
cPimNbrAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimNbrAddressType.setStatus(_A)
class _CPimNbrAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimNbrAddress_Type.__name__=_H
_CPimNbrAddress_Object=MibTableColumn
cPimNbrAddress=_CPimNbrAddress_Object((1,3,6,1,4,1,9,10,119,1,1,3,1,3),_CPimNbrAddress_Type())
cPimNbrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimNbrAddress.setStatus(_A)
_CPimNbrUpTime_Type=TimeTicks
_CPimNbrUpTime_Object=MibTableColumn
cPimNbrUpTime=_CPimNbrUpTime_Object((1,3,6,1,4,1,9,10,119,1,1,3,1,4),_CPimNbrUpTime_Type())
cPimNbrUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimNbrUpTime.setStatus(_A)
_CPimNbrExpiryTime_Type=TimeTicks
_CPimNbrExpiryTime_Object=MibTableColumn
cPimNbrExpiryTime=_CPimNbrExpiryTime_Object((1,3,6,1,4,1,9,10,119,1,1,3,1,5),_CPimNbrExpiryTime_Type())
cPimNbrExpiryTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimNbrExpiryTime.setStatus(_A)
_CPimInetMRouteTable_Object=MibTable
cPimInetMRouteTable=_CPimInetMRouteTable_Object((1,3,6,1,4,1,9,10,119,1,1,4))
if mibBuilder.loadTexts:cPimInetMRouteTable.setStatus(_A)
_CPimInetMRouteEntry_Object=MibTableRow
cPimInetMRouteEntry=_CPimInetMRouteEntry_Object((1,3,6,1,4,1,9,10,119,1,1,4,1))
cPimInetMRouteEntry.setIndexNames((0,_F,_S),(0,_F,_T),(0,_F,_a),(0,_F,_b))
if mibBuilder.loadTexts:cPimInetMRouteEntry.setStatus(_A)
_CPimInetMRouteUpstreamAssertTime_Type=TimeTicks
_CPimInetMRouteUpstreamAssertTime_Object=MibTableColumn
cPimInetMRouteUpstreamAssertTime=_CPimInetMRouteUpstreamAssertTime_Object((1,3,6,1,4,1,9,10,119,1,1,4,1,1),_CPimInetMRouteUpstreamAssertTime_Type())
cPimInetMRouteUpstreamAssertTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimInetMRouteUpstreamAssertTime.setStatus(_A)
class _CPimInetMRouteAssertMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CPimInetMRouteAssertMetric_Type.__name__=_G
_CPimInetMRouteAssertMetric_Object=MibTableColumn
cPimInetMRouteAssertMetric=_CPimInetMRouteAssertMetric_Object((1,3,6,1,4,1,9,10,119,1,1,4,1,2),_CPimInetMRouteAssertMetric_Type())
cPimInetMRouteAssertMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimInetMRouteAssertMetric.setStatus(_A)
class _CPimInetMRouteAssertMetricPref_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CPimInetMRouteAssertMetricPref_Type.__name__=_G
_CPimInetMRouteAssertMetricPref_Object=MibTableColumn
cPimInetMRouteAssertMetricPref=_CPimInetMRouteAssertMetricPref_Object((1,3,6,1,4,1,9,10,119,1,1,4,1,3),_CPimInetMRouteAssertMetricPref_Type())
cPimInetMRouteAssertMetricPref.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimInetMRouteAssertMetricPref.setStatus(_A)
_CPimInetMRouteAssertRPTBit_Type=TruthValue
_CPimInetMRouteAssertRPTBit_Object=MibTableColumn
cPimInetMRouteAssertRPTBit=_CPimInetMRouteAssertRPTBit_Object((1,3,6,1,4,1,9,10,119,1,1,4,1,4),_CPimInetMRouteAssertRPTBit_Type())
cPimInetMRouteAssertRPTBit.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimInetMRouteAssertRPTBit.setStatus(_A)
class _CPimInetMRouteFlags_Type(Bits):namedValues=NamedValues(*(('rpt',0),('spt',1)))
_CPimInetMRouteFlags_Type.__name__='Bits'
_CPimInetMRouteFlags_Object=MibTableColumn
cPimInetMRouteFlags=_CPimInetMRouteFlags_Object((1,3,6,1,4,1,9,10,119,1,1,4,1,5),_CPimInetMRouteFlags_Type())
cPimInetMRouteFlags.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimInetMRouteFlags.setStatus(_A)
_CPimInetMRouteNextHopTable_Object=MibTable
cPimInetMRouteNextHopTable=_CPimInetMRouteNextHopTable_Object((1,3,6,1,4,1,9,10,119,1,1,5))
if mibBuilder.loadTexts:cPimInetMRouteNextHopTable.setStatus(_A)
_CPimInetMRouteNextHopEntry_Object=MibTableRow
cPimInetMRouteNextHopEntry=_CPimInetMRouteNextHopEntry_Object((1,3,6,1,4,1,9,10,119,1,1,5,1))
cPimInetMRouteNextHopEntry.setIndexNames((0,_F,_U),(0,_F,_W),(0,_F,_Y),(0,_F,_Z),(0,_F,_X),(0,_F,_V))
if mibBuilder.loadTexts:cPimInetMRouteNextHopEntry.setStatus(_A)
class _CPimInetMRouteNextHopPruneReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('prune',2),('assert',3)))
_CPimInetMRouteNextHopPruneReason_Type.__name__=_J
_CPimInetMRouteNextHopPruneReason_Object=MibTableColumn
cPimInetMRouteNextHopPruneReason=_CPimInetMRouteNextHopPruneReason_Object((1,3,6,1,4,1,9,10,119,1,1,5,1,2),_CPimInetMRouteNextHopPruneReason_Type())
cPimInetMRouteNextHopPruneReason.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimInetMRouteNextHopPruneReason.setStatus(_A)
_CPimRPMapTable_Object=MibTable
cPimRPMapTable=_CPimRPMapTable_Object((1,3,6,1,4,1,9,10,119,1,1,6))
if mibBuilder.loadTexts:cPimRPMapTable.setStatus(_A)
_CPimRPMapEntry_Object=MibTableRow
cPimRPMapEntry=_CPimRPMapEntry_Object((1,3,6,1,4,1,9,10,119,1,1,6,1))
cPimRPMapEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:cPimRPMapEntry.setStatus(_A)
class _CPimRPMapComponent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CPimRPMapComponent_Type.__name__=_G
_CPimRPMapComponent_Object=MibTableColumn
cPimRPMapComponent=_CPimRPMapComponent_Object((1,3,6,1,4,1,9,10,119,1,1,6,1,1),_CPimRPMapComponent_Type())
cPimRPMapComponent.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimRPMapComponent.setStatus(_A)
_CPimRPMapAddrType_Type=InetAddressType
_CPimRPMapAddrType_Object=MibTableColumn
cPimRPMapAddrType=_CPimRPMapAddrType_Object((1,3,6,1,4,1,9,10,119,1,1,6,1,2),_CPimRPMapAddrType_Type())
cPimRPMapAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimRPMapAddrType.setStatus(_A)
class _CPimRPMapGroupAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimRPMapGroupAddress_Type.__name__=_H
_CPimRPMapGroupAddress_Object=MibTableColumn
cPimRPMapGroupAddress=_CPimRPMapGroupAddress_Object((1,3,6,1,4,1,9,10,119,1,1,6,1,3),_CPimRPMapGroupAddress_Type())
cPimRPMapGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimRPMapGroupAddress.setStatus(_A)
_CPimRPMapGroupMask_Type=InetAddressPrefixLength
_CPimRPMapGroupMask_Object=MibTableColumn
cPimRPMapGroupMask=_CPimRPMapGroupMask_Object((1,3,6,1,4,1,9,10,119,1,1,6,1,4),_CPimRPMapGroupMask_Type())
cPimRPMapGroupMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimRPMapGroupMask.setStatus(_A)
class _CPimRPMapAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimRPMapAddress_Type.__name__=_H
_CPimRPMapAddress_Object=MibTableColumn
cPimRPMapAddress=_CPimRPMapAddress_Object((1,3,6,1,4,1,9,10,119,1,1,6,1,5),_CPimRPMapAddress_Type())
cPimRPMapAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimRPMapAddress.setStatus(_A)
class _CPimRPMapHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CPimRPMapHoldTime_Type.__name__=_G
_CPimRPMapHoldTime_Object=MibTableColumn
cPimRPMapHoldTime=_CPimRPMapHoldTime_Object((1,3,6,1,4,1,9,10,119,1,1,6,1,6),_CPimRPMapHoldTime_Type())
cPimRPMapHoldTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimRPMapHoldTime.setStatus(_A)
if mibBuilder.loadTexts:cPimRPMapHoldTime.setUnits(_I)
_CPimRPMapExpiryTime_Type=TimeTicks
_CPimRPMapExpiryTime_Object=MibTableColumn
cPimRPMapExpiryTime=_CPimRPMapExpiryTime_Object((1,3,6,1,4,1,9,10,119,1,1,6,1,7),_CPimRPMapExpiryTime_Type())
cPimRPMapExpiryTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cPimRPMapExpiryTime.setStatus(_A)
_CPimCRPTable_Object=MibTable
cPimCRPTable=_CPimCRPTable_Object((1,3,6,1,4,1,9,10,119,1,1,7))
if mibBuilder.loadTexts:cPimCRPTable.setStatus(_A)
_CPimCRPEntry_Object=MibTableRow
cPimCRPEntry=_CPimCRPEntry_Object((1,3,6,1,4,1,9,10,119,1,1,7,1))
cPimCRPEntry.setIndexNames((0,_B,_m),(0,_B,_n),(0,_B,_o))
if mibBuilder.loadTexts:cPimCRPEntry.setStatus(_A)
_CPimCRPAddrType_Type=InetAddressType
_CPimCRPAddrType_Object=MibTableColumn
cPimCRPAddrType=_CPimCRPAddrType_Object((1,3,6,1,4,1,9,10,119,1,1,7,1,1),_CPimCRPAddrType_Type())
cPimCRPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimCRPAddrType.setStatus(_A)
class _CPimCRPGroupAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimCRPGroupAddress_Type.__name__=_H
_CPimCRPGroupAddress_Object=MibTableColumn
cPimCRPGroupAddress=_CPimCRPGroupAddress_Object((1,3,6,1,4,1,9,10,119,1,1,7,1,2),_CPimCRPGroupAddress_Type())
cPimCRPGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimCRPGroupAddress.setStatus(_A)
_CPimCRPGroupMask_Type=InetAddressPrefixLength
_CPimCRPGroupMask_Object=MibTableColumn
cPimCRPGroupMask=_CPimCRPGroupMask_Object((1,3,6,1,4,1,9,10,119,1,1,7,1,3),_CPimCRPGroupMask_Type())
cPimCRPGroupMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimCRPGroupMask.setStatus(_A)
class _CPimCRPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimCRPAddress_Type.__name__=_H
_CPimCRPAddress_Object=MibTableColumn
cPimCRPAddress=_CPimCRPAddress_Object((1,3,6,1,4,1,9,10,119,1,1,7,1,4),_CPimCRPAddress_Type())
cPimCRPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimCRPAddress.setStatus(_A)
_CPimCRPRowStatus_Type=RowStatus
_CPimCRPRowStatus_Object=MibTableColumn
cPimCRPRowStatus=_CPimCRPRowStatus_Object((1,3,6,1,4,1,9,10,119,1,1,7,1,5),_CPimCRPRowStatus_Type())
cPimCRPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimCRPRowStatus.setStatus(_A)
_CPimComponentTable_Object=MibTable
cPimComponentTable=_CPimComponentTable_Object((1,3,6,1,4,1,9,10,119,1,1,8))
if mibBuilder.loadTexts:cPimComponentTable.setStatus(_A)
_CPimComponentEntry_Object=MibTableRow
cPimComponentEntry=_CPimComponentEntry_Object((1,3,6,1,4,1,9,10,119,1,1,8,1))
cPimComponentEntry.setIndexNames((0,_B,_p))
if mibBuilder.loadTexts:cPimComponentEntry.setStatus(_A)
class _CPimComponentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CPimComponentIndex_Type.__name__=_G
_CPimComponentIndex_Object=MibTableColumn
cPimComponentIndex=_CPimComponentIndex_Object((1,3,6,1,4,1,9,10,119,1,1,8,1,1),_CPimComponentIndex_Type())
cPimComponentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cPimComponentIndex.setStatus(_A)
_CPimComponentBSRAddrType_Type=InetAddressType
_CPimComponentBSRAddrType_Object=MibTableColumn
cPimComponentBSRAddrType=_CPimComponentBSRAddrType_Object((1,3,6,1,4,1,9,10,119,1,1,8,1,2),_CPimComponentBSRAddrType_Type())
cPimComponentBSRAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimComponentBSRAddrType.setStatus(_A)
class _CPimComponentBSRAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CPimComponentBSRAddress_Type.__name__=_H
_CPimComponentBSRAddress_Object=MibTableColumn
cPimComponentBSRAddress=_CPimComponentBSRAddress_Object((1,3,6,1,4,1,9,10,119,1,1,8,1,3),_CPimComponentBSRAddress_Type())
cPimComponentBSRAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimComponentBSRAddress.setStatus(_A)
_CPimComponentBSRExpiryTime_Type=TimeTicks
_CPimComponentBSRExpiryTime_Object=MibTableColumn
cPimComponentBSRExpiryTime=_CPimComponentBSRExpiryTime_Object((1,3,6,1,4,1,9,10,119,1,1,8,1,4),_CPimComponentBSRExpiryTime_Type())
cPimComponentBSRExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimComponentBSRExpiryTime.setStatus(_A)
class _CPimComponentCRPHoldTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CPimComponentCRPHoldTime_Type.__name__=_G
_CPimComponentCRPHoldTime_Object=MibTableColumn
cPimComponentCRPHoldTime=_CPimComponentCRPHoldTime_Object((1,3,6,1,4,1,9,10,119,1,1,8,1,5),_CPimComponentCRPHoldTime_Type())
cPimComponentCRPHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimComponentCRPHoldTime.setStatus(_A)
if mibBuilder.loadTexts:cPimComponentCRPHoldTime.setUnits(_I)
_CPimComponentStatus_Type=RowStatus
_CPimComponentStatus_Object=MibTableColumn
cPimComponentStatus=_CPimComponentStatus_Object((1,3,6,1,4,1,9,10,119,1,1,8,1,6),_CPimComponentStatus_Type())
cPimComponentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cPimComponentStatus.setStatus(_A)
_CPimMIBConformance_ObjectIdentity=ObjectIdentity
cPimMIBConformance=_CPimMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,119,2))
_CPimMIBCompliances_ObjectIdentity=ObjectIdentity
cPimMIBCompliances=_CPimMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,119,2,1))
_CPimMIBGroups_ObjectIdentity=ObjectIdentity
cPimMIBGroups=_CPimMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,119,2,2))
cPimV2MIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,119,2,2,2))
cPimV2MIBGroup.setObjects(*((_B,_q),(_B,_K),(_B,_L),(_B,_r),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_s),(_B,_t),(_B,_R),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:cPimV2MIBGroup.setStatus(_A)
cPimDenseV2MIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,119,2,2,3))
cPimDenseV2MIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cPimDenseV2MIBGroup.setStatus(_A)
cPimV2CRPMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,119,2,2,4))
cPimV2CRPMIBGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:cPimV2CRPMIBGroup.setStatus(_A)
cPimNextHopGroup=ObjectGroup((1,3,6,1,4,1,9,10,119,2,2,5))
cPimNextHopGroup.setObjects((_B,_A5))
if mibBuilder.loadTexts:cPimNextHopGroup.setStatus(_A)
cPimAssertGroup=ObjectGroup((1,3,6,1,4,1,9,10,119,2,2,6))
cPimAssertGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:cPimAssertGroup.setStatus(_A)
cPimNbrLoss=NotificationType((1,3,6,1,4,1,9,10,119,0,2))
cPimNbrLoss.setObjects((_B,_K))
if mibBuilder.loadTexts:cPimNbrLoss.setStatus(_A)
cPimNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,119,2,2,1))
cPimNotificationGroup.setObjects((_B,_A9))
if mibBuilder.loadTexts:cPimNotificationGroup.setStatus(_A)
cPimSparseV2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,119,2,1,1))
cPimSparseV2MIBCompliance.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:cPimSparseV2MIBCompliance.setStatus(_A)
cPimDenseV2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,119,2,1,2))
cPimDenseV2MIBCompliance.setObjects((_B,_AC))
if mibBuilder.loadTexts:cPimDenseV2MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIetfPimMIB':ciscoIetfPimMIB,'cPimNotifs':cPimNotifs,_A9:cPimNbrLoss,'cPimMIBObjects':cPimMIBObjects,'cPim':cPim,_q:cPimJoinPruneInterval,'cPimIfTable':cPimIfTable,'cPimIfEntry':cPimIfEntry,_c:cPimIfIndex,_d:cPimIfInetVersion,_r:cPimIfAddressType,_M:cPimIfAddress,_N:cPimIfNetMask,_R:cPimIfMode,_O:cPimIfDR,_P:cPimIfHelloInterval,_s:cPimIfJoinPruneInterval,_t:cPimIfCBSRPreference,_Q:cPimIfStatus,'cPimNbrTable':cPimNbrTable,'cPimNbrEntry':cPimNbrEntry,_e:cPimNbrIfIndex,_f:cPimNbrAddressType,_g:cPimNbrAddress,_K:cPimNbrUpTime,_L:cPimNbrExpiryTime,'cPimInetMRouteTable':cPimInetMRouteTable,'cPimInetMRouteEntry':cPimInetMRouteEntry,_A2:cPimInetMRouteUpstreamAssertTime,_A6:cPimInetMRouteAssertMetric,_A7:cPimInetMRouteAssertMetricPref,_A8:cPimInetMRouteAssertRPTBit,_A1:cPimInetMRouteFlags,'cPimInetMRouteNextHopTable':cPimInetMRouteNextHopTable,'cPimInetMRouteNextHopEntry':cPimInetMRouteNextHopEntry,_A5:cPimInetMRouteNextHopPruneReason,'cPimRPMapTable':cPimRPMapTable,'cPimRPMapEntry':cPimRPMapEntry,_h:cPimRPMapComponent,_i:cPimRPMapAddrType,_j:cPimRPMapGroupAddress,_k:cPimRPMapGroupMask,_l:cPimRPMapAddress,_u:cPimRPMapHoldTime,_v:cPimRPMapExpiryTime,'cPimCRPTable':cPimCRPTable,'cPimCRPEntry':cPimCRPEntry,_m:cPimCRPAddrType,_n:cPimCRPGroupAddress,_o:cPimCRPGroupMask,_A3:cPimCRPAddress,_A4:cPimCRPRowStatus,'cPimComponentTable':cPimComponentTable,'cPimComponentEntry':cPimComponentEntry,_p:cPimComponentIndex,_w:cPimComponentBSRAddrType,_x:cPimComponentBSRAddress,_y:cPimComponentBSRExpiryTime,_z:cPimComponentCRPHoldTime,_A0:cPimComponentStatus,'cPimMIBConformance':cPimMIBConformance,'cPimMIBCompliances':cPimMIBCompliances,'cPimSparseV2MIBCompliance':cPimSparseV2MIBCompliance,'cPimDenseV2MIBCompliance':cPimDenseV2MIBCompliance,'cPimMIBGroups':cPimMIBGroups,'cPimNotificationGroup':cPimNotificationGroup,_AA:cPimV2MIBGroup,_AC:cPimDenseV2MIBGroup,_AB:cPimV2CRPMIBGroup,'cPimNextHopGroup':cPimNextHopGroup,'cPimAssertGroup':cPimAssertGroup})