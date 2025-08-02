_D='cucsIscsiAuthProfileInstanceId'
_C='CISCO-UNIFIED-COMPUTING-ISCSI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsPolicyPolicyOwner,=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsIscsiObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,60))
_CucsIscsiAuthProfileTable_Object=MibTable
cucsIscsiAuthProfileTable=_CucsIscsiAuthProfileTable_Object((1,3,6,1,4,1,9,9,719,1,60,1))
if mibBuilder.loadTexts:cucsIscsiAuthProfileTable.setStatus(_A)
_CucsIscsiAuthProfileEntry_Object=MibTableRow
cucsIscsiAuthProfileEntry=_CucsIscsiAuthProfileEntry_Object((1,3,6,1,4,1,9,9,719,1,60,1,1))
cucsIscsiAuthProfileEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsIscsiAuthProfileEntry.setStatus(_A)
_CucsIscsiAuthProfileInstanceId_Type=CucsManagedObjectId
_CucsIscsiAuthProfileInstanceId_Object=MibTableColumn
cucsIscsiAuthProfileInstanceId=_CucsIscsiAuthProfileInstanceId_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,1),_CucsIscsiAuthProfileInstanceId_Type())
cucsIscsiAuthProfileInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsIscsiAuthProfileInstanceId.setStatus(_A)
_CucsIscsiAuthProfileDn_Type=CucsManagedObjectDn
_CucsIscsiAuthProfileDn_Object=MibTableColumn
cucsIscsiAuthProfileDn=_CucsIscsiAuthProfileDn_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,2),_CucsIscsiAuthProfileDn_Type())
cucsIscsiAuthProfileDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfileDn.setStatus(_A)
_CucsIscsiAuthProfileRn_Type=SnmpAdminString
_CucsIscsiAuthProfileRn_Object=MibTableColumn
cucsIscsiAuthProfileRn=_CucsIscsiAuthProfileRn_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,3),_CucsIscsiAuthProfileRn_Type())
cucsIscsiAuthProfileRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfileRn.setStatus(_A)
_CucsIscsiAuthProfileDescr_Type=SnmpAdminString
_CucsIscsiAuthProfileDescr_Object=MibTableColumn
cucsIscsiAuthProfileDescr=_CucsIscsiAuthProfileDescr_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,4),_CucsIscsiAuthProfileDescr_Type())
cucsIscsiAuthProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfileDescr.setStatus(_A)
_CucsIscsiAuthProfileIntId_Type=SnmpAdminString
_CucsIscsiAuthProfileIntId_Object=MibTableColumn
cucsIscsiAuthProfileIntId=_CucsIscsiAuthProfileIntId_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,5),_CucsIscsiAuthProfileIntId_Type())
cucsIscsiAuthProfileIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfileIntId.setStatus(_A)
_CucsIscsiAuthProfileName_Type=SnmpAdminString
_CucsIscsiAuthProfileName_Object=MibTableColumn
cucsIscsiAuthProfileName=_CucsIscsiAuthProfileName_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,6),_CucsIscsiAuthProfileName_Type())
cucsIscsiAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfileName.setStatus(_A)
_CucsIscsiAuthProfilePassword_Type=SnmpAdminString
_CucsIscsiAuthProfilePassword_Object=MibTableColumn
cucsIscsiAuthProfilePassword=_CucsIscsiAuthProfilePassword_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,7),_CucsIscsiAuthProfilePassword_Type())
cucsIscsiAuthProfilePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfilePassword.setStatus(_A)
_CucsIscsiAuthProfileUserId_Type=SnmpAdminString
_CucsIscsiAuthProfileUserId_Object=MibTableColumn
cucsIscsiAuthProfileUserId=_CucsIscsiAuthProfileUserId_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,8),_CucsIscsiAuthProfileUserId_Type())
cucsIscsiAuthProfileUserId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfileUserId.setStatus(_A)
_CucsIscsiAuthProfileCtpassword_Type=SnmpAdminString
_CucsIscsiAuthProfileCtpassword_Object=MibTableColumn
cucsIscsiAuthProfileCtpassword=_CucsIscsiAuthProfileCtpassword_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,9),_CucsIscsiAuthProfileCtpassword_Type())
cucsIscsiAuthProfileCtpassword.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfileCtpassword.setStatus(_A)
_CucsIscsiAuthProfilePolicyLevel_Type=Gauge32
_CucsIscsiAuthProfilePolicyLevel_Object=MibTableColumn
cucsIscsiAuthProfilePolicyLevel=_CucsIscsiAuthProfilePolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,10),_CucsIscsiAuthProfilePolicyLevel_Type())
cucsIscsiAuthProfilePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfilePolicyLevel.setStatus(_A)
_CucsIscsiAuthProfilePolicyOwner_Type=CucsPolicyPolicyOwner
_CucsIscsiAuthProfilePolicyOwner_Object=MibTableColumn
cucsIscsiAuthProfilePolicyOwner=_CucsIscsiAuthProfilePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,60,1,1,11),_CucsIscsiAuthProfilePolicyOwner_Type())
cucsIscsiAuthProfilePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIscsiAuthProfilePolicyOwner.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsIscsiObjects':cucsIscsiObjects,'cucsIscsiAuthProfileTable':cucsIscsiAuthProfileTable,'cucsIscsiAuthProfileEntry':cucsIscsiAuthProfileEntry,_D:cucsIscsiAuthProfileInstanceId,'cucsIscsiAuthProfileDn':cucsIscsiAuthProfileDn,'cucsIscsiAuthProfileRn':cucsIscsiAuthProfileRn,'cucsIscsiAuthProfileDescr':cucsIscsiAuthProfileDescr,'cucsIscsiAuthProfileIntId':cucsIscsiAuthProfileIntId,'cucsIscsiAuthProfileName':cucsIscsiAuthProfileName,'cucsIscsiAuthProfilePassword':cucsIscsiAuthProfilePassword,'cucsIscsiAuthProfileUserId':cucsIscsiAuthProfileUserId,'cucsIscsiAuthProfileCtpassword':cucsIscsiAuthProfileCtpassword,'cucsIscsiAuthProfilePolicyLevel':cucsIscsiAuthProfilePolicyLevel,'cucsIscsiAuthProfilePolicyOwner':cucsIscsiAuthProfilePolicyOwner})