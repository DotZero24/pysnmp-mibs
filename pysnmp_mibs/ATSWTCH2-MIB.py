_s='atswitchDebugMallocLogIndex'
_r='atswitchPortMACPort'
_q='atswitchPortMACAddress'
_p='atswitchStaticMACAddress'
_o='atswitchBrTpPort'
_n='atswitchBrTpPortLanId'
_m='atswitchBrTpFdbAddress'
_l='atswitchBrTpFdbLanId'
_k='atswitchBrTpLanId'
_j='atswitchBrStpPort'
_i='atswitchBrStpPortLanId'
_h='atswitchBrStpLanId'
_g='atswitchBrBasePort'
_f='atswitchBrBasePortLanId'
_e='unknown'
_d='atswitchBrBaseLanId'
_c='active'
_b='inactive'
_a='atswitchFwdVlanMACAddr'
_Z='atswitchEthPortErrorId'
_Y='atswitchEthPortMonId'
_X='atswitchPvPortNumber'
_W='atswitchBeVlanIndex'
_V='learning'
_U='listening'
_T='blocking'
_S='enabled'
_R='atswitchPortNumber'
_Q='atswitchNwMgrIndex'
_P='rj45-mii'
_O='NotificationType'
_N='not-accessible'
_M='other'
_L='Timeout'
_K='OctetString'
_J='disabled'
_I='disable'
_H='enable'
_G='deprecated'
_F='DisplayString'
_E='ATSWTCH2-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
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
_MibObject_ObjectIdentity=ObjectIdentity
mibObject=_MibObject_ObjectIdentity((1,3,6,1,4,1,207,8))
_AtswitchMib_ObjectIdentity=ObjectIdentity
atswitchMib=_AtswitchMib_ObjectIdentity((1,3,6,1,4,1,207,8,10))
_AtswitchSysGroup_ObjectIdentity=ObjectIdentity
atswitchSysGroup=_AtswitchSysGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,1))
class _AtswitchProductType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,10)));namedValues=NamedValues(*(('at-3726',1),('at-3714',2),('at-8124XL',3),('at-8118',4),('at-3726XL',5),('at-3714FXL',6),('at-3716XL',7),(_M,10)))
_AtswitchProductType_Type.__name__=_D
_AtswitchProductType_Object=MibScalar
atswitchProductType=_AtswitchProductType_Object((1,3,6,1,4,1,207,8,10,1,1),_AtswitchProductType_Type())
atswitchProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchProductType.setStatus(_A)
_AtswitchEthernetPortCount_Type=Integer32
_AtswitchEthernetPortCount_Object=MibScalar
atswitchEthernetPortCount=_AtswitchEthernetPortCount_Object((1,3,6,1,4,1,207,8,10,1,2),_AtswitchEthernetPortCount_Type())
atswitchEthernetPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthernetPortCount.setStatus(_A)
class _AtswitchReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switch-no-reset',1),('switch-reset',2)))
_AtswitchReset_Type.__name__=_D
_AtswitchReset_Object=MibScalar
atswitchReset=_AtswitchReset_Object((1,3,6,1,4,1,207,8,10,1,3),_AtswitchReset_Type())
atswitchReset.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchReset.setStatus(_A)
class _AtswitchMDA1Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('fiber',2),('none',3)))
_AtswitchMDA1Type_Type.__name__=_D
_AtswitchMDA1Type_Object=MibScalar
atswitchMDA1Type=_AtswitchMDA1Type_Object((1,3,6,1,4,1,207,8,10,1,4),_AtswitchMDA1Type_Type())
atswitchMDA1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchMDA1Type.setStatus(_A)
class _AtswitchMDA2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('fiber',2),('none',3)))
_AtswitchMDA2Type_Type.__name__=_D
_AtswitchMDA2Type_Object=MibScalar
atswitchMDA2Type=_AtswitchMDA2Type_Object((1,3,6,1,4,1,207,8,10,1,5),_AtswitchMDA2Type_Type())
atswitchMDA2Type.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchMDA2Type.setStatus(_A)
class _AtswitchDeviceFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtswitchDeviceFlowControl_Type.__name__=_D
_AtswitchDeviceFlowControl_Object=MibScalar
atswitchDeviceFlowControl=_AtswitchDeviceFlowControl_Object((1,3,6,1,4,1,207,8,10,1,6),_AtswitchDeviceFlowControl_Type())
atswitchDeviceFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchDeviceFlowControl.setStatus(_A)
_AtswitchSwGroup_ObjectIdentity=ObjectIdentity
atswitchSwGroup=_AtswitchSwGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,1,7))
class _AtswitchSwProduct_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtswitchSwProduct_Type.__name__=_F
_AtswitchSwProduct_Object=MibScalar
atswitchSwProduct=_AtswitchSwProduct_Object((1,3,6,1,4,1,207,8,10,1,7,1),_AtswitchSwProduct_Type())
atswitchSwProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchSwProduct.setStatus(_A)
class _AtswitchSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtswitchSwVersion_Type.__name__=_F
_AtswitchSwVersion_Object=MibScalar
atswitchSwVersion=_AtswitchSwVersion_Object((1,3,6,1,4,1,207,8,10,1,7,2),_AtswitchSwVersion_Type())
atswitchSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchSwVersion.setStatus(_A)
_AtswitchIpGroup_ObjectIdentity=ObjectIdentity
atswitchIpGroup=_AtswitchIpGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,1,8))
_AtswitchCurrentIpAddress_Type=IpAddress
_AtswitchCurrentIpAddress_Object=MibScalar
atswitchCurrentIpAddress=_AtswitchCurrentIpAddress_Object((1,3,6,1,4,1,207,8,10,1,8,1),_AtswitchCurrentIpAddress_Type())
atswitchCurrentIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchCurrentIpAddress.setStatus(_A)
_AtswitchConfiguredIpAddress_Type=IpAddress
_AtswitchConfiguredIpAddress_Object=MibScalar
atswitchConfiguredIpAddress=_AtswitchConfiguredIpAddress_Object((1,3,6,1,4,1,207,8,10,1,8,2),_AtswitchConfiguredIpAddress_Type())
atswitchConfiguredIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchConfiguredIpAddress.setStatus(_A)
_AtswitchConfiguredSubnetMask_Type=IpAddress
_AtswitchConfiguredSubnetMask_Object=MibScalar
atswitchConfiguredSubnetMask=_AtswitchConfiguredSubnetMask_Object((1,3,6,1,4,1,207,8,10,1,8,3),_AtswitchConfiguredSubnetMask_Type())
atswitchConfiguredSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchConfiguredSubnetMask.setStatus(_A)
_AtswitchConfiguredRouter_Type=IpAddress
_AtswitchConfiguredRouter_Object=MibScalar
atswitchConfiguredRouter=_AtswitchConfiguredRouter_Object((1,3,6,1,4,1,207,8,10,1,8,4),_AtswitchConfiguredRouter_Type())
atswitchConfiguredRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchConfiguredRouter.setStatus(_A)
class _AtswitchIPAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('from-dhcp',1),('from-bootp',2),('from-psuedoip',3),('from-Omega',4)))
_AtswitchIPAddressStatus_Type.__name__=_D
_AtswitchIPAddressStatus_Object=MibScalar
atswitchIPAddressStatus=_AtswitchIPAddressStatus_Object((1,3,6,1,4,1,207,8,10,1,8,5),_AtswitchIPAddressStatus_Type())
atswitchIPAddressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchIPAddressStatus.setStatus(_A)
_AtswitchDNServer_Type=IpAddress
_AtswitchDNServer_Object=MibScalar
atswitchDNServer=_AtswitchDNServer_Object((1,3,6,1,4,1,207,8,10,1,8,6),_AtswitchDNServer_Type())
atswitchDNServer.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchDNServer.setStatus(_A)
class _AtswitchDefaultDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtswitchDefaultDomainName_Type.__name__=_F
_AtswitchDefaultDomainName_Object=MibScalar
atswitchDefaultDomainName=_AtswitchDefaultDomainName_Object((1,3,6,1,4,1,207,8,10,1,8,7),_AtswitchDefaultDomainName_Type())
atswitchDefaultDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchDefaultDomainName.setStatus(_A)
_AtswitchNMGroup_ObjectIdentity=ObjectIdentity
atswitchNMGroup=_AtswitchNMGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,1,9))
_AtswitchNwMgrTable_Object=MibTable
atswitchNwMgrTable=_AtswitchNwMgrTable_Object((1,3,6,1,4,1,207,8,10,1,9,1))
if mibBuilder.loadTexts:atswitchNwMgrTable.setStatus(_A)
_AtswitchNwMgrEntry_Object=MibTableRow
atswitchNwMgrEntry=_AtswitchNwMgrEntry_Object((1,3,6,1,4,1,207,8,10,1,9,1,1))
atswitchNwMgrEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:atswitchNwMgrEntry.setStatus(_A)
class _AtswitchNwMgrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AtswitchNwMgrIndex_Type.__name__=_D
_AtswitchNwMgrIndex_Object=MibTableColumn
atswitchNwMgrIndex=_AtswitchNwMgrIndex_Object((1,3,6,1,4,1,207,8,10,1,9,1,1,1),_AtswitchNwMgrIndex_Type())
atswitchNwMgrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchNwMgrIndex.setStatus(_A)
_AtswitchNwMgrIpAddr_Type=IpAddress
_AtswitchNwMgrIpAddr_Object=MibTableColumn
atswitchNwMgrIpAddr=_AtswitchNwMgrIpAddr_Object((1,3,6,1,4,1,207,8,10,1,9,1,1,2),_AtswitchNwMgrIpAddr_Type())
atswitchNwMgrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchNwMgrIpAddr.setStatus(_A)
_AtswitchConfigGroup_ObjectIdentity=ObjectIdentity
atswitchConfigGroup=_AtswitchConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,2))
class _AtswitchPortDisableOnSecurityViolation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable-on-security-voilation',1),('suspend-on-double-address',2),('security-not-yet-initalized',3)))
_AtswitchPortDisableOnSecurityViolation_Type.__name__=_D
_AtswitchPortDisableOnSecurityViolation_Object=MibScalar
atswitchPortDisableOnSecurityViolation=_AtswitchPortDisableOnSecurityViolation_Object((1,3,6,1,4,1,207,8,10,2,1),_AtswitchPortDisableOnSecurityViolation_Type())
atswitchPortDisableOnSecurityViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortDisableOnSecurityViolation.setStatus(_A)
_AtswitchMirroringSourcePort_Type=Integer32
_AtswitchMirroringSourcePort_Object=MibScalar
atswitchMirroringSourcePort=_AtswitchMirroringSourcePort_Object((1,3,6,1,4,1,207,8,10,2,2),_AtswitchMirroringSourcePort_Type())
atswitchMirroringSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchMirroringSourcePort.setStatus(_A)
class _AtswitchMirrorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('receive',1),('transmit',2),('both',3),(_J,4)))
_AtswitchMirrorState_Type.__name__=_D
_AtswitchMirrorState_Object=MibScalar
atswitchMirrorState=_AtswitchMirrorState_Object((1,3,6,1,4,1,207,8,10,2,3),_AtswitchMirrorState_Type())
atswitchMirrorState.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchMirrorState.setStatus(_A)
_AtswitchMirroringDestinationPort_Type=Integer32
_AtswitchMirroringDestinationPort_Object=MibScalar
atswitchMirroringDestinationPort=_AtswitchMirroringDestinationPort_Object((1,3,6,1,4,1,207,8,10,2,4),_AtswitchMirroringDestinationPort_Type())
atswitchMirroringDestinationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchMirroringDestinationPort.setStatus(_A)
class _AtswitchSecurityConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('enabled-with-learning-locked',2),('limited-enabled',3)))
_AtswitchSecurityConfig_Type.__name__=_D
_AtswitchSecurityConfig_Object=MibScalar
atswitchSecurityConfig=_AtswitchSecurityConfig_Object((1,3,6,1,4,1,207,8,10,2,5),_AtswitchSecurityConfig_Type())
atswitchSecurityConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchSecurityConfig.setStatus(_A)
class _AtswitchSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('send-trap-only',1),('disable-port-only',2),('disable-port-and-send-trap',3),('do-nothing',4)))
_AtswitchSecurityAction_Type.__name__=_D
_AtswitchSecurityAction_Object=MibScalar
atswitchSecurityAction=_AtswitchSecurityAction_Object((1,3,6,1,4,1,207,8,10,2,6),_AtswitchSecurityAction_Type())
atswitchSecurityAction.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchSecurityAction.setStatus(_A)
_AtswitchDebugAvailableBytes_Type=Integer32
_AtswitchDebugAvailableBytes_Object=MibScalar
atswitchDebugAvailableBytes=_AtswitchDebugAvailableBytes_Object((1,3,6,1,4,1,207,8,10,2,7),_AtswitchDebugAvailableBytes_Type())
atswitchDebugAvailableBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchDebugAvailableBytes.setStatus(_A)
class _AtswitchTrunkConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtswitchTrunkConfig_Type.__name__=_D
_AtswitchTrunkConfig_Object=MibScalar
atswitchTrunkConfig=_AtswitchTrunkConfig_Object((1,3,6,1,4,1,207,8,10,2,8),_AtswitchTrunkConfig_Type())
atswitchTrunkConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchTrunkConfig.setStatus(_A)
_AtswitchPortConfigGroup_ObjectIdentity=ObjectIdentity
atswitchPortConfigGroup=_AtswitchPortConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,3))
_AtswitchPortTable_Object=MibTable
atswitchPortTable=_AtswitchPortTable_Object((1,3,6,1,4,1,207,8,10,3,1))
if mibBuilder.loadTexts:atswitchPortTable.setStatus(_A)
_AtswitchPortEntry_Object=MibTableRow
atswitchPortEntry=_AtswitchPortEntry_Object((1,3,6,1,4,1,207,8,10,3,1,1))
atswitchPortEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:atswitchPortEntry.setStatus(_A)
_AtswitchPortNumber_Type=Integer32
_AtswitchPortNumber_Object=MibTableColumn
atswitchPortNumber=_AtswitchPortNumber_Object((1,3,6,1,4,1,207,8,10,3,1,1,1),_AtswitchPortNumber_Type())
atswitchPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchPortNumber.setStatus(_A)
class _AtswitchPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtswitchPortName_Type.__name__=_F
_AtswitchPortName_Object=MibTableColumn
atswitchPortName=_AtswitchPortName_Object((1,3,6,1,4,1,207,8,10,3,1,1,2),_AtswitchPortName_Type())
atswitchPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortName.setStatus(_A)
class _AtswitchPortAutosenseOrHalfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portAutoSense',1),('forceHalfDuplex',2)))
_AtswitchPortAutosenseOrHalfDuplex_Type.__name__=_D
_AtswitchPortAutosenseOrHalfDuplex_Object=MibTableColumn
atswitchPortAutosenseOrHalfDuplex=_AtswitchPortAutosenseOrHalfDuplex_Object((1,3,6,1,4,1,207,8,10,3,1,1,3),_AtswitchPortAutosenseOrHalfDuplex_Type())
atswitchPortAutosenseOrHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortAutosenseOrHalfDuplex.setStatus(_A)
class _AtswitchPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_AtswitchPortLinkState_Type.__name__=_D
_AtswitchPortLinkState_Object=MibTableColumn
atswitchPortLinkState=_AtswitchPortLinkState_Object((1,3,6,1,4,1,207,8,10,3,1,1,4),_AtswitchPortLinkState_Type())
atswitchPortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchPortLinkState.setStatus(_A)
class _AtswitchPortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fullDuplex',1),('halfDuplex',2)))
_AtswitchPortDuplexStatus_Type.__name__=_D
_AtswitchPortDuplexStatus_Object=MibTableColumn
atswitchPortDuplexStatus=_AtswitchPortDuplexStatus_Object((1,3,6,1,4,1,207,8,10,3,1,1,5),_AtswitchPortDuplexStatus_Type())
atswitchPortDuplexStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchPortDuplexStatus.setStatus(_A)
class _AtswitchPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tenMBits',1),('hundredMBits',2)))
_AtswitchPortSpeed_Type.__name__=_D
_AtswitchPortSpeed_Object=MibTableColumn
atswitchPortSpeed=_AtswitchPortSpeed_Object((1,3,6,1,4,1,207,8,10,3,1,1,6),_AtswitchPortSpeed_Type())
atswitchPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortSpeed.setStatus(_A)
class _AtswitchPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),(_J,2),(_T,3),(_U,4),(_V,5)))
_AtswitchPortState_Type.__name__=_D
_AtswitchPortState_Object=MibTableColumn
atswitchPortState=_AtswitchPortState_Object((1,3,6,1,4,1,207,8,10,3,1,1,7),_AtswitchPortState_Type())
atswitchPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortState.setStatus(_A)
class _AtswitchPortTransmitPacingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtswitchPortTransmitPacingConfig_Type.__name__=_D
_AtswitchPortTransmitPacingConfig_Object=MibTableColumn
atswitchPortTransmitPacingConfig=_AtswitchPortTransmitPacingConfig_Object((1,3,6,1,4,1,207,8,10,3,1,1,8),_AtswitchPortTransmitPacingConfig_Type())
atswitchPortTransmitPacingConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortTransmitPacingConfig.setStatus(_A)
class _AtswitchPortSTPConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtswitchPortSTPConfig_Type.__name__=_D
_AtswitchPortSTPConfig_Object=MibTableColumn
atswitchPortSTPConfig=_AtswitchPortSTPConfig_Object((1,3,6,1,4,1,207,8,10,3,1,1,9),_AtswitchPortSTPConfig_Type())
atswitchPortSTPConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortSTPConfig.setStatus(_A)
class _AtswitchPortBridgeid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_AtswitchPortBridgeid_Type.__name__=_D
_AtswitchPortBridgeid_Object=MibTableColumn
atswitchPortBridgeid=_AtswitchPortBridgeid_Object((1,3,6,1,4,1,207,8,10,3,1,1,10),_AtswitchPortBridgeid_Type())
atswitchPortBridgeid.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortBridgeid.setStatus(_A)
class _AtswitchPortSTPCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtswitchPortSTPCost_Type.__name__=_D
_AtswitchPortSTPCost_Object=MibTableColumn
atswitchPortSTPCost=_AtswitchPortSTPCost_Object((1,3,6,1,4,1,207,8,10,3,1,1,11),_AtswitchPortSTPCost_Type())
atswitchPortSTPCost.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortSTPCost.setStatus(_A)
class _AtswitchPortSTPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtswitchPortSTPPriority_Type.__name__=_D
_AtswitchPortSTPPriority_Object=MibTableColumn
atswitchPortSTPPriority=_AtswitchPortSTPPriority_Object((1,3,6,1,4,1,207,8,10,3,1,1,12),_AtswitchPortSTPPriority_Type())
atswitchPortSTPPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortSTPPriority.setStatus(_A)
class _AtswitchPortSwitchingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast-cut-through',1),('store-and-forward',2)))
_AtswitchPortSwitchingType_Type.__name__=_D
_AtswitchPortSwitchingType_Object=MibTableColumn
atswitchPortSwitchingType=_AtswitchPortSwitchingType_Object((1,3,6,1,4,1,207,8,10,3,1,1,13),_AtswitchPortSwitchingType_Type())
atswitchPortSwitchingType.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortSwitchingType.setStatus(_A)
class _AtswitchPortFlowControlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_AtswitchPortFlowControlEnable_Type.__name__=_D
_AtswitchPortFlowControlEnable_Object=MibTableColumn
atswitchPortFlowControlEnable=_AtswitchPortFlowControlEnable_Object((1,3,6,1,4,1,207,8,10,3,1,1,14),_AtswitchPortFlowControlEnable_Type())
atswitchPortFlowControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortFlowControlEnable.setStatus(_G)
_AtswitchPortSecurityNumberOfAddresses_Type=Integer32
_AtswitchPortSecurityNumberOfAddresses_Object=MibTableColumn
atswitchPortSecurityNumberOfAddresses=_AtswitchPortSecurityNumberOfAddresses_Object((1,3,6,1,4,1,207,8,10,3,1,1,15),_AtswitchPortSecurityNumberOfAddresses_Type())
atswitchPortSecurityNumberOfAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPortSecurityNumberOfAddresses.setStatus(_A)
_AtswitchVlanConfigGroup_ObjectIdentity=ObjectIdentity
atswitchVlanConfigGroup=_AtswitchVlanConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,4))
_AtswitchBasicVlanTable_Object=MibTable
atswitchBasicVlanTable=_AtswitchBasicVlanTable_Object((1,3,6,1,4,1,207,8,10,4,1))
if mibBuilder.loadTexts:atswitchBasicVlanTable.setStatus(_A)
_AtswitchBasicVlanEntry_Object=MibTableRow
atswitchBasicVlanEntry=_AtswitchBasicVlanEntry_Object((1,3,6,1,4,1,207,8,10,4,1,1))
atswitchBasicVlanEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:atswitchBasicVlanEntry.setStatus(_A)
class _AtswitchBeVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_AtswitchBeVlanIndex_Type.__name__=_D
_AtswitchBeVlanIndex_Object=MibTableColumn
atswitchBeVlanIndex=_AtswitchBeVlanIndex_Object((1,3,6,1,4,1,207,8,10,4,1,1,1),_AtswitchBeVlanIndex_Type())
atswitchBeVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBeVlanIndex.setStatus(_A)
class _AtswitchBeVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtswitchBeVlanName_Type.__name__=_F
_AtswitchBeVlanName_Object=MibTableColumn
atswitchBeVlanName=_AtswitchBeVlanName_Object((1,3,6,1,4,1,207,8,10,4,1,1,2),_AtswitchBeVlanName_Type())
atswitchBeVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBeVlanName.setStatus(_A)
class _AtswitchBeVlanTagId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AtswitchBeVlanTagId_Type.__name__=_D
_AtswitchBeVlanTagId_Object=MibTableColumn
atswitchBeVlanTagId=_AtswitchBeVlanTagId_Object((1,3,6,1,4,1,207,8,10,4,1,1,3),_AtswitchBeVlanTagId_Type())
atswitchBeVlanTagId.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBeVlanTagId.setStatus(_A)
_AtswitchBeVlanPortMask_Type=DisplayString
_AtswitchBeVlanPortMask_Object=MibTableColumn
atswitchBeVlanPortMask=_AtswitchBeVlanPortMask_Object((1,3,6,1,4,1,207,8,10,4,1,1,4),_AtswitchBeVlanPortMask_Type())
atswitchBeVlanPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBeVlanPortMask.setStatus(_A)
class _AtswitchBeVlanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('operational',2),('under-construction',3),('not-operational',4)))
_AtswitchBeVlanRowStatus_Type.__name__=_D
_AtswitchBeVlanRowStatus_Object=MibTableColumn
atswitchBeVlanRowStatus=_AtswitchBeVlanRowStatus_Object((1,3,6,1,4,1,207,8,10,4,1,1,5),_AtswitchBeVlanRowStatus_Type())
atswitchBeVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBeVlanRowStatus.setStatus(_A)
_AtswitchPort2VlanTable_Object=MibTable
atswitchPort2VlanTable=_AtswitchPort2VlanTable_Object((1,3,6,1,4,1,207,8,10,4,2))
if mibBuilder.loadTexts:atswitchPort2VlanTable.setStatus(_A)
_AtswitchPort2VlanEntry_Object=MibTableRow
atswitchPort2VlanEntry=_AtswitchPort2VlanEntry_Object((1,3,6,1,4,1,207,8,10,4,2,1))
atswitchPort2VlanEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:atswitchPort2VlanEntry.setStatus(_A)
_AtswitchPvPortNumber_Type=Integer32
_AtswitchPvPortNumber_Object=MibTableColumn
atswitchPvPortNumber=_AtswitchPvPortNumber_Object((1,3,6,1,4,1,207,8,10,4,2,1,1),_AtswitchPvPortNumber_Type())
atswitchPvPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchPvPortNumber.setStatus(_A)
_AtswitchPvVlanName_Type=DisplayString
_AtswitchPvVlanName_Object=MibTableColumn
atswitchPvVlanName=_AtswitchPvVlanName_Object((1,3,6,1,4,1,207,8,10,4,2,1,2),_AtswitchPvVlanName_Type())
atswitchPvVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchPvVlanName.setStatus(_A)
_AtswitchEthernetStatsGroup_ObjectIdentity=ObjectIdentity
atswitchEthernetStatsGroup=_AtswitchEthernetStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,5))
_AtswitchEthMonStats_ObjectIdentity=ObjectIdentity
atswitchEthMonStats=_AtswitchEthMonStats_ObjectIdentity((1,3,6,1,4,1,207,8,10,5,1))
_AtswitchEthMonRxGoodFrames_Type=Counter32
_AtswitchEthMonRxGoodFrames_Object=MibScalar
atswitchEthMonRxGoodFrames=_AtswitchEthMonRxGoodFrames_Object((1,3,6,1,4,1,207,8,10,5,1,1),_AtswitchEthMonRxGoodFrames_Type())
atswitchEthMonRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthMonRxGoodFrames.setStatus(_A)
_AtswitchEthMonTxGoodFrames_Type=Counter32
_AtswitchEthMonTxGoodFrames_Object=MibScalar
atswitchEthMonTxGoodFrames=_AtswitchEthMonTxGoodFrames_Object((1,3,6,1,4,1,207,8,10,5,1,2),_AtswitchEthMonTxGoodFrames_Type())
atswitchEthMonTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthMonTxGoodFrames.setStatus(_A)
_AtswitchEthMonTxTotalBytes_Type=Counter32
_AtswitchEthMonTxTotalBytes_Object=MibScalar
atswitchEthMonTxTotalBytes=_AtswitchEthMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,10,5,1,3),_AtswitchEthMonTxTotalBytes_Type())
atswitchEthMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthMonTxTotalBytes.setStatus(_A)
_AtswitchEthMonTxDeferred_Type=Counter32
_AtswitchEthMonTxDeferred_Object=MibScalar
atswitchEthMonTxDeferred=_AtswitchEthMonTxDeferred_Object((1,3,6,1,4,1,207,8,10,5,1,4),_AtswitchEthMonTxDeferred_Type())
atswitchEthMonTxDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthMonTxDeferred.setStatus(_A)
_AtswitchEthMonTxCollisions_Type=Counter32
_AtswitchEthMonTxCollisions_Object=MibScalar
atswitchEthMonTxCollisions=_AtswitchEthMonTxCollisions_Object((1,3,6,1,4,1,207,8,10,5,1,5),_AtswitchEthMonTxCollisions_Type())
atswitchEthMonTxCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthMonTxCollisions.setStatus(_A)
_AtswitchEthErrorStats_ObjectIdentity=ObjectIdentity
atswitchEthErrorStats=_AtswitchEthErrorStats_ObjectIdentity((1,3,6,1,4,1,207,8,10,5,2))
_AtswitchEthErrorCRC_Type=Counter32
_AtswitchEthErrorCRC_Object=MibScalar
atswitchEthErrorCRC=_AtswitchEthErrorCRC_Object((1,3,6,1,4,1,207,8,10,5,2,1),_AtswitchEthErrorCRC_Type())
atswitchEthErrorCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthErrorCRC.setStatus(_A)
_AtswitchEthErrorAlignment_Type=Counter32
_AtswitchEthErrorAlignment_Object=MibScalar
atswitchEthErrorAlignment=_AtswitchEthErrorAlignment_Object((1,3,6,1,4,1,207,8,10,5,2,2),_AtswitchEthErrorAlignment_Type())
atswitchEthErrorAlignment.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthErrorAlignment.setStatus(_A)
_AtswitchEthErrorRxBadFrames_Type=Counter32
_AtswitchEthErrorRxBadFrames_Object=MibScalar
atswitchEthErrorRxBadFrames=_AtswitchEthErrorRxBadFrames_Object((1,3,6,1,4,1,207,8,10,5,2,3),_AtswitchEthErrorRxBadFrames_Type())
atswitchEthErrorRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthErrorRxBadFrames.setStatus(_A)
_AtswitchEthErrorLateCollisions_Type=Counter32
_AtswitchEthErrorLateCollisions_Object=MibScalar
atswitchEthErrorLateCollisions=_AtswitchEthErrorLateCollisions_Object((1,3,6,1,4,1,207,8,10,5,2,4),_AtswitchEthErrorLateCollisions_Type())
atswitchEthErrorLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthErrorLateCollisions.setStatus(_A)
_AtswitchEthErrorTxTotal_Type=Counter32
_AtswitchEthErrorTxTotal_Object=MibScalar
atswitchEthErrorTxTotal=_AtswitchEthErrorTxTotal_Object((1,3,6,1,4,1,207,8,10,5,2,6),_AtswitchEthErrorTxTotal_Type())
atswitchEthErrorTxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthErrorTxTotal.setStatus(_A)
_AtswitchEthPortStatsGroup_ObjectIdentity=ObjectIdentity
atswitchEthPortStatsGroup=_AtswitchEthPortStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,6))
_AtswitchEthPortMonStats_ObjectIdentity=ObjectIdentity
atswitchEthPortMonStats=_AtswitchEthPortMonStats_ObjectIdentity((1,3,6,1,4,1,207,8,10,6,1))
_AtswitchEthPortMonTable_Object=MibTable
atswitchEthPortMonTable=_AtswitchEthPortMonTable_Object((1,3,6,1,4,1,207,8,10,6,1,1))
if mibBuilder.loadTexts:atswitchEthPortMonTable.setStatus(_A)
_AtswitchEthPortMonEntry_Object=MibTableRow
atswitchEthPortMonEntry=_AtswitchEthPortMonEntry_Object((1,3,6,1,4,1,207,8,10,6,1,1,1))
atswitchEthPortMonEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:atswitchEthPortMonEntry.setStatus(_A)
_AtswitchEthPortMonId_Type=Integer32
_AtswitchEthPortMonId_Object=MibTableColumn
atswitchEthPortMonId=_AtswitchEthPortMonId_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,1),_AtswitchEthPortMonId_Type())
atswitchEthPortMonId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthPortMonId.setStatus(_A)
_AtswitchEthPortMonTxTotalBytes_Type=Counter32
_AtswitchEthPortMonTxTotalBytes_Object=MibTableColumn
atswitchEthPortMonTxTotalBytes=_AtswitchEthPortMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,2),_AtswitchEthPortMonTxTotalBytes_Type())
atswitchEthPortMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthPortMonTxTotalBytes.setStatus(_A)
_AtswitchRxGoodFrames_Type=Counter32
_AtswitchRxGoodFrames_Object=MibTableColumn
atswitchRxGoodFrames=_AtswitchRxGoodFrames_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,3),_AtswitchRxGoodFrames_Type())
atswitchRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchRxGoodFrames.setStatus(_A)
_AtswitchTxGoodFrames_Type=Counter32
_AtswitchTxGoodFrames_Object=MibTableColumn
atswitchTxGoodFrames=_AtswitchTxGoodFrames_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,4),_AtswitchTxGoodFrames_Type())
atswitchTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchTxGoodFrames.setStatus(_A)
_AtswitchTxBroadcastFrames_Type=Counter32
_AtswitchTxBroadcastFrames_Object=MibTableColumn
atswitchTxBroadcastFrames=_AtswitchTxBroadcastFrames_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,5),_AtswitchTxBroadcastFrames_Type())
atswitchTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchTxBroadcastFrames.setStatus(_A)
_AtswitchTxMulticastFrames_Type=Counter32
_AtswitchTxMulticastFrames_Object=MibTableColumn
atswitchTxMulticastFrames=_AtswitchTxMulticastFrames_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,6),_AtswitchTxMulticastFrames_Type())
atswitchTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchTxMulticastFrames.setStatus(_A)
_AtswitchAddrDuplicate_Type=Counter32
_AtswitchAddrDuplicate_Object=MibTableColumn
atswitchAddrDuplicate=_AtswitchAddrDuplicate_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,7),_AtswitchAddrDuplicate_Type())
atswitchAddrDuplicate.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchAddrDuplicate.setStatus(_A)
_AtswitchAddrMismatches_Type=Counter32
_AtswitchAddrMismatches_Object=MibTableColumn
atswitchAddrMismatches=_AtswitchAddrMismatches_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,8),_AtswitchAddrMismatches_Type())
atswitchAddrMismatches.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchAddrMismatches.setStatus(_A)
_AtswitchRxOverruns_Type=Counter32
_AtswitchRxOverruns_Object=MibTableColumn
atswitchRxOverruns=_AtswitchRxOverruns_Object((1,3,6,1,4,1,207,8,10,6,1,1,1,9),_AtswitchRxOverruns_Type())
atswitchRxOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchRxOverruns.setStatus(_A)
_AtswitchEthPortError_ObjectIdentity=ObjectIdentity
atswitchEthPortError=_AtswitchEthPortError_ObjectIdentity((1,3,6,1,4,1,207,8,10,6,2))
_AtswitchEthPortErrorTable_Object=MibTable
atswitchEthPortErrorTable=_AtswitchEthPortErrorTable_Object((1,3,6,1,4,1,207,8,10,6,2,1))
if mibBuilder.loadTexts:atswitchEthPortErrorTable.setStatus(_A)
_AtswitchEthPortErrorEntry_Object=MibTableRow
atswitchEthPortErrorEntry=_AtswitchEthPortErrorEntry_Object((1,3,6,1,4,1,207,8,10,6,2,1,1))
atswitchEthPortErrorEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:atswitchEthPortErrorEntry.setStatus(_A)
_AtswitchEthPortErrorId_Type=Integer32
_AtswitchEthPortErrorId_Object=MibTableColumn
atswitchEthPortErrorId=_AtswitchEthPortErrorId_Object((1,3,6,1,4,1,207,8,10,6,2,1,1,1),_AtswitchEthPortErrorId_Type())
atswitchEthPortErrorId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthPortErrorId.setStatus(_A)
_AtswitchEthPortErrorRxBadFrames_Type=Counter32
_AtswitchEthPortErrorRxBadFrames_Object=MibTableColumn
atswitchEthPortErrorRxBadFrames=_AtswitchEthPortErrorRxBadFrames_Object((1,3,6,1,4,1,207,8,10,6,2,1,1,2),_AtswitchEthPortErrorRxBadFrames_Type())
atswitchEthPortErrorRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthPortErrorRxBadFrames.setStatus(_A)
_AtswitchEthPortErrorTxTotal_Type=Counter32
_AtswitchEthPortErrorTxTotal_Object=MibTableColumn
atswitchEthPortErrorTxTotal=_AtswitchEthPortErrorTxTotal_Object((1,3,6,1,4,1,207,8,10,6,2,1,1,3),_AtswitchEthPortErrorTxTotal_Type())
atswitchEthPortErrorTxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchEthPortErrorTxTotal.setStatus(_A)
_AtswitchFwdVlanGroup_ObjectIdentity=ObjectIdentity
atswitchFwdVlanGroup=_AtswitchFwdVlanGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,7))
_AtswitchFwdVlanTable_Object=MibTable
atswitchFwdVlanTable=_AtswitchFwdVlanTable_Object((1,3,6,1,4,1,207,8,10,7,1))
if mibBuilder.loadTexts:atswitchFwdVlanTable.setStatus(_A)
_AtswitchFwdVlanEntry_Object=MibTableRow
atswitchFwdVlanEntry=_AtswitchFwdVlanEntry_Object((1,3,6,1,4,1,207,8,10,7,1,1))
atswitchFwdVlanEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:atswitchFwdVlanEntry.setStatus(_A)
_AtswitchFwdVlanMACAddr_Type=MacAddress
_AtswitchFwdVlanMACAddr_Object=MibTableColumn
atswitchFwdVlanMACAddr=_AtswitchFwdVlanMACAddr_Object((1,3,6,1,4,1,207,8,10,7,1,1,1),_AtswitchFwdVlanMACAddr_Type())
atswitchFwdVlanMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchFwdVlanMACAddr.setStatus(_A)
_AtswitchFwdVlanVlanId_Type=Integer32
_AtswitchFwdVlanVlanId_Object=MibTableColumn
atswitchFwdVlanVlanId=_AtswitchFwdVlanVlanId_Object((1,3,6,1,4,1,207,8,10,7,1,1,2),_AtswitchFwdVlanVlanId_Type())
atswitchFwdVlanVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchFwdVlanVlanId.setStatus(_A)
_AtswitchFwdVlanAge_Type=Integer32
_AtswitchFwdVlanAge_Object=MibTableColumn
atswitchFwdVlanAge=_AtswitchFwdVlanAge_Object((1,3,6,1,4,1,207,8,10,7,1,1,3),_AtswitchFwdVlanAge_Type())
atswitchFwdVlanAge.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchFwdVlanAge.setStatus(_A)
class _AtswitchFwdVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),(_c,2),(_M,3)))
_AtswitchFwdVlanStatus_Type.__name__=_D
_AtswitchFwdVlanStatus_Object=MibTableColumn
atswitchFwdVlanStatus=_AtswitchFwdVlanStatus_Object((1,3,6,1,4,1,207,8,10,7,1,1,4),_AtswitchFwdVlanStatus_Type())
atswitchFwdVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchFwdVlanStatus.setStatus(_A)
_AtswitchFwdVlanPort_Type=Integer32
_AtswitchFwdVlanPort_Object=MibTableColumn
atswitchFwdVlanPort=_AtswitchFwdVlanPort_Object((1,3,6,1,4,1,207,8,10,7,1,1,5),_AtswitchFwdVlanPort_Type())
atswitchFwdVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchFwdVlanPort.setStatus(_A)
_AtswitchTrapAttrGroup_ObjectIdentity=ObjectIdentity
atswitchTrapAttrGroup=_AtswitchTrapAttrGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,8))
class _AtswitchDuplicateMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AtswitchDuplicateMacAddress_Type.__name__=_K
_AtswitchDuplicateMacAddress_Object=MibScalar
atswitchDuplicateMacAddress=_AtswitchDuplicateMacAddress_Object((1,3,6,1,4,1,207,8,10,8,1),_AtswitchDuplicateMacAddress_Type())
atswitchDuplicateMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:atswitchDuplicateMacAddress.setStatus(_A)
class _AtswitchIntruderMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AtswitchIntruderMacAddress_Type.__name__=_K
_AtswitchIntruderMacAddress_Object=MibScalar
atswitchIntruderMacAddress=_AtswitchIntruderMacAddress_Object((1,3,6,1,4,1,207,8,10,8,2),_AtswitchIntruderMacAddress_Type())
atswitchIntruderMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:atswitchIntruderMacAddress.setStatus(_A)
_AtswitchSecuredPortNumber_Type=Integer32
_AtswitchSecuredPortNumber_Object=MibScalar
atswitchSecuredPortNumber=_AtswitchSecuredPortNumber_Object((1,3,6,1,4,1,207,8,10,8,3),_AtswitchSecuredPortNumber_Type())
atswitchSecuredPortNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:atswitchSecuredPortNumber.setStatus(_A)
_AtswitchBridgeMib_ObjectIdentity=ObjectIdentity
atswitchBridgeMib=_AtswitchBridgeMib_ObjectIdentity((1,3,6,1,4,1,207,8,10,9))
_AtswitchBrBase_ObjectIdentity=ObjectIdentity
atswitchBrBase=_AtswitchBrBase_ObjectIdentity((1,3,6,1,4,1,207,8,10,9,1))
_AtswitchBrBaseTable_Object=MibTable
atswitchBrBaseTable=_AtswitchBrBaseTable_Object((1,3,6,1,4,1,207,8,10,9,1,1))
if mibBuilder.loadTexts:atswitchBrBaseTable.setStatus(_A)
_AtswitchBrBaseEntry_Object=MibTableRow
atswitchBrBaseEntry=_AtswitchBrBaseEntry_Object((1,3,6,1,4,1,207,8,10,9,1,1,1))
atswitchBrBaseEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:atswitchBrBaseEntry.setStatus(_A)
_AtswitchBrBaseLanId_Type=Integer32
_AtswitchBrBaseLanId_Object=MibTableColumn
atswitchBrBaseLanId=_AtswitchBrBaseLanId_Object((1,3,6,1,4,1,207,8,10,9,1,1,1,1),_AtswitchBrBaseLanId_Type())
atswitchBrBaseLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBaseLanId.setStatus(_A)
_AtswitchBrBaseBridgeAddress_Type=MacAddress
_AtswitchBrBaseBridgeAddress_Object=MibTableColumn
atswitchBrBaseBridgeAddress=_AtswitchBrBaseBridgeAddress_Object((1,3,6,1,4,1,207,8,10,9,1,1,1,2),_AtswitchBrBaseBridgeAddress_Type())
atswitchBrBaseBridgeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBaseBridgeAddress.setStatus(_A)
_AtswitchBrBaseNumPorts_Type=Integer32
_AtswitchBrBaseNumPorts_Object=MibTableColumn
atswitchBrBaseNumPorts=_AtswitchBrBaseNumPorts_Object((1,3,6,1,4,1,207,8,10,9,1,1,1,3),_AtswitchBrBaseNumPorts_Type())
atswitchBrBaseNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBaseNumPorts.setStatus(_A)
class _AtswitchBrBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),('transparent-only',2),('sourceroute-only',3),('srt',4)))
_AtswitchBrBaseType_Type.__name__=_D
_AtswitchBrBaseType_Object=MibTableColumn
atswitchBrBaseType=_AtswitchBrBaseType_Object((1,3,6,1,4,1,207,8,10,9,1,1,1,4),_AtswitchBrBaseType_Type())
atswitchBrBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBaseType.setStatus(_A)
_AtswitchBrBasePortTable_Object=MibTable
atswitchBrBasePortTable=_AtswitchBrBasePortTable_Object((1,3,6,1,4,1,207,8,10,9,1,4))
if mibBuilder.loadTexts:atswitchBrBasePortTable.setStatus(_A)
_AtswitchBrBasePortEntry_Object=MibTableRow
atswitchBrBasePortEntry=_AtswitchBrBasePortEntry_Object((1,3,6,1,4,1,207,8,10,9,1,4,1))
atswitchBrBasePortEntry.setIndexNames((0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:atswitchBrBasePortEntry.setStatus(_A)
_AtswitchBrBasePortLanId_Type=Integer32
_AtswitchBrBasePortLanId_Object=MibTableColumn
atswitchBrBasePortLanId=_AtswitchBrBasePortLanId_Object((1,3,6,1,4,1,207,8,10,9,1,4,1,1),_AtswitchBrBasePortLanId_Type())
atswitchBrBasePortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBasePortLanId.setStatus(_A)
class _AtswitchBrBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtswitchBrBasePort_Type.__name__=_D
_AtswitchBrBasePort_Object=MibTableColumn
atswitchBrBasePort=_AtswitchBrBasePort_Object((1,3,6,1,4,1,207,8,10,9,1,4,1,2),_AtswitchBrBasePort_Type())
atswitchBrBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBasePort.setStatus(_A)
_AtswitchBrBasePortIfIndex_Type=Integer32
_AtswitchBrBasePortIfIndex_Object=MibTableColumn
atswitchBrBasePortIfIndex=_AtswitchBrBasePortIfIndex_Object((1,3,6,1,4,1,207,8,10,9,1,4,1,3),_AtswitchBrBasePortIfIndex_Type())
atswitchBrBasePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBasePortIfIndex.setStatus(_A)
_AtswitchBrBasePortCircuit_Type=ObjectIdentifier
_AtswitchBrBasePortCircuit_Object=MibTableColumn
atswitchBrBasePortCircuit=_AtswitchBrBasePortCircuit_Object((1,3,6,1,4,1,207,8,10,9,1,4,1,4),_AtswitchBrBasePortCircuit_Type())
atswitchBrBasePortCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBasePortCircuit.setStatus(_A)
_AtswitchBrBasePortDelayExceededDiscards_Type=Counter32
_AtswitchBrBasePortDelayExceededDiscards_Object=MibTableColumn
atswitchBrBasePortDelayExceededDiscards=_AtswitchBrBasePortDelayExceededDiscards_Object((1,3,6,1,4,1,207,8,10,9,1,4,1,5),_AtswitchBrBasePortDelayExceededDiscards_Type())
atswitchBrBasePortDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBasePortDelayExceededDiscards.setStatus(_A)
_AtswitchBrBasePortMtuExceededDiscards_Type=Counter32
_AtswitchBrBasePortMtuExceededDiscards_Object=MibTableColumn
atswitchBrBasePortMtuExceededDiscards=_AtswitchBrBasePortMtuExceededDiscards_Object((1,3,6,1,4,1,207,8,10,9,1,4,1,6),_AtswitchBrBasePortMtuExceededDiscards_Type())
atswitchBrBasePortMtuExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrBasePortMtuExceededDiscards.setStatus(_A)
_AtswitchBrStp_ObjectIdentity=ObjectIdentity
atswitchBrStp=_AtswitchBrStp_ObjectIdentity((1,3,6,1,4,1,207,8,10,9,2))
_AtswitchBrStpTable_Object=MibTable
atswitchBrStpTable=_AtswitchBrStpTable_Object((1,3,6,1,4,1,207,8,10,9,2,1))
if mibBuilder.loadTexts:atswitchBrStpTable.setStatus(_A)
_AtswitchBrStpEntry_Object=MibTableRow
atswitchBrStpEntry=_AtswitchBrStpEntry_Object((1,3,6,1,4,1,207,8,10,9,2,1,1))
atswitchBrStpEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:atswitchBrStpEntry.setStatus(_A)
_AtswitchBrStpLanId_Type=Integer32
_AtswitchBrStpLanId_Object=MibTableColumn
atswitchBrStpLanId=_AtswitchBrStpLanId_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,1),_AtswitchBrStpLanId_Type())
atswitchBrStpLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpLanId.setStatus(_A)
class _AtswitchBrStpProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),('decLb100',2),('ieee8021d',3)))
_AtswitchBrStpProtocolSpecification_Type.__name__=_D
_AtswitchBrStpProtocolSpecification_Object=MibTableColumn
atswitchBrStpProtocolSpecification=_AtswitchBrStpProtocolSpecification_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,2),_AtswitchBrStpProtocolSpecification_Type())
atswitchBrStpProtocolSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpProtocolSpecification.setStatus(_A)
class _AtswitchBrStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtswitchBrStpPriority_Type.__name__=_D
_AtswitchBrStpPriority_Object=MibTableColumn
atswitchBrStpPriority=_AtswitchBrStpPriority_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,3),_AtswitchBrStpPriority_Type())
atswitchBrStpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrStpPriority.setStatus(_A)
_AtswitchBrStpTimeSinceTopologyChange_Type=TimeTicks
_AtswitchBrStpTimeSinceTopologyChange_Object=MibTableColumn
atswitchBrStpTimeSinceTopologyChange=_AtswitchBrStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,4),_AtswitchBrStpTimeSinceTopologyChange_Type())
atswitchBrStpTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpTimeSinceTopologyChange.setStatus(_A)
_AtswitchBrStpTopChanges_Type=Counter32
_AtswitchBrStpTopChanges_Object=MibTableColumn
atswitchBrStpTopChanges=_AtswitchBrStpTopChanges_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,5),_AtswitchBrStpTopChanges_Type())
atswitchBrStpTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpTopChanges.setStatus(_A)
_AtswitchBrStpDesignatedRoot_Type=BridgeId
_AtswitchBrStpDesignatedRoot_Object=MibTableColumn
atswitchBrStpDesignatedRoot=_AtswitchBrStpDesignatedRoot_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,6),_AtswitchBrStpDesignatedRoot_Type())
atswitchBrStpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpDesignatedRoot.setStatus(_A)
_AtswitchBrStpRootCost_Type=Integer32
_AtswitchBrStpRootCost_Object=MibTableColumn
atswitchBrStpRootCost=_AtswitchBrStpRootCost_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,7),_AtswitchBrStpRootCost_Type())
atswitchBrStpRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpRootCost.setStatus(_A)
_AtswitchBrStpRootPort_Type=Integer32
_AtswitchBrStpRootPort_Object=MibTableColumn
atswitchBrStpRootPort=_AtswitchBrStpRootPort_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,8),_AtswitchBrStpRootPort_Type())
atswitchBrStpRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpRootPort.setStatus(_A)
_AtswitchBrStpMaxAge_Type=Timeout
_AtswitchBrStpMaxAge_Object=MibTableColumn
atswitchBrStpMaxAge=_AtswitchBrStpMaxAge_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,9),_AtswitchBrStpMaxAge_Type())
atswitchBrStpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpMaxAge.setStatus(_A)
_AtswitchBrStpHelloTime_Type=Timeout
_AtswitchBrStpHelloTime_Object=MibTableColumn
atswitchBrStpHelloTime=_AtswitchBrStpHelloTime_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,10),_AtswitchBrStpHelloTime_Type())
atswitchBrStpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpHelloTime.setStatus(_A)
_AtswitchBrStpHoldTime_Type=Integer32
_AtswitchBrStpHoldTime_Object=MibTableColumn
atswitchBrStpHoldTime=_AtswitchBrStpHoldTime_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,11),_AtswitchBrStpHoldTime_Type())
atswitchBrStpHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpHoldTime.setStatus(_A)
_AtswitchBrStpForwardDelay_Type=Timeout
_AtswitchBrStpForwardDelay_Object=MibTableColumn
atswitchBrStpForwardDelay=_AtswitchBrStpForwardDelay_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,12),_AtswitchBrStpForwardDelay_Type())
atswitchBrStpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpForwardDelay.setStatus(_A)
class _AtswitchBrStpBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_AtswitchBrStpBridgeMaxAge_Type.__name__=_L
_AtswitchBrStpBridgeMaxAge_Object=MibTableColumn
atswitchBrStpBridgeMaxAge=_AtswitchBrStpBridgeMaxAge_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,13),_AtswitchBrStpBridgeMaxAge_Type())
atswitchBrStpBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrStpBridgeMaxAge.setStatus(_A)
class _AtswitchBrStpBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_AtswitchBrStpBridgeHelloTime_Type.__name__=_L
_AtswitchBrStpBridgeHelloTime_Object=MibTableColumn
atswitchBrStpBridgeHelloTime=_AtswitchBrStpBridgeHelloTime_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,14),_AtswitchBrStpBridgeHelloTime_Type())
atswitchBrStpBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrStpBridgeHelloTime.setStatus(_A)
class _AtswitchBrStpBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_AtswitchBrStpBridgeForwardDelay_Type.__name__=_L
_AtswitchBrStpBridgeForwardDelay_Object=MibTableColumn
atswitchBrStpBridgeForwardDelay=_AtswitchBrStpBridgeForwardDelay_Object((1,3,6,1,4,1,207,8,10,9,2,1,1,15),_AtswitchBrStpBridgeForwardDelay_Type())
atswitchBrStpBridgeForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrStpBridgeForwardDelay.setStatus(_A)
_AtswitchBrStpPortTable_Object=MibTable
atswitchBrStpPortTable=_AtswitchBrStpPortTable_Object((1,3,6,1,4,1,207,8,10,9,2,15))
if mibBuilder.loadTexts:atswitchBrStpPortTable.setStatus(_A)
_AtswitchBrStpPortEntry_Object=MibTableRow
atswitchBrStpPortEntry=_AtswitchBrStpPortEntry_Object((1,3,6,1,4,1,207,8,10,9,2,15,1))
atswitchBrStpPortEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:atswitchBrStpPortEntry.setStatus(_A)
_AtswitchBrStpPortLanId_Type=Integer32
_AtswitchBrStpPortLanId_Object=MibTableColumn
atswitchBrStpPortLanId=_AtswitchBrStpPortLanId_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,1),_AtswitchBrStpPortLanId_Type())
atswitchBrStpPortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPortLanId.setStatus(_A)
class _AtswitchBrStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtswitchBrStpPort_Type.__name__=_D
_AtswitchBrStpPort_Object=MibTableColumn
atswitchBrStpPort=_AtswitchBrStpPort_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,2),_AtswitchBrStpPort_Type())
atswitchBrStpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPort.setStatus(_A)
class _AtswitchBrStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtswitchBrStpPortPriority_Type.__name__=_D
_AtswitchBrStpPortPriority_Object=MibTableColumn
atswitchBrStpPortPriority=_AtswitchBrStpPortPriority_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,3),_AtswitchBrStpPortPriority_Type())
atswitchBrStpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrStpPortPriority.setStatus(_A)
class _AtswitchBrStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_T,2),(_U,3),(_V,4),('forwarding',5),('broken',6)))
_AtswitchBrStpPortState_Type.__name__=_D
_AtswitchBrStpPortState_Object=MibTableColumn
atswitchBrStpPortState=_AtswitchBrStpPortState_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,4),_AtswitchBrStpPortState_Type())
atswitchBrStpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPortState.setStatus(_A)
class _AtswitchBrStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_J,2)))
_AtswitchBrStpPortEnable_Type.__name__=_D
_AtswitchBrStpPortEnable_Object=MibTableColumn
atswitchBrStpPortEnable=_AtswitchBrStpPortEnable_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,5),_AtswitchBrStpPortEnable_Type())
atswitchBrStpPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrStpPortEnable.setStatus(_A)
class _AtswitchBrStpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtswitchBrStpPortPathCost_Type.__name__=_D
_AtswitchBrStpPortPathCost_Object=MibTableColumn
atswitchBrStpPortPathCost=_AtswitchBrStpPortPathCost_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,6),_AtswitchBrStpPortPathCost_Type())
atswitchBrStpPortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrStpPortPathCost.setStatus(_A)
_AtswitchBrStpPortDesignatedRoot_Type=BridgeId
_AtswitchBrStpPortDesignatedRoot_Object=MibTableColumn
atswitchBrStpPortDesignatedRoot=_AtswitchBrStpPortDesignatedRoot_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,7),_AtswitchBrStpPortDesignatedRoot_Type())
atswitchBrStpPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPortDesignatedRoot.setStatus(_A)
_AtswitchBrStpPortDesignatedCost_Type=Integer32
_AtswitchBrStpPortDesignatedCost_Object=MibTableColumn
atswitchBrStpPortDesignatedCost=_AtswitchBrStpPortDesignatedCost_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,8),_AtswitchBrStpPortDesignatedCost_Type())
atswitchBrStpPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPortDesignatedCost.setStatus(_A)
_AtswitchBrStpPortDesignatedBridge_Type=BridgeId
_AtswitchBrStpPortDesignatedBridge_Object=MibTableColumn
atswitchBrStpPortDesignatedBridge=_AtswitchBrStpPortDesignatedBridge_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,9),_AtswitchBrStpPortDesignatedBridge_Type())
atswitchBrStpPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPortDesignatedBridge.setStatus(_A)
class _AtswitchBrStpPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AtswitchBrStpPortDesignatedPort_Type.__name__=_K
_AtswitchBrStpPortDesignatedPort_Object=MibTableColumn
atswitchBrStpPortDesignatedPort=_AtswitchBrStpPortDesignatedPort_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,10),_AtswitchBrStpPortDesignatedPort_Type())
atswitchBrStpPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPortDesignatedPort.setStatus(_A)
_AtswitchBrStpPortForwardTransitions_Type=Counter32
_AtswitchBrStpPortForwardTransitions_Object=MibTableColumn
atswitchBrStpPortForwardTransitions=_AtswitchBrStpPortForwardTransitions_Object((1,3,6,1,4,1,207,8,10,9,2,15,1,11),_AtswitchBrStpPortForwardTransitions_Type())
atswitchBrStpPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrStpPortForwardTransitions.setStatus(_A)
_AtswitchBrTp_ObjectIdentity=ObjectIdentity
atswitchBrTp=_AtswitchBrTp_ObjectIdentity((1,3,6,1,4,1,207,8,10,9,3))
_AtswitchBrTpTable_Object=MibTable
atswitchBrTpTable=_AtswitchBrTpTable_Object((1,3,6,1,4,1,207,8,10,9,3,1))
if mibBuilder.loadTexts:atswitchBrTpTable.setStatus(_A)
_AtswitchBrTpEntry_Object=MibTableRow
atswitchBrTpEntry=_AtswitchBrTpEntry_Object((1,3,6,1,4,1,207,8,10,9,3,1,1))
atswitchBrTpEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:atswitchBrTpEntry.setStatus(_A)
_AtswitchBrTpLanId_Type=Integer32
_AtswitchBrTpLanId_Object=MibTableColumn
atswitchBrTpLanId=_AtswitchBrTpLanId_Object((1,3,6,1,4,1,207,8,10,9,3,1,1,1),_AtswitchBrTpLanId_Type())
atswitchBrTpLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpLanId.setStatus(_A)
_AtswitchBrTpLearnedEntryDiscards_Type=Counter32
_AtswitchBrTpLearnedEntryDiscards_Object=MibTableColumn
atswitchBrTpLearnedEntryDiscards=_AtswitchBrTpLearnedEntryDiscards_Object((1,3,6,1,4,1,207,8,10,9,3,1,1,2),_AtswitchBrTpLearnedEntryDiscards_Type())
atswitchBrTpLearnedEntryDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpLearnedEntryDiscards.setStatus(_A)
class _AtswitchBrTpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_AtswitchBrTpAgingTime_Type.__name__=_D
_AtswitchBrTpAgingTime_Object=MibTableColumn
atswitchBrTpAgingTime=_AtswitchBrTpAgingTime_Object((1,3,6,1,4,1,207,8,10,9,3,1,1,3),_AtswitchBrTpAgingTime_Type())
atswitchBrTpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchBrTpAgingTime.setStatus(_A)
_AtswitchBrTpFdbTable_Object=MibTable
atswitchBrTpFdbTable=_AtswitchBrTpFdbTable_Object((1,3,6,1,4,1,207,8,10,9,3,3))
if mibBuilder.loadTexts:atswitchBrTpFdbTable.setStatus(_A)
_AtswitchBrTpFdbEntry_Object=MibTableRow
atswitchBrTpFdbEntry=_AtswitchBrTpFdbEntry_Object((1,3,6,1,4,1,207,8,10,9,3,3,1))
atswitchBrTpFdbEntry.setIndexNames((0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:atswitchBrTpFdbEntry.setStatus(_A)
_AtswitchBrTpFdbLanId_Type=Integer32
_AtswitchBrTpFdbLanId_Object=MibTableColumn
atswitchBrTpFdbLanId=_AtswitchBrTpFdbLanId_Object((1,3,6,1,4,1,207,8,10,9,3,3,1,1),_AtswitchBrTpFdbLanId_Type())
atswitchBrTpFdbLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpFdbLanId.setStatus(_A)
_AtswitchBrTpFdbAddress_Type=MacAddress
_AtswitchBrTpFdbAddress_Object=MibTableColumn
atswitchBrTpFdbAddress=_AtswitchBrTpFdbAddress_Object((1,3,6,1,4,1,207,8,10,9,3,3,1,2),_AtswitchBrTpFdbAddress_Type())
atswitchBrTpFdbAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpFdbAddress.setStatus(_A)
_AtswitchBrTpFdbPort_Type=Integer32
_AtswitchBrTpFdbPort_Object=MibTableColumn
atswitchBrTpFdbPort=_AtswitchBrTpFdbPort_Object((1,3,6,1,4,1,207,8,10,9,3,3,1,3),_AtswitchBrTpFdbPort_Type())
atswitchBrTpFdbPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpFdbPort.setStatus(_A)
class _AtswitchBrTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),(_c,2),(_M,3)))
_AtswitchBrTpFdbStatus_Type.__name__=_D
_AtswitchBrTpFdbStatus_Object=MibTableColumn
atswitchBrTpFdbStatus=_AtswitchBrTpFdbStatus_Object((1,3,6,1,4,1,207,8,10,9,3,3,1,4),_AtswitchBrTpFdbStatus_Type())
atswitchBrTpFdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpFdbStatus.setStatus(_A)
_AtswitchBrTpPortTable_Object=MibTable
atswitchBrTpPortTable=_AtswitchBrTpPortTable_Object((1,3,6,1,4,1,207,8,10,9,3,4))
if mibBuilder.loadTexts:atswitchBrTpPortTable.setStatus(_A)
_AtswitchBrTpPortEntry_Object=MibTableRow
atswitchBrTpPortEntry=_AtswitchBrTpPortEntry_Object((1,3,6,1,4,1,207,8,10,9,3,4,1))
atswitchBrTpPortEntry.setIndexNames((0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:atswitchBrTpPortEntry.setStatus(_A)
_AtswitchBrTpPortLanId_Type=Integer32
_AtswitchBrTpPortLanId_Object=MibTableColumn
atswitchBrTpPortLanId=_AtswitchBrTpPortLanId_Object((1,3,6,1,4,1,207,8,10,9,3,4,1,1),_AtswitchBrTpPortLanId_Type())
atswitchBrTpPortLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpPortLanId.setStatus(_A)
class _AtswitchBrTpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtswitchBrTpPort_Type.__name__=_D
_AtswitchBrTpPort_Object=MibTableColumn
atswitchBrTpPort=_AtswitchBrTpPort_Object((1,3,6,1,4,1,207,8,10,9,3,4,1,2),_AtswitchBrTpPort_Type())
atswitchBrTpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpPort.setStatus(_A)
_AtswitchBrTpPortMaxInfo_Type=Integer32
_AtswitchBrTpPortMaxInfo_Object=MibTableColumn
atswitchBrTpPortMaxInfo=_AtswitchBrTpPortMaxInfo_Object((1,3,6,1,4,1,207,8,10,9,3,4,1,3),_AtswitchBrTpPortMaxInfo_Type())
atswitchBrTpPortMaxInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpPortMaxInfo.setStatus(_A)
_AtswitchBrTpPortInFrames_Type=Counter32
_AtswitchBrTpPortInFrames_Object=MibTableColumn
atswitchBrTpPortInFrames=_AtswitchBrTpPortInFrames_Object((1,3,6,1,4,1,207,8,10,9,3,4,1,4),_AtswitchBrTpPortInFrames_Type())
atswitchBrTpPortInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpPortInFrames.setStatus(_A)
_AtswitchBrTpPortOutFrames_Type=Counter32
_AtswitchBrTpPortOutFrames_Object=MibTableColumn
atswitchBrTpPortOutFrames=_AtswitchBrTpPortOutFrames_Object((1,3,6,1,4,1,207,8,10,9,3,4,1,5),_AtswitchBrTpPortOutFrames_Type())
atswitchBrTpPortOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpPortOutFrames.setStatus(_A)
_AtswitchBrTpPortInDiscards_Type=Counter32
_AtswitchBrTpPortInDiscards_Object=MibTableColumn
atswitchBrTpPortInDiscards=_AtswitchBrTpPortInDiscards_Object((1,3,6,1,4,1,207,8,10,9,3,4,1,6),_AtswitchBrTpPortInDiscards_Type())
atswitchBrTpPortInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchBrTpPortInDiscards.setStatus(_A)
_AtswitchStaticMACGroup_ObjectIdentity=ObjectIdentity
atswitchStaticMACGroup=_AtswitchStaticMACGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,10))
_AtswitchStaticMACTable_Object=MibTable
atswitchStaticMACTable=_AtswitchStaticMACTable_Object((1,3,6,1,4,1,207,8,10,10,1))
if mibBuilder.loadTexts:atswitchStaticMACTable.setStatus(_A)
_AtswitchStaticMACEntry_Object=MibTableRow
atswitchStaticMACEntry=_AtswitchStaticMACEntry_Object((1,3,6,1,4,1,207,8,10,10,1,1))
atswitchStaticMACEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:atswitchStaticMACEntry.setStatus(_A)
_AtswitchStaticMACAddress_Type=MacAddress
_AtswitchStaticMACAddress_Object=MibTableColumn
atswitchStaticMACAddress=_AtswitchStaticMACAddress_Object((1,3,6,1,4,1,207,8,10,10,1,1,1),_AtswitchStaticMACAddress_Type())
atswitchStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchStaticMACAddress.setStatus(_A)
_AtswitchStaticMACPortNumbers_Type=DisplayString
_AtswitchStaticMACPortNumbers_Object=MibTableColumn
atswitchStaticMACPortNumbers=_AtswitchStaticMACPortNumbers_Object((1,3,6,1,4,1,207,8,10,10,1,1,2),_AtswitchStaticMACPortNumbers_Type())
atswitchStaticMACPortNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchStaticMACPortNumbers.setStatus(_A)
_AtswitchStaticMACVlan_Type=Integer32
_AtswitchStaticMACVlan_Object=MibTableColumn
atswitchStaticMACVlan=_AtswitchStaticMACVlan_Object((1,3,6,1,4,1,207,8,10,10,1,1,3),_AtswitchStaticMACVlan_Type())
atswitchStaticMACVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:atswitchStaticMACVlan.setStatus(_A)
_AtswitchPortMacAddrGroup_ObjectIdentity=ObjectIdentity
atswitchPortMacAddrGroup=_AtswitchPortMacAddrGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,12))
_AtswitchPortMACTable_Object=MibTable
atswitchPortMACTable=_AtswitchPortMACTable_Object((1,3,6,1,4,1,207,8,10,12,1))
if mibBuilder.loadTexts:atswitchPortMACTable.setStatus(_A)
_AtswitchPortMACEntry_Object=MibTableRow
atswitchPortMACEntry=_AtswitchPortMACEntry_Object((1,3,6,1,4,1,207,8,10,12,1,1))
atswitchPortMACEntry.setIndexNames((0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:atswitchPortMACEntry.setStatus(_A)
_AtswitchPortMACAddress_Type=MacAddress
_AtswitchPortMACAddress_Object=MibTableColumn
atswitchPortMACAddress=_AtswitchPortMACAddress_Object((1,3,6,1,4,1,207,8,10,12,1,1,1),_AtswitchPortMACAddress_Type())
atswitchPortMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchPortMACAddress.setStatus(_A)
_AtswitchPortMACPort_Type=Integer32
_AtswitchPortMACPort_Object=MibTableColumn
atswitchPortMACPort=_AtswitchPortMACPort_Object((1,3,6,1,4,1,207,8,10,12,1,1,2),_AtswitchPortMACPort_Type())
atswitchPortMACPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchPortMACPort.setStatus(_A)
_AtswitchDebugMallocLogGroup_ObjectIdentity=ObjectIdentity
atswitchDebugMallocLogGroup=_AtswitchDebugMallocLogGroup_ObjectIdentity((1,3,6,1,4,1,207,8,10,13))
_AtswitchDebugMallocLogTable_Object=MibTable
atswitchDebugMallocLogTable=_AtswitchDebugMallocLogTable_Object((1,3,6,1,4,1,207,8,10,13,1))
if mibBuilder.loadTexts:atswitchDebugMallocLogTable.setStatus(_G)
_AtswitchMallocLogEntry_Object=MibTableRow
atswitchMallocLogEntry=_AtswitchMallocLogEntry_Object((1,3,6,1,4,1,207,8,10,13,1,1))
atswitchMallocLogEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:atswitchMallocLogEntry.setStatus(_G)
_AtswitchDebugMallocLogIndex_Type=Integer32
_AtswitchDebugMallocLogIndex_Object=MibTableColumn
atswitchDebugMallocLogIndex=_AtswitchDebugMallocLogIndex_Object((1,3,6,1,4,1,207,8,10,13,1,1,1),_AtswitchDebugMallocLogIndex_Type())
atswitchDebugMallocLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchDebugMallocLogIndex.setStatus(_G)
_AtswitchDebugMallocLogCaller_Type=Integer32
_AtswitchDebugMallocLogCaller_Object=MibTableColumn
atswitchDebugMallocLogCaller=_AtswitchDebugMallocLogCaller_Object((1,3,6,1,4,1,207,8,10,13,1,1,2),_AtswitchDebugMallocLogCaller_Type())
atswitchDebugMallocLogCaller.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchDebugMallocLogCaller.setStatus(_G)
_AtswitchDebugMallocLogAddress_Type=Integer32
_AtswitchDebugMallocLogAddress_Object=MibTableColumn
atswitchDebugMallocLogAddress=_AtswitchDebugMallocLogAddress_Object((1,3,6,1,4,1,207,8,10,13,1,1,3),_AtswitchDebugMallocLogAddress_Type())
atswitchDebugMallocLogAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atswitchDebugMallocLogAddress.setStatus(_G)
newRoot=NotificationType((1,3,6,1,4,1,207,0,101))
if mibBuilder.loadTexts:newRoot.setStatus('')
topologyChange=NotificationType((1,3,6,1,4,1,207,0,102))
if mibBuilder.loadTexts:topologyChange.setStatus('')
intruderTrap=NotificationType((1,3,6,1,4,1,207,0,105))
if mibBuilder.loadTexts:intruderTrap.setStatus('')
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'BridgeId':BridgeId,_L:Timeout,'alliedTelesyn':alliedTelesyn,'newRoot':newRoot,'topologyChange':topologyChange,'intruderTrap':intruderTrap,'atiProduct':atiProduct,'mibObject':mibObject,'atswitchMib':atswitchMib,'atswitchSysGroup':atswitchSysGroup,'atswitchProductType':atswitchProductType,'atswitchEthernetPortCount':atswitchEthernetPortCount,'atswitchReset':atswitchReset,'atswitchMDA1Type':atswitchMDA1Type,'atswitchMDA2Type':atswitchMDA2Type,'atswitchDeviceFlowControl':atswitchDeviceFlowControl,'atswitchSwGroup':atswitchSwGroup,'atswitchSwProduct':atswitchSwProduct,'atswitchSwVersion':atswitchSwVersion,'atswitchIpGroup':atswitchIpGroup,'atswitchCurrentIpAddress':atswitchCurrentIpAddress,'atswitchConfiguredIpAddress':atswitchConfiguredIpAddress,'atswitchConfiguredSubnetMask':atswitchConfiguredSubnetMask,'atswitchConfiguredRouter':atswitchConfiguredRouter,'atswitchIPAddressStatus':atswitchIPAddressStatus,'atswitchDNServer':atswitchDNServer,'atswitchDefaultDomainName':atswitchDefaultDomainName,'atswitchNMGroup':atswitchNMGroup,'atswitchNwMgrTable':atswitchNwMgrTable,'atswitchNwMgrEntry':atswitchNwMgrEntry,_Q:atswitchNwMgrIndex,'atswitchNwMgrIpAddr':atswitchNwMgrIpAddr,'atswitchConfigGroup':atswitchConfigGroup,'atswitchPortDisableOnSecurityViolation':atswitchPortDisableOnSecurityViolation,'atswitchMirroringSourcePort':atswitchMirroringSourcePort,'atswitchMirrorState':atswitchMirrorState,'atswitchMirroringDestinationPort':atswitchMirroringDestinationPort,'atswitchSecurityConfig':atswitchSecurityConfig,'atswitchSecurityAction':atswitchSecurityAction,'atswitchDebugAvailableBytes':atswitchDebugAvailableBytes,'atswitchTrunkConfig':atswitchTrunkConfig,'atswitchPortConfigGroup':atswitchPortConfigGroup,'atswitchPortTable':atswitchPortTable,'atswitchPortEntry':atswitchPortEntry,_R:atswitchPortNumber,'atswitchPortName':atswitchPortName,'atswitchPortAutosenseOrHalfDuplex':atswitchPortAutosenseOrHalfDuplex,'atswitchPortLinkState':atswitchPortLinkState,'atswitchPortDuplexStatus':atswitchPortDuplexStatus,'atswitchPortSpeed':atswitchPortSpeed,'atswitchPortState':atswitchPortState,'atswitchPortTransmitPacingConfig':atswitchPortTransmitPacingConfig,'atswitchPortSTPConfig':atswitchPortSTPConfig,'atswitchPortBridgeid':atswitchPortBridgeid,'atswitchPortSTPCost':atswitchPortSTPCost,'atswitchPortSTPPriority':atswitchPortSTPPriority,'atswitchPortSwitchingType':atswitchPortSwitchingType,'atswitchPortFlowControlEnable':atswitchPortFlowControlEnable,'atswitchPortSecurityNumberOfAddresses':atswitchPortSecurityNumberOfAddresses,'atswitchVlanConfigGroup':atswitchVlanConfigGroup,'atswitchBasicVlanTable':atswitchBasicVlanTable,'atswitchBasicVlanEntry':atswitchBasicVlanEntry,_W:atswitchBeVlanIndex,'atswitchBeVlanName':atswitchBeVlanName,'atswitchBeVlanTagId':atswitchBeVlanTagId,'atswitchBeVlanPortMask':atswitchBeVlanPortMask,'atswitchBeVlanRowStatus':atswitchBeVlanRowStatus,'atswitchPort2VlanTable':atswitchPort2VlanTable,'atswitchPort2VlanEntry':atswitchPort2VlanEntry,_X:atswitchPvPortNumber,'atswitchPvVlanName':atswitchPvVlanName,'atswitchEthernetStatsGroup':atswitchEthernetStatsGroup,'atswitchEthMonStats':atswitchEthMonStats,'atswitchEthMonRxGoodFrames':atswitchEthMonRxGoodFrames,'atswitchEthMonTxGoodFrames':atswitchEthMonTxGoodFrames,'atswitchEthMonTxTotalBytes':atswitchEthMonTxTotalBytes,'atswitchEthMonTxDeferred':atswitchEthMonTxDeferred,'atswitchEthMonTxCollisions':atswitchEthMonTxCollisions,'atswitchEthErrorStats':atswitchEthErrorStats,'atswitchEthErrorCRC':atswitchEthErrorCRC,'atswitchEthErrorAlignment':atswitchEthErrorAlignment,'atswitchEthErrorRxBadFrames':atswitchEthErrorRxBadFrames,'atswitchEthErrorLateCollisions':atswitchEthErrorLateCollisions,'atswitchEthErrorTxTotal':atswitchEthErrorTxTotal,'atswitchEthPortStatsGroup':atswitchEthPortStatsGroup,'atswitchEthPortMonStats':atswitchEthPortMonStats,'atswitchEthPortMonTable':atswitchEthPortMonTable,'atswitchEthPortMonEntry':atswitchEthPortMonEntry,_Y:atswitchEthPortMonId,'atswitchEthPortMonTxTotalBytes':atswitchEthPortMonTxTotalBytes,'atswitchRxGoodFrames':atswitchRxGoodFrames,'atswitchTxGoodFrames':atswitchTxGoodFrames,'atswitchTxBroadcastFrames':atswitchTxBroadcastFrames,'atswitchTxMulticastFrames':atswitchTxMulticastFrames,'atswitchAddrDuplicate':atswitchAddrDuplicate,'atswitchAddrMismatches':atswitchAddrMismatches,'atswitchRxOverruns':atswitchRxOverruns,'atswitchEthPortError':atswitchEthPortError,'atswitchEthPortErrorTable':atswitchEthPortErrorTable,'atswitchEthPortErrorEntry':atswitchEthPortErrorEntry,_Z:atswitchEthPortErrorId,'atswitchEthPortErrorRxBadFrames':atswitchEthPortErrorRxBadFrames,'atswitchEthPortErrorTxTotal':atswitchEthPortErrorTxTotal,'atswitchFwdVlanGroup':atswitchFwdVlanGroup,'atswitchFwdVlanTable':atswitchFwdVlanTable,'atswitchFwdVlanEntry':atswitchFwdVlanEntry,_a:atswitchFwdVlanMACAddr,'atswitchFwdVlanVlanId':atswitchFwdVlanVlanId,'atswitchFwdVlanAge':atswitchFwdVlanAge,'atswitchFwdVlanStatus':atswitchFwdVlanStatus,'atswitchFwdVlanPort':atswitchFwdVlanPort,'atswitchTrapAttrGroup':atswitchTrapAttrGroup,'atswitchDuplicateMacAddress':atswitchDuplicateMacAddress,'atswitchIntruderMacAddress':atswitchIntruderMacAddress,'atswitchSecuredPortNumber':atswitchSecuredPortNumber,'atswitchBridgeMib':atswitchBridgeMib,'atswitchBrBase':atswitchBrBase,'atswitchBrBaseTable':atswitchBrBaseTable,'atswitchBrBaseEntry':atswitchBrBaseEntry,_d:atswitchBrBaseLanId,'atswitchBrBaseBridgeAddress':atswitchBrBaseBridgeAddress,'atswitchBrBaseNumPorts':atswitchBrBaseNumPorts,'atswitchBrBaseType':atswitchBrBaseType,'atswitchBrBasePortTable':atswitchBrBasePortTable,'atswitchBrBasePortEntry':atswitchBrBasePortEntry,_f:atswitchBrBasePortLanId,_g:atswitchBrBasePort,'atswitchBrBasePortIfIndex':atswitchBrBasePortIfIndex,'atswitchBrBasePortCircuit':atswitchBrBasePortCircuit,'atswitchBrBasePortDelayExceededDiscards':atswitchBrBasePortDelayExceededDiscards,'atswitchBrBasePortMtuExceededDiscards':atswitchBrBasePortMtuExceededDiscards,'atswitchBrStp':atswitchBrStp,'atswitchBrStpTable':atswitchBrStpTable,'atswitchBrStpEntry':atswitchBrStpEntry,_h:atswitchBrStpLanId,'atswitchBrStpProtocolSpecification':atswitchBrStpProtocolSpecification,'atswitchBrStpPriority':atswitchBrStpPriority,'atswitchBrStpTimeSinceTopologyChange':atswitchBrStpTimeSinceTopologyChange,'atswitchBrStpTopChanges':atswitchBrStpTopChanges,'atswitchBrStpDesignatedRoot':atswitchBrStpDesignatedRoot,'atswitchBrStpRootCost':atswitchBrStpRootCost,'atswitchBrStpRootPort':atswitchBrStpRootPort,'atswitchBrStpMaxAge':atswitchBrStpMaxAge,'atswitchBrStpHelloTime':atswitchBrStpHelloTime,'atswitchBrStpHoldTime':atswitchBrStpHoldTime,'atswitchBrStpForwardDelay':atswitchBrStpForwardDelay,'atswitchBrStpBridgeMaxAge':atswitchBrStpBridgeMaxAge,'atswitchBrStpBridgeHelloTime':atswitchBrStpBridgeHelloTime,'atswitchBrStpBridgeForwardDelay':atswitchBrStpBridgeForwardDelay,'atswitchBrStpPortTable':atswitchBrStpPortTable,'atswitchBrStpPortEntry':atswitchBrStpPortEntry,_i:atswitchBrStpPortLanId,_j:atswitchBrStpPort,'atswitchBrStpPortPriority':atswitchBrStpPortPriority,'atswitchBrStpPortState':atswitchBrStpPortState,'atswitchBrStpPortEnable':atswitchBrStpPortEnable,'atswitchBrStpPortPathCost':atswitchBrStpPortPathCost,'atswitchBrStpPortDesignatedRoot':atswitchBrStpPortDesignatedRoot,'atswitchBrStpPortDesignatedCost':atswitchBrStpPortDesignatedCost,'atswitchBrStpPortDesignatedBridge':atswitchBrStpPortDesignatedBridge,'atswitchBrStpPortDesignatedPort':atswitchBrStpPortDesignatedPort,'atswitchBrStpPortForwardTransitions':atswitchBrStpPortForwardTransitions,'atswitchBrTp':atswitchBrTp,'atswitchBrTpTable':atswitchBrTpTable,'atswitchBrTpEntry':atswitchBrTpEntry,_k:atswitchBrTpLanId,'atswitchBrTpLearnedEntryDiscards':atswitchBrTpLearnedEntryDiscards,'atswitchBrTpAgingTime':atswitchBrTpAgingTime,'atswitchBrTpFdbTable':atswitchBrTpFdbTable,'atswitchBrTpFdbEntry':atswitchBrTpFdbEntry,_l:atswitchBrTpFdbLanId,_m:atswitchBrTpFdbAddress,'atswitchBrTpFdbPort':atswitchBrTpFdbPort,'atswitchBrTpFdbStatus':atswitchBrTpFdbStatus,'atswitchBrTpPortTable':atswitchBrTpPortTable,'atswitchBrTpPortEntry':atswitchBrTpPortEntry,_n:atswitchBrTpPortLanId,_o:atswitchBrTpPort,'atswitchBrTpPortMaxInfo':atswitchBrTpPortMaxInfo,'atswitchBrTpPortInFrames':atswitchBrTpPortInFrames,'atswitchBrTpPortOutFrames':atswitchBrTpPortOutFrames,'atswitchBrTpPortInDiscards':atswitchBrTpPortInDiscards,'atswitchStaticMACGroup':atswitchStaticMACGroup,'atswitchStaticMACTable':atswitchStaticMACTable,'atswitchStaticMACEntry':atswitchStaticMACEntry,_p:atswitchStaticMACAddress,'atswitchStaticMACPortNumbers':atswitchStaticMACPortNumbers,'atswitchStaticMACVlan':atswitchStaticMACVlan,'atswitchPortMacAddrGroup':atswitchPortMacAddrGroup,'atswitchPortMACTable':atswitchPortMACTable,'atswitchPortMACEntry':atswitchPortMACEntry,_q:atswitchPortMACAddress,_r:atswitchPortMACPort,'atswitchDebugMallocLogGroup':atswitchDebugMallocLogGroup,'atswitchDebugMallocLogTable':atswitchDebugMallocLogTable,'atswitchMallocLogEntry':atswitchMallocLogEntry,_s:atswitchDebugMallocLogIndex,'atswitchDebugMallocLogCaller':atswitchDebugMallocLogCaller,'atswitchDebugMallocLogAddress':atswitchDebugMallocLogAddress})