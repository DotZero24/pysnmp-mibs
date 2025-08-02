_K='etsysHauModuleGroup'
_J='etsysHauSystemGroup'
_I='etsysHauModuleGroupId'
_H='etsysHauSystemHauMode'
_G='etsysHauSystemInterGroupDelay'
_F='etsysHauModuleSlot'
_E='read-write'
_D='Unsigned32'
_C='ENTERASYS-HIGH-AVAILABILITY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeInterval')
etsysHighAvailabilityUpgradeMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,84))
if mibBuilder.loadTexts:etsysHighAvailabilityUpgradeMIB.setRevisions(('2011-12-12 15:14',))
class EtsysHauSystemStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('hauDisabled',1),('hauPending',2),('hauRunning',3),('hauHalted',4),('hauSuccess',5),('hauError',6),('hauForceComplete',7)))
class EtsysHauMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hauNever',1),('hauIfPossible',2),('hauAlways',3)))
class HauSlotList(TextualConvention,OctetString):status=_A
class HauSlot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_EtsysHauObjects_ObjectIdentity=ObjectIdentity
etsysHauObjects=_EtsysHauObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,84,1))
_EtsysHauStats_ObjectIdentity=ObjectIdentity
etsysHauStats=_EtsysHauStats_ObjectIdentity((1,3,6,1,4,1,5624,1,2,84,1,1))
_EtsysHauStatsStatus_Type=EtsysHauSystemStatus
_EtsysHauStatsStatus_Object=MibScalar
etsysHauStatsStatus=_EtsysHauStatsStatus_Object((1,3,6,1,4,1,5624,1,2,84,1,1,1),_EtsysHauStatsStatus_Type())
etsysHauStatsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsStatus.setStatus(_A)
_EtsysHauStatsOriginalImage_Type=SnmpAdminString
_EtsysHauStatsOriginalImage_Object=MibScalar
etsysHauStatsOriginalImage=_EtsysHauStatsOriginalImage_Object((1,3,6,1,4,1,5624,1,2,84,1,1,2),_EtsysHauStatsOriginalImage_Type())
etsysHauStatsOriginalImage.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsOriginalImage.setStatus(_A)
_EtsysHauStatsTargetImage_Type=SnmpAdminString
_EtsysHauStatsTargetImage_Object=MibScalar
etsysHauStatsTargetImage=_EtsysHauStatsTargetImage_Object((1,3,6,1,4,1,5624,1,2,84,1,1,3),_EtsysHauStatsTargetImage_Type())
etsysHauStatsTargetImage.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsTargetImage.setStatus(_A)
_EtsysHauStatsPendingSlotList_Type=HauSlotList
_EtsysHauStatsPendingSlotList_Object=MibScalar
etsysHauStatsPendingSlotList=_EtsysHauStatsPendingSlotList_Object((1,3,6,1,4,1,5624,1,2,84,1,1,4),_EtsysHauStatsPendingSlotList_Type())
etsysHauStatsPendingSlotList.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsPendingSlotList.setStatus(_A)
_EtsysHauStatsInProgressSlotList_Type=HauSlotList
_EtsysHauStatsInProgressSlotList_Object=MibScalar
etsysHauStatsInProgressSlotList=_EtsysHauStatsInProgressSlotList_Object((1,3,6,1,4,1,5624,1,2,84,1,1,5),_EtsysHauStatsInProgressSlotList_Type())
etsysHauStatsInProgressSlotList.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsInProgressSlotList.setStatus(_A)
_EtsysHauStatsUpgradedSlotList_Type=HauSlotList
_EtsysHauStatsUpgradedSlotList_Object=MibScalar
etsysHauStatsUpgradedSlotList=_EtsysHauStatsUpgradedSlotList_Object((1,3,6,1,4,1,5624,1,2,84,1,1,6),_EtsysHauStatsUpgradedSlotList_Type())
etsysHauStatsUpgradedSlotList.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsUpgradedSlotList.setStatus(_A)
_EtsysHauStatsErrorSlotList_Type=HauSlotList
_EtsysHauStatsErrorSlotList_Object=MibScalar
etsysHauStatsErrorSlotList=_EtsysHauStatsErrorSlotList_Object((1,3,6,1,4,1,5624,1,2,84,1,1,7),_EtsysHauStatsErrorSlotList_Type())
etsysHauStatsErrorSlotList.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsErrorSlotList.setStatus(_A)
_EtsysHauStatsStartTime_Type=DateAndTime
_EtsysHauStatsStartTime_Object=MibScalar
etsysHauStatsStartTime=_EtsysHauStatsStartTime_Object((1,3,6,1,4,1,5624,1,2,84,1,1,8),_EtsysHauStatsStartTime_Type())
etsysHauStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsStartTime.setStatus(_A)
_EtsysHauStatsDuration_Type=TimeInterval
_EtsysHauStatsDuration_Object=MibScalar
etsysHauStatsDuration=_EtsysHauStatsDuration_Object((1,3,6,1,4,1,5624,1,2,84,1,1,9),_EtsysHauStatsDuration_Type())
etsysHauStatsDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauStatsDuration.setStatus(_A)
_EtsysHauSystem_ObjectIdentity=ObjectIdentity
etsysHauSystem=_EtsysHauSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,84,1,2))
class _EtsysHauSystemInterGroupDelay_Type(Unsigned32):defaultValue=15
_EtsysHauSystemInterGroupDelay_Type.__name__=_D
_EtsysHauSystemInterGroupDelay_Object=MibScalar
etsysHauSystemInterGroupDelay=_EtsysHauSystemInterGroupDelay_Object((1,3,6,1,4,1,5624,1,2,84,1,2,1),_EtsysHauSystemInterGroupDelay_Type())
etsysHauSystemInterGroupDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysHauSystemInterGroupDelay.setStatus(_A)
if mibBuilder.loadTexts:etsysHauSystemInterGroupDelay.setUnits('seconds')
_EtsysHauSystemHauMode_Type=EtsysHauMode
_EtsysHauSystemHauMode_Object=MibScalar
etsysHauSystemHauMode=_EtsysHauSystemHauMode_Object((1,3,6,1,4,1,5624,1,2,84,1,2,2),_EtsysHauSystemHauMode_Type())
etsysHauSystemHauMode.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysHauSystemHauMode.setStatus(_A)
_EtsysHauModule_ObjectIdentity=ObjectIdentity
etsysHauModule=_EtsysHauModule_ObjectIdentity((1,3,6,1,4,1,5624,1,2,84,1,3))
_EtsysHauModuleTable_Object=MibTable
etsysHauModuleTable=_EtsysHauModuleTable_Object((1,3,6,1,4,1,5624,1,2,84,1,3,1))
if mibBuilder.loadTexts:etsysHauModuleTable.setStatus(_A)
_EtsysHauModuleEntry_Object=MibTableRow
etsysHauModuleEntry=_EtsysHauModuleEntry_Object((1,3,6,1,4,1,5624,1,2,84,1,3,1,1))
etsysHauModuleEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:etsysHauModuleEntry.setStatus(_A)
_EtsysHauModuleSlot_Type=HauSlot
_EtsysHauModuleSlot_Object=MibTableColumn
etsysHauModuleSlot=_EtsysHauModuleSlot_Object((1,3,6,1,4,1,5624,1,2,84,1,3,1,1,1),_EtsysHauModuleSlot_Type())
etsysHauModuleSlot.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysHauModuleSlot.setStatus(_A)
_EtsysHauModuleEntRef_Type=PhysicalIndex
_EtsysHauModuleEntRef_Object=MibTableColumn
etsysHauModuleEntRef=_EtsysHauModuleEntRef_Object((1,3,6,1,4,1,5624,1,2,84,1,3,1,1,2),_EtsysHauModuleEntRef_Type())
etsysHauModuleEntRef.setMaxAccess(_B)
if mibBuilder.loadTexts:etsysHauModuleEntRef.setStatus(_A)
class _EtsysHauModuleGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_EtsysHauModuleGroupId_Type.__name__=_D
_EtsysHauModuleGroupId_Object=MibTableColumn
etsysHauModuleGroupId=_EtsysHauModuleGroupId_Object((1,3,6,1,4,1,5624,1,2,84,1,3,1,1,3),_EtsysHauModuleGroupId_Type())
etsysHauModuleGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysHauModuleGroupId.setStatus(_A)
_EtsysHauConformance_ObjectIdentity=ObjectIdentity
etsysHauConformance=_EtsysHauConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,84,2))
_EtsysHauGroups_ObjectIdentity=ObjectIdentity
etsysHauGroups=_EtsysHauGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,84,2,1))
_EtsysHauCompliances_ObjectIdentity=ObjectIdentity
etsysHauCompliances=_EtsysHauCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,84,2,2))
etsysHauSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,84,2,1,1))
etsysHauSystemGroup.setObjects(*((_C,_G),(_C,_H)))
if mibBuilder.loadTexts:etsysHauSystemGroup.setStatus(_A)
etsysHauModuleGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,84,2,1,2))
etsysHauModuleGroup.setObjects((_C,_I))
if mibBuilder.loadTexts:etsysHauModuleGroup.setStatus(_A)
etsysHauCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,84,2,2,1))
etsysHauCompliance.setObjects(*((_C,_J),(_C,_K)))
if mibBuilder.loadTexts:etsysHauCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EtsysHauSystemStatus':EtsysHauSystemStatus,'EtsysHauMode':EtsysHauMode,'HauSlotList':HauSlotList,'HauSlot':HauSlot,'etsysHighAvailabilityUpgradeMIB':etsysHighAvailabilityUpgradeMIB,'etsysHauObjects':etsysHauObjects,'etsysHauStats':etsysHauStats,'etsysHauStatsStatus':etsysHauStatsStatus,'etsysHauStatsOriginalImage':etsysHauStatsOriginalImage,'etsysHauStatsTargetImage':etsysHauStatsTargetImage,'etsysHauStatsPendingSlotList':etsysHauStatsPendingSlotList,'etsysHauStatsInProgressSlotList':etsysHauStatsInProgressSlotList,'etsysHauStatsUpgradedSlotList':etsysHauStatsUpgradedSlotList,'etsysHauStatsErrorSlotList':etsysHauStatsErrorSlotList,'etsysHauStatsStartTime':etsysHauStatsStartTime,'etsysHauStatsDuration':etsysHauStatsDuration,'etsysHauSystem':etsysHauSystem,_G:etsysHauSystemInterGroupDelay,_H:etsysHauSystemHauMode,'etsysHauModule':etsysHauModule,'etsysHauModuleTable':etsysHauModuleTable,'etsysHauModuleEntry':etsysHauModuleEntry,_F:etsysHauModuleSlot,'etsysHauModuleEntRef':etsysHauModuleEntRef,_I:etsysHauModuleGroupId,'etsysHauConformance':etsysHauConformance,'etsysHauGroups':etsysHauGroups,_J:etsysHauSystemGroup,_K:etsysHauModuleGroup,'etsysHauCompliances':etsysHauCompliances,'etsysHauCompliance':etsysHauCompliance})