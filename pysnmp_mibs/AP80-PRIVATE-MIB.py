_z='dot11ReasonCode'
_y='dot11RequestType'
_x='enterpriseApSTPNodeIndex'
_w='enterpriseApWMMAPParamIndex'
_v='ebabled'
_u='enterpriseApWMMBSSParamIndex'
_t='enterpriseApWMMAckPolicyIndex'
_s='enterpriseApWMMModeIndex'
_r='wdsPeerIndex'
_q='enterpriseAPVapRadioIndex'
_p='enterpriseApSessionStationAddres'
_o='enterpriseApSessionIfIndex'
_n='enterpriseApSNMPTrapDestinationIndex'
_m='alphanumeric'
_l='enterpriseApSecurityIndex'
_k='enterpriseApSyslogServerIndex'
_j='uplinkPortMacAddrIndex'
_i='enterpriseApFilterProtocolIndex'
_h='nativeVlanSsidNumber'
_g='nativeVlanIfIndex'
_f='dot11Vap8021xIndex'
_e='dot11FilterAddress'
_d='dot11AuthenticationServerIndex'
_c='running'
_b='dot3xFlowControl'
_a='backPressure'
_Z='fullDuplex1000'
_Y='halfDuplex1000'
_X='fullDuplex100'
_W='halfDuplex100'
_V='fullDuplex10'
_U='halfDuplex10'
_T='portIndex'
_S='lineIndex'
_R='supported'
_Q='error'
_P='dot11ApIpAddress'
_O='enterpriseApRadioIndex'
_N='required'
_M='none'
_L='mandatory'
_K='obsolete'
_J='dot11Station'
_I='DisplayString'
_H='not-accessible'
_G='read-only'
_F='AP80-PRIVATE-MIB'
_E='enabled'
_D='disabled'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class DisplayString(OctetString):0
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Aruba_ObjectIdentity=ObjectIdentity
aruba=_Aruba_ObjectIdentity((1,3,6,1,4,1,14823))
_ArubaEnterpriseMibModules_ObjectIdentity=ObjectIdentity
arubaEnterpriseMibModules=_ArubaEnterpriseMibModules_ObjectIdentity((1,3,6,1,4,1,14823,2))
_ArubaAp_ObjectIdentity=ObjectIdentity
arubaAp=_ArubaAp_ObjectIdentity((1,3,6,1,4,1,14823,2,3))
_WlsrOutDoorApMibModules_ObjectIdentity=ObjectIdentity
wlsrOutDoorApMibModules=_WlsrOutDoorApMibModules_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2))
_EnterpriseApSys_ObjectIdentity=ObjectIdentity
enterpriseApSys=_EnterpriseApSys_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,1))
class _SwHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwHardwareVer_Type.__name__=_I
_SwHardwareVer_Object=MibScalar
swHardwareVer=_SwHardwareVer_Object((1,3,6,1,4,1,14823,2,3,2,1,1),_SwHardwareVer_Type())
swHardwareVer.setMaxAccess(_G)
if mibBuilder.loadTexts:swHardwareVer.setStatus(_A)
class _SwBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBootRomVer_Type.__name__=_I
_SwBootRomVer_Object=MibScalar
swBootRomVer=_SwBootRomVer_Object((1,3,6,1,4,1,14823,2,3,2,1,2),_SwBootRomVer_Type())
swBootRomVer.setMaxAccess(_G)
if mibBuilder.loadTexts:swBootRomVer.setStatus(_A)
class _SwOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwOpCodeVer_Type.__name__=_I
_SwOpCodeVer_Object=MibScalar
swOpCodeVer=_SwOpCodeVer_Object((1,3,6,1,4,1,14823,2,3,2,1,3),_SwOpCodeVer_Type())
swOpCodeVer.setMaxAccess(_G)
if mibBuilder.loadTexts:swOpCodeVer.setStatus(_A)
class _SwSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwSerialNumber_Type.__name__=_I
_SwSerialNumber_Object=MibScalar
swSerialNumber=_SwSerialNumber_Object((1,3,6,1,4,1,14823,2,3,2,1,4),_SwSerialNumber_Type())
swSerialNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:swSerialNumber.setStatus(_A)
_SysNotificationTree_ObjectIdentity=ObjectIdentity
sysNotificationTree=_SysNotificationTree_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,1,5))
_SysNotificationObjects_ObjectIdentity=ObjectIdentity
sysNotificationObjects=_SysNotificationObjects_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,1,5,1))
_SysNotifications_ObjectIdentity=ObjectIdentity
sysNotifications=_SysNotifications_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,1,5,2))
_EnterpriseApLineMgnt_ObjectIdentity=ObjectIdentity
enterpriseApLineMgnt=_EnterpriseApLineMgnt_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,2))
_LineTable_Object=MibTable
lineTable=_LineTable_Object((1,3,6,1,4,1,14823,2,3,2,2,1))
if mibBuilder.loadTexts:lineTable.setStatus(_A)
_LineEntry_Object=MibTableRow
lineEntry=_LineEntry_Object((1,3,6,1,4,1,14823,2,3,2,2,1,1))
lineEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:lineEntry.setStatus(_A)
_LineIndex_Type=Integer32
_LineIndex_Object=MibTableColumn
lineIndex=_LineIndex_Object((1,3,6,1,4,1,14823,2,3,2,2,1,1,1),_LineIndex_Type())
lineIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lineIndex.setStatus(_A)
_LineDataBits_Type=Integer32
_LineDataBits_Object=MibTableColumn
lineDataBits=_LineDataBits_Object((1,3,6,1,4,1,14823,2,3,2,2,1,1,2),_LineDataBits_Type())
lineDataBits.setMaxAccess(_G)
if mibBuilder.loadTexts:lineDataBits.setStatus(_A)
class _LineParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('odd',1),('even',2),(_M,99)))
_LineParity_Type.__name__=_C
_LineParity_Object=MibTableColumn
lineParity=_LineParity_Object((1,3,6,1,4,1,14823,2,3,2,2,1,1,3),_LineParity_Type())
lineParity.setMaxAccess(_G)
if mibBuilder.loadTexts:lineParity.setStatus(_A)
_LineSpeed_Type=Integer32
_LineSpeed_Object=MibTableColumn
lineSpeed=_LineSpeed_Object((1,3,6,1,4,1,14823,2,3,2,2,1,1,4),_LineSpeed_Type())
lineSpeed.setMaxAccess(_G)
if mibBuilder.loadTexts:lineSpeed.setStatus(_A)
_LineStopBits_Type=Integer32
_LineStopBits_Object=MibTableColumn
lineStopBits=_LineStopBits_Object((1,3,6,1,4,1,14823,2,3,2,2,1,1,5),_LineStopBits_Type())
lineStopBits.setMaxAccess(_G)
if mibBuilder.loadTexts:lineStopBits.setStatus(_A)
_EnterpriseApPortMgnt_ObjectIdentity=ObjectIdentity
enterpriseApPortMgnt=_EnterpriseApPortMgnt_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,3))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,14823,2,3,2,3,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1))
portEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_I
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,2),_PortName_Type())
portName.setMaxAccess(_G)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),('thousandBaseT',6),('thousandBaseGBIC',7),('thousandBaseMiniGBIC',8)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,3),_PortType_Type())
portType.setMaxAccess(_G)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reserved',1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7)))
_PortSpeedDpxCfg_Type.__name__=_C
_PortSpeedDpxCfg_Object=MibTableColumn
portSpeedDpxCfg=_PortSpeedDpxCfg_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,4),_PortSpeedDpxCfg_Type())
portSpeedDpxCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:portSpeedDpxCfg.setStatus(_A)
class _PortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_D,2),(_a,3),(_b,4)))
_PortFlowCtrlCfg_Type.__name__=_C
_PortFlowCtrlCfg_Object=MibTableColumn
portFlowCtrlCfg=_PortFlowCtrlCfg_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,5),_PortFlowCtrlCfg_Type())
portFlowCtrlCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:portFlowCtrlCfg.setStatus(_A)
class _PortCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,99)));namedValues=NamedValues(*(('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('reserved6',6),('reserved7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('portCapSym',14),('portCapFlowCtrl',15),('portCap10half',99)))
_PortCapabilities_Type.__name__=_C
_PortCapabilities_Object=MibTableColumn
portCapabilities=_PortCapabilities_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,6),_PortCapabilities_Type())
portCapabilities.setMaxAccess(_G)
if mibBuilder.loadTexts:portCapabilities.setStatus(_A)
class _PortAutonegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_PortAutonegotiation_Type.__name__=_C
_PortAutonegotiation_Object=MibTableColumn
portAutonegotiation=_PortAutonegotiation_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,7),_PortAutonegotiation_Type())
portAutonegotiation.setMaxAccess(_G)
if mibBuilder.loadTexts:portAutonegotiation.setStatus(_A)
class _PortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7)))
_PortSpeedDpxStatus_Type.__name__=_C
_PortSpeedDpxStatus_Object=MibTableColumn
portSpeedDpxStatus=_PortSpeedDpxStatus_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,8),_PortSpeedDpxStatus_Type())
portSpeedDpxStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:portSpeedDpxStatus.setStatus(_A)
class _PortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_a,2),(_b,3),(_M,4)))
_PortFlowCtrlStatus_Type.__name__=_C
_PortFlowCtrlStatus_Object=MibTableColumn
portFlowCtrlStatus=_PortFlowCtrlStatus_Object((1,3,6,1,4,1,14823,2,3,2,3,1,1,9),_PortFlowCtrlStatus_Type())
portFlowCtrlStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:portFlowCtrlStatus.setStatus(_A)
_EnterpriseApFileTransferMgt_ObjectIdentity=ObjectIdentity
enterpriseApFileTransferMgt=_EnterpriseApFileTransferMgt_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,4))
class _TransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftp',1),('tftp',2)))
_TransferType_Type.__name__=_C
_TransferType_Object=MibScalar
transferType=_TransferType_Object((1,3,6,1,4,1,14823,2,3,2,4,1),_TransferType_Type())
transferType.setMaxAccess(_B)
if mibBuilder.loadTexts:transferType.setStatus(_A)
class _FileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('application',1),('config',2),('bootcode',3)))
_FileType_Type.__name__=_C
_FileType_Object=MibScalar
fileType=_FileType_Object((1,3,6,1,4,1,14823,2,3,2,4,2),_FileType_Type())
fileType.setMaxAccess(_B)
if mibBuilder.loadTexts:fileType.setStatus(_A)
class _SrcFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SrcFile_Type.__name__=_I
_SrcFile_Object=MibScalar
srcFile=_SrcFile_Object((1,3,6,1,4,1,14823,2,3,2,4,3),_SrcFile_Type())
srcFile.setMaxAccess(_B)
if mibBuilder.loadTexts:srcFile.setStatus(_A)
class _DestFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DestFile_Type.__name__=_I
_DestFile_Object=MibScalar
destFile=_DestFile_Object((1,3,6,1,4,1,14823,2,3,2,4,4),_DestFile_Type())
destFile.setMaxAccess(_B)
if mibBuilder.loadTexts:destFile.setStatus(_A)
_FileServer_Type=IpAddress
_FileServer_Object=MibScalar
fileServer=_FileServer_Object((1,3,6,1,4,1,14823,2,3,2,4,5),_FileServer_Type())
fileServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fileServer.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_UserName_Type.__name__=_I
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,14823,2,3,2,4,6),_UserName_Type())
userName.setMaxAccess(_B)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _Password_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Password_Type.__name__=_I
_Password_Object=MibScalar
password=_Password_Object((1,3,6,1,4,1,14823,2,3,2,4,7),_Password_Type())
password.setMaxAccess(_B)
if mibBuilder.loadTexts:password.setStatus(_A)
class _Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,11,12,13,20,30)));namedValues=NamedValues(*((_c,1),('success',2),('failureGeneric',3),('flashOpenError',10),('flashMallocError',11),('flashReadError',12),('flashFtypeError',13),('socketWriteError',20),('protocolError',30)))
_Status_Type.__name__=_C
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,14823,2,3,2,4,8),_Status_Type())
status.setMaxAccess(_G)
if mibBuilder.loadTexts:status.setStatus(_A)
class _TransferStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nothing',0),('download',1),('upload',2)))
_TransferStart_Type.__name__=_C
_TransferStart_Object=MibScalar
transferStart=_TransferStart_Object((1,3,6,1,4,1,14823,2,3,2,4,9),_TransferStart_Type())
transferStart.setMaxAccess(_B)
if mibBuilder.loadTexts:transferStart.setStatus(_A)
_EnterpriseApResetMgt_ObjectIdentity=ObjectIdentity
enterpriseApResetMgt=_EnterpriseApResetMgt_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,5))
class _RestartOpCodeFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RestartOpCodeFile_Type.__name__=_I
_RestartOpCodeFile_Object=MibScalar
restartOpCodeFile=_RestartOpCodeFile_Object((1,3,6,1,4,1,14823,2,3,2,5,1),_RestartOpCodeFile_Type())
restartOpCodeFile.setMaxAccess(_B)
if mibBuilder.loadTexts:restartOpCodeFile.setStatus(_A)
class _RestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('warmBoot',2),('coldBoot',3)))
_RestartControl_Type.__name__=_C
_RestartControl_Object=MibScalar
restartControl=_RestartControl_Object((1,3,6,1,4,1,14823,2,3,2,5,2),_RestartControl_Type())
restartControl.setMaxAccess(_B)
if mibBuilder.loadTexts:restartControl.setStatus(_A)
_EnterpriseApIpMgt_ObjectIdentity=ObjectIdentity
enterpriseApIpMgt=_EnterpriseApIpMgt_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,6))
_NetConfigIPAddress_Type=IpAddress
_NetConfigIPAddress_Object=MibScalar
netConfigIPAddress=_NetConfigIPAddress_Object((1,3,6,1,4,1,14823,2,3,2,6,1),_NetConfigIPAddress_Type())
netConfigIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigIPAddress.setStatus(_A)
_NetConfigSubnetMask_Type=IpAddress
_NetConfigSubnetMask_Object=MibScalar
netConfigSubnetMask=_NetConfigSubnetMask_Object((1,3,6,1,4,1,14823,2,3,2,6,2),_NetConfigSubnetMask_Type())
netConfigSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigSubnetMask.setStatus(_A)
_NetConfigDefaultGateway_Type=IpAddress
_NetConfigDefaultGateway_Object=MibScalar
netConfigDefaultGateway=_NetConfigDefaultGateway_Object((1,3,6,1,4,1,14823,2,3,2,6,3),_NetConfigDefaultGateway_Type())
netConfigDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigDefaultGateway.setStatus(_A)
class _NetConfigHttpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_NetConfigHttpState_Type.__name__=_C
_NetConfigHttpState_Object=MibScalar
netConfigHttpState=_NetConfigHttpState_Object((1,3,6,1,4,1,14823,2,3,2,6,4),_NetConfigHttpState_Type())
netConfigHttpState.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpState.setStatus(_A)
class _NetConfigHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_NetConfigHttpPort_Type.__name__=_C
_NetConfigHttpPort_Object=MibScalar
netConfigHttpPort=_NetConfigHttpPort_Object((1,3,6,1,4,1,14823,2,3,2,6,5),_NetConfigHttpPort_Type())
netConfigHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpPort.setStatus(_A)
class _NetConfigHttpsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_NetConfigHttpsState_Type.__name__=_C
_NetConfigHttpsState_Object=MibScalar
netConfigHttpsState=_NetConfigHttpsState_Object((1,3,6,1,4,1,14823,2,3,2,6,6),_NetConfigHttpsState_Type())
netConfigHttpsState.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpsState.setStatus(_A)
class _NetConfigHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_NetConfigHttpsPort_Type.__name__=_C
_NetConfigHttpsPort_Object=MibScalar
netConfigHttpsPort=_NetConfigHttpsPort_Object((1,3,6,1,4,1,14823,2,3,2,6,7),_NetConfigHttpsPort_Type())
netConfigHttpsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpsPort.setStatus(_A)
class _NetConfigDHCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_NetConfigDHCPState_Type.__name__=_C
_NetConfigDHCPState_Object=MibScalar
netConfigDHCPState=_NetConfigDHCPState_Object((1,3,6,1,4,1,14823,2,3,2,6,8),_NetConfigDHCPState_Type())
netConfigDHCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigDHCPState.setStatus(_A)
_EnterpriseAPdot11_ObjectIdentity=ObjectIdentity
enterpriseAPdot11=_EnterpriseAPdot11_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,7))
_Dot11AuthenticationEntry_ObjectIdentity=ObjectIdentity
dot11AuthenticationEntry=_Dot11AuthenticationEntry_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,7,1))
class _Dot118021xState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_R,1),(_N,2)))
_Dot118021xState_Type.__name__=_C
_Dot118021xState_Object=MibScalar
dot118021xState=_Dot118021xState_Object((1,3,6,1,4,1,14823,2,3,2,7,1,1),_Dot118021xState_Type())
dot118021xState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xState.setStatus(_K)
class _Dot118021xBroadcastKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot118021xBroadcastKeyRefreshRate_Type.__name__=_C
_Dot118021xBroadcastKeyRefreshRate_Object=MibScalar
dot118021xBroadcastKeyRefreshRate=_Dot118021xBroadcastKeyRefreshRate_Object((1,3,6,1,4,1,14823,2,3,2,7,1,2),_Dot118021xBroadcastKeyRefreshRate_Type())
dot118021xBroadcastKeyRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xBroadcastKeyRefreshRate.setStatus(_K)
class _Dot118021xSessionKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot118021xSessionKeyRefreshRate_Type.__name__=_C
_Dot118021xSessionKeyRefreshRate_Object=MibScalar
dot118021xSessionKeyRefreshRate=_Dot118021xSessionKeyRefreshRate_Object((1,3,6,1,4,1,14823,2,3,2,7,1,3),_Dot118021xSessionKeyRefreshRate_Type())
dot118021xSessionKeyRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSessionKeyRefreshRate.setStatus(_K)
class _Dot118021xReauthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot118021xReauthenticationTimeout_Type.__name__=_C
_Dot118021xReauthenticationTimeout_Object=MibScalar
dot118021xReauthenticationTimeout=_Dot118021xReauthenticationTimeout_Object((1,3,6,1,4,1,14823,2,3,2,7,1,4),_Dot118021xReauthenticationTimeout_Type())
dot118021xReauthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xReauthenticationTimeout.setStatus(_K)
class _Dot11MACAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('local',1),('radius',2)))
_Dot11MACAuthenticationType_Type.__name__=_C
_Dot11MACAuthenticationType_Object=MibScalar
dot11MACAuthenticationType=_Dot11MACAuthenticationType_Object((1,3,6,1,4,1,14823,2,3,2,7,1,5),_Dot11MACAuthenticationType_Type())
dot11MACAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11MACAuthenticationType.setStatus(_K)
_Dot11AuthenticationServerTable_Object=MibTable
dot11AuthenticationServerTable=_Dot11AuthenticationServerTable_Object((1,3,6,1,4,1,14823,2,3,2,7,2))
if mibBuilder.loadTexts:dot11AuthenticationServerTable.setStatus(_A)
_Dot11AuthenticationServerEntry_Object=MibTableRow
dot11AuthenticationServerEntry=_Dot11AuthenticationServerEntry_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1))
dot11AuthenticationServerEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:dot11AuthenticationServerEntry.setStatus(_A)
_Dot11AuthenticationServerIndex_Type=Integer32
_Dot11AuthenticationServerIndex_Object=MibTableColumn
dot11AuthenticationServerIndex=_Dot11AuthenticationServerIndex_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,1),_Dot11AuthenticationServerIndex_Type())
dot11AuthenticationServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11AuthenticationServerIndex.setStatus(_A)
_Dot11AuthenticationServer_Type=IpAddress
_Dot11AuthenticationServer_Object=MibTableColumn
dot11AuthenticationServer=_Dot11AuthenticationServer_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,2),_Dot11AuthenticationServer_Type())
dot11AuthenticationServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationServer.setStatus(_A)
class _Dot11AuthenticationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_Dot11AuthenticationPort_Type.__name__=_C
_Dot11AuthenticationPort_Object=MibTableColumn
dot11AuthenticationPort=_Dot11AuthenticationPort_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,3),_Dot11AuthenticationPort_Type())
dot11AuthenticationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationPort.setStatus(_A)
class _Dot11AuthenticationKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Dot11AuthenticationKey_Type.__name__=_I
_Dot11AuthenticationKey_Object=MibTableColumn
dot11AuthenticationKey=_Dot11AuthenticationKey_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,4),_Dot11AuthenticationKey_Type())
dot11AuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationKey.setStatus(_A)
class _Dot11AuthenticationRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_Dot11AuthenticationRetransmit_Type.__name__=_C
_Dot11AuthenticationRetransmit_Object=MibTableColumn
dot11AuthenticationRetransmit=_Dot11AuthenticationRetransmit_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,5),_Dot11AuthenticationRetransmit_Type())
dot11AuthenticationRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationRetransmit.setStatus(_A)
class _Dot11AuthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Dot11AuthenticationTimeout_Type.__name__=_C
_Dot11AuthenticationTimeout_Object=MibTableColumn
dot11AuthenticationTimeout=_Dot11AuthenticationTimeout_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,6),_Dot11AuthenticationTimeout_Type())
dot11AuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationTimeout.setStatus(_A)
class _Dot11AuthenticationAcctPort_Type(Integer32):defaultValue=1813;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_Dot11AuthenticationAcctPort_Type.__name__=_C
_Dot11AuthenticationAcctPort_Object=MibTableColumn
dot11AuthenticationAcctPort=_Dot11AuthenticationAcctPort_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,7),_Dot11AuthenticationAcctPort_Type())
dot11AuthenticationAcctPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationAcctPort.setStatus(_A)
class _Dot11AuthenticationAcctInterimUpdate_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_Dot11AuthenticationAcctInterimUpdate_Type.__name__=_C
_Dot11AuthenticationAcctInterimUpdate_Object=MibTableColumn
dot11AuthenticationAcctInterimUpdate=_Dot11AuthenticationAcctInterimUpdate_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,8),_Dot11AuthenticationAcctInterimUpdate_Type())
dot11AuthenticationAcctInterimUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationAcctInterimUpdate.setStatus(_A)
class _Dot11AuthenticationMACAddressFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('no-delimiter',1),('single-dash',2),('multi-dash',3),('multi-colon',4)))
_Dot11AuthenticationMACAddressFormat_Type.__name__=_C
_Dot11AuthenticationMACAddressFormat_Object=MibTableColumn
dot11AuthenticationMACAddressFormat=_Dot11AuthenticationMACAddressFormat_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,9),_Dot11AuthenticationMACAddressFormat_Type())
dot11AuthenticationMACAddressFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationMACAddressFormat.setStatus(_A)
class _Dot11AuthenticationVLANIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hex',1),('ascii',2)))
_Dot11AuthenticationVLANIDFormat_Type.__name__=_C
_Dot11AuthenticationVLANIDFormat_Object=MibTableColumn
dot11AuthenticationVLANIDFormat=_Dot11AuthenticationVLANIDFormat_Object((1,3,6,1,4,1,14823,2,3,2,7,2,1,10),_Dot11AuthenticationVLANIDFormat_Type())
dot11AuthenticationVLANIDFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationVLANIDFormat.setStatus(_A)
_Dot11MACAuthenticationFilter_ObjectIdentity=ObjectIdentity
dot11MACAuthenticationFilter=_Dot11MACAuthenticationFilter_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,7,3))
class _Dot11FilterDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_Dot11FilterDefault_Type.__name__=_C
_Dot11FilterDefault_Object=MibScalar
dot11FilterDefault=_Dot11FilterDefault_Object((1,3,6,1,4,1,14823,2,3,2,7,3,1),_Dot11FilterDefault_Type())
dot11FilterDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FilterDefault.setStatus(_A)
_Dot11FilterTable_Object=MibTable
dot11FilterTable=_Dot11FilterTable_Object((1,3,6,1,4,1,14823,2,3,2,7,3,2))
if mibBuilder.loadTexts:dot11FilterTable.setStatus(_A)
_Dot11FilterEntry_Object=MibTableRow
dot11FilterEntry=_Dot11FilterEntry_Object((1,3,6,1,4,1,14823,2,3,2,7,3,2,1))
dot11FilterEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:dot11FilterEntry.setStatus(_A)
_Dot11FilterAddress_Type=MacAddress
_Dot11FilterAddress_Object=MibTableColumn
dot11FilterAddress=_Dot11FilterAddress_Object((1,3,6,1,4,1,14823,2,3,2,7,3,2,1,1),_Dot11FilterAddress_Type())
dot11FilterAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11FilterAddress.setStatus(_A)
class _Dot11FilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(30,31,32)));namedValues=NamedValues(*(('allowed',30),('denied',31),('delete',32)))
_Dot11FilterStatus_Type.__name__=_C
_Dot11FilterStatus_Object=MibTableColumn
dot11FilterStatus=_Dot11FilterStatus_Object((1,3,6,1,4,1,14823,2,3,2,7,3,2,1,2),_Dot11FilterStatus_Type())
dot11FilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FilterStatus.setStatus(_A)
_Dot11NotificationTree_ObjectIdentity=ObjectIdentity
dot11NotificationTree=_Dot11NotificationTree_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,7,4))
_Dot11NotificationObjects_ObjectIdentity=ObjectIdentity
dot11NotificationObjects=_Dot11NotificationObjects_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,7,4,1))
_Dot11MacAddr_Type=MacAddress
_Dot11MacAddr_Object=MibScalar
dot11MacAddr=_Dot11MacAddr_Object((1,3,6,1,4,1,14823,2,3,2,7,4,1,1),_Dot11MacAddr_Type())
dot11MacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11MacAddr.setStatus(_A)
_Dot11Station_Type=MacAddress
_Dot11Station_Object=MibScalar
dot11Station=_Dot11Station_Object((1,3,6,1,4,1,14823,2,3,2,7,4,1,2),_Dot11Station_Type())
dot11Station.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11Station.setStatus(_A)
class _Dot11RequestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('association',2),('reAssociation',3),('authentication',4)))
_Dot11RequestType_Type.__name__=_C
_Dot11RequestType_Object=MibScalar
dot11RequestType=_Dot11RequestType_Object((1,3,6,1,4,1,14823,2,3,2,7,4,1,3),_Dot11RequestType_Type())
dot11RequestType.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11RequestType.setStatus(_A)
class _Dot11ReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('invalidModeOrState',1),('unAuthenticatedStation',2),('internalError',3),('outOfSequenceFrame',4),('unsupportedAlgorithm',5),('invalidFrameLngth',6),('wepRequiredOnAP',7),('wepNotAllowed',8),('challengeTextMismatch',9)))
_Dot11ReasonCode_Type.__name__=_C
_Dot11ReasonCode_Object=MibScalar
dot11ReasonCode=_Dot11ReasonCode_Object((1,3,6,1,4,1,14823,2,3,2,7,4,1,4),_Dot11ReasonCode_Type())
dot11ReasonCode.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11ReasonCode.setStatus(_A)
_Dot11ApIpAddress_Type=IpAddress
_Dot11ApIpAddress_Object=MibScalar
dot11ApIpAddress=_Dot11ApIpAddress_Object((1,3,6,1,4,1,14823,2,3,2,7,4,1,5),_Dot11ApIpAddress_Type())
dot11ApIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11ApIpAddress.setStatus(_A)
_Dot1xAuthenticatorMacAddr_Type=MacAddress
_Dot1xAuthenticatorMacAddr_Object=MibScalar
dot1xAuthenticatorMacAddr=_Dot1xAuthenticatorMacAddr_Object((1,3,6,1,4,1,14823,2,3,2,7,4,1,6),_Dot1xAuthenticatorMacAddr_Type())
dot1xAuthenticatorMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:dot1xAuthenticatorMacAddr.setStatus(_A)
_Dot11Notifications_ObjectIdentity=ObjectIdentity
dot11Notifications=_Dot11Notifications_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,7,4,2))
_Dot11AuthenticationSupplicantTable_Object=MibTable
dot11AuthenticationSupplicantTable=_Dot11AuthenticationSupplicantTable_Object((1,3,6,1,4,1,14823,2,3,2,7,5))
if mibBuilder.loadTexts:dot11AuthenticationSupplicantTable.setStatus(_A)
_Dot11AuthenticationSupplicantEntry_Object=MibTableRow
dot11AuthenticationSupplicantEntry=_Dot11AuthenticationSupplicantEntry_Object((1,3,6,1,4,1,14823,2,3,2,7,5,1))
dot11AuthenticationSupplicantEntry.setIndexNames((0,_F,'dot11AuthenticationSuppIndex'))
if mibBuilder.loadTexts:dot11AuthenticationSupplicantEntry.setStatus(_A)
_Dot118021xSuppIndex_Type=Integer32
_Dot118021xSuppIndex_Object=MibTableColumn
dot118021xSuppIndex=_Dot118021xSuppIndex_Object((1,3,6,1,4,1,14823,2,3,2,7,5,1,1),_Dot118021xSuppIndex_Type())
dot118021xSuppIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dot118021xSuppIndex.setStatus(_A)
class _Dot118021xSuppState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_Dot118021xSuppState_Type.__name__=_C
_Dot118021xSuppState_Object=MibTableColumn
dot118021xSuppState=_Dot118021xSuppState_Object((1,3,6,1,4,1,14823,2,3,2,7,5,1,2),_Dot118021xSuppState_Type())
dot118021xSuppState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSuppState.setStatus(_A)
class _Dot118021xSuppUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Dot118021xSuppUser_Type.__name__=_I
_Dot118021xSuppUser_Object=MibTableColumn
dot118021xSuppUser=_Dot118021xSuppUser_Object((1,3,6,1,4,1,14823,2,3,2,7,5,1,3),_Dot118021xSuppUser_Type())
dot118021xSuppUser.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSuppUser.setStatus(_A)
class _Dot118021xSuppPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Dot118021xSuppPasswd_Type.__name__=_I
_Dot118021xSuppPasswd_Object=MibTableColumn
dot118021xSuppPasswd=_Dot118021xSuppPasswd_Object((1,3,6,1,4,1,14823,2,3,2,7,5,1,4),_Dot118021xSuppPasswd_Type())
dot118021xSuppPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSuppPasswd.setStatus(_A)
_Dot11VapAuthenticationTable_Object=MibTable
dot11VapAuthenticationTable=_Dot11VapAuthenticationTable_Object((1,3,6,1,4,1,14823,2,3,2,7,6))
if mibBuilder.loadTexts:dot11VapAuthenticationTable.setStatus(_A)
_Dot11VapAuthenticationEntry_Object=MibTableRow
dot11VapAuthenticationEntry=_Dot11VapAuthenticationEntry_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1))
dot11VapAuthenticationEntry.setIndexNames((0,_F,_f))
if mibBuilder.loadTexts:dot11VapAuthenticationEntry.setStatus(_A)
_Dot11Vap8021xIndex_Type=Integer32
_Dot11Vap8021xIndex_Object=MibTableColumn
dot11Vap8021xIndex=_Dot11Vap8021xIndex_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1,1),_Dot11Vap8021xIndex_Type())
dot11Vap8021xIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11Vap8021xIndex.setStatus(_A)
class _Dot11Vap8021xState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_R,1),(_N,2)))
_Dot11Vap8021xState_Type.__name__=_C
_Dot11Vap8021xState_Object=MibTableColumn
dot11Vap8021xState=_Dot11Vap8021xState_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1,2),_Dot11Vap8021xState_Type())
dot11Vap8021xState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11Vap8021xState.setStatus(_A)
class _Dot11Vap8021xBroadcastKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot11Vap8021xBroadcastKeyRefreshRate_Type.__name__=_C
_Dot11Vap8021xBroadcastKeyRefreshRate_Object=MibTableColumn
dot11Vap8021xBroadcastKeyRefreshRate=_Dot11Vap8021xBroadcastKeyRefreshRate_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1,3),_Dot11Vap8021xBroadcastKeyRefreshRate_Type())
dot11Vap8021xBroadcastKeyRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11Vap8021xBroadcastKeyRefreshRate.setStatus(_A)
class _Dot11Vap8021xSessionKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot11Vap8021xSessionKeyRefreshRate_Type.__name__=_C
_Dot11Vap8021xSessionKeyRefreshRate_Object=MibTableColumn
dot11Vap8021xSessionKeyRefreshRate=_Dot11Vap8021xSessionKeyRefreshRate_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1,4),_Dot11Vap8021xSessionKeyRefreshRate_Type())
dot11Vap8021xSessionKeyRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11Vap8021xSessionKeyRefreshRate.setStatus(_A)
class _Dot11Vap8021xReauthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot11Vap8021xReauthenticationTimeout_Type.__name__=_C
_Dot11Vap8021xReauthenticationTimeout_Object=MibTableColumn
dot11Vap8021xReauthenticationTimeout=_Dot11Vap8021xReauthenticationTimeout_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1,5),_Dot11Vap8021xReauthenticationTimeout_Type())
dot11Vap8021xReauthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11Vap8021xReauthenticationTimeout.setStatus(_A)
class _Dot11VapAuthMACAuthenticationType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('local',1),('remote',2)))
_Dot11VapAuthMACAuthenticationType_Type.__name__=_C
_Dot11VapAuthMACAuthenticationType_Object=MibTableColumn
dot11VapAuthMACAuthenticationType=_Dot11VapAuthMACAuthenticationType_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1,6),_Dot11VapAuthMACAuthenticationType_Type())
dot11VapAuthMACAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11VapAuthMACAuthenticationType.setStatus(_A)
class _Dot11VapAuthMACAuthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot11VapAuthMACAuthenticationTimeout_Type.__name__=_C
_Dot11VapAuthMACAuthenticationTimeout_Object=MibTableColumn
dot11VapAuthMACAuthenticationTimeout=_Dot11VapAuthMACAuthenticationTimeout_Object((1,3,6,1,4,1,14823,2,3,2,7,6,1,7),_Dot11VapAuthMACAuthenticationTimeout_Type())
dot11VapAuthMACAuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11VapAuthMACAuthenticationTimeout.setStatus(_A)
_EnterpriseApAdmin_ObjectIdentity=ObjectIdentity
enterpriseApAdmin=_EnterpriseApAdmin_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,8))
class _EnterpriseApAdminUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,16))
_EnterpriseApAdminUser_Type.__name__=_I
_EnterpriseApAdminUser_Object=MibScalar
enterpriseApAdminUser=_EnterpriseApAdminUser_Object((1,3,6,1,4,1,14823,2,3,2,8,1),_EnterpriseApAdminUser_Type())
enterpriseApAdminUser.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApAdminUser.setStatus(_A)
class _EnterpriseApAdminPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EnterpriseApAdminPassword_Type.__name__=_I
_EnterpriseApAdminPassword_Object=MibScalar
enterpriseApAdminPassword=_EnterpriseApAdminPassword_Object((1,3,6,1,4,1,14823,2,3,2,8,2),_EnterpriseApAdminPassword_Type())
enterpriseApAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApAdminPassword.setStatus(_A)
_EnterpriseApVLAN_ObjectIdentity=ObjectIdentity
enterpriseApVLAN=_EnterpriseApVLAN_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,9))
_EnterpriseApVLANNativeId_Type=Integer32
_EnterpriseApVLANNativeId_Object=MibScalar
enterpriseApVLANNativeId=_EnterpriseApVLANNativeId_Object((1,3,6,1,4,1,14823,2,3,2,9,1),_EnterpriseApVLANNativeId_Type())
enterpriseApVLANNativeId.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApVLANNativeId.setStatus(_A)
class _EnterpriseApVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApVLANState_Type.__name__=_C
_EnterpriseApVLANState_Object=MibScalar
enterpriseApVLANState=_EnterpriseApVLANState_Object((1,3,6,1,4,1,14823,2,3,2,9,2),_EnterpriseApVLANState_Type())
enterpriseApVLANState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApVLANState.setStatus(_A)
_EnterpriseApNativeVlanTable_Object=MibTable
enterpriseApNativeVlanTable=_EnterpriseApNativeVlanTable_Object((1,3,6,1,4,1,14823,2,3,2,9,3))
if mibBuilder.loadTexts:enterpriseApNativeVlanTable.setStatus(_L)
_EnterpriseApNativeVlanEntry_Object=MibTableRow
enterpriseApNativeVlanEntry=_EnterpriseApNativeVlanEntry_Object((1,3,6,1,4,1,14823,2,3,2,9,3,1))
enterpriseApNativeVlanEntry.setIndexNames((0,_F,_g),(0,_F,_h))
if mibBuilder.loadTexts:enterpriseApNativeVlanEntry.setStatus(_L)
_NativeVlanIfIndex_Type=Integer32
_NativeVlanIfIndex_Object=MibTableColumn
nativeVlanIfIndex=_NativeVlanIfIndex_Object((1,3,6,1,4,1,14823,2,3,2,9,3,1,1),_NativeVlanIfIndex_Type())
nativeVlanIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nativeVlanIfIndex.setStatus(_L)
_NativeVlanSsidNumber_Type=Integer32
_NativeVlanSsidNumber_Object=MibTableColumn
nativeVlanSsidNumber=_NativeVlanSsidNumber_Object((1,3,6,1,4,1,14823,2,3,2,9,3,1,2),_NativeVlanSsidNumber_Type())
nativeVlanSsidNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:nativeVlanSsidNumber.setStatus(_L)
_NativeVlanVlanId_Type=Integer32
_NativeVlanVlanId_Object=MibTableColumn
nativeVlanVlanId=_NativeVlanVlanId_Object((1,3,6,1,4,1,14823,2,3,2,9,3,1,3),_NativeVlanVlanId_Type())
nativeVlanVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:nativeVlanVlanId.setStatus(_L)
_EnterpriseApFilterControl_ObjectIdentity=ObjectIdentity
enterpriseApFilterControl=_EnterpriseApFilterControl_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,10))
class _EnterpriseApFilterControlInterClientSTAsCommun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('PreventIntraVAPClient',2),('PreventInterAndIntraVAPClient',3)))
_EnterpriseApFilterControlInterClientSTAsCommun_Type.__name__=_C
_EnterpriseApFilterControlInterClientSTAsCommun_Object=MibScalar
enterpriseApFilterControlInterClientSTAsCommun=_EnterpriseApFilterControlInterClientSTAsCommun_Object((1,3,6,1,4,1,14823,2,3,2,10,1),_EnterpriseApFilterControlInterClientSTAsCommun_Type())
enterpriseApFilterControlInterClientSTAsCommun.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApFilterControlInterClientSTAsCommun.setStatus(_A)
class _EnterpriseApFilterControlAPManage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApFilterControlAPManage_Type.__name__=_C
_EnterpriseApFilterControlAPManage_Object=MibScalar
enterpriseApFilterControlAPManage=_EnterpriseApFilterControlAPManage_Object((1,3,6,1,4,1,14823,2,3,2,10,2),_EnterpriseApFilterControlAPManage_Type())
enterpriseApFilterControlAPManage.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApFilterControlAPManage.setStatus(_A)
class _EnterpriseApFilterControlEthernet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApFilterControlEthernet_Type.__name__=_C
_EnterpriseApFilterControlEthernet_Object=MibScalar
enterpriseApFilterControlEthernet=_EnterpriseApFilterControlEthernet_Object((1,3,6,1,4,1,14823,2,3,2,10,3),_EnterpriseApFilterControlEthernet_Type())
enterpriseApFilterControlEthernet.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApFilterControlEthernet.setStatus(_A)
_EnterpriseApFilterProtocolTable_Object=MibTable
enterpriseApFilterProtocolTable=_EnterpriseApFilterProtocolTable_Object((1,3,6,1,4,1,14823,2,3,2,10,4))
if mibBuilder.loadTexts:enterpriseApFilterProtocolTable.setStatus(_A)
_EnterpriseApFilterProtocolEntry_Object=MibTableRow
enterpriseApFilterProtocolEntry=_EnterpriseApFilterProtocolEntry_Object((1,3,6,1,4,1,14823,2,3,2,10,4,1))
enterpriseApFilterProtocolEntry.setIndexNames((0,_F,_i))
if mibBuilder.loadTexts:enterpriseApFilterProtocolEntry.setStatus(_A)
_EnterpriseApFilterProtocolIndex_Type=Integer32
_EnterpriseApFilterProtocolIndex_Object=MibTableColumn
enterpriseApFilterProtocolIndex=_EnterpriseApFilterProtocolIndex_Object((1,3,6,1,4,1,14823,2,3,2,10,4,1,1),_EnterpriseApFilterProtocolIndex_Type())
enterpriseApFilterProtocolIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApFilterProtocolIndex.setStatus(_A)
_EnterpriseApFilterProtocolName_Type=DisplayString
_EnterpriseApFilterProtocolName_Object=MibTableColumn
enterpriseApFilterProtocolName=_EnterpriseApFilterProtocolName_Object((1,3,6,1,4,1,14823,2,3,2,10,4,1,2),_EnterpriseApFilterProtocolName_Type())
enterpriseApFilterProtocolName.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApFilterProtocolName.setStatus(_A)
_EnterpriseApFilterProtocolISODesignator_Type=DisplayString
_EnterpriseApFilterProtocolISODesignator_Object=MibTableColumn
enterpriseApFilterProtocolISODesignator=_EnterpriseApFilterProtocolISODesignator_Object((1,3,6,1,4,1,14823,2,3,2,10,4,1,3),_EnterpriseApFilterProtocolISODesignator_Type())
enterpriseApFilterProtocolISODesignator.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApFilterProtocolISODesignator.setStatus(_A)
class _EnterpriseApFilterProtocolState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApFilterProtocolState_Type.__name__=_C
_EnterpriseApFilterProtocolState_Object=MibTableColumn
enterpriseApFilterProtocolState=_EnterpriseApFilterProtocolState_Object((1,3,6,1,4,1,14823,2,3,2,10,4,1,4),_EnterpriseApFilterProtocolState_Type())
enterpriseApFilterProtocolState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApFilterProtocolState.setStatus(_A)
_EnterpriseApFilterUplinkPortMACAddrFilter_ObjectIdentity=ObjectIdentity
enterpriseApFilterUplinkPortMACAddrFilter=_EnterpriseApFilterUplinkPortMACAddrFilter_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,10,5))
class _UplinkPortMACAddrFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_D,2)))
_UplinkPortMACAddrFilterStatus_Type.__name__=_C
_UplinkPortMACAddrFilterStatus_Object=MibScalar
uplinkPortMACAddrFilterStatus=_UplinkPortMACAddrFilterStatus_Object((1,3,6,1,4,1,14823,2,3,2,10,5,1),_UplinkPortMACAddrFilterStatus_Type())
uplinkPortMACAddrFilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:uplinkPortMACAddrFilterStatus.setStatus(_A)
_UplinkPortMACAddrFilterAddMac_Type=MacAddress
_UplinkPortMACAddrFilterAddMac_Object=MibScalar
uplinkPortMACAddrFilterAddMac=_UplinkPortMACAddrFilterAddMac_Object((1,3,6,1,4,1,14823,2,3,2,10,5,2),_UplinkPortMACAddrFilterAddMac_Type())
uplinkPortMACAddrFilterAddMac.setMaxAccess(_B)
if mibBuilder.loadTexts:uplinkPortMACAddrFilterAddMac.setStatus(_A)
_UplinkPortMACAddrFilteringTable_Object=MibTable
uplinkPortMACAddrFilteringTable=_UplinkPortMACAddrFilteringTable_Object((1,3,6,1,4,1,14823,2,3,2,10,5,3))
if mibBuilder.loadTexts:uplinkPortMACAddrFilteringTable.setStatus(_A)
_UplinkPortMACAddrFilteringEntry_Object=MibTableRow
uplinkPortMACAddrFilteringEntry=_UplinkPortMACAddrFilteringEntry_Object((1,3,6,1,4,1,14823,2,3,2,10,5,3,1))
uplinkPortMACAddrFilteringEntry.setIndexNames((0,_F,_j))
if mibBuilder.loadTexts:uplinkPortMACAddrFilteringEntry.setStatus(_A)
_UplinkPortMacAddrIndex_Type=Integer32
_UplinkPortMacAddrIndex_Object=MibTableColumn
uplinkPortMacAddrIndex=_UplinkPortMacAddrIndex_Object((1,3,6,1,4,1,14823,2,3,2,10,5,3,1,1),_UplinkPortMacAddrIndex_Type())
uplinkPortMacAddrIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:uplinkPortMacAddrIndex.setStatus(_A)
_UplinkPortMACAddr_Type=MacAddress
_UplinkPortMACAddr_Object=MibTableColumn
uplinkPortMACAddr=_UplinkPortMACAddr_Object((1,3,6,1,4,1,14823,2,3,2,10,5,3,1,2),_UplinkPortMACAddr_Type())
uplinkPortMACAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:uplinkPortMACAddr.setStatus(_A)
class _DeleteMacAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('Delete',1),('Nothing',2)))
_DeleteMacAddr_Type.__name__=_C
_DeleteMacAddr_Object=MibTableColumn
deleteMacAddr=_DeleteMacAddr_Object((1,3,6,1,4,1,14823,2,3,2,10,5,3,1,3),_DeleteMacAddr_Type())
deleteMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:deleteMacAddr.setStatus(_A)
_EnterpriseApSNTP_ObjectIdentity=ObjectIdentity
enterpriseApSNTP=_EnterpriseApSNTP_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,11))
class _EnterpriseApSNTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSNTPState_Type.__name__=_C
_EnterpriseApSNTPState_Object=MibScalar
enterpriseApSNTPState=_EnterpriseApSNTPState_Object((1,3,6,1,4,1,14823,2,3,2,11,1),_EnterpriseApSNTPState_Type())
enterpriseApSNTPState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPState.setStatus(_A)
_EnterpriseApSNTPPrimaryServer_Type=IpAddress
_EnterpriseApSNTPPrimaryServer_Object=MibScalar
enterpriseApSNTPPrimaryServer=_EnterpriseApSNTPPrimaryServer_Object((1,3,6,1,4,1,14823,2,3,2,11,2),_EnterpriseApSNTPPrimaryServer_Type())
enterpriseApSNTPPrimaryServer.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPPrimaryServer.setStatus(_A)
_EnterpriseApSNTPSecondaryServer_Type=IpAddress
_EnterpriseApSNTPSecondaryServer_Object=MibScalar
enterpriseApSNTPSecondaryServer=_EnterpriseApSNTPSecondaryServer_Object((1,3,6,1,4,1,14823,2,3,2,11,3),_EnterpriseApSNTPSecondaryServer_Type())
enterpriseApSNTPSecondaryServer.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPSecondaryServer.setStatus(_A)
class _EnterpriseApSNTPTimezone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53)));namedValues=NamedValues(*(('enewetakKwajalein',0),('midwayIsland',1),('hawaii',2),('alaska',3),('pacific',4),('arizona',5),('mountain',6),('central',7),('mexicoCity',8),('saskatchewan',9),('bogota',10),('eastern',11),('indiana',12),('atlantic',13),('caracas',14),('santiago',15),('newfoundland',16),('brasilia',17),('buenos',18),('midAtlantic',19),('azores',20),('casablanca',21),('greenwichMeanTimeDublin',22),('greenwichMeanTimeLisbon',23),('amsterdam',24),('stockhoim',25),('bratislava',26),('prague',27),('paris',28),('sofija',29),('athens',30),('bucharest',31),('cairo',32),('harare',33),('helsinki',34),('israel',35),('baghdad',36),('moscow',37),('tehran',38),('abuDhabi',39),('vogograd',40),('islamabad',41),('almaty',42),('bangkok',43),('beijing',44),('taipei',45),('tokyo',46),('brisbane',47),('canberra',48),('guam',49),('hobart',50),('magadan',51),('fiji',52),('wellington',53)))
_EnterpriseApSNTPTimezone_Type.__name__=_C
_EnterpriseApSNTPTimezone_Object=MibScalar
enterpriseApSNTPTimezone=_EnterpriseApSNTPTimezone_Object((1,3,6,1,4,1,14823,2,3,2,11,4),_EnterpriseApSNTPTimezone_Type())
enterpriseApSNTPTimezone.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPTimezone.setStatus(_A)
class _EnterpriseApSNTPDST_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSNTPDST_Type.__name__=_C
_EnterpriseApSNTPDST_Object=MibScalar
enterpriseApSNTPDST=_EnterpriseApSNTPDST_Object((1,3,6,1,4,1,14823,2,3,2,11,5),_EnterpriseApSNTPDST_Type())
enterpriseApSNTPDST.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPDST.setStatus(_A)
class _EnterpriseApSNTPDSTStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_EnterpriseApSNTPDSTStartMonth_Type.__name__=_C
_EnterpriseApSNTPDSTStartMonth_Object=MibScalar
enterpriseApSNTPDSTStartMonth=_EnterpriseApSNTPDSTStartMonth_Object((1,3,6,1,4,1,14823,2,3,2,11,6),_EnterpriseApSNTPDSTStartMonth_Type())
enterpriseApSNTPDSTStartMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPDSTStartMonth.setStatus(_A)
class _EnterpriseApSNTPDSTStartDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_EnterpriseApSNTPDSTStartDay_Type.__name__=_C
_EnterpriseApSNTPDSTStartDay_Object=MibScalar
enterpriseApSNTPDSTStartDay=_EnterpriseApSNTPDSTStartDay_Object((1,3,6,1,4,1,14823,2,3,2,11,7),_EnterpriseApSNTPDSTStartDay_Type())
enterpriseApSNTPDSTStartDay.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPDSTStartDay.setStatus(_A)
class _EnterpriseApSNTPDSTEndMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_EnterpriseApSNTPDSTEndMonth_Type.__name__=_C
_EnterpriseApSNTPDSTEndMonth_Object=MibScalar
enterpriseApSNTPDSTEndMonth=_EnterpriseApSNTPDSTEndMonth_Object((1,3,6,1,4,1,14823,2,3,2,11,8),_EnterpriseApSNTPDSTEndMonth_Type())
enterpriseApSNTPDSTEndMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPDSTEndMonth.setStatus(_A)
class _EnterpriseApSNTPDSTEndDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_EnterpriseApSNTPDSTEndDay_Type.__name__=_C
_EnterpriseApSNTPDSTEndDay_Object=MibScalar
enterpriseApSNTPDSTEndDay=_EnterpriseApSNTPDSTEndDay_Object((1,3,6,1,4,1,14823,2,3,2,11,9),_EnterpriseApSNTPDSTEndDay_Type())
enterpriseApSNTPDSTEndDay.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNTPDSTEndDay.setStatus(_A)
_SntpNotificationTree_ObjectIdentity=ObjectIdentity
sntpNotificationTree=_SntpNotificationTree_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,11,10))
_SntpNotificationObjects_ObjectIdentity=ObjectIdentity
sntpNotificationObjects=_SntpNotificationObjects_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,11,10,1))
_SntpNotifications_ObjectIdentity=ObjectIdentity
sntpNotifications=_SntpNotifications_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,11,10,2))
_EnterpriseApDNS_ObjectIdentity=ObjectIdentity
enterpriseApDNS=_EnterpriseApDNS_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,12))
_EnterpriseApDNSPrimaryServer_Type=IpAddress
_EnterpriseApDNSPrimaryServer_Object=MibScalar
enterpriseApDNSPrimaryServer=_EnterpriseApDNSPrimaryServer_Object((1,3,6,1,4,1,14823,2,3,2,12,1),_EnterpriseApDNSPrimaryServer_Type())
enterpriseApDNSPrimaryServer.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApDNSPrimaryServer.setStatus(_A)
_EnterpriseApDNSSecondaryServer_Type=IpAddress
_EnterpriseApDNSSecondaryServer_Object=MibScalar
enterpriseApDNSSecondaryServer=_EnterpriseApDNSSecondaryServer_Object((1,3,6,1,4,1,14823,2,3,2,12,2),_EnterpriseApDNSSecondaryServer_Type())
enterpriseApDNSSecondaryServer.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApDNSSecondaryServer.setStatus(_A)
_EnterpriseApSyslog_ObjectIdentity=ObjectIdentity
enterpriseApSyslog=_EnterpriseApSyslog_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,13))
class _EnterpriseApSyslogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSyslogState_Type.__name__=_C
_EnterpriseApSyslogState_Object=MibScalar
enterpriseApSyslogState=_EnterpriseApSyslogState_Object((1,3,6,1,4,1,14823,2,3,2,13,1),_EnterpriseApSyslogState_Type())
enterpriseApSyslogState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSyslogState.setStatus(_A)
class _EnterpriseApSyslogConsoleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSyslogConsoleState_Type.__name__=_C
_EnterpriseApSyslogConsoleState_Object=MibScalar
enterpriseApSyslogConsoleState=_EnterpriseApSyslogConsoleState_Object((1,3,6,1,4,1,14823,2,3,2,13,2),_EnterpriseApSyslogConsoleState_Type())
enterpriseApSyslogConsoleState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSyslogConsoleState.setStatus(_A)
class _EnterpriseApSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),(_Q,3),('warning',4),('notice',5),('info',6),('debug',7)))
_EnterpriseApSyslogLevel_Type.__name__=_C
_EnterpriseApSyslogLevel_Object=MibScalar
enterpriseApSyslogLevel=_EnterpriseApSyslogLevel_Object((1,3,6,1,4,1,14823,2,3,2,13,3),_EnterpriseApSyslogLevel_Type())
enterpriseApSyslogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSyslogLevel.setStatus(_A)
_EnterpriseApSyslogServerTable_Object=MibTable
enterpriseApSyslogServerTable=_EnterpriseApSyslogServerTable_Object((1,3,6,1,4,1,14823,2,3,2,13,4))
if mibBuilder.loadTexts:enterpriseApSyslogServerTable.setStatus(_A)
_EnterpriseApSyslogServerEntry_Object=MibTableRow
enterpriseApSyslogServerEntry=_EnterpriseApSyslogServerEntry_Object((1,3,6,1,4,1,14823,2,3,2,13,4,1))
enterpriseApSyslogServerEntry.setIndexNames((0,_F,_k))
if mibBuilder.loadTexts:enterpriseApSyslogServerEntry.setStatus(_A)
_EnterpriseApSyslogServerIndex_Type=Integer32
_EnterpriseApSyslogServerIndex_Object=MibTableColumn
enterpriseApSyslogServerIndex=_EnterpriseApSyslogServerIndex_Object((1,3,6,1,4,1,14823,2,3,2,13,4,1,1),_EnterpriseApSyslogServerIndex_Type())
enterpriseApSyslogServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApSyslogServerIndex.setStatus(_A)
class _EnterpriseApSyslogServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSyslogServerState_Type.__name__=_C
_EnterpriseApSyslogServerState_Object=MibTableColumn
enterpriseApSyslogServerState=_EnterpriseApSyslogServerState_Object((1,3,6,1,4,1,14823,2,3,2,13,4,1,2),_EnterpriseApSyslogServerState_Type())
enterpriseApSyslogServerState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSyslogServerState.setStatus(_A)
_EnterpriseApSyslogServerIPAddress_Type=IpAddress
_EnterpriseApSyslogServerIPAddress_Object=MibTableColumn
enterpriseApSyslogServerIPAddress=_EnterpriseApSyslogServerIPAddress_Object((1,3,6,1,4,1,14823,2,3,2,13,4,1,3),_EnterpriseApSyslogServerIPAddress_Type())
enterpriseApSyslogServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSyslogServerIPAddress.setStatus(_A)
class _EnterpriseApSyslogServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_EnterpriseApSyslogServerPort_Type.__name__=_C
_EnterpriseApSyslogServerPort_Object=MibTableColumn
enterpriseApSyslogServerPort=_EnterpriseApSyslogServerPort_Object((1,3,6,1,4,1,14823,2,3,2,13,4,1,4),_EnterpriseApSyslogServerPort_Type())
enterpriseApSyslogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSyslogServerPort.setStatus(_A)
_EnterpriseApSecurity_ObjectIdentity=ObjectIdentity
enterpriseApSecurity=_EnterpriseApSecurity_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,14))
_EnterpriseApSecurityTable_Object=MibTable
enterpriseApSecurityTable=_EnterpriseApSecurityTable_Object((1,3,6,1,4,1,14823,2,3,2,14,1))
if mibBuilder.loadTexts:enterpriseApSecurityTable.setStatus(_A)
_EnterpriseApSecurityEntry_Object=MibTableRow
enterpriseApSecurityEntry=_EnterpriseApSecurityEntry_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1))
enterpriseApSecurityEntry.setIndexNames((0,_F,_l))
if mibBuilder.loadTexts:enterpriseApSecurityEntry.setStatus(_A)
_EnterpriseApSecurityIndex_Type=Integer32
_EnterpriseApSecurityIndex_Object=MibTableColumn
enterpriseApSecurityIndex=_EnterpriseApSecurityIndex_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,1),_EnterpriseApSecurityIndex_Type())
enterpriseApSecurityIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApSecurityIndex.setStatus(_A)
class _EnterpriseApSecurityAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('opensystem',0),('sharedkey',1),('wpa',2),('wpapsk',3),('wpawpa2mixed',4),('wpawpa2pskmixed',5),('wpa2',6),('wpa2psk',7)))
_EnterpriseApSecurityAuthType_Type.__name__=_C
_EnterpriseApSecurityAuthType_Object=MibTableColumn
enterpriseApSecurityAuthType=_EnterpriseApSecurityAuthType_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,2),_EnterpriseApSecurityAuthType_Type())
enterpriseApSecurityAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityAuthType.setStatus(_A)
class _EnterpriseApSecuritySharedKeyLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('sixtyFour',1),('oneHundredTwentyEight',2),('oneHundredFiftyTwo',3)))
_EnterpriseApSecuritySharedKeyLen_Type.__name__=_C
_EnterpriseApSecuritySharedKeyLen_Object=MibTableColumn
enterpriseApSecuritySharedKeyLen=_EnterpriseApSecuritySharedKeyLen_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,3),_EnterpriseApSecuritySharedKeyLen_Type())
enterpriseApSecuritySharedKeyLen.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSecuritySharedKeyLen.setStatus(_A)
class _EnterpriseApSecurityWPAMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),(_N,1),(_D,2)))
_EnterpriseApSecurityWPAMode_Type.__name__=_C
_EnterpriseApSecurityWPAMode_Object=MibTableColumn
enterpriseApSecurityWPAMode=_EnterpriseApSecurityWPAMode_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,4),_EnterpriseApSecurityWPAMode_Type())
enterpriseApSecurityWPAMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAMode.setStatus(_A)
class _EnterpriseApSecurityWPAKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dot1x',0),('presharedkey',1)))
_EnterpriseApSecurityWPAKeyType_Type.__name__=_C
_EnterpriseApSecurityWPAKeyType_Object=MibTableColumn
enterpriseApSecurityWPAKeyType=_EnterpriseApSecurityWPAKeyType_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,5),_EnterpriseApSecurityWPAKeyType_Type())
enterpriseApSecurityWPAKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAKeyType.setStatus(_A)
class _EnterpriseApSecurityWPACipher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('wep',0),('tkip',1),('aes',2)))
_EnterpriseApSecurityWPACipher_Type.__name__=_C
_EnterpriseApSecurityWPACipher_Object=MibTableColumn
enterpriseApSecurityWPACipher=_EnterpriseApSecurityWPACipher_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,6),_EnterpriseApSecurityWPACipher_Type())
enterpriseApSecurityWPACipher.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPACipher.setStatus(_K)
class _EnterpriseApSecurityWPAPSKType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hex',0),(_m,1)))
_EnterpriseApSecurityWPAPSKType_Type.__name__=_C
_EnterpriseApSecurityWPAPSKType_Object=MibTableColumn
enterpriseApSecurityWPAPSKType=_EnterpriseApSecurityWPAPSKType_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,7),_EnterpriseApSecurityWPAPSKType_Type())
enterpriseApSecurityWPAPSKType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAPSKType.setStatus(_A)
class _EnterpriseApSecurityWPAPSK_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EnterpriseApSecurityWPAPSK_Type.__name__=_I
_EnterpriseApSecurityWPAPSK_Object=MibTableColumn
enterpriseApSecurityWPAPSK=_EnterpriseApSecurityWPAPSK_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,8),_EnterpriseApSecurityWPAPSK_Type())
enterpriseApSecurityWPAPSK.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAPSK.setStatus(_A)
class _EnterpriseApSecurityWEPKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hexadecimal',0),(_m,1)))
_EnterpriseApSecurityWEPKeyType_Type.__name__=_C
_EnterpriseApSecurityWEPKeyType_Object=MibTableColumn
enterpriseApSecurityWEPKeyType=_EnterpriseApSecurityWEPKeyType_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,9),_EnterpriseApSecurityWEPKeyType_Type())
enterpriseApSecurityWEPKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWEPKeyType.setStatus(_A)
_EnterpriseApSecurityWEPEnabled_Type=TruthValue
_EnterpriseApSecurityWEPEnabled_Object=MibTableColumn
enterpriseApSecurityWEPEnabled=_EnterpriseApSecurityWEPEnabled_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,10),_EnterpriseApSecurityWEPEnabled_Type())
enterpriseApSecurityWEPEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWEPEnabled.setStatus(_A)
class _EnterpriseApSecurityWPACipherSuite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('aes-ccmp',0),('tkip',1),('wep',2)))
_EnterpriseApSecurityWPACipherSuite_Type.__name__=_C
_EnterpriseApSecurityWPACipherSuite_Object=MibTableColumn
enterpriseApSecurityWPACipherSuite=_EnterpriseApSecurityWPACipherSuite_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,11),_EnterpriseApSecurityWPACipherSuite_Type())
enterpriseApSecurityWPACipherSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPACipherSuite.setStatus(_A)
class _EnterpriseApSecurityWPAPreAuthentication_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSecurityWPAPreAuthentication_Type.__name__=_C
_EnterpriseApSecurityWPAPreAuthentication_Object=MibTableColumn
enterpriseApSecurityWPAPreAuthentication=_EnterpriseApSecurityWPAPreAuthentication_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,12),_EnterpriseApSecurityWPAPreAuthentication_Type())
enterpriseApSecurityWPAPreAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAPreAuthentication.setStatus(_A)
class _EnterpriseApSecurityWPAPmksaLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_EnterpriseApSecurityWPAPmksaLifetime_Type.__name__=_C
_EnterpriseApSecurityWPAPmksaLifetime_Object=MibTableColumn
enterpriseApSecurityWPAPmksaLifetime=_EnterpriseApSecurityWPAPmksaLifetime_Object((1,3,6,1,4,1,14823,2,3,2,14,1,1,13),_EnterpriseApSecurityWPAPmksaLifetime_Type())
enterpriseApSecurityWPAPmksaLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAPmksaLifetime.setStatus(_A)
_EnterpriseApSsh_ObjectIdentity=ObjectIdentity
enterpriseApSsh=_EnterpriseApSsh_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,14,2))
_EnterpriseApSshServerEnabled_Type=TruthValue
_EnterpriseApSshServerEnabled_Object=MibScalar
enterpriseApSshServerEnabled=_EnterpriseApSshServerEnabled_Object((1,3,6,1,4,1,14823,2,3,2,14,2,1),_EnterpriseApSshServerEnabled_Type())
enterpriseApSshServerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSshServerEnabled.setStatus(_L)
class _EnterpriseApSshServerPort_Type(Integer32):defaultValue=22
_EnterpriseApSshServerPort_Type.__name__=_C
_EnterpriseApSshServerPort_Object=MibScalar
enterpriseApSshServerPort=_EnterpriseApSshServerPort_Object((1,3,6,1,4,1,14823,2,3,2,14,2,2),_EnterpriseApSshServerPort_Type())
enterpriseApSshServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSshServerPort.setStatus(_L)
_EnterpriseApSshTelnetServerEnabled_Type=TruthValue
_EnterpriseApSshTelnetServerEnabled_Object=MibScalar
enterpriseApSshTelnetServerEnabled=_EnterpriseApSshTelnetServerEnabled_Object((1,3,6,1,4,1,14823,2,3,2,14,2,3),_EnterpriseApSshTelnetServerEnabled_Type())
enterpriseApSshTelnetServerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSshTelnetServerEnabled.setStatus(_L)
_EnterpriseApRadio_ObjectIdentity=ObjectIdentity
enterpriseApRadio=_EnterpriseApRadio_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,15))
_EnterpriseApRadioTable_Object=MibTable
enterpriseApRadioTable=_EnterpriseApRadioTable_Object((1,3,6,1,4,1,14823,2,3,2,15,1))
if mibBuilder.loadTexts:enterpriseApRadioTable.setStatus(_A)
_EnterpriseApRadioEntry_Object=MibTableRow
enterpriseApRadioEntry=_EnterpriseApRadioEntry_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1))
enterpriseApRadioEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:enterpriseApRadioEntry.setStatus(_A)
_EnterpriseApRadioIndex_Type=Integer32
_EnterpriseApRadioIndex_Object=MibTableColumn
enterpriseApRadioIndex=_EnterpriseApRadioIndex_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,1),_EnterpriseApRadioIndex_Type())
enterpriseApRadioIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApRadioIndex.setStatus(_A)
class _EnterpriseApRadioState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioState_Type.__name__=_C
_EnterpriseApRadioState_Object=MibTableColumn
enterpriseApRadioState=_EnterpriseApRadioState_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,2),_EnterpriseApRadioState_Type())
enterpriseApRadioState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioState.setStatus(_K)
class _EnterpriseApRadioAutoChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioAutoChannel_Type.__name__=_C
_EnterpriseApRadioAutoChannel_Object=MibTableColumn
enterpriseApRadioAutoChannel=_EnterpriseApRadioAutoChannel_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,3),_EnterpriseApRadioAutoChannel_Type())
enterpriseApRadioAutoChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioAutoChannel.setStatus(_A)
class _EnterpriseApRadioTransmitPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('min',0),('eighth',1),('quarter',2),('half',3),('full',4)))
_EnterpriseApRadioTransmitPower_Type.__name__=_C
_EnterpriseApRadioTransmitPower_Object=MibTableColumn
enterpriseApRadioTransmitPower=_EnterpriseApRadioTransmitPower_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,4),_EnterpriseApRadioTransmitPower_Type())
enterpriseApRadioTransmitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioTransmitPower.setStatus(_A)
class _EnterpriseApRadioClosedSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioClosedSystem_Type.__name__=_C
_EnterpriseApRadioClosedSystem_Object=MibTableColumn
enterpriseApRadioClosedSystem=_EnterpriseApRadioClosedSystem_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,5),_EnterpriseApRadioClosedSystem_Type())
enterpriseApRadioClosedSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioClosedSystem.setStatus(_K)
class _EnterpriseApRadioMaxAssoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_EnterpriseApRadioMaxAssoc_Type.__name__=_C
_EnterpriseApRadioMaxAssoc_Object=MibTableColumn
enterpriseApRadioMaxAssoc=_EnterpriseApRadioMaxAssoc_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,6),_EnterpriseApRadioMaxAssoc_Type())
enterpriseApRadioMaxAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioMaxAssoc.setStatus(_K)
class _EnterpriseApRadioTransmitKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EnterpriseApRadioTransmitKey_Type.__name__=_C
_EnterpriseApRadioTransmitKey_Object=MibTableColumn
enterpriseApRadioTransmitKey=_EnterpriseApRadioTransmitKey_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,7),_EnterpriseApRadioTransmitKey_Type())
enterpriseApRadioTransmitKey.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioTransmitKey.setStatus(_K)
class _EnterpriseApRadioTurboMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('static-turbo',2),('dynamic-turbo',3)))
_EnterpriseApRadioTurboMode_Type.__name__=_C
_EnterpriseApRadioTurboMode_Object=MibTableColumn
enterpriseApRadioTurboMode=_EnterpriseApRadioTurboMode_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,8),_EnterpriseApRadioTurboMode_Type())
enterpriseApRadioTurboMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioTurboMode.setStatus(_A)
class _EnterpriseApRadioDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EnterpriseApRadioDescription_Type.__name__=_I
_EnterpriseApRadioDescription_Object=MibTableColumn
enterpriseApRadioDescription=_EnterpriseApRadioDescription_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,9),_EnterpriseApRadioDescription_Type())
enterpriseApRadioDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioDescription.setStatus(_K)
class _EnterpriseApRadioDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,9,11,12,18,24,36,48,54,255)));namedValues=NamedValues(*(('oneMbps',1),('twoMbps',2),('fiveAndHalfMbps',5),('sixMbps',6),('nineMbps',9),('elevenMbps',11),('twelveMbps',12),('eighteenMbps',18),('twentyFourMbps',24),('thirtySixMbps',36),('fourtyEightMbps',48),('fiftyFourMbps',54),('auto',255)))
_EnterpriseApRadioDataRate_Type.__name__=_C
_EnterpriseApRadioDataRate_Object=MibTableColumn
enterpriseApRadioDataRate=_EnterpriseApRadioDataRate_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,10),_EnterpriseApRadioDataRate_Type())
enterpriseApRadioDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioDataRate.setStatus(_A)
class _EnterpriseApRadioGMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bOnly',1),('gOnly',2),('bg',3)))
_EnterpriseApRadioGMode_Type.__name__=_C
_EnterpriseApRadioGMode_Object=MibTableColumn
enterpriseApRadioGMode=_EnterpriseApRadioGMode_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,11),_EnterpriseApRadioGMode_Type())
enterpriseApRadioGMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioGMode.setStatus(_A)
class _EnterpriseApRadioAntennaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('external',2)))
_EnterpriseApRadioAntennaMode_Type.__name__=_C
_EnterpriseApRadioAntennaMode_Object=MibTableColumn
enterpriseApRadioAntennaMode=_EnterpriseApRadioAntennaMode_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,12),_EnterpriseApRadioAntennaMode_Type())
enterpriseApRadioAntennaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioAntennaMode.setStatus(_L)
_EnterpriseApRadioAntennaId_Type=DisplayString
_EnterpriseApRadioAntennaId_Object=MibTableColumn
enterpriseApRadioAntennaId=_EnterpriseApRadioAntennaId_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,13),_EnterpriseApRadioAntennaId_Type())
enterpriseApRadioAntennaId.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApRadioAntennaId.setStatus(_A)
class _EnterpriseApRadioAntennaControlMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('Diversity',1),('Left',2),('Right',3)))
_EnterpriseApRadioAntennaControlMethod_Type.__name__=_C
_EnterpriseApRadioAntennaControlMethod_Object=MibTableColumn
enterpriseApRadioAntennaControlMethod=_EnterpriseApRadioAntennaControlMethod_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,14),_EnterpriseApRadioAntennaControlMethod_Type())
enterpriseApRadioAntennaControlMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioAntennaControlMethod.setStatus(_A)
class _EnterpriseApRadioAntennaLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('Indoor',1),('Outdoor',2)))
_EnterpriseApRadioAntennaLocation_Type.__name__=_C
_EnterpriseApRadioAntennaLocation_Object=MibTableColumn
enterpriseApRadioAntennaLocation=_EnterpriseApRadioAntennaLocation_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,15),_EnterpriseApRadioAntennaLocation_Type())
enterpriseApRadioAntennaLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioAntennaLocation.setStatus(_A)
class _EnterpriseApRadioRogueApDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioRogueApDetection_Type.__name__=_C
_EnterpriseApRadioRogueApDetection_Object=MibTableColumn
enterpriseApRadioRogueApDetection=_EnterpriseApRadioRogueApDetection_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,16),_EnterpriseApRadioRogueApDetection_Type())
enterpriseApRadioRogueApDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioRogueApDetection.setStatus(_A)
class _EnterpriseApRadioRogueApScanInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_EnterpriseApRadioRogueApScanInterval_Type.__name__=_C
_EnterpriseApRadioRogueApScanInterval_Object=MibTableColumn
enterpriseApRadioRogueApScanInterval=_EnterpriseApRadioRogueApScanInterval_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,17),_EnterpriseApRadioRogueApScanInterval_Type())
enterpriseApRadioRogueApScanInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioRogueApScanInterval.setStatus(_A)
class _EnterpriseApRadioRogueApScanDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_EnterpriseApRadioRogueApScanDuration_Type.__name__=_C
_EnterpriseApRadioRogueApScanDuration_Object=MibTableColumn
enterpriseApRadioRogueApScanDuration=_EnterpriseApRadioRogueApScanDuration_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,18),_EnterpriseApRadioRogueApScanDuration_Type())
enterpriseApRadioRogueApScanDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioRogueApScanDuration.setStatus(_A)
class _EnterpriseApRadioRogueApScanNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioRogueApScanNow_Type.__name__=_C
_EnterpriseApRadioRogueApScanNow_Object=MibTableColumn
enterpriseApRadioRogueApScanNow=_EnterpriseApRadioRogueApScanNow_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,19),_EnterpriseApRadioRogueApScanNow_Type())
enterpriseApRadioRogueApScanNow.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioRogueApScanNow.setStatus(_A)
class _EnterpriseApRadioMICMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('software',1),('hardware',2)))
_EnterpriseApRadioMICMode_Type.__name__=_C
_EnterpriseApRadioMICMode_Object=MibTableColumn
enterpriseApRadioMICMode=_EnterpriseApRadioMICMode_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,21),_EnterpriseApRadioMICMode_Type())
enterpriseApRadioMICMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioMICMode.setStatus(_A)
class _EnterpriseApRadioSuperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioSuperMode_Type.__name__=_C
_EnterpriseApRadioSuperMode_Object=MibTableColumn
enterpriseApRadioSuperMode=_EnterpriseApRadioSuperMode_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,22),_EnterpriseApRadioSuperMode_Type())
enterpriseApRadioSuperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioSuperMode.setStatus(_A)
class _EnterpriseApRadioBeaconInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1000))
_EnterpriseApRadioBeaconInterval_Type.__name__=_C
_EnterpriseApRadioBeaconInterval_Object=MibTableColumn
enterpriseApRadioBeaconInterval=_EnterpriseApRadioBeaconInterval_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,23),_EnterpriseApRadioBeaconInterval_Type())
enterpriseApRadioBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioBeaconInterval.setStatus(_A)
_EnterpriseApRadioDataBeaconRate_Type=Integer32
_EnterpriseApRadioDataBeaconRate_Object=MibTableColumn
enterpriseApRadioDataBeaconRate=_EnterpriseApRadioDataBeaconRate_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,24),_EnterpriseApRadioDataBeaconRate_Type())
enterpriseApRadioDataBeaconRate.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioDataBeaconRate.setStatus(_A)
_EnterpriseApRadioChannel_Type=Integer32
_EnterpriseApRadioChannel_Object=MibTableColumn
enterpriseApRadioChannel=_EnterpriseApRadioChannel_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,25),_EnterpriseApRadioChannel_Type())
enterpriseApRadioChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioChannel.setStatus(_A)
class _EnterpriseApRadioFragmentLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_EnterpriseApRadioFragmentLength_Type.__name__=_C
_EnterpriseApRadioFragmentLength_Object=MibTableColumn
enterpriseApRadioFragmentLength=_EnterpriseApRadioFragmentLength_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,26),_EnterpriseApRadioFragmentLength_Type())
enterpriseApRadioFragmentLength.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioFragmentLength.setStatus(_A)
class _EnterpriseApRadioRTSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_EnterpriseApRadioRTSThreshold_Type.__name__=_C
_EnterpriseApRadioRTSThreshold_Object=MibTableColumn
enterpriseApRadioRTSThreshold=_EnterpriseApRadioRTSThreshold_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,27),_EnterpriseApRadioRTSThreshold_Type())
enterpriseApRadioRTSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioRTSThreshold.setStatus(_A)
class _EnterpriseApRadioAntennaGainReduction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,29))
_EnterpriseApRadioAntennaGainReduction_Type.__name__=_C
_EnterpriseApRadioAntennaGainReduction_Object=MibTableColumn
enterpriseApRadioAntennaGainReduction=_EnterpriseApRadioAntennaGainReduction_Object((1,3,6,1,4,1,14823,2,3,2,15,1,1,28),_EnterpriseApRadioAntennaGainReduction_Type())
enterpriseApRadioAntennaGainReduction.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioAntennaGainReduction.setStatus(_A)
_EnterpriseApSNMP_ObjectIdentity=ObjectIdentity
enterpriseApSNMP=_EnterpriseApSNMP_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,16))
class _EnterpriseApSNMPCommunityReadOnly_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EnterpriseApSNMPCommunityReadOnly_Type.__name__=_I
_EnterpriseApSNMPCommunityReadOnly_Object=MibScalar
enterpriseApSNMPCommunityReadOnly=_EnterpriseApSNMPCommunityReadOnly_Object((1,3,6,1,4,1,14823,2,3,2,16,1),_EnterpriseApSNMPCommunityReadOnly_Type())
enterpriseApSNMPCommunityReadOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNMPCommunityReadOnly.setStatus(_A)
class _EnterpriseApSNMPCommunityReadWrite_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EnterpriseApSNMPCommunityReadWrite_Type.__name__=_I
_EnterpriseApSNMPCommunityReadWrite_Object=MibScalar
enterpriseApSNMPCommunityReadWrite=_EnterpriseApSNMPCommunityReadWrite_Object((1,3,6,1,4,1,14823,2,3,2,16,2),_EnterpriseApSNMPCommunityReadWrite_Type())
enterpriseApSNMPCommunityReadWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNMPCommunityReadWrite.setStatus(_A)
_EnterpriseApSNMPTrapDestinationTable_Object=MibTable
enterpriseApSNMPTrapDestinationTable=_EnterpriseApSNMPTrapDestinationTable_Object((1,3,6,1,4,1,14823,2,3,2,16,3))
if mibBuilder.loadTexts:enterpriseApSNMPTrapDestinationTable.setStatus(_A)
_EnterpriseApSNMPTrapDestinationEntry_Object=MibTableRow
enterpriseApSNMPTrapDestinationEntry=_EnterpriseApSNMPTrapDestinationEntry_Object((1,3,6,1,4,1,14823,2,3,2,16,3,1))
enterpriseApSNMPTrapDestinationEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:enterpriseApSNMPTrapDestinationEntry.setStatus(_A)
class _EnterpriseApSNMPTrapDestinationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EnterpriseApSNMPTrapDestinationIndex_Type.__name__=_C
_EnterpriseApSNMPTrapDestinationIndex_Object=MibTableColumn
enterpriseApSNMPTrapDestinationIndex=_EnterpriseApSNMPTrapDestinationIndex_Object((1,3,6,1,4,1,14823,2,3,2,16,3,1,1),_EnterpriseApSNMPTrapDestinationIndex_Type())
enterpriseApSNMPTrapDestinationIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApSNMPTrapDestinationIndex.setStatus(_A)
class _EnterpriseApSNMPTrapDestinationCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EnterpriseApSNMPTrapDestinationCommunity_Type.__name__=_I
_EnterpriseApSNMPTrapDestinationCommunity_Object=MibTableColumn
enterpriseApSNMPTrapDestinationCommunity=_EnterpriseApSNMPTrapDestinationCommunity_Object((1,3,6,1,4,1,14823,2,3,2,16,3,1,2),_EnterpriseApSNMPTrapDestinationCommunity_Type())
enterpriseApSNMPTrapDestinationCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNMPTrapDestinationCommunity.setStatus(_A)
_EnterpriseApSNMPTrapDestinationIP_Type=IpAddress
_EnterpriseApSNMPTrapDestinationIP_Object=MibTableColumn
enterpriseApSNMPTrapDestinationIP=_EnterpriseApSNMPTrapDestinationIP_Object((1,3,6,1,4,1,14823,2,3,2,16,3,1,3),_EnterpriseApSNMPTrapDestinationIP_Type())
enterpriseApSNMPTrapDestinationIP.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNMPTrapDestinationIP.setStatus(_A)
class _EnterpriseApSNMPTrapDestinationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSNMPTrapDestinationState_Type.__name__=_C
_EnterpriseApSNMPTrapDestinationState_Object=MibTableColumn
enterpriseApSNMPTrapDestinationState=_EnterpriseApSNMPTrapDestinationState_Object((1,3,6,1,4,1,14823,2,3,2,16,3,1,4),_EnterpriseApSNMPTrapDestinationState_Type())
enterpriseApSNMPTrapDestinationState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSNMPTrapDestinationState.setStatus(_A)
_EnterpriseApSNMPTrapFilters_ObjectIdentity=ObjectIdentity
enterpriseApSNMPTrapFilters=_EnterpriseApSNMPTrapFilters_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,16,4))
class _SysSystemUpTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_SysSystemUpTrapEnabled_Type.__name__=_C
_SysSystemUpTrapEnabled_Object=MibScalar
sysSystemUpTrapEnabled=_SysSystemUpTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,1),_SysSystemUpTrapEnabled_Type())
sysSystemUpTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sysSystemUpTrapEnabled.setStatus(_A)
class _SysSystemDownTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_SysSystemDownTrapEnabled_Type.__name__=_C
_SysSystemDownTrapEnabled_Object=MibScalar
sysSystemDownTrapEnabled=_SysSystemDownTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,2),_SysSystemDownTrapEnabled_Type())
sysSystemDownTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sysSystemDownTrapEnabled.setStatus(_A)
class _SysRadiusServerChangedTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_SysRadiusServerChangedTrapEnabled_Type.__name__=_C
_SysRadiusServerChangedTrapEnabled_Object=MibScalar
sysRadiusServerChangedTrapEnabled=_SysRadiusServerChangedTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,3),_SysRadiusServerChangedTrapEnabled_Type())
sysRadiusServerChangedTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sysRadiusServerChangedTrapEnabled.setStatus(_A)
class _SysConfigFileVersionChangedTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_SysConfigFileVersionChangedTrapEnabled_Type.__name__=_C
_SysConfigFileVersionChangedTrapEnabled_Object=MibScalar
sysConfigFileVersionChangedTrapEnabled=_SysConfigFileVersionChangedTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,4),_SysConfigFileVersionChangedTrapEnabled_Type())
sysConfigFileVersionChangedTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfigFileVersionChangedTrapEnabled.setStatus(_A)
class _Dot11StationAssociationTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11StationAssociationTrapEnabled_Type.__name__=_C
_Dot11StationAssociationTrapEnabled_Object=MibScalar
dot11StationAssociationTrapEnabled=_Dot11StationAssociationTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,5),_Dot11StationAssociationTrapEnabled_Type())
dot11StationAssociationTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11StationAssociationTrapEnabled.setStatus(_A)
class _Dot11StationReAssociationTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11StationReAssociationTrapEnabled_Type.__name__=_C
_Dot11StationReAssociationTrapEnabled_Object=MibScalar
dot11StationReAssociationTrapEnabled=_Dot11StationReAssociationTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,6),_Dot11StationReAssociationTrapEnabled_Type())
dot11StationReAssociationTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11StationReAssociationTrapEnabled.setStatus(_A)
class _Dot11StationAuthenticationTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11StationAuthenticationTrapEnabled_Type.__name__=_C
_Dot11StationAuthenticationTrapEnabled_Object=MibScalar
dot11StationAuthenticationTrapEnabled=_Dot11StationAuthenticationTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,7),_Dot11StationAuthenticationTrapEnabled_Type())
dot11StationAuthenticationTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11StationAuthenticationTrapEnabled.setStatus(_A)
class _Dot11StationRequestFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11StationRequestFailTrapEnabled_Type.__name__=_C
_Dot11StationRequestFailTrapEnabled_Object=MibScalar
dot11StationRequestFailTrapEnabled=_Dot11StationRequestFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,8),_Dot11StationRequestFailTrapEnabled_Type())
dot11StationRequestFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11StationRequestFailTrapEnabled.setStatus(_A)
class _Dot11InterfaceBFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11InterfaceBFailTrapEnabled_Type.__name__=_C
_Dot11InterfaceBFailTrapEnabled_Object=MibScalar
dot11InterfaceBFailTrapEnabled=_Dot11InterfaceBFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,9),_Dot11InterfaceBFailTrapEnabled_Type())
dot11InterfaceBFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11InterfaceBFailTrapEnabled.setStatus(_A)
class _Dot11InterfaceAGFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11InterfaceAGFailTrapEnabled_Type.__name__=_C
_Dot11InterfaceAGFailTrapEnabled_Object=MibScalar
dot11InterfaceAGFailTrapEnabled=_Dot11InterfaceAGFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,10),_Dot11InterfaceAGFailTrapEnabled_Type())
dot11InterfaceAGFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11InterfaceAGFailTrapEnabled.setStatus(_A)
class _Dot1xMacAddrAuthSuccessTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot1xMacAddrAuthSuccessTrapEnabled_Type.__name__=_C
_Dot1xMacAddrAuthSuccessTrapEnabled_Object=MibScalar
dot1xMacAddrAuthSuccessTrapEnabled=_Dot1xMacAddrAuthSuccessTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,11),_Dot1xMacAddrAuthSuccessTrapEnabled_Type())
dot1xMacAddrAuthSuccessTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xMacAddrAuthSuccessTrapEnabled.setStatus(_A)
class _Dot1xMacAddrAuthFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot1xMacAddrAuthFailTrapEnabled_Type.__name__=_C
_Dot1xMacAddrAuthFailTrapEnabled_Object=MibScalar
dot1xMacAddrAuthFailTrapEnabled=_Dot1xMacAddrAuthFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,12),_Dot1xMacAddrAuthFailTrapEnabled_Type())
dot1xMacAddrAuthFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xMacAddrAuthFailTrapEnabled.setStatus(_A)
class _Dot1xAuthNotInitiatedTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot1xAuthNotInitiatedTrapEnabled_Type.__name__=_C
_Dot1xAuthNotInitiatedTrapEnabled_Object=MibScalar
dot1xAuthNotInitiatedTrapEnabled=_Dot1xAuthNotInitiatedTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,13),_Dot1xAuthNotInitiatedTrapEnabled_Type())
dot1xAuthNotInitiatedTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthNotInitiatedTrapEnabled.setStatus(_A)
class _Dot1xAuthSuccessTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot1xAuthSuccessTrapEnabled_Type.__name__=_C
_Dot1xAuthSuccessTrapEnabled_Object=MibScalar
dot1xAuthSuccessTrapEnabled=_Dot1xAuthSuccessTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,14),_Dot1xAuthSuccessTrapEnabled_Type())
dot1xAuthSuccessTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthSuccessTrapEnabled.setStatus(_A)
class _Dot1xAuthFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot1xAuthFailTrapEnabled_Type.__name__=_C
_Dot1xAuthFailTrapEnabled_Object=MibScalar
dot1xAuthFailTrapEnabled=_Dot1xAuthFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,15),_Dot1xAuthFailTrapEnabled_Type())
dot1xAuthFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xAuthFailTrapEnabled.setStatus(_A)
class _LocalMacAddrAuthSuccessTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_LocalMacAddrAuthSuccessTrapEnabled_Type.__name__=_C
_LocalMacAddrAuthSuccessTrapEnabled_Object=MibScalar
localMacAddrAuthSuccessTrapEnabled=_LocalMacAddrAuthSuccessTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,16),_LocalMacAddrAuthSuccessTrapEnabled_Type())
localMacAddrAuthSuccessTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:localMacAddrAuthSuccessTrapEnabled.setStatus(_A)
class _LocalMacAddrAuthFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_LocalMacAddrAuthFailTrapEnabled_Type.__name__=_C
_LocalMacAddrAuthFailTrapEnabled_Object=MibScalar
localMacAddrAuthFailTrapEnabled=_LocalMacAddrAuthFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,17),_LocalMacAddrAuthFailTrapEnabled_Type())
localMacAddrAuthFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:localMacAddrAuthFailTrapEnabled.setStatus(_A)
class _PppLogonFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_PppLogonFailTrapEnabled_Type.__name__=_C
_PppLogonFailTrapEnabled_Object=MibScalar
pppLogonFailTrapEnabled=_PppLogonFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,18),_PppLogonFailTrapEnabled_Type())
pppLogonFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLogonFailTrapEnabled.setStatus(_A)
class _IappStationRoamedFromTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_IappStationRoamedFromTrapEnabled_Type.__name__=_C
_IappStationRoamedFromTrapEnabled_Object=MibScalar
iappStationRoamedFromTrapEnabled=_IappStationRoamedFromTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,19),_IappStationRoamedFromTrapEnabled_Type())
iappStationRoamedFromTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:iappStationRoamedFromTrapEnabled.setStatus(_A)
class _IappStationRoamedToTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_IappStationRoamedToTrapEnabled_Type.__name__=_C
_IappStationRoamedToTrapEnabled_Object=MibScalar
iappStationRoamedToTrapEnabled=_IappStationRoamedToTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,20),_IappStationRoamedToTrapEnabled_Type())
iappStationRoamedToTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:iappStationRoamedToTrapEnabled.setStatus(_A)
class _IappContextDataSentTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_IappContextDataSentTrapEnabled_Type.__name__=_C
_IappContextDataSentTrapEnabled_Object=MibScalar
iappContextDataSentTrapEnabled=_IappContextDataSentTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,21),_IappContextDataSentTrapEnabled_Type())
iappContextDataSentTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:iappContextDataSentTrapEnabled.setStatus(_A)
class _SntpServerFailTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_SntpServerFailTrapEnabled_Type.__name__=_C
_SntpServerFailTrapEnabled_Object=MibScalar
sntpServerFailTrapEnabled=_SntpServerFailTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,22),_SntpServerFailTrapEnabled_Type())
sntpServerFailTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpServerFailTrapEnabled.setStatus(_A)
class _Dot1xSuppAuthenticatedTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot1xSuppAuthenticatedTrapEnabled_Type.__name__=_C
_Dot1xSuppAuthenticatedTrapEnabled_Object=MibScalar
dot1xSuppAuthenticatedTrapEnabled=_Dot1xSuppAuthenticatedTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,23),_Dot1xSuppAuthenticatedTrapEnabled_Type())
dot1xSuppAuthenticatedTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1xSuppAuthenticatedTrapEnabled.setStatus(_A)
class _Dot11FailedTransmitsTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11FailedTransmitsTrapEnabled_Type.__name__=_C
_Dot11FailedTransmitsTrapEnabled_Object=MibScalar
dot11FailedTransmitsTrapEnabled=_Dot11FailedTransmitsTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,24),_Dot11FailedTransmitsTrapEnabled_Type())
dot11FailedTransmitsTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FailedTransmitsTrapEnabled.setStatus(_A)
class _Dot11AckFailuresTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11AckFailuresTrapEnabled_Type.__name__=_C
_Dot11AckFailuresTrapEnabled_Object=MibScalar
dot11AckFailuresTrapEnabled=_Dot11AckFailuresTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,25),_Dot11AckFailuresTrapEnabled_Type())
dot11AckFailuresTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AckFailuresTrapEnabled.setStatus(_A)
class _Dot11FcsErrorsTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_Dot11FcsErrorsTrapEnabled_Type.__name__=_C
_Dot11FcsErrorsTrapEnabled_Object=MibScalar
dot11FcsErrorsTrapEnabled=_Dot11FcsErrorsTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,26),_Dot11FcsErrorsTrapEnabled_Type())
dot11FcsErrorsTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FcsErrorsTrapEnabled.setStatus(_A)
class _RogueAPDetectedTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_RogueAPDetectedTrapEnabled_Type.__name__=_C
_RogueAPDetectedTrapEnabled_Object=MibScalar
rogueAPDetectedTrapEnabled=_RogueAPDetectedTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,27),_RogueAPDetectedTrapEnabled_Type())
rogueAPDetectedTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:rogueAPDetectedTrapEnabled.setStatus(_A)
class _PossibleRogueAPDetectedTrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_PossibleRogueAPDetectedTrapEnabled_Type.__name__=_C
_PossibleRogueAPDetectedTrapEnabled_Object=MibScalar
possibleRogueAPDetectedTrapEnabled=_PossibleRogueAPDetectedTrapEnabled_Object((1,3,6,1,4,1,14823,2,3,2,16,4,28),_PossibleRogueAPDetectedTrapEnabled_Type())
possibleRogueAPDetectedTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:possibleRogueAPDetectedTrapEnabled.setStatus(_A)
_EnterpriseApSession_ObjectIdentity=ObjectIdentity
enterpriseApSession=_EnterpriseApSession_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,17))
_EnterpriseApSessionTable_Object=MibTable
enterpriseApSessionTable=_EnterpriseApSessionTable_Object((1,3,6,1,4,1,14823,2,3,2,17,1))
if mibBuilder.loadTexts:enterpriseApSessionTable.setStatus(_A)
_EnterpriseApSessionEntry_Object=MibTableRow
enterpriseApSessionEntry=_EnterpriseApSessionEntry_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1))
enterpriseApSessionEntry.setIndexNames((0,_F,_o),(0,_F,_p))
if mibBuilder.loadTexts:enterpriseApSessionEntry.setStatus(_A)
_EnterpriseApSessionIfIndex_Type=Integer32
_EnterpriseApSessionIfIndex_Object=MibTableColumn
enterpriseApSessionIfIndex=_EnterpriseApSessionIfIndex_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,1),_EnterpriseApSessionIfIndex_Type())
enterpriseApSessionIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApSessionIfIndex.setStatus(_A)
_EnterpriseApSessionStationAddres_Type=MacAddress
_EnterpriseApSessionStationAddres_Object=MibTableColumn
enterpriseApSessionStationAddres=_EnterpriseApSessionStationAddres_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,2),_EnterpriseApSessionStationAddres_Type())
enterpriseApSessionStationAddres.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApSessionStationAddres.setStatus(_A)
_EnterpriseApSessionAuthenticated_Type=TruthValue
_EnterpriseApSessionAuthenticated_Object=MibTableColumn
enterpriseApSessionAuthenticated=_EnterpriseApSessionAuthenticated_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,3),_EnterpriseApSessionAuthenticated_Type())
enterpriseApSessionAuthenticated.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionAuthenticated.setStatus(_A)
_EnterpriseApSessionAssociated_Type=TruthValue
_EnterpriseApSessionAssociated_Object=MibTableColumn
enterpriseApSessionAssociated=_EnterpriseApSessionAssociated_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,4),_EnterpriseApSessionAssociated_Type())
enterpriseApSessionAssociated.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionAssociated.setStatus(_A)
_EnterpriseApSessionIsForwarding_Type=TruthValue
_EnterpriseApSessionIsForwarding_Object=MibTableColumn
enterpriseApSessionIsForwarding=_EnterpriseApSessionIsForwarding_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,5),_EnterpriseApSessionIsForwarding_Type())
enterpriseApSessionIsForwarding.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionIsForwarding.setStatus(_A)
class _EnterpriseApSessionKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),('staticWep',2),('dynamicWep',3),('wpaWep',4),('wpaTkip',5),('wpaAes',6)))
_EnterpriseApSessionKeyType_Type.__name__=_C
_EnterpriseApSessionKeyType_Object=MibTableColumn
enterpriseApSessionKeyType=_EnterpriseApSessionKeyType_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,6),_EnterpriseApSessionKeyType_Type())
enterpriseApSessionKeyType.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionKeyType.setStatus(_A)
_EnterpriseApSessionAssociationId_Type=Integer32
_EnterpriseApSessionAssociationId_Object=MibTableColumn
enterpriseApSessionAssociationId=_EnterpriseApSessionAssociationId_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,7),_EnterpriseApSessionAssociationId_Type())
enterpriseApSessionAssociationId.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionAssociationId.setStatus(_A)
_EnterpriseApSessionLastAuthenticatedTime_Type=TimeTicks
_EnterpriseApSessionLastAuthenticatedTime_Object=MibTableColumn
enterpriseApSessionLastAuthenticatedTime=_EnterpriseApSessionLastAuthenticatedTime_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,8),_EnterpriseApSessionLastAuthenticatedTime_Type())
enterpriseApSessionLastAuthenticatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionLastAuthenticatedTime.setStatus(_A)
_EnterpriseApSessionAssociatedTime_Type=TimeTicks
_EnterpriseApSessionAssociatedTime_Object=MibTableColumn
enterpriseApSessionAssociatedTime=_EnterpriseApSessionAssociatedTime_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,9),_EnterpriseApSessionAssociatedTime_Type())
enterpriseApSessionAssociatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionAssociatedTime.setStatus(_A)
_EnterpriseApSessionLastAssociatedTime_Type=TimeTicks
_EnterpriseApSessionLastAssociatedTime_Object=MibTableColumn
enterpriseApSessionLastAssociatedTime=_EnterpriseApSessionLastAssociatedTime_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,10),_EnterpriseApSessionLastAssociatedTime_Type())
enterpriseApSessionLastAssociatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionLastAssociatedTime.setStatus(_A)
_EnterpriseApSessionLastDisassociatedTime_Type=TimeTicks
_EnterpriseApSessionLastDisassociatedTime_Object=MibTableColumn
enterpriseApSessionLastDisassociatedTime=_EnterpriseApSessionLastDisassociatedTime_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,11),_EnterpriseApSessionLastDisassociatedTime_Type())
enterpriseApSessionLastDisassociatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionLastDisassociatedTime.setStatus(_A)
_EnterpriseApSessionTxPacketCount_Type=Counter32
_EnterpriseApSessionTxPacketCount_Object=MibTableColumn
enterpriseApSessionTxPacketCount=_EnterpriseApSessionTxPacketCount_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,12),_EnterpriseApSessionTxPacketCount_Type())
enterpriseApSessionTxPacketCount.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionTxPacketCount.setStatus(_A)
_EnterpriseApSessionRxPacketCount_Type=Counter32
_EnterpriseApSessionRxPacketCount_Object=MibTableColumn
enterpriseApSessionRxPacketCount=_EnterpriseApSessionRxPacketCount_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,13),_EnterpriseApSessionRxPacketCount_Type())
enterpriseApSessionRxPacketCount.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionRxPacketCount.setStatus(_A)
_EnterpriseApSessionTxByteCount_Type=Counter32
_EnterpriseApSessionTxByteCount_Object=MibTableColumn
enterpriseApSessionTxByteCount=_EnterpriseApSessionTxByteCount_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,14),_EnterpriseApSessionTxByteCount_Type())
enterpriseApSessionTxByteCount.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionTxByteCount.setStatus(_A)
_EnterpriseApSessionRxByteCount_Type=Counter32
_EnterpriseApSessionRxByteCount_Object=MibTableColumn
enterpriseApSessionRxByteCount=_EnterpriseApSessionRxByteCount_Object((1,3,6,1,4,1,14823,2,3,2,17,1,1,15),_EnterpriseApSessionRxByteCount_Type())
enterpriseApSessionRxByteCount.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApSessionRxByteCount.setStatus(_A)
_EnterpriseAPVapRadio_ObjectIdentity=ObjectIdentity
enterpriseAPVapRadio=_EnterpriseAPVapRadio_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,20))
_EnterpriseAPVapRadioTable_Object=MibTable
enterpriseAPVapRadioTable=_EnterpriseAPVapRadioTable_Object((1,3,6,1,4,1,14823,2,3,2,20,1))
if mibBuilder.loadTexts:enterpriseAPVapRadioTable.setStatus(_A)
_EnterpriseAPVapRadioEntry_Object=MibTableRow
enterpriseAPVapRadioEntry=_EnterpriseAPVapRadioEntry_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1))
enterpriseAPVapRadioEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:enterpriseAPVapRadioEntry.setStatus(_A)
_EnterpriseAPVapRadioIndex_Type=Integer32
_EnterpriseAPVapRadioIndex_Object=MibTableColumn
enterpriseAPVapRadioIndex=_EnterpriseAPVapRadioIndex_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,1),_EnterpriseAPVapRadioIndex_Type())
enterpriseAPVapRadioIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseAPVapRadioIndex.setStatus(_A)
class _EnterpriseAPVapRadioState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseAPVapRadioState_Type.__name__=_C
_EnterpriseAPVapRadioState_Object=MibTableColumn
enterpriseAPVapRadioState=_EnterpriseAPVapRadioState_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,2),_EnterpriseAPVapRadioState_Type())
enterpriseAPVapRadioState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioState.setStatus(_A)
class _EnterpriseAPVapRadioClosedSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseAPVapRadioClosedSystem_Type.__name__=_C
_EnterpriseAPVapRadioClosedSystem_Object=MibTableColumn
enterpriseAPVapRadioClosedSystem=_EnterpriseAPVapRadioClosedSystem_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,3),_EnterpriseAPVapRadioClosedSystem_Type())
enterpriseAPVapRadioClosedSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioClosedSystem.setStatus(_A)
class _EnterpriseAPVapRadioMaxAssoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_EnterpriseAPVapRadioMaxAssoc_Type.__name__=_C
_EnterpriseAPVapRadioMaxAssoc_Object=MibTableColumn
enterpriseAPVapRadioMaxAssoc=_EnterpriseAPVapRadioMaxAssoc_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,4),_EnterpriseAPVapRadioMaxAssoc_Type())
enterpriseAPVapRadioMaxAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioMaxAssoc.setStatus(_A)
class _EnterpriseAPVapRadioTransmitKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EnterpriseAPVapRadioTransmitKey_Type.__name__=_C
_EnterpriseAPVapRadioTransmitKey_Object=MibTableColumn
enterpriseAPVapRadioTransmitKey=_EnterpriseAPVapRadioTransmitKey_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,5),_EnterpriseAPVapRadioTransmitKey_Type())
enterpriseAPVapRadioTransmitKey.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioTransmitKey.setStatus(_A)
class _EnterpriseAPVapRadioDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EnterpriseAPVapRadioDescription_Type.__name__=_I
_EnterpriseAPVapRadioDescription_Object=MibTableColumn
enterpriseAPVapRadioDescription=_EnterpriseAPVapRadioDescription_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,6),_EnterpriseAPVapRadioDescription_Type())
enterpriseAPVapRadioDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioDescription.setStatus(_A)
class _EnterpriseAPVapRadioAuthTimeoutInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_EnterpriseAPVapRadioAuthTimeoutInterval_Type.__name__=_C
_EnterpriseAPVapRadioAuthTimeoutInterval_Object=MibTableColumn
enterpriseAPVapRadioAuthTimeoutInterval=_EnterpriseAPVapRadioAuthTimeoutInterval_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,8),_EnterpriseAPVapRadioAuthTimeoutInterval_Type())
enterpriseAPVapRadioAuthTimeoutInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioAuthTimeoutInterval.setStatus(_A)
class _EnterpriseAPVapRadioAssocTimeoutInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_EnterpriseAPVapRadioAssocTimeoutInterval_Type.__name__=_C
_EnterpriseAPVapRadioAssocTimeoutInterval_Object=MibTableColumn
enterpriseAPVapRadioAssocTimeoutInterval=_EnterpriseAPVapRadioAssocTimeoutInterval_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,9),_EnterpriseAPVapRadioAssocTimeoutInterval_Type())
enterpriseAPVapRadioAssocTimeoutInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioAssocTimeoutInterval.setStatus(_A)
class _EnterpriseAPVapRadioWPA2PMKSALifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_EnterpriseAPVapRadioWPA2PMKSALifeTime_Type.__name__=_C
_EnterpriseAPVapRadioWPA2PMKSALifeTime_Object=MibTableColumn
enterpriseAPVapRadioWPA2PMKSALifeTime=_EnterpriseAPVapRadioWPA2PMKSALifeTime_Object((1,3,6,1,4,1,14823,2,3,2,20,1,1,10),_EnterpriseAPVapRadioWPA2PMKSALifeTime_Type())
enterpriseAPVapRadioWPA2PMKSALifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseAPVapRadioWPA2PMKSALifeTime.setStatus(_A)
_EnterpriseApRadioWds_ObjectIdentity=ObjectIdentity
enterpriseApRadioWds=_EnterpriseApRadioWds_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,22))
_EnterpriseApRadioWdsTable_Object=MibTable
enterpriseApRadioWdsTable=_EnterpriseApRadioWdsTable_Object((1,3,6,1,4,1,14823,2,3,2,22,1))
if mibBuilder.loadTexts:enterpriseApRadioWdsTable.setStatus(_A)
_EnterpriseApRadioWdsEntry_Object=MibTableRow
enterpriseApRadioWdsEntry=_EnterpriseApRadioWdsEntry_Object((1,3,6,1,4,1,14823,2,3,2,22,1,1))
enterpriseApRadioWdsEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:enterpriseApRadioWdsEntry.setStatus(_A)
class _WdsApRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('roleAp',1),('roleBridgeMaster',2),('roleBridge',4)))
_WdsApRole_Type.__name__=_C
_WdsApRole_Object=MibTableColumn
wdsApRole=_WdsApRole_Object((1,3,6,1,4,1,14823,2,3,2,22,1,1,1),_WdsApRole_Type())
wdsApRole.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsApRole.setStatus(_A)
class _WdsChannelAutoSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_WdsChannelAutoSync_Type.__name__=_C
_WdsChannelAutoSync_Object=MibTableColumn
wdsChannelAutoSync=_WdsChannelAutoSync_Object((1,3,6,1,4,1,14823,2,3,2,22,1,1,3),_WdsChannelAutoSync_Type())
wdsChannelAutoSync.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsChannelAutoSync.setStatus(_A)
class _WdsMasterSlaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_WdsMasterSlaveMode_Type.__name__=_C
_WdsMasterSlaveMode_Object=MibTableColumn
wdsMasterSlaveMode=_WdsMasterSlaveMode_Object((1,3,6,1,4,1,14823,2,3,2,22,1,1,4),_WdsMasterSlaveMode_Type())
wdsMasterSlaveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsMasterSlaveMode.setStatus(_A)
_EnterpriseApRadioWdsPeerTable_Object=MibTable
enterpriseApRadioWdsPeerTable=_EnterpriseApRadioWdsPeerTable_Object((1,3,6,1,4,1,14823,2,3,2,22,2))
if mibBuilder.loadTexts:enterpriseApRadioWdsPeerTable.setStatus(_A)
_EnterpriseApRadioWdsPeerEntry_Object=MibTableRow
enterpriseApRadioWdsPeerEntry=_EnterpriseApRadioWdsPeerEntry_Object((1,3,6,1,4,1,14823,2,3,2,22,2,1))
enterpriseApRadioWdsPeerEntry.setIndexNames((0,_F,_O),(0,_F,_r))
if mibBuilder.loadTexts:enterpriseApRadioWdsPeerEntry.setStatus(_A)
_WdsPeerIndex_Type=Integer32
_WdsPeerIndex_Object=MibTableColumn
wdsPeerIndex=_WdsPeerIndex_Object((1,3,6,1,4,1,14823,2,3,2,22,2,1,1),_WdsPeerIndex_Type())
wdsPeerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:wdsPeerIndex.setStatus(_A)
class _WdsPeerBssid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_WdsPeerBssid_Type.__name__=_I
_WdsPeerBssid_Object=MibTableColumn
wdsPeerBssid=_WdsPeerBssid_Object((1,3,6,1,4,1,14823,2,3,2,22,2,1,2),_WdsPeerBssid_Type())
wdsPeerBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsPeerBssid.setStatus(_A)
_EnterpriseApWMM_ObjectIdentity=ObjectIdentity
enterpriseApWMM=_EnterpriseApWMM_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,24))
_EnterpriseApWMMTable_Object=MibTable
enterpriseApWMMTable=_EnterpriseApWMMTable_Object((1,3,6,1,4,1,14823,2,3,2,24,1))
if mibBuilder.loadTexts:enterpriseApWMMTable.setStatus(_A)
_EnterpriseApWMMEntry_Object=MibTableRow
enterpriseApWMMEntry=_EnterpriseApWMMEntry_Object((1,3,6,1,4,1,14823,2,3,2,24,1,1))
enterpriseApWMMEntry.setIndexNames((0,_F,_s))
if mibBuilder.loadTexts:enterpriseApWMMEntry.setStatus(_A)
_EnterpriseApWMMModeIndex_Type=Integer32
_EnterpriseApWMMModeIndex_Object=MibTableColumn
enterpriseApWMMModeIndex=_EnterpriseApWMMModeIndex_Object((1,3,6,1,4,1,14823,2,3,2,24,1,1,1),_EnterpriseApWMMModeIndex_Type())
enterpriseApWMMModeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApWMMModeIndex.setStatus(_A)
class _EnterpriseApWMMMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('support',2),(_N,3)))
_EnterpriseApWMMMode_Type.__name__=_C
_EnterpriseApWMMMode_Object=MibTableColumn
enterpriseApWMMMode=_EnterpriseApWMMMode_Object((1,3,6,1,4,1,14823,2,3,2,24,1,1,2),_EnterpriseApWMMMode_Type())
enterpriseApWMMMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMMode.setStatus(_A)
_EnterpriseApWMMAckPolicyTable_Object=MibTable
enterpriseApWMMAckPolicyTable=_EnterpriseApWMMAckPolicyTable_Object((1,3,6,1,4,1,14823,2,3,2,24,2))
if mibBuilder.loadTexts:enterpriseApWMMAckPolicyTable.setStatus(_A)
_EnterpriseApWMMAckPolicyEntry_Object=MibTableRow
enterpriseApWMMAckPolicyEntry=_EnterpriseApWMMAckPolicyEntry_Object((1,3,6,1,4,1,14823,2,3,2,24,2,1))
enterpriseApWMMAckPolicyEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:enterpriseApWMMAckPolicyEntry.setStatus(_A)
_EnterpriseApWMMAckPolicyIndex_Type=Integer32
_EnterpriseApWMMAckPolicyIndex_Object=MibTableColumn
enterpriseApWMMAckPolicyIndex=_EnterpriseApWMMAckPolicyIndex_Object((1,3,6,1,4,1,14823,2,3,2,24,2,1,1),_EnterpriseApWMMAckPolicyIndex_Type())
enterpriseApWMMAckPolicyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApWMMAckPolicyIndex.setStatus(_A)
class _EnterpriseApWMMACKPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('acknowledge',1),('NoAcknowledge',2)))
_EnterpriseApWMMACKPolicy_Type.__name__=_C
_EnterpriseApWMMACKPolicy_Object=MibTableColumn
enterpriseApWMMACKPolicy=_EnterpriseApWMMACKPolicy_Object((1,3,6,1,4,1,14823,2,3,2,24,2,1,2),_EnterpriseApWMMACKPolicy_Type())
enterpriseApWMMACKPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMACKPolicy.setStatus(_A)
_EnterpriseApWMMBSSParamTable_Object=MibTable
enterpriseApWMMBSSParamTable=_EnterpriseApWMMBSSParamTable_Object((1,3,6,1,4,1,14823,2,3,2,24,3))
if mibBuilder.loadTexts:enterpriseApWMMBSSParamTable.setStatus(_A)
_EnterpriseApWMMBSSParamEntry_Object=MibTableRow
enterpriseApWMMBSSParamEntry=_EnterpriseApWMMBSSParamEntry_Object((1,3,6,1,4,1,14823,2,3,2,24,3,1))
enterpriseApWMMBSSParamEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:enterpriseApWMMBSSParamEntry.setStatus(_A)
_EnterpriseApWMMBSSParamIndex_Type=Integer32
_EnterpriseApWMMBSSParamIndex_Object=MibTableColumn
enterpriseApWMMBSSParamIndex=_EnterpriseApWMMBSSParamIndex_Object((1,3,6,1,4,1,14823,2,3,2,24,3,1,1),_EnterpriseApWMMBSSParamIndex_Type())
enterpriseApWMMBSSParamIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApWMMBSSParamIndex.setStatus(_A)
class _EnterpriseApWMMBSSParamLogCwMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_EnterpriseApWMMBSSParamLogCwMin_Type.__name__=_C
_EnterpriseApWMMBSSParamLogCwMin_Object=MibTableColumn
enterpriseApWMMBSSParamLogCwMin=_EnterpriseApWMMBSSParamLogCwMin_Object((1,3,6,1,4,1,14823,2,3,2,24,3,1,2),_EnterpriseApWMMBSSParamLogCwMin_Type())
enterpriseApWMMBSSParamLogCwMin.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMBSSParamLogCwMin.setStatus(_A)
class _EnterpriseApWMMBSSParamLogCwMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_EnterpriseApWMMBSSParamLogCwMax_Type.__name__=_C
_EnterpriseApWMMBSSParamLogCwMax_Object=MibTableColumn
enterpriseApWMMBSSParamLogCwMax=_EnterpriseApWMMBSSParamLogCwMax_Object((1,3,6,1,4,1,14823,2,3,2,24,3,1,3),_EnterpriseApWMMBSSParamLogCwMax_Type())
enterpriseApWMMBSSParamLogCwMax.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMBSSParamLogCwMax.setStatus(_A)
class _EnterpriseApWMMBSSParamAIFSN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_EnterpriseApWMMBSSParamAIFSN_Type.__name__=_C
_EnterpriseApWMMBSSParamAIFSN_Object=MibTableColumn
enterpriseApWMMBSSParamAIFSN=_EnterpriseApWMMBSSParamAIFSN_Object((1,3,6,1,4,1,14823,2,3,2,24,3,1,4),_EnterpriseApWMMBSSParamAIFSN_Type())
enterpriseApWMMBSSParamAIFSN.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMBSSParamAIFSN.setStatus(_A)
class _EnterpriseApWMMBSSParamTXOPLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EnterpriseApWMMBSSParamTXOPLimit_Type.__name__=_C
_EnterpriseApWMMBSSParamTXOPLimit_Object=MibTableColumn
enterpriseApWMMBSSParamTXOPLimit=_EnterpriseApWMMBSSParamTXOPLimit_Object((1,3,6,1,4,1,14823,2,3,2,24,3,1,5),_EnterpriseApWMMBSSParamTXOPLimit_Type())
enterpriseApWMMBSSParamTXOPLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMBSSParamTXOPLimit.setStatus(_A)
class _EnterpriseApWMMBSSParamAdmissionCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_D,2)))
_EnterpriseApWMMBSSParamAdmissionCtrl_Type.__name__=_C
_EnterpriseApWMMBSSParamAdmissionCtrl_Object=MibTableColumn
enterpriseApWMMBSSParamAdmissionCtrl=_EnterpriseApWMMBSSParamAdmissionCtrl_Object((1,3,6,1,4,1,14823,2,3,2,24,3,1,6),_EnterpriseApWMMBSSParamAdmissionCtrl_Type())
enterpriseApWMMBSSParamAdmissionCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMBSSParamAdmissionCtrl.setStatus(_A)
_EnterpriseApWMMAPParamTable_Object=MibTable
enterpriseApWMMAPParamTable=_EnterpriseApWMMAPParamTable_Object((1,3,6,1,4,1,14823,2,3,2,24,4))
if mibBuilder.loadTexts:enterpriseApWMMAPParamTable.setStatus(_A)
_EnterpriseApWMMAPParamEntry_Object=MibTableRow
enterpriseApWMMAPParamEntry=_EnterpriseApWMMAPParamEntry_Object((1,3,6,1,4,1,14823,2,3,2,24,4,1))
enterpriseApWMMAPParamEntry.setIndexNames((0,_F,_w))
if mibBuilder.loadTexts:enterpriseApWMMAPParamEntry.setStatus(_A)
_EnterpriseApWMMAPParamIndex_Type=Integer32
_EnterpriseApWMMAPParamIndex_Object=MibTableColumn
enterpriseApWMMAPParamIndex=_EnterpriseApWMMAPParamIndex_Object((1,3,6,1,4,1,14823,2,3,2,24,4,1,1),_EnterpriseApWMMAPParamIndex_Type())
enterpriseApWMMAPParamIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApWMMAPParamIndex.setStatus(_A)
class _EnterpriseApWMMAPParamLogCwMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_EnterpriseApWMMAPParamLogCwMin_Type.__name__=_C
_EnterpriseApWMMAPParamLogCwMin_Object=MibTableColumn
enterpriseApWMMAPParamLogCwMin=_EnterpriseApWMMAPParamLogCwMin_Object((1,3,6,1,4,1,14823,2,3,2,24,4,1,2),_EnterpriseApWMMAPParamLogCwMin_Type())
enterpriseApWMMAPParamLogCwMin.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMAPParamLogCwMin.setStatus(_A)
class _EnterpriseApWMMAPParamLogCwMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_EnterpriseApWMMAPParamLogCwMax_Type.__name__=_C
_EnterpriseApWMMAPParamLogCwMax_Object=MibTableColumn
enterpriseApWMMAPParamLogCwMax=_EnterpriseApWMMAPParamLogCwMax_Object((1,3,6,1,4,1,14823,2,3,2,24,4,1,3),_EnterpriseApWMMAPParamLogCwMax_Type())
enterpriseApWMMAPParamLogCwMax.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMAPParamLogCwMax.setStatus(_A)
class _EnterpriseApWMMAPParamAIFSN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_EnterpriseApWMMAPParamAIFSN_Type.__name__=_C
_EnterpriseApWMMAPParamAIFSN_Object=MibTableColumn
enterpriseApWMMAPParamAIFSN=_EnterpriseApWMMAPParamAIFSN_Object((1,3,6,1,4,1,14823,2,3,2,24,4,1,4),_EnterpriseApWMMAPParamAIFSN_Type())
enterpriseApWMMAPParamAIFSN.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMAPParamAIFSN.setStatus(_A)
class _EnterpriseApWMMAPParamTXOPLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EnterpriseApWMMAPParamTXOPLimit_Type.__name__=_C
_EnterpriseApWMMAPParamTXOPLimit_Object=MibTableColumn
enterpriseApWMMAPParamTXOPLimit=_EnterpriseApWMMAPParamTXOPLimit_Object((1,3,6,1,4,1,14823,2,3,2,24,4,1,5),_EnterpriseApWMMAPParamTXOPLimit_Type())
enterpriseApWMMAPParamTXOPLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMAPParamTXOPLimit.setStatus(_A)
class _EnterpriseApWMMAPParamAdmissionCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_D,2)))
_EnterpriseApWMMAPParamAdmissionCtrl_Type.__name__=_C
_EnterpriseApWMMAPParamAdmissionCtrl_Object=MibTableColumn
enterpriseApWMMAPParamAdmissionCtrl=_EnterpriseApWMMAPParamAdmissionCtrl_Object((1,3,6,1,4,1,14823,2,3,2,24,4,1,6),_EnterpriseApWMMAPParamAdmissionCtrl_Type())
enterpriseApWMMAPParamAdmissionCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApWMMAPParamAdmissionCtrl.setStatus(_A)
_EnterpriseApSTP_ObjectIdentity=ObjectIdentity
enterpriseApSTP=_EnterpriseApSTP_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,25))
class _EnterpriseApSTPBridgeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApSTPBridgeStatus_Type.__name__=_C
_EnterpriseApSTPBridgeStatus_Object=MibScalar
enterpriseApSTPBridgeStatus=_EnterpriseApSTPBridgeStatus_Object((1,3,6,1,4,1,14823,2,3,2,25,1),_EnterpriseApSTPBridgeStatus_Type())
enterpriseApSTPBridgeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPBridgeStatus.setStatus(_A)
class _EnterpriseApSTPBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EnterpriseApSTPBridgePriority_Type.__name__=_C
_EnterpriseApSTPBridgePriority_Object=MibScalar
enterpriseApSTPBridgePriority=_EnterpriseApSTPBridgePriority_Object((1,3,6,1,4,1,14823,2,3,2,25,2),_EnterpriseApSTPBridgePriority_Type())
enterpriseApSTPBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPBridgePriority.setStatus(_A)
class _EnterpriseApSTPBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_EnterpriseApSTPBridgeMaxAge_Type.__name__=_C
_EnterpriseApSTPBridgeMaxAge_Object=MibScalar
enterpriseApSTPBridgeMaxAge=_EnterpriseApSTPBridgeMaxAge_Object((1,3,6,1,4,1,14823,2,3,2,25,3),_EnterpriseApSTPBridgeMaxAge_Type())
enterpriseApSTPBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPBridgeMaxAge.setStatus(_A)
class _EnterpriseApSTPHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EnterpriseApSTPHelloTime_Type.__name__=_C
_EnterpriseApSTPHelloTime_Object=MibScalar
enterpriseApSTPHelloTime=_EnterpriseApSTPHelloTime_Object((1,3,6,1,4,1,14823,2,3,2,25,4),_EnterpriseApSTPHelloTime_Type())
enterpriseApSTPHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPHelloTime.setStatus(_A)
class _EnterpriseApSTPBridgeForwardingDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_EnterpriseApSTPBridgeForwardingDelay_Type.__name__=_C
_EnterpriseApSTPBridgeForwardingDelay_Object=MibScalar
enterpriseApSTPBridgeForwardingDelay=_EnterpriseApSTPBridgeForwardingDelay_Object((1,3,6,1,4,1,14823,2,3,2,25,5),_EnterpriseApSTPBridgeForwardingDelay_Type())
enterpriseApSTPBridgeForwardingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPBridgeForwardingDelay.setStatus(_A)
_EnterpriseApSTPRadioInterface_ObjectIdentity=ObjectIdentity
enterpriseApSTPRadioInterface=_EnterpriseApSTPRadioInterface_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,25,6))
_EnterpriseApSTPNodeTable_Object=MibTable
enterpriseApSTPNodeTable=_EnterpriseApSTPNodeTable_Object((1,3,6,1,4,1,14823,2,3,2,25,6,1))
if mibBuilder.loadTexts:enterpriseApSTPNodeTable.setStatus(_A)
_EnterpriseApSTPNodeEntry_Object=MibTableRow
enterpriseApSTPNodeEntry=_EnterpriseApSTPNodeEntry_Object((1,3,6,1,4,1,14823,2,3,2,25,6,1,1))
enterpriseApSTPNodeEntry.setIndexNames((0,_F,_x))
if mibBuilder.loadTexts:enterpriseApSTPNodeEntry.setStatus(_A)
_EnterpriseApSTPNodeIndex_Type=Integer32
_EnterpriseApSTPNodeIndex_Object=MibTableColumn
enterpriseApSTPNodeIndex=_EnterpriseApSTPNodeIndex_Object((1,3,6,1,4,1,14823,2,3,2,25,6,1,1,1),_EnterpriseApSTPNodeIndex_Type())
enterpriseApSTPNodeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApSTPNodeIndex.setStatus(_A)
class _EnterpriseApSTPNodeLinkPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EnterpriseApSTPNodeLinkPathCost_Type.__name__=_C
_EnterpriseApSTPNodeLinkPathCost_Object=MibTableColumn
enterpriseApSTPNodeLinkPathCost=_EnterpriseApSTPNodeLinkPathCost_Object((1,3,6,1,4,1,14823,2,3,2,25,6,1,1,2),_EnterpriseApSTPNodeLinkPathCost_Type())
enterpriseApSTPNodeLinkPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPNodeLinkPathCost.setStatus(_A)
class _EnterpriseApSTPNodeLinkPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EnterpriseApSTPNodeLinkPortPriority_Type.__name__=_C
_EnterpriseApSTPNodeLinkPortPriority_Object=MibTableColumn
enterpriseApSTPNodeLinkPortPriority=_EnterpriseApSTPNodeLinkPortPriority_Object((1,3,6,1,4,1,14823,2,3,2,25,6,1,1,3),_EnterpriseApSTPNodeLinkPortPriority_Type())
enterpriseApSTPNodeLinkPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPNodeLinkPortPriority.setStatus(_A)
_EnterpriseApSTPEthernetInterface_ObjectIdentity=ObjectIdentity
enterpriseApSTPEthernetInterface=_EnterpriseApSTPEthernetInterface_ObjectIdentity((1,3,6,1,4,1,14823,2,3,2,25,7))
class _EnterpriseApSTPEthernetLinkPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EnterpriseApSTPEthernetLinkPathCost_Type.__name__=_C
_EnterpriseApSTPEthernetLinkPathCost_Object=MibScalar
enterpriseApSTPEthernetLinkPathCost=_EnterpriseApSTPEthernetLinkPathCost_Object((1,3,6,1,4,1,14823,2,3,2,25,7,1),_EnterpriseApSTPEthernetLinkPathCost_Type())
enterpriseApSTPEthernetLinkPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPEthernetLinkPathCost.setStatus(_A)
class _EnterpriseApSTPEthernetLinkPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EnterpriseApSTPEthernetLinkPortPriority_Type.__name__=_C
_EnterpriseApSTPEthernetLinkPortPriority_Object=MibScalar
enterpriseApSTPEthernetLinkPortPriority=_EnterpriseApSTPEthernetLinkPortPriority_Object((1,3,6,1,4,1,14823,2,3,2,25,7,2),_EnterpriseApSTPEthernetLinkPortPriority_Type())
enterpriseApSTPEthernetLinkPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSTPEthernetLinkPortPriority.setStatus(_A)
sysSystemUp=NotificationType((1,3,6,1,4,1,14823,2,3,2,1,5,2,1))
if mibBuilder.loadTexts:sysSystemUp.setStatus(_A)
sysSystemDown=NotificationType((1,3,6,1,4,1,14823,2,3,2,1,5,2,2))
if mibBuilder.loadTexts:sysSystemDown.setStatus(_A)
sysRadiusServerChanged=NotificationType((1,3,6,1,4,1,14823,2,3,2,1,5,2,3))
if mibBuilder.loadTexts:sysRadiusServerChanged.setStatus(_A)
sysConfigFileVersionChanged=NotificationType((1,3,6,1,4,1,14823,2,3,2,1,5,2,4))
if mibBuilder.loadTexts:sysConfigFileVersionChanged.setStatus(_A)
dot11StationAssociation=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,1))
dot11StationAssociation.setObjects((_F,_J))
if mibBuilder.loadTexts:dot11StationAssociation.setStatus(_A)
dot11StationReAssociation=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,2))
dot11StationReAssociation.setObjects((_F,_J))
if mibBuilder.loadTexts:dot11StationReAssociation.setStatus(_A)
dot11StationAuthentication=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,3))
dot11StationAuthentication.setObjects((_F,_J))
if mibBuilder.loadTexts:dot11StationAuthentication.setStatus(_A)
dot11StationRequestFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,4))
dot11StationRequestFail.setObjects(*((_F,_J),(_F,_y),(_F,_z)))
if mibBuilder.loadTexts:dot11StationRequestFail.setStatus(_A)
dot11InterfaceBFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,5))
if mibBuilder.loadTexts:dot11InterfaceBFail.setStatus(_A)
dot11InterfaceAGFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,6))
if mibBuilder.loadTexts:dot11InterfaceAGFail.setStatus(_A)
dot1xMacAddrAuthSuccess=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,7))
dot1xMacAddrAuthSuccess.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xMacAddrAuthSuccess.setStatus(_A)
dot1xMacAddrAuthFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,8))
dot1xMacAddrAuthFail.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xMacAddrAuthFail.setStatus(_A)
dot1xAuthNotInitiated=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,9))
dot1xAuthNotInitiated.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xAuthNotInitiated.setStatus(_A)
dot1xAuthSuccess=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,10))
dot1xAuthSuccess.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xAuthSuccess.setStatus(_A)
dot1xAuthFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,11))
dot1xAuthFail.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xAuthFail.setStatus(_A)
localMacAddrAuthSuccess=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,12))
localMacAddrAuthSuccess.setObjects((_F,_J))
if mibBuilder.loadTexts:localMacAddrAuthSuccess.setStatus(_A)
localMacAddrAuthFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,13))
localMacAddrAuthFail.setObjects((_F,_J))
if mibBuilder.loadTexts:localMacAddrAuthFail.setStatus(_A)
pppLogonFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,14))
if mibBuilder.loadTexts:pppLogonFail.setStatus(_A)
iappStationRoamedFrom=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,15))
iappStationRoamedFrom.setObjects(*((_F,_J),(_F,_P)))
if mibBuilder.loadTexts:iappStationRoamedFrom.setStatus(_A)
iappStationRoamedTo=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,16))
iappStationRoamedTo.setObjects(*((_F,_J),(_F,_P)))
if mibBuilder.loadTexts:iappStationRoamedTo.setStatus(_A)
iappContextDataSent=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,17))
iappContextDataSent.setObjects(*((_F,_J),(_F,_P)))
if mibBuilder.loadTexts:iappContextDataSent.setStatus(_A)
dot1xSupplicantAuthenticated=NotificationType((1,3,6,1,4,1,14823,2,3,2,7,4,2,18))
dot1xSupplicantAuthenticated.setObjects((_F,'dot11AuthenticatorMacAddr'))
if mibBuilder.loadTexts:dot1xSupplicantAuthenticated.setStatus(_A)
sntpServerFail=NotificationType((1,3,6,1,4,1,14823,2,3,2,11,10,2,1))
if mibBuilder.loadTexts:sntpServerFail.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'MacAddress':MacAddress,_I:DisplayString,'TruthValue':TruthValue,'aruba':aruba,'arubaEnterpriseMibModules':arubaEnterpriseMibModules,'arubaAp':arubaAp,'wlsrOutDoorApMibModules':wlsrOutDoorApMibModules,'enterpriseApSys':enterpriseApSys,'swHardwareVer':swHardwareVer,'swBootRomVer':swBootRomVer,'swOpCodeVer':swOpCodeVer,'swSerialNumber':swSerialNumber,'sysNotificationTree':sysNotificationTree,'sysNotificationObjects':sysNotificationObjects,'sysNotifications':sysNotifications,'sysSystemUp':sysSystemUp,'sysSystemDown':sysSystemDown,'sysRadiusServerChanged':sysRadiusServerChanged,'sysConfigFileVersionChanged':sysConfigFileVersionChanged,'enterpriseApLineMgnt':enterpriseApLineMgnt,'lineTable':lineTable,'lineEntry':lineEntry,_S:lineIndex,'lineDataBits':lineDataBits,'lineParity':lineParity,'lineSpeed':lineSpeed,'lineStopBits':lineStopBits,'enterpriseApPortMgnt':enterpriseApPortMgnt,'portTable':portTable,'portEntry':portEntry,_T:portIndex,'portName':portName,'portType':portType,'portSpeedDpxCfg':portSpeedDpxCfg,'portFlowCtrlCfg':portFlowCtrlCfg,'portCapabilities':portCapabilities,'portAutonegotiation':portAutonegotiation,'portSpeedDpxStatus':portSpeedDpxStatus,'portFlowCtrlStatus':portFlowCtrlStatus,'enterpriseApFileTransferMgt':enterpriseApFileTransferMgt,'transferType':transferType,'fileType':fileType,'srcFile':srcFile,'destFile':destFile,'fileServer':fileServer,'userName':userName,'password':password,'status':status,'transferStart':transferStart,'enterpriseApResetMgt':enterpriseApResetMgt,'restartOpCodeFile':restartOpCodeFile,'restartControl':restartControl,'enterpriseApIpMgt':enterpriseApIpMgt,'netConfigIPAddress':netConfigIPAddress,'netConfigSubnetMask':netConfigSubnetMask,'netConfigDefaultGateway':netConfigDefaultGateway,'netConfigHttpState':netConfigHttpState,'netConfigHttpPort':netConfigHttpPort,'netConfigHttpsState':netConfigHttpsState,'netConfigHttpsPort':netConfigHttpsPort,'netConfigDHCPState':netConfigDHCPState,'enterpriseAPdot11':enterpriseAPdot11,'dot11AuthenticationEntry':dot11AuthenticationEntry,'dot118021xState':dot118021xState,'dot118021xBroadcastKeyRefreshRate':dot118021xBroadcastKeyRefreshRate,'dot118021xSessionKeyRefreshRate':dot118021xSessionKeyRefreshRate,'dot118021xReauthenticationTimeout':dot118021xReauthenticationTimeout,'dot11MACAuthenticationType':dot11MACAuthenticationType,'dot11AuthenticationServerTable':dot11AuthenticationServerTable,'dot11AuthenticationServerEntry':dot11AuthenticationServerEntry,_d:dot11AuthenticationServerIndex,'dot11AuthenticationServer':dot11AuthenticationServer,'dot11AuthenticationPort':dot11AuthenticationPort,'dot11AuthenticationKey':dot11AuthenticationKey,'dot11AuthenticationRetransmit':dot11AuthenticationRetransmit,'dot11AuthenticationTimeout':dot11AuthenticationTimeout,'dot11AuthenticationAcctPort':dot11AuthenticationAcctPort,'dot11AuthenticationAcctInterimUpdate':dot11AuthenticationAcctInterimUpdate,'dot11AuthenticationMACAddressFormat':dot11AuthenticationMACAddressFormat,'dot11AuthenticationVLANIDFormat':dot11AuthenticationVLANIDFormat,'dot11MACAuthenticationFilter':dot11MACAuthenticationFilter,'dot11FilterDefault':dot11FilterDefault,'dot11FilterTable':dot11FilterTable,'dot11FilterEntry':dot11FilterEntry,_e:dot11FilterAddress,'dot11FilterStatus':dot11FilterStatus,'dot11NotificationTree':dot11NotificationTree,'dot11NotificationObjects':dot11NotificationObjects,'dot11MacAddr':dot11MacAddr,_J:dot11Station,_y:dot11RequestType,_z:dot11ReasonCode,_P:dot11ApIpAddress,'dot1xAuthenticatorMacAddr':dot1xAuthenticatorMacAddr,'dot11Notifications':dot11Notifications,'dot11StationAssociation':dot11StationAssociation,'dot11StationReAssociation':dot11StationReAssociation,'dot11StationAuthentication':dot11StationAuthentication,'dot11StationRequestFail':dot11StationRequestFail,'dot11InterfaceBFail':dot11InterfaceBFail,'dot11InterfaceAGFail':dot11InterfaceAGFail,'dot1xMacAddrAuthSuccess':dot1xMacAddrAuthSuccess,'dot1xMacAddrAuthFail':dot1xMacAddrAuthFail,'dot1xAuthNotInitiated':dot1xAuthNotInitiated,'dot1xAuthSuccess':dot1xAuthSuccess,'dot1xAuthFail':dot1xAuthFail,'localMacAddrAuthSuccess':localMacAddrAuthSuccess,'localMacAddrAuthFail':localMacAddrAuthFail,'pppLogonFail':pppLogonFail,'iappStationRoamedFrom':iappStationRoamedFrom,'iappStationRoamedTo':iappStationRoamedTo,'iappContextDataSent':iappContextDataSent,'dot1xSupplicantAuthenticated':dot1xSupplicantAuthenticated,'dot11AuthenticationSupplicantTable':dot11AuthenticationSupplicantTable,'dot11AuthenticationSupplicantEntry':dot11AuthenticationSupplicantEntry,'dot118021xSuppIndex':dot118021xSuppIndex,'dot118021xSuppState':dot118021xSuppState,'dot118021xSuppUser':dot118021xSuppUser,'dot118021xSuppPasswd':dot118021xSuppPasswd,'dot11VapAuthenticationTable':dot11VapAuthenticationTable,'dot11VapAuthenticationEntry':dot11VapAuthenticationEntry,_f:dot11Vap8021xIndex,'dot11Vap8021xState':dot11Vap8021xState,'dot11Vap8021xBroadcastKeyRefreshRate':dot11Vap8021xBroadcastKeyRefreshRate,'dot11Vap8021xSessionKeyRefreshRate':dot11Vap8021xSessionKeyRefreshRate,'dot11Vap8021xReauthenticationTimeout':dot11Vap8021xReauthenticationTimeout,'dot11VapAuthMACAuthenticationType':dot11VapAuthMACAuthenticationType,'dot11VapAuthMACAuthenticationTimeout':dot11VapAuthMACAuthenticationTimeout,'enterpriseApAdmin':enterpriseApAdmin,'enterpriseApAdminUser':enterpriseApAdminUser,'enterpriseApAdminPassword':enterpriseApAdminPassword,'enterpriseApVLAN':enterpriseApVLAN,'enterpriseApVLANNativeId':enterpriseApVLANNativeId,'enterpriseApVLANState':enterpriseApVLANState,'enterpriseApNativeVlanTable':enterpriseApNativeVlanTable,'enterpriseApNativeVlanEntry':enterpriseApNativeVlanEntry,_g:nativeVlanIfIndex,_h:nativeVlanSsidNumber,'nativeVlanVlanId':nativeVlanVlanId,'enterpriseApFilterControl':enterpriseApFilterControl,'enterpriseApFilterControlInterClientSTAsCommun':enterpriseApFilterControlInterClientSTAsCommun,'enterpriseApFilterControlAPManage':enterpriseApFilterControlAPManage,'enterpriseApFilterControlEthernet':enterpriseApFilterControlEthernet,'enterpriseApFilterProtocolTable':enterpriseApFilterProtocolTable,'enterpriseApFilterProtocolEntry':enterpriseApFilterProtocolEntry,_i:enterpriseApFilterProtocolIndex,'enterpriseApFilterProtocolName':enterpriseApFilterProtocolName,'enterpriseApFilterProtocolISODesignator':enterpriseApFilterProtocolISODesignator,'enterpriseApFilterProtocolState':enterpriseApFilterProtocolState,'enterpriseApFilterUplinkPortMACAddrFilter':enterpriseApFilterUplinkPortMACAddrFilter,'uplinkPortMACAddrFilterStatus':uplinkPortMACAddrFilterStatus,'uplinkPortMACAddrFilterAddMac':uplinkPortMACAddrFilterAddMac,'uplinkPortMACAddrFilteringTable':uplinkPortMACAddrFilteringTable,'uplinkPortMACAddrFilteringEntry':uplinkPortMACAddrFilteringEntry,_j:uplinkPortMacAddrIndex,'uplinkPortMACAddr':uplinkPortMACAddr,'deleteMacAddr':deleteMacAddr,'enterpriseApSNTP':enterpriseApSNTP,'enterpriseApSNTPState':enterpriseApSNTPState,'enterpriseApSNTPPrimaryServer':enterpriseApSNTPPrimaryServer,'enterpriseApSNTPSecondaryServer':enterpriseApSNTPSecondaryServer,'enterpriseApSNTPTimezone':enterpriseApSNTPTimezone,'enterpriseApSNTPDST':enterpriseApSNTPDST,'enterpriseApSNTPDSTStartMonth':enterpriseApSNTPDSTStartMonth,'enterpriseApSNTPDSTStartDay':enterpriseApSNTPDSTStartDay,'enterpriseApSNTPDSTEndMonth':enterpriseApSNTPDSTEndMonth,'enterpriseApSNTPDSTEndDay':enterpriseApSNTPDSTEndDay,'sntpNotificationTree':sntpNotificationTree,'sntpNotificationObjects':sntpNotificationObjects,'sntpNotifications':sntpNotifications,'sntpServerFail':sntpServerFail,'enterpriseApDNS':enterpriseApDNS,'enterpriseApDNSPrimaryServer':enterpriseApDNSPrimaryServer,'enterpriseApDNSSecondaryServer':enterpriseApDNSSecondaryServer,'enterpriseApSyslog':enterpriseApSyslog,'enterpriseApSyslogState':enterpriseApSyslogState,'enterpriseApSyslogConsoleState':enterpriseApSyslogConsoleState,'enterpriseApSyslogLevel':enterpriseApSyslogLevel,'enterpriseApSyslogServerTable':enterpriseApSyslogServerTable,'enterpriseApSyslogServerEntry':enterpriseApSyslogServerEntry,_k:enterpriseApSyslogServerIndex,'enterpriseApSyslogServerState':enterpriseApSyslogServerState,'enterpriseApSyslogServerIPAddress':enterpriseApSyslogServerIPAddress,'enterpriseApSyslogServerPort':enterpriseApSyslogServerPort,'enterpriseApSecurity':enterpriseApSecurity,'enterpriseApSecurityTable':enterpriseApSecurityTable,'enterpriseApSecurityEntry':enterpriseApSecurityEntry,_l:enterpriseApSecurityIndex,'enterpriseApSecurityAuthType':enterpriseApSecurityAuthType,'enterpriseApSecuritySharedKeyLen':enterpriseApSecuritySharedKeyLen,'enterpriseApSecurityWPAMode':enterpriseApSecurityWPAMode,'enterpriseApSecurityWPAKeyType':enterpriseApSecurityWPAKeyType,'enterpriseApSecurityWPACipher':enterpriseApSecurityWPACipher,'enterpriseApSecurityWPAPSKType':enterpriseApSecurityWPAPSKType,'enterpriseApSecurityWPAPSK':enterpriseApSecurityWPAPSK,'enterpriseApSecurityWEPKeyType':enterpriseApSecurityWEPKeyType,'enterpriseApSecurityWEPEnabled':enterpriseApSecurityWEPEnabled,'enterpriseApSecurityWPACipherSuite':enterpriseApSecurityWPACipherSuite,'enterpriseApSecurityWPAPreAuthentication':enterpriseApSecurityWPAPreAuthentication,'enterpriseApSecurityWPAPmksaLifetime':enterpriseApSecurityWPAPmksaLifetime,'enterpriseApSsh':enterpriseApSsh,'enterpriseApSshServerEnabled':enterpriseApSshServerEnabled,'enterpriseApSshServerPort':enterpriseApSshServerPort,'enterpriseApSshTelnetServerEnabled':enterpriseApSshTelnetServerEnabled,'enterpriseApRadio':enterpriseApRadio,'enterpriseApRadioTable':enterpriseApRadioTable,'enterpriseApRadioEntry':enterpriseApRadioEntry,_O:enterpriseApRadioIndex,'enterpriseApRadioState':enterpriseApRadioState,'enterpriseApRadioAutoChannel':enterpriseApRadioAutoChannel,'enterpriseApRadioTransmitPower':enterpriseApRadioTransmitPower,'enterpriseApRadioClosedSystem':enterpriseApRadioClosedSystem,'enterpriseApRadioMaxAssoc':enterpriseApRadioMaxAssoc,'enterpriseApRadioTransmitKey':enterpriseApRadioTransmitKey,'enterpriseApRadioTurboMode':enterpriseApRadioTurboMode,'enterpriseApRadioDescription':enterpriseApRadioDescription,'enterpriseApRadioDataRate':enterpriseApRadioDataRate,'enterpriseApRadioGMode':enterpriseApRadioGMode,'enterpriseApRadioAntennaMode':enterpriseApRadioAntennaMode,'enterpriseApRadioAntennaId':enterpriseApRadioAntennaId,'enterpriseApRadioAntennaControlMethod':enterpriseApRadioAntennaControlMethod,'enterpriseApRadioAntennaLocation':enterpriseApRadioAntennaLocation,'enterpriseApRadioRogueApDetection':enterpriseApRadioRogueApDetection,'enterpriseApRadioRogueApScanInterval':enterpriseApRadioRogueApScanInterval,'enterpriseApRadioRogueApScanDuration':enterpriseApRadioRogueApScanDuration,'enterpriseApRadioRogueApScanNow':enterpriseApRadioRogueApScanNow,'enterpriseApRadioMICMode':enterpriseApRadioMICMode,'enterpriseApRadioSuperMode':enterpriseApRadioSuperMode,'enterpriseApRadioBeaconInterval':enterpriseApRadioBeaconInterval,'enterpriseApRadioDataBeaconRate':enterpriseApRadioDataBeaconRate,'enterpriseApRadioChannel':enterpriseApRadioChannel,'enterpriseApRadioFragmentLength':enterpriseApRadioFragmentLength,'enterpriseApRadioRTSThreshold':enterpriseApRadioRTSThreshold,'enterpriseApRadioAntennaGainReduction':enterpriseApRadioAntennaGainReduction,'enterpriseApSNMP':enterpriseApSNMP,'enterpriseApSNMPCommunityReadOnly':enterpriseApSNMPCommunityReadOnly,'enterpriseApSNMPCommunityReadWrite':enterpriseApSNMPCommunityReadWrite,'enterpriseApSNMPTrapDestinationTable':enterpriseApSNMPTrapDestinationTable,'enterpriseApSNMPTrapDestinationEntry':enterpriseApSNMPTrapDestinationEntry,_n:enterpriseApSNMPTrapDestinationIndex,'enterpriseApSNMPTrapDestinationCommunity':enterpriseApSNMPTrapDestinationCommunity,'enterpriseApSNMPTrapDestinationIP':enterpriseApSNMPTrapDestinationIP,'enterpriseApSNMPTrapDestinationState':enterpriseApSNMPTrapDestinationState,'enterpriseApSNMPTrapFilters':enterpriseApSNMPTrapFilters,'sysSystemUpTrapEnabled':sysSystemUpTrapEnabled,'sysSystemDownTrapEnabled':sysSystemDownTrapEnabled,'sysRadiusServerChangedTrapEnabled':sysRadiusServerChangedTrapEnabled,'sysConfigFileVersionChangedTrapEnabled':sysConfigFileVersionChangedTrapEnabled,'dot11StationAssociationTrapEnabled':dot11StationAssociationTrapEnabled,'dot11StationReAssociationTrapEnabled':dot11StationReAssociationTrapEnabled,'dot11StationAuthenticationTrapEnabled':dot11StationAuthenticationTrapEnabled,'dot11StationRequestFailTrapEnabled':dot11StationRequestFailTrapEnabled,'dot11InterfaceBFailTrapEnabled':dot11InterfaceBFailTrapEnabled,'dot11InterfaceAGFailTrapEnabled':dot11InterfaceAGFailTrapEnabled,'dot1xMacAddrAuthSuccessTrapEnabled':dot1xMacAddrAuthSuccessTrapEnabled,'dot1xMacAddrAuthFailTrapEnabled':dot1xMacAddrAuthFailTrapEnabled,'dot1xAuthNotInitiatedTrapEnabled':dot1xAuthNotInitiatedTrapEnabled,'dot1xAuthSuccessTrapEnabled':dot1xAuthSuccessTrapEnabled,'dot1xAuthFailTrapEnabled':dot1xAuthFailTrapEnabled,'localMacAddrAuthSuccessTrapEnabled':localMacAddrAuthSuccessTrapEnabled,'localMacAddrAuthFailTrapEnabled':localMacAddrAuthFailTrapEnabled,'pppLogonFailTrapEnabled':pppLogonFailTrapEnabled,'iappStationRoamedFromTrapEnabled':iappStationRoamedFromTrapEnabled,'iappStationRoamedToTrapEnabled':iappStationRoamedToTrapEnabled,'iappContextDataSentTrapEnabled':iappContextDataSentTrapEnabled,'sntpServerFailTrapEnabled':sntpServerFailTrapEnabled,'dot1xSuppAuthenticatedTrapEnabled':dot1xSuppAuthenticatedTrapEnabled,'dot11FailedTransmitsTrapEnabled':dot11FailedTransmitsTrapEnabled,'dot11AckFailuresTrapEnabled':dot11AckFailuresTrapEnabled,'dot11FcsErrorsTrapEnabled':dot11FcsErrorsTrapEnabled,'rogueAPDetectedTrapEnabled':rogueAPDetectedTrapEnabled,'possibleRogueAPDetectedTrapEnabled':possibleRogueAPDetectedTrapEnabled,'enterpriseApSession':enterpriseApSession,'enterpriseApSessionTable':enterpriseApSessionTable,'enterpriseApSessionEntry':enterpriseApSessionEntry,_o:enterpriseApSessionIfIndex,_p:enterpriseApSessionStationAddres,'enterpriseApSessionAuthenticated':enterpriseApSessionAuthenticated,'enterpriseApSessionAssociated':enterpriseApSessionAssociated,'enterpriseApSessionIsForwarding':enterpriseApSessionIsForwarding,'enterpriseApSessionKeyType':enterpriseApSessionKeyType,'enterpriseApSessionAssociationId':enterpriseApSessionAssociationId,'enterpriseApSessionLastAuthenticatedTime':enterpriseApSessionLastAuthenticatedTime,'enterpriseApSessionAssociatedTime':enterpriseApSessionAssociatedTime,'enterpriseApSessionLastAssociatedTime':enterpriseApSessionLastAssociatedTime,'enterpriseApSessionLastDisassociatedTime':enterpriseApSessionLastDisassociatedTime,'enterpriseApSessionTxPacketCount':enterpriseApSessionTxPacketCount,'enterpriseApSessionRxPacketCount':enterpriseApSessionRxPacketCount,'enterpriseApSessionTxByteCount':enterpriseApSessionTxByteCount,'enterpriseApSessionRxByteCount':enterpriseApSessionRxByteCount,'enterpriseAPVapRadio':enterpriseAPVapRadio,'enterpriseAPVapRadioTable':enterpriseAPVapRadioTable,'enterpriseAPVapRadioEntry':enterpriseAPVapRadioEntry,_q:enterpriseAPVapRadioIndex,'enterpriseAPVapRadioState':enterpriseAPVapRadioState,'enterpriseAPVapRadioClosedSystem':enterpriseAPVapRadioClosedSystem,'enterpriseAPVapRadioMaxAssoc':enterpriseAPVapRadioMaxAssoc,'enterpriseAPVapRadioTransmitKey':enterpriseAPVapRadioTransmitKey,'enterpriseAPVapRadioDescription':enterpriseAPVapRadioDescription,'enterpriseAPVapRadioAuthTimeoutInterval':enterpriseAPVapRadioAuthTimeoutInterval,'enterpriseAPVapRadioAssocTimeoutInterval':enterpriseAPVapRadioAssocTimeoutInterval,'enterpriseAPVapRadioWPA2PMKSALifeTime':enterpriseAPVapRadioWPA2PMKSALifeTime,'enterpriseApRadioWds':enterpriseApRadioWds,'enterpriseApRadioWdsTable':enterpriseApRadioWdsTable,'enterpriseApRadioWdsEntry':enterpriseApRadioWdsEntry,'wdsApRole':wdsApRole,'wdsChannelAutoSync':wdsChannelAutoSync,'wdsMasterSlaveMode':wdsMasterSlaveMode,'enterpriseApRadioWdsPeerTable':enterpriseApRadioWdsPeerTable,'enterpriseApRadioWdsPeerEntry':enterpriseApRadioWdsPeerEntry,_r:wdsPeerIndex,'wdsPeerBssid':wdsPeerBssid,'enterpriseApWMM':enterpriseApWMM,'enterpriseApWMMTable':enterpriseApWMMTable,'enterpriseApWMMEntry':enterpriseApWMMEntry,_s:enterpriseApWMMModeIndex,'enterpriseApWMMMode':enterpriseApWMMMode,'enterpriseApWMMAckPolicyTable':enterpriseApWMMAckPolicyTable,'enterpriseApWMMAckPolicyEntry':enterpriseApWMMAckPolicyEntry,_t:enterpriseApWMMAckPolicyIndex,'enterpriseApWMMACKPolicy':enterpriseApWMMACKPolicy,'enterpriseApWMMBSSParamTable':enterpriseApWMMBSSParamTable,'enterpriseApWMMBSSParamEntry':enterpriseApWMMBSSParamEntry,_u:enterpriseApWMMBSSParamIndex,'enterpriseApWMMBSSParamLogCwMin':enterpriseApWMMBSSParamLogCwMin,'enterpriseApWMMBSSParamLogCwMax':enterpriseApWMMBSSParamLogCwMax,'enterpriseApWMMBSSParamAIFSN':enterpriseApWMMBSSParamAIFSN,'enterpriseApWMMBSSParamTXOPLimit':enterpriseApWMMBSSParamTXOPLimit,'enterpriseApWMMBSSParamAdmissionCtrl':enterpriseApWMMBSSParamAdmissionCtrl,'enterpriseApWMMAPParamTable':enterpriseApWMMAPParamTable,'enterpriseApWMMAPParamEntry':enterpriseApWMMAPParamEntry,_w:enterpriseApWMMAPParamIndex,'enterpriseApWMMAPParamLogCwMin':enterpriseApWMMAPParamLogCwMin,'enterpriseApWMMAPParamLogCwMax':enterpriseApWMMAPParamLogCwMax,'enterpriseApWMMAPParamAIFSN':enterpriseApWMMAPParamAIFSN,'enterpriseApWMMAPParamTXOPLimit':enterpriseApWMMAPParamTXOPLimit,'enterpriseApWMMAPParamAdmissionCtrl':enterpriseApWMMAPParamAdmissionCtrl,'enterpriseApSTP':enterpriseApSTP,'enterpriseApSTPBridgeStatus':enterpriseApSTPBridgeStatus,'enterpriseApSTPBridgePriority':enterpriseApSTPBridgePriority,'enterpriseApSTPBridgeMaxAge':enterpriseApSTPBridgeMaxAge,'enterpriseApSTPHelloTime':enterpriseApSTPHelloTime,'enterpriseApSTPBridgeForwardingDelay':enterpriseApSTPBridgeForwardingDelay,'enterpriseApSTPRadioInterface':enterpriseApSTPRadioInterface,'enterpriseApSTPNodeTable':enterpriseApSTPNodeTable,'enterpriseApSTPNodeEntry':enterpriseApSTPNodeEntry,_x:enterpriseApSTPNodeIndex,'enterpriseApSTPNodeLinkPathCost':enterpriseApSTPNodeLinkPathCost,'enterpriseApSTPNodeLinkPortPriority':enterpriseApSTPNodeLinkPortPriority,'enterpriseApSTPEthernetInterface':enterpriseApSTPEthernetInterface,'enterpriseApSTPEthernetLinkPathCost':enterpriseApSTPEthernetLinkPathCost,'enterpriseApSTPEthernetLinkPortPriority':enterpriseApSTPEthernetLinkPortPriority})