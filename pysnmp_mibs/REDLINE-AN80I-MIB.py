_AE='redlineAn80iNotificationGroup'
_AD='redlineAn80iPtpGroup'
_AC='redlineAn80iPmpGroup'
_AB='redlineAn80iPtpPmpGroup'
_AA='an80iSWUpgradeSuccess'
_A9='an80iSWUpgradeFailed'
_A8='an80iIdChangedTrap'
_A7='an80iDFSEventTrap'
_A6='an80iSaveConfigTrap'
_A5='an80iHardwareFailTrap'
_A4='an80iEepromCorruptedTrap'
_A3='an80iFirmwareConfigFailTrap'
_A2='an80iPswdChangeFailTrap'
_A1='an80iResetStatistics'
_A0='an80iSaveIdConfiguration'
_z='an80iNextAvailId'
_y='an80iMaxId'
_x='an80iRegisteredConnections'
_w='an80iRegisteredStations'
_v='an80iMaximumDistance'
_u='an80iRegistrationPeriod'
_t='an80iSwDownloadControl'
_s='an80iSwDownloadStatus'
_r='an80iTelnetPort'
_q='an80iTelnetAccess'
_p='an80iHttpAccess'
_o='an80iEthernetFollowsWirelessTimeout'
_n='an80iEthernetFollowsWireless'
_m='an80iLowLatencyMode'
_l='an80iFlowControl'
_k='an80iEtherPortMode'
_j='an80iEtherPortConn'
_i='an80iTurboModeControl'
_h='an80iAtpControl'
_g='an80iActiveRFLinks'
_f='an80iAntennaGain'
_e='an80iDFSAction'
_d='an80iRFStatusCode'
_c='an80iSystemMode'
_b='an80iMaxTxPower'
_a='an80iOPeratingFrequency'
_Z='an80iCurrFrequency'
_Y='an80iChannelAutoScan'
_X='an80iCurrTxPower'
_W='an80iAntennaAllignmentMode'
_V='an80iActivateConfig'
_U='an80iSaveConfig'
_T='an80iRadioType'
_S='an80iHardwareType'
_R='an80iOptionsKey'
_Q='read-create'
_P='an80iOptionsKeyId'
_O='DisplayString'
_N='an80iLastModifId'
_M='disable'
_L='enable'
_K='an80iSwDownloadTftpFile'
_J='an80iSwDownloadTftpAddress'
_I='an80iSwDownloadTftpAddressType'
_H='disabled'
_G='enabled'
_F='noop'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='current'
_A='REDLINE-AN80I-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
redlineSystem,=mibBuilder.importSymbols('REDLINE-MIB','redlineSystem')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','RowStatus','TextualConvention')
redlineAn80iMib=ModuleIdentity((1,3,6,1,4,1,10728,2,1,3))
if mibBuilder.loadTexts:redlineAn80iMib.setRevisions(('2005-11-29 15:43',))
_RedlineAn80iTrapDefinitions_ObjectIdentity=ObjectIdentity
redlineAn80iTrapDefinitions=_RedlineAn80iTrapDefinitions_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,0))
_RedlineAn80iPtpPmpObjects_ObjectIdentity=ObjectIdentity
redlineAn80iPtpPmpObjects=_RedlineAn80iPtpPmpObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,1))
_RedlineAn80iSystemObjects_ObjectIdentity=ObjectIdentity
redlineAn80iSystemObjects=_RedlineAn80iSystemObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,1,1))
_An80iOptionsKeyTable_Object=MibTable
an80iOptionsKeyTable=_An80iOptionsKeyTable_Object((1,3,6,1,4,1,10728,2,1,3,1,1,1))
if mibBuilder.loadTexts:an80iOptionsKeyTable.setStatus(_B)
_An80iOptionsKeyEntry_Object=MibTableRow
an80iOptionsKeyEntry=_An80iOptionsKeyEntry_Object((1,3,6,1,4,1,10728,2,1,3,1,1,1,1))
an80iOptionsKeyEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:an80iOptionsKeyEntry.setStatus(_B)
class _An80iOptionsKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_An80iOptionsKeyId_Type.__name__=_D
_An80iOptionsKeyId_Object=MibTableColumn
an80iOptionsKeyId=_An80iOptionsKeyId_Object((1,3,6,1,4,1,10728,2,1,3,1,1,1,1,1),_An80iOptionsKeyId_Type())
an80iOptionsKeyId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:an80iOptionsKeyId.setStatus(_B)
_An80iOptionsKey_Type=DisplayString
_An80iOptionsKey_Object=MibTableColumn
an80iOptionsKey=_An80iOptionsKey_Object((1,3,6,1,4,1,10728,2,1,3,1,1,1,1,2),_An80iOptionsKey_Type())
an80iOptionsKey.setMaxAccess(_Q)
if mibBuilder.loadTexts:an80iOptionsKey.setStatus(_B)
_An80iOptionsKeyStatus_Type=RowStatus
_An80iOptionsKeyStatus_Object=MibTableColumn
an80iOptionsKeyStatus=_An80iOptionsKeyStatus_Object((1,3,6,1,4,1,10728,2,1,3,1,1,1,1,3),_An80iOptionsKeyStatus_Type())
an80iOptionsKeyStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:an80iOptionsKeyStatus.setStatus(_B)
_An80iHardwareType_Type=Integer32
_An80iHardwareType_Object=MibScalar
an80iHardwareType=_An80iHardwareType_Object((1,3,6,1,4,1,10728,2,1,3,1,1,2),_An80iHardwareType_Type())
an80iHardwareType.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iHardwareType.setStatus(_B)
_An80iRadioType_Type=Integer32
_An80iRadioType_Object=MibScalar
an80iRadioType=_An80iRadioType_Object((1,3,6,1,4,1,10728,2,1,3,1,1,3),_An80iRadioType_Type())
an80iRadioType.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iRadioType.setStatus(_B)
class _An80iSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('saveConfig',2)))
_An80iSaveConfig_Type.__name__=_D
_An80iSaveConfig_Object=MibScalar
an80iSaveConfig=_An80iSaveConfig_Object((1,3,6,1,4,1,10728,2,1,3,1,1,4),_An80iSaveConfig_Type())
an80iSaveConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iSaveConfig.setStatus(_B)
class _An80iActivateConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('activeConfig',2)))
_An80iActivateConfig_Type.__name__=_D
_An80iActivateConfig_Object=MibScalar
an80iActivateConfig=_An80iActivateConfig_Object((1,3,6,1,4,1,10728,2,1,3,1,1,5),_An80iActivateConfig_Type())
an80iActivateConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iActivateConfig.setStatus(_B)
_RedlineAn80iWirelesObjects_ObjectIdentity=ObjectIdentity
redlineAn80iWirelesObjects=_RedlineAn80iWirelesObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,1,2))
class _An80iAntennaAllignmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('buzzer',2)))
_An80iAntennaAllignmentMode_Type.__name__=_D
_An80iAntennaAllignmentMode_Object=MibScalar
an80iAntennaAllignmentMode=_An80iAntennaAllignmentMode_Object((1,3,6,1,4,1,10728,2,1,3,1,2,1),_An80iAntennaAllignmentMode_Type())
an80iAntennaAllignmentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iAntennaAllignmentMode.setStatus(_B)
class _An80iCurrTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,20))
_An80iCurrTxPower_Type.__name__=_D
_An80iCurrTxPower_Object=MibScalar
an80iCurrTxPower=_An80iCurrTxPower_Object((1,3,6,1,4,1,10728,2,1,3,1,2,2),_An80iCurrTxPower_Type())
an80iCurrTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iCurrTxPower.setStatus(_B)
class _An80iChannelAutoScan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_An80iChannelAutoScan_Type.__name__=_D
_An80iChannelAutoScan_Object=MibScalar
an80iChannelAutoScan=_An80iChannelAutoScan_Object((1,3,6,1,4,1,10728,2,1,3,1,2,3),_An80iChannelAutoScan_Type())
an80iChannelAutoScan.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iChannelAutoScan.setStatus(_B)
_An80iCurrFrequency_Type=Integer32
_An80iCurrFrequency_Object=MibScalar
an80iCurrFrequency=_An80iCurrFrequency_Object((1,3,6,1,4,1,10728,2,1,3,1,2,4),_An80iCurrFrequency_Type())
an80iCurrFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iCurrFrequency.setStatus(_B)
if mibBuilder.loadTexts:an80iCurrFrequency.setUnits('KHz')
_An80iOPeratingFrequency_Type=Integer32
_An80iOPeratingFrequency_Object=MibScalar
an80iOPeratingFrequency=_An80iOPeratingFrequency_Object((1,3,6,1,4,1,10728,2,1,3,1,2,5),_An80iOPeratingFrequency_Type())
an80iOPeratingFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iOPeratingFrequency.setStatus(_B)
if mibBuilder.loadTexts:an80iOPeratingFrequency.setUnits('KHz')
class _An80iMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_An80iMaxTxPower_Type.__name__=_D
_An80iMaxTxPower_Object=MibScalar
an80iMaxTxPower=_An80iMaxTxPower_Object((1,3,6,1,4,1,10728,2,1,3,1,2,6),_An80iMaxTxPower_Type())
an80iMaxTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iMaxTxPower.setStatus(_B)
class _An80iSystemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ptpSlave',1),('ptpMaster',2),('pmpSlave',3),('pmpMaster',4)))
_An80iSystemMode_Type.__name__=_D
_An80iSystemMode_Object=MibScalar
an80iSystemMode=_An80iSystemMode_Object((1,3,6,1,4,1,10728,2,1,3,1,2,7),_An80iSystemMode_Type())
an80iSystemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iSystemMode.setStatus(_B)
_An80iRFStatusCode_Type=Integer32
_An80iRFStatusCode_Object=MibScalar
an80iRFStatusCode=_An80iRFStatusCode_Object((1,3,6,1,4,1,10728,2,1,3,1,2,8),_An80iRFStatusCode_Type())
an80iRFStatusCode.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iRFStatusCode.setStatus(_B)
class _An80iDFSAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('txDisabled',2),('changeFreq',3)))
_An80iDFSAction_Type.__name__=_D
_An80iDFSAction_Object=MibScalar
an80iDFSAction=_An80iDFSAction_Object((1,3,6,1,4,1,10728,2,1,3,1,2,9),_An80iDFSAction_Type())
an80iDFSAction.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iDFSAction.setStatus(_B)
_An80iAntennaGain_Type=Integer32
_An80iAntennaGain_Object=MibScalar
an80iAntennaGain=_An80iAntennaGain_Object((1,3,6,1,4,1,10728,2,1,3,1,2,10),_An80iAntennaGain_Type())
an80iAntennaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iAntennaGain.setStatus(_B)
_An80iActiveRFLinks_Type=Integer32
_An80iActiveRFLinks_Object=MibScalar
an80iActiveRFLinks=_An80iActiveRFLinks_Object((1,3,6,1,4,1,10728,2,1,3,1,2,11),_An80iActiveRFLinks_Type())
an80iActiveRFLinks.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iActiveRFLinks.setStatus(_B)
class _An80iAtpControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_An80iAtpControl_Type.__name__=_D
_An80iAtpControl_Object=MibScalar
an80iAtpControl=_An80iAtpControl_Object((1,3,6,1,4,1,10728,2,1,3,1,2,12),_An80iAtpControl_Type())
an80iAtpControl.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iAtpControl.setStatus(_B)
class _An80iTurboModeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_An80iTurboModeControl_Type.__name__=_D
_An80iTurboModeControl_Object=MibScalar
an80iTurboModeControl=_An80iTurboModeControl_Object((1,3,6,1,4,1,10728,2,1,3,1,2,13),_An80iTurboModeControl_Type())
an80iTurboModeControl.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iTurboModeControl.setStatus(_B)
class _An80iChannelWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7)));namedValues=NamedValues(*(('chWidth10MHz',5),('chWidth20MHz',6),('chWidth40MHz',7)))
_An80iChannelWidth_Type.__name__=_D
_An80iChannelWidth_Object=MibScalar
an80iChannelWidth=_An80iChannelWidth_Object((1,3,6,1,4,1,10728,2,1,3,1,2,14),_An80iChannelWidth_Type())
an80iChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iChannelWidth.setStatus(_B)
_RedlineAn80iEthernetObjects_ObjectIdentity=ObjectIdentity
redlineAn80iEthernetObjects=_RedlineAn80iEthernetObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,1,3))
class _An80iEtherPortConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('normal',2),('crossover',3)))
_An80iEtherPortConn_Type.__name__=_D
_An80iEtherPortConn_Object=MibScalar
an80iEtherPortConn=_An80iEtherPortConn_Object((1,3,6,1,4,1,10728,2,1,3,1,3,1),_An80iEtherPortConn_Type())
an80iEtherPortConn.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iEtherPortConn.setStatus(_B)
class _An80iEtherPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('auto',1),('e10hd',2),('e10fd',3),('e100hd',4),('e100fd',5)))
_An80iEtherPortMode_Type.__name__=_D
_An80iEtherPortMode_Object=MibScalar
an80iEtherPortMode=_An80iEtherPortMode_Object((1,3,6,1,4,1,10728,2,1,3,1,3,2),_An80iEtherPortMode_Type())
an80iEtherPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iEtherPortMode.setStatus(_B)
class _An80iFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An80iFlowControl_Type.__name__=_D
_An80iFlowControl_Object=MibScalar
an80iFlowControl=_An80iFlowControl_Object((1,3,6,1,4,1,10728,2,1,3,1,3,3),_An80iFlowControl_Type())
an80iFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iFlowControl.setStatus(_B)
class _An80iLowLatencyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An80iLowLatencyMode_Type.__name__=_D
_An80iLowLatencyMode_Object=MibScalar
an80iLowLatencyMode=_An80iLowLatencyMode_Object((1,3,6,1,4,1,10728,2,1,3,1,3,4),_An80iLowLatencyMode_Type())
an80iLowLatencyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iLowLatencyMode.setStatus(_B)
class _An80iEthernetFollowsWireless_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An80iEthernetFollowsWireless_Type.__name__=_D
_An80iEthernetFollowsWireless_Object=MibScalar
an80iEthernetFollowsWireless=_An80iEthernetFollowsWireless_Object((1,3,6,1,4,1,10728,2,1,3,1,3,5),_An80iEthernetFollowsWireless_Type())
an80iEthernetFollowsWireless.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iEthernetFollowsWireless.setStatus(_B)
class _An80iEthernetFollowsWirelessTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An80iEthernetFollowsWirelessTimeout_Type.__name__=_D
_An80iEthernetFollowsWirelessTimeout_Object=MibScalar
an80iEthernetFollowsWirelessTimeout=_An80iEthernetFollowsWirelessTimeout_Object((1,3,6,1,4,1,10728,2,1,3,1,3,6),_An80iEthernetFollowsWirelessTimeout_Type())
an80iEthernetFollowsWirelessTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iEthernetFollowsWirelessTimeout.setStatus(_B)
_RedlineAn80iManagObjects_ObjectIdentity=ObjectIdentity
redlineAn80iManagObjects=_RedlineAn80iManagObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,1,4))
class _An80iHttpAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An80iHttpAccess_Type.__name__=_D
_An80iHttpAccess_Object=MibScalar
an80iHttpAccess=_An80iHttpAccess_Object((1,3,6,1,4,1,10728,2,1,3,1,4,1),_An80iHttpAccess_Type())
an80iHttpAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iHttpAccess.setStatus(_B)
class _An80iTelnetAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An80iTelnetAccess_Type.__name__=_D
_An80iTelnetAccess_Object=MibScalar
an80iTelnetAccess=_An80iTelnetAccess_Object((1,3,6,1,4,1,10728,2,1,3,1,4,2),_An80iTelnetAccess_Type())
an80iTelnetAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iTelnetAccess.setStatus(_B)
_An80iTelnetPort_Type=InetPortNumber
_An80iTelnetPort_Object=MibScalar
an80iTelnetPort=_An80iTelnetPort_Object((1,3,6,1,4,1,10728,2,1,3,1,4,3),_An80iTelnetPort_Type())
an80iTelnetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iTelnetPort.setStatus(_B)
_RedlineAn80iSWUpgradeObjects_ObjectIdentity=ObjectIdentity
redlineAn80iSWUpgradeObjects=_RedlineAn80iSWUpgradeObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,1,5))
_An80iSwDownloadTftpAddressType_Type=InetAddressType
_An80iSwDownloadTftpAddressType_Object=MibScalar
an80iSwDownloadTftpAddressType=_An80iSwDownloadTftpAddressType_Object((1,3,6,1,4,1,10728,2,1,3,1,5,1),_An80iSwDownloadTftpAddressType_Type())
an80iSwDownloadTftpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iSwDownloadTftpAddressType.setStatus(_B)
_An80iSwDownloadTftpAddress_Type=InetAddress
_An80iSwDownloadTftpAddress_Object=MibScalar
an80iSwDownloadTftpAddress=_An80iSwDownloadTftpAddress_Object((1,3,6,1,4,1,10728,2,1,3,1,5,2),_An80iSwDownloadTftpAddress_Type())
an80iSwDownloadTftpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iSwDownloadTftpAddress.setStatus(_B)
class _An80iSwDownloadTftpFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_An80iSwDownloadTftpFile_Type.__name__=_O
_An80iSwDownloadTftpFile_Object=MibScalar
an80iSwDownloadTftpFile=_An80iSwDownloadTftpFile_Object((1,3,6,1,4,1,10728,2,1,3,1,5,3),_An80iSwDownloadTftpFile_Type())
an80iSwDownloadTftpFile.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iSwDownloadTftpFile.setStatus(_B)
class _An80iSwDownloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('download',1),('inProgress',2),('success',3),('failed',4)))
_An80iSwDownloadStatus_Type.__name__=_D
_An80iSwDownloadStatus_Object=MibScalar
an80iSwDownloadStatus=_An80iSwDownloadStatus_Object((1,3,6,1,4,1,10728,2,1,3,1,5,4),_An80iSwDownloadStatus_Type())
an80iSwDownloadStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iSwDownloadStatus.setStatus(_B)
class _An80iSwDownloadControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('startUpgrade',2)))
_An80iSwDownloadControl_Type.__name__=_D
_An80iSwDownloadControl_Object=MibScalar
an80iSwDownloadControl=_An80iSwDownloadControl_Object((1,3,6,1,4,1,10728,2,1,3,1,5,5),_An80iSwDownloadControl_Type())
an80iSwDownloadControl.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iSwDownloadControl.setStatus(_B)
_RedlineAn80iPmpObjects_ObjectIdentity=ObjectIdentity
redlineAn80iPmpObjects=_RedlineAn80iPmpObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,2))
_RedlineAn80iPmpWirelesObjects_ObjectIdentity=ObjectIdentity
redlineAn80iPmpWirelesObjects=_RedlineAn80iPmpWirelesObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,2,1))
class _An80iRegistrationPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_An80iRegistrationPeriod_Type.__name__=_D
_An80iRegistrationPeriod_Object=MibScalar
an80iRegistrationPeriod=_An80iRegistrationPeriod_Object((1,3,6,1,4,1,10728,2,1,3,2,1,1),_An80iRegistrationPeriod_Type())
an80iRegistrationPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iRegistrationPeriod.setStatus(_B)
class _An80iMaximumDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_An80iMaximumDistance_Type.__name__=_D
_An80iMaximumDistance_Object=MibScalar
an80iMaximumDistance=_An80iMaximumDistance_Object((1,3,6,1,4,1,10728,2,1,3,2,1,2),_An80iMaximumDistance_Type())
an80iMaximumDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iMaximumDistance.setStatus(_B)
_An80iRegisteredStations_Type=Integer32
_An80iRegisteredStations_Object=MibScalar
an80iRegisteredStations=_An80iRegisteredStations_Object((1,3,6,1,4,1,10728,2,1,3,2,1,3),_An80iRegisteredStations_Type())
an80iRegisteredStations.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iRegisteredStations.setStatus(_B)
_An80iRegisteredConnections_Type=Integer32
_An80iRegisteredConnections_Object=MibScalar
an80iRegisteredConnections=_An80iRegisteredConnections_Object((1,3,6,1,4,1,10728,2,1,3,2,1,4),_An80iRegisteredConnections_Type())
an80iRegisteredConnections.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iRegisteredConnections.setStatus(_B)
class _An80iMaxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_An80iMaxId_Type.__name__=_D
_An80iMaxId_Object=MibScalar
an80iMaxId=_An80iMaxId_Object((1,3,6,1,4,1,10728,2,1,3,2,1,5),_An80iMaxId_Type())
an80iMaxId.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iMaxId.setStatus(_B)
_An80iNextAvailId_Type=Integer32
_An80iNextAvailId_Object=MibScalar
an80iNextAvailId=_An80iNextAvailId_Object((1,3,6,1,4,1,10728,2,1,3,2,1,6),_An80iNextAvailId_Type())
an80iNextAvailId.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iNextAvailId.setStatus(_B)
_An80iLastModifId_Type=Integer32
_An80iLastModifId_Object=MibScalar
an80iLastModifId=_An80iLastModifId_Object((1,3,6,1,4,1,10728,2,1,3,2,1,7),_An80iLastModifId_Type())
an80iLastModifId.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iLastModifId.setStatus(_B)
class _An80iSaveIdConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('save',2)))
_An80iSaveIdConfiguration_Type.__name__=_D
_An80iSaveIdConfiguration_Object=MibScalar
an80iSaveIdConfiguration=_An80iSaveIdConfiguration_Object((1,3,6,1,4,1,10728,2,1,3,2,1,8),_An80iSaveIdConfiguration_Type())
an80iSaveIdConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iSaveIdConfiguration.setStatus(_B)
_RedlineAn80iPtpObjects_ObjectIdentity=ObjectIdentity
redlineAn80iPtpObjects=_RedlineAn80iPtpObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,3))
_RedlineAn80iPtpSystemObjects_ObjectIdentity=ObjectIdentity
redlineAn80iPtpSystemObjects=_RedlineAn80iPtpSystemObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,3,1))
class _An80iResetStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reset',2)))
_An80iResetStatistics_Type.__name__=_D
_An80iResetStatistics_Object=MibScalar
an80iResetStatistics=_An80iResetStatistics_Object((1,3,6,1,4,1,10728,2,1,3,3,1,1),_An80iResetStatistics_Type())
an80iResetStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iResetStatistics.setStatus(_B)
_RedlineAn80iConformance_ObjectIdentity=ObjectIdentity
redlineAn80iConformance=_RedlineAn80iConformance_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,5))
_RedlineAn80iGroups_ObjectIdentity=ObjectIdentity
redlineAn80iGroups=_RedlineAn80iGroups_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,5,1))
_RedlineAn80iCompls_ObjectIdentity=ObjectIdentity
redlineAn80iCompls=_RedlineAn80iCompls_ObjectIdentity((1,3,6,1,4,1,10728,2,1,3,5,2))
redlineAn80iPtpPmpGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,3,5,1,1))
redlineAn80iPtpPmpGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_I),(_A,_J),(_A,_K),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:redlineAn80iPtpPmpGroup.setStatus(_B)
redlineAn80iPmpGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,3,5,1,2))
redlineAn80iPmpGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_N),(_A,_A0)))
if mibBuilder.loadTexts:redlineAn80iPmpGroup.setStatus(_B)
redlineAn80iPtpGroup=ObjectGroup((1,3,6,1,4,1,10728,2,1,3,5,1,3))
redlineAn80iPtpGroup.setObjects((_A,_A1))
if mibBuilder.loadTexts:redlineAn80iPtpGroup.setStatus(_B)
an80iPswdChangeFailTrap=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,1))
if mibBuilder.loadTexts:an80iPswdChangeFailTrap.setStatus(_B)
an80iFirmwareConfigFailTrap=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,2))
if mibBuilder.loadTexts:an80iFirmwareConfigFailTrap.setStatus(_B)
an80iEepromCorruptedTrap=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,3))
if mibBuilder.loadTexts:an80iEepromCorruptedTrap.setStatus(_B)
an80iHardwareFailTrap=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,4))
if mibBuilder.loadTexts:an80iHardwareFailTrap.setStatus(_B)
an80iSaveConfigTrap=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,5))
if mibBuilder.loadTexts:an80iSaveConfigTrap.setStatus(_B)
an80iDFSEventTrap=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,6))
if mibBuilder.loadTexts:an80iDFSEventTrap.setStatus(_B)
an80iIdChangedTrap=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,7))
an80iIdChangedTrap.setObjects((_A,_N))
if mibBuilder.loadTexts:an80iIdChangedTrap.setStatus(_B)
an80iSWUpgradeFailed=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,8))
an80iSWUpgradeFailed.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:an80iSWUpgradeFailed.setStatus(_B)
an80iSWUpgradeSuccess=NotificationType((1,3,6,1,4,1,10728,2,1,3,0,9))
an80iSWUpgradeSuccess.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:an80iSWUpgradeSuccess.setStatus(_B)
redlineAn80iNotificationGroup=NotificationGroup((1,3,6,1,4,1,10728,2,1,3,5,1,4))
redlineAn80iNotificationGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:redlineAn80iNotificationGroup.setStatus(_B)
redlineAn80iCompliance=ModuleCompliance((1,3,6,1,4,1,10728,2,1,3,5,2,1))
redlineAn80iCompliance.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:redlineAn80iCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'redlineAn80iMib':redlineAn80iMib,'redlineAn80iTrapDefinitions':redlineAn80iTrapDefinitions,_A2:an80iPswdChangeFailTrap,_A3:an80iFirmwareConfigFailTrap,_A4:an80iEepromCorruptedTrap,_A5:an80iHardwareFailTrap,_A6:an80iSaveConfigTrap,_A7:an80iDFSEventTrap,_A8:an80iIdChangedTrap,_A9:an80iSWUpgradeFailed,_AA:an80iSWUpgradeSuccess,'redlineAn80iPtpPmpObjects':redlineAn80iPtpPmpObjects,'redlineAn80iSystemObjects':redlineAn80iSystemObjects,'an80iOptionsKeyTable':an80iOptionsKeyTable,'an80iOptionsKeyEntry':an80iOptionsKeyEntry,_P:an80iOptionsKeyId,_R:an80iOptionsKey,'an80iOptionsKeyStatus':an80iOptionsKeyStatus,_S:an80iHardwareType,_T:an80iRadioType,_U:an80iSaveConfig,_V:an80iActivateConfig,'redlineAn80iWirelesObjects':redlineAn80iWirelesObjects,_W:an80iAntennaAllignmentMode,_X:an80iCurrTxPower,_Y:an80iChannelAutoScan,_Z:an80iCurrFrequency,_a:an80iOPeratingFrequency,_b:an80iMaxTxPower,_c:an80iSystemMode,_d:an80iRFStatusCode,_e:an80iDFSAction,_f:an80iAntennaGain,_g:an80iActiveRFLinks,_h:an80iAtpControl,_i:an80iTurboModeControl,'an80iChannelWidth':an80iChannelWidth,'redlineAn80iEthernetObjects':redlineAn80iEthernetObjects,_j:an80iEtherPortConn,_k:an80iEtherPortMode,_l:an80iFlowControl,_m:an80iLowLatencyMode,_n:an80iEthernetFollowsWireless,_o:an80iEthernetFollowsWirelessTimeout,'redlineAn80iManagObjects':redlineAn80iManagObjects,_p:an80iHttpAccess,_q:an80iTelnetAccess,_r:an80iTelnetPort,'redlineAn80iSWUpgradeObjects':redlineAn80iSWUpgradeObjects,_I:an80iSwDownloadTftpAddressType,_J:an80iSwDownloadTftpAddress,_K:an80iSwDownloadTftpFile,_s:an80iSwDownloadStatus,_t:an80iSwDownloadControl,'redlineAn80iPmpObjects':redlineAn80iPmpObjects,'redlineAn80iPmpWirelesObjects':redlineAn80iPmpWirelesObjects,_u:an80iRegistrationPeriod,_v:an80iMaximumDistance,_w:an80iRegisteredStations,_x:an80iRegisteredConnections,_y:an80iMaxId,_z:an80iNextAvailId,_N:an80iLastModifId,_A0:an80iSaveIdConfiguration,'redlineAn80iPtpObjects':redlineAn80iPtpObjects,'redlineAn80iPtpSystemObjects':redlineAn80iPtpSystemObjects,_A1:an80iResetStatistics,'redlineAn80iConformance':redlineAn80iConformance,'redlineAn80iGroups':redlineAn80iGroups,_AB:redlineAn80iPtpPmpGroup,_AC:redlineAn80iPmpGroup,_AD:redlineAn80iPtpGroup,_AE:redlineAn80iNotificationGroup,'redlineAn80iCompls':redlineAn80iCompls,'redlineAn80iCompliance':redlineAn80iCompliance})