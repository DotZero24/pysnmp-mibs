#
# PySNMP MIB module ENTERASYS-8021X-REKEYING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-8021X-REKEYING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
dot1xPaePortNumber, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
etsys8021xRekeyingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17))
etsys8021xRekeyingMIB.setRevisions(('2004-07-14 15:07', '2002-03-07 20:06',))
if mibBuilder.loadTexts: etsys8021xRekeyingMIB.setLastUpdated('200407141507Z')
if mibBuilder.loadTexts: etsys8021xRekeyingMIB.setOrganization('Enterasys Networks, Inc')
etsysDot1xRekeyingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1))
etsysDot1xRekeyBaseBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1))
etsysDot1xRekeyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1), )
if mibBuilder.loadTexts: etsysDot1xRekeyConfigTable.setStatus('current')
etsysDot1xRekeyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: etsysDot1xRekeyConfigEntry.setStatus('current')
etsysDot1xRekeyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyEnabled.setStatus('current')
etsysDot1xRekeyPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 2), Unsigned32().clone(1800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyPeriod.setStatus('current')
etsysDot1xRekeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keylen40", 1), ("keylen128", 2))).clone('keylen128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyLength.setStatus('current')
etsysDot1xRekeyAsymmetric = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyAsymmetric.setStatus('current')
etsysDot1xRekeyPairwise = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot1xRekeyPairwise.setStatus('current')
etsysDot1xRekeyingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2))
etsysDot1xRekeyingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1))
etsysDot1xRekeyingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 2))
etsysDot1xRekeyingBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1, 1)).setObjects(("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyPeriod"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyEnabled"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyLength"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyAsymmetric"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1xRekeyingBaseGroup = etsysDot1xRekeyingBaseGroup.setStatus('current')
etsysDot1xRekeyingPairwiseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1, 2)).setObjects(("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyPairwise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1xRekeyingPairwiseGroup = etsysDot1xRekeyingPairwiseGroup.setStatus('current')
etsysDot1xRekeyingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 2, 1)).setObjects(("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyingBaseGroup"), ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyingPairwiseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot1xRekeyingCompliance = etsysDot1xRekeyingCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-8021X-REKEYING-MIB", etsysDot1xRekeyingConformance=etsysDot1xRekeyingConformance, etsysDot1xRekeyingCompliances=etsysDot1xRekeyingCompliances, etsysDot1xRekeyConfigTable=etsysDot1xRekeyConfigTable, etsysDot1xRekeyConfigEntry=etsysDot1xRekeyConfigEntry, etsysDot1xRekeyingBaseGroup=etsysDot1xRekeyingBaseGroup, etsysDot1xRekeyingPairwiseGroup=etsysDot1xRekeyingPairwiseGroup, etsys8021xRekeyingMIB=etsys8021xRekeyingMIB, PYSNMP_MODULE_ID=etsys8021xRekeyingMIB, etsysDot1xRekeyingGroups=etsysDot1xRekeyingGroups, etsysDot1xRekeyingCompliance=etsysDot1xRekeyingCompliance, etsysDot1xRekeyBaseBranch=etsysDot1xRekeyBaseBranch, etsysDot1xRekeyAsymmetric=etsysDot1xRekeyAsymmetric, etsysDot1xRekeyPeriod=etsysDot1xRekeyPeriod, etsysDot1xRekeyPairwise=etsysDot1xRekeyPairwise, etsysDot1xRekeyEnabled=etsysDot1xRekeyEnabled, etsysDot1xRekeyingObjects=etsysDot1xRekeyingObjects, etsysDot1xRekeyLength=etsysDot1xRekeyLength)
