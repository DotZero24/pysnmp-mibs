_V='NotificationType'
_U='an50pmpLastRegisteredSsMacAddress'
_T='an50pmpLastModifiedCID'
_S='an50pmpLastMissedSsMacAddress'
_R='OctetString'
_Q='an50SwOperStatus'
_P='an50SwAdminStatus'
_O='an50SwFilename'
_N='an50SwServer'
_M='on'
_L='off'
_K='donothing'
_J='REDLINE-AN50-PMP-V1-MIB'
_I='unknown'
_H='yes'
_G='no'
_F='an50SysLastTrapTime'
_E='REDLINE-AN50-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
an50pmpLastMissedSsMacAddress,an50pmpLastModifiedCID,an50pmpLastRegisteredSsMacAddress=mibBuilder.importSymbols(_J,_S,_T,_U)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_V,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_V,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Redline_ObjectIdentity=ObjectIdentity
redline=_Redline_ObjectIdentity((1,3,6,1,4,1,10728))
_RedlineProducts_ObjectIdentity=ObjectIdentity
redlineProducts=_RedlineProducts_ObjectIdentity((1,3,6,1,4,1,10728,1))
_RedlineMgmt_ObjectIdentity=ObjectIdentity
redlineMgmt=_RedlineMgmt_ObjectIdentity((1,3,6,1,4,1,10728,2))
_RedlineAn50_ObjectIdentity=ObjectIdentity
redlineAn50=_RedlineAn50_ObjectIdentity((1,3,6,1,4,1,10728,2,16))
_An50General_ObjectIdentity=ObjectIdentity
an50General=_An50General_ObjectIdentity((1,3,6,1,4,1,10728,2,16,1))
_An50GenUBR_Type=Integer32
_An50GenUBR_Object=MibScalar
an50GenUBR=_An50GenUBR_Object((1,3,6,1,4,1,10728,2,16,1,1),_An50GenUBR_Type())
an50GenUBR.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenUBR.setStatus(_A)
class _An50GenRFLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notConnected',1),('connected',2)))
_An50GenRFLink_Type.__name__=_C
_An50GenRFLink_Object=MibScalar
an50GenRFLink=_An50GenRFLink_Object((1,3,6,1,4,1,10728,2,16,1,2),_An50GenRFLink_Type())
an50GenRFLink.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenRFLink.setStatus(_A)
_An50GenFrequency_Type=Integer32
_An50GenFrequency_Object=MibScalar
an50GenFrequency=_An50GenFrequency_Object((1,3,6,1,4,1,10728,2,16,1,3),_An50GenFrequency_Type())
an50GenFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenFrequency.setStatus(_A)
class _An50GenAllignmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('voltage',1),('buzzer',2)))
_An50GenAllignmentMode_Type.__name__=_C
_An50GenAllignmentMode_Object=MibScalar
an50GenAllignmentMode=_An50GenAllignmentMode_Object((1,3,6,1,4,1,10728,2,16,1,4),_An50GenAllignmentMode_Type())
an50GenAllignmentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenAllignmentMode.setStatus(_A)
class _An50GenEncryptionEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50GenEncryptionEnabled_Type.__name__=_C
_An50GenEncryptionEnabled_Object=MibScalar
an50GenEncryptionEnabled=_An50GenEncryptionEnabled_Object((1,3,6,1,4,1,10728,2,16,1,5),_An50GenEncryptionEnabled_Type())
an50GenEncryptionEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenEncryptionEnabled.setStatus(_A)
class _An50GenFlowControlEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50GenFlowControlEnabled_Type.__name__=_C
_An50GenFlowControlEnabled_Object=MibScalar
an50GenFlowControlEnabled=_An50GenFlowControlEnabled_Object((1,3,6,1,4,1,10728,2,16,1,6),_An50GenFlowControlEnabled_Type())
an50GenFlowControlEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenFlowControlEnabled.setStatus(_A)
class _An50GenHttpAccessEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50GenHttpAccessEnabled_Type.__name__=_C
_An50GenHttpAccessEnabled_Object=MibScalar
an50GenHttpAccessEnabled=_An50GenHttpAccessEnabled_Object((1,3,6,1,4,1,10728,2,16,1,7),_An50GenHttpAccessEnabled_Type())
an50GenHttpAccessEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenHttpAccessEnabled.setStatus(_A)
class _An50GenTelnetAccessEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50GenTelnetAccessEnabled_Type.__name__=_C
_An50GenTelnetAccessEnabled_Object=MibScalar
an50GenTelnetAccessEnabled=_An50GenTelnetAccessEnabled_Object((1,3,6,1,4,1,10728,2,16,1,8),_An50GenTelnetAccessEnabled_Type())
an50GenTelnetAccessEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenTelnetAccessEnabled.setStatus(_A)
_An50GenTelnetPort_Type=Integer32
_An50GenTelnetPort_Object=MibScalar
an50GenTelnetPort=_An50GenTelnetPort_Object((1,3,6,1,4,1,10728,2,16,1,9),_An50GenTelnetPort_Type())
an50GenTelnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenTelnetPort.setStatus(_A)
_An50GenOptionsKey_Type=OctetString
_An50GenOptionsKey_Object=MibScalar
an50GenOptionsKey=_An50GenOptionsKey_Object((1,3,6,1,4,1,10728,2,16,1,10),_An50GenOptionsKey_Type())
an50GenOptionsKey.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenOptionsKey.setStatus(_A)
class _An50GenResetDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('reset',2)))
_An50GenResetDevice_Type.__name__=_C
_An50GenResetDevice_Object=MibScalar
an50GenResetDevice=_An50GenResetDevice_Object((1,3,6,1,4,1,10728,2,16,1,11),_An50GenResetDevice_Type())
an50GenResetDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenResetDevice.setStatus(_A)
class _An50GenFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_I,3)))
_An50GenFault_Type.__name__=_C
_An50GenFault_Object=MibScalar
an50GenFault=_An50GenFault_Object((1,3,6,1,4,1,10728,2,16,1,12),_An50GenFault_Type())
an50GenFault.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenFault.setStatus(_A)
class _An50GenTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_An50GenTxPower_Type.__name__=_C
_An50GenTxPower_Object=MibScalar
an50GenTxPower=_An50GenTxPower_Object((1,3,6,1,4,1,10728,2,16,1,13),_An50GenTxPower_Type())
an50GenTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenTxPower.setStatus(_A)
_An50GenRegisteredStations_Type=Integer32
_An50GenRegisteredStations_Object=MibScalar
an50GenRegisteredStations=_An50GenRegisteredStations_Object((1,3,6,1,4,1,10728,2,16,1,14),_An50GenRegisteredStations_Type())
an50GenRegisteredStations.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenRegisteredStations.setStatus(_A)
_An50GenRegisteredConnections_Type=Integer32
_An50GenRegisteredConnections_Object=MibScalar
an50GenRegisteredConnections=_An50GenRegisteredConnections_Object((1,3,6,1,4,1,10728,2,16,1,15),_An50GenRegisteredConnections_Type())
an50GenRegisteredConnections.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenRegisteredConnections.setStatus(_A)
_An50GenActiveWirelessLinks_Type=Integer32
_An50GenActiveWirelessLinks_Object=MibScalar
an50GenActiveWirelessLinks=_An50GenActiveWirelessLinks_Object((1,3,6,1,4,1,10728,2,16,1,16),_An50GenActiveWirelessLinks_Type())
an50GenActiveWirelessLinks.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenActiveWirelessLinks.setStatus(_A)
class _An50GenChannelAutoScan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50GenChannelAutoScan_Type.__name__=_C
_An50GenChannelAutoScan_Object=MibScalar
an50GenChannelAutoScan=_An50GenChannelAutoScan_Object((1,3,6,1,4,1,10728,2,16,1,17),_An50GenChannelAutoScan_Type())
an50GenChannelAutoScan.setMaxAccess(_B)
if mibBuilder.loadTexts:an50GenChannelAutoScan.setStatus(_A)
_An50GenIduType_Type=Integer32
_An50GenIduType_Object=MibScalar
an50GenIduType=_An50GenIduType_Object((1,3,6,1,4,1,10728,2,16,1,18),_An50GenIduType_Type())
an50GenIduType.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenIduType.setStatus(_A)
_An50GenOduType_Type=Integer32
_An50GenOduType_Object=MibScalar
an50GenOduType=_An50GenOduType_Object((1,3,6,1,4,1,10728,2,16,1,19),_An50GenOduType_Type())
an50GenOduType.setMaxAccess(_D)
if mibBuilder.loadTexts:an50GenOduType.setStatus(_A)
_An50Config_ObjectIdentity=ObjectIdentity
an50Config=_An50Config_ObjectIdentity((1,3,6,1,4,1,10728,2,16,2))
_An50ConfigEther_ObjectIdentity=ObjectIdentity
an50ConfigEther=_An50ConfigEther_ObjectIdentity((1,3,6,1,4,1,10728,2,16,2,1))
_An50EtherMacAddress_Type=OctetString
_An50EtherMacAddress_Object=MibScalar
an50EtherMacAddress=_An50EtherMacAddress_Object((1,3,6,1,4,1,10728,2,16,2,1,1),_An50EtherMacAddress_Type())
an50EtherMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:an50EtherMacAddress.setStatus(_A)
_An50EtherGateway_Type=IpAddress
_An50EtherGateway_Object=MibScalar
an50EtherGateway=_An50EtherGateway_Object((1,3,6,1,4,1,10728,2,16,2,1,2),_An50EtherGateway_Type())
an50EtherGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:an50EtherGateway.setStatus(_A)
class _An50EtherPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),(_I,3)))
_An50EtherPortStatus_Type.__name__=_C
_An50EtherPortStatus_Object=MibScalar
an50EtherPortStatus=_An50EtherPortStatus_Object((1,3,6,1,4,1,10728,2,16,2,1,3),_An50EtherPortStatus_Type())
an50EtherPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:an50EtherPortStatus.setStatus(_A)
_An50EtherIP_Type=IpAddress
_An50EtherIP_Object=MibScalar
an50EtherIP=_An50EtherIP_Object((1,3,6,1,4,1,10728,2,16,2,1,4),_An50EtherIP_Type())
an50EtherIP.setMaxAccess(_B)
if mibBuilder.loadTexts:an50EtherIP.setStatus(_A)
_An50EtherMask_Type=IpAddress
_An50EtherMask_Object=MibScalar
an50EtherMask=_An50EtherMask_Object((1,3,6,1,4,1,10728,2,16,2,1,5),_An50EtherMask_Type())
an50EtherMask.setMaxAccess(_B)
if mibBuilder.loadTexts:an50EtherMask.setStatus(_A)
class _An50Ether100_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('s10Mbs',1),('s100Mbs',2),(_I,3)))
_An50Ether100_Type.__name__=_C
_An50Ether100_Object=MibScalar
an50Ether100=_An50Ether100_Object((1,3,6,1,4,1,10728,2,16,2,1,6),_An50Ether100_Type())
an50Ether100.setMaxAccess(_D)
if mibBuilder.loadTexts:an50Ether100.setStatus(_A)
class _An50EtherFd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplex',2),(_I,3)))
_An50EtherFd_Type.__name__=_C
_An50EtherFd_Object=MibScalar
an50EtherFd=_An50EtherFd_Object((1,3,6,1,4,1,10728,2,16,2,1,7),_An50EtherFd_Type())
an50EtherFd.setMaxAccess(_D)
if mibBuilder.loadTexts:an50EtherFd.setStatus(_A)
class _An50EtherMgmVidEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50EtherMgmVidEn_Type.__name__=_C
_An50EtherMgmVidEn_Object=MibScalar
an50EtherMgmVidEn=_An50EtherMgmVidEn_Object((1,3,6,1,4,1,10728,2,16,2,1,8),_An50EtherMgmVidEn_Type())
an50EtherMgmVidEn.setMaxAccess(_B)
if mibBuilder.loadTexts:an50EtherMgmVidEn.setStatus(_A)
class _An50EtherMgmVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_An50EtherMgmVid_Type.__name__=_C
_An50EtherMgmVid_Object=MibScalar
an50EtherMgmVid=_An50EtherMgmVid_Object((1,3,6,1,4,1,10728,2,16,2,1,9),_An50EtherMgmVid_Type())
an50EtherMgmVid.setMaxAccess(_B)
if mibBuilder.loadTexts:an50EtherMgmVid.setStatus(_A)
class _An50EtherLben_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50EtherLben_Type.__name__=_C
_An50EtherLben_Object=MibScalar
an50EtherLben=_An50EtherLben_Object((1,3,6,1,4,1,10728,2,16,2,1,10),_An50EtherLben_Type())
an50EtherLben.setMaxAccess(_B)
if mibBuilder.loadTexts:an50EtherLben.setStatus(_A)
_An50ConfigWireless_ObjectIdentity=ObjectIdentity
an50ConfigWireless=_An50ConfigWireless_ObjectIdentity((1,3,6,1,4,1,10728,2,16,2,2))
class _An50WrlsChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('chan1',1),('chan1A',2),('chan2',3),('chan2A',4),('chan3',5),('chan3A',6),('chan4',7),('chan4A',8),('chan5',9)))
_An50WrlsChannel_Type.__name__=_C
_An50WrlsChannel_Object=MibScalar
an50WrlsChannel=_An50WrlsChannel_Object((1,3,6,1,4,1,10728,2,16,2,2,1),_An50WrlsChannel_Type())
an50WrlsChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsChannel.setStatus(_A)
class _An50WrlsTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_An50WrlsTxPower_Type.__name__=_C
_An50WrlsTxPower_Object=MibScalar
an50WrlsTxPower=_An50WrlsTxPower_Object((1,3,6,1,4,1,10728,2,16,2,2,2),_An50WrlsTxPower_Type())
an50WrlsTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsTxPower.setStatus(_A)
class _An50WrlsModReduction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_An50WrlsModReduction_Type.__name__=_C
_An50WrlsModReduction_Object=MibScalar
an50WrlsModReduction=_An50WrlsModReduction_Object((1,3,6,1,4,1,10728,2,16,2,2,3),_An50WrlsModReduction_Type())
an50WrlsModReduction.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsModReduction.setStatus(_A)
class _An50WrlsAdaptiveMod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notAdaptiveRate',1),('adaptiveRate',2)))
_An50WrlsAdaptiveMod_Type.__name__=_C
_An50WrlsAdaptiveMod_Object=MibScalar
an50WrlsAdaptiveMod=_An50WrlsAdaptiveMod_Object((1,3,6,1,4,1,10728,2,16,2,2,4),_An50WrlsAdaptiveMod_Type())
an50WrlsAdaptiveMod.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsAdaptiveMod.setStatus(_A)
class _An50WrlsUBR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_An50WrlsUBR_Type.__name__=_C
_An50WrlsUBR_Object=MibScalar
an50WrlsUBR=_An50WrlsUBR_Object((1,3,6,1,4,1,10728,2,16,2,2,5),_An50WrlsUBR_Type())
an50WrlsUBR.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsUBR.setStatus(_A)
class _An50WrlsMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ptpSlave',1),('ptpMaster',2),('pmpSlave',3),('pmpMaster',4)))
_An50WrlsMaster_Type.__name__=_C
_An50WrlsMaster_Object=MibScalar
an50WrlsMaster=_An50WrlsMaster_Object((1,3,6,1,4,1,10728,2,16,2,2,6),_An50WrlsMaster_Type())
an50WrlsMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsMaster.setStatus(_A)
class _An50WrlsVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('firstFlash',1),('secondFlash',2)))
_An50WrlsVersion_Type.__name__=_C
_An50WrlsVersion_Object=MibScalar
an50WrlsVersion=_An50WrlsVersion_Object((1,3,6,1,4,1,10728,2,16,2,2,7),_An50WrlsVersion_Type())
an50WrlsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsVersion.setStatus(_A)
_An50WrlsEncryptCode_Type=OctetString
_An50WrlsEncryptCode_Object=MibScalar
an50WrlsEncryptCode=_An50WrlsEncryptCode_Object((1,3,6,1,4,1,10728,2,16,2,2,8),_An50WrlsEncryptCode_Type())
an50WrlsEncryptCode.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsEncryptCode.setStatus(_A)
_An50WrlsCableAttenuation_Type=Integer32
_An50WrlsCableAttenuation_Object=MibScalar
an50WrlsCableAttenuation=_An50WrlsCableAttenuation_Object((1,3,6,1,4,1,10728,2,16,2,2,9),_An50WrlsCableAttenuation_Type())
an50WrlsCableAttenuation.setMaxAccess(_D)
if mibBuilder.loadTexts:an50WrlsCableAttenuation.setStatus(_A)
class _An50WrlsRfPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),(_I,3)))
_An50WrlsRfPortStatus_Type.__name__=_C
_An50WrlsRfPortStatus_Object=MibScalar
an50WrlsRfPortStatus=_An50WrlsRfPortStatus_Object((1,3,6,1,4,1,10728,2,16,2,2,10),_An50WrlsRfPortStatus_Type())
an50WrlsRfPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:an50WrlsRfPortStatus.setStatus(_A)
class _An50WrlsSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('saveConfig',2)))
_An50WrlsSaveConfig_Type.__name__=_C
_An50WrlsSaveConfig_Object=MibScalar
an50WrlsSaveConfig=_An50WrlsSaveConfig_Object((1,3,6,1,4,1,10728,2,16,2,2,11),_An50WrlsSaveConfig_Type())
an50WrlsSaveConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsSaveConfig.setStatus(_A)
class _An50WrlsActivateConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('activeConfig',2)))
_An50WrlsActivateConfig_Type.__name__=_C
_An50WrlsActivateConfig_Object=MibScalar
an50WrlsActivateConfig=_An50WrlsActivateConfig_Object((1,3,6,1,4,1,10728,2,16,2,2,12),_An50WrlsActivateConfig_Type())
an50WrlsActivateConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsActivateConfig.setStatus(_A)
class _An50WrlsRadioEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('txOff',1),('txOn',2)))
_An50WrlsRadioEnable_Type.__name__=_C
_An50WrlsRadioEnable_Object=MibScalar
an50WrlsRadioEnable=_An50WrlsRadioEnable_Object((1,3,6,1,4,1,10728,2,16,2,2,13),_An50WrlsRadioEnable_Type())
an50WrlsRadioEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsRadioEnable.setStatus(_A)
_An50WrlsRfStatusErrorCode_Type=Integer32
_An50WrlsRfStatusErrorCode_Object=MibScalar
an50WrlsRfStatusErrorCode=_An50WrlsRfStatusErrorCode_Object((1,3,6,1,4,1,10728,2,16,2,2,14),_An50WrlsRfStatusErrorCode_Type())
an50WrlsRfStatusErrorCode.setMaxAccess(_D)
if mibBuilder.loadTexts:an50WrlsRfStatusErrorCode.setStatus(_A)
class _An50WrlsRfSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('blinking',3)))
_An50WrlsRfSignal_Type.__name__=_C
_An50WrlsRfSignal_Object=MibScalar
an50WrlsRfSignal=_An50WrlsRfSignal_Object((1,3,6,1,4,1,10728,2,16,2,2,15),_An50WrlsRfSignal_Type())
an50WrlsRfSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:an50WrlsRfSignal.setStatus(_A)
class _An50WrlsLLMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_An50WrlsLLMode_Type.__name__=_C
_An50WrlsLLMode_Object=MibScalar
an50WrlsLLMode=_An50WrlsLLMode_Object((1,3,6,1,4,1,10728,2,16,2,2,16),_An50WrlsLLMode_Type())
an50WrlsLLMode.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsLLMode.setStatus(_A)
class _An50WrlsLMU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mile',1),('km',2)))
_An50WrlsLMU_Type.__name__=_C
_An50WrlsLMU_Object=MibScalar
an50WrlsLMU=_An50WrlsLMU_Object((1,3,6,1,4,1,10728,2,16,2,2,17),_An50WrlsLMU_Type())
an50WrlsLMU.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsLMU.setStatus(_A)
_An50WrlsLL_Type=Integer32
_An50WrlsLL_Object=MibScalar
an50WrlsLL=_An50WrlsLL_Object((1,3,6,1,4,1,10728,2,16,2,2,18),_An50WrlsLL_Type())
an50WrlsLL.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsLL.setStatus(_A)
_An50ConfigScheduler_ObjectIdentity=ObjectIdentity
an50ConfigScheduler=_An50ConfigScheduler_ObjectIdentity((1,3,6,1,4,1,10728,2,16,2,2,19))
_An50WrlsFrameSize_Type=Integer32
_An50WrlsFrameSize_Object=MibScalar
an50WrlsFrameSize=_An50WrlsFrameSize_Object((1,3,6,1,4,1,10728,2,16,2,2,19,1),_An50WrlsFrameSize_Type())
an50WrlsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsFrameSize.setStatus(_A)
_An50WrlsMinBlockSize_Type=Integer32
_An50WrlsMinBlockSize_Object=MibScalar
an50WrlsMinBlockSize=_An50WrlsMinBlockSize_Object((1,3,6,1,4,1,10728,2,16,2,2,19,2),_An50WrlsMinBlockSize_Type())
an50WrlsMinBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsMinBlockSize.setStatus(_A)
_An50WrlsDownlinkSize_Type=Integer32
_An50WrlsDownlinkSize_Object=MibScalar
an50WrlsDownlinkSize=_An50WrlsDownlinkSize_Object((1,3,6,1,4,1,10728,2,16,2,2,19,3),_An50WrlsDownlinkSize_Type())
an50WrlsDownlinkSize.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsDownlinkSize.setStatus(_A)
_An50WrlsRoundTripDelay_Type=Integer32
_An50WrlsRoundTripDelay_Object=MibScalar
an50WrlsRoundTripDelay=_An50WrlsRoundTripDelay_Object((1,3,6,1,4,1,10728,2,16,2,2,19,4),_An50WrlsRoundTripDelay_Type())
an50WrlsRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsRoundTripDelay.setStatus(_A)
class _An50WrlsAdaptiveDLSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_An50WrlsAdaptiveDLSize_Type.__name__=_C
_An50WrlsAdaptiveDLSize_Object=MibScalar
an50WrlsAdaptiveDLSize=_An50WrlsAdaptiveDLSize_Object((1,3,6,1,4,1,10728,2,16,2,2,19,5),_An50WrlsAdaptiveDLSize_Type())
an50WrlsAdaptiveDLSize.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsAdaptiveDLSize.setStatus(_A)
class _An50WrlsExtSyncronize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_An50WrlsExtSyncronize_Type.__name__=_C
_An50WrlsExtSyncronize_Object=MibScalar
an50WrlsExtSyncronize=_An50WrlsExtSyncronize_Object((1,3,6,1,4,1,10728,2,16,2,2,19,6),_An50WrlsExtSyncronize_Type())
an50WrlsExtSyncronize.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsExtSyncronize.setStatus(_A)
class _An50WrlsMaximumDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_An50WrlsMaximumDistance_Type.__name__=_C
_An50WrlsMaximumDistance_Object=MibScalar
an50WrlsMaximumDistance=_An50WrlsMaximumDistance_Object((1,3,6,1,4,1,10728,2,16,2,2,19,7),_An50WrlsMaximumDistance_Type())
an50WrlsMaximumDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsMaximumDistance.setStatus(_A)
class _An50WrlsRegistrationPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_An50WrlsRegistrationPeriod_Type.__name__=_C
_An50WrlsRegistrationPeriod_Object=MibScalar
an50WrlsRegistrationPeriod=_An50WrlsRegistrationPeriod_Object((1,3,6,1,4,1,10728,2,16,2,2,19,8),_An50WrlsRegistrationPeriod_Type())
an50WrlsRegistrationPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsRegistrationPeriod.setStatus(_A)
_An50ConfigDefGroup_ObjectIdentity=ObjectIdentity
an50ConfigDefGroup=_An50ConfigDefGroup_ObjectIdentity((1,3,6,1,4,1,10728,2,16,2,2,20))
_An50WrlsBroadcastDLCIR_Type=Integer32
_An50WrlsBroadcastDLCIR_Object=MibScalar
an50WrlsBroadcastDLCIR=_An50WrlsBroadcastDLCIR_Object((1,3,6,1,4,1,10728,2,16,2,2,20,1),_An50WrlsBroadcastDLCIR_Type())
an50WrlsBroadcastDLCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsBroadcastDLCIR.setStatus(_A)
_An50WrlsBroadcastDLPIR_Type=Integer32
_An50WrlsBroadcastDLPIR_Object=MibScalar
an50WrlsBroadcastDLPIR=_An50WrlsBroadcastDLPIR_Object((1,3,6,1,4,1,10728,2,16,2,2,20,2),_An50WrlsBroadcastDLPIR_Type())
an50WrlsBroadcastDLPIR.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsBroadcastDLPIR.setStatus(_A)
class _An50WrlsDFSAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('txDisabled',2),('changeFreq',3)))
_An50WrlsDFSAction_Type.__name__=_C
_An50WrlsDFSAction_Object=MibScalar
an50WrlsDFSAction=_An50WrlsDFSAction_Object((1,3,6,1,4,1,10728,2,16,2,2,21),_An50WrlsDFSAction_Type())
an50WrlsDFSAction.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsDFSAction.setStatus(_A)
_An50WrlsAntennaGain_Type=Integer32
_An50WrlsAntennaGain_Object=MibScalar
an50WrlsAntennaGain=_An50WrlsAntennaGain_Object((1,3,6,1,4,1,10728,2,16,2,2,22),_An50WrlsAntennaGain_Type())
an50WrlsAntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsAntennaGain.setStatus(_A)
class _An50WrlsATPEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_An50WrlsATPEnabled_Type.__name__=_C
_An50WrlsATPEnabled_Object=MibScalar
an50WrlsATPEnabled=_An50WrlsATPEnabled_Object((1,3,6,1,4,1,10728,2,16,2,2,23),_An50WrlsATPEnabled_Type())
an50WrlsATPEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:an50WrlsATPEnabled.setStatus(_A)
_An50Sw_ObjectIdentity=ObjectIdentity
an50Sw=_An50Sw_ObjectIdentity((1,3,6,1,4,1,10728,2,16,2,3))
_An50SwServer_Type=IpAddress
_An50SwServer_Object=MibScalar
an50SwServer=_An50SwServer_Object((1,3,6,1,4,1,10728,2,16,2,3,1),_An50SwServer_Type())
an50SwServer.setMaxAccess(_B)
if mibBuilder.loadTexts:an50SwServer.setStatus(_A)
class _An50SwFilename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_An50SwFilename_Type.__name__=_R
_An50SwFilename_Object=MibScalar
an50SwFilename=_An50SwFilename_Object((1,3,6,1,4,1,10728,2,16,2,3,2),_An50SwFilename_Type())
an50SwFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:an50SwFilename.setStatus(_A)
class _An50SwAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noUpgrade',1),('upgrade',2)))
_An50SwAdminStatus_Type.__name__=_C
_An50SwAdminStatus_Object=MibScalar
an50SwAdminStatus=_An50SwAdminStatus_Object((1,3,6,1,4,1,10728,2,16,2,3,3),_An50SwAdminStatus_Type())
an50SwAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:an50SwAdminStatus.setStatus(_A)
class _An50SwOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inProgress',1),('completeSuccess',2),('failed',3),('other',4)))
_An50SwOperStatus_Type.__name__=_C
_An50SwOperStatus_Object=MibScalar
an50SwOperStatus=_An50SwOperStatus_Object((1,3,6,1,4,1,10728,2,16,2,3,4),_An50SwOperStatus_Type())
an50SwOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:an50SwOperStatus.setStatus(_A)
_An50SwCurrentVers_Type=OctetString
_An50SwCurrentVers_Object=MibScalar
an50SwCurrentVers=_An50SwCurrentVers_Object((1,3,6,1,4,1,10728,2,16,2,3,5),_An50SwCurrentVers_Type())
an50SwCurrentVers.setMaxAccess(_D)
if mibBuilder.loadTexts:an50SwCurrentVers.setStatus(_A)
_An50SwOtherVers_Type=OctetString
_An50SwOtherVers_Object=MibScalar
an50SwOtherVers=_An50SwOtherVers_Object((1,3,6,1,4,1,10728,2,16,2,3,6),_An50SwOtherVers_Type())
an50SwOtherVers.setMaxAccess(_D)
if mibBuilder.loadTexts:an50SwOtherVers.setStatus(_A)
_An50Pm_ObjectIdentity=ObjectIdentity
an50Pm=_An50Pm_ObjectIdentity((1,3,6,1,4,1,10728,2,16,3))
class _An50ResetStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('reset',2)))
_An50ResetStatistics_Type.__name__=_C
_An50ResetStatistics_Object=MibScalar
an50ResetStatistics=_An50ResetStatistics_Object((1,3,6,1,4,1,10728,2,16,3,1),_An50ResetStatistics_Type())
an50ResetStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:an50ResetStatistics.setStatus(_A)
_An50PmEther_ObjectIdentity=ObjectIdentity
an50PmEther=_An50PmEther_ObjectIdentity((1,3,6,1,4,1,10728,2,16,3,2))
_An50PmEtherRxPackets_Type=Counter32
_An50PmEtherRxPackets_Object=MibScalar
an50PmEtherRxPackets=_An50PmEtherRxPackets_Object((1,3,6,1,4,1,10728,2,16,3,2,1),_An50PmEtherRxPackets_Type())
an50PmEtherRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmEtherRxPackets.setStatus(_A)
_An50PmEtherRxPacketsErr_Type=Counter32
_An50PmEtherRxPacketsErr_Object=MibScalar
an50PmEtherRxPacketsErr=_An50PmEtherRxPacketsErr_Object((1,3,6,1,4,1,10728,2,16,3,2,2),_An50PmEtherRxPacketsErr_Type())
an50PmEtherRxPacketsErr.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmEtherRxPacketsErr.setStatus(_A)
_An50PmEtherTxPackets_Type=Counter32
_An50PmEtherTxPackets_Object=MibScalar
an50PmEtherTxPackets=_An50PmEtherTxPackets_Object((1,3,6,1,4,1,10728,2,16,3,2,3),_An50PmEtherTxPackets_Type())
an50PmEtherTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmEtherTxPackets.setStatus(_A)
_An50PmEtherTxPacketsErr_Type=Counter32
_An50PmEtherTxPacketsErr_Object=MibScalar
an50PmEtherTxPacketsErr=_An50PmEtherTxPacketsErr_Object((1,3,6,1,4,1,10728,2,16,3,2,4),_An50PmEtherTxPacketsErr_Type())
an50PmEtherTxPacketsErr.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmEtherTxPacketsErr.setStatus(_A)
_An50PmEtherRxPacketsDisc_Type=Counter32
_An50PmEtherRxPacketsDisc_Object=MibScalar
an50PmEtherRxPacketsDisc=_An50PmEtherRxPacketsDisc_Object((1,3,6,1,4,1,10728,2,16,3,2,5),_An50PmEtherRxPacketsDisc_Type())
an50PmEtherRxPacketsDisc.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmEtherRxPacketsDisc.setStatus(_A)
_An50PmEtherTxPacketsDisc_Type=Counter32
_An50PmEtherTxPacketsDisc_Object=MibScalar
an50PmEtherTxPacketsDisc=_An50PmEtherTxPacketsDisc_Object((1,3,6,1,4,1,10728,2,16,3,2,6),_An50PmEtherTxPacketsDisc_Type())
an50PmEtherTxPacketsDisc.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmEtherTxPacketsDisc.setStatus(_A)
_An50PmWrls_ObjectIdentity=ObjectIdentity
an50PmWrls=_An50PmWrls_ObjectIdentity((1,3,6,1,4,1,10728,2,16,3,3))
_An50PmWrlsRxSigMin_Type=Integer32
_An50PmWrlsRxSigMin_Object=MibScalar
an50PmWrlsRxSigMin=_An50PmWrlsRxSigMin_Object((1,3,6,1,4,1,10728,2,16,3,3,1),_An50PmWrlsRxSigMin_Type())
an50PmWrlsRxSigMin.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsRxSigMin.setStatus(_A)
_An50PmWrlsRxSigMean_Type=Integer32
_An50PmWrlsRxSigMean_Object=MibScalar
an50PmWrlsRxSigMean=_An50PmWrlsRxSigMean_Object((1,3,6,1,4,1,10728,2,16,3,3,2),_An50PmWrlsRxSigMean_Type())
an50PmWrlsRxSigMean.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsRxSigMean.setStatus(_A)
_An50PmWrlsRxSigMax_Type=Integer32
_An50PmWrlsRxSigMax_Object=MibScalar
an50PmWrlsRxSigMax=_An50PmWrlsRxSigMax_Object((1,3,6,1,4,1,10728,2,16,3,3,3),_An50PmWrlsRxSigMax_Type())
an50PmWrlsRxSigMax.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsRxSigMax.setStatus(_A)
_An50PmWrlsAvgSinAdr_Type=Integer32
_An50PmWrlsAvgSinAdr_Object=MibScalar
an50PmWrlsAvgSinAdr=_An50PmWrlsAvgSinAdr_Object((1,3,6,1,4,1,10728,2,16,3,3,4),_An50PmWrlsAvgSinAdr_Type())
an50PmWrlsAvgSinAdr.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsAvgSinAdr.setStatus(_A)
_An50PmWrlsRxPackets_Type=Counter32
_An50PmWrlsRxPackets_Object=MibScalar
an50PmWrlsRxPackets=_An50PmWrlsRxPackets_Object((1,3,6,1,4,1,10728,2,16,3,3,5),_An50PmWrlsRxPackets_Type())
an50PmWrlsRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsRxPackets.setStatus(_A)
_An50PmWrlsRxPacketsRetx_Type=Counter32
_An50PmWrlsRxPacketsRetx_Object=MibScalar
an50PmWrlsRxPacketsRetx=_An50PmWrlsRxPacketsRetx_Object((1,3,6,1,4,1,10728,2,16,3,3,6),_An50PmWrlsRxPacketsRetx_Type())
an50PmWrlsRxPacketsRetx.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsRxPacketsRetx.setStatus(_A)
_An50PmWrlsRxPacketsDisc_Type=Counter32
_An50PmWrlsRxPacketsDisc_Object=MibScalar
an50PmWrlsRxPacketsDisc=_An50PmWrlsRxPacketsDisc_Object((1,3,6,1,4,1,10728,2,16,3,3,7),_An50PmWrlsRxPacketsDisc_Type())
an50PmWrlsRxPacketsDisc.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsRxPacketsDisc.setStatus(_A)
_An50PmWrlsTxPackets_Type=Counter32
_An50PmWrlsTxPackets_Object=MibScalar
an50PmWrlsTxPackets=_An50PmWrlsTxPackets_Object((1,3,6,1,4,1,10728,2,16,3,3,8),_An50PmWrlsTxPackets_Type())
an50PmWrlsTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsTxPackets.setStatus(_A)
_An50PmWrlsTxPacketsRetx_Type=Counter32
_An50PmWrlsTxPacketsRetx_Object=MibScalar
an50PmWrlsTxPacketsRetx=_An50PmWrlsTxPacketsRetx_Object((1,3,6,1,4,1,10728,2,16,3,3,9),_An50PmWrlsTxPacketsRetx_Type())
an50PmWrlsTxPacketsRetx.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsTxPacketsRetx.setStatus(_A)
_An50PmWrlsTxPacketsDisc_Type=Counter32
_An50PmWrlsTxPacketsDisc_Object=MibScalar
an50PmWrlsTxPacketsDisc=_An50PmWrlsTxPacketsDisc_Object((1,3,6,1,4,1,10728,2,16,3,3,10),_An50PmWrlsTxPacketsDisc_Type())
an50PmWrlsTxPacketsDisc.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsTxPacketsDisc.setStatus(_A)
_An50PmWrlsCalcDst_Type=Integer32
_An50PmWrlsCalcDst_Object=MibScalar
an50PmWrlsCalcDst=_An50PmWrlsCalcDst_Object((1,3,6,1,4,1,10728,2,16,3,3,11),_An50PmWrlsCalcDst_Type())
an50PmWrlsCalcDst.setMaxAccess(_D)
if mibBuilder.loadTexts:an50PmWrlsCalcDst.setStatus(_A)
_An50Trap_ObjectIdentity=ObjectIdentity
an50Trap=_An50Trap_ObjectIdentity((1,3,6,1,4,1,10728,2,16,4))
_An50SysLastTrapTime_Type=TimeTicks
_An50SysLastTrapTime_Object=MibScalar
an50SysLastTrapTime=_An50SysLastTrapTime_Object((1,3,6,1,4,1,10728,2,16,4,1),_An50SysLastTrapTime_Type())
an50SysLastTrapTime.setMaxAccess(_D)
if mibBuilder.loadTexts:an50SysLastTrapTime.setStatus(_A)
_An50LinkPmp_ObjectIdentity=ObjectIdentity
an50LinkPmp=_An50LinkPmp_ObjectIdentity((1,3,6,1,4,1,10728,2,16,5))
class _An50MaxCid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50MaxCid_Type.__name__=_C
_An50MaxCid_Object=MibScalar
an50MaxCid=_An50MaxCid_Object((1,3,6,1,4,1,10728,2,16,5,1),_An50MaxCid_Type())
an50MaxCid.setMaxAccess(_D)
if mibBuilder.loadTexts:an50MaxCid.setStatus(_A)
_An50LinkCurrentAvailId_Type=Integer32
_An50LinkCurrentAvailId_Object=MibScalar
an50LinkCurrentAvailId=_An50LinkCurrentAvailId_Object((1,3,6,1,4,1,10728,2,16,5,2),_An50LinkCurrentAvailId_Type())
an50LinkCurrentAvailId.setMaxAccess(_D)
if mibBuilder.loadTexts:an50LinkCurrentAvailId.setStatus(_A)
an50TftpFailTrap=NotificationType((1,3,6,1,4,1,10728,0,1))
an50TftpFailTrap.setObjects(*((_E,_N),(_E,_O),(_E,_P),(_E,_Q),(_E,_F)))
if mibBuilder.loadTexts:an50TftpFailTrap.setStatus('')
an50TftpSuccessTrap=NotificationType((1,3,6,1,4,1,10728,0,2))
an50TftpSuccessTrap.setObjects(*((_E,_N),(_E,_O),(_E,_P),(_E,_Q),(_E,_F)))
if mibBuilder.loadTexts:an50TftpSuccessTrap.setStatus('')
an50PswdChangeFailTrap=NotificationType((1,3,6,1,4,1,10728,0,3))
an50PswdChangeFailTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:an50PswdChangeFailTrap.setStatus('')
an50FirmwareConfigFailTrap=NotificationType((1,3,6,1,4,1,10728,0,4))
an50FirmwareConfigFailTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:an50FirmwareConfigFailTrap.setStatus('')
an50EepromCorruptedTrap=NotificationType((1,3,6,1,4,1,10728,0,5))
an50EepromCorruptedTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:an50EepromCorruptedTrap.setStatus('')
an50PowerSupplyFailureTrap=NotificationType((1,3,6,1,4,1,10728,0,6))
an50PowerSupplyFailureTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:an50PowerSupplyFailureTrap.setStatus('')
an50SaveConfigTrap=NotificationType((1,3,6,1,4,1,10728,0,7))
an50SaveConfigTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:an50SaveConfigTrap.setStatus('')
an50ModifiedIDTrap=NotificationType((1,3,6,1,4,1,10728,0,8))
an50ModifiedIDTrap.setObjects(*((_J,_T),(_E,_F)))
if mibBuilder.loadTexts:an50ModifiedIDTrap.setStatus('')
an50pmpRegistrationMissed=NotificationType((1,3,6,1,4,1,10728,0,9))
an50pmpRegistrationMissed.setObjects(*((_J,_S),(_E,_F)))
if mibBuilder.loadTexts:an50pmpRegistrationMissed.setStatus('')
an50pmpRegistrationSuccessful=NotificationType((1,3,6,1,4,1,10728,0,10))
an50pmpRegistrationSuccessful.setObjects(*((_J,_U),(_E,_F)))
if mibBuilder.loadTexts:an50pmpRegistrationSuccessful.setStatus('')
an50DFSEvent=NotificationType((1,3,6,1,4,1,10728,0,11))
an50DFSEvent.setObjects((_E,_F))
if mibBuilder.loadTexts:an50DFSEvent.setStatus('')
mibBuilder.exportSymbols(_E,**{'redline':redline,'an50TftpFailTrap':an50TftpFailTrap,'an50TftpSuccessTrap':an50TftpSuccessTrap,'an50PswdChangeFailTrap':an50PswdChangeFailTrap,'an50FirmwareConfigFailTrap':an50FirmwareConfigFailTrap,'an50EepromCorruptedTrap':an50EepromCorruptedTrap,'an50PowerSupplyFailureTrap':an50PowerSupplyFailureTrap,'an50SaveConfigTrap':an50SaveConfigTrap,'an50ModifiedIDTrap':an50ModifiedIDTrap,'an50pmpRegistrationMissed':an50pmpRegistrationMissed,'an50pmpRegistrationSuccessful':an50pmpRegistrationSuccessful,'an50DFSEvent':an50DFSEvent,'redlineProducts':redlineProducts,'redlineMgmt':redlineMgmt,'redlineAn50':redlineAn50,'an50General':an50General,'an50GenUBR':an50GenUBR,'an50GenRFLink':an50GenRFLink,'an50GenFrequency':an50GenFrequency,'an50GenAllignmentMode':an50GenAllignmentMode,'an50GenEncryptionEnabled':an50GenEncryptionEnabled,'an50GenFlowControlEnabled':an50GenFlowControlEnabled,'an50GenHttpAccessEnabled':an50GenHttpAccessEnabled,'an50GenTelnetAccessEnabled':an50GenTelnetAccessEnabled,'an50GenTelnetPort':an50GenTelnetPort,'an50GenOptionsKey':an50GenOptionsKey,'an50GenResetDevice':an50GenResetDevice,'an50GenFault':an50GenFault,'an50GenTxPower':an50GenTxPower,'an50GenRegisteredStations':an50GenRegisteredStations,'an50GenRegisteredConnections':an50GenRegisteredConnections,'an50GenActiveWirelessLinks':an50GenActiveWirelessLinks,'an50GenChannelAutoScan':an50GenChannelAutoScan,'an50GenIduType':an50GenIduType,'an50GenOduType':an50GenOduType,'an50Config':an50Config,'an50ConfigEther':an50ConfigEther,'an50EtherMacAddress':an50EtherMacAddress,'an50EtherGateway':an50EtherGateway,'an50EtherPortStatus':an50EtherPortStatus,'an50EtherIP':an50EtherIP,'an50EtherMask':an50EtherMask,'an50Ether100':an50Ether100,'an50EtherFd':an50EtherFd,'an50EtherMgmVidEn':an50EtherMgmVidEn,'an50EtherMgmVid':an50EtherMgmVid,'an50EtherLben':an50EtherLben,'an50ConfigWireless':an50ConfigWireless,'an50WrlsChannel':an50WrlsChannel,'an50WrlsTxPower':an50WrlsTxPower,'an50WrlsModReduction':an50WrlsModReduction,'an50WrlsAdaptiveMod':an50WrlsAdaptiveMod,'an50WrlsUBR':an50WrlsUBR,'an50WrlsMaster':an50WrlsMaster,'an50WrlsVersion':an50WrlsVersion,'an50WrlsEncryptCode':an50WrlsEncryptCode,'an50WrlsCableAttenuation':an50WrlsCableAttenuation,'an50WrlsRfPortStatus':an50WrlsRfPortStatus,'an50WrlsSaveConfig':an50WrlsSaveConfig,'an50WrlsActivateConfig':an50WrlsActivateConfig,'an50WrlsRadioEnable':an50WrlsRadioEnable,'an50WrlsRfStatusErrorCode':an50WrlsRfStatusErrorCode,'an50WrlsRfSignal':an50WrlsRfSignal,'an50WrlsLLMode':an50WrlsLLMode,'an50WrlsLMU':an50WrlsLMU,'an50WrlsLL':an50WrlsLL,'an50ConfigScheduler':an50ConfigScheduler,'an50WrlsFrameSize':an50WrlsFrameSize,'an50WrlsMinBlockSize':an50WrlsMinBlockSize,'an50WrlsDownlinkSize':an50WrlsDownlinkSize,'an50WrlsRoundTripDelay':an50WrlsRoundTripDelay,'an50WrlsAdaptiveDLSize':an50WrlsAdaptiveDLSize,'an50WrlsExtSyncronize':an50WrlsExtSyncronize,'an50WrlsMaximumDistance':an50WrlsMaximumDistance,'an50WrlsRegistrationPeriod':an50WrlsRegistrationPeriod,'an50ConfigDefGroup':an50ConfigDefGroup,'an50WrlsBroadcastDLCIR':an50WrlsBroadcastDLCIR,'an50WrlsBroadcastDLPIR':an50WrlsBroadcastDLPIR,'an50WrlsDFSAction':an50WrlsDFSAction,'an50WrlsAntennaGain':an50WrlsAntennaGain,'an50WrlsATPEnabled':an50WrlsATPEnabled,'an50Sw':an50Sw,_N:an50SwServer,_O:an50SwFilename,_P:an50SwAdminStatus,_Q:an50SwOperStatus,'an50SwCurrentVers':an50SwCurrentVers,'an50SwOtherVers':an50SwOtherVers,'an50Pm':an50Pm,'an50ResetStatistics':an50ResetStatistics,'an50PmEther':an50PmEther,'an50PmEtherRxPackets':an50PmEtherRxPackets,'an50PmEtherRxPacketsErr':an50PmEtherRxPacketsErr,'an50PmEtherTxPackets':an50PmEtherTxPackets,'an50PmEtherTxPacketsErr':an50PmEtherTxPacketsErr,'an50PmEtherRxPacketsDisc':an50PmEtherRxPacketsDisc,'an50PmEtherTxPacketsDisc':an50PmEtherTxPacketsDisc,'an50PmWrls':an50PmWrls,'an50PmWrlsRxSigMin':an50PmWrlsRxSigMin,'an50PmWrlsRxSigMean':an50PmWrlsRxSigMean,'an50PmWrlsRxSigMax':an50PmWrlsRxSigMax,'an50PmWrlsAvgSinAdr':an50PmWrlsAvgSinAdr,'an50PmWrlsRxPackets':an50PmWrlsRxPackets,'an50PmWrlsRxPacketsRetx':an50PmWrlsRxPacketsRetx,'an50PmWrlsRxPacketsDisc':an50PmWrlsRxPacketsDisc,'an50PmWrlsTxPackets':an50PmWrlsTxPackets,'an50PmWrlsTxPacketsRetx':an50PmWrlsTxPacketsRetx,'an50PmWrlsTxPacketsDisc':an50PmWrlsTxPacketsDisc,'an50PmWrlsCalcDst':an50PmWrlsCalcDst,'an50Trap':an50Trap,_F:an50SysLastTrapTime,'an50LinkPmp':an50LinkPmp,'an50MaxCid':an50MaxCid,'an50LinkCurrentAvailId':an50LinkCurrentAvailId})