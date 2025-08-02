if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lexmark,lexmarkModules=mibBuilder.importSymbols('LEXMARK-ROOT-MIB','lexmark','lexmarkModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
settings=ModuleIdentity((1,3,6,1,4,1,641,7))
if mibBuilder.loadTexts:settings.setRevisions(('2014-03-16 12:42',))
_SettingsMIBAdminInfo_ObjectIdentity=ObjectIdentity
settingsMIBAdminInfo=_SettingsMIBAdminInfo_ObjectIdentity((1,3,6,1,4,1,641,7,1))
_SettingsMIBCompliances_ObjectIdentity=ObjectIdentity
settingsMIBCompliances=_SettingsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,641,7,1,1))
_SettingsMIBGroups_ObjectIdentity=ObjectIdentity
settingsMIBGroups=_SettingsMIBGroups_ObjectIdentity((1,3,6,1,4,1,641,7,1,2))
_SettingsControl_ObjectIdentity=ObjectIdentity
settingsControl=_SettingsControl_ObjectIdentity((1,3,6,1,4,1,641,7,2))
_SettingsDefinition_ObjectIdentity=ObjectIdentity
settingsDefinition=_SettingsDefinition_ObjectIdentity((1,3,6,1,4,1,641,7,3))
mibBuilder.exportSymbols('LEXMARK-SETTINGS-MIB',**{'settings':settings,'settingsMIBAdminInfo':settingsMIBAdminInfo,'settingsMIBCompliances':settingsMIBCompliances,'settingsMIBGroups':settingsMIBGroups,'settingsControl':settingsControl,'settingsDefinition':settingsDefinition})