#
# PySNMP MIB module ME1200-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-DNS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200Unsigned16, = mibBuilder.importSymbols("ME1200-TC", "ME1200Unsigned16")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
me1200DnsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53))
me1200DnsMib.setRevisions(('2014-01-29 00:00', '2013-10-30 00:00',))
if mibBuilder.loadTexts: me1200DnsMib.setLastUpdated('201401290000Z')
if mibBuilder.loadTexts: me1200DnsMib.setOrganization('Cisco Systems, Inc')
class ME1200DnsServerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("dhcp", 0), ("none", 1), ("static", 2), ("dhcpVlan", 3))

me1200DnsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1))
me1200DnsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2))
me1200DnsGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1))
me1200DnsGlobalsServerSetting = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 1), ME1200DnsServerType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200DnsGlobalsServerSetting.setStatus('current')
me1200DnsGlobalsServerStaticAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200DnsGlobalsServerStaticAddress.setStatus('current')
me1200DnsGlobalsServerStaticVlanId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 3), ME1200Unsigned16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200DnsGlobalsServerStaticVlanId.setStatus('current')
me1200DnsGlobalsProxyAdminState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200DnsGlobalsProxyAdminState.setStatus('current')
me1200DnsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 3))
me1200DnsServerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 3, 1))
me1200DnsServerStatusIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200DnsServerStatusIpAddress.setStatus('current')
me1200DnsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2))
me1200DnsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 1))
me1200DnsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 2))
me1200DnsGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 2, 1)).setObjects(("ME1200-DNS-MIB", "me1200DnsGlobalsServerSetting"), ("ME1200-DNS-MIB", "me1200DnsGlobalsServerStaticAddress"), ("ME1200-DNS-MIB", "me1200DnsGlobalsServerStaticVlanId"), ("ME1200-DNS-MIB", "me1200DnsGlobalsProxyAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200DnsGlobalsInfoGroup = me1200DnsGlobalsInfoGroup.setStatus('current')
me1200DnsServerStatusInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 2, 2)).setObjects(("ME1200-DNS-MIB", "me1200DnsServerStatusIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200DnsServerStatusInfoGroup = me1200DnsServerStatusInfoGroup.setStatus('current')
me1200DnsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 1, 1)).setObjects(("ME1200-DNS-MIB", "me1200DnsGlobalsInfoGroup"), ("ME1200-DNS-MIB", "me1200DnsServerStatusInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200DnsMibCompliance = me1200DnsMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-DNS-MIB", ME1200DnsServerType=ME1200DnsServerType, me1200DnsMib=me1200DnsMib, me1200DnsGlobalsServerStaticVlanId=me1200DnsGlobalsServerStaticVlanId, me1200DnsMIBGroups=me1200DnsMIBGroups, me1200DnsStatus=me1200DnsStatus, me1200DnsServerStatusIpAddress=me1200DnsServerStatusIpAddress, me1200DnsGlobalsServerSetting=me1200DnsGlobalsServerSetting, me1200DnsMIBConformance=me1200DnsMIBConformance, me1200DnsServerStatusInfoGroup=me1200DnsServerStatusInfoGroup, me1200DnsServerStatus=me1200DnsServerStatus, me1200DnsMIBObjects=me1200DnsMIBObjects, me1200DnsMIBCompliances=me1200DnsMIBCompliances, me1200DnsGlobals=me1200DnsGlobals, PYSNMP_MODULE_ID=me1200DnsMib, me1200DnsConfig=me1200DnsConfig, me1200DnsGlobalsServerStaticAddress=me1200DnsGlobalsServerStaticAddress, me1200DnsMibCompliance=me1200DnsMibCompliance, me1200DnsGlobalsInfoGroup=me1200DnsGlobalsInfoGroup, me1200DnsGlobalsProxyAdminState=me1200DnsGlobalsProxyAdminState)
