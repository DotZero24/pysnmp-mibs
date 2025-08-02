_O='pdnEntitySensorExtThresholdNtfyGroup'
_N='pdnEntitySensorExtThresholdGroup'
_M='pdnEntPhySensorExtThresholdExceededCleared'
_L='pdnEntPhySensorExtThresholdExceededSet'
_K='pdnEntPhySensorExtLowerThreshold'
_J='pdnEntPhySensorExtUpperThreshold'
_I='pdnEntPhySensorExtNotificationEnable'
_H='pdnEntPhySensorExtEntry'
_G='Integer32'
_F='read-write'
_E='entPhySensorValue'
_D='ENTITY-SENSOR-MIB'
_C='pdnEntPhySensorExtThresholdState'
_B='current'
_A='PDN-ENTITY-SENSOR-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntitySensorValue,entPhySensorEntry,entPhySensorValue=mibBuilder.importSymbols(_D,'EntitySensorValue','entPhySensorEntry',_E)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnEntitySensorExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,45))
if mibBuilder.loadTexts:pdnEntitySensorExtMIB.setRevisions(('2003-06-06 00:00','2003-04-24 00:00','2003-04-16 00:00'))
_PdnEntitySensorExtNotifications_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtNotifications=_PdnEntitySensorExtNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,0))
_PdnEntitySensorExtObjects_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtObjects=_PdnEntitySensorExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,1))
_PdnEntPhySensorExtTable_Object=MibTable
pdnEntPhySensorExtTable=_PdnEntPhySensorExtTable_Object((1,3,6,1,4,1,1795,2,24,2,45,1,1))
if mibBuilder.loadTexts:pdnEntPhySensorExtTable.setStatus(_B)
_PdnEntPhySensorExtEntry_Object=MibTableRow
pdnEntPhySensorExtEntry=_PdnEntPhySensorExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,45,1,1,1))
if mibBuilder.loadTexts:pdnEntPhySensorExtEntry.setStatus(_B)
class _PdnEntPhySensorExtNotificationEnable_Type(Bits):namedValues=NamedValues(('thresholdExceeded',0))
_PdnEntPhySensorExtNotificationEnable_Type.__name__='Bits'
_PdnEntPhySensorExtNotificationEnable_Object=MibTableColumn
pdnEntPhySensorExtNotificationEnable=_PdnEntPhySensorExtNotificationEnable_Object((1,3,6,1,4,1,1795,2,24,2,45,1,1,1,1),_PdnEntPhySensorExtNotificationEnable_Type())
pdnEntPhySensorExtNotificationEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnEntPhySensorExtNotificationEnable.setStatus(_B)
_PdnEntPhySensorExtUpperThreshold_Type=EntitySensorValue
_PdnEntPhySensorExtUpperThreshold_Object=MibTableColumn
pdnEntPhySensorExtUpperThreshold=_PdnEntPhySensorExtUpperThreshold_Object((1,3,6,1,4,1,1795,2,24,2,45,1,1,1,2),_PdnEntPhySensorExtUpperThreshold_Type())
pdnEntPhySensorExtUpperThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnEntPhySensorExtUpperThreshold.setStatus(_B)
_PdnEntPhySensorExtLowerThreshold_Type=EntitySensorValue
_PdnEntPhySensorExtLowerThreshold_Object=MibTableColumn
pdnEntPhySensorExtLowerThreshold=_PdnEntPhySensorExtLowerThreshold_Object((1,3,6,1,4,1,1795,2,24,2,45,1,1,1,3),_PdnEntPhySensorExtLowerThreshold_Type())
pdnEntPhySensorExtLowerThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnEntPhySensorExtLowerThreshold.setStatus(_B)
class _PdnEntPhySensorExtThresholdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noThresholdsExceeded',1),('upperThresholdExceeded',2),('lowerThresholdExceeded',3)))
_PdnEntPhySensorExtThresholdState_Type.__name__=_G
_PdnEntPhySensorExtThresholdState_Object=MibTableColumn
pdnEntPhySensorExtThresholdState=_PdnEntPhySensorExtThresholdState_Object((1,3,6,1,4,1,1795,2,24,2,45,1,1,1,4),_PdnEntPhySensorExtThresholdState_Type())
pdnEntPhySensorExtThresholdState.setMaxAccess('read-only')
if mibBuilder.loadTexts:pdnEntPhySensorExtThresholdState.setStatus(_B)
_PdnEntitySensorExtAFNs_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtAFNs=_PdnEntitySensorExtAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,2))
_PdnEntitySensorExtConformance_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtConformance=_PdnEntitySensorExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,3))
_PdnEntitySensorExtCompliances_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtCompliances=_PdnEntitySensorExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,3,1))
_PdnEntitySensorExtGroups_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtGroups=_PdnEntitySensorExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,3,2))
_PdnEntitySensorExtObjGroups_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtObjGroups=_PdnEntitySensorExtObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,3,2,1))
_PdnEntitySensorExtAfnGroups_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtAfnGroups=_PdnEntitySensorExtAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,3,2,2))
_PdnEntitySensorExtNtfyGroups_ObjectIdentity=ObjectIdentity
pdnEntitySensorExtNtfyGroups=_PdnEntitySensorExtNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,45,3,2,3))
entPhySensorEntry.registerAugmentions((_A,_H))
pdnEntPhySensorExtEntry.setIndexNames(*entPhySensorEntry.getIndexNames())
pdnEntitySensorExtThresholdGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,45,3,2,1,1))
pdnEntitySensorExtThresholdGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:pdnEntitySensorExtThresholdGroup.setStatus(_B)
pdnEntPhySensorExtThresholdExceededSet=NotificationType((1,3,6,1,4,1,1795,2,24,2,45,0,1))
pdnEntPhySensorExtThresholdExceededSet.setObjects(*((_D,_E),(_A,_C)))
if mibBuilder.loadTexts:pdnEntPhySensorExtThresholdExceededSet.setStatus(_B)
pdnEntPhySensorExtThresholdExceededCleared=NotificationType((1,3,6,1,4,1,1795,2,24,2,45,0,100))
pdnEntPhySensorExtThresholdExceededCleared.setObjects(*((_D,_E),(_A,_C)))
if mibBuilder.loadTexts:pdnEntPhySensorExtThresholdExceededCleared.setStatus(_B)
pdnEntitySensorExtThresholdNtfyGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,45,3,2,3,1))
pdnEntitySensorExtThresholdNtfyGroup.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:pdnEntitySensorExtThresholdNtfyGroup.setStatus(_B)
pdnEntitySensorExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,45,3,1,1))
pdnEntitySensorExtMIBCompliance.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:pdnEntitySensorExtMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pdnEntitySensorExtMIB':pdnEntitySensorExtMIB,'pdnEntitySensorExtNotifications':pdnEntitySensorExtNotifications,_L:pdnEntPhySensorExtThresholdExceededSet,_M:pdnEntPhySensorExtThresholdExceededCleared,'pdnEntitySensorExtObjects':pdnEntitySensorExtObjects,'pdnEntPhySensorExtTable':pdnEntPhySensorExtTable,_H:pdnEntPhySensorExtEntry,_I:pdnEntPhySensorExtNotificationEnable,_J:pdnEntPhySensorExtUpperThreshold,_K:pdnEntPhySensorExtLowerThreshold,_C:pdnEntPhySensorExtThresholdState,'pdnEntitySensorExtAFNs':pdnEntitySensorExtAFNs,'pdnEntitySensorExtConformance':pdnEntitySensorExtConformance,'pdnEntitySensorExtCompliances':pdnEntitySensorExtCompliances,'pdnEntitySensorExtMIBCompliance':pdnEntitySensorExtMIBCompliance,'pdnEntitySensorExtGroups':pdnEntitySensorExtGroups,'pdnEntitySensorExtObjGroups':pdnEntitySensorExtObjGroups,_N:pdnEntitySensorExtThresholdGroup,'pdnEntitySensorExtAfnGroups':pdnEntitySensorExtAfnGroups,'pdnEntitySensorExtNtfyGroups':pdnEntitySensorExtNtfyGroups,_O:pdnEntitySensorExtThresholdNtfyGroup})