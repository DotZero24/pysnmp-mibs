_f='h3cNATDnsMapDomainName'
_e='h3cNATStaticInsideIp'
_d='h3cNATSessionVpnIndex'
_c='h3cNATSessionPeerPort'
_b='h3cNATSessionPeerIP'
_a='h3cNATSessionInsidePort'
_Z='h3cNATSessionInsideIP'
_Y='h3cNATSessionProtocol'
_X='h3cNATSessionHashNumber'
_W='h3cNATStatNATBoardNo'
_V='h3cNATBLSlotNo'
_U='h3cNATBLIpAdress'
_T='h3cNATBLIPConnectLimitParaIP'
_S='h3cNATBLEnableSlotNo'
_R='h3cNATTimeOutProtocol'
_Q='h3cNATServerVpnIndex'
_P='h3cNATServerStartGlobalPort'
_O='h3cNATServerGlobalIP'
_N='h3cNATServerProType'
_M='h3cNATOutboundAclNo'
_L='h3cNATPoolIdx'
_K='disable'
_J='enable'
_I='ifIndex'
_H='IF-MIB'
_G='read-write'
_F='read-only'
_E='not-accessible'
_D='A3COM-HUAWEI-NAT-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cNat=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,18))
if mibBuilder.loadTexts:h3cNat.setRevisions(('2005-01-20 15:18',))
_H3cNATGlobalVars_ObjectIdentity=ObjectIdentity
h3cNATGlobalVars=_H3cNATGlobalVars_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,18,1))
_H3cNATClearSession_ObjectIdentity=ObjectIdentity
h3cNATClearSession=_H3cNATClearSession_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,18,1,1))
class _H3cNATClearSessionSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_H3cNATClearSessionSlotNo_Type.__name__=_B
_H3cNATClearSessionSlotNo_Object=MibScalar
h3cNATClearSessionSlotNo=_H3cNATClearSessionSlotNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,1,1),_H3cNATClearSessionSlotNo_Type())
h3cNATClearSessionSlotNo.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATClearSessionSlotNo.setStatus(_A)
_H3cNATBLConnectLimitPara_ObjectIdentity=ObjectIdentity
h3cNATBLConnectLimitPara=_H3cNATBLConnectLimitPara_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,18,1,2))
class _H3cNATBLConnectHighValue_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_H3cNATBLConnectHighValue_Type.__name__=_B
_H3cNATBLConnectHighValue_Object=MibScalar
h3cNATBLConnectHighValue=_H3cNATBLConnectHighValue_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,2,1),_H3cNATBLConnectHighValue_Type())
h3cNATBLConnectHighValue.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLConnectHighValue.setStatus(_A)
class _H3cNATBLConnectLowValue_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_H3cNATBLConnectLowValue_Type.__name__=_B
_H3cNATBLConnectLowValue_Object=MibScalar
h3cNATBLConnectLowValue=_H3cNATBLConnectLowValue_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,2,2),_H3cNATBLConnectLowValue_Type())
h3cNATBLConnectLowValue.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLConnectLowValue.setStatus(_A)
class _H3cNATBLConnectHighRate_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_H3cNATBLConnectHighRate_Type.__name__=_B
_H3cNATBLConnectHighRate_Object=MibScalar
h3cNATBLConnectHighRate=_H3cNATBLConnectHighRate_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,2,3),_H3cNATBLConnectHighRate_Type())
h3cNATBLConnectHighRate.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLConnectHighRate.setStatus(_A)
class _H3cNATBLConnectLowRate_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_H3cNATBLConnectLowRate_Type.__name__=_B
_H3cNATBLConnectLowRate_Object=MibScalar
h3cNATBLConnectLowRate=_H3cNATBLConnectLowRate_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,2,4),_H3cNATBLConnectLowRate_Type())
h3cNATBLConnectLowRate.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLConnectLowRate.setStatus(_A)
class _H3cNATBLSpecialConnectHighRate_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_H3cNATBLSpecialConnectHighRate_Type.__name__=_B
_H3cNATBLSpecialConnectHighRate_Object=MibScalar
h3cNATBLSpecialConnectHighRate=_H3cNATBLSpecialConnectHighRate_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,2,5),_H3cNATBLSpecialConnectHighRate_Type())
h3cNATBLSpecialConnectHighRate.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLSpecialConnectHighRate.setStatus(_A)
class _H3cNATBLSpecialConnectLowRate_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_H3cNATBLSpecialConnectLowRate_Type.__name__=_B
_H3cNATBLSpecialConnectLowRate_Object=MibScalar
h3cNATBLSpecialConnectLowRate=_H3cNATBLSpecialConnectLowRate_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,2,6),_H3cNATBLSpecialConnectLowRate_Type())
h3cNATBLSpecialConnectLowRate.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLSpecialConnectLowRate.setStatus(_A)
_H3cNATBLCtrlEnable_ObjectIdentity=ObjectIdentity
h3cNATBLCtrlEnable=_H3cNATBLCtrlEnable_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,18,1,3))
class _H3cNATBLConnectSumEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_H3cNATBLConnectSumEnable_Type.__name__=_B
_H3cNATBLConnectSumEnable_Object=MibScalar
h3cNATBLConnectSumEnable=_H3cNATBLConnectSumEnable_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,3,1),_H3cNATBLConnectSumEnable_Type())
h3cNATBLConnectSumEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLConnectSumEnable.setStatus(_A)
class _H3cNATBLConnectRateEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_H3cNATBLConnectRateEnable_Type.__name__=_B
_H3cNATBLConnectRateEnable_Object=MibScalar
h3cNATBLConnectRateEnable=_H3cNATBLConnectRateEnable_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,3,2),_H3cNATBLConnectRateEnable_Type())
h3cNATBLConnectRateEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLConnectRateEnable.setStatus(_A)
_H3cNATNPTimer_ObjectIdentity=ObjectIdentity
h3cNATNPTimer=_H3cNATNPTimer_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,18,1,4))
class _H3cNATNPAgingTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('slow',2)))
_H3cNATNPAgingTime_Type.__name__=_B
_H3cNATNPAgingTime_Object=MibScalar
h3cNATNPAgingTime=_H3cNATNPAgingTime_Object((1,3,6,1,4,1,43,45,1,10,2,18,1,4,1),_H3cNATNPAgingTime_Type())
h3cNATNPAgingTime.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATNPAgingTime.setStatus(_A)
_H3cNATMibObjects_ObjectIdentity=ObjectIdentity
h3cNATMibObjects=_H3cNATMibObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,18,2))
_H3cNATPoolInfoTable_Object=MibTable
h3cNATPoolInfoTable=_H3cNATPoolInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1))
if mibBuilder.loadTexts:h3cNATPoolInfoTable.setStatus(_A)
_H3cNATPoolInfoEntry_Object=MibTableRow
h3cNATPoolInfoEntry=_H3cNATPoolInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1,1))
h3cNATPoolInfoEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:h3cNATPoolInfoEntry.setStatus(_A)
class _H3cNATPoolIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,320))
_H3cNATPoolIdx_Type.__name__=_B
_H3cNATPoolIdx_Object=MibTableColumn
h3cNATPoolIdx=_H3cNATPoolIdx_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1,1,1),_H3cNATPoolIdx_Type())
h3cNATPoolIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATPoolIdx.setStatus(_A)
_H3cNATPoolStartIpAddr_Type=IpAddress
_H3cNATPoolStartIpAddr_Object=MibTableColumn
h3cNATPoolStartIpAddr=_H3cNATPoolStartIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1,1,2),_H3cNATPoolStartIpAddr_Type())
h3cNATPoolStartIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATPoolStartIpAddr.setStatus(_A)
_H3cNATPoolEndIpAddr_Type=IpAddress
_H3cNATPoolEndIpAddr_Object=MibTableColumn
h3cNATPoolEndIpAddr=_H3cNATPoolEndIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1,1,3),_H3cNATPoolEndIpAddr_Type())
h3cNATPoolEndIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATPoolEndIpAddr.setStatus(_A)
class _H3cNATPoolSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_H3cNATPoolSlotNo_Type.__name__=_B
_H3cNATPoolSlotNo_Object=MibTableColumn
h3cNATPoolSlotNo=_H3cNATPoolSlotNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1,1,4),_H3cNATPoolSlotNo_Type())
h3cNATPoolSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATPoolSlotNo.setStatus(_A)
_H3cNATPoolRefCounter_Type=Integer32
_H3cNATPoolRefCounter_Object=MibTableColumn
h3cNATPoolRefCounter=_H3cNATPoolRefCounter_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1,1,5),_H3cNATPoolRefCounter_Type())
h3cNATPoolRefCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATPoolRefCounter.setStatus(_A)
_H3cNATPoolRowStatus_Type=RowStatus
_H3cNATPoolRowStatus_Object=MibTableColumn
h3cNATPoolRowStatus=_H3cNATPoolRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,1,1,6),_H3cNATPoolRowStatus_Type())
h3cNATPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATPoolRowStatus.setStatus(_A)
_H3cNATOutboundTable_Object=MibTable
h3cNATOutboundTable=_H3cNATOutboundTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,2))
if mibBuilder.loadTexts:h3cNATOutboundTable.setStatus(_A)
_H3cNATOutboundEntry_Object=MibTableRow
h3cNATOutboundEntry=_H3cNATOutboundEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,2,1))
h3cNATOutboundEntry.setIndexNames((0,_H,_I),(0,_D,_M))
if mibBuilder.loadTexts:h3cNATOutboundEntry.setStatus(_A)
class _H3cNATOutboundAclNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,3999))
_H3cNATOutboundAclNo_Type.__name__=_B
_H3cNATOutboundAclNo_Object=MibTableColumn
h3cNATOutboundAclNo=_H3cNATOutboundAclNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,2,1,1),_H3cNATOutboundAclNo_Type())
h3cNATOutboundAclNo.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATOutboundAclNo.setStatus(_A)
class _H3cNATOutboundPoolIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,320),ValueRangeConstraint(2147483647,2147483647))
_H3cNATOutboundPoolIdx_Type.__name__=_B
_H3cNATOutboundPoolIdx_Object=MibTableColumn
h3cNATOutboundPoolIdx=_H3cNATOutboundPoolIdx_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,2,1,2),_H3cNATOutboundPoolIdx_Type())
h3cNATOutboundPoolIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATOutboundPoolIdx.setStatus(_A)
class _H3cNATOutboundIsNoPat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_H3cNATOutboundIsNoPat_Type.__name__=_B
_H3cNATOutboundIsNoPat_Object=MibTableColumn
h3cNATOutboundIsNoPat=_H3cNATOutboundIsNoPat_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,2,1,3),_H3cNATOutboundIsNoPat_Type())
h3cNATOutboundIsNoPat.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATOutboundIsNoPat.setStatus(_A)
class _H3cNATOutboundSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_H3cNATOutboundSlotNo_Type.__name__=_B
_H3cNATOutboundSlotNo_Object=MibTableColumn
h3cNATOutboundSlotNo=_H3cNATOutboundSlotNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,2,1,4),_H3cNATOutboundSlotNo_Type())
h3cNATOutboundSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATOutboundSlotNo.setStatus(_A)
_H3cNATOutboundRowStatus_Type=RowStatus
_H3cNATOutboundRowStatus_Object=MibTableColumn
h3cNATOutboundRowStatus=_H3cNATOutboundRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,2,1,5),_H3cNATOutboundRowStatus_Type())
h3cNATOutboundRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATOutboundRowStatus.setStatus(_A)
_H3cNATServerTable_Object=MibTable
h3cNATServerTable=_H3cNATServerTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3))
if mibBuilder.loadTexts:h3cNATServerTable.setStatus(_A)
_H3cNATServerEntry_Object=MibTableRow
h3cNATServerEntry=_H3cNATServerEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1))
h3cNATServerEntry.setIndexNames((0,_H,_I),(0,_D,_N),(0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:h3cNATServerEntry.setStatus(_A)
class _H3cNATServerProType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cNATServerProType_Type.__name__=_B
_H3cNATServerProType_Object=MibTableColumn
h3cNATServerProType=_H3cNATServerProType_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,1),_H3cNATServerProType_Type())
h3cNATServerProType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATServerProType.setStatus(_A)
_H3cNATServerGlobalIP_Type=IpAddress
_H3cNATServerGlobalIP_Object=MibTableColumn
h3cNATServerGlobalIP=_H3cNATServerGlobalIP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,2),_H3cNATServerGlobalIP_Type())
h3cNATServerGlobalIP.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATServerGlobalIP.setStatus(_A)
class _H3cNATServerStartGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cNATServerStartGlobalPort_Type.__name__=_B
_H3cNATServerStartGlobalPort_Object=MibTableColumn
h3cNATServerStartGlobalPort=_H3cNATServerStartGlobalPort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,3),_H3cNATServerStartGlobalPort_Type())
h3cNATServerStartGlobalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATServerStartGlobalPort.setStatus(_A)
class _H3cNATServerEndGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cNATServerEndGlobalPort_Type.__name__=_B
_H3cNATServerEndGlobalPort_Object=MibTableColumn
h3cNATServerEndGlobalPort=_H3cNATServerEndGlobalPort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,4),_H3cNATServerEndGlobalPort_Type())
h3cNATServerEndGlobalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATServerEndGlobalPort.setStatus(_A)
_H3cNATServerStartInsideIP_Type=IpAddress
_H3cNATServerStartInsideIP_Object=MibTableColumn
h3cNATServerStartInsideIP=_H3cNATServerStartInsideIP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,5),_H3cNATServerStartInsideIP_Type())
h3cNATServerStartInsideIP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATServerStartInsideIP.setStatus(_A)
_H3cNATServerEndInsideIP_Type=IpAddress
_H3cNATServerEndInsideIP_Object=MibTableColumn
h3cNATServerEndInsideIP=_H3cNATServerEndInsideIP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,6),_H3cNATServerEndInsideIP_Type())
h3cNATServerEndInsideIP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATServerEndInsideIP.setStatus(_A)
class _H3cNATServerInsidePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cNATServerInsidePort_Type.__name__=_B
_H3cNATServerInsidePort_Object=MibTableColumn
h3cNATServerInsidePort=_H3cNATServerInsidePort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,7),_H3cNATServerInsidePort_Type())
h3cNATServerInsidePort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATServerInsidePort.setStatus(_A)
class _H3cNATServerSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_H3cNATServerSlotNo_Type.__name__=_B
_H3cNATServerSlotNo_Object=MibTableColumn
h3cNATServerSlotNo=_H3cNATServerSlotNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,8),_H3cNATServerSlotNo_Type())
h3cNATServerSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATServerSlotNo.setStatus(_A)
class _H3cNATServerVpnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cNATServerVpnIndex_Type.__name__=_B
_H3cNATServerVpnIndex_Object=MibTableColumn
h3cNATServerVpnIndex=_H3cNATServerVpnIndex_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,10),_H3cNATServerVpnIndex_Type())
h3cNATServerVpnIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATServerVpnIndex.setStatus(_A)
class _H3cNATServerAclNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_H3cNATServerAclNumber_Type.__name__=_B
_H3cNATServerAclNumber_Object=MibTableColumn
h3cNATServerAclNumber=_H3cNATServerAclNumber_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,11),_H3cNATServerAclNumber_Type())
h3cNATServerAclNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATServerAclNumber.setStatus(_A)
_H3cNATServerRowStatus_Type=RowStatus
_H3cNATServerRowStatus_Object=MibTableColumn
h3cNATServerRowStatus=_H3cNATServerRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,3,1,12),_H3cNATServerRowStatus_Type())
h3cNATServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATServerRowStatus.setStatus(_A)
_H3cNATTimeOutTable_Object=MibTable
h3cNATTimeOutTable=_H3cNATTimeOutTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,4))
if mibBuilder.loadTexts:h3cNATTimeOutTable.setStatus(_A)
_H3cNATTimeOutEntry_Object=MibTableRow
h3cNATTimeOutEntry=_H3cNATTimeOutEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,4,1))
h3cNATTimeOutEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:h3cNATTimeOutEntry.setStatus(_A)
class _H3cNATTimeOutProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('tcp',1),('udp',2),('icmp',3),('pptp',4),('dns',5),('tcpFin',6),('tcpSyn',7),('ftpCtrl',8),('ftpData',9)))
_H3cNATTimeOutProtocol_Type.__name__=_B
_H3cNATTimeOutProtocol_Object=MibTableColumn
h3cNATTimeOutProtocol=_H3cNATTimeOutProtocol_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,4,1,1),_H3cNATTimeOutProtocol_Type())
h3cNATTimeOutProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATTimeOutProtocol.setStatus(_A)
class _H3cNATTimeOutTimeValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,86400))
_H3cNATTimeOutTimeValue_Type.__name__=_B
_H3cNATTimeOutTimeValue_Object=MibTableColumn
h3cNATTimeOutTimeValue=_H3cNATTimeOutTimeValue_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,4,1,2),_H3cNATTimeOutTimeValue_Type())
h3cNATTimeOutTimeValue.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATTimeOutTimeValue.setStatus(_A)
_H3cNATBLEnableTable_Object=MibTable
h3cNATBLEnableTable=_H3cNATBLEnableTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,5))
if mibBuilder.loadTexts:h3cNATBLEnableTable.setStatus(_A)
_H3cNATBLEnableEntry_Object=MibTableRow
h3cNATBLEnableEntry=_H3cNATBLEnableEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,5,1))
h3cNATBLEnableEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:h3cNATBLEnableEntry.setStatus(_A)
class _H3cNATBLEnableSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_H3cNATBLEnableSlotNo_Type.__name__=_B
_H3cNATBLEnableSlotNo_Object=MibTableColumn
h3cNATBLEnableSlotNo=_H3cNATBLEnableSlotNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,5,1,1),_H3cNATBLEnableSlotNo_Type())
h3cNATBLEnableSlotNo.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATBLEnableSlotNo.setStatus(_A)
class _H3cNATBLEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_H3cNATBLEnable_Type.__name__=_B
_H3cNATBLEnable_Object=MibTableColumn
h3cNATBLEnable=_H3cNATBLEnable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,5,1,2),_H3cNATBLEnable_Type())
h3cNATBLEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATBLEnable.setStatus(_A)
_H3cNATBLIPConnectLimitParaTable_Object=MibTable
h3cNATBLIPConnectLimitParaTable=_H3cNATBLIPConnectLimitParaTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,6))
if mibBuilder.loadTexts:h3cNATBLIPConnectLimitParaTable.setStatus(_A)
_H3cNATBLIPConnectLimitParaEntry_Object=MibTableRow
h3cNATBLIPConnectLimitParaEntry=_H3cNATBLIPConnectLimitParaEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,6,1))
h3cNATBLIPConnectLimitParaEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:h3cNATBLIPConnectLimitParaEntry.setStatus(_A)
_H3cNATBLIPConnectLimitParaIP_Type=IpAddress
_H3cNATBLIPConnectLimitParaIP_Object=MibTableColumn
h3cNATBLIPConnectLimitParaIP=_H3cNATBLIPConnectLimitParaIP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,6,1,1),_H3cNATBLIPConnectLimitParaIP_Type())
h3cNATBLIPConnectLimitParaIP.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATBLIPConnectLimitParaIP.setStatus(_A)
class _H3cNATBLIPConnectHighValue_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_H3cNATBLIPConnectHighValue_Type.__name__=_B
_H3cNATBLIPConnectHighValue_Object=MibTableColumn
h3cNATBLIPConnectHighValue=_H3cNATBLIPConnectHighValue_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,6,1,2),_H3cNATBLIPConnectHighValue_Type())
h3cNATBLIPConnectHighValue.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATBLIPConnectHighValue.setStatus(_A)
class _H3cNATBLIPConnectLowValue_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_H3cNATBLIPConnectLowValue_Type.__name__=_B
_H3cNATBLIPConnectLowValue_Object=MibTableColumn
h3cNATBLIPConnectLowValue=_H3cNATBLIPConnectLowValue_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,6,1,3),_H3cNATBLIPConnectLowValue_Type())
h3cNATBLIPConnectLowValue.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATBLIPConnectLowValue.setStatus(_A)
class _H3cNATBLIPUseSpecialConnectRate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_H3cNATBLIPUseSpecialConnectRate_Type.__name__=_B
_H3cNATBLIPUseSpecialConnectRate_Object=MibTableColumn
h3cNATBLIPUseSpecialConnectRate=_H3cNATBLIPUseSpecialConnectRate_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,6,1,4),_H3cNATBLIPUseSpecialConnectRate_Type())
h3cNATBLIPUseSpecialConnectRate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATBLIPUseSpecialConnectRate.setStatus(_A)
_H3cNATBLIPConnectLimitRowStatus_Type=RowStatus
_H3cNATBLIPConnectLimitRowStatus_Object=MibTableColumn
h3cNATBLIPConnectLimitRowStatus=_H3cNATBLIPConnectLimitRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,6,1,5),_H3cNATBLIPConnectLimitRowStatus_Type())
h3cNATBLIPConnectLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATBLIPConnectLimitRowStatus.setStatus(_A)
_H3cNATBLManagerTable_Object=MibTable
h3cNATBLManagerTable=_H3cNATBLManagerTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,7))
if mibBuilder.loadTexts:h3cNATBLManagerTable.setStatus(_A)
_H3cNATBLManagerEntry_Object=MibTableRow
h3cNATBLManagerEntry=_H3cNATBLManagerEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,7,1))
h3cNATBLManagerEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:h3cNATBLManagerEntry.setStatus(_A)
_H3cNATBLIpAdress_Type=IpAddress
_H3cNATBLIpAdress_Object=MibTableColumn
h3cNATBLIpAdress=_H3cNATBLIpAdress_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,7,1,1),_H3cNATBLIpAdress_Type())
h3cNATBLIpAdress.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATBLIpAdress.setStatus(_A)
class _H3cNATBLSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_H3cNATBLSlotNo_Type.__name__=_B
_H3cNATBLSlotNo_Object=MibTableColumn
h3cNATBLSlotNo=_H3cNATBLSlotNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,7,1,2),_H3cNATBLSlotNo_Type())
h3cNATBLSlotNo.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATBLSlotNo.setStatus(_A)
_H3cNATBLConSum_Type=Integer32
_H3cNATBLConSum_Object=MibTableColumn
h3cNATBLConSum=_H3cNATBLConSum_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,7,1,3),_H3cNATBLConSum_Type())
h3cNATBLConSum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATBLConSum.setStatus(_A)
class _H3cNATBLConSpd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('red',1),('yellow',2),('green',3)))
_H3cNATBLConSpd_Type.__name__=_B
_H3cNATBLConSpd_Object=MibTableColumn
h3cNATBLConSpd=_H3cNATBLConSpd_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,7,1,4),_H3cNATBLConSpd_Type())
h3cNATBLConSpd.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATBLConSpd.setStatus(_A)
_H3cNATStatTable_Object=MibTable
h3cNATStatTable=_H3cNATStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8))
if mibBuilder.loadTexts:h3cNATStatTable.setStatus(_A)
_H3cNATStatEntry_Object=MibTableRow
h3cNATStatEntry=_H3cNATStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1))
h3cNATStatEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:h3cNATStatEntry.setStatus(_A)
class _H3cNATStatNATBoardNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_H3cNATStatNATBoardNo_Type.__name__=_B
_H3cNATStatNATBoardNo_Object=MibTableColumn
h3cNATStatNATBoardNo=_H3cNATStatNATBoardNo_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,1),_H3cNATStatNATBoardNo_Type())
h3cNATStatNATBoardNo.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATStatNATBoardNo.setStatus(_A)
_H3cNATStatActiveTblCount_Type=Counter32
_H3cNATStatActiveTblCount_Object=MibTableColumn
h3cNATStatActiveTblCount=_H3cNATStatActiveTblCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,2),_H3cNATStatActiveTblCount_Type())
h3cNATStatActiveTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatActiveTblCount.setStatus(_A)
_H3cNATStatActiveTblCountInNP_Type=Counter32
_H3cNATStatActiveTblCountInNP_Object=MibTableColumn
h3cNATStatActiveTblCountInNP=_H3cNATStatActiveTblCountInNP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,3),_H3cNATStatActiveTblCountInNP_Type())
h3cNATStatActiveTblCountInNP.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatActiveTblCountInNP.setStatus(_A)
_H3cNATStatActiveNatTblCount_Type=Counter32
_H3cNATStatActiveNatTblCount_Object=MibTableColumn
h3cNATStatActiveNatTblCount=_H3cNATStatActiveNatTblCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,4),_H3cNATStatActiveNatTblCount_Type())
h3cNATStatActiveNatTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatActiveNatTblCount.setStatus(_A)
_H3cNATStatActiveSvrTblCount_Type=Counter32
_H3cNATStatActiveSvrTblCount_Object=MibTableColumn
h3cNATStatActiveSvrTblCount=_H3cNATStatActiveSvrTblCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,5),_H3cNATStatActiveSvrTblCount_Type())
h3cNATStatActiveSvrTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatActiveSvrTblCount.setStatus(_A)
_H3cNATStatActivePoolTblCount_Type=Counter32
_H3cNATStatActivePoolTblCount_Object=MibTableColumn
h3cNATStatActivePoolTblCount=_H3cNATStatActivePoolTblCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,6),_H3cNATStatActivePoolTblCount_Type())
h3cNATStatActivePoolTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatActivePoolTblCount.setStatus(_A)
_H3cNATStatNumOfUsedPort_Type=Counter32
_H3cNATStatNumOfUsedPort_Object=MibTableColumn
h3cNATStatNumOfUsedPort=_H3cNATStatNumOfUsedPort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,7),_H3cNATStatNumOfUsedPort_Type())
h3cNATStatNumOfUsedPort.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatNumOfUsedPort.setStatus(_A)
_H3cNATStatNumOfGoodPkt_Type=Counter32
_H3cNATStatNumOfGoodPkt_Object=MibTableColumn
h3cNATStatNumOfGoodPkt=_H3cNATStatNumOfGoodPkt_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,8),_H3cNATStatNumOfGoodPkt_Type())
h3cNATStatNumOfGoodPkt.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatNumOfGoodPkt.setStatus(_A)
_H3cNATStatNumOfBadPkt_Type=Counter32
_H3cNATStatNumOfBadPkt_Object=MibTableColumn
h3cNATStatNumOfBadPkt=_H3cNATStatNumOfBadPkt_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,9),_H3cNATStatNumOfBadPkt_Type())
h3cNATStatNumOfBadPkt.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStatNumOfBadPkt.setStatus(_A)
_H3cNATStaticSessionCount_Type=Integer32
_H3cNATStaticSessionCount_Object=MibTableColumn
h3cNATStaticSessionCount=_H3cNATStaticSessionCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,10),_H3cNATStaticSessionCount_Type())
h3cNATStaticSessionCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATStaticSessionCount.setStatus(_A)
_H3cNATFragmentSessionCount_Type=Integer32
_H3cNATFragmentSessionCount_Object=MibTableColumn
h3cNATFragmentSessionCount=_H3cNATFragmentSessionCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,11),_H3cNATFragmentSessionCount_Type())
h3cNATFragmentSessionCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATFragmentSessionCount.setStatus(_A)
_H3cNATSequenceSessionCount_Type=Integer32
_H3cNATSequenceSessionCount_Object=MibTableColumn
h3cNATSequenceSessionCount=_H3cNATSequenceSessionCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,12),_H3cNATSequenceSessionCount_Type())
h3cNATSequenceSessionCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATSequenceSessionCount.setStatus(_A)
_H3cNATLogCount_Type=Integer32
_H3cNATLogCount_Object=MibTableColumn
h3cNATLogCount=_H3cNATLogCount_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,8,1,13),_H3cNATLogCount_Type())
h3cNATLogCount.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATLogCount.setStatus(_A)
_H3cNATSessionTable_Object=MibTable
h3cNATSessionTable=_H3cNATSessionTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9))
if mibBuilder.loadTexts:h3cNATSessionTable.setStatus(_A)
_H3cNATSessionEntry_Object=MibTableRow
h3cNATSessionEntry=_H3cNATSessionEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1))
h3cNATSessionEntry.setIndexNames((0,_D,_X),(0,_D,_Y),(0,_D,_Z),(0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:h3cNATSessionEntry.setStatus(_A)
class _H3cNATSessionHashNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300000))
_H3cNATSessionHashNumber_Type.__name__=_B
_H3cNATSessionHashNumber_Object=MibTableColumn
h3cNATSessionHashNumber=_H3cNATSessionHashNumber_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,1),_H3cNATSessionHashNumber_Type())
h3cNATSessionHashNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATSessionHashNumber.setStatus(_A)
class _H3cNATSessionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cNATSessionProtocol_Type.__name__=_B
_H3cNATSessionProtocol_Object=MibTableColumn
h3cNATSessionProtocol=_H3cNATSessionProtocol_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,2),_H3cNATSessionProtocol_Type())
h3cNATSessionProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATSessionProtocol.setStatus(_A)
_H3cNATSessionGlobalIP_Type=IpAddress
_H3cNATSessionGlobalIP_Object=MibTableColumn
h3cNATSessionGlobalIP=_H3cNATSessionGlobalIP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,3),_H3cNATSessionGlobalIP_Type())
h3cNATSessionGlobalIP.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATSessionGlobalIP.setStatus(_A)
class _H3cNATSessionGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cNATSessionGlobalPort_Type.__name__=_B
_H3cNATSessionGlobalPort_Object=MibTableColumn
h3cNATSessionGlobalPort=_H3cNATSessionGlobalPort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,4),_H3cNATSessionGlobalPort_Type())
h3cNATSessionGlobalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATSessionGlobalPort.setStatus(_A)
_H3cNATSessionInsideIP_Type=IpAddress
_H3cNATSessionInsideIP_Object=MibTableColumn
h3cNATSessionInsideIP=_H3cNATSessionInsideIP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,5),_H3cNATSessionInsideIP_Type())
h3cNATSessionInsideIP.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATSessionInsideIP.setStatus(_A)
class _H3cNATSessionInsidePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cNATSessionInsidePort_Type.__name__=_B
_H3cNATSessionInsidePort_Object=MibTableColumn
h3cNATSessionInsidePort=_H3cNATSessionInsidePort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,6),_H3cNATSessionInsidePort_Type())
h3cNATSessionInsidePort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATSessionInsidePort.setStatus(_A)
_H3cNATSessionPeerIP_Type=IpAddress
_H3cNATSessionPeerIP_Object=MibTableColumn
h3cNATSessionPeerIP=_H3cNATSessionPeerIP_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,7),_H3cNATSessionPeerIP_Type())
h3cNATSessionPeerIP.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATSessionPeerIP.setStatus(_A)
class _H3cNATSessionPeerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cNATSessionPeerPort_Type.__name__=_B
_H3cNATSessionPeerPort_Object=MibTableColumn
h3cNATSessionPeerPort=_H3cNATSessionPeerPort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,8),_H3cNATSessionPeerPort_Type())
h3cNATSessionPeerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATSessionPeerPort.setStatus(_A)
class _H3cNATSessionVpnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cNATSessionVpnIndex_Type.__name__=_B
_H3cNATSessionVpnIndex_Object=MibTableColumn
h3cNATSessionVpnIndex=_H3cNATSessionVpnIndex_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,9),_H3cNATSessionVpnIndex_Type())
h3cNATSessionVpnIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATSessionVpnIndex.setStatus(_A)
_H3cNATSessionTTL_Type=Integer32
_H3cNATSessionTTL_Object=MibTableColumn
h3cNATSessionTTL=_H3cNATSessionTTL_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,10),_H3cNATSessionTTL_Type())
h3cNATSessionTTL.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATSessionTTL.setStatus(_A)
_H3cNATSessionStatus_Type=Integer32
_H3cNATSessionStatus_Object=MibTableColumn
h3cNATSessionStatus=_H3cNATSessionStatus_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,11),_H3cNATSessionStatus_Type())
h3cNATSessionStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATSessionStatus.setStatus(_A)
_H3cNATSessionLeftTime_Type=TimeTicks
_H3cNATSessionLeftTime_Object=MibTableColumn
h3cNATSessionLeftTime=_H3cNATSessionLeftTime_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,9,1,12),_H3cNATSessionLeftTime_Type())
h3cNATSessionLeftTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNATSessionLeftTime.setStatus(_A)
_H3cNATStaticConfTable_Object=MibTable
h3cNATStaticConfTable=_H3cNATStaticConfTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,10))
if mibBuilder.loadTexts:h3cNATStaticConfTable.setStatus(_A)
_H3cNATStaticConfEntry_Object=MibTableRow
h3cNATStaticConfEntry=_H3cNATStaticConfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,10,1))
h3cNATStaticConfEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:h3cNATStaticConfEntry.setStatus(_A)
_H3cNATStaticInsideIp_Type=IpAddress
_H3cNATStaticInsideIp_Object=MibTableColumn
h3cNATStaticInsideIp=_H3cNATStaticInsideIp_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,10,1,1),_H3cNATStaticInsideIp_Type())
h3cNATStaticInsideIp.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATStaticInsideIp.setStatus(_A)
_H3cNATStaticGlobalIp_Type=IpAddress
_H3cNATStaticGlobalIp_Object=MibTableColumn
h3cNATStaticGlobalIp=_H3cNATStaticGlobalIp_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,10,1,2),_H3cNATStaticGlobalIp_Type())
h3cNATStaticGlobalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATStaticGlobalIp.setStatus(_A)
_H3cNATStaticRowStatus_Type=RowStatus
_H3cNATStaticRowStatus_Object=MibTableColumn
h3cNATStaticRowStatus=_H3cNATStaticRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,10,1,3),_H3cNATStaticRowStatus_Type())
h3cNATStaticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATStaticRowStatus.setStatus(_A)
_H3cNATStaticEnableTable_Object=MibTable
h3cNATStaticEnableTable=_H3cNATStaticEnableTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,11))
if mibBuilder.loadTexts:h3cNATStaticEnableTable.setStatus(_A)
_H3cNATStaticEnableEntry_Object=MibTableRow
h3cNATStaticEnableEntry=_H3cNATStaticEnableEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,11,1))
h3cNATStaticEnableEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cNATStaticEnableEntry.setStatus(_A)
class _H3cNATStaticEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_J,1)))
_H3cNATStaticEnable_Type.__name__=_B
_H3cNATStaticEnable_Object=MibTableColumn
h3cNATStaticEnable=_H3cNATStaticEnable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,11,1,2),_H3cNATStaticEnable_Type())
h3cNATStaticEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cNATStaticEnable.setStatus(_A)
_H3cNATDnsMapTable_Object=MibTable
h3cNATDnsMapTable=_H3cNATDnsMapTable_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12))
if mibBuilder.loadTexts:h3cNATDnsMapTable.setStatus(_A)
_H3cNATDnsMapEntry_Object=MibTableRow
h3cNATDnsMapEntry=_H3cNATDnsMapEntry_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12,1))
h3cNATDnsMapEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:h3cNATDnsMapEntry.setStatus(_A)
_H3cNATDnsMapDomainName_Type=DisplayString
_H3cNATDnsMapDomainName_Object=MibTableColumn
h3cNATDnsMapDomainName=_H3cNATDnsMapDomainName_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12,1,1),_H3cNATDnsMapDomainName_Type())
h3cNATDnsMapDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cNATDnsMapDomainName.setStatus(_A)
_H3cNATDnsMapGlobalIp_Type=IpAddress
_H3cNATDnsMapGlobalIp_Object=MibTableColumn
h3cNATDnsMapGlobalIp=_H3cNATDnsMapGlobalIp_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12,1,2),_H3cNATDnsMapGlobalIp_Type())
h3cNATDnsMapGlobalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATDnsMapGlobalIp.setStatus(_A)
class _H3cNATDnsMapGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cNATDnsMapGlobalPort_Type.__name__=_B
_H3cNATDnsMapGlobalPort_Object=MibTableColumn
h3cNATDnsMapGlobalPort=_H3cNATDnsMapGlobalPort_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12,1,3),_H3cNATDnsMapGlobalPort_Type())
h3cNATDnsMapGlobalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATDnsMapGlobalPort.setStatus(_A)
class _H3cNATDnsMapProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('any',0),('typeTCP',1),('typeUDP',2)))
_H3cNATDnsMapProtocolType_Type.__name__=_B
_H3cNATDnsMapProtocolType_Object=MibTableColumn
h3cNATDnsMapProtocolType=_H3cNATDnsMapProtocolType_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12,1,4),_H3cNATDnsMapProtocolType_Type())
h3cNATDnsMapProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATDnsMapProtocolType.setStatus(_A)
_H3cNATDnsMapLastUseTime_Type=TimeTicks
_H3cNATDnsMapLastUseTime_Object=MibTableColumn
h3cNATDnsMapLastUseTime=_H3cNATDnsMapLastUseTime_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12,1,5),_H3cNATDnsMapLastUseTime_Type())
h3cNATDnsMapLastUseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATDnsMapLastUseTime.setStatus(_A)
_H3cNATDnsMapRowStatus_Type=RowStatus
_H3cNATDnsMapRowStatus_Object=MibTableColumn
h3cNATDnsMapRowStatus=_H3cNATDnsMapRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,18,2,12,1,6),_H3cNATDnsMapRowStatus_Type())
h3cNATDnsMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cNATDnsMapRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cNat':h3cNat,'h3cNATGlobalVars':h3cNATGlobalVars,'h3cNATClearSession':h3cNATClearSession,'h3cNATClearSessionSlotNo':h3cNATClearSessionSlotNo,'h3cNATBLConnectLimitPara':h3cNATBLConnectLimitPara,'h3cNATBLConnectHighValue':h3cNATBLConnectHighValue,'h3cNATBLConnectLowValue':h3cNATBLConnectLowValue,'h3cNATBLConnectHighRate':h3cNATBLConnectHighRate,'h3cNATBLConnectLowRate':h3cNATBLConnectLowRate,'h3cNATBLSpecialConnectHighRate':h3cNATBLSpecialConnectHighRate,'h3cNATBLSpecialConnectLowRate':h3cNATBLSpecialConnectLowRate,'h3cNATBLCtrlEnable':h3cNATBLCtrlEnable,'h3cNATBLConnectSumEnable':h3cNATBLConnectSumEnable,'h3cNATBLConnectRateEnable':h3cNATBLConnectRateEnable,'h3cNATNPTimer':h3cNATNPTimer,'h3cNATNPAgingTime':h3cNATNPAgingTime,'h3cNATMibObjects':h3cNATMibObjects,'h3cNATPoolInfoTable':h3cNATPoolInfoTable,'h3cNATPoolInfoEntry':h3cNATPoolInfoEntry,_L:h3cNATPoolIdx,'h3cNATPoolStartIpAddr':h3cNATPoolStartIpAddr,'h3cNATPoolEndIpAddr':h3cNATPoolEndIpAddr,'h3cNATPoolSlotNo':h3cNATPoolSlotNo,'h3cNATPoolRefCounter':h3cNATPoolRefCounter,'h3cNATPoolRowStatus':h3cNATPoolRowStatus,'h3cNATOutboundTable':h3cNATOutboundTable,'h3cNATOutboundEntry':h3cNATOutboundEntry,_M:h3cNATOutboundAclNo,'h3cNATOutboundPoolIdx':h3cNATOutboundPoolIdx,'h3cNATOutboundIsNoPat':h3cNATOutboundIsNoPat,'h3cNATOutboundSlotNo':h3cNATOutboundSlotNo,'h3cNATOutboundRowStatus':h3cNATOutboundRowStatus,'h3cNATServerTable':h3cNATServerTable,'h3cNATServerEntry':h3cNATServerEntry,_N:h3cNATServerProType,_O:h3cNATServerGlobalIP,_P:h3cNATServerStartGlobalPort,'h3cNATServerEndGlobalPort':h3cNATServerEndGlobalPort,'h3cNATServerStartInsideIP':h3cNATServerStartInsideIP,'h3cNATServerEndInsideIP':h3cNATServerEndInsideIP,'h3cNATServerInsidePort':h3cNATServerInsidePort,'h3cNATServerSlotNo':h3cNATServerSlotNo,_Q:h3cNATServerVpnIndex,'h3cNATServerAclNumber':h3cNATServerAclNumber,'h3cNATServerRowStatus':h3cNATServerRowStatus,'h3cNATTimeOutTable':h3cNATTimeOutTable,'h3cNATTimeOutEntry':h3cNATTimeOutEntry,_R:h3cNATTimeOutProtocol,'h3cNATTimeOutTimeValue':h3cNATTimeOutTimeValue,'h3cNATBLEnableTable':h3cNATBLEnableTable,'h3cNATBLEnableEntry':h3cNATBLEnableEntry,_S:h3cNATBLEnableSlotNo,'h3cNATBLEnable':h3cNATBLEnable,'h3cNATBLIPConnectLimitParaTable':h3cNATBLIPConnectLimitParaTable,'h3cNATBLIPConnectLimitParaEntry':h3cNATBLIPConnectLimitParaEntry,_T:h3cNATBLIPConnectLimitParaIP,'h3cNATBLIPConnectHighValue':h3cNATBLIPConnectHighValue,'h3cNATBLIPConnectLowValue':h3cNATBLIPConnectLowValue,'h3cNATBLIPUseSpecialConnectRate':h3cNATBLIPUseSpecialConnectRate,'h3cNATBLIPConnectLimitRowStatus':h3cNATBLIPConnectLimitRowStatus,'h3cNATBLManagerTable':h3cNATBLManagerTable,'h3cNATBLManagerEntry':h3cNATBLManagerEntry,_U:h3cNATBLIpAdress,_V:h3cNATBLSlotNo,'h3cNATBLConSum':h3cNATBLConSum,'h3cNATBLConSpd':h3cNATBLConSpd,'h3cNATStatTable':h3cNATStatTable,'h3cNATStatEntry':h3cNATStatEntry,_W:h3cNATStatNATBoardNo,'h3cNATStatActiveTblCount':h3cNATStatActiveTblCount,'h3cNATStatActiveTblCountInNP':h3cNATStatActiveTblCountInNP,'h3cNATStatActiveNatTblCount':h3cNATStatActiveNatTblCount,'h3cNATStatActiveSvrTblCount':h3cNATStatActiveSvrTblCount,'h3cNATStatActivePoolTblCount':h3cNATStatActivePoolTblCount,'h3cNATStatNumOfUsedPort':h3cNATStatNumOfUsedPort,'h3cNATStatNumOfGoodPkt':h3cNATStatNumOfGoodPkt,'h3cNATStatNumOfBadPkt':h3cNATStatNumOfBadPkt,'h3cNATStaticSessionCount':h3cNATStaticSessionCount,'h3cNATFragmentSessionCount':h3cNATFragmentSessionCount,'h3cNATSequenceSessionCount':h3cNATSequenceSessionCount,'h3cNATLogCount':h3cNATLogCount,'h3cNATSessionTable':h3cNATSessionTable,'h3cNATSessionEntry':h3cNATSessionEntry,_X:h3cNATSessionHashNumber,_Y:h3cNATSessionProtocol,'h3cNATSessionGlobalIP':h3cNATSessionGlobalIP,'h3cNATSessionGlobalPort':h3cNATSessionGlobalPort,_Z:h3cNATSessionInsideIP,_a:h3cNATSessionInsidePort,_b:h3cNATSessionPeerIP,_c:h3cNATSessionPeerPort,_d:h3cNATSessionVpnIndex,'h3cNATSessionTTL':h3cNATSessionTTL,'h3cNATSessionStatus':h3cNATSessionStatus,'h3cNATSessionLeftTime':h3cNATSessionLeftTime,'h3cNATStaticConfTable':h3cNATStaticConfTable,'h3cNATStaticConfEntry':h3cNATStaticConfEntry,_e:h3cNATStaticInsideIp,'h3cNATStaticGlobalIp':h3cNATStaticGlobalIp,'h3cNATStaticRowStatus':h3cNATStaticRowStatus,'h3cNATStaticEnableTable':h3cNATStaticEnableTable,'h3cNATStaticEnableEntry':h3cNATStaticEnableEntry,'h3cNATStaticEnable':h3cNATStaticEnable,'h3cNATDnsMapTable':h3cNATDnsMapTable,'h3cNATDnsMapEntry':h3cNATDnsMapEntry,_f:h3cNATDnsMapDomainName,'h3cNATDnsMapGlobalIp':h3cNATDnsMapGlobalIp,'h3cNATDnsMapGlobalPort':h3cNATDnsMapGlobalPort,'h3cNATDnsMapProtocolType':h3cNATDnsMapProtocolType,'h3cNATDnsMapLastUseTime':h3cNATDnsMapLastUseTime,'h3cNATDnsMapRowStatus':h3cNATDnsMapRowStatus})