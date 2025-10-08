#
# PySNMP MIB module TPT-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-HOST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_host_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12)).setLabel("tpt-host-objs")
tpt_host_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_host_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_host_objs.setOrganization('Trend Micro, Inc.')
class EnabledOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class ActiveOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inactive", 0), ("active", 1))

class IpAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("iptypeIPv4", 1), ("iptypeIPv6user", 2), ("iptypeIPv6local", 3), ("iptypeIPv6auto", 4))

class FipsMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("crypto", 1), ("full", 2))

class ActiveCert(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("temporary", 1), ("authorized", 2))

class InitState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("in-progress", 0), ("complete", 1))

hostIpTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1), )
if mibBuilder.loadTexts: hostIpTable.setStatus('current')
hostIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1), ).setIndexNames((0, "TPT-HOST-MIB", "hostIpIndex"))
if mibBuilder.loadTexts: hostIpEntry.setStatus('current')
hostIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hostIpIndex.setStatus('current')
hostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpAddress.setStatus('current')
hostIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 3), IpAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpType.setStatus('current')
hostIpActive = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 4), ActiveOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpActive.setStatus('current')
hostIPv4Gateway = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv4Gateway.setStatus('current')
hostIPv6Gateway = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6Gateway.setStatus('current')
hostIPv6Enabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 4), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6Enabled.setStatus('current')
hostIPv6AutoConfig = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 5), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6AutoConfig.setStatus('current')
hostFipsCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 6), FipsMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostFipsCfgMode.setStatus('current')
hostFipsMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 7), FipsMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostFipsMode.setStatus('current')
hostSSLCert = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 8), ActiveCert()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostSSLCert.setStatus('current')
hostInitState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 9), InitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInitState.setStatus('current')
mibBuilder.exportSymbols("TPT-HOST-MIB", ActiveOrNot=ActiveOrNot, InitState=InitState, hostIPv6Enabled=hostIPv6Enabled, hostFipsMode=hostFipsMode, hostIpEntry=hostIpEntry, hostIPv6AutoConfig=hostIPv6AutoConfig, hostIpType=hostIpType, hostIpIndex=hostIpIndex, hostIpTable=hostIpTable, hostIpAddress=hostIpAddress, hostInitState=hostInitState, ActiveCert=ActiveCert, hostFipsCfgMode=hostFipsCfgMode, PYSNMP_MODULE_ID=tpt_host_objs, hostSSLCert=hostSSLCert, hostIPv6Gateway=hostIPv6Gateway, hostIPv4Gateway=hostIPv4Gateway, IpAddressType=IpAddressType, tpt_host_objs=tpt_host_objs, FipsMode=FipsMode, EnabledOrNot=EnabledOrNot, hostIpActive=hostIpActive)
