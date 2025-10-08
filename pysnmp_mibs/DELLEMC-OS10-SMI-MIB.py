#
# PySNMP MIB module DELLEMC-OS10-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELLEMC-OS10-SMI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dell = ModuleIdentity((1, 3, 6, 1, 4, 1, 674))
dell.setRevisions(('2018-07-06 12:00',))
if mibBuilder.loadTexts: dell.setLastUpdated('201807061200Z')
if mibBuilder.loadTexts: dell.setOrganization('Dell Emc')
enterpriseSW = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000))
networking = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000, 5000))
os10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100))
if mibBuilder.loadTexts: os10.setStatus('current')
os10Experiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200))
if mibBuilder.loadTexts: os10Experiment.setStatus('current')
mibBuilder.exportSymbols("DELLEMC-OS10-SMI-MIB", PYSNMP_MODULE_ID=dell, enterpriseSW=enterpriseSW, dell=dell, os10Experiment=os10Experiment, networking=networking, os10=os10)
