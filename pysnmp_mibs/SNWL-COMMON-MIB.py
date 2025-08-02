_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sonicwallCommon,=mibBuilder.importSymbols('SONICWALL-SMI','sonicwallCommon')
snwlCommonModule=ModuleIdentity((1,3,6,1,4,1,8741,2,1))
if mibBuilder.loadTexts:snwlCommonModule.setRevisions(('2017-01-06 00:00','2007-11-09 00:00'))
_SnwlSys_ObjectIdentity=ObjectIdentity
snwlSys=_SnwlSys_ObjectIdentity((1,3,6,1,4,1,8741,2,1,1))
_SnwlSysModel_Type=DisplayString
_SnwlSysModel_Object=MibScalar
snwlSysModel=_SnwlSysModel_Object((1,3,6,1,4,1,8741,2,1,1,1),_SnwlSysModel_Type())
snwlSysModel.setMaxAccess(_A)
if mibBuilder.loadTexts:snwlSysModel.setStatus(_B)
_SnwlSysSerialNumber_Type=DisplayString
_SnwlSysSerialNumber_Object=MibScalar
snwlSysSerialNumber=_SnwlSysSerialNumber_Object((1,3,6,1,4,1,8741,2,1,1,2),_SnwlSysSerialNumber_Type())
snwlSysSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:snwlSysSerialNumber.setStatus(_B)
_SnwlSysFirmwareVersion_Type=DisplayString
_SnwlSysFirmwareVersion_Object=MibScalar
snwlSysFirmwareVersion=_SnwlSysFirmwareVersion_Object((1,3,6,1,4,1,8741,2,1,1,3),_SnwlSysFirmwareVersion_Type())
snwlSysFirmwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:snwlSysFirmwareVersion.setStatus(_B)
_SnwlSysROMVersion_Type=DisplayString
_SnwlSysROMVersion_Object=MibScalar
snwlSysROMVersion=_SnwlSysROMVersion_Object((1,3,6,1,4,1,8741,2,1,1,4),_SnwlSysROMVersion_Type())
snwlSysROMVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:snwlSysROMVersion.setStatus(_B)
_SnwlSysAssetNumber_Type=DisplayString
_SnwlSysAssetNumber_Object=MibScalar
snwlSysAssetNumber=_SnwlSysAssetNumber_Object((1,3,6,1,4,1,8741,2,1,1,5),_SnwlSysAssetNumber_Type())
snwlSysAssetNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:snwlSysAssetNumber.setStatus(_B)
mibBuilder.exportSymbols('SNWL-COMMON-MIB',**{'snwlCommonModule':snwlCommonModule,'snwlSys':snwlSys,'snwlSysModel':snwlSysModel,'snwlSysSerialNumber':snwlSysSerialNumber,'snwlSysFirmwareVersion':snwlSysFirmwareVersion,'snwlSysROMVersion':snwlSysROMVersion,'snwlSysAssetNumber':snwlSysAssetNumber})