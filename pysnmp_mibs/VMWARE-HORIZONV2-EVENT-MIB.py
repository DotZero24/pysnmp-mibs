_F='vmwHorizonv2ObjectGroup'
_E='vmwHorizonv2NotificationGroup'
_D='vmwHorizonv2LicenseEventTrap'
_C='vmwHorizonv2LicenseFailureStatus'
_B='current'
_A='VMWARE-HORIZONV2-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwHorizonv2,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwHorizonv2')
vmwHorizonv2MIB=ModuleIdentity((1,3,6,1,4,1,6876,150,1))
if mibBuilder.loadTexts:vmwHorizonv2MIB.setRevisions(('2023-07-28 00:00',))
_VmwHorizonv2Notifications_ObjectIdentity=ObjectIdentity
vmwHorizonv2Notifications=_VmwHorizonv2Notifications_ObjectIdentity((1,3,6,1,4,1,6876,150,0))
_VmwHorizonv2MIBConformance_ObjectIdentity=ObjectIdentity
vmwHorizonv2MIBConformance=_VmwHorizonv2MIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,150,1,1))
_VmwHorizonv2MIBCompliances_ObjectIdentity=ObjectIdentity
vmwHorizonv2MIBCompliances=_VmwHorizonv2MIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,150,1,1,1))
_VmwHorizonv2MIBGroups_ObjectIdentity=ObjectIdentity
vmwHorizonv2MIBGroups=_VmwHorizonv2MIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,150,1,1,2))
_VmwHorizonv2LicenseEvents_ObjectIdentity=ObjectIdentity
vmwHorizonv2LicenseEvents=_VmwHorizonv2LicenseEvents_ObjectIdentity((1,3,6,1,4,1,6876,150,5))
_VmwHorizonv2LicenseFailureStatus_Type=SnmpAdminString
_VmwHorizonv2LicenseFailureStatus_Object=MibScalar
vmwHorizonv2LicenseFailureStatus=_VmwHorizonv2LicenseFailureStatus_Object((1,3,6,1,4,1,6876,150,5,1),_VmwHorizonv2LicenseFailureStatus_Type())
vmwHorizonv2LicenseFailureStatus.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:vmwHorizonv2LicenseFailureStatus.setStatus(_B)
vmwHorizonv2ObjectGroup=ObjectGroup((1,3,6,1,4,1,6876,150,1,1,2,1))
vmwHorizonv2ObjectGroup.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwHorizonv2ObjectGroup.setStatus(_B)
vmwHorizonv2LicenseEventTrap=NotificationType((1,3,6,1,4,1,6876,150,0,2))
vmwHorizonv2LicenseEventTrap.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwHorizonv2LicenseEventTrap.setStatus(_B)
vmwHorizonv2NotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,150,1,1,2,2))
vmwHorizonv2NotificationGroup.setObjects((_A,_D))
if mibBuilder.loadTexts:vmwHorizonv2NotificationGroup.setStatus(_B)
vmwHorizonv2MIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,150,1,1,1,1))
vmwHorizonv2MIBBasicCompliance.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:vmwHorizonv2MIBBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwHorizonv2Notifications':vmwHorizonv2Notifications,_D:vmwHorizonv2LicenseEventTrap,'vmwHorizonv2MIB':vmwHorizonv2MIB,'vmwHorizonv2MIBConformance':vmwHorizonv2MIBConformance,'vmwHorizonv2MIBCompliances':vmwHorizonv2MIBCompliances,'vmwHorizonv2MIBBasicCompliance':vmwHorizonv2MIBBasicCompliance,'vmwHorizonv2MIBGroups':vmwHorizonv2MIBGroups,_F:vmwHorizonv2ObjectGroup,_E:vmwHorizonv2NotificationGroup,'vmwHorizonv2LicenseEvents':vmwHorizonv2LicenseEvents,_C:vmwHorizonv2LicenseFailureStatus})