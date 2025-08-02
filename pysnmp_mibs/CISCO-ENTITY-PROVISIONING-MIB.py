_J='ceProvContainerGroup'
_I='ceProvContainerDetected'
_H='ceProvContainerEquipped'
_G='ceProvContainerStatus'
_F='read-only'
_E='Integer32'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='CISCO-ENTITY-PROVISIONING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention')
ciscoEntityProvMIB=ModuleIdentity((1,3,6,1,4,1,9,9,139))
_CiscoEntityProvMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityProvMIBObjects=_CiscoEntityProvMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,139,1))
_CeProvContainerTable_Object=MibTable
ceProvContainerTable=_CeProvContainerTable_Object((1,3,6,1,4,1,9,9,139,1,1))
if mibBuilder.loadTexts:ceProvContainerTable.setStatus(_A)
_CeProvContainerEntry_Object=MibTableRow
ceProvContainerEntry=_CeProvContainerEntry_Object((1,3,6,1,4,1,9,9,139,1,1,1))
ceProvContainerEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ceProvContainerEntry.setStatus(_A)
class _CeProvContainerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unequipped',1),('provisioned',2),('mismatched',3),('invalid',4),('equipped',5),('failed',6)))
_CeProvContainerStatus_Type.__name__=_E
_CeProvContainerStatus_Object=MibTableColumn
ceProvContainerStatus=_CeProvContainerStatus_Object((1,3,6,1,4,1,9,9,139,1,1,1,1),_CeProvContainerStatus_Type())
ceProvContainerStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ceProvContainerStatus.setStatus(_A)
_CeProvContainerEquipped_Type=AutonomousType
_CeProvContainerEquipped_Object=MibTableColumn
ceProvContainerEquipped=_CeProvContainerEquipped_Object((1,3,6,1,4,1,9,9,139,1,1,1,2),_CeProvContainerEquipped_Type())
ceProvContainerEquipped.setMaxAccess('read-write')
if mibBuilder.loadTexts:ceProvContainerEquipped.setStatus(_A)
_CeProvContainerDetected_Type=AutonomousType
_CeProvContainerDetected_Object=MibTableColumn
ceProvContainerDetected=_CeProvContainerDetected_Object((1,3,6,1,4,1,9,9,139,1,1,1,3),_CeProvContainerDetected_Type())
ceProvContainerDetected.setMaxAccess(_F)
if mibBuilder.loadTexts:ceProvContainerDetected.setStatus(_A)
_CeProvMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ceProvMIBNotificationsPrefix=_CeProvMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,139,2))
_CeProvMIBNotifications_ObjectIdentity=ObjectIdentity
ceProvMIBNotifications=_CeProvMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,139,2,0))
_CeProvMIBConformance_ObjectIdentity=ObjectIdentity
ceProvMIBConformance=_CeProvMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,139,3))
_CeProvMIBCompliances_ObjectIdentity=ObjectIdentity
ceProvMIBCompliances=_CeProvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,139,3,1))
_CeProvMIBGroups_ObjectIdentity=ObjectIdentity
ceProvMIBGroups=_CeProvMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,139,3,2))
ceProvContainerGroup=ObjectGroup((1,3,6,1,4,1,9,9,139,3,2,1))
ceProvContainerGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ceProvContainerGroup.setStatus(_A)
ceProvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,139,3,1,1))
ceProvMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ceProvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoEntityProvMIB':ciscoEntityProvMIB,'ciscoEntityProvMIBObjects':ciscoEntityProvMIBObjects,'ceProvContainerTable':ceProvContainerTable,'ceProvContainerEntry':ceProvContainerEntry,_G:ceProvContainerStatus,_H:ceProvContainerEquipped,_I:ceProvContainerDetected,'ceProvMIBNotificationsPrefix':ceProvMIBNotificationsPrefix,'ceProvMIBNotifications':ceProvMIBNotifications,'ceProvMIBConformance':ceProvMIBConformance,'ceProvMIBCompliances':ceProvMIBCompliances,'ceProvMIBCompliance':ceProvMIBCompliance,'ceProvMIBGroups':ceProvMIBGroups,_J:ceProvContainerGroup})