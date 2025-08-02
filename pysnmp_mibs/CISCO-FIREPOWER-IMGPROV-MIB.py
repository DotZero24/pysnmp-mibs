_F='cfprImgprovTargetInstanceId'
_E='not-accessible'
_D='cfprImgprovPolicyInstanceId'
_C='CISCO-FIREPOWER-IMGPROV-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprPolicyPolicyOwner,=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprImgprovObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,37))
_CfprImgprovPolicyTable_Object=MibTable
cfprImgprovPolicyTable=_CfprImgprovPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,37,1))
if mibBuilder.loadTexts:cfprImgprovPolicyTable.setStatus(_A)
_CfprImgprovPolicyEntry_Object=MibTableRow
cfprImgprovPolicyEntry=_CfprImgprovPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,37,1,1))
cfprImgprovPolicyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprImgprovPolicyEntry.setStatus(_A)
_CfprImgprovPolicyInstanceId_Type=CfprManagedObjectId
_CfprImgprovPolicyInstanceId_Object=MibTableColumn
cfprImgprovPolicyInstanceId=_CfprImgprovPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,1),_CfprImgprovPolicyInstanceId_Type())
cfprImgprovPolicyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprImgprovPolicyInstanceId.setStatus(_A)
_CfprImgprovPolicyDn_Type=CfprManagedObjectDn
_CfprImgprovPolicyDn_Object=MibTableColumn
cfprImgprovPolicyDn=_CfprImgprovPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,2),_CfprImgprovPolicyDn_Type())
cfprImgprovPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovPolicyDn.setStatus(_A)
_CfprImgprovPolicyRn_Type=SnmpAdminString
_CfprImgprovPolicyRn_Object=MibTableColumn
cfprImgprovPolicyRn=_CfprImgprovPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,3),_CfprImgprovPolicyRn_Type())
cfprImgprovPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovPolicyRn.setStatus(_A)
_CfprImgprovPolicyDescr_Type=SnmpAdminString
_CfprImgprovPolicyDescr_Object=MibTableColumn
cfprImgprovPolicyDescr=_CfprImgprovPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,4),_CfprImgprovPolicyDescr_Type())
cfprImgprovPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovPolicyDescr.setStatus(_A)
_CfprImgprovPolicyIntId_Type=SnmpAdminString
_CfprImgprovPolicyIntId_Object=MibTableColumn
cfprImgprovPolicyIntId=_CfprImgprovPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,5),_CfprImgprovPolicyIntId_Type())
cfprImgprovPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovPolicyIntId.setStatus(_A)
_CfprImgprovPolicyName_Type=SnmpAdminString
_CfprImgprovPolicyName_Object=MibTableColumn
cfprImgprovPolicyName=_CfprImgprovPolicyName_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,6),_CfprImgprovPolicyName_Type())
cfprImgprovPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovPolicyName.setStatus(_A)
_CfprImgprovPolicyPolicyLevel_Type=Gauge32
_CfprImgprovPolicyPolicyLevel_Object=MibTableColumn
cfprImgprovPolicyPolicyLevel=_CfprImgprovPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,7),_CfprImgprovPolicyPolicyLevel_Type())
cfprImgprovPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovPolicyPolicyLevel.setStatus(_A)
_CfprImgprovPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprImgprovPolicyPolicyOwner_Object=MibTableColumn
cfprImgprovPolicyPolicyOwner=_CfprImgprovPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,37,1,1,8),_CfprImgprovPolicyPolicyOwner_Type())
cfprImgprovPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovPolicyPolicyOwner.setStatus(_A)
_CfprImgprovTargetTable_Object=MibTable
cfprImgprovTargetTable=_CfprImgprovTargetTable_Object((1,3,6,1,4,1,9,9,826,1,37,2))
if mibBuilder.loadTexts:cfprImgprovTargetTable.setStatus(_A)
_CfprImgprovTargetEntry_Object=MibTableRow
cfprImgprovTargetEntry=_CfprImgprovTargetEntry_Object((1,3,6,1,4,1,9,9,826,1,37,2,1))
cfprImgprovTargetEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprImgprovTargetEntry.setStatus(_A)
_CfprImgprovTargetInstanceId_Type=CfprManagedObjectId
_CfprImgprovTargetInstanceId_Object=MibTableColumn
cfprImgprovTargetInstanceId=_CfprImgprovTargetInstanceId_Object((1,3,6,1,4,1,9,9,826,1,37,2,1,1),_CfprImgprovTargetInstanceId_Type())
cfprImgprovTargetInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprImgprovTargetInstanceId.setStatus(_A)
_CfprImgprovTargetDn_Type=CfprManagedObjectDn
_CfprImgprovTargetDn_Object=MibTableColumn
cfprImgprovTargetDn=_CfprImgprovTargetDn_Object((1,3,6,1,4,1,9,9,826,1,37,2,1,2),_CfprImgprovTargetDn_Type())
cfprImgprovTargetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovTargetDn.setStatus(_A)
_CfprImgprovTargetRn_Type=SnmpAdminString
_CfprImgprovTargetRn_Object=MibTableColumn
cfprImgprovTargetRn=_CfprImgprovTargetRn_Object((1,3,6,1,4,1,9,9,826,1,37,2,1,3),_CfprImgprovTargetRn_Type())
cfprImgprovTargetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovTargetRn.setStatus(_A)
_CfprImgprovTargetName_Type=SnmpAdminString
_CfprImgprovTargetName_Object=MibTableColumn
cfprImgprovTargetName=_CfprImgprovTargetName_Object((1,3,6,1,4,1,9,9,826,1,37,2,1,4),_CfprImgprovTargetName_Type())
cfprImgprovTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgprovTargetName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprImgprovObjects':cfprImgprovObjects,'cfprImgprovPolicyTable':cfprImgprovPolicyTable,'cfprImgprovPolicyEntry':cfprImgprovPolicyEntry,_D:cfprImgprovPolicyInstanceId,'cfprImgprovPolicyDn':cfprImgprovPolicyDn,'cfprImgprovPolicyRn':cfprImgprovPolicyRn,'cfprImgprovPolicyDescr':cfprImgprovPolicyDescr,'cfprImgprovPolicyIntId':cfprImgprovPolicyIntId,'cfprImgprovPolicyName':cfprImgprovPolicyName,'cfprImgprovPolicyPolicyLevel':cfprImgprovPolicyPolicyLevel,'cfprImgprovPolicyPolicyOwner':cfprImgprovPolicyPolicyOwner,'cfprImgprovTargetTable':cfprImgprovTargetTable,'cfprImgprovTargetEntry':cfprImgprovTargetEntry,_F:cfprImgprovTargetInstanceId,'cfprImgprovTargetDn':cfprImgprovTargetDn,'cfprImgprovTargetRn':cfprImgprovTargetRn,'cfprImgprovTargetName':cfprImgprovTargetName})