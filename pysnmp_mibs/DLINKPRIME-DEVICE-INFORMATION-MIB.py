#
# PySNMP MIB module DLINKPRIME-DEVICE-INFORMATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-DEVICE-INFORMATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
dlinkPrimeDeviceInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 3))
dlinkPrimeDeviceInfoMIB.setRevisions(('2014-05-30 00:00',))
if mibBuilder.loadTexts: dlinkPrimeDeviceInfoMIB.setLastUpdated('201405300000Z')
if mibBuilder.loadTexts: dlinkPrimeDeviceInfoMIB.setOrganization('D-Link Corp.')
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class Ipv6Address(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

dpDeviceInfoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 3, 1))
dpDeviceInfoSysConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1))
dpDeviceInfoIpV4AddrCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("dhcp", 2), ("bootp", 3))).clone('manual')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDeviceInfoIpV4AddrCfgMode.setStatus('current')
dpDeviceInfoIpV4Addr = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDeviceInfoIpV4Addr.setStatus('current')
dpDeviceInfoIpV4SubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDeviceInfoIpV4SubnetMask.setStatus('current')
dpDeviceInfoGateway = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDeviceInfoGateway.setStatus('current')
dpDeviceInfoDhcpRetry = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 128)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDeviceInfoDhcpRetry.setStatus('current')
dpDeviceInfoIpV6GlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDeviceInfoIpV6GlobalState.setStatus('current')
dpDeviceInfoIpV6AddressIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 1, 7), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDeviceInfoIpV6AddressIpAddr.setStatus('current')
dpDeviceInfoMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpDeviceInfoMacAddr.setStatus('current')
dpDeviceInfoBootPromVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpDeviceInfoBootPromVersion.setStatus('current')
dpDeviceInfoFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpDeviceInfoFirmwareVersion.setStatus('current')
dpDeviceInfoHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpDeviceInfoHardwareVersion.setStatus('current')
dpDeviceInfoSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpDeviceInfoSerialNumber.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-DEVICE-INFORMATION-MIB", dpDeviceInfoIpV6GlobalState=dpDeviceInfoIpV6GlobalState, dpDeviceInfoFirmwareVersion=dpDeviceInfoFirmwareVersion, dpDeviceInfoIpV4Addr=dpDeviceInfoIpV4Addr, dpDeviceInfoHardwareVersion=dpDeviceInfoHardwareVersion, Ipv6Address=Ipv6Address, dpDeviceInfoIpV6AddressIpAddr=dpDeviceInfoIpV6AddressIpAddr, dpDeviceInfoMacAddr=dpDeviceInfoMacAddr, PYSNMP_MODULE_ID=dlinkPrimeDeviceInfoMIB, dpDeviceInfoDhcpRetry=dpDeviceInfoDhcpRetry, dpDeviceInfoIpV4SubnetMask=dpDeviceInfoIpV4SubnetMask, dpDeviceInfoBootPromVersion=dpDeviceInfoBootPromVersion, dpDeviceInfoSerialNumber=dpDeviceInfoSerialNumber, MacAddress=MacAddress, dpDeviceInfoMIBObjects=dpDeviceInfoMIBObjects, dlinkPrimeDeviceInfoMIB=dlinkPrimeDeviceInfoMIB, dpDeviceInfoSysConfiguration=dpDeviceInfoSysConfiguration, dpDeviceInfoGateway=dpDeviceInfoGateway, dpDeviceInfoIpV4AddrCfgMode=dpDeviceInfoIpV4AddrCfgMode)
