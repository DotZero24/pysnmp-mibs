_q='ntWlanDot11DisassociationStationAddress'
_p='ntWlanApMUStatsMUAddress'
_o='ntWlanApVlanMUMACToVidAddress'
_n='ntWlanApVlanIfIndex'
_m='ntWlanApQoSMACToQueueAddress'
_l='ntWlanApQoSEtherTypeToQueueIndex'
_k='ntWlanApSecurityIfIndex'
_j='supported'
_i='ntWlanApRateSupportSpeed'
_h='ntWlanApRateSupportIfIndex'
_g='ntWlanDot11InterfaceIndex'
_f='ntWlanDot11FilterIndex'
_e='ntWlanDot11ServerIndex'
_d='Minutes'
_c='ntWlanDot11Index'
_b='dot3xFlowControl'
_a='backPressure'
_Z='fullDuplex1000'
_Y='halfDuplex1000'
_X='fullDuplex100'
_W='halfDuplex100'
_V='fullDuplex10'
_U='halfDuplex10'
_T='ntWlanPortIndex'
_S='ntWlanLineIndex'
_R='OctetString'
_Q='ntWlanDot11AssociationMU'
_P='Seconds'
_O='off'
_N='disabled'
_M='enabled'
_L='ifIndex'
_K='none'
_J='ifPhysAddress'
_I='ntWlanDot11AssociationStationAddress'
_H='IF-MIB'
_G='not-accessible'
_F='DisplayString'
_E='NORTEL-WLAN-AP-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex,ifPhysAddress=mibBuilder.importSymbols(_H,'InterfaceIndex',_L,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
wlan2200,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','wlan2200')
nortelWlanApMib=ModuleIdentity((1,3,6,1,4,1,45,1,11,1))
if mibBuilder.loadTexts:nortelWlanApMib.setRevisions(('2003-07-16 00:00','2003-09-11 00:00','2004-04-12 00:00'))
class NtWlanApDataRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,127))
class NtWlanApWEPKey(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(5,5),ValueSizeConstraint(13,13),ValueSizeConstraint(16,16))
_NtWlanApSys_ObjectIdentity=ObjectIdentity
ntWlanApSys=_NtWlanApSys_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,1))
class _NtWlanSwHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtWlanSwHardwareVer_Type.__name__=_F
_NtWlanSwHardwareVer_Object=MibScalar
ntWlanSwHardwareVer=_NtWlanSwHardwareVer_Object((1,3,6,1,4,1,45,1,11,1,1,1),_NtWlanSwHardwareVer_Type())
ntWlanSwHardwareVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanSwHardwareVer.setStatus(_A)
class _NtWlanSwBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtWlanSwBootRomVer_Type.__name__=_F
_NtWlanSwBootRomVer_Object=MibScalar
ntWlanSwBootRomVer=_NtWlanSwBootRomVer_Object((1,3,6,1,4,1,45,1,11,1,1,2),_NtWlanSwBootRomVer_Type())
ntWlanSwBootRomVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanSwBootRomVer.setStatus(_A)
class _NtWlanSwOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtWlanSwOpCodeVer_Type.__name__=_F
_NtWlanSwOpCodeVer_Object=MibScalar
ntWlanSwOpCodeVer=_NtWlanSwOpCodeVer_Object((1,3,6,1,4,1,45,1,11,1,1,3),_NtWlanSwOpCodeVer_Type())
ntWlanSwOpCodeVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanSwOpCodeVer.setStatus(_A)
class _NtWlanSwCountryCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NtWlanSwCountryCode_Type.__name__=_F
_NtWlanSwCountryCode_Object=MibScalar
ntWlanSwCountryCode=_NtWlanSwCountryCode_Object((1,3,6,1,4,1,45,1,11,1,1,4),_NtWlanSwCountryCode_Type())
ntWlanSwCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanSwCountryCode.setStatus(_A)
class _NtWlanSwNNDataFileVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtWlanSwNNDataFileVer_Type.__name__=_F
_NtWlanSwNNDataFileVer_Object=MibScalar
ntWlanSwNNDataFileVer=_NtWlanSwNNDataFileVer_Object((1,3,6,1,4,1,45,1,11,1,1,5),_NtWlanSwNNDataFileVer_Type())
ntWlanSwNNDataFileVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanSwNNDataFileVer.setStatus(_A)
_NtWlanApLineMgnt_ObjectIdentity=ObjectIdentity
ntWlanApLineMgnt=_NtWlanApLineMgnt_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,2))
_NtWlanLineTable_Object=MibTable
ntWlanLineTable=_NtWlanLineTable_Object((1,3,6,1,4,1,45,1,11,1,2,1))
if mibBuilder.loadTexts:ntWlanLineTable.setStatus(_A)
_NtWlanLineEntry_Object=MibTableRow
ntWlanLineEntry=_NtWlanLineEntry_Object((1,3,6,1,4,1,45,1,11,1,2,1,1))
ntWlanLineEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:ntWlanLineEntry.setStatus(_A)
class _NtWlanLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NtWlanLineIndex_Type.__name__=_C
_NtWlanLineIndex_Object=MibTableColumn
ntWlanLineIndex=_NtWlanLineIndex_Object((1,3,6,1,4,1,45,1,11,1,2,1,1,1),_NtWlanLineIndex_Type())
ntWlanLineIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanLineIndex.setStatus(_A)
_NtWlanLineDataBits_Type=Integer32
_NtWlanLineDataBits_Object=MibTableColumn
ntWlanLineDataBits=_NtWlanLineDataBits_Object((1,3,6,1,4,1,45,1,11,1,2,1,1,2),_NtWlanLineDataBits_Type())
ntWlanLineDataBits.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanLineDataBits.setStatus(_A)
class _NtWlanLineParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('odd',1),('even',2),(_K,99)))
_NtWlanLineParity_Type.__name__=_C
_NtWlanLineParity_Object=MibTableColumn
ntWlanLineParity=_NtWlanLineParity_Object((1,3,6,1,4,1,45,1,11,1,2,1,1,3),_NtWlanLineParity_Type())
ntWlanLineParity.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanLineParity.setStatus(_A)
_NtWlanLineSpeed_Type=Integer32
_NtWlanLineSpeed_Object=MibTableColumn
ntWlanLineSpeed=_NtWlanLineSpeed_Object((1,3,6,1,4,1,45,1,11,1,2,1,1,4),_NtWlanLineSpeed_Type())
ntWlanLineSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanLineSpeed.setStatus(_A)
_NtWlanLineStopBits_Type=Integer32
_NtWlanLineStopBits_Object=MibTableColumn
ntWlanLineStopBits=_NtWlanLineStopBits_Object((1,3,6,1,4,1,45,1,11,1,2,1,1,5),_NtWlanLineStopBits_Type())
ntWlanLineStopBits.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanLineStopBits.setStatus(_A)
_NtWlanApPortMgnt_ObjectIdentity=ObjectIdentity
ntWlanApPortMgnt=_NtWlanApPortMgnt_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,3))
_NtWlanPortTable_Object=MibTable
ntWlanPortTable=_NtWlanPortTable_Object((1,3,6,1,4,1,45,1,11,1,3,1))
if mibBuilder.loadTexts:ntWlanPortTable.setStatus(_A)
_NtWlanPortEntry_Object=MibTableRow
ntWlanPortEntry=_NtWlanPortEntry_Object((1,3,6,1,4,1,45,1,11,1,3,1,1))
ntWlanPortEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:ntWlanPortEntry.setStatus(_A)
_NtWlanPortIndex_Type=InterfaceIndex
_NtWlanPortIndex_Object=MibTableColumn
ntWlanPortIndex=_NtWlanPortIndex_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,1),_NtWlanPortIndex_Type())
ntWlanPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanPortIndex.setStatus(_A)
class _NtWlanPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtWlanPortName_Type.__name__=_F
_NtWlanPortName_Object=MibTableColumn
ntWlanPortName=_NtWlanPortName_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,2),_NtWlanPortName_Type())
ntWlanPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortName.setStatus(_A)
class _NtWlanPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),('thousandBaseT',6),('thousandBaseGBIC',7),('thousandBaseMiniGBIC',8)))
_NtWlanPortType_Type.__name__=_C
_NtWlanPortType_Object=MibTableColumn
ntWlanPortType=_NtWlanPortType_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,3),_NtWlanPortType_Type())
ntWlanPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortType.setStatus(_A)
class _NtWlanPortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reserved',1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7)))
_NtWlanPortSpeedDpxCfg_Type.__name__=_C
_NtWlanPortSpeedDpxCfg_Object=MibTableColumn
ntWlanPortSpeedDpxCfg=_NtWlanPortSpeedDpxCfg_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,4),_NtWlanPortSpeedDpxCfg_Type())
ntWlanPortSpeedDpxCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortSpeedDpxCfg.setStatus(_A)
class _NtWlanPortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_a,3),(_b,4)))
_NtWlanPortFlowCtrlCfg_Type.__name__=_C
_NtWlanPortFlowCtrlCfg_Object=MibTableColumn
ntWlanPortFlowCtrlCfg=_NtWlanPortFlowCtrlCfg_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,5),_NtWlanPortFlowCtrlCfg_Type())
ntWlanPortFlowCtrlCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortFlowCtrlCfg.setStatus(_A)
class _NtWlanPortCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,99)));namedValues=NamedValues(*(('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('reserved6',6),('reserved7',7),('reserved8',8),('reserved9',9),('reserved10',10),('reserved11',11),('reserved12',12),('reserved13',13),('portCapSym',14),('portCapFlowCtrl',15),('portCap10half',99)))
_NtWlanPortCapabilities_Type.__name__=_C
_NtWlanPortCapabilities_Object=MibTableColumn
ntWlanPortCapabilities=_NtWlanPortCapabilities_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,6),_NtWlanPortCapabilities_Type())
ntWlanPortCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortCapabilities.setStatus(_A)
class _NtWlanPortAutonegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NtWlanPortAutonegotiation_Type.__name__=_C
_NtWlanPortAutonegotiation_Object=MibTableColumn
ntWlanPortAutonegotiation=_NtWlanPortAutonegotiation_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,7),_NtWlanPortAutonegotiation_Type())
ntWlanPortAutonegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortAutonegotiation.setStatus(_A)
class _NtWlanPortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('error',1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7)))
_NtWlanPortSpeedDpxStatus_Type.__name__=_C
_NtWlanPortSpeedDpxStatus_Object=MibTableColumn
ntWlanPortSpeedDpxStatus=_NtWlanPortSpeedDpxStatus_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,8),_NtWlanPortSpeedDpxStatus_Type())
ntWlanPortSpeedDpxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortSpeedDpxStatus.setStatus(_A)
class _NtWlanPortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('error',1),(_a,2),(_b,3),(_K,4)))
_NtWlanPortFlowCtrlStatus_Type.__name__=_C
_NtWlanPortFlowCtrlStatus_Object=MibTableColumn
ntWlanPortFlowCtrlStatus=_NtWlanPortFlowCtrlStatus_Object((1,3,6,1,4,1,45,1,11,1,3,1,1,9),_NtWlanPortFlowCtrlStatus_Type())
ntWlanPortFlowCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanPortFlowCtrlStatus.setStatus(_A)
_NtWlanApFileTransferMgt_ObjectIdentity=ObjectIdentity
ntWlanApFileTransferMgt=_NtWlanApFileTransferMgt_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,4))
class _NtWlanTransferStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('go',1),('nogo',2)))
_NtWlanTransferStart_Type.__name__=_C
_NtWlanTransferStart_Object=MibScalar
ntWlanTransferStart=_NtWlanTransferStart_Object((1,3,6,1,4,1,45,1,11,1,4,1),_NtWlanTransferStart_Type())
ntWlanTransferStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanTransferStart.setStatus(_A)
class _NtWlanTransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ftpDownload',1),('tftpDownload',2),('ftpUpload',3),('tftpUpload',4)))
_NtWlanTransferType_Type.__name__=_C
_NtWlanTransferType_Object=MibScalar
ntWlanTransferType=_NtWlanTransferType_Object((1,3,6,1,4,1,45,1,11,1,4,2),_NtWlanTransferType_Type())
ntWlanTransferType.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanTransferType.setStatus(_A)
class _NtWlanFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('firmware',1),('config',2),('nortelConfig',3)))
_NtWlanFileType_Type.__name__=_C
_NtWlanFileType_Object=MibScalar
ntWlanFileType=_NtWlanFileType_Object((1,3,6,1,4,1,45,1,11,1,4,3),_NtWlanFileType_Type())
ntWlanFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanFileType.setStatus(_A)
class _NtWlanSrcFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_NtWlanSrcFile_Type.__name__=_F
_NtWlanSrcFile_Object=MibScalar
ntWlanSrcFile=_NtWlanSrcFile_Object((1,3,6,1,4,1,45,1,11,1,4,4),_NtWlanSrcFile_Type())
ntWlanSrcFile.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanSrcFile.setStatus(_A)
class _NtWlanDestFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_NtWlanDestFile_Type.__name__=_F
_NtWlanDestFile_Object=MibScalar
ntWlanDestFile=_NtWlanDestFile_Object((1,3,6,1,4,1,45,1,11,1,4,5),_NtWlanDestFile_Type())
ntWlanDestFile.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDestFile.setStatus(_A)
_NtWlanFileServer_Type=IpAddress
_NtWlanFileServer_Object=MibScalar
ntWlanFileServer=_NtWlanFileServer_Object((1,3,6,1,4,1,45,1,11,1,4,6),_NtWlanFileServer_Type())
ntWlanFileServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanFileServer.setStatus(_A)
class _NtWlanUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_NtWlanUserName_Type.__name__=_F
_NtWlanUserName_Object=MibScalar
ntWlanUserName=_NtWlanUserName_Object((1,3,6,1,4,1,45,1,11,1,4,7),_NtWlanUserName_Type())
ntWlanUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanUserName.setStatus(_A)
class _NtWlanPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_NtWlanPassword_Type.__name__=_F
_NtWlanPassword_Object=MibScalar
ntWlanPassword=_NtWlanPassword_Object((1,3,6,1,4,1,45,1,11,1,4,8),_NtWlanPassword_Type())
ntWlanPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanPassword.setStatus(_A)
class _NtWlanFileTransferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_K,1),('inProgress',2),('success',3),('fail',4),('invalidSource',5),('invalidDestination',6),('outOfMemory',7),('outOfSpace',8),('fileNotFound',9)))
_NtWlanFileTransferStatus_Type.__name__=_C
_NtWlanFileTransferStatus_Object=MibScalar
ntWlanFileTransferStatus=_NtWlanFileTransferStatus_Object((1,3,6,1,4,1,45,1,11,1,4,9),_NtWlanFileTransferStatus_Type())
ntWlanFileTransferStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanFileTransferStatus.setStatus(_A)
_NtWlanApResetMgt_ObjectIdentity=ObjectIdentity
ntWlanApResetMgt=_NtWlanApResetMgt_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,5))
class _NtWlanRestartOpCodeFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_NtWlanRestartOpCodeFile_Type.__name__=_F
_NtWlanRestartOpCodeFile_Object=MibScalar
ntWlanRestartOpCodeFile=_NtWlanRestartOpCodeFile_Object((1,3,6,1,4,1,45,1,11,1,5,1),_NtWlanRestartOpCodeFile_Type())
ntWlanRestartOpCodeFile.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanRestartOpCodeFile.setStatus(_A)
class _NtWlanRestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('warmBoot',2),('coldBoot',3)))
_NtWlanRestartControl_Type.__name__=_C
_NtWlanRestartControl_Object=MibScalar
ntWlanRestartControl=_NtWlanRestartControl_Object((1,3,6,1,4,1,45,1,11,1,5,2),_NtWlanRestartControl_Type())
ntWlanRestartControl.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanRestartControl.setStatus(_A)
_NtWlanApIpMgt_ObjectIdentity=ObjectIdentity
ntWlanApIpMgt=_NtWlanApIpMgt_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,6))
_NtWlanNetConfigIPAddress_Type=IpAddress
_NtWlanNetConfigIPAddress_Object=MibScalar
ntWlanNetConfigIPAddress=_NtWlanNetConfigIPAddress_Object((1,3,6,1,4,1,45,1,11,1,6,1),_NtWlanNetConfigIPAddress_Type())
ntWlanNetConfigIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanNetConfigIPAddress.setStatus(_A)
_NtWlanNetConfigSubnetMask_Type=IpAddress
_NtWlanNetConfigSubnetMask_Object=MibScalar
ntWlanNetConfigSubnetMask=_NtWlanNetConfigSubnetMask_Object((1,3,6,1,4,1,45,1,11,1,6,2),_NtWlanNetConfigSubnetMask_Type())
ntWlanNetConfigSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanNetConfigSubnetMask.setStatus(_A)
_NtWlanNetDefaultGateway_Type=IpAddress
_NtWlanNetDefaultGateway_Object=MibScalar
ntWlanNetDefaultGateway=_NtWlanNetDefaultGateway_Object((1,3,6,1,4,1,45,1,11,1,6,3),_NtWlanNetDefaultGateway_Type())
ntWlanNetDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanNetDefaultGateway.setStatus(_A)
class _NtWlanIpHttpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NtWlanIpHttpState_Type.__name__=_C
_NtWlanIpHttpState_Object=MibScalar
ntWlanIpHttpState=_NtWlanIpHttpState_Object((1,3,6,1,4,1,45,1,11,1,6,4),_NtWlanIpHttpState_Type())
ntWlanIpHttpState.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanIpHttpState.setStatus(_A)
class _NtWlanIpHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtWlanIpHttpPort_Type.__name__=_C
_NtWlanIpHttpPort_Object=MibScalar
ntWlanIpHttpPort=_NtWlanIpHttpPort_Object((1,3,6,1,4,1,45,1,11,1,6,5),_NtWlanIpHttpPort_Type())
ntWlanIpHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanIpHttpPort.setStatus(_A)
_NtWlanApDot11_ObjectIdentity=ObjectIdentity
ntWlanApDot11=_NtWlanApDot11_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,7))
_NtWlanDot11Phy_ObjectIdentity=ObjectIdentity
ntWlanDot11Phy=_NtWlanDot11Phy_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,7,4))
_NtWlanDot11PhyOperationTable_Object=MibTable
ntWlanDot11PhyOperationTable=_NtWlanDot11PhyOperationTable_Object((1,3,6,1,4,1,45,1,11,1,7,4,1))
if mibBuilder.loadTexts:ntWlanDot11PhyOperationTable.setStatus(_A)
_NtWlanDot11PhyOperationEntry_Object=MibTableRow
ntWlanDot11PhyOperationEntry=_NtWlanDot11PhyOperationEntry_Object((1,3,6,1,4,1,45,1,11,1,7,4,1,1))
ntWlanDot11PhyOperationEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:ntWlanDot11PhyOperationEntry.setStatus(_A)
class _NtWlanDot11Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NtWlanDot11Index_Type.__name__=_C
_NtWlanDot11Index_Object=MibTableColumn
ntWlanDot11Index=_NtWlanDot11Index_Object((1,3,6,1,4,1,45,1,11,1,7,4,1,1,1),_NtWlanDot11Index_Type())
ntWlanDot11Index.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanDot11Index.setStatus(_A)
class _NtWlanDot11TurboModeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('on',1),(_O,2),(_K,99)))
_NtWlanDot11TurboModeEnabled_Type.__name__=_C
_NtWlanDot11TurboModeEnabled_Object=MibTableColumn
ntWlanDot11TurboModeEnabled=_NtWlanDot11TurboModeEnabled_Object((1,3,6,1,4,1,45,1,11,1,7,4,1,1,3),_NtWlanDot11TurboModeEnabled_Type())
ntWlanDot11TurboModeEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanDot11TurboModeEnabled.setStatus(_A)
class _NtWlanDot11PreambleLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('short',1),('long',2),('twelveSymbols',99)))
_NtWlanDot11PreambleLength_Type.__name__=_C
_NtWlanDot11PreambleLength_Object=MibTableColumn
ntWlanDot11PreambleLength=_NtWlanDot11PreambleLength_Object((1,3,6,1,4,1,45,1,11,1,7,4,1,1,4),_NtWlanDot11PreambleLength_Type())
ntWlanDot11PreambleLength.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11PreambleLength.setStatus(_A)
_NtWlanDot11dWorldModeEnabled_Type=TruthValue
_NtWlanDot11dWorldModeEnabled_Object=MibTableColumn
ntWlanDot11dWorldModeEnabled=_NtWlanDot11dWorldModeEnabled_Object((1,3,6,1,4,1,45,1,11,1,7,4,1,1,5),_NtWlanDot11dWorldModeEnabled_Type())
ntWlanDot11dWorldModeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11dWorldModeEnabled.setStatus(_A)
_NtWlanDot11ClosedSystem_Type=TruthValue
_NtWlanDot11ClosedSystem_Object=MibTableColumn
ntWlanDot11ClosedSystem=_NtWlanDot11ClosedSystem_Object((1,3,6,1,4,1,45,1,11,1,7,4,1,1,6),_NtWlanDot11ClosedSystem_Type())
ntWlanDot11ClosedSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11ClosedSystem.setStatus(_A)
_NtWlanDot11AuthenticationEntry_ObjectIdentity=ObjectIdentity
ntWlanDot11AuthenticationEntry=_NtWlanDot11AuthenticationEntry_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,7,5))
_NtWlanDot118021xSupport_Type=TruthValue
_NtWlanDot118021xSupport_Object=MibScalar
ntWlanDot118021xSupport=_NtWlanDot118021xSupport_Object((1,3,6,1,4,1,45,1,11,1,7,5,1),_NtWlanDot118021xSupport_Type())
ntWlanDot118021xSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot118021xSupport.setStatus(_A)
_NtWlanDot118021xRequired_Type=TruthValue
_NtWlanDot118021xRequired_Object=MibScalar
ntWlanDot118021xRequired=_NtWlanDot118021xRequired_Object((1,3,6,1,4,1,45,1,11,1,7,5,2),_NtWlanDot118021xRequired_Type())
ntWlanDot118021xRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot118021xRequired.setStatus(_A)
class _NtWlanDot118021xBcastKeyRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_NtWlanDot118021xBcastKeyRefresh_Type.__name__=_C
_NtWlanDot118021xBcastKeyRefresh_Object=MibScalar
ntWlanDot118021xBcastKeyRefresh=_NtWlanDot118021xBcastKeyRefresh_Object((1,3,6,1,4,1,45,1,11,1,7,5,3),_NtWlanDot118021xBcastKeyRefresh_Type())
ntWlanDot118021xBcastKeyRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot118021xBcastKeyRefresh.setStatus(_A)
if mibBuilder.loadTexts:ntWlanDot118021xBcastKeyRefresh.setUnits(_d)
class _NtWlanDot118021xSessKeyRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_NtWlanDot118021xSessKeyRefresh_Type.__name__=_C
_NtWlanDot118021xSessKeyRefresh_Object=MibScalar
ntWlanDot118021xSessKeyRefresh=_NtWlanDot118021xSessKeyRefresh_Object((1,3,6,1,4,1,45,1,11,1,7,5,4),_NtWlanDot118021xSessKeyRefresh_Type())
ntWlanDot118021xSessKeyRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot118021xSessKeyRefresh.setStatus(_A)
if mibBuilder.loadTexts:ntWlanDot118021xSessKeyRefresh.setUnits(_d)
class _NtWlanDot118021xReAuthRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtWlanDot118021xReAuthRefresh_Type.__name__=_C
_NtWlanDot118021xReAuthRefresh_Object=MibScalar
ntWlanDot118021xReAuthRefresh=_NtWlanDot118021xReAuthRefresh_Object((1,3,6,1,4,1,45,1,11,1,7,5,5),_NtWlanDot118021xReAuthRefresh_Type())
ntWlanDot118021xReAuthRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot118021xReAuthRefresh.setStatus(_A)
if mibBuilder.loadTexts:ntWlanDot118021xReAuthRefresh.setUnits(_P)
_NtWlanDot11AuthenticationServerTable_Object=MibTable
ntWlanDot11AuthenticationServerTable=_NtWlanDot11AuthenticationServerTable_Object((1,3,6,1,4,1,45,1,11,1,7,6))
if mibBuilder.loadTexts:ntWlanDot11AuthenticationServerTable.setStatus(_A)
_NtWlanDot11AuthenticationServerEntry_Object=MibTableRow
ntWlanDot11AuthenticationServerEntry=_NtWlanDot11AuthenticationServerEntry_Object((1,3,6,1,4,1,45,1,11,1,7,6,1))
ntWlanDot11AuthenticationServerEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:ntWlanDot11AuthenticationServerEntry.setStatus(_A)
class _NtWlanDot11ServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NtWlanDot11ServerIndex_Type.__name__=_C
_NtWlanDot11ServerIndex_Object=MibTableColumn
ntWlanDot11ServerIndex=_NtWlanDot11ServerIndex_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,1),_NtWlanDot11ServerIndex_Type())
ntWlanDot11ServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanDot11ServerIndex.setStatus(_A)
_NtWlanDot11AuthenticationServer_Type=IpAddress
_NtWlanDot11AuthenticationServer_Object=MibTableColumn
ntWlanDot11AuthenticationServer=_NtWlanDot11AuthenticationServer_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,2),_NtWlanDot11AuthenticationServer_Type())
ntWlanDot11AuthenticationServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11AuthenticationServer.setStatus(_A)
class _NtWlanDot11AuthenticationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_NtWlanDot11AuthenticationPort_Type.__name__=_C
_NtWlanDot11AuthenticationPort_Object=MibTableColumn
ntWlanDot11AuthenticationPort=_NtWlanDot11AuthenticationPort_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,3),_NtWlanDot11AuthenticationPort_Type())
ntWlanDot11AuthenticationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11AuthenticationPort.setStatus(_A)
class _NtWlanDot11AuthenticationKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtWlanDot11AuthenticationKey_Type.__name__=_F
_NtWlanDot11AuthenticationKey_Object=MibTableColumn
ntWlanDot11AuthenticationKey=_NtWlanDot11AuthenticationKey_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,4),_NtWlanDot11AuthenticationKey_Type())
ntWlanDot11AuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11AuthenticationKey.setStatus(_A)
class _NtWlanDot11AuthenticationRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_NtWlanDot11AuthenticationRetransmit_Type.__name__=_C
_NtWlanDot11AuthenticationRetransmit_Object=MibTableColumn
ntWlanDot11AuthenticationRetransmit=_NtWlanDot11AuthenticationRetransmit_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,5),_NtWlanDot11AuthenticationRetransmit_Type())
ntWlanDot11AuthenticationRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11AuthenticationRetransmit.setStatus(_A)
class _NtWlanDot11AuthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_NtWlanDot11AuthenticationTimeout_Type.__name__=_C
_NtWlanDot11AuthenticationTimeout_Object=MibTableColumn
ntWlanDot11AuthenticationTimeout=_NtWlanDot11AuthenticationTimeout_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,6),_NtWlanDot11AuthenticationTimeout_Type())
ntWlanDot11AuthenticationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11AuthenticationTimeout.setStatus(_A)
if mibBuilder.loadTexts:ntWlanDot11AuthenticationTimeout.setUnits(_P)
_NtWlanDot11SecondaryAuthServer_Type=IpAddress
_NtWlanDot11SecondaryAuthServer_Object=MibTableColumn
ntWlanDot11SecondaryAuthServer=_NtWlanDot11SecondaryAuthServer_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,7),_NtWlanDot11SecondaryAuthServer_Type())
ntWlanDot11SecondaryAuthServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11SecondaryAuthServer.setStatus(_A)
class _NtWlanDot11SecondaryAuthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_NtWlanDot11SecondaryAuthPort_Type.__name__=_C
_NtWlanDot11SecondaryAuthPort_Object=MibTableColumn
ntWlanDot11SecondaryAuthPort=_NtWlanDot11SecondaryAuthPort_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,8),_NtWlanDot11SecondaryAuthPort_Type())
ntWlanDot11SecondaryAuthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11SecondaryAuthPort.setStatus(_A)
class _NtWlanDot11SecondaryAuthKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtWlanDot11SecondaryAuthKey_Type.__name__=_F
_NtWlanDot11SecondaryAuthKey_Object=MibTableColumn
ntWlanDot11SecondaryAuthKey=_NtWlanDot11SecondaryAuthKey_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,9),_NtWlanDot11SecondaryAuthKey_Type())
ntWlanDot11SecondaryAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11SecondaryAuthKey.setStatus(_A)
class _NtWlanDot11SecondaryAuthRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_NtWlanDot11SecondaryAuthRetransmit_Type.__name__=_C
_NtWlanDot11SecondaryAuthRetransmit_Object=MibTableColumn
ntWlanDot11SecondaryAuthRetransmit=_NtWlanDot11SecondaryAuthRetransmit_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,10),_NtWlanDot11SecondaryAuthRetransmit_Type())
ntWlanDot11SecondaryAuthRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11SecondaryAuthRetransmit.setStatus(_A)
class _NtWlanDot11SecondaryAuthTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_NtWlanDot11SecondaryAuthTimeout_Type.__name__=_C
_NtWlanDot11SecondaryAuthTimeout_Object=MibTableColumn
ntWlanDot11SecondaryAuthTimeout=_NtWlanDot11SecondaryAuthTimeout_Object((1,3,6,1,4,1,45,1,11,1,7,6,1,11),_NtWlanDot11SecondaryAuthTimeout_Type())
ntWlanDot11SecondaryAuthTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11SecondaryAuthTimeout.setStatus(_A)
if mibBuilder.loadTexts:ntWlanDot11SecondaryAuthTimeout.setUnits(_P)
_NtWlanDot11FilterTable_Object=MibTable
ntWlanDot11FilterTable=_NtWlanDot11FilterTable_Object((1,3,6,1,4,1,45,1,11,1,7,7))
if mibBuilder.loadTexts:ntWlanDot11FilterTable.setStatus(_A)
_NtWlanDot11FilterEntry_Object=MibTableRow
ntWlanDot11FilterEntry=_NtWlanDot11FilterEntry_Object((1,3,6,1,4,1,45,1,11,1,7,7,1))
ntWlanDot11FilterEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:ntWlanDot11FilterEntry.setStatus(_A)
class _NtWlanDot11FilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NtWlanDot11FilterIndex_Type.__name__=_C
_NtWlanDot11FilterIndex_Object=MibTableColumn
ntWlanDot11FilterIndex=_NtWlanDot11FilterIndex_Object((1,3,6,1,4,1,45,1,11,1,7,7,1,1),_NtWlanDot11FilterIndex_Type())
ntWlanDot11FilterIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanDot11FilterIndex.setStatus(_A)
_NtWlanDot11FilterAddress_Type=PhysAddress
_NtWlanDot11FilterAddress_Object=MibTableColumn
ntWlanDot11FilterAddress=_NtWlanDot11FilterAddress_Object((1,3,6,1,4,1,45,1,11,1,7,7,1,2),_NtWlanDot11FilterAddress_Type())
ntWlanDot11FilterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11FilterAddress.setStatus(_A)
class _NtWlanDot11FilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(30,31)));namedValues=NamedValues(*(('allowed',30),('denied',31)))
_NtWlanDot11FilterStatus_Type.__name__=_C
_NtWlanDot11FilterStatus_Object=MibTableColumn
ntWlanDot11FilterStatus=_NtWlanDot11FilterStatus_Object((1,3,6,1,4,1,45,1,11,1,7,7,1,3),_NtWlanDot11FilterStatus_Type())
ntWlanDot11FilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanDot11FilterStatus.setStatus(_A)
_NtWlanDot11TrapTable_Object=MibTable
ntWlanDot11TrapTable=_NtWlanDot11TrapTable_Object((1,3,6,1,4,1,45,1,11,1,7,9))
if mibBuilder.loadTexts:ntWlanDot11TrapTable.setStatus(_A)
_NtWlanDot11TrapEntry_Object=MibTableRow
ntWlanDot11TrapEntry=_NtWlanDot11TrapEntry_Object((1,3,6,1,4,1,45,1,11,1,7,9,1))
ntWlanDot11TrapEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:ntWlanDot11TrapEntry.setStatus(_A)
class _NtWlanDot11InterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NtWlanDot11InterfaceIndex_Type.__name__=_C
_NtWlanDot11InterfaceIndex_Object=MibTableColumn
ntWlanDot11InterfaceIndex=_NtWlanDot11InterfaceIndex_Object((1,3,6,1,4,1,45,1,11,1,7,9,1,1),_NtWlanDot11InterfaceIndex_Type())
ntWlanDot11InterfaceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanDot11InterfaceIndex.setStatus(_A)
_NtWlanDot11AssociationStationAddress_Type=PhysAddress
_NtWlanDot11AssociationStationAddress_Object=MibTableColumn
ntWlanDot11AssociationStationAddress=_NtWlanDot11AssociationStationAddress_Object((1,3,6,1,4,1,45,1,11,1,7,9,1,2),_NtWlanDot11AssociationStationAddress_Type())
ntWlanDot11AssociationStationAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanDot11AssociationStationAddress.setStatus(_A)
_NtWlanDot11DisassociationStationAddress_Type=PhysAddress
_NtWlanDot11DisassociationStationAddress_Object=MibTableColumn
ntWlanDot11DisassociationStationAddress=_NtWlanDot11DisassociationStationAddress_Object((1,3,6,1,4,1,45,1,11,1,7,9,1,3),_NtWlanDot11DisassociationStationAddress_Type())
ntWlanDot11DisassociationStationAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanDot11DisassociationStationAddress.setStatus(_A)
class _NtWlanDot11AssociationMU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtWlanDot11AssociationMU_Type.__name__=_C
_NtWlanDot11AssociationMU_Object=MibTableColumn
ntWlanDot11AssociationMU=_NtWlanDot11AssociationMU_Object((1,3,6,1,4,1,45,1,11,1,7,9,1,4),_NtWlanDot11AssociationMU_Type())
ntWlanDot11AssociationMU.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanDot11AssociationMU.setStatus(_A)
_NtWlanApTraps_ObjectIdentity=ObjectIdentity
ntWlanApTraps=_NtWlanApTraps_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,8))
_NtWlanApTraps0_ObjectIdentity=ObjectIdentity
ntWlanApTraps0=_NtWlanApTraps0_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,8,0))
_NtWlanApMuAssocTrapEnabled_Type=TruthValue
_NtWlanApMuAssocTrapEnabled_Object=MibScalar
ntWlanApMuAssocTrapEnabled=_NtWlanApMuAssocTrapEnabled_Object((1,3,6,1,4,1,45,1,11,1,8,1),_NtWlanApMuAssocTrapEnabled_Type())
ntWlanApMuAssocTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApMuAssocTrapEnabled.setStatus(_A)
_NtWlanApMuDisAssocTrapEnabled_Type=TruthValue
_NtWlanApMuDisAssocTrapEnabled_Object=MibScalar
ntWlanApMuDisAssocTrapEnabled=_NtWlanApMuDisAssocTrapEnabled_Object((1,3,6,1,4,1,45,1,11,1,8,2),_NtWlanApMuDisAssocTrapEnabled_Type())
ntWlanApMuDisAssocTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApMuDisAssocTrapEnabled.setStatus(_A)
_NtWlanApLID_ObjectIdentity=ObjectIdentity
ntWlanApLID=_NtWlanApLID_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,9))
_NtWlanApLIDCheckEtherLinkEnabled_Type=TruthValue
_NtWlanApLIDCheckEtherLinkEnabled_Object=MibScalar
ntWlanApLIDCheckEtherLinkEnabled=_NtWlanApLIDCheckEtherLinkEnabled_Object((1,3,6,1,4,1,45,1,11,1,9,1),_NtWlanApLIDCheckEtherLinkEnabled_Type())
ntWlanApLIDCheckEtherLinkEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApLIDCheckEtherLinkEnabled.setStatus(_A)
_NtWlanApLIDCheckIPLinkEnabled_Type=TruthValue
_NtWlanApLIDCheckIPLinkEnabled_Object=MibScalar
ntWlanApLIDCheckIPLinkEnabled=_NtWlanApLIDCheckIPLinkEnabled_Object((1,3,6,1,4,1,45,1,11,1,9,2),_NtWlanApLIDCheckIPLinkEnabled_Type())
ntWlanApLIDCheckIPLinkEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApLIDCheckIPLinkEnabled.setStatus(_A)
_NtWlanApLIDCheckIpLinkAddress_Type=IpAddress
_NtWlanApLIDCheckIpLinkAddress_Object=MibScalar
ntWlanApLIDCheckIpLinkAddress=_NtWlanApLIDCheckIpLinkAddress_Object((1,3,6,1,4,1,45,1,11,1,9,3),_NtWlanApLIDCheckIpLinkAddress_Type())
ntWlanApLIDCheckIpLinkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApLIDCheckIpLinkAddress.setStatus(_A)
_NtWlanApRateSupport_ObjectIdentity=ObjectIdentity
ntWlanApRateSupport=_NtWlanApRateSupport_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,10))
_NtWlanApRateSupportTable_Object=MibTable
ntWlanApRateSupportTable=_NtWlanApRateSupportTable_Object((1,3,6,1,4,1,45,1,11,1,10,1))
if mibBuilder.loadTexts:ntWlanApRateSupportTable.setStatus(_A)
_NtWlanApRateSupportEntry_Object=MibTableRow
ntWlanApRateSupportEntry=_NtWlanApRateSupportEntry_Object((1,3,6,1,4,1,45,1,11,1,10,1,1))
ntWlanApRateSupportEntry.setIndexNames((0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:ntWlanApRateSupportEntry.setStatus(_A)
_NtWlanApRateSupportIfIndex_Type=InterfaceIndex
_NtWlanApRateSupportIfIndex_Object=MibTableColumn
ntWlanApRateSupportIfIndex=_NtWlanApRateSupportIfIndex_Object((1,3,6,1,4,1,45,1,11,1,10,1,1,1),_NtWlanApRateSupportIfIndex_Type())
ntWlanApRateSupportIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApRateSupportIfIndex.setStatus(_A)
_NtWlanApRateSupportSpeed_Type=NtWlanApDataRate
_NtWlanApRateSupportSpeed_Object=MibTableColumn
ntWlanApRateSupportSpeed=_NtWlanApRateSupportSpeed_Object((1,3,6,1,4,1,45,1,11,1,10,1,1,2),_NtWlanApRateSupportSpeed_Type())
ntWlanApRateSupportSpeed.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApRateSupportSpeed.setStatus(_A)
class _NtWlanApRateSupportLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),(_j,1),('supportedBasic',2)))
_NtWlanApRateSupportLevel_Type.__name__=_C
_NtWlanApRateSupportLevel_Object=MibTableColumn
ntWlanApRateSupportLevel=_NtWlanApRateSupportLevel_Object((1,3,6,1,4,1,45,1,11,1,10,1,1,3),_NtWlanApRateSupportLevel_Type())
ntWlanApRateSupportLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApRateSupportLevel.setStatus(_A)
_NtWlanApSecurity_ObjectIdentity=ObjectIdentity
ntWlanApSecurity=_NtWlanApSecurity_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,11))
_NtWlanApSecurityTable_Object=MibTable
ntWlanApSecurityTable=_NtWlanApSecurityTable_Object((1,3,6,1,4,1,45,1,11,1,11,1))
if mibBuilder.loadTexts:ntWlanApSecurityTable.setStatus(_A)
_NtWlanApSecurityEntry_Object=MibTableRow
ntWlanApSecurityEntry=_NtWlanApSecurityEntry_Object((1,3,6,1,4,1,45,1,11,1,11,1,1))
ntWlanApSecurityEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:ntWlanApSecurityEntry.setStatus(_A)
_NtWlanApSecurityIfIndex_Type=InterfaceIndex
_NtWlanApSecurityIfIndex_Object=MibTableColumn
ntWlanApSecurityIfIndex=_NtWlanApSecurityIfIndex_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,1),_NtWlanApSecurityIfIndex_Type())
ntWlanApSecurityIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApSecurityIfIndex.setStatus(_A)
_NtWlanApSecurityEnabled_Type=TruthValue
_NtWlanApSecurityEnabled_Object=MibTableColumn
ntWlanApSecurityEnabled=_NtWlanApSecurityEnabled_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,2),_NtWlanApSecurityEnabled_Type())
ntWlanApSecurityEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityEnabled.setStatus(_A)
class _NtWlanApSecurityWEPAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('openSystem',0),('sharedKey',1)))
_NtWlanApSecurityWEPAuthType_Type.__name__=_C
_NtWlanApSecurityWEPAuthType_Object=MibTableColumn
ntWlanApSecurityWEPAuthType=_NtWlanApSecurityWEPAuthType_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,3),_NtWlanApSecurityWEPAuthType_Type())
ntWlanApSecurityWEPAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWEPAuthType.setStatus(_A)
class _NtWlanApSecurityWEPKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('wepKey64',0),('wepKey128',1),('wepKey152',2)))
_NtWlanApSecurityWEPKeyLength_Type.__name__=_C
_NtWlanApSecurityWEPKeyLength_Object=MibTableColumn
ntWlanApSecurityWEPKeyLength=_NtWlanApSecurityWEPKeyLength_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,4),_NtWlanApSecurityWEPKeyLength_Type())
ntWlanApSecurityWEPKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWEPKeyLength.setStatus(_A)
class _NtWlanApSecurityWEPActiveKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NtWlanApSecurityWEPActiveKey_Type.__name__=_C
_NtWlanApSecurityWEPActiveKey_Object=MibTableColumn
ntWlanApSecurityWEPActiveKey=_NtWlanApSecurityWEPActiveKey_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,5),_NtWlanApSecurityWEPActiveKey_Type())
ntWlanApSecurityWEPActiveKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWEPActiveKey.setStatus(_A)
_NtWlanApSecurityWEPKey1_Type=NtWlanApWEPKey
_NtWlanApSecurityWEPKey1_Object=MibTableColumn
ntWlanApSecurityWEPKey1=_NtWlanApSecurityWEPKey1_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,6),_NtWlanApSecurityWEPKey1_Type())
ntWlanApSecurityWEPKey1.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWEPKey1.setStatus(_A)
_NtWlanApSecurityWEPKey2_Type=NtWlanApWEPKey
_NtWlanApSecurityWEPKey2_Object=MibTableColumn
ntWlanApSecurityWEPKey2=_NtWlanApSecurityWEPKey2_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,7),_NtWlanApSecurityWEPKey2_Type())
ntWlanApSecurityWEPKey2.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWEPKey2.setStatus(_A)
_NtWlanApSecurityWEPKey3_Type=NtWlanApWEPKey
_NtWlanApSecurityWEPKey3_Object=MibTableColumn
ntWlanApSecurityWEPKey3=_NtWlanApSecurityWEPKey3_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,8),_NtWlanApSecurityWEPKey3_Type())
ntWlanApSecurityWEPKey3.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWEPKey3.setStatus(_A)
_NtWlanApSecurityWEPKey4_Type=NtWlanApWEPKey
_NtWlanApSecurityWEPKey4_Object=MibTableColumn
ntWlanApSecurityWEPKey4=_NtWlanApSecurityWEPKey4_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,9),_NtWlanApSecurityWEPKey4_Type())
ntWlanApSecurityWEPKey4.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWEPKey4.setStatus(_A)
class _NtWlanApSecurityWPASupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_j,1),('required',2),('wepOnly',3)))
_NtWlanApSecurityWPASupport_Type.__name__=_C
_NtWlanApSecurityWPASupport_Object=MibTableColumn
ntWlanApSecurityWPASupport=_NtWlanApSecurityWPASupport_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,10),_NtWlanApSecurityWPASupport_Type())
ntWlanApSecurityWPASupport.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWPASupport.setStatus(_A)
class _NtWlanApSecurityWPAMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dynamic',0),('preSharedKey',1)))
_NtWlanApSecurityWPAMode_Type.__name__=_C
_NtWlanApSecurityWPAMode_Object=MibTableColumn
ntWlanApSecurityWPAMode=_NtWlanApSecurityWPAMode_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,11),_NtWlanApSecurityWPAMode_Type())
ntWlanApSecurityWPAMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWPAMode.setStatus(_A)
class _NtWlanApSecurityWPAPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(63,63));fixedLength=63
_NtWlanApSecurityWPAPreSharedKey_Type.__name__=_R
_NtWlanApSecurityWPAPreSharedKey_Object=MibTableColumn
ntWlanApSecurityWPAPreSharedKey=_NtWlanApSecurityWPAPreSharedKey_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,12),_NtWlanApSecurityWPAPreSharedKey_Type())
ntWlanApSecurityWPAPreSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWPAPreSharedKey.setStatus(_A)
class _NtWlanApSecurityWPAMcastCypherMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('wep',0),('tkip',1),('aes',2)))
_NtWlanApSecurityWPAMcastCypherMode_Type.__name__=_C
_NtWlanApSecurityWPAMcastCypherMode_Object=MibTableColumn
ntWlanApSecurityWPAMcastCypherMode=_NtWlanApSecurityWPAMcastCypherMode_Object((1,3,6,1,4,1,45,1,11,1,11,1,1,13),_NtWlanApSecurityWPAMcastCypherMode_Type())
ntWlanApSecurityWPAMcastCypherMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApSecurityWPAMcastCypherMode.setStatus(_A)
_NtWlanApQoS_ObjectIdentity=ObjectIdentity
ntWlanApQoS=_NtWlanApQoS_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,12))
class _NtWlanApQoSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_O,0),('etherSrc',1),('etherDst',2),('ethertype',3),('directPriorityMap',4)))
_NtWlanApQoSMode_Type.__name__=_C
_NtWlanApQoSMode_Object=MibScalar
ntWlanApQoSMode=_NtWlanApQoSMode_Object((1,3,6,1,4,1,45,1,11,1,12,1),_NtWlanApQoSMode_Type())
ntWlanApQoSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApQoSMode.setStatus(_A)
_NtWlanApQoSEtherTypeToQueueTable_Object=MibTable
ntWlanApQoSEtherTypeToQueueTable=_NtWlanApQoSEtherTypeToQueueTable_Object((1,3,6,1,4,1,45,1,11,1,12,2))
if mibBuilder.loadTexts:ntWlanApQoSEtherTypeToQueueTable.setStatus(_A)
_NtWlanApQoSEtherTypeToQueueEntry_Object=MibTableRow
ntWlanApQoSEtherTypeToQueueEntry=_NtWlanApQoSEtherTypeToQueueEntry_Object((1,3,6,1,4,1,45,1,11,1,12,2,1))
ntWlanApQoSEtherTypeToQueueEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:ntWlanApQoSEtherTypeToQueueEntry.setStatus(_A)
class _NtWlanApQoSEtherTypeToQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtWlanApQoSEtherTypeToQueueIndex_Type.__name__=_C
_NtWlanApQoSEtherTypeToQueueIndex_Object=MibTableColumn
ntWlanApQoSEtherTypeToQueueIndex=_NtWlanApQoSEtherTypeToQueueIndex_Object((1,3,6,1,4,1,45,1,11,1,12,2,1,1),_NtWlanApQoSEtherTypeToQueueIndex_Type())
ntWlanApQoSEtherTypeToQueueIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApQoSEtherTypeToQueueIndex.setStatus(_A)
class _NtWlanApQoSEtherTypeToQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NtWlanApQoSEtherTypeToQueueNumber_Type.__name__=_C
_NtWlanApQoSEtherTypeToQueueNumber_Object=MibTableColumn
ntWlanApQoSEtherTypeToQueueNumber=_NtWlanApQoSEtherTypeToQueueNumber_Object((1,3,6,1,4,1,45,1,11,1,12,2,1,2),_NtWlanApQoSEtherTypeToQueueNumber_Type())
ntWlanApQoSEtherTypeToQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApQoSEtherTypeToQueueNumber.setStatus(_A)
_NtWlanApQoSEtherTypeToQueueRowStatus_Type=RowStatus
_NtWlanApQoSEtherTypeToQueueRowStatus_Object=MibTableColumn
ntWlanApQoSEtherTypeToQueueRowStatus=_NtWlanApQoSEtherTypeToQueueRowStatus_Object((1,3,6,1,4,1,45,1,11,1,12,2,1,3),_NtWlanApQoSEtherTypeToQueueRowStatus_Type())
ntWlanApQoSEtherTypeToQueueRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApQoSEtherTypeToQueueRowStatus.setStatus(_A)
_NtWlanApQoSMACToQueueTable_Object=MibTable
ntWlanApQoSMACToQueueTable=_NtWlanApQoSMACToQueueTable_Object((1,3,6,1,4,1,45,1,11,1,12,3))
if mibBuilder.loadTexts:ntWlanApQoSMACToQueueTable.setStatus(_A)
_NtWlanApQoSMACToQueueEntry_Object=MibTableRow
ntWlanApQoSMACToQueueEntry=_NtWlanApQoSMACToQueueEntry_Object((1,3,6,1,4,1,45,1,11,1,12,3,1))
ntWlanApQoSMACToQueueEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:ntWlanApQoSMACToQueueEntry.setStatus(_A)
_NtWlanApQoSMACToQueueAddress_Type=MacAddress
_NtWlanApQoSMACToQueueAddress_Object=MibTableColumn
ntWlanApQoSMACToQueueAddress=_NtWlanApQoSMACToQueueAddress_Object((1,3,6,1,4,1,45,1,11,1,12,3,1,1),_NtWlanApQoSMACToQueueAddress_Type())
ntWlanApQoSMACToQueueAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApQoSMACToQueueAddress.setStatus(_A)
class _NtWlanApQoSMACToQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NtWlanApQoSMACToQueueNumber_Type.__name__=_C
_NtWlanApQoSMACToQueueNumber_Object=MibTableColumn
ntWlanApQoSMACToQueueNumber=_NtWlanApQoSMACToQueueNumber_Object((1,3,6,1,4,1,45,1,11,1,12,3,1,2),_NtWlanApQoSMACToQueueNumber_Type())
ntWlanApQoSMACToQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApQoSMACToQueueNumber.setStatus(_A)
_NtWlanApQoSMACToQueueRowStatus_Type=RowStatus
_NtWlanApQoSMACToQueueRowStatus_Object=MibTableColumn
ntWlanApQoSMACToQueueRowStatus=_NtWlanApQoSMACToQueueRowStatus_Object((1,3,6,1,4,1,45,1,11,1,12,3,1,3),_NtWlanApQoSMACToQueueRowStatus_Type())
ntWlanApQoSMACToQueueRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApQoSMACToQueueRowStatus.setStatus(_A)
_NtWlanApVlan_ObjectIdentity=ObjectIdentity
ntWlanApVlan=_NtWlanApVlan_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,13))
_NtWlanApVlanEnabled_Type=TruthValue
_NtWlanApVlanEnabled_Object=MibScalar
ntWlanApVlanEnabled=_NtWlanApVlanEnabled_Object((1,3,6,1,4,1,45,1,11,1,13,1),_NtWlanApVlanEnabled_Type())
ntWlanApVlanEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApVlanEnabled.setStatus(_A)
_NtWlanApVlanTable_Object=MibTable
ntWlanApVlanTable=_NtWlanApVlanTable_Object((1,3,6,1,4,1,45,1,11,1,13,2))
if mibBuilder.loadTexts:ntWlanApVlanTable.setStatus(_A)
_NtWlanApVlanEntry_Object=MibTableRow
ntWlanApVlanEntry=_NtWlanApVlanEntry_Object((1,3,6,1,4,1,45,1,11,1,13,2,1))
ntWlanApVlanEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:ntWlanApVlanEntry.setStatus(_A)
_NtWlanApVlanIfIndex_Type=InterfaceIndex
_NtWlanApVlanIfIndex_Object=MibTableColumn
ntWlanApVlanIfIndex=_NtWlanApVlanIfIndex_Object((1,3,6,1,4,1,45,1,11,1,13,2,1,1),_NtWlanApVlanIfIndex_Type())
ntWlanApVlanIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApVlanIfIndex.setStatus(_A)
class _NtWlanApVlanDefaultVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_NtWlanApVlanDefaultVid_Type.__name__=_C
_NtWlanApVlanDefaultVid_Object=MibTableColumn
ntWlanApVlanDefaultVid=_NtWlanApVlanDefaultVid_Object((1,3,6,1,4,1,45,1,11,1,13,2,1,2),_NtWlanApVlanDefaultVid_Type())
ntWlanApVlanDefaultVid.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApVlanDefaultVid.setStatus(_A)
_NtWlanApVlanMUMACToVidTable_Object=MibTable
ntWlanApVlanMUMACToVidTable=_NtWlanApVlanMUMACToVidTable_Object((1,3,6,1,4,1,45,1,11,1,13,3))
if mibBuilder.loadTexts:ntWlanApVlanMUMACToVidTable.setStatus(_A)
_NtWlanApVlanMUMACToVidEntry_Object=MibTableRow
ntWlanApVlanMUMACToVidEntry=_NtWlanApVlanMUMACToVidEntry_Object((1,3,6,1,4,1,45,1,11,1,13,3,1))
ntWlanApVlanMUMACToVidEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:ntWlanApVlanMUMACToVidEntry.setStatus(_A)
_NtWlanApVlanMUMACToVidAddress_Type=MacAddress
_NtWlanApVlanMUMACToVidAddress_Object=MibTableColumn
ntWlanApVlanMUMACToVidAddress=_NtWlanApVlanMUMACToVidAddress_Object((1,3,6,1,4,1,45,1,11,1,13,3,1,1),_NtWlanApVlanMUMACToVidAddress_Type())
ntWlanApVlanMUMACToVidAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApVlanMUMACToVidAddress.setStatus(_A)
class _NtWlanApVlanMUMACToVidNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_NtWlanApVlanMUMACToVidNumber_Type.__name__=_C
_NtWlanApVlanMUMACToVidNumber_Object=MibTableColumn
ntWlanApVlanMUMACToVidNumber=_NtWlanApVlanMUMACToVidNumber_Object((1,3,6,1,4,1,45,1,11,1,13,3,1,2),_NtWlanApVlanMUMACToVidNumber_Type())
ntWlanApVlanMUMACToVidNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ntWlanApVlanMUMACToVidNumber.setStatus(_A)
_NtWlanApStats_ObjectIdentity=ObjectIdentity
ntWlanApStats=_NtWlanApStats_ObjectIdentity((1,3,6,1,4,1,45,1,11,1,14))
_NtWlanApMUStatsTable_Object=MibTable
ntWlanApMUStatsTable=_NtWlanApMUStatsTable_Object((1,3,6,1,4,1,45,1,11,1,14,1))
if mibBuilder.loadTexts:ntWlanApMUStatsTable.setStatus(_A)
_NtWlanApMUStatsEntry_Object=MibTableRow
ntWlanApMUStatsEntry=_NtWlanApMUStatsEntry_Object((1,3,6,1,4,1,45,1,11,1,14,1,1))
ntWlanApMUStatsEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:ntWlanApMUStatsEntry.setStatus(_A)
_NtWlanApMUStatsMUAddress_Type=MacAddress
_NtWlanApMUStatsMUAddress_Object=MibTableColumn
ntWlanApMUStatsMUAddress=_NtWlanApMUStatsMUAddress_Object((1,3,6,1,4,1,45,1,11,1,14,1,1,1),_NtWlanApMUStatsMUAddress_Type())
ntWlanApMUStatsMUAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ntWlanApMUStatsMUAddress.setStatus(_A)
_NtWlanApMUStatsPacketsIn_Type=Counter32
_NtWlanApMUStatsPacketsIn_Object=MibTableColumn
ntWlanApMUStatsPacketsIn=_NtWlanApMUStatsPacketsIn_Object((1,3,6,1,4,1,45,1,11,1,14,1,1,2),_NtWlanApMUStatsPacketsIn_Type())
ntWlanApMUStatsPacketsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanApMUStatsPacketsIn.setStatus(_A)
_NtWlanApMUStatsPacketsOut_Type=Counter32
_NtWlanApMUStatsPacketsOut_Object=MibTableColumn
ntWlanApMUStatsPacketsOut=_NtWlanApMUStatsPacketsOut_Object((1,3,6,1,4,1,45,1,11,1,14,1,1,3),_NtWlanApMUStatsPacketsOut_Type())
ntWlanApMUStatsPacketsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanApMUStatsPacketsOut.setStatus(_A)
_NtWlanApMUStatsOctetsIn_Type=Counter32
_NtWlanApMUStatsOctetsIn_Object=MibTableColumn
ntWlanApMUStatsOctetsIn=_NtWlanApMUStatsOctetsIn_Object((1,3,6,1,4,1,45,1,11,1,14,1,1,4),_NtWlanApMUStatsOctetsIn_Type())
ntWlanApMUStatsOctetsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanApMUStatsOctetsIn.setStatus(_A)
_NtWlanApMUStatsOctetsOut_Type=Counter32
_NtWlanApMUStatsOctetsOut_Object=MibTableColumn
ntWlanApMUStatsOctetsOut=_NtWlanApMUStatsOctetsOut_Object((1,3,6,1,4,1,45,1,11,1,14,1,1,5),_NtWlanApMUStatsOctetsOut_Type())
ntWlanApMUStatsOctetsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:ntWlanApMUStatsOctetsOut.setStatus(_A)
ntWlanApDot1xAuthenticationFail=NotificationType((1,3,6,1,4,1,45,1,11,1,8,0,101))
ntWlanApDot1xAuthenticationFail.setObjects(*((_H,_J),(_E,_I)))
if mibBuilder.loadTexts:ntWlanApDot1xAuthenticationFail.setStatus(_A)
ntWlanApMuAssocTrap=NotificationType((1,3,6,1,4,1,45,1,11,1,8,0,111))
ntWlanApMuAssocTrap.setObjects(*((_H,_J),(_E,_I),(_E,_Q)))
if mibBuilder.loadTexts:ntWlanApMuAssocTrap.setStatus(_A)
ntWlanApMuDisAssocTrap=NotificationType((1,3,6,1,4,1,45,1,11,1,8,0,112))
ntWlanApMuDisAssocTrap.setObjects(*((_H,_J),(_E,_q),(_E,_Q)))
if mibBuilder.loadTexts:ntWlanApMuDisAssocTrap.setStatus(_A)
ntWlanApMuWEPAuthFail=NotificationType((1,3,6,1,4,1,45,1,11,1,8,0,113))
ntWlanApMuWEPAuthFail.setObjects(*((_H,_L),(_E,_I)))
if mibBuilder.loadTexts:ntWlanApMuWEPAuthFail.setStatus(_A)
ntWlanApMuWPAAuthFail=NotificationType((1,3,6,1,4,1,45,1,11,1,8,0,114))
ntWlanApMuWPAAuthFail.setObjects(*((_H,_L),(_E,_I)))
if mibBuilder.loadTexts:ntWlanApMuWPAAuthFail.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'NtWlanApDataRate':NtWlanApDataRate,'NtWlanApWEPKey':NtWlanApWEPKey,'nortelWlanApMib':nortelWlanApMib,'ntWlanApSys':ntWlanApSys,'ntWlanSwHardwareVer':ntWlanSwHardwareVer,'ntWlanSwBootRomVer':ntWlanSwBootRomVer,'ntWlanSwOpCodeVer':ntWlanSwOpCodeVer,'ntWlanSwCountryCode':ntWlanSwCountryCode,'ntWlanSwNNDataFileVer':ntWlanSwNNDataFileVer,'ntWlanApLineMgnt':ntWlanApLineMgnt,'ntWlanLineTable':ntWlanLineTable,'ntWlanLineEntry':ntWlanLineEntry,_S:ntWlanLineIndex,'ntWlanLineDataBits':ntWlanLineDataBits,'ntWlanLineParity':ntWlanLineParity,'ntWlanLineSpeed':ntWlanLineSpeed,'ntWlanLineStopBits':ntWlanLineStopBits,'ntWlanApPortMgnt':ntWlanApPortMgnt,'ntWlanPortTable':ntWlanPortTable,'ntWlanPortEntry':ntWlanPortEntry,_T:ntWlanPortIndex,'ntWlanPortName':ntWlanPortName,'ntWlanPortType':ntWlanPortType,'ntWlanPortSpeedDpxCfg':ntWlanPortSpeedDpxCfg,'ntWlanPortFlowCtrlCfg':ntWlanPortFlowCtrlCfg,'ntWlanPortCapabilities':ntWlanPortCapabilities,'ntWlanPortAutonegotiation':ntWlanPortAutonegotiation,'ntWlanPortSpeedDpxStatus':ntWlanPortSpeedDpxStatus,'ntWlanPortFlowCtrlStatus':ntWlanPortFlowCtrlStatus,'ntWlanApFileTransferMgt':ntWlanApFileTransferMgt,'ntWlanTransferStart':ntWlanTransferStart,'ntWlanTransferType':ntWlanTransferType,'ntWlanFileType':ntWlanFileType,'ntWlanSrcFile':ntWlanSrcFile,'ntWlanDestFile':ntWlanDestFile,'ntWlanFileServer':ntWlanFileServer,'ntWlanUserName':ntWlanUserName,'ntWlanPassword':ntWlanPassword,'ntWlanFileTransferStatus':ntWlanFileTransferStatus,'ntWlanApResetMgt':ntWlanApResetMgt,'ntWlanRestartOpCodeFile':ntWlanRestartOpCodeFile,'ntWlanRestartControl':ntWlanRestartControl,'ntWlanApIpMgt':ntWlanApIpMgt,'ntWlanNetConfigIPAddress':ntWlanNetConfigIPAddress,'ntWlanNetConfigSubnetMask':ntWlanNetConfigSubnetMask,'ntWlanNetDefaultGateway':ntWlanNetDefaultGateway,'ntWlanIpHttpState':ntWlanIpHttpState,'ntWlanIpHttpPort':ntWlanIpHttpPort,'ntWlanApDot11':ntWlanApDot11,'ntWlanDot11Phy':ntWlanDot11Phy,'ntWlanDot11PhyOperationTable':ntWlanDot11PhyOperationTable,'ntWlanDot11PhyOperationEntry':ntWlanDot11PhyOperationEntry,_c:ntWlanDot11Index,'ntWlanDot11TurboModeEnabled':ntWlanDot11TurboModeEnabled,'ntWlanDot11PreambleLength':ntWlanDot11PreambleLength,'ntWlanDot11dWorldModeEnabled':ntWlanDot11dWorldModeEnabled,'ntWlanDot11ClosedSystem':ntWlanDot11ClosedSystem,'ntWlanDot11AuthenticationEntry':ntWlanDot11AuthenticationEntry,'ntWlanDot118021xSupport':ntWlanDot118021xSupport,'ntWlanDot118021xRequired':ntWlanDot118021xRequired,'ntWlanDot118021xBcastKeyRefresh':ntWlanDot118021xBcastKeyRefresh,'ntWlanDot118021xSessKeyRefresh':ntWlanDot118021xSessKeyRefresh,'ntWlanDot118021xReAuthRefresh':ntWlanDot118021xReAuthRefresh,'ntWlanDot11AuthenticationServerTable':ntWlanDot11AuthenticationServerTable,'ntWlanDot11AuthenticationServerEntry':ntWlanDot11AuthenticationServerEntry,_e:ntWlanDot11ServerIndex,'ntWlanDot11AuthenticationServer':ntWlanDot11AuthenticationServer,'ntWlanDot11AuthenticationPort':ntWlanDot11AuthenticationPort,'ntWlanDot11AuthenticationKey':ntWlanDot11AuthenticationKey,'ntWlanDot11AuthenticationRetransmit':ntWlanDot11AuthenticationRetransmit,'ntWlanDot11AuthenticationTimeout':ntWlanDot11AuthenticationTimeout,'ntWlanDot11SecondaryAuthServer':ntWlanDot11SecondaryAuthServer,'ntWlanDot11SecondaryAuthPort':ntWlanDot11SecondaryAuthPort,'ntWlanDot11SecondaryAuthKey':ntWlanDot11SecondaryAuthKey,'ntWlanDot11SecondaryAuthRetransmit':ntWlanDot11SecondaryAuthRetransmit,'ntWlanDot11SecondaryAuthTimeout':ntWlanDot11SecondaryAuthTimeout,'ntWlanDot11FilterTable':ntWlanDot11FilterTable,'ntWlanDot11FilterEntry':ntWlanDot11FilterEntry,_f:ntWlanDot11FilterIndex,'ntWlanDot11FilterAddress':ntWlanDot11FilterAddress,'ntWlanDot11FilterStatus':ntWlanDot11FilterStatus,'ntWlanDot11TrapTable':ntWlanDot11TrapTable,'ntWlanDot11TrapEntry':ntWlanDot11TrapEntry,_g:ntWlanDot11InterfaceIndex,_I:ntWlanDot11AssociationStationAddress,_q:ntWlanDot11DisassociationStationAddress,_Q:ntWlanDot11AssociationMU,'ntWlanApTraps':ntWlanApTraps,'ntWlanApTraps0':ntWlanApTraps0,'ntWlanApDot1xAuthenticationFail':ntWlanApDot1xAuthenticationFail,'ntWlanApMuAssocTrap':ntWlanApMuAssocTrap,'ntWlanApMuDisAssocTrap':ntWlanApMuDisAssocTrap,'ntWlanApMuWEPAuthFail':ntWlanApMuWEPAuthFail,'ntWlanApMuWPAAuthFail':ntWlanApMuWPAAuthFail,'ntWlanApMuAssocTrapEnabled':ntWlanApMuAssocTrapEnabled,'ntWlanApMuDisAssocTrapEnabled':ntWlanApMuDisAssocTrapEnabled,'ntWlanApLID':ntWlanApLID,'ntWlanApLIDCheckEtherLinkEnabled':ntWlanApLIDCheckEtherLinkEnabled,'ntWlanApLIDCheckIPLinkEnabled':ntWlanApLIDCheckIPLinkEnabled,'ntWlanApLIDCheckIpLinkAddress':ntWlanApLIDCheckIpLinkAddress,'ntWlanApRateSupport':ntWlanApRateSupport,'ntWlanApRateSupportTable':ntWlanApRateSupportTable,'ntWlanApRateSupportEntry':ntWlanApRateSupportEntry,_h:ntWlanApRateSupportIfIndex,_i:ntWlanApRateSupportSpeed,'ntWlanApRateSupportLevel':ntWlanApRateSupportLevel,'ntWlanApSecurity':ntWlanApSecurity,'ntWlanApSecurityTable':ntWlanApSecurityTable,'ntWlanApSecurityEntry':ntWlanApSecurityEntry,_k:ntWlanApSecurityIfIndex,'ntWlanApSecurityEnabled':ntWlanApSecurityEnabled,'ntWlanApSecurityWEPAuthType':ntWlanApSecurityWEPAuthType,'ntWlanApSecurityWEPKeyLength':ntWlanApSecurityWEPKeyLength,'ntWlanApSecurityWEPActiveKey':ntWlanApSecurityWEPActiveKey,'ntWlanApSecurityWEPKey1':ntWlanApSecurityWEPKey1,'ntWlanApSecurityWEPKey2':ntWlanApSecurityWEPKey2,'ntWlanApSecurityWEPKey3':ntWlanApSecurityWEPKey3,'ntWlanApSecurityWEPKey4':ntWlanApSecurityWEPKey4,'ntWlanApSecurityWPASupport':ntWlanApSecurityWPASupport,'ntWlanApSecurityWPAMode':ntWlanApSecurityWPAMode,'ntWlanApSecurityWPAPreSharedKey':ntWlanApSecurityWPAPreSharedKey,'ntWlanApSecurityWPAMcastCypherMode':ntWlanApSecurityWPAMcastCypherMode,'ntWlanApQoS':ntWlanApQoS,'ntWlanApQoSMode':ntWlanApQoSMode,'ntWlanApQoSEtherTypeToQueueTable':ntWlanApQoSEtherTypeToQueueTable,'ntWlanApQoSEtherTypeToQueueEntry':ntWlanApQoSEtherTypeToQueueEntry,_l:ntWlanApQoSEtherTypeToQueueIndex,'ntWlanApQoSEtherTypeToQueueNumber':ntWlanApQoSEtherTypeToQueueNumber,'ntWlanApQoSEtherTypeToQueueRowStatus':ntWlanApQoSEtherTypeToQueueRowStatus,'ntWlanApQoSMACToQueueTable':ntWlanApQoSMACToQueueTable,'ntWlanApQoSMACToQueueEntry':ntWlanApQoSMACToQueueEntry,_m:ntWlanApQoSMACToQueueAddress,'ntWlanApQoSMACToQueueNumber':ntWlanApQoSMACToQueueNumber,'ntWlanApQoSMACToQueueRowStatus':ntWlanApQoSMACToQueueRowStatus,'ntWlanApVlan':ntWlanApVlan,'ntWlanApVlanEnabled':ntWlanApVlanEnabled,'ntWlanApVlanTable':ntWlanApVlanTable,'ntWlanApVlanEntry':ntWlanApVlanEntry,_n:ntWlanApVlanIfIndex,'ntWlanApVlanDefaultVid':ntWlanApVlanDefaultVid,'ntWlanApVlanMUMACToVidTable':ntWlanApVlanMUMACToVidTable,'ntWlanApVlanMUMACToVidEntry':ntWlanApVlanMUMACToVidEntry,_o:ntWlanApVlanMUMACToVidAddress,'ntWlanApVlanMUMACToVidNumber':ntWlanApVlanMUMACToVidNumber,'ntWlanApStats':ntWlanApStats,'ntWlanApMUStatsTable':ntWlanApMUStatsTable,'ntWlanApMUStatsEntry':ntWlanApMUStatsEntry,_p:ntWlanApMUStatsMUAddress,'ntWlanApMUStatsPacketsIn':ntWlanApMUStatsPacketsIn,'ntWlanApMUStatsPacketsOut':ntWlanApMUStatsPacketsOut,'ntWlanApMUStatsOctetsIn':ntWlanApMUStatsOctetsIn,'ntWlanApMUStatsOctetsOut':ntWlanApMUStatsOctetsOut})