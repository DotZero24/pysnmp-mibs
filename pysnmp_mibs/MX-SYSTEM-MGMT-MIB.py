_J='sysMgmtGroupVer1'
_I='sysSerialNumber'
_H='sysMibVersion'
_G='sysSoftwareVersion'
_F='sysHardwareVersion'
_E='sysMacAddress'
_D='read-only'
_C='OctetString'
_B='MX-SYSTEM-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixMgmt,=mibBuilder.importSymbols('MX-SMI','mediatrixMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sysMgmtMIB=ModuleIdentity((1,3,6,1,4,1,4935,10,15))
if mibBuilder.loadTexts:sysMgmtMIB.setRevisions(('2010-03-01 00:00','1901-08-29 00:00'))
_SysMgmtMIBObjects_ObjectIdentity=ObjectIdentity
sysMgmtMIBObjects=_SysMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,10,15,1))
class _SysMacAddress_Type(OctetString):defaultValue=OctetString(' ');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_SysMacAddress_Type.__name__=_C
_SysMacAddress_Object=MibScalar
sysMacAddress=_SysMacAddress_Object((1,3,6,1,4,1,4935,10,15,1,1),_SysMacAddress_Type())
sysMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:sysMacAddress.setStatus(_A)
class _SysHardwareVersion_Type(OctetString):defaultValue=OctetString(' ');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SysHardwareVersion_Type.__name__=_C
_SysHardwareVersion_Object=MibScalar
sysHardwareVersion=_SysHardwareVersion_Object((1,3,6,1,4,1,4935,10,15,1,2),_SysHardwareVersion_Type())
sysHardwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:sysHardwareVersion.setStatus(_A)
class _SysSoftwareVersion_Type(OctetString):defaultValue=OctetString(' ');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SysSoftwareVersion_Type.__name__=_C
_SysSoftwareVersion_Object=MibScalar
sysSoftwareVersion=_SysSoftwareVersion_Object((1,3,6,1,4,1,4935,10,15,1,3),_SysSoftwareVersion_Type())
sysSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSoftwareVersion.setStatus(_A)
class _SysMibVersion_Type(OctetString):defaultValue=OctetString(' ');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SysMibVersion_Type.__name__=_C
_SysMibVersion_Object=MibScalar
sysMibVersion=_SysMibVersion_Object((1,3,6,1,4,1,4935,10,15,1,4),_SysMibVersion_Type())
sysMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:sysMibVersion.setStatus(_A)
class _SysSerialNumber_Type(OctetString):defaultValue=OctetString(' ');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_SysSerialNumber_Type.__name__=_C
_SysSerialNumber_Object=MibScalar
sysSerialNumber=_SysSerialNumber_Object((1,3,6,1,4,1,4935,10,15,1,5),_SysSerialNumber_Type())
sysSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSerialNumber.setStatus(_A)
_SysMgmtConformance_ObjectIdentity=ObjectIdentity
sysMgmtConformance=_SysMgmtConformance_ObjectIdentity((1,3,6,1,4,1,4935,10,15,2))
_SysMgmtCompliances_ObjectIdentity=ObjectIdentity
sysMgmtCompliances=_SysMgmtCompliances_ObjectIdentity((1,3,6,1,4,1,4935,10,15,2,1))
_SysMgmtGroups_ObjectIdentity=ObjectIdentity
sysMgmtGroups=_SysMgmtGroups_ObjectIdentity((1,3,6,1,4,1,4935,10,15,2,2))
sysMgmtGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,10,15,2,2,1))
sysMgmtGroupVer1.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:sysMgmtGroupVer1.setStatus(_A)
sysMgmtComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,10,15,2,1,1))
sysMgmtComplVer1.setObjects((_B,_J))
if mibBuilder.loadTexts:sysMgmtComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sysMgmtMIB':sysMgmtMIB,'sysMgmtMIBObjects':sysMgmtMIBObjects,_E:sysMacAddress,_F:sysHardwareVersion,_G:sysSoftwareVersion,_H:sysMibVersion,_I:sysSerialNumber,'sysMgmtConformance':sysMgmtConformance,'sysMgmtCompliances':sysMgmtCompliances,'sysMgmtComplVer1':sysMgmtComplVer1,'sysMgmtGroups':sysMgmtGroups,_J:sysMgmtGroupVer1})