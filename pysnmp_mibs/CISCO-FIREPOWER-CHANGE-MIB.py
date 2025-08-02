_D='cfprChangeChangedObjectRefInstanceId'
_C='CISCO-FIREPOWER-CHANGE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprChangeStatus,CfprMoMoClassId=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprChangeStatus','CfprMoMoClassId')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprChangeObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,9))
_CfprChangeChangedObjectRefTable_Object=MibTable
cfprChangeChangedObjectRefTable=_CfprChangeChangedObjectRefTable_Object((1,3,6,1,4,1,9,9,826,1,9,1))
if mibBuilder.loadTexts:cfprChangeChangedObjectRefTable.setStatus(_A)
_CfprChangeChangedObjectRefEntry_Object=MibTableRow
cfprChangeChangedObjectRefEntry=_CfprChangeChangedObjectRefEntry_Object((1,3,6,1,4,1,9,9,826,1,9,1,1))
cfprChangeChangedObjectRefEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprChangeChangedObjectRefEntry.setStatus(_A)
_CfprChangeChangedObjectRefInstanceId_Type=CfprManagedObjectId
_CfprChangeChangedObjectRefInstanceId_Object=MibTableColumn
cfprChangeChangedObjectRefInstanceId=_CfprChangeChangedObjectRefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,1),_CfprChangeChangedObjectRefInstanceId_Type())
cfprChangeChangedObjectRefInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfprChangeChangedObjectRefInstanceId.setStatus(_A)
_CfprChangeChangedObjectRefDn_Type=CfprManagedObjectDn
_CfprChangeChangedObjectRefDn_Object=MibTableColumn
cfprChangeChangedObjectRefDn=_CfprChangeChangedObjectRefDn_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,2),_CfprChangeChangedObjectRefDn_Type())
cfprChangeChangedObjectRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefDn.setStatus(_A)
_CfprChangeChangedObjectRefRn_Type=SnmpAdminString
_CfprChangeChangedObjectRefRn_Object=MibTableColumn
cfprChangeChangedObjectRefRn=_CfprChangeChangedObjectRefRn_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,3),_CfprChangeChangedObjectRefRn_Type())
cfprChangeChangedObjectRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefRn.setStatus(_A)
_CfprChangeChangedObjectRefCentraleMoDn_Type=SnmpAdminString
_CfprChangeChangedObjectRefCentraleMoDn_Object=MibTableColumn
cfprChangeChangedObjectRefCentraleMoDn=_CfprChangeChangedObjectRefCentraleMoDn_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,4),_CfprChangeChangedObjectRefCentraleMoDn_Type())
cfprChangeChangedObjectRefCentraleMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefCentraleMoDn.setStatus(_A)
_CfprChangeChangedObjectRefChangedMoClassId_Type=CfprMoMoClassId
_CfprChangeChangedObjectRefChangedMoClassId_Object=MibTableColumn
cfprChangeChangedObjectRefChangedMoClassId=_CfprChangeChangedObjectRefChangedMoClassId_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,5),_CfprChangeChangedObjectRefChangedMoClassId_Type())
cfprChangeChangedObjectRefChangedMoClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefChangedMoClassId.setStatus(_A)
_CfprChangeChangedObjectRefGuid_Type=SnmpAdminString
_CfprChangeChangedObjectRefGuid_Object=MibTableColumn
cfprChangeChangedObjectRefGuid=_CfprChangeChangedObjectRefGuid_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,6),_CfprChangeChangedObjectRefGuid_Type())
cfprChangeChangedObjectRefGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefGuid.setStatus(_A)
_CfprChangeChangedObjectRefId_Type=Gauge32
_CfprChangeChangedObjectRefId_Object=MibTableColumn
cfprChangeChangedObjectRefId=_CfprChangeChangedObjectRefId_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,7),_CfprChangeChangedObjectRefId_Type())
cfprChangeChangedObjectRefId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefId.setStatus(_A)
_CfprChangeChangedObjectRefOldCentraleMoDn_Type=SnmpAdminString
_CfprChangeChangedObjectRefOldCentraleMoDn_Object=MibTableColumn
cfprChangeChangedObjectRefOldCentraleMoDn=_CfprChangeChangedObjectRefOldCentraleMoDn_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,8),_CfprChangeChangedObjectRefOldCentraleMoDn_Type())
cfprChangeChangedObjectRefOldCentraleMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefOldCentraleMoDn.setStatus(_A)
_CfprChangeChangedObjectRefRefObjStatus_Type=CfprChangeStatus
_CfprChangeChangedObjectRefRefObjStatus_Object=MibTableColumn
cfprChangeChangedObjectRefRefObjStatus=_CfprChangeChangedObjectRefRefObjStatus_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,9),_CfprChangeChangedObjectRefRefObjStatus_Type())
cfprChangeChangedObjectRefRefObjStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefRefObjStatus.setStatus(_A)
_CfprChangeChangedObjectRefFprmMoDn_Type=SnmpAdminString
_CfprChangeChangedObjectRefFprmMoDn_Object=MibTableColumn
cfprChangeChangedObjectRefFprmMoDn=_CfprChangeChangedObjectRefFprmMoDn_Object((1,3,6,1,4,1,9,9,826,1,9,1,1,10),_CfprChangeChangedObjectRefFprmMoDn_Type())
cfprChangeChangedObjectRefFprmMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprChangeChangedObjectRefFprmMoDn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprChangeObjects':cfprChangeObjects,'cfprChangeChangedObjectRefTable':cfprChangeChangedObjectRefTable,'cfprChangeChangedObjectRefEntry':cfprChangeChangedObjectRefEntry,_D:cfprChangeChangedObjectRefInstanceId,'cfprChangeChangedObjectRefDn':cfprChangeChangedObjectRefDn,'cfprChangeChangedObjectRefRn':cfprChangeChangedObjectRefRn,'cfprChangeChangedObjectRefCentraleMoDn':cfprChangeChangedObjectRefCentraleMoDn,'cfprChangeChangedObjectRefChangedMoClassId':cfprChangeChangedObjectRefChangedMoClassId,'cfprChangeChangedObjectRefGuid':cfprChangeChangedObjectRefGuid,'cfprChangeChangedObjectRefId':cfprChangeChangedObjectRefId,'cfprChangeChangedObjectRefOldCentraleMoDn':cfprChangeChangedObjectRefOldCentraleMoDn,'cfprChangeChangedObjectRefRefObjStatus':cfprChangeChangedObjectRefRefObjStatus,'cfprChangeChangedObjectRefFprmMoDn':cfprChangeChangedObjectRefFprmMoDn})