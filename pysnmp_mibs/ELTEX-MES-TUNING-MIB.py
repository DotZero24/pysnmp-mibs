#
# PySNMP MIB module ELTEX-MES-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-TUNING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
eltMesTuning = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29))
eltMesTuning.setRevisions(('2014-12-19 00:00',))
if mibBuilder.loadTexts: eltMesTuning.setLastUpdated('201412190000Z')
if mibBuilder.loadTexts: eltMesTuning.setOrganization('Eltex Ltd.')
eltMesTcamTuning = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1))
eltMaxSelectiveQinqIngressRules = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRules.setStatus('current')
eltMaxSelectiveQinqIngressRulesAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRulesAfterReset.setStatus('current')
eltMaxSelectiveQinqEgressRules = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRules.setStatus('current')
eltMaxSelectiveQinqEgressRulesAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRulesAfterReset.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-TUNING-MIB", PYSNMP_MODULE_ID=eltMesTuning, eltMaxSelectiveQinqIngressRulesAfterReset=eltMaxSelectiveQinqIngressRulesAfterReset, eltMesTuning=eltMesTuning, eltMaxSelectiveQinqEgressRulesAfterReset=eltMaxSelectiveQinqEgressRulesAfterReset, eltMaxSelectiveQinqEgressRules=eltMaxSelectiveQinqEgressRules, eltMesTcamTuning=eltMesTcamTuning, eltMaxSelectiveQinqIngressRules=eltMaxSelectiveQinqIngressRules)
