#
# PySNMP MIB module ELTEX-MES-ISS-ERPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-ERPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
fsErpsContextId, fsErpsRingId = mibBuilder.importSymbols("ARICENT-ERPS-MIB", "fsErpsContextId", "fsErpsRingId")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
eltMesIssErpsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 29))
eltMesIssErpsMIB.setRevisions(('2021-12-06 00:00',))
if mibBuilder.loadTexts: eltMesIssErpsMIB.setLastUpdated('202112060000Z')
if mibBuilder.loadTexts: eltMesIssErpsMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssErpsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1))
eltMesIssErpsRingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1))
eltMesIssErpsRingIfmTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2), )
if mibBuilder.loadTexts: eltMesIssErpsRingIfmTable.setStatus('current')
eltMesIssErpsRingIfmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2, 1), ).setIndexNames((0, "ARICENT-ERPS-MIB", "fsErpsContextId"), (0, "ARICENT-ERPS-MIB", "fsErpsRingId"))
if mibBuilder.loadTexts: eltMesIssErpsRingIfmEntry.setStatus('current')
eltMesIssErpsRingIfmMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssErpsRingIfmMdLevel.setStatus('current')
eltMesIssErpsRingIfmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 29, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssErpsRingIfmRowStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-ERPS-MIB", eltMesIssErpsRingIfmRowStatus=eltMesIssErpsRingIfmRowStatus, eltMesIssErpsRingIfmEntry=eltMesIssErpsRingIfmEntry, eltMesIssErpsRingConfig=eltMesIssErpsRingConfig, eltMesIssErpsRingIfmMdLevel=eltMesIssErpsRingIfmMdLevel, eltMesIssErpsMIB=eltMesIssErpsMIB, PYSNMP_MODULE_ID=eltMesIssErpsMIB, eltMesIssErpsRingIfmTable=eltMesIssErpsRingIfmTable, eltMesIssErpsObjects=eltMesIssErpsObjects)
