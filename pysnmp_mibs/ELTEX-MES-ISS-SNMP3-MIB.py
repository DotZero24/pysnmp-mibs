#
# PySNMP MIB module ELTEX-MES-ISS-SNMP3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SNMP3-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
eltMesIssSnmp3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19))
eltMesIssSnmp3MIB.setRevisions(('2019-11-06 00:00',))
if mibBuilder.loadTexts: eltMesIssSnmp3MIB.setLastUpdated('201911060000Z')
if mibBuilder.loadTexts: eltMesIssSnmp3MIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssSnmp3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1))
eltMesIssSnmp3Globals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1, 1))
eltMesIssWarmStartTrapControl = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssWarmStartTrapControl.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-SNMP3-MIB", eltMesIssSnmp3Objects=eltMesIssSnmp3Objects, PYSNMP_MODULE_ID=eltMesIssSnmp3MIB, eltMesIssSnmp3Globals=eltMesIssSnmp3Globals, eltMesIssWarmStartTrapControl=eltMesIssWarmStartTrapControl, eltMesIssSnmp3MIB=eltMesIssSnmp3MIB)
