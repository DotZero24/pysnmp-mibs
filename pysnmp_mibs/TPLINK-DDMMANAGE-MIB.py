#
# PySNMP MIB module TPLINK-DDMMANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-DDMMANAGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkDdmManageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 96))
tplinkDdmManageMIB.setRevisions(('2009-08-27 00:00',))
if mibBuilder.loadTexts: tplinkDdmManageMIB.setLastUpdated('200908270000Z')
if mibBuilder.loadTexts: tplinkDdmManageMIB.setOrganization('TPLINK')
tplinkDdmManageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1))
tplinkDdmManageNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 96, 2))
tempExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 96, 2, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tempExceedThreshold.setStatus('current')
volExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 96, 2, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: volExceedThreshold.setStatus('current')
biasCurExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 96, 2, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: biasCurExceedThreshold.setStatus('current')
txPowExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 96, 2, 4)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: txPowExceedThreshold.setStatus('current')
rxPowExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 96, 2, 5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rxPowExceedThreshold.setStatus('current')
mibBuilder.exportSymbols("TPLINK-DDMMANAGE-MIB", tplinkDdmManageNotifications=tplinkDdmManageNotifications, tempExceedThreshold=tempExceedThreshold, tplinkDdmManageMIB=tplinkDdmManageMIB, biasCurExceedThreshold=biasCurExceedThreshold, PYSNMP_MODULE_ID=tplinkDdmManageMIB, tplinkDdmManageMIBObjects=tplinkDdmManageMIBObjects, txPowExceedThreshold=txPowExceedThreshold, volExceedThreshold=volExceedThreshold, rxPowExceedThreshold=rxPowExceedThreshold)
