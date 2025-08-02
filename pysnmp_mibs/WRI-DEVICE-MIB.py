_S='msppDevLoggingInfo'
_R='msppDevDescr'
_Q='msppDevMac'
_P='PhysAddress'
_O='crc16-upper'
_N='crc16-lower'
_M='lsb'
_L='crc32-lower'
_K='crc32-upper'
_J='master'
_I='WRI-DEVICE-MIB'
_H='enable'
_G='disable'
_F='backup'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,_P,'TextualConvention')
wriProducts,wriProtocol=mibBuilder.importSymbols('WRI-SMI','wriProducts','wriProtocol')
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class DisplayString(TextualConvention,OctetString):status=_A
class RerRingDir(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('west',0),('east',1)))
class EntryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
class VlanIndex(TextualConvention,Unsigned32):status=_A
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Mspp_ObjectIdentity=ObjectIdentity
mspp=_Mspp_ObjectIdentity((1,3,6,1,4,1,3807,1,8012))
_MsppChassis_ObjectIdentity=ObjectIdentity
msppChassis=_MsppChassis_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1))
_MsppDev_ObjectIdentity=ObjectIdentity
msppDev=_MsppDev_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,2))
_MsppDevGeneral_ObjectIdentity=ObjectIdentity
msppDevGeneral=_MsppDevGeneral_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,2,1))
class _MsppDevMac_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_MsppDevMac_Type.__name__=_P
_MsppDevMac_Object=MibScalar
msppDevMac=_MsppDevMac_Object((1,3,6,1,4,1,3807,1,8012,2,1,1),_MsppDevMac_Type())
msppDevMac.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevMac.setStatus(_A)
class _MsppDevDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MsppDevDescr_Type.__name__=_E
_MsppDevDescr_Object=MibScalar
msppDevDescr=_MsppDevDescr_Object((1,3,6,1,4,1,3807,1,8012,2,1,2),_MsppDevDescr_Type())
msppDevDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevDescr.setStatus(_A)
class _MsppDevHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MsppDevHwVersion_Type.__name__=_E
_MsppDevHwVersion_Object=MibScalar
msppDevHwVersion=_MsppDevHwVersion_Object((1,3,6,1,4,1,3807,1,8012,2,1,3),_MsppDevHwVersion_Type())
msppDevHwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevHwVersion.setStatus(_A)
class _MsppDevSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MsppDevSwVersion_Type.__name__=_E
_MsppDevSwVersion_Object=MibScalar
msppDevSwVersion=_MsppDevSwVersion_Object((1,3,6,1,4,1,3807,1,8012,2,1,4),_MsppDevSwVersion_Type())
msppDevSwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevSwVersion.setStatus(_A)
_MsppDevCardBits_Type=Counter32
_MsppDevCardBits_Object=MibScalar
msppDevCardBits=_MsppDevCardBits_Object((1,3,6,1,4,1,3807,1,8012,2,1,5),_MsppDevCardBits_Type())
msppDevCardBits.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevCardBits.setStatus(_A)
_MsppDevCardNum_Type=Integer32
_MsppDevCardNum_Object=MibScalar
msppDevCardNum=_MsppDevCardNum_Object((1,3,6,1,4,1,3807,1,8012,2,1,6),_MsppDevCardNum_Type())
msppDevCardNum.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevCardNum.setStatus(_A)
_MsppDevLastChange_Type=TimeTicks
_MsppDevLastChange_Object=MibScalar
msppDevLastChange=_MsppDevLastChange_Object((1,3,6,1,4,1,3807,1,8012,2,1,7),_MsppDevLastChange_Type())
msppDevLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevLastChange.setStatus(_A)
_MsppDevUpTime_Type=TimeTicks
_MsppDevUpTime_Object=MibScalar
msppDevUpTime=_MsppDevUpTime_Object((1,3,6,1,4,1,3807,1,8012,2,1,8),_MsppDevUpTime_Type())
msppDevUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevUpTime.setStatus(_A)
class _MsppDevTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MsppDevTime_Type.__name__=_E
_MsppDevTime_Object=MibScalar
msppDevTime=_MsppDevTime_Object((1,3,6,1,4,1,3807,1,8012,2,1,9),_MsppDevTime_Type())
msppDevTime.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTime.setStatus(_A)
class _MsppDevFlushMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_MsppDevFlushMac_Type.__name__=_C
_MsppDevFlushMac_Object=MibScalar
msppDevFlushMac=_MsppDevFlushMac_Object((1,3,6,1,4,1,3807,1,8012,2,1,10),_MsppDevFlushMac_Type())
msppDevFlushMac.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevFlushMac.setStatus(_A)
class _MsppDevReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('reboot',1),('writeconfigandreboot',2),('writeconfigandrebootsys',3),('eraseconfigandreboot',4),('eraseconfigandrebootsys',5)))
_MsppDevReboot_Type.__name__=_C
_MsppDevReboot_Object=MibScalar
msppDevReboot=_MsppDevReboot_Object((1,3,6,1,4,1,3807,1,8012,2,1,11),_MsppDevReboot_Type())
msppDevReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevReboot.setStatus(_A)
class _MsppDevCfgFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MsppDevCfgFile_Type.__name__=_E
_MsppDevCfgFile_Object=MibScalar
msppDevCfgFile=_MsppDevCfgFile_Object((1,3,6,1,4,1,3807,1,8012,2,1,12),_MsppDevCfgFile_Type())
msppDevCfgFile.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevCfgFile.setStatus(_A)
class _MsppDevCfgAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('write',1),('erase',2),('exec',3),('upgrade',4),('writestartup',5),('erasestartup',6),('execstartup',7),('upgradestartup',8),('writebackup',9),('erasebackup',10),('execbackup',11),('upgradebackup',12),('writeboth',13),('eraseboth',14),('upgradeboth',15),('recoverconfig',16)))
_MsppDevCfgAction_Type.__name__=_C
_MsppDevCfgAction_Object=MibScalar
msppDevCfgAction=_MsppDevCfgAction_Object((1,3,6,1,4,1,3807,1,8012,2,1,13),_MsppDevCfgAction_Type())
msppDevCfgAction.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevCfgAction.setStatus(_A)
class _MsppDevOsFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MsppDevOsFile_Type.__name__=_E
_MsppDevOsFile_Object=MibScalar
msppDevOsFile=_MsppDevOsFile_Object((1,3,6,1,4,1,3807,1,8012,2,1,14),_MsppDevOsFile_Type())
msppDevOsFile.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevOsFile.setStatus(_A)
class _MsppDevOsAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('upgradebootos',1),('upgradebootosandreboot',2),('upgrademainos',3),('upgradebakos',4),('upgradebothos',5),('recoverbootos',6)))
_MsppDevOsAction_Type.__name__=_C
_MsppDevOsAction_Object=MibScalar
msppDevOsAction=_MsppDevOsAction_Object((1,3,6,1,4,1,3807,1,8012,2,1,15),_MsppDevOsAction_Type())
msppDevOsAction.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevOsAction.setStatus(_A)
class _MsppDevVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mspp1',1),('mspp2EO',2),('mspp2O',3),('mspp3',4)))
_MsppDevVer_Type.__name__=_C
_MsppDevVer_Object=MibScalar
msppDevVer=_MsppDevVer_Object((1,3,6,1,4,1,3807,1,8012,2,1,16),_MsppDevVer_Type())
msppDevVer.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevVer.setStatus(_A)
_MsppDevErrorBits_Type=Counter32
_MsppDevErrorBits_Object=MibScalar
msppDevErrorBits=_MsppDevErrorBits_Object((1,3,6,1,4,1,3807,1,8012,2,1,17),_MsppDevErrorBits_Type())
msppDevErrorBits.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevErrorBits.setStatus(_A)
_MsppDevTemperatureLThreshold_Type=Integer32
_MsppDevTemperatureLThreshold_Object=MibScalar
msppDevTemperatureLThreshold=_MsppDevTemperatureLThreshold_Object((1,3,6,1,4,1,3807,1,8012,2,1,18),_MsppDevTemperatureLThreshold_Type())
msppDevTemperatureLThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTemperatureLThreshold.setStatus(_A)
_MsppDevTemperatureHThreshold_Type=Integer32
_MsppDevTemperatureHThreshold_Object=MibScalar
msppDevTemperatureHThreshold=_MsppDevTemperatureHThreshold_Object((1,3,6,1,4,1,3807,1,8012,2,1,19),_MsppDevTemperatureHThreshold_Type())
msppDevTemperatureHThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTemperatureHThreshold.setStatus(_A)
_MsppDevTemperature_Type=Integer32
_MsppDevTemperature_Object=MibScalar
msppDevTemperature=_MsppDevTemperature_Object((1,3,6,1,4,1,3807,1,8012,2,1,20),_MsppDevTemperature_Type())
msppDevTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTemperature.setStatus(_A)
_MsppDevTemperatureTrapEnable_Type=Integer32
_MsppDevTemperatureTrapEnable_Object=MibScalar
msppDevTemperatureTrapEnable=_MsppDevTemperatureTrapEnable_Object((1,3,6,1,4,1,3807,1,8012,2,1,21),_MsppDevTemperatureTrapEnable_Type())
msppDevTemperatureTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTemperatureTrapEnable.setStatus(_A)
class _MsppDevWRED_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_MsppDevWRED_Type.__name__=_C
_MsppDevWRED_Object=MibScalar
msppDevWRED=_MsppDevWRED_Object((1,3,6,1,4,1,3807,1,8012,2,1,22),_MsppDevWRED_Type())
msppDevWRED.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevWRED.setStatus(_A)
_MsppDevMirrorToPort_Type=Integer32
_MsppDevMirrorToPort_Object=MibScalar
msppDevMirrorToPort=_MsppDevMirrorToPort_Object((1,3,6,1,4,1,3807,1,8012,2,1,23),_MsppDevMirrorToPort_Type())
msppDevMirrorToPort.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevMirrorToPort.setStatus(_A)
_MsppDevMirrorMode_Type=Integer32
_MsppDevMirrorMode_Object=MibScalar
msppDevMirrorMode=_MsppDevMirrorMode_Object((1,3,6,1,4,1,3807,1,8012,2,1,24),_MsppDevMirrorMode_Type())
msppDevMirrorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevMirrorMode.setStatus(_A)
_MsppDevLcd_Type=Integer32
_MsppDevLcd_Object=MibScalar
msppDevLcd=_MsppDevLcd_Object((1,3,6,1,4,1,3807,1,8012,2,1,25),_MsppDevLcd_Type())
msppDevLcd.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevLcd.setStatus(_A)
_MsppDevTDMVlan_Type=Integer32
_MsppDevTDMVlan_Object=MibScalar
msppDevTDMVlan=_MsppDevTDMVlan_Object((1,3,6,1,4,1,3807,1,8012,2,1,26),_MsppDevTDMVlan_Type())
msppDevTDMVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTDMVlan.setStatus(_A)
_MsppDevFtpd_Type=Integer32
_MsppDevFtpd_Object=MibScalar
msppDevFtpd=_MsppDevFtpd_Object((1,3,6,1,4,1,3807,1,8012,2,1,27),_MsppDevFtpd_Type())
msppDevFtpd.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevFtpd.setStatus(_A)
_MsppDevTelnetd_Type=Integer32
_MsppDevTelnetd_Object=MibScalar
msppDevTelnetd=_MsppDevTelnetd_Object((1,3,6,1,4,1,3807,1,8012,2,1,28),_MsppDevTelnetd_Type())
msppDevTelnetd.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTelnetd.setStatus(_A)
_MsppDevMirrorToRspanVid_Type=Integer32
_MsppDevMirrorToRspanVid_Object=MibScalar
msppDevMirrorToRspanVid=_MsppDevMirrorToRspanVid_Object((1,3,6,1,4,1,3807,1,8012,2,1,29),_MsppDevMirrorToRspanVid_Type())
msppDevMirrorToRspanVid.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevMirrorToRspanVid.setStatus(_A)
_MsppDevMirrorToTpid_Type=Integer32
_MsppDevMirrorToTpid_Object=MibScalar
msppDevMirrorToTpid=_MsppDevMirrorToTpid_Object((1,3,6,1,4,1,3807,1,8012,2,1,30),_MsppDevMirrorToTpid_Type())
msppDevMirrorToTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevMirrorToTpid.setStatus(_A)
class _MsppRebootFileMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_F,1)))
_MsppRebootFileMode_Type.__name__=_C
_MsppRebootFileMode_Object=MibScalar
msppRebootFileMode=_MsppRebootFileMode_Object((1,3,6,1,4,1,3807,1,8012,2,1,31),_MsppRebootFileMode_Type())
msppRebootFileMode.setMaxAccess(_B)
if mibBuilder.loadTexts:msppRebootFileMode.setStatus(_A)
class _MsppFileExecMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_F,1)))
_MsppFileExecMode_Type.__name__=_C
_MsppFileExecMode_Object=MibScalar
msppFileExecMode=_MsppFileExecMode_Object((1,3,6,1,4,1,3807,1,8012,2,1,32),_MsppFileExecMode_Type())
msppFileExecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:msppFileExecMode.setStatus(_A)
class _MsppUpgradeBkOs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_F,1)))
_MsppUpgradeBkOs_Type.__name__=_C
_MsppUpgradeBkOs_Object=MibScalar
msppUpgradeBkOs=_MsppUpgradeBkOs_Object((1,3,6,1,4,1,3807,1,8012,2,1,33),_MsppUpgradeBkOs_Type())
msppUpgradeBkOs.setMaxAccess(_B)
if mibBuilder.loadTexts:msppUpgradeBkOs.setStatus(_A)
class _MsppInbandIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_MsppInbandIp_Type.__name__=_E
_MsppInbandIp_Object=MibScalar
msppInbandIp=_MsppInbandIp_Object((1,3,6,1,4,1,3807,1,8012,2,1,34),_MsppInbandIp_Type())
msppInbandIp.setMaxAccess(_B)
if mibBuilder.loadTexts:msppInbandIp.setStatus(_A)
class _MsppOutbandIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_MsppOutbandIp_Type.__name__=_E
_MsppOutbandIp_Object=MibScalar
msppOutbandIp=_MsppOutbandIp_Object((1,3,6,1,4,1,3807,1,8012,2,1,35),_MsppOutbandIp_Type())
msppOutbandIp.setMaxAccess(_B)
if mibBuilder.loadTexts:msppOutbandIp.setStatus(_A)
class _ResetEraseCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ResetEraseCfg_Type.__name__=_C
_ResetEraseCfg_Object=MibScalar
resetEraseCfg=_ResetEraseCfg_Object((1,3,6,1,4,1,3807,1,8012,2,1,36),_ResetEraseCfg_Type())
resetEraseCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:resetEraseCfg.setStatus(_A)
class _MsppDevLicenseEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_MsppDevLicenseEnable_Type.__name__=_C
_MsppDevLicenseEnable_Object=MibScalar
msppDevLicenseEnable=_MsppDevLicenseEnable_Object((1,3,6,1,4,1,3807,1,8012,2,1,37),_MsppDevLicenseEnable_Type())
msppDevLicenseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevLicenseEnable.setStatus(_A)
class _MsppDevLicenseKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MsppDevLicenseKey_Type.__name__=_E
_MsppDevLicenseKey_Object=MibScalar
msppDevLicenseKey=_MsppDevLicenseKey_Object((1,3,6,1,4,1,3807,1,8012,2,1,38),_MsppDevLicenseKey_Type())
msppDevLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevLicenseKey.setStatus(_A)
class _MsppDevSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MsppDevSerialNum_Type.__name__=_E
_MsppDevSerialNum_Object=MibScalar
msppDevSerialNum=_MsppDevSerialNum_Object((1,3,6,1,4,1,3807,1,8012,2,1,39),_MsppDevSerialNum_Type())
msppDevSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevSerialNum.setStatus(_A)
_MsppDevMtu_Type=Unsigned32
_MsppDevMtu_Object=MibScalar
msppDevMtu=_MsppDevMtu_Object((1,3,6,1,4,1,3807,1,8012,2,1,40),_MsppDevMtu_Type())
msppDevMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevMtu.setStatus(_A)
_MsppDevFlushDynamicArp_Type=Unsigned32
_MsppDevFlushDynamicArp_Object=MibScalar
msppDevFlushDynamicArp=_MsppDevFlushDynamicArp_Object((1,3,6,1,4,1,3807,1,8012,2,1,41),_MsppDevFlushDynamicArp_Type())
msppDevFlushDynamicArp.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevFlushDynamicArp.setStatus(_A)
_MsppDevFlushStaticArp_Type=Unsigned32
_MsppDevFlushStaticArp_Object=MibScalar
msppDevFlushStaticArp=_MsppDevFlushStaticArp_Object((1,3,6,1,4,1,3807,1,8012,2,1,42),_MsppDevFlushStaticArp_Type())
msppDevFlushStaticArp.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevFlushStaticArp.setStatus(_A)
_MsppDevFlushAllArp_Type=Unsigned32
_MsppDevFlushAllArp_Object=MibScalar
msppDevFlushAllArp=_MsppDevFlushAllArp_Object((1,3,6,1,4,1,3807,1,8012,2,1,43),_MsppDevFlushAllArp_Type())
msppDevFlushAllArp.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevFlushAllArp.setStatus(_A)
class _MsppDevBootOs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('main',0),(_F,1)))
_MsppDevBootOs_Type.__name__=_C
_MsppDevBootOs_Object=MibScalar
msppDevBootOs=_MsppDevBootOs_Object((1,3,6,1,4,1,3807,1,8012,2,1,44),_MsppDevBootOs_Type())
msppDevBootOs.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevBootOs.setStatus(_A)
class _MsppDevBootCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('main',0),(_F,1)))
_MsppDevBootCfg_Type.__name__=_C
_MsppDevBootCfg_Object=MibScalar
msppDevBootCfg=_MsppDevBootCfg_Object((1,3,6,1,4,1,3807,1,8012,2,1,45),_MsppDevBootCfg_Type())
msppDevBootCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevBootCfg.setStatus(_A)
class _Msppl2HashMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5)))
_Msppl2HashMode_Type.__name__=_C
_Msppl2HashMode_Object=MibScalar
msppl2HashMode=_Msppl2HashMode_Object((1,3,6,1,4,1,3807,1,8012,2,1,46),_Msppl2HashMode_Type())
msppl2HashMode.setMaxAccess(_B)
if mibBuilder.loadTexts:msppl2HashMode.setStatus(_A)
class _Msppl3HashMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5)))
_Msppl3HashMode_Type.__name__=_C
_Msppl3HashMode_Object=MibScalar
msppl3HashMode=_Msppl3HashMode_Object((1,3,6,1,4,1,3807,1,8012,2,1,47),_Msppl3HashMode_Type())
msppl3HashMode.setMaxAccess(_B)
if mibBuilder.loadTexts:msppl3HashMode.setStatus(_A)
class _Msppl2AuxHashMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('zero',0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5)))
_Msppl2AuxHashMode_Type.__name__=_C
_Msppl2AuxHashMode_Object=MibScalar
msppl2AuxHashMode=_Msppl2AuxHashMode_Object((1,3,6,1,4,1,3807,1,8012,2,1,48),_Msppl2AuxHashMode_Type())
msppl2AuxHashMode.setMaxAccess(_B)
if mibBuilder.loadTexts:msppl2AuxHashMode.setStatus(_A)
_MsppIpv4AddrNum_Type=Integer32
_MsppIpv4AddrNum_Object=MibScalar
msppIpv4AddrNum=_MsppIpv4AddrNum_Object((1,3,6,1,4,1,3807,1,8012,2,1,49),_MsppIpv4AddrNum_Type())
msppIpv4AddrNum.setMaxAccess(_D)
if mibBuilder.loadTexts:msppIpv4AddrNum.setStatus(_A)
class _MsppDevCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MsppDevCode_Type.__name__=_E
_MsppDevCode_Object=MibScalar
msppDevCode=_MsppDevCode_Object((1,3,6,1,4,1,3807,1,8012,2,1,50),_MsppDevCode_Type())
msppDevCode.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevCode.setStatus(_A)
_MsppCmuState_Type=Integer32
_MsppCmuState_Object=MibScalar
msppCmuState=_MsppCmuState_Object((1,3,6,1,4,1,3807,1,8012,2,1,51),_MsppCmuState_Type())
msppCmuState.setMaxAccess(_D)
if mibBuilder.loadTexts:msppCmuState.setStatus(_A)
_MsppDevTpid_Type=Unsigned32
_MsppDevTpid_Object=MibScalar
msppDevTpid=_MsppDevTpid_Object((1,3,6,1,4,1,3807,1,8012,2,1,52),_MsppDevTpid_Type())
msppDevTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevTpid.setStatus(_A)
class _MsppDevLoggingInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_MsppDevLoggingInfo_Type.__name__=_E
_MsppDevLoggingInfo_Object=MibScalar
msppDevLoggingInfo=_MsppDevLoggingInfo_Object((1,3,6,1,4,1,3807,1,8012,2,1,53),_MsppDevLoggingInfo_Type())
msppDevLoggingInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:msppDevLoggingInfo.setStatus(_A)
_LoggingTrapObjects_ObjectIdentity=ObjectIdentity
loggingTrapObjects=_LoggingTrapObjects_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,2,1,54))
class _MsppDevFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MsppDevFileName_Type.__name__=_E
_MsppDevFileName_Object=MibScalar
msppDevFileName=_MsppDevFileName_Object((1,3,6,1,4,1,3807,1,8012,2,1,55),_MsppDevFileName_Type())
msppDevFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevFileName.setStatus(_A)
class _MsppDevFileAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('delet',1))
_MsppDevFileAction_Type.__name__=_C
_MsppDevFileAction_Object=MibScalar
msppDevFileAction=_MsppDevFileAction_Object((1,3,6,1,4,1,3807,1,8012,2,1,56),_MsppDevFileAction_Type())
msppDevFileAction.setMaxAccess(_B)
if mibBuilder.loadTexts:msppDevFileAction.setStatus(_A)
class _MsppShareVlanEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_MsppShareVlanEn_Type.__name__=_C
_MsppShareVlanEn_Object=MibScalar
msppShareVlanEn=_MsppShareVlanEn_Object((1,3,6,1,4,1,3807,1,8012,2,1,57),_MsppShareVlanEn_Type())
msppShareVlanEn.setMaxAccess(_B)
if mibBuilder.loadTexts:msppShareVlanEn.setStatus(_A)
_MsppUpgradeStatus_Type=Integer32
_MsppUpgradeStatus_Object=MibScalar
msppUpgradeStatus=_MsppUpgradeStatus_Object((1,3,6,1,4,1,3807,1,8012,2,1,58),_MsppUpgradeStatus_Type())
msppUpgradeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:msppUpgradeStatus.setStatus(_A)
_MsppCliVersion_Type=OctetString
_MsppCliVersion_Object=MibScalar
msppCliVersion=_MsppCliVersion_Object((1,3,6,1,4,1,3807,1,8012,2,1,59),_MsppCliVersion_Type())
msppCliVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:msppCliVersion.setStatus(_A)
_MsppSnmpVersion_Type=OctetString
_MsppSnmpVersion_Object=MibScalar
msppSnmpVersion=_MsppSnmpVersion_Object((1,3,6,1,4,1,3807,1,8012,2,1,60),_MsppSnmpVersion_Type())
msppSnmpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:msppSnmpVersion.setStatus(_A)
_MsppHttpVersion_Type=OctetString
_MsppHttpVersion_Object=MibScalar
msppHttpVersion=_MsppHttpVersion_Object((1,3,6,1,4,1,3807,1,8012,2,1,61),_MsppHttpVersion_Type())
msppHttpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:msppHttpVersion.setStatus(_A)
loggingTrap=NotificationType((1,3,6,1,4,1,3807,1,8012,2,1,54,1))
loggingTrap.setObjects(*((_I,_Q),(_I,_R),(_I,_S)))
if mibBuilder.loadTexts:loggingTrap.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'PortList':PortList,'BridgeId':BridgeId,_E:DisplayString,'RerRingDir':RerRingDir,'EntryStatus':EntryStatus,'VlanIndex':VlanIndex,'VlanId':VlanId,'mspp':mspp,'msppChassis':msppChassis,'msppDev':msppDev,'msppDevGeneral':msppDevGeneral,_Q:msppDevMac,_R:msppDevDescr,'msppDevHwVersion':msppDevHwVersion,'msppDevSwVersion':msppDevSwVersion,'msppDevCardBits':msppDevCardBits,'msppDevCardNum':msppDevCardNum,'msppDevLastChange':msppDevLastChange,'msppDevUpTime':msppDevUpTime,'msppDevTime':msppDevTime,'msppDevFlushMac':msppDevFlushMac,'msppDevReboot':msppDevReboot,'msppDevCfgFile':msppDevCfgFile,'msppDevCfgAction':msppDevCfgAction,'msppDevOsFile':msppDevOsFile,'msppDevOsAction':msppDevOsAction,'msppDevVer':msppDevVer,'msppDevErrorBits':msppDevErrorBits,'msppDevTemperatureLThreshold':msppDevTemperatureLThreshold,'msppDevTemperatureHThreshold':msppDevTemperatureHThreshold,'msppDevTemperature':msppDevTemperature,'msppDevTemperatureTrapEnable':msppDevTemperatureTrapEnable,'msppDevWRED':msppDevWRED,'msppDevMirrorToPort':msppDevMirrorToPort,'msppDevMirrorMode':msppDevMirrorMode,'msppDevLcd':msppDevLcd,'msppDevTDMVlan':msppDevTDMVlan,'msppDevFtpd':msppDevFtpd,'msppDevTelnetd':msppDevTelnetd,'msppDevMirrorToRspanVid':msppDevMirrorToRspanVid,'msppDevMirrorToTpid':msppDevMirrorToTpid,'msppRebootFileMode':msppRebootFileMode,'msppFileExecMode':msppFileExecMode,'msppUpgradeBkOs':msppUpgradeBkOs,'msppInbandIp':msppInbandIp,'msppOutbandIp':msppOutbandIp,'resetEraseCfg':resetEraseCfg,'msppDevLicenseEnable':msppDevLicenseEnable,'msppDevLicenseKey':msppDevLicenseKey,'msppDevSerialNum':msppDevSerialNum,'msppDevMtu':msppDevMtu,'msppDevFlushDynamicArp':msppDevFlushDynamicArp,'msppDevFlushStaticArp':msppDevFlushStaticArp,'msppDevFlushAllArp':msppDevFlushAllArp,'msppDevBootOs':msppDevBootOs,'msppDevBootCfg':msppDevBootCfg,'msppl2HashMode':msppl2HashMode,'msppl3HashMode':msppl3HashMode,'msppl2AuxHashMode':msppl2AuxHashMode,'msppIpv4AddrNum':msppIpv4AddrNum,'msppDevCode':msppDevCode,'msppCmuState':msppCmuState,'msppDevTpid':msppDevTpid,_S:msppDevLoggingInfo,'loggingTrapObjects':loggingTrapObjects,'loggingTrap':loggingTrap,'msppDevFileName':msppDevFileName,'msppDevFileAction':msppDevFileAction,'msppShareVlanEn':msppShareVlanEn,'msppUpgradeStatus':msppUpgradeStatus,'msppCliVersion':msppCliVersion,'msppSnmpVersion':msppSnmpVersion,'msppHttpVersion':msppHttpVersion})