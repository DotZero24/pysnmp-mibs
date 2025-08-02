_F='cucsQueryresultUsageInstanceId'
_E='not-accessible'
_D='cucsQueryresultDependencyInstanceId'
_C='CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsQueryresultObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,75))
_CucsQueryresultDependencyTable_Object=MibTable
cucsQueryresultDependencyTable=_CucsQueryresultDependencyTable_Object((1,3,6,1,4,1,9,9,719,1,75,1))
if mibBuilder.loadTexts:cucsQueryresultDependencyTable.setStatus(_A)
_CucsQueryresultDependencyEntry_Object=MibTableRow
cucsQueryresultDependencyEntry=_CucsQueryresultDependencyEntry_Object((1,3,6,1,4,1,9,9,719,1,75,1,1))
cucsQueryresultDependencyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsQueryresultDependencyEntry.setStatus(_A)
_CucsQueryresultDependencyInstanceId_Type=CucsManagedObjectId
_CucsQueryresultDependencyInstanceId_Object=MibTableColumn
cucsQueryresultDependencyInstanceId=_CucsQueryresultDependencyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,1),_CucsQueryresultDependencyInstanceId_Type())
cucsQueryresultDependencyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsQueryresultDependencyInstanceId.setStatus(_A)
_CucsQueryresultDependencyDn_Type=CucsManagedObjectDn
_CucsQueryresultDependencyDn_Object=MibTableColumn
cucsQueryresultDependencyDn=_CucsQueryresultDependencyDn_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,2),_CucsQueryresultDependencyDn_Type())
cucsQueryresultDependencyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyDn.setStatus(_A)
_CucsQueryresultDependencyRn_Type=SnmpAdminString
_CucsQueryresultDependencyRn_Object=MibTableColumn
cucsQueryresultDependencyRn=_CucsQueryresultDependencyRn_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,3),_CucsQueryresultDependencyRn_Type())
cucsQueryresultDependencyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyRn.setStatus(_A)
_CucsQueryresultDependencyClassType_Type=SnmpAdminString
_CucsQueryresultDependencyClassType_Object=MibTableColumn
cucsQueryresultDependencyClassType=_CucsQueryresultDependencyClassType_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,4),_CucsQueryresultDependencyClassType_Type())
cucsQueryresultDependencyClassType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyClassType.setStatus(_A)
_CucsQueryresultDependencyIsImportable_Type=TruthValue
_CucsQueryresultDependencyIsImportable_Object=MibTableColumn
cucsQueryresultDependencyIsImportable=_CucsQueryresultDependencyIsImportable_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,5),_CucsQueryresultDependencyIsImportable_Type())
cucsQueryresultDependencyIsImportable.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyIsImportable.setStatus(_A)
_CucsQueryresultDependencyPolicyOwner_Type=SnmpAdminString
_CucsQueryresultDependencyPolicyOwner_Object=MibTableColumn
cucsQueryresultDependencyPolicyOwner=_CucsQueryresultDependencyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,6),_CucsQueryresultDependencyPolicyOwner_Type())
cucsQueryresultDependencyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyPolicyOwner.setStatus(_A)
_CucsQueryresultDependencyRefConvertedDn_Type=SnmpAdminString
_CucsQueryresultDependencyRefConvertedDn_Object=MibTableColumn
cucsQueryresultDependencyRefConvertedDn=_CucsQueryresultDependencyRefConvertedDn_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,7),_CucsQueryresultDependencyRefConvertedDn_Type())
cucsQueryresultDependencyRefConvertedDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyRefConvertedDn.setStatus(_A)
_CucsQueryresultDependencyRefDn_Type=SnmpAdminString
_CucsQueryresultDependencyRefDn_Object=MibTableColumn
cucsQueryresultDependencyRefDn=_CucsQueryresultDependencyRefDn_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,8),_CucsQueryresultDependencyRefDn_Type())
cucsQueryresultDependencyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyRefDn.setStatus(_A)
_CucsQueryresultDependencyRefName_Type=SnmpAdminString
_CucsQueryresultDependencyRefName_Object=MibTableColumn
cucsQueryresultDependencyRefName=_CucsQueryresultDependencyRefName_Object((1,3,6,1,4,1,9,9,719,1,75,1,1,9),_CucsQueryresultDependencyRefName_Type())
cucsQueryresultDependencyRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultDependencyRefName.setStatus(_A)
_CucsQueryresultUsageTable_Object=MibTable
cucsQueryresultUsageTable=_CucsQueryresultUsageTable_Object((1,3,6,1,4,1,9,9,719,1,75,2))
if mibBuilder.loadTexts:cucsQueryresultUsageTable.setStatus(_A)
_CucsQueryresultUsageEntry_Object=MibTableRow
cucsQueryresultUsageEntry=_CucsQueryresultUsageEntry_Object((1,3,6,1,4,1,9,9,719,1,75,2,1))
cucsQueryresultUsageEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsQueryresultUsageEntry.setStatus(_A)
_CucsQueryresultUsageInstanceId_Type=CucsManagedObjectId
_CucsQueryresultUsageInstanceId_Object=MibTableColumn
cucsQueryresultUsageInstanceId=_CucsQueryresultUsageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,1),_CucsQueryresultUsageInstanceId_Type())
cucsQueryresultUsageInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsQueryresultUsageInstanceId.setStatus(_A)
_CucsQueryresultUsageDn_Type=CucsManagedObjectDn
_CucsQueryresultUsageDn_Object=MibTableColumn
cucsQueryresultUsageDn=_CucsQueryresultUsageDn_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,2),_CucsQueryresultUsageDn_Type())
cucsQueryresultUsageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsageDn.setStatus(_A)
_CucsQueryresultUsageRn_Type=SnmpAdminString
_CucsQueryresultUsageRn_Object=MibTableColumn
cucsQueryresultUsageRn=_CucsQueryresultUsageRn_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,3),_CucsQueryresultUsageRn_Type())
cucsQueryresultUsageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsageRn.setStatus(_A)
_CucsQueryresultUsageClassType_Type=SnmpAdminString
_CucsQueryresultUsageClassType_Object=MibTableColumn
cucsQueryresultUsageClassType=_CucsQueryresultUsageClassType_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,4),_CucsQueryresultUsageClassType_Type())
cucsQueryresultUsageClassType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsageClassType.setStatus(_A)
_CucsQueryresultUsageIsServiceTemplate_Type=TruthValue
_CucsQueryresultUsageIsServiceTemplate_Object=MibTableColumn
cucsQueryresultUsageIsServiceTemplate=_CucsQueryresultUsageIsServiceTemplate_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,5),_CucsQueryresultUsageIsServiceTemplate_Type())
cucsQueryresultUsageIsServiceTemplate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsageIsServiceTemplate.setStatus(_A)
_CucsQueryresultUsagePolicyOwner_Type=SnmpAdminString
_CucsQueryresultUsagePolicyOwner_Object=MibTableColumn
cucsQueryresultUsagePolicyOwner=_CucsQueryresultUsagePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,6),_CucsQueryresultUsagePolicyOwner_Type())
cucsQueryresultUsagePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsagePolicyOwner.setStatus(_A)
_CucsQueryresultUsageRefConvertedDn_Type=SnmpAdminString
_CucsQueryresultUsageRefConvertedDn_Object=MibTableColumn
cucsQueryresultUsageRefConvertedDn=_CucsQueryresultUsageRefConvertedDn_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,7),_CucsQueryresultUsageRefConvertedDn_Type())
cucsQueryresultUsageRefConvertedDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsageRefConvertedDn.setStatus(_A)
_CucsQueryresultUsageRefDn_Type=SnmpAdminString
_CucsQueryresultUsageRefDn_Object=MibTableColumn
cucsQueryresultUsageRefDn=_CucsQueryresultUsageRefDn_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,8),_CucsQueryresultUsageRefDn_Type())
cucsQueryresultUsageRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsageRefDn.setStatus(_A)
_CucsQueryresultUsageRefName_Type=SnmpAdminString
_CucsQueryresultUsageRefName_Object=MibTableColumn
cucsQueryresultUsageRefName=_CucsQueryresultUsageRefName_Object((1,3,6,1,4,1,9,9,719,1,75,2,1,9),_CucsQueryresultUsageRefName_Type())
cucsQueryresultUsageRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsQueryresultUsageRefName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsQueryresultObjects':cucsQueryresultObjects,'cucsQueryresultDependencyTable':cucsQueryresultDependencyTable,'cucsQueryresultDependencyEntry':cucsQueryresultDependencyEntry,_D:cucsQueryresultDependencyInstanceId,'cucsQueryresultDependencyDn':cucsQueryresultDependencyDn,'cucsQueryresultDependencyRn':cucsQueryresultDependencyRn,'cucsQueryresultDependencyClassType':cucsQueryresultDependencyClassType,'cucsQueryresultDependencyIsImportable':cucsQueryresultDependencyIsImportable,'cucsQueryresultDependencyPolicyOwner':cucsQueryresultDependencyPolicyOwner,'cucsQueryresultDependencyRefConvertedDn':cucsQueryresultDependencyRefConvertedDn,'cucsQueryresultDependencyRefDn':cucsQueryresultDependencyRefDn,'cucsQueryresultDependencyRefName':cucsQueryresultDependencyRefName,'cucsQueryresultUsageTable':cucsQueryresultUsageTable,'cucsQueryresultUsageEntry':cucsQueryresultUsageEntry,_F:cucsQueryresultUsageInstanceId,'cucsQueryresultUsageDn':cucsQueryresultUsageDn,'cucsQueryresultUsageRn':cucsQueryresultUsageRn,'cucsQueryresultUsageClassType':cucsQueryresultUsageClassType,'cucsQueryresultUsageIsServiceTemplate':cucsQueryresultUsageIsServiceTemplate,'cucsQueryresultUsagePolicyOwner':cucsQueryresultUsagePolicyOwner,'cucsQueryresultUsageRefConvertedDn':cucsQueryresultUsageRefConvertedDn,'cucsQueryresultUsageRefDn':cucsQueryresultUsageRefDn,'cucsQueryresultUsageRefName':cucsQueryresultUsageRefName})