#
# PySNMP MIB module RUGGEDCOM-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-IP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ruggedcomMgmt, = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RUGGEDCOM-IP-MIB", PYSNMP_MODULE_ID=rcIp, rcIpConfigDefaultGateway=rcIpConfigDefaultGateway, rcIpConformance=rcIpConformance, rcIpConfigMgmtIpSubnet=rcIpConfigMgmtIpSubnet, rcIp=rcIp, rcIpGroups=rcIpGroups, rcIpObjectsGroupDflt=rcIpObjectsGroupDflt, rcIpConfigDfltMgmtIpSubnet=rcIpConfigDfltMgmtIpSubnet, rcIpObjectsGroup=rcIpObjectsGroup, rcIpConfigMgmtIpAddress=rcIpConfigMgmtIpAddress, rcIpConfigDfltMgmtIpAddress=rcIpConfigDfltMgmtIpAddress, rcIpConfig=rcIpConfig)
