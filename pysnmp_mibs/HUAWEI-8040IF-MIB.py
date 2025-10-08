#
# PySNMP MIB module HUAWEI-8040IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/HUAWEI-8040IF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mlsr, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "mlsr")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hw8040If = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7))
if mibBuilder.loadTexts: hw8040If.setLastUpdated('200410110000Z')
if mibBuilder.loadTexts: hw8040If.setOrganization('Huawei-3com Technologies co.,Ltd.')
hw8040IfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1), )
if mibBuilder.loadTexts: hw8040IfTable.setStatus('current')
hw8040IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hw8040IfEntry.setStatus('current')
hw8040IfInPerSecBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040IfInPerSecBits.setStatus('current')
hw8040IfOutPerSecBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040IfOutPerSecBits.setStatus('current')
hw8040CRCIfInputErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040CRCIfInputErr.setStatus('current')
hw8040IfOutCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040IfOutCollisions.setStatus('current')
hw8040IfDescCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hw8040IfDescCfg.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-8040IF-MIB", hw8040IfTable=hw8040IfTable, PYSNMP_MODULE_ID=hw8040If, hw8040CRCIfInputErr=hw8040CRCIfInputErr, hw8040If=hw8040If, hw8040IfEntry=hw8040IfEntry, hw8040IfOutPerSecBits=hw8040IfOutPerSecBits, hw8040IfOutCollisions=hw8040IfOutCollisions, hw8040IfDescCfg=hw8040IfDescCfg, hw8040IfInPerSecBits=hw8040IfInPerSecBits)
