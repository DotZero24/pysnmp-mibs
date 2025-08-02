_K='h3cBgpEvpnPAtrAddrPrefix'
_J='h3cBgpEvpnPAtrAddrPrefixLen'
_I='h3cBgpEvpnPAtrPeer'
_H='h3cBgpEvpnPAtrRD'
_G='h3cBgpEvpnNbrAddr'
_F='not-accessible'
_E='H3C-BGP-EVPN-MIB'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cBgpEvpn=ModuleIdentity((1,3,6,1,4,1,2011,10,2,172))
if mibBuilder.loadTexts:h3cBgpEvpn.setRevisions(('2017-11-29 14:31','2017-11-04 14:31'))
_H3cBgpEvpnObjects_ObjectIdentity=ObjectIdentity
h3cBgpEvpnObjects=_H3cBgpEvpnObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,172,1))
_H3cBgpEvpnConf_ObjectIdentity=ObjectIdentity
h3cBgpEvpnConf=_H3cBgpEvpnConf_ObjectIdentity((1,3,6,1,4,1,2011,10,2,172,1,1))
_H3cBgpEvpnNbrAddrTable_Object=MibTable
h3cBgpEvpnNbrAddrTable=_H3cBgpEvpnNbrAddrTable_Object((1,3,6,1,4,1,2011,10,2,172,1,1,1))
if mibBuilder.loadTexts:h3cBgpEvpnNbrAddrTable.setStatus(_A)
_H3cBgpEvpnNbrAddrEntry_Object=MibTableRow
h3cBgpEvpnNbrAddrEntry=_H3cBgpEvpnNbrAddrEntry_Object((1,3,6,1,4,1,2011,10,2,172,1,1,1,1))
h3cBgpEvpnNbrAddrEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:h3cBgpEvpnNbrAddrEntry.setStatus(_A)
_H3cBgpEvpnNbrAddr_Type=IpAddress
_H3cBgpEvpnNbrAddr_Object=MibTableColumn
h3cBgpEvpnNbrAddr=_H3cBgpEvpnNbrAddr_Object((1,3,6,1,4,1,2011,10,2,172,1,1,1,1,1),_H3cBgpEvpnNbrAddr_Type())
h3cBgpEvpnNbrAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBgpEvpnNbrAddr.setStatus(_A)
_H3cBgpEvpnNbrAsNumber_Type=Unsigned32
_H3cBgpEvpnNbrAsNumber_Object=MibTableColumn
h3cBgpEvpnNbrAsNumber=_H3cBgpEvpnNbrAsNumber_Object((1,3,6,1,4,1,2011,10,2,172,1,1,1,1,2),_H3cBgpEvpnNbrAsNumber_Type())
h3cBgpEvpnNbrAsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnNbrAsNumber.setStatus(_A)
_H3cBgpEvpnNbrPrefixTable_Object=MibTable
h3cBgpEvpnNbrPrefixTable=_H3cBgpEvpnNbrPrefixTable_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2))
if mibBuilder.loadTexts:h3cBgpEvpnNbrPrefixTable.setStatus(_A)
_H3cBgpEvpnNbrPrefixEntry_Object=MibTableRow
h3cBgpEvpnNbrPrefixEntry=_H3cBgpEvpnNbrPrefixEntry_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1))
h3cBgpEvpnNbrPrefixEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:h3cBgpEvpnNbrPrefixEntry.setStatus(_A)
class _H3cBgpEvpnPAtrRD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,21))
_H3cBgpEvpnPAtrRD_Type.__name__=_C
_H3cBgpEvpnPAtrRD_Object=MibTableColumn
h3cBgpEvpnPAtrRD=_H3cBgpEvpnPAtrRD_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,1),_H3cBgpEvpnPAtrRD_Type())
h3cBgpEvpnPAtrRD.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrRD.setStatus(_A)
class _H3cBgpEvpnPAtrPeer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,86))
_H3cBgpEvpnPAtrPeer_Type.__name__=_C
_H3cBgpEvpnPAtrPeer_Object=MibTableColumn
h3cBgpEvpnPAtrPeer=_H3cBgpEvpnPAtrPeer_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,2),_H3cBgpEvpnPAtrPeer_Type())
h3cBgpEvpnPAtrPeer.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrPeer.setStatus(_A)
class _H3cBgpEvpnPAtrAddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_H3cBgpEvpnPAtrAddrPrefixLen_Type.__name__=_D
_H3cBgpEvpnPAtrAddrPrefixLen_Object=MibTableColumn
h3cBgpEvpnPAtrAddrPrefixLen=_H3cBgpEvpnPAtrAddrPrefixLen_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,3),_H3cBgpEvpnPAtrAddrPrefixLen_Type())
h3cBgpEvpnPAtrAddrPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrAddrPrefixLen.setStatus(_A)
_H3cBgpEvpnPAtrAddrPrefix_Type=IpAddress
_H3cBgpEvpnPAtrAddrPrefix_Object=MibTableColumn
h3cBgpEvpnPAtrAddrPrefix=_H3cBgpEvpnPAtrAddrPrefix_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,4),_H3cBgpEvpnPAtrAddrPrefix_Type())
h3cBgpEvpnPAtrAddrPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrAddrPrefix.setStatus(_A)
_H3cBgpEvpnPAtrRouteType_Type=Unsigned32
_H3cBgpEvpnPAtrRouteType_Object=MibTableColumn
h3cBgpEvpnPAtrRouteType=_H3cBgpEvpnPAtrRouteType_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,5),_H3cBgpEvpnPAtrRouteType_Type())
h3cBgpEvpnPAtrRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrRouteType.setStatus(_A)
class _H3cBgpEvpnPAtrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_H3cBgpEvpnPAtrOrigin_Type.__name__=_D
_H3cBgpEvpnPAtrOrigin_Object=MibTableColumn
h3cBgpEvpnPAtrOrigin=_H3cBgpEvpnPAtrOrigin_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,6),_H3cBgpEvpnPAtrOrigin_Type())
h3cBgpEvpnPAtrOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrOrigin.setStatus(_A)
class _H3cBgpEvpnPAtrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_H3cBgpEvpnPAtrASPathSegment_Type.__name__=_C
_H3cBgpEvpnPAtrASPathSegment_Object=MibTableColumn
h3cBgpEvpnPAtrASPathSegment=_H3cBgpEvpnPAtrASPathSegment_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,7),_H3cBgpEvpnPAtrASPathSegment_Type())
h3cBgpEvpnPAtrASPathSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrASPathSegment.setStatus(_A)
_H3cBgpEvpnPAtrNextHop_Type=IpAddress
_H3cBgpEvpnPAtrNextHop_Object=MibTableColumn
h3cBgpEvpnPAtrNextHop=_H3cBgpEvpnPAtrNextHop_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,8),_H3cBgpEvpnPAtrNextHop_Type())
h3cBgpEvpnPAtrNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrNextHop.setStatus(_A)
class _H3cBgpEvpnPAtrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_H3cBgpEvpnPAtrMultiExitDisc_Type.__name__=_D
_H3cBgpEvpnPAtrMultiExitDisc_Object=MibTableColumn
h3cBgpEvpnPAtrMultiExitDisc=_H3cBgpEvpnPAtrMultiExitDisc_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,9),_H3cBgpEvpnPAtrMultiExitDisc_Type())
h3cBgpEvpnPAtrMultiExitDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrMultiExitDisc.setStatus(_A)
class _H3cBgpEvpnPAtrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_H3cBgpEvpnPAtrLocalPref_Type.__name__=_D
_H3cBgpEvpnPAtrLocalPref_Object=MibTableColumn
h3cBgpEvpnPAtrLocalPref=_H3cBgpEvpnPAtrLocalPref_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,10),_H3cBgpEvpnPAtrLocalPref_Type())
h3cBgpEvpnPAtrLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrLocalPref.setStatus(_A)
class _H3cBgpEvpnPAtrIGMPFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igmpv1',1),('igmpv2',2),('igmpv3',3)))
_H3cBgpEvpnPAtrIGMPFlags_Type.__name__=_D
_H3cBgpEvpnPAtrIGMPFlags_Object=MibTableColumn
h3cBgpEvpnPAtrIGMPFlags=_H3cBgpEvpnPAtrIGMPFlags_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,11),_H3cBgpEvpnPAtrIGMPFlags_Type())
h3cBgpEvpnPAtrIGMPFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrIGMPFlags.setStatus(_A)
_H3cBgpEvpnPAtrMaxRespTime_Type=Unsigned32
_H3cBgpEvpnPAtrMaxRespTime_Object=MibTableColumn
h3cBgpEvpnPAtrMaxRespTime=_H3cBgpEvpnPAtrMaxRespTime_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,12),_H3cBgpEvpnPAtrMaxRespTime_Type())
h3cBgpEvpnPAtrMaxRespTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrMaxRespTime.setStatus(_A)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrMaxRespTime.setUnits('ms')
class _H3cBgpEvpnPAtrPMSITunnel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,21))
_H3cBgpEvpnPAtrPMSITunnel_Type.__name__=_C
_H3cBgpEvpnPAtrPMSITunnel_Object=MibTableColumn
h3cBgpEvpnPAtrPMSITunnel=_H3cBgpEvpnPAtrPMSITunnel_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,13),_H3cBgpEvpnPAtrPMSITunnel_Type())
h3cBgpEvpnPAtrPMSITunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrPMSITunnel.setStatus(_A)
_H3cBgpEvpnPAtrL2VNI_Type=Unsigned32
_H3cBgpEvpnPAtrL2VNI_Object=MibTableColumn
h3cBgpEvpnPAtrL2VNI=_H3cBgpEvpnPAtrL2VNI_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,14),_H3cBgpEvpnPAtrL2VNI_Type())
h3cBgpEvpnPAtrL2VNI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrL2VNI.setStatus(_A)
_H3cBgpEvpnPAtrL3VNI_Type=Unsigned32
_H3cBgpEvpnPAtrL3VNI_Object=MibTableColumn
h3cBgpEvpnPAtrL3VNI=_H3cBgpEvpnPAtrL3VNI_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,15),_H3cBgpEvpnPAtrL3VNI_Type())
h3cBgpEvpnPAtrL3VNI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrL3VNI.setStatus(_A)
_H3cBgpEvpnPAtrBest_Type=TruthValue
_H3cBgpEvpnPAtrBest_Object=MibTableColumn
h3cBgpEvpnPAtrBest=_H3cBgpEvpnPAtrBest_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,16),_H3cBgpEvpnPAtrBest_Type())
h3cBgpEvpnPAtrBest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrBest.setStatus(_A)
class _H3cBgpEvpnPAtrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cBgpEvpnPAtrUnknown_Type.__name__=_C
_H3cBgpEvpnPAtrUnknown_Object=MibTableColumn
h3cBgpEvpnPAtrUnknown=_H3cBgpEvpnPAtrUnknown_Object((1,3,6,1,4,1,2011,10,2,172,1,1,2,1,17),_H3cBgpEvpnPAtrUnknown_Type())
h3cBgpEvpnPAtrUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBgpEvpnPAtrUnknown.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cBgpEvpn':h3cBgpEvpn,'h3cBgpEvpnObjects':h3cBgpEvpnObjects,'h3cBgpEvpnConf':h3cBgpEvpnConf,'h3cBgpEvpnNbrAddrTable':h3cBgpEvpnNbrAddrTable,'h3cBgpEvpnNbrAddrEntry':h3cBgpEvpnNbrAddrEntry,_G:h3cBgpEvpnNbrAddr,'h3cBgpEvpnNbrAsNumber':h3cBgpEvpnNbrAsNumber,'h3cBgpEvpnNbrPrefixTable':h3cBgpEvpnNbrPrefixTable,'h3cBgpEvpnNbrPrefixEntry':h3cBgpEvpnNbrPrefixEntry,_H:h3cBgpEvpnPAtrRD,_I:h3cBgpEvpnPAtrPeer,_J:h3cBgpEvpnPAtrAddrPrefixLen,_K:h3cBgpEvpnPAtrAddrPrefix,'h3cBgpEvpnPAtrRouteType':h3cBgpEvpnPAtrRouteType,'h3cBgpEvpnPAtrOrigin':h3cBgpEvpnPAtrOrigin,'h3cBgpEvpnPAtrASPathSegment':h3cBgpEvpnPAtrASPathSegment,'h3cBgpEvpnPAtrNextHop':h3cBgpEvpnPAtrNextHop,'h3cBgpEvpnPAtrMultiExitDisc':h3cBgpEvpnPAtrMultiExitDisc,'h3cBgpEvpnPAtrLocalPref':h3cBgpEvpnPAtrLocalPref,'h3cBgpEvpnPAtrIGMPFlags':h3cBgpEvpnPAtrIGMPFlags,'h3cBgpEvpnPAtrMaxRespTime':h3cBgpEvpnPAtrMaxRespTime,'h3cBgpEvpnPAtrPMSITunnel':h3cBgpEvpnPAtrPMSITunnel,'h3cBgpEvpnPAtrL2VNI':h3cBgpEvpnPAtrL2VNI,'h3cBgpEvpnPAtrL3VNI':h3cBgpEvpnPAtrL3VNI,'h3cBgpEvpnPAtrBest':h3cBgpEvpnPAtrBest,'h3cBgpEvpnPAtrUnknown':h3cBgpEvpnPAtrUnknown})