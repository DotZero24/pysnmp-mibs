_B7='sleDebugRipStatusChanged'
_B6='sleDebugPimStatusChanged'
_B5='sleDebugOspfStatusChanged'
_B4='sleDebugBgpStatusChanged'
_B3='sleDebugNsmMcastStatusChanged'
_B2='sleDebugNsmStatusChanged'
_B1='sleDebugIgmpSnoopStatusChanged'
_B0='sleDebugIgmpStatusChanged'
_A_='sleDebugDhcpStatusChanged'
_Az='sleDebugControlRipStatus'
_Ay='sleDebugControlPimStatus'
_Ax='sleDebugControlOspfStatus'
_Aw='sleDebugControlBgpStatus'
_Av='sleDebugControlNsmMcastStatus'
_Au='sleDebugControlNsmStatus'
_At='sleDebugControlIgmpSnoopStatus'
_As='sleDebugControlIgmpStatus'
_Ar='sleDebugControlDhcpStatus'
_Aq='sleDebugControlTimer'
_Ap='sleDebugControlStatus'
_Ao='debugTimerRegister'
_An='debugTimerJoinprunePpt'
_Am='debugTimerJoinpruneOt'
_Al='debugTimerJoinpruneKat'
_Ak='debugTimerJoinpruneJt'
_Aj='debugTimerJoinpruneEt'
_Ai='debugTimerJoinprune'
_Ah='debugTimerHelloTht'
_Ag='debugTimerHelloNlt'
_Af='debugTimerHelloHt'
_Ae='debugTimerHello'
_Ad='debugTimerBsrCrp'
_Ac='debugTimerBsrBst'
_Ab='debugTimerBsr'
_Aa='debugTimerAssertAt'
_AZ='debugState'
_AY='debugPacketOut'
_AX='debugPacketIn'
_AW='debugNexthop'
_AV='debugEvent'
_AU='debugPacketLsUpdateSend'
_AT='debugPacketLsUpdateRecv'
_AS='debugPacketLsUpdateDetail'
_AR='debugPacketLsRequestSend'
_AQ='debugPacketLsRequestRecv'
_AP='debugPacketLsRequestDetail'
_AO='debugPacketLsAckSend'
_AN='debugPacketLsAckRecv'
_AM='debugPacketLsAckDetail'
_AL='debugPacketHelloSend'
_AK='debugPacketHelloRecv'
_AJ='debugPacketHelloDetail'
_AI='debugPacketDDSend'
_AH='debugPacketDDRecv'
_AG='debugPacketDDDetail'
_AF='debugRouteSpf'
_AE='debugRouteInstall'
_AD='debugRouteIa'
_AC='debugRouteAse'
_AB='debugNsmRedistribute'
_AA='debugNsmInterface'
_A9='debugNfsmTimers'
_A8='debugNfsmStatus'
_A7='debugNfsmEvents'
_A6='debugLsaRefrash'
_A5='debugLsaMaxage'
_A4='debugLsaInstall'
_A3='debugLsaGenerate'
_A2='debugLsaFlooding'
_A1='debugIfsmTimers'
_A0='debugIfsmStatus'
_z='debugIfsmEvent'
_y='debugEventVlink'
_x='debugEventRouter'
_w='debugEventOs'
_v='debugEventNssa'
_u='debugEventLsa'
_t='debugEventAsbr'
_s='debugEventAbr'
_r='debugUpdatesOut'
_q='debugUpdatesIn'
_p='debugKeepalives'
_o='debugFilters'
_n='debugDampening'
_m='debugNormal'
_l='debugMcastVif'
_k='debugMcastStats'
_j='debugMcastRegister'
_i='debugMcastMrt'
_h='debugMcastFibMsg'
_g='debugKernel'
_f='debugTcn'
_e='debugTib'
_d='debugEncode'
_c='debugDecode'
_b='debugServices'
_a='debugPacket'
_Z='debugLease'
_Y='debugFilter'
_X='Integer32'
_W='sleDebugRipStatus'
_V='sleDebugPimStatus'
_U='sleDebugOspfStatus'
_T='sleDebugBgpStatus'
_S='sleDebugNsmMcastStatus'
_R='sleDebugNsmStatus'
_Q='sleDebugIgmpSnoopStatus'
_P='sleDebugIgmpStatus'
_O='sleDebugDhcpStatus'
_N='debugPacketSend'
_M='debugPacketRecv'
_L='debugPacketDetail'
_K='debugFsm'
_J='debugNsm'
_I='debugEvents'
_H='sleDebugControlReqResult'
_G='sleDebugControlTimeStamp'
_F='sleDebugControlRequest'
_E='read-write'
_D='read-only'
_C='Bits'
_B='current'
_A='SLE-DEBUG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_C,_C,'Counter32','Counter64','Gauge32',_X,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleDebug=ModuleIdentity((1,3,6,1,4,1,6296,101,99))
class OwnerString(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SleDebugBase_ObjectIdentity=ObjectIdentity
sleDebugBase=_SleDebugBase_ObjectIdentity((1,3,6,1,4,1,6296,101,99,1))
_SleDebugStatus_ObjectIdentity=ObjectIdentity
sleDebugStatus=_SleDebugStatus_ObjectIdentity((1,3,6,1,4,1,6296,101,99,1,1))
class _SleDebugDhcpStatus_Type(Bits):namedValues=NamedValues(*((_Y,0),(_Z,1),(_a,2),(_b,3)))
_SleDebugDhcpStatus_Type.__name__=_C
_SleDebugDhcpStatus_Object=MibScalar
sleDebugDhcpStatus=_SleDebugDhcpStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,1),_SleDebugDhcpStatus_Type())
sleDebugDhcpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugDhcpStatus.setStatus(_B)
class _SleDebugIgmpStatus_Type(Bits):namedValues=NamedValues(*((_c,0),(_d,1),(_I,2),(_K,3),(_e,4)))
_SleDebugIgmpStatus_Type.__name__=_C
_SleDebugIgmpStatus_Object=MibScalar
sleDebugIgmpStatus=_SleDebugIgmpStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,2),_SleDebugIgmpStatus_Type())
sleDebugIgmpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugIgmpStatus.setStatus(_B)
class _SleDebugIgmpSnoopStatus_Type(Bits):namedValues=NamedValues((_f,0))
_SleDebugIgmpSnoopStatus_Type.__name__=_C
_SleDebugIgmpSnoopStatus_Object=MibScalar
sleDebugIgmpSnoopStatus=_SleDebugIgmpSnoopStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,3),_SleDebugIgmpSnoopStatus_Type())
sleDebugIgmpSnoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugIgmpSnoopStatus.setStatus(_B)
class _SleDebugNsmStatus_Type(Bits):namedValues=NamedValues(*((_I,0),(_g,1),(_L,2),(_M,3),(_N,4)))
_SleDebugNsmStatus_Type.__name__=_C
_SleDebugNsmStatus_Object=MibScalar
sleDebugNsmStatus=_SleDebugNsmStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,4),_SleDebugNsmStatus_Type())
sleDebugNsmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugNsmStatus.setStatus(_B)
class _SleDebugNsmMcastStatus_Type(Bits):namedValues=NamedValues(*((_h,0),(_i,1),(_j,2),(_k,3),(_l,4)))
_SleDebugNsmMcastStatus_Type.__name__=_C
_SleDebugNsmMcastStatus_Object=MibScalar
sleDebugNsmMcastStatus=_SleDebugNsmMcastStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,5),_SleDebugNsmMcastStatus_Type())
sleDebugNsmMcastStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugNsmMcastStatus.setStatus(_B)
class _SleDebugBgpStatus_Type(Bits):namedValues=NamedValues(*((_m,0),(_n,1),(_I,2),(_o,3),(_K,4),(_p,5),(_J,6),(_q,7),(_r,8)))
_SleDebugBgpStatus_Type.__name__=_C
_SleDebugBgpStatus_Object=MibScalar
sleDebugBgpStatus=_SleDebugBgpStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,6),_SleDebugBgpStatus_Type())
sleDebugBgpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugBgpStatus.setStatus(_B)
class _SleDebugOspfStatus_Type(Bits):namedValues=NamedValues(*((_s,0),(_t,1),(_u,2),(_v,3),(_w,4),(_x,5),(_y,6),(_z,7),(_A0,8),(_A1,9),(_A2,10),(_A3,11),(_A4,12),(_A5,13),(_A6,14),(_A7,15),(_A8,16),(_A9,17),(_AA,18),(_AB,19),(_AC,20),(_AD,21),(_AE,22),(_AF,23),(_AG,24),(_AH,25),(_AI,26),(_AJ,27),(_AK,28),(_AL,29),(_AM,30),(_AN,31),(_AO,32),(_AP,33),(_AQ,34),(_AR,35),(_AS,36),(_AT,37),(_AU,38)))
_SleDebugOspfStatus_Type.__name__=_C
_SleDebugOspfStatus_Object=MibScalar
sleDebugOspfStatus=_SleDebugOspfStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,7),_SleDebugOspfStatus_Type())
sleDebugOspfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugOspfStatus.setStatus(_B)
class _SleDebugPimStatus_Type(Bits):namedValues=NamedValues(*((_AV,0),('debugMfc',1),('debugMib',2),(_AW,3),(_J,4),(_AX,5),(_AY,6),(_AZ,7),(_Aa,8),(_Ab,9),(_Ac,10),(_Ad,11),(_Ae,12),(_Af,13),(_Ag,14),(_Ah,15),(_Ai,16),(_Aj,17),(_Ak,18),(_Al,19),(_Am,20),(_An,21),(_Ao,22)))
_SleDebugPimStatus_Type.__name__=_C
_SleDebugPimStatus_Object=MibScalar
sleDebugPimStatus=_SleDebugPimStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,8),_SleDebugPimStatus_Type())
sleDebugPimStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugPimStatus.setStatus(_B)
class _SleDebugRipStatus_Type(Bits):namedValues=NamedValues(*((_I,0),(_J,1),(_L,2),(_M,3),(_N,4)))
_SleDebugRipStatus_Type.__name__=_C
_SleDebugRipStatus_Object=MibScalar
sleDebugRipStatus=_SleDebugRipStatus_Object((1,3,6,1,4,1,6296,101,99,1,1,9),_SleDebugRipStatus_Type())
sleDebugRipStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugRipStatus.setStatus(_B)
_SleDebugStatusControl_ObjectIdentity=ObjectIdentity
sleDebugStatusControl=_SleDebugStatusControl_ObjectIdentity((1,3,6,1,4,1,6296,101,99,1,2))
class _SleDebugControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('setDhcpDebugStatus',1),('setIgmpDebugStatus',2),('setIgmpSnoopDebugStats',3),('setNsmDebugStatus',4),('setNsmMcastDebugStatus',5),('setBgpDebugStatus',6),('setOspfDebugStatus',7),('setPimDebugStatus',8),('setRipDebugStatus',9)))
_SleDebugControlRequest_Type.__name__=_X
_SleDebugControlRequest_Object=MibScalar
sleDebugControlRequest=_SleDebugControlRequest_Object((1,3,6,1,4,1,6296,101,99,1,2,1),_SleDebugControlRequest_Type())
sleDebugControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlRequest.setStatus(_B)
_SleDebugControlStatus_Type=SleControlStatusType
_SleDebugControlStatus_Object=MibScalar
sleDebugControlStatus=_SleDebugControlStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,2),_SleDebugControlStatus_Type())
sleDebugControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugControlStatus.setStatus(_B)
_SleDebugControlTimer_Type=Gauge32
_SleDebugControlTimer_Object=MibScalar
sleDebugControlTimer=_SleDebugControlTimer_Object((1,3,6,1,4,1,6296,101,99,1,2,3),_SleDebugControlTimer_Type())
sleDebugControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlTimer.setStatus(_B)
_SleDebugControlTimeStamp_Type=TimeTicks
_SleDebugControlTimeStamp_Object=MibScalar
sleDebugControlTimeStamp=_SleDebugControlTimeStamp_Object((1,3,6,1,4,1,6296,101,99,1,2,4),_SleDebugControlTimeStamp_Type())
sleDebugControlTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugControlTimeStamp.setStatus(_B)
_SleDebugControlReqResult_Type=SleControlRequestResultType
_SleDebugControlReqResult_Object=MibScalar
sleDebugControlReqResult=_SleDebugControlReqResult_Object((1,3,6,1,4,1,6296,101,99,1,2,5),_SleDebugControlReqResult_Type())
sleDebugControlReqResult.setMaxAccess(_D)
if mibBuilder.loadTexts:sleDebugControlReqResult.setStatus(_B)
class _SleDebugControlDhcpStatus_Type(Bits):namedValues=NamedValues(*((_Y,0),(_Z,1),(_a,2),(_b,3)))
_SleDebugControlDhcpStatus_Type.__name__=_C
_SleDebugControlDhcpStatus_Object=MibScalar
sleDebugControlDhcpStatus=_SleDebugControlDhcpStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,6),_SleDebugControlDhcpStatus_Type())
sleDebugControlDhcpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlDhcpStatus.setStatus(_B)
class _SleDebugControlIgmpStatus_Type(Bits):namedValues=NamedValues(*((_c,0),(_d,1),(_I,2),(_K,3),(_e,4)))
_SleDebugControlIgmpStatus_Type.__name__=_C
_SleDebugControlIgmpStatus_Object=MibScalar
sleDebugControlIgmpStatus=_SleDebugControlIgmpStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,7),_SleDebugControlIgmpStatus_Type())
sleDebugControlIgmpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlIgmpStatus.setStatus(_B)
class _SleDebugControlIgmpSnoopStatus_Type(Bits):namedValues=NamedValues((_f,0))
_SleDebugControlIgmpSnoopStatus_Type.__name__=_C
_SleDebugControlIgmpSnoopStatus_Object=MibScalar
sleDebugControlIgmpSnoopStatus=_SleDebugControlIgmpSnoopStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,8),_SleDebugControlIgmpSnoopStatus_Type())
sleDebugControlIgmpSnoopStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlIgmpSnoopStatus.setStatus(_B)
class _SleDebugControlNsmStatus_Type(Bits):namedValues=NamedValues(*((_I,0),(_g,1),(_L,2),(_M,3),(_N,4)))
_SleDebugControlNsmStatus_Type.__name__=_C
_SleDebugControlNsmStatus_Object=MibScalar
sleDebugControlNsmStatus=_SleDebugControlNsmStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,9),_SleDebugControlNsmStatus_Type())
sleDebugControlNsmStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlNsmStatus.setStatus(_B)
class _SleDebugControlNsmMcastStatus_Type(Bits):namedValues=NamedValues(*((_h,0),(_i,1),(_j,2),(_k,3),(_l,4)))
_SleDebugControlNsmMcastStatus_Type.__name__=_C
_SleDebugControlNsmMcastStatus_Object=MibScalar
sleDebugControlNsmMcastStatus=_SleDebugControlNsmMcastStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,10),_SleDebugControlNsmMcastStatus_Type())
sleDebugControlNsmMcastStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlNsmMcastStatus.setStatus(_B)
class _SleDebugControlBgpStatus_Type(Bits):namedValues=NamedValues(*((_m,0),(_n,1),(_I,2),(_o,3),(_K,4),(_p,5),(_J,6),(_q,7),(_r,8)))
_SleDebugControlBgpStatus_Type.__name__=_C
_SleDebugControlBgpStatus_Object=MibScalar
sleDebugControlBgpStatus=_SleDebugControlBgpStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,11),_SleDebugControlBgpStatus_Type())
sleDebugControlBgpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlBgpStatus.setStatus(_B)
class _SleDebugControlOspfStatus_Type(Bits):namedValues=NamedValues(*((_s,0),(_t,1),(_u,2),(_v,3),(_w,4),(_x,5),(_y,6),(_z,7),(_A0,8),(_A1,9),(_A2,10),(_A3,11),(_A4,12),(_A5,13),(_A6,14),(_A7,15),(_A8,16),(_A9,17),(_AA,18),(_AB,19),(_AC,20),(_AD,21),(_AE,22),(_AF,23),(_AG,24),(_AH,25),(_AI,26),(_AJ,27),(_AK,28),(_AL,29),(_AM,30),(_AN,31),(_AO,32),(_AP,33),(_AQ,34),(_AR,35),(_AS,36),(_AT,37),(_AU,38)))
_SleDebugControlOspfStatus_Type.__name__=_C
_SleDebugControlOspfStatus_Object=MibScalar
sleDebugControlOspfStatus=_SleDebugControlOspfStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,12),_SleDebugControlOspfStatus_Type())
sleDebugControlOspfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlOspfStatus.setStatus(_B)
class _SleDebugControlPimStatus_Type(Bits):namedValues=NamedValues(*((_AV,0),('debugMfc',1),('debugMib',2),(_AW,3),(_J,4),(_AX,5),(_AY,6),(_AZ,7),(_Aa,8),(_Ab,9),(_Ac,10),(_Ad,11),(_Ae,12),(_Af,13),(_Ag,14),(_Ah,15),(_Ai,16),(_Aj,17),(_Ak,18),(_Al,19),(_Am,20),(_An,21),(_Ao,22)))
_SleDebugControlPimStatus_Type.__name__=_C
_SleDebugControlPimStatus_Object=MibScalar
sleDebugControlPimStatus=_SleDebugControlPimStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,13),_SleDebugControlPimStatus_Type())
sleDebugControlPimStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlPimStatus.setStatus(_B)
class _SleDebugControlRipStatus_Type(Bits):namedValues=NamedValues(*((_I,0),(_J,1),(_L,2),(_M,3),(_N,4)))
_SleDebugControlRipStatus_Type.__name__=_C
_SleDebugControlRipStatus_Object=MibScalar
sleDebugControlRipStatus=_SleDebugControlRipStatus_Object((1,3,6,1,4,1,6296,101,99,1,2,14),_SleDebugControlRipStatus_Type())
sleDebugControlRipStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleDebugControlRipStatus.setStatus(_B)
_SleDebugStatusNotification_ObjectIdentity=ObjectIdentity
sleDebugStatusNotification=_SleDebugStatusNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,99,1,3))
sleDebugGroup=ObjectGroup((1,3,6,1,4,1,6296,101,99,2))
sleDebugGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_F),(_A,_Ap),(_A,_Aq),(_A,_G),(_A,_H),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:sleDebugGroup.setStatus(_B)
sleDebugDhcpStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,1))
sleDebugDhcpStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_O)))
if mibBuilder.loadTexts:sleDebugDhcpStatusChanged.setStatus(_B)
sleDebugIgmpStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,2))
sleDebugIgmpStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_P)))
if mibBuilder.loadTexts:sleDebugIgmpStatusChanged.setStatus(_B)
sleDebugIgmpSnoopStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,3))
sleDebugIgmpSnoopStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_Q)))
if mibBuilder.loadTexts:sleDebugIgmpSnoopStatusChanged.setStatus(_B)
sleDebugNsmStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,4))
sleDebugNsmStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_R)))
if mibBuilder.loadTexts:sleDebugNsmStatusChanged.setStatus(_B)
sleDebugNsmMcastStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,5))
sleDebugNsmMcastStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_S)))
if mibBuilder.loadTexts:sleDebugNsmMcastStatusChanged.setStatus(_B)
sleDebugBgpStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,6))
sleDebugBgpStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_T)))
if mibBuilder.loadTexts:sleDebugBgpStatusChanged.setStatus(_B)
sleDebugOspfStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,7))
sleDebugOspfStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_U)))
if mibBuilder.loadTexts:sleDebugOspfStatusChanged.setStatus(_B)
sleDebugPimStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,8))
sleDebugPimStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_V)))
if mibBuilder.loadTexts:sleDebugPimStatusChanged.setStatus(_B)
sleDebugRipStatusChanged=NotificationType((1,3,6,1,4,1,6296,101,99,1,3,9))
sleDebugRipStatusChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_W)))
if mibBuilder.loadTexts:sleDebugRipStatusChanged.setStatus(_B)
sleDebugNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,99,3))
sleDebugNotificationGroup.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7)))
if mibBuilder.loadTexts:sleDebugNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'OwnerString':OwnerString,'sleDebug':sleDebug,'sleDebugBase':sleDebugBase,'sleDebugStatus':sleDebugStatus,_O:sleDebugDhcpStatus,_P:sleDebugIgmpStatus,_Q:sleDebugIgmpSnoopStatus,_R:sleDebugNsmStatus,_S:sleDebugNsmMcastStatus,_T:sleDebugBgpStatus,_U:sleDebugOspfStatus,_V:sleDebugPimStatus,_W:sleDebugRipStatus,'sleDebugStatusControl':sleDebugStatusControl,_F:sleDebugControlRequest,_Ap:sleDebugControlStatus,_Aq:sleDebugControlTimer,_G:sleDebugControlTimeStamp,_H:sleDebugControlReqResult,_Ar:sleDebugControlDhcpStatus,_As:sleDebugControlIgmpStatus,_At:sleDebugControlIgmpSnoopStatus,_Au:sleDebugControlNsmStatus,_Av:sleDebugControlNsmMcastStatus,_Aw:sleDebugControlBgpStatus,_Ax:sleDebugControlOspfStatus,_Ay:sleDebugControlPimStatus,_Az:sleDebugControlRipStatus,'sleDebugStatusNotification':sleDebugStatusNotification,_A_:sleDebugDhcpStatusChanged,_B0:sleDebugIgmpStatusChanged,_B1:sleDebugIgmpSnoopStatusChanged,_B2:sleDebugNsmStatusChanged,_B3:sleDebugNsmMcastStatusChanged,_B4:sleDebugBgpStatusChanged,_B5:sleDebugOspfStatusChanged,_B6:sleDebugPimStatusChanged,_B7:sleDebugRipStatusChanged,'sleDebugGroup':sleDebugGroup,'sleDebugNotificationGroup':sleDebugNotificationGroup})