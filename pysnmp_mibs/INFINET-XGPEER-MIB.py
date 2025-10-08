#
# PySNMP MIB module INFINET-XGPEER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinet/INFINET-XGPEER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
xg, = mibBuilder.importSymbols("INFINET-XG-MIB", "xg")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
xgPeer = ModuleIdentity((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2))
xgPeer.setRevisions(('2015-10-08 08:35',))
if mibBuilder.loadTexts: xgPeer.setLastUpdated('201510080835Z')
if mibBuilder.loadTexts: xgPeer.setOrganization('Infinet Wireless Ltd.')
xgPeerSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgPeerSerialNumber.setStatus('current')
xgPeerSysName = MibScalar((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgPeerSysName.setStatus('current')
xgPeerIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 3), )
if mibBuilder.loadTexts: xgPeerIpAddrTable.setStatus('current')
xgPeerIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 3, 1), ).setIndexNames((0, "INFINET-XGPEER-MIB", "xgPeerIpAddress"))
if mibBuilder.loadTexts: xgPeerIpAddrEntry.setStatus('current')
xgPeerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgPeerIpAddress.setStatus('current')
xgPeerMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10))
xgPeerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 1))
xgPeerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 2))
xgPeerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 1, 1)).setObjects(("INFINET-XGPEER-MIB", "xgPeerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgPeerMIBCompliance = xgPeerMIBCompliance.setStatus('current')
xgPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 2, 1)).setObjects(("INFINET-XGPEER-MIB", "xgPeerSerialNumber"), ("INFINET-XGPEER-MIB", "xgPeerSysName"), ("INFINET-XGPEER-MIB", "xgPeerIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgPeerGroup = xgPeerGroup.setStatus('current')
mibBuilder.exportSymbols("INFINET-XGPEER-MIB", xgPeerIpAddrTable=xgPeerIpAddrTable, xgPeerIpAddress=xgPeerIpAddress, xgPeerIpAddrEntry=xgPeerIpAddrEntry, xgPeerMIBGroups=xgPeerMIBGroups, xgPeerMIBCompliances=xgPeerMIBCompliances, xgPeerSerialNumber=xgPeerSerialNumber, xgPeerGroup=xgPeerGroup, xgPeerMIBCompliance=xgPeerMIBCompliance, xgPeerSysName=xgPeerSysName, xgPeer=xgPeer, PYSNMP_MODULE_ID=xgPeer, xgPeerMIBConformance=xgPeerMIBConformance)
