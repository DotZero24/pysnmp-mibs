_A6='atiL2TrapAttrPortId'
_A5='atiL2TrafficClassIndex'
_A4='not-accessible'
_A3='atiL2BrTpPort'
_A2='atiL2BrTpPortLanId'
_A1='atiL2BrTpFdbAddress'
_A0='atiL2BrTpFdbLanId'
_z='atiL2BrTpLanId'
_y='atiL2BrStpPort'
_x='atiL2BrStpPortLanId'
_w='atiL2BrStpLanId'
_v='atiL2BrBasePort'
_u='atiL2BrBasePortLanId'
_t='atiL2BrBaseLanId'
_s='atiIfExtnIndex'
_r='atiL2PvPortNumber'
_q='atiL2PvModuleId'
_p='atiL2BeVlanIndex'
_o='learning'
_n='listening'
_m='blocking'
_l='enabled'
_k='atiL2DevicePortNumber'
_j='atiL2DeviceId'
_i='atiL2EthPortErrPortId'
_h='atiL2EthPortErrModuleId'
_g='atiL2EthErrModuleId'
_f='atiL2EthPortMonPortId'
_e='atiL2EthPortMonModuleId'
_d='atiL2EthMonModuleId'
_c='oneGb-Fiber'
_b='oneGb-rj45'
_a='hundredfiber-mii'
_Z='ten-100rj45-mii'
_Y='at-8350GB'
_X='at-9410GB'
_W='at-8326GB'
_V='at-8124XL-V2'
_U='at-8316F'
_T='at-8324'
_S='atiL2deviceIndex'
_R='atiL2NwMgrIndex'
_Q='switch-reset'
_P='switch-no-reset'
_O='NotificationType'
_N='OctetString'
_M='unknown'
_L='Timeout'
_K='atiL2TrapAttrModuleId'
_J='disabled'
_I='deprecated'
_H='disable'
_G='enable'
_F='DisplayString'
_E='AtiL2-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_O,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_O,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(Integer32):0
_AlliedTelesyn_ObjectIdentity=ObjectIdentity
alliedTelesyn=_AlliedTelesyn_ObjectIdentity((1,3,6,1,4,1,207))
_AtiProduct_ObjectIdentity=ObjectIdentity
atiProduct=_AtiProduct_ObjectIdentity((1,3,6,1,4,1,207,1))
_Swhub_ObjectIdentity=ObjectIdentity
swhub=_Swhub_ObjectIdentity((1,3,6,1,4,1,207,1,4))
_At_8324_ObjectIdentity=ObjectIdentity
at_8324=_At_8324_ObjectIdentity((1,3,6,1,4,1,207,1,4,37))
_At_8124XL_V2_ObjectIdentity=ObjectIdentity
at_8124XL_V2=_At_8124XL_V2_ObjectIdentity((1,3,6,1,4,1,207,1,4,52))
_At_8326GB_ObjectIdentity=ObjectIdentity
at_8326GB=_At_8326GB_ObjectIdentity((1,3,6,1,4,1,207,1,4,72))
_At_9410GB_ObjectIdentity=ObjectIdentity
at_9410GB=_At_9410GB_ObjectIdentity((1,3,6,1,4,1,207,1,4,73))
_At_8350GB_ObjectIdentity=ObjectIdentity
at_8350GB=_At_8350GB_ObjectIdentity((1,3,6,1,4,1,207,1,4,74))
_At_8316F_ObjectIdentity=ObjectIdentity
at_8316F=_At_8316F_ObjectIdentity((1,3,6,1,4,1,207,1,4,77))
_MibObject_ObjectIdentity=ObjectIdentity
mibObject=_MibObject_ObjectIdentity((1,3,6,1,4,1,207,8))
_AtiL2Mib_ObjectIdentity=ObjectIdentity
atiL2Mib=_AtiL2Mib_ObjectIdentity((1,3,6,1,4,1,207,8,33))
_AtiL2GlobalGroup_ObjectIdentity=ObjectIdentity
atiL2GlobalGroup=_AtiL2GlobalGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,1))
class _AtiL2SwProduct_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiL2SwProduct_Type.__name__=_F
_AtiL2SwProduct_Object=MibScalar
atiL2SwProduct=_AtiL2SwProduct_Object((1,3,6,1,4,1,207,8,33,1,1),_AtiL2SwProduct_Type())
atiL2SwProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2SwProduct.setStatus(_A)
class _AtiL2SwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiL2SwVersion_Type.__name__=_F
_AtiL2SwVersion_Object=MibScalar
atiL2SwVersion=_AtiL2SwVersion_Object((1,3,6,1,4,1,207,8,33,1,2),_AtiL2SwVersion_Type())
atiL2SwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2SwVersion.setStatus(_A)
class _AtiL2Reset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_AtiL2Reset_Type.__name__=_D
_AtiL2Reset_Object=MibScalar
atiL2Reset=_AtiL2Reset_Object((1,3,6,1,4,1,207,8,33,1,3),_AtiL2Reset_Type())
atiL2Reset.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2Reset.setStatus(_A)
_AtiL2MirroringSourceModule_Type=Integer32
_AtiL2MirroringSourceModule_Object=MibScalar
atiL2MirroringSourceModule=_AtiL2MirroringSourceModule_Object((1,3,6,1,4,1,207,8,33,1,4),_AtiL2MirroringSourceModule_Type())
atiL2MirroringSourceModule.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2MirroringSourceModule.setStatus(_A)
_AtiL2MirroringSourcePort_Type=Integer32
_AtiL2MirroringSourcePort_Object=MibScalar
atiL2MirroringSourcePort=_AtiL2MirroringSourcePort_Object((1,3,6,1,4,1,207,8,33,1,5),_AtiL2MirroringSourcePort_Type())
atiL2MirroringSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2MirroringSourcePort.setStatus(_A)
_AtiL2MirroringDestinationModule_Type=Integer32
_AtiL2MirroringDestinationModule_Object=MibScalar
atiL2MirroringDestinationModule=_AtiL2MirroringDestinationModule_Object((1,3,6,1,4,1,207,8,33,1,6),_AtiL2MirroringDestinationModule_Type())
atiL2MirroringDestinationModule.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2MirroringDestinationModule.setStatus(_A)
_AtiL2MirroringDestinationPort_Type=Integer32
_AtiL2MirroringDestinationPort_Object=MibScalar
atiL2MirroringDestinationPort=_AtiL2MirroringDestinationPort_Object((1,3,6,1,4,1,207,8,33,1,7),_AtiL2MirroringDestinationPort_Type())
atiL2MirroringDestinationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2MirroringDestinationPort.setStatus(_A)
class _AtiL2MirrorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receive-and-transmit',1),(_J,2)))
_AtiL2MirrorState_Type.__name__=_D
_AtiL2MirrorState_Object=MibScalar
atiL2MirrorState=_AtiL2MirrorState_Object((1,3,6,1,4,1,207,8,33,1,8),_AtiL2MirrorState_Type())
atiL2MirrorState.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2MirrorState.setStatus(_A)
class _AtiL2IGMPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AtiL2IGMPState_Type.__name__=_D
_AtiL2IGMPState_Object=MibScalar
atiL2IGMPState=_AtiL2IGMPState_Object((1,3,6,1,4,1,207,8,33,1,9),_AtiL2IGMPState_Type())
atiL2IGMPState.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2IGMPState.setStatus(_A)
_AtiL2DeviceNumber_Type=Integer32
_AtiL2DeviceNumber_Object=MibScalar
atiL2DeviceNumber=_AtiL2DeviceNumber_Object((1,3,6,1,4,1,207,8,33,1,10),_AtiL2DeviceNumber_Type())
atiL2DeviceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DeviceNumber.setStatus(_A)
_AtiL2IpGroup_ObjectIdentity=ObjectIdentity
atiL2IpGroup=_AtiL2IpGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,2))
_AtiL2CurrentIpAddress_Type=IpAddress
_AtiL2CurrentIpAddress_Object=MibScalar
atiL2CurrentIpAddress=_AtiL2CurrentIpAddress_Object((1,3,6,1,4,1,207,8,33,2,1),_AtiL2CurrentIpAddress_Type())
atiL2CurrentIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2CurrentIpAddress.setStatus(_A)
_AtiL2ConfiguredIpAddress_Type=IpAddress
_AtiL2ConfiguredIpAddress_Object=MibScalar
atiL2ConfiguredIpAddress=_AtiL2ConfiguredIpAddress_Object((1,3,6,1,4,1,207,8,33,2,2),_AtiL2ConfiguredIpAddress_Type())
atiL2ConfiguredIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2ConfiguredIpAddress.setStatus(_A)
_AtiL2ConfiguredSubnetMask_Type=IpAddress
_AtiL2ConfiguredSubnetMask_Object=MibScalar
atiL2ConfiguredSubnetMask=_AtiL2ConfiguredSubnetMask_Object((1,3,6,1,4,1,207,8,33,2,3),_AtiL2ConfiguredSubnetMask_Type())
atiL2ConfiguredSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2ConfiguredSubnetMask.setStatus(_A)
_AtiL2ConfiguredRouter_Type=IpAddress
_AtiL2ConfiguredRouter_Object=MibScalar
atiL2ConfiguredRouter=_AtiL2ConfiguredRouter_Object((1,3,6,1,4,1,207,8,33,2,4),_AtiL2ConfiguredRouter_Type())
atiL2ConfiguredRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2ConfiguredRouter.setStatus(_A)
class _AtiL2IPAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('from-dhcp',1),('from-bootp',2),('from-psuedoip',3),('from-Omega',4)))
_AtiL2IPAddressStatus_Type.__name__=_D
_AtiL2IPAddressStatus_Object=MibScalar
atiL2IPAddressStatus=_AtiL2IPAddressStatus_Object((1,3,6,1,4,1,207,8,33,2,5),_AtiL2IPAddressStatus_Type())
atiL2IPAddressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2IPAddressStatus.setStatus(_A)
_AtiL2DNServer_Type=IpAddress
_AtiL2DNServer_Object=MibScalar
atiL2DNServer=_AtiL2DNServer_Object((1,3,6,1,4,1,207,8,33,2,6),_AtiL2DNServer_Type())
atiL2DNServer.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DNServer.setStatus(_A)
class _AtiL2DefaultDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiL2DefaultDomainName_Type.__name__=_F
_AtiL2DefaultDomainName_Object=MibScalar
atiL2DefaultDomainName=_AtiL2DefaultDomainName_Object((1,3,6,1,4,1,207,8,33,2,7),_AtiL2DefaultDomainName_Type())
atiL2DefaultDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DefaultDomainName.setStatus(_A)
_AtiL2NMGroup_ObjectIdentity=ObjectIdentity
atiL2NMGroup=_AtiL2NMGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,3))
_AtiL2NwMgrTable_Object=MibTable
atiL2NwMgrTable=_AtiL2NwMgrTable_Object((1,3,6,1,4,1,207,8,33,3,1))
if mibBuilder.loadTexts:atiL2NwMgrTable.setStatus(_A)
_AtiL2NwMgrEntry_Object=MibTableRow
atiL2NwMgrEntry=_AtiL2NwMgrEntry_Object((1,3,6,1,4,1,207,8,33,3,1,1))
atiL2NwMgrEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:atiL2NwMgrEntry.setStatus(_A)
class _AtiL2NwMgrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AtiL2NwMgrIndex_Type.__name__=_D
_AtiL2NwMgrIndex_Object=MibTableColumn
atiL2NwMgrIndex=_AtiL2NwMgrIndex_Object((1,3,6,1,4,1,207,8,33,3,1,1,1),_AtiL2NwMgrIndex_Type())
atiL2NwMgrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2NwMgrIndex.setStatus(_A)
_AtiL2NwMgrIpAddr_Type=IpAddress
_AtiL2NwMgrIpAddr_Object=MibTableColumn
atiL2NwMgrIpAddr=_AtiL2NwMgrIpAddr_Object((1,3,6,1,4,1,207,8,33,3,1,1,2),_AtiL2NwMgrIpAddr_Type())
atiL2NwMgrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2NwMgrIpAddr.setStatus(_A)
_AtiL2DHCPGroup_ObjectIdentity=ObjectIdentity
atiL2DHCPGroup=_AtiL2DHCPGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,4))
_AtiL2DHCPSysGroup_ObjectIdentity=ObjectIdentity
atiL2DHCPSysGroup=_AtiL2DHCPSysGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,4,1))
_AtiL2DHCPCurrentDHCPClientAddress_Type=IpAddress
_AtiL2DHCPCurrentDHCPClientAddress_Object=MibScalar
atiL2DHCPCurrentDHCPClientAddress=_AtiL2DHCPCurrentDHCPClientAddress_Object((1,3,6,1,4,1,207,8,33,4,1,1),_AtiL2DHCPCurrentDHCPClientAddress_Type())
atiL2DHCPCurrentDHCPClientAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DHCPCurrentDHCPClientAddress.setStatus(_A)
_AtiL2DHCPSubnetMask_Type=IpAddress
_AtiL2DHCPSubnetMask_Object=MibScalar
atiL2DHCPSubnetMask=_AtiL2DHCPSubnetMask_Object((1,3,6,1,4,1,207,8,33,4,1,2),_AtiL2DHCPSubnetMask_Type())
atiL2DHCPSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DHCPSubnetMask.setStatus(_A)
_AtiL2DHCPCurrentRelayAgentAddress_Type=IpAddress
_AtiL2DHCPCurrentRelayAgentAddress_Object=MibScalar
atiL2DHCPCurrentRelayAgentAddress=_AtiL2DHCPCurrentRelayAgentAddress_Object((1,3,6,1,4,1,207,8,33,4,1,3),_AtiL2DHCPCurrentRelayAgentAddress_Type())
atiL2DHCPCurrentRelayAgentAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DHCPCurrentRelayAgentAddress.setStatus(_A)
_AtiL2DHCPNextDHCPServerAddress_Type=IpAddress
_AtiL2DHCPNextDHCPServerAddress_Object=MibScalar
atiL2DHCPNextDHCPServerAddress=_AtiL2DHCPNextDHCPServerAddress_Object((1,3,6,1,4,1,207,8,33,4,1,4),_AtiL2DHCPNextDHCPServerAddress_Type())
atiL2DHCPNextDHCPServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DHCPNextDHCPServerAddress.setStatus(_A)
_AtiL2DHCPTimerGroup_ObjectIdentity=ObjectIdentity
atiL2DHCPTimerGroup=_AtiL2DHCPTimerGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,4,2))
_AtiL2DHCPLeaseTimer_Type=TimeTicks
_AtiL2DHCPLeaseTimer_Object=MibScalar
atiL2DHCPLeaseTimer=_AtiL2DHCPLeaseTimer_Object((1,3,6,1,4,1,207,8,33,4,2,1),_AtiL2DHCPLeaseTimer_Type())
atiL2DHCPLeaseTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DHCPLeaseTimer.setStatus(_A)
_AtiL2DHCPReacquisitionTimer_Type=TimeTicks
_AtiL2DHCPReacquisitionTimer_Object=MibScalar
atiL2DHCPReacquisitionTimer=_AtiL2DHCPReacquisitionTimer_Object((1,3,6,1,4,1,207,8,33,4,2,2),_AtiL2DHCPReacquisitionTimer_Type())
atiL2DHCPReacquisitionTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DHCPReacquisitionTimer.setStatus(_A)
_AtiL2DHCPExpirationTimer_Type=TimeTicks
_AtiL2DHCPExpirationTimer_Object=MibScalar
atiL2DHCPExpirationTimer=_AtiL2DHCPExpirationTimer_Object((1,3,6,1,4,1,207,8,33,4,2,3),_AtiL2DHCPExpirationTimer_Type())
atiL2DHCPExpirationTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DHCPExpirationTimer.setStatus(_A)
_AtiL2DeviceGroup_ObjectIdentity=ObjectIdentity
atiL2DeviceGroup=_AtiL2DeviceGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,5))
_AtiL2deviceTable_Object=MibTable
atiL2deviceTable=_AtiL2deviceTable_Object((1,3,6,1,4,1,207,8,33,5,1))
if mibBuilder.loadTexts:atiL2deviceTable.setStatus(_A)
_AtiL2deviceEntry_Object=MibTableRow
atiL2deviceEntry=_AtiL2deviceEntry_Object((1,3,6,1,4,1,207,8,33,5,1,1))
atiL2deviceEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:atiL2deviceEntry.setStatus(_A)
class _AtiL2deviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiL2deviceIndex_Type.__name__=_D
_AtiL2deviceIndex_Object=MibTableColumn
atiL2deviceIndex=_AtiL2deviceIndex_Object((1,3,6,1,4,1,207,8,33,5,1,1,2),_AtiL2deviceIndex_Type())
atiL2deviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2deviceIndex.setStatus(_A)
class _AtiL2deviceDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiL2deviceDescr_Type.__name__=_F
_AtiL2deviceDescr_Object=MibTableColumn
atiL2deviceDescr=_AtiL2deviceDescr_Object((1,3,6,1,4,1,207,8,33,5,1,1,3),_AtiL2deviceDescr_Type())
atiL2deviceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2deviceDescr.setStatus(_A)
class _AtiL2deviceProductType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,20)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),('other',20)))
_AtiL2deviceProductType_Type.__name__=_D
_AtiL2deviceProductType_Object=MibTableColumn
atiL2deviceProductType=_AtiL2deviceProductType_Object((1,3,6,1,4,1,207,8,33,5,1,1,4),_AtiL2deviceProductType_Type())
atiL2deviceProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2deviceProductType.setStatus(_A)
class _AtiL2devicePortCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_AtiL2devicePortCount_Type.__name__=_D
_AtiL2devicePortCount_Object=MibTableColumn
atiL2devicePortCount=_AtiL2devicePortCount_Object((1,3,6,1,4,1,207,8,33,5,1,1,5),_AtiL2devicePortCount_Type())
atiL2devicePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2devicePortCount.setStatus(_A)
class _AtiL2deviceSecurityConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('enabled-with-learning-locked',2),('limited-enabled',3)))
_AtiL2deviceSecurityConfig_Type.__name__=_D
_AtiL2deviceSecurityConfig_Object=MibTableColumn
atiL2deviceSecurityConfig=_AtiL2deviceSecurityConfig_Object((1,3,6,1,4,1,207,8,33,5,1,1,6),_AtiL2deviceSecurityConfig_Type())
atiL2deviceSecurityConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2deviceSecurityConfig.setStatus(_A)
class _AtiL2deviceSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('send-trap-only',1),('disable-port-only',2),('disable-port-and-send-trap',3),('do-nothing',4)))
_AtiL2deviceSecurityAction_Type.__name__=_D
_AtiL2deviceSecurityAction_Object=MibTableColumn
atiL2deviceSecurityAction=_AtiL2deviceSecurityAction_Object((1,3,6,1,4,1,207,8,33,5,1,1,7),_AtiL2deviceSecurityAction_Type())
atiL2deviceSecurityAction.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2deviceSecurityAction.setStatus(_A)
_AtiL2deviceDebugAvailableBytes_Type=Integer32
_AtiL2deviceDebugAvailableBytes_Object=MibTableColumn
atiL2deviceDebugAvailableBytes=_AtiL2deviceDebugAvailableBytes_Object((1,3,6,1,4,1,207,8,33,5,1,1,8),_AtiL2deviceDebugAvailableBytes_Type())
atiL2deviceDebugAvailableBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2deviceDebugAvailableBytes.setStatus(_A)
class _AtiL2deviceMDA1Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),('none',5)))
_AtiL2deviceMDA1Type_Type.__name__=_D
_AtiL2deviceMDA1Type_Object=MibTableColumn
atiL2deviceMDA1Type=_AtiL2deviceMDA1Type_Object((1,3,6,1,4,1,207,8,33,5,1,1,9),_AtiL2deviceMDA1Type_Type())
atiL2deviceMDA1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2deviceMDA1Type.setStatus(_A)
class _AtiL2deviceMDA2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),('none',5)))
_AtiL2deviceMDA2Type_Type.__name__=_D
_AtiL2deviceMDA2Type_Object=MibTableColumn
atiL2deviceMDA2Type=_AtiL2deviceMDA2Type_Object((1,3,6,1,4,1,207,8,33,5,1,1,10),_AtiL2deviceMDA2Type_Type())
atiL2deviceMDA2Type.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2deviceMDA2Type.setStatus(_A)
class _AtiL2deviceReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_AtiL2deviceReset_Type.__name__=_D
_AtiL2deviceReset_Object=MibTableColumn
atiL2deviceReset=_AtiL2deviceReset_Object((1,3,6,1,4,1,207,8,33,5,1,1,11),_AtiL2deviceReset_Type())
atiL2deviceReset.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2deviceReset.setStatus(_A)
_AtiL2EthernetStatsGroup_ObjectIdentity=ObjectIdentity
atiL2EthernetStatsGroup=_AtiL2EthernetStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,6))
_AtiL2EthMonStatsGroup_ObjectIdentity=ObjectIdentity
atiL2EthMonStatsGroup=_AtiL2EthMonStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,6,1))
_AtiL2EthMonStatsTable_Object=MibTable
atiL2EthMonStatsTable=_AtiL2EthMonStatsTable_Object((1,3,6,1,4,1,207,8,33,6,1,1))
if mibBuilder.loadTexts:atiL2EthMonStatsTable.setStatus(_A)
_AtiL2EthMonStatsEntry_Object=MibTableRow
atiL2EthMonStatsEntry=_AtiL2EthMonStatsEntry_Object((1,3,6,1,4,1,207,8,33,6,1,1,1))
atiL2EthMonStatsEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:atiL2EthMonStatsEntry.setStatus(_A)
_AtiL2EthMonModuleId_Type=Integer32
_AtiL2EthMonModuleId_Object=MibTableColumn
atiL2EthMonModuleId=_AtiL2EthMonModuleId_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,1),_AtiL2EthMonModuleId_Type())
atiL2EthMonModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonModuleId.setStatus(_A)
_AtiL2EthMonRxGoodFrames_Type=Counter32
_AtiL2EthMonRxGoodFrames_Object=MibTableColumn
atiL2EthMonRxGoodFrames=_AtiL2EthMonRxGoodFrames_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,2),_AtiL2EthMonRxGoodFrames_Type())
atiL2EthMonRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonRxGoodFrames.setStatus(_A)
_AtiL2EthMonTxGoodFrames_Type=Counter32
_AtiL2EthMonTxGoodFrames_Object=MibTableColumn
atiL2EthMonTxGoodFrames=_AtiL2EthMonTxGoodFrames_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,3),_AtiL2EthMonTxGoodFrames_Type())
atiL2EthMonTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonTxGoodFrames.setStatus(_A)
_AtiL2EthMonTxTotalBytes_Type=Counter32
_AtiL2EthMonTxTotalBytes_Object=MibTableColumn
atiL2EthMonTxTotalBytes=_AtiL2EthMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,4),_AtiL2EthMonTxTotalBytes_Type())
atiL2EthMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonTxTotalBytes.setStatus(_A)
_AtiL2EthMonTxDeferred_Type=Counter32
_AtiL2EthMonTxDeferred_Object=MibTableColumn
atiL2EthMonTxDeferred=_AtiL2EthMonTxDeferred_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,5),_AtiL2EthMonTxDeferred_Type())
atiL2EthMonTxDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonTxDeferred.setStatus(_I)
_AtiL2EthMonTxCollisions_Type=Counter32
_AtiL2EthMonTxCollisions_Object=MibTableColumn
atiL2EthMonTxCollisions=_AtiL2EthMonTxCollisions_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,6),_AtiL2EthMonTxCollisions_Type())
atiL2EthMonTxCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonTxCollisions.setStatus(_A)
_AtiL2EthMonTxBroadcastFrames_Type=Counter32
_AtiL2EthMonTxBroadcastFrames_Object=MibTableColumn
atiL2EthMonTxBroadcastFrames=_AtiL2EthMonTxBroadcastFrames_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,7),_AtiL2EthMonTxBroadcastFrames_Type())
atiL2EthMonTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonTxBroadcastFrames.setStatus(_A)
_AtiL2EthMonTxMulticastFrames_Type=Counter32
_AtiL2EthMonTxMulticastFrames_Object=MibTableColumn
atiL2EthMonTxMulticastFrames=_AtiL2EthMonTxMulticastFrames_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,8),_AtiL2EthMonTxMulticastFrames_Type())
atiL2EthMonTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonTxMulticastFrames.setStatus(_A)
_AtiL2EthMonRxOverruns_Type=Counter32
_AtiL2EthMonRxOverruns_Object=MibTableColumn
atiL2EthMonRxOverruns=_AtiL2EthMonRxOverruns_Object((1,3,6,1,4,1,207,8,33,6,1,1,1,9),_AtiL2EthMonRxOverruns_Type())
atiL2EthMonRxOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthMonRxOverruns.setStatus(_A)
_AtiL2EthPortMonStatsTable_Object=MibTable
atiL2EthPortMonStatsTable=_AtiL2EthPortMonStatsTable_Object((1,3,6,1,4,1,207,8,33,6,1,2))
if mibBuilder.loadTexts:atiL2EthPortMonStatsTable.setStatus(_A)
_AtiL2EthPortMonStatsEntry_Object=MibTableRow
atiL2EthPortMonStatsEntry=_AtiL2EthPortMonStatsEntry_Object((1,3,6,1,4,1,207,8,33,6,1,2,1))
atiL2EthPortMonStatsEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:atiL2EthPortMonStatsEntry.setStatus(_A)
_AtiL2EthPortMonModuleId_Type=Integer32
_AtiL2EthPortMonModuleId_Object=MibTableColumn
atiL2EthPortMonModuleId=_AtiL2EthPortMonModuleId_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,1),_AtiL2EthPortMonModuleId_Type())
atiL2EthPortMonModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonModuleId.setStatus(_A)
_AtiL2EthPortMonPortId_Type=Integer32
_AtiL2EthPortMonPortId_Object=MibTableColumn
atiL2EthPortMonPortId=_AtiL2EthPortMonPortId_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,2),_AtiL2EthPortMonPortId_Type())
atiL2EthPortMonPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonPortId.setStatus(_A)
_AtiL2EthPortMonRxGoodFrames_Type=Counter32
_AtiL2EthPortMonRxGoodFrames_Object=MibTableColumn
atiL2EthPortMonRxGoodFrames=_AtiL2EthPortMonRxGoodFrames_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,3),_AtiL2EthPortMonRxGoodFrames_Type())
atiL2EthPortMonRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonRxGoodFrames.setStatus(_A)
_AtiL2EthPortMonTxGoodFrames_Type=Counter32
_AtiL2EthPortMonTxGoodFrames_Object=MibTableColumn
atiL2EthPortMonTxGoodFrames=_AtiL2EthPortMonTxGoodFrames_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,4),_AtiL2EthPortMonTxGoodFrames_Type())
atiL2EthPortMonTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonTxGoodFrames.setStatus(_A)
_AtiL2EthPortMonTxTotalBytes_Type=Counter32
_AtiL2EthPortMonTxTotalBytes_Object=MibTableColumn
atiL2EthPortMonTxTotalBytes=_AtiL2EthPortMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,5),_AtiL2EthPortMonTxTotalBytes_Type())
atiL2EthPortMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonTxTotalBytes.setStatus(_A)
_AtiL2EthPortMonTxDeferred_Type=Counter32
_AtiL2EthPortMonTxDeferred_Object=MibTableColumn
atiL2EthPortMonTxDeferred=_AtiL2EthPortMonTxDeferred_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,6),_AtiL2EthPortMonTxDeferred_Type())
atiL2EthPortMonTxDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonTxDeferred.setStatus(_I)
_AtiL2EthPortMonTxCollisions_Type=Counter32
_AtiL2EthPortMonTxCollisions_Object=MibTableColumn
atiL2EthPortMonTxCollisions=_AtiL2EthPortMonTxCollisions_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,7),_AtiL2EthPortMonTxCollisions_Type())
atiL2EthPortMonTxCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonTxCollisions.setStatus(_A)
_AtiL2EthPortMonTxBroadcastFrames_Type=Counter32
_AtiL2EthPortMonTxBroadcastFrames_Object=MibTableColumn
atiL2EthPortMonTxBroadcastFrames=_AtiL2EthPortMonTxBroadcastFrames_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,8),_AtiL2EthPortMonTxBroadcastFrames_Type())
atiL2EthPortMonTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonTxBroadcastFrames.setStatus(_A)
_AtiL2EthPortMonTxMulticastFrames_Type=Counter32
_AtiL2EthPortMonTxMulticastFrames_Object=MibTableColumn
atiL2EthPortMonTxMulticastFrames=_AtiL2EthPortMonTxMulticastFrames_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,9),_AtiL2EthPortMonTxMulticastFrames_Type())
atiL2EthPortMonTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonTxMulticastFrames.setStatus(_A)
_AtiL2EthPortMonRxOverruns_Type=Counter32
_AtiL2EthPortMonRxOverruns_Object=MibTableColumn
atiL2EthPortMonRxOverruns=_AtiL2EthPortMonRxOverruns_Object((1,3,6,1,4,1,207,8,33,6,1,2,1,10),_AtiL2EthPortMonRxOverruns_Type())
atiL2EthPortMonRxOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortMonRxOverruns.setStatus(_A)
_AtiL2EthErrStatsGroup_ObjectIdentity=ObjectIdentity
atiL2EthErrStatsGroup=_AtiL2EthErrStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,6,2))
_AtiL2EthErrStatsTable_Object=MibTable
atiL2EthErrStatsTable=_AtiL2EthErrStatsTable_Object((1,3,6,1,4,1,207,8,33,6,2,1))
if mibBuilder.loadTexts:atiL2EthErrStatsTable.setStatus(_A)
_AtiL2EthErrorStatsEntry_Object=MibTableRow
atiL2EthErrorStatsEntry=_AtiL2EthErrorStatsEntry_Object((1,3,6,1,4,1,207,8,33,6,2,1,1))
atiL2EthErrorStatsEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:atiL2EthErrorStatsEntry.setStatus(_A)
_AtiL2EthErrModuleId_Type=Integer32
_AtiL2EthErrModuleId_Object=MibTableColumn
atiL2EthErrModuleId=_AtiL2EthErrModuleId_Object((1,3,6,1,4,1,207,8,33,6,2,1,1,1),_AtiL2EthErrModuleId_Type())
atiL2EthErrModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthErrModuleId.setStatus(_A)
_AtiL2EthErrorCRC_Type=Counter32
_AtiL2EthErrorCRC_Object=MibTableColumn
atiL2EthErrorCRC=_AtiL2EthErrorCRC_Object((1,3,6,1,4,1,207,8,33,6,2,1,1,2),_AtiL2EthErrorCRC_Type())
atiL2EthErrorCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthErrorCRC.setStatus(_A)
_AtiL2EthErrorAlignment_Type=Counter32
_AtiL2EthErrorAlignment_Object=MibTableColumn
atiL2EthErrorAlignment=_AtiL2EthErrorAlignment_Object((1,3,6,1,4,1,207,8,33,6,2,1,1,3),_AtiL2EthErrorAlignment_Type())
atiL2EthErrorAlignment.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthErrorAlignment.setStatus(_A)
_AtiL2EthErrorRxBadFrames_Type=Counter32
_AtiL2EthErrorRxBadFrames_Object=MibTableColumn
atiL2EthErrorRxBadFrames=_AtiL2EthErrorRxBadFrames_Object((1,3,6,1,4,1,207,8,33,6,2,1,1,4),_AtiL2EthErrorRxBadFrames_Type())
atiL2EthErrorRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthErrorRxBadFrames.setStatus(_A)
_AtiL2EthErrorLateCollisions_Type=Counter32
_AtiL2EthErrorLateCollisions_Object=MibTableColumn
atiL2EthErrorLateCollisions=_AtiL2EthErrorLateCollisions_Object((1,3,6,1,4,1,207,8,33,6,2,1,1,5),_AtiL2EthErrorLateCollisions_Type())
atiL2EthErrorLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthErrorLateCollisions.setStatus(_A)
_AtiL2EthErrorTxTotal_Type=Counter32
_AtiL2EthErrorTxTotal_Object=MibTableColumn
atiL2EthErrorTxTotal=_AtiL2EthErrorTxTotal_Object((1,3,6,1,4,1,207,8,33,6,2,1,1,6),_AtiL2EthErrorTxTotal_Type())
atiL2EthErrorTxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthErrorTxTotal.setStatus(_A)
_AtiL2EthPortErrStatsTable_Object=MibTable
atiL2EthPortErrStatsTable=_AtiL2EthPortErrStatsTable_Object((1,3,6,1,4,1,207,8,33,6,2,2))
if mibBuilder.loadTexts:atiL2EthPortErrStatsTable.setStatus(_A)
_AtiL2EthPortErrorStatsEntry_Object=MibTableRow
atiL2EthPortErrorStatsEntry=_AtiL2EthPortErrorStatsEntry_Object((1,3,6,1,4,1,207,8,33,6,2,2,1))
atiL2EthPortErrorStatsEntry.setIndexNames((0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:atiL2EthPortErrorStatsEntry.setStatus(_A)
_AtiL2EthPortErrModuleId_Type=Integer32
_AtiL2EthPortErrModuleId_Object=MibTableColumn
atiL2EthPortErrModuleId=_AtiL2EthPortErrModuleId_Object((1,3,6,1,4,1,207,8,33,6,2,2,1,1),_AtiL2EthPortErrModuleId_Type())
atiL2EthPortErrModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortErrModuleId.setStatus(_A)
_AtiL2EthPortErrPortId_Type=Integer32
_AtiL2EthPortErrPortId_Object=MibTableColumn
atiL2EthPortErrPortId=_AtiL2EthPortErrPortId_Object((1,3,6,1,4,1,207,8,33,6,2,2,1,2),_AtiL2EthPortErrPortId_Type())
atiL2EthPortErrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortErrPortId.setStatus(_A)
_AtiL2EthPortErrorCRC_Type=Counter32
_AtiL2EthPortErrorCRC_Object=MibTableColumn
atiL2EthPortErrorCRC=_AtiL2EthPortErrorCRC_Object((1,3,6,1,4,1,207,8,33,6,2,2,1,3),_AtiL2EthPortErrorCRC_Type())
atiL2EthPortErrorCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortErrorCRC.setStatus(_A)
_AtiL2EthPortErrorAlignment_Type=Counter32
_AtiL2EthPortErrorAlignment_Object=MibTableColumn
atiL2EthPortErrorAlignment=_AtiL2EthPortErrorAlignment_Object((1,3,6,1,4,1,207,8,33,6,2,2,1,4),_AtiL2EthPortErrorAlignment_Type())
atiL2EthPortErrorAlignment.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortErrorAlignment.setStatus(_A)
_AtiL2EthPortErrorRxBadFrames_Type=Counter32
_AtiL2EthPortErrorRxBadFrames_Object=MibTableColumn
atiL2EthPortErrorRxBadFrames=_AtiL2EthPortErrorRxBadFrames_Object((1,3,6,1,4,1,207,8,33,6,2,2,1,5),_AtiL2EthPortErrorRxBadFrames_Type())
atiL2EthPortErrorRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortErrorRxBadFrames.setStatus(_A)
_AtiL2EthPortErrorLateCollisions_Type=Counter32
_AtiL2EthPortErrorLateCollisions_Object=MibTableColumn
atiL2EthPortErrorLateCollisions=_AtiL2EthPortErrorLateCollisions_Object((1,3,6,1,4,1,207,8,33,6,2,2,1,6),_AtiL2EthPortErrorLateCollisions_Type())
atiL2EthPortErrorLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortErrorLateCollisions.setStatus(_A)
_AtiL2EthPortErrorTxTotal_Type=Counter32
_AtiL2EthPortErrorTxTotal_Object=MibTableColumn
atiL2EthPortErrorTxTotal=_AtiL2EthPortErrorTxTotal_Object((1,3,6,1,4,1,207,8,33,6,2,2,1,7),_AtiL2EthPortErrorTxTotal_Type())
atiL2EthPortErrorTxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2EthPortErrorTxTotal.setStatus(_A)
_AtiL2DevicePortConfigGroup_ObjectIdentity=ObjectIdentity
atiL2DevicePortConfigGroup=_AtiL2DevicePortConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,7))
_AtiL2DevicePortTable_Object=MibTable
atiL2DevicePortTable=_AtiL2DevicePortTable_Object((1,3,6,1,4,1,207,8,33,7,1))
if mibBuilder.loadTexts:atiL2DevicePortTable.setStatus(_A)
_AtiL2DevicePortEntry_Object=MibTableRow
atiL2DevicePortEntry=_AtiL2DevicePortEntry_Object((1,3,6,1,4,1,207,8,33,7,1,1))
atiL2DevicePortEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:atiL2DevicePortEntry.setStatus(_A)
_AtiL2DeviceId_Type=Integer32
_AtiL2DeviceId_Object=MibTableColumn
atiL2DeviceId=_AtiL2DeviceId_Object((1,3,6,1,4,1,207,8,33,7,1,1,1),_AtiL2DeviceId_Type())
atiL2DeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DeviceId.setStatus(_A)
_AtiL2DevicePortNumber_Type=Integer32
_AtiL2DevicePortNumber_Object=MibTableColumn
atiL2DevicePortNumber=_AtiL2DevicePortNumber_Object((1,3,6,1,4,1,207,8,33,7,1,1,2),_AtiL2DevicePortNumber_Type())
atiL2DevicePortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DevicePortNumber.setStatus(_A)
class _AtiL2DevicePortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiL2DevicePortName_Type.__name__=_F
_AtiL2DevicePortName_Object=MibTableColumn
atiL2DevicePortName=_AtiL2DevicePortName_Object((1,3,6,1,4,1,207,8,33,7,1,1,3),_AtiL2DevicePortName_Type())
atiL2DevicePortName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortName.setStatus(_A)
class _AtiL2DevicePortAutosenseOrHalfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('portAutoSense',1),('forceHalfDuplex-10M',2),('forceHalfDuplex-100M',3),('forceFullDuplex-10M',4),('forceFullDuplex-100M',5),('forceHalfDuplex-1G',6),('forceFullDuplex-1G',7)))
_AtiL2DevicePortAutosenseOrHalfDuplex_Type.__name__=_D
_AtiL2DevicePortAutosenseOrHalfDuplex_Object=MibTableColumn
atiL2DevicePortAutosenseOrHalfDuplex=_AtiL2DevicePortAutosenseOrHalfDuplex_Object((1,3,6,1,4,1,207,8,33,7,1,1,4),_AtiL2DevicePortAutosenseOrHalfDuplex_Type())
atiL2DevicePortAutosenseOrHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortAutosenseOrHalfDuplex.setStatus(_A)
class _AtiL2DevicePortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_AtiL2DevicePortLinkState_Type.__name__=_D
_AtiL2DevicePortLinkState_Object=MibTableColumn
atiL2DevicePortLinkState=_AtiL2DevicePortLinkState_Object((1,3,6,1,4,1,207,8,33,7,1,1,5),_AtiL2DevicePortLinkState_Type())
atiL2DevicePortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DevicePortLinkState.setStatus(_A)
class _AtiL2DevicePortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fullDuplex',1),('halfDuplex',2),('autosense',3)))
_AtiL2DevicePortDuplexStatus_Type.__name__=_D
_AtiL2DevicePortDuplexStatus_Object=MibTableColumn
atiL2DevicePortDuplexStatus=_AtiL2DevicePortDuplexStatus_Object((1,3,6,1,4,1,207,8,33,7,1,1,6),_AtiL2DevicePortDuplexStatus_Type())
atiL2DevicePortDuplexStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DevicePortDuplexStatus.setStatus(_A)
class _AtiL2DevicePortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tenMBits',1),('hundredMBits',2),('gigaBits',3),(_M,4)))
_AtiL2DevicePortSpeed_Type.__name__=_D
_AtiL2DevicePortSpeed_Object=MibTableColumn
atiL2DevicePortSpeed=_AtiL2DevicePortSpeed_Object((1,3,6,1,4,1,207,8,33,7,1,1,7),_AtiL2DevicePortSpeed_Type())
atiL2DevicePortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2DevicePortSpeed.setStatus(_A)
class _AtiL2DevicePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_l,1),(_J,2),(_m,3),(_n,4),(_o,5)))
_AtiL2DevicePortState_Type.__name__=_D
_AtiL2DevicePortState_Object=MibTableColumn
atiL2DevicePortState=_AtiL2DevicePortState_Object((1,3,6,1,4,1,207,8,33,7,1,1,8),_AtiL2DevicePortState_Type())
atiL2DevicePortState.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortState.setStatus(_A)
class _AtiL2DevicePortTransmitPacingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AtiL2DevicePortTransmitPacingConfig_Type.__name__=_D
_AtiL2DevicePortTransmitPacingConfig_Object=MibTableColumn
atiL2DevicePortTransmitPacingConfig=_AtiL2DevicePortTransmitPacingConfig_Object((1,3,6,1,4,1,207,8,33,7,1,1,9),_AtiL2DevicePortTransmitPacingConfig_Type())
atiL2DevicePortTransmitPacingConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortTransmitPacingConfig.setStatus(_A)
class _AtiL2DevicePortSTPConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AtiL2DevicePortSTPConfig_Type.__name__=_D
_AtiL2DevicePortSTPConfig_Object=MibTableColumn
atiL2DevicePortSTPConfig=_AtiL2DevicePortSTPConfig_Object((1,3,6,1,4,1,207,8,33,7,1,1,10),_AtiL2DevicePortSTPConfig_Type())
atiL2DevicePortSTPConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortSTPConfig.setStatus(_A)
class _AtiL2DevicePortBridgeid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_AtiL2DevicePortBridgeid_Type.__name__=_D
_AtiL2DevicePortBridgeid_Object=MibTableColumn
atiL2DevicePortBridgeid=_AtiL2DevicePortBridgeid_Object((1,3,6,1,4,1,207,8,33,7,1,1,11),_AtiL2DevicePortBridgeid_Type())
atiL2DevicePortBridgeid.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortBridgeid.setStatus(_A)
class _AtiL2DevicePortSTPCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiL2DevicePortSTPCost_Type.__name__=_D
_AtiL2DevicePortSTPCost_Object=MibTableColumn
atiL2DevicePortSTPCost=_AtiL2DevicePortSTPCost_Object((1,3,6,1,4,1,207,8,33,7,1,1,12),_AtiL2DevicePortSTPCost_Type())
atiL2DevicePortSTPCost.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortSTPCost.setStatus(_A)
class _AtiL2DevicePortSTPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtiL2DevicePortSTPPriority_Type.__name__=_D
_AtiL2DevicePortSTPPriority_Object=MibTableColumn
atiL2DevicePortSTPPriority=_AtiL2DevicePortSTPPriority_Object((1,3,6,1,4,1,207,8,33,7,1,1,13),_AtiL2DevicePortSTPPriority_Type())
atiL2DevicePortSTPPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortSTPPriority.setStatus(_A)
class _AtiL2DevicePortFlowControlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_AtiL2DevicePortFlowControlEnable_Type.__name__=_D
_AtiL2DevicePortFlowControlEnable_Object=MibTableColumn
atiL2DevicePortFlowControlEnable=_AtiL2DevicePortFlowControlEnable_Object((1,3,6,1,4,1,207,8,33,7,1,1,14),_AtiL2DevicePortFlowControlEnable_Type())
atiL2DevicePortFlowControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortFlowControlEnable.setStatus(_I)
class _AtiL2DevicePortBackPressureEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_AtiL2DevicePortBackPressureEnable_Type.__name__=_D
_AtiL2DevicePortBackPressureEnable_Object=MibTableColumn
atiL2DevicePortBackPressureEnable=_AtiL2DevicePortBackPressureEnable_Object((1,3,6,1,4,1,207,8,33,7,1,1,15),_AtiL2DevicePortBackPressureEnable_Type())
atiL2DevicePortBackPressureEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortBackPressureEnable.setStatus(_I)
class _AtiL2DevicePortVlanTagPriorityConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('use-vlan-priority',1),('override-vlan-priority',2)))
_AtiL2DevicePortVlanTagPriorityConfig_Type.__name__=_D
_AtiL2DevicePortVlanTagPriorityConfig_Object=MibTableColumn
atiL2DevicePortVlanTagPriorityConfig=_AtiL2DevicePortVlanTagPriorityConfig_Object((1,3,6,1,4,1,207,8,33,7,1,1,16),_AtiL2DevicePortVlanTagPriorityConfig_Type())
atiL2DevicePortVlanTagPriorityConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortVlanTagPriorityConfig.setStatus(_I)
class _AtiL2DevicePortQOSPriorityConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high-priority',1),('normal-priority',2)))
_AtiL2DevicePortQOSPriorityConfig_Type.__name__=_D
_AtiL2DevicePortQOSPriorityConfig_Object=MibTableColumn
atiL2DevicePortQOSPriorityConfig=_AtiL2DevicePortQOSPriorityConfig_Object((1,3,6,1,4,1,207,8,33,7,1,1,17),_AtiL2DevicePortQOSPriorityConfig_Type())
atiL2DevicePortQOSPriorityConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2DevicePortQOSPriorityConfig.setStatus(_I)
_AtiL2VlanConfigGroup_ObjectIdentity=ObjectIdentity
atiL2VlanConfigGroup=_AtiL2VlanConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,8))
_AtiL2BasicVlanTable_Object=MibTable
atiL2BasicVlanTable=_AtiL2BasicVlanTable_Object((1,3,6,1,4,1,207,8,33,8,1))
if mibBuilder.loadTexts:atiL2BasicVlanTable.setStatus(_A)
_AtiL2BasicVlanEntry_Object=MibTableRow
atiL2BasicVlanEntry=_AtiL2BasicVlanEntry_Object((1,3,6,1,4,1,207,8,33,8,1,1))
atiL2BasicVlanEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:atiL2BasicVlanEntry.setStatus(_A)
class _AtiL2BeVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_AtiL2BeVlanIndex_Type.__name__=_D
_AtiL2BeVlanIndex_Object=MibTableColumn
atiL2BeVlanIndex=_AtiL2BeVlanIndex_Object((1,3,6,1,4,1,207,8,33,8,1,1,1),_AtiL2BeVlanIndex_Type())
atiL2BeVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BeVlanIndex.setStatus(_A)
class _AtiL2BeVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiL2BeVlanName_Type.__name__=_F
_AtiL2BeVlanName_Object=MibTableColumn
atiL2BeVlanName=_AtiL2BeVlanName_Object((1,3,6,1,4,1,207,8,33,8,1,1,2),_AtiL2BeVlanName_Type())
atiL2BeVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanName.setStatus(_A)
class _AtiL2BeVlanTagId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AtiL2BeVlanTagId_Type.__name__=_D
_AtiL2BeVlanTagId_Object=MibTableColumn
atiL2BeVlanTagId=_AtiL2BeVlanTagId_Object((1,3,6,1,4,1,207,8,33,8,1,1,3),_AtiL2BeVlanTagId_Type())
atiL2BeVlanTagId.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanTagId.setStatus(_A)
_AtiL2BeVlanModule1UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule1UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule1UntaggedPorts=_AtiL2BeVlanModule1UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,4),_AtiL2BeVlanModule1UntaggedPorts_Type())
atiL2BeVlanModule1UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule1UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule1TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule1TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule1TaggedPorts=_AtiL2BeVlanModule1TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,5),_AtiL2BeVlanModule1TaggedPorts_Type())
atiL2BeVlanModule1TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule1TaggedPorts.setStatus(_A)
_AtiL2BeVlanModule2UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule2UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule2UntaggedPorts=_AtiL2BeVlanModule2UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,6),_AtiL2BeVlanModule2UntaggedPorts_Type())
atiL2BeVlanModule2UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule2UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule2TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule2TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule2TaggedPorts=_AtiL2BeVlanModule2TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,7),_AtiL2BeVlanModule2TaggedPorts_Type())
atiL2BeVlanModule2TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule2TaggedPorts.setStatus(_A)
_AtiL2BeVlanModule3UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule3UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule3UntaggedPorts=_AtiL2BeVlanModule3UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,8),_AtiL2BeVlanModule3UntaggedPorts_Type())
atiL2BeVlanModule3UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule3UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule3TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule3TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule3TaggedPorts=_AtiL2BeVlanModule3TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,9),_AtiL2BeVlanModule3TaggedPorts_Type())
atiL2BeVlanModule3TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule3TaggedPorts.setStatus(_A)
_AtiL2BeVlanModule4UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule4UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule4UntaggedPorts=_AtiL2BeVlanModule4UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,10),_AtiL2BeVlanModule4UntaggedPorts_Type())
atiL2BeVlanModule4UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule4UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule4TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule4TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule4TaggedPorts=_AtiL2BeVlanModule4TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,11),_AtiL2BeVlanModule4TaggedPorts_Type())
atiL2BeVlanModule4TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule4TaggedPorts.setStatus(_A)
_AtiL2BeVlanModule5UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule5UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule5UntaggedPorts=_AtiL2BeVlanModule5UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,12),_AtiL2BeVlanModule5UntaggedPorts_Type())
atiL2BeVlanModule5UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule5UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule5TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule5TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule5TaggedPorts=_AtiL2BeVlanModule5TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,13),_AtiL2BeVlanModule5TaggedPorts_Type())
atiL2BeVlanModule5TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule5TaggedPorts.setStatus(_A)
_AtiL2BeVlanModule6UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule6UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule6UntaggedPorts=_AtiL2BeVlanModule6UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,14),_AtiL2BeVlanModule6UntaggedPorts_Type())
atiL2BeVlanModule6UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule6UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule6TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule6TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule6TaggedPorts=_AtiL2BeVlanModule6TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,15),_AtiL2BeVlanModule6TaggedPorts_Type())
atiL2BeVlanModule6TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule6TaggedPorts.setStatus(_A)
_AtiL2BeVlanModule7UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule7UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule7UntaggedPorts=_AtiL2BeVlanModule7UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,16),_AtiL2BeVlanModule7UntaggedPorts_Type())
atiL2BeVlanModule7UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule7UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule7TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule7TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule7TaggedPorts=_AtiL2BeVlanModule7TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,17),_AtiL2BeVlanModule7TaggedPorts_Type())
atiL2BeVlanModule7TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule7TaggedPorts.setStatus(_A)
_AtiL2BeVlanModule8UntaggedPorts_Type=DisplayString
_AtiL2BeVlanModule8UntaggedPorts_Object=MibTableColumn
atiL2BeVlanModule8UntaggedPorts=_AtiL2BeVlanModule8UntaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,18),_AtiL2BeVlanModule8UntaggedPorts_Type())
atiL2BeVlanModule8UntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule8UntaggedPorts.setStatus(_A)
_AtiL2BeVlanModule8TaggedPorts_Type=DisplayString
_AtiL2BeVlanModule8TaggedPorts_Object=MibTableColumn
atiL2BeVlanModule8TaggedPorts=_AtiL2BeVlanModule8TaggedPorts_Object((1,3,6,1,4,1,207,8,33,8,1,1,19),_AtiL2BeVlanModule8TaggedPorts_Type())
atiL2BeVlanModule8TaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanModule8TaggedPorts.setStatus(_A)
class _AtiL2BeVlanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('operational',2),('under-construction',3),('not-operational',4)))
_AtiL2BeVlanRowStatus_Type.__name__=_D
_AtiL2BeVlanRowStatus_Object=MibTableColumn
atiL2BeVlanRowStatus=_AtiL2BeVlanRowStatus_Object((1,3,6,1,4,1,207,8,33,8,1,1,20),_AtiL2BeVlanRowStatus_Type())
atiL2BeVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BeVlanRowStatus.setStatus(_A)
_AtiL2Port2VlanTable_Object=MibTable
atiL2Port2VlanTable=_AtiL2Port2VlanTable_Object((1,3,6,1,4,1,207,8,33,8,2))
if mibBuilder.loadTexts:atiL2Port2VlanTable.setStatus(_A)
_AtiL2Port2VlanEntry_Object=MibTableRow
atiL2Port2VlanEntry=_AtiL2Port2VlanEntry_Object((1,3,6,1,4,1,207,8,33,8,2,1))
atiL2Port2VlanEntry.setIndexNames((0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:atiL2Port2VlanEntry.setStatus(_A)
_AtiL2PvModuleId_Type=Integer32
_AtiL2PvModuleId_Object=MibTableColumn
atiL2PvModuleId=_AtiL2PvModuleId_Object((1,3,6,1,4,1,207,8,33,8,2,1,1),_AtiL2PvModuleId_Type())
atiL2PvModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2PvModuleId.setStatus(_A)
_AtiL2PvPortNumber_Type=Integer32
_AtiL2PvPortNumber_Object=MibTableColumn
atiL2PvPortNumber=_AtiL2PvPortNumber_Object((1,3,6,1,4,1,207,8,33,8,2,1,2),_AtiL2PvPortNumber_Type())
atiL2PvPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2PvPortNumber.setStatus(_A)
_AtiL2PvVlanName_Type=DisplayString
_AtiL2PvVlanName_Object=MibTableColumn
atiL2PvVlanName=_AtiL2PvVlanName_Object((1,3,6,1,4,1,207,8,33,8,2,1,3),_AtiL2PvVlanName_Type())
atiL2PvVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2PvVlanName.setStatus(_A)
_AtiL2IfExt_ObjectIdentity=ObjectIdentity
atiL2IfExt=_AtiL2IfExt_ObjectIdentity((1,3,6,1,4,1,207,8,33,9))
_AtiL2IfExtensions_ObjectIdentity=ObjectIdentity
atiL2IfExtensions=_AtiL2IfExtensions_ObjectIdentity((1,3,6,1,4,1,207,8,33,9,1))
_AtiIfExtnTable_Object=MibTable
atiIfExtnTable=_AtiIfExtnTable_Object((1,3,6,1,4,1,207,8,33,9,1,1))
if mibBuilder.loadTexts:atiIfExtnTable.setStatus(_A)
_AtiIfExtnEntry_Object=MibTableRow
atiIfExtnEntry=_AtiIfExtnEntry_Object((1,3,6,1,4,1,207,8,33,9,1,1,1))
atiIfExtnEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:atiIfExtnEntry.setStatus(_A)
class _AtiIfExtnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_AtiIfExtnIndex_Type.__name__=_D
_AtiIfExtnIndex_Object=MibTableColumn
atiIfExtnIndex=_AtiIfExtnIndex_Object((1,3,6,1,4,1,207,8,33,9,1,1,1,1),_AtiIfExtnIndex_Type())
atiIfExtnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiIfExtnIndex.setStatus(_A)
class _AtiIfExtnModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiIfExtnModuleId_Type.__name__=_D
_AtiIfExtnModuleId_Object=MibTableColumn
atiIfExtnModuleId=_AtiIfExtnModuleId_Object((1,3,6,1,4,1,207,8,33,9,1,1,1,2),_AtiIfExtnModuleId_Type())
atiIfExtnModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiIfExtnModuleId.setStatus(_A)
class _AtiIfExtnPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AtiIfExtnPort_Type.__name__=_D
_AtiIfExtnPort_Object=MibTableColumn
atiIfExtnPort=_AtiIfExtnPort_Object((1,3,6,1,4,1,207,8,33,9,1,1,1,3),_AtiIfExtnPort_Type())
atiIfExtnPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiIfExtnPort.setStatus(_A)
_AtiL2BridgeMib_ObjectIdentity=ObjectIdentity
atiL2BridgeMib=_AtiL2BridgeMib_ObjectIdentity((1,3,6,1,4,1,207,8,33,10))
_AtiL2BrBase_ObjectIdentity=ObjectIdentity
atiL2BrBase=_AtiL2BrBase_ObjectIdentity((1,3,6,1,4,1,207,8,33,10,1))
_AtiL2BrBaseTable_Object=MibTable
atiL2BrBaseTable=_AtiL2BrBaseTable_Object((1,3,6,1,4,1,207,8,33,10,1,1))
if mibBuilder.loadTexts:atiL2BrBaseTable.setStatus(_A)
_AtiL2BrBaseEntry_Object=MibTableRow
atiL2BrBaseEntry=_AtiL2BrBaseEntry_Object((1,3,6,1,4,1,207,8,33,10,1,1,1))
atiL2BrBaseEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:atiL2BrBaseEntry.setStatus(_A)
_AtiL2BrBaseLanId_Type=Integer32
_AtiL2BrBaseLanId_Object=MibTableColumn
atiL2BrBaseLanId=_AtiL2BrBaseLanId_Object((1,3,6,1,4,1,207,8,33,10,1,1,1,1),_AtiL2BrBaseLanId_Type())
atiL2BrBaseLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBaseLanId.setStatus(_A)
_AtiL2BrBaseBridgeAddress_Type=MacAddress
_AtiL2BrBaseBridgeAddress_Object=MibTableColumn
atiL2BrBaseBridgeAddress=_AtiL2BrBaseBridgeAddress_Object((1,3,6,1,4,1,207,8,33,10,1,1,1,2),_AtiL2BrBaseBridgeAddress_Type())
atiL2BrBaseBridgeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBaseBridgeAddress.setStatus(_A)
_AtiL2BrBaseNumPorts_Type=Integer32
_AtiL2BrBaseNumPorts_Object=MibTableColumn
atiL2BrBaseNumPorts=_AtiL2BrBaseNumPorts_Object((1,3,6,1,4,1,207,8,33,10,1,1,1,3),_AtiL2BrBaseNumPorts_Type())
atiL2BrBaseNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBaseNumPorts.setStatus(_A)
class _AtiL2BrBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('transparent-only',2),('sourceroute-only',3),('srt',4)))
_AtiL2BrBaseType_Type.__name__=_D
_AtiL2BrBaseType_Object=MibTableColumn
atiL2BrBaseType=_AtiL2BrBaseType_Object((1,3,6,1,4,1,207,8,33,10,1,1,1,4),_AtiL2BrBaseType_Type())
atiL2BrBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBaseType.setStatus(_A)
_AtiL2BrBasePortTable_Object=MibTable
atiL2BrBasePortTable=_AtiL2BrBasePortTable_Object((1,3,6,1,4,1,207,8,33,10,1,4))
if mibBuilder.loadTexts:atiL2BrBasePortTable.setStatus(_A)
_AtiL2BrBasePortEntry_Object=MibTableRow
atiL2BrBasePortEntry=_AtiL2BrBasePortEntry_Object((1,3,6,1,4,1,207,8,33,10,1,4,1))
atiL2BrBasePortEntry.setIndexNames((0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:atiL2BrBasePortEntry.setStatus(_A)
_AtiL2BrBasePortLanId_Type=Integer32
_AtiL2BrBasePortLanId_Object=MibTableColumn
atiL2BrBasePortLanId=_AtiL2BrBasePortLanId_Object((1,3,6,1,4,1,207,8,33,10,1,4,1,1),_AtiL2BrBasePortLanId_Type())
atiL2BrBasePortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBasePortLanId.setStatus(_A)
class _AtiL2BrBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiL2BrBasePort_Type.__name__=_D
_AtiL2BrBasePort_Object=MibTableColumn
atiL2BrBasePort=_AtiL2BrBasePort_Object((1,3,6,1,4,1,207,8,33,10,1,4,1,2),_AtiL2BrBasePort_Type())
atiL2BrBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBasePort.setStatus(_A)
_AtiL2BrBasePortIfIndex_Type=Integer32
_AtiL2BrBasePortIfIndex_Object=MibTableColumn
atiL2BrBasePortIfIndex=_AtiL2BrBasePortIfIndex_Object((1,3,6,1,4,1,207,8,33,10,1,4,1,3),_AtiL2BrBasePortIfIndex_Type())
atiL2BrBasePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBasePortIfIndex.setStatus(_A)
_AtiL2BrBasePortCircuit_Type=ObjectIdentifier
_AtiL2BrBasePortCircuit_Object=MibTableColumn
atiL2BrBasePortCircuit=_AtiL2BrBasePortCircuit_Object((1,3,6,1,4,1,207,8,33,10,1,4,1,4),_AtiL2BrBasePortCircuit_Type())
atiL2BrBasePortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBasePortCircuit.setStatus(_A)
_AtiL2BrBasePortDelayExceededDiscards_Type=Counter32
_AtiL2BrBasePortDelayExceededDiscards_Object=MibTableColumn
atiL2BrBasePortDelayExceededDiscards=_AtiL2BrBasePortDelayExceededDiscards_Object((1,3,6,1,4,1,207,8,33,10,1,4,1,5),_AtiL2BrBasePortDelayExceededDiscards_Type())
atiL2BrBasePortDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBasePortDelayExceededDiscards.setStatus(_A)
_AtiL2BrBasePortMtuExceededDiscards_Type=Counter32
_AtiL2BrBasePortMtuExceededDiscards_Object=MibTableColumn
atiL2BrBasePortMtuExceededDiscards=_AtiL2BrBasePortMtuExceededDiscards_Object((1,3,6,1,4,1,207,8,33,10,1,4,1,6),_AtiL2BrBasePortMtuExceededDiscards_Type())
atiL2BrBasePortMtuExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrBasePortMtuExceededDiscards.setStatus(_A)
_AtiL2BrStp_ObjectIdentity=ObjectIdentity
atiL2BrStp=_AtiL2BrStp_ObjectIdentity((1,3,6,1,4,1,207,8,33,10,2))
_AtiL2BrStpTable_Object=MibTable
atiL2BrStpTable=_AtiL2BrStpTable_Object((1,3,6,1,4,1,207,8,33,10,2,1))
if mibBuilder.loadTexts:atiL2BrStpTable.setStatus(_A)
_AtiL2BrStpEntry_Object=MibTableRow
atiL2BrStpEntry=_AtiL2BrStpEntry_Object((1,3,6,1,4,1,207,8,33,10,2,1,1))
atiL2BrStpEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:atiL2BrStpEntry.setStatus(_A)
_AtiL2BrStpLanId_Type=Integer32
_AtiL2BrStpLanId_Object=MibTableColumn
atiL2BrStpLanId=_AtiL2BrStpLanId_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,1),_AtiL2BrStpLanId_Type())
atiL2BrStpLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpLanId.setStatus(_A)
class _AtiL2BrStpProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('decLb100',2),('ieee8021d',3)))
_AtiL2BrStpProtocolSpecification_Type.__name__=_D
_AtiL2BrStpProtocolSpecification_Object=MibTableColumn
atiL2BrStpProtocolSpecification=_AtiL2BrStpProtocolSpecification_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,2),_AtiL2BrStpProtocolSpecification_Type())
atiL2BrStpProtocolSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpProtocolSpecification.setStatus(_A)
class _AtiL2BrStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtiL2BrStpPriority_Type.__name__=_D
_AtiL2BrStpPriority_Object=MibTableColumn
atiL2BrStpPriority=_AtiL2BrStpPriority_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,3),_AtiL2BrStpPriority_Type())
atiL2BrStpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrStpPriority.setStatus(_A)
_AtiL2BrStpTimeSinceTopologyChange_Type=TimeTicks
_AtiL2BrStpTimeSinceTopologyChange_Object=MibTableColumn
atiL2BrStpTimeSinceTopologyChange=_AtiL2BrStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,4),_AtiL2BrStpTimeSinceTopologyChange_Type())
atiL2BrStpTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpTimeSinceTopologyChange.setStatus(_A)
_AtiL2BrStpTopChanges_Type=Counter32
_AtiL2BrStpTopChanges_Object=MibTableColumn
atiL2BrStpTopChanges=_AtiL2BrStpTopChanges_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,5),_AtiL2BrStpTopChanges_Type())
atiL2BrStpTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpTopChanges.setStatus(_A)
_AtiL2BrStpDesignatedRoot_Type=BridgeId
_AtiL2BrStpDesignatedRoot_Object=MibTableColumn
atiL2BrStpDesignatedRoot=_AtiL2BrStpDesignatedRoot_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,6),_AtiL2BrStpDesignatedRoot_Type())
atiL2BrStpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpDesignatedRoot.setStatus(_A)
_AtiL2BrStpRootCost_Type=Integer32
_AtiL2BrStpRootCost_Object=MibTableColumn
atiL2BrStpRootCost=_AtiL2BrStpRootCost_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,7),_AtiL2BrStpRootCost_Type())
atiL2BrStpRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpRootCost.setStatus(_A)
_AtiL2BrStpRootPort_Type=Integer32
_AtiL2BrStpRootPort_Object=MibTableColumn
atiL2BrStpRootPort=_AtiL2BrStpRootPort_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,8),_AtiL2BrStpRootPort_Type())
atiL2BrStpRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpRootPort.setStatus(_A)
_AtiL2BrStpMaxAge_Type=Timeout
_AtiL2BrStpMaxAge_Object=MibTableColumn
atiL2BrStpMaxAge=_AtiL2BrStpMaxAge_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,9),_AtiL2BrStpMaxAge_Type())
atiL2BrStpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpMaxAge.setStatus(_A)
_AtiL2BrStpHelloTime_Type=Timeout
_AtiL2BrStpHelloTime_Object=MibTableColumn
atiL2BrStpHelloTime=_AtiL2BrStpHelloTime_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,10),_AtiL2BrStpHelloTime_Type())
atiL2BrStpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpHelloTime.setStatus(_A)
_AtiL2BrStpHoldTime_Type=Integer32
_AtiL2BrStpHoldTime_Object=MibTableColumn
atiL2BrStpHoldTime=_AtiL2BrStpHoldTime_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,11),_AtiL2BrStpHoldTime_Type())
atiL2BrStpHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpHoldTime.setStatus(_A)
_AtiL2BrStpForwardDelay_Type=Timeout
_AtiL2BrStpForwardDelay_Object=MibTableColumn
atiL2BrStpForwardDelay=_AtiL2BrStpForwardDelay_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,12),_AtiL2BrStpForwardDelay_Type())
atiL2BrStpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpForwardDelay.setStatus(_A)
class _AtiL2BrStpBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_AtiL2BrStpBridgeMaxAge_Type.__name__=_L
_AtiL2BrStpBridgeMaxAge_Object=MibTableColumn
atiL2BrStpBridgeMaxAge=_AtiL2BrStpBridgeMaxAge_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,13),_AtiL2BrStpBridgeMaxAge_Type())
atiL2BrStpBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrStpBridgeMaxAge.setStatus(_A)
class _AtiL2BrStpBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_AtiL2BrStpBridgeHelloTime_Type.__name__=_L
_AtiL2BrStpBridgeHelloTime_Object=MibTableColumn
atiL2BrStpBridgeHelloTime=_AtiL2BrStpBridgeHelloTime_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,14),_AtiL2BrStpBridgeHelloTime_Type())
atiL2BrStpBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrStpBridgeHelloTime.setStatus(_A)
class _AtiL2BrStpBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_AtiL2BrStpBridgeForwardDelay_Type.__name__=_L
_AtiL2BrStpBridgeForwardDelay_Object=MibTableColumn
atiL2BrStpBridgeForwardDelay=_AtiL2BrStpBridgeForwardDelay_Object((1,3,6,1,4,1,207,8,33,10,2,1,1,15),_AtiL2BrStpBridgeForwardDelay_Type())
atiL2BrStpBridgeForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrStpBridgeForwardDelay.setStatus(_A)
_AtiL2BrStpPortTable_Object=MibTable
atiL2BrStpPortTable=_AtiL2BrStpPortTable_Object((1,3,6,1,4,1,207,8,33,10,2,15))
if mibBuilder.loadTexts:atiL2BrStpPortTable.setStatus(_A)
_AtiL2BrStpPortEntry_Object=MibTableRow
atiL2BrStpPortEntry=_AtiL2BrStpPortEntry_Object((1,3,6,1,4,1,207,8,33,10,2,15,1))
atiL2BrStpPortEntry.setIndexNames((0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:atiL2BrStpPortEntry.setStatus(_A)
_AtiL2BrStpPortLanId_Type=Integer32
_AtiL2BrStpPortLanId_Object=MibTableColumn
atiL2BrStpPortLanId=_AtiL2BrStpPortLanId_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,1),_AtiL2BrStpPortLanId_Type())
atiL2BrStpPortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPortLanId.setStatus(_A)
class _AtiL2BrStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiL2BrStpPort_Type.__name__=_D
_AtiL2BrStpPort_Object=MibTableColumn
atiL2BrStpPort=_AtiL2BrStpPort_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,2),_AtiL2BrStpPort_Type())
atiL2BrStpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPort.setStatus(_A)
class _AtiL2BrStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtiL2BrStpPortPriority_Type.__name__=_D
_AtiL2BrStpPortPriority_Object=MibTableColumn
atiL2BrStpPortPriority=_AtiL2BrStpPortPriority_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,3),_AtiL2BrStpPortPriority_Type())
atiL2BrStpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrStpPortPriority.setStatus(_A)
class _AtiL2BrStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_m,2),(_n,3),(_o,4),('forwarding',5),('broken',6)))
_AtiL2BrStpPortState_Type.__name__=_D
_AtiL2BrStpPortState_Object=MibTableColumn
atiL2BrStpPortState=_AtiL2BrStpPortState_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,4),_AtiL2BrStpPortState_Type())
atiL2BrStpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPortState.setStatus(_A)
class _AtiL2BrStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_J,2)))
_AtiL2BrStpPortEnable_Type.__name__=_D
_AtiL2BrStpPortEnable_Object=MibTableColumn
atiL2BrStpPortEnable=_AtiL2BrStpPortEnable_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,5),_AtiL2BrStpPortEnable_Type())
atiL2BrStpPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrStpPortEnable.setStatus(_A)
class _AtiL2BrStpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiL2BrStpPortPathCost_Type.__name__=_D
_AtiL2BrStpPortPathCost_Object=MibTableColumn
atiL2BrStpPortPathCost=_AtiL2BrStpPortPathCost_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,6),_AtiL2BrStpPortPathCost_Type())
atiL2BrStpPortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrStpPortPathCost.setStatus(_A)
_AtiL2BrStpPortDesignatedRoot_Type=BridgeId
_AtiL2BrStpPortDesignatedRoot_Object=MibTableColumn
atiL2BrStpPortDesignatedRoot=_AtiL2BrStpPortDesignatedRoot_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,7),_AtiL2BrStpPortDesignatedRoot_Type())
atiL2BrStpPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPortDesignatedRoot.setStatus(_A)
_AtiL2BrStpPortDesignatedCost_Type=Integer32
_AtiL2BrStpPortDesignatedCost_Object=MibTableColumn
atiL2BrStpPortDesignatedCost=_AtiL2BrStpPortDesignatedCost_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,8),_AtiL2BrStpPortDesignatedCost_Type())
atiL2BrStpPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPortDesignatedCost.setStatus(_A)
_AtiL2BrStpPortDesignatedBridge_Type=BridgeId
_AtiL2BrStpPortDesignatedBridge_Object=MibTableColumn
atiL2BrStpPortDesignatedBridge=_AtiL2BrStpPortDesignatedBridge_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,9),_AtiL2BrStpPortDesignatedBridge_Type())
atiL2BrStpPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPortDesignatedBridge.setStatus(_A)
class _AtiL2BrStpPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AtiL2BrStpPortDesignatedPort_Type.__name__=_N
_AtiL2BrStpPortDesignatedPort_Object=MibTableColumn
atiL2BrStpPortDesignatedPort=_AtiL2BrStpPortDesignatedPort_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,10),_AtiL2BrStpPortDesignatedPort_Type())
atiL2BrStpPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPortDesignatedPort.setStatus(_A)
_AtiL2BrStpPortForwardTransitions_Type=Counter32
_AtiL2BrStpPortForwardTransitions_Object=MibTableColumn
atiL2BrStpPortForwardTransitions=_AtiL2BrStpPortForwardTransitions_Object((1,3,6,1,4,1,207,8,33,10,2,15,1,11),_AtiL2BrStpPortForwardTransitions_Type())
atiL2BrStpPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrStpPortForwardTransitions.setStatus(_A)
_AtiL2BrTp_ObjectIdentity=ObjectIdentity
atiL2BrTp=_AtiL2BrTp_ObjectIdentity((1,3,6,1,4,1,207,8,33,10,3))
_AtiL2BrTpTable_Object=MibTable
atiL2BrTpTable=_AtiL2BrTpTable_Object((1,3,6,1,4,1,207,8,33,10,3,1))
if mibBuilder.loadTexts:atiL2BrTpTable.setStatus(_A)
_AtiL2BrTpEntry_Object=MibTableRow
atiL2BrTpEntry=_AtiL2BrTpEntry_Object((1,3,6,1,4,1,207,8,33,10,3,1,1))
atiL2BrTpEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:atiL2BrTpEntry.setStatus(_A)
_AtiL2BrTpLanId_Type=Integer32
_AtiL2BrTpLanId_Object=MibTableColumn
atiL2BrTpLanId=_AtiL2BrTpLanId_Object((1,3,6,1,4,1,207,8,33,10,3,1,1,1),_AtiL2BrTpLanId_Type())
atiL2BrTpLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpLanId.setStatus(_A)
_AtiL2BrTpLearnedEntryDiscards_Type=Counter32
_AtiL2BrTpLearnedEntryDiscards_Object=MibTableColumn
atiL2BrTpLearnedEntryDiscards=_AtiL2BrTpLearnedEntryDiscards_Object((1,3,6,1,4,1,207,8,33,10,3,1,1,2),_AtiL2BrTpLearnedEntryDiscards_Type())
atiL2BrTpLearnedEntryDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpLearnedEntryDiscards.setStatus(_A)
class _AtiL2BrTpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_AtiL2BrTpAgingTime_Type.__name__=_D
_AtiL2BrTpAgingTime_Object=MibTableColumn
atiL2BrTpAgingTime=_AtiL2BrTpAgingTime_Object((1,3,6,1,4,1,207,8,33,10,3,1,1,3),_AtiL2BrTpAgingTime_Type())
atiL2BrTpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2BrTpAgingTime.setStatus(_A)
_AtiL2BrTpFdbTable_Object=MibTable
atiL2BrTpFdbTable=_AtiL2BrTpFdbTable_Object((1,3,6,1,4,1,207,8,33,10,3,3))
if mibBuilder.loadTexts:atiL2BrTpFdbTable.setStatus(_A)
_AtiL2BrTpFdbEntry_Object=MibTableRow
atiL2BrTpFdbEntry=_AtiL2BrTpFdbEntry_Object((1,3,6,1,4,1,207,8,33,10,3,3,1))
atiL2BrTpFdbEntry.setIndexNames((0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:atiL2BrTpFdbEntry.setStatus(_A)
_AtiL2BrTpFdbLanId_Type=Integer32
_AtiL2BrTpFdbLanId_Object=MibTableColumn
atiL2BrTpFdbLanId=_AtiL2BrTpFdbLanId_Object((1,3,6,1,4,1,207,8,33,10,3,3,1,1),_AtiL2BrTpFdbLanId_Type())
atiL2BrTpFdbLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpFdbLanId.setStatus(_A)
_AtiL2BrTpFdbAddress_Type=MacAddress
_AtiL2BrTpFdbAddress_Object=MibTableColumn
atiL2BrTpFdbAddress=_AtiL2BrTpFdbAddress_Object((1,3,6,1,4,1,207,8,33,10,3,3,1,2),_AtiL2BrTpFdbAddress_Type())
atiL2BrTpFdbAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpFdbAddress.setStatus(_A)
_AtiL2BrTpFdbPort_Type=Integer32
_AtiL2BrTpFdbPort_Object=MibTableColumn
atiL2BrTpFdbPort=_AtiL2BrTpFdbPort_Object((1,3,6,1,4,1,207,8,33,10,3,3,1,3),_AtiL2BrTpFdbPort_Type())
atiL2BrTpFdbPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpFdbPort.setStatus(_A)
class _AtiL2BrTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('active',2),('other',3)))
_AtiL2BrTpFdbStatus_Type.__name__=_D
_AtiL2BrTpFdbStatus_Object=MibTableColumn
atiL2BrTpFdbStatus=_AtiL2BrTpFdbStatus_Object((1,3,6,1,4,1,207,8,33,10,3,3,1,4),_AtiL2BrTpFdbStatus_Type())
atiL2BrTpFdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpFdbStatus.setStatus(_A)
_AtiL2BrTpPortTable_Object=MibTable
atiL2BrTpPortTable=_AtiL2BrTpPortTable_Object((1,3,6,1,4,1,207,8,33,10,3,4))
if mibBuilder.loadTexts:atiL2BrTpPortTable.setStatus(_A)
_AtiL2BrTpPortEntry_Object=MibTableRow
atiL2BrTpPortEntry=_AtiL2BrTpPortEntry_Object((1,3,6,1,4,1,207,8,33,10,3,4,1))
atiL2BrTpPortEntry.setIndexNames((0,_E,_A2),(0,_E,_A3))
if mibBuilder.loadTexts:atiL2BrTpPortEntry.setStatus(_A)
_AtiL2BrTpPortLanId_Type=Integer32
_AtiL2BrTpPortLanId_Object=MibTableColumn
atiL2BrTpPortLanId=_AtiL2BrTpPortLanId_Object((1,3,6,1,4,1,207,8,33,10,3,4,1,1),_AtiL2BrTpPortLanId_Type())
atiL2BrTpPortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpPortLanId.setStatus(_A)
class _AtiL2BrTpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiL2BrTpPort_Type.__name__=_D
_AtiL2BrTpPort_Object=MibTableColumn
atiL2BrTpPort=_AtiL2BrTpPort_Object((1,3,6,1,4,1,207,8,33,10,3,4,1,2),_AtiL2BrTpPort_Type())
atiL2BrTpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpPort.setStatus(_A)
_AtiL2BrTpPortMaxInfo_Type=Integer32
_AtiL2BrTpPortMaxInfo_Object=MibTableColumn
atiL2BrTpPortMaxInfo=_AtiL2BrTpPortMaxInfo_Object((1,3,6,1,4,1,207,8,33,10,3,4,1,3),_AtiL2BrTpPortMaxInfo_Type())
atiL2BrTpPortMaxInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpPortMaxInfo.setStatus(_A)
_AtiL2BrTpPortInFrames_Type=Counter32
_AtiL2BrTpPortInFrames_Object=MibTableColumn
atiL2BrTpPortInFrames=_AtiL2BrTpPortInFrames_Object((1,3,6,1,4,1,207,8,33,10,3,4,1,4),_AtiL2BrTpPortInFrames_Type())
atiL2BrTpPortInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpPortInFrames.setStatus(_A)
_AtiL2BrTpPortOutFrames_Type=Counter32
_AtiL2BrTpPortOutFrames_Object=MibTableColumn
atiL2BrTpPortOutFrames=_AtiL2BrTpPortOutFrames_Object((1,3,6,1,4,1,207,8,33,10,3,4,1,5),_AtiL2BrTpPortOutFrames_Type())
atiL2BrTpPortOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpPortOutFrames.setStatus(_A)
_AtiL2BrTpPortInDiscards_Type=Counter32
_AtiL2BrTpPortInDiscards_Object=MibTableColumn
atiL2BrTpPortInDiscards=_AtiL2BrTpPortInDiscards_Object((1,3,6,1,4,1,207,8,33,10,3,4,1,6),_AtiL2BrTpPortInDiscards_Type())
atiL2BrTpPortInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2BrTpPortInDiscards.setStatus(_A)
_AtiL2TrapAttrGroup_ObjectIdentity=ObjectIdentity
atiL2TrapAttrGroup=_AtiL2TrapAttrGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,11))
class _AtiL2TrapAttrModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiL2TrapAttrModuleId_Type.__name__=_D
_AtiL2TrapAttrModuleId_Object=MibScalar
atiL2TrapAttrModuleId=_AtiL2TrapAttrModuleId_Object((1,3,6,1,4,1,207,8,33,11,1),_AtiL2TrapAttrModuleId_Type())
atiL2TrapAttrModuleId.setMaxAccess(_A4)
if mibBuilder.loadTexts:atiL2TrapAttrModuleId.setStatus(_A)
class _AtiL2TrapAttrPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AtiL2TrapAttrPortId_Type.__name__=_D
_AtiL2TrapAttrPortId_Object=MibScalar
atiL2TrapAttrPortId=_AtiL2TrapAttrPortId_Object((1,3,6,1,4,1,207,8,33,11,2),_AtiL2TrapAttrPortId_Type())
atiL2TrapAttrPortId.setMaxAccess(_A4)
if mibBuilder.loadTexts:atiL2TrapAttrPortId.setStatus(_A)
_AtiL2QOSConfigGroup_ObjectIdentity=ObjectIdentity
atiL2QOSConfigGroup=_AtiL2QOSConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,33,12))
class _AtiL2QOSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AtiL2QOSStatus_Type.__name__=_D
_AtiL2QOSStatus_Object=MibScalar
atiL2QOSStatus=_AtiL2QOSStatus_Object((1,3,6,1,4,1,207,8,33,12,1),_AtiL2QOSStatus_Type())
atiL2QOSStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2QOSStatus.setStatus(_A)
_AtiL2TrafficMappingTable_Object=MibTable
atiL2TrafficMappingTable=_AtiL2TrafficMappingTable_Object((1,3,6,1,4,1,207,8,33,12,2))
if mibBuilder.loadTexts:atiL2TrafficMappingTable.setStatus(_A)
_AtiL2TrafficMappingEntry_Object=MibTableRow
atiL2TrafficMappingEntry=_AtiL2TrafficMappingEntry_Object((1,3,6,1,4,1,207,8,33,12,2,1))
atiL2TrafficMappingEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:atiL2TrafficMappingEntry.setStatus(_A)
class _AtiL2TrafficClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AtiL2TrafficClassIndex_Type.__name__=_D
_AtiL2TrafficClassIndex_Object=MibTableColumn
atiL2TrafficClassIndex=_AtiL2TrafficClassIndex_Object((1,3,6,1,4,1,207,8,33,12,2,1,1),_AtiL2TrafficClassIndex_Type())
atiL2TrafficClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiL2TrafficClassIndex.setStatus(_A)
class _AtiL2PriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('highest',0),('lowest',1)))
_AtiL2PriorityQueue_Type.__name__=_D
_AtiL2PriorityQueue_Object=MibTableColumn
atiL2PriorityQueue=_AtiL2PriorityQueue_Object((1,3,6,1,4,1,207,8,33,12,2,1,2),_AtiL2PriorityQueue_Type())
atiL2PriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:atiL2PriorityQueue.setStatus(_A)
newRoot=NotificationType((1,3,6,1,4,1,207,0,101))
if mibBuilder.loadTexts:newRoot.setStatus('')
topologyChange=NotificationType((1,3,6,1,4,1,207,0,102))
if mibBuilder.loadTexts:topologyChange.setStatus('')
atiL2FanStopTrap=NotificationType((1,3,6,1,4,1,207,0,103))
atiL2FanStopTrap.setObjects((_E,_K))
if mibBuilder.loadTexts:atiL2FanStopTrap.setStatus('')
atiL2TemperatureAbnormalTrap=NotificationType((1,3,6,1,4,1,207,0,104))
atiL2TemperatureAbnormalTrap.setObjects((_E,_K))
if mibBuilder.loadTexts:atiL2TemperatureAbnormalTrap.setStatus('')
atiL2PowerSupplyOutage=NotificationType((1,3,6,1,4,1,207,0,105))
atiL2PowerSupplyOutage.setObjects((_E,_K))
if mibBuilder.loadTexts:atiL2PowerSupplyOutage.setStatus('')
atiL2IntruderAlert=NotificationType((1,3,6,1,4,1,207,0,106))
atiL2IntruderAlert.setObjects(*((_E,_K),(_E,_A6)))
if mibBuilder.loadTexts:atiL2IntruderAlert.setStatus('')
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'BridgeId':BridgeId,_L:Timeout,'alliedTelesyn':alliedTelesyn,'newRoot':newRoot,'topologyChange':topologyChange,'atiL2FanStopTrap':atiL2FanStopTrap,'atiL2TemperatureAbnormalTrap':atiL2TemperatureAbnormalTrap,'atiL2PowerSupplyOutage':atiL2PowerSupplyOutage,'atiL2IntruderAlert':atiL2IntruderAlert,'atiProduct':atiProduct,'swhub':swhub,_T:at_8324,_V:at_8124XL_V2,_W:at_8326GB,_X:at_9410GB,_Y:at_8350GB,_U:at_8316F,'mibObject':mibObject,'atiL2Mib':atiL2Mib,'atiL2GlobalGroup':atiL2GlobalGroup,'atiL2SwProduct':atiL2SwProduct,'atiL2SwVersion':atiL2SwVersion,'atiL2Reset':atiL2Reset,'atiL2MirroringSourceModule':atiL2MirroringSourceModule,'atiL2MirroringSourcePort':atiL2MirroringSourcePort,'atiL2MirroringDestinationModule':atiL2MirroringDestinationModule,'atiL2MirroringDestinationPort':atiL2MirroringDestinationPort,'atiL2MirrorState':atiL2MirrorState,'atiL2IGMPState':atiL2IGMPState,'atiL2DeviceNumber':atiL2DeviceNumber,'atiL2IpGroup':atiL2IpGroup,'atiL2CurrentIpAddress':atiL2CurrentIpAddress,'atiL2ConfiguredIpAddress':atiL2ConfiguredIpAddress,'atiL2ConfiguredSubnetMask':atiL2ConfiguredSubnetMask,'atiL2ConfiguredRouter':atiL2ConfiguredRouter,'atiL2IPAddressStatus':atiL2IPAddressStatus,'atiL2DNServer':atiL2DNServer,'atiL2DefaultDomainName':atiL2DefaultDomainName,'atiL2NMGroup':atiL2NMGroup,'atiL2NwMgrTable':atiL2NwMgrTable,'atiL2NwMgrEntry':atiL2NwMgrEntry,_R:atiL2NwMgrIndex,'atiL2NwMgrIpAddr':atiL2NwMgrIpAddr,'atiL2DHCPGroup':atiL2DHCPGroup,'atiL2DHCPSysGroup':atiL2DHCPSysGroup,'atiL2DHCPCurrentDHCPClientAddress':atiL2DHCPCurrentDHCPClientAddress,'atiL2DHCPSubnetMask':atiL2DHCPSubnetMask,'atiL2DHCPCurrentRelayAgentAddress':atiL2DHCPCurrentRelayAgentAddress,'atiL2DHCPNextDHCPServerAddress':atiL2DHCPNextDHCPServerAddress,'atiL2DHCPTimerGroup':atiL2DHCPTimerGroup,'atiL2DHCPLeaseTimer':atiL2DHCPLeaseTimer,'atiL2DHCPReacquisitionTimer':atiL2DHCPReacquisitionTimer,'atiL2DHCPExpirationTimer':atiL2DHCPExpirationTimer,'atiL2DeviceGroup':atiL2DeviceGroup,'atiL2deviceTable':atiL2deviceTable,'atiL2deviceEntry':atiL2deviceEntry,_S:atiL2deviceIndex,'atiL2deviceDescr':atiL2deviceDescr,'atiL2deviceProductType':atiL2deviceProductType,'atiL2devicePortCount':atiL2devicePortCount,'atiL2deviceSecurityConfig':atiL2deviceSecurityConfig,'atiL2deviceSecurityAction':atiL2deviceSecurityAction,'atiL2deviceDebugAvailableBytes':atiL2deviceDebugAvailableBytes,'atiL2deviceMDA1Type':atiL2deviceMDA1Type,'atiL2deviceMDA2Type':atiL2deviceMDA2Type,'atiL2deviceReset':atiL2deviceReset,'atiL2EthernetStatsGroup':atiL2EthernetStatsGroup,'atiL2EthMonStatsGroup':atiL2EthMonStatsGroup,'atiL2EthMonStatsTable':atiL2EthMonStatsTable,'atiL2EthMonStatsEntry':atiL2EthMonStatsEntry,_d:atiL2EthMonModuleId,'atiL2EthMonRxGoodFrames':atiL2EthMonRxGoodFrames,'atiL2EthMonTxGoodFrames':atiL2EthMonTxGoodFrames,'atiL2EthMonTxTotalBytes':atiL2EthMonTxTotalBytes,'atiL2EthMonTxDeferred':atiL2EthMonTxDeferred,'atiL2EthMonTxCollisions':atiL2EthMonTxCollisions,'atiL2EthMonTxBroadcastFrames':atiL2EthMonTxBroadcastFrames,'atiL2EthMonTxMulticastFrames':atiL2EthMonTxMulticastFrames,'atiL2EthMonRxOverruns':atiL2EthMonRxOverruns,'atiL2EthPortMonStatsTable':atiL2EthPortMonStatsTable,'atiL2EthPortMonStatsEntry':atiL2EthPortMonStatsEntry,_e:atiL2EthPortMonModuleId,_f:atiL2EthPortMonPortId,'atiL2EthPortMonRxGoodFrames':atiL2EthPortMonRxGoodFrames,'atiL2EthPortMonTxGoodFrames':atiL2EthPortMonTxGoodFrames,'atiL2EthPortMonTxTotalBytes':atiL2EthPortMonTxTotalBytes,'atiL2EthPortMonTxDeferred':atiL2EthPortMonTxDeferred,'atiL2EthPortMonTxCollisions':atiL2EthPortMonTxCollisions,'atiL2EthPortMonTxBroadcastFrames':atiL2EthPortMonTxBroadcastFrames,'atiL2EthPortMonTxMulticastFrames':atiL2EthPortMonTxMulticastFrames,'atiL2EthPortMonRxOverruns':atiL2EthPortMonRxOverruns,'atiL2EthErrStatsGroup':atiL2EthErrStatsGroup,'atiL2EthErrStatsTable':atiL2EthErrStatsTable,'atiL2EthErrorStatsEntry':atiL2EthErrorStatsEntry,_g:atiL2EthErrModuleId,'atiL2EthErrorCRC':atiL2EthErrorCRC,'atiL2EthErrorAlignment':atiL2EthErrorAlignment,'atiL2EthErrorRxBadFrames':atiL2EthErrorRxBadFrames,'atiL2EthErrorLateCollisions':atiL2EthErrorLateCollisions,'atiL2EthErrorTxTotal':atiL2EthErrorTxTotal,'atiL2EthPortErrStatsTable':atiL2EthPortErrStatsTable,'atiL2EthPortErrorStatsEntry':atiL2EthPortErrorStatsEntry,_h:atiL2EthPortErrModuleId,_i:atiL2EthPortErrPortId,'atiL2EthPortErrorCRC':atiL2EthPortErrorCRC,'atiL2EthPortErrorAlignment':atiL2EthPortErrorAlignment,'atiL2EthPortErrorRxBadFrames':atiL2EthPortErrorRxBadFrames,'atiL2EthPortErrorLateCollisions':atiL2EthPortErrorLateCollisions,'atiL2EthPortErrorTxTotal':atiL2EthPortErrorTxTotal,'atiL2DevicePortConfigGroup':atiL2DevicePortConfigGroup,'atiL2DevicePortTable':atiL2DevicePortTable,'atiL2DevicePortEntry':atiL2DevicePortEntry,_j:atiL2DeviceId,_k:atiL2DevicePortNumber,'atiL2DevicePortName':atiL2DevicePortName,'atiL2DevicePortAutosenseOrHalfDuplex':atiL2DevicePortAutosenseOrHalfDuplex,'atiL2DevicePortLinkState':atiL2DevicePortLinkState,'atiL2DevicePortDuplexStatus':atiL2DevicePortDuplexStatus,'atiL2DevicePortSpeed':atiL2DevicePortSpeed,'atiL2DevicePortState':atiL2DevicePortState,'atiL2DevicePortTransmitPacingConfig':atiL2DevicePortTransmitPacingConfig,'atiL2DevicePortSTPConfig':atiL2DevicePortSTPConfig,'atiL2DevicePortBridgeid':atiL2DevicePortBridgeid,'atiL2DevicePortSTPCost':atiL2DevicePortSTPCost,'atiL2DevicePortSTPPriority':atiL2DevicePortSTPPriority,'atiL2DevicePortFlowControlEnable':atiL2DevicePortFlowControlEnable,'atiL2DevicePortBackPressureEnable':atiL2DevicePortBackPressureEnable,'atiL2DevicePortVlanTagPriorityConfig':atiL2DevicePortVlanTagPriorityConfig,'atiL2DevicePortQOSPriorityConfig':atiL2DevicePortQOSPriorityConfig,'atiL2VlanConfigGroup':atiL2VlanConfigGroup,'atiL2BasicVlanTable':atiL2BasicVlanTable,'atiL2BasicVlanEntry':atiL2BasicVlanEntry,_p:atiL2BeVlanIndex,'atiL2BeVlanName':atiL2BeVlanName,'atiL2BeVlanTagId':atiL2BeVlanTagId,'atiL2BeVlanModule1UntaggedPorts':atiL2BeVlanModule1UntaggedPorts,'atiL2BeVlanModule1TaggedPorts':atiL2BeVlanModule1TaggedPorts,'atiL2BeVlanModule2UntaggedPorts':atiL2BeVlanModule2UntaggedPorts,'atiL2BeVlanModule2TaggedPorts':atiL2BeVlanModule2TaggedPorts,'atiL2BeVlanModule3UntaggedPorts':atiL2BeVlanModule3UntaggedPorts,'atiL2BeVlanModule3TaggedPorts':atiL2BeVlanModule3TaggedPorts,'atiL2BeVlanModule4UntaggedPorts':atiL2BeVlanModule4UntaggedPorts,'atiL2BeVlanModule4TaggedPorts':atiL2BeVlanModule4TaggedPorts,'atiL2BeVlanModule5UntaggedPorts':atiL2BeVlanModule5UntaggedPorts,'atiL2BeVlanModule5TaggedPorts':atiL2BeVlanModule5TaggedPorts,'atiL2BeVlanModule6UntaggedPorts':atiL2BeVlanModule6UntaggedPorts,'atiL2BeVlanModule6TaggedPorts':atiL2BeVlanModule6TaggedPorts,'atiL2BeVlanModule7UntaggedPorts':atiL2BeVlanModule7UntaggedPorts,'atiL2BeVlanModule7TaggedPorts':atiL2BeVlanModule7TaggedPorts,'atiL2BeVlanModule8UntaggedPorts':atiL2BeVlanModule8UntaggedPorts,'atiL2BeVlanModule8TaggedPorts':atiL2BeVlanModule8TaggedPorts,'atiL2BeVlanRowStatus':atiL2BeVlanRowStatus,'atiL2Port2VlanTable':atiL2Port2VlanTable,'atiL2Port2VlanEntry':atiL2Port2VlanEntry,_q:atiL2PvModuleId,_r:atiL2PvPortNumber,'atiL2PvVlanName':atiL2PvVlanName,'atiL2IfExt':atiL2IfExt,'atiL2IfExtensions':atiL2IfExtensions,'atiIfExtnTable':atiIfExtnTable,'atiIfExtnEntry':atiIfExtnEntry,_s:atiIfExtnIndex,'atiIfExtnModuleId':atiIfExtnModuleId,'atiIfExtnPort':atiIfExtnPort,'atiL2BridgeMib':atiL2BridgeMib,'atiL2BrBase':atiL2BrBase,'atiL2BrBaseTable':atiL2BrBaseTable,'atiL2BrBaseEntry':atiL2BrBaseEntry,_t:atiL2BrBaseLanId,'atiL2BrBaseBridgeAddress':atiL2BrBaseBridgeAddress,'atiL2BrBaseNumPorts':atiL2BrBaseNumPorts,'atiL2BrBaseType':atiL2BrBaseType,'atiL2BrBasePortTable':atiL2BrBasePortTable,'atiL2BrBasePortEntry':atiL2BrBasePortEntry,_u:atiL2BrBasePortLanId,_v:atiL2BrBasePort,'atiL2BrBasePortIfIndex':atiL2BrBasePortIfIndex,'atiL2BrBasePortCircuit':atiL2BrBasePortCircuit,'atiL2BrBasePortDelayExceededDiscards':atiL2BrBasePortDelayExceededDiscards,'atiL2BrBasePortMtuExceededDiscards':atiL2BrBasePortMtuExceededDiscards,'atiL2BrStp':atiL2BrStp,'atiL2BrStpTable':atiL2BrStpTable,'atiL2BrStpEntry':atiL2BrStpEntry,_w:atiL2BrStpLanId,'atiL2BrStpProtocolSpecification':atiL2BrStpProtocolSpecification,'atiL2BrStpPriority':atiL2BrStpPriority,'atiL2BrStpTimeSinceTopologyChange':atiL2BrStpTimeSinceTopologyChange,'atiL2BrStpTopChanges':atiL2BrStpTopChanges,'atiL2BrStpDesignatedRoot':atiL2BrStpDesignatedRoot,'atiL2BrStpRootCost':atiL2BrStpRootCost,'atiL2BrStpRootPort':atiL2BrStpRootPort,'atiL2BrStpMaxAge':atiL2BrStpMaxAge,'atiL2BrStpHelloTime':atiL2BrStpHelloTime,'atiL2BrStpHoldTime':atiL2BrStpHoldTime,'atiL2BrStpForwardDelay':atiL2BrStpForwardDelay,'atiL2BrStpBridgeMaxAge':atiL2BrStpBridgeMaxAge,'atiL2BrStpBridgeHelloTime':atiL2BrStpBridgeHelloTime,'atiL2BrStpBridgeForwardDelay':atiL2BrStpBridgeForwardDelay,'atiL2BrStpPortTable':atiL2BrStpPortTable,'atiL2BrStpPortEntry':atiL2BrStpPortEntry,_x:atiL2BrStpPortLanId,_y:atiL2BrStpPort,'atiL2BrStpPortPriority':atiL2BrStpPortPriority,'atiL2BrStpPortState':atiL2BrStpPortState,'atiL2BrStpPortEnable':atiL2BrStpPortEnable,'atiL2BrStpPortPathCost':atiL2BrStpPortPathCost,'atiL2BrStpPortDesignatedRoot':atiL2BrStpPortDesignatedRoot,'atiL2BrStpPortDesignatedCost':atiL2BrStpPortDesignatedCost,'atiL2BrStpPortDesignatedBridge':atiL2BrStpPortDesignatedBridge,'atiL2BrStpPortDesignatedPort':atiL2BrStpPortDesignatedPort,'atiL2BrStpPortForwardTransitions':atiL2BrStpPortForwardTransitions,'atiL2BrTp':atiL2BrTp,'atiL2BrTpTable':atiL2BrTpTable,'atiL2BrTpEntry':atiL2BrTpEntry,_z:atiL2BrTpLanId,'atiL2BrTpLearnedEntryDiscards':atiL2BrTpLearnedEntryDiscards,'atiL2BrTpAgingTime':atiL2BrTpAgingTime,'atiL2BrTpFdbTable':atiL2BrTpFdbTable,'atiL2BrTpFdbEntry':atiL2BrTpFdbEntry,_A0:atiL2BrTpFdbLanId,_A1:atiL2BrTpFdbAddress,'atiL2BrTpFdbPort':atiL2BrTpFdbPort,'atiL2BrTpFdbStatus':atiL2BrTpFdbStatus,'atiL2BrTpPortTable':atiL2BrTpPortTable,'atiL2BrTpPortEntry':atiL2BrTpPortEntry,_A2:atiL2BrTpPortLanId,_A3:atiL2BrTpPort,'atiL2BrTpPortMaxInfo':atiL2BrTpPortMaxInfo,'atiL2BrTpPortInFrames':atiL2BrTpPortInFrames,'atiL2BrTpPortOutFrames':atiL2BrTpPortOutFrames,'atiL2BrTpPortInDiscards':atiL2BrTpPortInDiscards,'atiL2TrapAttrGroup':atiL2TrapAttrGroup,_K:atiL2TrapAttrModuleId,_A6:atiL2TrapAttrPortId,'atiL2QOSConfigGroup':atiL2QOSConfigGroup,'atiL2QOSStatus':atiL2QOSStatus,'atiL2TrafficMappingTable':atiL2TrafficMappingTable,'atiL2TrafficMappingEntry':atiL2TrafficMappingEntry,_A5:atiL2TrafficClassIndex,'atiL2PriorityQueue':atiL2PriorityQueue})