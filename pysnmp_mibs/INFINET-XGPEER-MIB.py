#
# PySNMP MIB module INFINET-XGPEER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinet/INFINET-XGPEER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
xg, = mibBuilder.importSymbols("INFINET-XG-MIB", "xg")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINET-XGPEER-MIB", xgPeerSysName=xgPeerSysName, xgPeerIpAddrEntry=xgPeerIpAddrEntry, xgPeerMIBConformance=xgPeerMIBConformance, xgPeerMIBCompliances=xgPeerMIBCompliances, PYSNMP_MODULE_ID=xgPeer, xgPeerSerialNumber=xgPeerSerialNumber, xgPeerMIBCompliance=xgPeerMIBCompliance, xgPeerIpAddrTable=xgPeerIpAddrTable, xgPeerIpAddress=xgPeerIpAddress, xgPeer=xgPeer, xgPeerGroup=xgPeerGroup, xgPeerMIBGroups=xgPeerMIBGroups)
