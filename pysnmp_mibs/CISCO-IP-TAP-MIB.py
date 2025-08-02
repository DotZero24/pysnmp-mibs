_e='ciscoIpTapStreamComplianceGroup'
_d='citapStreamStatus'
_c='citapStreamVRF'
_b='citapStreamSourceL4PortMax'
_a='citapStreamSourceL4PortMin'
_Z='citapStreamDestL4PortMax'
_Y='citapStreamDestL4PortMin'
_X='citapStreamProtocol'
_W='citapStreamFlowId'
_V='citapStreamTosByteMask'
_U='citapStreamTosByte'
_T='citapStreamSourceLength'
_S='citapStreamSourceAddress'
_R='citapStreamDestinationLength'
_Q='citapStreamDestinationAddress'
_P='citapStreamAddrType'
_O='citapStreamInterface'
_N='citapStreamCapabilities'
_M='00000000'
_L='SnmpAdminString'
_K='InetAddressType'
_J='cTap2StreamIndex'
_I='cTap2MediationContentId'
_H='InetAddressPrefixLength'
_G='InetAddress'
_F='CISCO-TAP2-MIB'
_E='InetPortNumber'
_D='Integer32'
_C='read-create'
_B='CISCO-IP-TAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cTap2MediationContentId,cTap2StreamIndex=mibBuilder.importSymbols(_F,_I,_J)
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_H,_K,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoIpTapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,394))
if mibBuilder.loadTexts:ciscoIpTapMIB.setRevisions(('2004-03-11 00:00',))
_CiscoIpTapMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpTapMIBNotifs=_CiscoIpTapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,394,0))
_CiscoIpTapMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpTapMIBObjects=_CiscoIpTapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,394,1))
_CitapStreamEncodePacket_ObjectIdentity=ObjectIdentity
citapStreamEncodePacket=_CitapStreamEncodePacket_ObjectIdentity((1,3,6,1,4,1,9,9,394,1,1))
class _CitapStreamCapabilities_Type(Bits):namedValues=NamedValues(*(('tapEnable',0),('interface',1),('ipV4',2),('ipV6',3),('l4Port',4),('dscp',5),('voip',6)))
_CitapStreamCapabilities_Type.__name__='Bits'
_CitapStreamCapabilities_Object=MibScalar
citapStreamCapabilities=_CitapStreamCapabilities_Object((1,3,6,1,4,1,9,9,394,1,1,1),_CitapStreamCapabilities_Type())
citapStreamCapabilities.setMaxAccess('read-only')
if mibBuilder.loadTexts:citapStreamCapabilities.setStatus(_A)
_CitapStreamTable_Object=MibTable
citapStreamTable=_CitapStreamTable_Object((1,3,6,1,4,1,9,9,394,1,1,2))
if mibBuilder.loadTexts:citapStreamTable.setStatus(_A)
_CitapStreamEntry_Object=MibTableRow
citapStreamEntry=_CitapStreamEntry_Object((1,3,6,1,4,1,9,9,394,1,1,2,1))
citapStreamEntry.setIndexNames((0,_F,_I),(0,_F,_J))
if mibBuilder.loadTexts:citapStreamEntry.setStatus(_A)
class _CitapStreamInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_CitapStreamInterface_Type.__name__=_D
_CitapStreamInterface_Object=MibTableColumn
citapStreamInterface=_CitapStreamInterface_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,1),_CitapStreamInterface_Type())
citapStreamInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamInterface.setStatus(_A)
class _CitapStreamAddrType_Type(InetAddressType):defaultValue=1
_CitapStreamAddrType_Type.__name__=_K
_CitapStreamAddrType_Object=MibTableColumn
citapStreamAddrType=_CitapStreamAddrType_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,2),_CitapStreamAddrType_Type())
citapStreamAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamAddrType.setStatus(_A)
class _CitapStreamDestinationAddress_Type(InetAddress):defaultHexValue=_M
_CitapStreamDestinationAddress_Type.__name__=_G
_CitapStreamDestinationAddress_Object=MibTableColumn
citapStreamDestinationAddress=_CitapStreamDestinationAddress_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,3),_CitapStreamDestinationAddress_Type())
citapStreamDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamDestinationAddress.setStatus(_A)
class _CitapStreamDestinationLength_Type(InetAddressPrefixLength):defaultValue=0
_CitapStreamDestinationLength_Type.__name__=_H
_CitapStreamDestinationLength_Object=MibTableColumn
citapStreamDestinationLength=_CitapStreamDestinationLength_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,4),_CitapStreamDestinationLength_Type())
citapStreamDestinationLength.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamDestinationLength.setStatus(_A)
class _CitapStreamSourceAddress_Type(InetAddress):defaultHexValue=_M
_CitapStreamSourceAddress_Type.__name__=_G
_CitapStreamSourceAddress_Object=MibTableColumn
citapStreamSourceAddress=_CitapStreamSourceAddress_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,5),_CitapStreamSourceAddress_Type())
citapStreamSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamSourceAddress.setStatus(_A)
class _CitapStreamSourceLength_Type(InetAddressPrefixLength):defaultValue=0
_CitapStreamSourceLength_Type.__name__=_H
_CitapStreamSourceLength_Object=MibTableColumn
citapStreamSourceLength=_CitapStreamSourceLength_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,6),_CitapStreamSourceLength_Type())
citapStreamSourceLength.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamSourceLength.setStatus(_A)
class _CitapStreamTosByte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CitapStreamTosByte_Type.__name__=_D
_CitapStreamTosByte_Object=MibTableColumn
citapStreamTosByte=_CitapStreamTosByte_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,7),_CitapStreamTosByte_Type())
citapStreamTosByte.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamTosByte.setStatus(_A)
class _CitapStreamTosByteMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CitapStreamTosByteMask_Type.__name__=_D
_CitapStreamTosByteMask_Object=MibTableColumn
citapStreamTosByteMask=_CitapStreamTosByteMask_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,8),_CitapStreamTosByteMask_Type())
citapStreamTosByteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamTosByteMask.setStatus(_A)
class _CitapStreamFlowId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1048575))
_CitapStreamFlowId_Type.__name__=_D
_CitapStreamFlowId_Object=MibTableColumn
citapStreamFlowId=_CitapStreamFlowId_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,9),_CitapStreamFlowId_Type())
citapStreamFlowId.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamFlowId.setStatus(_A)
class _CitapStreamProtocol_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_CitapStreamProtocol_Type.__name__=_D
_CitapStreamProtocol_Object=MibTableColumn
citapStreamProtocol=_CitapStreamProtocol_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,10),_CitapStreamProtocol_Type())
citapStreamProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamProtocol.setStatus(_A)
class _CitapStreamDestL4PortMin_Type(InetPortNumber):defaultValue=0
_CitapStreamDestL4PortMin_Type.__name__=_E
_CitapStreamDestL4PortMin_Object=MibTableColumn
citapStreamDestL4PortMin=_CitapStreamDestL4PortMin_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,11),_CitapStreamDestL4PortMin_Type())
citapStreamDestL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamDestL4PortMin.setStatus(_A)
class _CitapStreamDestL4PortMax_Type(InetPortNumber):defaultValue=65535
_CitapStreamDestL4PortMax_Type.__name__=_E
_CitapStreamDestL4PortMax_Object=MibTableColumn
citapStreamDestL4PortMax=_CitapStreamDestL4PortMax_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,12),_CitapStreamDestL4PortMax_Type())
citapStreamDestL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamDestL4PortMax.setStatus(_A)
class _CitapStreamSourceL4PortMin_Type(InetPortNumber):defaultValue=0
_CitapStreamSourceL4PortMin_Type.__name__=_E
_CitapStreamSourceL4PortMin_Object=MibTableColumn
citapStreamSourceL4PortMin=_CitapStreamSourceL4PortMin_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,13),_CitapStreamSourceL4PortMin_Type())
citapStreamSourceL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamSourceL4PortMin.setStatus(_A)
class _CitapStreamSourceL4PortMax_Type(InetPortNumber):defaultValue=65535
_CitapStreamSourceL4PortMax_Type.__name__=_E
_CitapStreamSourceL4PortMax_Object=MibTableColumn
citapStreamSourceL4PortMax=_CitapStreamSourceL4PortMax_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,14),_CitapStreamSourceL4PortMax_Type())
citapStreamSourceL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamSourceL4PortMax.setStatus(_A)
class _CitapStreamVRF_Type(SnmpAdminString):defaultValue=OctetString('')
_CitapStreamVRF_Type.__name__=_L
_CitapStreamVRF_Object=MibTableColumn
citapStreamVRF=_CitapStreamVRF_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,15),_CitapStreamVRF_Type())
citapStreamVRF.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamVRF.setStatus(_A)
_CitapStreamStatus_Type=RowStatus
_CitapStreamStatus_Object=MibTableColumn
citapStreamStatus=_CitapStreamStatus_Object((1,3,6,1,4,1,9,9,394,1,1,2,1,16),_CitapStreamStatus_Type())
citapStreamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:citapStreamStatus.setStatus(_A)
_CiscoIpTapMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpTapMIBConform=_CiscoIpTapMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,394,2))
_CiscoIpTapMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpTapMIBCompliances=_CiscoIpTapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,394,2,1))
_CiscoIpTapMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpTapMIBGroups=_CiscoIpTapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,394,2,2))
ciscoIpTapStreamComplianceGroup=ObjectGroup((1,3,6,1,4,1,9,9,394,2,2,1))
ciscoIpTapStreamComplianceGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoIpTapStreamComplianceGroup.setStatus(_A)
ciscoIpTapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,394,2,1,1))
ciscoIpTapMIBCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:ciscoIpTapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpTapMIB':ciscoIpTapMIB,'ciscoIpTapMIBNotifs':ciscoIpTapMIBNotifs,'ciscoIpTapMIBObjects':ciscoIpTapMIBObjects,'citapStreamEncodePacket':citapStreamEncodePacket,_N:citapStreamCapabilities,'citapStreamTable':citapStreamTable,'citapStreamEntry':citapStreamEntry,_O:citapStreamInterface,_P:citapStreamAddrType,_Q:citapStreamDestinationAddress,_R:citapStreamDestinationLength,_S:citapStreamSourceAddress,_T:citapStreamSourceLength,_U:citapStreamTosByte,_V:citapStreamTosByteMask,_W:citapStreamFlowId,_X:citapStreamProtocol,_Y:citapStreamDestL4PortMin,_Z:citapStreamDestL4PortMax,_a:citapStreamSourceL4PortMin,_b:citapStreamSourceL4PortMax,_c:citapStreamVRF,_d:citapStreamStatus,'ciscoIpTapMIBConform':ciscoIpTapMIBConform,'ciscoIpTapMIBCompliances':ciscoIpTapMIBCompliances,'ciscoIpTapMIBCompliance':ciscoIpTapMIBCompliance,'ciscoIpTapMIBGroups':ciscoIpTapMIBGroups,_e:ciscoIpTapStreamComplianceGroup})