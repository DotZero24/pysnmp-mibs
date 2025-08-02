_F='cfprVersionEpInstanceId'
_E='not-accessible'
_D='cfprVersionApplicationInstanceId'
_C='CISCO-FIREPOWER-VERSION-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprVersionObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,81))
_CfprVersionApplicationTable_Object=MibTable
cfprVersionApplicationTable=_CfprVersionApplicationTable_Object((1,3,6,1,4,1,9,9,826,1,81,1))
if mibBuilder.loadTexts:cfprVersionApplicationTable.setStatus(_A)
_CfprVersionApplicationEntry_Object=MibTableRow
cfprVersionApplicationEntry=_CfprVersionApplicationEntry_Object((1,3,6,1,4,1,9,9,826,1,81,1,1))
cfprVersionApplicationEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprVersionApplicationEntry.setStatus(_A)
_CfprVersionApplicationInstanceId_Type=CfprManagedObjectId
_CfprVersionApplicationInstanceId_Object=MibTableColumn
cfprVersionApplicationInstanceId=_CfprVersionApplicationInstanceId_Object((1,3,6,1,4,1,9,9,826,1,81,1,1,1),_CfprVersionApplicationInstanceId_Type())
cfprVersionApplicationInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprVersionApplicationInstanceId.setStatus(_A)
_CfprVersionApplicationDn_Type=CfprManagedObjectDn
_CfprVersionApplicationDn_Object=MibTableColumn
cfprVersionApplicationDn=_CfprVersionApplicationDn_Object((1,3,6,1,4,1,9,9,826,1,81,1,1,2),_CfprVersionApplicationDn_Type())
cfprVersionApplicationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVersionApplicationDn.setStatus(_A)
_CfprVersionApplicationRn_Type=SnmpAdminString
_CfprVersionApplicationRn_Object=MibTableColumn
cfprVersionApplicationRn=_CfprVersionApplicationRn_Object((1,3,6,1,4,1,9,9,826,1,81,1,1,3),_CfprVersionApplicationRn_Type())
cfprVersionApplicationRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVersionApplicationRn.setStatus(_A)
_CfprVersionApplicationDetail_Type=SnmpAdminString
_CfprVersionApplicationDetail_Object=MibTableColumn
cfprVersionApplicationDetail=_CfprVersionApplicationDetail_Object((1,3,6,1,4,1,9,9,826,1,81,1,1,4),_CfprVersionApplicationDetail_Type())
cfprVersionApplicationDetail.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVersionApplicationDetail.setStatus(_A)
_CfprVersionApplicationTime_Type=SnmpAdminString
_CfprVersionApplicationTime_Object=MibTableColumn
cfprVersionApplicationTime=_CfprVersionApplicationTime_Object((1,3,6,1,4,1,9,9,826,1,81,1,1,5),_CfprVersionApplicationTime_Type())
cfprVersionApplicationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVersionApplicationTime.setStatus(_A)
_CfprVersionApplicationVersion_Type=SnmpAdminString
_CfprVersionApplicationVersion_Object=MibTableColumn
cfprVersionApplicationVersion=_CfprVersionApplicationVersion_Object((1,3,6,1,4,1,9,9,826,1,81,1,1,6),_CfprVersionApplicationVersion_Type())
cfprVersionApplicationVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVersionApplicationVersion.setStatus(_A)
_CfprVersionEpTable_Object=MibTable
cfprVersionEpTable=_CfprVersionEpTable_Object((1,3,6,1,4,1,9,9,826,1,81,2))
if mibBuilder.loadTexts:cfprVersionEpTable.setStatus(_A)
_CfprVersionEpEntry_Object=MibTableRow
cfprVersionEpEntry=_CfprVersionEpEntry_Object((1,3,6,1,4,1,9,9,826,1,81,2,1))
cfprVersionEpEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprVersionEpEntry.setStatus(_A)
_CfprVersionEpInstanceId_Type=CfprManagedObjectId
_CfprVersionEpInstanceId_Object=MibTableColumn
cfprVersionEpInstanceId=_CfprVersionEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,81,2,1,1),_CfprVersionEpInstanceId_Type())
cfprVersionEpInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprVersionEpInstanceId.setStatus(_A)
_CfprVersionEpDn_Type=CfprManagedObjectDn
_CfprVersionEpDn_Object=MibTableColumn
cfprVersionEpDn=_CfprVersionEpDn_Object((1,3,6,1,4,1,9,9,826,1,81,2,1,2),_CfprVersionEpDn_Type())
cfprVersionEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVersionEpDn.setStatus(_A)
_CfprVersionEpRn_Type=SnmpAdminString
_CfprVersionEpRn_Object=MibTableColumn
cfprVersionEpRn=_CfprVersionEpRn_Object((1,3,6,1,4,1,9,9,826,1,81,2,1,3),_CfprVersionEpRn_Type())
cfprVersionEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVersionEpRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprVersionObjects':cfprVersionObjects,'cfprVersionApplicationTable':cfprVersionApplicationTable,'cfprVersionApplicationEntry':cfprVersionApplicationEntry,_D:cfprVersionApplicationInstanceId,'cfprVersionApplicationDn':cfprVersionApplicationDn,'cfprVersionApplicationRn':cfprVersionApplicationRn,'cfprVersionApplicationDetail':cfprVersionApplicationDetail,'cfprVersionApplicationTime':cfprVersionApplicationTime,'cfprVersionApplicationVersion':cfprVersionApplicationVersion,'cfprVersionEpTable':cfprVersionEpTable,'cfprVersionEpEntry':cfprVersionEpEntry,_F:cfprVersionEpInstanceId,'cfprVersionEpDn':cfprVersionEpDn,'cfprVersionEpRn':cfprVersionEpRn})