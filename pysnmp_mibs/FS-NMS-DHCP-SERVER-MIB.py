#
# PySNMP MIB module FS-NMS-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-NMS-DHCP-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nmsMgmt, = mibBuilder.importSymbols("FS-NMS-SMI", "nmsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 355))
dhcpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 52642, 9, 355, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerStatus.setStatus('mandatory')
nmsDhcpIpAddrPoolTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2), )
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolTable.setStatus('mandatory')
nmsDhcpIpAddrPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1), ).setIndexNames((0, "FS-NMS-DHCP-SERVER-MIB", "nmsDhcpIpAddrPoolIndex"))
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolEntry.setStatus('mandatory')
nmsDhcpIpAddrPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolIndex.setStatus('mandatory')
nmsDhcpIpAddrPoolSubNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolSubNetwork.setStatus('mandatory')
nmsDhcpIpAddrPoolMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolMask.setStatus('mandatory')
nmsDhcpIpAddrPoolStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolStart.setStatus('mandatory')
nmsDhcpIpAddrPoolEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolEnd.setStatus('mandatory')
nmsDhcpIpAddrPoolReserveAddrList = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 355, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsDhcpIpAddrPoolReserveAddrList.setStatus('mandatory')
mibBuilder.exportSymbols("FS-NMS-DHCP-SERVER-MIB", nmsDhcpIpAddrPoolEntry=nmsDhcpIpAddrPoolEntry, nmsDhcpIpAddrPoolEnd=nmsDhcpIpAddrPoolEnd, nmsDhcpIpAddrPoolTable=nmsDhcpIpAddrPoolTable, nmsDhcpIpAddrPoolIndex=nmsDhcpIpAddrPoolIndex, nmsDhcpIpAddrPoolMask=nmsDhcpIpAddrPoolMask, dhcp=dhcp, dhcpServerStatus=dhcpServerStatus, nmsDhcpIpAddrPoolReserveAddrList=nmsDhcpIpAddrPoolReserveAddrList, nmsDhcpIpAddrPoolSubNetwork=nmsDhcpIpAddrPoolSubNetwork, nmsDhcpIpAddrPoolStart=nmsDhcpIpAddrPoolStart)
