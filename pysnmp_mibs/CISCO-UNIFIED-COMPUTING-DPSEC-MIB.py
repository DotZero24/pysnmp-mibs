_D='cucsDpsecMacInstanceId'
_C='CISCO-UNIFIED-COMPUTING-DPSEC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsDpsecForgedTransmit,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsDpsecForgedTransmit','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsDpsecObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,13))
_CucsDpsecMacTable_Object=MibTable
cucsDpsecMacTable=_CucsDpsecMacTable_Object((1,3,6,1,4,1,9,9,719,1,13,1))
if mibBuilder.loadTexts:cucsDpsecMacTable.setStatus(_A)
_CucsDpsecMacEntry_Object=MibTableRow
cucsDpsecMacEntry=_CucsDpsecMacEntry_Object((1,3,6,1,4,1,9,9,719,1,13,1,1))
cucsDpsecMacEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsDpsecMacEntry.setStatus(_A)
_CucsDpsecMacInstanceId_Type=CucsManagedObjectId
_CucsDpsecMacInstanceId_Object=MibTableColumn
cucsDpsecMacInstanceId=_CucsDpsecMacInstanceId_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,1),_CucsDpsecMacInstanceId_Type())
cucsDpsecMacInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsDpsecMacInstanceId.setStatus(_A)
_CucsDpsecMacDn_Type=CucsManagedObjectDn
_CucsDpsecMacDn_Object=MibTableColumn
cucsDpsecMacDn=_CucsDpsecMacDn_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,2),_CucsDpsecMacDn_Type())
cucsDpsecMacDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacDn.setStatus(_A)
_CucsDpsecMacRn_Type=SnmpAdminString
_CucsDpsecMacRn_Object=MibTableColumn
cucsDpsecMacRn=_CucsDpsecMacRn_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,3),_CucsDpsecMacRn_Type())
cucsDpsecMacRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacRn.setStatus(_A)
_CucsDpsecMacDescr_Type=SnmpAdminString
_CucsDpsecMacDescr_Object=MibTableColumn
cucsDpsecMacDescr=_CucsDpsecMacDescr_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,4),_CucsDpsecMacDescr_Type())
cucsDpsecMacDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacDescr.setStatus(_A)
_CucsDpsecMacForge_Type=CucsDpsecForgedTransmit
_CucsDpsecMacForge_Object=MibTableColumn
cucsDpsecMacForge=_CucsDpsecMacForge_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,5),_CucsDpsecMacForge_Type())
cucsDpsecMacForge.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacForge.setStatus(_A)
_CucsDpsecMacIntId_Type=SnmpAdminString
_CucsDpsecMacIntId_Object=MibTableColumn
cucsDpsecMacIntId=_CucsDpsecMacIntId_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,6),_CucsDpsecMacIntId_Type())
cucsDpsecMacIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacIntId.setStatus(_A)
_CucsDpsecMacName_Type=SnmpAdminString
_CucsDpsecMacName_Object=MibTableColumn
cucsDpsecMacName=_CucsDpsecMacName_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,7),_CucsDpsecMacName_Type())
cucsDpsecMacName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacName.setStatus(_A)
_CucsDpsecMacPolicyLevel_Type=Gauge32
_CucsDpsecMacPolicyLevel_Object=MibTableColumn
cucsDpsecMacPolicyLevel=_CucsDpsecMacPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,8),_CucsDpsecMacPolicyLevel_Type())
cucsDpsecMacPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacPolicyLevel.setStatus(_A)
_CucsDpsecMacPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsDpsecMacPolicyOwner_Object=MibTableColumn
cucsDpsecMacPolicyOwner=_CucsDpsecMacPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,9),_CucsDpsecMacPolicyOwner_Type())
cucsDpsecMacPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacPolicyOwner.setStatus(_A)
_CucsDpsecMacPropAcl_Type=Unsigned64
_CucsDpsecMacPropAcl_Object=MibTableColumn
cucsDpsecMacPropAcl=_CucsDpsecMacPropAcl_Object((1,3,6,1,4,1,9,9,719,1,13,1,1,10),_CucsDpsecMacPropAcl_Type())
cucsDpsecMacPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDpsecMacPropAcl.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsDpsecObjects':cucsDpsecObjects,'cucsDpsecMacTable':cucsDpsecMacTable,'cucsDpsecMacEntry':cucsDpsecMacEntry,_D:cucsDpsecMacInstanceId,'cucsDpsecMacDn':cucsDpsecMacDn,'cucsDpsecMacRn':cucsDpsecMacRn,'cucsDpsecMacDescr':cucsDpsecMacDescr,'cucsDpsecMacForge':cucsDpsecMacForge,'cucsDpsecMacIntId':cucsDpsecMacIntId,'cucsDpsecMacName':cucsDpsecMacName,'cucsDpsecMacPolicyLevel':cucsDpsecMacPolicyLevel,'cucsDpsecMacPolicyOwner':cucsDpsecMacPolicyOwner,'cucsDpsecMacPropAcl':cucsDpsecMacPropAcl})