#
# PySNMP MIB module ELTEX-VLAN-TRANSLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-VLAN-TRANSLATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
eltexVlanTranslationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 54))
eltexVlanTranslationMIB.setRevisions(('2019-11-07 00:00', '2019-02-04 00:00',))
if mibBuilder.loadTexts: eltexVlanTranslationMIB.setLastUpdated('201911070000Z')
if mibBuilder.loadTexts: eltexVlanTranslationMIB.setOrganization('Eltex Enterprise Co, Ltd.')
class EltexSqinqDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ingress", 1), ("egress", 2))

class EltexSqinqAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("overrideVlan", 1), ("addVlan", 2), ("permit", 3), ("deny", 4))

eltexVlanTranslationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 54, 1))
eltexSqinqObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1))
eltexSqinqGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 1))
eltexSqinqConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2))
eltexSqinqStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 3))
eltexSqinqPortTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1), )
if mibBuilder.loadTexts: eltexSqinqPortTable.setStatus('current')
eltexSqinqPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ELTEX-VLAN-TRANSLATION-MIB", "eltexSqinqDirection"), (0, "ELTEX-VLAN-TRANSLATION-MIB", "eltexSqinqClassifierVlan"))
if mibBuilder.loadTexts: eltexSqinqPortEntry.setStatus('current')
eltexSqinqDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 1), EltexSqinqDirection())
if mibBuilder.loadTexts: eltexSqinqDirection.setStatus('current')
eltexSqinqClassifierVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 2), VlanId())
if mibBuilder.loadTexts: eltexSqinqClassifierVlan.setStatus('current')
eltexSqinqAction = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 3), EltexSqinqAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexSqinqAction.setStatus('current')
eltexSqinqActionVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexSqinqActionVlan.setStatus('current')
eltexSqinqRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexSqinqRowStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-VLAN-TRANSLATION-MIB", eltexSqinqObjects=eltexSqinqObjects, eltexSqinqRowStatus=eltexSqinqRowStatus, eltexSqinqDirection=eltexSqinqDirection, eltexSqinqClassifierVlan=eltexSqinqClassifierVlan, eltexSqinqPortEntry=eltexSqinqPortEntry, EltexSqinqDirection=EltexSqinqDirection, EltexSqinqAction=EltexSqinqAction, eltexSqinqGlobals=eltexSqinqGlobals, PYSNMP_MODULE_ID=eltexVlanTranslationMIB, eltexVlanTranslationMIB=eltexVlanTranslationMIB, eltexSqinqAction=eltexSqinqAction, eltexSqinqStatistics=eltexSqinqStatistics, eltexSqinqPortTable=eltexSqinqPortTable, eltexVlanTranslationObjects=eltexVlanTranslationObjects, eltexSqinqConfigs=eltexSqinqConfigs, eltexSqinqActionVlan=eltexSqinqActionVlan)
