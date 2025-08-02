_F='cucsImgprovTargetInstanceId'
_E='not-accessible'
_D='cucsImgprovPolicyInstanceId'
_C='CISCO-UNIFIED-COMPUTING-IMGPROV-MIB'
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
cucsImgprovObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,55))
_CucsImgprovPolicyTable_Object=MibTable
cucsImgprovPolicyTable=_CucsImgprovPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,55,1))
if mibBuilder.loadTexts:cucsImgprovPolicyTable.setStatus(_A)
_CucsImgprovPolicyEntry_Object=MibTableRow
cucsImgprovPolicyEntry=_CucsImgprovPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,55,1,1))
cucsImgprovPolicyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsImgprovPolicyEntry.setStatus(_A)
_CucsImgprovPolicyInstanceId_Type=CucsManagedObjectId
_CucsImgprovPolicyInstanceId_Object=MibTableColumn
cucsImgprovPolicyInstanceId=_CucsImgprovPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,1),_CucsImgprovPolicyInstanceId_Type())
cucsImgprovPolicyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsImgprovPolicyInstanceId.setStatus(_A)
_CucsImgprovPolicyDn_Type=CucsManagedObjectDn
_CucsImgprovPolicyDn_Object=MibTableColumn
cucsImgprovPolicyDn=_CucsImgprovPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,2),_CucsImgprovPolicyDn_Type())
cucsImgprovPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovPolicyDn.setStatus(_A)
_CucsImgprovPolicyRn_Type=SnmpAdminString
_CucsImgprovPolicyRn_Object=MibTableColumn
cucsImgprovPolicyRn=_CucsImgprovPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,3),_CucsImgprovPolicyRn_Type())
cucsImgprovPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovPolicyRn.setStatus(_A)
_CucsImgprovPolicyDescr_Type=SnmpAdminString
_CucsImgprovPolicyDescr_Object=MibTableColumn
cucsImgprovPolicyDescr=_CucsImgprovPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,4),_CucsImgprovPolicyDescr_Type())
cucsImgprovPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovPolicyDescr.setStatus(_A)
_CucsImgprovPolicyIntId_Type=SnmpAdminString
_CucsImgprovPolicyIntId_Object=MibTableColumn
cucsImgprovPolicyIntId=_CucsImgprovPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,5),_CucsImgprovPolicyIntId_Type())
cucsImgprovPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovPolicyIntId.setStatus(_A)
_CucsImgprovPolicyName_Type=SnmpAdminString
_CucsImgprovPolicyName_Object=MibTableColumn
cucsImgprovPolicyName=_CucsImgprovPolicyName_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,6),_CucsImgprovPolicyName_Type())
cucsImgprovPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovPolicyName.setStatus(_A)
_CucsImgprovPolicyPolicyLevel_Type=Gauge32
_CucsImgprovPolicyPolicyLevel_Object=MibTableColumn
cucsImgprovPolicyPolicyLevel=_CucsImgprovPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,7),_CucsImgprovPolicyPolicyLevel_Type())
cucsImgprovPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovPolicyPolicyLevel.setStatus(_A)
_CucsImgprovPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsImgprovPolicyPolicyOwner_Object=MibTableColumn
cucsImgprovPolicyPolicyOwner=_CucsImgprovPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,55,1,1,8),_CucsImgprovPolicyPolicyOwner_Type())
cucsImgprovPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovPolicyPolicyOwner.setStatus(_A)
_CucsImgprovTargetTable_Object=MibTable
cucsImgprovTargetTable=_CucsImgprovTargetTable_Object((1,3,6,1,4,1,9,9,719,1,55,2))
if mibBuilder.loadTexts:cucsImgprovTargetTable.setStatus(_A)
_CucsImgprovTargetEntry_Object=MibTableRow
cucsImgprovTargetEntry=_CucsImgprovTargetEntry_Object((1,3,6,1,4,1,9,9,719,1,55,2,1))
cucsImgprovTargetEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsImgprovTargetEntry.setStatus(_A)
_CucsImgprovTargetInstanceId_Type=CucsManagedObjectId
_CucsImgprovTargetInstanceId_Object=MibTableColumn
cucsImgprovTargetInstanceId=_CucsImgprovTargetInstanceId_Object((1,3,6,1,4,1,9,9,719,1,55,2,1,1),_CucsImgprovTargetInstanceId_Type())
cucsImgprovTargetInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsImgprovTargetInstanceId.setStatus(_A)
_CucsImgprovTargetDn_Type=CucsManagedObjectDn
_CucsImgprovTargetDn_Object=MibTableColumn
cucsImgprovTargetDn=_CucsImgprovTargetDn_Object((1,3,6,1,4,1,9,9,719,1,55,2,1,2),_CucsImgprovTargetDn_Type())
cucsImgprovTargetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovTargetDn.setStatus(_A)
_CucsImgprovTargetRn_Type=SnmpAdminString
_CucsImgprovTargetRn_Object=MibTableColumn
cucsImgprovTargetRn=_CucsImgprovTargetRn_Object((1,3,6,1,4,1,9,9,719,1,55,2,1,3),_CucsImgprovTargetRn_Type())
cucsImgprovTargetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovTargetRn.setStatus(_A)
_CucsImgprovTargetName_Type=SnmpAdminString
_CucsImgprovTargetName_Object=MibTableColumn
cucsImgprovTargetName=_CucsImgprovTargetName_Object((1,3,6,1,4,1,9,9,719,1,55,2,1,4),_CucsImgprovTargetName_Type())
cucsImgprovTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsImgprovTargetName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsImgprovObjects':cucsImgprovObjects,'cucsImgprovPolicyTable':cucsImgprovPolicyTable,'cucsImgprovPolicyEntry':cucsImgprovPolicyEntry,_D:cucsImgprovPolicyInstanceId,'cucsImgprovPolicyDn':cucsImgprovPolicyDn,'cucsImgprovPolicyRn':cucsImgprovPolicyRn,'cucsImgprovPolicyDescr':cucsImgprovPolicyDescr,'cucsImgprovPolicyIntId':cucsImgprovPolicyIntId,'cucsImgprovPolicyName':cucsImgprovPolicyName,'cucsImgprovPolicyPolicyLevel':cucsImgprovPolicyPolicyLevel,'cucsImgprovPolicyPolicyOwner':cucsImgprovPolicyPolicyOwner,'cucsImgprovTargetTable':cucsImgprovTargetTable,'cucsImgprovTargetEntry':cucsImgprovTargetEntry,_F:cucsImgprovTargetInstanceId,'cucsImgprovTargetDn':cucsImgprovTargetDn,'cucsImgprovTargetRn':cucsImgprovTargetRn,'cucsImgprovTargetName':cucsImgprovTargetName})