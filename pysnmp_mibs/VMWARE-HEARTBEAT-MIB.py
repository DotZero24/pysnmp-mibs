_F='vmwHbHeartbeat'
_E='sysUpTime'
_D='SNMPv2-MIB'
_C='vmwHbNotificationGroup'
_B='current'
_A='VMWARE-HEARTBEAT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysUpTime,=mibBuilder.importSymbols(_D,_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwProductSpecific,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwProductSpecific')
vmwHBMIB=ModuleIdentity((1,3,6,1,4,1,6876,4,190,66))
if mibBuilder.loadTexts:vmwHBMIB.setRevisions(('2016-02-10 00:00',))
_VmwHb_ObjectIdentity=ObjectIdentity
vmwHb=_VmwHb_ObjectIdentity((1,3,6,1,4,1,6876,4,190))
_VmwHbNotifications_ObjectIdentity=ObjectIdentity
vmwHbNotifications=_VmwHbNotifications_ObjectIdentity((1,3,6,1,4,1,6876,4,190,0))
_VmwHbMIBConformance_ObjectIdentity=ObjectIdentity
vmwHbMIBConformance=_VmwHbMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,4,190,2))
_VmwHbMIBCompliances_ObjectIdentity=ObjectIdentity
vmwHbMIBCompliances=_VmwHbMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,4,190,2,1))
_VmwHbMIBGroups_ObjectIdentity=ObjectIdentity
vmwHbMIBGroups=_VmwHbMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,4,190,2,2))
vmwHbHeartbeat=NotificationType((1,3,6,1,4,1,6876,4,190,0,401))
vmwHbHeartbeat.setObjects((_D,_E))
if mibBuilder.loadTexts:vmwHbHeartbeat.setStatus(_B)
vmwHbNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,4,190,2,2,2))
vmwHbNotificationGroup.setObjects((_A,_F))
if mibBuilder.loadTexts:vmwHbNotificationGroup.setStatus(_B)
vmwHbMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,4,190,2,1,4))
vmwHbMIBBasicCompliance.setObjects(*((_A,_C),(_A,_C)))
if mibBuilder.loadTexts:vmwHbMIBBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwHb':vmwHb,'vmwHbNotifications':vmwHbNotifications,_F:vmwHbHeartbeat,'vmwHbMIBConformance':vmwHbMIBConformance,'vmwHbMIBCompliances':vmwHbMIBCompliances,'vmwHbMIBBasicCompliance':vmwHbMIBBasicCompliance,'vmwHbMIBGroups':vmwHbMIBGroups,_C:vmwHbNotificationGroup,'vmwHBMIB':vmwHBMIB})