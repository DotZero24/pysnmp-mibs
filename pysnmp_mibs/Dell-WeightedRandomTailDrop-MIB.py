#
# PySNMP MIB module Dell-WeightedRandomTailDrop-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/Dell-WeightedRandomTailDrop-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlWeightedRandomTailDrop = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 146))
rlWeightedRandomTailDrop.setRevisions(('2009-09-29 00:00',))
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setLastUpdated('200909290000Z')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setOrganization('Dell')
rlWeightedRandomTailDropCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 146, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlWeightedRandomTailDropCurrentStatus.setStatus('current')
rlWeightedRandomTailDropStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 146, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlWeightedRandomTailDropStatusAfterReset.setStatus('current')
mibBuilder.exportSymbols("Dell-WeightedRandomTailDrop-MIB", rlWeightedRandomTailDrop=rlWeightedRandomTailDrop, rlWeightedRandomTailDropCurrentStatus=rlWeightedRandomTailDropCurrentStatus, PYSNMP_MODULE_ID=rlWeightedRandomTailDrop, rlWeightedRandomTailDropStatusAfterReset=rlWeightedRandomTailDropStatusAfterReset)
