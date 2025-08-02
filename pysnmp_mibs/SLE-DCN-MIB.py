_B4='sleDcnIfGneOspfAreaChanged'
_B3='sleDcnVlanIpChanged'
_B2='sleDcnLoIpChanged'
_B1='sleDcnLoIpBaseChanged'
_B0='sleDcnRemoteIfNetworkChanged'
_A_='sleDcnRemoteLoIpChanged'
_Az='sleDcnIfNetworkChanged'
_Ay='sleDcnL2GatewayEnableChanged'
_Ax='sleDcnMgmtIpChanged'
_Aw='sleDcnNodeTypeChanged'
_Av='sleDcnIfModeChanged'
_Au='sleDcnNeUnegisterChanged'
_At='sleDcnNeRegisterChanged'
_As='sleDcnMl2gwPriorityChanged'
_Ar='sleDcnMl2gwCandidateChanged'
_Aq='sleDcnMl2gwSwitchOverChanged'
_Ap='sleDcnMgnePriorityChanged'
_Ao='sleDcnMgneCandidateChanged'
_An='sleDcnMgneSwitchOverChanged'
_Am='sleDcnIfIpBaseChanged'
_Al='sleDcnVlanIpRegisterType'
_Ak='sleDcnIfNetworkRegisterType'
_Aj='sleDcnIfNetwork'
_Ai='sleDcnLoIpRegisterType'
_Ah='sleDcnNearMacAddress'
_Ag='sleDcnL2GatewayIp'
_Af='sleDcnIfGneOspfArea'
_Ae='sleNeDcnOspfArea'
_Ad='sleDcnVlanIp'
_Ac='sleDcnLoIp'
_Ab='sleDcnLoIpBasePrefixlen'
_Aa='sleDcnLoIpBase'
_AZ='sleDcnNeType'
_AY='sleDcnGneState'
_AX='sleDcnNearIfFail'
_AW='sleDcnVlanIpPrefixlen'
_AV='sleDcnMgmtIpPrefixlen'
_AU='sleDcnMgmtIp'
_AT='sleDcnIfControlTimer'
_AS='sleDcnIfControlStatus'
_AR='sleDcnNearNodeIfName'
_AQ='sleDcnNearNodeLoIpAddr'
_AP='sleDcnGneNodeFail'
_AO='sleDcnGneLoIpAddr'
_AN='sleDcnNodeFail'
_AM='sleDcnControlTimer'
_AL='sleDcnControlStatus'
_AK='sleDcnIfCurrentIpAddress'
_AJ='sleDcnIfAllocIpAddress'
_AI='sleDcnIfDcnMode'
_AH='sleDcnIfName'
_AG='sleDcnGNeGatewayState'
_AF='sleDcnGneNodeType'
_AE='sleDcnNeControlTimer'
_AD='sleDcnNeControlStatus'
_AC='sleDcnNeNodeRegisterType'
_AB='sleDcnNeLoipRegsterType'
_AA='sleDcnNeLoIpAddr'
_A9='sleDcnMl2gwPriority'
_A8='sleDcnMl2gwCandidate'
_A7='sleDcnL2gwState'
_A6='sleDcnIfIpBasePrefixlen'
_A5='sleDcnIfIpBase'
_A4='sleDcnMgnePriority'
_A3='sleDcnMgneCandidate'
_A2='sleDcnMacAddress'
_A1='sleDcnNodeType'
_A0='sleDcnIfControlGneOspfArea'
_z='sleDcnControlDcnVlanIp'
_y='sleDcnControlDcnLoIpBasePrefixlen'
_x='sleDcnControlDcnLoIpBase'
_w='sleDcnControlL2GatewayEnable'
_v='sleDcnControlDcnVlanIpPrefixlen'
_u='sleDcnControlDcnMgmtIpPrefixlen'
_t='sleDcnControlDcnMgmtIp'
_s='sleDcnControlNodeType'
_r='sleDcnIfControlDcnMode'
_q='sleDcnControlDcnMl2gwPriority'
_p='sleDcnControlDcnMl2gwCandidate'
_o='sleDcnControlDcnMgnePriority'
_n='sleDcnControlDcnMgneCandidate'
_m='sleDcnControlDcnIfIpBasePrefixlen'
_l='sleDcnControlDcnIfIpBase'
_k='sleDcnIfIndex'
_j='sleDcnGneMacAddr'
_i='sleDcnGneMasterType'
_h='fail'
_g='normal'
_f='sleDcnNeMacAddress'
_e='master'
_d='slave'
_c='waiting'
_b='noCandidate'
_a='OctetString'
_Z='sleDcnControlDcnIfNetwork'
_Y='sleDcnControlDcnMacAddr'
_X='sleDcnControlDcnLoIp'
_W='sleDcnIfControlIfIndex'
_V='sleDcnIfControlReqResult'
_U='sleDcnIfControlTimeStamp'
_T='sleDcnIfControlRequest'
_S='sleDcnNeControlNeMacAddr'
_R='sleDcnNeControlReqResult'
_Q='sleDcnNeControlTimeStamp'
_P='sleDcnNeControlRequest'
_O='l2ne'
_N='ne'
_M='enable'
_L='disable'
_K='manual'
_J='gne'
_I='auto'
_H='read-write'
_G='sleDcnControlReqResult'
_F='sleDcnControlTimeStamp'
_E='sleDcnControlRequest'
_D='Integer32'
_C='read-only'
_B='current'
_A='SLE-DCN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_a,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleDCN=ModuleIdentity((1,3,6,1,4,1,6296,101,91))
_SleDcnNodeInfo_ObjectIdentity=ObjectIdentity
sleDcnNodeInfo=_SleDcnNodeInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,91,1))
_SleDcnNodeBaseInfo_ObjectIdentity=ObjectIdentity
sleDcnNodeBaseInfo=_SleDcnNodeBaseInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,91,1,1))
class _SleDcnNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_J,1),(_O,2)))
_SleDcnNodeType_Type.__name__=_D
_SleDcnNodeType_Object=MibScalar
sleDcnNodeType=_SleDcnNodeType_Object((1,3,6,1,4,1,6296,101,91,1,1,1),_SleDcnNodeType_Type())
sleDcnNodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNodeType.setStatus(_B)
_SleDcnMacAddress_Type=OctetString
_SleDcnMacAddress_Object=MibScalar
sleDcnMacAddress=_SleDcnMacAddress_Object((1,3,6,1,4,1,6296,101,91,1,1,2),_SleDcnMacAddress_Type())
sleDcnMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnMacAddress.setStatus(_B)
_SleDcnLoIp_Type=IpAddress
_SleDcnLoIp_Object=MibScalar
sleDcnLoIp=_SleDcnLoIp_Object((1,3,6,1,4,1,6296,101,91,1,1,3),_SleDcnLoIp_Type())
sleDcnLoIp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnLoIp.setStatus(_B)
class _SleDcnLoIpRegisterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_SleDcnLoIpRegisterType_Type.__name__=_D
_SleDcnLoIpRegisterType_Object=MibScalar
sleDcnLoIpRegisterType=_SleDcnLoIpRegisterType_Object((1,3,6,1,4,1,6296,101,91,1,1,4),_SleDcnLoIpRegisterType_Type())
sleDcnLoIpRegisterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnLoIpRegisterType.setStatus(_B)
_SleDcnIfNetwork_Type=IpAddress
_SleDcnIfNetwork_Object=MibScalar
sleDcnIfNetwork=_SleDcnIfNetwork_Object((1,3,6,1,4,1,6296,101,91,1,1,5),_SleDcnIfNetwork_Type())
sleDcnIfNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfNetwork.setStatus(_B)
class _SleDcnIfNetworkRegisterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_SleDcnIfNetworkRegisterType_Type.__name__=_D
_SleDcnIfNetworkRegisterType_Object=MibScalar
sleDcnIfNetworkRegisterType=_SleDcnIfNetworkRegisterType_Object((1,3,6,1,4,1,6296,101,91,1,1,6),_SleDcnIfNetworkRegisterType_Type())
sleDcnIfNetworkRegisterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfNetworkRegisterType.setStatus(_B)
_SleNeDcnOspfArea_Type=IpAddress
_SleNeDcnOspfArea_Object=MibScalar
sleNeDcnOspfArea=_SleNeDcnOspfArea_Object((1,3,6,1,4,1,6296,101,91,1,1,7),_SleNeDcnOspfArea_Type())
sleNeDcnOspfArea.setMaxAccess(_C)
if mibBuilder.loadTexts:sleNeDcnOspfArea.setStatus(_B)
class _SleDcnGneState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noneGne',0),(_b,1),(_c,2),(_d,3),(_e,4)))
_SleDcnGneState_Type.__name__=_D
_SleDcnGneState_Object=MibScalar
sleDcnGneState=_SleDcnGneState_Object((1,3,6,1,4,1,6296,101,91,1,1,8),_SleDcnGneState_Type())
sleDcnGneState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnGneState.setStatus(_B)
class _SleDcnMgneCandidate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleDcnMgneCandidate_Type.__name__=_D
_SleDcnMgneCandidate_Object=MibScalar
sleDcnMgneCandidate=_SleDcnMgneCandidate_Object((1,3,6,1,4,1,6296,101,91,1,1,9),_SleDcnMgneCandidate_Type())
sleDcnMgneCandidate.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnMgneCandidate.setStatus(_B)
class _SleDcnMgnePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleDcnMgnePriority_Type.__name__=_D
_SleDcnMgnePriority_Object=MibScalar
sleDcnMgnePriority=_SleDcnMgnePriority_Object((1,3,6,1,4,1,6296,101,91,1,1,10),_SleDcnMgnePriority_Type())
sleDcnMgnePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnMgnePriority.setStatus(_B)
_SleDcnLoIpBase_Type=IpAddress
_SleDcnLoIpBase_Object=MibScalar
sleDcnLoIpBase=_SleDcnLoIpBase_Object((1,3,6,1,4,1,6296,101,91,1,1,11),_SleDcnLoIpBase_Type())
sleDcnLoIpBase.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnLoIpBase.setStatus(_B)
class _SleDcnLoIpBasePrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_SleDcnLoIpBasePrefixlen_Type.__name__=_D
_SleDcnLoIpBasePrefixlen_Object=MibScalar
sleDcnLoIpBasePrefixlen=_SleDcnLoIpBasePrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,1,12),_SleDcnLoIpBasePrefixlen_Type())
sleDcnLoIpBasePrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnLoIpBasePrefixlen.setStatus(_B)
_SleDcnIfIpBase_Type=IpAddress
_SleDcnIfIpBase_Object=MibScalar
sleDcnIfIpBase=_SleDcnIfIpBase_Object((1,3,6,1,4,1,6296,101,91,1,1,13),_SleDcnIfIpBase_Type())
sleDcnIfIpBase.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfIpBase.setStatus(_B)
class _SleDcnIfIpBasePrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_SleDcnIfIpBasePrefixlen_Type.__name__=_D
_SleDcnIfIpBasePrefixlen_Object=MibScalar
sleDcnIfIpBasePrefixlen=_SleDcnIfIpBasePrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,1,14),_SleDcnIfIpBasePrefixlen_Type())
sleDcnIfIpBasePrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfIpBasePrefixlen.setStatus(_B)
class _SleDcnL2gwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noneL2gw',0),(_b,1),(_c,2),(_d,3),(_e,4)))
_SleDcnL2gwState_Type.__name__=_D
_SleDcnL2gwState_Object=MibScalar
sleDcnL2gwState=_SleDcnL2gwState_Object((1,3,6,1,4,1,6296,101,91,1,1,15),_SleDcnL2gwState_Type())
sleDcnL2gwState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnL2gwState.setStatus(_B)
class _SleDcnMl2gwCandidate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleDcnMl2gwCandidate_Type.__name__=_D
_SleDcnMl2gwCandidate_Object=MibScalar
sleDcnMl2gwCandidate=_SleDcnMl2gwCandidate_Object((1,3,6,1,4,1,6296,101,91,1,1,16),_SleDcnMl2gwCandidate_Type())
sleDcnMl2gwCandidate.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnMl2gwCandidate.setStatus(_B)
class _SleDcnMl2gwPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleDcnMl2gwPriority_Type.__name__=_D
_SleDcnMl2gwPriority_Object=MibScalar
sleDcnMl2gwPriority=_SleDcnMl2gwPriority_Object((1,3,6,1,4,1,6296,101,91,1,1,17),_SleDcnMl2gwPriority_Type())
sleDcnMl2gwPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnMl2gwPriority.setStatus(_B)
_SleDcnVlanIp_Type=IpAddress
_SleDcnVlanIp_Object=MibScalar
sleDcnVlanIp=_SleDcnVlanIp_Object((1,3,6,1,4,1,6296,101,91,1,1,18),_SleDcnVlanIp_Type())
sleDcnVlanIp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnVlanIp.setStatus(_B)
class _SleDcnVlanIpPrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_SleDcnVlanIpPrefixlen_Type.__name__=_D
_SleDcnVlanIpPrefixlen_Object=MibScalar
sleDcnVlanIpPrefixlen=_SleDcnVlanIpPrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,1,19),_SleDcnVlanIpPrefixlen_Type())
sleDcnVlanIpPrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnVlanIpPrefixlen.setStatus(_B)
class _SleDcnVlanIpRegisterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_SleDcnVlanIpRegisterType_Type.__name__=_D
_SleDcnVlanIpRegisterType_Object=MibScalar
sleDcnVlanIpRegisterType=_SleDcnVlanIpRegisterType_Object((1,3,6,1,4,1,6296,101,91,1,1,20),_SleDcnVlanIpRegisterType_Type())
sleDcnVlanIpRegisterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnVlanIpRegisterType.setStatus(_B)
_SleDcnL2GatewayIp_Type=IpAddress
_SleDcnL2GatewayIp_Object=MibScalar
sleDcnL2GatewayIp=_SleDcnL2GatewayIp_Object((1,3,6,1,4,1,6296,101,91,1,1,21),_SleDcnL2GatewayIp_Type())
sleDcnL2GatewayIp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnL2GatewayIp.setStatus(_B)
_SleDcnMgmtIp_Type=IpAddress
_SleDcnMgmtIp_Object=MibScalar
sleDcnMgmtIp=_SleDcnMgmtIp_Object((1,3,6,1,4,1,6296,101,91,1,1,22),_SleDcnMgmtIp_Type())
sleDcnMgmtIp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnMgmtIp.setStatus(_B)
class _SleDcnMgmtIpPrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_SleDcnMgmtIpPrefixlen_Type.__name__=_D
_SleDcnMgmtIpPrefixlen_Object=MibScalar
sleDcnMgmtIpPrefixlen=_SleDcnMgmtIpPrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,1,23),_SleDcnMgmtIpPrefixlen_Type())
sleDcnMgmtIpPrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnMgmtIpPrefixlen.setStatus(_B)
_SleDcnNodeBaseControl_ObjectIdentity=ObjectIdentity
sleDcnNodeBaseControl=_SleDcnNodeBaseControl_ObjectIdentity((1,3,6,1,4,1,6296,101,91,1,2))
class _SleDcnControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('setNodeType',1),('dcnLoip',2),('dcnLoIpBase',3),('dcnIfNetwork',4),('dcnIfIpBase',5),('mgneSwitchOver',6),('mgneCandidate',7),('mgnePriority',8),('l2GatewayEnable',9),('dcnVlanIp',10),('ml2gwSwitchOver',11),('ml2gwCandidate',12),('ml2gwPriority',13),('remoteLoip',14),('remoteIfNetwork',15),('mgmtIp',16)))
_SleDcnControlRequest_Type.__name__=_D
_SleDcnControlRequest_Object=MibScalar
sleDcnControlRequest=_SleDcnControlRequest_Object((1,3,6,1,4,1,6296,101,91,1,2,1),_SleDcnControlRequest_Type())
sleDcnControlRequest.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlRequest.setStatus(_B)
_SleDcnControlStatus_Type=SleControlStatusType
_SleDcnControlStatus_Object=MibScalar
sleDcnControlStatus=_SleDcnControlStatus_Object((1,3,6,1,4,1,6296,101,91,1,2,2),_SleDcnControlStatus_Type())
sleDcnControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlStatus.setStatus(_B)
_SleDcnControlTimer_Type=Gauge32
_SleDcnControlTimer_Object=MibScalar
sleDcnControlTimer=_SleDcnControlTimer_Object((1,3,6,1,4,1,6296,101,91,1,2,3),_SleDcnControlTimer_Type())
sleDcnControlTimer.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlTimer.setStatus(_B)
_SleDcnControlTimeStamp_Type=TimeTicks
_SleDcnControlTimeStamp_Object=MibScalar
sleDcnControlTimeStamp=_SleDcnControlTimeStamp_Object((1,3,6,1,4,1,6296,101,91,1,2,4),_SleDcnControlTimeStamp_Type())
sleDcnControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlTimeStamp.setStatus(_B)
_SleDcnControlReqResult_Type=SleControlRequestResultType
_SleDcnControlReqResult_Object=MibScalar
sleDcnControlReqResult=_SleDcnControlReqResult_Object((1,3,6,1,4,1,6296,101,91,1,2,5),_SleDcnControlReqResult_Type())
sleDcnControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlReqResult.setStatus(_B)
class _SleDcnControlNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_J,1),(_O,2)))
_SleDcnControlNodeType_Type.__name__=_D
_SleDcnControlNodeType_Object=MibScalar
sleDcnControlNodeType=_SleDcnControlNodeType_Object((1,3,6,1,4,1,6296,101,91,1,2,6),_SleDcnControlNodeType_Type())
sleDcnControlNodeType.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlNodeType.setStatus(_B)
_SleDcnControlDcnLoIp_Type=IpAddress
_SleDcnControlDcnLoIp_Object=MibScalar
sleDcnControlDcnLoIp=_SleDcnControlDcnLoIp_Object((1,3,6,1,4,1,6296,101,91,1,2,7),_SleDcnControlDcnLoIp_Type())
sleDcnControlDcnLoIp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnLoIp.setStatus(_B)
_SleDcnControlDcnLoIpBase_Type=IpAddress
_SleDcnControlDcnLoIpBase_Object=MibScalar
sleDcnControlDcnLoIpBase=_SleDcnControlDcnLoIpBase_Object((1,3,6,1,4,1,6296,101,91,1,2,8),_SleDcnControlDcnLoIpBase_Type())
sleDcnControlDcnLoIpBase.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnLoIpBase.setStatus(_B)
class _SleDcnControlDcnLoIpBasePrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,24))
_SleDcnControlDcnLoIpBasePrefixlen_Type.__name__=_D
_SleDcnControlDcnLoIpBasePrefixlen_Object=MibScalar
sleDcnControlDcnLoIpBasePrefixlen=_SleDcnControlDcnLoIpBasePrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,2,9),_SleDcnControlDcnLoIpBasePrefixlen_Type())
sleDcnControlDcnLoIpBasePrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnLoIpBasePrefixlen.setStatus(_B)
_SleDcnControlDcnIfIpBase_Type=IpAddress
_SleDcnControlDcnIfIpBase_Object=MibScalar
sleDcnControlDcnIfIpBase=_SleDcnControlDcnIfIpBase_Object((1,3,6,1,4,1,6296,101,91,1,2,10),_SleDcnControlDcnIfIpBase_Type())
sleDcnControlDcnIfIpBase.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnIfIpBase.setStatus(_B)
class _SleDcnControlDcnIfIpBasePrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,16))
_SleDcnControlDcnIfIpBasePrefixlen_Type.__name__=_D
_SleDcnControlDcnIfIpBasePrefixlen_Object=MibScalar
sleDcnControlDcnIfIpBasePrefixlen=_SleDcnControlDcnIfIpBasePrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,2,11),_SleDcnControlDcnIfIpBasePrefixlen_Type())
sleDcnControlDcnIfIpBasePrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnIfIpBasePrefixlen.setStatus(_B)
class _SleDcnControlDcnMgneCandidate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleDcnControlDcnMgneCandidate_Type.__name__=_D
_SleDcnControlDcnMgneCandidate_Object=MibScalar
sleDcnControlDcnMgneCandidate=_SleDcnControlDcnMgneCandidate_Object((1,3,6,1,4,1,6296,101,91,1,2,12),_SleDcnControlDcnMgneCandidate_Type())
sleDcnControlDcnMgneCandidate.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlDcnMgneCandidate.setStatus(_B)
class _SleDcnControlDcnMgnePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleDcnControlDcnMgnePriority_Type.__name__=_D
_SleDcnControlDcnMgnePriority_Object=MibScalar
sleDcnControlDcnMgnePriority=_SleDcnControlDcnMgnePriority_Object((1,3,6,1,4,1,6296,101,91,1,2,13),_SleDcnControlDcnMgnePriority_Type())
sleDcnControlDcnMgnePriority.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlDcnMgnePriority.setStatus(_B)
class _SleDcnControlL2GatewayEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleDcnControlL2GatewayEnable_Type.__name__=_D
_SleDcnControlL2GatewayEnable_Object=MibScalar
sleDcnControlL2GatewayEnable=_SleDcnControlL2GatewayEnable_Object((1,3,6,1,4,1,6296,101,91,1,2,14),_SleDcnControlL2GatewayEnable_Type())
sleDcnControlL2GatewayEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlL2GatewayEnable.setStatus(_B)
_SleDcnControlDcnVlanIp_Type=IpAddress
_SleDcnControlDcnVlanIp_Object=MibScalar
sleDcnControlDcnVlanIp=_SleDcnControlDcnVlanIp_Object((1,3,6,1,4,1,6296,101,91,1,2,15),_SleDcnControlDcnVlanIp_Type())
sleDcnControlDcnVlanIp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnVlanIp.setStatus(_B)
class _SleDcnControlDcnVlanIpPrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,24))
_SleDcnControlDcnVlanIpPrefixlen_Type.__name__=_D
_SleDcnControlDcnVlanIpPrefixlen_Object=MibScalar
sleDcnControlDcnVlanIpPrefixlen=_SleDcnControlDcnVlanIpPrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,2,16),_SleDcnControlDcnVlanIpPrefixlen_Type())
sleDcnControlDcnVlanIpPrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnVlanIpPrefixlen.setStatus(_B)
class _SleDcnControlDcnMl2gwCandidate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleDcnControlDcnMl2gwCandidate_Type.__name__=_D
_SleDcnControlDcnMl2gwCandidate_Object=MibScalar
sleDcnControlDcnMl2gwCandidate=_SleDcnControlDcnMl2gwCandidate_Object((1,3,6,1,4,1,6296,101,91,1,2,17),_SleDcnControlDcnMl2gwCandidate_Type())
sleDcnControlDcnMl2gwCandidate.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlDcnMl2gwCandidate.setStatus(_B)
class _SleDcnControlDcnMl2gwPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleDcnControlDcnMl2gwPriority_Type.__name__=_D
_SleDcnControlDcnMl2gwPriority_Object=MibScalar
sleDcnControlDcnMl2gwPriority=_SleDcnControlDcnMl2gwPriority_Object((1,3,6,1,4,1,6296,101,91,1,2,18),_SleDcnControlDcnMl2gwPriority_Type())
sleDcnControlDcnMl2gwPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnControlDcnMl2gwPriority.setStatus(_B)
_SleDcnControlDcnMacAddr_Type=OctetString
_SleDcnControlDcnMacAddr_Object=MibScalar
sleDcnControlDcnMacAddr=_SleDcnControlDcnMacAddr_Object((1,3,6,1,4,1,6296,101,91,1,2,19),_SleDcnControlDcnMacAddr_Type())
sleDcnControlDcnMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnMacAddr.setStatus(_B)
_SleDcnControlDcnIfNetwork_Type=IpAddress
_SleDcnControlDcnIfNetwork_Object=MibScalar
sleDcnControlDcnIfNetwork=_SleDcnControlDcnIfNetwork_Object((1,3,6,1,4,1,6296,101,91,1,2,20),_SleDcnControlDcnIfNetwork_Type())
sleDcnControlDcnIfNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnIfNetwork.setStatus(_B)
_SleDcnControlDcnMgmtIp_Type=IpAddress
_SleDcnControlDcnMgmtIp_Object=MibScalar
sleDcnControlDcnMgmtIp=_SleDcnControlDcnMgmtIp_Object((1,3,6,1,4,1,6296,101,91,1,2,21),_SleDcnControlDcnMgmtIp_Type())
sleDcnControlDcnMgmtIp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnMgmtIp.setStatus(_B)
class _SleDcnControlDcnMgmtIpPrefixlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_SleDcnControlDcnMgmtIpPrefixlen_Type.__name__=_D
_SleDcnControlDcnMgmtIpPrefixlen_Object=MibScalar
sleDcnControlDcnMgmtIpPrefixlen=_SleDcnControlDcnMgmtIpPrefixlen_Object((1,3,6,1,4,1,6296,101,91,1,2,22),_SleDcnControlDcnMgmtIpPrefixlen_Type())
sleDcnControlDcnMgmtIpPrefixlen.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnControlDcnMgmtIpPrefixlen.setStatus(_B)
_SleDcnNodeBaseNotification_ObjectIdentity=ObjectIdentity
sleDcnNodeBaseNotification=_SleDcnNodeBaseNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,91,1,3))
_SleDcnGneInfo_ObjectIdentity=ObjectIdentity
sleDcnGneInfo=_SleDcnGneInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,91,2))
_SleDcnNe_ObjectIdentity=ObjectIdentity
sleDcnNe=_SleDcnNe_ObjectIdentity((1,3,6,1,4,1,6296,101,91,2,1))
_SleDcnNeTable_Object=MibTable
sleDcnNeTable=_SleDcnNeTable_Object((1,3,6,1,4,1,6296,101,91,2,1,1))
if mibBuilder.loadTexts:sleDcnNeTable.setStatus(_B)
_SleDcnNeEntry_Object=MibTableRow
sleDcnNeEntry=_SleDcnNeEntry_Object((1,3,6,1,4,1,6296,101,91,2,1,1,1))
sleDcnNeEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:sleDcnNeEntry.setStatus(_B)
_SleDcnNeMacAddress_Type=OctetString
_SleDcnNeMacAddress_Object=MibTableColumn
sleDcnNeMacAddress=_SleDcnNeMacAddress_Object((1,3,6,1,4,1,6296,101,91,2,1,1,1,1),_SleDcnNeMacAddress_Type())
sleDcnNeMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeMacAddress.setStatus(_B)
_SleDcnNeLoIpAddr_Type=IpAddress
_SleDcnNeLoIpAddr_Object=MibTableColumn
sleDcnNeLoIpAddr=_SleDcnNeLoIpAddr_Object((1,3,6,1,4,1,6296,101,91,2,1,1,1,2),_SleDcnNeLoIpAddr_Type())
sleDcnNeLoIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeLoIpAddr.setStatus(_B)
class _SleDcnNeLoipRegsterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_SleDcnNeLoipRegsterType_Type.__name__=_D
_SleDcnNeLoipRegsterType_Object=MibTableColumn
sleDcnNeLoipRegsterType=_SleDcnNeLoipRegsterType_Object((1,3,6,1,4,1,6296,101,91,2,1,1,1,3),_SleDcnNeLoipRegsterType_Type())
sleDcnNeLoipRegsterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeLoipRegsterType.setStatus(_B)
class _SleDcnNeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_J,1),(_O,2)))
_SleDcnNeType_Type.__name__=_D
_SleDcnNeType_Object=MibTableColumn
sleDcnNeType=_SleDcnNeType_Object((1,3,6,1,4,1,6296,101,91,2,1,1,1,4),_SleDcnNeType_Type())
sleDcnNeType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeType.setStatus(_B)
class _SleDcnNeNodeRegisterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_SleDcnNeNodeRegisterType_Type.__name__=_D
_SleDcnNeNodeRegisterType_Object=MibTableColumn
sleDcnNeNodeRegisterType=_SleDcnNeNodeRegisterType_Object((1,3,6,1,4,1,6296,101,91,2,1,1,1,5),_SleDcnNeNodeRegisterType_Type())
sleDcnNeNodeRegisterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeNodeRegisterType.setStatus(_B)
class _SleDcnNodeFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_g,0),(_h,1)))
_SleDcnNodeFail_Type.__name__=_D
_SleDcnNodeFail_Object=MibTableColumn
sleDcnNodeFail=_SleDcnNodeFail_Object((1,3,6,1,4,1,6296,101,91,2,1,1,1,6),_SleDcnNodeFail_Type())
sleDcnNodeFail.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNodeFail.setStatus(_B)
_SleDcnNeSetControl_ObjectIdentity=ObjectIdentity
sleDcnNeSetControl=_SleDcnNeSetControl_ObjectIdentity((1,3,6,1,4,1,6296,101,91,2,1,2))
class _SleDcnNeControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('register',1),('unregister',2)))
_SleDcnNeControlRequest_Type.__name__=_D
_SleDcnNeControlRequest_Object=MibScalar
sleDcnNeControlRequest=_SleDcnNeControlRequest_Object((1,3,6,1,4,1,6296,101,91,2,1,2,1),_SleDcnNeControlRequest_Type())
sleDcnNeControlRequest.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnNeControlRequest.setStatus(_B)
_SleDcnNeControlStatus_Type=SleControlStatusType
_SleDcnNeControlStatus_Object=MibScalar
sleDcnNeControlStatus=_SleDcnNeControlStatus_Object((1,3,6,1,4,1,6296,101,91,2,1,2,2),_SleDcnNeControlStatus_Type())
sleDcnNeControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeControlStatus.setStatus(_B)
_SleDcnNeControlTimer_Type=Gauge32
_SleDcnNeControlTimer_Object=MibScalar
sleDcnNeControlTimer=_SleDcnNeControlTimer_Object((1,3,6,1,4,1,6296,101,91,2,1,2,3),_SleDcnNeControlTimer_Type())
sleDcnNeControlTimer.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnNeControlTimer.setStatus(_B)
_SleDcnNeControlTimeStamp_Type=TimeTicks
_SleDcnNeControlTimeStamp_Object=MibScalar
sleDcnNeControlTimeStamp=_SleDcnNeControlTimeStamp_Object((1,3,6,1,4,1,6296,101,91,2,1,2,4),_SleDcnNeControlTimeStamp_Type())
sleDcnNeControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeControlTimeStamp.setStatus(_B)
_SleDcnNeControlReqResult_Type=SleControlRequestResultType
_SleDcnNeControlReqResult_Object=MibScalar
sleDcnNeControlReqResult=_SleDcnNeControlReqResult_Object((1,3,6,1,4,1,6296,101,91,2,1,2,5),_SleDcnNeControlReqResult_Type())
sleDcnNeControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNeControlReqResult.setStatus(_B)
_SleDcnNeControlNeMacAddr_Type=OctetString
_SleDcnNeControlNeMacAddr_Object=MibScalar
sleDcnNeControlNeMacAddr=_SleDcnNeControlNeMacAddr_Object((1,3,6,1,4,1,6296,101,91,2,1,2,6),_SleDcnNeControlNeMacAddr_Type())
sleDcnNeControlNeMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnNeControlNeMacAddr.setStatus(_B)
_SleDcnProxySetNotification_ObjectIdentity=ObjectIdentity
sleDcnProxySetNotification=_SleDcnProxySetNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,91,2,1,3))
_SleDcnNeInfo_ObjectIdentity=ObjectIdentity
sleDcnNeInfo=_SleDcnNeInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,91,3))
_SleDcnGNE_ObjectIdentity=ObjectIdentity
sleDcnGNE=_SleDcnGNE_ObjectIdentity((1,3,6,1,4,1,6296,101,91,3,1))
_SleDcnGneTable_Object=MibTable
sleDcnGneTable=_SleDcnGneTable_Object((1,3,6,1,4,1,6296,101,91,3,1,1))
if mibBuilder.loadTexts:sleDcnGneTable.setStatus(_B)
_SleDcnGneEntry_Object=MibTableRow
sleDcnGneEntry=_SleDcnGneEntry_Object((1,3,6,1,4,1,6296,101,91,3,1,1,1))
sleDcnGneEntry.setIndexNames((0,_A,_i),(0,_A,_j))
if mibBuilder.loadTexts:sleDcnGneEntry.setStatus(_B)
class _SleDcnGneMasterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('l2gw',2)))
_SleDcnGneMasterType_Type.__name__=_D
_SleDcnGneMasterType_Object=MibTableColumn
sleDcnGneMasterType=_SleDcnGneMasterType_Object((1,3,6,1,4,1,6296,101,91,3,1,1,1,1),_SleDcnGneMasterType_Type())
sleDcnGneMasterType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnGneMasterType.setStatus(_B)
_SleDcnGneMacAddr_Type=OctetString
_SleDcnGneMacAddr_Object=MibTableColumn
sleDcnGneMacAddr=_SleDcnGneMacAddr_Object((1,3,6,1,4,1,6296,101,91,3,1,1,1,2),_SleDcnGneMacAddr_Type())
sleDcnGneMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnGneMacAddr.setStatus(_B)
_SleDcnGneLoIpAddr_Type=IpAddress
_SleDcnGneLoIpAddr_Object=MibTableColumn
sleDcnGneLoIpAddr=_SleDcnGneLoIpAddr_Object((1,3,6,1,4,1,6296,101,91,3,1,1,1,3),_SleDcnGneLoIpAddr_Type())
sleDcnGneLoIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnGneLoIpAddr.setStatus(_B)
class _SleDcnGneNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_J,1),(_O,2)))
_SleDcnGneNodeType_Type.__name__=_D
_SleDcnGneNodeType_Object=MibTableColumn
sleDcnGneNodeType=_SleDcnGneNodeType_Object((1,3,6,1,4,1,6296,101,91,3,1,1,1,4),_SleDcnGneNodeType_Type())
sleDcnGneNodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnGneNodeType.setStatus(_B)
class _SleDcnGNeGatewayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),(_b,1),(_c,2),(_d,3),(_e,4)))
_SleDcnGNeGatewayState_Type.__name__=_D
_SleDcnGNeGatewayState_Object=MibTableColumn
sleDcnGNeGatewayState=_SleDcnGNeGatewayState_Object((1,3,6,1,4,1,6296,101,91,3,1,1,1,5),_SleDcnGNeGatewayState_Type())
sleDcnGNeGatewayState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnGNeGatewayState.setStatus(_B)
class _SleDcnGneNodeFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_g,0),(_h,1)))
_SleDcnGneNodeFail_Type.__name__=_D
_SleDcnGneNodeFail_Object=MibTableColumn
sleDcnGneNodeFail=_SleDcnGneNodeFail_Object((1,3,6,1,4,1,6296,101,91,3,1,1,1,6),_SleDcnGneNodeFail_Type())
sleDcnGneNodeFail.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnGneNodeFail.setStatus(_B)
_SleDcnInterface_ObjectIdentity=ObjectIdentity
sleDcnInterface=_SleDcnInterface_ObjectIdentity((1,3,6,1,4,1,6296,101,91,4))
_SleDcnIf_ObjectIdentity=ObjectIdentity
sleDcnIf=_SleDcnIf_ObjectIdentity((1,3,6,1,4,1,6296,101,91,4,1))
_SleDcnIfTable_Object=MibTable
sleDcnIfTable=_SleDcnIfTable_Object((1,3,6,1,4,1,6296,101,91,4,1,1))
if mibBuilder.loadTexts:sleDcnIfTable.setStatus(_B)
_SleDcnIfEntry_Object=MibTableRow
sleDcnIfEntry=_SleDcnIfEntry_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1))
sleDcnIfEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:sleDcnIfEntry.setStatus(_B)
class _SleDcnIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SleDcnIfIndex_Type.__name__=_D
_SleDcnIfIndex_Object=MibTableColumn
sleDcnIfIndex=_SleDcnIfIndex_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,1),_SleDcnIfIndex_Type())
sleDcnIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfIndex.setStatus(_B)
class _SleDcnIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleDcnIfName_Type.__name__=_a
_SleDcnIfName_Object=MibTableColumn
sleDcnIfName=_SleDcnIfName_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,2),_SleDcnIfName_Type())
sleDcnIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfName.setStatus(_B)
class _SleDcnIfDcnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noDcnIf',0),(_I,1),('passive',2),('l2',3)))
_SleDcnIfDcnMode_Type.__name__=_D
_SleDcnIfDcnMode_Object=MibTableColumn
sleDcnIfDcnMode=_SleDcnIfDcnMode_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,3),_SleDcnIfDcnMode_Type())
sleDcnIfDcnMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfDcnMode.setStatus(_B)
_SleDcnIfAllocIpAddress_Type=IpAddress
_SleDcnIfAllocIpAddress_Object=MibTableColumn
sleDcnIfAllocIpAddress=_SleDcnIfAllocIpAddress_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,4),_SleDcnIfAllocIpAddress_Type())
sleDcnIfAllocIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfAllocIpAddress.setStatus(_B)
_SleDcnIfCurrentIpAddress_Type=IpAddress
_SleDcnIfCurrentIpAddress_Object=MibTableColumn
sleDcnIfCurrentIpAddress=_SleDcnIfCurrentIpAddress_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,5),_SleDcnIfCurrentIpAddress_Type())
sleDcnIfCurrentIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfCurrentIpAddress.setStatus(_B)
_SleDcnIfGneOspfArea_Type=IpAddress
_SleDcnIfGneOspfArea_Object=MibTableColumn
sleDcnIfGneOspfArea=_SleDcnIfGneOspfArea_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,6),_SleDcnIfGneOspfArea_Type())
sleDcnIfGneOspfArea.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfGneOspfArea.setStatus(_B)
_SleDcnNearMacAddress_Type=OctetString
_SleDcnNearMacAddress_Object=MibTableColumn
sleDcnNearMacAddress=_SleDcnNearMacAddress_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,7),_SleDcnNearMacAddress_Type())
sleDcnNearMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNearMacAddress.setStatus(_B)
_SleDcnNearNodeLoIpAddr_Type=IpAddress
_SleDcnNearNodeLoIpAddr_Object=MibTableColumn
sleDcnNearNodeLoIpAddr=_SleDcnNearNodeLoIpAddr_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,8),_SleDcnNearNodeLoIpAddr_Type())
sleDcnNearNodeLoIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNearNodeLoIpAddr.setStatus(_B)
class _SleDcnNearNodeIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleDcnNearNodeIfName_Type.__name__=_a
_SleDcnNearNodeIfName_Object=MibTableColumn
sleDcnNearNodeIfName=_SleDcnNearNodeIfName_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,9),_SleDcnNearNodeIfName_Type())
sleDcnNearNodeIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNearNodeIfName.setStatus(_B)
class _SleDcnNearIfFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_g,0),(_h,1)))
_SleDcnNearIfFail_Type.__name__=_D
_SleDcnNearIfFail_Object=MibTableColumn
sleDcnNearIfFail=_SleDcnNearIfFail_Object((1,3,6,1,4,1,6296,101,91,4,1,1,1,10),_SleDcnNearIfFail_Type())
sleDcnNearIfFail.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnNearIfFail.setStatus(_B)
_SleDcnIfControl_ObjectIdentity=ObjectIdentity
sleDcnIfControl=_SleDcnIfControl_ObjectIdentity((1,3,6,1,4,1,6296,101,91,4,1,2))
class _SleDcnIfControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dcnifDcnMode',1),('gneIfOspfArea',2)))
_SleDcnIfControlRequest_Type.__name__=_D
_SleDcnIfControlRequest_Object=MibScalar
sleDcnIfControlRequest=_SleDcnIfControlRequest_Object((1,3,6,1,4,1,6296,101,91,4,1,2,1),_SleDcnIfControlRequest_Type())
sleDcnIfControlRequest.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnIfControlRequest.setStatus(_B)
_SleDcnIfControlStatus_Type=SleControlStatusType
_SleDcnIfControlStatus_Object=MibScalar
sleDcnIfControlStatus=_SleDcnIfControlStatus_Object((1,3,6,1,4,1,6296,101,91,4,1,2,2),_SleDcnIfControlStatus_Type())
sleDcnIfControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfControlStatus.setStatus(_B)
_SleDcnIfControlTimer_Type=Gauge32
_SleDcnIfControlTimer_Object=MibScalar
sleDcnIfControlTimer=_SleDcnIfControlTimer_Object((1,3,6,1,4,1,6296,101,91,4,1,2,3),_SleDcnIfControlTimer_Type())
sleDcnIfControlTimer.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnIfControlTimer.setStatus(_B)
_SleDcnIfControlTimeStamp_Type=TimeTicks
_SleDcnIfControlTimeStamp_Object=MibScalar
sleDcnIfControlTimeStamp=_SleDcnIfControlTimeStamp_Object((1,3,6,1,4,1,6296,101,91,4,1,2,4),_SleDcnIfControlTimeStamp_Type())
sleDcnIfControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfControlTimeStamp.setStatus(_B)
_SleDcnIfControlReqResult_Type=SleControlRequestResultType
_SleDcnIfControlReqResult_Object=MibScalar
sleDcnIfControlReqResult=_SleDcnIfControlReqResult_Object((1,3,6,1,4,1,6296,101,91,4,1,2,5),_SleDcnIfControlReqResult_Type())
sleDcnIfControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleDcnIfControlReqResult.setStatus(_B)
_SleDcnIfControlIfIndex_Type=Integer32
_SleDcnIfControlIfIndex_Object=MibScalar
sleDcnIfControlIfIndex=_SleDcnIfControlIfIndex_Object((1,3,6,1,4,1,6296,101,91,4,1,2,6),_SleDcnIfControlIfIndex_Type())
sleDcnIfControlIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnIfControlIfIndex.setStatus(_B)
class _SleDcnIfControlDcnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noDcnIf',0),(_I,1),('passive',2),('l2',3)))
_SleDcnIfControlDcnMode_Type.__name__=_D
_SleDcnIfControlDcnMode_Object=MibScalar
sleDcnIfControlDcnMode=_SleDcnIfControlDcnMode_Object((1,3,6,1,4,1,6296,101,91,4,1,2,7),_SleDcnIfControlDcnMode_Type())
sleDcnIfControlDcnMode.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnIfControlDcnMode.setStatus(_B)
_SleDcnIfControlGneOspfArea_Type=IpAddress
_SleDcnIfControlGneOspfArea_Object=MibScalar
sleDcnIfControlGneOspfArea=_SleDcnIfControlGneOspfArea_Object((1,3,6,1,4,1,6296,101,91,4,1,2,8),_SleDcnIfControlGneOspfArea_Type())
sleDcnIfControlGneOspfArea.setMaxAccess(_H)
if mibBuilder.loadTexts:sleDcnIfControlGneOspfArea.setStatus(_B)
_SleDcnIfNotification_ObjectIdentity=ObjectIdentity
sleDcnIfNotification=_SleDcnIfNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,91,4,1,3))
sleDcnObjectGroup=ObjectGroup((1,3,6,1,4,1,6296,101,91,13))
sleDcnObjectGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_f),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_P),(_A,_AD),(_A,_AE),(_A,_Q),(_A,_R),(_A,_S),(_A,_j),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_r),(_A,_E),(_A,_AL),(_A,_AM),(_A,_F),(_A,_G),(_A,_s),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_k),(_A,_AQ),(_A,_AR),(_A,_T),(_A,_AS),(_A,_AT),(_A,_U),(_A,_V),(_A,_W),(_A,_t),(_A,_AU),(_A,_u),(_A,_AV),(_A,_v),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_w),(_A,_x),(_A,_y),(_A,_X),(_A,_z),(_A,_Af),(_A,_Ag),(_A,_A0),(_A,_Y),(_A,_Z),(_A,_Ah),(_A,_i),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:sleDcnObjectGroup.setStatus(_B)
sleDcnNodeTypeChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,1))
sleDcnNodeTypeChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_s)))
if mibBuilder.loadTexts:sleDcnNodeTypeChanged.setStatus(_B)
sleDcnLoIpChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,2))
sleDcnLoIpChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_X)))
if mibBuilder.loadTexts:sleDcnLoIpChanged.setStatus(_B)
sleDcnLoIpBaseChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,3))
sleDcnLoIpBaseChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:sleDcnLoIpBaseChanged.setStatus(_B)
sleDcnIfNetworkChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,4))
sleDcnIfNetworkChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_Z)))
if mibBuilder.loadTexts:sleDcnIfNetworkChanged.setStatus(_B)
sleDcnIfIpBaseChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,5))
sleDcnIfIpBaseChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:sleDcnIfIpBaseChanged.setStatus(_B)
sleDcnMgneSwitchOverChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,6))
sleDcnMgneSwitchOverChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:sleDcnMgneSwitchOverChanged.setStatus(_B)
sleDcnMgneCandidateChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,7))
sleDcnMgneCandidateChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_n)))
if mibBuilder.loadTexts:sleDcnMgneCandidateChanged.setStatus(_B)
sleDcnMgnePriorityChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,8))
sleDcnMgnePriorityChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_o)))
if mibBuilder.loadTexts:sleDcnMgnePriorityChanged.setStatus(_B)
sleDcnL2GatewayEnableChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,9))
sleDcnL2GatewayEnableChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_w)))
if mibBuilder.loadTexts:sleDcnL2GatewayEnableChanged.setStatus(_B)
sleDcnVlanIpChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,10))
sleDcnVlanIpChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_z),(_A,_v)))
if mibBuilder.loadTexts:sleDcnVlanIpChanged.setStatus(_B)
sleDcnMl2gwSwitchOverChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,11))
sleDcnMl2gwSwitchOverChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:sleDcnMl2gwSwitchOverChanged.setStatus(_B)
sleDcnMl2gwCandidateChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,12))
sleDcnMl2gwCandidateChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_p)))
if mibBuilder.loadTexts:sleDcnMl2gwCandidateChanged.setStatus(_B)
sleDcnMl2gwPriorityChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,13))
sleDcnMl2gwPriorityChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_q)))
if mibBuilder.loadTexts:sleDcnMl2gwPriorityChanged.setStatus(_B)
sleDcnRemoteLoIpChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,14))
sleDcnRemoteLoIpChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_Y),(_A,_X)))
if mibBuilder.loadTexts:sleDcnRemoteLoIpChanged.setStatus(_B)
sleDcnRemoteIfNetworkChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,15))
sleDcnRemoteIfNetworkChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:sleDcnRemoteIfNetworkChanged.setStatus(_B)
sleDcnMgmtIpChanged=NotificationType((1,3,6,1,4,1,6296,101,91,1,3,16))
sleDcnMgmtIpChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:sleDcnMgmtIpChanged.setStatus(_B)
sleDcnNeRegisterChanged=NotificationType((1,3,6,1,4,1,6296,101,91,2,1,3,1))
sleDcnNeRegisterChanged.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:sleDcnNeRegisterChanged.setStatus(_B)
sleDcnNeUnegisterChanged=NotificationType((1,3,6,1,4,1,6296,101,91,2,1,3,2))
sleDcnNeUnegisterChanged.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:sleDcnNeUnegisterChanged.setStatus(_B)
sleDcnIfModeChanged=NotificationType((1,3,6,1,4,1,6296,101,91,4,1,3,1))
sleDcnIfModeChanged.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_r)))
if mibBuilder.loadTexts:sleDcnIfModeChanged.setStatus(_B)
sleDcnIfGneOspfAreaChanged=NotificationType((1,3,6,1,4,1,6296,101,91,4,1,3,2))
sleDcnIfGneOspfAreaChanged.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_A0)))
if mibBuilder.loadTexts:sleDcnIfGneOspfAreaChanged.setStatus(_B)
sleDcnNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,91,14))
sleDcnNotificationGroup.setObjects(*((_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4)))
if mibBuilder.loadTexts:sleDcnNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'sleDCN':sleDCN,'sleDcnNodeInfo':sleDcnNodeInfo,'sleDcnNodeBaseInfo':sleDcnNodeBaseInfo,_A1:sleDcnNodeType,_A2:sleDcnMacAddress,_Ac:sleDcnLoIp,_Ai:sleDcnLoIpRegisterType,_Aj:sleDcnIfNetwork,_Ak:sleDcnIfNetworkRegisterType,_Ae:sleNeDcnOspfArea,_AY:sleDcnGneState,_A3:sleDcnMgneCandidate,_A4:sleDcnMgnePriority,_Aa:sleDcnLoIpBase,_Ab:sleDcnLoIpBasePrefixlen,_A5:sleDcnIfIpBase,_A6:sleDcnIfIpBasePrefixlen,_A7:sleDcnL2gwState,_A8:sleDcnMl2gwCandidate,_A9:sleDcnMl2gwPriority,_Ad:sleDcnVlanIp,_AW:sleDcnVlanIpPrefixlen,_Al:sleDcnVlanIpRegisterType,_Ag:sleDcnL2GatewayIp,_AU:sleDcnMgmtIp,_AV:sleDcnMgmtIpPrefixlen,'sleDcnNodeBaseControl':sleDcnNodeBaseControl,_E:sleDcnControlRequest,_AL:sleDcnControlStatus,_AM:sleDcnControlTimer,_F:sleDcnControlTimeStamp,_G:sleDcnControlReqResult,_s:sleDcnControlNodeType,_X:sleDcnControlDcnLoIp,_x:sleDcnControlDcnLoIpBase,_y:sleDcnControlDcnLoIpBasePrefixlen,_l:sleDcnControlDcnIfIpBase,_m:sleDcnControlDcnIfIpBasePrefixlen,_n:sleDcnControlDcnMgneCandidate,_o:sleDcnControlDcnMgnePriority,_w:sleDcnControlL2GatewayEnable,_z:sleDcnControlDcnVlanIp,_v:sleDcnControlDcnVlanIpPrefixlen,_p:sleDcnControlDcnMl2gwCandidate,_q:sleDcnControlDcnMl2gwPriority,_Y:sleDcnControlDcnMacAddr,_Z:sleDcnControlDcnIfNetwork,_t:sleDcnControlDcnMgmtIp,_u:sleDcnControlDcnMgmtIpPrefixlen,'sleDcnNodeBaseNotification':sleDcnNodeBaseNotification,_Aw:sleDcnNodeTypeChanged,_B2:sleDcnLoIpChanged,_B1:sleDcnLoIpBaseChanged,_Az:sleDcnIfNetworkChanged,_Am:sleDcnIfIpBaseChanged,_An:sleDcnMgneSwitchOverChanged,_Ao:sleDcnMgneCandidateChanged,_Ap:sleDcnMgnePriorityChanged,_Ay:sleDcnL2GatewayEnableChanged,_B3:sleDcnVlanIpChanged,_Aq:sleDcnMl2gwSwitchOverChanged,_Ar:sleDcnMl2gwCandidateChanged,_As:sleDcnMl2gwPriorityChanged,_A_:sleDcnRemoteLoIpChanged,_B0:sleDcnRemoteIfNetworkChanged,_Ax:sleDcnMgmtIpChanged,'sleDcnGneInfo':sleDcnGneInfo,'sleDcnNe':sleDcnNe,'sleDcnNeTable':sleDcnNeTable,'sleDcnNeEntry':sleDcnNeEntry,_f:sleDcnNeMacAddress,_AA:sleDcnNeLoIpAddr,_AB:sleDcnNeLoipRegsterType,_AZ:sleDcnNeType,_AC:sleDcnNeNodeRegisterType,_AN:sleDcnNodeFail,'sleDcnNeSetControl':sleDcnNeSetControl,_P:sleDcnNeControlRequest,_AD:sleDcnNeControlStatus,_AE:sleDcnNeControlTimer,_Q:sleDcnNeControlTimeStamp,_R:sleDcnNeControlReqResult,_S:sleDcnNeControlNeMacAddr,'sleDcnProxySetNotification':sleDcnProxySetNotification,_At:sleDcnNeRegisterChanged,_Au:sleDcnNeUnegisterChanged,'sleDcnNeInfo':sleDcnNeInfo,'sleDcnGNE':sleDcnGNE,'sleDcnGneTable':sleDcnGneTable,'sleDcnGneEntry':sleDcnGneEntry,_i:sleDcnGneMasterType,_j:sleDcnGneMacAddr,_AO:sleDcnGneLoIpAddr,_AF:sleDcnGneNodeType,_AG:sleDcnGNeGatewayState,_AP:sleDcnGneNodeFail,'sleDcnInterface':sleDcnInterface,'sleDcnIf':sleDcnIf,'sleDcnIfTable':sleDcnIfTable,'sleDcnIfEntry':sleDcnIfEntry,_k:sleDcnIfIndex,_AH:sleDcnIfName,_AI:sleDcnIfDcnMode,_AJ:sleDcnIfAllocIpAddress,_AK:sleDcnIfCurrentIpAddress,_Af:sleDcnIfGneOspfArea,_Ah:sleDcnNearMacAddress,_AQ:sleDcnNearNodeLoIpAddr,_AR:sleDcnNearNodeIfName,_AX:sleDcnNearIfFail,'sleDcnIfControl':sleDcnIfControl,_T:sleDcnIfControlRequest,_AS:sleDcnIfControlStatus,_AT:sleDcnIfControlTimer,_U:sleDcnIfControlTimeStamp,_V:sleDcnIfControlReqResult,_W:sleDcnIfControlIfIndex,_r:sleDcnIfControlDcnMode,_A0:sleDcnIfControlGneOspfArea,'sleDcnIfNotification':sleDcnIfNotification,_Av:sleDcnIfModeChanged,_B4:sleDcnIfGneOspfAreaChanged,'sleDcnObjectGroup':sleDcnObjectGroup,'sleDcnNotificationGroup':sleDcnNotificationGroup})