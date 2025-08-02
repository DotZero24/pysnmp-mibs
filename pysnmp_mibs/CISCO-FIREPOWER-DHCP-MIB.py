_G='cfprDhcpLeaseInstanceId'
_F='cfprDhcpInstInstanceId'
_E='cfprDhcpAcquiredInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-DHCP-MIB'
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
cfprDhcpObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,15))
_CfprDhcpAcquiredTable_Object=MibTable
cfprDhcpAcquiredTable=_CfprDhcpAcquiredTable_Object((1,3,6,1,4,1,9,9,826,1,15,1))
if mibBuilder.loadTexts:cfprDhcpAcquiredTable.setStatus(_A)
_CfprDhcpAcquiredEntry_Object=MibTableRow
cfprDhcpAcquiredEntry=_CfprDhcpAcquiredEntry_Object((1,3,6,1,4,1,9,9,826,1,15,1,1))
cfprDhcpAcquiredEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprDhcpAcquiredEntry.setStatus(_A)
_CfprDhcpAcquiredInstanceId_Type=CfprManagedObjectId
_CfprDhcpAcquiredInstanceId_Object=MibTableColumn
cfprDhcpAcquiredInstanceId=_CfprDhcpAcquiredInstanceId_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,1),_CfprDhcpAcquiredInstanceId_Type())
cfprDhcpAcquiredInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDhcpAcquiredInstanceId.setStatus(_A)
_CfprDhcpAcquiredDn_Type=CfprManagedObjectDn
_CfprDhcpAcquiredDn_Object=MibTableColumn
cfprDhcpAcquiredDn=_CfprDhcpAcquiredDn_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,2),_CfprDhcpAcquiredDn_Type())
cfprDhcpAcquiredDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredDn.setStatus(_A)
_CfprDhcpAcquiredRn_Type=SnmpAdminString
_CfprDhcpAcquiredRn_Object=MibTableColumn
cfprDhcpAcquiredRn=_CfprDhcpAcquiredRn_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,3),_CfprDhcpAcquiredRn_Type())
cfprDhcpAcquiredRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredRn.setStatus(_A)
_CfprDhcpAcquiredAcqts_Type=DateAndTime
_CfprDhcpAcquiredAcqts_Object=MibTableColumn
cfprDhcpAcquiredAcqts=_CfprDhcpAcquiredAcqts_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,4),_CfprDhcpAcquiredAcqts_Type())
cfprDhcpAcquiredAcqts.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredAcqts.setStatus(_A)
_CfprDhcpAcquiredCookie_Type=SnmpAdminString
_CfprDhcpAcquiredCookie_Object=MibTableColumn
cfprDhcpAcquiredCookie=_CfprDhcpAcquiredCookie_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,5),_CfprDhcpAcquiredCookie_Type())
cfprDhcpAcquiredCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredCookie.setStatus(_A)
_CfprDhcpAcquiredEnds_Type=DateAndTime
_CfprDhcpAcquiredEnds_Object=MibTableColumn
cfprDhcpAcquiredEnds=_CfprDhcpAcquiredEnds_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,6),_CfprDhcpAcquiredEnds_Type())
cfprDhcpAcquiredEnds.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredEnds.setStatus(_A)
_CfprDhcpAcquiredIp_Type=InetAddressIPv4
_CfprDhcpAcquiredIp_Object=MibTableColumn
cfprDhcpAcquiredIp=_CfprDhcpAcquiredIp_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,7),_CfprDhcpAcquiredIp_Type())
cfprDhcpAcquiredIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredIp.setStatus(_A)
_CfprDhcpAcquiredMac_Type=MacAddress
_CfprDhcpAcquiredMac_Object=MibTableColumn
cfprDhcpAcquiredMac=_CfprDhcpAcquiredMac_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,8),_CfprDhcpAcquiredMac_Type())
cfprDhcpAcquiredMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredMac.setStatus(_A)
_CfprDhcpAcquiredSysId_Type=SnmpAdminString
_CfprDhcpAcquiredSysId_Object=MibTableColumn
cfprDhcpAcquiredSysId=_CfprDhcpAcquiredSysId_Object((1,3,6,1,4,1,9,9,826,1,15,1,1,9),_CfprDhcpAcquiredSysId_Type())
cfprDhcpAcquiredSysId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpAcquiredSysId.setStatus(_A)
_CfprDhcpInstTable_Object=MibTable
cfprDhcpInstTable=_CfprDhcpInstTable_Object((1,3,6,1,4,1,9,9,826,1,15,2))
if mibBuilder.loadTexts:cfprDhcpInstTable.setStatus(_A)
_CfprDhcpInstEntry_Object=MibTableRow
cfprDhcpInstEntry=_CfprDhcpInstEntry_Object((1,3,6,1,4,1,9,9,826,1,15,2,1))
cfprDhcpInstEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprDhcpInstEntry.setStatus(_A)
_CfprDhcpInstInstanceId_Type=CfprManagedObjectId
_CfprDhcpInstInstanceId_Object=MibTableColumn
cfprDhcpInstInstanceId=_CfprDhcpInstInstanceId_Object((1,3,6,1,4,1,9,9,826,1,15,2,1,1),_CfprDhcpInstInstanceId_Type())
cfprDhcpInstInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDhcpInstInstanceId.setStatus(_A)
_CfprDhcpInstDn_Type=CfprManagedObjectDn
_CfprDhcpInstDn_Object=MibTableColumn
cfprDhcpInstDn=_CfprDhcpInstDn_Object((1,3,6,1,4,1,9,9,826,1,15,2,1,2),_CfprDhcpInstDn_Type())
cfprDhcpInstDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpInstDn.setStatus(_A)
_CfprDhcpInstRn_Type=SnmpAdminString
_CfprDhcpInstRn_Object=MibTableColumn
cfprDhcpInstRn=_CfprDhcpInstRn_Object((1,3,6,1,4,1,9,9,826,1,15,2,1,3),_CfprDhcpInstRn_Type())
cfprDhcpInstRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpInstRn.setStatus(_A)
_CfprDhcpLeaseTable_Object=MibTable
cfprDhcpLeaseTable=_CfprDhcpLeaseTable_Object((1,3,6,1,4,1,9,9,826,1,15,3))
if mibBuilder.loadTexts:cfprDhcpLeaseTable.setStatus(_A)
_CfprDhcpLeaseEntry_Object=MibTableRow
cfprDhcpLeaseEntry=_CfprDhcpLeaseEntry_Object((1,3,6,1,4,1,9,9,826,1,15,3,1))
cfprDhcpLeaseEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprDhcpLeaseEntry.setStatus(_A)
_CfprDhcpLeaseInstanceId_Type=CfprManagedObjectId
_CfprDhcpLeaseInstanceId_Object=MibTableColumn
cfprDhcpLeaseInstanceId=_CfprDhcpLeaseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,1),_CfprDhcpLeaseInstanceId_Type())
cfprDhcpLeaseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDhcpLeaseInstanceId.setStatus(_A)
_CfprDhcpLeaseDn_Type=CfprManagedObjectDn
_CfprDhcpLeaseDn_Object=MibTableColumn
cfprDhcpLeaseDn=_CfprDhcpLeaseDn_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,2),_CfprDhcpLeaseDn_Type())
cfprDhcpLeaseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseDn.setStatus(_A)
_CfprDhcpLeaseRn_Type=SnmpAdminString
_CfprDhcpLeaseRn_Object=MibTableColumn
cfprDhcpLeaseRn=_CfprDhcpLeaseRn_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,3),_CfprDhcpLeaseRn_Type())
cfprDhcpLeaseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseRn.setStatus(_A)
_CfprDhcpLeaseCliId_Type=SnmpAdminString
_CfprDhcpLeaseCliId_Object=MibTableColumn
cfprDhcpLeaseCliId=_CfprDhcpLeaseCliId_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,4),_CfprDhcpLeaseCliId_Type())
cfprDhcpLeaseCliId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseCliId.setStatus(_A)
_CfprDhcpLeaseCookie_Type=SnmpAdminString
_CfprDhcpLeaseCookie_Object=MibTableColumn
cfprDhcpLeaseCookie=_CfprDhcpLeaseCookie_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,5),_CfprDhcpLeaseCookie_Type())
cfprDhcpLeaseCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseCookie.setStatus(_A)
_CfprDhcpLeaseEnds_Type=DateAndTime
_CfprDhcpLeaseEnds_Object=MibTableColumn
cfprDhcpLeaseEnds=_CfprDhcpLeaseEnds_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,6),_CfprDhcpLeaseEnds_Type())
cfprDhcpLeaseEnds.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseEnds.setStatus(_A)
_CfprDhcpLeaseHostname_Type=SnmpAdminString
_CfprDhcpLeaseHostname_Object=MibTableColumn
cfprDhcpLeaseHostname=_CfprDhcpLeaseHostname_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,7),_CfprDhcpLeaseHostname_Type())
cfprDhcpLeaseHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseHostname.setStatus(_A)
_CfprDhcpLeaseIntf_Type=SnmpAdminString
_CfprDhcpLeaseIntf_Object=MibTableColumn
cfprDhcpLeaseIntf=_CfprDhcpLeaseIntf_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,8),_CfprDhcpLeaseIntf_Type())
cfprDhcpLeaseIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseIntf.setStatus(_A)
_CfprDhcpLeaseIp_Type=InetAddressIPv4
_CfprDhcpLeaseIp_Object=MibTableColumn
cfprDhcpLeaseIp=_CfprDhcpLeaseIp_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,9),_CfprDhcpLeaseIp_Type())
cfprDhcpLeaseIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseIp.setStatus(_A)
_CfprDhcpLeaseMac_Type=MacAddress
_CfprDhcpLeaseMac_Object=MibTableColumn
cfprDhcpLeaseMac=_CfprDhcpLeaseMac_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,10),_CfprDhcpLeaseMac_Type())
cfprDhcpLeaseMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseMac.setStatus(_A)
_CfprDhcpLeaseStarts_Type=DateAndTime
_CfprDhcpLeaseStarts_Object=MibTableColumn
cfprDhcpLeaseStarts=_CfprDhcpLeaseStarts_Object((1,3,6,1,4,1,9,9,826,1,15,3,1,11),_CfprDhcpLeaseStarts_Type())
cfprDhcpLeaseStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDhcpLeaseStarts.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprDhcpObjects':cfprDhcpObjects,'cfprDhcpAcquiredTable':cfprDhcpAcquiredTable,'cfprDhcpAcquiredEntry':cfprDhcpAcquiredEntry,_E:cfprDhcpAcquiredInstanceId,'cfprDhcpAcquiredDn':cfprDhcpAcquiredDn,'cfprDhcpAcquiredRn':cfprDhcpAcquiredRn,'cfprDhcpAcquiredAcqts':cfprDhcpAcquiredAcqts,'cfprDhcpAcquiredCookie':cfprDhcpAcquiredCookie,'cfprDhcpAcquiredEnds':cfprDhcpAcquiredEnds,'cfprDhcpAcquiredIp':cfprDhcpAcquiredIp,'cfprDhcpAcquiredMac':cfprDhcpAcquiredMac,'cfprDhcpAcquiredSysId':cfprDhcpAcquiredSysId,'cfprDhcpInstTable':cfprDhcpInstTable,'cfprDhcpInstEntry':cfprDhcpInstEntry,_F:cfprDhcpInstInstanceId,'cfprDhcpInstDn':cfprDhcpInstDn,'cfprDhcpInstRn':cfprDhcpInstRn,'cfprDhcpLeaseTable':cfprDhcpLeaseTable,'cfprDhcpLeaseEntry':cfprDhcpLeaseEntry,_G:cfprDhcpLeaseInstanceId,'cfprDhcpLeaseDn':cfprDhcpLeaseDn,'cfprDhcpLeaseRn':cfprDhcpLeaseRn,'cfprDhcpLeaseCliId':cfprDhcpLeaseCliId,'cfprDhcpLeaseCookie':cfprDhcpLeaseCookie,'cfprDhcpLeaseEnds':cfprDhcpLeaseEnds,'cfprDhcpLeaseHostname':cfprDhcpLeaseHostname,'cfprDhcpLeaseIntf':cfprDhcpLeaseIntf,'cfprDhcpLeaseIp':cfprDhcpLeaseIp,'cfprDhcpLeaseMac':cfprDhcpLeaseMac,'cfprDhcpLeaseStarts':cfprDhcpLeaseStarts})