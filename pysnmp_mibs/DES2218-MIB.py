_g='swPortCounterIndex'
_f='swPortCounterGroupIndex'
_e='swPortCtrlIndex'
_d='swPortCtrlGroupIndex'
_c='speed-100M'
_b='speed-10M'
_a='swPortInfoGroupIndex'
_Z='portType-Option-module-100Bridge'
_Y='portType-Option-module-RAS'
_X='portType-BNC'
_W='portType-Fiber'
_V='portType-AUI'
_U='portType-UTP'
_T='agentIpTrapManagerIpAddr'
_S='agentIpIfIndex'
_R='no-reset'
_Q='agentMibCapabilityIndex'
_P='NotificationType'
_O='OctetString'
_N='swPortInfoDuplexMode'
_M='swPortInfoLinkStatus'
_L='swPortInfoPartitionStatus'
_K='swPortInfoType'
_J='swPortInfoIndex'
_I='enabled'
_H='disabled'
_G='DisplayString'
_F='DES2218-MIB'
_E='read-write'
_D='other'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_P,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_P,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Dlink_ObjectIdentity=ObjectIdentity
dlink=_Dlink_ObjectIdentity((1,3,6,1,4,1,171))
_Dlink_products_ObjectIdentity=ObjectIdentity
dlink_products=_Dlink_products_ObjectIdentity((1,3,6,1,4,1,171,10))
_Dlink_Des2218Prod_ObjectIdentity=ObjectIdentity
dlink_Des2218Prod=_Dlink_Des2218Prod_ObjectIdentity((1,3,6,1,4,1,171,10,7))
_Dlink_Des2218ProdId_ObjectIdentity=ObjectIdentity
dlink_Des2218ProdId=_Dlink_Des2218ProdId_ObjectIdentity((1,3,6,1,4,1,171,10,7,1))
_Des2218SwHub_ObjectIdentity=ObjectIdentity
des2218SwHub=_Des2218SwHub_ObjectIdentity((1,3,6,1,4,1,171,10,7,2))
_Dlink_mgmt_ObjectIdentity=ObjectIdentity
dlink_mgmt=_Dlink_mgmt_ObjectIdentity((1,3,6,1,4,1,171,11))
_AgentConfigInfo_ObjectIdentity=ObjectIdentity
agentConfigInfo=_AgentConfigInfo_ObjectIdentity((1,3,6,1,4,1,171,11,1))
_AgentBasicInfo_ObjectIdentity=ObjectIdentity
agentBasicInfo=_AgentBasicInfo_ObjectIdentity((1,3,6,1,4,1,171,11,1,1))
class _AgentRuntimeSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_AgentRuntimeSwVersion_Type.__name__=_G
_AgentRuntimeSwVersion_Object=MibScalar
agentRuntimeSwVersion=_AgentRuntimeSwVersion_Object((1,3,6,1,4,1,171,11,1,1,1),_AgentRuntimeSwVersion_Type())
agentRuntimeSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRuntimeSwVersion.setStatus(_A)
class _AgentPromFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_AgentPromFwVersion_Type.__name__=_G
_AgentPromFwVersion_Object=MibScalar
agentPromFwVersion=_AgentPromFwVersion_Object((1,3,6,1,4,1,171,11,1,1,2),_AgentPromFwVersion_Type())
agentPromFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPromFwVersion.setStatus(_A)
class _AgentHwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_AgentHwRevision_Type.__name__=_G
_AgentHwRevision_Object=MibScalar
agentHwRevision=_AgentHwRevision_Object((1,3,6,1,4,1,171,11,1,1,3),_AgentHwRevision_Type())
agentHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:agentHwRevision.setStatus(_A)
class _AgentMgmtProtocolCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('snmp-ip',2),('snmp-ipx',3),('snmp-ip-ipx',4)))
_AgentMgmtProtocolCapability_Type.__name__=_C
_AgentMgmtProtocolCapability_Object=MibScalar
agentMgmtProtocolCapability=_AgentMgmtProtocolCapability_Object((1,3,6,1,4,1,171,11,1,1,4),_AgentMgmtProtocolCapability_Type())
agentMgmtProtocolCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:agentMgmtProtocolCapability.setStatus(_A)
_AgentMibCapabilityTable_Object=MibTable
agentMibCapabilityTable=_AgentMibCapabilityTable_Object((1,3,6,1,4,1,171,11,1,1,5))
if mibBuilder.loadTexts:agentMibCapabilityTable.setStatus(_A)
_AgentMibCapabilityEntry_Object=MibTableRow
agentMibCapabilityEntry=_AgentMibCapabilityEntry_Object((1,3,6,1,4,1,171,11,1,1,5,1))
agentMibCapabilityEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:agentMibCapabilityEntry.setStatus(_A)
_AgentMibCapabilityIndex_Type=Integer32
_AgentMibCapabilityIndex_Object=MibTableColumn
agentMibCapabilityIndex=_AgentMibCapabilityIndex_Object((1,3,6,1,4,1,171,11,1,1,5,1,1),_AgentMibCapabilityIndex_Type())
agentMibCapabilityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentMibCapabilityIndex.setStatus(_A)
class _AgentMibCapabilityDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AgentMibCapabilityDescr_Type.__name__=_G
_AgentMibCapabilityDescr_Object=MibTableColumn
agentMibCapabilityDescr=_AgentMibCapabilityDescr_Object((1,3,6,1,4,1,171,11,1,1,5,1,2),_AgentMibCapabilityDescr_Type())
agentMibCapabilityDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentMibCapabilityDescr.setStatus(_A)
_AgentMibCapabilityVersion_Type=Integer32
_AgentMibCapabilityVersion_Object=MibTableColumn
agentMibCapabilityVersion=_AgentMibCapabilityVersion_Object((1,3,6,1,4,1,171,11,1,1,5,1,3),_AgentMibCapabilityVersion_Type())
agentMibCapabilityVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentMibCapabilityVersion.setStatus(_A)
class _AgentMibCapabilityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('standard',2),('proprietary',3),('experiment',4)))
_AgentMibCapabilityType_Type.__name__=_C
_AgentMibCapabilityType_Object=MibTableColumn
agentMibCapabilityType=_AgentMibCapabilityType_Object((1,3,6,1,4,1,171,11,1,1,5,1,4),_AgentMibCapabilityType_Type())
agentMibCapabilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentMibCapabilityType.setStatus(_A)
_AgentBasicConfig_ObjectIdentity=ObjectIdentity
agentBasicConfig=_AgentBasicConfig_ObjectIdentity((1,3,6,1,4,1,171,11,1,2))
class _AgentSwUpdateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('network-load',2),('out-of-band-load',3)))
_AgentSwUpdateMode_Type.__name__=_C
_AgentSwUpdateMode_Object=MibScalar
agentSwUpdateMode=_AgentSwUpdateMode_Object((1,3,6,1,4,1,171,11,1,2,1),_AgentSwUpdateMode_Type())
agentSwUpdateMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentSwUpdateMode.setStatus(_A)
class _AgentSwUpdateCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_AgentSwUpdateCtrl_Type.__name__=_C
_AgentSwUpdateCtrl_Object=MibScalar
agentSwUpdateCtrl=_AgentSwUpdateCtrl_Object((1,3,6,1,4,1,171,11,1,2,2),_AgentSwUpdateCtrl_Type())
agentSwUpdateCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:agentSwUpdateCtrl.setStatus(_A)
class _AgentBootFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentBootFile_Type.__name__=_G
_AgentBootFile_Object=MibScalar
agentBootFile=_AgentBootFile_Object((1,3,6,1,4,1,171,11,1,2,3),_AgentBootFile_Type())
agentBootFile.setMaxAccess(_E)
if mibBuilder.loadTexts:agentBootFile.setStatus(_A)
class _AgentSystemReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('reset',2),(_R,3)))
_AgentSystemReset_Type.__name__=_C
_AgentSystemReset_Object=MibScalar
agentSystemReset=_AgentSystemReset_Object((1,3,6,1,4,1,171,11,1,2,4),_AgentSystemReset_Type())
agentSystemReset.setMaxAccess(_E)
if mibBuilder.loadTexts:agentSystemReset.setStatus(_A)
class _AgentRs232PortConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('console',2),('out-of-band',3)))
_AgentRs232PortConfig_Type.__name__=_C
_AgentRs232PortConfig_Object=MibScalar
agentRs232PortConfig=_AgentRs232PortConfig_Object((1,3,6,1,4,1,171,11,1,2,5),_AgentRs232PortConfig_Type())
agentRs232PortConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRs232PortConfig.setStatus(_A)
class _AgentOutOfBandBaudRateConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('baudRate-2400',2),('baudRate-9600',3),('baudRate-19200',4),('baudRate-38400',5)))
_AgentOutOfBandBaudRateConfig_Type.__name__=_C
_AgentOutOfBandBaudRateConfig_Object=MibScalar
agentOutOfBandBaudRateConfig=_AgentOutOfBandBaudRateConfig_Object((1,3,6,1,4,1,171,11,1,2,6),_AgentOutOfBandBaudRateConfig_Type())
agentOutOfBandBaudRateConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOutOfBandBaudRateConfig.setStatus(_A)
class _AgentOutOfBandDialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgentOutOfBandDialNumber_Type.__name__=_G
_AgentOutOfBandDialNumber_Object=MibScalar
agentOutOfBandDialNumber=_AgentOutOfBandDialNumber_Object((1,3,6,1,4,1,171,11,1,2,7),_AgentOutOfBandDialNumber_Type())
agentOutOfBandDialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOutOfBandDialNumber.setStatus(_A)
_AgentIpProtoConfig_ObjectIdentity=ObjectIdentity
agentIpProtoConfig=_AgentIpProtoConfig_ObjectIdentity((1,3,6,1,4,1,171,11,1,3))
_AgentIpNumOfIf_Type=Integer32
_AgentIpNumOfIf_Object=MibScalar
agentIpNumOfIf=_AgentIpNumOfIf_Object((1,3,6,1,4,1,171,11,1,3,1),_AgentIpNumOfIf_Type())
agentIpNumOfIf.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpNumOfIf.setStatus(_A)
_AgentIpIfTable_Object=MibTable
agentIpIfTable=_AgentIpIfTable_Object((1,3,6,1,4,1,171,11,1,3,2))
if mibBuilder.loadTexts:agentIpIfTable.setStatus(_A)
_AgentIpIfEntry_Object=MibTableRow
agentIpIfEntry=_AgentIpIfEntry_Object((1,3,6,1,4,1,171,11,1,3,2,1))
agentIpIfEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:agentIpIfEntry.setStatus(_A)
class _AgentIpIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentIpIfIndex_Type.__name__=_C
_AgentIpIfIndex_Object=MibTableColumn
agentIpIfIndex=_AgentIpIfIndex_Object((1,3,6,1,4,1,171,11,1,3,2,1,1),_AgentIpIfIndex_Type())
agentIpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpIfIndex.setStatus(_A)
_AgentIpIfAddress_Type=IpAddress
_AgentIpIfAddress_Object=MibTableColumn
agentIpIfAddress=_AgentIpIfAddress_Object((1,3,6,1,4,1,171,11,1,3,2,1,2),_AgentIpIfAddress_Type())
agentIpIfAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpIfAddress.setStatus(_A)
_AgentIpIfNetMask_Type=IpAddress
_AgentIpIfNetMask_Object=MibTableColumn
agentIpIfNetMask=_AgentIpIfNetMask_Object((1,3,6,1,4,1,171,11,1,3,2,1,3),_AgentIpIfNetMask_Type())
agentIpIfNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpIfNetMask.setStatus(_A)
_AgentIpIfDefaultRouter_Type=IpAddress
_AgentIpIfDefaultRouter_Object=MibTableColumn
agentIpIfDefaultRouter=_AgentIpIfDefaultRouter_Object((1,3,6,1,4,1,171,11,1,3,2,1,4),_AgentIpIfDefaultRouter_Type())
agentIpIfDefaultRouter.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpIfDefaultRouter.setStatus(_A)
_AgentIpIfMacAddr_Type=PhysAddress
_AgentIpIfMacAddr_Object=MibTableColumn
agentIpIfMacAddr=_AgentIpIfMacAddr_Object((1,3,6,1,4,1,171,11,1,3,2,1,5),_AgentIpIfMacAddr_Type())
agentIpIfMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpIfMacAddr.setStatus(_A)
class _AgentIpIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,28)));namedValues=NamedValues(*((_D,1),('ethernet-csmacd',6),('slip',28)))
_AgentIpIfType_Type.__name__=_C
_AgentIpIfType_Object=MibTableColumn
agentIpIfType=_AgentIpIfType_Object((1,3,6,1,4,1,171,11,1,3,2,1,6),_AgentIpIfType_Type())
agentIpIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpIfType.setStatus(_A)
_AgentIpBootServerAddr_Type=IpAddress
_AgentIpBootServerAddr_Object=MibScalar
agentIpBootServerAddr=_AgentIpBootServerAddr_Object((1,3,6,1,4,1,171,11,1,3,3),_AgentIpBootServerAddr_Type())
agentIpBootServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpBootServerAddr.setStatus(_A)
class _AgentIpBootProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('bootp-tftp',2),('tftp',3)))
_AgentIpBootProtocol_Type.__name__=_C
_AgentIpBootProtocol_Object=MibScalar
agentIpBootProtocol=_AgentIpBootProtocol_Object((1,3,6,1,4,1,171,11,1,3,4),_AgentIpBootProtocol_Type())
agentIpBootProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpBootProtocol.setStatus(_A)
class _AgentIpGetIpFromBootpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_AgentIpGetIpFromBootpServer_Type.__name__=_C
_AgentIpGetIpFromBootpServer_Object=MibScalar
agentIpGetIpFromBootpServer=_AgentIpGetIpFromBootpServer_Object((1,3,6,1,4,1,171,11,1,3,5),_AgentIpGetIpFromBootpServer_Type())
agentIpGetIpFromBootpServer.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpGetIpFromBootpServer.setStatus(_A)
_AgentIpUnauthAddr_Type=IpAddress
_AgentIpUnauthAddr_Object=MibScalar
agentIpUnauthAddr=_AgentIpUnauthAddr_Object((1,3,6,1,4,1,171,11,1,3,6),_AgentIpUnauthAddr_Type())
agentIpUnauthAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpUnauthAddr.setStatus(_A)
class _AgentIpUnauthComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AgentIpUnauthComm_Type.__name__=_G
_AgentIpUnauthComm_Object=MibScalar
agentIpUnauthComm=_AgentIpUnauthComm_Object((1,3,6,1,4,1,171,11,1,3,7),_AgentIpUnauthComm_Type())
agentIpUnauthComm.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpUnauthComm.setStatus(_A)
_AgentIpLastBootServerAddr_Type=IpAddress
_AgentIpLastBootServerAddr_Object=MibScalar
agentIpLastBootServerAddr=_AgentIpLastBootServerAddr_Object((1,3,6,1,4,1,171,11,1,3,8),_AgentIpLastBootServerAddr_Type())
agentIpLastBootServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpLastBootServerAddr.setStatus(_A)
_AgentIpLastIpAddr_Type=IpAddress
_AgentIpLastIpAddr_Object=MibScalar
agentIpLastIpAddr=_AgentIpLastIpAddr_Object((1,3,6,1,4,1,171,11,1,3,9),_AgentIpLastIpAddr_Type())
agentIpLastIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpLastIpAddr.setStatus(_A)
_AgentIpTrapManagerTable_Object=MibTable
agentIpTrapManagerTable=_AgentIpTrapManagerTable_Object((1,3,6,1,4,1,171,11,1,3,10))
if mibBuilder.loadTexts:agentIpTrapManagerTable.setStatus(_A)
_AgentIpTrapManagerEntry_Object=MibTableRow
agentIpTrapManagerEntry=_AgentIpTrapManagerEntry_Object((1,3,6,1,4,1,171,11,1,3,10,1))
agentIpTrapManagerEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:agentIpTrapManagerEntry.setStatus(_A)
_AgentIpTrapManagerIpAddr_Type=IpAddress
_AgentIpTrapManagerIpAddr_Object=MibTableColumn
agentIpTrapManagerIpAddr=_AgentIpTrapManagerIpAddr_Object((1,3,6,1,4,1,171,11,1,3,10,1,1),_AgentIpTrapManagerIpAddr_Type())
agentIpTrapManagerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIpTrapManagerIpAddr.setStatus(_A)
class _AgentIpTrapManagerComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AgentIpTrapManagerComm_Type.__name__=_G
_AgentIpTrapManagerComm_Object=MibTableColumn
agentIpTrapManagerComm=_AgentIpTrapManagerComm_Object((1,3,6,1,4,1,171,11,1,3,10,1,2),_AgentIpTrapManagerComm_Type())
agentIpTrapManagerComm.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpTrapManagerComm.setStatus(_A)
class _AgentIpTrapManagerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_AgentIpTrapManagerStatus_Type.__name__=_C
_AgentIpTrapManagerStatus_Object=MibTableColumn
agentIpTrapManagerStatus=_AgentIpTrapManagerStatus_Object((1,3,6,1,4,1,171,11,1,3,10,1,3),_AgentIpTrapManagerStatus_Type())
agentIpTrapManagerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpTrapManagerStatus.setStatus(_A)
_Des2218series_ObjectIdentity=ObjectIdentity
des2218series=_Des2218series_ObjectIdentity((1,3,6,1,4,1,171,11,7))
_Des2218MIB_ObjectIdentity=ObjectIdentity
des2218MIB=_Des2218MIB_ObjectIdentity((1,3,6,1,4,1,171,11,7,1))
_SwDevicePackage_ObjectIdentity=ObjectIdentity
swDevicePackage=_SwDevicePackage_ObjectIdentity((1,3,6,1,4,1,171,11,7,1,1))
_SwDeviceInfo_ObjectIdentity=ObjectIdentity
swDeviceInfo=_SwDeviceInfo_ObjectIdentity((1,3,6,1,4,1,171,11,7,1,1,1))
_SwDevInfoTotalNumOfPort_Type=Integer32
_SwDevInfoTotalNumOfPort_Object=MibScalar
swDevInfoTotalNumOfPort=_SwDevInfoTotalNumOfPort_Object((1,3,6,1,4,1,171,11,7,1,1,1,1),_SwDevInfoTotalNumOfPort_Type())
swDevInfoTotalNumOfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoTotalNumOfPort.setStatus(_A)
_SwDevInfoNumOfPortOnUse_Type=Integer32
_SwDevInfoNumOfPortOnUse_Object=MibScalar
swDevInfoNumOfPortOnUse=_SwDevInfoNumOfPortOnUse_Object((1,3,6,1,4,1,171,11,7,1,1,1,2),_SwDevInfoNumOfPortOnUse_Type())
swDevInfoNumOfPortOnUse.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoNumOfPortOnUse.setStatus(_A)
class _SwDevInfoDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwDevInfoDesc_Type.__name__=_G
_SwDevInfoDesc_Object=MibScalar
swDevInfoDesc=_SwDevInfoDesc_Object((1,3,6,1,4,1,171,11,7,1,1,1,3),_SwDevInfoDesc_Type())
swDevInfoDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoDesc.setStatus(_A)
class _SwDevInfoPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7)))
_SwDevInfoPortType_Type.__name__=_C
_SwDevInfoPortType_Object=MibScalar
swDevInfoPortType=_SwDevInfoPortType_Object((1,3,6,1,4,1,171,11,7,1,1,1,4),_SwDevInfoPortType_Type())
swDevInfoPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoPortType.setStatus(_A)
class _SwDevInfoHwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwDevInfoHwRev_Type.__name__=_G
_SwDevInfoHwRev_Object=MibScalar
swDevInfoHwRev=_SwDevInfoHwRev_Object((1,3,6,1,4,1,171,11,7,1,1,1,5),_SwDevInfoHwRev_Type())
swDevInfoHwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoHwRev.setStatus(_A)
_SwDevInfoSystemUpTime_Type=TimeTicks
_SwDevInfoSystemUpTime_Object=MibScalar
swDevInfoSystemUpTime=_SwDevInfoSystemUpTime_Object((1,3,6,1,4,1,171,11,7,1,1,1,6),_SwDevInfoSystemUpTime_Type())
swDevInfoSystemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoSystemUpTime.setStatus(_A)
class _SwDevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwDevInfoFrontPanelLedStatus_Type.__name__=_O
_SwDevInfoFrontPanelLedStatus_Object=MibScalar
swDevInfoFrontPanelLedStatus=_SwDevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,7,1,1,1,7),_SwDevInfoFrontPanelLedStatus_Type())
swDevInfoFrontPanelLedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoFrontPanelLedStatus.setStatus(_A)
_SwDevInfoDramSize_Type=Integer32
_SwDevInfoDramSize_Object=MibScalar
swDevInfoDramSize=_SwDevInfoDramSize_Object((1,3,6,1,4,1,171,11,7,1,1,1,8),_SwDevInfoDramSize_Type())
swDevInfoDramSize.setMaxAccess(_B)
if mibBuilder.loadTexts:swDevInfoDramSize.setStatus(_A)
_SwDeviceCtl_ObjectIdentity=ObjectIdentity
swDeviceCtl=_SwDeviceCtl_ObjectIdentity((1,3,6,1,4,1,171,11,7,1,1,2))
class _SwDevCtrlDisableLearningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwDevCtrlDisableLearningState_Type.__name__=_C
_SwDevCtrlDisableLearningState_Object=MibScalar
swDevCtrlDisableLearningState=_SwDevCtrlDisableLearningState_Object((1,3,6,1,4,1,171,11,7,1,1,2,1),_SwDevCtrlDisableLearningState_Type())
swDevCtrlDisableLearningState.setMaxAccess(_E)
if mibBuilder.loadTexts:swDevCtrlDisableLearningState.setStatus(_A)
class _SwDevCtrlReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('reset',2),(_R,3)))
_SwDevCtrlReset_Type.__name__=_C
_SwDevCtrlReset_Object=MibScalar
swDevCtrlReset=_SwDevCtrlReset_Object((1,3,6,1,4,1,171,11,7,1,1,2,2),_SwDevCtrlReset_Type())
swDevCtrlReset.setMaxAccess(_E)
if mibBuilder.loadTexts:swDevCtrlReset.setStatus(_A)
class _SwDevCtrlSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwDevCtrlSpanningTree_Type.__name__=_C
_SwDevCtrlSpanningTree_Object=MibScalar
swDevCtrlSpanningTree=_SwDevCtrlSpanningTree_Object((1,3,6,1,4,1,171,11,7,1,1,2,3),_SwDevCtrlSpanningTree_Type())
swDevCtrlSpanningTree.setMaxAccess(_E)
if mibBuilder.loadTexts:swDevCtrlSpanningTree.setStatus(_A)
_SwPortPackage_ObjectIdentity=ObjectIdentity
swPortPackage=_SwPortPackage_ObjectIdentity((1,3,6,1,4,1,171,11,7,1,2))
_SwPortInfoTable_Object=MibTable
swPortInfoTable=_SwPortInfoTable_Object((1,3,6,1,4,1,171,11,7,1,2,1))
if mibBuilder.loadTexts:swPortInfoTable.setStatus(_A)
_SwPortInfoEntry_Object=MibTableRow
swPortInfoEntry=_SwPortInfoEntry_Object((1,3,6,1,4,1,171,11,7,1,2,1,1))
swPortInfoEntry.setIndexNames((0,_F,_a),(0,_F,_J))
if mibBuilder.loadTexts:swPortInfoEntry.setStatus(_A)
_SwPortInfoGroupIndex_Type=Integer32
_SwPortInfoGroupIndex_Object=MibTableColumn
swPortInfoGroupIndex=_SwPortInfoGroupIndex_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,1),_SwPortInfoGroupIndex_Type())
swPortInfoGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoGroupIndex.setStatus(_A)
_SwPortInfoIndex_Type=Integer32
_SwPortInfoIndex_Object=MibTableColumn
swPortInfoIndex=_SwPortInfoIndex_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,2),_SwPortInfoIndex_Type())
swPortInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoIndex.setStatus(_A)
class _SwPortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7)))
_SwPortInfoType_Type.__name__=_C
_SwPortInfoType_Object=MibTableColumn
swPortInfoType=_SwPortInfoType_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,3),_SwPortInfoType_Type())
swPortInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoType.setStatus(_A)
class _SwPortInfoPartitionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no-partion',2),('partion',3)))
_SwPortInfoPartitionStatus_Type.__name__=_C
_SwPortInfoPartitionStatus_Object=MibTableColumn
swPortInfoPartitionStatus=_SwPortInfoPartitionStatus_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,4),_SwPortInfoPartitionStatus_Type())
swPortInfoPartitionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoPartitionStatus.setStatus(_A)
class _SwPortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('link-pass',2),('link-fail',3)))
_SwPortInfoLinkStatus_Type.__name__=_C
_SwPortInfoLinkStatus_Object=MibTableColumn
swPortInfoLinkStatus=_SwPortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,5),_SwPortInfoLinkStatus_Type())
swPortInfoLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoLinkStatus.setStatus(_A)
class _SwPortInfoDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('half',2),('full',3)))
_SwPortInfoDuplexMode_Type.__name__=_C
_SwPortInfoDuplexMode_Object=MibTableColumn
swPortInfoDuplexMode=_SwPortInfoDuplexMode_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,6),_SwPortInfoDuplexMode_Type())
swPortInfoDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoDuplexMode.setStatus(_A)
class _SwPortInfoNegotiationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwPortInfoNegotiationStatus_Type.__name__=_C
_SwPortInfoNegotiationStatus_Object=MibTableColumn
swPortInfoNegotiationStatus=_SwPortInfoNegotiationStatus_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,7),_SwPortInfoNegotiationStatus_Type())
swPortInfoNegotiationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoNegotiationStatus.setStatus(_A)
class _SwPortInfoSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_b,2),(_c,3)))
_SwPortInfoSpeedStatus_Type.__name__=_C
_SwPortInfoSpeedStatus_Object=MibTableColumn
swPortInfoSpeedStatus=_SwPortInfoSpeedStatus_Object((1,3,6,1,4,1,171,11,7,1,2,1,1,8),_SwPortInfoSpeedStatus_Type())
swPortInfoSpeedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortInfoSpeedStatus.setStatus(_A)
_SwPortCtrlTable_Object=MibTable
swPortCtrlTable=_SwPortCtrlTable_Object((1,3,6,1,4,1,171,11,7,1,2,2))
if mibBuilder.loadTexts:swPortCtrlTable.setStatus(_A)
_SwPortCtrlEntry_Object=MibTableRow
swPortCtrlEntry=_SwPortCtrlEntry_Object((1,3,6,1,4,1,171,11,7,1,2,2,1))
swPortCtrlEntry.setIndexNames((0,_F,_d),(0,_F,_e))
if mibBuilder.loadTexts:swPortCtrlEntry.setStatus(_A)
_SwPortCtrlGroupIndex_Type=Integer32
_SwPortCtrlGroupIndex_Object=MibTableColumn
swPortCtrlGroupIndex=_SwPortCtrlGroupIndex_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,1),_SwPortCtrlGroupIndex_Type())
swPortCtrlGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCtrlGroupIndex.setStatus(_A)
_SwPortCtrlIndex_Type=Integer32
_SwPortCtrlIndex_Object=MibTableColumn
swPortCtrlIndex=_SwPortCtrlIndex_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,2),_SwPortCtrlIndex_Type())
swPortCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCtrlIndex.setStatus(_A)
class _SwPortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwPortCtrlAdminState_Type.__name__=_C
_SwPortCtrlAdminState_Object=MibTableColumn
swPortCtrlAdminState=_SwPortCtrlAdminState_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,3),_SwPortCtrlAdminState_Type())
swPortCtrlAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlAdminState.setStatus(_A)
class _SwPortCtrlDuplexState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('half',2),('full',3)))
_SwPortCtrlDuplexState_Type.__name__=_C
_SwPortCtrlDuplexState_Object=MibTableColumn
swPortCtrlDuplexState=_SwPortCtrlDuplexState_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,4),_SwPortCtrlDuplexState_Type())
swPortCtrlDuplexState.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlDuplexState.setStatus(_A)
class _SwPortCtrlLinkStatusAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwPortCtrlLinkStatusAlarmState_Type.__name__=_C
_SwPortCtrlLinkStatusAlarmState_Object=MibTableColumn
swPortCtrlLinkStatusAlarmState=_SwPortCtrlLinkStatusAlarmState_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,5),_SwPortCtrlLinkStatusAlarmState_Type())
swPortCtrlLinkStatusAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlLinkStatusAlarmState.setStatus(_A)
class _SwPortCtrlFilterBcastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('forward',2),('discard',3)))
_SwPortCtrlFilterBcastState_Type.__name__=_C
_SwPortCtrlFilterBcastState_Object=MibTableColumn
swPortCtrlFilterBcastState=_SwPortCtrlFilterBcastState_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,6),_SwPortCtrlFilterBcastState_Type())
swPortCtrlFilterBcastState.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlFilterBcastState.setStatus(_A)
class _SwPortCtrlForwardUnknowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwPortCtrlForwardUnknowState_Type.__name__=_C
_SwPortCtrlForwardUnknowState_Object=MibTableColumn
swPortCtrlForwardUnknowState=_SwPortCtrlForwardUnknowState_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,7),_SwPortCtrlForwardUnknowState_Type())
swPortCtrlForwardUnknowState.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlForwardUnknowState.setStatus(_A)
class _SwPortCtrlPartitionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwPortCtrlPartitionStatus_Type.__name__=_C
_SwPortCtrlPartitionStatus_Object=MibTableColumn
swPortCtrlPartitionStatus=_SwPortCtrlPartitionStatus_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,8),_SwPortCtrlPartitionStatus_Type())
swPortCtrlPartitionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlPartitionStatus.setStatus(_A)
class _SwPortCtrlNegotiationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_H,2),(_I,3)))
_SwPortCtrlNegotiationStatus_Type.__name__=_C
_SwPortCtrlNegotiationStatus_Object=MibTableColumn
swPortCtrlNegotiationStatus=_SwPortCtrlNegotiationStatus_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,9),_SwPortCtrlNegotiationStatus_Type())
swPortCtrlNegotiationStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlNegotiationStatus.setStatus(_A)
class _SwPortCtrlSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_b,2),(_c,3)))
_SwPortCtrlSpeedStatus_Type.__name__=_C
_SwPortCtrlSpeedStatus_Object=MibTableColumn
swPortCtrlSpeedStatus=_SwPortCtrlSpeedStatus_Object((1,3,6,1,4,1,171,11,7,1,2,2,1,10),_SwPortCtrlSpeedStatus_Type())
swPortCtrlSpeedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swPortCtrlSpeedStatus.setStatus(_A)
_SwPortCounterTable_Object=MibTable
swPortCounterTable=_SwPortCounterTable_Object((1,3,6,1,4,1,171,11,7,1,2,3))
if mibBuilder.loadTexts:swPortCounterTable.setStatus(_A)
_SwPortCounterEntry_Object=MibTableRow
swPortCounterEntry=_SwPortCounterEntry_Object((1,3,6,1,4,1,171,11,7,1,2,3,1))
swPortCounterEntry.setIndexNames((0,_F,_f),(0,_F,_g))
if mibBuilder.loadTexts:swPortCounterEntry.setStatus(_A)
_SwPortCounterGroupIndex_Type=Integer32
_SwPortCounterGroupIndex_Object=MibTableColumn
swPortCounterGroupIndex=_SwPortCounterGroupIndex_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,1),_SwPortCounterGroupIndex_Type())
swPortCounterGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCounterGroupIndex.setStatus(_A)
_SwPortCounterIndex_Type=Integer32
_SwPortCounterIndex_Object=MibTableColumn
swPortCounterIndex=_SwPortCounterIndex_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,2),_SwPortCounterIndex_Type())
swPortCounterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCounterIndex.setStatus(_A)
_SwPortBytesReceived_Type=Counter32
_SwPortBytesReceived_Object=MibTableColumn
swPortBytesReceived=_SwPortBytesReceived_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,3),_SwPortBytesReceived_Type())
swPortBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortBytesReceived.setStatus(_A)
_SwPortBytesSent_Type=Counter32
_SwPortBytesSent_Object=MibTableColumn
swPortBytesSent=_SwPortBytesSent_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,4),_SwPortBytesSent_Type())
swPortBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortBytesSent.setStatus(_A)
_SwPortFramesReceived_Type=Counter32
_SwPortFramesReceived_Object=MibTableColumn
swPortFramesReceived=_SwPortFramesReceived_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,5),_SwPortFramesReceived_Type())
swPortFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFramesReceived.setStatus(_A)
_SwPortFramesSent_Type=Counter32
_SwPortFramesSent_Object=MibTableColumn
swPortFramesSent=_SwPortFramesSent_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,6),_SwPortFramesSent_Type())
swPortFramesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFramesSent.setStatus(_A)
_SwPortTotalBytesReceived_Type=Counter32
_SwPortTotalBytesReceived_Object=MibTableColumn
swPortTotalBytesReceived=_SwPortTotalBytesReceived_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,7),_SwPortTotalBytesReceived_Type())
swPortTotalBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortTotalBytesReceived.setStatus(_A)
_SwPortTotalFramesReceived_Type=Counter32
_SwPortTotalFramesReceived_Object=MibTableColumn
swPortTotalFramesReceived=_SwPortTotalFramesReceived_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,8),_SwPortTotalFramesReceived_Type())
swPortTotalFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortTotalFramesReceived.setStatus(_A)
_SwPortBroadcastFramesReceived_Type=Counter32
_SwPortBroadcastFramesReceived_Object=MibTableColumn
swPortBroadcastFramesReceived=_SwPortBroadcastFramesReceived_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,9),_SwPortBroadcastFramesReceived_Type())
swPortBroadcastFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortBroadcastFramesReceived.setStatus(_A)
_SwPortMulticastFramesReceived_Type=Counter32
_SwPortMulticastFramesReceived_Object=MibTableColumn
swPortMulticastFramesReceived=_SwPortMulticastFramesReceived_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,10),_SwPortMulticastFramesReceived_Type())
swPortMulticastFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortMulticastFramesReceived.setStatus(_A)
_SwPortCRCError_Type=Counter32
_SwPortCRCError_Object=MibTableColumn
swPortCRCError=_SwPortCRCError_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,11),_SwPortCRCError_Type())
swPortCRCError.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCRCError.setStatus(_A)
_SwPortOversizeFrames_Type=Counter32
_SwPortOversizeFrames_Object=MibTableColumn
swPortOversizeFrames=_SwPortOversizeFrames_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,12),_SwPortOversizeFrames_Type())
swPortOversizeFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortOversizeFrames.setStatus(_A)
_SwPortFragments_Type=Counter32
_SwPortFragments_Object=MibTableColumn
swPortFragments=_SwPortFragments_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,13),_SwPortFragments_Type())
swPortFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFragments.setStatus(_A)
_SwPortJabber_Type=Counter32
_SwPortJabber_Object=MibTableColumn
swPortJabber=_SwPortJabber_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,14),_SwPortJabber_Type())
swPortJabber.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortJabber.setStatus(_A)
_SwPortCollision_Type=Counter32
_SwPortCollision_Object=MibTableColumn
swPortCollision=_SwPortCollision_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,15),_SwPortCollision_Type())
swPortCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCollision.setStatus(_A)
_SwPortLateCollision_Type=Counter32
_SwPortLateCollision_Object=MibTableColumn
swPortLateCollision=_SwPortLateCollision_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,16),_SwPortLateCollision_Type())
swPortLateCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortLateCollision.setStatus(_A)
_SwPortFrames64Bytes_Type=Counter32
_SwPortFrames64Bytes_Object=MibTableColumn
swPortFrames64Bytes=_SwPortFrames64Bytes_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,17),_SwPortFrames64Bytes_Type())
swPortFrames64Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFrames64Bytes.setStatus(_A)
_SwPortFrames65To127Bytes_Type=Counter32
_SwPortFrames65To127Bytes_Object=MibTableColumn
swPortFrames65To127Bytes=_SwPortFrames65To127Bytes_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,18),_SwPortFrames65To127Bytes_Type())
swPortFrames65To127Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFrames65To127Bytes.setStatus(_A)
_SwPortFrames128To255Bytes_Type=Counter32
_SwPortFrames128To255Bytes_Object=MibTableColumn
swPortFrames128To255Bytes=_SwPortFrames128To255Bytes_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,19),_SwPortFrames128To255Bytes_Type())
swPortFrames128To255Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFrames128To255Bytes.setStatus(_A)
_SwPortFrames256To511Bytes_Type=Counter32
_SwPortFrames256To511Bytes_Object=MibTableColumn
swPortFrames256To511Bytes=_SwPortFrames256To511Bytes_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,20),_SwPortFrames256To511Bytes_Type())
swPortFrames256To511Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFrames256To511Bytes.setStatus(_A)
_SwPortFrames512To1023Bytes_Type=Counter32
_SwPortFrames512To1023Bytes_Object=MibTableColumn
swPortFrames512To1023Bytes=_SwPortFrames512To1023Bytes_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,21),_SwPortFrames512To1023Bytes_Type())
swPortFrames512To1023Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFrames512To1023Bytes.setStatus(_A)
_SwPortFrames1024To1522Bytes_Type=Counter32
_SwPortFrames1024To1522Bytes_Object=MibTableColumn
swPortFrames1024To1522Bytes=_SwPortFrames1024To1522Bytes_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,22),_SwPortFrames1024To1522Bytes_Type())
swPortFrames1024To1522Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFrames1024To1522Bytes.setStatus(_A)
_SwPortMACRxError_Type=Counter32
_SwPortMACRxError_Object=MibTableColumn
swPortMACRxError=_SwPortMACRxError_Object((1,3,6,1,4,1,171,11,7,1,2,3,1,23),_SwPortMACRxError_Type())
swPortMACRxError.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortMACRxError.setStatus(_A)
linkChangeEvent=NotificationType((1,3,6,1,4,1,171,0,1))
linkChangeEvent.setObjects(*((_F,_J),(_F,_K),(_F,_L),(_F,_M),(_F,_N)))
if mibBuilder.loadTexts:linkChangeEvent.setStatus('')
portPartition=NotificationType((1,3,6,1,4,1,171,0,2))
portPartition.setObjects(*((_F,_J),(_F,_K),(_F,_L),(_F,_M),(_F,_N)))
if mibBuilder.loadTexts:portPartition.setStatus('')
mibBuilder.exportSymbols(_F,**{'dlink':dlink,'linkChangeEvent':linkChangeEvent,'portPartition':portPartition,'dlink-products':dlink_products,'dlink-Des2218Prod':dlink_Des2218Prod,'dlink-Des2218ProdId':dlink_Des2218ProdId,'des2218SwHub':des2218SwHub,'dlink-mgmt':dlink_mgmt,'agentConfigInfo':agentConfigInfo,'agentBasicInfo':agentBasicInfo,'agentRuntimeSwVersion':agentRuntimeSwVersion,'agentPromFwVersion':agentPromFwVersion,'agentHwRevision':agentHwRevision,'agentMgmtProtocolCapability':agentMgmtProtocolCapability,'agentMibCapabilityTable':agentMibCapabilityTable,'agentMibCapabilityEntry':agentMibCapabilityEntry,_Q:agentMibCapabilityIndex,'agentMibCapabilityDescr':agentMibCapabilityDescr,'agentMibCapabilityVersion':agentMibCapabilityVersion,'agentMibCapabilityType':agentMibCapabilityType,'agentBasicConfig':agentBasicConfig,'agentSwUpdateMode':agentSwUpdateMode,'agentSwUpdateCtrl':agentSwUpdateCtrl,'agentBootFile':agentBootFile,'agentSystemReset':agentSystemReset,'agentRs232PortConfig':agentRs232PortConfig,'agentOutOfBandBaudRateConfig':agentOutOfBandBaudRateConfig,'agentOutOfBandDialNumber':agentOutOfBandDialNumber,'agentIpProtoConfig':agentIpProtoConfig,'agentIpNumOfIf':agentIpNumOfIf,'agentIpIfTable':agentIpIfTable,'agentIpIfEntry':agentIpIfEntry,_S:agentIpIfIndex,'agentIpIfAddress':agentIpIfAddress,'agentIpIfNetMask':agentIpIfNetMask,'agentIpIfDefaultRouter':agentIpIfDefaultRouter,'agentIpIfMacAddr':agentIpIfMacAddr,'agentIpIfType':agentIpIfType,'agentIpBootServerAddr':agentIpBootServerAddr,'agentIpBootProtocol':agentIpBootProtocol,'agentIpGetIpFromBootpServer':agentIpGetIpFromBootpServer,'agentIpUnauthAddr':agentIpUnauthAddr,'agentIpUnauthComm':agentIpUnauthComm,'agentIpLastBootServerAddr':agentIpLastBootServerAddr,'agentIpLastIpAddr':agentIpLastIpAddr,'agentIpTrapManagerTable':agentIpTrapManagerTable,'agentIpTrapManagerEntry':agentIpTrapManagerEntry,_T:agentIpTrapManagerIpAddr,'agentIpTrapManagerComm':agentIpTrapManagerComm,'agentIpTrapManagerStatus':agentIpTrapManagerStatus,'des2218series':des2218series,'des2218MIB':des2218MIB,'swDevicePackage':swDevicePackage,'swDeviceInfo':swDeviceInfo,'swDevInfoTotalNumOfPort':swDevInfoTotalNumOfPort,'swDevInfoNumOfPortOnUse':swDevInfoNumOfPortOnUse,'swDevInfoDesc':swDevInfoDesc,'swDevInfoPortType':swDevInfoPortType,'swDevInfoHwRev':swDevInfoHwRev,'swDevInfoSystemUpTime':swDevInfoSystemUpTime,'swDevInfoFrontPanelLedStatus':swDevInfoFrontPanelLedStatus,'swDevInfoDramSize':swDevInfoDramSize,'swDeviceCtl':swDeviceCtl,'swDevCtrlDisableLearningState':swDevCtrlDisableLearningState,'swDevCtrlReset':swDevCtrlReset,'swDevCtrlSpanningTree':swDevCtrlSpanningTree,'swPortPackage':swPortPackage,'swPortInfoTable':swPortInfoTable,'swPortInfoEntry':swPortInfoEntry,_a:swPortInfoGroupIndex,_J:swPortInfoIndex,_K:swPortInfoType,_L:swPortInfoPartitionStatus,_M:swPortInfoLinkStatus,_N:swPortInfoDuplexMode,'swPortInfoNegotiationStatus':swPortInfoNegotiationStatus,'swPortInfoSpeedStatus':swPortInfoSpeedStatus,'swPortCtrlTable':swPortCtrlTable,'swPortCtrlEntry':swPortCtrlEntry,_d:swPortCtrlGroupIndex,_e:swPortCtrlIndex,'swPortCtrlAdminState':swPortCtrlAdminState,'swPortCtrlDuplexState':swPortCtrlDuplexState,'swPortCtrlLinkStatusAlarmState':swPortCtrlLinkStatusAlarmState,'swPortCtrlFilterBcastState':swPortCtrlFilterBcastState,'swPortCtrlForwardUnknowState':swPortCtrlForwardUnknowState,'swPortCtrlPartitionStatus':swPortCtrlPartitionStatus,'swPortCtrlNegotiationStatus':swPortCtrlNegotiationStatus,'swPortCtrlSpeedStatus':swPortCtrlSpeedStatus,'swPortCounterTable':swPortCounterTable,'swPortCounterEntry':swPortCounterEntry,_f:swPortCounterGroupIndex,_g:swPortCounterIndex,'swPortBytesReceived':swPortBytesReceived,'swPortBytesSent':swPortBytesSent,'swPortFramesReceived':swPortFramesReceived,'swPortFramesSent':swPortFramesSent,'swPortTotalBytesReceived':swPortTotalBytesReceived,'swPortTotalFramesReceived':swPortTotalFramesReceived,'swPortBroadcastFramesReceived':swPortBroadcastFramesReceived,'swPortMulticastFramesReceived':swPortMulticastFramesReceived,'swPortCRCError':swPortCRCError,'swPortOversizeFrames':swPortOversizeFrames,'swPortFragments':swPortFragments,'swPortJabber':swPortJabber,'swPortCollision':swPortCollision,'swPortLateCollision':swPortLateCollision,'swPortFrames64Bytes':swPortFrames64Bytes,'swPortFrames65To127Bytes':swPortFrames65To127Bytes,'swPortFrames128To255Bytes':swPortFrames128To255Bytes,'swPortFrames256To511Bytes':swPortFrames256To511Bytes,'swPortFrames512To1023Bytes':swPortFrames512To1023Bytes,'swPortFrames1024To1522Bytes':swPortFrames1024To1522Bytes,'swPortMACRxError':swPortMACRxError})