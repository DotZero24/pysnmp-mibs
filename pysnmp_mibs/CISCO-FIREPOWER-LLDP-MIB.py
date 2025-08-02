_D='cfprLldpAcquiredInstanceId'
_C='CISCO-FIREPOWER-LLDP-MIB'
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
cfprLldpObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,45))
_CfprLldpAcquiredTable_Object=MibTable
cfprLldpAcquiredTable=_CfprLldpAcquiredTable_Object((1,3,6,1,4,1,9,9,826,1,45,1))
if mibBuilder.loadTexts:cfprLldpAcquiredTable.setStatus(_A)
_CfprLldpAcquiredEntry_Object=MibTableRow
cfprLldpAcquiredEntry=_CfprLldpAcquiredEntry_Object((1,3,6,1,4,1,9,9,826,1,45,1,1))
cfprLldpAcquiredEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprLldpAcquiredEntry.setStatus(_A)
_CfprLldpAcquiredInstanceId_Type=CfprManagedObjectId
_CfprLldpAcquiredInstanceId_Object=MibTableColumn
cfprLldpAcquiredInstanceId=_CfprLldpAcquiredInstanceId_Object((1,3,6,1,4,1,9,9,826,1,45,1,1,1),_CfprLldpAcquiredInstanceId_Type())
cfprLldpAcquiredInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfprLldpAcquiredInstanceId.setStatus(_A)
_CfprLldpAcquiredDn_Type=CfprManagedObjectDn
_CfprLldpAcquiredDn_Object=MibTableColumn
cfprLldpAcquiredDn=_CfprLldpAcquiredDn_Object((1,3,6,1,4,1,9,9,826,1,45,1,1,2),_CfprLldpAcquiredDn_Type())
cfprLldpAcquiredDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLldpAcquiredDn.setStatus(_A)
_CfprLldpAcquiredRn_Type=SnmpAdminString
_CfprLldpAcquiredRn_Object=MibTableColumn
cfprLldpAcquiredRn=_CfprLldpAcquiredRn_Object((1,3,6,1,4,1,9,9,826,1,45,1,1,3),_CfprLldpAcquiredRn_Type())
cfprLldpAcquiredRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLldpAcquiredRn.setStatus(_A)
_CfprLldpAcquiredAcqts_Type=DateAndTime
_CfprLldpAcquiredAcqts_Object=MibTableColumn
cfprLldpAcquiredAcqts=_CfprLldpAcquiredAcqts_Object((1,3,6,1,4,1,9,9,826,1,45,1,1,4),_CfprLldpAcquiredAcqts_Type())
cfprLldpAcquiredAcqts.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLldpAcquiredAcqts.setStatus(_A)
_CfprLldpAcquiredChassisMac_Type=MacAddress
_CfprLldpAcquiredChassisMac_Object=MibTableColumn
cfprLldpAcquiredChassisMac=_CfprLldpAcquiredChassisMac_Object((1,3,6,1,4,1,9,9,826,1,45,1,1,5),_CfprLldpAcquiredChassisMac_Type())
cfprLldpAcquiredChassisMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLldpAcquiredChassisMac.setStatus(_A)
_CfprLldpAcquiredPeerDn_Type=SnmpAdminString
_CfprLldpAcquiredPeerDn_Object=MibTableColumn
cfprLldpAcquiredPeerDn=_CfprLldpAcquiredPeerDn_Object((1,3,6,1,4,1,9,9,826,1,45,1,1,6),_CfprLldpAcquiredPeerDn_Type())
cfprLldpAcquiredPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLldpAcquiredPeerDn.setStatus(_A)
_CfprLldpAcquiredPortMac_Type=MacAddress
_CfprLldpAcquiredPortMac_Object=MibTableColumn
cfprLldpAcquiredPortMac=_CfprLldpAcquiredPortMac_Object((1,3,6,1,4,1,9,9,826,1,45,1,1,7),_CfprLldpAcquiredPortMac_Type())
cfprLldpAcquiredPortMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLldpAcquiredPortMac.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprLldpObjects':cfprLldpObjects,'cfprLldpAcquiredTable':cfprLldpAcquiredTable,'cfprLldpAcquiredEntry':cfprLldpAcquiredEntry,_D:cfprLldpAcquiredInstanceId,'cfprLldpAcquiredDn':cfprLldpAcquiredDn,'cfprLldpAcquiredRn':cfprLldpAcquiredRn,'cfprLldpAcquiredAcqts':cfprLldpAcquiredAcqts,'cfprLldpAcquiredChassisMac':cfprLldpAcquiredChassisMac,'cfprLldpAcquiredPeerDn':cfprLldpAcquiredPeerDn,'cfprLldpAcquiredPortMac':cfprLldpAcquiredPortMac})