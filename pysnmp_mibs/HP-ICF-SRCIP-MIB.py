#
# PySNMP MIB module HP-ICF-SRCIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-SRCIP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpicfCommon, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfCommon")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfSrcIpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13))
hpicfSrcIpMIB.setRevisions(('2020-06-20 00:00', '2016-08-29 00:00', '2011-07-21 00:00', '2009-04-30 00:00', '2008-10-10 00:00',))
if mibBuilder.loadTexts: hpicfSrcIpMIB.setLastUpdated('202006200000Z')
if mibBuilder.loadTexts: hpicfSrcIpMIB.setOrganization('HP Networking')
hpicfSrcIpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1))
hpicfSrcIpAddrPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1), )
if mibBuilder.loadTexts: hpicfSrcIpAddrPolicyTable.setStatus('current')
hpicfSrcIpAddrPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1), ).setIndexNames((0, "HP-ICF-SRCIP-MIB", "hpicfSrcIpAddressType"), (0, "HP-ICF-SRCIP-MIB", "hpicfSrcIpProtocolIndex"))
if mibBuilder.loadTexts: hpicfSrcIpAddrPolicyEntry.setStatus('current')
hpicfSrcIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfSrcIpAddressType.setStatus('current')
hpicfSrcIpProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("tacacs", 1), ("radius", 2), ("syslog", 3), ("telnet", 4), ("tftp", 5), ("sntp", 6), ("sflow", 7), ("tunnelednodeserver", 8), ("radsec", 9), ("central", 10))))
if mibBuilder.loadTexts: hpicfSrcIpProtocolIndex.setStatus('current')
hpicfSrcIpAddrPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("outgoingInterface", 1), ("configuredIpAddr", 2), ("configuredInterface", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSrcIpAddrPolicy.setStatus('current')
hpicfSrcIpAddrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSrcIpAddrIfIndex.setStatus('current')
hpicfSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 5), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSrcIpAddress.setStatus('current')
hpicfSrcIpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2))
hpicfSrcIpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 1))
hpicfSrcIpBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 1, 1)).setObjects(("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddrPolicy"), ("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddrIfIndex"), ("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSrcIpBaseGroup = hpicfSrcIpBaseGroup.setStatus('current')
hpicfSrcIpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 2))
hpicfSrcIpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 2, 1)).setObjects(("HP-ICF-SRCIP-MIB", "hpicfSrcIpBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSrcIpCompliance = hpicfSrcIpCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-SRCIP-MIB", hpicfSrcIpAddressType=hpicfSrcIpAddressType, hpicfSrcIpAddrIfIndex=hpicfSrcIpAddrIfIndex, hpicfSrcIpAddress=hpicfSrcIpAddress, hpicfSrcIpMIB=hpicfSrcIpMIB, hpicfSrcIpBaseGroup=hpicfSrcIpBaseGroup, PYSNMP_MODULE_ID=hpicfSrcIpMIB, hpicfSrcIpAddrPolicy=hpicfSrcIpAddrPolicy, hpicfSrcIpAddrPolicyEntry=hpicfSrcIpAddrPolicyEntry, hpicfSrcIpCompliances=hpicfSrcIpCompliances, hpicfSrcIpConformance=hpicfSrcIpConformance, hpicfSrcIpProtocolIndex=hpicfSrcIpProtocolIndex, hpicfSrcIpAddrPolicyTable=hpicfSrcIpAddrPolicyTable, hpicfSrcIpCompliance=hpicfSrcIpCompliance, hpicfSrcIpConfig=hpicfSrcIpConfig, hpicfSrcIpGroups=hpicfSrcIpGroups)
