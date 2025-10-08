#
# PySNMP MIB module DGS3120-24SC-LED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DGS3120-24SC-LED-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Dgs3120Proj_DGS_3120_24SC_bx, = mibBuilder.importSymbols("SWDGS3120PRIMGMT-MIB", "dlink-Dgs3120Proj-DGS-3120-24SC-bx")
swLedMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 117, 4, 1, 4))
if mibBuilder.loadTexts: swLedMIB.setLastUpdated('201106100000Z')
if mibBuilder.loadTexts: swLedMIB.setOrganization('D-Link Corp.')
swLedMIBObject = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 4, 1, 4, 1))
swLedInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 117, 4, 1, 4, 1, 1), )
if mibBuilder.loadTexts: swLedInfoTable.setStatus('current')
swLedInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 117, 4, 1, 4, 1, 1, 1), ).setIndexNames((0, "DGS3120-24SC-LED-MIB", "swLedInfoUnitId"))
if mibBuilder.loadTexts: swLedInfoEntry.setStatus('current')
swLedInfoUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 4, 1, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLedInfoUnitId.setStatus('current')
swLedInfoFrontPanelLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 4, 1, 4, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLedInfoFrontPanelLedStatus.setStatus('current')
mibBuilder.exportSymbols("DGS3120-24SC-LED-MIB", swLedInfoFrontPanelLedStatus=swLedInfoFrontPanelLedStatus, swLedMIBObject=swLedMIBObject, swLedMIB=swLedMIB, swLedInfoTable=swLedInfoTable, PYSNMP_MODULE_ID=swLedMIB, swLedInfoEntry=swLedInfoEntry, swLedInfoUnitId=swLedInfoUnitId)
