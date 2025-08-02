_D='cfprDpsecMacInstanceId'
_C='CISCO-FIREPOWER-DPSEC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprDpsecForgedTransmit,CfprPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprDpsecForgedTransmit','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprDpsecObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,18))
_CfprDpsecMacTable_Object=MibTable
cfprDpsecMacTable=_CfprDpsecMacTable_Object((1,3,6,1,4,1,9,9,826,1,18,1))
if mibBuilder.loadTexts:cfprDpsecMacTable.setStatus(_A)
_CfprDpsecMacEntry_Object=MibTableRow
cfprDpsecMacEntry=_CfprDpsecMacEntry_Object((1,3,6,1,4,1,9,9,826,1,18,1,1))
cfprDpsecMacEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprDpsecMacEntry.setStatus(_A)
_CfprDpsecMacInstanceId_Type=CfprManagedObjectId
_CfprDpsecMacInstanceId_Object=MibTableColumn
cfprDpsecMacInstanceId=_CfprDpsecMacInstanceId_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,1),_CfprDpsecMacInstanceId_Type())
cfprDpsecMacInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfprDpsecMacInstanceId.setStatus(_A)
_CfprDpsecMacDn_Type=CfprManagedObjectDn
_CfprDpsecMacDn_Object=MibTableColumn
cfprDpsecMacDn=_CfprDpsecMacDn_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,2),_CfprDpsecMacDn_Type())
cfprDpsecMacDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacDn.setStatus(_A)
_CfprDpsecMacRn_Type=SnmpAdminString
_CfprDpsecMacRn_Object=MibTableColumn
cfprDpsecMacRn=_CfprDpsecMacRn_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,3),_CfprDpsecMacRn_Type())
cfprDpsecMacRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacRn.setStatus(_A)
_CfprDpsecMacDescr_Type=SnmpAdminString
_CfprDpsecMacDescr_Object=MibTableColumn
cfprDpsecMacDescr=_CfprDpsecMacDescr_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,4),_CfprDpsecMacDescr_Type())
cfprDpsecMacDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacDescr.setStatus(_A)
_CfprDpsecMacForge_Type=CfprDpsecForgedTransmit
_CfprDpsecMacForge_Object=MibTableColumn
cfprDpsecMacForge=_CfprDpsecMacForge_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,5),_CfprDpsecMacForge_Type())
cfprDpsecMacForge.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacForge.setStatus(_A)
_CfprDpsecMacIntId_Type=SnmpAdminString
_CfprDpsecMacIntId_Object=MibTableColumn
cfprDpsecMacIntId=_CfprDpsecMacIntId_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,6),_CfprDpsecMacIntId_Type())
cfprDpsecMacIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacIntId.setStatus(_A)
_CfprDpsecMacName_Type=SnmpAdminString
_CfprDpsecMacName_Object=MibTableColumn
cfprDpsecMacName=_CfprDpsecMacName_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,7),_CfprDpsecMacName_Type())
cfprDpsecMacName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacName.setStatus(_A)
_CfprDpsecMacPolicyLevel_Type=Gauge32
_CfprDpsecMacPolicyLevel_Object=MibTableColumn
cfprDpsecMacPolicyLevel=_CfprDpsecMacPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,8),_CfprDpsecMacPolicyLevel_Type())
cfprDpsecMacPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacPolicyLevel.setStatus(_A)
_CfprDpsecMacPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprDpsecMacPolicyOwner_Object=MibTableColumn
cfprDpsecMacPolicyOwner=_CfprDpsecMacPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,18,1,1,9),_CfprDpsecMacPolicyOwner_Type())
cfprDpsecMacPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDpsecMacPolicyOwner.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprDpsecObjects':cfprDpsecObjects,'cfprDpsecMacTable':cfprDpsecMacTable,'cfprDpsecMacEntry':cfprDpsecMacEntry,_D:cfprDpsecMacInstanceId,'cfprDpsecMacDn':cfprDpsecMacDn,'cfprDpsecMacRn':cfprDpsecMacRn,'cfprDpsecMacDescr':cfprDpsecMacDescr,'cfprDpsecMacForge':cfprDpsecMacForge,'cfprDpsecMacIntId':cfprDpsecMacIntId,'cfprDpsecMacName':cfprDpsecMacName,'cfprDpsecMacPolicyLevel':cfprDpsecMacPolicyLevel,'cfprDpsecMacPolicyOwner':cfprDpsecMacPolicyOwner})