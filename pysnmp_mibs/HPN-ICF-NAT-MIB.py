_f='hpnicfNATDnsMapDomainName'
_e='hpnicfNATStaticInsideIp'
_d='hpnicfNATSessionVpnIndex'
_c='hpnicfNATSessionPeerPort'
_b='hpnicfNATSessionPeerIP'
_a='hpnicfNATSessionInsidePort'
_Z='hpnicfNATSessionInsideIP'
_Y='hpnicfNATSessionProtocol'
_X='hpnicfNATSessionHashNumber'
_W='hpnicfNATStatNATBoardNo'
_V='hpnicfNATBLSlotNo'
_U='hpnicfNATBLIpAdress'
_T='hpnicfNATBLIPConnectLimitParaIP'
_S='hpnicfNATBLEnableSlotNo'
_R='hpnicfNATTimeOutProtocol'
_Q='hpnicfNATServerVpnIndex'
_P='hpnicfNATServerStartGlobalPort'
_O='hpnicfNATServerGlobalIP'
_N='hpnicfNATServerProType'
_M='hpnicfNATOutboundAclNo'
_L='hpnicfNATPoolIdx'
_K='disable'
_J='enable'
_I='ifIndex'
_H='IF-MIB'
_G='read-write'
_F='read-only'
_E='not-accessible'
_D='HPN-ICF-NAT-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfNat=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,18))
if mibBuilder.loadTexts:hpnicfNat.setRevisions(('2005-01-20 15:18',))
_HpnicfNATGlobalVars_ObjectIdentity=ObjectIdentity
hpnicfNATGlobalVars=_HpnicfNATGlobalVars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,18,1))
_HpnicfNATClearSession_ObjectIdentity=ObjectIdentity
hpnicfNATClearSession=_HpnicfNATClearSession_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,18,1,1))
class _HpnicfNATClearSessionSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_HpnicfNATClearSessionSlotNo_Type.__name__=_B
_HpnicfNATClearSessionSlotNo_Object=MibScalar
hpnicfNATClearSessionSlotNo=_HpnicfNATClearSessionSlotNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,1,1),_HpnicfNATClearSessionSlotNo_Type())
hpnicfNATClearSessionSlotNo.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATClearSessionSlotNo.setStatus(_A)
_HpnicfNATBLConnectLimitPara_ObjectIdentity=ObjectIdentity
hpnicfNATBLConnectLimitPara=_HpnicfNATBLConnectLimitPara_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,18,1,2))
class _HpnicfNATBLConnectHighValue_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_HpnicfNATBLConnectHighValue_Type.__name__=_B
_HpnicfNATBLConnectHighValue_Object=MibScalar
hpnicfNATBLConnectHighValue=_HpnicfNATBLConnectHighValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,2,1),_HpnicfNATBLConnectHighValue_Type())
hpnicfNATBLConnectHighValue.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLConnectHighValue.setStatus(_A)
class _HpnicfNATBLConnectLowValue_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_HpnicfNATBLConnectLowValue_Type.__name__=_B
_HpnicfNATBLConnectLowValue_Object=MibScalar
hpnicfNATBLConnectLowValue=_HpnicfNATBLConnectLowValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,2,2),_HpnicfNATBLConnectLowValue_Type())
hpnicfNATBLConnectLowValue.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLConnectLowValue.setStatus(_A)
class _HpnicfNATBLConnectHighRate_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_HpnicfNATBLConnectHighRate_Type.__name__=_B
_HpnicfNATBLConnectHighRate_Object=MibScalar
hpnicfNATBLConnectHighRate=_HpnicfNATBLConnectHighRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,2,3),_HpnicfNATBLConnectHighRate_Type())
hpnicfNATBLConnectHighRate.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLConnectHighRate.setStatus(_A)
class _HpnicfNATBLConnectLowRate_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_HpnicfNATBLConnectLowRate_Type.__name__=_B
_HpnicfNATBLConnectLowRate_Object=MibScalar
hpnicfNATBLConnectLowRate=_HpnicfNATBLConnectLowRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,2,4),_HpnicfNATBLConnectLowRate_Type())
hpnicfNATBLConnectLowRate.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLConnectLowRate.setStatus(_A)
class _HpnicfNATBLSpecialConnectHighRate_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_HpnicfNATBLSpecialConnectHighRate_Type.__name__=_B
_HpnicfNATBLSpecialConnectHighRate_Object=MibScalar
hpnicfNATBLSpecialConnectHighRate=_HpnicfNATBLSpecialConnectHighRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,2,5),_HpnicfNATBLSpecialConnectHighRate_Type())
hpnicfNATBLSpecialConnectHighRate.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLSpecialConnectHighRate.setStatus(_A)
class _HpnicfNATBLSpecialConnectLowRate_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,21474836))
_HpnicfNATBLSpecialConnectLowRate_Type.__name__=_B
_HpnicfNATBLSpecialConnectLowRate_Object=MibScalar
hpnicfNATBLSpecialConnectLowRate=_HpnicfNATBLSpecialConnectLowRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,2,6),_HpnicfNATBLSpecialConnectLowRate_Type())
hpnicfNATBLSpecialConnectLowRate.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLSpecialConnectLowRate.setStatus(_A)
_HpnicfNATBLCtrlEnable_ObjectIdentity=ObjectIdentity
hpnicfNATBLCtrlEnable=_HpnicfNATBLCtrlEnable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,18,1,3))
class _HpnicfNATBLConnectSumEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfNATBLConnectSumEnable_Type.__name__=_B
_HpnicfNATBLConnectSumEnable_Object=MibScalar
hpnicfNATBLConnectSumEnable=_HpnicfNATBLConnectSumEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,3,1),_HpnicfNATBLConnectSumEnable_Type())
hpnicfNATBLConnectSumEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLConnectSumEnable.setStatus(_A)
class _HpnicfNATBLConnectRateEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfNATBLConnectRateEnable_Type.__name__=_B
_HpnicfNATBLConnectRateEnable_Object=MibScalar
hpnicfNATBLConnectRateEnable=_HpnicfNATBLConnectRateEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,3,2),_HpnicfNATBLConnectRateEnable_Type())
hpnicfNATBLConnectRateEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLConnectRateEnable.setStatus(_A)
_HpnicfNATNPTimer_ObjectIdentity=ObjectIdentity
hpnicfNATNPTimer=_HpnicfNATNPTimer_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,18,1,4))
class _HpnicfNATNPAgingTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('slow',2)))
_HpnicfNATNPAgingTime_Type.__name__=_B
_HpnicfNATNPAgingTime_Object=MibScalar
hpnicfNATNPAgingTime=_HpnicfNATNPAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,1,4,1),_HpnicfNATNPAgingTime_Type())
hpnicfNATNPAgingTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATNPAgingTime.setStatus(_A)
_HpnicfNATMibObjects_ObjectIdentity=ObjectIdentity
hpnicfNATMibObjects=_HpnicfNATMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,18,2))
_HpnicfNATPoolInfoTable_Object=MibTable
hpnicfNATPoolInfoTable=_HpnicfNATPoolInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1))
if mibBuilder.loadTexts:hpnicfNATPoolInfoTable.setStatus(_A)
_HpnicfNATPoolInfoEntry_Object=MibTableRow
hpnicfNATPoolInfoEntry=_HpnicfNATPoolInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1,1))
hpnicfNATPoolInfoEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:hpnicfNATPoolInfoEntry.setStatus(_A)
class _HpnicfNATPoolIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,320))
_HpnicfNATPoolIdx_Type.__name__=_B
_HpnicfNATPoolIdx_Object=MibTableColumn
hpnicfNATPoolIdx=_HpnicfNATPoolIdx_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1,1,1),_HpnicfNATPoolIdx_Type())
hpnicfNATPoolIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATPoolIdx.setStatus(_A)
_HpnicfNATPoolStartIpAddr_Type=IpAddress
_HpnicfNATPoolStartIpAddr_Object=MibTableColumn
hpnicfNATPoolStartIpAddr=_HpnicfNATPoolStartIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1,1,2),_HpnicfNATPoolStartIpAddr_Type())
hpnicfNATPoolStartIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATPoolStartIpAddr.setStatus(_A)
_HpnicfNATPoolEndIpAddr_Type=IpAddress
_HpnicfNATPoolEndIpAddr_Object=MibTableColumn
hpnicfNATPoolEndIpAddr=_HpnicfNATPoolEndIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1,1,3),_HpnicfNATPoolEndIpAddr_Type())
hpnicfNATPoolEndIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATPoolEndIpAddr.setStatus(_A)
class _HpnicfNATPoolSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_HpnicfNATPoolSlotNo_Type.__name__=_B
_HpnicfNATPoolSlotNo_Object=MibTableColumn
hpnicfNATPoolSlotNo=_HpnicfNATPoolSlotNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1,1,4),_HpnicfNATPoolSlotNo_Type())
hpnicfNATPoolSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATPoolSlotNo.setStatus(_A)
_HpnicfNATPoolRefCounter_Type=Integer32
_HpnicfNATPoolRefCounter_Object=MibTableColumn
hpnicfNATPoolRefCounter=_HpnicfNATPoolRefCounter_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1,1,5),_HpnicfNATPoolRefCounter_Type())
hpnicfNATPoolRefCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATPoolRefCounter.setStatus(_A)
_HpnicfNATPoolRowStatus_Type=RowStatus
_HpnicfNATPoolRowStatus_Object=MibTableColumn
hpnicfNATPoolRowStatus=_HpnicfNATPoolRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,1,1,6),_HpnicfNATPoolRowStatus_Type())
hpnicfNATPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATPoolRowStatus.setStatus(_A)
_HpnicfNATOutboundTable_Object=MibTable
hpnicfNATOutboundTable=_HpnicfNATOutboundTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,2))
if mibBuilder.loadTexts:hpnicfNATOutboundTable.setStatus(_A)
_HpnicfNATOutboundEntry_Object=MibTableRow
hpnicfNATOutboundEntry=_HpnicfNATOutboundEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,2,1))
hpnicfNATOutboundEntry.setIndexNames((0,_H,_I),(0,_D,_M))
if mibBuilder.loadTexts:hpnicfNATOutboundEntry.setStatus(_A)
class _HpnicfNATOutboundAclNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,3999))
_HpnicfNATOutboundAclNo_Type.__name__=_B
_HpnicfNATOutboundAclNo_Object=MibTableColumn
hpnicfNATOutboundAclNo=_HpnicfNATOutboundAclNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,2,1,1),_HpnicfNATOutboundAclNo_Type())
hpnicfNATOutboundAclNo.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATOutboundAclNo.setStatus(_A)
class _HpnicfNATOutboundPoolIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,320),ValueRangeConstraint(2147483647,2147483647))
_HpnicfNATOutboundPoolIdx_Type.__name__=_B
_HpnicfNATOutboundPoolIdx_Object=MibTableColumn
hpnicfNATOutboundPoolIdx=_HpnicfNATOutboundPoolIdx_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,2,1,2),_HpnicfNATOutboundPoolIdx_Type())
hpnicfNATOutboundPoolIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATOutboundPoolIdx.setStatus(_A)
class _HpnicfNATOutboundIsNoPat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HpnicfNATOutboundIsNoPat_Type.__name__=_B
_HpnicfNATOutboundIsNoPat_Object=MibTableColumn
hpnicfNATOutboundIsNoPat=_HpnicfNATOutboundIsNoPat_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,2,1,3),_HpnicfNATOutboundIsNoPat_Type())
hpnicfNATOutboundIsNoPat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATOutboundIsNoPat.setStatus(_A)
class _HpnicfNATOutboundSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_HpnicfNATOutboundSlotNo_Type.__name__=_B
_HpnicfNATOutboundSlotNo_Object=MibTableColumn
hpnicfNATOutboundSlotNo=_HpnicfNATOutboundSlotNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,2,1,4),_HpnicfNATOutboundSlotNo_Type())
hpnicfNATOutboundSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATOutboundSlotNo.setStatus(_A)
_HpnicfNATOutboundRowStatus_Type=RowStatus
_HpnicfNATOutboundRowStatus_Object=MibTableColumn
hpnicfNATOutboundRowStatus=_HpnicfNATOutboundRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,2,1,5),_HpnicfNATOutboundRowStatus_Type())
hpnicfNATOutboundRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATOutboundRowStatus.setStatus(_A)
_HpnicfNATServerTable_Object=MibTable
hpnicfNATServerTable=_HpnicfNATServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3))
if mibBuilder.loadTexts:hpnicfNATServerTable.setStatus(_A)
_HpnicfNATServerEntry_Object=MibTableRow
hpnicfNATServerEntry=_HpnicfNATServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1))
hpnicfNATServerEntry.setIndexNames((0,_H,_I),(0,_D,_N),(0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:hpnicfNATServerEntry.setStatus(_A)
class _HpnicfNATServerProType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfNATServerProType_Type.__name__=_B
_HpnicfNATServerProType_Object=MibTableColumn
hpnicfNATServerProType=_HpnicfNATServerProType_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,1),_HpnicfNATServerProType_Type())
hpnicfNATServerProType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATServerProType.setStatus(_A)
_HpnicfNATServerGlobalIP_Type=IpAddress
_HpnicfNATServerGlobalIP_Object=MibTableColumn
hpnicfNATServerGlobalIP=_HpnicfNATServerGlobalIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,2),_HpnicfNATServerGlobalIP_Type())
hpnicfNATServerGlobalIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATServerGlobalIP.setStatus(_A)
class _HpnicfNATServerStartGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNATServerStartGlobalPort_Type.__name__=_B
_HpnicfNATServerStartGlobalPort_Object=MibTableColumn
hpnicfNATServerStartGlobalPort=_HpnicfNATServerStartGlobalPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,3),_HpnicfNATServerStartGlobalPort_Type())
hpnicfNATServerStartGlobalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATServerStartGlobalPort.setStatus(_A)
class _HpnicfNATServerEndGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNATServerEndGlobalPort_Type.__name__=_B
_HpnicfNATServerEndGlobalPort_Object=MibTableColumn
hpnicfNATServerEndGlobalPort=_HpnicfNATServerEndGlobalPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,4),_HpnicfNATServerEndGlobalPort_Type())
hpnicfNATServerEndGlobalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATServerEndGlobalPort.setStatus(_A)
_HpnicfNATServerStartInsideIP_Type=IpAddress
_HpnicfNATServerStartInsideIP_Object=MibTableColumn
hpnicfNATServerStartInsideIP=_HpnicfNATServerStartInsideIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,5),_HpnicfNATServerStartInsideIP_Type())
hpnicfNATServerStartInsideIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATServerStartInsideIP.setStatus(_A)
_HpnicfNATServerEndInsideIP_Type=IpAddress
_HpnicfNATServerEndInsideIP_Object=MibTableColumn
hpnicfNATServerEndInsideIP=_HpnicfNATServerEndInsideIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,6),_HpnicfNATServerEndInsideIP_Type())
hpnicfNATServerEndInsideIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATServerEndInsideIP.setStatus(_A)
class _HpnicfNATServerInsidePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNATServerInsidePort_Type.__name__=_B
_HpnicfNATServerInsidePort_Object=MibTableColumn
hpnicfNATServerInsidePort=_HpnicfNATServerInsidePort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,7),_HpnicfNATServerInsidePort_Type())
hpnicfNATServerInsidePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATServerInsidePort.setStatus(_A)
class _HpnicfNATServerSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_HpnicfNATServerSlotNo_Type.__name__=_B
_HpnicfNATServerSlotNo_Object=MibTableColumn
hpnicfNATServerSlotNo=_HpnicfNATServerSlotNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,8),_HpnicfNATServerSlotNo_Type())
hpnicfNATServerSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATServerSlotNo.setStatus(_A)
class _HpnicfNATServerVpnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNATServerVpnIndex_Type.__name__=_B
_HpnicfNATServerVpnIndex_Object=MibTableColumn
hpnicfNATServerVpnIndex=_HpnicfNATServerVpnIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,10),_HpnicfNATServerVpnIndex_Type())
hpnicfNATServerVpnIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATServerVpnIndex.setStatus(_A)
class _HpnicfNATServerAclNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_HpnicfNATServerAclNumber_Type.__name__=_B
_HpnicfNATServerAclNumber_Object=MibTableColumn
hpnicfNATServerAclNumber=_HpnicfNATServerAclNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,11),_HpnicfNATServerAclNumber_Type())
hpnicfNATServerAclNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATServerAclNumber.setStatus(_A)
_HpnicfNATServerRowStatus_Type=RowStatus
_HpnicfNATServerRowStatus_Object=MibTableColumn
hpnicfNATServerRowStatus=_HpnicfNATServerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,3,1,12),_HpnicfNATServerRowStatus_Type())
hpnicfNATServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATServerRowStatus.setStatus(_A)
_HpnicfNATTimeOutTable_Object=MibTable
hpnicfNATTimeOutTable=_HpnicfNATTimeOutTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,4))
if mibBuilder.loadTexts:hpnicfNATTimeOutTable.setStatus(_A)
_HpnicfNATTimeOutEntry_Object=MibTableRow
hpnicfNATTimeOutEntry=_HpnicfNATTimeOutEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,4,1))
hpnicfNATTimeOutEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:hpnicfNATTimeOutEntry.setStatus(_A)
class _HpnicfNATTimeOutProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('tcp',1),('udp',2),('icmp',3),('pptp',4),('dns',5),('tcpFin',6),('tcpSyn',7),('ftpCtrl',8),('ftpData',9)))
_HpnicfNATTimeOutProtocol_Type.__name__=_B
_HpnicfNATTimeOutProtocol_Object=MibTableColumn
hpnicfNATTimeOutProtocol=_HpnicfNATTimeOutProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,4,1,1),_HpnicfNATTimeOutProtocol_Type())
hpnicfNATTimeOutProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATTimeOutProtocol.setStatus(_A)
class _HpnicfNATTimeOutTimeValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,86400))
_HpnicfNATTimeOutTimeValue_Type.__name__=_B
_HpnicfNATTimeOutTimeValue_Object=MibTableColumn
hpnicfNATTimeOutTimeValue=_HpnicfNATTimeOutTimeValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,4,1,2),_HpnicfNATTimeOutTimeValue_Type())
hpnicfNATTimeOutTimeValue.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATTimeOutTimeValue.setStatus(_A)
_HpnicfNATBLEnableTable_Object=MibTable
hpnicfNATBLEnableTable=_HpnicfNATBLEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,5))
if mibBuilder.loadTexts:hpnicfNATBLEnableTable.setStatus(_A)
_HpnicfNATBLEnableEntry_Object=MibTableRow
hpnicfNATBLEnableEntry=_HpnicfNATBLEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,5,1))
hpnicfNATBLEnableEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:hpnicfNATBLEnableEntry.setStatus(_A)
class _HpnicfNATBLEnableSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_HpnicfNATBLEnableSlotNo_Type.__name__=_B
_HpnicfNATBLEnableSlotNo_Object=MibTableColumn
hpnicfNATBLEnableSlotNo=_HpnicfNATBLEnableSlotNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,5,1,1),_HpnicfNATBLEnableSlotNo_Type())
hpnicfNATBLEnableSlotNo.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATBLEnableSlotNo.setStatus(_A)
class _HpnicfNATBLEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfNATBLEnable_Type.__name__=_B
_HpnicfNATBLEnable_Object=MibTableColumn
hpnicfNATBLEnable=_HpnicfNATBLEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,5,1,2),_HpnicfNATBLEnable_Type())
hpnicfNATBLEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATBLEnable.setStatus(_A)
_HpnicfNATBLIPConnectLimitParaTable_Object=MibTable
hpnicfNATBLIPConnectLimitParaTable=_HpnicfNATBLIPConnectLimitParaTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,6))
if mibBuilder.loadTexts:hpnicfNATBLIPConnectLimitParaTable.setStatus(_A)
_HpnicfNATBLIPConnectLimitParaEntry_Object=MibTableRow
hpnicfNATBLIPConnectLimitParaEntry=_HpnicfNATBLIPConnectLimitParaEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,6,1))
hpnicfNATBLIPConnectLimitParaEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:hpnicfNATBLIPConnectLimitParaEntry.setStatus(_A)
_HpnicfNATBLIPConnectLimitParaIP_Type=IpAddress
_HpnicfNATBLIPConnectLimitParaIP_Object=MibTableColumn
hpnicfNATBLIPConnectLimitParaIP=_HpnicfNATBLIPConnectLimitParaIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,6,1,1),_HpnicfNATBLIPConnectLimitParaIP_Type())
hpnicfNATBLIPConnectLimitParaIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATBLIPConnectLimitParaIP.setStatus(_A)
class _HpnicfNATBLIPConnectHighValue_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_HpnicfNATBLIPConnectHighValue_Type.__name__=_B
_HpnicfNATBLIPConnectHighValue_Object=MibTableColumn
hpnicfNATBLIPConnectHighValue=_HpnicfNATBLIPConnectHighValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,6,1,2),_HpnicfNATBLIPConnectHighValue_Type())
hpnicfNATBLIPConnectHighValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATBLIPConnectHighValue.setStatus(_A)
class _HpnicfNATBLIPConnectLowValue_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20000))
_HpnicfNATBLIPConnectLowValue_Type.__name__=_B
_HpnicfNATBLIPConnectLowValue_Object=MibTableColumn
hpnicfNATBLIPConnectLowValue=_HpnicfNATBLIPConnectLowValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,6,1,3),_HpnicfNATBLIPConnectLowValue_Type())
hpnicfNATBLIPConnectLowValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATBLIPConnectLowValue.setStatus(_A)
class _HpnicfNATBLIPUseSpecialConnectRate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HpnicfNATBLIPUseSpecialConnectRate_Type.__name__=_B
_HpnicfNATBLIPUseSpecialConnectRate_Object=MibTableColumn
hpnicfNATBLIPUseSpecialConnectRate=_HpnicfNATBLIPUseSpecialConnectRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,6,1,4),_HpnicfNATBLIPUseSpecialConnectRate_Type())
hpnicfNATBLIPUseSpecialConnectRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATBLIPUseSpecialConnectRate.setStatus(_A)
_HpnicfNATBLIPConnectLimitRowStatus_Type=RowStatus
_HpnicfNATBLIPConnectLimitRowStatus_Object=MibTableColumn
hpnicfNATBLIPConnectLimitRowStatus=_HpnicfNATBLIPConnectLimitRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,6,1,5),_HpnicfNATBLIPConnectLimitRowStatus_Type())
hpnicfNATBLIPConnectLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATBLIPConnectLimitRowStatus.setStatus(_A)
_HpnicfNATBLManagerTable_Object=MibTable
hpnicfNATBLManagerTable=_HpnicfNATBLManagerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,7))
if mibBuilder.loadTexts:hpnicfNATBLManagerTable.setStatus(_A)
_HpnicfNATBLManagerEntry_Object=MibTableRow
hpnicfNATBLManagerEntry=_HpnicfNATBLManagerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,7,1))
hpnicfNATBLManagerEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:hpnicfNATBLManagerEntry.setStatus(_A)
_HpnicfNATBLIpAdress_Type=IpAddress
_HpnicfNATBLIpAdress_Object=MibTableColumn
hpnicfNATBLIpAdress=_HpnicfNATBLIpAdress_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,7,1,1),_HpnicfNATBLIpAdress_Type())
hpnicfNATBLIpAdress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATBLIpAdress.setStatus(_A)
class _HpnicfNATBLSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_HpnicfNATBLSlotNo_Type.__name__=_B
_HpnicfNATBLSlotNo_Object=MibTableColumn
hpnicfNATBLSlotNo=_HpnicfNATBLSlotNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,7,1,2),_HpnicfNATBLSlotNo_Type())
hpnicfNATBLSlotNo.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATBLSlotNo.setStatus(_A)
_HpnicfNATBLConSum_Type=Integer32
_HpnicfNATBLConSum_Object=MibTableColumn
hpnicfNATBLConSum=_HpnicfNATBLConSum_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,7,1,3),_HpnicfNATBLConSum_Type())
hpnicfNATBLConSum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATBLConSum.setStatus(_A)
class _HpnicfNATBLConSpd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('red',1),('yellow',2),('green',3)))
_HpnicfNATBLConSpd_Type.__name__=_B
_HpnicfNATBLConSpd_Object=MibTableColumn
hpnicfNATBLConSpd=_HpnicfNATBLConSpd_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,7,1,4),_HpnicfNATBLConSpd_Type())
hpnicfNATBLConSpd.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATBLConSpd.setStatus(_A)
_HpnicfNATStatTable_Object=MibTable
hpnicfNATStatTable=_HpnicfNATStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8))
if mibBuilder.loadTexts:hpnicfNATStatTable.setStatus(_A)
_HpnicfNATStatEntry_Object=MibTableRow
hpnicfNATStatEntry=_HpnicfNATStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1))
hpnicfNATStatEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:hpnicfNATStatEntry.setStatus(_A)
class _HpnicfNATStatNATBoardNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14),ValueRangeConstraint(255,255))
_HpnicfNATStatNATBoardNo_Type.__name__=_B
_HpnicfNATStatNATBoardNo_Object=MibTableColumn
hpnicfNATStatNATBoardNo=_HpnicfNATStatNATBoardNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,1),_HpnicfNATStatNATBoardNo_Type())
hpnicfNATStatNATBoardNo.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATStatNATBoardNo.setStatus(_A)
_HpnicfNATStatActiveTblCount_Type=Counter32
_HpnicfNATStatActiveTblCount_Object=MibTableColumn
hpnicfNATStatActiveTblCount=_HpnicfNATStatActiveTblCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,2),_HpnicfNATStatActiveTblCount_Type())
hpnicfNATStatActiveTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatActiveTblCount.setStatus(_A)
_HpnicfNATStatActiveTblCountInNP_Type=Counter32
_HpnicfNATStatActiveTblCountInNP_Object=MibTableColumn
hpnicfNATStatActiveTblCountInNP=_HpnicfNATStatActiveTblCountInNP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,3),_HpnicfNATStatActiveTblCountInNP_Type())
hpnicfNATStatActiveTblCountInNP.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatActiveTblCountInNP.setStatus(_A)
_HpnicfNATStatActiveNatTblCount_Type=Counter32
_HpnicfNATStatActiveNatTblCount_Object=MibTableColumn
hpnicfNATStatActiveNatTblCount=_HpnicfNATStatActiveNatTblCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,4),_HpnicfNATStatActiveNatTblCount_Type())
hpnicfNATStatActiveNatTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatActiveNatTblCount.setStatus(_A)
_HpnicfNATStatActiveSvrTblCount_Type=Counter32
_HpnicfNATStatActiveSvrTblCount_Object=MibTableColumn
hpnicfNATStatActiveSvrTblCount=_HpnicfNATStatActiveSvrTblCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,5),_HpnicfNATStatActiveSvrTblCount_Type())
hpnicfNATStatActiveSvrTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatActiveSvrTblCount.setStatus(_A)
_HpnicfNATStatActivePoolTblCount_Type=Counter32
_HpnicfNATStatActivePoolTblCount_Object=MibTableColumn
hpnicfNATStatActivePoolTblCount=_HpnicfNATStatActivePoolTblCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,6),_HpnicfNATStatActivePoolTblCount_Type())
hpnicfNATStatActivePoolTblCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatActivePoolTblCount.setStatus(_A)
_HpnicfNATStatNumOfUsedPort_Type=Counter32
_HpnicfNATStatNumOfUsedPort_Object=MibTableColumn
hpnicfNATStatNumOfUsedPort=_HpnicfNATStatNumOfUsedPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,7),_HpnicfNATStatNumOfUsedPort_Type())
hpnicfNATStatNumOfUsedPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatNumOfUsedPort.setStatus(_A)
_HpnicfNATStatNumOfGoodPkt_Type=Counter32
_HpnicfNATStatNumOfGoodPkt_Object=MibTableColumn
hpnicfNATStatNumOfGoodPkt=_HpnicfNATStatNumOfGoodPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,8),_HpnicfNATStatNumOfGoodPkt_Type())
hpnicfNATStatNumOfGoodPkt.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatNumOfGoodPkt.setStatus(_A)
_HpnicfNATStatNumOfBadPkt_Type=Counter32
_HpnicfNATStatNumOfBadPkt_Object=MibTableColumn
hpnicfNATStatNumOfBadPkt=_HpnicfNATStatNumOfBadPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,9),_HpnicfNATStatNumOfBadPkt_Type())
hpnicfNATStatNumOfBadPkt.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStatNumOfBadPkt.setStatus(_A)
_HpnicfNATStaticSessionCount_Type=Integer32
_HpnicfNATStaticSessionCount_Object=MibTableColumn
hpnicfNATStaticSessionCount=_HpnicfNATStaticSessionCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,10),_HpnicfNATStaticSessionCount_Type())
hpnicfNATStaticSessionCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATStaticSessionCount.setStatus(_A)
_HpnicfNATFragmentSessionCount_Type=Integer32
_HpnicfNATFragmentSessionCount_Object=MibTableColumn
hpnicfNATFragmentSessionCount=_HpnicfNATFragmentSessionCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,11),_HpnicfNATFragmentSessionCount_Type())
hpnicfNATFragmentSessionCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATFragmentSessionCount.setStatus(_A)
_HpnicfNATSequenceSessionCount_Type=Integer32
_HpnicfNATSequenceSessionCount_Object=MibTableColumn
hpnicfNATSequenceSessionCount=_HpnicfNATSequenceSessionCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,12),_HpnicfNATSequenceSessionCount_Type())
hpnicfNATSequenceSessionCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATSequenceSessionCount.setStatus(_A)
_HpnicfNATLogCount_Type=Integer32
_HpnicfNATLogCount_Object=MibTableColumn
hpnicfNATLogCount=_HpnicfNATLogCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,8,1,13),_HpnicfNATLogCount_Type())
hpnicfNATLogCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATLogCount.setStatus(_A)
_HpnicfNATSessionTable_Object=MibTable
hpnicfNATSessionTable=_HpnicfNATSessionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9))
if mibBuilder.loadTexts:hpnicfNATSessionTable.setStatus(_A)
_HpnicfNATSessionEntry_Object=MibTableRow
hpnicfNATSessionEntry=_HpnicfNATSessionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1))
hpnicfNATSessionEntry.setIndexNames((0,_D,_X),(0,_D,_Y),(0,_D,_Z),(0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:hpnicfNATSessionEntry.setStatus(_A)
class _HpnicfNATSessionHashNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300000))
_HpnicfNATSessionHashNumber_Type.__name__=_B
_HpnicfNATSessionHashNumber_Object=MibTableColumn
hpnicfNATSessionHashNumber=_HpnicfNATSessionHashNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,1),_HpnicfNATSessionHashNumber_Type())
hpnicfNATSessionHashNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATSessionHashNumber.setStatus(_A)
class _HpnicfNATSessionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfNATSessionProtocol_Type.__name__=_B
_HpnicfNATSessionProtocol_Object=MibTableColumn
hpnicfNATSessionProtocol=_HpnicfNATSessionProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,2),_HpnicfNATSessionProtocol_Type())
hpnicfNATSessionProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATSessionProtocol.setStatus(_A)
_HpnicfNATSessionGlobalIP_Type=IpAddress
_HpnicfNATSessionGlobalIP_Object=MibTableColumn
hpnicfNATSessionGlobalIP=_HpnicfNATSessionGlobalIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,3),_HpnicfNATSessionGlobalIP_Type())
hpnicfNATSessionGlobalIP.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATSessionGlobalIP.setStatus(_A)
class _HpnicfNATSessionGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNATSessionGlobalPort_Type.__name__=_B
_HpnicfNATSessionGlobalPort_Object=MibTableColumn
hpnicfNATSessionGlobalPort=_HpnicfNATSessionGlobalPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,4),_HpnicfNATSessionGlobalPort_Type())
hpnicfNATSessionGlobalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATSessionGlobalPort.setStatus(_A)
_HpnicfNATSessionInsideIP_Type=IpAddress
_HpnicfNATSessionInsideIP_Object=MibTableColumn
hpnicfNATSessionInsideIP=_HpnicfNATSessionInsideIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,5),_HpnicfNATSessionInsideIP_Type())
hpnicfNATSessionInsideIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATSessionInsideIP.setStatus(_A)
class _HpnicfNATSessionInsidePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNATSessionInsidePort_Type.__name__=_B
_HpnicfNATSessionInsidePort_Object=MibTableColumn
hpnicfNATSessionInsidePort=_HpnicfNATSessionInsidePort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,6),_HpnicfNATSessionInsidePort_Type())
hpnicfNATSessionInsidePort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATSessionInsidePort.setStatus(_A)
_HpnicfNATSessionPeerIP_Type=IpAddress
_HpnicfNATSessionPeerIP_Object=MibTableColumn
hpnicfNATSessionPeerIP=_HpnicfNATSessionPeerIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,7),_HpnicfNATSessionPeerIP_Type())
hpnicfNATSessionPeerIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATSessionPeerIP.setStatus(_A)
class _HpnicfNATSessionPeerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfNATSessionPeerPort_Type.__name__=_B
_HpnicfNATSessionPeerPort_Object=MibTableColumn
hpnicfNATSessionPeerPort=_HpnicfNATSessionPeerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,8),_HpnicfNATSessionPeerPort_Type())
hpnicfNATSessionPeerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATSessionPeerPort.setStatus(_A)
class _HpnicfNATSessionVpnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfNATSessionVpnIndex_Type.__name__=_B
_HpnicfNATSessionVpnIndex_Object=MibTableColumn
hpnicfNATSessionVpnIndex=_HpnicfNATSessionVpnIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,9),_HpnicfNATSessionVpnIndex_Type())
hpnicfNATSessionVpnIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATSessionVpnIndex.setStatus(_A)
_HpnicfNATSessionTTL_Type=Integer32
_HpnicfNATSessionTTL_Object=MibTableColumn
hpnicfNATSessionTTL=_HpnicfNATSessionTTL_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,10),_HpnicfNATSessionTTL_Type())
hpnicfNATSessionTTL.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATSessionTTL.setStatus(_A)
_HpnicfNATSessionStatus_Type=Integer32
_HpnicfNATSessionStatus_Object=MibTableColumn
hpnicfNATSessionStatus=_HpnicfNATSessionStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,11),_HpnicfNATSessionStatus_Type())
hpnicfNATSessionStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATSessionStatus.setStatus(_A)
_HpnicfNATSessionLeftTime_Type=TimeTicks
_HpnicfNATSessionLeftTime_Object=MibTableColumn
hpnicfNATSessionLeftTime=_HpnicfNATSessionLeftTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,9,1,12),_HpnicfNATSessionLeftTime_Type())
hpnicfNATSessionLeftTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNATSessionLeftTime.setStatus(_A)
_HpnicfNATStaticConfTable_Object=MibTable
hpnicfNATStaticConfTable=_HpnicfNATStaticConfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,10))
if mibBuilder.loadTexts:hpnicfNATStaticConfTable.setStatus(_A)
_HpnicfNATStaticConfEntry_Object=MibTableRow
hpnicfNATStaticConfEntry=_HpnicfNATStaticConfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,10,1))
hpnicfNATStaticConfEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:hpnicfNATStaticConfEntry.setStatus(_A)
_HpnicfNATStaticInsideIp_Type=IpAddress
_HpnicfNATStaticInsideIp_Object=MibTableColumn
hpnicfNATStaticInsideIp=_HpnicfNATStaticInsideIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,10,1,1),_HpnicfNATStaticInsideIp_Type())
hpnicfNATStaticInsideIp.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATStaticInsideIp.setStatus(_A)
_HpnicfNATStaticGlobalIp_Type=IpAddress
_HpnicfNATStaticGlobalIp_Object=MibTableColumn
hpnicfNATStaticGlobalIp=_HpnicfNATStaticGlobalIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,10,1,2),_HpnicfNATStaticGlobalIp_Type())
hpnicfNATStaticGlobalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATStaticGlobalIp.setStatus(_A)
_HpnicfNATStaticRowStatus_Type=RowStatus
_HpnicfNATStaticRowStatus_Object=MibTableColumn
hpnicfNATStaticRowStatus=_HpnicfNATStaticRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,10,1,3),_HpnicfNATStaticRowStatus_Type())
hpnicfNATStaticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATStaticRowStatus.setStatus(_A)
_HpnicfNATStaticEnableTable_Object=MibTable
hpnicfNATStaticEnableTable=_HpnicfNATStaticEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,11))
if mibBuilder.loadTexts:hpnicfNATStaticEnableTable.setStatus(_A)
_HpnicfNATStaticEnableEntry_Object=MibTableRow
hpnicfNATStaticEnableEntry=_HpnicfNATStaticEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,11,1))
hpnicfNATStaticEnableEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfNATStaticEnableEntry.setStatus(_A)
class _HpnicfNATStaticEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_J,1)))
_HpnicfNATStaticEnable_Type.__name__=_B
_HpnicfNATStaticEnable_Object=MibTableColumn
hpnicfNATStaticEnable=_HpnicfNATStaticEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,11,1,2),_HpnicfNATStaticEnable_Type())
hpnicfNATStaticEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNATStaticEnable.setStatus(_A)
_HpnicfNATDnsMapTable_Object=MibTable
hpnicfNATDnsMapTable=_HpnicfNATDnsMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12))
if mibBuilder.loadTexts:hpnicfNATDnsMapTable.setStatus(_A)
_HpnicfNATDnsMapEntry_Object=MibTableRow
hpnicfNATDnsMapEntry=_HpnicfNATDnsMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12,1))
hpnicfNATDnsMapEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:hpnicfNATDnsMapEntry.setStatus(_A)
_HpnicfNATDnsMapDomainName_Type=DisplayString
_HpnicfNATDnsMapDomainName_Object=MibTableColumn
hpnicfNATDnsMapDomainName=_HpnicfNATDnsMapDomainName_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12,1,1),_HpnicfNATDnsMapDomainName_Type())
hpnicfNATDnsMapDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNATDnsMapDomainName.setStatus(_A)
_HpnicfNATDnsMapGlobalIp_Type=IpAddress
_HpnicfNATDnsMapGlobalIp_Object=MibTableColumn
hpnicfNATDnsMapGlobalIp=_HpnicfNATDnsMapGlobalIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12,1,2),_HpnicfNATDnsMapGlobalIp_Type())
hpnicfNATDnsMapGlobalIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATDnsMapGlobalIp.setStatus(_A)
class _HpnicfNATDnsMapGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfNATDnsMapGlobalPort_Type.__name__=_B
_HpnicfNATDnsMapGlobalPort_Object=MibTableColumn
hpnicfNATDnsMapGlobalPort=_HpnicfNATDnsMapGlobalPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12,1,3),_HpnicfNATDnsMapGlobalPort_Type())
hpnicfNATDnsMapGlobalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATDnsMapGlobalPort.setStatus(_A)
class _HpnicfNATDnsMapProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('any',0),('typeTCP',1),('typeUDP',2)))
_HpnicfNATDnsMapProtocolType_Type.__name__=_B
_HpnicfNATDnsMapProtocolType_Object=MibTableColumn
hpnicfNATDnsMapProtocolType=_HpnicfNATDnsMapProtocolType_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12,1,4),_HpnicfNATDnsMapProtocolType_Type())
hpnicfNATDnsMapProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATDnsMapProtocolType.setStatus(_A)
_HpnicfNATDnsMapLastUseTime_Type=TimeTicks
_HpnicfNATDnsMapLastUseTime_Object=MibTableColumn
hpnicfNATDnsMapLastUseTime=_HpnicfNATDnsMapLastUseTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12,1,5),_HpnicfNATDnsMapLastUseTime_Type())
hpnicfNATDnsMapLastUseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATDnsMapLastUseTime.setStatus(_A)
_HpnicfNATDnsMapRowStatus_Type=RowStatus
_HpnicfNATDnsMapRowStatus_Object=MibTableColumn
hpnicfNATDnsMapRowStatus=_HpnicfNATDnsMapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,18,2,12,1,6),_HpnicfNATDnsMapRowStatus_Type())
hpnicfNATDnsMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfNATDnsMapRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfNat':hpnicfNat,'hpnicfNATGlobalVars':hpnicfNATGlobalVars,'hpnicfNATClearSession':hpnicfNATClearSession,'hpnicfNATClearSessionSlotNo':hpnicfNATClearSessionSlotNo,'hpnicfNATBLConnectLimitPara':hpnicfNATBLConnectLimitPara,'hpnicfNATBLConnectHighValue':hpnicfNATBLConnectHighValue,'hpnicfNATBLConnectLowValue':hpnicfNATBLConnectLowValue,'hpnicfNATBLConnectHighRate':hpnicfNATBLConnectHighRate,'hpnicfNATBLConnectLowRate':hpnicfNATBLConnectLowRate,'hpnicfNATBLSpecialConnectHighRate':hpnicfNATBLSpecialConnectHighRate,'hpnicfNATBLSpecialConnectLowRate':hpnicfNATBLSpecialConnectLowRate,'hpnicfNATBLCtrlEnable':hpnicfNATBLCtrlEnable,'hpnicfNATBLConnectSumEnable':hpnicfNATBLConnectSumEnable,'hpnicfNATBLConnectRateEnable':hpnicfNATBLConnectRateEnable,'hpnicfNATNPTimer':hpnicfNATNPTimer,'hpnicfNATNPAgingTime':hpnicfNATNPAgingTime,'hpnicfNATMibObjects':hpnicfNATMibObjects,'hpnicfNATPoolInfoTable':hpnicfNATPoolInfoTable,'hpnicfNATPoolInfoEntry':hpnicfNATPoolInfoEntry,_L:hpnicfNATPoolIdx,'hpnicfNATPoolStartIpAddr':hpnicfNATPoolStartIpAddr,'hpnicfNATPoolEndIpAddr':hpnicfNATPoolEndIpAddr,'hpnicfNATPoolSlotNo':hpnicfNATPoolSlotNo,'hpnicfNATPoolRefCounter':hpnicfNATPoolRefCounter,'hpnicfNATPoolRowStatus':hpnicfNATPoolRowStatus,'hpnicfNATOutboundTable':hpnicfNATOutboundTable,'hpnicfNATOutboundEntry':hpnicfNATOutboundEntry,_M:hpnicfNATOutboundAclNo,'hpnicfNATOutboundPoolIdx':hpnicfNATOutboundPoolIdx,'hpnicfNATOutboundIsNoPat':hpnicfNATOutboundIsNoPat,'hpnicfNATOutboundSlotNo':hpnicfNATOutboundSlotNo,'hpnicfNATOutboundRowStatus':hpnicfNATOutboundRowStatus,'hpnicfNATServerTable':hpnicfNATServerTable,'hpnicfNATServerEntry':hpnicfNATServerEntry,_N:hpnicfNATServerProType,_O:hpnicfNATServerGlobalIP,_P:hpnicfNATServerStartGlobalPort,'hpnicfNATServerEndGlobalPort':hpnicfNATServerEndGlobalPort,'hpnicfNATServerStartInsideIP':hpnicfNATServerStartInsideIP,'hpnicfNATServerEndInsideIP':hpnicfNATServerEndInsideIP,'hpnicfNATServerInsidePort':hpnicfNATServerInsidePort,'hpnicfNATServerSlotNo':hpnicfNATServerSlotNo,_Q:hpnicfNATServerVpnIndex,'hpnicfNATServerAclNumber':hpnicfNATServerAclNumber,'hpnicfNATServerRowStatus':hpnicfNATServerRowStatus,'hpnicfNATTimeOutTable':hpnicfNATTimeOutTable,'hpnicfNATTimeOutEntry':hpnicfNATTimeOutEntry,_R:hpnicfNATTimeOutProtocol,'hpnicfNATTimeOutTimeValue':hpnicfNATTimeOutTimeValue,'hpnicfNATBLEnableTable':hpnicfNATBLEnableTable,'hpnicfNATBLEnableEntry':hpnicfNATBLEnableEntry,_S:hpnicfNATBLEnableSlotNo,'hpnicfNATBLEnable':hpnicfNATBLEnable,'hpnicfNATBLIPConnectLimitParaTable':hpnicfNATBLIPConnectLimitParaTable,'hpnicfNATBLIPConnectLimitParaEntry':hpnicfNATBLIPConnectLimitParaEntry,_T:hpnicfNATBLIPConnectLimitParaIP,'hpnicfNATBLIPConnectHighValue':hpnicfNATBLIPConnectHighValue,'hpnicfNATBLIPConnectLowValue':hpnicfNATBLIPConnectLowValue,'hpnicfNATBLIPUseSpecialConnectRate':hpnicfNATBLIPUseSpecialConnectRate,'hpnicfNATBLIPConnectLimitRowStatus':hpnicfNATBLIPConnectLimitRowStatus,'hpnicfNATBLManagerTable':hpnicfNATBLManagerTable,'hpnicfNATBLManagerEntry':hpnicfNATBLManagerEntry,_U:hpnicfNATBLIpAdress,_V:hpnicfNATBLSlotNo,'hpnicfNATBLConSum':hpnicfNATBLConSum,'hpnicfNATBLConSpd':hpnicfNATBLConSpd,'hpnicfNATStatTable':hpnicfNATStatTable,'hpnicfNATStatEntry':hpnicfNATStatEntry,_W:hpnicfNATStatNATBoardNo,'hpnicfNATStatActiveTblCount':hpnicfNATStatActiveTblCount,'hpnicfNATStatActiveTblCountInNP':hpnicfNATStatActiveTblCountInNP,'hpnicfNATStatActiveNatTblCount':hpnicfNATStatActiveNatTblCount,'hpnicfNATStatActiveSvrTblCount':hpnicfNATStatActiveSvrTblCount,'hpnicfNATStatActivePoolTblCount':hpnicfNATStatActivePoolTblCount,'hpnicfNATStatNumOfUsedPort':hpnicfNATStatNumOfUsedPort,'hpnicfNATStatNumOfGoodPkt':hpnicfNATStatNumOfGoodPkt,'hpnicfNATStatNumOfBadPkt':hpnicfNATStatNumOfBadPkt,'hpnicfNATStaticSessionCount':hpnicfNATStaticSessionCount,'hpnicfNATFragmentSessionCount':hpnicfNATFragmentSessionCount,'hpnicfNATSequenceSessionCount':hpnicfNATSequenceSessionCount,'hpnicfNATLogCount':hpnicfNATLogCount,'hpnicfNATSessionTable':hpnicfNATSessionTable,'hpnicfNATSessionEntry':hpnicfNATSessionEntry,_X:hpnicfNATSessionHashNumber,_Y:hpnicfNATSessionProtocol,'hpnicfNATSessionGlobalIP':hpnicfNATSessionGlobalIP,'hpnicfNATSessionGlobalPort':hpnicfNATSessionGlobalPort,_Z:hpnicfNATSessionInsideIP,_a:hpnicfNATSessionInsidePort,_b:hpnicfNATSessionPeerIP,_c:hpnicfNATSessionPeerPort,_d:hpnicfNATSessionVpnIndex,'hpnicfNATSessionTTL':hpnicfNATSessionTTL,'hpnicfNATSessionStatus':hpnicfNATSessionStatus,'hpnicfNATSessionLeftTime':hpnicfNATSessionLeftTime,'hpnicfNATStaticConfTable':hpnicfNATStaticConfTable,'hpnicfNATStaticConfEntry':hpnicfNATStaticConfEntry,_e:hpnicfNATStaticInsideIp,'hpnicfNATStaticGlobalIp':hpnicfNATStaticGlobalIp,'hpnicfNATStaticRowStatus':hpnicfNATStaticRowStatus,'hpnicfNATStaticEnableTable':hpnicfNATStaticEnableTable,'hpnicfNATStaticEnableEntry':hpnicfNATStaticEnableEntry,'hpnicfNATStaticEnable':hpnicfNATStaticEnable,'hpnicfNATDnsMapTable':hpnicfNATDnsMapTable,'hpnicfNATDnsMapEntry':hpnicfNATDnsMapEntry,_f:hpnicfNATDnsMapDomainName,'hpnicfNATDnsMapGlobalIp':hpnicfNATDnsMapGlobalIp,'hpnicfNATDnsMapGlobalPort':hpnicfNATDnsMapGlobalPort,'hpnicfNATDnsMapProtocolType':hpnicfNATDnsMapProtocolType,'hpnicfNATDnsMapLastUseTime':hpnicfNATDnsMapLastUseTime,'hpnicfNATDnsMapRowStatus':hpnicfNATDnsMapRowStatus})