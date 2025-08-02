_A2='ciscoOspfTrapEventGroupRev1'
_A1='ciscoOspfTrapEventGroup'
_A0='cospfShamLinkTxRetransmit'
_z='cospfShamLinkRxBadPacket'
_y='cospfShamLinkAuthFailure'
_x='cospfShamLinkConfigError'
_w='cospfShamLinkNbrStateChange'
_v='cospfShamLinksStateChange'
_u='cospfShamLinkStateChange'
_t='cospfSetTrap'
_s='ospfNbrRtrId'
_r='ospfAreaId'
_q='cospfShamLinksState'
_p='cospfShamLinkState'
_o='cospfShamLinkNeighborId'
_n='cospfShamLinkNbrState'
_m='cospfShamLinkNbrRtrId'
_l='cospfShamLinkNbrIpAddrType'
_k='cospfShamLinkNbrIpAddr'
_j='cospfShamLinkNbrArea'
_i='cospfShamLinkLocalIpAddress'
_h='cospfShamLinkAreaId'
_g='cospfAreaNssaTranslatorState'
_f='ciscoOspfTrapControlGroup'
_e='cospfNssaTranslatorStatusChange'
_d='cospfMaxAgeLsa'
_c='cospfOriginateLsa'
_b='cospfVirtIfTxRetransmit'
_a='cospfTxRetransmit'
_Z='cospfVirtIfConfigError'
_Y='cospfIfConfigError'
_X='deprecated'
_W='cospfPacketSrc'
_V='read-only'
_U='Integer32'
_T='ospfVirtIfNeighbor'
_S='ospfVirtIfAreaId'
_R='ospfLsdbAreaId'
_Q='ospfIfIpAddress'
_P='ospfAddressLessIf'
_O='cospfConfigErrorType'
_N='ospfLsdbRouterId'
_M='ospfLsdbLsid'
_L='cospfShamLinksRemoteIpAddrType'
_K='cospfShamLinksRemoteIpAddr'
_J='cospfShamLinksAreaId'
_I='cospfShamLinksLocalIpAddrType'
_H='cospfShamLinksLocalIpAddr'
_G='cospfLsdbType'
_F='cospfPacketType'
_E='ospfRouterId'
_D='current'
_C='OSPF-MIB'
_B='CISCO-OSPF-TRAP-MIB'
_A='CISCO-OSPF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cospfAreaNssaTranslatorState,cospfLsdbType,cospfShamLinkAreaId,cospfShamLinkLocalIpAddress,cospfShamLinkNbrArea,cospfShamLinkNbrIpAddr,cospfShamLinkNbrIpAddrType,cospfShamLinkNbrRtrId,cospfShamLinkNbrState,cospfShamLinkNeighborId,cospfShamLinkState,cospfShamLinksAreaId,cospfShamLinksLocalIpAddr,cospfShamLinksLocalIpAddrType,cospfShamLinksRemoteIpAddr,cospfShamLinksRemoteIpAddrType,cospfShamLinksState=mibBuilder.importSymbols(_A,_g,_G,_h,_i,_j,_k,_l,_m,_n,_o,_p,_J,_H,_I,_K,_L,_q)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ospfAddressLessIf,ospfAreaId,ospfIfIpAddress,ospfLsdbAreaId,ospfLsdbLsid,ospfLsdbRouterId,ospfNbrRtrId,ospfRouterId,ospfVirtIfAreaId,ospfVirtIfNeighbor=mibBuilder.importSymbols(_C,_P,_r,_Q,_R,_M,_N,_s,_E,_S,_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_U,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoOspfTrapMIB=ModuleIdentity((1,3,6,1,4,1,9,10,101))
if mibBuilder.loadTexts:ciscoOspfTrapMIB.setRevisions(('2003-07-18 00:00','2003-02-27 00:00'))
_CiscoOspfTrapMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoOspfTrapMIBNotifs=_CiscoOspfTrapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,101,0))
_CiscoOspfTrapMIBObjects_ObjectIdentity=ObjectIdentity
ciscoOspfTrapMIBObjects=_CiscoOspfTrapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,101,1))
_CospfTrapControl_ObjectIdentity=ObjectIdentity
cospfTrapControl=_CospfTrapControl_ObjectIdentity((1,3,6,1,4,1,9,10,101,1,1))
class _CospfSetTrap_Type(Bits):namedValues=NamedValues(*(('ifConfigError',0),('virtIfConfigError',1),('retransmit',2),('virtRetransmit',3),('originateLsa',4),('originateMaxAgeLsa',5),('nssaTranslatorStatusChange',6),('shamLinkStateChange',7),('shamLinkNbrStateChange',8),('shamLinkConfigError',9),('shamLinkAuthFailure',10),('shamLinkRxBadPacket',11),('shamLinkTxRetransmit',12),('shamLinksStateChange',13)))
_CospfSetTrap_Type.__name__='Bits'
_CospfSetTrap_Object=MibScalar
cospfSetTrap=_CospfSetTrap_Object((1,3,6,1,4,1,9,10,101,1,1,1),_CospfSetTrap_Type())
cospfSetTrap.setMaxAccess('read-write')
if mibBuilder.loadTexts:cospfSetTrap.setStatus(_D)
class _CospfConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('badVersion',1),('areaMismatch',2),('unknownNbmaNbr',3),('unknownVirtualNbr',4),('authTypeMismatch',5),('authFailure',6),('netMaskMismatch',7),('helloIntervalMismatch',8),('deadIntervalMismatch',9),('optionMismatch',10),('mtuMismatch',11),('noError',12),('unknownShamLinkNbr',13)))
_CospfConfigErrorType_Type.__name__=_U
_CospfConfigErrorType_Object=MibScalar
cospfConfigErrorType=_CospfConfigErrorType_Object((1,3,6,1,4,1,9,10,101,1,1,2),_CospfConfigErrorType_Type())
cospfConfigErrorType.setMaxAccess(_V)
if mibBuilder.loadTexts:cospfConfigErrorType.setStatus(_D)
class _CospfPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('hello',1),('dbDescript',2),('lsReq',3),('lsUpdate',4),('lsAck',5),('nullPacket',6)))
_CospfPacketType_Type.__name__=_U
_CospfPacketType_Object=MibScalar
cospfPacketType=_CospfPacketType_Object((1,3,6,1,4,1,9,10,101,1,1,3),_CospfPacketType_Type())
cospfPacketType.setMaxAccess(_V)
if mibBuilder.loadTexts:cospfPacketType.setStatus(_D)
_CospfPacketSrc_Type=IpAddress
_CospfPacketSrc_Object=MibScalar
cospfPacketSrc=_CospfPacketSrc_Object((1,3,6,1,4,1,9,10,101,1,1,4),_CospfPacketSrc_Type())
cospfPacketSrc.setMaxAccess(_V)
if mibBuilder.loadTexts:cospfPacketSrc.setStatus(_D)
_CiscoOspfTrapMIBConform_ObjectIdentity=ObjectIdentity
ciscoOspfTrapMIBConform=_CiscoOspfTrapMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,101,2))
_CiscoOspfTrapMIBGroups_ObjectIdentity=ObjectIdentity
ciscoOspfTrapMIBGroups=_CiscoOspfTrapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,101,2,1))
_CiscoOspfTrapMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoOspfTrapMIBCompliances=_CiscoOspfTrapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,101,2,2))
ciscoOspfTrapControlGroup=ObjectGroup((1,3,6,1,4,1,9,10,101,2,1,2))
ciscoOspfTrapControlGroup.setObjects(*((_B,_t),(_B,_O),(_B,_F),(_B,_W)))
if mibBuilder.loadTexts:ciscoOspfTrapControlGroup.setStatus(_D)
cospfIfConfigError=NotificationType((1,3,6,1,4,1,9,10,101,0,1))
cospfIfConfigError.setObjects(*((_C,_E),(_C,_Q),(_C,_P),(_B,_W),(_B,_O),(_B,_F)))
if mibBuilder.loadTexts:cospfIfConfigError.setStatus(_D)
cospfVirtIfConfigError=NotificationType((1,3,6,1,4,1,9,10,101,0,2))
cospfVirtIfConfigError.setObjects(*((_C,_E),(_C,_S),(_C,_T),(_B,_O),(_B,_F)))
if mibBuilder.loadTexts:cospfVirtIfConfigError.setStatus(_D)
cospfTxRetransmit=NotificationType((1,3,6,1,4,1,9,10,101,0,3))
cospfTxRetransmit.setObjects(*((_C,_E),(_C,_Q),(_C,_P),(_C,_s),(_B,_F),(_A,_G),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:cospfTxRetransmit.setStatus(_D)
cospfVirtIfTxRetransmit=NotificationType((1,3,6,1,4,1,9,10,101,0,4))
cospfVirtIfTxRetransmit.setObjects(*((_C,_E),(_C,_S),(_C,_T),(_B,_F),(_A,_G),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:cospfVirtIfTxRetransmit.setStatus(_D)
cospfOriginateLsa=NotificationType((1,3,6,1,4,1,9,10,101,0,5))
cospfOriginateLsa.setObjects(*((_C,_E),(_C,_R),(_A,_G),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:cospfOriginateLsa.setStatus(_D)
cospfMaxAgeLsa=NotificationType((1,3,6,1,4,1,9,10,101,0,6))
cospfMaxAgeLsa.setObjects(*((_C,_E),(_C,_R),(_A,_G),(_C,_M),(_A,_G),(_C,_N)))
if mibBuilder.loadTexts:cospfMaxAgeLsa.setStatus(_D)
cospfNssaTranslatorStatusChange=NotificationType((1,3,6,1,4,1,9,10,101,0,7))
cospfNssaTranslatorStatusChange.setObjects(*((_C,_E),(_C,_r),(_A,_g)))
if mibBuilder.loadTexts:cospfNssaTranslatorStatusChange.setStatus(_D)
cospfShamLinkStateChange=NotificationType((1,3,6,1,4,1,9,10,101,0,8))
cospfShamLinkStateChange.setObjects(*((_C,_E),(_A,_h),(_A,_i),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:cospfShamLinkStateChange.setStatus(_X)
cospfShamLinkNbrStateChange=NotificationType((1,3,6,1,4,1,9,10,101,0,9))
cospfShamLinkNbrStateChange.setObjects(*((_C,_E),(_A,_j),(_A,_I),(_A,_H),(_A,_l),(_A,_k),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cospfShamLinkNbrStateChange.setStatus(_D)
cospfShamLinkConfigError=NotificationType((1,3,6,1,4,1,9,10,101,0,10))
cospfShamLinkConfigError.setObjects(*((_C,_E),(_A,_J),(_A,_I),(_A,_H),(_A,_L),(_A,_K),(_B,_O),(_B,_F)))
if mibBuilder.loadTexts:cospfShamLinkConfigError.setStatus(_D)
cospfShamLinkAuthFailure=NotificationType((1,3,6,1,4,1,9,10,101,0,11))
cospfShamLinkAuthFailure.setObjects(*((_C,_E),(_A,_J),(_A,_I),(_A,_H),(_A,_L),(_A,_K),(_B,_O),(_B,_F)))
if mibBuilder.loadTexts:cospfShamLinkAuthFailure.setStatus(_D)
cospfShamLinkRxBadPacket=NotificationType((1,3,6,1,4,1,9,10,101,0,12))
cospfShamLinkRxBadPacket.setObjects(*((_C,_E),(_A,_J),(_A,_I),(_A,_H),(_A,_L),(_A,_K),(_B,_F)))
if mibBuilder.loadTexts:cospfShamLinkRxBadPacket.setStatus(_D)
cospfShamLinkTxRetransmit=NotificationType((1,3,6,1,4,1,9,10,101,0,13))
cospfShamLinkTxRetransmit.setObjects(*((_C,_E),(_A,_J),(_A,_I),(_A,_H),(_A,_L),(_A,_K),(_B,_F),(_A,_G),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:cospfShamLinkTxRetransmit.setStatus(_D)
cospfShamLinksStateChange=NotificationType((1,3,6,1,4,1,9,10,101,0,14))
cospfShamLinksStateChange.setObjects(*((_C,_E),(_A,_J),(_A,_I),(_A,_H),(_A,_L),(_A,_K),(_A,_q)))
if mibBuilder.loadTexts:cospfShamLinksStateChange.setStatus(_D)
ciscoOspfTrapEventGroup=NotificationGroup((1,3,6,1,4,1,9,10,101,2,1,1))
ciscoOspfTrapEventGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_u)))
if mibBuilder.loadTexts:ciscoOspfTrapEventGroup.setStatus(_X)
ciscoOspfTrapEventGroupRev1=NotificationGroup((1,3,6,1,4,1,9,10,101,2,1,3))
ciscoOspfTrapEventGroupRev1.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ciscoOspfTrapEventGroupRev1.setStatus(_D)
ciscoOspfTrapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,101,2,2,1))
ciscoOspfTrapMIBCompliance.setObjects(*((_B,_A1),(_B,_f)))
if mibBuilder.loadTexts:ciscoOspfTrapMIBCompliance.setStatus(_X)
ciscoOspfTrapMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,101,2,2,2))
ciscoOspfTrapMIBComplianceRev1.setObjects(*((_B,_A2),(_B,_f)))
if mibBuilder.loadTexts:ciscoOspfTrapMIBComplianceRev1.setStatus(_D)
mibBuilder.exportSymbols(_B,**{'ciscoOspfTrapMIB':ciscoOspfTrapMIB,'ciscoOspfTrapMIBNotifs':ciscoOspfTrapMIBNotifs,_Y:cospfIfConfigError,_Z:cospfVirtIfConfigError,_a:cospfTxRetransmit,_b:cospfVirtIfTxRetransmit,_c:cospfOriginateLsa,_d:cospfMaxAgeLsa,_e:cospfNssaTranslatorStatusChange,_u:cospfShamLinkStateChange,_w:cospfShamLinkNbrStateChange,_x:cospfShamLinkConfigError,_y:cospfShamLinkAuthFailure,_z:cospfShamLinkRxBadPacket,_A0:cospfShamLinkTxRetransmit,_v:cospfShamLinksStateChange,'ciscoOspfTrapMIBObjects':ciscoOspfTrapMIBObjects,'cospfTrapControl':cospfTrapControl,_t:cospfSetTrap,_O:cospfConfigErrorType,_F:cospfPacketType,_W:cospfPacketSrc,'ciscoOspfTrapMIBConform':ciscoOspfTrapMIBConform,'ciscoOspfTrapMIBGroups':ciscoOspfTrapMIBGroups,_A1:ciscoOspfTrapEventGroup,_f:ciscoOspfTrapControlGroup,_A2:ciscoOspfTrapEventGroupRev1,'ciscoOspfTrapMIBCompliances':ciscoOspfTrapMIBCompliances,'ciscoOspfTrapMIBCompliance':ciscoOspfTrapMIBCompliance,'ciscoOspfTrapMIBComplianceRev1':ciscoOspfTrapMIBComplianceRev1})