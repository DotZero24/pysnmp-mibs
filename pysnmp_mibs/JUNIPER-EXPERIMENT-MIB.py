#
# PySNMP MIB module JUNIPER-EXPERIMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/JUNIPER-EXPERIMENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
juniperMIB, = mibBuilder.importSymbols("JUNIPER-SMI", "juniperMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxExperiment = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 5))
jnxExperiment.setRevisions(('2003-04-17 01:00',))
if mibBuilder.loadTexts: jnxExperiment.setLastUpdated('200304170100Z')
if mibBuilder.loadTexts: jnxExperiment.setOrganization('Juniper Networks, Inc.')
jnxBgpM2Experiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 5, 1))
if mibBuilder.loadTexts: jnxBgpM2Experiment.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-EXPERIMENT-MIB", jnxExperiment=jnxExperiment, jnxBgpM2Experiment=jnxBgpM2Experiment, PYSNMP_MODULE_ID=jnxExperiment)
