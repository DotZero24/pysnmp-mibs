_i='qtechmplsL3VpnVrfBgpGroup'
_h='qtechmplsL3VpnVrfBgpPAtrUnknown'
_g='qtechmplsL3VpnVrfBgpPAtrBest'
_f='qtechmplsL3VpnVrfBgpPAtrCalcLocalPref'
_e='qtechmplsL3VpnVrfBgpPAtrAggregatorAddr'
_d='qtechmplsL3VpnVrfBgpPAtrAggrAddrType'
_c='qtechmplsL3VpnVrfBgpPAtrAggregatorAS'
_b='qtechmplsL3VpnVrfBgpPAtrAtomicAggregate'
_a='qtechmplsL3VpnVrfBgpPAtrLocalPref'
_Z='qtechmplsL3VpnVrfBgpPAtrMultiExitDisc'
_Y='qtechmplsL3VpnVrfBgpPAtrNextHop'
_X='qtechmplsL3VpnVrfBgpPAtrNextHopType'
_W='qtechmplsL3VpnVrfBgpPAtrASPathSegment'
_V='qtechmplsL3VpnVrfBgpPAtrOrigin'
_U='qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType'
_T='qtechmplsL3VpnVrfBgpPAtrPeerType'
_S='qtechmplsL3VpnVrfBgpNbrRemoteAS'
_R='qtechmplsL3VpnVrfBgpNbrStorageType'
_Q='qtechmplsL3VpnVrfBgpNbrRowStatus'
_P='qtechmplsL3VpnVrfBgpNbrType'
_O='qtechmplsL3VpnVrfBgpNbrRole'
_N='read-write'
_M='StorageType'
_L='bgp4PathAttrPeer'
_K='bgp4PathAttrIpAddrPrefixLen'
_J='bgp4PathAttrIpAddrPrefix'
_I='qtechmplsL3VpnVrfBgpNbrAddr'
_H='mplsL3VpnVrfName'
_G='MPLS-L3VPN-STD-MIB'
_F='OctetString'
_E='BGP4-MIB'
_D='Integer32'
_C='read-only'
_B='QTECH-MPLS-L3VPN-BGP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgp4PathAttrIpAddrPrefix,bgp4PathAttrIpAddrPrefixLen,bgp4PathAttrPeer=mibBuilder.importSymbols(_E,_J,_K,_L)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
mplsL3VpnVrfName,=mibBuilder.importSymbols(_G,_H)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_M,'TextualConvention')
qtechmplsL3VpnNbrMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,100))
if mibBuilder.loadTexts:qtechmplsL3VpnNbrMIB.setRevisions(('2011-09-16 00:00',))
_QtechmplsL3VpnVrfBgpNbrTable_Object=MibTable
qtechmplsL3VpnVrfBgpNbrTable=_QtechmplsL3VpnVrfBgpNbrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1))
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrTable.setStatus(_A)
_QtechmplsL3VpnVrfBgpNbrEntry_Object=MibTableRow
qtechmplsL3VpnVrfBgpNbrEntry=_QtechmplsL3VpnVrfBgpNbrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1,1))
qtechmplsL3VpnVrfBgpNbrEntry.setIndexNames((0,_G,_H),(0,_B,_I))
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrEntry.setStatus(_A)
class _QtechmplsL3VpnVrfBgpNbrRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ce',1),('pe',2)))
_QtechmplsL3VpnVrfBgpNbrRole_Type.__name__=_D
_QtechmplsL3VpnVrfBgpNbrRole_Object=MibTableColumn
qtechmplsL3VpnVrfBgpNbrRole=_QtechmplsL3VpnVrfBgpNbrRole_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1,1,1),_QtechmplsL3VpnVrfBgpNbrRole_Type())
qtechmplsL3VpnVrfBgpNbrRole.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrRole.setStatus(_A)
_QtechmplsL3VpnVrfBgpNbrType_Type=InetAddressType
_QtechmplsL3VpnVrfBgpNbrType_Object=MibTableColumn
qtechmplsL3VpnVrfBgpNbrType=_QtechmplsL3VpnVrfBgpNbrType_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1,1,2),_QtechmplsL3VpnVrfBgpNbrType_Type())
qtechmplsL3VpnVrfBgpNbrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrType.setStatus(_A)
_QtechmplsL3VpnVrfBgpNbrAddr_Type=InetAddress
_QtechmplsL3VpnVrfBgpNbrAddr_Object=MibTableColumn
qtechmplsL3VpnVrfBgpNbrAddr=_QtechmplsL3VpnVrfBgpNbrAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1,1,3),_QtechmplsL3VpnVrfBgpNbrAddr_Type())
qtechmplsL3VpnVrfBgpNbrAddr.setMaxAccess(_N)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrAddr.setStatus(_A)
_QtechmplsL3VpnVrfBgpNbrRowStatus_Type=RowStatus
_QtechmplsL3VpnVrfBgpNbrRowStatus_Object=MibTableColumn
qtechmplsL3VpnVrfBgpNbrRowStatus=_QtechmplsL3VpnVrfBgpNbrRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1,1,4),_QtechmplsL3VpnVrfBgpNbrRowStatus_Type())
qtechmplsL3VpnVrfBgpNbrRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrRowStatus.setStatus(_A)
class _QtechmplsL3VpnVrfBgpNbrStorageType_Type(StorageType):defaultValue=2
_QtechmplsL3VpnVrfBgpNbrStorageType_Type.__name__=_M
_QtechmplsL3VpnVrfBgpNbrStorageType_Object=MibTableColumn
qtechmplsL3VpnVrfBgpNbrStorageType=_QtechmplsL3VpnVrfBgpNbrStorageType_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1,1,5),_QtechmplsL3VpnVrfBgpNbrStorageType_Type())
qtechmplsL3VpnVrfBgpNbrStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrStorageType.setStatus(_A)
class _QtechmplsL3VpnVrfBgpNbrRemoteAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechmplsL3VpnVrfBgpNbrRemoteAS_Type.__name__=_D
_QtechmplsL3VpnVrfBgpNbrRemoteAS_Object=MibTableColumn
qtechmplsL3VpnVrfBgpNbrRemoteAS=_QtechmplsL3VpnVrfBgpNbrRemoteAS_Object((1,3,6,1,4,1,27514,1,1,10,2,100,1,1,6),_QtechmplsL3VpnVrfBgpNbrRemoteAS_Type())
qtechmplsL3VpnVrfBgpNbrRemoteAS.setMaxAccess(_N)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpNbrRemoteAS.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrTable_Object=MibTable
qtechmplsL3VpnVrfBgpPAtrTable=_QtechmplsL3VpnVrfBgpPAtrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2))
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrTable.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrEntry_Object=MibTableRow
qtechmplsL3VpnVrfBgpPAtrEntry=_QtechmplsL3VpnVrfBgpPAtrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1))
qtechmplsL3VpnVrfBgpPAtrEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrEntry.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrPeerType_Type=InetAddressType
_QtechmplsL3VpnVrfBgpPAtrPeerType_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrPeerType=_QtechmplsL3VpnVrfBgpPAtrPeerType_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,1),_QtechmplsL3VpnVrfBgpPAtrPeerType_Type())
qtechmplsL3VpnVrfBgpPAtrPeerType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrPeerType.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type=InetAddressType
_QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType=_QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,2),_QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type())
qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_QtechmplsL3VpnVrfBgpPAtrOrigin_Type.__name__=_D
_QtechmplsL3VpnVrfBgpPAtrOrigin_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrOrigin=_QtechmplsL3VpnVrfBgpPAtrOrigin_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,3),_QtechmplsL3VpnVrfBgpPAtrOrigin_Type())
qtechmplsL3VpnVrfBgpPAtrOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrOrigin.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrNextHop_Type=InetAddress
_QtechmplsL3VpnVrfBgpPAtrNextHop_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrNextHop=_QtechmplsL3VpnVrfBgpPAtrNextHop_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,4),_QtechmplsL3VpnVrfBgpPAtrNextHop_Type())
qtechmplsL3VpnVrfBgpPAtrNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrNextHop.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_QtechmplsL3VpnVrfBgpPAtrASPathSegment_Type.__name__=_F
_QtechmplsL3VpnVrfBgpPAtrASPathSegment_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrASPathSegment=_QtechmplsL3VpnVrfBgpPAtrASPathSegment_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,5),_QtechmplsL3VpnVrfBgpPAtrASPathSegment_Type())
qtechmplsL3VpnVrfBgpPAtrASPathSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrASPathSegment.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrNextHopType_Type=InetAddressType
_QtechmplsL3VpnVrfBgpPAtrNextHopType_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrNextHopType=_QtechmplsL3VpnVrfBgpPAtrNextHopType_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,6),_QtechmplsL3VpnVrfBgpPAtrNextHopType_Type())
qtechmplsL3VpnVrfBgpPAtrNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrNextHopType.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Type.__name__=_D
_QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrMultiExitDisc=_QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,7),_QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Type())
qtechmplsL3VpnVrfBgpPAtrMultiExitDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrMultiExitDisc.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_QtechmplsL3VpnVrfBgpPAtrLocalPref_Type.__name__=_D
_QtechmplsL3VpnVrfBgpPAtrLocalPref_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrLocalPref=_QtechmplsL3VpnVrfBgpPAtrLocalPref_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,8),_QtechmplsL3VpnVrfBgpPAtrLocalPref_Type())
qtechmplsL3VpnVrfBgpPAtrLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrLocalPref.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRrouteNotSelected',1),('lessSpecificRouteSelected',2)))
_QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Type.__name__=_D
_QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAtomicAggregate=_QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,9),_QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Type())
qtechmplsL3VpnVrfBgpPAtrAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrAtomicAggregate.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Type.__name__=_D
_QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAggregatorAS=_QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,10),_QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Type())
qtechmplsL3VpnVrfBgpPAtrAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrAggregatorAS.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Type=InetAddressType
_QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAggrAddrType=_QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,11),_QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Type())
qtechmplsL3VpnVrfBgpPAtrAggrAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrAggrAddrType.setStatus(_A)
_QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Type=InetAddress
_QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAggregatorAddr=_QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,12),_QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Type())
qtechmplsL3VpnVrfBgpPAtrAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrAggregatorAddr.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Type.__name__=_D
_QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrCalcLocalPref=_QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,13),_QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Type())
qtechmplsL3VpnVrfBgpPAtrCalcLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrCalcLocalPref.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_QtechmplsL3VpnVrfBgpPAtrBest_Type.__name__=_D
_QtechmplsL3VpnVrfBgpPAtrBest_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrBest=_QtechmplsL3VpnVrfBgpPAtrBest_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,14),_QtechmplsL3VpnVrfBgpPAtrBest_Type())
qtechmplsL3VpnVrfBgpPAtrBest.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrBest.setStatus(_A)
class _QtechmplsL3VpnVrfBgpPAtrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechmplsL3VpnVrfBgpPAtrUnknown_Type.__name__=_F
_QtechmplsL3VpnVrfBgpPAtrUnknown_Object=MibTableColumn
qtechmplsL3VpnVrfBgpPAtrUnknown=_QtechmplsL3VpnVrfBgpPAtrUnknown_Object((1,3,6,1,4,1,27514,1,1,10,2,100,2,1,15),_QtechmplsL3VpnVrfBgpPAtrUnknown_Type())
qtechmplsL3VpnVrfBgpPAtrUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpPAtrUnknown.setStatus(_A)
_QtechmplsL3VpnVrfBgpNbrCom_ObjectIdentity=ObjectIdentity
qtechmplsL3VpnVrfBgpNbrCom=_QtechmplsL3VpnVrfBgpNbrCom_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,100,3))
_QtechmplsL3VpnVrfBgpCompliances_ObjectIdentity=ObjectIdentity
qtechmplsL3VpnVrfBgpCompliances=_QtechmplsL3VpnVrfBgpCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,100,3,1))
_QtechmplsL3VpnVrfBgpGroups_ObjectIdentity=ObjectIdentity
qtechmplsL3VpnVrfBgpGroups=_QtechmplsL3VpnVrfBgpGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,100,3,2))
qtechmplsL3VpnVrfBgpGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,100,3,2,1))
qtechmplsL3VpnVrfBgpGroup.setObjects(*((_B,_O),(_B,_P),(_B,_I),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpGroup.setStatus(_A)
qtechmplsL3VpnVrfBgpCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,100,3,1,1))
qtechmplsL3VpnVrfBgpCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:qtechmplsL3VpnVrfBgpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechmplsL3VpnNbrMIB':qtechmplsL3VpnNbrMIB,'qtechmplsL3VpnVrfBgpNbrTable':qtechmplsL3VpnVrfBgpNbrTable,'qtechmplsL3VpnVrfBgpNbrEntry':qtechmplsL3VpnVrfBgpNbrEntry,_O:qtechmplsL3VpnVrfBgpNbrRole,_P:qtechmplsL3VpnVrfBgpNbrType,_I:qtechmplsL3VpnVrfBgpNbrAddr,_Q:qtechmplsL3VpnVrfBgpNbrRowStatus,_R:qtechmplsL3VpnVrfBgpNbrStorageType,_S:qtechmplsL3VpnVrfBgpNbrRemoteAS,'qtechmplsL3VpnVrfBgpPAtrTable':qtechmplsL3VpnVrfBgpPAtrTable,'qtechmplsL3VpnVrfBgpPAtrEntry':qtechmplsL3VpnVrfBgpPAtrEntry,_T:qtechmplsL3VpnVrfBgpPAtrPeerType,_U:qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType,_V:qtechmplsL3VpnVrfBgpPAtrOrigin,_Y:qtechmplsL3VpnVrfBgpPAtrNextHop,_W:qtechmplsL3VpnVrfBgpPAtrASPathSegment,_X:qtechmplsL3VpnVrfBgpPAtrNextHopType,_Z:qtechmplsL3VpnVrfBgpPAtrMultiExitDisc,_a:qtechmplsL3VpnVrfBgpPAtrLocalPref,_b:qtechmplsL3VpnVrfBgpPAtrAtomicAggregate,_c:qtechmplsL3VpnVrfBgpPAtrAggregatorAS,_d:qtechmplsL3VpnVrfBgpPAtrAggrAddrType,_e:qtechmplsL3VpnVrfBgpPAtrAggregatorAddr,_f:qtechmplsL3VpnVrfBgpPAtrCalcLocalPref,_g:qtechmplsL3VpnVrfBgpPAtrBest,_h:qtechmplsL3VpnVrfBgpPAtrUnknown,'qtechmplsL3VpnVrfBgpNbrCom':qtechmplsL3VpnVrfBgpNbrCom,'qtechmplsL3VpnVrfBgpCompliances':qtechmplsL3VpnVrfBgpCompliances,'qtechmplsL3VpnVrfBgpCompliance':qtechmplsL3VpnVrfBgpCompliance,'qtechmplsL3VpnVrfBgpGroups':qtechmplsL3VpnVrfBgpGroups,_i:qtechmplsL3VpnVrfBgpGroup})