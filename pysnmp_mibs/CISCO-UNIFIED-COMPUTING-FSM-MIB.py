_D='cucsFsmStatusInstanceId'
_C='CISCO-UNIFIED-COMPUTING-FSM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsFsmFsmStageStatus,=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsFsmFsmStageStatus')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsFsmObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,63))
_CucsFsmStatusTable_Object=MibTable
cucsFsmStatusTable=_CucsFsmStatusTable_Object((1,3,6,1,4,1,9,9,719,1,63,1))
if mibBuilder.loadTexts:cucsFsmStatusTable.setStatus(_A)
_CucsFsmStatusEntry_Object=MibTableRow
cucsFsmStatusEntry=_CucsFsmStatusEntry_Object((1,3,6,1,4,1,9,9,719,1,63,1,1))
cucsFsmStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsFsmStatusEntry.setStatus(_A)
_CucsFsmStatusInstanceId_Type=CucsManagedObjectId
_CucsFsmStatusInstanceId_Object=MibTableColumn
cucsFsmStatusInstanceId=_CucsFsmStatusInstanceId_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,1),_CucsFsmStatusInstanceId_Type())
cucsFsmStatusInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsFsmStatusInstanceId.setStatus(_A)
_CucsFsmStatusDn_Type=CucsManagedObjectDn
_CucsFsmStatusDn_Object=MibTableColumn
cucsFsmStatusDn=_CucsFsmStatusDn_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,2),_CucsFsmStatusDn_Type())
cucsFsmStatusDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusDn.setStatus(_A)
_CucsFsmStatusRn_Type=SnmpAdminString
_CucsFsmStatusRn_Object=MibTableColumn
cucsFsmStatusRn=_CucsFsmStatusRn_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,3),_CucsFsmStatusRn_Type())
cucsFsmStatusRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusRn.setStatus(_A)
_CucsFsmStatusConvertedEpRef_Type=SnmpAdminString
_CucsFsmStatusConvertedEpRef_Object=MibTableColumn
cucsFsmStatusConvertedEpRef=_CucsFsmStatusConvertedEpRef_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,4),_CucsFsmStatusConvertedEpRef_Type())
cucsFsmStatusConvertedEpRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusConvertedEpRef.setStatus(_A)
_CucsFsmStatusDescr_Type=SnmpAdminString
_CucsFsmStatusDescr_Object=MibTableColumn
cucsFsmStatusDescr=_CucsFsmStatusDescr_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,5),_CucsFsmStatusDescr_Type())
cucsFsmStatusDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusDescr.setStatus(_A)
_CucsFsmStatusName_Type=SnmpAdminString
_CucsFsmStatusName_Object=MibTableColumn
cucsFsmStatusName=_CucsFsmStatusName_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,6),_CucsFsmStatusName_Type())
cucsFsmStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusName.setStatus(_A)
_CucsFsmStatusObjectClassName_Type=SnmpAdminString
_CucsFsmStatusObjectClassName_Object=MibTableColumn
cucsFsmStatusObjectClassName=_CucsFsmStatusObjectClassName_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,7),_CucsFsmStatusObjectClassName_Type())
cucsFsmStatusObjectClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusObjectClassName.setStatus(_A)
_CucsFsmStatusRemoteEpRef_Type=SnmpAdminString
_CucsFsmStatusRemoteEpRef_Object=MibTableColumn
cucsFsmStatusRemoteEpRef=_CucsFsmStatusRemoteEpRef_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,8),_CucsFsmStatusRemoteEpRef_Type())
cucsFsmStatusRemoteEpRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusRemoteEpRef.setStatus(_A)
_CucsFsmStatusState_Type=CucsFsmFsmStageStatus
_CucsFsmStatusState_Object=MibTableColumn
cucsFsmStatusState=_CucsFsmStatusState_Object((1,3,6,1,4,1,9,9,719,1,63,1,1,9),_CucsFsmStatusState_Type())
cucsFsmStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFsmStatusState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsFsmObjects':cucsFsmObjects,'cucsFsmStatusTable':cucsFsmStatusTable,'cucsFsmStatusEntry':cucsFsmStatusEntry,_D:cucsFsmStatusInstanceId,'cucsFsmStatusDn':cucsFsmStatusDn,'cucsFsmStatusRn':cucsFsmStatusRn,'cucsFsmStatusConvertedEpRef':cucsFsmStatusConvertedEpRef,'cucsFsmStatusDescr':cucsFsmStatusDescr,'cucsFsmStatusName':cucsFsmStatusName,'cucsFsmStatusObjectClassName':cucsFsmStatusObjectClassName,'cucsFsmStatusRemoteEpRef':cucsFsmStatusRemoteEpRef,'cucsFsmStatusState':cucsFsmStatusState})