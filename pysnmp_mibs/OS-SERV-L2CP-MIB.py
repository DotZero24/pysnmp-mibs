#
# PySNMP MIB module OS-SERV-L2CP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-SERV-L2CP-MIB
# Produced by pysmi-1.1.12 at Mon Aug  4 17:02:28 2025
# On host macmini.vegmond.io platform Darwin version 24.5.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
oaOptiSwitch, ServiceType = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch", "ServiceType")
osEthServId, = mibBuilder.importSymbols("OS-ETH-SERV-MIB", "osEthServId")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Integer32, Gauge32, ModuleIdentity, TimeTicks, NotificationType, Counter32, Bits, IpAddress, iso, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "TimeTicks", "NotificationType", "Counter32", "Bits", "IpAddress", "iso", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
osServL2Cp = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 15))
osServL2Cp.setRevisions(('2009-01-09 00:00',))
if mibBuilder.loadTexts: osServL2Cp.setLastUpdated('200901090000Z')
if mibBuilder.loadTexts: osServL2Cp.setOrganization('MRV Communications, Inc.')
osServL2CpGen = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 15, 1))
osServL2CpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 15, 100))
osServL2CpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 15, 100, 1))
osServL2CpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 15, 100, 2))
class L2CpProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("unknown", 1), ("stp", 2), ("vtp", 3), ("cdp", 4), ("pvst", 5), ("lacp", 6), ("dot1x", 7), ("udld", 8), ("efm", 9), ("esmc", 10), ("dtp", 11), ("ethoam", 12), ("pagp", 13), ("erp", 14), ("lamp", 15), ("elmi", 16), ("lldp", 17), ("garp", 18))

osServL2CpL2TpMac = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 15, 1, 2), MacAddress().clone(hexValue="01000CCDCDD0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osServL2CpL2TpMac.setStatus('current')
osServL2CpOptTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 15, 3), )
if mibBuilder.loadTexts: osServL2CpOptTable.setStatus('current')
osServL2CpOptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 15, 3, 1), ).setIndexNames((0, "OS-SERV-L2CP-MIB", "osServL2CpOptSrvType"), (0, "OS-SERV-L2CP-MIB", "osServL2CpOptProtocol"))
if mibBuilder.loadTexts: osServL2CpOptEntry.setStatus('current')
osServL2CpOptSrvType = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 15, 3, 1, 1), ServiceType())
if mibBuilder.loadTexts: osServL2CpOptSrvType.setStatus('current')
osServL2CpOptProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 15, 3, 1, 2), L2CpProtocol())
if mibBuilder.loadTexts: osServL2CpOptProtocol.setStatus('current')
osServL2CpOptSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 15, 3, 1, 3), Bits().clone(namedValues=NamedValues(("discard", 0), ("peer", 1), ("tunnelTransparent", 2), ("tunnelL2Tp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osServL2CpOptSupported.setStatus('current')
osServL2CpSrvTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 15, 4), )
if mibBuilder.loadTexts: osServL2CpSrvTable.setStatus('current')
osServL2CpSrvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 15, 4, 1), ).setIndexNames((0, "OS-ETH-SERV-MIB", "osEthServId"), (0, "OS-SERV-L2CP-MIB", "osServL2CpOptProtocol"))
if mibBuilder.loadTexts: osServL2CpSrvEntry.setStatus('current')
osServL2CpSrvOption = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 15, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("transparent", 2), ("discard", 3), ("peer", 4), ("tunnelL2Tp", 5))).clone('transparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osServL2CpSrvOption.setStatus('current')
osServL2CpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 15, 100, 1, 1)).setObjects(("OS-SERV-L2CP-MIB", "osServL2CpMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osServL2CpMIBCompliance = osServL2CpMIBCompliance.setStatus('current')
osServL2CpMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 15, 100, 2, 1)).setObjects(("OS-SERV-L2CP-MIB", "osServL2CpL2TpMac"), ("OS-SERV-L2CP-MIB", "osServL2CpOptSupported"), ("OS-SERV-L2CP-MIB", "osServL2CpSrvOption"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osServL2CpMandatoryGroup = osServL2CpMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OS-SERV-L2CP-MIB", osServL2CpOptSrvType=osServL2CpOptSrvType, osServL2CpConformance=osServL2CpConformance, osServL2CpSrvOption=osServL2CpSrvOption, osServL2CpOptProtocol=osServL2CpOptProtocol, osServL2CpSrvEntry=osServL2CpSrvEntry, L2CpProtocol=L2CpProtocol, osServL2CpMandatoryGroup=osServL2CpMandatoryGroup, osServL2CpL2TpMac=osServL2CpL2TpMac, osServL2CpOptEntry=osServL2CpOptEntry, osServL2CpGen=osServL2CpGen, osServL2CpOptSupported=osServL2CpOptSupported, osServL2CpMIBCompliances=osServL2CpMIBCompliances, PYSNMP_MODULE_ID=osServL2Cp, osServL2CpOptTable=osServL2CpOptTable, osServL2CpSrvTable=osServL2CpSrvTable, osServL2CpMIBCompliance=osServL2CpMIBCompliance, osServL2Cp=osServL2Cp, osServL2CpMIBGroups=osServL2CpMIBGroups)
