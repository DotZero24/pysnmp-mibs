#
# PySNMP MIB module ELTEX-MES-ISS-ERPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-ERPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
fsErpsContextId, fsErpsRingId = mibBuilder.importSymbols("ARICENT-ERPS-MIB", "fsErpsContextId", "fsErpsRingId")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-ISS-ERPS-MIB", eltMesIssErpsRingConfig=eltMesIssErpsRingConfig, eltMesIssErpsRingIfmMdLevel=eltMesIssErpsRingIfmMdLevel, PYSNMP_MODULE_ID=eltMesIssErpsMIB, eltMesIssErpsObjects=eltMesIssErpsObjects, eltMesIssErpsRingIfmRowStatus=eltMesIssErpsRingIfmRowStatus, eltMesIssErpsRingIfmTable=eltMesIssErpsRingIfmTable, eltMesIssErpsMIB=eltMesIssErpsMIB, eltMesIssErpsRingIfmEntry=eltMesIssErpsRingIfmEntry)
