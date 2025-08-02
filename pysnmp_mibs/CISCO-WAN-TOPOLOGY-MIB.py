_AD='cwtLinkMIBGroups'
_AC='cwtLinkInfoDelete'
_AB='cwtLinkInfoModify'
_AA='cwtLinkInfoAdd'
_A9='cwtLinkRowStatus'
_A8='cwtLinkOutsideLink'
_A7='cwtFeederRowStatus'
_A6='cwtRowStatus'
_A5='cwtGatewayNodeOperStatus'
_A4='cwtLinkIndex'
_A3='cwtFeederIndex'
_A2='read-write'
_A1='cwtFeederMIBGroups'
_A0='cwtFeederInfoDelete'
_z='cwtFeederInfoModify'
_y='cwtFeederInfoAdd'
_x='cwtLinkInfoTimeOutFlag'
_w='cwtLinkRemotePhysicalId'
_v='cwtLinkLocalPhysicalId'
_u='cwtFeederModelNumber'
_t='cwtFeederPort'
_s='cwtFeederSlot'
_r='cwtFeederShelf'
_q='cwtLocalIfName'
_p='cwtGatewayAdminStatus'
_o='not-accessible'
_n='cwtNodalMIBGroups'
_m='cwtSystemMIBGroups'
_l='deprecated'
_k='cwtTopoDbFull'
_j='cwtTopoInfoDelete'
_i='cwtTopoInfoModify'
_h='cwtTopoInfoAdd'
_g='cwtConfigGatewayStatus'
_f='cwtFeederAtmIP'
_e='cwtFeederAtmIPAddrType'
_d='cwtFeederLanIP'
_c='cwtFeederLanIPAddrType'
_b='cwtFeederType'
_a='cwtFeederLMIType'
_Z='cwtNodeInfoTimeOutFlag'
_Y='cwtSysObjId'
_X='cwtSecIP'
_W='cwtSecIPAddrType'
_V='cwtSecIPIfName'
_U='cwtSecIPIfType'
_T='cwtPrimIP'
_S='cwtPrimIPAddrType'
_R='cwtPrimIPIfName'
_Q='cwtPrimIPIfType'
_P='cwtNodeName'
_O='cwtGatewayNodeFlag'
_N='cwtLinkRemoteIfIndex'
_M='cwtLinkLocalIfIndex'
_L='cwtLinkRemoteNodeId'
_K='cwtLinkLocalNodeId'
_J='cwtFeederName'
_I='cwtLocalIfIndex'
_H='cwtLocalNodeId'
_G='cwtNodeId'
_F='cwtDBLastChange'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='current'
_A='CISCO-WAN-TOPOLOGY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PnniNodeId,=mibBuilder.importSymbols('PNNI-MIB','PnniNodeId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoWanTopologyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,234))
if mibBuilder.loadTexts:ciscoWanTopologyMIB.setRevisions(('2002-07-16 00:00','2002-05-20 00:00','2002-04-22 00:00','2001-12-03 00:00'))
class CwtNodeInfoTableIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CiscoWanTopologyMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWanTopologyMIBNotifs=_CiscoWanTopologyMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,234,0))
_CiscoWanTopologyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanTopologyMIBObjects=_CiscoWanTopologyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,234,1))
_CwtSystemGroup_ObjectIdentity=ObjectIdentity
cwtSystemGroup=_CwtSystemGroup_ObjectIdentity((1,3,6,1,4,1,9,9,234,1,1))
class _CwtGatewayAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_CwtGatewayAdminStatus_Type.__name__=_E
_CwtGatewayAdminStatus_Object=MibScalar
cwtGatewayAdminStatus=_CwtGatewayAdminStatus_Object((1,3,6,1,4,1,9,9,234,1,1,1),_CwtGatewayAdminStatus_Type())
cwtGatewayAdminStatus.setMaxAccess(_A2)
if mibBuilder.loadTexts:cwtGatewayAdminStatus.setStatus(_B)
class _CwtGatewayNodeOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('disabled',1),('enabled',2),('disabling',3),('enabling',4),('enabledAndFull',5)))
_CwtGatewayNodeOperStatus_Type.__name__=_E
_CwtGatewayNodeOperStatus_Object=MibScalar
cwtGatewayNodeOperStatus=_CwtGatewayNodeOperStatus_Object((1,3,6,1,4,1,9,9,234,1,1,2),_CwtGatewayNodeOperStatus_Type())
cwtGatewayNodeOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtGatewayNodeOperStatus.setStatus(_B)
_CwtDBLastChange_Type=TimeStamp
_CwtDBLastChange_Object=MibScalar
cwtDBLastChange=_CwtDBLastChange_Object((1,3,6,1,4,1,9,9,234,1,1,3),_CwtDBLastChange_Type())
cwtDBLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtDBLastChange.setStatus(_B)
_CwtNodalInfoGroup_ObjectIdentity=ObjectIdentity
cwtNodalInfoGroup=_CwtNodalInfoGroup_ObjectIdentity((1,3,6,1,4,1,9,9,234,1,2))
_CwtNodeInfoTable_Object=MibTable
cwtNodeInfoTable=_CwtNodeInfoTable_Object((1,3,6,1,4,1,9,9,234,1,2,1))
if mibBuilder.loadTexts:cwtNodeInfoTable.setStatus(_B)
_CwtNodeInfoEntry_Object=MibTableRow
cwtNodeInfoEntry=_CwtNodeInfoEntry_Object((1,3,6,1,4,1,9,9,234,1,2,1,1))
cwtNodeInfoEntry.setIndexNames((0,_A,'cwtIndex'))
if mibBuilder.loadTexts:cwtNodeInfoEntry.setStatus(_B)
_CwtIndex_Type=CwtNodeInfoTableIndex
_CwtIndex_Object=MibTableColumn
cwtIndex=_CwtIndex_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,1),_CwtIndex_Type())
cwtIndex.setMaxAccess(_o)
if mibBuilder.loadTexts:cwtIndex.setStatus(_B)
_CwtGatewayNodeFlag_Type=TruthValue
_CwtGatewayNodeFlag_Object=MibTableColumn
cwtGatewayNodeFlag=_CwtGatewayNodeFlag_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,2),_CwtGatewayNodeFlag_Type())
cwtGatewayNodeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtGatewayNodeFlag.setStatus(_B)
_CwtNodeId_Type=PnniNodeId
_CwtNodeId_Object=MibTableColumn
cwtNodeId=_CwtNodeId_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,3),_CwtNodeId_Type())
cwtNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtNodeId.setStatus(_B)
_CwtNodeName_Type=SnmpAdminString
_CwtNodeName_Object=MibTableColumn
cwtNodeName=_CwtNodeName_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,4),_CwtNodeName_Type())
cwtNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtNodeName.setStatus(_B)
_CwtPrimIPIfType_Type=IANAifType
_CwtPrimIPIfType_Object=MibTableColumn
cwtPrimIPIfType=_CwtPrimIPIfType_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,5),_CwtPrimIPIfType_Type())
cwtPrimIPIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtPrimIPIfType.setStatus(_B)
_CwtPrimIPIfName_Type=SnmpAdminString
_CwtPrimIPIfName_Object=MibTableColumn
cwtPrimIPIfName=_CwtPrimIPIfName_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,6),_CwtPrimIPIfName_Type())
cwtPrimIPIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtPrimIPIfName.setStatus(_B)
_CwtPrimIPAddrType_Type=InetAddressType
_CwtPrimIPAddrType_Object=MibTableColumn
cwtPrimIPAddrType=_CwtPrimIPAddrType_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,7),_CwtPrimIPAddrType_Type())
cwtPrimIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtPrimIPAddrType.setStatus(_B)
_CwtPrimIP_Type=InetAddress
_CwtPrimIP_Object=MibTableColumn
cwtPrimIP=_CwtPrimIP_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,8),_CwtPrimIP_Type())
cwtPrimIP.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtPrimIP.setStatus(_B)
_CwtSecIPIfType_Type=IANAifType
_CwtSecIPIfType_Object=MibTableColumn
cwtSecIPIfType=_CwtSecIPIfType_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,9),_CwtSecIPIfType_Type())
cwtSecIPIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtSecIPIfType.setStatus(_B)
_CwtSecIPIfName_Type=SnmpAdminString
_CwtSecIPIfName_Object=MibTableColumn
cwtSecIPIfName=_CwtSecIPIfName_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,10),_CwtSecIPIfName_Type())
cwtSecIPIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtSecIPIfName.setStatus(_B)
_CwtSecIPAddrType_Type=InetAddressType
_CwtSecIPAddrType_Object=MibTableColumn
cwtSecIPAddrType=_CwtSecIPAddrType_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,11),_CwtSecIPAddrType_Type())
cwtSecIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtSecIPAddrType.setStatus(_B)
_CwtSecIP_Type=InetAddress
_CwtSecIP_Object=MibTableColumn
cwtSecIP=_CwtSecIP_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,12),_CwtSecIP_Type())
cwtSecIP.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtSecIP.setStatus(_B)
_CwtSysObjId_Type=ObjectIdentifier
_CwtSysObjId_Object=MibTableColumn
cwtSysObjId=_CwtSysObjId_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,13),_CwtSysObjId_Type())
cwtSysObjId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtSysObjId.setStatus(_B)
_CwtNodeInfoTimeOutFlag_Type=TruthValue
_CwtNodeInfoTimeOutFlag_Object=MibTableColumn
cwtNodeInfoTimeOutFlag=_CwtNodeInfoTimeOutFlag_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,14),_CwtNodeInfoTimeOutFlag_Type())
cwtNodeInfoTimeOutFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtNodeInfoTimeOutFlag.setStatus(_B)
_CwtRowStatus_Type=RowStatus
_CwtRowStatus_Object=MibTableColumn
cwtRowStatus=_CwtRowStatus_Object((1,3,6,1,4,1,9,9,234,1,2,1,1,15),_CwtRowStatus_Type())
cwtRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtRowStatus.setStatus(_B)
_CwtFeederInfoGroup_ObjectIdentity=ObjectIdentity
cwtFeederInfoGroup=_CwtFeederInfoGroup_ObjectIdentity((1,3,6,1,4,1,9,9,234,1,3))
_CwtFeederInfoTable_Object=MibTable
cwtFeederInfoTable=_CwtFeederInfoTable_Object((1,3,6,1,4,1,9,9,234,1,3,1))
if mibBuilder.loadTexts:cwtFeederInfoTable.setStatus(_B)
_CwtFeederInfoEntry_Object=MibTableRow
cwtFeederInfoEntry=_CwtFeederInfoEntry_Object((1,3,6,1,4,1,9,9,234,1,3,1,1))
cwtFeederInfoEntry.setIndexNames((0,_A,_A3))
if mibBuilder.loadTexts:cwtFeederInfoEntry.setStatus(_B)
_CwtFeederIndex_Type=Integer32
_CwtFeederIndex_Object=MibTableColumn
cwtFeederIndex=_CwtFeederIndex_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,1),_CwtFeederIndex_Type())
cwtFeederIndex.setMaxAccess(_o)
if mibBuilder.loadTexts:cwtFeederIndex.setStatus(_B)
_CwtLocalNodeId_Type=PnniNodeId
_CwtLocalNodeId_Object=MibTableColumn
cwtLocalNodeId=_CwtLocalNodeId_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,2),_CwtLocalNodeId_Type())
cwtLocalNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtLocalNodeId.setStatus(_B)
_CwtLocalIfIndex_Type=InterfaceIndex
_CwtLocalIfIndex_Object=MibTableColumn
cwtLocalIfIndex=_CwtLocalIfIndex_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,3),_CwtLocalIfIndex_Type())
cwtLocalIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtLocalIfIndex.setStatus(_B)
_CwtLocalIfName_Type=SnmpAdminString
_CwtLocalIfName_Object=MibTableColumn
cwtLocalIfName=_CwtLocalIfName_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,4),_CwtLocalIfName_Type())
cwtLocalIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtLocalIfName.setStatus(_B)
class _CwtFeederShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CwtFeederShelf_Type.__name__=_E
_CwtFeederShelf_Object=MibTableColumn
cwtFeederShelf=_CwtFeederShelf_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,5),_CwtFeederShelf_Type())
cwtFeederShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederShelf.setStatus(_B)
class _CwtFeederSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CwtFeederSlot_Type.__name__=_E
_CwtFeederSlot_Object=MibTableColumn
cwtFeederSlot=_CwtFeederSlot_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,6),_CwtFeederSlot_Type())
cwtFeederSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederSlot.setStatus(_B)
class _CwtFeederPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CwtFeederPort_Type.__name__=_E
_CwtFeederPort_Object=MibTableColumn
cwtFeederPort=_CwtFeederPort_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,7),_CwtFeederPort_Type())
cwtFeederPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederPort.setStatus(_B)
class _CwtFeederLMIType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('feeder',1),('xLMI',2)))
_CwtFeederLMIType_Type.__name__=_E
_CwtFeederLMIType_Object=MibTableColumn
cwtFeederLMIType=_CwtFeederLMIType_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,8),_CwtFeederLMIType_Type())
cwtFeederLMIType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederLMIType.setStatus(_B)
class _CwtFeederType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('fdrIPX',1),('fdrBPX',2),('fdrIpxAF',3),('fdrBASIS',4),('fdrUNKNOWN',5),('fdrUNI',6),('fdrAPS',7),('fdrIGX',8),('fdrIgxAF',9),('fdrVSI',10),('fdrPAR',11),('fdrNON',12)))
_CwtFeederType_Type.__name__=_E
_CwtFeederType_Object=MibTableColumn
cwtFeederType=_CwtFeederType_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,9),_CwtFeederType_Type())
cwtFeederType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederType.setStatus(_B)
_CwtFeederName_Type=SnmpAdminString
_CwtFeederName_Object=MibTableColumn
cwtFeederName=_CwtFeederName_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,10),_CwtFeederName_Type())
cwtFeederName.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederName.setStatus(_B)
_CwtFeederLanIPAddrType_Type=InetAddressType
_CwtFeederLanIPAddrType_Object=MibTableColumn
cwtFeederLanIPAddrType=_CwtFeederLanIPAddrType_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,11),_CwtFeederLanIPAddrType_Type())
cwtFeederLanIPAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederLanIPAddrType.setStatus(_B)
_CwtFeederLanIP_Type=InetAddress
_CwtFeederLanIP_Object=MibTableColumn
cwtFeederLanIP=_CwtFeederLanIP_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,12),_CwtFeederLanIP_Type())
cwtFeederLanIP.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederLanIP.setStatus(_B)
_CwtFeederAtmIPAddrType_Type=InetAddressType
_CwtFeederAtmIPAddrType_Object=MibTableColumn
cwtFeederAtmIPAddrType=_CwtFeederAtmIPAddrType_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,13),_CwtFeederAtmIPAddrType_Type())
cwtFeederAtmIPAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederAtmIPAddrType.setStatus(_B)
_CwtFeederAtmIP_Type=InetAddress
_CwtFeederAtmIP_Object=MibTableColumn
cwtFeederAtmIP=_CwtFeederAtmIP_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,14),_CwtFeederAtmIP_Type())
cwtFeederAtmIP.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederAtmIP.setStatus(_B)
class _CwtFeederModelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwtFeederModelNumber_Type.__name__=_E
_CwtFeederModelNumber_Object=MibTableColumn
cwtFeederModelNumber=_CwtFeederModelNumber_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,15),_CwtFeederModelNumber_Type())
cwtFeederModelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cwtFeederModelNumber.setStatus(_B)
_CwtFeederRowStatus_Type=RowStatus
_CwtFeederRowStatus_Object=MibTableColumn
cwtFeederRowStatus=_CwtFeederRowStatus_Object((1,3,6,1,4,1,9,9,234,1,3,1,1,16),_CwtFeederRowStatus_Type())
cwtFeederRowStatus.setMaxAccess(_A2)
if mibBuilder.loadTexts:cwtFeederRowStatus.setStatus(_B)
_CwtLinkInfoGroup_ObjectIdentity=ObjectIdentity
cwtLinkInfoGroup=_CwtLinkInfoGroup_ObjectIdentity((1,3,6,1,4,1,9,9,234,1,4))
_CwtLinkInfoTable_Object=MibTable
cwtLinkInfoTable=_CwtLinkInfoTable_Object((1,3,6,1,4,1,9,9,234,1,4,1))
if mibBuilder.loadTexts:cwtLinkInfoTable.setStatus(_B)
_CwtLinkInfoEntry_Object=MibTableRow
cwtLinkInfoEntry=_CwtLinkInfoEntry_Object((1,3,6,1,4,1,9,9,234,1,4,1,1))
cwtLinkInfoEntry.setIndexNames((0,_A,_A4))
if mibBuilder.loadTexts:cwtLinkInfoEntry.setStatus(_B)
_CwtLinkIndex_Type=Integer32
_CwtLinkIndex_Object=MibTableColumn
cwtLinkIndex=_CwtLinkIndex_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,1),_CwtLinkIndex_Type())
cwtLinkIndex.setMaxAccess(_o)
if mibBuilder.loadTexts:cwtLinkIndex.setStatus(_B)
_CwtLinkLocalNodeId_Type=PnniNodeId
_CwtLinkLocalNodeId_Object=MibTableColumn
cwtLinkLocalNodeId=_CwtLinkLocalNodeId_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,2),_CwtLinkLocalNodeId_Type())
cwtLinkLocalNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkLocalNodeId.setStatus(_B)
_CwtLinkRemoteNodeId_Type=PnniNodeId
_CwtLinkRemoteNodeId_Object=MibTableColumn
cwtLinkRemoteNodeId=_CwtLinkRemoteNodeId_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,3),_CwtLinkRemoteNodeId_Type())
cwtLinkRemoteNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkRemoteNodeId.setStatus(_B)
_CwtLinkLocalIfIndex_Type=InterfaceIndex
_CwtLinkLocalIfIndex_Object=MibTableColumn
cwtLinkLocalIfIndex=_CwtLinkLocalIfIndex_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,4),_CwtLinkLocalIfIndex_Type())
cwtLinkLocalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkLocalIfIndex.setStatus(_B)
_CwtLinkRemoteIfIndex_Type=InterfaceIndex
_CwtLinkRemoteIfIndex_Object=MibTableColumn
cwtLinkRemoteIfIndex=_CwtLinkRemoteIfIndex_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,5),_CwtLinkRemoteIfIndex_Type())
cwtLinkRemoteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkRemoteIfIndex.setStatus(_B)
_CwtLinkLocalPhysicalId_Type=SnmpAdminString
_CwtLinkLocalPhysicalId_Object=MibTableColumn
cwtLinkLocalPhysicalId=_CwtLinkLocalPhysicalId_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,6),_CwtLinkLocalPhysicalId_Type())
cwtLinkLocalPhysicalId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkLocalPhysicalId.setStatus(_B)
_CwtLinkRemotePhysicalId_Type=SnmpAdminString
_CwtLinkRemotePhysicalId_Object=MibTableColumn
cwtLinkRemotePhysicalId=_CwtLinkRemotePhysicalId_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,7),_CwtLinkRemotePhysicalId_Type())
cwtLinkRemotePhysicalId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkRemotePhysicalId.setStatus(_B)
_CwtLinkInfoTimeOutFlag_Type=TruthValue
_CwtLinkInfoTimeOutFlag_Object=MibTableColumn
cwtLinkInfoTimeOutFlag=_CwtLinkInfoTimeOutFlag_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,8),_CwtLinkInfoTimeOutFlag_Type())
cwtLinkInfoTimeOutFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkInfoTimeOutFlag.setStatus(_B)
_CwtLinkOutsideLink_Type=TruthValue
_CwtLinkOutsideLink_Object=MibTableColumn
cwtLinkOutsideLink=_CwtLinkOutsideLink_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,9),_CwtLinkOutsideLink_Type())
cwtLinkOutsideLink.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkOutsideLink.setStatus(_B)
_CwtLinkRowStatus_Type=RowStatus
_CwtLinkRowStatus_Object=MibTableColumn
cwtLinkRowStatus=_CwtLinkRowStatus_Object((1,3,6,1,4,1,9,9,234,1,4,1,1,10),_CwtLinkRowStatus_Type())
cwtLinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwtLinkRowStatus.setStatus(_B)
_CwtMIBConformance_ObjectIdentity=ObjectIdentity
cwtMIBConformance=_CwtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,234,2))
_CwtMIBCompliances_ObjectIdentity=ObjectIdentity
cwtMIBCompliances=_CwtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,234,2,1))
_CwtMIBGroups_ObjectIdentity=ObjectIdentity
cwtMIBGroups=_CwtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,234,2,2))
cwtSystemMIBGroups=ObjectGroup((1,3,6,1,4,1,9,9,234,2,2,1))
cwtSystemMIBGroups.setObjects(*((_A,_p),(_A,_A5),(_A,_F)))
if mibBuilder.loadTexts:cwtSystemMIBGroups.setStatus(_B)
cwtNodalMIBGroups=ObjectGroup((1,3,6,1,4,1,9,9,234,2,2,2))
cwtNodalMIBGroups.setObjects(*((_A,_O),(_A,_G),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A6)))
if mibBuilder.loadTexts:cwtNodalMIBGroups.setStatus(_B)
cwtFeederMIBGroups=ObjectGroup((1,3,6,1,4,1,9,9,234,2,2,3))
cwtFeederMIBGroups.setObjects(*((_A,_H),(_A,_I),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_a),(_A,_b),(_A,_J),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_u),(_A,_A7)))
if mibBuilder.loadTexts:cwtFeederMIBGroups.setStatus(_B)
cwtLinkMIBGroups=ObjectGroup((1,3,6,1,4,1,9,9,234,2,2,7))
cwtLinkMIBGroups.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_v),(_A,_w),(_A,_x),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cwtLinkMIBGroups.setStatus(_B)
cwtConfigGatewayStatus=NotificationType((1,3,6,1,4,1,9,9,234,0,1))
cwtConfigGatewayStatus.setObjects(*((_A,_p),(_A,_F)))
if mibBuilder.loadTexts:cwtConfigGatewayStatus.setStatus(_B)
cwtTopoInfoAdd=NotificationType((1,3,6,1,4,1,9,9,234,0,2))
cwtTopoInfoAdd.setObjects(*((_A,_O),(_A,_G),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_F)))
if mibBuilder.loadTexts:cwtTopoInfoAdd.setStatus(_B)
cwtTopoInfoModify=NotificationType((1,3,6,1,4,1,9,9,234,0,3))
cwtTopoInfoModify.setObjects(*((_A,_O),(_A,_G),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_F)))
if mibBuilder.loadTexts:cwtTopoInfoModify.setStatus(_B)
cwtTopoInfoDelete=NotificationType((1,3,6,1,4,1,9,9,234,0,4))
cwtTopoInfoDelete.setObjects(*((_A,_G),(_A,_F)))
if mibBuilder.loadTexts:cwtTopoInfoDelete.setStatus(_B)
cwtTopoDbFull=NotificationType((1,3,6,1,4,1,9,9,234,0,5))
cwtTopoDbFull.setObjects((_A,_F))
if mibBuilder.loadTexts:cwtTopoDbFull.setStatus(_B)
cwtFeederInfoAdd=NotificationType((1,3,6,1,4,1,9,9,234,0,6))
cwtFeederInfoAdd.setObjects(*((_A,_H),(_A,_I),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_a),(_A,_b),(_A,_J),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_u)))
if mibBuilder.loadTexts:cwtFeederInfoAdd.setStatus(_B)
cwtFeederInfoModify=NotificationType((1,3,6,1,4,1,9,9,234,0,7))
cwtFeederInfoModify.setObjects(*((_A,_H),(_A,_I),(_A,_a),(_A,_b),(_A,_J),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:cwtFeederInfoModify.setStatus(_B)
cwtFeederInfoDelete=NotificationType((1,3,6,1,4,1,9,9,234,0,8))
cwtFeederInfoDelete.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cwtFeederInfoDelete.setStatus(_B)
cwtLinkInfoAdd=NotificationType((1,3,6,1,4,1,9,9,234,0,9))
cwtLinkInfoAdd.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cwtLinkInfoAdd.setStatus(_B)
cwtLinkInfoModify=NotificationType((1,3,6,1,4,1,9,9,234,0,10))
cwtLinkInfoModify.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_x)))
if mibBuilder.loadTexts:cwtLinkInfoModify.setStatus(_B)
cwtLinkInfoDelete=NotificationType((1,3,6,1,4,1,9,9,234,0,11))
cwtLinkInfoDelete.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cwtLinkInfoDelete.setStatus(_B)
cwtNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,234,2,2,4))
cwtNotificationsGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:cwtNotificationsGroup.setStatus(_l)
cwtNotificationsGroup2=NotificationGroup((1,3,6,1,4,1,9,9,234,2,2,5))
cwtNotificationsGroup2.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:cwtNotificationsGroup2.setStatus(_l)
cwtNotificationsGroup3=NotificationGroup((1,3,6,1,4,1,9,9,234,2,2,6))
cwtNotificationsGroup3.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_y),(_A,_z),(_A,_A0),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:cwtNotificationsGroup3.setStatus(_B)
cwtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,234,2,1,1))
cwtMIBCompliance.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cwtMIBCompliance.setStatus(_l)
cwtMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,234,2,1,2))
cwtMIBCompliance2.setObjects(*((_A,_m),(_A,_n),(_A,_A1)))
if mibBuilder.loadTexts:cwtMIBCompliance2.setStatus(_l)
cwtMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,234,2,1,3))
cwtMIBCompliance3.setObjects(*((_A,_m),(_A,_n),(_A,_A1),(_A,_AD)))
if mibBuilder.loadTexts:cwtMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CwtNodeInfoTableIndex':CwtNodeInfoTableIndex,'ciscoWanTopologyMIB':ciscoWanTopologyMIB,'ciscoWanTopologyMIBNotifs':ciscoWanTopologyMIBNotifs,_g:cwtConfigGatewayStatus,_h:cwtTopoInfoAdd,_i:cwtTopoInfoModify,_j:cwtTopoInfoDelete,_k:cwtTopoDbFull,_y:cwtFeederInfoAdd,_z:cwtFeederInfoModify,_A0:cwtFeederInfoDelete,_AA:cwtLinkInfoAdd,_AB:cwtLinkInfoModify,_AC:cwtLinkInfoDelete,'ciscoWanTopologyMIBObjects':ciscoWanTopologyMIBObjects,'cwtSystemGroup':cwtSystemGroup,_p:cwtGatewayAdminStatus,_A5:cwtGatewayNodeOperStatus,_F:cwtDBLastChange,'cwtNodalInfoGroup':cwtNodalInfoGroup,'cwtNodeInfoTable':cwtNodeInfoTable,'cwtNodeInfoEntry':cwtNodeInfoEntry,'cwtIndex':cwtIndex,_O:cwtGatewayNodeFlag,_G:cwtNodeId,_P:cwtNodeName,_Q:cwtPrimIPIfType,_R:cwtPrimIPIfName,_S:cwtPrimIPAddrType,_T:cwtPrimIP,_U:cwtSecIPIfType,_V:cwtSecIPIfName,_W:cwtSecIPAddrType,_X:cwtSecIP,_Y:cwtSysObjId,_Z:cwtNodeInfoTimeOutFlag,_A6:cwtRowStatus,'cwtFeederInfoGroup':cwtFeederInfoGroup,'cwtFeederInfoTable':cwtFeederInfoTable,'cwtFeederInfoEntry':cwtFeederInfoEntry,_A3:cwtFeederIndex,_H:cwtLocalNodeId,_I:cwtLocalIfIndex,_q:cwtLocalIfName,_r:cwtFeederShelf,_s:cwtFeederSlot,_t:cwtFeederPort,_a:cwtFeederLMIType,_b:cwtFeederType,_J:cwtFeederName,_c:cwtFeederLanIPAddrType,_d:cwtFeederLanIP,_e:cwtFeederAtmIPAddrType,_f:cwtFeederAtmIP,_u:cwtFeederModelNumber,_A7:cwtFeederRowStatus,'cwtLinkInfoGroup':cwtLinkInfoGroup,'cwtLinkInfoTable':cwtLinkInfoTable,'cwtLinkInfoEntry':cwtLinkInfoEntry,_A4:cwtLinkIndex,_K:cwtLinkLocalNodeId,_L:cwtLinkRemoteNodeId,_M:cwtLinkLocalIfIndex,_N:cwtLinkRemoteIfIndex,_v:cwtLinkLocalPhysicalId,_w:cwtLinkRemotePhysicalId,_x:cwtLinkInfoTimeOutFlag,_A8:cwtLinkOutsideLink,_A9:cwtLinkRowStatus,'cwtMIBConformance':cwtMIBConformance,'cwtMIBCompliances':cwtMIBCompliances,'cwtMIBCompliance':cwtMIBCompliance,'cwtMIBCompliance2':cwtMIBCompliance2,'cwtMIBCompliance3':cwtMIBCompliance3,'cwtMIBGroups':cwtMIBGroups,_m:cwtSystemMIBGroups,_n:cwtNodalMIBGroups,_A1:cwtFeederMIBGroups,'cwtNotificationsGroup':cwtNotificationsGroup,'cwtNotificationsGroup2':cwtNotificationsGroup2,'cwtNotificationsGroup3':cwtNotificationsGroup3,_AD:cwtLinkMIBGroups})