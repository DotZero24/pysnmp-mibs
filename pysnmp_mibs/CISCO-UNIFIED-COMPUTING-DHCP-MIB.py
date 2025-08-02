_G='cucsDhcpLeaseInstanceId'
_F='cucsDhcpInstInstanceId'
_E='cucsDhcpAcquiredInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-DHCP-MIB'
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
cucsDhcpObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,11))
_CucsDhcpAcquiredTable_Object=MibTable
cucsDhcpAcquiredTable=_CucsDhcpAcquiredTable_Object((1,3,6,1,4,1,9,9,719,1,11,1))
if mibBuilder.loadTexts:cucsDhcpAcquiredTable.setStatus(_A)
_CucsDhcpAcquiredEntry_Object=MibTableRow
cucsDhcpAcquiredEntry=_CucsDhcpAcquiredEntry_Object((1,3,6,1,4,1,9,9,719,1,11,1,1))
cucsDhcpAcquiredEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsDhcpAcquiredEntry.setStatus(_A)
_CucsDhcpAcquiredInstanceId_Type=CucsManagedObjectId
_CucsDhcpAcquiredInstanceId_Object=MibTableColumn
cucsDhcpAcquiredInstanceId=_CucsDhcpAcquiredInstanceId_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,1),_CucsDhcpAcquiredInstanceId_Type())
cucsDhcpAcquiredInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsDhcpAcquiredInstanceId.setStatus(_A)
_CucsDhcpAcquiredDn_Type=CucsManagedObjectDn
_CucsDhcpAcquiredDn_Object=MibTableColumn
cucsDhcpAcquiredDn=_CucsDhcpAcquiredDn_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,2),_CucsDhcpAcquiredDn_Type())
cucsDhcpAcquiredDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredDn.setStatus(_A)
_CucsDhcpAcquiredRn_Type=SnmpAdminString
_CucsDhcpAcquiredRn_Object=MibTableColumn
cucsDhcpAcquiredRn=_CucsDhcpAcquiredRn_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,3),_CucsDhcpAcquiredRn_Type())
cucsDhcpAcquiredRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredRn.setStatus(_A)
_CucsDhcpAcquiredAcqts_Type=DateAndTime
_CucsDhcpAcquiredAcqts_Object=MibTableColumn
cucsDhcpAcquiredAcqts=_CucsDhcpAcquiredAcqts_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,4),_CucsDhcpAcquiredAcqts_Type())
cucsDhcpAcquiredAcqts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredAcqts.setStatus(_A)
_CucsDhcpAcquiredCookie_Type=SnmpAdminString
_CucsDhcpAcquiredCookie_Object=MibTableColumn
cucsDhcpAcquiredCookie=_CucsDhcpAcquiredCookie_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,5),_CucsDhcpAcquiredCookie_Type())
cucsDhcpAcquiredCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredCookie.setStatus(_A)
_CucsDhcpAcquiredEnds_Type=DateAndTime
_CucsDhcpAcquiredEnds_Object=MibTableColumn
cucsDhcpAcquiredEnds=_CucsDhcpAcquiredEnds_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,6),_CucsDhcpAcquiredEnds_Type())
cucsDhcpAcquiredEnds.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredEnds.setStatus(_A)
_CucsDhcpAcquiredIp_Type=InetAddressIPv4
_CucsDhcpAcquiredIp_Object=MibTableColumn
cucsDhcpAcquiredIp=_CucsDhcpAcquiredIp_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,7),_CucsDhcpAcquiredIp_Type())
cucsDhcpAcquiredIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredIp.setStatus(_A)
_CucsDhcpAcquiredSysId_Type=SnmpAdminString
_CucsDhcpAcquiredSysId_Object=MibTableColumn
cucsDhcpAcquiredSysId=_CucsDhcpAcquiredSysId_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,8),_CucsDhcpAcquiredSysId_Type())
cucsDhcpAcquiredSysId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredSysId.setStatus(_A)
_CucsDhcpAcquiredMac_Type=MacAddress
_CucsDhcpAcquiredMac_Object=MibTableColumn
cucsDhcpAcquiredMac=_CucsDhcpAcquiredMac_Object((1,3,6,1,4,1,9,9,719,1,11,1,1,9),_CucsDhcpAcquiredMac_Type())
cucsDhcpAcquiredMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpAcquiredMac.setStatus(_A)
_CucsDhcpInstTable_Object=MibTable
cucsDhcpInstTable=_CucsDhcpInstTable_Object((1,3,6,1,4,1,9,9,719,1,11,2))
if mibBuilder.loadTexts:cucsDhcpInstTable.setStatus(_A)
_CucsDhcpInstEntry_Object=MibTableRow
cucsDhcpInstEntry=_CucsDhcpInstEntry_Object((1,3,6,1,4,1,9,9,719,1,11,2,1))
cucsDhcpInstEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsDhcpInstEntry.setStatus(_A)
_CucsDhcpInstInstanceId_Type=CucsManagedObjectId
_CucsDhcpInstInstanceId_Object=MibTableColumn
cucsDhcpInstInstanceId=_CucsDhcpInstInstanceId_Object((1,3,6,1,4,1,9,9,719,1,11,2,1,1),_CucsDhcpInstInstanceId_Type())
cucsDhcpInstInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsDhcpInstInstanceId.setStatus(_A)
_CucsDhcpInstDn_Type=CucsManagedObjectDn
_CucsDhcpInstDn_Object=MibTableColumn
cucsDhcpInstDn=_CucsDhcpInstDn_Object((1,3,6,1,4,1,9,9,719,1,11,2,1,2),_CucsDhcpInstDn_Type())
cucsDhcpInstDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpInstDn.setStatus(_A)
_CucsDhcpInstRn_Type=SnmpAdminString
_CucsDhcpInstRn_Object=MibTableColumn
cucsDhcpInstRn=_CucsDhcpInstRn_Object((1,3,6,1,4,1,9,9,719,1,11,2,1,3),_CucsDhcpInstRn_Type())
cucsDhcpInstRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpInstRn.setStatus(_A)
_CucsDhcpLeaseTable_Object=MibTable
cucsDhcpLeaseTable=_CucsDhcpLeaseTable_Object((1,3,6,1,4,1,9,9,719,1,11,3))
if mibBuilder.loadTexts:cucsDhcpLeaseTable.setStatus(_A)
_CucsDhcpLeaseEntry_Object=MibTableRow
cucsDhcpLeaseEntry=_CucsDhcpLeaseEntry_Object((1,3,6,1,4,1,9,9,719,1,11,3,1))
cucsDhcpLeaseEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsDhcpLeaseEntry.setStatus(_A)
_CucsDhcpLeaseInstanceId_Type=CucsManagedObjectId
_CucsDhcpLeaseInstanceId_Object=MibTableColumn
cucsDhcpLeaseInstanceId=_CucsDhcpLeaseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,1),_CucsDhcpLeaseInstanceId_Type())
cucsDhcpLeaseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsDhcpLeaseInstanceId.setStatus(_A)
_CucsDhcpLeaseDn_Type=CucsManagedObjectDn
_CucsDhcpLeaseDn_Object=MibTableColumn
cucsDhcpLeaseDn=_CucsDhcpLeaseDn_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,2),_CucsDhcpLeaseDn_Type())
cucsDhcpLeaseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseDn.setStatus(_A)
_CucsDhcpLeaseRn_Type=SnmpAdminString
_CucsDhcpLeaseRn_Object=MibTableColumn
cucsDhcpLeaseRn=_CucsDhcpLeaseRn_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,3),_CucsDhcpLeaseRn_Type())
cucsDhcpLeaseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseRn.setStatus(_A)
_CucsDhcpLeaseCliId_Type=SnmpAdminString
_CucsDhcpLeaseCliId_Object=MibTableColumn
cucsDhcpLeaseCliId=_CucsDhcpLeaseCliId_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,4),_CucsDhcpLeaseCliId_Type())
cucsDhcpLeaseCliId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseCliId.setStatus(_A)
_CucsDhcpLeaseCookie_Type=SnmpAdminString
_CucsDhcpLeaseCookie_Object=MibTableColumn
cucsDhcpLeaseCookie=_CucsDhcpLeaseCookie_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,5),_CucsDhcpLeaseCookie_Type())
cucsDhcpLeaseCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseCookie.setStatus(_A)
_CucsDhcpLeaseEnds_Type=DateAndTime
_CucsDhcpLeaseEnds_Object=MibTableColumn
cucsDhcpLeaseEnds=_CucsDhcpLeaseEnds_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,6),_CucsDhcpLeaseEnds_Type())
cucsDhcpLeaseEnds.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseEnds.setStatus(_A)
_CucsDhcpLeaseHostname_Type=SnmpAdminString
_CucsDhcpLeaseHostname_Object=MibTableColumn
cucsDhcpLeaseHostname=_CucsDhcpLeaseHostname_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,7),_CucsDhcpLeaseHostname_Type())
cucsDhcpLeaseHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseHostname.setStatus(_A)
_CucsDhcpLeaseIntf_Type=SnmpAdminString
_CucsDhcpLeaseIntf_Object=MibTableColumn
cucsDhcpLeaseIntf=_CucsDhcpLeaseIntf_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,8),_CucsDhcpLeaseIntf_Type())
cucsDhcpLeaseIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseIntf.setStatus(_A)
_CucsDhcpLeaseIp_Type=InetAddressIPv4
_CucsDhcpLeaseIp_Object=MibTableColumn
cucsDhcpLeaseIp=_CucsDhcpLeaseIp_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,9),_CucsDhcpLeaseIp_Type())
cucsDhcpLeaseIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseIp.setStatus(_A)
_CucsDhcpLeaseMac_Type=MacAddress
_CucsDhcpLeaseMac_Object=MibTableColumn
cucsDhcpLeaseMac=_CucsDhcpLeaseMac_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,10),_CucsDhcpLeaseMac_Type())
cucsDhcpLeaseMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseMac.setStatus(_A)
_CucsDhcpLeaseStarts_Type=DateAndTime
_CucsDhcpLeaseStarts_Object=MibTableColumn
cucsDhcpLeaseStarts=_CucsDhcpLeaseStarts_Object((1,3,6,1,4,1,9,9,719,1,11,3,1,11),_CucsDhcpLeaseStarts_Type())
cucsDhcpLeaseStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsDhcpLeaseStarts.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsDhcpObjects':cucsDhcpObjects,'cucsDhcpAcquiredTable':cucsDhcpAcquiredTable,'cucsDhcpAcquiredEntry':cucsDhcpAcquiredEntry,_E:cucsDhcpAcquiredInstanceId,'cucsDhcpAcquiredDn':cucsDhcpAcquiredDn,'cucsDhcpAcquiredRn':cucsDhcpAcquiredRn,'cucsDhcpAcquiredAcqts':cucsDhcpAcquiredAcqts,'cucsDhcpAcquiredCookie':cucsDhcpAcquiredCookie,'cucsDhcpAcquiredEnds':cucsDhcpAcquiredEnds,'cucsDhcpAcquiredIp':cucsDhcpAcquiredIp,'cucsDhcpAcquiredSysId':cucsDhcpAcquiredSysId,'cucsDhcpAcquiredMac':cucsDhcpAcquiredMac,'cucsDhcpInstTable':cucsDhcpInstTable,'cucsDhcpInstEntry':cucsDhcpInstEntry,_F:cucsDhcpInstInstanceId,'cucsDhcpInstDn':cucsDhcpInstDn,'cucsDhcpInstRn':cucsDhcpInstRn,'cucsDhcpLeaseTable':cucsDhcpLeaseTable,'cucsDhcpLeaseEntry':cucsDhcpLeaseEntry,_G:cucsDhcpLeaseInstanceId,'cucsDhcpLeaseDn':cucsDhcpLeaseDn,'cucsDhcpLeaseRn':cucsDhcpLeaseRn,'cucsDhcpLeaseCliId':cucsDhcpLeaseCliId,'cucsDhcpLeaseCookie':cucsDhcpLeaseCookie,'cucsDhcpLeaseEnds':cucsDhcpLeaseEnds,'cucsDhcpLeaseHostname':cucsDhcpLeaseHostname,'cucsDhcpLeaseIntf':cucsDhcpLeaseIntf,'cucsDhcpLeaseIp':cucsDhcpLeaseIp,'cucsDhcpLeaseMac':cucsDhcpLeaseMac,'cucsDhcpLeaseStarts':cucsDhcpLeaseStarts})