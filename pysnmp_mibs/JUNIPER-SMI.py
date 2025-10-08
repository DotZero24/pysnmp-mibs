#
# PySNMP MIB module JUNIPER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/JUNIPER-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("JUNIPER-SMI", juniperMIB=juniperMIB, jnxExperiment=jnxExperiment, jnxServices=jnxServices, jnxRmonTraps=jnxRmonTraps, jnxTraps=jnxTraps, jnxPMonNotifications=jnxPMonNotifications, jnxCmNotifications=jnxCmNotifications, jnxChassisOKTraps=jnxChassisOKTraps, PYSNMP_MODULE_ID=juniperMIB, jnxMibs=jnxMibs, jnxProducts=jnxProducts, jnxChassisTraps=jnxChassisTraps, jnxSonetNotifications=jnxSonetNotifications, jnxLdpTraps=jnxLdpTraps)
