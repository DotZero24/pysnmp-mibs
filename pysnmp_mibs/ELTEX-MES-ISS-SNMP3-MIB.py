#
# PySNMP MIB module ELTEX-MES-ISS-SNMP3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SNMP3-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
eltMesIssSnmp3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19))
eltMesIssSnmp3MIB.setRevisions(('2019-11-06 00:00',))
if mibBuilder.loadTexts: eltMesIssSnmp3MIB.setLastUpdated('201911060000Z')
if mibBuilder.loadTexts: eltMesIssSnmp3MIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssSnmp3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1))
eltMesIssSnmp3Globals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1, 1))
eltMesIssWarmStartTrapControl = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssWarmStartTrapControl.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-SNMP3-MIB", eltMesIssSnmp3Globals=eltMesIssSnmp3Globals, eltMesIssWarmStartTrapControl=eltMesIssWarmStartTrapControl, eltMesIssSnmp3MIB=eltMesIssSnmp3MIB, eltMesIssSnmp3Objects=eltMesIssSnmp3Objects, PYSNMP_MODULE_ID=eltMesIssSnmp3MIB)
