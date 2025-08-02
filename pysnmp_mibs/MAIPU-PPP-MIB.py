_Z='pppMultiIntIfIndex'
_Y='pppVirtualAccInt'
_X='pppCompStatIfIndex'
_W='listen'
_V='pppStatIfIndex'
_U='pppIfIndex'
_T='badAuthentication'
_S='open'
_R='pending'
_Q='opened'
_P='ackSent'
_O='ackReceived'
_N='requestSent'
_M='stopping'
_L='closing'
_K='stopped'
_J='starting'
_I='MAIPU-PPP-MIB'
_H='closed'
_G='initial'
_F='disable'
_E='enable'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mpPppMib=ModuleIdentity((1,3,6,1,4,1,5651,3,5))
_PppConfTable_Object=MibTable
pppConfTable=_PppConfTable_Object((1,3,6,1,4,1,5651,3,5,1))
if mibBuilder.loadTexts:pppConfTable.setStatus(_A)
_PppConfEntry_Object=MibTableRow
pppConfEntry=_PppConfEntry_Object((1,3,6,1,4,1,5651,3,5,1,1))
pppConfEntry.setIndexNames((0,_I,_U))
if mibBuilder.loadTexts:pppConfEntry.setStatus(_A)
_PppIfIndex_Type=Integer32
_PppIfIndex_Object=MibTableColumn
pppIfIndex=_PppIfIndex_Object((1,3,6,1,4,1,5651,3,5,1,1,1),_PppIfIndex_Type())
pppIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfIndex.setStatus(_A)
class _PppIpNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppIpNeg_Type.__name__=_D
_PppIpNeg_Object=MibTableColumn
pppIpNeg=_PppIpNeg_Object((1,3,6,1,4,1,5651,3,5,1,1,2),_PppIpNeg_Type())
pppIpNeg.setMaxAccess(_C)
if mibBuilder.loadTexts:pppIpNeg.setStatus(_A)
_PppDefIpAddr_Type=IpAddress
_PppDefIpAddr_Object=MibTableColumn
pppDefIpAddr=_PppDefIpAddr_Object((1,3,6,1,4,1,5651,3,5,1,1,3),_PppDefIpAddr_Type())
pppDefIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pppDefIpAddr.setStatus(_A)
class _PppDefIpDhcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppDefIpDhcp_Type.__name__=_D
_PppDefIpDhcp_Object=MibTableColumn
pppDefIpDhcp=_PppDefIpDhcp_Object((1,3,6,1,4,1,5651,3,5,1,1,4),_PppDefIpDhcp_Type())
pppDefIpDhcp.setMaxAccess(_C)
if mibBuilder.loadTexts:pppDefIpDhcp.setStatus(_A)
class _PppDefIpPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppDefIpPool_Type.__name__=_D
_PppDefIpPool_Object=MibTableColumn
pppDefIpPool=_PppDefIpPool_Object((1,3,6,1,4,1,5651,3,5,1,1,5),_PppDefIpPool_Type())
pppDefIpPool.setMaxAccess(_C)
if mibBuilder.loadTexts:pppDefIpPool.setStatus(_A)
_PppDefIpPoolName_Type=OctetString
_PppDefIpPoolName_Object=MibScalar
pppDefIpPoolName=_PppDefIpPoolName_Object((1,3,6,1,4,1,5651,3,5,1,1,6),_PppDefIpPoolName_Type())
pppDefIpPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:pppDefIpPoolName.setStatus(_A)
class _PppAc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppAc_Type.__name__=_D
_PppAc_Object=MibTableColumn
pppAc=_PppAc_Object((1,3,6,1,4,1,5651,3,5,1,1,7),_PppAc_Type())
pppAc.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAc.setStatus(_A)
_PppAccountName_Type=OctetString
_PppAccountName_Object=MibTableColumn
pppAccountName=_PppAccountName_Object((1,3,6,1,4,1,5651,3,5,1,1,8),_PppAccountName_Type())
pppAccountName.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAccountName.setStatus(_A)
class _PppAuthChap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppAuthChap_Type.__name__=_D
_PppAuthChap_Object=MibTableColumn
pppAuthChap=_PppAuthChap_Object((1,3,6,1,4,1,5651,3,5,1,1,9),_PppAuthChap_Type())
pppAuthChap.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAuthChap.setStatus(_A)
_PppAuthChapName_Type=OctetString
_PppAuthChapName_Object=MibTableColumn
pppAuthChapName=_PppAuthChapName_Object((1,3,6,1,4,1,5651,3,5,1,1,10),_PppAuthChapName_Type())
pppAuthChapName.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAuthChapName.setStatus(_A)
_PppChapHostName_Type=OctetString
_PppChapHostName_Object=MibTableColumn
pppChapHostName=_PppChapHostName_Object((1,3,6,1,4,1,5651,3,5,1,1,11),_PppChapHostName_Type())
pppChapHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:pppChapHostName.setStatus(_A)
class _PppAuthPap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppAuthPap_Type.__name__=_D
_PppAuthPap_Object=MibTableColumn
pppAuthPap=_PppAuthPap_Object((1,3,6,1,4,1,5651,3,5,1,1,12),_PppAuthPap_Type())
pppAuthPap.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAuthPap.setStatus(_A)
_PppAuthPapName_Type=OctetString
_PppAuthPapName_Object=MibTableColumn
pppAuthPapName=_PppAuthPapName_Object((1,3,6,1,4,1,5651,3,5,1,1,13),_PppAuthPapName_Type())
pppAuthPapName.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAuthPapName.setStatus(_A)
_PppPapUsername_Type=OctetString
_PppPapUsername_Object=MibTableColumn
pppPapUsername=_PppPapUsername_Object((1,3,6,1,4,1,5651,3,5,1,1,14),_PppPapUsername_Type())
pppPapUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:pppPapUsername.setStatus(_A)
_PppPapPassword_Type=OctetString
_PppPapPassword_Object=MibTableColumn
pppPapPassword=_PppPapPassword_Object((1,3,6,1,4,1,5651,3,5,1,1,15),_PppPapPassword_Type())
pppPapPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:pppPapPassword.setStatus(_A)
class _PppAuthMsChap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppAuthMsChap_Type.__name__=_D
_PppAuthMsChap_Object=MibTableColumn
pppAuthMsChap=_PppAuthMsChap_Object((1,3,6,1,4,1,5651,3,5,1,1,16),_PppAuthMsChap_Type())
pppAuthMsChap.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAuthMsChap.setStatus(_A)
_PppAuthMsChapName_Type=OctetString
_PppAuthMsChapName_Object=MibTableColumn
pppAuthMsChapName=_PppAuthMsChapName_Object((1,3,6,1,4,1,5651,3,5,1,1,17),_PppAuthMsChapName_Type())
pppAuthMsChapName.setMaxAccess(_C)
if mibBuilder.loadTexts:pppAuthMsChapName.setStatus(_A)
class _PppCallbackReq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppCallbackReq_Type.__name__=_D
_PppCallbackReq_Object=MibTableColumn
pppCallbackReq=_PppCallbackReq_Object((1,3,6,1,4,1,5651,3,5,1,1,18),_PppCallbackReq_Type())
pppCallbackReq.setMaxAccess(_C)
if mibBuilder.loadTexts:pppCallbackReq.setStatus(_A)
class _PppCallbackAcc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppCallbackAcc_Type.__name__=_D
_PppCallbackAcc_Object=MibTableColumn
pppCallbackAcc=_PppCallbackAcc_Object((1,3,6,1,4,1,5651,3,5,1,1,19),_PppCallbackAcc_Type())
pppCallbackAcc.setMaxAccess(_C)
if mibBuilder.loadTexts:pppCallbackAcc.setStatus(_A)
class _PppCdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppCdp_Type.__name__=_D
_PppCdp_Object=MibTableColumn
pppCdp=_PppCdp_Object((1,3,6,1,4,1,5651,3,5,1,1,20),_PppCdp_Type())
pppCdp.setMaxAccess(_C)
if mibBuilder.loadTexts:pppCdp.setStatus(_A)
class _PppComprePredictor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppComprePredictor_Type.__name__=_D
_PppComprePredictor_Object=MibTableColumn
pppComprePredictor=_PppComprePredictor_Object((1,3,6,1,4,1,5651,3,5,1,1,21),_PppComprePredictor_Type())
pppComprePredictor.setMaxAccess(_C)
if mibBuilder.loadTexts:pppComprePredictor.setStatus(_A)
class _PppCompreStacker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppCompreStacker_Type.__name__=_D
_PppCompreStacker_Object=MibTableColumn
pppCompreStacker=_PppCompreStacker_Object((1,3,6,1,4,1,5651,3,5,1,1,22),_PppCompreStacker_Type())
pppCompreStacker.setMaxAccess(_C)
if mibBuilder.loadTexts:pppCompreStacker.setStatus(_A)
_PppEncDesKey_Type=OctetString
_PppEncDesKey_Object=MibTableColumn
pppEncDesKey=_PppEncDesKey_Object((1,3,6,1,4,1,5651,3,5,1,1,23),_PppEncDesKey_Type())
pppEncDesKey.setMaxAccess(_C)
if mibBuilder.loadTexts:pppEncDesKey.setStatus(_A)
_PppEnc3DesKey_Type=OctetString
_PppEnc3DesKey_Object=MibTableColumn
pppEnc3DesKey=_PppEnc3DesKey_Object((1,3,6,1,4,1,5651,3,5,1,1,24),_PppEnc3DesKey_Type())
pppEnc3DesKey.setMaxAccess(_C)
if mibBuilder.loadTexts:pppEnc3DesKey.setStatus(_A)
_PppEncDesBisKey_Type=OctetString
_PppEncDesBisKey_Object=MibTableColumn
pppEncDesBisKey=_PppEncDesBisKey_Object((1,3,6,1,4,1,5651,3,5,1,1,25),_PppEncDesBisKey_Type())
pppEncDesBisKey.setMaxAccess(_C)
if mibBuilder.loadTexts:pppEncDesBisKey.setStatus(_A)
class _PppMultilink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),('bap',3)))
_PppMultilink_Type.__name__=_D
_PppMultilink_Object=MibTableColumn
pppMultilink=_PppMultilink_Object((1,3,6,1,4,1,5651,3,5,1,1,26),_PppMultilink_Type())
pppMultilink.setMaxAccess(_C)
if mibBuilder.loadTexts:pppMultilink.setStatus(_A)
class _PppPc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppPc_Type.__name__=_D
_PppPc_Object=MibTableColumn
pppPc=_PppPc_Object((1,3,6,1,4,1,5651,3,5,1,1,27),_PppPc_Type())
pppPc.setMaxAccess(_C)
if mibBuilder.loadTexts:pppPc.setStatus(_A)
class _PppReliableLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PppReliableLink_Type.__name__=_D
_PppReliableLink_Object=MibTableColumn
pppReliableLink=_PppReliableLink_Object((1,3,6,1,4,1,5651,3,5,1,1,28),_PppReliableLink_Type())
pppReliableLink.setMaxAccess(_C)
if mibBuilder.loadTexts:pppReliableLink.setStatus(_A)
class _PppTimeoutAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PppTimeoutAuth_Type.__name__=_D
_PppTimeoutAuth_Object=MibTableColumn
pppTimeoutAuth=_PppTimeoutAuth_Object((1,3,6,1,4,1,5651,3,5,1,1,29),_PppTimeoutAuth_Type())
pppTimeoutAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:pppTimeoutAuth.setStatus(_A)
class _PppTimeoutIpcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PppTimeoutIpcp_Type.__name__=_D
_PppTimeoutIpcp_Object=MibTableColumn
pppTimeoutIpcp=_PppTimeoutIpcp_Object((1,3,6,1,4,1,5651,3,5,1,1,30),_PppTimeoutIpcp_Type())
pppTimeoutIpcp.setMaxAccess(_C)
if mibBuilder.loadTexts:pppTimeoutIpcp.setStatus(_A)
class _PppTimeoutRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PppTimeoutRetry_Type.__name__=_D
_PppTimeoutRetry_Object=MibTableColumn
pppTimeoutRetry=_PppTimeoutRetry_Object((1,3,6,1,4,1,5651,3,5,1,1,31),_PppTimeoutRetry_Type())
pppTimeoutRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:pppTimeoutRetry.setStatus(_A)
_PppMultilinkBap_Type=Integer32
_PppMultilinkBap_Object=MibTableColumn
pppMultilinkBap=_PppMultilinkBap_Object((1,3,6,1,4,1,5651,3,5,1,1,32),_PppMultilinkBap_Type())
pppMultilinkBap.setMaxAccess(_C)
if mibBuilder.loadTexts:pppMultilinkBap.setStatus(_A)
_PppStatTable_Object=MibTable
pppStatTable=_PppStatTable_Object((1,3,6,1,4,1,5651,3,5,2))
if mibBuilder.loadTexts:pppStatTable.setStatus(_A)
_PppStatEntry_Object=MibTableRow
pppStatEntry=_PppStatEntry_Object((1,3,6,1,4,1,5651,3,5,2,1))
pppStatEntry.setIndexNames((0,_I,_V))
if mibBuilder.loadTexts:pppStatEntry.setStatus(_A)
_PppStatIfIndex_Type=Integer32
_PppStatIfIndex_Object=MibTableColumn
pppStatIfIndex=_PppStatIfIndex_Object((1,3,6,1,4,1,5651,3,5,2,1,1),_PppStatIfIndex_Type())
pppStatIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppStatIfIndex.setStatus(_A)
class _PppLcpPhase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('dead',1),('establish',2),('authenticate',3),('network',4),('terminate',5)))
_PppLcpPhase_Type.__name__=_D
_PppLcpPhase_Object=MibTableColumn
pppLcpPhase=_PppLcpPhase_Object((1,3,6,1,4,1,5651,3,5,2,1,2),_PppLcpPhase_Type())
pppLcpPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpPhase.setStatus(_A)
class _PppLcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_J,2),(_H,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10)))
_PppLcpState_Type.__name__=_D
_PppLcpState_Object=MibTableColumn
pppLcpState=_PppLcpState_Object((1,3,6,1,4,1,5651,3,5,2,1,3),_PppLcpState_Type())
pppLcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpState.setStatus(_A)
_PppLcpMru_Type=Integer32
_PppLcpMru_Object=MibTableColumn
pppLcpMru=_PppLcpMru_Object((1,3,6,1,4,1,5651,3,5,2,1,4),_PppLcpMru_Type())
pppLcpMru.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpMru.setStatus(_A)
_PppLcpMtu_Type=Integer32
_PppLcpMtu_Object=MibTableColumn
pppLcpMtu=_PppLcpMtu_Object((1,3,6,1,4,1,5651,3,5,2,1,5),_PppLcpMtu_Type())
pppLcpMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpMtu.setStatus(_A)
_PppLcpAsyncMap_Type=Integer32
_PppLcpAsyncMap_Object=MibTableColumn
pppLcpAsyncMap=_PppLcpAsyncMap_Object((1,3,6,1,4,1,5651,3,5,2,1,6),_PppLcpAsyncMap_Type())
pppLcpAsyncMap.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpAsyncMap.setStatus(_A)
_PppLcpLocalMagicNo_Type=Integer32
_PppLcpLocalMagicNo_Object=MibTableColumn
pppLcpLocalMagicNo=_PppLcpLocalMagicNo_Object((1,3,6,1,4,1,5651,3,5,2,1,7),_PppLcpLocalMagicNo_Type())
pppLcpLocalMagicNo.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpLocalMagicNo.setStatus(_A)
_PppLcpProtoFieldComp_Type=Integer32
_PppLcpProtoFieldComp_Object=MibTableColumn
pppLcpProtoFieldComp=_PppLcpProtoFieldComp_Object((1,3,6,1,4,1,5651,3,5,2,1,8),_PppLcpProtoFieldComp_Type())
pppLcpProtoFieldComp.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpProtoFieldComp.setStatus(_A)
_PppLcpACFieldComp_Type=Integer32
_PppLcpACFieldComp_Object=MibTableColumn
pppLcpACFieldComp=_PppLcpACFieldComp_Object((1,3,6,1,4,1,5651,3,5,2,1,9),_PppLcpACFieldComp_Type())
pppLcpACFieldComp.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpACFieldComp.setStatus(_A)
_PppLcpEchoTimer_Type=Integer32
_PppLcpEchoTimer_Object=MibTableColumn
pppLcpEchoTimer=_PppLcpEchoTimer_Object((1,3,6,1,4,1,5651,3,5,2,1,10),_PppLcpEchoTimer_Type())
pppLcpEchoTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpEchoTimer.setStatus(_A)
_PppLcpEchoPend_Type=Integer32
_PppLcpEchoPend_Object=MibTableColumn
pppLcpEchoPend=_PppLcpEchoPend_Object((1,3,6,1,4,1,5651,3,5,2,1,11),_PppLcpEchoPend_Type())
pppLcpEchoPend.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpEchoPend.setStatus(_A)
_PppLcpEchoNo_Type=Integer32
_PppLcpEchoNo_Object=MibTableColumn
pppLcpEchoNo=_PppLcpEchoNo_Object((1,3,6,1,4,1,5651,3,5,2,1,12),_PppLcpEchoNo_Type())
pppLcpEchoNo.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpEchoNo.setStatus(_A)
_PppLcpEchoInter_Type=Integer32
_PppLcpEchoInter_Object=MibTableColumn
pppLcpEchoInter=_PppLcpEchoInter_Object((1,3,6,1,4,1,5651,3,5,2,1,13),_PppLcpEchoInter_Type())
pppLcpEchoInter.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpEchoInter.setStatus(_A)
_PppLcpEchoFails_Type=Integer32
_PppLcpEchoFails_Object=MibTableColumn
pppLcpEchoFails=_PppLcpEchoFails_Object((1,3,6,1,4,1,5651,3,5,2,1,14),_PppLcpEchoFails_Type())
pppLcpEchoFails.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLcpEchoFails.setStatus(_A)
class _PppIpcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_J,2),(_H,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10)))
_PppIpcpState_Type.__name__=_D
_PppIpcpState_Object=MibTableColumn
pppIpcpState=_PppIpcpState_Object((1,3,6,1,4,1,5651,3,5,2,1,15),_PppIpcpState_Type())
pppIpcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIpcpState.setStatus(_A)
_PppIpcpLocalIPAddr_Type=IpAddress
_PppIpcpLocalIPAddr_Object=MibTableColumn
pppIpcpLocalIPAddr=_PppIpcpLocalIPAddr_Object((1,3,6,1,4,1,5651,3,5,2,1,16),_PppIpcpLocalIPAddr_Type())
pppIpcpLocalIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIpcpLocalIPAddr.setStatus(_A)
_PppIpcpRemIPAddr_Type=IpAddress
_PppIpcpRemIPAddr_Object=MibTableColumn
pppIpcpRemIPAddr=_PppIpcpRemIPAddr_Object((1,3,6,1,4,1,5651,3,5,2,1,17),_PppIpcpRemIPAddr_Type())
pppIpcpRemIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIpcpRemIPAddr.setStatus(_A)
_PppIpcpVJCompProto_Type=Integer32
_PppIpcpVJCompProto_Object=MibTableColumn
pppIpcpVJCompProto=_PppIpcpVJCompProto_Object((1,3,6,1,4,1,5651,3,5,2,1,18),_PppIpcpVJCompProto_Type())
pppIpcpVJCompProto.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIpcpVJCompProto.setStatus(_A)
_PppIpcpVJCompPassive_Type=Integer32
_PppIpcpVJCompPassive_Object=MibTableColumn
pppIpcpVJCompPassive=_PppIpcpVJCompPassive_Object((1,3,6,1,4,1,5651,3,5,2,1,19),_PppIpcpVJCompPassive_Type())
pppIpcpVJCompPassive.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIpcpVJCompPassive.setStatus(_A)
_PppIpcpRtpCompProto_Type=Integer32
_PppIpcpRtpCompProto_Object=MibTableColumn
pppIpcpRtpCompProto=_PppIpcpRtpCompProto_Object((1,3,6,1,4,1,5651,3,5,2,1,20),_PppIpcpRtpCompProto_Type())
pppIpcpRtpCompProto.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIpcpRtpCompProto.setStatus(_A)
_PppIpcpRtpCompPassive_Type=Integer32
_PppIpcpRtpCompPassive_Object=MibTableColumn
pppIpcpRtpCompPassive=_PppIpcpRtpCompPassive_Object((1,3,6,1,4,1,5651,3,5,2,1,21),_PppIpcpRtpCompPassive_Type())
pppIpcpRtpCompPassive.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIpcpRtpCompPassive.setStatus(_A)
class _PppCdpcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_J,2),(_H,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10)))
_PppCdpcpState_Type.__name__=_D
_PppCdpcpState_Object=MibTableColumn
pppCdpcpState=_PppCdpcpState_Object((1,3,6,1,4,1,5651,3,5,2,1,22),_PppCdpcpState_Type())
pppCdpcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCdpcpState.setStatus(_A)
class _PppCcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_J,2),(_H,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10)))
_PppCcpState_Type.__name__=_D
_PppCcpState_Object=MibTableColumn
pppCcpState=_PppCcpState_Object((1,3,6,1,4,1,5651,3,5,2,1,23),_PppCcpState_Type())
pppCcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCcpState.setStatus(_A)
class _PppEcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_J,2),(_H,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10)))
_PppEcpState_Type.__name__=_D
_PppEcpState_Object=MibTableColumn
pppEcpState=_PppEcpState_Object((1,3,6,1,4,1,5651,3,5,2,1,24),_PppEcpState_Type())
pppEcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppEcpState.setStatus(_A)
class _PppPapClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_H,2),(_R,3),('authenticationReq',4),(_S,5),(_T,6)))
_PppPapClientState_Type.__name__=_D
_PppPapClientState_Object=MibTableColumn
pppPapClientState=_PppPapClientState_Object((1,3,6,1,4,1,5651,3,5,2,1,25),_PppPapClientState_Type())
pppPapClientState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPapClientState.setStatus(_A)
class _PppPapServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_H,2),(_R,3),(_W,4),(_S,5),(_T,6)))
_PppPapServerState_Type.__name__=_D
_PppPapServerState_Object=MibTableColumn
pppPapServerState=_PppPapServerState_Object((1,3,6,1,4,1,5651,3,5,2,1,26),_PppPapServerState_Type())
pppPapServerState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPapServerState.setStatus(_A)
class _PppChapClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_H,2),(_R,3),(_W,4),('response',5),(_S,6)))
_PppChapClientState_Type.__name__=_D
_PppChapClientState_Object=MibTableColumn
pppChapClientState=_PppChapClientState_Object((1,3,6,1,4,1,5651,3,5,2,1,27),_PppChapClientState_Type())
pppChapClientState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppChapClientState.setStatus(_A)
class _PppChapServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_H,2),(_R,3),('initialChallenge',4),('oepn',5),('rechallenge',6),(_T,7)))
_PppChapServerState_Type.__name__=_D
_PppChapServerState_Object=MibTableColumn
pppChapServerState=_PppChapServerState_Object((1,3,6,1,4,1,5651,3,5,2,1,28),_PppChapServerState_Type())
pppChapServerState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppChapServerState.setStatus(_A)
_PppLzsdcpState_Type=Integer32
_PppLzsdcpState_Object=MibTableColumn
pppLzsdcpState=_PppLzsdcpState_Object((1,3,6,1,4,1,5651,3,5,2,1,29),_PppLzsdcpState_Type())
pppLzsdcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLzsdcpState.setStatus(_A)
_PppPredictor_Type=Integer32
_PppPredictor_Object=MibTableColumn
pppPredictor=_PppPredictor_Object((1,3,6,1,4,1,5651,3,5,2,1,30),_PppPredictor_Type())
pppPredictor.setMaxAccess(_B)
if mibBuilder.loadTexts:pppPredictor.setStatus(_A)
_PppDes_Type=Integer32
_PppDes_Object=MibTableColumn
pppDes=_PppDes_Object((1,3,6,1,4,1,5651,3,5,2,1,31),_PppDes_Type())
pppDes.setMaxAccess(_B)
if mibBuilder.loadTexts:pppDes.setStatus(_A)
_PppDesBis_Type=Integer32
_PppDesBis_Object=MibTableColumn
pppDesBis=_PppDesBis_Object((1,3,6,1,4,1,5651,3,5,2,1,32),_PppDesBis_Type())
pppDesBis.setMaxAccess(_B)
if mibBuilder.loadTexts:pppDesBis.setStatus(_A)
_Ppp3Des_Type=Integer32
_Ppp3Des_Object=MibTableColumn
ppp3Des=_Ppp3Des_Object((1,3,6,1,4,1,5651,3,5,2,1,33),_Ppp3Des_Type())
ppp3Des.setMaxAccess(_B)
if mibBuilder.loadTexts:ppp3Des.setStatus(_A)
_PppCompStatTable_Object=MibTable
pppCompStatTable=_PppCompStatTable_Object((1,3,6,1,4,1,5651,3,5,3))
if mibBuilder.loadTexts:pppCompStatTable.setStatus(_A)
_PppCompStatEntry_Object=MibTableRow
pppCompStatEntry=_PppCompStatEntry_Object((1,3,6,1,4,1,5651,3,5,3,1))
pppCompStatEntry.setIndexNames((0,_I,_X))
if mibBuilder.loadTexts:pppCompStatEntry.setStatus(_A)
_PppCompStatIfIndex_Type=Integer32
_PppCompStatIfIndex_Object=MibTableColumn
pppCompStatIfIndex=_PppCompStatIfIndex_Object((1,3,6,1,4,1,5651,3,5,3,1,1),_PppCompStatIfIndex_Type())
pppCompStatIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCompStatIfIndex.setStatus(_A)
class _PppCompType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stacker',1),('predictor',2)))
_PppCompType_Type.__name__=_D
_PppCompType_Object=MibTableColumn
pppCompType=_PppCompType_Object((1,3,6,1,4,1,5651,3,5,3,1,2),_PppCompType_Type())
pppCompType.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCompType.setStatus(_A)
_PppUncompBytes_Type=Counter32
_PppUncompBytes_Object=MibTableColumn
pppUncompBytes=_PppUncompBytes_Object((1,3,6,1,4,1,5651,3,5,3,1,3),_PppUncompBytes_Type())
pppUncompBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pppUncompBytes.setStatus(_A)
_PppUncompPkts_Type=Counter32
_PppUncompPkts_Object=MibTableColumn
pppUncompPkts=_PppUncompPkts_Object((1,3,6,1,4,1,5651,3,5,3,1,4),_PppUncompPkts_Type())
pppUncompPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppUncompPkts.setStatus(_A)
_PppCompBytes_Type=Counter32
_PppCompBytes_Object=MibTableColumn
pppCompBytes=_PppCompBytes_Object((1,3,6,1,4,1,5651,3,5,3,1,5),_PppCompBytes_Type())
pppCompBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCompBytes.setStatus(_A)
_PppCompPkts_Type=Counter32
_PppCompPkts_Object=MibTableColumn
pppCompPkts=_PppCompPkts_Object((1,3,6,1,4,1,5651,3,5,3,1,6),_PppCompPkts_Type())
pppCompPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCompPkts.setStatus(_A)
_PppIncompBytes_Type=Counter32
_PppIncompBytes_Object=MibTableColumn
pppIncompBytes=_PppIncompBytes_Object((1,3,6,1,4,1,5651,3,5,3,1,7),_PppIncompBytes_Type())
pppIncompBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIncompBytes.setStatus(_A)
_PppIncompPkts_Type=Counter32
_PppIncompPkts_Object=MibTableColumn
pppIncompPkts=_PppIncompPkts_Object((1,3,6,1,4,1,5651,3,5,3,1,8),_PppIncompPkts_Type())
pppIncompPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIncompPkts.setStatus(_A)
_PppRecvBytes_Type=Counter32
_PppRecvBytes_Object=MibTableColumn
pppRecvBytes=_PppRecvBytes_Object((1,3,6,1,4,1,5651,3,5,3,1,9),_PppRecvBytes_Type())
pppRecvBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pppRecvBytes.setStatus(_A)
_PppTransBytes_Type=Counter32
_PppTransBytes_Object=MibTableColumn
pppTransBytes=_PppTransBytes_Object((1,3,6,1,4,1,5651,3,5,3,1,10),_PppTransBytes_Type())
pppTransBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:pppTransBytes.setStatus(_A)
_PppCompRatio_Type=Integer32
_PppCompRatio_Object=MibTableColumn
pppCompRatio=_PppCompRatio_Object((1,3,6,1,4,1,5651,3,5,3,1,11),_PppCompRatio_Type())
pppCompRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:pppCompRatio.setStatus(_A)
_PppMultiTable_Object=MibTable
pppMultiTable=_PppMultiTable_Object((1,3,6,1,4,1,5651,3,5,4))
if mibBuilder.loadTexts:pppMultiTable.setStatus(_A)
_PppMultiEntry_Object=MibTableRow
pppMultiEntry=_PppMultiEntry_Object((1,3,6,1,4,1,5651,3,5,4,1))
pppMultiEntry.setIndexNames((0,_I,_Y))
if mibBuilder.loadTexts:pppMultiEntry.setStatus(_A)
_PppVirtualAccInt_Type=OctetString
_PppVirtualAccInt_Object=MibTableColumn
pppVirtualAccInt=_PppVirtualAccInt_Object((1,3,6,1,4,1,5651,3,5,4,1,1),_PppVirtualAccInt_Type())
pppVirtualAccInt.setMaxAccess(_B)
if mibBuilder.loadTexts:pppVirtualAccInt.setStatus(_A)
_PppLogicInt_Type=OctetString
_PppLogicInt_Object=MibTableColumn
pppLogicInt=_PppLogicInt_Object((1,3,6,1,4,1,5651,3,5,4,1,2),_PppLogicInt_Type())
pppLogicInt.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLogicInt.setStatus(_A)
_PppLocalVirtualIpAddr_Type=IpAddress
_PppLocalVirtualIpAddr_Object=MibTableColumn
pppLocalVirtualIpAddr=_PppLocalVirtualIpAddr_Object((1,3,6,1,4,1,5651,3,5,4,1,3),_PppLocalVirtualIpAddr_Type())
pppLocalVirtualIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLocalVirtualIpAddr.setStatus(_A)
_PppRemVirtualIpAddr_Type=IpAddress
_PppRemVirtualIpAddr_Object=MibScalar
pppRemVirtualIpAddr=_PppRemVirtualIpAddr_Object((1,3,6,1,4,1,5651,3,5,4,1,4),_PppRemVirtualIpAddr_Type())
pppRemVirtualIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pppRemVirtualIpAddr.setStatus(_A)
_PppMultiMemNum_Type=Integer32
_PppMultiMemNum_Object=MibTableColumn
pppMultiMemNum=_PppMultiMemNum_Object((1,3,6,1,4,1,5651,3,5,4,1,5),_PppMultiMemNum_Type())
pppMultiMemNum.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMultiMemNum.setStatus(_A)
_PppMultiIntTable_Object=MibTable
pppMultiIntTable=_PppMultiIntTable_Object((1,3,6,1,4,1,5651,3,5,5))
if mibBuilder.loadTexts:pppMultiIntTable.setStatus(_A)
_PppMultiIntEntry_Object=MibTableRow
pppMultiIntEntry=_PppMultiIntEntry_Object((1,3,6,1,4,1,5651,3,5,5,1))
pppMultiIntEntry.setIndexNames((0,_I,_Z))
if mibBuilder.loadTexts:pppMultiIntEntry.setStatus(_A)
_PppMultiIntIfIndex_Type=Integer32
_PppMultiIntIfIndex_Object=MibTableColumn
pppMultiIntIfIndex=_PppMultiIntIfIndex_Object((1,3,6,1,4,1,5651,3,5,5,1,1),_PppMultiIntIfIndex_Type())
pppMultiIntIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMultiIntIfIndex.setStatus(_A)
_PppMultiIntName_Type=OctetString
_PppMultiIntName_Object=MibTableColumn
pppMultiIntName=_PppMultiIntName_Object((1,3,6,1,4,1,5651,3,5,5,1,2),_PppMultiIntName_Type())
pppMultiIntName.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMultiIntName.setStatus(_A)
_PppMultiIntBBandWidth_Type=Integer32
_PppMultiIntBBandWidth_Object=MibTableColumn
pppMultiIntBBandWidth=_PppMultiIntBBandWidth_Object((1,3,6,1,4,1,5651,3,5,5,1,3),_PppMultiIntBBandWidth_Type())
pppMultiIntBBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:pppMultiIntBBandWidth.setStatus(_A)
_PppVirtualIntName_Type=OctetString
_PppVirtualIntName_Object=MibTableColumn
pppVirtualIntName=_PppVirtualIntName_Object((1,3,6,1,4,1,5651,3,5,5,1,4),_PppVirtualIntName_Type())
pppVirtualIntName.setMaxAccess(_B)
if mibBuilder.loadTexts:pppVirtualIntName.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'mpPppMib':mpPppMib,'pppConfTable':pppConfTable,'pppConfEntry':pppConfEntry,_U:pppIfIndex,'pppIpNeg':pppIpNeg,'pppDefIpAddr':pppDefIpAddr,'pppDefIpDhcp':pppDefIpDhcp,'pppDefIpPool':pppDefIpPool,'pppDefIpPoolName':pppDefIpPoolName,'pppAc':pppAc,'pppAccountName':pppAccountName,'pppAuthChap':pppAuthChap,'pppAuthChapName':pppAuthChapName,'pppChapHostName':pppChapHostName,'pppAuthPap':pppAuthPap,'pppAuthPapName':pppAuthPapName,'pppPapUsername':pppPapUsername,'pppPapPassword':pppPapPassword,'pppAuthMsChap':pppAuthMsChap,'pppAuthMsChapName':pppAuthMsChapName,'pppCallbackReq':pppCallbackReq,'pppCallbackAcc':pppCallbackAcc,'pppCdp':pppCdp,'pppComprePredictor':pppComprePredictor,'pppCompreStacker':pppCompreStacker,'pppEncDesKey':pppEncDesKey,'pppEnc3DesKey':pppEnc3DesKey,'pppEncDesBisKey':pppEncDesBisKey,'pppMultilink':pppMultilink,'pppPc':pppPc,'pppReliableLink':pppReliableLink,'pppTimeoutAuth':pppTimeoutAuth,'pppTimeoutIpcp':pppTimeoutIpcp,'pppTimeoutRetry':pppTimeoutRetry,'pppMultilinkBap':pppMultilinkBap,'pppStatTable':pppStatTable,'pppStatEntry':pppStatEntry,_V:pppStatIfIndex,'pppLcpPhase':pppLcpPhase,'pppLcpState':pppLcpState,'pppLcpMru':pppLcpMru,'pppLcpMtu':pppLcpMtu,'pppLcpAsyncMap':pppLcpAsyncMap,'pppLcpLocalMagicNo':pppLcpLocalMagicNo,'pppLcpProtoFieldComp':pppLcpProtoFieldComp,'pppLcpACFieldComp':pppLcpACFieldComp,'pppLcpEchoTimer':pppLcpEchoTimer,'pppLcpEchoPend':pppLcpEchoPend,'pppLcpEchoNo':pppLcpEchoNo,'pppLcpEchoInter':pppLcpEchoInter,'pppLcpEchoFails':pppLcpEchoFails,'pppIpcpState':pppIpcpState,'pppIpcpLocalIPAddr':pppIpcpLocalIPAddr,'pppIpcpRemIPAddr':pppIpcpRemIPAddr,'pppIpcpVJCompProto':pppIpcpVJCompProto,'pppIpcpVJCompPassive':pppIpcpVJCompPassive,'pppIpcpRtpCompProto':pppIpcpRtpCompProto,'pppIpcpRtpCompPassive':pppIpcpRtpCompPassive,'pppCdpcpState':pppCdpcpState,'pppCcpState':pppCcpState,'pppEcpState':pppEcpState,'pppPapClientState':pppPapClientState,'pppPapServerState':pppPapServerState,'pppChapClientState':pppChapClientState,'pppChapServerState':pppChapServerState,'pppLzsdcpState':pppLzsdcpState,'pppPredictor':pppPredictor,'pppDes':pppDes,'pppDesBis':pppDesBis,'ppp3Des':ppp3Des,'pppCompStatTable':pppCompStatTable,'pppCompStatEntry':pppCompStatEntry,_X:pppCompStatIfIndex,'pppCompType':pppCompType,'pppUncompBytes':pppUncompBytes,'pppUncompPkts':pppUncompPkts,'pppCompBytes':pppCompBytes,'pppCompPkts':pppCompPkts,'pppIncompBytes':pppIncompBytes,'pppIncompPkts':pppIncompPkts,'pppRecvBytes':pppRecvBytes,'pppTransBytes':pppTransBytes,'pppCompRatio':pppCompRatio,'pppMultiTable':pppMultiTable,'pppMultiEntry':pppMultiEntry,_Y:pppVirtualAccInt,'pppLogicInt':pppLogicInt,'pppLocalVirtualIpAddr':pppLocalVirtualIpAddr,'pppRemVirtualIpAddr':pppRemVirtualIpAddr,'pppMultiMemNum':pppMultiMemNum,'pppMultiIntTable':pppMultiIntTable,'pppMultiIntEntry':pppMultiIntEntry,_Z:pppMultiIntIfIndex,'pppMultiIntName':pppMultiIntName,'pppMultiIntBBandWidth':pppMultiIntBBandWidth,'pppVirtualIntName':pppVirtualIntName})