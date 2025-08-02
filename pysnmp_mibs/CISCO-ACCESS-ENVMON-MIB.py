_K='caemGroup'
_J='caemSupplyFailedComponent'
_I='caemSupplyStatusEntry'
_H='Integer32'
_G='ciscoEnvMonVoltageStatusDescr'
_F='ciscoEnvMonVoltageState'
_E='ciscoEnvMonTemperatureStatusDescr'
_D='ciscoEnvMonTemperatureState'
_C='CISCO-ACCESS-ENVMON-MIB'
_B='CISCO-ENVMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoEnvMonSupplyStatusEntry,ciscoEnvMonTemperatureState,ciscoEnvMonTemperatureStatusDescr,ciscoEnvMonVoltageState,ciscoEnvMonVoltageStatusDescr=mibBuilder.importSymbols(_B,'ciscoEnvMonSupplyStatusEntry',_D,_E,_F,_G)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAccessEnvMonMIB=ModuleIdentity((1,3,6,1,4,1,9,9,61))
if mibBuilder.loadTexts:ciscoAccessEnvMonMIB.setRevisions(('1998-08-05 00:00',))
_CaemObjects_ObjectIdentity=ObjectIdentity
caemObjects=_CaemObjects_ObjectIdentity((1,3,6,1,4,1,9,9,61,1))
_CaemSupplyStatusTable_Object=MibTable
caemSupplyStatusTable=_CaemSupplyStatusTable_Object((1,3,6,1,4,1,9,9,61,1,1))
if mibBuilder.loadTexts:caemSupplyStatusTable.setStatus(_A)
_CaemSupplyStatusEntry_Object=MibTableRow
caemSupplyStatusEntry=_CaemSupplyStatusEntry_Object((1,3,6,1,4,1,9,9,61,1,1,1))
if mibBuilder.loadTexts:caemSupplyStatusEntry.setStatus(_A)
class _CaemSupplyFailedComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('inputVoltage',2),('dcOutputVoltage',3),('thermal',4),('multiple',5),('fan',6),('overvoltage',7)))
_CaemSupplyFailedComponent_Type.__name__=_H
_CaemSupplyFailedComponent_Object=MibTableColumn
caemSupplyFailedComponent=_CaemSupplyFailedComponent_Object((1,3,6,1,4,1,9,9,61,1,1,1,1),_CaemSupplyFailedComponent_Type())
caemSupplyFailedComponent.setMaxAccess('read-only')
if mibBuilder.loadTexts:caemSupplyFailedComponent.setStatus(_A)
_CaemMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
caemMIBNotificationPrefix=_CaemMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,61,2))
_CaemMIBNotifications_ObjectIdentity=ObjectIdentity
caemMIBNotifications=_CaemMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,61,2,0))
_CaemConformance_ObjectIdentity=ObjectIdentity
caemConformance=_CaemConformance_ObjectIdentity((1,3,6,1,4,1,9,9,61,3))
_CaemCompliances_ObjectIdentity=ObjectIdentity
caemCompliances=_CaemCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,61,3,1))
_CaemGroups_ObjectIdentity=ObjectIdentity
caemGroups=_CaemGroups_ObjectIdentity((1,3,6,1,4,1,9,9,61,3,2))
ciscoEnvMonSupplyStatusEntry.registerAugmentions((_C,_I))
caemSupplyStatusEntry.setIndexNames(*ciscoEnvMonSupplyStatusEntry.getIndexNames())
caemGroup=ObjectGroup((1,3,6,1,4,1,9,9,61,3,2,1))
caemGroup.setObjects((_C,_J))
if mibBuilder.loadTexts:caemGroup.setStatus(_A)
caemTemperatureNotification=NotificationType((1,3,6,1,4,1,9,9,61,2,0,1))
caemTemperatureNotification.setObjects(*((_B,_E),(_B,_D)))
if mibBuilder.loadTexts:caemTemperatureNotification.setStatus(_A)
caemVoltageNotification=NotificationType((1,3,6,1,4,1,9,9,61,2,0,2))
caemVoltageNotification.setObjects(*((_B,_G),(_B,_F)))
if mibBuilder.loadTexts:caemVoltageNotification.setStatus(_A)
caemCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,61,3,1,1))
caemCompliance.setObjects((_C,_K))
if mibBuilder.loadTexts:caemCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ciscoAccessEnvMonMIB':ciscoAccessEnvMonMIB,'caemObjects':caemObjects,'caemSupplyStatusTable':caemSupplyStatusTable,_I:caemSupplyStatusEntry,_J:caemSupplyFailedComponent,'caemMIBNotificationPrefix':caemMIBNotificationPrefix,'caemMIBNotifications':caemMIBNotifications,'caemTemperatureNotification':caemTemperatureNotification,'caemVoltageNotification':caemVoltageNotification,'caemConformance':caemConformance,'caemCompliances':caemCompliances,'caemCompliance':caemCompliance,'caemGroups':caemGroups,_K:caemGroup})