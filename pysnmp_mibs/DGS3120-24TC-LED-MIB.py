#
# PySNMP MIB module DGS3120-24TC-LED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DGS3120-24TC-LED-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Dgs3120Proj_DGS_3120_24TC_bx, = mibBuilder.importSymbols("SWDGS3120PRIMGMT-MIB", "dlink-Dgs3120Proj-DGS-3120-24TC-bx")
swLedMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 117, 2, 1, 4))
if mibBuilder.loadTexts: swLedMIB.setLastUpdated('201106100000Z')
if mibBuilder.loadTexts: swLedMIB.setOrganization('D-Link Corp.')
swLedMIBObject = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 2, 1, 4, 1))
swLedInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 117, 2, 1, 4, 1, 1), )
if mibBuilder.loadTexts: swLedInfoTable.setStatus('current')
swLedInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 117, 2, 1, 4, 1, 1, 1), ).setIndexNames((0, "DGS3120-24TC-LED-MIB", "swLedInfoUnitId"))
if mibBuilder.loadTexts: swLedInfoEntry.setStatus('current')
swLedInfoUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 2, 1, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLedInfoUnitId.setStatus('current')
swLedInfoFrontPanelLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 2, 1, 4, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLedInfoFrontPanelLedStatus.setStatus('current')
mibBuilder.exportSymbols("DGS3120-24TC-LED-MIB", swLedMIBObject=swLedMIBObject, PYSNMP_MODULE_ID=swLedMIB, swLedInfoUnitId=swLedInfoUnitId, swLedInfoTable=swLedInfoTable, swLedInfoFrontPanelLedStatus=swLedInfoFrontPanelLedStatus, swLedMIB=swLedMIB, swLedInfoEntry=swLedInfoEntry)
