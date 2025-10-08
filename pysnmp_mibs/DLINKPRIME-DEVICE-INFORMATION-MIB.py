#
# PySNMP MIB module DLINKPRIME-DEVICE-INFORMATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-DEVICE-INFORMATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("DLINKPRIME-DEVICE-INFORMATION-MIB", PYSNMP_MODULE_ID=dlinkPrimeDeviceInfoMIB, dpDeviceInfoIpV4Addr=dpDeviceInfoIpV4Addr, MacAddress=MacAddress, dpDeviceInfoDhcpRetry=dpDeviceInfoDhcpRetry, dpDeviceInfoMIBObjects=dpDeviceInfoMIBObjects, dlinkPrimeDeviceInfoMIB=dlinkPrimeDeviceInfoMIB, dpDeviceInfoFirmwareVersion=dpDeviceInfoFirmwareVersion, dpDeviceInfoIpV6GlobalState=dpDeviceInfoIpV6GlobalState, Ipv6Address=Ipv6Address, dpDeviceInfoIpV6AddressIpAddr=dpDeviceInfoIpV6AddressIpAddr, dpDeviceInfoSerialNumber=dpDeviceInfoSerialNumber, dpDeviceInfoIpV4SubnetMask=dpDeviceInfoIpV4SubnetMask, dpDeviceInfoSysConfiguration=dpDeviceInfoSysConfiguration, dpDeviceInfoBootPromVersion=dpDeviceInfoBootPromVersion, dpDeviceInfoIpV4AddrCfgMode=dpDeviceInfoIpV4AddrCfgMode, dpDeviceInfoHardwareVersion=dpDeviceInfoHardwareVersion, dpDeviceInfoMacAddr=dpDeviceInfoMacAddr, dpDeviceInfoGateway=dpDeviceInfoGateway)
