#
# PySNMP MIB module CISCO-CDSTV-BWMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-CDSTV-BWMGR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCdstvBwmgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 749))
ciscoCdstvBwmgrMIB.setRevisions(('2010-06-24 00:00',))
if mibBuilder.loadTexts: ciscoCdstvBwmgrMIB.setLastUpdated('201006240000Z')
if mibBuilder.loadTexts: ciscoCdstvBwmgrMIB.setOrganization('Cisco Systems, Inc.')
ciscoCdstvBWMgrMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 0))
ciscoCdstvBWMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 1))
ciscoCdstvBWMgrMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 2))
ciscoCdstvBWMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 1))
cdstvBWMgrAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrAddressType.setStatus('current')
cdstvBWMgrAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrAddress.setStatus('current')
cdstvBWMgrPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 3), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(7791)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrPort.setStatus('current')
cdstvBWMgrDatabaseThreadPool = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrDatabaseThreadPool.setStatus('current')
cdstvBWMgrServerThreadPool = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrServerThreadPool.setStatus('current')
cdstvBWMgrSyncThreadPool = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrSyncThreadPool.setStatus('current')
cdstvBWMgrSyncAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 7), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(2400, 4294967295)).clone(864000)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrSyncAlarm.setStatus('current')
ciscoCdstvBWMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 2))
ciscoCdstvBWMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 1, 1)).setObjects(("CISCO-CDSTV-BWMGR-MIB", "ciscoCdstvBWMgrMIBMainObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvBWMgrMIBCompliance = ciscoCdstvBWMgrMIBCompliance.setStatus('current')
ciscoCdstvBWMgrMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 2, 1)).setObjects(("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrAddress"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrPort"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrDatabaseThreadPool"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrServerThreadPool"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrSyncThreadPool"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrSyncAlarm"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvBWMgrMIBMainObjectGroup = ciscoCdstvBWMgrMIBMainObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-BWMGR-MIB", ciscoCdstvBWMgrMIBCompliance=ciscoCdstvBWMgrMIBCompliance, ciscoCdstvBWMgrMIBMainObjectGroup=ciscoCdstvBWMgrMIBMainObjectGroup, ciscoCdstvBWMgrMIBGroups=ciscoCdstvBWMgrMIBGroups, ciscoCdstvBWMgrMIBNotifs=ciscoCdstvBWMgrMIBNotifs, cdstvBWMgrDatabaseThreadPool=cdstvBWMgrDatabaseThreadPool, cdstvBWMgrPort=cdstvBWMgrPort, ciscoCdstvBWMgrMIBConform=ciscoCdstvBWMgrMIBConform, PYSNMP_MODULE_ID=ciscoCdstvBwmgrMIB, cdstvBWMgrAddressType=cdstvBWMgrAddressType, cdstvBWMgrSyncThreadPool=cdstvBWMgrSyncThreadPool, ciscoCdstvBwmgrMIB=ciscoCdstvBwmgrMIB, ciscoCdstvBWMgrMIBCompliances=ciscoCdstvBWMgrMIBCompliances, cdstvBWMgrAddress=cdstvBWMgrAddress, ciscoCdstvBWMgrMIBObjects=ciscoCdstvBWMgrMIBObjects, cdstvBWMgrServerThreadPool=cdstvBWMgrServerThreadPool, cdstvBWMgrSyncAlarm=cdstvBWMgrSyncAlarm)
