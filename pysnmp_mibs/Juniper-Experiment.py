#
# PySNMP MIB module Juniper-Experiment (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-Experiment
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniperUniExperiment, = mibBuilder.importSymbols("Juniper-UNI-SMI", "juniperUniExperiment")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniExperiment = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2))
juniExperiment.setRevisions(('2002-11-13 20:58', '2001-06-20 20:36', '2000-10-24 21:00',))
if mibBuilder.loadTexts: juniExperiment.setLastUpdated('200211132058Z')
if mibBuilder.loadTexts: juniExperiment.setOrganization('Juniper Networks, Inc.')
juniDvmrpExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1))
if mibBuilder.loadTexts: juniDvmrpExperiment.setStatus('current')
juniSonetApsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 2))
if mibBuilder.loadTexts: juniSonetApsExperiment.setStatus('current')
juniMplsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 3))
if mibBuilder.loadTexts: juniMplsExperiment.setStatus('current')
juniMplsVPNExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 4))
if mibBuilder.loadTexts: juniMplsVPNExperiment.setStatus('current')
juniBFDExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 5))
if mibBuilder.loadTexts: juniBFDExperiment.setStatus('current')
mibBuilder.exportSymbols("Juniper-Experiment", juniMplsExperiment=juniMplsExperiment, PYSNMP_MODULE_ID=juniExperiment, juniSonetApsExperiment=juniSonetApsExperiment, juniMplsVPNExperiment=juniMplsVPNExperiment, juniExperiment=juniExperiment, juniBFDExperiment=juniBFDExperiment, juniDvmrpExperiment=juniDvmrpExperiment)
