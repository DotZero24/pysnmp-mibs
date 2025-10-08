#
# PySNMP MIB module FSS-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fujitsu/FSS-COMMON-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fujitsu = ModuleIdentity((1, 3, 6, 1, 4, 1, 211))
if mibBuilder.loadTexts: fujitsu.setLastUpdated('201605131500Z')
if mibBuilder.loadTexts: fujitsu.setOrganization('Fujitsu Network Communications, Inc.')
product = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1))
transport = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24))
fssCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12))
fssInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700))
fssRouting = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 900))
fssProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100))
mibBuilder.exportSymbols("FSS-COMMON-SMI", PYSNMP_MODULE_ID=fujitsu, transport=transport, fssProtocols=fssProtocols, product=product, fssCommon=fssCommon, fssInterfaces=fssInterfaces, fujitsu=fujitsu, fssRouting=fssRouting)
