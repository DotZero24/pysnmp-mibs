_O='ciscoSibuFlashMIBGroup'
_N='csfUpgradeFirmwareStatus'
_M='csfUpgradeFlashMode'
_L='csfUpgradeTFTPInitiate'
_K='csfUpgradeTFTPLoadFilename'
_J='csfUpgradeTFTPServerAddress'
_I='csfUpgradeFlashSize'
_H='csfUpgradeFirmwareVersion'
_G='IpAddress'
_F='read-only'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='CISCO-SIBU-FLASH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_G,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ciscoSibuFlashMIB=ModuleIdentity((1,3,6,1,4,1,9,10,45))
if mibBuilder.loadTexts:ciscoSibuFlashMIB.setRevisions(('1998-10-23 00:00',))
_CiscoSibuFlashMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSibuFlashMIBObjects=_CiscoSibuFlashMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,45,1))
_CsfUpgrade_ObjectIdentity=ObjectIdentity
csfUpgrade=_CsfUpgrade_ObjectIdentity((1,3,6,1,4,1,9,10,45,1,1))
class _CsfUpgradeFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CsfUpgradeFirmwareVersion_Type.__name__=_E
_CsfUpgradeFirmwareVersion_Object=MibScalar
csfUpgradeFirmwareVersion=_CsfUpgradeFirmwareVersion_Object((1,3,6,1,4,1,9,10,45,1,1,1),_CsfUpgradeFirmwareVersion_Type())
csfUpgradeFirmwareVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:csfUpgradeFirmwareVersion.setStatus(_A)
class _CsfUpgradeFlashSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CsfUpgradeFlashSize_Type.__name__=_C
_CsfUpgradeFlashSize_Object=MibScalar
csfUpgradeFlashSize=_CsfUpgradeFlashSize_Object((1,3,6,1,4,1,9,10,45,1,1,2),_CsfUpgradeFlashSize_Type())
csfUpgradeFlashSize.setMaxAccess(_F)
if mibBuilder.loadTexts:csfUpgradeFlashSize.setStatus(_A)
if mibBuilder.loadTexts:csfUpgradeFlashSize.setUnits('kbytes')
class _CsfUpgradeTFTPServerAddress_Type(IpAddress):defaultHexValue='00000000'
_CsfUpgradeTFTPServerAddress_Type.__name__=_G
_CsfUpgradeTFTPServerAddress_Object=MibScalar
csfUpgradeTFTPServerAddress=_CsfUpgradeTFTPServerAddress_Object((1,3,6,1,4,1,9,10,45,1,1,3),_CsfUpgradeTFTPServerAddress_Type())
csfUpgradeTFTPServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:csfUpgradeTFTPServerAddress.setStatus(_A)
class _CsfUpgradeTFTPLoadFilename_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CsfUpgradeTFTPLoadFilename_Type.__name__=_E
_CsfUpgradeTFTPLoadFilename_Object=MibScalar
csfUpgradeTFTPLoadFilename=_CsfUpgradeTFTPLoadFilename_Object((1,3,6,1,4,1,9,10,45,1,1,4),_CsfUpgradeTFTPLoadFilename_Type())
csfUpgradeTFTPLoadFilename.setMaxAccess(_D)
if mibBuilder.loadTexts:csfUpgradeTFTPLoadFilename.setStatus(_A)
class _CsfUpgradeTFTPInitiate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upgrade',1),('noUpgrade',2)))
_CsfUpgradeTFTPInitiate_Type.__name__=_C
_CsfUpgradeTFTPInitiate_Object=MibScalar
csfUpgradeTFTPInitiate=_CsfUpgradeTFTPInitiate_Object((1,3,6,1,4,1,9,10,45,1,1,5),_CsfUpgradeTFTPInitiate_Type())
csfUpgradeTFTPInitiate.setMaxAccess(_D)
if mibBuilder.loadTexts:csfUpgradeTFTPInitiate.setStatus(_A)
class _CsfUpgradeFlashMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permanent',1),('temporary',2)))
_CsfUpgradeFlashMode_Type.__name__=_C
_CsfUpgradeFlashMode_Object=MibScalar
csfUpgradeFlashMode=_CsfUpgradeFlashMode_Object((1,3,6,1,4,1,9,10,45,1,1,6),_CsfUpgradeFlashMode_Type())
csfUpgradeFlashMode.setMaxAccess(_D)
if mibBuilder.loadTexts:csfUpgradeFlashMode.setStatus(_A)
class _CsfUpgradeFirmwareStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('inProgress',2),('succeeded',3),('failed',4)))
_CsfUpgradeFirmwareStatus_Type.__name__=_C
_CsfUpgradeFirmwareStatus_Object=MibScalar
csfUpgradeFirmwareStatus=_CsfUpgradeFirmwareStatus_Object((1,3,6,1,4,1,9,10,45,1,1,7),_CsfUpgradeFirmwareStatus_Type())
csfUpgradeFirmwareStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:csfUpgradeFirmwareStatus.setStatus(_A)
_CiscoSibuFlashMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoSibuFlashMIBNotificationsPrefix=_CiscoSibuFlashMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,45,2))
_CiscoSibuFlashMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoSibuFlashMIBNotifications=_CiscoSibuFlashMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,45,2,0))
_CiscoSibuFlashMIBComformance_ObjectIdentity=ObjectIdentity
ciscoSibuFlashMIBComformance=_CiscoSibuFlashMIBComformance_ObjectIdentity((1,3,6,1,4,1,9,10,45,3))
_CiscoSibuFlashMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSibuFlashMIBCompliances=_CiscoSibuFlashMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,45,3,1))
_CiscoSibuFlashMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSibuFlashMIBGroups=_CiscoSibuFlashMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,45,3,2))
ciscoSibuFlashMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,45,3,2,1))
ciscoSibuFlashMIBGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoSibuFlashMIBGroup.setStatus(_A)
ciscoSibuFlashCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,45,3,1,1))
ciscoSibuFlashCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoSibuFlashCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSibuFlashMIB':ciscoSibuFlashMIB,'ciscoSibuFlashMIBObjects':ciscoSibuFlashMIBObjects,'csfUpgrade':csfUpgrade,_H:csfUpgradeFirmwareVersion,_I:csfUpgradeFlashSize,_J:csfUpgradeTFTPServerAddress,_K:csfUpgradeTFTPLoadFilename,_L:csfUpgradeTFTPInitiate,_M:csfUpgradeFlashMode,_N:csfUpgradeFirmwareStatus,'ciscoSibuFlashMIBNotificationsPrefix':ciscoSibuFlashMIBNotificationsPrefix,'ciscoSibuFlashMIBNotifications':ciscoSibuFlashMIBNotifications,'ciscoSibuFlashMIBComformance':ciscoSibuFlashMIBComformance,'ciscoSibuFlashMIBCompliances':ciscoSibuFlashMIBCompliances,'ciscoSibuFlashCompliance':ciscoSibuFlashCompliance,'ciscoSibuFlashMIBGroups':ciscoSibuFlashMIBGroups,_O:ciscoSibuFlashMIBGroup})