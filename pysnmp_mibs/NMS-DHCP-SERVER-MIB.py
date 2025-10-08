#
# PySNMP MIB module NMS-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bdcom/NMS-DHCP-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
nmsMgmt, = mibBuilder.importSymbols("NMS-SMI", "nmsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 355))
dhcpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 3320, 9, 355, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerStatus.setStatus('mandatory')
nmsDhcpIpAddrPoolTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2), )
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolTable.setStatus('mandatory')
nmsDhcpIpAddrPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2, 1), ).setIndexNames((0, "NMS-DHCP-SERVER-MIB", "nmsDhcpIpAddrPoolIndex"))
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolEntry.setStatus('mandatory')
nmsDhcpIpAddrPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolIndex.setStatus('mandatory')
nmsDhcpIpAddrPoolSubNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolSubNetwork.setStatus('mandatory')
nmsDhcpIpAddrPoolMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolMask.setStatus('mandatory')
nmsDhcpIpAddrPoolStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolStart.setStatus('mandatory')
nmsDhcpIpAddrPoolEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolEnd.setStatus('mandatory')
nmsDhcpIpAddrPoolReserveAddrList = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 355, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolReserveAddrList.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-DHCP-SERVER-MIB", nmsDhcpIpAddrPoolEnd=nmsDhcpIpAddrPoolEnd, nmsDhcpIpAddrPoolEntry=nmsDhcpIpAddrPoolEntry, nmsDhcpIpAddrPoolTable=nmsDhcpIpAddrPoolTable, dhcpServerStatus=dhcpServerStatus, nmsDhcpIpAddrPoolSubNetwork=nmsDhcpIpAddrPoolSubNetwork, nmsDhcpIpAddrPoolMask=nmsDhcpIpAddrPoolMask, nmsDhcpIpAddrPoolStart=nmsDhcpIpAddrPoolStart, nmsDhcpIpAddrPoolIndex=nmsDhcpIpAddrPoolIndex, nmsDhcpIpAddrPoolReserveAddrList=nmsDhcpIpAddrPoolReserveAddrList, dhcp=dhcp)
