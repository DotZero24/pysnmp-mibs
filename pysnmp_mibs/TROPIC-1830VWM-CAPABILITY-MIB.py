#
# PySNMP MIB module TROPIC-1830VWM-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TROPIC-1830VWM-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:19:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tnVwmMsAgentCapability, = mibBuilder.importSymbols("TROPIC-VWMMS-MIB", "tnVwmMsAgentCapability")
tn1830VwmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 100, 1))
tn1830VwmCapability.setRevisions(('2019-05-09 00:00', '2019-04-30 00:00', '2019-04-11 00:00', '2019-03-11 00:00', '2019-03-08 00:00', '2019-01-31 00:00', '2018-12-07 00:00', '2018-11-30 00:00', '2018-11-15 00:00', '2018-11-05 00:00', '2018-10-03 00:00', '2018-09-12 00:00', '2018-09-05 00:00', '2018-08-20 00:00', '2018-07-09 00:00', '2018-06-22 00:00', '2018-06-06 00:00', '2018-06-01 00:00', '2018-05-15 00:00', '2018-03-16 00:00', '2018-03-08 00:00', '2018-02-27 00:00', '2018-02-23 12:00', '2018-02-08 00:00', '2018-01-12 00:00', '2017-12-13 00:00', '2017-11-21 00:00', '2017-11-01 00:00', '2017-10-13 00:00', '2017-09-29 00:00', '2017-07-14 00:00', '2017-07-05 00:00', '2017-06-16 00:00', '2017-04-24 00:00', '2017-04-06 00:00', '2017-02-06 00:00', '2017-01-13 00:00', '2016-12-16 00:00', '2016-11-04 00:00', '2016-10-28 00:00', '2016-09-26 00:00', '2016-08-17 00:00', '2016-08-11 00:00', '2016-06-16 00:00', '2016-05-31 00:00', '2016-05-13 00:00', '2016-04-15 00:00',))
if mibBuilder.loadTexts: tn1830VwmCapability.setLastUpdated('201905090000Z')
if mibBuilder.loadTexts: tn1830VwmCapability.setOrganization('Nokia')
tn1830VwmCapabilityR901 = AgentCapabilities((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 100, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn1830VwmCapabilityR901 = tn1830VwmCapabilityR901.setProductRelease('Release 9.0.1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn1830VwmCapabilityR901 = tn1830VwmCapabilityR901.setStatus('current')
mibBuilder.exportSymbols("TROPIC-1830VWM-CAPABILITY-MIB", PYSNMP_MODULE_ID=tn1830VwmCapability, tn1830VwmCapability=tn1830VwmCapability, tn1830VwmCapabilityR901=tn1830VwmCapabilityR901)
