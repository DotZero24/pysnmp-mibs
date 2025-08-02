_D='cucsBmcSELCounterInstanceId'
_C='CISCO-UNIFIED-COMPUTING-BMC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsBmcSELCntEqptClassId,CucsBmcSELCntEqptInstIdPropId,CucsBmcSELCntStatsClassId=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsBmcSELCntEqptClassId','CucsBmcSELCntEqptInstIdPropId','CucsBmcSELCntStatsClassId')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsBmcObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,5))
_CucsBmcSELCounterTable_Object=MibTable
cucsBmcSELCounterTable=_CucsBmcSELCounterTable_Object((1,3,6,1,4,1,9,9,719,1,5,1))
if mibBuilder.loadTexts:cucsBmcSELCounterTable.setStatus(_A)
_CucsBmcSELCounterEntry_Object=MibTableRow
cucsBmcSELCounterEntry=_CucsBmcSELCounterEntry_Object((1,3,6,1,4,1,9,9,719,1,5,1,1))
cucsBmcSELCounterEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsBmcSELCounterEntry.setStatus(_A)
_CucsBmcSELCounterInstanceId_Type=CucsManagedObjectId
_CucsBmcSELCounterInstanceId_Object=MibTableColumn
cucsBmcSELCounterInstanceId=_CucsBmcSELCounterInstanceId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,1),_CucsBmcSELCounterInstanceId_Type())
cucsBmcSELCounterInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsBmcSELCounterInstanceId.setStatus(_A)
_CucsBmcSELCounterDn_Type=CucsManagedObjectDn
_CucsBmcSELCounterDn_Object=MibTableColumn
cucsBmcSELCounterDn=_CucsBmcSELCounterDn_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,2),_CucsBmcSELCounterDn_Type())
cucsBmcSELCounterDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterDn.setStatus(_A)
_CucsBmcSELCounterRn_Type=SnmpAdminString
_CucsBmcSELCounterRn_Object=MibTableColumn
cucsBmcSELCounterRn=_CucsBmcSELCounterRn_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,3),_CucsBmcSELCounterRn_Type())
cucsBmcSELCounterRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterRn.setStatus(_A)
_CucsBmcSELCounterBitmask_Type=SnmpAdminString
_CucsBmcSELCounterBitmask_Object=MibTableColumn
cucsBmcSELCounterBitmask=_CucsBmcSELCounterBitmask_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,4),_CucsBmcSELCounterBitmask_Type())
cucsBmcSELCounterBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterBitmask.setStatus(_A)
_CucsBmcSELCounterCollInterval_Type=Gauge32
_CucsBmcSELCounterCollInterval_Object=MibTableColumn
cucsBmcSELCounterCollInterval=_CucsBmcSELCounterCollInterval_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,5),_CucsBmcSELCounterCollInterval_Type())
cucsBmcSELCounterCollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterCollInterval.setStatus(_A)
_CucsBmcSELCounterContClassId_Type=CucsBmcSELCntEqptClassId
_CucsBmcSELCounterContClassId_Object=MibTableColumn
cucsBmcSELCounterContClassId=_CucsBmcSELCounterContClassId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,6),_CucsBmcSELCounterContClassId_Type())
cucsBmcSELCounterContClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterContClassId.setStatus(_A)
_CucsBmcSELCounterContInstId_Type=SnmpAdminString
_CucsBmcSELCounterContInstId_Object=MibTableColumn
cucsBmcSELCounterContInstId=_CucsBmcSELCounterContInstId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,7),_CucsBmcSELCounterContInstId_Type())
cucsBmcSELCounterContInstId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterContInstId.setStatus(_A)
_CucsBmcSELCounterContInstIdPropId_Type=CucsBmcSELCntEqptInstIdPropId
_CucsBmcSELCounterContInstIdPropId_Object=MibTableColumn
cucsBmcSELCounterContInstIdPropId=_CucsBmcSELCounterContInstIdPropId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,8),_CucsBmcSELCounterContInstIdPropId_Type())
cucsBmcSELCounterContInstIdPropId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterContInstIdPropId.setStatus(_A)
_CucsBmcSELCounterEqptClassId_Type=CucsBmcSELCntEqptClassId
_CucsBmcSELCounterEqptClassId_Object=MibTableColumn
cucsBmcSELCounterEqptClassId=_CucsBmcSELCounterEqptClassId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,9),_CucsBmcSELCounterEqptClassId_Type())
cucsBmcSELCounterEqptClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterEqptClassId.setStatus(_A)
_CucsBmcSELCounterEqptInstId_Type=SnmpAdminString
_CucsBmcSELCounterEqptInstId_Object=MibTableColumn
cucsBmcSELCounterEqptInstId=_CucsBmcSELCounterEqptInstId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,10),_CucsBmcSELCounterEqptInstId_Type())
cucsBmcSELCounterEqptInstId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterEqptInstId.setStatus(_A)
_CucsBmcSELCounterEqptInstIdPropId_Type=CucsBmcSELCntEqptInstIdPropId
_CucsBmcSELCounterEqptInstIdPropId_Object=MibTableColumn
cucsBmcSELCounterEqptInstIdPropId=_CucsBmcSELCounterEqptInstIdPropId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,11),_CucsBmcSELCounterEqptInstIdPropId_Type())
cucsBmcSELCounterEqptInstIdPropId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterEqptInstIdPropId.setStatus(_A)
_CucsBmcSELCounterGlobalId_Type=SnmpAdminString
_CucsBmcSELCounterGlobalId_Object=MibTableColumn
cucsBmcSELCounterGlobalId=_CucsBmcSELCounterGlobalId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,12),_CucsBmcSELCounterGlobalId_Type())
cucsBmcSELCounterGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterGlobalId.setStatus(_A)
_CucsBmcSELCounterLocalId_Type=SnmpAdminString
_CucsBmcSELCounterLocalId_Object=MibTableColumn
cucsBmcSELCounterLocalId=_CucsBmcSELCounterLocalId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,13),_CucsBmcSELCounterLocalId_Type())
cucsBmcSELCounterLocalId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterLocalId.setStatus(_A)
_CucsBmcSELCounterPcGlobalId_Type=SnmpAdminString
_CucsBmcSELCounterPcGlobalId_Object=MibTableColumn
cucsBmcSELCounterPcGlobalId=_CucsBmcSELCounterPcGlobalId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,14),_CucsBmcSELCounterPcGlobalId_Type())
cucsBmcSELCounterPcGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterPcGlobalId.setStatus(_A)
_CucsBmcSELCounterPcLocalId_Type=SnmpAdminString
_CucsBmcSELCounterPcLocalId_Object=MibTableColumn
cucsBmcSELCounterPcLocalId=_CucsBmcSELCounterPcLocalId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,15),_CucsBmcSELCounterPcLocalId_Type())
cucsBmcSELCounterPcLocalId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterPcLocalId.setStatus(_A)
_CucsBmcSELCounterStatsClassId_Type=CucsBmcSELCntStatsClassId
_CucsBmcSELCounterStatsClassId_Object=MibTableColumn
cucsBmcSELCounterStatsClassId=_CucsBmcSELCounterStatsClassId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,16),_CucsBmcSELCounterStatsClassId_Type())
cucsBmcSELCounterStatsClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterStatsClassId.setStatus(_A)
_CucsBmcSELCounterStatsPropId_Type=Integer32
_CucsBmcSELCounterStatsPropId_Object=MibTableColumn
cucsBmcSELCounterStatsPropId=_CucsBmcSELCounterStatsPropId_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,17),_CucsBmcSELCounterStatsPropId_Type())
cucsBmcSELCounterStatsPropId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterStatsPropId.setStatus(_A)
_CucsBmcSELCounterThreshold_Type=Gauge32
_CucsBmcSELCounterThreshold_Object=MibTableColumn
cucsBmcSELCounterThreshold=_CucsBmcSELCounterThreshold_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,18),_CucsBmcSELCounterThreshold_Type())
cucsBmcSELCounterThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterThreshold.setStatus(_A)
_CucsBmcSELCounterValue_Type=SnmpAdminString
_CucsBmcSELCounterValue_Object=MibTableColumn
cucsBmcSELCounterValue=_CucsBmcSELCounterValue_Object((1,3,6,1,4,1,9,9,719,1,5,1,1,19),_CucsBmcSELCounterValue_Type())
cucsBmcSELCounterValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsBmcSELCounterValue.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsBmcObjects':cucsBmcObjects,'cucsBmcSELCounterTable':cucsBmcSELCounterTable,'cucsBmcSELCounterEntry':cucsBmcSELCounterEntry,_D:cucsBmcSELCounterInstanceId,'cucsBmcSELCounterDn':cucsBmcSELCounterDn,'cucsBmcSELCounterRn':cucsBmcSELCounterRn,'cucsBmcSELCounterBitmask':cucsBmcSELCounterBitmask,'cucsBmcSELCounterCollInterval':cucsBmcSELCounterCollInterval,'cucsBmcSELCounterContClassId':cucsBmcSELCounterContClassId,'cucsBmcSELCounterContInstId':cucsBmcSELCounterContInstId,'cucsBmcSELCounterContInstIdPropId':cucsBmcSELCounterContInstIdPropId,'cucsBmcSELCounterEqptClassId':cucsBmcSELCounterEqptClassId,'cucsBmcSELCounterEqptInstId':cucsBmcSELCounterEqptInstId,'cucsBmcSELCounterEqptInstIdPropId':cucsBmcSELCounterEqptInstIdPropId,'cucsBmcSELCounterGlobalId':cucsBmcSELCounterGlobalId,'cucsBmcSELCounterLocalId':cucsBmcSELCounterLocalId,'cucsBmcSELCounterPcGlobalId':cucsBmcSELCounterPcGlobalId,'cucsBmcSELCounterPcLocalId':cucsBmcSELCounterPcLocalId,'cucsBmcSELCounterStatsClassId':cucsBmcSELCounterStatsClassId,'cucsBmcSELCounterStatsPropId':cucsBmcSELCounterStatsPropId,'cucsBmcSELCounterThreshold':cucsBmcSELCounterThreshold,'cucsBmcSELCounterValue':cucsBmcSELCounterValue})