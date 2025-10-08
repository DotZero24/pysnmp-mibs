#
# PySNMP MIB module JUNIPER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/JUNIPER-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniperMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636))
juniperMIB.setRevisions(('2003-04-17 01:00',))
if mibBuilder.loadTexts: juniperMIB.setLastUpdated('200304170100Z')
if mibBuilder.loadTexts: juniperMIB.setOrganization('Juniper Networks, Inc.')
jnxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 1))
if mibBuilder.loadTexts: jnxProducts.setStatus('current')
jnxServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 2))
if mibBuilder.loadTexts: jnxServices.setStatus('current')
jnxMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3))
if mibBuilder.loadTexts: jnxMibs.setStatus('current')
jnxTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 4))
if mibBuilder.loadTexts: jnxTraps.setStatus('current')
jnxChassisTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 1))
jnxChassisOKTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 2))
jnxRmonTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 3))
jnxLdpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 4))
jnxCmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 5))
jnxSonetNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 6))
jnxPMonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 7))
jnxExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5))
mibBuilder.exportSymbols("JUNIPER-SMI", jnxExperiment=jnxExperiment, jnxLdpTraps=jnxLdpTraps, jnxServices=jnxServices, PYSNMP_MODULE_ID=juniperMIB, jnxPMonNotifications=jnxPMonNotifications, jnxChassisOKTraps=jnxChassisOKTraps, jnxSonetNotifications=jnxSonetNotifications, jnxTraps=jnxTraps, jnxChassisTraps=jnxChassisTraps, jnxCmNotifications=jnxCmNotifications, juniperMIB=juniperMIB, jnxMibs=jnxMibs, jnxProducts=jnxProducts, jnxRmonTraps=jnxRmonTraps)
