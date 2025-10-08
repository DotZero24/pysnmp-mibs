#
# PySNMP MIB module ZTE-DSL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZTE-DSL-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
zxDslPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1004, 43))
if mibBuilder.loadTexts: zxDslPortMib.setLastUpdated('200712161500Z')
if mibBuilder.loadTexts: zxDslPortMib.setOrganization('ZTE Corporation')
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxDsl = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004))
zxDslPortMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1))
zxDslPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1))
zxDslPortTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 3))
zxDslPortTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1, 10), )
if mibBuilder.loadTexts: zxDslPortTable.setStatus('current')
zxDslPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zxDslPortEntry.setStatus('current')
zxDslPortLockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unlock", 1), ("lock", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslPortLockStatus.setStatus('current')
mibBuilder.exportSymbols("ZTE-DSL-PORT-MIB", zte=zte, zxDslPortObjects=zxDslPortObjects, zxDslPortEntry=zxDslPortEntry, zxDslPortLockStatus=zxDslPortLockStatus, zxDslPortMib=zxDslPortMib, zxDslPortTrapObjects=zxDslPortTrapObjects, zxDslPortTable=zxDslPortTable, zxDslPortMibObjects=zxDslPortMibObjects, PYSNMP_MODULE_ID=zxDslPortMib, zxDsl=zxDsl)
