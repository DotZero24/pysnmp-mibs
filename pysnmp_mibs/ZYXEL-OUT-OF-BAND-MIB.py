#
# PySNMP MIB module ZYXEL-OUT-OF-BAND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-OUT-OF-BAND-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-OUT-OF-BAND-MIB", zyOutOfBandGateway=zyOutOfBandGateway, zyxelOutOfBandIpSetup=zyxelOutOfBandIpSetup, zyOutOfBandIpAddress=zyOutOfBandIpAddress, PYSNMP_MODULE_ID=zyxelOutOfBand, zyxelOutOfBand=zyxelOutOfBand, zyOutOfBandSubnetMask=zyOutOfBandSubnetMask)
