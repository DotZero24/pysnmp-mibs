#
# PySNMP MIB module ELTEX-MES-ISS-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-LLDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
eltMesIssLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10))
eltMesIssLldpMIB.setRevisions(('2019-02-12 00:00',))
if mibBuilder.loadTexts: eltMesIssLldpMIB.setLastUpdated('201902120000Z')
if mibBuilder.loadTexts: eltMesIssLldpMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1))
eltMesIssLldpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1, 1))
eltMesIssLldpduMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filtering", 1), ("flooding", 2))).clone('filtering')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssLldpduMode.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-LLDP-MIB", PYSNMP_MODULE_ID=eltMesIssLldpMIB, eltMesIssLldpMIB=eltMesIssLldpMIB, eltMesIssLldpObjects=eltMesIssLldpObjects, eltMesIssLldpGlobalConfig=eltMesIssLldpGlobalConfig, eltMesIssLldpduMode=eltMesIssLldpduMode)
