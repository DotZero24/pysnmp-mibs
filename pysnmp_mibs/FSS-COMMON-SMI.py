#
# PySNMP MIB module FSS-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fujitsu/FSS-COMMON-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fujitsu = ModuleIdentity((1, 3, 6, 1, 4, 1, 211))
if mibBuilder.loadTexts: fujitsu.setLastUpdated('201605131500Z')
if mibBuilder.loadTexts: fujitsu.setOrganization('Fujitsu Network Communications, Inc.')
product = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1))
transport = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24))
fssCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12))
fssInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700))
fssRouting = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 900))
fssProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100))
mibBuilder.exportSymbols("FSS-COMMON-SMI", transport=transport, fssProtocols=fssProtocols, fssRouting=fssRouting, fssInterfaces=fssInterfaces, PYSNMP_MODULE_ID=fujitsu, fujitsu=fujitsu, product=product, fssCommon=fssCommon)
