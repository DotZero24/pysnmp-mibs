#
# PySNMP MIB module PPPOE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/PPPOE-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swPPPoEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 79))
if mibBuilder.loadTexts: swPPPoEMIB.setLastUpdated('0904020000Z')
if mibBuilder.loadTexts: swPPPoEMIB.setOrganization('D-Link Corp')
swPPPoEMgmtCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 79, 1))
swPPPoECirIDInsertState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertState.setStatus('current')
swPPPoECirIDInsertPortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2))
swPPPoECirIDInsertPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1), )
if mibBuilder.loadTexts: swPPPoECirIDInsertPortTable.setStatus('current')
swPPPoECirIDInsertPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1), ).setIndexNames((0, "PPPOE-MGMT-MIB", "swPPPoECirIDInsertPortIndex"))
if mibBuilder.loadTexts: swPPPoECirIDInsertPortEntry.setStatus('current')
swPPPoECirIDInsertPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: swPPPoECirIDInsertPortIndex.setStatus('current')
swPPPoECirIDInsertPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertPortState.setStatus('current')
swPPPoECirIDInsertPortCirID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("switch-ip", 1), ("switch-mac", 2), ("udf-string", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertPortCirID.setStatus('current')
swPPPoECirIDInsertPortUDFString = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertPortUDFString.setStatus('current')
mibBuilder.exportSymbols("PPPOE-MGMT-MIB", swPPPoECirIDInsertPortTable=swPPPoECirIDInsertPortTable, swPPPoECirIDInsertPortUDFString=swPPPoECirIDInsertPortUDFString, swPPPoECirIDInsertPortIndex=swPPPoECirIDInsertPortIndex, swPPPoECirIDInsertPortEntry=swPPPoECirIDInsertPortEntry, swPPPoECirIDInsertState=swPPPoECirIDInsertState, swPPPoECirIDInsertPortCirID=swPPPoECirIDInsertPortCirID, swPPPoECirIDInsertPortMgmt=swPPPoECirIDInsertPortMgmt, swPPPoEMgmtCtrl=swPPPoEMgmtCtrl, swPPPoECirIDInsertPortState=swPPPoECirIDInsertPortState, swPPPoEMIB=swPPPoEMIB, PYSNMP_MODULE_ID=swPPPoEMIB)
