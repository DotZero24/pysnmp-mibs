_A9='ospfTrapEventGroup'
_A8='ospfVirtNbrRestartHelperStatusChange'
_A7='ospfNbrRestartHelperStatusChange'
_A6='ospfRestartStatusChange'
_A5='ospfNssaTranslatorStatusChange'
_A4='ospfIfStateChange'
_A3='ospfLsdbApproachingOverflow'
_A2='ospfLsdbOverflow'
_A1='ospfMaxAgeLsa'
_A0='ospfOriginateLsa'
_z='ospfVirtIfTxRetransmit'
_y='ospfTxRetransmit'
_x='ospfVirtIfRxBadPacket'
_w='ospfIfRxBadPacket'
_v='ospfVirtIfAuthFailure'
_u='ospfIfAuthFailure'
_t='ospfVirtIfConfigError'
_s='ospfIfConfigError'
_r='ospfVirtNbrStateChange'
_q='ospfNbrStateChange'
_p='ospfVirtIfStateChange'
_o='ospfSetTrap'
_n='ospfVirtNbrState'
_m='ospfVirtNbrRestartHelperStatus'
_l='ospfVirtNbrRestartHelperExitReason'
_k='ospfVirtNbrRestartHelperAge'
_j='ospfVirtIfState'
_i='ospfRestartStatus'
_h='ospfRestartInterval'
_g='ospfRestartExitReason'
_f='ospfNbrState'
_e='ospfNbrRestartHelperStatus'
_d='ospfNbrRestartHelperExitReason'
_c='ospfNbrRestartHelperAge'
_b='ospfIfState'
_a='ospfAreaNssaTranslatorState'
_Z='ospfAreaId'
_Y='OctetString'
_X='read-only'
_W='Integer32'
_V='ospfVirtNbrRtrId'
_U='ospfVirtNbrArea'
_T='ospfNbrIpAddr'
_S='ospfNbrAddressLessIndex'
_R='ospfLsdbAreaId'
_Q='ospfExtLsdbLimit'
_P='ospfTrapControlGroup'
_O='ospfNbrRtrId'
_N='ospfPacketSrc'
_M='ospfLsdbType'
_L='ospfLsdbRouterId'
_K='ospfLsdbLsid'
_J='ospfConfigErrorType'
_I='ospfVirtIfNeighbor'
_H='ospfVirtIfAreaId'
_G='ospfIfIpAddress'
_F='ospfAddressLessIf'
_E='ospfPacketType'
_D='ospfRouterId'
_C='current'
_B='OSPF-TRAP-MIB'
_A='OSPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ospf,ospfAddressLessIf,ospfAreaId,ospfAreaNssaTranslatorState,ospfExtLsdbLimit,ospfIfIpAddress,ospfIfState,ospfLsdbAreaId,ospfLsdbLsid,ospfLsdbRouterId,ospfLsdbType,ospfNbrAddressLessIndex,ospfNbrIpAddr,ospfNbrRestartHelperAge,ospfNbrRestartHelperExitReason,ospfNbrRestartHelperStatus,ospfNbrRtrId,ospfNbrState,ospfRestartExitReason,ospfRestartInterval,ospfRestartStatus,ospfRouterId,ospfVirtIfAreaId,ospfVirtIfNeighbor,ospfVirtIfState,ospfVirtNbrArea,ospfVirtNbrRestartHelperAge,ospfVirtNbrRestartHelperExitReason,ospfVirtNbrRestartHelperStatus,ospfVirtNbrRtrId,ospfVirtNbrState=mibBuilder.importSymbols(_A,'ospf',_F,_Z,_a,_Q,_G,_b,_R,_K,_L,_M,_S,_T,_c,_d,_e,_O,_f,_g,_h,_i,_D,_H,_I,_j,_U,_k,_l,_m,_V,_n)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_W,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ospfTrap=ModuleIdentity((1,3,6,1,2,1,14,16))
if mibBuilder.loadTexts:ospfTrap.setRevisions(('2006-11-10 00:00','1995-01-20 12:25'))
_OspfTrapControl_ObjectIdentity=ObjectIdentity
ospfTrapControl=_OspfTrapControl_ObjectIdentity((1,3,6,1,2,1,14,16,1))
class _OspfSetTrap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_OspfSetTrap_Type.__name__=_Y
_OspfSetTrap_Object=MibScalar
ospfSetTrap=_OspfSetTrap_Object((1,3,6,1,2,1,14,16,1,1),_OspfSetTrap_Type())
ospfSetTrap.setMaxAccess('read-write')
if mibBuilder.loadTexts:ospfSetTrap.setStatus(_C)
class _OspfConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('badVersion',1),('areaMismatch',2),('unknownNbmaNbr',3),('unknownVirtualNbr',4),('authTypeMismatch',5),('authFailure',6),('netMaskMismatch',7),('helloIntervalMismatch',8),('deadIntervalMismatch',9),('optionMismatch',10),('mtuMismatch',11),('duplicateRouterId',12),('noError',13)))
_OspfConfigErrorType_Type.__name__=_W
_OspfConfigErrorType_Object=MibScalar
ospfConfigErrorType=_OspfConfigErrorType_Object((1,3,6,1,2,1,14,16,1,2),_OspfConfigErrorType_Type())
ospfConfigErrorType.setMaxAccess(_X)
if mibBuilder.loadTexts:ospfConfigErrorType.setStatus(_C)
class _OspfPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('hello',1),('dbDescript',2),('lsReq',3),('lsUpdate',4),('lsAck',5),('nullPacket',6)))
_OspfPacketType_Type.__name__=_W
_OspfPacketType_Object=MibScalar
ospfPacketType=_OspfPacketType_Object((1,3,6,1,2,1,14,16,1,3),_OspfPacketType_Type())
ospfPacketType.setMaxAccess(_X)
if mibBuilder.loadTexts:ospfPacketType.setStatus(_C)
_OspfPacketSrc_Type=IpAddress
_OspfPacketSrc_Object=MibScalar
ospfPacketSrc=_OspfPacketSrc_Object((1,3,6,1,2,1,14,16,1,4),_OspfPacketSrc_Type())
ospfPacketSrc.setMaxAccess(_X)
if mibBuilder.loadTexts:ospfPacketSrc.setStatus(_C)
_OspfTraps_ObjectIdentity=ObjectIdentity
ospfTraps=_OspfTraps_ObjectIdentity((1,3,6,1,2,1,14,16,2))
_OspfTrapConformance_ObjectIdentity=ObjectIdentity
ospfTrapConformance=_OspfTrapConformance_ObjectIdentity((1,3,6,1,2,1,14,16,3))
_OspfTrapGroups_ObjectIdentity=ObjectIdentity
ospfTrapGroups=_OspfTrapGroups_ObjectIdentity((1,3,6,1,2,1,14,16,3,1))
_OspfTrapCompliances_ObjectIdentity=ObjectIdentity
ospfTrapCompliances=_OspfTrapCompliances_ObjectIdentity((1,3,6,1,2,1,14,16,3,2))
ospfTrapControlGroup=ObjectGroup((1,3,6,1,2,1,14,16,3,1,1))
ospfTrapControlGroup.setObjects(*((_B,_o),(_B,_J),(_B,_E),(_B,_N)))
if mibBuilder.loadTexts:ospfTrapControlGroup.setStatus(_C)
ospfVirtIfStateChange=NotificationType((1,3,6,1,2,1,14,16,2,1))
ospfVirtIfStateChange.setObjects(*((_A,_D),(_A,_H),(_A,_I),(_A,_j)))
if mibBuilder.loadTexts:ospfVirtIfStateChange.setStatus(_C)
ospfNbrStateChange=NotificationType((1,3,6,1,2,1,14,16,2,2))
ospfNbrStateChange.setObjects(*((_A,_D),(_A,_T),(_A,_S),(_A,_O),(_A,_f)))
if mibBuilder.loadTexts:ospfNbrStateChange.setStatus(_C)
ospfVirtNbrStateChange=NotificationType((1,3,6,1,2,1,14,16,2,3))
ospfVirtNbrStateChange.setObjects(*((_A,_D),(_A,_U),(_A,_V),(_A,_n)))
if mibBuilder.loadTexts:ospfVirtNbrStateChange.setStatus(_C)
ospfIfConfigError=NotificationType((1,3,6,1,2,1,14,16,2,4))
ospfIfConfigError.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_B,_N),(_B,_J),(_B,_E)))
if mibBuilder.loadTexts:ospfIfConfigError.setStatus(_C)
ospfVirtIfConfigError=NotificationType((1,3,6,1,2,1,14,16,2,5))
ospfVirtIfConfigError.setObjects(*((_A,_D),(_A,_H),(_A,_I),(_B,_J),(_B,_E)))
if mibBuilder.loadTexts:ospfVirtIfConfigError.setStatus(_C)
ospfIfAuthFailure=NotificationType((1,3,6,1,2,1,14,16,2,6))
ospfIfAuthFailure.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_B,_N),(_B,_J),(_B,_E)))
if mibBuilder.loadTexts:ospfIfAuthFailure.setStatus(_C)
ospfVirtIfAuthFailure=NotificationType((1,3,6,1,2,1,14,16,2,7))
ospfVirtIfAuthFailure.setObjects(*((_A,_D),(_A,_H),(_A,_I),(_B,_J),(_B,_E)))
if mibBuilder.loadTexts:ospfVirtIfAuthFailure.setStatus(_C)
ospfIfRxBadPacket=NotificationType((1,3,6,1,2,1,14,16,2,8))
ospfIfRxBadPacket.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_B,_N),(_B,_E)))
if mibBuilder.loadTexts:ospfIfRxBadPacket.setStatus(_C)
ospfVirtIfRxBadPacket=NotificationType((1,3,6,1,2,1,14,16,2,9))
ospfVirtIfRxBadPacket.setObjects(*((_A,_D),(_A,_H),(_A,_I),(_B,_E)))
if mibBuilder.loadTexts:ospfVirtIfRxBadPacket.setStatus(_C)
ospfTxRetransmit=NotificationType((1,3,6,1,2,1,14,16,2,10))
ospfTxRetransmit.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_O),(_B,_E),(_A,_M),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ospfTxRetransmit.setStatus(_C)
ospfVirtIfTxRetransmit=NotificationType((1,3,6,1,2,1,14,16,2,11))
ospfVirtIfTxRetransmit.setObjects(*((_A,_D),(_A,_H),(_A,_I),(_B,_E),(_A,_M),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ospfVirtIfTxRetransmit.setStatus(_C)
ospfOriginateLsa=NotificationType((1,3,6,1,2,1,14,16,2,12))
ospfOriginateLsa.setObjects(*((_A,_D),(_A,_R),(_A,_M),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ospfOriginateLsa.setStatus(_C)
ospfMaxAgeLsa=NotificationType((1,3,6,1,2,1,14,16,2,13))
ospfMaxAgeLsa.setObjects(*((_A,_D),(_A,_R),(_A,_M),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ospfMaxAgeLsa.setStatus(_C)
ospfLsdbOverflow=NotificationType((1,3,6,1,2,1,14,16,2,14))
ospfLsdbOverflow.setObjects(*((_A,_D),(_A,_Q)))
if mibBuilder.loadTexts:ospfLsdbOverflow.setStatus(_C)
ospfLsdbApproachingOverflow=NotificationType((1,3,6,1,2,1,14,16,2,15))
ospfLsdbApproachingOverflow.setObjects(*((_A,_D),(_A,_Q)))
if mibBuilder.loadTexts:ospfLsdbApproachingOverflow.setStatus(_C)
ospfIfStateChange=NotificationType((1,3,6,1,2,1,14,16,2,16))
ospfIfStateChange.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_b)))
if mibBuilder.loadTexts:ospfIfStateChange.setStatus(_C)
ospfNssaTranslatorStatusChange=NotificationType((1,3,6,1,2,1,14,16,2,17))
ospfNssaTranslatorStatusChange.setObjects(*((_A,_D),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ospfNssaTranslatorStatusChange.setStatus(_C)
ospfRestartStatusChange=NotificationType((1,3,6,1,2,1,14,16,2,18))
ospfRestartStatusChange.setObjects(*((_A,_D),(_A,_i),(_A,_h),(_A,_g)))
if mibBuilder.loadTexts:ospfRestartStatusChange.setStatus(_C)
ospfNbrRestartHelperStatusChange=NotificationType((1,3,6,1,2,1,14,16,2,19))
ospfNbrRestartHelperStatusChange.setObjects(*((_A,_D),(_A,_T),(_A,_S),(_A,_O),(_A,_e),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ospfNbrRestartHelperStatusChange.setStatus(_C)
ospfVirtNbrRestartHelperStatusChange=NotificationType((1,3,6,1,2,1,14,16,2,20))
ospfVirtNbrRestartHelperStatusChange.setObjects(*((_A,_D),(_A,_U),(_A,_V),(_A,_m),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ospfVirtNbrRestartHelperStatusChange.setStatus(_C)
ospfTrapEventGroup=NotificationGroup((1,3,6,1,2,1,14,16,3,1,2))
ospfTrapEventGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ospfTrapEventGroup.setStatus(_C)
ospfTrapCompliance=ModuleCompliance((1,3,6,1,2,1,14,16,3,2,1))
ospfTrapCompliance.setObjects(*((_B,_P),(_B,_P)))
if mibBuilder.loadTexts:ospfTrapCompliance.setStatus('obsolete')
ospfTrapCompliance2=ModuleCompliance((1,3,6,1,2,1,14,16,3,2,2))
ospfTrapCompliance2.setObjects(*((_B,_P),(_B,_A9)))
if mibBuilder.loadTexts:ospfTrapCompliance2.setStatus(_C)
mibBuilder.exportSymbols(_B,**{'ospfTrap':ospfTrap,'ospfTrapControl':ospfTrapControl,_o:ospfSetTrap,_J:ospfConfigErrorType,_E:ospfPacketType,_N:ospfPacketSrc,'ospfTraps':ospfTraps,_p:ospfVirtIfStateChange,_q:ospfNbrStateChange,_r:ospfVirtNbrStateChange,_s:ospfIfConfigError,_t:ospfVirtIfConfigError,_u:ospfIfAuthFailure,_v:ospfVirtIfAuthFailure,_w:ospfIfRxBadPacket,_x:ospfVirtIfRxBadPacket,_y:ospfTxRetransmit,_z:ospfVirtIfTxRetransmit,_A0:ospfOriginateLsa,_A1:ospfMaxAgeLsa,_A2:ospfLsdbOverflow,_A3:ospfLsdbApproachingOverflow,_A4:ospfIfStateChange,_A5:ospfNssaTranslatorStatusChange,_A6:ospfRestartStatusChange,_A7:ospfNbrRestartHelperStatusChange,_A8:ospfVirtNbrRestartHelperStatusChange,'ospfTrapConformance':ospfTrapConformance,'ospfTrapGroups':ospfTrapGroups,_P:ospfTrapControlGroup,_A9:ospfTrapEventGroup,'ospfTrapCompliances':ospfTrapCompliances,'ospfTrapCompliance':ospfTrapCompliance,'ospfTrapCompliance2':ospfTrapCompliance2})