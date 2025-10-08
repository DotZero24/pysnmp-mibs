#
# PySNMP MIB module TPLINK-DDMMANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-DDMMANAGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TPLINK-DDMMANAGE-MIB", PYSNMP_MODULE_ID=tplinkDdmManageMIB, tempExceedThreshold=tempExceedThreshold, txPowExceedThreshold=txPowExceedThreshold, biasCurExceedThreshold=biasCurExceedThreshold, volExceedThreshold=volExceedThreshold, tplinkDdmManageMIBObjects=tplinkDdmManageMIBObjects, tplinkDdmManageNotifications=tplinkDdmManageNotifications, tplinkDdmManageMIB=tplinkDdmManageMIB, rxPowExceedThreshold=rxPowExceedThreshold)
