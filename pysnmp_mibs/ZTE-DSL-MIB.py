#
# PySNMP MIB module ZTE-DSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZTE-DSL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zte = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902))
zte.setRevisions(('1904-09-22 00:00',))
if mibBuilder.loadTexts: zte.setLastUpdated('0110290000Z')
if mibBuilder.loadTexts: zte.setOrganization('Zhongxing Telcom Co. Ltd.')
zxDsl = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004))
zxPON = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1012))
mibBuilder.exportSymbols("ZTE-DSL-MIB", zxPON=zxPON, zte=zte, zxDsl=zxDsl, PYSNMP_MODULE_ID=zte)
