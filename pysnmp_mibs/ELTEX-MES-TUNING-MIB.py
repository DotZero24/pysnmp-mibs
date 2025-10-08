#
# PySNMP MIB module ELTEX-MES-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-TUNING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-TUNING-MIB", eltMaxSelectiveQinqIngressRulesAfterReset=eltMaxSelectiveQinqIngressRulesAfterReset, eltMaxSelectiveQinqIngressRules=eltMaxSelectiveQinqIngressRules, eltMaxSelectiveQinqEgressRules=eltMaxSelectiveQinqEgressRules, PYSNMP_MODULE_ID=eltMesTuning, eltMesTcamTuning=eltMesTcamTuning, eltMaxSelectiveQinqEgressRulesAfterReset=eltMaxSelectiveQinqEgressRulesAfterReset, eltMesTuning=eltMesTuning)
