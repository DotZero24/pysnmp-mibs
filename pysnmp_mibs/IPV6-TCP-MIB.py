#
# PySNMP MIB module IPV6-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/IPV6-TCP-MIB.txt
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Ipv6IfIndexOrZero, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6Address")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, experimental, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "experimental", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipv6TcpMIB = ModuleIdentity((1, 3, 6, 1, 3, 86))
if mibBuilder.loadTexts: ipv6TcpMIB.setLastUpdated('9801290000Z')
if mibBuilder.loadTexts: ipv6TcpMIB.setOrganization('IETF IPv6 MIB Working Group')
tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
ipv6TcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 16), )
if mibBuilder.loadTexts: ipv6TcpConnTable.setStatus('current')
ipv6TcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 16, 1), ).setIndexNames((0, "IPV6-TCP-MIB", "ipv6TcpConnLocalAddress"), (0, "IPV6-TCP-MIB", "ipv6TcpConnLocalPort"), (0, "IPV6-TCP-MIB", "ipv6TcpConnRemAddress"), (0, "IPV6-TCP-MIB", "ipv6TcpConnRemPort"), (0, "IPV6-TCP-MIB", "ipv6TcpConnIfIndex"))
if mibBuilder.loadTexts: ipv6TcpConnEntry.setStatus('current')
ipv6TcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6TcpConnLocalAddress.setStatus('current')
ipv6TcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6TcpConnLocalPort.setStatus('current')
ipv6TcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 3), Ipv6Address())
if mibBuilder.loadTexts: ipv6TcpConnRemAddress.setStatus('current')
ipv6TcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6TcpConnRemPort.setStatus('current')
ipv6TcpConnIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 5), Ipv6IfIndexOrZero())
if mibBuilder.loadTexts: ipv6TcpConnIfIndex.setStatus('current')
ipv6TcpConnState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6TcpConnState.setStatus('current')
ipv6TcpConformance = MibIdentifier((1, 3, 6, 1, 3, 86, 2))
ipv6TcpCompliances = MibIdentifier((1, 3, 6, 1, 3, 86, 2, 1))
ipv6TcpGroups = MibIdentifier((1, 3, 6, 1, 3, 86, 2, 2))
ipv6TcpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 86, 2, 1, 1)).setObjects(("IPV6-TCP-MIB", "ipv6TcpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6TcpCompliance = ipv6TcpCompliance.setStatus('current')
ipv6TcpGroup = ObjectGroup((1, 3, 6, 1, 3, 86, 2, 2, 1)).setObjects(("IPV6-TCP-MIB", "ipv6TcpConnState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6TcpGroup = ipv6TcpGroup.setStatus('current')
mibBuilder.exportSymbols("IPV6-TCP-MIB", ipv6TcpConnLocalAddress=ipv6TcpConnLocalAddress, ipv6TcpConnIfIndex=ipv6TcpConnIfIndex, ipv6TcpConnLocalPort=ipv6TcpConnLocalPort, ipv6TcpCompliances=ipv6TcpCompliances, ipv6TcpGroups=ipv6TcpGroups, ipv6TcpGroup=ipv6TcpGroup, ipv6TcpConnEntry=ipv6TcpConnEntry, ipv6TcpConformance=ipv6TcpConformance, ipv6TcpCompliance=ipv6TcpCompliance, tcp=tcp, ipv6TcpConnTable=ipv6TcpConnTable, ipv6TcpConnRemAddress=ipv6TcpConnRemAddress, ipv6TcpConnRemPort=ipv6TcpConnRemPort, ipv6TcpConnState=ipv6TcpConnState, ipv6TcpMIB=ipv6TcpMIB, PYSNMP_MODULE_ID=ipv6TcpMIB)
