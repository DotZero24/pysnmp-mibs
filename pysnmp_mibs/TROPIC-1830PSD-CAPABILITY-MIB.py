#
# PySNMP MIB module TROPIC-1830PSD-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TROPIC-1830PSD-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:37:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tnPsdAgentCapability, = mibBuilder.importSymbols("TROPIC-PSD-MIB", "tnPsdAgentCapability")
tn1830PsdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 100, 1))
tn1830PsdCapability.setRevisions(('2021-08-11 00:00', '2021-07-01 00:00', '2021-06-17 00:00', '2021-01-28 12:00', '2021-01-24 12:00', '2021-01-14 12:00', '2020-12-14 12:00', '2020-12-09 12:00', '2020-12-03 12:00', '2020-11-18 12:00', '2020-10-26 12:00', '2020-10-23 12:00', '2020-06-15 12:00', '2020-06-09 12:00', '2020-04-15 12:00', '2020-04-06 12:00', '2020-03-11 12:00', '2020-02-25 12:00', '2020-01-13 12:00', '2019-09-16 12:00', '2018-05-25 12:00', '2018-04-30 12:00', '2018-03-19 12:00', '2018-02-23 12:00', '2018-02-14 12:00', '2017-12-07 12:00', '2017-09-25 12:00', '2017-08-18 12:00', '2017-07-07 12:00', '2017-05-05 12:00', '2017-03-13 12:00', '2017-02-06 12:00', '2016-12-21 12:00', '2016-10-28 12:00',))
if mibBuilder.loadTexts: tn1830PsdCapability.setLastUpdated('202108110000Z')
if mibBuilder.loadTexts: tn1830PsdCapability.setOrganization('Nokia')
tn1830Capability = AgentCapabilities((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 100, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn1830Capability = tn1830Capability.setProductRelease('Release 4.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn1830Capability = tn1830Capability.setStatus('current')
mibBuilder.exportSymbols("TROPIC-1830PSD-CAPABILITY-MIB", tn1830Capability=tn1830Capability, tn1830PsdCapability=tn1830PsdCapability, PYSNMP_MODULE_ID=tn1830PsdCapability)
