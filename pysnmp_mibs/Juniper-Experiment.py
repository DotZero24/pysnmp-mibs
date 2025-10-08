#
# PySNMP MIB module Juniper-Experiment (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-Experiment
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
juniperUniExperiment, = mibBuilder.importSymbols("Juniper-UNI-SMI", "juniperUniExperiment")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("Juniper-Experiment", juniMplsVPNExperiment=juniMplsVPNExperiment, PYSNMP_MODULE_ID=juniExperiment, juniSonetApsExperiment=juniSonetApsExperiment, juniExperiment=juniExperiment, juniMplsExperiment=juniMplsExperiment, juniBFDExperiment=juniBFDExperiment, juniDvmrpExperiment=juniDvmrpExperiment)
