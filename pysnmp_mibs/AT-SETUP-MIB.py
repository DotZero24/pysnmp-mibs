_E='Integer32'
_D='TruthValue'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
setup=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,500))
if mibBuilder.loadTexts:setup.setRevisions(('2008-10-02 00:00','2008-09-30 00:00','2008-09-24 00:00','2008-05-21 00:00'))
class _RestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_RestartDevice_Type.__name__=_E
_RestartDevice_Object=MibScalar
restartDevice=_RestartDevice_Object((1,3,6,1,4,1,207,8,4,4,4,500,1),_RestartDevice_Type())
restartDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:restartDevice.setStatus(_A)
_Firmware_ObjectIdentity=ObjectIdentity
firmware=_Firmware_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,2))
_CurrentFirmware_ObjectIdentity=ObjectIdentity
currentFirmware=_CurrentFirmware_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,2,1))
_CurrSoftVersion_Type=DisplayString
_CurrSoftVersion_Object=MibScalar
currSoftVersion=_CurrSoftVersion_Object((1,3,6,1,4,1,207,8,4,4,4,500,2,1,1),_CurrSoftVersion_Type())
currSoftVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:currSoftVersion.setStatus(_A)
_CurrSoftName_Type=DisplayString
_CurrSoftName_Object=MibScalar
currSoftName=_CurrSoftName_Object((1,3,6,1,4,1,207,8,4,4,4,500,2,1,2),_CurrSoftName_Type())
currSoftName.setMaxAccess(_B)
if mibBuilder.loadTexts:currSoftName.setStatus(_A)
_CurrSoftSaveAs_Type=DisplayString
_CurrSoftSaveAs_Object=MibScalar
currSoftSaveAs=_CurrSoftSaveAs_Object((1,3,6,1,4,1,207,8,4,4,4,500,2,1,3),_CurrSoftSaveAs_Type())
currSoftSaveAs.setMaxAccess(_C)
if mibBuilder.loadTexts:currSoftSaveAs.setStatus(_A)
_NextBootFirmware_ObjectIdentity=ObjectIdentity
nextBootFirmware=_NextBootFirmware_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,2,2))
_NextBootVersion_Type=DisplayString
_NextBootVersion_Object=MibScalar
nextBootVersion=_NextBootVersion_Object((1,3,6,1,4,1,207,8,4,4,4,500,2,2,1),_NextBootVersion_Type())
nextBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nextBootVersion.setStatus(_A)
_NextBootPath_Type=DisplayString
_NextBootPath_Object=MibScalar
nextBootPath=_NextBootPath_Object((1,3,6,1,4,1,207,8,4,4,4,500,2,2,2),_NextBootPath_Type())
nextBootPath.setMaxAccess(_C)
if mibBuilder.loadTexts:nextBootPath.setStatus(_A)
_BackupFirmware_ObjectIdentity=ObjectIdentity
backupFirmware=_BackupFirmware_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,2,3))
_BackupVersion_Type=DisplayString
_BackupVersion_Object=MibScalar
backupVersion=_BackupVersion_Object((1,3,6,1,4,1,207,8,4,4,4,500,2,3,1),_BackupVersion_Type())
backupVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:backupVersion.setStatus(_A)
_BackupPath_Type=DisplayString
_BackupPath_Object=MibScalar
backupPath=_BackupPath_Object((1,3,6,1,4,1,207,8,4,4,4,500,2,3,2),_BackupPath_Type())
backupPath.setMaxAccess(_C)
if mibBuilder.loadTexts:backupPath.setStatus(_A)
_DeviceConfiguration_ObjectIdentity=ObjectIdentity
deviceConfiguration=_DeviceConfiguration_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,3))
_RunningConfig_ObjectIdentity=ObjectIdentity
runningConfig=_RunningConfig_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,3,1))
_RunCnfgSaveAs_Type=DisplayString
_RunCnfgSaveAs_Object=MibScalar
runCnfgSaveAs=_RunCnfgSaveAs_Object((1,3,6,1,4,1,207,8,4,4,4,500,3,1,1),_RunCnfgSaveAs_Type())
runCnfgSaveAs.setMaxAccess(_C)
if mibBuilder.loadTexts:runCnfgSaveAs.setStatus(_A)
_NextBootConfig_ObjectIdentity=ObjectIdentity
nextBootConfig=_NextBootConfig_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,3,2))
_BootCnfgPath_Type=DisplayString
_BootCnfgPath_Object=MibScalar
bootCnfgPath=_BootCnfgPath_Object((1,3,6,1,4,1,207,8,4,4,4,500,3,2,1),_BootCnfgPath_Type())
bootCnfgPath.setMaxAccess(_C)
if mibBuilder.loadTexts:bootCnfgPath.setStatus(_A)
class _BootCnfgExists_Type(TruthValue):subtypeSpec=TruthValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_BootCnfgExists_Type.__name__=_D
_BootCnfgExists_Object=MibScalar
bootCnfgExists=_BootCnfgExists_Object((1,3,6,1,4,1,207,8,4,4,4,500,3,2,2),_BootCnfgExists_Type())
bootCnfgExists.setMaxAccess(_B)
if mibBuilder.loadTexts:bootCnfgExists.setStatus(_A)
_DefaultConfig_ObjectIdentity=ObjectIdentity
defaultConfig=_DefaultConfig_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,3,3))
_DfltCnfgPath_Type=DisplayString
_DfltCnfgPath_Object=MibScalar
dfltCnfgPath=_DfltCnfgPath_Object((1,3,6,1,4,1,207,8,4,4,4,500,3,3,1),_DfltCnfgPath_Type())
dfltCnfgPath.setMaxAccess(_B)
if mibBuilder.loadTexts:dfltCnfgPath.setStatus(_A)
class _DfltCnfgExists_Type(TruthValue):subtypeSpec=TruthValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DfltCnfgExists_Type.__name__=_D
_DfltCnfgExists_Object=MibScalar
dfltCnfgExists=_DfltCnfgExists_Object((1,3,6,1,4,1,207,8,4,4,4,500,3,3,2),_DfltCnfgExists_Type())
dfltCnfgExists.setMaxAccess(_B)
if mibBuilder.loadTexts:dfltCnfgExists.setStatus(_A)
_ServiceConfig_ObjectIdentity=ObjectIdentity
serviceConfig=_ServiceConfig_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,5))
_SrvcTelnetEnable_Type=TruthValue
_SrvcTelnetEnable_Object=MibScalar
srvcTelnetEnable=_SrvcTelnetEnable_Object((1,3,6,1,4,1,207,8,4,4,4,500,5,1),_SrvcTelnetEnable_Type())
srvcTelnetEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:srvcTelnetEnable.setStatus(_A)
_SrvcSshEnable_Type=TruthValue
_SrvcSshEnable_Object=MibScalar
srvcSshEnable=_SrvcSshEnable_Object((1,3,6,1,4,1,207,8,4,4,4,500,5,2),_SrvcSshEnable_Type())
srvcSshEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:srvcSshEnable.setStatus(_A)
_GuiConfig_ObjectIdentity=ObjectIdentity
guiConfig=_GuiConfig_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,6))
_GuiAppletConfig_ObjectIdentity=ObjectIdentity
guiAppletConfig=_GuiAppletConfig_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,500,6,1))
_GuiAppletSysSwVer_Type=DisplayString
_GuiAppletSysSwVer_Object=MibScalar
guiAppletSysSwVer=_GuiAppletSysSwVer_Object((1,3,6,1,4,1,207,8,4,4,4,500,6,1,1),_GuiAppletSysSwVer_Type())
guiAppletSysSwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:guiAppletSysSwVer.setStatus(_A)
_GuiAppletSwVer_Type=DisplayString
_GuiAppletSwVer_Object=MibScalar
guiAppletSwVer=_GuiAppletSwVer_Object((1,3,6,1,4,1,207,8,4,4,4,500,6,1,2),_GuiAppletSwVer_Type())
guiAppletSwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:guiAppletSwVer.setStatus(_A)
mibBuilder.exportSymbols('AT-SETUP-MIB',**{'setup':setup,'restartDevice':restartDevice,'firmware':firmware,'currentFirmware':currentFirmware,'currSoftVersion':currSoftVersion,'currSoftName':currSoftName,'currSoftSaveAs':currSoftSaveAs,'nextBootFirmware':nextBootFirmware,'nextBootVersion':nextBootVersion,'nextBootPath':nextBootPath,'backupFirmware':backupFirmware,'backupVersion':backupVersion,'backupPath':backupPath,'deviceConfiguration':deviceConfiguration,'runningConfig':runningConfig,'runCnfgSaveAs':runCnfgSaveAs,'nextBootConfig':nextBootConfig,'bootCnfgPath':bootCnfgPath,'bootCnfgExists':bootCnfgExists,'defaultConfig':defaultConfig,'dfltCnfgPath':dfltCnfgPath,'dfltCnfgExists':dfltCnfgExists,'serviceConfig':serviceConfig,'srvcTelnetEnable':srvcTelnetEnable,'srvcSshEnable':srvcSshEnable,'guiConfig':guiConfig,'guiAppletConfig':guiAppletConfig,'guiAppletSysSwVer':guiAppletSysSwVer,'guiAppletSwVer':guiAppletSwVer})