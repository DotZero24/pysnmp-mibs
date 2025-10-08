#
# PySNMP MIB module SUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oracle/SUN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42))
if mibBuilder.loadTexts: sunMIB.setLastUpdated('200309180000Z')
if mibBuilder.loadTexts: sunMIB.setOrganization('Sun Microsystems, Inc.')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 2))
sma = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 2, 4))
mibBuilder.exportSymbols("SUN-MIB", sun=sun, sunMIB=sunMIB, sma=sma, products=products, management=management, PYSNMP_MODULE_ID=sunMIB)
