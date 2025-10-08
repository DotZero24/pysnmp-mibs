#
# PySNMP MIB module A3COM-HUAWEI-GRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-GRE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("A3COM-HUAWEI-GRE-MIB", h3cGreObjects=h3cGreObjects, h3cGreKeyValue=h3cGreKeyValue, h3cGre=h3cGre, PYSNMP_MODULE_ID=h3cGre, h3cGreEntry=h3cGreEntry, h3cGreKey=h3cGreKey, h3cGreChecksum=h3cGreChecksum, h3cGreTable=h3cGreTable)
