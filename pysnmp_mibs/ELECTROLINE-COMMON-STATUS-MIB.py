#
# PySNMP MIB module ELECTROLINE-COMMON-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-COMMON-STATUS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
commonStatus, electrolineCommon = mibBuilder.importSymbols("ELECTROLINE-COMMON-ROOT-MIB", "commonStatus", "electrolineCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
commonLogicalID, commonPhysAddress = mibBuilder.importSymbols("SCTE-HMS-COMMON-MIB", "commonLogicalID", "commonPhysAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
internalTemperature = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 130))).setMaxAccess("readonly")
if mibBuilder.loadTexts: internalTemperature.setStatus('current')
inetNetworkAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 3, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetNetworkAddressType.setStatus('current')
inetNetworkAddress = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 3, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetNetworkAddress.setStatus('current')
inetMonitoringNetworkAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 3, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetMonitoringNetworkAddressType.setStatus('current')
inetMonitoringNetworkAddress = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 3, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetMonitoringNetworkAddress.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-COMMON-STATUS-MIB", inetNetworkAddressType=inetNetworkAddressType, inetNetworkAddress=inetNetworkAddress, inetMonitoringNetworkAddressType=inetMonitoringNetworkAddressType, inetMonitoringNetworkAddress=inetMonitoringNetworkAddress, internalTemperature=internalTemperature)
