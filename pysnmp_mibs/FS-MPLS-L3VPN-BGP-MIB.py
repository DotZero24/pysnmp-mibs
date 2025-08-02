_i='fsmplsL3VpnVrfBgpGroup'
_h='fsmplsL3VpnVrfBgpPAtrUnknown'
_g='fsmplsL3VpnVrfBgpPAtrBest'
_f='fsmplsL3VpnVrfBgpPAtrCalcLocalPref'
_e='fsmplsL3VpnVrfBgpPAtrAggregatorAddr'
_d='fsmplsL3VpnVrfBgpPAtrAggrAddrType'
_c='fsmplsL3VpnVrfBgpPAtrAggregatorAS'
_b='fsmplsL3VpnVrfBgpPAtrAtomicAggregate'
_a='fsmplsL3VpnVrfBgpPAtrLocalPref'
_Z='fsmplsL3VpnVrfBgpPAtrMultiExitDisc'
_Y='fsmplsL3VpnVrfBgpPAtrNextHop'
_X='fsmplsL3VpnVrfBgpPAtrNextHopType'
_W='fsmplsL3VpnVrfBgpPAtrASPathSegment'
_V='fsmplsL3VpnVrfBgpPAtrOrigin'
_U='fsmplsL3VpnVrfBgpPAtrIpAddrPfxType'
_T='fsmplsL3VpnVrfBgpPAtrPeerType'
_S='fsmplsL3VpnVrfBgpNbrRemoteAS'
_R='fsmplsL3VpnVrfBgpNbrStorageType'
_Q='fsmplsL3VpnVrfBgpNbrRowStatus'
_P='fsmplsL3VpnVrfBgpNbrType'
_O='fsmplsL3VpnVrfBgpNbrRole'
_N='read-write'
_M='StorageType'
_L='bgp4PathAttrPeer'
_K='bgp4PathAttrIpAddrPrefixLen'
_J='bgp4PathAttrIpAddrPrefix'
_I='fsmplsL3VpnVrfBgpNbrAddr'
_H='mplsL3VpnVrfName'
_G='MPLS-L3VPN-STD-MIB'
_F='OctetString'
_E='BGP4-MIB'
_D='Integer32'
_C='read-only'
_B='FS-MPLS-L3VPN-BGP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgp4PathAttrIpAddrPrefix,bgp4PathAttrIpAddrPrefixLen,bgp4PathAttrPeer=mibBuilder.importSymbols(_E,_J,_K,_L)
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
mplsL3VpnVrfName,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_M,'TextualConvention')
fsmplsL3VpnNbrMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,100))
if mibBuilder.loadTexts:fsmplsL3VpnNbrMIB.setRevisions(('2011-09-16 00:00',))
_FsmplsL3VpnVrfBgpNbrTable_Object=MibTable
fsmplsL3VpnVrfBgpNbrTable=_FsmplsL3VpnVrfBgpNbrTable_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1))
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrTable.setStatus(_A)
_FsmplsL3VpnVrfBgpNbrEntry_Object=MibTableRow
fsmplsL3VpnVrfBgpNbrEntry=_FsmplsL3VpnVrfBgpNbrEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1,1))
fsmplsL3VpnVrfBgpNbrEntry.setIndexNames((0,_G,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrEntry.setStatus(_A)
class _FsmplsL3VpnVrfBgpNbrRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ce',1),('pe',2)))
_FsmplsL3VpnVrfBgpNbrRole_Type.__name__=_D
_FsmplsL3VpnVrfBgpNbrRole_Object=MibTableColumn
fsmplsL3VpnVrfBgpNbrRole=_FsmplsL3VpnVrfBgpNbrRole_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1,1,1),_FsmplsL3VpnVrfBgpNbrRole_Type())
fsmplsL3VpnVrfBgpNbrRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrRole.setStatus(_A)
_FsmplsL3VpnVrfBgpNbrType_Type=InetAddressType
_FsmplsL3VpnVrfBgpNbrType_Object=MibTableColumn
fsmplsL3VpnVrfBgpNbrType=_FsmplsL3VpnVrfBgpNbrType_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1,1,2),_FsmplsL3VpnVrfBgpNbrType_Type())
fsmplsL3VpnVrfBgpNbrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrType.setStatus(_A)
_FsmplsL3VpnVrfBgpNbrAddr_Type=InetAddress
_FsmplsL3VpnVrfBgpNbrAddr_Object=MibTableColumn
fsmplsL3VpnVrfBgpNbrAddr=_FsmplsL3VpnVrfBgpNbrAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1,1,3),_FsmplsL3VpnVrfBgpNbrAddr_Type())
fsmplsL3VpnVrfBgpNbrAddr.setMaxAccess(_N)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrAddr.setStatus(_A)
_FsmplsL3VpnVrfBgpNbrRowStatus_Type=RowStatus
_FsmplsL3VpnVrfBgpNbrRowStatus_Object=MibTableColumn
fsmplsL3VpnVrfBgpNbrRowStatus=_FsmplsL3VpnVrfBgpNbrRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1,1,4),_FsmplsL3VpnVrfBgpNbrRowStatus_Type())
fsmplsL3VpnVrfBgpNbrRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrRowStatus.setStatus(_A)
class _FsmplsL3VpnVrfBgpNbrStorageType_Type(StorageType):defaultValue=2
_FsmplsL3VpnVrfBgpNbrStorageType_Type.__name__=_M
_FsmplsL3VpnVrfBgpNbrStorageType_Object=MibTableColumn
fsmplsL3VpnVrfBgpNbrStorageType=_FsmplsL3VpnVrfBgpNbrStorageType_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1,1,5),_FsmplsL3VpnVrfBgpNbrStorageType_Type())
fsmplsL3VpnVrfBgpNbrStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrStorageType.setStatus(_A)
class _FsmplsL3VpnVrfBgpNbrRemoteAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsmplsL3VpnVrfBgpNbrRemoteAS_Type.__name__=_D
_FsmplsL3VpnVrfBgpNbrRemoteAS_Object=MibTableColumn
fsmplsL3VpnVrfBgpNbrRemoteAS=_FsmplsL3VpnVrfBgpNbrRemoteAS_Object((1,3,6,1,4,1,52642,1,1,10,2,100,1,1,6),_FsmplsL3VpnVrfBgpNbrRemoteAS_Type())
fsmplsL3VpnVrfBgpNbrRemoteAS.setMaxAccess(_N)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpNbrRemoteAS.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrTable_Object=MibTable
fsmplsL3VpnVrfBgpPAtrTable=_FsmplsL3VpnVrfBgpPAtrTable_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2))
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrTable.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrEntry_Object=MibTableRow
fsmplsL3VpnVrfBgpPAtrEntry=_FsmplsL3VpnVrfBgpPAtrEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1))
fsmplsL3VpnVrfBgpPAtrEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrEntry.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrPeerType_Type=InetAddressType
_FsmplsL3VpnVrfBgpPAtrPeerType_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrPeerType=_FsmplsL3VpnVrfBgpPAtrPeerType_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,1),_FsmplsL3VpnVrfBgpPAtrPeerType_Type())
fsmplsL3VpnVrfBgpPAtrPeerType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrPeerType.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type=InetAddressType
_FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrIpAddrPfxType=_FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,2),_FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type())
fsmplsL3VpnVrfBgpPAtrIpAddrPfxType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrIpAddrPfxType.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_FsmplsL3VpnVrfBgpPAtrOrigin_Type.__name__=_D
_FsmplsL3VpnVrfBgpPAtrOrigin_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrOrigin=_FsmplsL3VpnVrfBgpPAtrOrigin_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,3),_FsmplsL3VpnVrfBgpPAtrOrigin_Type())
fsmplsL3VpnVrfBgpPAtrOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrOrigin.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrNextHop_Type=InetAddress
_FsmplsL3VpnVrfBgpPAtrNextHop_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrNextHop=_FsmplsL3VpnVrfBgpPAtrNextHop_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,4),_FsmplsL3VpnVrfBgpPAtrNextHop_Type())
fsmplsL3VpnVrfBgpPAtrNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrNextHop.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_FsmplsL3VpnVrfBgpPAtrASPathSegment_Type.__name__=_F
_FsmplsL3VpnVrfBgpPAtrASPathSegment_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrASPathSegment=_FsmplsL3VpnVrfBgpPAtrASPathSegment_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,5),_FsmplsL3VpnVrfBgpPAtrASPathSegment_Type())
fsmplsL3VpnVrfBgpPAtrASPathSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrASPathSegment.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrNextHopType_Type=InetAddressType
_FsmplsL3VpnVrfBgpPAtrNextHopType_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrNextHopType=_FsmplsL3VpnVrfBgpPAtrNextHopType_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,6),_FsmplsL3VpnVrfBgpPAtrNextHopType_Type())
fsmplsL3VpnVrfBgpPAtrNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrNextHopType.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Type.__name__=_D
_FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrMultiExitDisc=_FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,7),_FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Type())
fsmplsL3VpnVrfBgpPAtrMultiExitDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrMultiExitDisc.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_FsmplsL3VpnVrfBgpPAtrLocalPref_Type.__name__=_D
_FsmplsL3VpnVrfBgpPAtrLocalPref_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrLocalPref=_FsmplsL3VpnVrfBgpPAtrLocalPref_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,8),_FsmplsL3VpnVrfBgpPAtrLocalPref_Type())
fsmplsL3VpnVrfBgpPAtrLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrLocalPref.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRrouteNotSelected',1),('lessSpecificRouteSelected',2)))
_FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Type.__name__=_D
_FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrAtomicAggregate=_FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,9),_FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Type())
fsmplsL3VpnVrfBgpPAtrAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrAtomicAggregate.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsmplsL3VpnVrfBgpPAtrAggregatorAS_Type.__name__=_D
_FsmplsL3VpnVrfBgpPAtrAggregatorAS_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrAggregatorAS=_FsmplsL3VpnVrfBgpPAtrAggregatorAS_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,10),_FsmplsL3VpnVrfBgpPAtrAggregatorAS_Type())
fsmplsL3VpnVrfBgpPAtrAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrAggregatorAS.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrAggrAddrType_Type=InetAddressType
_FsmplsL3VpnVrfBgpPAtrAggrAddrType_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrAggrAddrType=_FsmplsL3VpnVrfBgpPAtrAggrAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,11),_FsmplsL3VpnVrfBgpPAtrAggrAddrType_Type())
fsmplsL3VpnVrfBgpPAtrAggrAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrAggrAddrType.setStatus(_A)
_FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Type=InetAddress
_FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrAggregatorAddr=_FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,12),_FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Type())
fsmplsL3VpnVrfBgpPAtrAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrAggregatorAddr.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Type.__name__=_D
_FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrCalcLocalPref=_FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,13),_FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Type())
fsmplsL3VpnVrfBgpPAtrCalcLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrCalcLocalPref.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_FsmplsL3VpnVrfBgpPAtrBest_Type.__name__=_D
_FsmplsL3VpnVrfBgpPAtrBest_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrBest=_FsmplsL3VpnVrfBgpPAtrBest_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,14),_FsmplsL3VpnVrfBgpPAtrBest_Type())
fsmplsL3VpnVrfBgpPAtrBest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrBest.setStatus(_A)
class _FsmplsL3VpnVrfBgpPAtrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsmplsL3VpnVrfBgpPAtrUnknown_Type.__name__=_F
_FsmplsL3VpnVrfBgpPAtrUnknown_Object=MibTableColumn
fsmplsL3VpnVrfBgpPAtrUnknown=_FsmplsL3VpnVrfBgpPAtrUnknown_Object((1,3,6,1,4,1,52642,1,1,10,2,100,2,1,15),_FsmplsL3VpnVrfBgpPAtrUnknown_Type())
fsmplsL3VpnVrfBgpPAtrUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpPAtrUnknown.setStatus(_A)
_FsmplsL3VpnVrfBgpNbrCom_ObjectIdentity=ObjectIdentity
fsmplsL3VpnVrfBgpNbrCom=_FsmplsL3VpnVrfBgpNbrCom_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,100,3))
_FsmplsL3VpnVrfBgpCompliances_ObjectIdentity=ObjectIdentity
fsmplsL3VpnVrfBgpCompliances=_FsmplsL3VpnVrfBgpCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,100,3,1))
_FsmplsL3VpnVrfBgpGroups_ObjectIdentity=ObjectIdentity
fsmplsL3VpnVrfBgpGroups=_FsmplsL3VpnVrfBgpGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,100,3,2))
fsmplsL3VpnVrfBgpGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,100,3,2,1))
fsmplsL3VpnVrfBgpGroup.setObjects(*((_B,_O),(_B,_P),(_B,_I),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpGroup.setStatus(_A)
fsmplsL3VpnVrfBgpCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,100,3,1,1))
fsmplsL3VpnVrfBgpCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:fsmplsL3VpnVrfBgpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsmplsL3VpnNbrMIB':fsmplsL3VpnNbrMIB,'fsmplsL3VpnVrfBgpNbrTable':fsmplsL3VpnVrfBgpNbrTable,'fsmplsL3VpnVrfBgpNbrEntry':fsmplsL3VpnVrfBgpNbrEntry,_O:fsmplsL3VpnVrfBgpNbrRole,_P:fsmplsL3VpnVrfBgpNbrType,_I:fsmplsL3VpnVrfBgpNbrAddr,_Q:fsmplsL3VpnVrfBgpNbrRowStatus,_R:fsmplsL3VpnVrfBgpNbrStorageType,_S:fsmplsL3VpnVrfBgpNbrRemoteAS,'fsmplsL3VpnVrfBgpPAtrTable':fsmplsL3VpnVrfBgpPAtrTable,'fsmplsL3VpnVrfBgpPAtrEntry':fsmplsL3VpnVrfBgpPAtrEntry,_T:fsmplsL3VpnVrfBgpPAtrPeerType,_U:fsmplsL3VpnVrfBgpPAtrIpAddrPfxType,_V:fsmplsL3VpnVrfBgpPAtrOrigin,_Y:fsmplsL3VpnVrfBgpPAtrNextHop,_W:fsmplsL3VpnVrfBgpPAtrASPathSegment,_X:fsmplsL3VpnVrfBgpPAtrNextHopType,_Z:fsmplsL3VpnVrfBgpPAtrMultiExitDisc,_a:fsmplsL3VpnVrfBgpPAtrLocalPref,_b:fsmplsL3VpnVrfBgpPAtrAtomicAggregate,_c:fsmplsL3VpnVrfBgpPAtrAggregatorAS,_d:fsmplsL3VpnVrfBgpPAtrAggrAddrType,_e:fsmplsL3VpnVrfBgpPAtrAggregatorAddr,_f:fsmplsL3VpnVrfBgpPAtrCalcLocalPref,_g:fsmplsL3VpnVrfBgpPAtrBest,_h:fsmplsL3VpnVrfBgpPAtrUnknown,'fsmplsL3VpnVrfBgpNbrCom':fsmplsL3VpnVrfBgpNbrCom,'fsmplsL3VpnVrfBgpCompliances':fsmplsL3VpnVrfBgpCompliances,'fsmplsL3VpnVrfBgpCompliance':fsmplsL3VpnVrfBgpCompliance,'fsmplsL3VpnVrfBgpGroups':fsmplsL3VpnVrfBgpGroups,_i:fsmplsL3VpnVrfBgpGroup})