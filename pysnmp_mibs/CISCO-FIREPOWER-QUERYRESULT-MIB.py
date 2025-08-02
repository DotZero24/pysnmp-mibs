_F='cfprQueryresultUsageInstanceId'
_E='not-accessible'
_D='cfprQueryresultDependencyInstanceId'
_C='CISCO-FIREPOWER-QUERYRESULT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprQueryresultObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,68))
_CfprQueryresultDependencyTable_Object=MibTable
cfprQueryresultDependencyTable=_CfprQueryresultDependencyTable_Object((1,3,6,1,4,1,9,9,826,1,68,1))
if mibBuilder.loadTexts:cfprQueryresultDependencyTable.setStatus(_A)
_CfprQueryresultDependencyEntry_Object=MibTableRow
cfprQueryresultDependencyEntry=_CfprQueryresultDependencyEntry_Object((1,3,6,1,4,1,9,9,826,1,68,1,1))
cfprQueryresultDependencyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprQueryresultDependencyEntry.setStatus(_A)
_CfprQueryresultDependencyInstanceId_Type=CfprManagedObjectId
_CfprQueryresultDependencyInstanceId_Object=MibTableColumn
cfprQueryresultDependencyInstanceId=_CfprQueryresultDependencyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,1),_CfprQueryresultDependencyInstanceId_Type())
cfprQueryresultDependencyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprQueryresultDependencyInstanceId.setStatus(_A)
_CfprQueryresultDependencyDn_Type=CfprManagedObjectDn
_CfprQueryresultDependencyDn_Object=MibTableColumn
cfprQueryresultDependencyDn=_CfprQueryresultDependencyDn_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,2),_CfprQueryresultDependencyDn_Type())
cfprQueryresultDependencyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyDn.setStatus(_A)
_CfprQueryresultDependencyRn_Type=SnmpAdminString
_CfprQueryresultDependencyRn_Object=MibTableColumn
cfprQueryresultDependencyRn=_CfprQueryresultDependencyRn_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,3),_CfprQueryresultDependencyRn_Type())
cfprQueryresultDependencyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyRn.setStatus(_A)
_CfprQueryresultDependencyClassType_Type=SnmpAdminString
_CfprQueryresultDependencyClassType_Object=MibTableColumn
cfprQueryresultDependencyClassType=_CfprQueryresultDependencyClassType_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,4),_CfprQueryresultDependencyClassType_Type())
cfprQueryresultDependencyClassType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyClassType.setStatus(_A)
_CfprQueryresultDependencyIsImportable_Type=TruthValue
_CfprQueryresultDependencyIsImportable_Object=MibTableColumn
cfprQueryresultDependencyIsImportable=_CfprQueryresultDependencyIsImportable_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,5),_CfprQueryresultDependencyIsImportable_Type())
cfprQueryresultDependencyIsImportable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyIsImportable.setStatus(_A)
_CfprQueryresultDependencyPolicyOwner_Type=SnmpAdminString
_CfprQueryresultDependencyPolicyOwner_Object=MibTableColumn
cfprQueryresultDependencyPolicyOwner=_CfprQueryresultDependencyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,6),_CfprQueryresultDependencyPolicyOwner_Type())
cfprQueryresultDependencyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyPolicyOwner.setStatus(_A)
_CfprQueryresultDependencyRefConvertedDn_Type=SnmpAdminString
_CfprQueryresultDependencyRefConvertedDn_Object=MibTableColumn
cfprQueryresultDependencyRefConvertedDn=_CfprQueryresultDependencyRefConvertedDn_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,7),_CfprQueryresultDependencyRefConvertedDn_Type())
cfprQueryresultDependencyRefConvertedDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyRefConvertedDn.setStatus(_A)
_CfprQueryresultDependencyRefDn_Type=SnmpAdminString
_CfprQueryresultDependencyRefDn_Object=MibTableColumn
cfprQueryresultDependencyRefDn=_CfprQueryresultDependencyRefDn_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,8),_CfprQueryresultDependencyRefDn_Type())
cfprQueryresultDependencyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyRefDn.setStatus(_A)
_CfprQueryresultDependencyRefName_Type=SnmpAdminString
_CfprQueryresultDependencyRefName_Object=MibTableColumn
cfprQueryresultDependencyRefName=_CfprQueryresultDependencyRefName_Object((1,3,6,1,4,1,9,9,826,1,68,1,1,9),_CfprQueryresultDependencyRefName_Type())
cfprQueryresultDependencyRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultDependencyRefName.setStatus(_A)
_CfprQueryresultUsageTable_Object=MibTable
cfprQueryresultUsageTable=_CfprQueryresultUsageTable_Object((1,3,6,1,4,1,9,9,826,1,68,2))
if mibBuilder.loadTexts:cfprQueryresultUsageTable.setStatus(_A)
_CfprQueryresultUsageEntry_Object=MibTableRow
cfprQueryresultUsageEntry=_CfprQueryresultUsageEntry_Object((1,3,6,1,4,1,9,9,826,1,68,2,1))
cfprQueryresultUsageEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprQueryresultUsageEntry.setStatus(_A)
_CfprQueryresultUsageInstanceId_Type=CfprManagedObjectId
_CfprQueryresultUsageInstanceId_Object=MibTableColumn
cfprQueryresultUsageInstanceId=_CfprQueryresultUsageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,1),_CfprQueryresultUsageInstanceId_Type())
cfprQueryresultUsageInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprQueryresultUsageInstanceId.setStatus(_A)
_CfprQueryresultUsageDn_Type=CfprManagedObjectDn
_CfprQueryresultUsageDn_Object=MibTableColumn
cfprQueryresultUsageDn=_CfprQueryresultUsageDn_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,2),_CfprQueryresultUsageDn_Type())
cfprQueryresultUsageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsageDn.setStatus(_A)
_CfprQueryresultUsageRn_Type=SnmpAdminString
_CfprQueryresultUsageRn_Object=MibTableColumn
cfprQueryresultUsageRn=_CfprQueryresultUsageRn_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,3),_CfprQueryresultUsageRn_Type())
cfprQueryresultUsageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsageRn.setStatus(_A)
_CfprQueryresultUsageClassType_Type=SnmpAdminString
_CfprQueryresultUsageClassType_Object=MibTableColumn
cfprQueryresultUsageClassType=_CfprQueryresultUsageClassType_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,4),_CfprQueryresultUsageClassType_Type())
cfprQueryresultUsageClassType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsageClassType.setStatus(_A)
_CfprQueryresultUsageIsServiceTemplate_Type=TruthValue
_CfprQueryresultUsageIsServiceTemplate_Object=MibTableColumn
cfprQueryresultUsageIsServiceTemplate=_CfprQueryresultUsageIsServiceTemplate_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,5),_CfprQueryresultUsageIsServiceTemplate_Type())
cfprQueryresultUsageIsServiceTemplate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsageIsServiceTemplate.setStatus(_A)
_CfprQueryresultUsagePolicyOwner_Type=SnmpAdminString
_CfprQueryresultUsagePolicyOwner_Object=MibTableColumn
cfprQueryresultUsagePolicyOwner=_CfprQueryresultUsagePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,6),_CfprQueryresultUsagePolicyOwner_Type())
cfprQueryresultUsagePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsagePolicyOwner.setStatus(_A)
_CfprQueryresultUsageRefConvertedDn_Type=SnmpAdminString
_CfprQueryresultUsageRefConvertedDn_Object=MibTableColumn
cfprQueryresultUsageRefConvertedDn=_CfprQueryresultUsageRefConvertedDn_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,7),_CfprQueryresultUsageRefConvertedDn_Type())
cfprQueryresultUsageRefConvertedDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsageRefConvertedDn.setStatus(_A)
_CfprQueryresultUsageRefDn_Type=SnmpAdminString
_CfprQueryresultUsageRefDn_Object=MibTableColumn
cfprQueryresultUsageRefDn=_CfprQueryresultUsageRefDn_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,8),_CfprQueryresultUsageRefDn_Type())
cfprQueryresultUsageRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsageRefDn.setStatus(_A)
_CfprQueryresultUsageRefName_Type=SnmpAdminString
_CfprQueryresultUsageRefName_Object=MibTableColumn
cfprQueryresultUsageRefName=_CfprQueryresultUsageRefName_Object((1,3,6,1,4,1,9,9,826,1,68,2,1,9),_CfprQueryresultUsageRefName_Type())
cfprQueryresultUsageRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprQueryresultUsageRefName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprQueryresultObjects':cfprQueryresultObjects,'cfprQueryresultDependencyTable':cfprQueryresultDependencyTable,'cfprQueryresultDependencyEntry':cfprQueryresultDependencyEntry,_D:cfprQueryresultDependencyInstanceId,'cfprQueryresultDependencyDn':cfprQueryresultDependencyDn,'cfprQueryresultDependencyRn':cfprQueryresultDependencyRn,'cfprQueryresultDependencyClassType':cfprQueryresultDependencyClassType,'cfprQueryresultDependencyIsImportable':cfprQueryresultDependencyIsImportable,'cfprQueryresultDependencyPolicyOwner':cfprQueryresultDependencyPolicyOwner,'cfprQueryresultDependencyRefConvertedDn':cfprQueryresultDependencyRefConvertedDn,'cfprQueryresultDependencyRefDn':cfprQueryresultDependencyRefDn,'cfprQueryresultDependencyRefName':cfprQueryresultDependencyRefName,'cfprQueryresultUsageTable':cfprQueryresultUsageTable,'cfprQueryresultUsageEntry':cfprQueryresultUsageEntry,_F:cfprQueryresultUsageInstanceId,'cfprQueryresultUsageDn':cfprQueryresultUsageDn,'cfprQueryresultUsageRn':cfprQueryresultUsageRn,'cfprQueryresultUsageClassType':cfprQueryresultUsageClassType,'cfprQueryresultUsageIsServiceTemplate':cfprQueryresultUsageIsServiceTemplate,'cfprQueryresultUsagePolicyOwner':cfprQueryresultUsagePolicyOwner,'cfprQueryresultUsageRefConvertedDn':cfprQueryresultUsageRefConvertedDn,'cfprQueryresultUsageRefDn':cfprQueryresultUsageRefDn,'cfprQueryresultUsageRefName':cfprQueryresultUsageRefName})