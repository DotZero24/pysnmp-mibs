#
# PySNMP MIB module CISCO-CDSTV-BWMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-CDSTV-BWMGR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-CDSTV-BWMGR-MIB", cdstvBWMgrAddressType=cdstvBWMgrAddressType, cdstvBWMgrDatabaseThreadPool=cdstvBWMgrDatabaseThreadPool, cdstvBWMgrSyncAlarm=cdstvBWMgrSyncAlarm, ciscoCdstvBWMgrMIBConform=ciscoCdstvBWMgrMIBConform, PYSNMP_MODULE_ID=ciscoCdstvBwmgrMIB, ciscoCdstvBWMgrMIBMainObjectGroup=ciscoCdstvBWMgrMIBMainObjectGroup, ciscoCdstvBWMgrMIBNotifs=ciscoCdstvBWMgrMIBNotifs, cdstvBWMgrPort=cdstvBWMgrPort, ciscoCdstvBwmgrMIB=ciscoCdstvBwmgrMIB, cdstvBWMgrServerThreadPool=cdstvBWMgrServerThreadPool, ciscoCdstvBWMgrMIBCompliances=ciscoCdstvBWMgrMIBCompliances, ciscoCdstvBWMgrMIBCompliance=ciscoCdstvBWMgrMIBCompliance, cdstvBWMgrAddress=cdstvBWMgrAddress, ciscoCdstvBWMgrMIBObjects=ciscoCdstvBWMgrMIBObjects, cdstvBWMgrSyncThreadPool=cdstvBWMgrSyncThreadPool, ciscoCdstvBWMgrMIBGroups=ciscoCdstvBWMgrMIBGroups)
