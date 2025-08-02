_D='cucsChangeChangedObjectRefInstanceId'
_C='CISCO-UNIFIED-COMPUTING-CHANGE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsChangeStatus,CucsMoMoClassId=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsChangeStatus','CucsMoMoClassId')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsChangeObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,71))
_CucsChangeChangedObjectRefTable_Object=MibTable
cucsChangeChangedObjectRefTable=_CucsChangeChangedObjectRefTable_Object((1,3,6,1,4,1,9,9,719,1,71,1))
if mibBuilder.loadTexts:cucsChangeChangedObjectRefTable.setStatus(_A)
_CucsChangeChangedObjectRefEntry_Object=MibTableRow
cucsChangeChangedObjectRefEntry=_CucsChangeChangedObjectRefEntry_Object((1,3,6,1,4,1,9,9,719,1,71,1,1))
cucsChangeChangedObjectRefEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsChangeChangedObjectRefEntry.setStatus(_A)
_CucsChangeChangedObjectRefInstanceId_Type=CucsManagedObjectId
_CucsChangeChangedObjectRefInstanceId_Object=MibTableColumn
cucsChangeChangedObjectRefInstanceId=_CucsChangeChangedObjectRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,1),_CucsChangeChangedObjectRefInstanceId_Type())
cucsChangeChangedObjectRefInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsChangeChangedObjectRefInstanceId.setStatus(_A)
_CucsChangeChangedObjectRefDn_Type=CucsManagedObjectDn
_CucsChangeChangedObjectRefDn_Object=MibTableColumn
cucsChangeChangedObjectRefDn=_CucsChangeChangedObjectRefDn_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,2),_CucsChangeChangedObjectRefDn_Type())
cucsChangeChangedObjectRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefDn.setStatus(_A)
_CucsChangeChangedObjectRefRn_Type=SnmpAdminString
_CucsChangeChangedObjectRefRn_Object=MibTableColumn
cucsChangeChangedObjectRefRn=_CucsChangeChangedObjectRefRn_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,3),_CucsChangeChangedObjectRefRn_Type())
cucsChangeChangedObjectRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefRn.setStatus(_A)
_CucsChangeChangedObjectRefCentraleMoDn_Type=SnmpAdminString
_CucsChangeChangedObjectRefCentraleMoDn_Object=MibTableColumn
cucsChangeChangedObjectRefCentraleMoDn=_CucsChangeChangedObjectRefCentraleMoDn_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,4),_CucsChangeChangedObjectRefCentraleMoDn_Type())
cucsChangeChangedObjectRefCentraleMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefCentraleMoDn.setStatus(_A)
_CucsChangeChangedObjectRefChangedMoClassId_Type=CucsMoMoClassId
_CucsChangeChangedObjectRefChangedMoClassId_Object=MibTableColumn
cucsChangeChangedObjectRefChangedMoClassId=_CucsChangeChangedObjectRefChangedMoClassId_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,5),_CucsChangeChangedObjectRefChangedMoClassId_Type())
cucsChangeChangedObjectRefChangedMoClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefChangedMoClassId.setStatus(_A)
_CucsChangeChangedObjectRefId_Type=Gauge32
_CucsChangeChangedObjectRefId_Object=MibTableColumn
cucsChangeChangedObjectRefId=_CucsChangeChangedObjectRefId_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,6),_CucsChangeChangedObjectRefId_Type())
cucsChangeChangedObjectRefId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefId.setStatus(_A)
_CucsChangeChangedObjectRefOldCentraleMoDn_Type=SnmpAdminString
_CucsChangeChangedObjectRefOldCentraleMoDn_Object=MibTableColumn
cucsChangeChangedObjectRefOldCentraleMoDn=_CucsChangeChangedObjectRefOldCentraleMoDn_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,7),_CucsChangeChangedObjectRefOldCentraleMoDn_Type())
cucsChangeChangedObjectRefOldCentraleMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefOldCentraleMoDn.setStatus(_A)
_CucsChangeChangedObjectRefRefObjStatus_Type=CucsChangeStatus
_CucsChangeChangedObjectRefRefObjStatus_Object=MibTableColumn
cucsChangeChangedObjectRefRefObjStatus=_CucsChangeChangedObjectRefRefObjStatus_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,8),_CucsChangeChangedObjectRefRefObjStatus_Type())
cucsChangeChangedObjectRefRefObjStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefRefObjStatus.setStatus(_A)
_CucsChangeChangedObjectRefUcsmMoDn_Type=SnmpAdminString
_CucsChangeChangedObjectRefUcsmMoDn_Object=MibTableColumn
cucsChangeChangedObjectRefUcsmMoDn=_CucsChangeChangedObjectRefUcsmMoDn_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,9),_CucsChangeChangedObjectRefUcsmMoDn_Type())
cucsChangeChangedObjectRefUcsmMoDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefUcsmMoDn.setStatus(_A)
_CucsChangeChangedObjectRefGuid_Type=SnmpAdminString
_CucsChangeChangedObjectRefGuid_Object=MibTableColumn
cucsChangeChangedObjectRefGuid=_CucsChangeChangedObjectRefGuid_Object((1,3,6,1,4,1,9,9,719,1,71,1,1,10),_CucsChangeChangedObjectRefGuid_Type())
cucsChangeChangedObjectRefGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsChangeChangedObjectRefGuid.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsChangeObjects':cucsChangeObjects,'cucsChangeChangedObjectRefTable':cucsChangeChangedObjectRefTable,'cucsChangeChangedObjectRefEntry':cucsChangeChangedObjectRefEntry,_D:cucsChangeChangedObjectRefInstanceId,'cucsChangeChangedObjectRefDn':cucsChangeChangedObjectRefDn,'cucsChangeChangedObjectRefRn':cucsChangeChangedObjectRefRn,'cucsChangeChangedObjectRefCentraleMoDn':cucsChangeChangedObjectRefCentraleMoDn,'cucsChangeChangedObjectRefChangedMoClassId':cucsChangeChangedObjectRefChangedMoClassId,'cucsChangeChangedObjectRefId':cucsChangeChangedObjectRefId,'cucsChangeChangedObjectRefOldCentraleMoDn':cucsChangeChangedObjectRefOldCentraleMoDn,'cucsChangeChangedObjectRefRefObjStatus':cucsChangeChangedObjectRefRefObjStatus,'cucsChangeChangedObjectRefUcsmMoDn':cucsChangeChangedObjectRefUcsmMoDn,'cucsChangeChangedObjectRefGuid':cucsChangeChangedObjectRefGuid})