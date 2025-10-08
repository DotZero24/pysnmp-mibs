#
# PySNMP MIB module ELTEX-MES-ISS-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-LLDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltMesIssLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10))
eltMesIssLldpMIB.setRevisions(('2019-02-12 00:00',))
if mibBuilder.loadTexts: eltMesIssLldpMIB.setLastUpdated('201902120000Z')
if mibBuilder.loadTexts: eltMesIssLldpMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1))
eltMesIssLldpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1, 1))
eltMesIssLldpduMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filtering", 1), ("flooding", 2))).clone('filtering')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssLldpduMode.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-LLDP-MIB", eltMesIssLldpMIB=eltMesIssLldpMIB, PYSNMP_MODULE_ID=eltMesIssLldpMIB, eltMesIssLldpGlobalConfig=eltMesIssLldpGlobalConfig, eltMesIssLldpduMode=eltMesIssLldpduMode, eltMesIssLldpObjects=eltMesIssLldpObjects)
