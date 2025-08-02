_H='juniMteTriggerTableGroup'
_G='juniMteExistenceTestResult'
_F='juniMteTriggerContextNameLimit'
_E='juniMteTriggerEntry'
_D='Unsigned32'
_C='Integer32'
_B='Juniper-DISMAN-EVENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mteTriggerEntry,=mibBuilder.importSymbols('DISMAN-EVENT-MIB','mteTriggerEntry')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniDismanEventMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,66))
if mibBuilder.loadTexts:juniDismanEventMIB.setRevisions(('2003-10-30 15:35',))
_JuniDismanEventMIBObjects_ObjectIdentity=ObjectIdentity
juniDismanEventMIBObjects=_JuniDismanEventMIBObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,66,1))
_JuniMteTrigger_ObjectIdentity=ObjectIdentity
juniMteTrigger=_JuniMteTrigger_ObjectIdentity((1,3,6,1,4,1,4874,2,2,66,1,1))
_JuniMteTriggerTable_Object=MibTable
juniMteTriggerTable=_JuniMteTriggerTable_Object((1,3,6,1,4,1,4874,2,2,66,1,1,1))
if mibBuilder.loadTexts:juniMteTriggerTable.setStatus(_A)
_JuniMteTriggerEntry_Object=MibTableRow
juniMteTriggerEntry=_JuniMteTriggerEntry_Object((1,3,6,1,4,1,4874,2,2,66,1,1,1,1))
if mibBuilder.loadTexts:juniMteTriggerEntry.setStatus(_A)
class _JuniMteTriggerContextNameLimit_Type(Unsigned32):defaultValue=0
_JuniMteTriggerContextNameLimit_Type.__name__=_D
_JuniMteTriggerContextNameLimit_Object=MibTableColumn
juniMteTriggerContextNameLimit=_JuniMteTriggerContextNameLimit_Object((1,3,6,1,4,1,4874,2,2,66,1,1,1,1,2),_JuniMteTriggerContextNameLimit_Type())
juniMteTriggerContextNameLimit.setMaxAccess('read-create')
if mibBuilder.loadTexts:juniMteTriggerContextNameLimit.setStatus(_A)
_JuniDismanEventMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
juniDismanEventMIBNotificationPrefix=_JuniDismanEventMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,4874,2,2,66,2))
_JuniDismanEventMIBNotificationObjects_ObjectIdentity=ObjectIdentity
juniDismanEventMIBNotificationObjects=_JuniDismanEventMIBNotificationObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,66,2,1))
class _JuniMteExistenceTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('present',0),('absent',1),('changed',2)))
_JuniMteExistenceTestResult_Type.__name__=_C
_JuniMteExistenceTestResult_Object=MibScalar
juniMteExistenceTestResult=_JuniMteExistenceTestResult_Object((1,3,6,1,4,1,4874,2,2,66,2,1,1),_JuniMteExistenceTestResult_Type())
juniMteExistenceTestResult.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:juniMteExistenceTestResult.setStatus(_A)
_JuniDismanEventConformance_ObjectIdentity=ObjectIdentity
juniDismanEventConformance=_JuniDismanEventConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,66,3))
_JuniDismanEventCompliances_ObjectIdentity=ObjectIdentity
juniDismanEventCompliances=_JuniDismanEventCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,66,3,1))
_JuniDismanEventGroups_ObjectIdentity=ObjectIdentity
juniDismanEventGroups=_JuniDismanEventGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,66,3,2))
mteTriggerEntry.registerAugmentions((_B,_E))
juniMteTriggerEntry.setIndexNames(*mteTriggerEntry.getIndexNames())
juniMteTriggerTableGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,66,3,2,1))
juniMteTriggerTableGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:juniMteTriggerTableGroup.setStatus(_A)
juniDismanEventCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,66,3,1,1))
juniDismanEventCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:juniDismanEventCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniDismanEventMIB':juniDismanEventMIB,'juniDismanEventMIBObjects':juniDismanEventMIBObjects,'juniMteTrigger':juniMteTrigger,'juniMteTriggerTable':juniMteTriggerTable,_E:juniMteTriggerEntry,_F:juniMteTriggerContextNameLimit,'juniDismanEventMIBNotificationPrefix':juniDismanEventMIBNotificationPrefix,'juniDismanEventMIBNotificationObjects':juniDismanEventMIBNotificationObjects,_G:juniMteExistenceTestResult,'juniDismanEventConformance':juniDismanEventConformance,'juniDismanEventCompliances':juniDismanEventCompliances,'juniDismanEventCompliance':juniDismanEventCompliance,'juniDismanEventGroups':juniDismanEventGroups,_H:juniMteTriggerTableGroup})