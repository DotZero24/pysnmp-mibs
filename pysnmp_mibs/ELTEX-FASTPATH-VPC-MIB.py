#
# PySNMP MIB module ELTEX-FASTPATH-VPC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-FASTPATH-VPC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesFastpath, = mibBuilder.importSymbols("ELTEX-MES-FASTPATH-MIB", "eltMesFastpath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltFastpathVpcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 103, 6))
eltFastpathVpcMIB.setRevisions(('2018-08-31 00:00',))
if mibBuilder.loadTexts: eltFastpathVpcMIB.setLastUpdated('201808310000Z')
if mibBuilder.loadTexts: eltFastpathVpcMIB.setOrganization('Eltex Enterprise Co, Ltd.')
efpVpcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 6, 1))
efpVpcGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 6, 1, 1))
efpVpcOrphanIsolationMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 103, 6, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: efpVpcOrphanIsolationMode.setStatus('current')
efpVpcNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 6, 2))
efpVpcNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 6, 2, 0))
efpVpcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 6, 3))
mibBuilder.exportSymbols("ELTEX-FASTPATH-VPC-MIB", efpVpcNotificationsPrefix=efpVpcNotificationsPrefix, efpVpcGlobals=efpVpcGlobals, efpVpcObjects=efpVpcObjects, efpVpcConformance=efpVpcConformance, PYSNMP_MODULE_ID=eltFastpathVpcMIB, efpVpcNotifications=efpVpcNotifications, eltFastpathVpcMIB=eltFastpathVpcMIB, efpVpcOrphanIsolationMode=efpVpcOrphanIsolationMode)
