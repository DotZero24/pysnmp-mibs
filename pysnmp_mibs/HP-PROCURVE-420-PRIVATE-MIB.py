_b='hpdot11FilterIndex'
_a='hpdot11serverIndex'
_Z='hpdot11Index'
_Y='hpdot11OperationIndex'
_X='hpdot11PrivacyportIndex'
_W='hpdot11portIndex'
_V='dot3xFlowControl'
_U='backPressure'
_T='fullDuplex1000'
_S='halfDuplex1000'
_R='fullDuplex100'
_Q='halfDuplex100'
_P='fullDuplex10'
_O='halfDuplex10'
_N='portIndex'
_M='lineIndex'
_L='PhysAddress'
_K='disabled'
_J='enabled'
_I='none'
_H='OctetString'
_G='not-accessible'
_F='HP-PROCURVE-420-PRIVATE-MIB'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,_L,'TextualConvention')
class PhysAddress(OctetString):0
class Guage32(Counter32):0
class MacAddress(OctetString):0
class DisplayString(OctetString):0
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HP_ObjectIdentity=ObjectIdentity
hP=_HP_ObjectIdentity((1,3,6,1,4,1,11))
_Wireless_ObjectIdentity=ObjectIdentity
wireless=_Wireless_ObjectIdentity((1,3,6,1,4,1,11,2))
_Enterprise_ObjectIdentity=ObjectIdentity
enterprise=_Enterprise_ObjectIdentity((1,3,6,1,4,1,11,2,3))
_AccessPoint_ObjectIdentity=ObjectIdentity
accessPoint=_AccessPoint_ObjectIdentity((1,3,6,1,4,1,11,2,3,7))
_ProCurve_ObjectIdentity=ObjectIdentity
proCurve=_ProCurve_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11))
_HPProCuve420_ObjectIdentity=ObjectIdentity
hPProCuve420=_HPProCuve420_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37))
_EnterpriseApSys_ObjectIdentity=ObjectIdentity
enterpriseApSys=_EnterpriseApSys_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,1))
class _SwHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwHardwareVer_Type.__name__=_E
_SwHardwareVer_Object=MibScalar
swHardwareVer=_SwHardwareVer_Object((1,3,6,1,4,1,11,2,3,7,11,37,1,1),_SwHardwareVer_Type())
swHardwareVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swHardwareVer.setStatus(_A)
class _SwBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBootRomVer_Type.__name__=_E
_SwBootRomVer_Object=MibScalar
swBootRomVer=_SwBootRomVer_Object((1,3,6,1,4,1,11,2,3,7,11,37,1,2),_SwBootRomVer_Type())
swBootRomVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swBootRomVer.setStatus(_A)
class _SwOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwOpCodeVer_Type.__name__=_E
_SwOpCodeVer_Object=MibScalar
swOpCodeVer=_SwOpCodeVer_Object((1,3,6,1,4,1,11,2,3,7,11,37,1,3),_SwOpCodeVer_Type())
swOpCodeVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swOpCodeVer.setStatus(_A)
class _SwCountryCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwCountryCode_Type.__name__=_E
_SwCountryCode_Object=MibScalar
swCountryCode=_SwCountryCode_Object((1,3,6,1,4,1,11,2,3,7,11,37,1,4),_SwCountryCode_Type())
swCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:swCountryCode.setStatus(_A)
_EnterpriseApLineMgnt_ObjectIdentity=ObjectIdentity
enterpriseApLineMgnt=_EnterpriseApLineMgnt_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,2))
_LineTable_Object=MibTable
lineTable=_LineTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,2,1))
if mibBuilder.loadTexts:lineTable.setStatus(_A)
_LineEntry_Object=MibTableRow
lineEntry=_LineEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,2,1,1))
lineEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:lineEntry.setStatus(_A)
_LineIndex_Type=Integer32
_LineIndex_Object=MibTableColumn
lineIndex=_LineIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,2,1,1,1),_LineIndex_Type())
lineIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lineIndex.setStatus(_A)
_LineDataBits_Type=Integer32
_LineDataBits_Object=MibTableColumn
lineDataBits=_LineDataBits_Object((1,3,6,1,4,1,11,2,3,7,11,37,2,1,1,2),_LineDataBits_Type())
lineDataBits.setMaxAccess(_D)
if mibBuilder.loadTexts:lineDataBits.setStatus(_A)
class _LineParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('odd',1),('even',2),(_I,99)))
_LineParity_Type.__name__=_C
_LineParity_Object=MibTableColumn
lineParity=_LineParity_Object((1,3,6,1,4,1,11,2,3,7,11,37,2,1,1,3),_LineParity_Type())
lineParity.setMaxAccess(_D)
if mibBuilder.loadTexts:lineParity.setStatus(_A)
_LineSpeed_Type=Integer32
_LineSpeed_Object=MibTableColumn
lineSpeed=_LineSpeed_Object((1,3,6,1,4,1,11,2,3,7,11,37,2,1,1,4),_LineSpeed_Type())
lineSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:lineSpeed.setStatus(_A)
_LineStopBits_Type=Integer32
_LineStopBits_Object=MibTableColumn
lineStopBits=_LineStopBits_Object((1,3,6,1,4,1,11,2,3,7,11,37,2,1,1,5),_LineStopBits_Type())
lineStopBits.setMaxAccess(_D)
if mibBuilder.loadTexts:lineStopBits.setStatus(_A)
_EnterpriseApPortMgnt_ObjectIdentity=ObjectIdentity
enterpriseApPortMgnt=_EnterpriseApPortMgnt_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,3))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1))
portEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_E
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,2),_PortName_Type())
portName.setMaxAccess(_D)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),('thousandBaseT',6),('thousandBaseGBIC',7),('thousandBaseMiniGBIC',8)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,3),_PortType_Type())
portType.setMaxAccess(_D)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('auto',1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_PortSpeedDpxCfg_Type.__name__=_C
_PortSpeedDpxCfg_Object=MibTableColumn
portSpeedDpxCfg=_PortSpeedDpxCfg_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,4),_PortSpeedDpxCfg_Type())
portSpeedDpxCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:portSpeedDpxCfg.setStatus(_A)
class _PortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_U,3),(_V,4)))
_PortFlowCtrlCfg_Type.__name__=_C
_PortFlowCtrlCfg_Object=MibTableColumn
portFlowCtrlCfg=_PortFlowCtrlCfg_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,5),_PortFlowCtrlCfg_Type())
portFlowCtrlCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:portFlowCtrlCfg.setStatus(_A)
class _PortCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,99)));namedValues=NamedValues(*(('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('reserved6',6),('reserved7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('portCapSym',14),('portCapFlowCtrl',15),('portCap10half',99)))
_PortCapabilities_Type.__name__=_C
_PortCapabilities_Object=MibTableColumn
portCapabilities=_PortCapabilities_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,6),_PortCapabilities_Type())
portCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:portCapabilities.setStatus(_A)
class _PortAutonegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_PortAutonegotiation_Type.__name__=_C
_PortAutonegotiation_Object=MibTableColumn
portAutonegotiation=_PortAutonegotiation_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,7),_PortAutonegotiation_Type())
portAutonegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:portAutonegotiation.setStatus(_A)
class _PortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('error',1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_PortSpeedDpxStatus_Type.__name__=_C
_PortSpeedDpxStatus_Object=MibTableColumn
portSpeedDpxStatus=_PortSpeedDpxStatus_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,8),_PortSpeedDpxStatus_Type())
portSpeedDpxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portSpeedDpxStatus.setStatus(_A)
class _PortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('error',1),(_U,2),(_V,3),(_I,4)))
_PortFlowCtrlStatus_Type.__name__=_C
_PortFlowCtrlStatus_Object=MibTableColumn
portFlowCtrlStatus=_PortFlowCtrlStatus_Object((1,3,6,1,4,1,11,2,3,7,11,37,3,1,1,9),_PortFlowCtrlStatus_Type())
portFlowCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portFlowCtrlStatus.setStatus(_A)
_EnterpriseApFileTransferMgt_ObjectIdentity=ObjectIdentity
enterpriseApFileTransferMgt=_EnterpriseApFileTransferMgt_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,4))
class _TransferStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('go',1),('nogo',2)))
_TransferStart_Type.__name__=_C
_TransferStart_Object=MibScalar
transferStart=_TransferStart_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,1),_TransferStart_Type())
transferStart.setMaxAccess(_B)
if mibBuilder.loadTexts:transferStart.setStatus(_A)
class _TransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftp',1),('tftp',2)))
_TransferType_Type.__name__=_C
_TransferType_Object=MibScalar
transferType=_TransferType_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,2),_TransferType_Type())
transferType.setMaxAccess(_B)
if mibBuilder.loadTexts:transferType.setStatus(_A)
class _FileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('opcode',1),('config',2)))
_FileType_Type.__name__=_C
_FileType_Object=MibScalar
fileType=_FileType_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,3),_FileType_Type())
fileType.setMaxAccess(_B)
if mibBuilder.loadTexts:fileType.setStatus(_A)
class _SrcFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SrcFile_Type.__name__=_E
_SrcFile_Object=MibScalar
srcFile=_SrcFile_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,4),_SrcFile_Type())
srcFile.setMaxAccess(_B)
if mibBuilder.loadTexts:srcFile.setStatus(_A)
class _DestFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DestFile_Type.__name__=_E
_DestFile_Object=MibScalar
destFile=_DestFile_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,5),_DestFile_Type())
destFile.setMaxAccess(_B)
if mibBuilder.loadTexts:destFile.setStatus(_A)
_FileServer_Type=IpAddress
_FileServer_Object=MibScalar
fileServer=_FileServer_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,6),_FileServer_Type())
fileServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fileServer.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_UserName_Type.__name__=_E
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,7),_UserName_Type())
userName.setMaxAccess(_B)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _Password_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Password_Type.__name__=_E
_Password_Object=MibScalar
password=_Password_Object((1,3,6,1,4,1,11,2,3,7,11,37,4,8),_Password_Type())
password.setMaxAccess(_B)
if mibBuilder.loadTexts:password.setStatus(_A)
_EnterpriseApResetMgt_ObjectIdentity=ObjectIdentity
enterpriseApResetMgt=_EnterpriseApResetMgt_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,5))
class _RestartOpCodeFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RestartOpCodeFile_Type.__name__=_E
_RestartOpCodeFile_Object=MibScalar
restartOpCodeFile=_RestartOpCodeFile_Object((1,3,6,1,4,1,11,2,3,7,11,37,5,1),_RestartOpCodeFile_Type())
restartOpCodeFile.setMaxAccess(_B)
if mibBuilder.loadTexts:restartOpCodeFile.setStatus(_A)
class _RestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('warmBoot',2),('coldBoot',3)))
_RestartControl_Type.__name__=_C
_RestartControl_Object=MibScalar
restartControl=_RestartControl_Object((1,3,6,1,4,1,11,2,3,7,11,37,5,2),_RestartControl_Type())
restartControl.setMaxAccess(_B)
if mibBuilder.loadTexts:restartControl.setStatus(_A)
_EnterpriseApIpMgt_ObjectIdentity=ObjectIdentity
enterpriseApIpMgt=_EnterpriseApIpMgt_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,6))
_NetConfigIPAddress_Type=IpAddress
_NetConfigIPAddress_Object=MibScalar
netConfigIPAddress=_NetConfigIPAddress_Object((1,3,6,1,4,1,11,2,3,7,11,37,6,1),_NetConfigIPAddress_Type())
netConfigIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigIPAddress.setStatus(_A)
_NetConfigSubnetMask_Type=IpAddress
_NetConfigSubnetMask_Object=MibScalar
netConfigSubnetMask=_NetConfigSubnetMask_Object((1,3,6,1,4,1,11,2,3,7,11,37,6,2),_NetConfigSubnetMask_Type())
netConfigSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:netConfigSubnetMask.setStatus(_A)
_NetDefaultGateway_Type=IpAddress
_NetDefaultGateway_Object=MibScalar
netDefaultGateway=_NetDefaultGateway_Object((1,3,6,1,4,1,11,2,3,7,11,37,6,3),_NetDefaultGateway_Type())
netDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:netDefaultGateway.setStatus(_A)
class _IpHttpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IpHttpState_Type.__name__=_C
_IpHttpState_Object=MibScalar
ipHttpState=_IpHttpState_Object((1,3,6,1,4,1,11,2,3,7,11,37,6,4),_IpHttpState_Type())
ipHttpState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipHttpState.setStatus(_A)
_IpHttpPort_Type=Integer32
_IpHttpPort_Object=MibScalar
ipHttpPort=_IpHttpPort_Object((1,3,6,1,4,1,11,2,3,7,11,37,6,5),_IpHttpPort_Type())
ipHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipHttpPort.setStatus(_A)
_EnterpriseAPdot11_ObjectIdentity=ObjectIdentity
enterpriseAPdot11=_EnterpriseAPdot11_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,7))
_Hpdot11StationConfigTable_Object=MibTable
hpdot11StationConfigTable=_Hpdot11StationConfigTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1))
if mibBuilder.loadTexts:hpdot11StationConfigTable.setStatus(_A)
_Hpdot11StationConfigEntry_Object=MibTableRow
hpdot11StationConfigEntry=_Hpdot11StationConfigEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1,1))
hpdot11StationConfigEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:hpdot11StationConfigEntry.setStatus(_A)
_Hpdot11portIndex_Type=Integer32
_Hpdot11portIndex_Object=MibTableColumn
hpdot11portIndex=_Hpdot11portIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1,1,1),_Hpdot11portIndex_Type())
hpdot11portIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpdot11portIndex.setStatus(_A)
class _Hpdot11DesiredSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hpdot11DesiredSSID_Type.__name__=_H
_Hpdot11DesiredSSID_Object=MibTableColumn
hpdot11DesiredSSID=_Hpdot11DesiredSSID_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1,1,2),_Hpdot11DesiredSSID_Type())
hpdot11DesiredSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11DesiredSSID.setStatus(_A)
class _Hpdot11BeaconPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1000))
_Hpdot11BeaconPeriod_Type.__name__=_C
_Hpdot11BeaconPeriod_Object=MibTableColumn
hpdot11BeaconPeriod=_Hpdot11BeaconPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1,1,3),_Hpdot11BeaconPeriod_Type())
hpdot11BeaconPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11BeaconPeriod.setStatus(_A)
class _Hpdot11DTIMPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hpdot11DTIMPeriod_Type.__name__=_C
_Hpdot11DTIMPeriod_Object=MibTableColumn
hpdot11DTIMPeriod=_Hpdot11DTIMPeriod_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1,1,4),_Hpdot11DTIMPeriod_Type())
hpdot11DTIMPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11DTIMPeriod.setStatus(_A)
class _Hpdot11OperationalRateSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,108))
_Hpdot11OperationalRateSet_Type.__name__=_C
_Hpdot11OperationalRateSet_Object=MibTableColumn
hpdot11OperationalRateSet=_Hpdot11OperationalRateSet_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1,1,5),_Hpdot11OperationalRateSet_Type())
hpdot11OperationalRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11OperationalRateSet.setStatus(_A)
class _Hpdot11AuthenticationAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('openSystem',1),('sharedKey',2)))
_Hpdot11AuthenticationAlgorithm_Type.__name__=_C
_Hpdot11AuthenticationAlgorithm_Object=MibTableColumn
hpdot11AuthenticationAlgorithm=_Hpdot11AuthenticationAlgorithm_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,1,1,6),_Hpdot11AuthenticationAlgorithm_Type())
hpdot11AuthenticationAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11AuthenticationAlgorithm.setStatus(_A)
_Hpdot11PrivacyTable_Object=MibTable
hpdot11PrivacyTable=_Hpdot11PrivacyTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,2))
if mibBuilder.loadTexts:hpdot11PrivacyTable.setStatus(_A)
_Hpdot11PrivacyEntry_Object=MibTableRow
hpdot11PrivacyEntry=_Hpdot11PrivacyEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,2,1))
hpdot11PrivacyEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:hpdot11PrivacyEntry.setStatus(_A)
_Hpdot11PrivacyportIndex_Type=Integer32
_Hpdot11PrivacyportIndex_Object=MibTableColumn
hpdot11PrivacyportIndex=_Hpdot11PrivacyportIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,2,1,1),_Hpdot11PrivacyportIndex_Type())
hpdot11PrivacyportIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpdot11PrivacyportIndex.setStatus(_A)
class _Hpdot11PrivacyInvoked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hpdot11PrivacyInvoked_Type.__name__=_C
_Hpdot11PrivacyInvoked_Object=MibTableColumn
hpdot11PrivacyInvoked=_Hpdot11PrivacyInvoked_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,2,1,2),_Hpdot11PrivacyInvoked_Type())
hpdot11PrivacyInvoked.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11PrivacyInvoked.setStatus(_A)
class _Hpdot11WEPDefaultKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Hpdot11WEPDefaultKeyID_Type.__name__=_C
_Hpdot11WEPDefaultKeyID_Object=MibTableColumn
hpdot11WEPDefaultKeyID=_Hpdot11WEPDefaultKeyID_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,2,1,3),_Hpdot11WEPDefaultKeyID_Type())
hpdot11WEPDefaultKeyID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11WEPDefaultKeyID.setStatus(_A)
class _Hpdot11WEPKeyMappingLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2147483647))
_Hpdot11WEPKeyMappingLength_Type.__name__=_C
_Hpdot11WEPKeyMappingLength_Object=MibTableColumn
hpdot11WEPKeyMappingLength=_Hpdot11WEPKeyMappingLength_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,2,1,4),_Hpdot11WEPKeyMappingLength_Type())
hpdot11WEPKeyMappingLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11WEPKeyMappingLength.setStatus(_A)
_Hpdot11mac_ObjectIdentity=ObjectIdentity
hpdot11mac=_Hpdot11mac_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,7,3))
_Hpdot11OperationTable_Object=MibTable
hpdot11OperationTable=_Hpdot11OperationTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,3,1))
if mibBuilder.loadTexts:hpdot11OperationTable.setStatus(_A)
_Hpdot11OperationEntry_Object=MibTableRow
hpdot11OperationEntry=_Hpdot11OperationEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,3,1,1))
hpdot11OperationEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:hpdot11OperationEntry.setStatus(_A)
_Hpdot11OperationIndex_Type=Integer32
_Hpdot11OperationIndex_Object=MibTableColumn
hpdot11OperationIndex=_Hpdot11OperationIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,3,1,1,1),_Hpdot11OperationIndex_Type())
hpdot11OperationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpdot11OperationIndex.setStatus(_A)
class _Hpdot11RTSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_Hpdot11RTSThreshold_Type.__name__=_C
_Hpdot11RTSThreshold_Object=MibTableColumn
hpdot11RTSThreshold=_Hpdot11RTSThreshold_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,3,1,1,2),_Hpdot11RTSThreshold_Type())
hpdot11RTSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11RTSThreshold.setStatus(_A)
class _Hpdot11FragmentationThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_Hpdot11FragmentationThreshold_Type.__name__=_C
_Hpdot11FragmentationThreshold_Object=MibTableColumn
hpdot11FragmentationThreshold=_Hpdot11FragmentationThreshold_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,3,1,1,3),_Hpdot11FragmentationThreshold_Type())
hpdot11FragmentationThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11FragmentationThreshold.setStatus(_A)
_Hpdot11phy_ObjectIdentity=ObjectIdentity
hpdot11phy=_Hpdot11phy_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,7,4))
_Hpdot11PhyOperationTable_Object=MibTable
hpdot11PhyOperationTable=_Hpdot11PhyOperationTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,4,1))
if mibBuilder.loadTexts:hpdot11PhyOperationTable.setStatus(_A)
_Hpdot11PhyOperationEntry_Object=MibTableRow
hpdot11PhyOperationEntry=_Hpdot11PhyOperationEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,4,1,1))
hpdot11PhyOperationEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:hpdot11PhyOperationEntry.setStatus(_A)
_Hpdot11Index_Type=Integer32
_Hpdot11Index_Object=MibTableColumn
hpdot11Index=_Hpdot11Index_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,4,1,1,1),_Hpdot11Index_Type())
hpdot11Index.setMaxAccess(_G)
if mibBuilder.loadTexts:hpdot11Index.setStatus(_A)
_Hpdot11CurrentChannel_Type=Integer32
_Hpdot11CurrentChannel_Object=MibTableColumn
hpdot11CurrentChannel=_Hpdot11CurrentChannel_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,4,1,1,2),_Hpdot11CurrentChannel_Type())
hpdot11CurrentChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11CurrentChannel.setStatus(_A)
class _Hpdot11TurboModeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('on',1),('off',2),(_I,99)))
_Hpdot11TurboModeEnabled_Type.__name__=_C
_Hpdot11TurboModeEnabled_Object=MibTableColumn
hpdot11TurboModeEnabled=_Hpdot11TurboModeEnabled_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,4,1,1,3),_Hpdot11TurboModeEnabled_Type())
hpdot11TurboModeEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:hpdot11TurboModeEnabled.setStatus(_A)
class _Hpdot11PreambleLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_Hpdot11PreambleLength_Type.__name__=_C
_Hpdot11PreambleLength_Object=MibTableColumn
hpdot11PreambleLength=_Hpdot11PreambleLength_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,4,1,1,4),_Hpdot11PreambleLength_Type())
hpdot11PreambleLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11PreambleLength.setStatus(_A)
_Hpdot11AuthenticationEntry_ObjectIdentity=ObjectIdentity
hpdot11AuthenticationEntry=_Hpdot11AuthenticationEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,7,5))
_Hpdot118021xSupport_Type=TruthValue
_Hpdot118021xSupport_Object=MibScalar
hpdot118021xSupport=_Hpdot118021xSupport_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,5,1),_Hpdot118021xSupport_Type())
hpdot118021xSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot118021xSupport.setStatus(_A)
_Hpdot118021xRequired_Type=TruthValue
_Hpdot118021xRequired_Object=MibScalar
hpdot118021xRequired=_Hpdot118021xRequired_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,5,2),_Hpdot118021xRequired_Type())
hpdot118021xRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot118021xRequired.setStatus(_A)
_Hpdot11AuthenticationServerTable_Object=MibTable
hpdot11AuthenticationServerTable=_Hpdot11AuthenticationServerTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6))
if mibBuilder.loadTexts:hpdot11AuthenticationServerTable.setStatus(_A)
_Hpdot11AuthenticationServerEntry_Object=MibTableRow
hpdot11AuthenticationServerEntry=_Hpdot11AuthenticationServerEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6,1))
hpdot11AuthenticationServerEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:hpdot11AuthenticationServerEntry.setStatus(_A)
_Hpdot11serverIndex_Type=Integer32
_Hpdot11serverIndex_Object=MibTableColumn
hpdot11serverIndex=_Hpdot11serverIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6,1,1),_Hpdot11serverIndex_Type())
hpdot11serverIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpdot11serverIndex.setStatus(_A)
_Hpdot11AuthenticationServer_Type=IpAddress
_Hpdot11AuthenticationServer_Object=MibTableColumn
hpdot11AuthenticationServer=_Hpdot11AuthenticationServer_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6,1,2),_Hpdot11AuthenticationServer_Type())
hpdot11AuthenticationServer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11AuthenticationServer.setStatus(_A)
class _Hpdot11AuthenticationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_Hpdot11AuthenticationPort_Type.__name__=_C
_Hpdot11AuthenticationPort_Object=MibTableColumn
hpdot11AuthenticationPort=_Hpdot11AuthenticationPort_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6,1,3),_Hpdot11AuthenticationPort_Type())
hpdot11AuthenticationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11AuthenticationPort.setStatus(_A)
class _Hpdot11AuthenticationKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_Hpdot11AuthenticationKey_Type.__name__=_E
_Hpdot11AuthenticationKey_Object=MibTableColumn
hpdot11AuthenticationKey=_Hpdot11AuthenticationKey_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6,1,4),_Hpdot11AuthenticationKey_Type())
hpdot11AuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11AuthenticationKey.setStatus(_A)
class _Hpdot11AuthenticationRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_Hpdot11AuthenticationRetransmit_Type.__name__=_C
_Hpdot11AuthenticationRetransmit_Object=MibTableColumn
hpdot11AuthenticationRetransmit=_Hpdot11AuthenticationRetransmit_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6,1,5),_Hpdot11AuthenticationRetransmit_Type())
hpdot11AuthenticationRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11AuthenticationRetransmit.setStatus(_A)
class _Hpdot11AuthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Hpdot11AuthenticationTimeout_Type.__name__=_C
_Hpdot11AuthenticationTimeout_Object=MibTableColumn
hpdot11AuthenticationTimeout=_Hpdot11AuthenticationTimeout_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,6,1,6),_Hpdot11AuthenticationTimeout_Type())
hpdot11AuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11AuthenticationTimeout.setStatus(_A)
_Hpdot11FilterTable_Object=MibTable
hpdot11FilterTable=_Hpdot11FilterTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,7))
if mibBuilder.loadTexts:hpdot11FilterTable.setStatus(_A)
_Hpdot11FilterEntry_Object=MibTableRow
hpdot11FilterEntry=_Hpdot11FilterEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,7,1))
hpdot11FilterEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:hpdot11FilterEntry.setStatus(_A)
_Hpdot11FilterIndex_Type=Integer32
_Hpdot11FilterIndex_Object=MibTableColumn
hpdot11FilterIndex=_Hpdot11FilterIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,7,1,1),_Hpdot11FilterIndex_Type())
hpdot11FilterIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpdot11FilterIndex.setStatus(_A)
_Hpdot11FilterAddress_Type=PhysAddress
_Hpdot11FilterAddress_Object=MibTableColumn
hpdot11FilterAddress=_Hpdot11FilterAddress_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,7,1,2),_Hpdot11FilterAddress_Type())
hpdot11FilterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11FilterAddress.setStatus(_A)
class _Hpdot11FilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(30,31)));namedValues=NamedValues(*(('allowed',30),('denied',31)))
_Hpdot11FilterStatus_Type.__name__=_C
_Hpdot11FilterStatus_Object=MibTableColumn
hpdot11FilterStatus=_Hpdot11FilterStatus_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,7,1,3),_Hpdot11FilterStatus_Type())
hpdot11FilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11FilterStatus.setStatus(_A)
_Hpdot11smt_ObjectIdentity=ObjectIdentity
hpdot11smt=_Hpdot11smt_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,7,8))
_Hpdot11WEPDefaultKeys11g_ObjectIdentity=ObjectIdentity
hpdot11WEPDefaultKeys11g=_Hpdot11WEPDefaultKeys11g_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,37,7,8,1))
_Hpdot11WEPDefaultKeys11gTable_Object=MibTable
hpdot11WEPDefaultKeys11gTable=_Hpdot11WEPDefaultKeys11gTable_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,8,1,1))
if mibBuilder.loadTexts:hpdot11WEPDefaultKeys11gTable.setStatus(_A)
_Hpdot11WEPDefaultKeys11gEntry_Object=MibTableRow
hpdot11WEPDefaultKeys11gEntry=_Hpdot11WEPDefaultKeys11gEntry_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,8,1,1,1))
hpdot11WEPDefaultKeys11gEntry.setIndexNames((0,_F,'dot11WEPDefaultKey11gLength'))
if mibBuilder.loadTexts:hpdot11WEPDefaultKeys11gEntry.setStatus(_A)
class _Hpdot11WEPDefaultKey11gLength_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(64,128,152)));namedValues=NamedValues(*(('sixtyFour',64),('oneHundredTwentyEight',128),('oneHundredFiftyTwo',152)))
_Hpdot11WEPDefaultKey11gLength_Type.__name__=_C
_Hpdot11WEPDefaultKey11gLength_Object=MibTableColumn
hpdot11WEPDefaultKey11gLength=_Hpdot11WEPDefaultKey11gLength_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,8,1,1,1,1),_Hpdot11WEPDefaultKey11gLength_Type())
hpdot11WEPDefaultKey11gLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11WEPDefaultKey11gLength.setStatus(_A)
class _Hpdot11WEPDefaultKey11gIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hpdot11WEPDefaultKey11gIndex_Type.__name__=_C
_Hpdot11WEPDefaultKey11gIndex_Object=MibTableColumn
hpdot11WEPDefaultKey11gIndex=_Hpdot11WEPDefaultKey11gIndex_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,8,1,1,1,2),_Hpdot11WEPDefaultKey11gIndex_Type())
hpdot11WEPDefaultKey11gIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpdot11WEPDefaultKey11gIndex.setStatus(_A)
class _Hpdot11WEPDefaultKey11gValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Hpdot11WEPDefaultKey11gValue_Type.__name__=_H
_Hpdot11WEPDefaultKey11gValue_Object=MibTableColumn
hpdot11WEPDefaultKey11gValue=_Hpdot11WEPDefaultKey11gValue_Object((1,3,6,1,4,1,11,2,3,7,11,37,7,8,1,1,1,3),_Hpdot11WEPDefaultKey11gValue_Type())
hpdot11WEPDefaultKey11gValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpdot11WEPDefaultKey11gValue.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_L:PhysAddress,'Guage32':Guage32,'MacAddress':MacAddress,_E:DisplayString,'TruthValue':TruthValue,'hP':hP,'wireless':wireless,'enterprise':enterprise,'accessPoint':accessPoint,'proCurve':proCurve,'hPProCuve420':hPProCuve420,'enterpriseApSys':enterpriseApSys,'swHardwareVer':swHardwareVer,'swBootRomVer':swBootRomVer,'swOpCodeVer':swOpCodeVer,'swCountryCode':swCountryCode,'enterpriseApLineMgnt':enterpriseApLineMgnt,'lineTable':lineTable,'lineEntry':lineEntry,_M:lineIndex,'lineDataBits':lineDataBits,'lineParity':lineParity,'lineSpeed':lineSpeed,'lineStopBits':lineStopBits,'enterpriseApPortMgnt':enterpriseApPortMgnt,'portTable':portTable,'portEntry':portEntry,_N:portIndex,'portName':portName,'portType':portType,'portSpeedDpxCfg':portSpeedDpxCfg,'portFlowCtrlCfg':portFlowCtrlCfg,'portCapabilities':portCapabilities,'portAutonegotiation':portAutonegotiation,'portSpeedDpxStatus':portSpeedDpxStatus,'portFlowCtrlStatus':portFlowCtrlStatus,'enterpriseApFileTransferMgt':enterpriseApFileTransferMgt,'transferStart':transferStart,'transferType':transferType,'fileType':fileType,'srcFile':srcFile,'destFile':destFile,'fileServer':fileServer,'userName':userName,'password':password,'enterpriseApResetMgt':enterpriseApResetMgt,'restartOpCodeFile':restartOpCodeFile,'restartControl':restartControl,'enterpriseApIpMgt':enterpriseApIpMgt,'netConfigIPAddress':netConfigIPAddress,'netConfigSubnetMask':netConfigSubnetMask,'netDefaultGateway':netDefaultGateway,'ipHttpState':ipHttpState,'ipHttpPort':ipHttpPort,'enterpriseAPdot11':enterpriseAPdot11,'hpdot11StationConfigTable':hpdot11StationConfigTable,'hpdot11StationConfigEntry':hpdot11StationConfigEntry,_W:hpdot11portIndex,'hpdot11DesiredSSID':hpdot11DesiredSSID,'hpdot11BeaconPeriod':hpdot11BeaconPeriod,'hpdot11DTIMPeriod':hpdot11DTIMPeriod,'hpdot11OperationalRateSet':hpdot11OperationalRateSet,'hpdot11AuthenticationAlgorithm':hpdot11AuthenticationAlgorithm,'hpdot11PrivacyTable':hpdot11PrivacyTable,'hpdot11PrivacyEntry':hpdot11PrivacyEntry,_X:hpdot11PrivacyportIndex,'hpdot11PrivacyInvoked':hpdot11PrivacyInvoked,'hpdot11WEPDefaultKeyID':hpdot11WEPDefaultKeyID,'hpdot11WEPKeyMappingLength':hpdot11WEPKeyMappingLength,'hpdot11mac':hpdot11mac,'hpdot11OperationTable':hpdot11OperationTable,'hpdot11OperationEntry':hpdot11OperationEntry,_Y:hpdot11OperationIndex,'hpdot11RTSThreshold':hpdot11RTSThreshold,'hpdot11FragmentationThreshold':hpdot11FragmentationThreshold,'hpdot11phy':hpdot11phy,'hpdot11PhyOperationTable':hpdot11PhyOperationTable,'hpdot11PhyOperationEntry':hpdot11PhyOperationEntry,_Z:hpdot11Index,'hpdot11CurrentChannel':hpdot11CurrentChannel,'hpdot11TurboModeEnabled':hpdot11TurboModeEnabled,'hpdot11PreambleLength':hpdot11PreambleLength,'hpdot11AuthenticationEntry':hpdot11AuthenticationEntry,'hpdot118021xSupport':hpdot118021xSupport,'hpdot118021xRequired':hpdot118021xRequired,'hpdot11AuthenticationServerTable':hpdot11AuthenticationServerTable,'hpdot11AuthenticationServerEntry':hpdot11AuthenticationServerEntry,_a:hpdot11serverIndex,'hpdot11AuthenticationServer':hpdot11AuthenticationServer,'hpdot11AuthenticationPort':hpdot11AuthenticationPort,'hpdot11AuthenticationKey':hpdot11AuthenticationKey,'hpdot11AuthenticationRetransmit':hpdot11AuthenticationRetransmit,'hpdot11AuthenticationTimeout':hpdot11AuthenticationTimeout,'hpdot11FilterTable':hpdot11FilterTable,'hpdot11FilterEntry':hpdot11FilterEntry,_b:hpdot11FilterIndex,'hpdot11FilterAddress':hpdot11FilterAddress,'hpdot11FilterStatus':hpdot11FilterStatus,'hpdot11smt':hpdot11smt,'hpdot11WEPDefaultKeys11g':hpdot11WEPDefaultKeys11g,'hpdot11WEPDefaultKeys11gTable':hpdot11WEPDefaultKeys11gTable,'hpdot11WEPDefaultKeys11gEntry':hpdot11WEPDefaultKeys11gEntry,'hpdot11WEPDefaultKey11gLength':hpdot11WEPDefaultKey11gLength,'hpdot11WEPDefaultKey11gIndex':hpdot11WEPDefaultKey11gIndex,'hpdot11WEPDefaultKey11gValue':hpdot11WEPDefaultKey11gValue})