#
# PySNMP MIB module HP-ICF-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-VRRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
vrrpAssoIpAddrEntry, vrrpOperEntry, vrrpOperVrId = mibBuilder.importSymbols("VRRP-MIB", "vrrpAssoIpAddrEntry", "vrrpOperEntry", "vrrpOperVrId")
hpicfVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31))
hpicfVrrpMIB.setRevisions(('2021-06-10 00:00', '2012-11-15 00:00', '2013-06-12 00:00', '2012-02-22 00:00', '2010-10-20 00:00', '2010-07-28 00:00', '2009-05-19 00:00', '2008-02-20 00:00', '2007-12-12 00:00', '2007-08-22 00:00', '2005-07-14 00:00',))
if mibBuilder.loadTexts: hpicfVrrpMIB.setLastUpdated('202106100000Z')
if mibBuilder.loadTexts: hpicfVrrpMIB.setOrganization('HP Networking')
hpicfVrrpOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1))
hpicfVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2))
hpicfVrrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpAdminStatus.setStatus('deprecated')
hpicfVrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2), )
if mibBuilder.loadTexts: hpicfVrrpOperTable.setStatus('current')
hpicfVrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1), )
vrrpOperEntry.registerAugmentions(("HP-ICF-VRRP-MIB", "hpicfVrrpOperEntry"))
hpicfVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfVrrpOperEntry.setStatus('current')
hpicfVrrpVrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("owner", 1), ("backup", 2), ("uninitialized", 3))).clone('uninitialized')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrMode.setStatus('current')
hpicfVrrpVrMasterPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrMasterPreempt.setStatus('current')
hpicfVrrpVrTransferControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrTransferControl.setStatus('current')
hpicfVrrpVrPreemptDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrPreemptDelayTime.setStatus('current')
hpicfVrrpVrControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("failback", 1), ("failover", 2), ("failoverWithMonitoring", 3), ("invalid", 4))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrControl.setStatus('current')
hpicfVrrpVrRespondToPing = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrRespondToPing.setStatus('current')
hpicfVrrpVrMainPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrMainPreempt.setStatus('current')
hpicfVrrpAssoIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3), )
if mibBuilder.loadTexts: hpicfVrrpAssoIpAddrTable.setStatus('current')
hpicfVrrpAssoIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3, 1), )
vrrpAssoIpAddrEntry.registerAugmentions(("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpAddrEntry"))
hpicfVrrpAssoIpAddrEntry.setIndexNames(*vrrpAssoIpAddrEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfVrrpAssoIpAddrEntry.setStatus('current')
hpicfVrrpAssoIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3, 1, 1), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpAssoIpMask.setStatus('current')
hpicfVrrpTrackTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5), )
if mibBuilder.loadTexts: hpicfVrrpTrackTable.setStatus('current')
hpicfVrrpTrackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "HP-ICF-VRRP-MIB", "hpicfVrrpVrTrackType"), (0, "HP-ICF-VRRP-MIB", "hpicfVrrpVrTrackEntity"))
if mibBuilder.loadTexts: hpicfVrrpTrackEntry.setStatus('current')
hpicfVrrpVrTrackType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("port", 1), ("trunk", 2), ("vlan", 3))))
if mibBuilder.loadTexts: hpicfVrrpVrTrackType.setStatus('current')
hpicfVrrpVrTrackEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: hpicfVrrpVrTrackEntity.setStatus('current')
hpicfVrrpTrackRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpTrackRowStatus.setStatus('current')
hpicfVrrpTrackState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVrrpTrackState.setStatus('current')
hpicfVrrpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6), )
if mibBuilder.loadTexts: hpicfVrrpStatsTable.setStatus('current')
hpicfVrrpRespondToPing = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpRespondToPing.setStatus('deprecated')
hpicfVrrpRemoveConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpRemoveConfig.setStatus('deprecated')
hpicfVrrpNonstop = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpNonstop.setStatus('deprecated')
hpicfVrrpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6, 1), )
vrrpOperEntry.registerAugmentions(("HP-ICF-VRRP-MIB", "hpicfVrrpStatsEntry"))
hpicfVrrpStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfVrrpStatsEntry.setStatus('current')
hpicfVrrpStatsNearFailovers = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVrrpStatsNearFailovers.setStatus('current')
hpicfVrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1))
hpicfVrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2))
hpicfVrrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 1)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance = hpicfVrrpMIBCompliance.setStatus('deprecated')
hpicfVrrpMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 2)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance1 = hpicfVrrpMIBCompliance1.setStatus('deprecated')
hpicfVrrpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 3)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpVrPingGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance2 = hpicfVrrpMIBCompliance2.setStatus('current')
hpicfVrrpMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 4)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpNonstopGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpNonstopGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance3 = hpicfVrrpMIBCompliance3.setStatus('deprecated')
hpicfVrrpMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 5)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance4 = hpicfVrrpMIBCompliance4.setStatus('deprecated')
hpicfVrrpMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 6)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance5 = hpicfVrrpMIBCompliance5.setStatus('deprecated')
hpicfVrrpMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 7)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance6 = hpicfVrrpMIBCompliance6.setStatus('deprecated')
hpicfVrrpMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 8)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperationsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance7 = hpicfVrrpMIBCompliance7.setStatus('current')
hpicfVrrpMIBCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 9)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup2"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup2"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance8 = hpicfVrrpMIBCompliance8.setStatus('current')
hpicfVrrpOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 1)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpAdminStatus"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMode"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMasterPreempt"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrTransferControl"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPreemptDelayTime"), ("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperGroup = hpicfVrrpOperGroup.setStatus('deprecated')
hpicfVrrpTrackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 2)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpTrackRowStatus"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpTrackGroup = hpicfVrrpTrackGroup.setStatus('deprecated')
hpicfVrrpVrPingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 3)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpVrRespondToPing"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpVrPingGroup = hpicfVrrpVrPingGroup.setStatus('current')
hpicfVrrpNonstopGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 4)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpNonstop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpNonstopGroup = hpicfVrrpNonstopGroup.setStatus('deprecated')
hpicfVrrpOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 5)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpRespondToPing"), ("HP-ICF-VRRP-MIB", "hpicfVrrpRemoveConfig"), ("HP-ICF-VRRP-MIB", "hpicfVrrpStatsNearFailovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperationsGroup = hpicfVrrpOperationsGroup.setStatus('deprecated')
hpicfVrrpTrackGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 6)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpTrackRowStatus"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrControl"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpTrackGroup1 = hpicfVrrpTrackGroup1.setStatus('current')
hpicfVrrpOperGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 7)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpVrMode"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMasterPreempt"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrTransferControl"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPreemptDelayTime"), ("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperGroup1 = hpicfVrrpOperGroup1.setStatus('deprecated')
hpicfVrrpOperationsGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 8)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpStatsNearFailovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperationsGroup1 = hpicfVrrpOperationsGroup1.setStatus('current')
hpicfVrrpOperGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 9)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpVrMode"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMasterPreempt"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrTransferControl"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPreemptDelayTime"), ("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpMask"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMainPreempt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperGroup2 = hpicfVrrpOperGroup2.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-VRRP-MIB", hpicfVrrpMIBCompliance7=hpicfVrrpMIBCompliance7, hpicfVrrpNonstop=hpicfVrrpNonstop, hpicfVrrpVrMasterPreempt=hpicfVrrpVrMasterPreempt, hpicfVrrpTrackTable=hpicfVrrpTrackTable, hpicfVrrpMIBCompliance6=hpicfVrrpMIBCompliance6, hpicfVrrpTrackGroup1=hpicfVrrpTrackGroup1, hpicfVrrpMIBCompliance4=hpicfVrrpMIBCompliance4, hpicfVrrpAssoIpAddrTable=hpicfVrrpAssoIpAddrTable, hpicfVrrpStatsNearFailovers=hpicfVrrpStatsNearFailovers, hpicfVrrpVrTrackEntity=hpicfVrrpVrTrackEntity, hpicfVrrpTrackRowStatus=hpicfVrrpTrackRowStatus, hpicfVrrpMIBCompliance8=hpicfVrrpMIBCompliance8, hpicfVrrpOperTable=hpicfVrrpOperTable, hpicfVrrpVrTrackType=hpicfVrrpVrTrackType, hpicfVrrpStatsEntry=hpicfVrrpStatsEntry, hpicfVrrpMIB=hpicfVrrpMIB, hpicfVrrpMIBCompliance=hpicfVrrpMIBCompliance, hpicfVrrpMIBCompliances=hpicfVrrpMIBCompliances, hpicfVrrpTrackGroup=hpicfVrrpTrackGroup, hpicfVrrpMIBGroups=hpicfVrrpMIBGroups, hpicfVrrpOperations=hpicfVrrpOperations, hpicfVrrpMIBCompliance5=hpicfVrrpMIBCompliance5, hpicfVrrpRespondToPing=hpicfVrrpRespondToPing, hpicfVrrpNonstopGroup=hpicfVrrpNonstopGroup, hpicfVrrpOperationsGroup1=hpicfVrrpOperationsGroup1, hpicfVrrpTrackState=hpicfVrrpTrackState, hpicfVrrpVrTransferControl=hpicfVrrpVrTransferControl, hpicfVrrpVrMainPreempt=hpicfVrrpVrMainPreempt, hpicfVrrpOperEntry=hpicfVrrpOperEntry, PYSNMP_MODULE_ID=hpicfVrrpMIB, hpicfVrrpMIBCompliance1=hpicfVrrpMIBCompliance1, hpicfVrrpVrMode=hpicfVrrpVrMode, hpicfVrrpConformance=hpicfVrrpConformance, hpicfVrrpTrackEntry=hpicfVrrpTrackEntry, hpicfVrrpMIBCompliance3=hpicfVrrpMIBCompliance3, hpicfVrrpAdminStatus=hpicfVrrpAdminStatus, hpicfVrrpOperGroup2=hpicfVrrpOperGroup2, hpicfVrrpStatsTable=hpicfVrrpStatsTable, hpicfVrrpAssoIpAddrEntry=hpicfVrrpAssoIpAddrEntry, hpicfVrrpRemoveConfig=hpicfVrrpRemoveConfig, hpicfVrrpOperGroup1=hpicfVrrpOperGroup1, hpicfVrrpVrRespondToPing=hpicfVrrpVrRespondToPing, hpicfVrrpVrPingGroup=hpicfVrrpVrPingGroup, hpicfVrrpOperGroup=hpicfVrrpOperGroup, hpicfVrrpOperationsGroup=hpicfVrrpOperationsGroup, hpicfVrrpVrPreemptDelayTime=hpicfVrrpVrPreemptDelayTime, hpicfVrrpAssoIpMask=hpicfVrrpAssoIpMask, hpicfVrrpMIBCompliance2=hpicfVrrpMIBCompliance2, hpicfVrrpVrControl=hpicfVrrpVrControl)
