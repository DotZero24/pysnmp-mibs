_R='aristaEntSensorNotificationsGroup'
_Q='aristaEntSensorThresholdGroup'
_P='aristaEntSensorAlarm'
_O='aristaEntSensorStatusDescr'
_N='aristaEntSensorThresholdHighCritical'
_M='aristaEntSensorThresholdHighWarning'
_L='aristaEntSensorThresholdLowCritical'
_K='aristaEntSensorThresholdLowWarning'
_J='entStateAlarm'
_I='ENTITY-STATE-MIB'
_H='entPhySensorValue'
_G='ENTITY-SENSOR-MIB'
_F='entPhysicalIndex'
_E='entPhysicalDescr'
_D='ENTITY-MIB'
_C='read-only'
_B='ARISTA-ENTITY-SENSOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
entPhysicalDescr,entPhysicalIndex=mibBuilder.importSymbols(_D,_E,_F)
EntitySensorValue,entPhySensorValue=mibBuilder.importSymbols(_G,'EntitySensorValue',_H)
entStateAlarm,=mibBuilder.importSymbols(_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaEntSensorMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,12))
if mibBuilder.loadTexts:aristaEntSensorMIB.setRevisions(('2014-08-15 00:00','2013-05-09 09:50'))
_AristaEntSensorMibNotifications_ObjectIdentity=ObjectIdentity
aristaEntSensorMibNotifications=_AristaEntSensorMibNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,12,0))
_AristaEntSensorMibObjects_ObjectIdentity=ObjectIdentity
aristaEntSensorMibObjects=_AristaEntSensorMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,12,1))
_AristaEntSensorThresholdTable_Object=MibTable
aristaEntSensorThresholdTable=_AristaEntSensorThresholdTable_Object((1,3,6,1,4,1,30065,3,12,1,1))
if mibBuilder.loadTexts:aristaEntSensorThresholdTable.setStatus(_A)
_AristaEntSensorThresholdEntry_Object=MibTableRow
aristaEntSensorThresholdEntry=_AristaEntSensorThresholdEntry_Object((1,3,6,1,4,1,30065,3,12,1,1,1))
aristaEntSensorThresholdEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:aristaEntSensorThresholdEntry.setStatus(_A)
_AristaEntSensorThresholdLowWarning_Type=EntitySensorValue
_AristaEntSensorThresholdLowWarning_Object=MibTableColumn
aristaEntSensorThresholdLowWarning=_AristaEntSensorThresholdLowWarning_Object((1,3,6,1,4,1,30065,3,12,1,1,1,1),_AristaEntSensorThresholdLowWarning_Type())
aristaEntSensorThresholdLowWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEntSensorThresholdLowWarning.setStatus(_A)
_AristaEntSensorThresholdLowCritical_Type=EntitySensorValue
_AristaEntSensorThresholdLowCritical_Object=MibTableColumn
aristaEntSensorThresholdLowCritical=_AristaEntSensorThresholdLowCritical_Object((1,3,6,1,4,1,30065,3,12,1,1,1,2),_AristaEntSensorThresholdLowCritical_Type())
aristaEntSensorThresholdLowCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEntSensorThresholdLowCritical.setStatus(_A)
_AristaEntSensorThresholdHighWarning_Type=EntitySensorValue
_AristaEntSensorThresholdHighWarning_Object=MibTableColumn
aristaEntSensorThresholdHighWarning=_AristaEntSensorThresholdHighWarning_Object((1,3,6,1,4,1,30065,3,12,1,1,1,3),_AristaEntSensorThresholdHighWarning_Type())
aristaEntSensorThresholdHighWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEntSensorThresholdHighWarning.setStatus(_A)
_AristaEntSensorThresholdHighCritical_Type=EntitySensorValue
_AristaEntSensorThresholdHighCritical_Object=MibTableColumn
aristaEntSensorThresholdHighCritical=_AristaEntSensorThresholdHighCritical_Object((1,3,6,1,4,1,30065,3,12,1,1,1,4),_AristaEntSensorThresholdHighCritical_Type())
aristaEntSensorThresholdHighCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEntSensorThresholdHighCritical.setStatus(_A)
_AristaEntSensorStatusDescr_Type=SnmpAdminString
_AristaEntSensorStatusDescr_Object=MibTableColumn
aristaEntSensorStatusDescr=_AristaEntSensorStatusDescr_Object((1,3,6,1,4,1,30065,3,12,1,1,1,5),_AristaEntSensorStatusDescr_Type())
aristaEntSensorStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEntSensorStatusDescr.setStatus(_A)
_AristaEntSensorMibConformance_ObjectIdentity=ObjectIdentity
aristaEntSensorMibConformance=_AristaEntSensorMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,12,2))
_AristaEntSensorMibCompliances_ObjectIdentity=ObjectIdentity
aristaEntSensorMibCompliances=_AristaEntSensorMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,12,2,1))
_AristaEntSensorMibGroups_ObjectIdentity=ObjectIdentity
aristaEntSensorMibGroups=_AristaEntSensorMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,12,2,2))
aristaEntSensorThresholdGroup=ObjectGroup((1,3,6,1,4,1,30065,3,12,2,2,1))
aristaEntSensorThresholdGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:aristaEntSensorThresholdGroup.setStatus(_A)
aristaEntSensorAlarm=NotificationType((1,3,6,1,4,1,30065,3,12,0,1))
aristaEntSensorAlarm.setObjects(*((_D,_E),(_G,_H),(_I,_J)))
if mibBuilder.loadTexts:aristaEntSensorAlarm.setStatus(_A)
aristaEntSensorNotificationsGroup=NotificationGroup((1,3,6,1,4,1,30065,3,12,2,2,2))
aristaEntSensorNotificationsGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:aristaEntSensorNotificationsGroup.setStatus(_A)
aristaEntSensorMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,12,2,1,1))
aristaEntSensorMibCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:aristaEntSensorMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaEntSensorMIB':aristaEntSensorMIB,'aristaEntSensorMibNotifications':aristaEntSensorMibNotifications,_P:aristaEntSensorAlarm,'aristaEntSensorMibObjects':aristaEntSensorMibObjects,'aristaEntSensorThresholdTable':aristaEntSensorThresholdTable,'aristaEntSensorThresholdEntry':aristaEntSensorThresholdEntry,_K:aristaEntSensorThresholdLowWarning,_L:aristaEntSensorThresholdLowCritical,_M:aristaEntSensorThresholdHighWarning,_N:aristaEntSensorThresholdHighCritical,_O:aristaEntSensorStatusDescr,'aristaEntSensorMibConformance':aristaEntSensorMibConformance,'aristaEntSensorMibCompliances':aristaEntSensorMibCompliances,'aristaEntSensorMibCompliance':aristaEntSensorMibCompliance,'aristaEntSensorMibGroups':aristaEntSensorMibGroups,_Q:aristaEntSensorThresholdGroup,_R:aristaEntSensorNotificationsGroup})