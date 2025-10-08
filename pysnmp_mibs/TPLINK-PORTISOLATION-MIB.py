#
# PySNMP MIB module TPLINK-PORTISOLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-PORTISOLATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:55 2025
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
mibBuilder.exportSymbols("TPLINK-PORTISOLATION-MIB", tplinkPortIsolationMIB=tplinkPortIsolationMIB, tplinkPortIsolationMIBNotifications=tplinkPortIsolationMIBNotifications, tplinkPortIsolationMIBObjects=tplinkPortIsolationMIBObjects, portIsolationPortId=portIsolationPortId, portIsolationForList=portIsolationForList, portIsolationCtrlEntry=portIsolationCtrlEntry, portIsolationLagId=portIsolationLagId, portIsolationCtrlTable=portIsolationCtrlTable, PYSNMP_MODULE_ID=tplinkPortIsolationMIB)
