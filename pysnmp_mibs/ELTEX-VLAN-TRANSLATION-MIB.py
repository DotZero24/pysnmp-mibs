#
# PySNMP MIB module ELTEX-VLAN-TRANSLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-VLAN-TRANSLATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-VLAN-TRANSLATION-MIB", eltexSqinqObjects=eltexSqinqObjects, eltexSqinqActionVlan=eltexSqinqActionVlan, eltexSqinqAction=eltexSqinqAction, PYSNMP_MODULE_ID=eltexVlanTranslationMIB, eltexSqinqPortEntry=eltexSqinqPortEntry, eltexSqinqDirection=eltexSqinqDirection, EltexSqinqAction=EltexSqinqAction, eltexVlanTranslationObjects=eltexVlanTranslationObjects, eltexSqinqStatistics=eltexSqinqStatistics, EltexSqinqDirection=EltexSqinqDirection, eltexSqinqGlobals=eltexSqinqGlobals, eltexSqinqRowStatus=eltexSqinqRowStatus, eltexSqinqConfigs=eltexSqinqConfigs, eltexVlanTranslationMIB=eltexVlanTranslationMIB, eltexSqinqPortTable=eltexSqinqPortTable, eltexSqinqClassifierVlan=eltexSqinqClassifierVlan)
