#
# PySNMP MIB module A3COM-HUAWEI-GRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-GRE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cGre = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54))
h3cGre.setRevisions(('2005-06-04 00:00',))
if mibBuilder.loadTexts: h3cGre.setLastUpdated('200506040000Z')
if mibBuilder.loadTexts: h3cGre.setOrganization('Huawei 3Com Technologies Co., Ltd. ')
h3cGreObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1))
h3cGreTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1), )
if mibBuilder.loadTexts: h3cGreTable.setStatus('current')
h3cGreEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cGreEntry.setStatus('current')
h3cGreKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cGreKeyValue.setStatus('current')
h3cGreKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cGreKey.setStatus('current')
h3cGreChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cGreChecksum.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-GRE-MIB", h3cGreObjects=h3cGreObjects, h3cGreKeyValue=h3cGreKeyValue, h3cGreKey=h3cGreKey, h3cGreChecksum=h3cGreChecksum, PYSNMP_MODULE_ID=h3cGre, h3cGre=h3cGre, h3cGreTable=h3cGreTable, h3cGreEntry=h3cGreEntry)
