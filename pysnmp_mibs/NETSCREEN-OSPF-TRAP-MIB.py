_h='nsOspfVirtNbrState'
_g='nsOspfVirtNbrRtrId'
_f='nsOspfVirtNbrArea'
_e='nsOspfVirtIfState'
_d='nsOspfNbrState'
_c='nsOspfNbrIpAddr'
_b='nsOspfNbrAddressLessIndex'
_a='nsOspfIfState'
_Z='OctetString'
_Y='Integer32'
_X='nsOspfNbrRtrId'
_W='nsOspfLsdbAreaId'
_V='nsOspfExtLsdbLimit'
_U='nsOspfIfVRID'
_T='nsOspfPacketSrc'
_S='nsOspfVirtIfVRID'
_R='read-only'
_Q='nsOspfConfigErrorType'
_P='nsOspfLsdbType'
_O='nsOspfLsdbRouterId'
_N='nsOspfLsdbLsid'
_M='nsOspfLsdbVRID'
_L='nsOspfVirtIfNeighbor'
_K='nsOspfVirtIfAreaId'
_J='nsOspfIfIpAddress'
_I='nsOspfAddressLessIf'
_H='nsOspfPacketType'
_G='netscreenTrapType'
_F='netscreenTrapDesc'
_E='nsOspfRouterId'
_D='current'
_C='NETSCREEN-OSPF-TRAP-MIB'
_B='NETSCREEN-TRAP-MIB'
_A='NETSCREEN-OSPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Z,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nsOspf,nsOspfAddressLessIf,nsOspfExtLsdbLimit,nsOspfIfIpAddress,nsOspfIfState,nsOspfLsdbAreaId,nsOspfLsdbLsid,nsOspfLsdbRouterId,nsOspfLsdbType,nsOspfNbrAddressLessIndex,nsOspfNbrIpAddr,nsOspfNbrRtrId,nsOspfNbrState,nsOspfRouterId,nsOspfVirtIfAreaId,nsOspfVirtIfNeighbor,nsOspfVirtIfState,nsOspfVirtNbrArea,nsOspfVirtNbrRtrId,nsOspfVirtNbrState=mibBuilder.importSymbols(_A,'nsOspf',_I,_V,_J,_a,_W,_N,_O,_P,_b,_c,_X,_d,_E,_K,_L,_e,_f,_g,_h)
netscreenTrapDesc,netscreenTrapType=mibBuilder.importSymbols(_B,_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Y,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nsOspfTrap=ModuleIdentity((1,3,6,1,4,1,3224,18,2,16))
_NsOspfTrapControl_ObjectIdentity=ObjectIdentity
nsOspfTrapControl=_NsOspfTrapControl_ObjectIdentity((1,3,6,1,4,1,3224,18,2,16,1))
class _NsOspfSetTrap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NsOspfSetTrap_Type.__name__=_Z
_NsOspfSetTrap_Object=MibScalar
nsOspfSetTrap=_NsOspfSetTrap_Object((1,3,6,1,4,1,3224,18,2,16,1,1),_NsOspfSetTrap_Type())
nsOspfSetTrap.setMaxAccess(_R)
if mibBuilder.loadTexts:nsOspfSetTrap.setStatus(_D)
class _NsOspfConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('badVersion',1),('areaMismatch',2),('unknownNbmaNbr',3),('unknownVirtualNbr',4),('authTypeMismatch',5),('authFailure',6),('netMaskMismatch',7),('helloIntervalMismatch',8),('deadIntervalMismatch',9),('optionMismatch',10)))
_NsOspfConfigErrorType_Type.__name__=_Y
_NsOspfConfigErrorType_Object=MibScalar
nsOspfConfigErrorType=_NsOspfConfigErrorType_Object((1,3,6,1,4,1,3224,18,2,16,1,2),_NsOspfConfigErrorType_Type())
nsOspfConfigErrorType.setMaxAccess(_R)
if mibBuilder.loadTexts:nsOspfConfigErrorType.setStatus(_D)
class _NsOspfPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('hello',1),('dbDescript',2),('lsReq',3),('lsUpdate',4),('lsAck',5)))
_NsOspfPacketType_Type.__name__=_Y
_NsOspfPacketType_Object=MibScalar
nsOspfPacketType=_NsOspfPacketType_Object((1,3,6,1,4,1,3224,18,2,16,1,3),_NsOspfPacketType_Type())
nsOspfPacketType.setMaxAccess(_R)
if mibBuilder.loadTexts:nsOspfPacketType.setStatus(_D)
_NsOspfPacketSrc_Type=IpAddress
_NsOspfPacketSrc_Object=MibScalar
nsOspfPacketSrc=_NsOspfPacketSrc_Object((1,3,6,1,4,1,3224,18,2,16,1,4),_NsOspfPacketSrc_Type())
nsOspfPacketSrc.setMaxAccess(_R)
if mibBuilder.loadTexts:nsOspfPacketSrc.setStatus(_D)
_NsOspfTraps_ObjectIdentity=ObjectIdentity
nsOspfTraps=_NsOspfTraps_ObjectIdentity((1,3,6,1,4,1,3224,18,2,16,2))
nsOspfVirtIfStateChange=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,1))
nsOspfVirtIfStateChange.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_K),(_A,_L),(_A,_e),(_C,_S)))
if mibBuilder.loadTexts:nsOspfVirtIfStateChange.setStatus(_D)
nsOspfNbrStateChange=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,2))
nsOspfNbrStateChange.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_c),(_A,_b),(_A,_X),(_A,_d),(_C,'nsOspfNbrVRID')))
if mibBuilder.loadTexts:nsOspfNbrStateChange.setStatus(_D)
nsOspfVirtNbrStateChange=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,3))
nsOspfVirtNbrStateChange.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_f),(_A,_g),(_A,_h),(_C,'nsOspfVirtNbrVRID')))
if mibBuilder.loadTexts:nsOspfVirtNbrStateChange.setStatus(_D)
nsOspfIfConfigError=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,4))
nsOspfIfConfigError.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_J),(_A,_I),(_C,_T),(_C,_Q),(_C,_H),(_C,_U)))
if mibBuilder.loadTexts:nsOspfIfConfigError.setStatus(_D)
nsOspfVirtIfConfigError=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,5))
nsOspfVirtIfConfigError.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_K),(_A,_L),(_C,_Q),(_C,_H),(_C,_S)))
if mibBuilder.loadTexts:nsOspfVirtIfConfigError.setStatus(_D)
nsOspfIfAuthFailure=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,6))
nsOspfIfAuthFailure.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_J),(_A,_I),(_C,_T),(_C,_Q),(_C,_H),(_C,_U)))
if mibBuilder.loadTexts:nsOspfIfAuthFailure.setStatus(_D)
nsOspfVirtIfAuthFailure=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,7))
nsOspfVirtIfAuthFailure.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_K),(_A,_L),(_C,_Q),(_C,_H),(_C,_S)))
if mibBuilder.loadTexts:nsOspfVirtIfAuthFailure.setStatus(_D)
nsOspfIfRxBadPacket=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,8))
nsOspfIfRxBadPacket.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_J),(_A,_I),(_C,_T),(_C,_H),(_C,_U)))
if mibBuilder.loadTexts:nsOspfIfRxBadPacket.setStatus(_D)
nsOspfVirtIfRxBadPacket=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,9))
nsOspfVirtIfRxBadPacket.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_K),(_A,_L),(_C,_H),(_C,_S)))
if mibBuilder.loadTexts:nsOspfVirtIfRxBadPacket.setStatus(_D)
nsOspfTxRetransmit=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,10))
nsOspfTxRetransmit.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_J),(_A,_I),(_A,_X),(_C,_H),(_A,_P),(_A,_N),(_A,_O),(_C,_M)))
if mibBuilder.loadTexts:nsOspfTxRetransmit.setStatus(_D)
nsOspfVirtIfTxRetransmit=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,11))
nsOspfVirtIfTxRetransmit.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_K),(_A,_L),(_C,_H),(_A,_P),(_A,_N),(_A,_O),(_C,_M)))
if mibBuilder.loadTexts:nsOspfVirtIfTxRetransmit.setStatus(_D)
nsOspfOriginateLsa=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,12))
nsOspfOriginateLsa.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_W),(_A,_P),(_A,_N),(_A,_O),(_C,_M)))
if mibBuilder.loadTexts:nsOspfOriginateLsa.setStatus(_D)
nsOspfMaxAgeLsa=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,13))
nsOspfMaxAgeLsa.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_W),(_A,_P),(_A,_N),(_A,_O),(_C,_M)))
if mibBuilder.loadTexts:nsOspfMaxAgeLsa.setStatus(_D)
nsOspfLsdbOverflow=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,14))
nsOspfLsdbOverflow.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_V),(_C,_M)))
if mibBuilder.loadTexts:nsOspfLsdbOverflow.setStatus(_D)
nsOspfLsdbApproachingOverflow=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,15))
nsOspfLsdbApproachingOverflow.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_V),(_C,_M)))
if mibBuilder.loadTexts:nsOspfLsdbApproachingOverflow.setStatus(_D)
nsOspfIfStateChange=NotificationType((1,3,6,1,4,1,3224,18,2,16,2,16))
nsOspfIfStateChange.setObjects(*((_B,_G),(_B,_F),(_A,_E),(_A,_J),(_A,_I),(_A,_a),(_C,_U)))
if mibBuilder.loadTexts:nsOspfIfStateChange.setStatus(_D)
mibBuilder.exportSymbols(_C,**{'nsOspfTrap':nsOspfTrap,'nsOspfTrapControl':nsOspfTrapControl,'nsOspfSetTrap':nsOspfSetTrap,_Q:nsOspfConfigErrorType,_H:nsOspfPacketType,_T:nsOspfPacketSrc,'nsOspfTraps':nsOspfTraps,'nsOspfVirtIfStateChange':nsOspfVirtIfStateChange,'nsOspfNbrStateChange':nsOspfNbrStateChange,'nsOspfVirtNbrStateChange':nsOspfVirtNbrStateChange,'nsOspfIfConfigError':nsOspfIfConfigError,'nsOspfVirtIfConfigError':nsOspfVirtIfConfigError,'nsOspfIfAuthFailure':nsOspfIfAuthFailure,'nsOspfVirtIfAuthFailure':nsOspfVirtIfAuthFailure,'nsOspfIfRxBadPacket':nsOspfIfRxBadPacket,'nsOspfVirtIfRxBadPacket':nsOspfVirtIfRxBadPacket,'nsOspfTxRetransmit':nsOspfTxRetransmit,'nsOspfVirtIfTxRetransmit':nsOspfVirtIfTxRetransmit,'nsOspfOriginateLsa':nsOspfOriginateLsa,'nsOspfMaxAgeLsa':nsOspfMaxAgeLsa,'nsOspfLsdbOverflow':nsOspfLsdbOverflow,'nsOspfLsdbApproachingOverflow':nsOspfLsdbApproachingOverflow,'nsOspfIfStateChange':nsOspfIfStateChange})