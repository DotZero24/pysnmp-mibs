#
# PySNMP MIB module MICROSENS-G6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/microsens/MICROSENS-G6-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
microsens = ModuleIdentity((1, 3, 6, 1, 4, 1, 3181))
microsens.setRevisions(('2018-02-12 16:19',))
if mibBuilder.loadTexts: microsens.setLastUpdated('201802121619Z')
if mibBuilder.loadTexts: microsens.setOrganization('MICROSENS GmbH & Co. KG')
managedSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10))
g6 = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10, 6))
mibBuilder.exportSymbols("MICROSENS-G6-MIB", managedSwitches=managedSwitches, PYSNMP_MODULE_ID=microsens, microsens=microsens, g6=g6)
