_F='cfprImgsecPolicyInstanceId'
_E='not-accessible'
_D='cfprImgsecKeyInstanceId'
_C='CISCO-FIREPOWER-IMGSEC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprImgsecKeyType,CfprPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprImgsecKeyType','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprImgsecObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,38))
_CfprImgsecKeyTable_Object=MibTable
cfprImgsecKeyTable=_CfprImgsecKeyTable_Object((1,3,6,1,4,1,9,9,826,1,38,1))
if mibBuilder.loadTexts:cfprImgsecKeyTable.setStatus(_A)
_CfprImgsecKeyEntry_Object=MibTableRow
cfprImgsecKeyEntry=_CfprImgsecKeyEntry_Object((1,3,6,1,4,1,9,9,826,1,38,1,1))
cfprImgsecKeyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprImgsecKeyEntry.setStatus(_A)
_CfprImgsecKeyInstanceId_Type=CfprManagedObjectId
_CfprImgsecKeyInstanceId_Object=MibTableColumn
cfprImgsecKeyInstanceId=_CfprImgsecKeyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,38,1,1,1),_CfprImgsecKeyInstanceId_Type())
cfprImgsecKeyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprImgsecKeyInstanceId.setStatus(_A)
_CfprImgsecKeyDn_Type=CfprManagedObjectDn
_CfprImgsecKeyDn_Object=MibTableColumn
cfprImgsecKeyDn=_CfprImgsecKeyDn_Object((1,3,6,1,4,1,9,9,826,1,38,1,1,2),_CfprImgsecKeyDn_Type())
cfprImgsecKeyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecKeyDn.setStatus(_A)
_CfprImgsecKeyRn_Type=SnmpAdminString
_CfprImgsecKeyRn_Object=MibTableColumn
cfprImgsecKeyRn=_CfprImgsecKeyRn_Object((1,3,6,1,4,1,9,9,826,1,38,1,1,3),_CfprImgsecKeyRn_Type())
cfprImgsecKeyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecKeyRn.setStatus(_A)
_CfprImgsecKeyType_Type=CfprImgsecKeyType
_CfprImgsecKeyType_Object=MibTableColumn
cfprImgsecKeyType=_CfprImgsecKeyType_Object((1,3,6,1,4,1,9,9,826,1,38,1,1,4),_CfprImgsecKeyType_Type())
cfprImgsecKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecKeyType.setStatus(_A)
_CfprImgsecKeyValue_Type=SnmpAdminString
_CfprImgsecKeyValue_Object=MibTableColumn
cfprImgsecKeyValue=_CfprImgsecKeyValue_Object((1,3,6,1,4,1,9,9,826,1,38,1,1,5),_CfprImgsecKeyValue_Type())
cfprImgsecKeyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecKeyValue.setStatus(_A)
_CfprImgsecPolicyTable_Object=MibTable
cfprImgsecPolicyTable=_CfprImgsecPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,38,2))
if mibBuilder.loadTexts:cfprImgsecPolicyTable.setStatus(_A)
_CfprImgsecPolicyEntry_Object=MibTableRow
cfprImgsecPolicyEntry=_CfprImgsecPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,38,2,1))
cfprImgsecPolicyEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprImgsecPolicyEntry.setStatus(_A)
_CfprImgsecPolicyInstanceId_Type=CfprManagedObjectId
_CfprImgsecPolicyInstanceId_Object=MibTableColumn
cfprImgsecPolicyInstanceId=_CfprImgsecPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,1),_CfprImgsecPolicyInstanceId_Type())
cfprImgsecPolicyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprImgsecPolicyInstanceId.setStatus(_A)
_CfprImgsecPolicyDn_Type=CfprManagedObjectDn
_CfprImgsecPolicyDn_Object=MibTableColumn
cfprImgsecPolicyDn=_CfprImgsecPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,2),_CfprImgsecPolicyDn_Type())
cfprImgsecPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecPolicyDn.setStatus(_A)
_CfprImgsecPolicyRn_Type=SnmpAdminString
_CfprImgsecPolicyRn_Object=MibTableColumn
cfprImgsecPolicyRn=_CfprImgsecPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,3),_CfprImgsecPolicyRn_Type())
cfprImgsecPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecPolicyRn.setStatus(_A)
_CfprImgsecPolicyDescr_Type=SnmpAdminString
_CfprImgsecPolicyDescr_Object=MibTableColumn
cfprImgsecPolicyDescr=_CfprImgsecPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,4),_CfprImgsecPolicyDescr_Type())
cfprImgsecPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecPolicyDescr.setStatus(_A)
_CfprImgsecPolicyIntId_Type=SnmpAdminString
_CfprImgsecPolicyIntId_Object=MibTableColumn
cfprImgsecPolicyIntId=_CfprImgsecPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,5),_CfprImgsecPolicyIntId_Type())
cfprImgsecPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecPolicyIntId.setStatus(_A)
_CfprImgsecPolicyName_Type=SnmpAdminString
_CfprImgsecPolicyName_Object=MibTableColumn
cfprImgsecPolicyName=_CfprImgsecPolicyName_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,6),_CfprImgsecPolicyName_Type())
cfprImgsecPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecPolicyName.setStatus(_A)
_CfprImgsecPolicyPolicyLevel_Type=Gauge32
_CfprImgsecPolicyPolicyLevel_Object=MibTableColumn
cfprImgsecPolicyPolicyLevel=_CfprImgsecPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,7),_CfprImgsecPolicyPolicyLevel_Type())
cfprImgsecPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecPolicyPolicyLevel.setStatus(_A)
_CfprImgsecPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprImgsecPolicyPolicyOwner_Object=MibTableColumn
cfprImgsecPolicyPolicyOwner=_CfprImgsecPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,38,2,1,8),_CfprImgsecPolicyPolicyOwner_Type())
cfprImgsecPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprImgsecPolicyPolicyOwner.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprImgsecObjects':cfprImgsecObjects,'cfprImgsecKeyTable':cfprImgsecKeyTable,'cfprImgsecKeyEntry':cfprImgsecKeyEntry,_D:cfprImgsecKeyInstanceId,'cfprImgsecKeyDn':cfprImgsecKeyDn,'cfprImgsecKeyRn':cfprImgsecKeyRn,'cfprImgsecKeyType':cfprImgsecKeyType,'cfprImgsecKeyValue':cfprImgsecKeyValue,'cfprImgsecPolicyTable':cfprImgsecPolicyTable,'cfprImgsecPolicyEntry':cfprImgsecPolicyEntry,_F:cfprImgsecPolicyInstanceId,'cfprImgsecPolicyDn':cfprImgsecPolicyDn,'cfprImgsecPolicyRn':cfprImgsecPolicyRn,'cfprImgsecPolicyDescr':cfprImgsecPolicyDescr,'cfprImgsecPolicyIntId':cfprImgsecPolicyIntId,'cfprImgsecPolicyName':cfprImgsecPolicyName,'cfprImgsecPolicyPolicyLevel':cfprImgsecPolicyPolicyLevel,'cfprImgsecPolicyPolicyOwner':cfprImgsecPolicyPolicyOwner})