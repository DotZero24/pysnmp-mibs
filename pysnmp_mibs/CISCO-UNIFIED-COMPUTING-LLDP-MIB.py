_D='cucsLldpAcquiredInstanceId'
_C='CISCO-UNIFIED-COMPUTING-LLDP-MIB'
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
cucsLldpObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,58))
_CucsLldpAcquiredTable_Object=MibTable
cucsLldpAcquiredTable=_CucsLldpAcquiredTable_Object((1,3,6,1,4,1,9,9,719,1,58,1))
if mibBuilder.loadTexts:cucsLldpAcquiredTable.setStatus(_A)
_CucsLldpAcquiredEntry_Object=MibTableRow
cucsLldpAcquiredEntry=_CucsLldpAcquiredEntry_Object((1,3,6,1,4,1,9,9,719,1,58,1,1))
cucsLldpAcquiredEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsLldpAcquiredEntry.setStatus(_A)
_CucsLldpAcquiredInstanceId_Type=CucsManagedObjectId
_CucsLldpAcquiredInstanceId_Object=MibTableColumn
cucsLldpAcquiredInstanceId=_CucsLldpAcquiredInstanceId_Object((1,3,6,1,4,1,9,9,719,1,58,1,1,1),_CucsLldpAcquiredInstanceId_Type())
cucsLldpAcquiredInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cucsLldpAcquiredInstanceId.setStatus(_A)
_CucsLldpAcquiredDn_Type=CucsManagedObjectDn
_CucsLldpAcquiredDn_Object=MibTableColumn
cucsLldpAcquiredDn=_CucsLldpAcquiredDn_Object((1,3,6,1,4,1,9,9,719,1,58,1,1,2),_CucsLldpAcquiredDn_Type())
cucsLldpAcquiredDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLldpAcquiredDn.setStatus(_A)
_CucsLldpAcquiredRn_Type=SnmpAdminString
_CucsLldpAcquiredRn_Object=MibTableColumn
cucsLldpAcquiredRn=_CucsLldpAcquiredRn_Object((1,3,6,1,4,1,9,9,719,1,58,1,1,3),_CucsLldpAcquiredRn_Type())
cucsLldpAcquiredRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLldpAcquiredRn.setStatus(_A)
_CucsLldpAcquiredAcqts_Type=DateAndTime
_CucsLldpAcquiredAcqts_Object=MibTableColumn
cucsLldpAcquiredAcqts=_CucsLldpAcquiredAcqts_Object((1,3,6,1,4,1,9,9,719,1,58,1,1,4),_CucsLldpAcquiredAcqts_Type())
cucsLldpAcquiredAcqts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLldpAcquiredAcqts.setStatus(_A)
_CucsLldpAcquiredChassisMac_Type=MacAddress
_CucsLldpAcquiredChassisMac_Object=MibTableColumn
cucsLldpAcquiredChassisMac=_CucsLldpAcquiredChassisMac_Object((1,3,6,1,4,1,9,9,719,1,58,1,1,5),_CucsLldpAcquiredChassisMac_Type())
cucsLldpAcquiredChassisMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLldpAcquiredChassisMac.setStatus(_A)
_CucsLldpAcquiredPeerDn_Type=SnmpAdminString
_CucsLldpAcquiredPeerDn_Object=MibTableColumn
cucsLldpAcquiredPeerDn=_CucsLldpAcquiredPeerDn_Object((1,3,6,1,4,1,9,9,719,1,58,1,1,6),_CucsLldpAcquiredPeerDn_Type())
cucsLldpAcquiredPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLldpAcquiredPeerDn.setStatus(_A)
_CucsLldpAcquiredPortMac_Type=MacAddress
_CucsLldpAcquiredPortMac_Object=MibTableColumn
cucsLldpAcquiredPortMac=_CucsLldpAcquiredPortMac_Object((1,3,6,1,4,1,9,9,719,1,58,1,1,7),_CucsLldpAcquiredPortMac_Type())
cucsLldpAcquiredPortMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLldpAcquiredPortMac.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsLldpObjects':cucsLldpObjects,'cucsLldpAcquiredTable':cucsLldpAcquiredTable,'cucsLldpAcquiredEntry':cucsLldpAcquiredEntry,_D:cucsLldpAcquiredInstanceId,'cucsLldpAcquiredDn':cucsLldpAcquiredDn,'cucsLldpAcquiredRn':cucsLldpAcquiredRn,'cucsLldpAcquiredAcqts':cucsLldpAcquiredAcqts,'cucsLldpAcquiredChassisMac':cucsLldpAcquiredChassisMac,'cucsLldpAcquiredPeerDn':cucsLldpAcquiredPeerDn,'cucsLldpAcquiredPortMac':cucsLldpAcquiredPortMac})