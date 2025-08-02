_k='apNotificationDot11ReasonCode'
_j='apNotificationDot11RequestType'
_i='rogueApIndex'
_h='wdsPeerIndex'
_g='enterpriseApVapRadioIndex'
_f='alphanumeric'
_e='enterpriseApSecurityIndex'
_d='dot118021xSuppIndex'
_c='dot11FilterAddress'
_b='dot11AuthenticationServerIndex'
_a='required'
_Z='supported'
_Y='running'
_X='dot3xFlowControl'
_W='backPressure'
_V='fullDuplex1000'
_U='halfDuplex1000'
_T='fullDuplex100'
_S='halfDuplex100'
_R='fullDuplex10'
_Q='halfDuplex10'
_P='portIndex'
_O='lineIndex'
_N='invalid'
_M='none'
_L='apNotificationDot11IpAddress'
_K='enterpriseApRadioIndex'
_J='enabled'
_I='apNotificationDot11Station'
_H='not-accessible'
_G='disabled'
_F='DisplayString'
_E='read-only'
_D='A3COM-PRIVATE-MIB'
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
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
rivet=ModuleIdentity((1,3,6,1,4,1,43,35,8))
if mibBuilder.loadTexts:rivet.setRevisions(('2004-04-27 07:55','2004-09-01 00:00','2004-10-12 00:00'))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_Wlan_mib_ObjectIdentity=ObjectIdentity
wlan_mib=_Wlan_mib_ObjectIdentity((1,3,6,1,4,1,43,35))
_EnterpriseApSys_ObjectIdentity=ObjectIdentity
enterpriseApSys=_EnterpriseApSys_ObjectIdentity((1,3,6,1,4,1,43,35,8,1))
class _SwHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwHardwareVer_Type.__name__=_F
_SwHardwareVer_Object=MibScalar
swHardwareVer=_SwHardwareVer_Object((1,3,6,1,4,1,43,35,8,1,1),_SwHardwareVer_Type())
swHardwareVer.setMaxAccess(_E)
if mibBuilder.loadTexts:swHardwareVer.setStatus(_A)
class _SwBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBootRomVer_Type.__name__=_F
_SwBootRomVer_Object=MibScalar
swBootRomVer=_SwBootRomVer_Object((1,3,6,1,4,1,43,35,8,1,2),_SwBootRomVer_Type())
swBootRomVer.setMaxAccess(_E)
if mibBuilder.loadTexts:swBootRomVer.setStatus(_A)
class _SwOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwOpCodeVer_Type.__name__=_F
_SwOpCodeVer_Object=MibScalar
swOpCodeVer=_SwOpCodeVer_Object((1,3,6,1,4,1,43,35,8,1,3),_SwOpCodeVer_Type())
swOpCodeVer.setMaxAccess(_E)
if mibBuilder.loadTexts:swOpCodeVer.setStatus(_A)
class _SwSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwSerialNumber_Type.__name__=_F
_SwSerialNumber_Object=MibScalar
swSerialNumber=_SwSerialNumber_Object((1,3,6,1,4,1,43,35,8,1,4),_SwSerialNumber_Type())
swSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:swSerialNumber.setStatus(_A)
_EnterpriseApLineMgnt_ObjectIdentity=ObjectIdentity
enterpriseApLineMgnt=_EnterpriseApLineMgnt_ObjectIdentity((1,3,6,1,4,1,43,35,8,2))
_LineTable_Object=MibTable
lineTable=_LineTable_Object((1,3,6,1,4,1,43,35,8,2,1))
if mibBuilder.loadTexts:lineTable.setStatus(_A)
_LineEntry_Object=MibTableRow
lineEntry=_LineEntry_Object((1,3,6,1,4,1,43,35,8,2,1,1))
lineEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:lineEntry.setStatus(_A)
_LineIndex_Type=Integer32
_LineIndex_Object=MibTableColumn
lineIndex=_LineIndex_Object((1,3,6,1,4,1,43,35,8,2,1,1,1),_LineIndex_Type())
lineIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lineIndex.setStatus(_A)
_LineDataBits_Type=Integer32
_LineDataBits_Object=MibTableColumn
lineDataBits=_LineDataBits_Object((1,3,6,1,4,1,43,35,8,2,1,1,2),_LineDataBits_Type())
lineDataBits.setMaxAccess(_E)
if mibBuilder.loadTexts:lineDataBits.setStatus(_A)
class _LineParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('odd',1),('even',2),(_M,99)))
_LineParity_Type.__name__=_C
_LineParity_Object=MibTableColumn
lineParity=_LineParity_Object((1,3,6,1,4,1,43,35,8,2,1,1,3),_LineParity_Type())
lineParity.setMaxAccess(_E)
if mibBuilder.loadTexts:lineParity.setStatus(_A)
_LineSpeed_Type=Integer32
_LineSpeed_Object=MibTableColumn
lineSpeed=_LineSpeed_Object((1,3,6,1,4,1,43,35,8,2,1,1,4),_LineSpeed_Type())
lineSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:lineSpeed.setStatus(_A)
_LineStopBits_Type=Integer32
_LineStopBits_Object=MibTableColumn
lineStopBits=_LineStopBits_Object((1,3,6,1,4,1,43,35,8,2,1,1,5),_LineStopBits_Type())
lineStopBits.setMaxAccess(_E)
if mibBuilder.loadTexts:lineStopBits.setStatus(_A)
_EnterpriseApPortMgnt_ObjectIdentity=ObjectIdentity
enterpriseApPortMgnt=_EnterpriseApPortMgnt_ObjectIdentity((1,3,6,1,4,1,43,35,8,3))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,43,35,8,3,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,43,35,8,3,1,1))
portEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,43,35,8,3,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_F
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,43,35,8,3,1,1,2),_PortName_Type())
portName.setMaxAccess(_E)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),('thousandBaseT',6),('thousandBaseGBIC',7),('thousandBaseMiniGBIC',8)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,43,35,8,3,1,1,3),_PortType_Type())
portType.setMaxAccess(_E)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reserved',1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7)))
_PortSpeedDpxCfg_Type.__name__=_C
_PortSpeedDpxCfg_Object=MibTableColumn
portSpeedDpxCfg=_PortSpeedDpxCfg_Object((1,3,6,1,4,1,43,35,8,3,1,1,4),_PortSpeedDpxCfg_Type())
portSpeedDpxCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:portSpeedDpxCfg.setStatus(_A)
class _PortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_G,2),(_W,3),(_X,4)))
_PortFlowCtrlCfg_Type.__name__=_C
_PortFlowCtrlCfg_Object=MibTableColumn
portFlowCtrlCfg=_PortFlowCtrlCfg_Object((1,3,6,1,4,1,43,35,8,3,1,1,5),_PortFlowCtrlCfg_Type())
portFlowCtrlCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:portFlowCtrlCfg.setStatus(_A)
class _PortCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,99)));namedValues=NamedValues(*(('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('reserved6',6),('reserved7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('portCapSym',14),('portCapFlowCtrl',15),('portCap10half',99)))
_PortCapabilities_Type.__name__=_C
_PortCapabilities_Object=MibTableColumn
portCapabilities=_PortCapabilities_Object((1,3,6,1,4,1,43,35,8,3,1,1,6),_PortCapabilities_Type())
portCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:portCapabilities.setStatus(_A)
class _PortAutonegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_PortAutonegotiation_Type.__name__=_C
_PortAutonegotiation_Object=MibTableColumn
portAutonegotiation=_PortAutonegotiation_Object((1,3,6,1,4,1,43,35,8,3,1,1,7),_PortAutonegotiation_Type())
portAutonegotiation.setMaxAccess(_E)
if mibBuilder.loadTexts:portAutonegotiation.setStatus(_A)
class _PortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('error',1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7)))
_PortSpeedDpxStatus_Type.__name__=_C
_PortSpeedDpxStatus_Object=MibTableColumn
portSpeedDpxStatus=_PortSpeedDpxStatus_Object((1,3,6,1,4,1,43,35,8,3,1,1,8),_PortSpeedDpxStatus_Type())
portSpeedDpxStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portSpeedDpxStatus.setStatus(_A)
class _PortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('error',1),(_W,2),(_X,3),(_M,4)))
_PortFlowCtrlStatus_Type.__name__=_C
_PortFlowCtrlStatus_Object=MibTableColumn
portFlowCtrlStatus=_PortFlowCtrlStatus_Object((1,3,6,1,4,1,43,35,8,3,1,1,9),_PortFlowCtrlStatus_Type())
portFlowCtrlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portFlowCtrlStatus.setStatus(_A)
_EnterpriseApFileTransferMgt_ObjectIdentity=ObjectIdentity
enterpriseApFileTransferMgt=_EnterpriseApFileTransferMgt_ObjectIdentity((1,3,6,1,4,1,43,35,8,4))
class _TransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftp',1),('tftp',2)))
_TransferType_Type.__name__=_C
_TransferType_Object=MibScalar
transferType=_TransferType_Object((1,3,6,1,4,1,43,35,8,4,1),_TransferType_Type())
transferType.setMaxAccess(_B)
if mibBuilder.loadTexts:transferType.setStatus(_A)
class _FileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('application',1),('config',2)))
_FileType_Type.__name__=_C
_FileType_Object=MibScalar
fileType=_FileType_Object((1,3,6,1,4,1,43,35,8,4,2),_FileType_Type())
fileType.setMaxAccess(_B)
if mibBuilder.loadTexts:fileType.setStatus(_A)
class _SrcFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SrcFile_Type.__name__=_F
_SrcFile_Object=MibScalar
srcFile=_SrcFile_Object((1,3,6,1,4,1,43,35,8,4,3),_SrcFile_Type())
srcFile.setMaxAccess(_B)
if mibBuilder.loadTexts:srcFile.setStatus(_A)
class _DestFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DestFile_Type.__name__=_F
_DestFile_Object=MibScalar
destFile=_DestFile_Object((1,3,6,1,4,1,43,35,8,4,4),_DestFile_Type())
destFile.setMaxAccess(_B)
if mibBuilder.loadTexts:destFile.setStatus(_A)
_FileServer_Type=IpAddress
_FileServer_Object=MibScalar
fileServer=_FileServer_Object((1,3,6,1,4,1,43,35,8,4,5),_FileServer_Type())
fileServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fileServer.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_UserName_Type.__name__=_F
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,43,35,8,4,6),_UserName_Type())
userName.setMaxAccess(_B)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _Password_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Password_Type.__name__=_F
_Password_Object=MibScalar
password=_Password_Object((1,3,6,1,4,1,43,35,8,4,7),_Password_Type())
password.setMaxAccess(_B)
if mibBuilder.loadTexts:password.setStatus(_A)
class _Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,11,12,13,20,30)));namedValues=NamedValues(*((_Y,1),('success',2),('failureGeneric',3),('flashOpenError',10),('flashMallocError',11),('flashReadError',12),('flashFtypeError',13),('socketWriteError',20),('protocolError',30)))
_Status_Type.__name__=_C
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,43,35,8,4,8),_Status_Type())
status.setMaxAccess(_E)
if mibBuilder.loadTexts:status.setStatus(_A)
class _TransferStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('download',1),('upload',2)))
_TransferStart_Type.__name__=_C
_TransferStart_Object=MibScalar
transferStart=_TransferStart_Object((1,3,6,1,4,1,43,35,8,4,9),_TransferStart_Type())
transferStart.setMaxAccess(_B)
if mibBuilder.loadTexts:transferStart.setStatus(_A)
_EnterpriseApResetMgt_ObjectIdentity=ObjectIdentity
enterpriseApResetMgt=_EnterpriseApResetMgt_ObjectIdentity((1,3,6,1,4,1,43,35,8,5))
class _RestartOpCodeFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RestartOpCodeFile_Type.__name__=_F
_RestartOpCodeFile_Object=MibScalar
restartOpCodeFile=_RestartOpCodeFile_Object((1,3,6,1,4,1,43,35,8,5,1),_RestartOpCodeFile_Type())
restartOpCodeFile.setMaxAccess(_B)
if mibBuilder.loadTexts:restartOpCodeFile.setStatus(_A)
class _RestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),('warmBoot',2),('coldBoot',3)))
_RestartControl_Type.__name__=_C
_RestartControl_Object=MibScalar
restartControl=_RestartControl_Object((1,3,6,1,4,1,43,35,8,5,2),_RestartControl_Type())
restartControl.setMaxAccess(_B)
if mibBuilder.loadTexts:restartControl.setStatus(_A)
_EnterpriseApIpMgt_ObjectIdentity=ObjectIdentity
enterpriseApIpMgt=_EnterpriseApIpMgt_ObjectIdentity((1,3,6,1,4,1,43,35,8,6))
_NetConfigIPAddress_Type=IpAddress
_NetConfigIPAddress_Object=MibScalar
netConfigIPAddress=_NetConfigIPAddress_Object((1,3,6,1,4,1,43,35,8,6,1),_NetConfigIPAddress_Type())
netConfigIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigIPAddress.setStatus(_A)
_NetConfigSubnetMask_Type=IpAddress
_NetConfigSubnetMask_Object=MibScalar
netConfigSubnetMask=_NetConfigSubnetMask_Object((1,3,6,1,4,1,43,35,8,6,2),_NetConfigSubnetMask_Type())
netConfigSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigSubnetMask.setStatus(_A)
_NetConfigDefaultGateway_Type=IpAddress
_NetConfigDefaultGateway_Object=MibScalar
netConfigDefaultGateway=_NetConfigDefaultGateway_Object((1,3,6,1,4,1,43,35,8,6,3),_NetConfigDefaultGateway_Type())
netConfigDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigDefaultGateway.setStatus(_A)
class _NetConfigHttpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_NetConfigHttpState_Type.__name__=_C
_NetConfigHttpState_Object=MibScalar
netConfigHttpState=_NetConfigHttpState_Object((1,3,6,1,4,1,43,35,8,6,4),_NetConfigHttpState_Type())
netConfigHttpState.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpState.setStatus(_A)
class _NetConfigHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_NetConfigHttpPort_Type.__name__=_C
_NetConfigHttpPort_Object=MibScalar
netConfigHttpPort=_NetConfigHttpPort_Object((1,3,6,1,4,1,43,35,8,6,5),_NetConfigHttpPort_Type())
netConfigHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpPort.setStatus(_A)
class _NetConfigHttpsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_NetConfigHttpsState_Type.__name__=_C
_NetConfigHttpsState_Object=MibScalar
netConfigHttpsState=_NetConfigHttpsState_Object((1,3,6,1,4,1,43,35,8,6,6),_NetConfigHttpsState_Type())
netConfigHttpsState.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpsState.setStatus(_A)
class _NetConfigHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_NetConfigHttpsPort_Type.__name__=_C
_NetConfigHttpsPort_Object=MibScalar
netConfigHttpsPort=_NetConfigHttpsPort_Object((1,3,6,1,4,1,43,35,8,6,7),_NetConfigHttpsPort_Type())
netConfigHttpsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigHttpsPort.setStatus(_A)
class _NetConfigDHCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_NetConfigDHCPState_Type.__name__=_C
_NetConfigDHCPState_Object=MibScalar
netConfigDHCPState=_NetConfigDHCPState_Object((1,3,6,1,4,1,43,35,8,6,8),_NetConfigDHCPState_Type())
netConfigDHCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigDHCPState.setStatus(_A)
_EnterpriseAPdot11_ObjectIdentity=ObjectIdentity
enterpriseAPdot11=_EnterpriseAPdot11_ObjectIdentity((1,3,6,1,4,1,43,35,8,7))
_Dot11AuthenticationEntry_ObjectIdentity=ObjectIdentity
dot11AuthenticationEntry=_Dot11AuthenticationEntry_ObjectIdentity((1,3,6,1,4,1,43,35,8,7,5))
class _Dot118021xState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_Z,1),(_a,2)))
_Dot118021xState_Type.__name__=_C
_Dot118021xState_Object=MibScalar
dot118021xState=_Dot118021xState_Object((1,3,6,1,4,1,43,35,8,7,5,1),_Dot118021xState_Type())
dot118021xState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xState.setStatus(_A)
class _Dot118021xBroadcastKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot118021xBroadcastKeyRefreshRate_Type.__name__=_C
_Dot118021xBroadcastKeyRefreshRate_Object=MibScalar
dot118021xBroadcastKeyRefreshRate=_Dot118021xBroadcastKeyRefreshRate_Object((1,3,6,1,4,1,43,35,8,7,5,2),_Dot118021xBroadcastKeyRefreshRate_Type())
dot118021xBroadcastKeyRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xBroadcastKeyRefreshRate.setStatus(_A)
class _Dot118021xSessionKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot118021xSessionKeyRefreshRate_Type.__name__=_C
_Dot118021xSessionKeyRefreshRate_Object=MibScalar
dot118021xSessionKeyRefreshRate=_Dot118021xSessionKeyRefreshRate_Object((1,3,6,1,4,1,43,35,8,7,5,3),_Dot118021xSessionKeyRefreshRate_Type())
dot118021xSessionKeyRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSessionKeyRefreshRate.setStatus(_A)
class _Dot118021xReauthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Dot118021xReauthenticationTimeout_Type.__name__=_C
_Dot118021xReauthenticationTimeout_Object=MibScalar
dot118021xReauthenticationTimeout=_Dot118021xReauthenticationTimeout_Object((1,3,6,1,4,1,43,35,8,7,5,4),_Dot118021xReauthenticationTimeout_Type())
dot118021xReauthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xReauthenticationTimeout.setStatus(_A)
class _Dot11MACAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('local',1),('radius',2)))
_Dot11MACAuthenticationType_Type.__name__=_C
_Dot11MACAuthenticationType_Object=MibScalar
dot11MACAuthenticationType=_Dot11MACAuthenticationType_Object((1,3,6,1,4,1,43,35,8,7,5,5),_Dot11MACAuthenticationType_Type())
dot11MACAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11MACAuthenticationType.setStatus(_A)
_Dot11AuthenticationServerTable_Object=MibTable
dot11AuthenticationServerTable=_Dot11AuthenticationServerTable_Object((1,3,6,1,4,1,43,35,8,7,6))
if mibBuilder.loadTexts:dot11AuthenticationServerTable.setStatus(_A)
_Dot11AuthenticationServerEntry_Object=MibTableRow
dot11AuthenticationServerEntry=_Dot11AuthenticationServerEntry_Object((1,3,6,1,4,1,43,35,8,7,6,1))
dot11AuthenticationServerEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:dot11AuthenticationServerEntry.setStatus(_A)
_Dot11AuthenticationServerIndex_Type=Integer32
_Dot11AuthenticationServerIndex_Object=MibTableColumn
dot11AuthenticationServerIndex=_Dot11AuthenticationServerIndex_Object((1,3,6,1,4,1,43,35,8,7,6,1,1),_Dot11AuthenticationServerIndex_Type())
dot11AuthenticationServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11AuthenticationServerIndex.setStatus(_A)
_Dot11AuthenticationServer_Type=IpAddress
_Dot11AuthenticationServer_Object=MibTableColumn
dot11AuthenticationServer=_Dot11AuthenticationServer_Object((1,3,6,1,4,1,43,35,8,7,6,1,2),_Dot11AuthenticationServer_Type())
dot11AuthenticationServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationServer.setStatus(_A)
class _Dot11AuthenticationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_Dot11AuthenticationPort_Type.__name__=_C
_Dot11AuthenticationPort_Object=MibTableColumn
dot11AuthenticationPort=_Dot11AuthenticationPort_Object((1,3,6,1,4,1,43,35,8,7,6,1,3),_Dot11AuthenticationPort_Type())
dot11AuthenticationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationPort.setStatus(_A)
class _Dot11AuthenticationKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Dot11AuthenticationKey_Type.__name__=_F
_Dot11AuthenticationKey_Object=MibTableColumn
dot11AuthenticationKey=_Dot11AuthenticationKey_Object((1,3,6,1,4,1,43,35,8,7,6,1,4),_Dot11AuthenticationKey_Type())
dot11AuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationKey.setStatus(_A)
class _Dot11AuthenticationRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_Dot11AuthenticationRetransmit_Type.__name__=_C
_Dot11AuthenticationRetransmit_Object=MibTableColumn
dot11AuthenticationRetransmit=_Dot11AuthenticationRetransmit_Object((1,3,6,1,4,1,43,35,8,7,6,1,5),_Dot11AuthenticationRetransmit_Type())
dot11AuthenticationRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationRetransmit.setStatus(_A)
class _Dot11AuthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Dot11AuthenticationTimeout_Type.__name__=_C
_Dot11AuthenticationTimeout_Object=MibTableColumn
dot11AuthenticationTimeout=_Dot11AuthenticationTimeout_Object((1,3,6,1,4,1,43,35,8,7,6,1,6),_Dot11AuthenticationTimeout_Type())
dot11AuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationTimeout.setStatus(_A)
class _Dot11AuthenticationAcctPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_Dot11AuthenticationAcctPort_Type.__name__=_C
_Dot11AuthenticationAcctPort_Object=MibTableColumn
dot11AuthenticationAcctPort=_Dot11AuthenticationAcctPort_Object((1,3,6,1,4,1,43,35,8,7,6,1,7),_Dot11AuthenticationAcctPort_Type())
dot11AuthenticationAcctPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationAcctPort.setStatus(_A)
class _Dot11AuthenticationInterimUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_Dot11AuthenticationInterimUpdate_Type.__name__=_C
_Dot11AuthenticationInterimUpdate_Object=MibTableColumn
dot11AuthenticationInterimUpdate=_Dot11AuthenticationInterimUpdate_Object((1,3,6,1,4,1,43,35,8,7,6,1,8),_Dot11AuthenticationInterimUpdate_Type())
dot11AuthenticationInterimUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationInterimUpdate.setStatus(_A)
_Dot11Filter_ObjectIdentity=ObjectIdentity
dot11Filter=_Dot11Filter_ObjectIdentity((1,3,6,1,4,1,43,35,8,7,7))
class _Dot11FilterDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_Dot11FilterDefault_Type.__name__=_C
_Dot11FilterDefault_Object=MibScalar
dot11FilterDefault=_Dot11FilterDefault_Object((1,3,6,1,4,1,43,35,8,7,7,1),_Dot11FilterDefault_Type())
dot11FilterDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FilterDefault.setStatus(_A)
_Dot11FilterTable_Object=MibTable
dot11FilterTable=_Dot11FilterTable_Object((1,3,6,1,4,1,43,35,8,7,7,2))
if mibBuilder.loadTexts:dot11FilterTable.setStatus(_A)
_Dot11FilterEntry_Object=MibTableRow
dot11FilterEntry=_Dot11FilterEntry_Object((1,3,6,1,4,1,43,35,8,7,7,2,1))
dot11FilterEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:dot11FilterEntry.setStatus(_A)
_Dot11FilterAddress_Type=MacAddress
_Dot11FilterAddress_Object=MibTableColumn
dot11FilterAddress=_Dot11FilterAddress_Object((1,3,6,1,4,1,43,35,8,7,7,2,1,1),_Dot11FilterAddress_Type())
dot11FilterAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:dot11FilterAddress.setStatus(_A)
class _Dot11FilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(30,31,32)));namedValues=NamedValues(*(('allowed',30),('denied',31),('delete',32)))
_Dot11FilterStatus_Type.__name__=_C
_Dot11FilterStatus_Object=MibTableColumn
dot11FilterStatus=_Dot11FilterStatus_Object((1,3,6,1,4,1,43,35,8,7,7,2,1,2),_Dot11FilterStatus_Type())
dot11FilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FilterStatus.setStatus(_A)
_Dot11AuthenticationSupplicantTable_Object=MibTable
dot11AuthenticationSupplicantTable=_Dot11AuthenticationSupplicantTable_Object((1,3,6,1,4,1,43,35,8,7,8))
if mibBuilder.loadTexts:dot11AuthenticationSupplicantTable.setStatus(_A)
_Dot11AuthenticationSupplicantEntry_Object=MibTableRow
dot11AuthenticationSupplicantEntry=_Dot11AuthenticationSupplicantEntry_Object((1,3,6,1,4,1,43,35,8,7,8,1))
dot11AuthenticationSupplicantEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:dot11AuthenticationSupplicantEntry.setStatus(_A)
_Dot118021xSuppIndex_Type=Integer32
_Dot118021xSuppIndex_Object=MibTableColumn
dot118021xSuppIndex=_Dot118021xSuppIndex_Object((1,3,6,1,4,1,43,35,8,7,8,1,1),_Dot118021xSuppIndex_Type())
dot118021xSuppIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dot118021xSuppIndex.setStatus(_A)
class _Dot118021xSuppState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_J,1)))
_Dot118021xSuppState_Type.__name__=_C
_Dot118021xSuppState_Object=MibTableColumn
dot118021xSuppState=_Dot118021xSuppState_Object((1,3,6,1,4,1,43,35,8,7,8,1,2),_Dot118021xSuppState_Type())
dot118021xSuppState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSuppState.setStatus(_A)
class _Dot118021xSuppUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Dot118021xSuppUser_Type.__name__=_F
_Dot118021xSuppUser_Object=MibTableColumn
dot118021xSuppUser=_Dot118021xSuppUser_Object((1,3,6,1,4,1,43,35,8,7,8,1,3),_Dot118021xSuppUser_Type())
dot118021xSuppUser.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSuppUser.setStatus(_A)
class _Dot118021xSuppPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Dot118021xSuppPasswd_Type.__name__=_F
_Dot118021xSuppPasswd_Object=MibTableColumn
dot118021xSuppPasswd=_Dot118021xSuppPasswd_Object((1,3,6,1,4,1,43,35,8,7,8,1,4),_Dot118021xSuppPasswd_Type())
dot118021xSuppPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:dot118021xSuppPasswd.setStatus(_A)
_EnterpriseApAdmin_ObjectIdentity=ObjectIdentity
enterpriseApAdmin=_EnterpriseApAdmin_ObjectIdentity((1,3,6,1,4,1,43,35,8,8))
class _EnterpriseApAdminUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,16))
_EnterpriseApAdminUser_Type.__name__=_F
_EnterpriseApAdminUser_Object=MibScalar
enterpriseApAdminUser=_EnterpriseApAdminUser_Object((1,3,6,1,4,1,43,35,8,8,1),_EnterpriseApAdminUser_Type())
enterpriseApAdminUser.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApAdminUser.setStatus(_A)
class _EnterpriseApAdminPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,16))
_EnterpriseApAdminPassword_Type.__name__=_F
_EnterpriseApAdminPassword_Object=MibScalar
enterpriseApAdminPassword=_EnterpriseApAdminPassword_Object((1,3,6,1,4,1,43,35,8,8,2),_EnterpriseApAdminPassword_Type())
enterpriseApAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApAdminPassword.setStatus(_A)
_EnterpriseApSecurity_ObjectIdentity=ObjectIdentity
enterpriseApSecurity=_EnterpriseApSecurity_ObjectIdentity((1,3,6,1,4,1,43,35,8,9))
_EnterpriseApSecurityTable_Object=MibTable
enterpriseApSecurityTable=_EnterpriseApSecurityTable_Object((1,3,6,1,4,1,43,35,8,9,1))
if mibBuilder.loadTexts:enterpriseApSecurityTable.setStatus(_A)
_EnterpriseApSecurityEntry_Object=MibTableRow
enterpriseApSecurityEntry=_EnterpriseApSecurityEntry_Object((1,3,6,1,4,1,43,35,8,9,1,1))
enterpriseApSecurityEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:enterpriseApSecurityEntry.setStatus(_A)
_EnterpriseApSecurityIndex_Type=Integer32
_EnterpriseApSecurityIndex_Object=MibTableColumn
enterpriseApSecurityIndex=_EnterpriseApSecurityIndex_Object((1,3,6,1,4,1,43,35,8,9,1,1,1),_EnterpriseApSecurityIndex_Type())
enterpriseApSecurityIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApSecurityIndex.setStatus(_A)
class _EnterpriseApSecurityAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),('shared',1)))
_EnterpriseApSecurityAuthType_Type.__name__=_C
_EnterpriseApSecurityAuthType_Object=MibTableColumn
enterpriseApSecurityAuthType=_EnterpriseApSecurityAuthType_Object((1,3,6,1,4,1,43,35,8,9,1,1,2),_EnterpriseApSecurityAuthType_Type())
enterpriseApSecurityAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityAuthType.setStatus(_A)
class _EnterpriseApSecuritySharedKeyLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('sixtyFour',1),('oneHundredTwentyEight',2),('oneHundredFiftyTwo',3)))
_EnterpriseApSecuritySharedKeyLen_Type.__name__=_C
_EnterpriseApSecuritySharedKeyLen_Object=MibTableColumn
enterpriseApSecuritySharedKeyLen=_EnterpriseApSecuritySharedKeyLen_Object((1,3,6,1,4,1,43,35,8,9,1,1,3),_EnterpriseApSecuritySharedKeyLen_Type())
enterpriseApSecuritySharedKeyLen.setMaxAccess(_E)
if mibBuilder.loadTexts:enterpriseApSecuritySharedKeyLen.setStatus(_A)
class _EnterpriseApSecurityWPAMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),(_a,1),(_G,2)))
_EnterpriseApSecurityWPAMode_Type.__name__=_C
_EnterpriseApSecurityWPAMode_Object=MibTableColumn
enterpriseApSecurityWPAMode=_EnterpriseApSecurityWPAMode_Object((1,3,6,1,4,1,43,35,8,9,1,1,4),_EnterpriseApSecurityWPAMode_Type())
enterpriseApSecurityWPAMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAMode.setStatus(_A)
class _EnterpriseApSecurityWPAKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dot1x',0),('presharedkey',1)))
_EnterpriseApSecurityWPAKeyType_Type.__name__=_C
_EnterpriseApSecurityWPAKeyType_Object=MibTableColumn
enterpriseApSecurityWPAKeyType=_EnterpriseApSecurityWPAKeyType_Object((1,3,6,1,4,1,43,35,8,9,1,1,5),_EnterpriseApSecurityWPAKeyType_Type())
enterpriseApSecurityWPAKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAKeyType.setStatus(_A)
class _EnterpriseApSecurityWPACipher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('wep',0),('tkip',1),('aes',2)))
_EnterpriseApSecurityWPACipher_Type.__name__=_C
_EnterpriseApSecurityWPACipher_Object=MibTableColumn
enterpriseApSecurityWPACipher=_EnterpriseApSecurityWPACipher_Object((1,3,6,1,4,1,43,35,8,9,1,1,6),_EnterpriseApSecurityWPACipher_Type())
enterpriseApSecurityWPACipher.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPACipher.setStatus(_A)
class _EnterpriseApSecurityWPAPSKType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hex',0),(_f,1)))
_EnterpriseApSecurityWPAPSKType_Type.__name__=_C
_EnterpriseApSecurityWPAPSKType_Object=MibTableColumn
enterpriseApSecurityWPAPSKType=_EnterpriseApSecurityWPAPSKType_Object((1,3,6,1,4,1,43,35,8,9,1,1,7),_EnterpriseApSecurityWPAPSKType_Type())
enterpriseApSecurityWPAPSKType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAPSKType.setStatus(_A)
class _EnterpriseApSecurityWPAPSK_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EnterpriseApSecurityWPAPSK_Type.__name__=_F
_EnterpriseApSecurityWPAPSK_Object=MibTableColumn
enterpriseApSecurityWPAPSK=_EnterpriseApSecurityWPAPSK_Object((1,3,6,1,4,1,43,35,8,9,1,1,8),_EnterpriseApSecurityWPAPSK_Type())
enterpriseApSecurityWPAPSK.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWPAPSK.setStatus(_A)
class _EnterpriseApSecurityWEPKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hexadecimal',0),(_f,1)))
_EnterpriseApSecurityWEPKeyType_Type.__name__=_C
_EnterpriseApSecurityWEPKeyType_Object=MibTableColumn
enterpriseApSecurityWEPKeyType=_EnterpriseApSecurityWEPKeyType_Object((1,3,6,1,4,1,43,35,8,9,1,1,9),_EnterpriseApSecurityWEPKeyType_Type())
enterpriseApSecurityWEPKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWEPKeyType.setStatus(_A)
_EnterpriseApSecurityWEPEnabled_Type=TruthValue
_EnterpriseApSecurityWEPEnabled_Object=MibTableColumn
enterpriseApSecurityWEPEnabled=_EnterpriseApSecurityWEPEnabled_Object((1,3,6,1,4,1,43,35,8,9,1,1,10),_EnterpriseApSecurityWEPEnabled_Type())
enterpriseApSecurityWEPEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApSecurityWEPEnabled.setStatus(_A)
_EnterpriseApRadio_ObjectIdentity=ObjectIdentity
enterpriseApRadio=_EnterpriseApRadio_ObjectIdentity((1,3,6,1,4,1,43,35,8,10))
_EnterpriseApRadioTable_Object=MibTable
enterpriseApRadioTable=_EnterpriseApRadioTable_Object((1,3,6,1,4,1,43,35,8,10,1))
if mibBuilder.loadTexts:enterpriseApRadioTable.setStatus(_A)
_EnterpriseApRadioEntry_Object=MibTableRow
enterpriseApRadioEntry=_EnterpriseApRadioEntry_Object((1,3,6,1,4,1,43,35,8,10,1,1))
enterpriseApRadioEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:enterpriseApRadioEntry.setStatus(_A)
_EnterpriseApRadioIndex_Type=Integer32
_EnterpriseApRadioIndex_Object=MibTableColumn
enterpriseApRadioIndex=_EnterpriseApRadioIndex_Object((1,3,6,1,4,1,43,35,8,10,1,1,1),_EnterpriseApRadioIndex_Type())
enterpriseApRadioIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApRadioIndex.setStatus(_A)
class _EnterpriseApRadioAutoChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_EnterpriseApRadioAutoChannel_Type.__name__=_C
_EnterpriseApRadioAutoChannel_Object=MibTableColumn
enterpriseApRadioAutoChannel=_EnterpriseApRadioAutoChannel_Object((1,3,6,1,4,1,43,35,8,10,1,1,2),_EnterpriseApRadioAutoChannel_Type())
enterpriseApRadioAutoChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioAutoChannel.setStatus(_A)
class _EnterpriseApRadioTransmitPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('full',1),('half',2),('middle',3),('quarter',4),('eighth',5),('min',6)))
_EnterpriseApRadioTransmitPower_Type.__name__=_C
_EnterpriseApRadioTransmitPower_Object=MibTableColumn
enterpriseApRadioTransmitPower=_EnterpriseApRadioTransmitPower_Object((1,3,6,1,4,1,43,35,8,10,1,1,3),_EnterpriseApRadioTransmitPower_Type())
enterpriseApRadioTransmitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioTransmitPower.setStatus(_A)
class _EnterpriseApRadioTurboMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_G,2),(_N,3)))
_EnterpriseApRadioTurboMode_Type.__name__=_C
_EnterpriseApRadioTurboMode_Object=MibTableColumn
enterpriseApRadioTurboMode=_EnterpriseApRadioTurboMode_Object((1,3,6,1,4,1,43,35,8,10,1,1,4),_EnterpriseApRadioTurboMode_Type())
enterpriseApRadioTurboMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioTurboMode.setStatus(_A)
class _EnterpriseApRadioDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,9,11,12,18,24,36,48,54,255)));namedValues=NamedValues(*(('oneMbps',1),('twoMbps',2),('fiveAndHalfMbps',5),('sixMbps',6),('nineMbps',9),('elevenMbps',11),('twelveMbps',12),('eighteenMbps',18),('twentyFourMbps',24),('thirtySixMbps',36),('fourtyEightMbps',48),('fiftyFourMbps',54),('auto',255)))
_EnterpriseApRadioDataRate_Type.__name__=_C
_EnterpriseApRadioDataRate_Object=MibTableColumn
enterpriseApRadioDataRate=_EnterpriseApRadioDataRate_Object((1,3,6,1,4,1,43,35,8,10,1,1,5),_EnterpriseApRadioDataRate_Type())
enterpriseApRadioDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioDataRate.setStatus(_A)
class _EnterpriseApRadioGMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bOnly',1),('gOnly',2),('bg',3),(_N,4)))
_EnterpriseApRadioGMode_Type.__name__=_C
_EnterpriseApRadioGMode_Object=MibTableColumn
enterpriseApRadioGMode=_EnterpriseApRadioGMode_Object((1,3,6,1,4,1,43,35,8,10,1,1,6),_EnterpriseApRadioGMode_Type())
enterpriseApRadioGMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioGMode.setStatus(_A)
class _EnterpriseApRadioAntennaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('both',1),('left',2),('right',3),(_N,4)))
_EnterpriseApRadioAntennaMode_Type.__name__=_C
_EnterpriseApRadioAntennaMode_Object=MibTableColumn
enterpriseApRadioAntennaMode=_EnterpriseApRadioAntennaMode_Object((1,3,6,1,4,1,43,35,8,10,1,1,7),_EnterpriseApRadioAntennaMode_Type())
enterpriseApRadioAntennaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApRadioAntennaMode.setStatus(_A)
class _RogueApState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_RogueApState_Type.__name__=_C
_RogueApState_Object=MibTableColumn
rogueApState=_RogueApState_Object((1,3,6,1,4,1,43,35,8,10,1,1,8),_RogueApState_Type())
rogueApState.setMaxAccess(_B)
if mibBuilder.loadTexts:rogueApState.setStatus(_A)
class _RogueApInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,10080))
_RogueApInterval_Type.__name__=_C
_RogueApInterval_Object=MibTableColumn
rogueApInterval=_RogueApInterval_Object((1,3,6,1,4,1,43,35,8,10,1,1,9),_RogueApInterval_Type())
rogueApInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rogueApInterval.setStatus(_A)
class _RogueApDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_RogueApDuration_Type.__name__=_C
_RogueApDuration_Object=MibTableColumn
rogueApDuration=_RogueApDuration_Object((1,3,6,1,4,1,43,35,8,10,1,1,10),_RogueApDuration_Type())
rogueApDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:rogueApDuration.setStatus(_A)
class _RogueApScanNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_RogueApScanNow_Type.__name__=_C
_RogueApScanNow_Object=MibTableColumn
rogueApScanNow=_RogueApScanNow_Object((1,3,6,1,4,1,43,35,8,10,1,1,11),_RogueApScanNow_Type())
rogueApScanNow.setMaxAccess(_B)
if mibBuilder.loadTexts:rogueApScanNow.setStatus(_A)
_EnterpriseApVapRadioTable_Object=MibTable
enterpriseApVapRadioTable=_EnterpriseApVapRadioTable_Object((1,3,6,1,4,1,43,35,8,10,2))
if mibBuilder.loadTexts:enterpriseApVapRadioTable.setStatus(_A)
_EnterpriseApVapRadioEntry_Object=MibTableRow
enterpriseApVapRadioEntry=_EnterpriseApVapRadioEntry_Object((1,3,6,1,4,1,43,35,8,10,2,1))
enterpriseApVapRadioEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:enterpriseApVapRadioEntry.setStatus(_A)
_EnterpriseApVapRadioIndex_Type=Integer32
_EnterpriseApVapRadioIndex_Object=MibTableColumn
enterpriseApVapRadioIndex=_EnterpriseApVapRadioIndex_Object((1,3,6,1,4,1,43,35,8,10,2,1,1),_EnterpriseApVapRadioIndex_Type())
enterpriseApVapRadioIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:enterpriseApVapRadioIndex.setStatus(_A)
class _EnterpriseApVapRadioState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_EnterpriseApVapRadioState_Type.__name__=_C
_EnterpriseApVapRadioState_Object=MibTableColumn
enterpriseApVapRadioState=_EnterpriseApVapRadioState_Object((1,3,6,1,4,1,43,35,8,10,2,1,2),_EnterpriseApVapRadioState_Type())
enterpriseApVapRadioState.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApVapRadioState.setStatus(_A)
class _EnterpriseApVapRadioClosedSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_EnterpriseApVapRadioClosedSystem_Type.__name__=_C
_EnterpriseApVapRadioClosedSystem_Object=MibTableColumn
enterpriseApVapRadioClosedSystem=_EnterpriseApVapRadioClosedSystem_Object((1,3,6,1,4,1,43,35,8,10,2,1,3),_EnterpriseApVapRadioClosedSystem_Type())
enterpriseApVapRadioClosedSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApVapRadioClosedSystem.setStatus(_A)
class _EnterpriseApVapRadioMaxAssoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_EnterpriseApVapRadioMaxAssoc_Type.__name__=_C
_EnterpriseApVapRadioMaxAssoc_Object=MibTableColumn
enterpriseApVapRadioMaxAssoc=_EnterpriseApVapRadioMaxAssoc_Object((1,3,6,1,4,1,43,35,8,10,2,1,4),_EnterpriseApVapRadioMaxAssoc_Type())
enterpriseApVapRadioMaxAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApVapRadioMaxAssoc.setStatus(_A)
class _EnterpriseApVapRadioTransmitKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EnterpriseApVapRadioTransmitKey_Type.__name__=_C
_EnterpriseApVapRadioTransmitKey_Object=MibTableColumn
enterpriseApVapRadioTransmitKey=_EnterpriseApVapRadioTransmitKey_Object((1,3,6,1,4,1,43,35,8,10,2,1,5),_EnterpriseApVapRadioTransmitKey_Type())
enterpriseApVapRadioTransmitKey.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApVapRadioTransmitKey.setStatus(_A)
class _EnterpriseApVapRadioDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EnterpriseApVapRadioDescription_Type.__name__=_F
_EnterpriseApVapRadioDescription_Object=MibTableColumn
enterpriseApVapRadioDescription=_EnterpriseApVapRadioDescription_Object((1,3,6,1,4,1,43,35,8,10,2,1,6),_EnterpriseApVapRadioDescription_Type())
enterpriseApVapRadioDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:enterpriseApVapRadioDescription.setStatus(_A)
_RadioWdsTable_Object=MibTable
radioWdsTable=_RadioWdsTable_Object((1,3,6,1,4,1,43,35,8,10,3))
if mibBuilder.loadTexts:radioWdsTable.setStatus(_A)
_RadioWdsEntry_Object=MibTableRow
radioWdsEntry=_RadioWdsEntry_Object((1,3,6,1,4,1,43,35,8,10,3,1))
radioWdsEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:radioWdsEntry.setStatus(_A)
class _WdsApRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('roleAp',1),('roleBridgeMaster',2),('roleRepeater',3),('roleBridge',4)))
_WdsApRole_Type.__name__=_C
_WdsApRole_Object=MibTableColumn
wdsApRole=_WdsApRole_Object((1,3,6,1,4,1,43,35,8,10,3,1,1),_WdsApRole_Type())
wdsApRole.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsApRole.setStatus(_A)
_RadioWdsPeerTable_Object=MibTable
radioWdsPeerTable=_RadioWdsPeerTable_Object((1,3,6,1,4,1,43,35,8,10,4))
if mibBuilder.loadTexts:radioWdsPeerTable.setStatus(_A)
_RadioWdsPeerEntry_Object=MibTableRow
radioWdsPeerEntry=_RadioWdsPeerEntry_Object((1,3,6,1,4,1,43,35,8,10,4,1))
radioWdsPeerEntry.setIndexNames((0,_D,_K),(0,_D,_h))
if mibBuilder.loadTexts:radioWdsPeerEntry.setStatus(_A)
_WdsPeerIndex_Type=Integer32
_WdsPeerIndex_Object=MibTableColumn
wdsPeerIndex=_WdsPeerIndex_Object((1,3,6,1,4,1,43,35,8,10,4,1,1),_WdsPeerIndex_Type())
wdsPeerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:wdsPeerIndex.setStatus(_A)
class _WdsPeerBssid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_WdsPeerBssid_Type.__name__=_F
_WdsPeerBssid_Object=MibTableColumn
wdsPeerBssid=_WdsPeerBssid_Object((1,3,6,1,4,1,43,35,8,10,4,1,2),_WdsPeerBssid_Type())
wdsPeerBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsPeerBssid.setStatus(_A)
_EnterpriseApWebRedirection_ObjectIdentity=ObjectIdentity
enterpriseApWebRedirection=_EnterpriseApWebRedirection_ObjectIdentity((1,3,6,1,4,1,43,35,8,11))
class _WebRedirectionEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_WebRedirectionEnabled_Type.__name__=_C
_WebRedirectionEnabled_Object=MibScalar
webRedirectionEnabled=_WebRedirectionEnabled_Object((1,3,6,1,4,1,43,35,8,11,1),_WebRedirectionEnabled_Type())
webRedirectionEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:webRedirectionEnabled.setStatus(_A)
_EnterpriseApProxyArp_ObjectIdentity=ObjectIdentity
enterpriseApProxyArp=_EnterpriseApProxyArp_ObjectIdentity((1,3,6,1,4,1,43,35,8,12))
class _ProxyArpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_ProxyArpEnabled_Type.__name__=_C
_ProxyArpEnabled_Object=MibScalar
proxyArpEnabled=_ProxyArpEnabled_Object((1,3,6,1,4,1,43,35,8,12,1),_ProxyArpEnabled_Type())
proxyArpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:proxyArpEnabled.setStatus(_A)
_EnterpriseApRogueAp_ObjectIdentity=ObjectIdentity
enterpriseApRogueAp=_EnterpriseApRogueAp_ObjectIdentity((1,3,6,1,4,1,43,35,8,13))
_RogueApDetectionTable_Object=MibTable
rogueApDetectionTable=_RogueApDetectionTable_Object((1,3,6,1,4,1,43,35,8,13,1))
if mibBuilder.loadTexts:rogueApDetectionTable.setStatus(_A)
_RogueApEntry_Object=MibTableRow
rogueApEntry=_RogueApEntry_Object((1,3,6,1,4,1,43,35,8,13,1,1))
rogueApEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:rogueApEntry.setStatus(_A)
class _RogueApIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_RogueApIndex_Type.__name__=_C
_RogueApIndex_Object=MibTableColumn
rogueApIndex=_RogueApIndex_Object((1,3,6,1,4,1,43,35,8,13,1,1,1),_RogueApIndex_Type())
rogueApIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rogueApIndex.setStatus(_A)
class _RogueApBssid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_RogueApBssid_Type.__name__=_F
_RogueApBssid_Object=MibTableColumn
rogueApBssid=_RogueApBssid_Object((1,3,6,1,4,1,43,35,8,13,1,1,2),_RogueApBssid_Type())
rogueApBssid.setMaxAccess(_E)
if mibBuilder.loadTexts:rogueApBssid.setStatus(_A)
class _RogueApSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RogueApSsid_Type.__name__=_F
_RogueApSsid_Object=MibTableColumn
rogueApSsid=_RogueApSsid_Object((1,3,6,1,4,1,43,35,8,13,1,1,3),_RogueApSsid_Type())
rogueApSsid.setMaxAccess(_E)
if mibBuilder.loadTexts:rogueApSsid.setStatus(_A)
_RogueApPortNumber_Type=Integer32
_RogueApPortNumber_Object=MibTableColumn
rogueApPortNumber=_RogueApPortNumber_Object((1,3,6,1,4,1,43,35,8,13,1,1,4),_RogueApPortNumber_Type())
rogueApPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rogueApPortNumber.setStatus(_A)
_RogueApChannelNumber_Type=Integer32
_RogueApChannelNumber_Object=MibTableColumn
rogueApChannelNumber=_RogueApChannelNumber_Object((1,3,6,1,4,1,43,35,8,13,1,1,5),_RogueApChannelNumber_Type())
rogueApChannelNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rogueApChannelNumber.setStatus(_A)
_RogueApRSSIValue_Type=Integer32
_RogueApRSSIValue_Object=MibTableColumn
rogueApRSSIValue=_RogueApRSSIValue_Object((1,3,6,1,4,1,43,35,8,13,1,1,6),_RogueApRSSIValue_Type())
rogueApRSSIValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rogueApRSSIValue.setStatus(_A)
_ApNotificationTrapTree_ObjectIdentity=ObjectIdentity
apNotificationTrapTree=_ApNotificationTrapTree_ObjectIdentity((1,3,6,1,4,1,43,35,8,100))
_ApNotificationObjects_ObjectIdentity=ObjectIdentity
apNotificationObjects=_ApNotificationObjects_ObjectIdentity((1,3,6,1,4,1,43,35,8,100,1))
_ApNotificationDot11MacAddr_Type=MacAddress
_ApNotificationDot11MacAddr_Object=MibScalar
apNotificationDot11MacAddr=_ApNotificationDot11MacAddr_Object((1,3,6,1,4,1,43,35,8,100,1,1),_ApNotificationDot11MacAddr_Type())
apNotificationDot11MacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:apNotificationDot11MacAddr.setStatus(_A)
_ApNotificationDot11Station_Type=MacAddress
_ApNotificationDot11Station_Object=MibScalar
apNotificationDot11Station=_ApNotificationDot11Station_Object((1,3,6,1,4,1,43,35,8,100,1,2),_ApNotificationDot11Station_Type())
apNotificationDot11Station.setMaxAccess(_H)
if mibBuilder.loadTexts:apNotificationDot11Station.setStatus(_A)
class _ApNotificationDot11RequestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('association',2),('reAssociation',3),('authentication',4)))
_ApNotificationDot11RequestType_Type.__name__=_C
_ApNotificationDot11RequestType_Object=MibScalar
apNotificationDot11RequestType=_ApNotificationDot11RequestType_Object((1,3,6,1,4,1,43,35,8,100,1,3),_ApNotificationDot11RequestType_Type())
apNotificationDot11RequestType.setMaxAccess(_H)
if mibBuilder.loadTexts:apNotificationDot11RequestType.setStatus(_A)
class _ApNotificationDot11ReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('invalidModeOrState',1),('unAuthenticatedStation',2),('internalError',3),('outOfSequenceFrame',4),('unsupportedAlgorithm',5),('invalidFrameLngth',6),('wepRequiredOnAP',7),('wepNotAllowed',8),('challengeTextMismatch',9)))
_ApNotificationDot11ReasonCode_Type.__name__=_C
_ApNotificationDot11ReasonCode_Object=MibScalar
apNotificationDot11ReasonCode=_ApNotificationDot11ReasonCode_Object((1,3,6,1,4,1,43,35,8,100,1,4),_ApNotificationDot11ReasonCode_Type())
apNotificationDot11ReasonCode.setMaxAccess(_H)
if mibBuilder.loadTexts:apNotificationDot11ReasonCode.setStatus(_A)
_ApNotificationDot11IpAddress_Type=IpAddress
_ApNotificationDot11IpAddress_Object=MibScalar
apNotificationDot11IpAddress=_ApNotificationDot11IpAddress_Object((1,3,6,1,4,1,43,35,8,100,1,5),_ApNotificationDot11IpAddress_Type())
apNotificationDot11IpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:apNotificationDot11IpAddress.setStatus(_A)
_ApNotificationDot11AuthenticatorMacAddr_Type=MacAddress
_ApNotificationDot11AuthenticatorMacAddr_Object=MibScalar
apNotificationDot11AuthenticatorMacAddr=_ApNotificationDot11AuthenticatorMacAddr_Object((1,3,6,1,4,1,43,35,8,100,1,6),_ApNotificationDot11AuthenticatorMacAddr_Type())
apNotificationDot11AuthenticatorMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:apNotificationDot11AuthenticatorMacAddr.setStatus(_A)
_ApNotificationTrapObjects_ObjectIdentity=ObjectIdentity
apNotificationTrapObjects=_ApNotificationTrapObjects_ObjectIdentity((1,3,6,1,4,1,43,35,8,100,2))
sysSystemUp=NotificationType((1,3,6,1,4,1,43,35,8,100,2,1))
if mibBuilder.loadTexts:sysSystemUp.setStatus(_A)
sysSystemDown=NotificationType((1,3,6,1,4,1,43,35,8,100,2,2))
if mibBuilder.loadTexts:sysSystemDown.setStatus(_A)
sysRadiusServerChanged=NotificationType((1,3,6,1,4,1,43,35,8,100,2,3))
if mibBuilder.loadTexts:sysRadiusServerChanged.setStatus(_A)
dot11StationAssociation=NotificationType((1,3,6,1,4,1,43,35,8,100,2,4))
dot11StationAssociation.setObjects((_D,_I))
if mibBuilder.loadTexts:dot11StationAssociation.setStatus(_A)
dot11StationReAssociation=NotificationType((1,3,6,1,4,1,43,35,8,100,2,5))
dot11StationReAssociation.setObjects((_D,_I))
if mibBuilder.loadTexts:dot11StationReAssociation.setStatus(_A)
dot11StationAuthentication=NotificationType((1,3,6,1,4,1,43,35,8,100,2,6))
dot11StationAuthentication.setObjects((_D,_I))
if mibBuilder.loadTexts:dot11StationAuthentication.setStatus(_A)
dot11StationRequestFail=NotificationType((1,3,6,1,4,1,43,35,8,100,2,7))
dot11StationRequestFail.setObjects(*((_D,_I),(_D,_j),(_D,_k)))
if mibBuilder.loadTexts:dot11StationRequestFail.setStatus(_A)
dot11InterfaceAGFail=NotificationType((1,3,6,1,4,1,43,35,8,100,2,8))
if mibBuilder.loadTexts:dot11InterfaceAGFail.setStatus(_A)
dot1xMacAddrAuthSuccess=NotificationType((1,3,6,1,4,1,43,35,8,100,2,9))
dot1xMacAddrAuthSuccess.setObjects((_D,_I))
if mibBuilder.loadTexts:dot1xMacAddrAuthSuccess.setStatus(_A)
dot1xMacAddrAuthFail=NotificationType((1,3,6,1,4,1,43,35,8,100,2,10))
dot1xMacAddrAuthFail.setObjects((_D,_I))
if mibBuilder.loadTexts:dot1xMacAddrAuthFail.setStatus(_A)
dot1xAuthNotInitiated=NotificationType((1,3,6,1,4,1,43,35,8,100,2,11))
dot1xAuthNotInitiated.setObjects((_D,_I))
if mibBuilder.loadTexts:dot1xAuthNotInitiated.setStatus(_A)
dot1xAuthSuccess=NotificationType((1,3,6,1,4,1,43,35,8,100,2,12))
dot1xAuthSuccess.setObjects((_D,_I))
if mibBuilder.loadTexts:dot1xAuthSuccess.setStatus(_A)
dot1xAuthFail=NotificationType((1,3,6,1,4,1,43,35,8,100,2,13))
dot1xAuthFail.setObjects((_D,_I))
if mibBuilder.loadTexts:dot1xAuthFail.setStatus(_A)
localMacAddrAuthSuccess=NotificationType((1,3,6,1,4,1,43,35,8,100,2,14))
localMacAddrAuthSuccess.setObjects((_D,_I))
if mibBuilder.loadTexts:localMacAddrAuthSuccess.setStatus(_A)
localMacAddrAuthFail=NotificationType((1,3,6,1,4,1,43,35,8,100,2,15))
localMacAddrAuthFail.setObjects((_D,_I))
if mibBuilder.loadTexts:localMacAddrAuthFail.setStatus(_A)
pppLogonFail=NotificationType((1,3,6,1,4,1,43,35,8,100,2,16))
if mibBuilder.loadTexts:pppLogonFail.setStatus(_A)
iappStationRoamedFrom=NotificationType((1,3,6,1,4,1,43,35,8,100,2,17))
iappStationRoamedFrom.setObjects(*((_D,_I),(_D,_L)))
if mibBuilder.loadTexts:iappStationRoamedFrom.setStatus(_A)
iappStationRoamedTo=NotificationType((1,3,6,1,4,1,43,35,8,100,2,18))
iappStationRoamedTo.setObjects(*((_D,_I),(_D,_L)))
if mibBuilder.loadTexts:iappStationRoamedTo.setStatus(_A)
iappContextDataSent=NotificationType((1,3,6,1,4,1,43,35,8,100,2,19))
iappContextDataSent.setObjects(*((_D,_I),(_D,_L)))
if mibBuilder.loadTexts:iappContextDataSent.setStatus(_A)
sntpServerFail=NotificationType((1,3,6,1,4,1,43,35,8,100,2,20))
if mibBuilder.loadTexts:sntpServerFail.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'a3Com':a3Com,'wlan-mib':wlan_mib,'rivet':rivet,'enterpriseApSys':enterpriseApSys,'swHardwareVer':swHardwareVer,'swBootRomVer':swBootRomVer,'swOpCodeVer':swOpCodeVer,'swSerialNumber':swSerialNumber,'enterpriseApLineMgnt':enterpriseApLineMgnt,'lineTable':lineTable,'lineEntry':lineEntry,_O:lineIndex,'lineDataBits':lineDataBits,'lineParity':lineParity,'lineSpeed':lineSpeed,'lineStopBits':lineStopBits,'enterpriseApPortMgnt':enterpriseApPortMgnt,'portTable':portTable,'portEntry':portEntry,_P:portIndex,'portName':portName,'portType':portType,'portSpeedDpxCfg':portSpeedDpxCfg,'portFlowCtrlCfg':portFlowCtrlCfg,'portCapabilities':portCapabilities,'portAutonegotiation':portAutonegotiation,'portSpeedDpxStatus':portSpeedDpxStatus,'portFlowCtrlStatus':portFlowCtrlStatus,'enterpriseApFileTransferMgt':enterpriseApFileTransferMgt,'transferType':transferType,'fileType':fileType,'srcFile':srcFile,'destFile':destFile,'fileServer':fileServer,'userName':userName,'password':password,'status':status,'transferStart':transferStart,'enterpriseApResetMgt':enterpriseApResetMgt,'restartOpCodeFile':restartOpCodeFile,'restartControl':restartControl,'enterpriseApIpMgt':enterpriseApIpMgt,'netConfigIPAddress':netConfigIPAddress,'netConfigSubnetMask':netConfigSubnetMask,'netConfigDefaultGateway':netConfigDefaultGateway,'netConfigHttpState':netConfigHttpState,'netConfigHttpPort':netConfigHttpPort,'netConfigHttpsState':netConfigHttpsState,'netConfigHttpsPort':netConfigHttpsPort,'netConfigDHCPState':netConfigDHCPState,'enterpriseAPdot11':enterpriseAPdot11,'dot11AuthenticationEntry':dot11AuthenticationEntry,'dot118021xState':dot118021xState,'dot118021xBroadcastKeyRefreshRate':dot118021xBroadcastKeyRefreshRate,'dot118021xSessionKeyRefreshRate':dot118021xSessionKeyRefreshRate,'dot118021xReauthenticationTimeout':dot118021xReauthenticationTimeout,'dot11MACAuthenticationType':dot11MACAuthenticationType,'dot11AuthenticationServerTable':dot11AuthenticationServerTable,'dot11AuthenticationServerEntry':dot11AuthenticationServerEntry,_b:dot11AuthenticationServerIndex,'dot11AuthenticationServer':dot11AuthenticationServer,'dot11AuthenticationPort':dot11AuthenticationPort,'dot11AuthenticationKey':dot11AuthenticationKey,'dot11AuthenticationRetransmit':dot11AuthenticationRetransmit,'dot11AuthenticationTimeout':dot11AuthenticationTimeout,'dot11AuthenticationAcctPort':dot11AuthenticationAcctPort,'dot11AuthenticationInterimUpdate':dot11AuthenticationInterimUpdate,'dot11Filter':dot11Filter,'dot11FilterDefault':dot11FilterDefault,'dot11FilterTable':dot11FilterTable,'dot11FilterEntry':dot11FilterEntry,_c:dot11FilterAddress,'dot11FilterStatus':dot11FilterStatus,'dot11AuthenticationSupplicantTable':dot11AuthenticationSupplicantTable,'dot11AuthenticationSupplicantEntry':dot11AuthenticationSupplicantEntry,_d:dot118021xSuppIndex,'dot118021xSuppState':dot118021xSuppState,'dot118021xSuppUser':dot118021xSuppUser,'dot118021xSuppPasswd':dot118021xSuppPasswd,'enterpriseApAdmin':enterpriseApAdmin,'enterpriseApAdminUser':enterpriseApAdminUser,'enterpriseApAdminPassword':enterpriseApAdminPassword,'enterpriseApSecurity':enterpriseApSecurity,'enterpriseApSecurityTable':enterpriseApSecurityTable,'enterpriseApSecurityEntry':enterpriseApSecurityEntry,_e:enterpriseApSecurityIndex,'enterpriseApSecurityAuthType':enterpriseApSecurityAuthType,'enterpriseApSecuritySharedKeyLen':enterpriseApSecuritySharedKeyLen,'enterpriseApSecurityWPAMode':enterpriseApSecurityWPAMode,'enterpriseApSecurityWPAKeyType':enterpriseApSecurityWPAKeyType,'enterpriseApSecurityWPACipher':enterpriseApSecurityWPACipher,'enterpriseApSecurityWPAPSKType':enterpriseApSecurityWPAPSKType,'enterpriseApSecurityWPAPSK':enterpriseApSecurityWPAPSK,'enterpriseApSecurityWEPKeyType':enterpriseApSecurityWEPKeyType,'enterpriseApSecurityWEPEnabled':enterpriseApSecurityWEPEnabled,'enterpriseApRadio':enterpriseApRadio,'enterpriseApRadioTable':enterpriseApRadioTable,'enterpriseApRadioEntry':enterpriseApRadioEntry,_K:enterpriseApRadioIndex,'enterpriseApRadioAutoChannel':enterpriseApRadioAutoChannel,'enterpriseApRadioTransmitPower':enterpriseApRadioTransmitPower,'enterpriseApRadioTurboMode':enterpriseApRadioTurboMode,'enterpriseApRadioDataRate':enterpriseApRadioDataRate,'enterpriseApRadioGMode':enterpriseApRadioGMode,'enterpriseApRadioAntennaMode':enterpriseApRadioAntennaMode,'rogueApState':rogueApState,'rogueApInterval':rogueApInterval,'rogueApDuration':rogueApDuration,'rogueApScanNow':rogueApScanNow,'enterpriseApVapRadioTable':enterpriseApVapRadioTable,'enterpriseApVapRadioEntry':enterpriseApVapRadioEntry,_g:enterpriseApVapRadioIndex,'enterpriseApVapRadioState':enterpriseApVapRadioState,'enterpriseApVapRadioClosedSystem':enterpriseApVapRadioClosedSystem,'enterpriseApVapRadioMaxAssoc':enterpriseApVapRadioMaxAssoc,'enterpriseApVapRadioTransmitKey':enterpriseApVapRadioTransmitKey,'enterpriseApVapRadioDescription':enterpriseApVapRadioDescription,'radioWdsTable':radioWdsTable,'radioWdsEntry':radioWdsEntry,'wdsApRole':wdsApRole,'radioWdsPeerTable':radioWdsPeerTable,'radioWdsPeerEntry':radioWdsPeerEntry,_h:wdsPeerIndex,'wdsPeerBssid':wdsPeerBssid,'enterpriseApWebRedirection':enterpriseApWebRedirection,'webRedirectionEnabled':webRedirectionEnabled,'enterpriseApProxyArp':enterpriseApProxyArp,'proxyArpEnabled':proxyArpEnabled,'enterpriseApRogueAp':enterpriseApRogueAp,'rogueApDetectionTable':rogueApDetectionTable,'rogueApEntry':rogueApEntry,_i:rogueApIndex,'rogueApBssid':rogueApBssid,'rogueApSsid':rogueApSsid,'rogueApPortNumber':rogueApPortNumber,'rogueApChannelNumber':rogueApChannelNumber,'rogueApRSSIValue':rogueApRSSIValue,'apNotificationTrapTree':apNotificationTrapTree,'apNotificationObjects':apNotificationObjects,'apNotificationDot11MacAddr':apNotificationDot11MacAddr,_I:apNotificationDot11Station,_j:apNotificationDot11RequestType,_k:apNotificationDot11ReasonCode,_L:apNotificationDot11IpAddress,'apNotificationDot11AuthenticatorMacAddr':apNotificationDot11AuthenticatorMacAddr,'apNotificationTrapObjects':apNotificationTrapObjects,'sysSystemUp':sysSystemUp,'sysSystemDown':sysSystemDown,'sysRadiusServerChanged':sysRadiusServerChanged,'dot11StationAssociation':dot11StationAssociation,'dot11StationReAssociation':dot11StationReAssociation,'dot11StationAuthentication':dot11StationAuthentication,'dot11StationRequestFail':dot11StationRequestFail,'dot11InterfaceAGFail':dot11InterfaceAGFail,'dot1xMacAddrAuthSuccess':dot1xMacAddrAuthSuccess,'dot1xMacAddrAuthFail':dot1xMacAddrAuthFail,'dot1xAuthNotInitiated':dot1xAuthNotInitiated,'dot1xAuthSuccess':dot1xAuthSuccess,'dot1xAuthFail':dot1xAuthFail,'localMacAddrAuthSuccess':localMacAddrAuthSuccess,'localMacAddrAuthFail':localMacAddrAuthFail,'pppLogonFail':pppLogonFail,'iappStationRoamedFrom':iappStationRoamedFrom,'iappStationRoamedTo':iappStationRoamedTo,'iappContextDataSent':iappContextDataSent,'sntpServerFail':sntpServerFail})