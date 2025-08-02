_L='h3cMplsVpnVrfBgpPAtrIpAddrPrefix'
_K='h3cMplsVpnVrfBgpPAtrIpAddrPrefixLen'
_J='h3cMplsVpnVrfBgpPAtrPeer'
_I='h3cMplsVpnVrfBgpNbrAddr'
_H='OctetString'
_G='h3cMplsVpnVrfName'
_F='not-accessible'
_E='H3C-MPLS-VPN-BGP-MIB'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cMplsVpnBgp=ModuleIdentity((1,3,6,1,4,1,2011,10,2,160))
if mibBuilder.loadTexts:h3cMplsVpnBgp.setRevisions(('2016-10-26 20:00','2015-11-14 20:00','2014-12-03 20:00'))
class H3cMplsVpnId(TextualConvention,OctetString):status=_A;displayHint='31a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class H3cMplsVpnRtDistinguisher(TextualConvention,OctetString):status=_A;displayHint='256a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cMplsVpnObjects_ObjectIdentity=ObjectIdentity
h3cMplsVpnObjects=_H3cMplsVpnObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,160,1))
_H3cMplsVpnConf_ObjectIdentity=ObjectIdentity
h3cMplsVpnConf=_H3cMplsVpnConf_ObjectIdentity((1,3,6,1,4,1,2011,10,2,160,1,1))
_H3cMplsVpnVrfConfTable_Object=MibTable
h3cMplsVpnVrfConfTable=_H3cMplsVpnVrfConfTable_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1))
if mibBuilder.loadTexts:h3cMplsVpnVrfConfTable.setStatus(_A)
_H3cMplsVpnVrfConfEntry_Object=MibTableRow
h3cMplsVpnVrfConfEntry=_H3cMplsVpnVrfConfEntry_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1))
h3cMplsVpnVrfConfEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:h3cMplsVpnVrfConfEntry.setStatus(_A)
_H3cMplsVpnVrfName_Type=H3cMplsVpnId
_H3cMplsVpnVrfName_Object=MibTableColumn
h3cMplsVpnVrfName=_H3cMplsVpnVrfName_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,1),_H3cMplsVpnVrfName_Type())
h3cMplsVpnVrfName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMplsVpnVrfName.setStatus(_A)
_H3cMplsVpnVrfRtDistinguisher_Type=H3cMplsVpnRtDistinguisher
_H3cMplsVpnVrfRtDistinguisher_Object=MibTableColumn
h3cMplsVpnVrfRtDistinguisher=_H3cMplsVpnVrfRtDistinguisher_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,2),_H3cMplsVpnVrfRtDistinguisher_Type())
h3cMplsVpnVrfRtDistinguisher.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfRtDistinguisher.setStatus(_A)
class _H3cMplsVpnVrfNetPrefixType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('rip',2),('ospf',3),('isis',4),('bgp',5),('static',6)))
_H3cMplsVpnVrfNetPrefixType_Type.__name__=_C
_H3cMplsVpnVrfNetPrefixType_Object=MibTableColumn
h3cMplsVpnVrfNetPrefixType=_H3cMplsVpnVrfNetPrefixType_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,3),_H3cMplsVpnVrfNetPrefixType_Type())
h3cMplsVpnVrfNetPrefixType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfNetPrefixType.setStatus(_A)
_H3cMplsVpnVrfNetPrefix_Type=IpAddress
_H3cMplsVpnVrfNetPrefix_Object=MibTableColumn
h3cMplsVpnVrfNetPrefix=_H3cMplsVpnVrfNetPrefix_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,4),_H3cMplsVpnVrfNetPrefix_Type())
h3cMplsVpnVrfNetPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfNetPrefix.setStatus(_A)
_H3cMplsVpnVrfIpRtRedistributeConn_Type=TruthValue
_H3cMplsVpnVrfIpRtRedistributeConn_Object=MibTableColumn
h3cMplsVpnVrfIpRtRedistributeConn=_H3cMplsVpnVrfIpRtRedistributeConn_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,5),_H3cMplsVpnVrfIpRtRedistributeConn_Type())
h3cMplsVpnVrfIpRtRedistributeConn.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfIpRtRedistributeConn.setStatus(_A)
_H3cMplsVpnVrfIpRtRedistributeStatic_Type=TruthValue
_H3cMplsVpnVrfIpRtRedistributeStatic_Object=MibTableColumn
h3cMplsVpnVrfIpRtRedistributeStatic=_H3cMplsVpnVrfIpRtRedistributeStatic_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,6),_H3cMplsVpnVrfIpRtRedistributeStatic_Type())
h3cMplsVpnVrfIpRtRedistributeStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfIpRtRedistributeStatic.setStatus(_A)
_H3cMplsVpnVrfIpRtRedistributeRip_Type=TruthValue
_H3cMplsVpnVrfIpRtRedistributeRip_Object=MibTableColumn
h3cMplsVpnVrfIpRtRedistributeRip=_H3cMplsVpnVrfIpRtRedistributeRip_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,7),_H3cMplsVpnVrfIpRtRedistributeRip_Type())
h3cMplsVpnVrfIpRtRedistributeRip.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfIpRtRedistributeRip.setStatus(_A)
_H3cMplsVpnVrfConfHighRtThreshold_Type=Unsigned32
_H3cMplsVpnVrfConfHighRtThreshold_Object=MibTableColumn
h3cMplsVpnVrfConfHighRtThreshold=_H3cMplsVpnVrfConfHighRtThreshold_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,8),_H3cMplsVpnVrfConfHighRtThreshold_Type())
h3cMplsVpnVrfConfHighRtThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfConfHighRtThreshold.setStatus(_A)
_H3cMplsVpnVrfConfIsWarnOnly_Type=TruthValue
_H3cMplsVpnVrfConfIsWarnOnly_Object=MibTableColumn
h3cMplsVpnVrfConfIsWarnOnly=_H3cMplsVpnVrfConfIsWarnOnly_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,9),_H3cMplsVpnVrfConfIsWarnOnly_Type())
h3cMplsVpnVrfConfIsWarnOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfConfIsWarnOnly.setStatus(_A)
_H3cMplsVpnVrfConfMaxRts_Type=Unsigned32
_H3cMplsVpnVrfConfMaxRts_Object=MibTableColumn
h3cMplsVpnVrfConfMaxRts=_H3cMplsVpnVrfConfMaxRts_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,10),_H3cMplsVpnVrfConfMaxRts_Type())
h3cMplsVpnVrfConfMaxRts.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfConfMaxRts.setStatus(_A)
_H3cMplsVpnVrfConfRowStatus_Type=RowStatus
_H3cMplsVpnVrfConfRowStatus_Object=MibTableColumn
h3cMplsVpnVrfConfRowStatus=_H3cMplsVpnVrfConfRowStatus_Object((1,3,6,1,4,1,2011,10,2,160,1,1,1,1,11),_H3cMplsVpnVrfConfRowStatus_Type())
h3cMplsVpnVrfConfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfConfRowStatus.setStatus(_A)
_H3cMplsVpnVrfBgpNbrAddrTable_Object=MibTable
h3cMplsVpnVrfBgpNbrAddrTable=_H3cMplsVpnVrfBgpNbrAddrTable_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2))
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrAddrTable.setStatus(_A)
_H3cMplsVpnVrfBgpNbrAddrEntry_Object=MibTableRow
h3cMplsVpnVrfBgpNbrAddrEntry=_H3cMplsVpnVrfBgpNbrAddrEntry_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2,1))
h3cMplsVpnVrfBgpNbrAddrEntry.setIndexNames((0,_E,_G),(0,_E,_I))
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrAddrEntry.setStatus(_A)
_H3cMplsVpnVrfBgpNbrAddr_Type=IpAddress
_H3cMplsVpnVrfBgpNbrAddr_Object=MibTableColumn
h3cMplsVpnVrfBgpNbrAddr=_H3cMplsVpnVrfBgpNbrAddr_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2,1,1),_H3cMplsVpnVrfBgpNbrAddr_Type())
h3cMplsVpnVrfBgpNbrAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrAddr.setStatus(_A)
class _H3cMplsVpnVrfBgpNbrRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ce',1),('pe',2)))
_H3cMplsVpnVrfBgpNbrRole_Type.__name__=_C
_H3cMplsVpnVrfBgpNbrRole_Object=MibTableColumn
h3cMplsVpnVrfBgpNbrRole=_H3cMplsVpnVrfBgpNbrRole_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2,1,2),_H3cMplsVpnVrfBgpNbrRole_Type())
h3cMplsVpnVrfBgpNbrRole.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrRole.setStatus(_A)
_H3cMplsVpnVrfBgpNbrAsNumber_Type=Unsigned32
_H3cMplsVpnVrfBgpNbrAsNumber_Object=MibTableColumn
h3cMplsVpnVrfBgpNbrAsNumber=_H3cMplsVpnVrfBgpNbrAsNumber_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2,1,3),_H3cMplsVpnVrfBgpNbrAsNumber_Type())
h3cMplsVpnVrfBgpNbrAsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrAsNumber.setStatus(_A)
class _H3cMplsVpnVrfBgpNbrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mplsVpnVrfBgpNbrSetUp',1),('mplsVpnVrfBgpNbrSetDown',2)))
_H3cMplsVpnVrfBgpNbrAdminStatus_Type.__name__=_C
_H3cMplsVpnVrfBgpNbrAdminStatus_Object=MibTableColumn
h3cMplsVpnVrfBgpNbrAdminStatus=_H3cMplsVpnVrfBgpNbrAdminStatus_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2,1,4),_H3cMplsVpnVrfBgpNbrAdminStatus_Type())
h3cMplsVpnVrfBgpNbrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrAdminStatus.setStatus(_A)
_H3cMplsVpnVrfBgpNbrRowStatus_Type=RowStatus
_H3cMplsVpnVrfBgpNbrRowStatus_Object=MibTableColumn
h3cMplsVpnVrfBgpNbrRowStatus=_H3cMplsVpnVrfBgpNbrRowStatus_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2,1,5),_H3cMplsVpnVrfBgpNbrRowStatus_Type())
h3cMplsVpnVrfBgpNbrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrRowStatus.setStatus(_A)
class _H3cMplsVpnVrfBgpNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_H3cMplsVpnVrfBgpNbrState_Type.__name__=_C
_H3cMplsVpnVrfBgpNbrState_Object=MibTableColumn
h3cMplsVpnVrfBgpNbrState=_H3cMplsVpnVrfBgpNbrState_Object((1,3,6,1,4,1,2011,10,2,160,1,1,2,1,6),_H3cMplsVpnVrfBgpNbrState_Type())
h3cMplsVpnVrfBgpNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrState.setStatus(_A)
_H3cMplsVpnVrfBgpNbrPrefixTable_Object=MibTable
h3cMplsVpnVrfBgpNbrPrefixTable=_H3cMplsVpnVrfBgpNbrPrefixTable_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3))
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrPrefixTable.setStatus(_A)
_H3cMplsVpnVrfBgpNbrPrefixEntry_Object=MibTableRow
h3cMplsVpnVrfBgpNbrPrefixEntry=_H3cMplsVpnVrfBgpNbrPrefixEntry_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1))
h3cMplsVpnVrfBgpNbrPrefixEntry.setIndexNames((0,_E,_G),(0,_E,_J),(0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpNbrPrefixEntry.setStatus(_A)
_H3cMplsVpnVrfBgpPAtrPeer_Type=IpAddress
_H3cMplsVpnVrfBgpPAtrPeer_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrPeer=_H3cMplsVpnVrfBgpPAtrPeer_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,1),_H3cMplsVpnVrfBgpPAtrPeer_Type())
h3cMplsVpnVrfBgpPAtrPeer.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrPeer.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_H3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Type.__name__=_C
_H3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrIpAddrPrefixLen=_H3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,2),_H3cMplsVpnVrfBgpPAtrIpAddrPrefixLen_Type())
h3cMplsVpnVrfBgpPAtrIpAddrPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrIpAddrPrefixLen.setStatus(_A)
_H3cMplsVpnVrfBgpPAtrIpAddrPrefix_Type=IpAddress
_H3cMplsVpnVrfBgpPAtrIpAddrPrefix_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrIpAddrPrefix=_H3cMplsVpnVrfBgpPAtrIpAddrPrefix_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,3),_H3cMplsVpnVrfBgpPAtrIpAddrPrefix_Type())
h3cMplsVpnVrfBgpPAtrIpAddrPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrIpAddrPrefix.setStatus(_A)
_H3cMplsVpnVrfBgpPAtrPeerType_Type=InetAddressType
_H3cMplsVpnVrfBgpPAtrPeerType_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrPeerType=_H3cMplsVpnVrfBgpPAtrPeerType_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,4),_H3cMplsVpnVrfBgpPAtrPeerType_Type())
h3cMplsVpnVrfBgpPAtrPeerType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrPeerType.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_H3cMplsVpnVrfBgpPAtrOrigin_Type.__name__=_C
_H3cMplsVpnVrfBgpPAtrOrigin_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrOrigin=_H3cMplsVpnVrfBgpPAtrOrigin_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,5),_H3cMplsVpnVrfBgpPAtrOrigin_Type())
h3cMplsVpnVrfBgpPAtrOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrOrigin.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_H3cMplsVpnVrfBgpPAtrASPathSegment_Type.__name__=_H
_H3cMplsVpnVrfBgpPAtrASPathSegment_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrASPathSegment=_H3cMplsVpnVrfBgpPAtrASPathSegment_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,6),_H3cMplsVpnVrfBgpPAtrASPathSegment_Type())
h3cMplsVpnVrfBgpPAtrASPathSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrASPathSegment.setStatus(_A)
_H3cMplsVpnVrfBgpPAtrNextHop_Type=IpAddress
_H3cMplsVpnVrfBgpPAtrNextHop_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrNextHop=_H3cMplsVpnVrfBgpPAtrNextHop_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,7),_H3cMplsVpnVrfBgpPAtrNextHop_Type())
h3cMplsVpnVrfBgpPAtrNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrNextHop.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_H3cMplsVpnVrfBgpPAtrMultiExitDisc_Type.__name__=_C
_H3cMplsVpnVrfBgpPAtrMultiExitDisc_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrMultiExitDisc=_H3cMplsVpnVrfBgpPAtrMultiExitDisc_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,8),_H3cMplsVpnVrfBgpPAtrMultiExitDisc_Type())
h3cMplsVpnVrfBgpPAtrMultiExitDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrMultiExitDisc.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_H3cMplsVpnVrfBgpPAtrLocalPref_Type.__name__=_C
_H3cMplsVpnVrfBgpPAtrLocalPref_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrLocalPref=_H3cMplsVpnVrfBgpPAtrLocalPref_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,9),_H3cMplsVpnVrfBgpPAtrLocalPref_Type())
h3cMplsVpnVrfBgpPAtrLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrLocalPref.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRtNotSelected',1),('lessSpecificRtSelected',2)))
_H3cMplsVpnVrfBgpPAtrAtomicAggregate_Type.__name__=_C
_H3cMplsVpnVrfBgpPAtrAtomicAggregate_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrAtomicAggregate=_H3cMplsVpnVrfBgpPAtrAtomicAggregate_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,10),_H3cMplsVpnVrfBgpPAtrAtomicAggregate_Type())
h3cMplsVpnVrfBgpPAtrAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrAtomicAggregate.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cMplsVpnVrfBgpPAtrAggregatorAS_Type.__name__=_C
_H3cMplsVpnVrfBgpPAtrAggregatorAS_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrAggregatorAS=_H3cMplsVpnVrfBgpPAtrAggregatorAS_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,11),_H3cMplsVpnVrfBgpPAtrAggregatorAS_Type())
h3cMplsVpnVrfBgpPAtrAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrAggregatorAS.setStatus(_A)
_H3cMplsVpnVrfBgpPAtrAggregatorAddr_Type=IpAddress
_H3cMplsVpnVrfBgpPAtrAggregatorAddr_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrAggregatorAddr=_H3cMplsVpnVrfBgpPAtrAggregatorAddr_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,12),_H3cMplsVpnVrfBgpPAtrAggregatorAddr_Type())
h3cMplsVpnVrfBgpPAtrAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrAggregatorAddr.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_H3cMplsVpnVrfBgpPAtrCalcLocalPref_Type.__name__=_C
_H3cMplsVpnVrfBgpPAtrCalcLocalPref_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrCalcLocalPref=_H3cMplsVpnVrfBgpPAtrCalcLocalPref_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,13),_H3cMplsVpnVrfBgpPAtrCalcLocalPref_Type())
h3cMplsVpnVrfBgpPAtrCalcLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrCalcLocalPref.setStatus(_A)
_H3cMplsVpnVrfBgpPAtrBest_Type=TruthValue
_H3cMplsVpnVrfBgpPAtrBest_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrBest=_H3cMplsVpnVrfBgpPAtrBest_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,14),_H3cMplsVpnVrfBgpPAtrBest_Type())
h3cMplsVpnVrfBgpPAtrBest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrBest.setStatus(_A)
class _H3cMplsVpnVrfBgpPAtrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cMplsVpnVrfBgpPAtrUnknown_Type.__name__=_H
_H3cMplsVpnVrfBgpPAtrUnknown_Object=MibTableColumn
h3cMplsVpnVrfBgpPAtrUnknown=_H3cMplsVpnVrfBgpPAtrUnknown_Object((1,3,6,1,4,1,2011,10,2,160,1,1,3,1,15),_H3cMplsVpnVrfBgpPAtrUnknown_Type())
h3cMplsVpnVrfBgpPAtrUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsVpnVrfBgpPAtrUnknown.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'H3cMplsVpnId':H3cMplsVpnId,'H3cMplsVpnRtDistinguisher':H3cMplsVpnRtDistinguisher,'h3cMplsVpnBgp':h3cMplsVpnBgp,'h3cMplsVpnObjects':h3cMplsVpnObjects,'h3cMplsVpnConf':h3cMplsVpnConf,'h3cMplsVpnVrfConfTable':h3cMplsVpnVrfConfTable,'h3cMplsVpnVrfConfEntry':h3cMplsVpnVrfConfEntry,_G:h3cMplsVpnVrfName,'h3cMplsVpnVrfRtDistinguisher':h3cMplsVpnVrfRtDistinguisher,'h3cMplsVpnVrfNetPrefixType':h3cMplsVpnVrfNetPrefixType,'h3cMplsVpnVrfNetPrefix':h3cMplsVpnVrfNetPrefix,'h3cMplsVpnVrfIpRtRedistributeConn':h3cMplsVpnVrfIpRtRedistributeConn,'h3cMplsVpnVrfIpRtRedistributeStatic':h3cMplsVpnVrfIpRtRedistributeStatic,'h3cMplsVpnVrfIpRtRedistributeRip':h3cMplsVpnVrfIpRtRedistributeRip,'h3cMplsVpnVrfConfHighRtThreshold':h3cMplsVpnVrfConfHighRtThreshold,'h3cMplsVpnVrfConfIsWarnOnly':h3cMplsVpnVrfConfIsWarnOnly,'h3cMplsVpnVrfConfMaxRts':h3cMplsVpnVrfConfMaxRts,'h3cMplsVpnVrfConfRowStatus':h3cMplsVpnVrfConfRowStatus,'h3cMplsVpnVrfBgpNbrAddrTable':h3cMplsVpnVrfBgpNbrAddrTable,'h3cMplsVpnVrfBgpNbrAddrEntry':h3cMplsVpnVrfBgpNbrAddrEntry,_I:h3cMplsVpnVrfBgpNbrAddr,'h3cMplsVpnVrfBgpNbrRole':h3cMplsVpnVrfBgpNbrRole,'h3cMplsVpnVrfBgpNbrAsNumber':h3cMplsVpnVrfBgpNbrAsNumber,'h3cMplsVpnVrfBgpNbrAdminStatus':h3cMplsVpnVrfBgpNbrAdminStatus,'h3cMplsVpnVrfBgpNbrRowStatus':h3cMplsVpnVrfBgpNbrRowStatus,'h3cMplsVpnVrfBgpNbrState':h3cMplsVpnVrfBgpNbrState,'h3cMplsVpnVrfBgpNbrPrefixTable':h3cMplsVpnVrfBgpNbrPrefixTable,'h3cMplsVpnVrfBgpNbrPrefixEntry':h3cMplsVpnVrfBgpNbrPrefixEntry,_J:h3cMplsVpnVrfBgpPAtrPeer,_K:h3cMplsVpnVrfBgpPAtrIpAddrPrefixLen,_L:h3cMplsVpnVrfBgpPAtrIpAddrPrefix,'h3cMplsVpnVrfBgpPAtrPeerType':h3cMplsVpnVrfBgpPAtrPeerType,'h3cMplsVpnVrfBgpPAtrOrigin':h3cMplsVpnVrfBgpPAtrOrigin,'h3cMplsVpnVrfBgpPAtrASPathSegment':h3cMplsVpnVrfBgpPAtrASPathSegment,'h3cMplsVpnVrfBgpPAtrNextHop':h3cMplsVpnVrfBgpPAtrNextHop,'h3cMplsVpnVrfBgpPAtrMultiExitDisc':h3cMplsVpnVrfBgpPAtrMultiExitDisc,'h3cMplsVpnVrfBgpPAtrLocalPref':h3cMplsVpnVrfBgpPAtrLocalPref,'h3cMplsVpnVrfBgpPAtrAtomicAggregate':h3cMplsVpnVrfBgpPAtrAtomicAggregate,'h3cMplsVpnVrfBgpPAtrAggregatorAS':h3cMplsVpnVrfBgpPAtrAggregatorAS,'h3cMplsVpnVrfBgpPAtrAggregatorAddr':h3cMplsVpnVrfBgpPAtrAggregatorAddr,'h3cMplsVpnVrfBgpPAtrCalcLocalPref':h3cMplsVpnVrfBgpPAtrCalcLocalPref,'h3cMplsVpnVrfBgpPAtrBest':h3cMplsVpnVrfBgpPAtrBest,'h3cMplsVpnVrfBgpPAtrUnknown':h3cMplsVpnVrfBgpPAtrUnknown})