#
# PySNMP MIB module ZYXEL-OUT-OF-BAND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-OUT-OF-BAND-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelOutOfBand = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58))
if mibBuilder.loadTexts: zyxelOutOfBand.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelOutOfBand.setOrganization('Enterprise Solution ZyXEL')
zyxelOutOfBandIpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1))
zyOutOfBandIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandIpAddress.setStatus('current')
zyOutOfBandSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandSubnetMask.setStatus('current')
zyOutOfBandGateway = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandGateway.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-OUT-OF-BAND-MIB", PYSNMP_MODULE_ID=zyxelOutOfBand, zyOutOfBandIpAddress=zyOutOfBandIpAddress, zyOutOfBandGateway=zyOutOfBandGateway, zyOutOfBandSubnetMask=zyOutOfBandSubnetMask, zyxelOutOfBand=zyxelOutOfBand, zyxelOutOfBandIpSetup=zyxelOutOfBandIpSetup)
