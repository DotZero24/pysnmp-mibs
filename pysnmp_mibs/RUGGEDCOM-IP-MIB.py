#
# PySNMP MIB module RUGGEDCOM-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-IP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ruggedcomMgmt, = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rcIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 3))
rcIp.setRevisions(('2013-12-11 10:00', '2008-11-11 10:00',))
if mibBuilder.loadTexts: rcIp.setLastUpdated('201312111000Z')
if mibBuilder.loadTexts: rcIp.setOrganization('RuggedCom')
rcIpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 3, 5))
rcIpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 3, 5, 1))
rcIpConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 3, 1))
if mibBuilder.loadTexts: rcIpConfig.setStatus('current')
rcIpConfigMgmtIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIpConfigMgmtIpAddress.setStatus('current')
rcIpConfigMgmtIpSubnet = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIpConfigMgmtIpSubnet.setStatus('current')
rcIpConfigDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIpConfigDefaultGateway.setStatus('current')
rcIpConfigDfltMgmtIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIpConfigDfltMgmtIpAddress.setStatus('current')
rcIpConfigDfltMgmtIpSubnet = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIpConfigDfltMgmtIpSubnet.setStatus('current')
rcIpObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 3, 5, 1, 1)).setObjects(("RUGGEDCOM-IP-MIB", "rcIpConfigMgmtIpAddress"), ("RUGGEDCOM-IP-MIB", "rcIpConfigMgmtIpSubnet"), ("RUGGEDCOM-IP-MIB", "rcIpConfigDefaultGateway"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIpObjectsGroup = rcIpObjectsGroup.setStatus('current')
rcIpObjectsGroupDflt = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 3, 5, 1, 2)).setObjects(("RUGGEDCOM-IP-MIB", "rcIpConfigDfltMgmtIpAddress"), ("RUGGEDCOM-IP-MIB", "rcIpConfigDfltMgmtIpSubnet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcIpObjectsGroupDflt = rcIpObjectsGroupDflt.setStatus('current')
mibBuilder.exportSymbols("RUGGEDCOM-IP-MIB", rcIpConfigMgmtIpSubnet=rcIpConfigMgmtIpSubnet, rcIpConfigMgmtIpAddress=rcIpConfigMgmtIpAddress, rcIp=rcIp, rcIpConformance=rcIpConformance, rcIpConfig=rcIpConfig, rcIpConfigDefaultGateway=rcIpConfigDefaultGateway, PYSNMP_MODULE_ID=rcIp, rcIpObjectsGroup=rcIpObjectsGroup, rcIpGroups=rcIpGroups, rcIpConfigDfltMgmtIpSubnet=rcIpConfigDfltMgmtIpSubnet, rcIpConfigDfltMgmtIpAddress=rcIpConfigDfltMgmtIpAddress, rcIpObjectsGroupDflt=rcIpObjectsGroupDflt)
