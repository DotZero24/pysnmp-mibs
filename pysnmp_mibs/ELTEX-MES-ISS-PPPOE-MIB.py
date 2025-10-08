#
# PySNMP MIB module ELTEX-MES-ISS-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-PPPOE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
eltMesIssPppoeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2))
eltMesIssPppoeMIB.setRevisions(('2018-11-22 00:00',))
if mibBuilder.loadTexts: eltMesIssPppoeMIB.setLastUpdated('201811220000Z')
if mibBuilder.loadTexts: eltMesIssPppoeMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssPppoeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2, 1))
eltMesIssPppoeGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2, 1, 1))
eltMesIssPppoePassthroughEnabled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 2, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssPppoePassthroughEnabled.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-PPPOE-MIB", eltMesIssPppoeGlobals=eltMesIssPppoeGlobals, eltMesIssPppoeMIB=eltMesIssPppoeMIB, eltMesIssPppoePassthroughEnabled=eltMesIssPppoePassthroughEnabled, eltMesIssPppoeObjects=eltMesIssPppoeObjects, PYSNMP_MODULE_ID=eltMesIssPppoeMIB)
