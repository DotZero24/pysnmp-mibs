#
# PySNMP MIB module ELTEX-MES-ISS-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-PPPOE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
eltMesIssPppoeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2))
eltMesIssPppoeMIB.setRevisions(('2018-11-22 00:00',))
if mibBuilder.loadTexts: eltMesIssPppoeMIB.setLastUpdated('201811220000Z')
if mibBuilder.loadTexts: eltMesIssPppoeMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssPppoeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2, 1))
eltMesIssPppoeGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2, 1, 1))
eltMesIssPppoePassthroughEnabled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssPppoePassthroughEnabled.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-PPPOE-MIB", eltMesIssPppoeMIB=eltMesIssPppoeMIB, eltMesIssPppoePassthroughEnabled=eltMesIssPppoePassthroughEnabled, eltMesIssPppoeObjects=eltMesIssPppoeObjects, eltMesIssPppoeGlobals=eltMesIssPppoeGlobals, PYSNMP_MODULE_ID=eltMesIssPppoeMIB)
