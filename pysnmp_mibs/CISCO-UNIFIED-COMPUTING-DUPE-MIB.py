_F='cucsDupeScopeResultInstanceId'
_E='not-accessible'
_D='cucsDupeScopeInstanceId'
_C='CISCO-UNIFIED-COMPUTING-DUPE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsDupeOperation,CucsDupeStatus,CucsMoMoClassId=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsDupeOperation','CucsDupeStatus','CucsMoMoClassId')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsDupeObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,78))
_CucsDupeScopeTable_Object=MibTable
cucsDupeScopeTable=_CucsDupeScopeTable_Object((1,3,6,1,4,1,9,9,719,1,78,1))
if mibBuilder.loadTexts:cucsDupeScopeTable.setStatus(_A)
_CucsDupeScopeEntry_Object=MibTableRow
cucsDupeScopeEntry=_CucsDupeScopeEntry_Object((1,3,6,1,4,1,9,9,719,1,78,1,1))
cucsDupeScopeEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsDupeScopeEntry.setStatus(_A)
_CucsDupeScopeInstanceId_Type=CucsManagedObjectId
_CucsDupeScopeInstanceId_Object=MibTableColumn
cucsDupeScopeInstanceId=_CucsDupeScopeInstanceId_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,1),_CucsDupeScopeInstanceId_Type())
cucsDupeScopeInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsDupeScopeInstanceId.setStatus(_A)
_CucsDupeScopeDn_Type=CucsManagedObjectDn
_CucsDupeScopeDn_Object=MibTableColumn
cucsDupeScopeDn=_CucsDupeScopeDn_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,2),_CucsDupeScopeDn_Type())
cucsDupeScopeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeDn.setStatus(_A)
_CucsDupeScopeRn_Type=SnmpAdminString
_CucsDupeScopeRn_Object=MibTableColumn
cucsDupeScopeRn=_CucsDupeScopeRn_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,3),_CucsDupeScopeRn_Type())
cucsDupeScopeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeRn.setStatus(_A)
_CucsDupeScopeClientMoDn_Type=SnmpAdminString
_CucsDupeScopeClientMoDn_Object=MibTableColumn
cucsDupeScopeClientMoDn=_CucsDupeScopeClientMoDn_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,4),_CucsDupeScopeClientMoDn_Type())
cucsDupeScopeClientMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeClientMoDn.setStatus(_A)
_CucsDupeScopeId_Type=Gauge32
_CucsDupeScopeId_Object=MibTableColumn
cucsDupeScopeId=_CucsDupeScopeId_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,5),_CucsDupeScopeId_Type())
cucsDupeScopeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeId.setStatus(_A)
_CucsDupeScopeIsSystem_Type=TruthValue
_CucsDupeScopeIsSystem_Object=MibTableColumn
cucsDupeScopeIsSystem=_CucsDupeScopeIsSystem_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,6),_CucsDupeScopeIsSystem_Type())
cucsDupeScopeIsSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeIsSystem.setStatus(_A)
_CucsDupeScopeMoClassId_Type=CucsMoMoClassId
_CucsDupeScopeMoClassId_Object=MibTableColumn
cucsDupeScopeMoClassId=_CucsDupeScopeMoClassId_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,7),_CucsDupeScopeMoClassId_Type())
cucsDupeScopeMoClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeMoClassId.setStatus(_A)
_CucsDupeScopeOperCode_Type=CucsDupeOperation
_CucsDupeScopeOperCode_Object=MibTableColumn
cucsDupeScopeOperCode=_CucsDupeScopeOperCode_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,8),_CucsDupeScopeOperCode_Type())
cucsDupeScopeOperCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeOperCode.setStatus(_A)
_CucsDupeScopeSecondaryKey_Type=SnmpAdminString
_CucsDupeScopeSecondaryKey_Object=MibTableColumn
cucsDupeScopeSecondaryKey=_CucsDupeScopeSecondaryKey_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,9),_CucsDupeScopeSecondaryKey_Type())
cucsDupeScopeSecondaryKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeSecondaryKey.setStatus(_A)
_CucsDupeScopeSourceMoDn_Type=SnmpAdminString
_CucsDupeScopeSourceMoDn_Object=MibTableColumn
cucsDupeScopeSourceMoDn=_CucsDupeScopeSourceMoDn_Object((1,3,6,1,4,1,9,9,719,1,78,1,1,10),_CucsDupeScopeSourceMoDn_Type())
cucsDupeScopeSourceMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeSourceMoDn.setStatus(_A)
_CucsDupeScopeResultTable_Object=MibTable
cucsDupeScopeResultTable=_CucsDupeScopeResultTable_Object((1,3,6,1,4,1,9,9,719,1,78,2))
if mibBuilder.loadTexts:cucsDupeScopeResultTable.setStatus(_A)
_CucsDupeScopeResultEntry_Object=MibTableRow
cucsDupeScopeResultEntry=_CucsDupeScopeResultEntry_Object((1,3,6,1,4,1,9,9,719,1,78,2,1))
cucsDupeScopeResultEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsDupeScopeResultEntry.setStatus(_A)
_CucsDupeScopeResultInstanceId_Type=CucsManagedObjectId
_CucsDupeScopeResultInstanceId_Object=MibTableColumn
cucsDupeScopeResultInstanceId=_CucsDupeScopeResultInstanceId_Object((1,3,6,1,4,1,9,9,719,1,78,2,1,1),_CucsDupeScopeResultInstanceId_Type())
cucsDupeScopeResultInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsDupeScopeResultInstanceId.setStatus(_A)
_CucsDupeScopeResultDn_Type=CucsManagedObjectDn
_CucsDupeScopeResultDn_Object=MibTableColumn
cucsDupeScopeResultDn=_CucsDupeScopeResultDn_Object((1,3,6,1,4,1,9,9,719,1,78,2,1,2),_CucsDupeScopeResultDn_Type())
cucsDupeScopeResultDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeResultDn.setStatus(_A)
_CucsDupeScopeResultRn_Type=SnmpAdminString
_CucsDupeScopeResultRn_Object=MibTableColumn
cucsDupeScopeResultRn=_CucsDupeScopeResultRn_Object((1,3,6,1,4,1,9,9,719,1,78,2,1,3),_CucsDupeScopeResultRn_Type())
cucsDupeScopeResultRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeResultRn.setStatus(_A)
_CucsDupeScopeResultMessage_Type=SnmpAdminString
_CucsDupeScopeResultMessage_Object=MibTableColumn
cucsDupeScopeResultMessage=_CucsDupeScopeResultMessage_Object((1,3,6,1,4,1,9,9,719,1,78,2,1,4),_CucsDupeScopeResultMessage_Type())
cucsDupeScopeResultMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeResultMessage.setStatus(_A)
_CucsDupeScopeResultScopeStatus_Type=CucsDupeStatus
_CucsDupeScopeResultScopeStatus_Object=MibTableColumn
cucsDupeScopeResultScopeStatus=_CucsDupeScopeResultScopeStatus_Object((1,3,6,1,4,1,9,9,719,1,78,2,1,5),_CucsDupeScopeResultScopeStatus_Type())
cucsDupeScopeResultScopeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeResultScopeStatus.setStatus(_A)
_CucsDupeScopeResultUpdateTime_Type=DateAndTime
_CucsDupeScopeResultUpdateTime_Object=MibTableColumn
cucsDupeScopeResultUpdateTime=_CucsDupeScopeResultUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,78,2,1,6),_CucsDupeScopeResultUpdateTime_Type())
cucsDupeScopeResultUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDupeScopeResultUpdateTime.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsDupeObjects':cucsDupeObjects,'cucsDupeScopeTable':cucsDupeScopeTable,'cucsDupeScopeEntry':cucsDupeScopeEntry,_D:cucsDupeScopeInstanceId,'cucsDupeScopeDn':cucsDupeScopeDn,'cucsDupeScopeRn':cucsDupeScopeRn,'cucsDupeScopeClientMoDn':cucsDupeScopeClientMoDn,'cucsDupeScopeId':cucsDupeScopeId,'cucsDupeScopeIsSystem':cucsDupeScopeIsSystem,'cucsDupeScopeMoClassId':cucsDupeScopeMoClassId,'cucsDupeScopeOperCode':cucsDupeScopeOperCode,'cucsDupeScopeSecondaryKey':cucsDupeScopeSecondaryKey,'cucsDupeScopeSourceMoDn':cucsDupeScopeSourceMoDn,'cucsDupeScopeResultTable':cucsDupeScopeResultTable,'cucsDupeScopeResultEntry':cucsDupeScopeResultEntry,_F:cucsDupeScopeResultInstanceId,'cucsDupeScopeResultDn':cucsDupeScopeResultDn,'cucsDupeScopeResultRn':cucsDupeScopeResultRn,'cucsDupeScopeResultMessage':cucsDupeScopeResultMessage,'cucsDupeScopeResultScopeStatus':cucsDupeScopeResultScopeStatus,'cucsDupeScopeResultUpdateTime':cucsDupeScopeResultUpdateTime})