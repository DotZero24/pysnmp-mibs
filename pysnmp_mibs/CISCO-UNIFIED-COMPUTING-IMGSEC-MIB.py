_F='cucsImgsecPolicyInstanceId'
_E='not-accessible'
_D='cucsImgsecKeyInstanceId'
_C='CISCO-UNIFIED-COMPUTING-IMGSEC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsImgsecKeyType,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsImgsecKeyType','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsImgsecObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,56))
_CucsImgsecKeyTable_Object=MibTable
cucsImgsecKeyTable=_CucsImgsecKeyTable_Object((1,3,6,1,4,1,9,9,719,1,56,1))
if mibBuilder.loadTexts:cucsImgsecKeyTable.setStatus(_A)
_CucsImgsecKeyEntry_Object=MibTableRow
cucsImgsecKeyEntry=_CucsImgsecKeyEntry_Object((1,3,6,1,4,1,9,9,719,1,56,1,1))
cucsImgsecKeyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsImgsecKeyEntry.setStatus(_A)
_CucsImgsecKeyInstanceId_Type=CucsManagedObjectId
_CucsImgsecKeyInstanceId_Object=MibTableColumn
cucsImgsecKeyInstanceId=_CucsImgsecKeyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,56,1,1,1),_CucsImgsecKeyInstanceId_Type())
cucsImgsecKeyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsImgsecKeyInstanceId.setStatus(_A)
_CucsImgsecKeyDn_Type=CucsManagedObjectDn
_CucsImgsecKeyDn_Object=MibTableColumn
cucsImgsecKeyDn=_CucsImgsecKeyDn_Object((1,3,6,1,4,1,9,9,719,1,56,1,1,2),_CucsImgsecKeyDn_Type())
cucsImgsecKeyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecKeyDn.setStatus(_A)
_CucsImgsecKeyRn_Type=SnmpAdminString
_CucsImgsecKeyRn_Object=MibTableColumn
cucsImgsecKeyRn=_CucsImgsecKeyRn_Object((1,3,6,1,4,1,9,9,719,1,56,1,1,3),_CucsImgsecKeyRn_Type())
cucsImgsecKeyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecKeyRn.setStatus(_A)
_CucsImgsecKeyType_Type=CucsImgsecKeyType
_CucsImgsecKeyType_Object=MibTableColumn
cucsImgsecKeyType=_CucsImgsecKeyType_Object((1,3,6,1,4,1,9,9,719,1,56,1,1,4),_CucsImgsecKeyType_Type())
cucsImgsecKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecKeyType.setStatus(_A)
_CucsImgsecKeyValue_Type=SnmpAdminString
_CucsImgsecKeyValue_Object=MibTableColumn
cucsImgsecKeyValue=_CucsImgsecKeyValue_Object((1,3,6,1,4,1,9,9,719,1,56,1,1,5),_CucsImgsecKeyValue_Type())
cucsImgsecKeyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecKeyValue.setStatus(_A)
_CucsImgsecPolicyTable_Object=MibTable
cucsImgsecPolicyTable=_CucsImgsecPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,56,2))
if mibBuilder.loadTexts:cucsImgsecPolicyTable.setStatus(_A)
_CucsImgsecPolicyEntry_Object=MibTableRow
cucsImgsecPolicyEntry=_CucsImgsecPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,56,2,1))
cucsImgsecPolicyEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsImgsecPolicyEntry.setStatus(_A)
_CucsImgsecPolicyInstanceId_Type=CucsManagedObjectId
_CucsImgsecPolicyInstanceId_Object=MibTableColumn
cucsImgsecPolicyInstanceId=_CucsImgsecPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,1),_CucsImgsecPolicyInstanceId_Type())
cucsImgsecPolicyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsImgsecPolicyInstanceId.setStatus(_A)
_CucsImgsecPolicyDn_Type=CucsManagedObjectDn
_CucsImgsecPolicyDn_Object=MibTableColumn
cucsImgsecPolicyDn=_CucsImgsecPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,2),_CucsImgsecPolicyDn_Type())
cucsImgsecPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecPolicyDn.setStatus(_A)
_CucsImgsecPolicyRn_Type=SnmpAdminString
_CucsImgsecPolicyRn_Object=MibTableColumn
cucsImgsecPolicyRn=_CucsImgsecPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,3),_CucsImgsecPolicyRn_Type())
cucsImgsecPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecPolicyRn.setStatus(_A)
_CucsImgsecPolicyDescr_Type=SnmpAdminString
_CucsImgsecPolicyDescr_Object=MibTableColumn
cucsImgsecPolicyDescr=_CucsImgsecPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,4),_CucsImgsecPolicyDescr_Type())
cucsImgsecPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecPolicyDescr.setStatus(_A)
_CucsImgsecPolicyIntId_Type=SnmpAdminString
_CucsImgsecPolicyIntId_Object=MibTableColumn
cucsImgsecPolicyIntId=_CucsImgsecPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,5),_CucsImgsecPolicyIntId_Type())
cucsImgsecPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecPolicyIntId.setStatus(_A)
_CucsImgsecPolicyName_Type=SnmpAdminString
_CucsImgsecPolicyName_Object=MibTableColumn
cucsImgsecPolicyName=_CucsImgsecPolicyName_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,6),_CucsImgsecPolicyName_Type())
cucsImgsecPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecPolicyName.setStatus(_A)
_CucsImgsecPolicyPolicyLevel_Type=Gauge32
_CucsImgsecPolicyPolicyLevel_Object=MibTableColumn
cucsImgsecPolicyPolicyLevel=_CucsImgsecPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,7),_CucsImgsecPolicyPolicyLevel_Type())
cucsImgsecPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecPolicyPolicyLevel.setStatus(_A)
_CucsImgsecPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsImgsecPolicyPolicyOwner_Object=MibTableColumn
cucsImgsecPolicyPolicyOwner=_CucsImgsecPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,56,2,1,8),_CucsImgsecPolicyPolicyOwner_Type())
cucsImgsecPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgsecPolicyPolicyOwner.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsImgsecObjects':cucsImgsecObjects,'cucsImgsecKeyTable':cucsImgsecKeyTable,'cucsImgsecKeyEntry':cucsImgsecKeyEntry,_D:cucsImgsecKeyInstanceId,'cucsImgsecKeyDn':cucsImgsecKeyDn,'cucsImgsecKeyRn':cucsImgsecKeyRn,'cucsImgsecKeyType':cucsImgsecKeyType,'cucsImgsecKeyValue':cucsImgsecKeyValue,'cucsImgsecPolicyTable':cucsImgsecPolicyTable,'cucsImgsecPolicyEntry':cucsImgsecPolicyEntry,_F:cucsImgsecPolicyInstanceId,'cucsImgsecPolicyDn':cucsImgsecPolicyDn,'cucsImgsecPolicyRn':cucsImgsecPolicyRn,'cucsImgsecPolicyDescr':cucsImgsecPolicyDescr,'cucsImgsecPolicyIntId':cucsImgsecPolicyIntId,'cucsImgsecPolicyName':cucsImgsecPolicyName,'cucsImgsecPolicyPolicyLevel':cucsImgsecPolicyPolicyLevel,'cucsImgsecPolicyPolicyOwner':cucsImgsecPolicyPolicyOwner})