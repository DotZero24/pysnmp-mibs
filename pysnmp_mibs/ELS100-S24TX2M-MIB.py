_f='notActive'
_e='active'
_d='dot3xFlowControl'
_c='backPressure'
_b='fullDuplex1000'
_a='halfDuplex1000'
_Z='fullDuplex100'
_Y='halfDuplex100'
_X='fullDuplex10'
_W='halfDuplex10'
_V='swPortMgtIndex'
_U='switchOIDIndex'
_T='notPresent'
_S='stackingModule2GB'
_R='thousandBaseGBIC'
_Q='thousandBaseT'
_P='thousandBaseLX'
_O='hundredBaseFX1Port'
_N='stackingModule4GB'
_M='hundredBaseFX2Port'
_L='IpAddress'
_K='thousandBaseSX'
_J='not-accessible'
_I='swUnitIndex'
_H='ELS100-S24TX2M-MIB'
_G='DisplayString'
_F='disabled'
_E='enabled'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,internet,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_L,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','internet','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
tpELS100S24TX2M=ModuleIdentity((1,3,6,1,4,1,52,3,9,1,10,7))
if mibBuilder.loadTexts:tpELS100S24TX2M.setRevisions(('2002-08-05 17:53','2002-02-20 22:02','1999-10-01 00:00'))
_SwitchInfo_ObjectIdentity=ObjectIdentity
switchInfo=_SwitchInfo_ObjectIdentity((1,3,6,1,4,1,52,3,9,1,10,7,1))
_SwitchNumber_Type=Integer32
_SwitchNumber_Object=MibScalar
switchNumber=_SwitchNumber_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,1),_SwitchNumber_Type())
switchNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:switchNumber.setStatus(_A)
_SwitchInfoTable_Object=MibTable
switchInfoTable=_SwitchInfoTable_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2))
if mibBuilder.loadTexts:switchInfoTable.setStatus(_A)
_SwitchInfoEntry_Object=MibTableRow
switchInfoEntry=_SwitchInfoEntry_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1))
switchInfoEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:switchInfoEntry.setStatus(_A)
_SwUnitIndex_Type=Integer32
_SwUnitIndex_Object=MibTableColumn
swUnitIndex=_SwUnitIndex_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,1),_SwUnitIndex_Type())
swUnitIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swUnitIndex.setStatus(_A)
class _SwMainBoardHwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwMainBoardHwVer_Type.__name__=_G
_SwMainBoardHwVer_Object=MibTableColumn
swMainBoardHwVer=_SwMainBoardHwVer_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,2),_SwMainBoardHwVer_Type())
swMainBoardHwVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swMainBoardHwVer.setStatus(_A)
class _SwMainBoardFwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwMainBoardFwVer_Type.__name__=_G
_SwMainBoardFwVer_Object=MibTableColumn
swMainBoardFwVer=_SwMainBoardFwVer_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,3),_SwMainBoardFwVer_Type())
swMainBoardFwVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swMainBoardFwVer.setStatus(_A)
class _SwAgentBoardHwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwAgentBoardHwVer_Type.__name__=_G
_SwAgentBoardHwVer_Object=MibTableColumn
swAgentBoardHwVer=_SwAgentBoardHwVer_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,4),_SwAgentBoardHwVer_Type())
swAgentBoardHwVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swAgentBoardHwVer.setStatus(_A)
class _SwAgentBoardFwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwAgentBoardFwVer_Type.__name__=_G
_SwAgentBoardFwVer_Object=MibTableColumn
swAgentBoardFwVer=_SwAgentBoardFwVer_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,5),_SwAgentBoardFwVer_Type())
swAgentBoardFwVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swAgentBoardFwVer.setStatus(_A)
class _SwAgentBoardPOSTCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwAgentBoardPOSTCodeVer_Type.__name__=_G
_SwAgentBoardPOSTCodeVer_Object=MibTableColumn
swAgentBoardPOSTCodeVer=_SwAgentBoardPOSTCodeVer_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,6),_SwAgentBoardPOSTCodeVer_Type())
swAgentBoardPOSTCodeVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swAgentBoardPOSTCodeVer.setStatus(_A)
_SwPortNumber_Type=Integer32
_SwPortNumber_Object=MibTableColumn
swPortNumber=_SwPortNumber_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,7),_SwPortNumber_Type())
swPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortNumber.setStatus(_A)
class _SwPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internalPower',1),('redundantPower',2),('internalAndRedundantPower',3)))
_SwPowerStatus_Type.__name__=_B
_SwPowerStatus_Object=MibTableColumn
swPowerStatus=_SwPowerStatus_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,8),_SwPowerStatus_Type())
swPowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swPowerStatus.setStatus(_A)
class _SwExpansionSlot1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_M,1),(_K,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),('other',9),(_T,10)))
_SwExpansionSlot1_Type.__name__=_B
_SwExpansionSlot1_Object=MibTableColumn
swExpansionSlot1=_SwExpansionSlot1_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,9),_SwExpansionSlot1_Type())
swExpansionSlot1.setMaxAccess(_D)
if mibBuilder.loadTexts:swExpansionSlot1.setStatus(_A)
class _SwExpansionSlot2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_M,1),(_K,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),('other',9),(_T,10)))
_SwExpansionSlot2_Type.__name__=_B
_SwExpansionSlot2_Object=MibTableColumn
swExpansionSlot2=_SwExpansionSlot2_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,10),_SwExpansionSlot2_Type())
swExpansionSlot2.setMaxAccess(_D)
if mibBuilder.loadTexts:swExpansionSlot2.setStatus(_A)
class _SwRoleInSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('backupMaster',2),('slave',3)))
_SwRoleInSystem_Type.__name__=_B
_SwRoleInSystem_Object=MibTableColumn
swRoleInSystem=_SwRoleInSystem_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,2,1,11),_SwRoleInSystem_Type())
swRoleInSystem.setMaxAccess(_D)
if mibBuilder.loadTexts:swRoleInSystem.setStatus(_A)
_SwitchOIDTable_Object=MibTable
switchOIDTable=_SwitchOIDTable_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,3))
if mibBuilder.loadTexts:switchOIDTable.setStatus(_A)
_SwitchOIDEntry_Object=MibTableRow
switchOIDEntry=_SwitchOIDEntry_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,3,1))
switchOIDEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:switchOIDEntry.setStatus(_A)
class _SwitchOIDIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwitchOIDIndex_Type.__name__=_B
_SwitchOIDIndex_Object=MibTableColumn
switchOIDIndex=_SwitchOIDIndex_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,3,1,1),_SwitchOIDIndex_Type())
switchOIDIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:switchOIDIndex.setStatus(_A)
_SwitchOIDValue_Type=ObjectIdentifier
_SwitchOIDValue_Object=MibTableColumn
switchOIDValue=_SwitchOIDValue_Object((1,3,6,1,4,1,52,3,9,1,10,7,1,3,1,2),_SwitchOIDValue_Type())
switchOIDValue.setMaxAccess(_D)
if mibBuilder.loadTexts:switchOIDValue.setStatus(_A)
_SwitchPortMgt_ObjectIdentity=ObjectIdentity
switchPortMgt=_SwitchPortMgt_ObjectIdentity((1,3,6,1,4,1,52,3,9,1,10,7,2))
_SwitchPortMgtTable_Object=MibTable
switchPortMgtTable=_SwitchPortMgtTable_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1))
if mibBuilder.loadTexts:switchPortMgtTable.setStatus(_A)
_SwitchPortMgtEntry_Object=MibTableRow
switchPortMgtEntry=_SwitchPortMgtEntry_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1,1))
switchPortMgtEntry.setIndexNames((0,_H,_I),(0,_H,_V))
if mibBuilder.loadTexts:switchPortMgtEntry.setStatus(_A)
_SwPortMgtIndex_Type=Integer32
_SwPortMgtIndex_Object=MibTableColumn
swPortMgtIndex=_SwPortMgtIndex_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1,1,1),_SwPortMgtIndex_Type())
swPortMgtIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swPortMgtIndex.setStatus(_A)
class _SwPortMgtPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hundredBaseTX',1),('hundredBaseFX',2),(_K,3)))
_SwPortMgtPortType_Type.__name__=_B
_SwPortMgtPortType_Object=MibTableColumn
swPortMgtPortType=_SwPortMgtPortType_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1,1,2),_SwPortMgtPortType_Type())
swPortMgtPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortMgtPortType.setStatus(_A)
class _SwPortMgtSpeedDpxAdmin_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),('autoNegotiation',7)))
_SwPortMgtSpeedDpxAdmin_Type.__name__=_B
_SwPortMgtSpeedDpxAdmin_Object=MibTableColumn
swPortMgtSpeedDpxAdmin=_SwPortMgtSpeedDpxAdmin_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1,1,3),_SwPortMgtSpeedDpxAdmin_Type())
swPortMgtSpeedDpxAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMgtSpeedDpxAdmin.setStatus(_A)
class _SwPortMgtSpeedDpxInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_SwPortMgtSpeedDpxInUse_Type.__name__=_B
_SwPortMgtSpeedDpxInUse_Object=MibTableColumn
swPortMgtSpeedDpxInUse=_SwPortMgtSpeedDpxInUse_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1,1,4),_SwPortMgtSpeedDpxInUse_Type())
swPortMgtSpeedDpxInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortMgtSpeedDpxInUse.setStatus(_A)
class _SwPortMgtFlowCtrlAdmin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_c,3),(_d,4)))
_SwPortMgtFlowCtrlAdmin_Type.__name__=_B
_SwPortMgtFlowCtrlAdmin_Object=MibTableColumn
swPortMgtFlowCtrlAdmin=_SwPortMgtFlowCtrlAdmin_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1,1,5),_SwPortMgtFlowCtrlAdmin_Type())
swPortMgtFlowCtrlAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMgtFlowCtrlAdmin.setStatus(_A)
class _SwPortMgtFlowCtrlInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),('none',3)))
_SwPortMgtFlowCtrlInUse_Type.__name__=_B
_SwPortMgtFlowCtrlInUse_Object=MibTableColumn
swPortMgtFlowCtrlInUse=_SwPortMgtFlowCtrlInUse_Object((1,3,6,1,4,1,52,3,9,1,10,7,2,1,1,6),_SwPortMgtFlowCtrlInUse_Type())
swPortMgtFlowCtrlInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortMgtFlowCtrlInUse.setStatus(_A)
_SystemSTAMgt_ObjectIdentity=ObjectIdentity
systemSTAMgt=_SystemSTAMgt_ObjectIdentity((1,3,6,1,4,1,52,3,9,1,10,7,3))
class _SystemSTAStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SystemSTAStatus_Type.__name__=_B
_SystemSTAStatus_Object=MibScalar
systemSTAStatus=_SystemSTAStatus_Object((1,3,6,1,4,1,52,3,9,1,10,7,3,1),_SystemSTAStatus_Type())
systemSTAStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSTAStatus.setStatus(_A)
_TftpDownloadMgt_ObjectIdentity=ObjectIdentity
tftpDownloadMgt=_TftpDownloadMgt_ObjectIdentity((1,3,6,1,4,1,52,3,9,1,10,7,4))
class _TftpDownloadServerIP_Type(IpAddress):defaultHexValue='00000000'
_TftpDownloadServerIP_Type.__name__=_L
_TftpDownloadServerIP_Object=MibScalar
tftpDownloadServerIP=_TftpDownloadServerIP_Object((1,3,6,1,4,1,52,3,9,1,10,7,4,1),_TftpDownloadServerIP_Type())
tftpDownloadServerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpDownloadServerIP.setStatus(_A)
class _TftpDownloadAgentBoardFwFileName_Type(DisplayString):defaultValue=OctetString('es3526f.bin');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TftpDownloadAgentBoardFwFileName_Type.__name__=_G
_TftpDownloadAgentBoardFwFileName_Object=MibScalar
tftpDownloadAgentBoardFwFileName=_TftpDownloadAgentBoardFwFileName_Object((1,3,6,1,4,1,52,3,9,1,10,7,4,2),_TftpDownloadAgentBoardFwFileName_Type())
tftpDownloadAgentBoardFwFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpDownloadAgentBoardFwFileName.setStatus(_A)
class _TftpDownloadAgentBoardFwDownloadNode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permanent',1),('temporary',2)))
_TftpDownloadAgentBoardFwDownloadNode_Type.__name__=_B
_TftpDownloadAgentBoardFwDownloadNode_Object=MibScalar
tftpDownloadAgentBoardFwDownloadNode=_TftpDownloadAgentBoardFwDownloadNode_Object((1,3,6,1,4,1,52,3,9,1,10,7,4,3),_TftpDownloadAgentBoardFwDownloadNode_Type())
tftpDownloadAgentBoardFwDownloadNode.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpDownloadAgentBoardFwDownloadNode.setStatus(_A)
class _TftpDownloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_TftpDownloadStatus_Type.__name__=_B
_TftpDownloadStatus_Object=MibScalar
tftpDownloadStatus=_TftpDownloadStatus_Object((1,3,6,1,4,1,52,3,9,1,10,7,4,4),_TftpDownloadStatus_Type())
tftpDownloadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpDownloadStatus.setStatus(_A)
_RestartMgt_ObjectIdentity=ObjectIdentity
restartMgt=_RestartMgt_ObjectIdentity((1,3,6,1,4,1,52,3,9,1,10,7,5))
class _RestartOptionPOST_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RestartOptionPOST_Type.__name__=_B
_RestartOptionPOST_Object=MibScalar
restartOptionPOST=_RestartOptionPOST_Object((1,3,6,1,4,1,52,3,9,1,10,7,5,1),_RestartOptionPOST_Type())
restartOptionPOST.setMaxAccess(_C)
if mibBuilder.loadTexts:restartOptionPOST.setStatus(_A)
class _RestartOptionReloadFactoryDefault_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RestartOptionReloadFactoryDefault_Type.__name__=_B
_RestartOptionReloadFactoryDefault_Object=MibScalar
restartOptionReloadFactoryDefault=_RestartOptionReloadFactoryDefault_Object((1,3,6,1,4,1,52,3,9,1,10,7,5,2),_RestartOptionReloadFactoryDefault_Type())
restartOptionReloadFactoryDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:restartOptionReloadFactoryDefault.setStatus(_A)
class _RestartOptionKeepIpSetting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RestartOptionKeepIpSetting_Type.__name__=_B
_RestartOptionKeepIpSetting_Object=MibScalar
restartOptionKeepIpSetting=_RestartOptionKeepIpSetting_Object((1,3,6,1,4,1,52,3,9,1,10,7,5,3),_RestartOptionKeepIpSetting_Type())
restartOptionKeepIpSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:restartOptionKeepIpSetting.setStatus(_A)
class _RestartOptionKeepUserAuthentication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RestartOptionKeepUserAuthentication_Type.__name__=_B
_RestartOptionKeepUserAuthentication_Object=MibScalar
restartOptionKeepUserAuthentication=_RestartOptionKeepUserAuthentication_Object((1,3,6,1,4,1,52,3,9,1,10,7,5,4),_RestartOptionKeepUserAuthentication_Type())
restartOptionKeepUserAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:restartOptionKeepUserAuthentication.setStatus(_A)
class _RestartAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_RestartAction_Type.__name__=_B
_RestartAction_Object=MibScalar
restartAction=_RestartAction_Object((1,3,6,1,4,1,52,3,9,1,10,7,5,5),_RestartAction_Type())
restartAction.setMaxAccess(_C)
if mibBuilder.loadTexts:restartAction.setStatus(_A)
_PortMirrorMgt_ObjectIdentity=ObjectIdentity
portMirrorMgt=_PortMirrorMgt_ObjectIdentity((1,3,6,1,4,1,52,3,9,1,10,7,6))
class _PortMirrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PortMirrorStatus_Type.__name__=_B
_PortMirrorStatus_Object=MibScalar
portMirrorStatus=_PortMirrorStatus_Object((1,3,6,1,4,1,52,3,9,1,10,7,6,1),_PortMirrorStatus_Type())
portMirrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portMirrorStatus.setStatus(_A)
_PortMirrorSnifferPort_Type=Integer32
_PortMirrorSnifferPort_Object=MibScalar
portMirrorSnifferPort=_PortMirrorSnifferPort_Object((1,3,6,1,4,1,52,3,9,1,10,7,6,2),_PortMirrorSnifferPort_Type())
portMirrorSnifferPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portMirrorSnifferPort.setStatus(_A)
_PortMirrorMirroredPort_Type=Integer32
_PortMirrorMirroredPort_Object=MibScalar
portMirrorMirroredPort=_PortMirrorMirroredPort_Object((1,3,6,1,4,1,52,3,9,1,10,7,6,3),_PortMirrorMirroredPort_Type())
portMirrorMirroredPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portMirrorMirroredPort.setStatus(_A)
_IgmpMgt_ObjectIdentity=ObjectIdentity
igmpMgt=_IgmpMgt_ObjectIdentity((1,3,6,1,4,1,52,3,9,1,10,7,7))
class _IgmpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_IgmpStatus_Type.__name__=_B
_IgmpStatus_Object=MibScalar
igmpStatus=_IgmpStatus_Object((1,3,6,1,4,1,52,3,9,1,10,7,7,1),_IgmpStatus_Type())
igmpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpStatus.setStatus(_A)
class _IgmpQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,16))
_IgmpQueryCount_Type.__name__=_B
_IgmpQueryCount_Object=MibScalar
igmpQueryCount=_IgmpQueryCount_Object((1,3,6,1,4,1,52,3,9,1,10,7,7,2),_IgmpQueryCount_Type())
igmpQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpQueryCount.setStatus(_A)
class _IgmpReportDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_IgmpReportDelay_Type.__name__=_B
_IgmpReportDelay_Object=MibScalar
igmpReportDelay=_IgmpReportDelay_Object((1,3,6,1,4,1,52,3,9,1,10,7,7,3),_IgmpReportDelay_Type())
igmpReportDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpReportDelay.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'tpELS100S24TX2M':tpELS100S24TX2M,'switchInfo':switchInfo,'switchNumber':switchNumber,'switchInfoTable':switchInfoTable,'switchInfoEntry':switchInfoEntry,_I:swUnitIndex,'swMainBoardHwVer':swMainBoardHwVer,'swMainBoardFwVer':swMainBoardFwVer,'swAgentBoardHwVer':swAgentBoardHwVer,'swAgentBoardFwVer':swAgentBoardFwVer,'swAgentBoardPOSTCodeVer':swAgentBoardPOSTCodeVer,'swPortNumber':swPortNumber,'swPowerStatus':swPowerStatus,'swExpansionSlot1':swExpansionSlot1,'swExpansionSlot2':swExpansionSlot2,'swRoleInSystem':swRoleInSystem,'switchOIDTable':switchOIDTable,'switchOIDEntry':switchOIDEntry,_U:switchOIDIndex,'switchOIDValue':switchOIDValue,'switchPortMgt':switchPortMgt,'switchPortMgtTable':switchPortMgtTable,'switchPortMgtEntry':switchPortMgtEntry,_V:swPortMgtIndex,'swPortMgtPortType':swPortMgtPortType,'swPortMgtSpeedDpxAdmin':swPortMgtSpeedDpxAdmin,'swPortMgtSpeedDpxInUse':swPortMgtSpeedDpxInUse,'swPortMgtFlowCtrlAdmin':swPortMgtFlowCtrlAdmin,'swPortMgtFlowCtrlInUse':swPortMgtFlowCtrlInUse,'systemSTAMgt':systemSTAMgt,'systemSTAStatus':systemSTAStatus,'tftpDownloadMgt':tftpDownloadMgt,'tftpDownloadServerIP':tftpDownloadServerIP,'tftpDownloadAgentBoardFwFileName':tftpDownloadAgentBoardFwFileName,'tftpDownloadAgentBoardFwDownloadNode':tftpDownloadAgentBoardFwDownloadNode,'tftpDownloadStatus':tftpDownloadStatus,'restartMgt':restartMgt,'restartOptionPOST':restartOptionPOST,'restartOptionReloadFactoryDefault':restartOptionReloadFactoryDefault,'restartOptionKeepIpSetting':restartOptionKeepIpSetting,'restartOptionKeepUserAuthentication':restartOptionKeepUserAuthentication,'restartAction':restartAction,'portMirrorMgt':portMirrorMgt,'portMirrorStatus':portMirrorStatus,'portMirrorSnifferPort':portMirrorSnifferPort,'portMirrorMirroredPort':portMirrorMirroredPort,'igmpMgt':igmpMgt,'igmpStatus':igmpStatus,'igmpQueryCount':igmpQueryCount,'igmpReportDelay':igmpReportDelay})