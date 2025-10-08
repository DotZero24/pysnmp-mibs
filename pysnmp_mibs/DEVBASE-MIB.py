#
# PySNMP MIB module DEVBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/DEVBASE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DEVBASE-MIB", aniDevMacAddr=aniDevMacAddr, PYSNMP_MODULE_ID=aniDevBase, aniDevProductName=aniDevProductName, aniDevLanSubnetMask=aniDevLanSubnetMask, aniDevLanIpAddr=aniDevLanIpAddr, aniDevBase=aniDevBase, aniDevDefaultGateway=aniDevDefaultGateway)
