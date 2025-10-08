#
# PySNMP MIB module TPLINK-PORTISOLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-PORTISOLATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:30 2025
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
tplinkPortIsolationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 13))
tplinkPortIsolationMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkPortIsolationMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkPortIsolationMIB.setOrganization('TPLINK')
tplinkPortIsolationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 13, 1))
tplinkPortIsolationMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 13, 2))
portIsolationCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1), )
if mibBuilder.loadTexts: portIsolationCtrlTable.setStatus('current')
portIsolationCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: portIsolationCtrlEntry.setStatus('current')
portIsolationPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIsolationPortId.setStatus('current')
portIsolationForList = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portIsolationForList.setStatus('current')
portIsolationLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIsolationLagId.setStatus('current')
mibBuilder.exportSymbols("TPLINK-PORTISOLATION-MIB", portIsolationPortId=portIsolationPortId, tplinkPortIsolationMIBNotifications=tplinkPortIsolationMIBNotifications, portIsolationCtrlTable=portIsolationCtrlTable, portIsolationLagId=portIsolationLagId, portIsolationCtrlEntry=portIsolationCtrlEntry, PYSNMP_MODULE_ID=tplinkPortIsolationMIB, tplinkPortIsolationMIBObjects=tplinkPortIsolationMIBObjects, tplinkPortIsolationMIB=tplinkPortIsolationMIB, portIsolationForList=portIsolationForList)
