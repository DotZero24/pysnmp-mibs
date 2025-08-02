_S='ipeCmdDhcpMainLeaseIpAddr'
_R='ipeCmdDhcpMainIndex'
_Q='read-only'
_P='ipeStsDhcpMainLeaseIpAddr'
_O='ipeStsDhcpMainLeaseServerIndex'
_N='ipeCfgDhcpMainRegisteredMacNo'
_M='ipeCfgDhcpMainRegisteredMacId'
_L='ipeCfgDhcpMainServerIndex'
_K='OctetString'
_J='read-create'
_I='EnableDisableValue'
_H='invalid'
_G='00000000'
_F='IPE-DHCP-MAIN-MIB'
_E='IpAddress'
_D='not-accessible'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_E,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
class EnableDisableValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('disable',1),('enable',2)))
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_RadioEquipment_ObjectIdentity=ObjectIdentity
radioEquipment=_RadioEquipment_ObjectIdentity((1,3,6,1,4,1,119,2,3,69))
_System5_ObjectIdentity=ObjectIdentity
system5=_System5_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,5))
_IpeConfigurationGroup_ObjectIdentity=ObjectIdentity
ipeConfigurationGroup=_IpeConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,5,3))
_IpeCfgDhcpGroup_ObjectIdentity=ObjectIdentity
ipeCfgDhcpGroup=_IpeCfgDhcpGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,5,3,13))
_IpeCfgDhcpMainServerTable_Object=MibTable
ipeCfgDhcpMainServerTable=_IpeCfgDhcpMainServerTable_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2))
if mibBuilder.loadTexts:ipeCfgDhcpMainServerTable.setStatus(_A)
_IpeCfgDhcpMainServerEntry_Object=MibTableRow
ipeCfgDhcpMainServerEntry=_IpeCfgDhcpMainServerEntry_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1))
ipeCfgDhcpMainServerEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:ipeCfgDhcpMainServerEntry.setStatus(_A)
class _IpeCfgDhcpMainServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_IpeCfgDhcpMainServerIndex_Type.__name__=_C
_IpeCfgDhcpMainServerIndex_Object=MibTableColumn
ipeCfgDhcpMainServerIndex=_IpeCfgDhcpMainServerIndex_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,1),_IpeCfgDhcpMainServerIndex_Type())
ipeCfgDhcpMainServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerIndex.setStatus(_A)
_IpeCfgDhcpMainServerNEAddress_Type=IpAddress
_IpeCfgDhcpMainServerNEAddress_Object=MibTableColumn
ipeCfgDhcpMainServerNEAddress=_IpeCfgDhcpMainServerNEAddress_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,2),_IpeCfgDhcpMainServerNEAddress_Type())
ipeCfgDhcpMainServerNEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerNEAddress.setStatus(_A)
class _IpeCfgDhcpMainServerEnable_Type(EnableDisableValue):defaultValue=1
_IpeCfgDhcpMainServerEnable_Type.__name__=_I
_IpeCfgDhcpMainServerEnable_Object=MibTableColumn
ipeCfgDhcpMainServerEnable=_IpeCfgDhcpMainServerEnable_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,3),_IpeCfgDhcpMainServerEnable_Type())
ipeCfgDhcpMainServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerEnable.setStatus(_A)
class _IpeCfgDhcpMainServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('server',1),('relay',2)))
_IpeCfgDhcpMainServerMode_Type.__name__=_C
_IpeCfgDhcpMainServerMode_Object=MibTableColumn
ipeCfgDhcpMainServerMode=_IpeCfgDhcpMainServerMode_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,4),_IpeCfgDhcpMainServerMode_Type())
ipeCfgDhcpMainServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerMode.setStatus(_A)
_IpeCfgDhcpMainServerInterface_Type=InterfaceIndex
_IpeCfgDhcpMainServerInterface_Object=MibTableColumn
ipeCfgDhcpMainServerInterface=_IpeCfgDhcpMainServerInterface_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,5),_IpeCfgDhcpMainServerInterface_Type())
ipeCfgDhcpMainServerInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerInterface.setStatus(_A)
_IpeCfgDhcpMainServerIpAddr_Type=IpAddress
_IpeCfgDhcpMainServerIpAddr_Object=MibTableColumn
ipeCfgDhcpMainServerIpAddr=_IpeCfgDhcpMainServerIpAddr_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,6),_IpeCfgDhcpMainServerIpAddr_Type())
ipeCfgDhcpMainServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerIpAddr.setStatus(_A)
class _IpeCfgDhcpMainServerLeaseTime_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,259200))
_IpeCfgDhcpMainServerLeaseTime_Type.__name__=_C
_IpeCfgDhcpMainServerLeaseTime_Object=MibTableColumn
ipeCfgDhcpMainServerLeaseTime=_IpeCfgDhcpMainServerLeaseTime_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,7),_IpeCfgDhcpMainServerLeaseTime_Type())
ipeCfgDhcpMainServerLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerLeaseTime.setUnits('seconds')
class _IpeCfgDhcpMainServerLeaseAddrRangeBegin_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainServerLeaseAddrRangeBegin_Type.__name__=_E
_IpeCfgDhcpMainServerLeaseAddrRangeBegin_Object=MibTableColumn
ipeCfgDhcpMainServerLeaseAddrRangeBegin=_IpeCfgDhcpMainServerLeaseAddrRangeBegin_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,8),_IpeCfgDhcpMainServerLeaseAddrRangeBegin_Type())
ipeCfgDhcpMainServerLeaseAddrRangeBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerLeaseAddrRangeBegin.setStatus(_A)
class _IpeCfgDhcpMainServerLeaseAddrRangeEnd_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainServerLeaseAddrRangeEnd_Type.__name__=_E
_IpeCfgDhcpMainServerLeaseAddrRangeEnd_Object=MibTableColumn
ipeCfgDhcpMainServerLeaseAddrRangeEnd=_IpeCfgDhcpMainServerLeaseAddrRangeEnd_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,9),_IpeCfgDhcpMainServerLeaseAddrRangeEnd_Type())
ipeCfgDhcpMainServerLeaseAddrRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerLeaseAddrRangeEnd.setStatus(_A)
class _IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Type.__name__=_E
_IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Object=MibTableColumn
ipeCfgDhcpMainServerLeaseAddrExcludeBegin=_IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,10),_IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Type())
ipeCfgDhcpMainServerLeaseAddrExcludeBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerLeaseAddrExcludeBegin.setStatus(_A)
class _IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Type.__name__=_E
_IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Object=MibTableColumn
ipeCfgDhcpMainServerLeaseAddrExcludeEnd=_IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,11),_IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Type())
ipeCfgDhcpMainServerLeaseAddrExcludeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerLeaseAddrExcludeEnd.setStatus(_A)
class _IpeCfgDhcpMainServerOptGatewayAddrEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('enabledInterface',1),('enabledSpecify',2),('disabled',3)))
_IpeCfgDhcpMainServerOptGatewayAddrEnable_Type.__name__=_C
_IpeCfgDhcpMainServerOptGatewayAddrEnable_Object=MibTableColumn
ipeCfgDhcpMainServerOptGatewayAddrEnable=_IpeCfgDhcpMainServerOptGatewayAddrEnable_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,12),_IpeCfgDhcpMainServerOptGatewayAddrEnable_Type())
ipeCfgDhcpMainServerOptGatewayAddrEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptGatewayAddrEnable.setStatus(_A)
class _IpeCfgDhcpMainServerOptGatewayAddr_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainServerOptGatewayAddr_Type.__name__=_E
_IpeCfgDhcpMainServerOptGatewayAddr_Object=MibTableColumn
ipeCfgDhcpMainServerOptGatewayAddr=_IpeCfgDhcpMainServerOptGatewayAddr_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,13),_IpeCfgDhcpMainServerOptGatewayAddr_Type())
ipeCfgDhcpMainServerOptGatewayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptGatewayAddr.setStatus(_A)
class _IpeCfgDhcpMainServerOptDnsServerPrimary_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainServerOptDnsServerPrimary_Type.__name__=_E
_IpeCfgDhcpMainServerOptDnsServerPrimary_Object=MibTableColumn
ipeCfgDhcpMainServerOptDnsServerPrimary=_IpeCfgDhcpMainServerOptDnsServerPrimary_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,14),_IpeCfgDhcpMainServerOptDnsServerPrimary_Type())
ipeCfgDhcpMainServerOptDnsServerPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptDnsServerPrimary.setStatus(_A)
class _IpeCfgDhcpMainServerOptDnsServerSecondary_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainServerOptDnsServerSecondary_Type.__name__=_E
_IpeCfgDhcpMainServerOptDnsServerSecondary_Object=MibTableColumn
ipeCfgDhcpMainServerOptDnsServerSecondary=_IpeCfgDhcpMainServerOptDnsServerSecondary_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,15),_IpeCfgDhcpMainServerOptDnsServerSecondary_Type())
ipeCfgDhcpMainServerOptDnsServerSecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptDnsServerSecondary.setStatus(_A)
class _IpeCfgDhcpMainServerOptSpecifyEnable_Type(EnableDisableValue):defaultValue=1
_IpeCfgDhcpMainServerOptSpecifyEnable_Type.__name__=_I
_IpeCfgDhcpMainServerOptSpecifyEnable_Object=MibTableColumn
ipeCfgDhcpMainServerOptSpecifyEnable=_IpeCfgDhcpMainServerOptSpecifyEnable_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,16),_IpeCfgDhcpMainServerOptSpecifyEnable_Type())
ipeCfgDhcpMainServerOptSpecifyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptSpecifyEnable.setStatus(_A)
class _IpeCfgDhcpMainServerOptSpecifyId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpeCfgDhcpMainServerOptSpecifyId_Type.__name__=_C
_IpeCfgDhcpMainServerOptSpecifyId_Object=MibTableColumn
ipeCfgDhcpMainServerOptSpecifyId=_IpeCfgDhcpMainServerOptSpecifyId_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,17),_IpeCfgDhcpMainServerOptSpecifyId_Type())
ipeCfgDhcpMainServerOptSpecifyId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptSpecifyId.setStatus(_A)
class _IpeCfgDhcpMainServerOptSpecifyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('ipv4',1),('ipv6',2),('displayString',3),('octetString',4)))
_IpeCfgDhcpMainServerOptSpecifyType_Type.__name__=_C
_IpeCfgDhcpMainServerOptSpecifyType_Object=MibTableColumn
ipeCfgDhcpMainServerOptSpecifyType=_IpeCfgDhcpMainServerOptSpecifyType_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,18),_IpeCfgDhcpMainServerOptSpecifyType_Type())
ipeCfgDhcpMainServerOptSpecifyType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptSpecifyType.setStatus(_A)
class _IpeCfgDhcpMainServerOptSpecifyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpeCfgDhcpMainServerOptSpecifyValue_Type.__name__=_K
_IpeCfgDhcpMainServerOptSpecifyValue_Object=MibTableColumn
ipeCfgDhcpMainServerOptSpecifyValue=_IpeCfgDhcpMainServerOptSpecifyValue_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,19),_IpeCfgDhcpMainServerOptSpecifyValue_Type())
ipeCfgDhcpMainServerOptSpecifyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerOptSpecifyValue.setStatus(_A)
class _IpeCfgDhcpMainServerSecurityLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('any',1),('onlyRegistered',2)))
_IpeCfgDhcpMainServerSecurityLevel_Type.__name__=_C
_IpeCfgDhcpMainServerSecurityLevel_Object=MibTableColumn
ipeCfgDhcpMainServerSecurityLevel=_IpeCfgDhcpMainServerSecurityLevel_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,20),_IpeCfgDhcpMainServerSecurityLevel_Type())
ipeCfgDhcpMainServerSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerSecurityLevel.setStatus(_A)
class _IpeCfgDhcpMainServerRegisteredMacId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_IpeCfgDhcpMainServerRegisteredMacId_Type.__name__=_C
_IpeCfgDhcpMainServerRegisteredMacId_Object=MibTableColumn
ipeCfgDhcpMainServerRegisteredMacId=_IpeCfgDhcpMainServerRegisteredMacId_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,2,1,21),_IpeCfgDhcpMainServerRegisteredMacId_Type())
ipeCfgDhcpMainServerRegisteredMacId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCfgDhcpMainServerRegisteredMacId.setStatus(_A)
_IpeCfgDhcpMainRegisteredMacTable_Object=MibTable
ipeCfgDhcpMainRegisteredMacTable=_IpeCfgDhcpMainRegisteredMacTable_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3))
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacTable.setStatus(_A)
_IpeCfgDhcpMainRegisteredMacEntry_Object=MibTableRow
ipeCfgDhcpMainRegisteredMacEntry=_IpeCfgDhcpMainRegisteredMacEntry_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3,1))
ipeCfgDhcpMainRegisteredMacEntry.setIndexNames((0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacEntry.setStatus(_A)
class _IpeCfgDhcpMainRegisteredMacId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_IpeCfgDhcpMainRegisteredMacId_Type.__name__=_C
_IpeCfgDhcpMainRegisteredMacId_Object=MibTableColumn
ipeCfgDhcpMainRegisteredMacId=_IpeCfgDhcpMainRegisteredMacId_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3,1,1),_IpeCfgDhcpMainRegisteredMacId_Type())
ipeCfgDhcpMainRegisteredMacId.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacId.setStatus(_A)
class _IpeCfgDhcpMainRegisteredMacNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_IpeCfgDhcpMainRegisteredMacNo_Type.__name__=_C
_IpeCfgDhcpMainRegisteredMacNo_Object=MibTableColumn
ipeCfgDhcpMainRegisteredMacNo=_IpeCfgDhcpMainRegisteredMacNo_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3,1,2),_IpeCfgDhcpMainRegisteredMacNo_Type())
ipeCfgDhcpMainRegisteredMacNo.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacNo.setStatus(_A)
_IpeCfgDhcpMainRegisteredMacNEAddress_Type=IpAddress
_IpeCfgDhcpMainRegisteredMacNEAddress_Object=MibTableColumn
ipeCfgDhcpMainRegisteredMacNEAddress=_IpeCfgDhcpMainRegisteredMacNEAddress_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3,1,3),_IpeCfgDhcpMainRegisteredMacNEAddress_Type())
ipeCfgDhcpMainRegisteredMacNEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacNEAddress.setStatus(_A)
_IpeCfgDhcpMainRegisteredMacAddr_Type=MacAddress
_IpeCfgDhcpMainRegisteredMacAddr_Object=MibTableColumn
ipeCfgDhcpMainRegisteredMacAddr=_IpeCfgDhcpMainRegisteredMacAddr_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3,1,4),_IpeCfgDhcpMainRegisteredMacAddr_Type())
ipeCfgDhcpMainRegisteredMacAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacAddr.setStatus(_A)
class _IpeCfgDhcpMainRegisteredMacIpAddr_Type(IpAddress):defaultHexValue=_G
_IpeCfgDhcpMainRegisteredMacIpAddr_Type.__name__=_E
_IpeCfgDhcpMainRegisteredMacIpAddr_Object=MibTableColumn
ipeCfgDhcpMainRegisteredMacIpAddr=_IpeCfgDhcpMainRegisteredMacIpAddr_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3,1,5),_IpeCfgDhcpMainRegisteredMacIpAddr_Type())
ipeCfgDhcpMainRegisteredMacIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacIpAddr.setStatus(_A)
_IpeCfgDhcpMainRegisteredMacRowStatus_Type=RowStatus
_IpeCfgDhcpMainRegisteredMacRowStatus_Object=MibTableColumn
ipeCfgDhcpMainRegisteredMacRowStatus=_IpeCfgDhcpMainRegisteredMacRowStatus_Object((1,3,6,1,4,1,119,2,3,69,5,3,13,3,1,6),_IpeCfgDhcpMainRegisteredMacRowStatus_Type())
ipeCfgDhcpMainRegisteredMacRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:ipeCfgDhcpMainRegisteredMacRowStatus.setStatus(_A)
_IpeStatusGroup_ObjectIdentity=ObjectIdentity
ipeStatusGroup=_IpeStatusGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,5,6))
_IpeStsDhcpGroup_ObjectIdentity=ObjectIdentity
ipeStsDhcpGroup=_IpeStsDhcpGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,5,6,13))
_IpeStsDhcpMainLeaseTable_Object=MibTable
ipeStsDhcpMainLeaseTable=_IpeStsDhcpMainLeaseTable_Object((1,3,6,1,4,1,119,2,3,69,5,6,13,1))
if mibBuilder.loadTexts:ipeStsDhcpMainLeaseTable.setStatus(_A)
_IpeStsDhcpMainLeaseEntry_Object=MibTableRow
ipeStsDhcpMainLeaseEntry=_IpeStsDhcpMainLeaseEntry_Object((1,3,6,1,4,1,119,2,3,69,5,6,13,1,1))
ipeStsDhcpMainLeaseEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:ipeStsDhcpMainLeaseEntry.setStatus(_A)
class _IpeStsDhcpMainLeaseServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_IpeStsDhcpMainLeaseServerIndex_Type.__name__=_C
_IpeStsDhcpMainLeaseServerIndex_Object=MibTableColumn
ipeStsDhcpMainLeaseServerIndex=_IpeStsDhcpMainLeaseServerIndex_Object((1,3,6,1,4,1,119,2,3,69,5,6,13,1,1,1),_IpeStsDhcpMainLeaseServerIndex_Type())
ipeStsDhcpMainLeaseServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeStsDhcpMainLeaseServerIndex.setStatus(_A)
_IpeStsDhcpMainLeaseIpAddr_Type=IpAddress
_IpeStsDhcpMainLeaseIpAddr_Object=MibTableColumn
ipeStsDhcpMainLeaseIpAddr=_IpeStsDhcpMainLeaseIpAddr_Object((1,3,6,1,4,1,119,2,3,69,5,6,13,1,1,2),_IpeStsDhcpMainLeaseIpAddr_Type())
ipeStsDhcpMainLeaseIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeStsDhcpMainLeaseIpAddr.setStatus(_A)
_IpeStsDhcpMainLeaseNEAddress_Type=IpAddress
_IpeStsDhcpMainLeaseNEAddress_Object=MibTableColumn
ipeStsDhcpMainLeaseNEAddress=_IpeStsDhcpMainLeaseNEAddress_Object((1,3,6,1,4,1,119,2,3,69,5,6,13,1,1,3),_IpeStsDhcpMainLeaseNEAddress_Type())
ipeStsDhcpMainLeaseNEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeStsDhcpMainLeaseNEAddress.setStatus(_A)
_IpeStsDhcpMainLeaseMacAddr_Type=MacAddress
_IpeStsDhcpMainLeaseMacAddr_Object=MibTableColumn
ipeStsDhcpMainLeaseMacAddr=_IpeStsDhcpMainLeaseMacAddr_Object((1,3,6,1,4,1,119,2,3,69,5,6,13,1,1,4),_IpeStsDhcpMainLeaseMacAddr_Type())
ipeStsDhcpMainLeaseMacAddr.setMaxAccess(_Q)
if mibBuilder.loadTexts:ipeStsDhcpMainLeaseMacAddr.setStatus(_A)
_IpeStsDhcpMainLeaseDateAndTime_Type=DateAndTime
_IpeStsDhcpMainLeaseDateAndTime_Object=MibTableColumn
ipeStsDhcpMainLeaseDateAndTime=_IpeStsDhcpMainLeaseDateAndTime_Object((1,3,6,1,4,1,119,2,3,69,5,6,13,1,1,5),_IpeStsDhcpMainLeaseDateAndTime_Type())
ipeStsDhcpMainLeaseDateAndTime.setMaxAccess(_Q)
if mibBuilder.loadTexts:ipeStsDhcpMainLeaseDateAndTime.setStatus(_A)
_IpeCommandGroup_ObjectIdentity=ObjectIdentity
ipeCommandGroup=_IpeCommandGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,5,8))
_IpeCmdDhcpGroup_ObjectIdentity=ObjectIdentity
ipeCmdDhcpGroup=_IpeCmdDhcpGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,5,8,13))
_IpeCmdDhcpMainTable_Object=MibTable
ipeCmdDhcpMainTable=_IpeCmdDhcpMainTable_Object((1,3,6,1,4,1,119,2,3,69,5,8,13,1))
if mibBuilder.loadTexts:ipeCmdDhcpMainTable.setStatus(_A)
_IpeCmdDhcpMainEntry_Object=MibTableRow
ipeCmdDhcpMainEntry=_IpeCmdDhcpMainEntry_Object((1,3,6,1,4,1,119,2,3,69,5,8,13,1,1))
ipeCmdDhcpMainEntry.setIndexNames((0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:ipeCmdDhcpMainEntry.setStatus(_A)
class _IpeCmdDhcpMainIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_IpeCmdDhcpMainIndex_Type.__name__=_C
_IpeCmdDhcpMainIndex_Object=MibTableColumn
ipeCmdDhcpMainIndex=_IpeCmdDhcpMainIndex_Object((1,3,6,1,4,1,119,2,3,69,5,8,13,1,1,1),_IpeCmdDhcpMainIndex_Type())
ipeCmdDhcpMainIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCmdDhcpMainIndex.setStatus(_A)
_IpeCmdDhcpMainLeaseIpAddr_Type=IpAddress
_IpeCmdDhcpMainLeaseIpAddr_Object=MibTableColumn
ipeCmdDhcpMainLeaseIpAddr=_IpeCmdDhcpMainLeaseIpAddr_Object((1,3,6,1,4,1,119,2,3,69,5,8,13,1,1,2),_IpeCmdDhcpMainLeaseIpAddr_Type())
ipeCmdDhcpMainLeaseIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCmdDhcpMainLeaseIpAddr.setStatus(_A)
_IpeCmdDhcpMainNEAddress_Type=IpAddress
_IpeCmdDhcpMainNEAddress_Object=MibTableColumn
ipeCmdDhcpMainNEAddress=_IpeCmdDhcpMainNEAddress_Object((1,3,6,1,4,1,119,2,3,69,5,8,13,1,1,3),_IpeCmdDhcpMainNEAddress_Type())
ipeCmdDhcpMainNEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipeCmdDhcpMainNEAddress.setStatus(_A)
class _IpeCmdDhcpMainManualDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('normal',1),('manualDelete',2)))
_IpeCmdDhcpMainManualDelete_Type.__name__=_C
_IpeCmdDhcpMainManualDelete_Object=MibTableColumn
ipeCmdDhcpMainManualDelete=_IpeCmdDhcpMainManualDelete_Object((1,3,6,1,4,1,119,2,3,69,5,8,13,1,1,4),_IpeCmdDhcpMainManualDelete_Type())
ipeCmdDhcpMainManualDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipeCmdDhcpMainManualDelete.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_I:EnableDisableValue,'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'radioEquipment':radioEquipment,'system5':system5,'ipeConfigurationGroup':ipeConfigurationGroup,'ipeCfgDhcpGroup':ipeCfgDhcpGroup,'ipeCfgDhcpMainServerTable':ipeCfgDhcpMainServerTable,'ipeCfgDhcpMainServerEntry':ipeCfgDhcpMainServerEntry,_L:ipeCfgDhcpMainServerIndex,'ipeCfgDhcpMainServerNEAddress':ipeCfgDhcpMainServerNEAddress,'ipeCfgDhcpMainServerEnable':ipeCfgDhcpMainServerEnable,'ipeCfgDhcpMainServerMode':ipeCfgDhcpMainServerMode,'ipeCfgDhcpMainServerInterface':ipeCfgDhcpMainServerInterface,'ipeCfgDhcpMainServerIpAddr':ipeCfgDhcpMainServerIpAddr,'ipeCfgDhcpMainServerLeaseTime':ipeCfgDhcpMainServerLeaseTime,'ipeCfgDhcpMainServerLeaseAddrRangeBegin':ipeCfgDhcpMainServerLeaseAddrRangeBegin,'ipeCfgDhcpMainServerLeaseAddrRangeEnd':ipeCfgDhcpMainServerLeaseAddrRangeEnd,'ipeCfgDhcpMainServerLeaseAddrExcludeBegin':ipeCfgDhcpMainServerLeaseAddrExcludeBegin,'ipeCfgDhcpMainServerLeaseAddrExcludeEnd':ipeCfgDhcpMainServerLeaseAddrExcludeEnd,'ipeCfgDhcpMainServerOptGatewayAddrEnable':ipeCfgDhcpMainServerOptGatewayAddrEnable,'ipeCfgDhcpMainServerOptGatewayAddr':ipeCfgDhcpMainServerOptGatewayAddr,'ipeCfgDhcpMainServerOptDnsServerPrimary':ipeCfgDhcpMainServerOptDnsServerPrimary,'ipeCfgDhcpMainServerOptDnsServerSecondary':ipeCfgDhcpMainServerOptDnsServerSecondary,'ipeCfgDhcpMainServerOptSpecifyEnable':ipeCfgDhcpMainServerOptSpecifyEnable,'ipeCfgDhcpMainServerOptSpecifyId':ipeCfgDhcpMainServerOptSpecifyId,'ipeCfgDhcpMainServerOptSpecifyType':ipeCfgDhcpMainServerOptSpecifyType,'ipeCfgDhcpMainServerOptSpecifyValue':ipeCfgDhcpMainServerOptSpecifyValue,'ipeCfgDhcpMainServerSecurityLevel':ipeCfgDhcpMainServerSecurityLevel,'ipeCfgDhcpMainServerRegisteredMacId':ipeCfgDhcpMainServerRegisteredMacId,'ipeCfgDhcpMainRegisteredMacTable':ipeCfgDhcpMainRegisteredMacTable,'ipeCfgDhcpMainRegisteredMacEntry':ipeCfgDhcpMainRegisteredMacEntry,_M:ipeCfgDhcpMainRegisteredMacId,_N:ipeCfgDhcpMainRegisteredMacNo,'ipeCfgDhcpMainRegisteredMacNEAddress':ipeCfgDhcpMainRegisteredMacNEAddress,'ipeCfgDhcpMainRegisteredMacAddr':ipeCfgDhcpMainRegisteredMacAddr,'ipeCfgDhcpMainRegisteredMacIpAddr':ipeCfgDhcpMainRegisteredMacIpAddr,'ipeCfgDhcpMainRegisteredMacRowStatus':ipeCfgDhcpMainRegisteredMacRowStatus,'ipeStatusGroup':ipeStatusGroup,'ipeStsDhcpGroup':ipeStsDhcpGroup,'ipeStsDhcpMainLeaseTable':ipeStsDhcpMainLeaseTable,'ipeStsDhcpMainLeaseEntry':ipeStsDhcpMainLeaseEntry,_O:ipeStsDhcpMainLeaseServerIndex,_P:ipeStsDhcpMainLeaseIpAddr,'ipeStsDhcpMainLeaseNEAddress':ipeStsDhcpMainLeaseNEAddress,'ipeStsDhcpMainLeaseMacAddr':ipeStsDhcpMainLeaseMacAddr,'ipeStsDhcpMainLeaseDateAndTime':ipeStsDhcpMainLeaseDateAndTime,'ipeCommandGroup':ipeCommandGroup,'ipeCmdDhcpGroup':ipeCmdDhcpGroup,'ipeCmdDhcpMainTable':ipeCmdDhcpMainTable,'ipeCmdDhcpMainEntry':ipeCmdDhcpMainEntry,_R:ipeCmdDhcpMainIndex,_S:ipeCmdDhcpMainLeaseIpAddr,'ipeCmdDhcpMainNEAddress':ipeCmdDhcpMainNEAddress,'ipeCmdDhcpMainManualDelete':ipeCmdDhcpMainManualDelete})