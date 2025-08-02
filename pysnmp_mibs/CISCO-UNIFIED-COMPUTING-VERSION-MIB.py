_F='cucsVersionEpInstanceId'
_E='not-accessible'
_D='cucsVersionApplicationInstanceId'
_C='CISCO-UNIFIED-COMPUTING-VERSION-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsVersionObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,70))
_CucsVersionApplicationTable_Object=MibTable
cucsVersionApplicationTable=_CucsVersionApplicationTable_Object((1,3,6,1,4,1,9,9,719,1,70,1))
if mibBuilder.loadTexts:cucsVersionApplicationTable.setStatus(_A)
_CucsVersionApplicationEntry_Object=MibTableRow
cucsVersionApplicationEntry=_CucsVersionApplicationEntry_Object((1,3,6,1,4,1,9,9,719,1,70,1,1))
cucsVersionApplicationEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsVersionApplicationEntry.setStatus(_A)
_CucsVersionApplicationInstanceId_Type=CucsManagedObjectId
_CucsVersionApplicationInstanceId_Object=MibTableColumn
cucsVersionApplicationInstanceId=_CucsVersionApplicationInstanceId_Object((1,3,6,1,4,1,9,9,719,1,70,1,1,1),_CucsVersionApplicationInstanceId_Type())
cucsVersionApplicationInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsVersionApplicationInstanceId.setStatus(_A)
_CucsVersionApplicationDn_Type=CucsManagedObjectDn
_CucsVersionApplicationDn_Object=MibTableColumn
cucsVersionApplicationDn=_CucsVersionApplicationDn_Object((1,3,6,1,4,1,9,9,719,1,70,1,1,2),_CucsVersionApplicationDn_Type())
cucsVersionApplicationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVersionApplicationDn.setStatus(_A)
_CucsVersionApplicationRn_Type=SnmpAdminString
_CucsVersionApplicationRn_Object=MibTableColumn
cucsVersionApplicationRn=_CucsVersionApplicationRn_Object((1,3,6,1,4,1,9,9,719,1,70,1,1,3),_CucsVersionApplicationRn_Type())
cucsVersionApplicationRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVersionApplicationRn.setStatus(_A)
_CucsVersionApplicationDetail_Type=SnmpAdminString
_CucsVersionApplicationDetail_Object=MibTableColumn
cucsVersionApplicationDetail=_CucsVersionApplicationDetail_Object((1,3,6,1,4,1,9,9,719,1,70,1,1,4),_CucsVersionApplicationDetail_Type())
cucsVersionApplicationDetail.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVersionApplicationDetail.setStatus(_A)
_CucsVersionApplicationTime_Type=SnmpAdminString
_CucsVersionApplicationTime_Object=MibTableColumn
cucsVersionApplicationTime=_CucsVersionApplicationTime_Object((1,3,6,1,4,1,9,9,719,1,70,1,1,5),_CucsVersionApplicationTime_Type())
cucsVersionApplicationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVersionApplicationTime.setStatus(_A)
_CucsVersionApplicationVersion_Type=SnmpAdminString
_CucsVersionApplicationVersion_Object=MibTableColumn
cucsVersionApplicationVersion=_CucsVersionApplicationVersion_Object((1,3,6,1,4,1,9,9,719,1,70,1,1,6),_CucsVersionApplicationVersion_Type())
cucsVersionApplicationVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVersionApplicationVersion.setStatus(_A)
_CucsVersionEpTable_Object=MibTable
cucsVersionEpTable=_CucsVersionEpTable_Object((1,3,6,1,4,1,9,9,719,1,70,2))
if mibBuilder.loadTexts:cucsVersionEpTable.setStatus(_A)
_CucsVersionEpEntry_Object=MibTableRow
cucsVersionEpEntry=_CucsVersionEpEntry_Object((1,3,6,1,4,1,9,9,719,1,70,2,1))
cucsVersionEpEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsVersionEpEntry.setStatus(_A)
_CucsVersionEpInstanceId_Type=CucsManagedObjectId
_CucsVersionEpInstanceId_Object=MibTableColumn
cucsVersionEpInstanceId=_CucsVersionEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,70,2,1,1),_CucsVersionEpInstanceId_Type())
cucsVersionEpInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsVersionEpInstanceId.setStatus(_A)
_CucsVersionEpDn_Type=CucsManagedObjectDn
_CucsVersionEpDn_Object=MibTableColumn
cucsVersionEpDn=_CucsVersionEpDn_Object((1,3,6,1,4,1,9,9,719,1,70,2,1,2),_CucsVersionEpDn_Type())
cucsVersionEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVersionEpDn.setStatus(_A)
_CucsVersionEpRn_Type=SnmpAdminString
_CucsVersionEpRn_Object=MibTableColumn
cucsVersionEpRn=_CucsVersionEpRn_Object((1,3,6,1,4,1,9,9,719,1,70,2,1,3),_CucsVersionEpRn_Type())
cucsVersionEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVersionEpRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsVersionObjects':cucsVersionObjects,'cucsVersionApplicationTable':cucsVersionApplicationTable,'cucsVersionApplicationEntry':cucsVersionApplicationEntry,_D:cucsVersionApplicationInstanceId,'cucsVersionApplicationDn':cucsVersionApplicationDn,'cucsVersionApplicationRn':cucsVersionApplicationRn,'cucsVersionApplicationDetail':cucsVersionApplicationDetail,'cucsVersionApplicationTime':cucsVersionApplicationTime,'cucsVersionApplicationVersion':cucsVersionApplicationVersion,'cucsVersionEpTable':cucsVersionEpTable,'cucsVersionEpEntry':cucsVersionEpEntry,_F:cucsVersionEpInstanceId,'cucsVersionEpDn':cucsVersionEpDn,'cucsVersionEpRn':cucsVersionEpRn})