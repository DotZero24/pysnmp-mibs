_F='vmwCimOmHeartbeat'
_E='vmwEnvIndicationTime'
_D='VMWARE-ENV-MIB'
_C='vmwCimOmNotificationGroup'
_B='current'
_A='VMWARE-CIMOM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwEnvIndicationTime,=mibBuilder.importSymbols(_D,_E)
vmwProductSpecific,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwProductSpecific')
vmwCIMOMMIB=ModuleIdentity((1,3,6,1,4,1,6876,4,90,10))
if mibBuilder.loadTexts:vmwCIMOMMIB.setRevisions(('2010-08-20 00:00',))
_VmwCimOm_ObjectIdentity=ObjectIdentity
vmwCimOm=_VmwCimOm_ObjectIdentity((1,3,6,1,4,1,6876,4,90))
_VmwCimOmNotifications_ObjectIdentity=ObjectIdentity
vmwCimOmNotifications=_VmwCimOmNotifications_ObjectIdentity((1,3,6,1,4,1,6876,4,90,0))
_VmwCimOmMIBConformance_ObjectIdentity=ObjectIdentity
vmwCimOmMIBConformance=_VmwCimOmMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,4,90,2))
_VmwCimOmMIBCompliances_ObjectIdentity=ObjectIdentity
vmwCimOmMIBCompliances=_VmwCimOmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,4,90,2,1))
_VmwCimOmMIBGroups_ObjectIdentity=ObjectIdentity
vmwCimOmMIBGroups=_VmwCimOmMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,4,90,2,2))
vmwCimOmHeartbeat=NotificationType((1,3,6,1,4,1,6876,4,90,0,401))
vmwCimOmHeartbeat.setObjects((_D,_E))
if mibBuilder.loadTexts:vmwCimOmHeartbeat.setStatus(_B)
vmwCimOmNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,4,90,2,2,2))
vmwCimOmNotificationGroup.setObjects((_A,_F))
if mibBuilder.loadTexts:vmwCimOmNotificationGroup.setStatus(_B)
vmwCimOmMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,4,90,2,1,4))
vmwCimOmMIBBasicCompliance.setObjects(*((_A,_C),(_A,_C)))
if mibBuilder.loadTexts:vmwCimOmMIBBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwCimOm':vmwCimOm,'vmwCimOmNotifications':vmwCimOmNotifications,_F:vmwCimOmHeartbeat,'vmwCimOmMIBConformance':vmwCimOmMIBConformance,'vmwCimOmMIBCompliances':vmwCimOmMIBCompliances,'vmwCimOmMIBBasicCompliance':vmwCimOmMIBBasicCompliance,'vmwCimOmMIBGroups':vmwCimOmMIBGroups,_C:vmwCimOmNotificationGroup,'vmwCIMOMMIB':vmwCIMOMMIB})