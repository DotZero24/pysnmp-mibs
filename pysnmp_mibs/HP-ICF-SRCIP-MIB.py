#
# PySNMP MIB module HP-ICF-SRCIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-SRCIP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpicfCommon, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfCommon")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ICF-SRCIP-MIB", hpicfSrcIpConformance=hpicfSrcIpConformance, hpicfSrcIpGroups=hpicfSrcIpGroups, hpicfSrcIpAddrPolicyEntry=hpicfSrcIpAddrPolicyEntry, hpicfSrcIpProtocolIndex=hpicfSrcIpProtocolIndex, hpicfSrcIpAddrPolicy=hpicfSrcIpAddrPolicy, hpicfSrcIpAddrIfIndex=hpicfSrcIpAddrIfIndex, hpicfSrcIpCompliance=hpicfSrcIpCompliance, PYSNMP_MODULE_ID=hpicfSrcIpMIB, hpicfSrcIpCompliances=hpicfSrcIpCompliances, hpicfSrcIpAddressType=hpicfSrcIpAddressType, hpicfSrcIpAddress=hpicfSrcIpAddress, hpicfSrcIpMIB=hpicfSrcIpMIB, hpicfSrcIpAddrPolicyTable=hpicfSrcIpAddrPolicyTable, hpicfSrcIpBaseGroup=hpicfSrcIpBaseGroup, hpicfSrcIpConfig=hpicfSrcIpConfig)
