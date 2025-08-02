_F='cfprHostimgTargetInstanceId'
_E='not-accessible'
_D='cfprHostimgPolicyInstanceId'
_C='CISCO-FIREPOWER-HOSTIMG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprHostimgComposition,CfprHostimgDistribution,CfprHostimgImgType,CfprHostimgType,CfprPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprHostimgComposition','CfprHostimgDistribution','CfprHostimgImgType','CfprHostimgType','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprHostimgObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,35))
_CfprHostimgPolicyTable_Object=MibTable
cfprHostimgPolicyTable=_CfprHostimgPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,35,1))
if mibBuilder.loadTexts:cfprHostimgPolicyTable.setStatus(_A)
_CfprHostimgPolicyEntry_Object=MibTableRow
cfprHostimgPolicyEntry=_CfprHostimgPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,35,1,1))
cfprHostimgPolicyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprHostimgPolicyEntry.setStatus(_A)
_CfprHostimgPolicyInstanceId_Type=CfprManagedObjectId
_CfprHostimgPolicyInstanceId_Object=MibTableColumn
cfprHostimgPolicyInstanceId=_CfprHostimgPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,1),_CfprHostimgPolicyInstanceId_Type())
cfprHostimgPolicyInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprHostimgPolicyInstanceId.setStatus(_A)
_CfprHostimgPolicyDn_Type=CfprManagedObjectDn
_CfprHostimgPolicyDn_Object=MibTableColumn
cfprHostimgPolicyDn=_CfprHostimgPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,2),_CfprHostimgPolicyDn_Type())
cfprHostimgPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyDn.setStatus(_A)
_CfprHostimgPolicyRn_Type=SnmpAdminString
_CfprHostimgPolicyRn_Object=MibTableColumn
cfprHostimgPolicyRn=_CfprHostimgPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,3),_CfprHostimgPolicyRn_Type())
cfprHostimgPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyRn.setStatus(_A)
_CfprHostimgPolicyComp_Type=CfprHostimgComposition
_CfprHostimgPolicyComp_Object=MibTableColumn
cfprHostimgPolicyComp=_CfprHostimgPolicyComp_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,4),_CfprHostimgPolicyComp_Type())
cfprHostimgPolicyComp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyComp.setStatus(_A)
_CfprHostimgPolicyConf_Type=SnmpAdminString
_CfprHostimgPolicyConf_Object=MibTableColumn
cfprHostimgPolicyConf=_CfprHostimgPolicyConf_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,5),_CfprHostimgPolicyConf_Type())
cfprHostimgPolicyConf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyConf.setStatus(_A)
_CfprHostimgPolicyDescr_Type=SnmpAdminString
_CfprHostimgPolicyDescr_Object=MibTableColumn
cfprHostimgPolicyDescr=_CfprHostimgPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,6),_CfprHostimgPolicyDescr_Type())
cfprHostimgPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyDescr.setStatus(_A)
_CfprHostimgPolicyDistro_Type=CfprHostimgDistribution
_CfprHostimgPolicyDistro_Object=MibTableColumn
cfprHostimgPolicyDistro=_CfprHostimgPolicyDistro_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,7),_CfprHostimgPolicyDistro_Type())
cfprHostimgPolicyDistro.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyDistro.setStatus(_A)
_CfprHostimgPolicyIntId_Type=SnmpAdminString
_CfprHostimgPolicyIntId_Object=MibTableColumn
cfprHostimgPolicyIntId=_CfprHostimgPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,8),_CfprHostimgPolicyIntId_Type())
cfprHostimgPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyIntId.setStatus(_A)
_CfprHostimgPolicyName_Type=SnmpAdminString
_CfprHostimgPolicyName_Object=MibTableColumn
cfprHostimgPolicyName=_CfprHostimgPolicyName_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,9),_CfprHostimgPolicyName_Type())
cfprHostimgPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyName.setStatus(_A)
_CfprHostimgPolicyPolicyLevel_Type=Gauge32
_CfprHostimgPolicyPolicyLevel_Object=MibTableColumn
cfprHostimgPolicyPolicyLevel=_CfprHostimgPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,10),_CfprHostimgPolicyPolicyLevel_Type())
cfprHostimgPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyPolicyLevel.setStatus(_A)
_CfprHostimgPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprHostimgPolicyPolicyOwner_Object=MibTableColumn
cfprHostimgPolicyPolicyOwner=_CfprHostimgPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,11),_CfprHostimgPolicyPolicyOwner_Type())
cfprHostimgPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyPolicyOwner.setStatus(_A)
_CfprHostimgPolicyType_Type=CfprHostimgImgType
_CfprHostimgPolicyType_Object=MibTableColumn
cfprHostimgPolicyType=_CfprHostimgPolicyType_Object((1,3,6,1,4,1,9,9,826,1,35,1,1,12),_CfprHostimgPolicyType_Type())
cfprHostimgPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgPolicyType.setStatus(_A)
_CfprHostimgTargetTable_Object=MibTable
cfprHostimgTargetTable=_CfprHostimgTargetTable_Object((1,3,6,1,4,1,9,9,826,1,35,2))
if mibBuilder.loadTexts:cfprHostimgTargetTable.setStatus(_A)
_CfprHostimgTargetEntry_Object=MibTableRow
cfprHostimgTargetEntry=_CfprHostimgTargetEntry_Object((1,3,6,1,4,1,9,9,826,1,35,2,1))
cfprHostimgTargetEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprHostimgTargetEntry.setStatus(_A)
_CfprHostimgTargetInstanceId_Type=CfprManagedObjectId
_CfprHostimgTargetInstanceId_Object=MibTableColumn
cfprHostimgTargetInstanceId=_CfprHostimgTargetInstanceId_Object((1,3,6,1,4,1,9,9,826,1,35,2,1,1),_CfprHostimgTargetInstanceId_Type())
cfprHostimgTargetInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprHostimgTargetInstanceId.setStatus(_A)
_CfprHostimgTargetDn_Type=CfprManagedObjectDn
_CfprHostimgTargetDn_Object=MibTableColumn
cfprHostimgTargetDn=_CfprHostimgTargetDn_Object((1,3,6,1,4,1,9,9,826,1,35,2,1,2),_CfprHostimgTargetDn_Type())
cfprHostimgTargetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgTargetDn.setStatus(_A)
_CfprHostimgTargetRn_Type=SnmpAdminString
_CfprHostimgTargetRn_Object=MibTableColumn
cfprHostimgTargetRn=_CfprHostimgTargetRn_Object((1,3,6,1,4,1,9,9,826,1,35,2,1,3),_CfprHostimgTargetRn_Type())
cfprHostimgTargetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgTargetRn.setStatus(_A)
_CfprHostimgTargetName_Type=SnmpAdminString
_CfprHostimgTargetName_Object=MibTableColumn
cfprHostimgTargetName=_CfprHostimgTargetName_Object((1,3,6,1,4,1,9,9,826,1,35,2,1,4),_CfprHostimgTargetName_Type())
cfprHostimgTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgTargetName.setStatus(_A)
_CfprHostimgTargetOrder_Type=Gauge32
_CfprHostimgTargetOrder_Object=MibTableColumn
cfprHostimgTargetOrder=_CfprHostimgTargetOrder_Object((1,3,6,1,4,1,9,9,826,1,35,2,1,5),_CfprHostimgTargetOrder_Type())
cfprHostimgTargetOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgTargetOrder.setStatus(_A)
_CfprHostimgTargetType_Type=CfprHostimgType
_CfprHostimgTargetType_Object=MibTableColumn
cfprHostimgTargetType=_CfprHostimgTargetType_Object((1,3,6,1,4,1,9,9,826,1,35,2,1,6),_CfprHostimgTargetType_Type())
cfprHostimgTargetType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgTargetType.setStatus(_A)
_CfprHostimgTargetUri_Type=SnmpAdminString
_CfprHostimgTargetUri_Object=MibTableColumn
cfprHostimgTargetUri=_CfprHostimgTargetUri_Object((1,3,6,1,4,1,9,9,826,1,35,2,1,7),_CfprHostimgTargetUri_Type())
cfprHostimgTargetUri.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprHostimgTargetUri.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprHostimgObjects':cfprHostimgObjects,'cfprHostimgPolicyTable':cfprHostimgPolicyTable,'cfprHostimgPolicyEntry':cfprHostimgPolicyEntry,_D:cfprHostimgPolicyInstanceId,'cfprHostimgPolicyDn':cfprHostimgPolicyDn,'cfprHostimgPolicyRn':cfprHostimgPolicyRn,'cfprHostimgPolicyComp':cfprHostimgPolicyComp,'cfprHostimgPolicyConf':cfprHostimgPolicyConf,'cfprHostimgPolicyDescr':cfprHostimgPolicyDescr,'cfprHostimgPolicyDistro':cfprHostimgPolicyDistro,'cfprHostimgPolicyIntId':cfprHostimgPolicyIntId,'cfprHostimgPolicyName':cfprHostimgPolicyName,'cfprHostimgPolicyPolicyLevel':cfprHostimgPolicyPolicyLevel,'cfprHostimgPolicyPolicyOwner':cfprHostimgPolicyPolicyOwner,'cfprHostimgPolicyType':cfprHostimgPolicyType,'cfprHostimgTargetTable':cfprHostimgTargetTable,'cfprHostimgTargetEntry':cfprHostimgTargetEntry,_F:cfprHostimgTargetInstanceId,'cfprHostimgTargetDn':cfprHostimgTargetDn,'cfprHostimgTargetRn':cfprHostimgTargetRn,'cfprHostimgTargetName':cfprHostimgTargetName,'cfprHostimgTargetOrder':cfprHostimgTargetOrder,'cfprHostimgTargetType':cfprHostimgTargetType,'cfprHostimgTargetUri':cfprHostimgTargetUri})