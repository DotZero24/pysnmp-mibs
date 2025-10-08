#
# PySNMP MIB module DEVBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVBASE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
aniDevBase = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 1))
if mibBuilder.loadTexts: aniDevBase.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevBase.setOrganization('Aperto Networks')
aniDevProductName = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevProductName.setStatus('current')
aniDevLanIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevLanIpAddr.setStatus('current')
aniDevLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevLanSubnetMask.setStatus('current')
aniDevDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevDefaultGateway.setStatus('current')
aniDevMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevMacAddr.setStatus('current')
mibBuilder.exportSymbols("DEVBASE-MIB", aniDevDefaultGateway=aniDevDefaultGateway, PYSNMP_MODULE_ID=aniDevBase, aniDevBase=aniDevBase, aniDevMacAddr=aniDevMacAddr, aniDevLanSubnetMask=aniDevLanSubnetMask, aniDevProductName=aniDevProductName, aniDevLanIpAddr=aniDevLanIpAddr)
