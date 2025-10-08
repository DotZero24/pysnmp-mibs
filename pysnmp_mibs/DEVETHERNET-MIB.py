#
# PySNMP MIB module DEVETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVETHERNET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniDevEthernet = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 11))
if mibBuilder.loadTexts: aniDevEthernet.setLastUpdated('0210251725Z')
if mibBuilder.loadTexts: aniDevEthernet.setOrganization('Aperto Networks')
aniDevEthernetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1))
aniDevEthernetConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("auto-negotiate", 1), ("speed-100mbps-full", 2), ("speed-100mbps-half", 3), ("speed-10mbps-full", 4), ("speed-10mbps-half", 5))).clone('auto-negotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEthernetConfigMode.setStatus('current')
aniDevEthernetCurrentLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevEthernetCurrentLinkStatus.setStatus('current')
aniDevEthernetCurrentSpeed = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("speed-10-mbps", 1), ("speed-100-mbps", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevEthernetCurrentSpeed.setStatus('current')
aniDevEthernetCurrentDuplex = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half-duplex", 1), ("full-duplex", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevEthernetCurrentDuplex.setStatus('current')
mibBuilder.exportSymbols("DEVETHERNET-MIB", aniDevEthernetConfig=aniDevEthernetConfig, aniDevEthernetConfigMode=aniDevEthernetConfigMode, aniDevEthernetCurrentDuplex=aniDevEthernetCurrentDuplex, aniDevEthernetCurrentLinkStatus=aniDevEthernetCurrentLinkStatus, aniDevEthernet=aniDevEthernet, PYSNMP_MODULE_ID=aniDevEthernet, aniDevEthernetCurrentSpeed=aniDevEthernetCurrentSpeed)
