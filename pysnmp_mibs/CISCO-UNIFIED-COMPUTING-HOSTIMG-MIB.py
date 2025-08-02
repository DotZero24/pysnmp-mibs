_F='cucsHostimgTargetInstanceId'
_E='not-accessible'
_D='cucsHostimgPolicyInstanceId'
_C='CISCO-UNIFIED-COMPUTING-HOSTIMG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsHostimgComposition,CucsHostimgDistribution,CucsHostimgImgType,CucsHostimgType,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsHostimgComposition','CucsHostimgDistribution','CucsHostimgImgType','CucsHostimgType','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsHostimgObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,54))
_CucsHostimgPolicyTable_Object=MibTable
cucsHostimgPolicyTable=_CucsHostimgPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,54,1))
if mibBuilder.loadTexts:cucsHostimgPolicyTable.setStatus(_A)
_CucsHostimgPolicyEntry_Object=MibTableRow
cucsHostimgPolicyEntry=_CucsHostimgPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,54,1,1))
cucsHostimgPolicyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsHostimgPolicyEntry.setStatus(_A)
_CucsHostimgPolicyInstanceId_Type=CucsManagedObjectId
_CucsHostimgPolicyInstanceId_Object=MibTableColumn
cucsHostimgPolicyInstanceId=_CucsHostimgPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,1),_CucsHostimgPolicyInstanceId_Type())
cucsHostimgPolicyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsHostimgPolicyInstanceId.setStatus(_A)
_CucsHostimgPolicyDn_Type=CucsManagedObjectDn
_CucsHostimgPolicyDn_Object=MibTableColumn
cucsHostimgPolicyDn=_CucsHostimgPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,2),_CucsHostimgPolicyDn_Type())
cucsHostimgPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyDn.setStatus(_A)
_CucsHostimgPolicyRn_Type=SnmpAdminString
_CucsHostimgPolicyRn_Object=MibTableColumn
cucsHostimgPolicyRn=_CucsHostimgPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,3),_CucsHostimgPolicyRn_Type())
cucsHostimgPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyRn.setStatus(_A)
_CucsHostimgPolicyComp_Type=CucsHostimgComposition
_CucsHostimgPolicyComp_Object=MibTableColumn
cucsHostimgPolicyComp=_CucsHostimgPolicyComp_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,4),_CucsHostimgPolicyComp_Type())
cucsHostimgPolicyComp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyComp.setStatus(_A)
_CucsHostimgPolicyDescr_Type=SnmpAdminString
_CucsHostimgPolicyDescr_Object=MibTableColumn
cucsHostimgPolicyDescr=_CucsHostimgPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,5),_CucsHostimgPolicyDescr_Type())
cucsHostimgPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyDescr.setStatus(_A)
_CucsHostimgPolicyIntId_Type=SnmpAdminString
_CucsHostimgPolicyIntId_Object=MibTableColumn
cucsHostimgPolicyIntId=_CucsHostimgPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,6),_CucsHostimgPolicyIntId_Type())
cucsHostimgPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyIntId.setStatus(_A)
_CucsHostimgPolicyName_Type=SnmpAdminString
_CucsHostimgPolicyName_Object=MibTableColumn
cucsHostimgPolicyName=_CucsHostimgPolicyName_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,7),_CucsHostimgPolicyName_Type())
cucsHostimgPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyName.setStatus(_A)
_CucsHostimgPolicyConf_Type=SnmpAdminString
_CucsHostimgPolicyConf_Object=MibTableColumn
cucsHostimgPolicyConf=_CucsHostimgPolicyConf_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,8),_CucsHostimgPolicyConf_Type())
cucsHostimgPolicyConf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyConf.setStatus(_A)
_CucsHostimgPolicyDistro_Type=CucsHostimgDistribution
_CucsHostimgPolicyDistro_Object=MibTableColumn
cucsHostimgPolicyDistro=_CucsHostimgPolicyDistro_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,9),_CucsHostimgPolicyDistro_Type())
cucsHostimgPolicyDistro.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyDistro.setStatus(_A)
_CucsHostimgPolicyType_Type=CucsHostimgImgType
_CucsHostimgPolicyType_Object=MibTableColumn
cucsHostimgPolicyType=_CucsHostimgPolicyType_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,10),_CucsHostimgPolicyType_Type())
cucsHostimgPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyType.setStatus(_A)
_CucsHostimgPolicyPolicyLevel_Type=Gauge32
_CucsHostimgPolicyPolicyLevel_Object=MibTableColumn
cucsHostimgPolicyPolicyLevel=_CucsHostimgPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,11),_CucsHostimgPolicyPolicyLevel_Type())
cucsHostimgPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyPolicyLevel.setStatus(_A)
_CucsHostimgPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsHostimgPolicyPolicyOwner_Object=MibTableColumn
cucsHostimgPolicyPolicyOwner=_CucsHostimgPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,54,1,1,12),_CucsHostimgPolicyPolicyOwner_Type())
cucsHostimgPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgPolicyPolicyOwner.setStatus(_A)
_CucsHostimgTargetTable_Object=MibTable
cucsHostimgTargetTable=_CucsHostimgTargetTable_Object((1,3,6,1,4,1,9,9,719,1,54,2))
if mibBuilder.loadTexts:cucsHostimgTargetTable.setStatus(_A)
_CucsHostimgTargetEntry_Object=MibTableRow
cucsHostimgTargetEntry=_CucsHostimgTargetEntry_Object((1,3,6,1,4,1,9,9,719,1,54,2,1))
cucsHostimgTargetEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsHostimgTargetEntry.setStatus(_A)
_CucsHostimgTargetInstanceId_Type=CucsManagedObjectId
_CucsHostimgTargetInstanceId_Object=MibTableColumn
cucsHostimgTargetInstanceId=_CucsHostimgTargetInstanceId_Object((1,3,6,1,4,1,9,9,719,1,54,2,1,1),_CucsHostimgTargetInstanceId_Type())
cucsHostimgTargetInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsHostimgTargetInstanceId.setStatus(_A)
_CucsHostimgTargetDn_Type=CucsManagedObjectDn
_CucsHostimgTargetDn_Object=MibTableColumn
cucsHostimgTargetDn=_CucsHostimgTargetDn_Object((1,3,6,1,4,1,9,9,719,1,54,2,1,2),_CucsHostimgTargetDn_Type())
cucsHostimgTargetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgTargetDn.setStatus(_A)
_CucsHostimgTargetRn_Type=SnmpAdminString
_CucsHostimgTargetRn_Object=MibTableColumn
cucsHostimgTargetRn=_CucsHostimgTargetRn_Object((1,3,6,1,4,1,9,9,719,1,54,2,1,3),_CucsHostimgTargetRn_Type())
cucsHostimgTargetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgTargetRn.setStatus(_A)
_CucsHostimgTargetName_Type=SnmpAdminString
_CucsHostimgTargetName_Object=MibTableColumn
cucsHostimgTargetName=_CucsHostimgTargetName_Object((1,3,6,1,4,1,9,9,719,1,54,2,1,4),_CucsHostimgTargetName_Type())
cucsHostimgTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgTargetName.setStatus(_A)
_CucsHostimgTargetType_Type=CucsHostimgType
_CucsHostimgTargetType_Object=MibTableColumn
cucsHostimgTargetType=_CucsHostimgTargetType_Object((1,3,6,1,4,1,9,9,719,1,54,2,1,5),_CucsHostimgTargetType_Type())
cucsHostimgTargetType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgTargetType.setStatus(_A)
_CucsHostimgTargetUri_Type=SnmpAdminString
_CucsHostimgTargetUri_Object=MibTableColumn
cucsHostimgTargetUri=_CucsHostimgTargetUri_Object((1,3,6,1,4,1,9,9,719,1,54,2,1,6),_CucsHostimgTargetUri_Type())
cucsHostimgTargetUri.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgTargetUri.setStatus(_A)
_CucsHostimgTargetOrder_Type=Gauge32
_CucsHostimgTargetOrder_Object=MibTableColumn
cucsHostimgTargetOrder=_CucsHostimgTargetOrder_Object((1,3,6,1,4,1,9,9,719,1,54,2,1,7),_CucsHostimgTargetOrder_Type())
cucsHostimgTargetOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsHostimgTargetOrder.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsHostimgObjects':cucsHostimgObjects,'cucsHostimgPolicyTable':cucsHostimgPolicyTable,'cucsHostimgPolicyEntry':cucsHostimgPolicyEntry,_D:cucsHostimgPolicyInstanceId,'cucsHostimgPolicyDn':cucsHostimgPolicyDn,'cucsHostimgPolicyRn':cucsHostimgPolicyRn,'cucsHostimgPolicyComp':cucsHostimgPolicyComp,'cucsHostimgPolicyDescr':cucsHostimgPolicyDescr,'cucsHostimgPolicyIntId':cucsHostimgPolicyIntId,'cucsHostimgPolicyName':cucsHostimgPolicyName,'cucsHostimgPolicyConf':cucsHostimgPolicyConf,'cucsHostimgPolicyDistro':cucsHostimgPolicyDistro,'cucsHostimgPolicyType':cucsHostimgPolicyType,'cucsHostimgPolicyPolicyLevel':cucsHostimgPolicyPolicyLevel,'cucsHostimgPolicyPolicyOwner':cucsHostimgPolicyPolicyOwner,'cucsHostimgTargetTable':cucsHostimgTargetTable,'cucsHostimgTargetEntry':cucsHostimgTargetEntry,_F:cucsHostimgTargetInstanceId,'cucsHostimgTargetDn':cucsHostimgTargetDn,'cucsHostimgTargetRn':cucsHostimgTargetRn,'cucsHostimgTargetName':cucsHostimgTargetName,'cucsHostimgTargetType':cucsHostimgTargetType,'cucsHostimgTargetUri':cucsHostimgTargetUri,'cucsHostimgTargetOrder':cucsHostimgTargetOrder})