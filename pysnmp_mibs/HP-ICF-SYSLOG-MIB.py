#
# PySNMP MIB module HP-ICF-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-SYSLOG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpicfSyslog, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfSyslog")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
hpicfSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1))
hpicfSyslogMIB.setRevisions(('2019-01-08 00:00', '2018-07-10 00:00', '2018-08-22 00:00', '2018-02-14 00:00', '2017-12-11 00:00', '2017-10-17 00:00', '2017-10-12 00:00', '2017-09-05 00:00', '2017-07-03 00:00', '2016-07-13 00:00', '2016-06-14 00:00', '2016-05-12 00:00', '2016-04-01 00:00', '2016-03-23 00:00', '2016-03-10 00:00', '2016-01-21 05:26', '2015-09-11 05:26', '2015-09-04 00:00', '2015-09-03 00:00', '2015-08-31 00:00', '2015-08-28 00:00', '2015-08-07 00:00', '2015-05-20 00:00', '2015-05-09 00:00', '2015-05-09 00:00', '2015-05-08 00:00', '2015-04-16 00:00', '2014-11-13 00:00', '2014-07-17 00:00', '2013-11-06 00:00', '2013-09-24 00:00', '2013-09-14 00:00', '2013-09-05 00:00', '2013-06-25 00:00', '2013-08-07 00:00', '2012-03-15 00:00', '2012-01-30 00:00', '2011-10-11 00:00', '2011-08-24 00:00', '2011-07-19 00:00', '2011-06-13 00:00', '2011-05-27 00:00', '2011-03-21 00:00', '2011-03-05 00:00', '2010-11-09 00:00', '2010-10-25 00:00', '2010-08-11 00:00', '2010-06-20 00:00', '2010-03-20 00:00', '2010-03-12 00:00', '2010-01-27 00:00', '2009-08-19 00:00', '2009-02-18 00:00', '2009-01-30 00:00', '2008-11-18 00:00', '2008-07-09 00:00', '2008-06-26 00:00', '2008-06-25 00:00', '2008-01-25 00:00', '2008-01-01 11:21',))
if mibBuilder.loadTexts: hpicfSyslogMIB.setLastUpdated('201807100000Z')
if mibBuilder.loadTexts: hpicfSyslogMIB.setOrganization('HPE Networking')
class HpicfSyslogFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kern", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("sys9", 9), ("sys10", 10), ("sys11", 11), ("sys12", 12), ("sys13", 13), ("sys14", 14), ("cron", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class HpicfSyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("major", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

class HpicfSyslogSystemModule(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149))
    namedValues = NamedValues(("all-pass", 0), ("vlan", 1), ("ip", 2), ("igmp", 3), ("ipx", 4), ("stp", 5), ("system", 6), ("chassis", 7), ("console", 8), ("ports", 9), ("dhcp", 10), ("download", 11), ("tcp", 12), ("telnet", 13), ("timep", 14), ("tftp", 15), ("xmodem", 16), ("update", 17), ("mgr", 18), ("bridge", 19), ("snmp", 20), ("addrmgr", 21), ("agp", 22), ("fault", 23), ("ldbal", 24), ("garp", 25), ("gvrp", 26), ("cos", 27), ("lacp", 28), ("dhcpr", 29), ("stack", 30), ("dma", 31), ("sntp", 32), ("ieee8021x", 33), ("cdp", 34), ("auth", 35), ("tacacs", 36), ("radius", 37), ("ssh", 38), ("netinet", 39), ("ospf", 40), ("xrrp", 41), ("ssl", 42), ("ipaddrmgr", 43), ("macauth", 44), ("kms", 45), ("pim", 46), ("maclock", 47), ("acl", 48), ("udpf", 49), ("inst-mon", 50), ("udld", 51), ("hpesp", 52), ("lldp", 53), ("connfilt", 54), ("ratelim", 55), ("idm", 56), ("iplock", 57), ("dhcp-snoop", 58), ("vrrp", 59), ("usb", 60), ("licensing", 61), ("loop-protect", 62), ("sflow", 63), ("arp-protect", 64), ("dhcpv6c", 65), ("mtm", 66), ("mld", 67), ("dca", 68), ("qinq", 69), ("autorun", 70), ("ffi", 71), ("wsm", 72), ("dipld", 73), ("hpsm", 74), ("srcip", 75), ("policy", 76), ("oobm", 77), ("trmode", 78), ("ospf3", 79), ("dhcpv6r", 80), ("bgp", 81), ("ufd", 82), ("fips", 83), ("dt", 84), ("dcbx", 85), ("sftp", 86), ("stacking", 87), ("rfs", 88), ("testmode", 89), ("crypto", 90), ("slp", 91), ("ra-guard", 92), ("ecm", 93), ("hpespip", 94), ("mobility-agent", 95), ("securemode", 96), ("mSatProxy", 97), ("eSatProxy", 98), ("hpespcm", 99), ("openflow", 100), ("smart-link", 101), ("insysprog", 102), ("dhcp-server", 103), ("job", 104), ("dsnoopv6", 105), ("dipldv6", 106), ("servicetunnel", 107), ("tr069", 108), ("http", 109), ("vxlantunnel", 110), ("bpdu", 111), ("byod-redirect", 112), ("dldp", 113), ("macsec", 114), ("acct", 115), ("tls", 116), ("ripng", 117), ("arpthrottle", 120), ("ndsnoop", 122), ("ntp", 123), ("ipsla", 124), ("psDetect", 125), ("mdns", 126), ("mvrp", 127), ("rip", 128), ("bfd", 129), ("lldpmad", 130), ("captive-portal", 131), ("profile-manager", 132), ("vsf", 133), ("tunneledNode", 134), ("amp-server", 135), ("activate", 136), ("central", 137), ("ztpIpsec", 138), ("greTunnel", 139), ("userTnode", 140), ("vlanMad", 141), ("cfgRestore", 143), ("devOnboard", 144), ("httpProxy", 145), ("dfp", 146), ("authOrder", 147), ("caDownload", 148), ("estc", 149))

class HpicfSyslogOriginId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ip-address", 1), ("hostname", 2), ("none", 3))

hpicfSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 0))
hpicfSyslogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1))
hpicfSyslogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3))
hpicfSyslogControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfSyslogControlTable.setStatus('current')
hpicfSyslogControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogControlIndex"))
if mibBuilder.loadTexts: hpicfSyslogControlEntry.setStatus('current')
hpicfSyslogControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpicfSyslogControlIndex.setStatus('current')
hpicfSyslogControlDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSyslogControlDescr.setStatus('current')
hpicfSyslogControlBindAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSyslogControlBindAddrType.setStatus('current')
hpicfSyslogControlBindAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSyslogControlBindAddr.setStatus('current')
hpicfSyslogControlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSyslogControlRowStatus.setStatus('current')
hpicfSyslogControlBindAddrIsOobm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSyslogControlBindAddrIsOobm.setStatus('current')
hpicfSyslogControlSmmLog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSyslogControlSmmLog.setStatus('current')
hpicfSyslogControlTransportProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("udp", 1), ("tcp", 2), ("tls", 3))).clone('udp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogControlTransportProtocol.setStatus('current')
hpicfSyslogControlDestinationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 9), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogControlDestinationPort.setStatus('current')
hpicfSyslogControlFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogControlFilterName.setStatus('current')
hpicfSyslogOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2))
hpicfSyslogOperationsMsgsTransmitted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsMsgsTransmitted.setStatus('current')
hpicfSyslogOperationsMsgsDropped = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsMsgsDropped.setStatus('current')
hpicfSyslogOperationsLastMsgTransmittedTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsLastMsgTransmittedTime.setStatus('current')
hpicfSyslogOperationsStartTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsStartTime.setStatus('current')
hpicfSyslogOperationsLastError = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsLastError.setStatus('current')
hpicfSyslogOperationsLastErrorTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsLastErrorTime.setStatus('current')
hpicfSyslogOperationsCounterDiscontinuityTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsCounterDiscontinuityTime.setStatus('current')
hpicfSyslogOperationsStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("started", 2), ("suspended", 3), ("stopped", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogOperationsStatus.setStatus('current')
hpicfSyslogPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3))
hpicfSyslogPriorityFacility = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 1), HpicfSyslogFacility().clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogPriorityFacility.setStatus('current')
hpicfSyslogPrioritySeverity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 2), HpicfSyslogSeverity().clone('debug')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogPrioritySeverity.setStatus('current')
hpicfSyslogPriorityDescr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogPriorityDescr.setStatus('current')
hpicfSyslogSystemModule = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 4), HpicfSyslogSystemModule().clone('all-pass')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogSystemModule.setStatus('current')
hpicfSyslogOriginId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 5), HpicfSyslogOriginId().clone('ip-address')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogOriginId.setStatus('current')
hpicfSyslogPrefixString = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogPrefixString.setStatus('current')
hpicfSyslogStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4))
hpicfSyslogGeneralStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1))
hpicfSyslogGeneralLogSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogGeneralLogSent.setStatus('current')
hpicfSyslogGeneralLogRecv = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogGeneralLogRecv.setStatus('current')
hpicfSyslogGeneralLogRelay = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogGeneralLogRelay.setStatus('current')
hpicfSyslogGeneralSendError = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogGeneralSendError.setStatus('current')
hpicfSyslogGeneralLogResend = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogGeneralLogResend.setStatus('current')
hpicfSyslogGeneralResendError = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogGeneralResendError.setStatus('current')
hpicfSyslogGeneralLogBuffered = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogGeneralLogBuffered.setStatus('current')
hpicfSyslogSeverityStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2))
hpicfSyslogSeverityCounterInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1), )
if mibBuilder.loadTexts: hpicfSyslogSeverityCounterInfoTable.setStatus('current')
hpicfSyslogSeverityCounterInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1), ).setIndexNames((0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogSeverityTypeIndex"))
if mibBuilder.loadTexts: hpicfSyslogSeverityCounterInfoEntry.setStatus('current')
hpicfSyslogSeverityTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpicfSyslogSeverityTypeIndex.setStatus('current')
hpicfSyslogSeverityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1, 2), HpicfSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogSeverityType.setStatus('current')
hpicfSyslogSeverityCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogSeverityCounter.setStatus('current')
hpicfSyslogFacilityStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3))
hpicfSyslogFacilityCounterInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1), )
if mibBuilder.loadTexts: hpicfSyslogFacilityCounterInfoTable.setStatus('current')
hpicfSyslogFacilityCounterInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1), ).setIndexNames((0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogfacilityCounterIndex"))
if mibBuilder.loadTexts: hpicfSyslogFacilityCounterInfoEntry.setStatus('current')
hpicfSyslogfacilityCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpicfSyslogfacilityCounterIndex.setStatus('current')
hpicfSyslogfacilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1, 2), HpicfSyslogFacility()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogfacilityType.setStatus('current')
hpicfSyslogfacilityCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 4, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogfacilityCounter.setStatus('current')
hpicfSyslogLogMsgOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 5))
hpicfSyslogClearLog = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogClearLog.setStatus('current')
hpicfSyslogSecClearLog = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 5, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogSecClearLog.setStatus('current')
hpicfSyslogCmdClearLog = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 5, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogCmdClearLog.setStatus('current')
hpicfSyslogServerStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6), )
if mibBuilder.loadTexts: hpicfSyslogServerStatisticsTable.setStatus('current')
hpicfSyslogServerStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1), ).setIndexNames((0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogControlIndex"))
if mibBuilder.loadTexts: hpicfSyslogServerStatisticsEntry.setStatus('current')
hpicfSyslogServerLogSent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogServerLogSent.setStatus('current')
hpicfSyslogServerLogRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogServerLogRecv.setStatus('current')
hpicfSyslogServerLogRelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogServerLogRelay.setStatus('current')
hpicfSyslogServerSendError = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogServerSendError.setStatus('current')
hpicfSyslogServerLogResend = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogServerLogResend.setStatus('current')
hpicfSyslogServerResendError = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogServerResendError.setStatus('current')
hpicfSyslogServerLogBuffered = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSyslogServerLogBuffered.setStatus('current')
hpicfSyslogAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7))
hpicfSyslogAlertsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1), )
if mibBuilder.loadTexts: hpicfSyslogAlertsTable.setStatus('current')
hpicfSyslogAlertsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1), ).setIndexNames((0, "HP-ICF-SYSLOG-MIB", "hpicfSyslogAlertIndex"))
if mibBuilder.loadTexts: hpicfSyslogAlertsEntry.setStatus('current')
hpicfSyslogAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("runningCfgChg", 1))))
if mibBuilder.loadTexts: hpicfSyslogAlertIndex.setStatus('current')
hpicfSyslogAlertAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogAlertAdminStatus.setStatus('current')
hpicfSyslogAlertTransmitInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 7, 1, 1, 3), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogAlertTransmitInterval.setStatus('current')
hpicfSyslogLogging = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 8))
hpicfSyslogCommandLogging = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 1, 8, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSyslogCommandLogging.setStatus('current')
hpicfSyslogStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 0, 1)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlIndex"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlDescr"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddrType"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlRowStatus"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityDescr"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPrioritySeverity"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityFacility"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSystemModule"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsStatus"))
if mibBuilder.loadTexts: hpicfSyslogStatusChanged.setStatus('current')
hpicfSyslogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1))
hpicfSyslogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2))
hpicfSyslogOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 1)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsMsgsTransmitted"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsMsgsDropped"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsLastMsgTransmittedTime"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsStartTime"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsLastError"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsLastErrorTime"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsCounterDiscontinuityTime"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogOperationsGroup = hpicfSyslogOperationsGroup.setStatus('current')
hpicfSyslogControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 2)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlDescr"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddrType"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogControlGroup = hpicfSyslogControlGroup.setStatus('current')
hpicfSyslogPriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 3)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogPriorityGroup = hpicfSyslogPriorityGroup.setStatus('current')
hpicfSyslogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 5)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogStatusChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogNotificationGroup = hpicfSyslogNotificationGroup.setStatus('current')
hpicfSyslogControlGroupOobm = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 6)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddrIsOobm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogControlGroupOobm = hpicfSyslogControlGroupOobm.setStatus('current')
hpicfSyslogGeneralStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 7)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogSent"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogRecv"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogRelay"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralSendError"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogResend"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralResendError"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralLogBuffered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogGeneralStatisticsGroup = hpicfSyslogGeneralStatisticsGroup.setStatus('current')
hpicfSyslogSeverityStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 8)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogSeverityType"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSeverityCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogSeverityStatisticsGroup = hpicfSyslogSeverityStatisticsGroup.setStatus('current')
hpicfSyslogFacilityStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 9)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogfacilityType"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogfacilityCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogFacilityStatisticsGroup = hpicfSyslogFacilityStatisticsGroup.setStatus('current')
hpicfSyslogControlGroupSmm = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 10)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlBindAddr"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlSmmLog"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogControlGroupSmm = hpicfSyslogControlGroupSmm.setStatus('current')
hpicfSyslogLogMsgOptionsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 11)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogClearLog"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogLogMsgOptionsGroup = hpicfSyslogLogMsgOptionsGroup.setStatus('deprecated')
hpicfSyslogControlTransportGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 12)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlTransportProtocol"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlDestinationPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogControlTransportGroup = hpicfSyslogControlTransportGroup.setStatus('current')
hpicfSyslogServerStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 13)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogSent"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogRecv"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogRelay"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerSendError"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogResend"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerResendError"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerLogBuffered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogServerStatisticsGroup = hpicfSyslogServerStatisticsGroup.setStatus('current')
hpicfSyslogPriorityGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 14)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityFacility"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPrioritySeverity"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSystemModule"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogPriorityGroup1 = hpicfSyslogPriorityGroup1.setStatus('current')
hpicfSyslogAlertsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 15)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogAlertAdminStatus"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogAlertTransmitInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogAlertsGroup = hpicfSyslogAlertsGroup.setStatus('current')
hpicfSyslogOriginIdGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 16)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogOriginId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogOriginIdGroup1 = hpicfSyslogOriginIdGroup1.setStatus('current')
hpicfSyslogLogMsgOptionsGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 17)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogClearLog"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSecClearLog"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogLogMsgOptionsGroup1 = hpicfSyslogLogMsgOptionsGroup1.setStatus('deprecated')
hpicfSyslogCommandLoggingGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 18)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogCommandLogging"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogCommandLoggingGroup1 = hpicfSyslogCommandLoggingGroup1.setStatus('deprecated')
hpicfSyslogLogMsgOptionsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 19)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogClearLog"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSecClearLog"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogCmdClearLog"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogLogMsgOptionsGroup2 = hpicfSyslogLogMsgOptionsGroup2.setStatus('current')
hpicfSyslogControlFilterNameGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 20)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlFilterName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogControlFilterNameGroup = hpicfSyslogControlFilterNameGroup.setStatus('current')
hpicfSyslogPrefixStringGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 1, 23)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogPrefixString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogPrefixStringGroup1 = hpicfSyslogPrefixStringGroup1.setStatus('current')
hpicfSyslogFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 1)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogNotificationGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogFullCompliance1 = hpicfSyslogFullCompliance1.setStatus('current')
hpicfSyslogFullCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 2)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogFullCompliance2 = hpicfSyslogFullCompliance2.setStatus('current')
hpicfSyslogReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 4)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogNotificationGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogReadOnlyCompliance1 = hpicfSyslogReadOnlyCompliance1.setStatus('current')
hpicfSyslogReadOnlyCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 5)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogOperationsGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogReadOnlyCompliance2 = hpicfSyslogReadOnlyCompliance2.setStatus('current')
hpicfSyslogNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 7)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogNotificationCompliance = hpicfSyslogNotificationCompliance.setStatus('current')
hpicfSyslogFullComplianceOobm = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 8)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroupOobm"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogFullComplianceOobm = hpicfSyslogFullComplianceOobm.setStatus('current')
hpicfSyslogStatisticsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 9)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogGeneralStatisticsGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogSeverityStatisticsGroup"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogFacilityStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogStatisticsCompliance = hpicfSyslogStatisticsCompliance.setStatus('current')
hpicfSyslogSmmLogMsgCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 10)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroupSmm"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogLogMsgOptionsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogSmmLogMsgCompliance = hpicfSyslogSmmLogMsgCompliance.setStatus('deprecated')
hpicfSyslogTransportCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 11)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlTransportGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogTransportCompliance = hpicfSyslogTransportCompliance.setStatus('current')
hpicfSyslogPriorityCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 12)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogPriorityGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogPriorityCompliance = hpicfSyslogPriorityCompliance.setStatus('current')
hpicfSyslogServerStatisticsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 13)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogServerStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogServerStatisticsCompliance = hpicfSyslogServerStatisticsCompliance.setStatus('current')
hpicfSyslogAlertsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 14)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogAlertsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogAlertsCompliance = hpicfSyslogAlertsCompliance.setStatus('current')
hpicfSyslogOriginIdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 15)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogOriginIdGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogOriginIdCompliance = hpicfSyslogOriginIdCompliance.setStatus('current')
hpicfSyslogSmmLogMsgCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 16)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroupSmm"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogLogMsgOptionsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogSmmLogMsgCompliance1 = hpicfSyslogSmmLogMsgCompliance1.setStatus('deprecated')
hpicfSyslogCommandLoggingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 17)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogCommandLoggingGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogCommandLoggingCompliance = hpicfSyslogCommandLoggingCompliance.setStatus('deprecated')
hpicfSyslogSmmLogMsgCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 18)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlGroupSmm"), ("HP-ICF-SYSLOG-MIB", "hpicfSyslogLogMsgOptionsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogSmmLogMsgCompliance2 = hpicfSyslogSmmLogMsgCompliance2.setStatus('current')
hpicfSyslogTransportFilterNameCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 19)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogControlFilterNameGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogTransportFilterNameCompliance = hpicfSyslogTransportFilterNameCompliance.setStatus('current')
hpicfSyslogPrefixStringCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 14, 1, 3, 2, 22)).setObjects(("HP-ICF-SYSLOG-MIB", "hpicfSyslogPrefixStringGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSyslogPrefixStringCompliance = hpicfSyslogPrefixStringCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-SYSLOG-MIB", hpicfSyslogStatistics=hpicfSyslogStatistics, hpicfSyslogSeverityCounter=hpicfSyslogSeverityCounter, hpicfSyslogConformance=hpicfSyslogConformance, hpicfSyslogClearLog=hpicfSyslogClearLog, hpicfSyslogCmdClearLog=hpicfSyslogCmdClearLog, hpicfSyslogAlertTransmitInterval=hpicfSyslogAlertTransmitInterval, hpicfSyslogGeneralLogRecv=hpicfSyslogGeneralLogRecv, hpicfSyslogTransportCompliance=hpicfSyslogTransportCompliance, hpicfSyslogReadOnlyCompliance2=hpicfSyslogReadOnlyCompliance2, hpicfSyslogFullComplianceOobm=hpicfSyslogFullComplianceOobm, hpicfSyslogSecClearLog=hpicfSyslogSecClearLog, hpicfSyslogSmmLogMsgCompliance=hpicfSyslogSmmLogMsgCompliance, hpicfSyslogServerStatisticsTable=hpicfSyslogServerStatisticsTable, hpicfSyslogControlIndex=hpicfSyslogControlIndex, hpicfSyslogPrefixStringGroup1=hpicfSyslogPrefixStringGroup1, PYSNMP_MODULE_ID=hpicfSyslogMIB, hpicfSyslogControlSmmLog=hpicfSyslogControlSmmLog, hpicfSyslogOriginId=hpicfSyslogOriginId, hpicfSyslogSeverityTypeIndex=hpicfSyslogSeverityTypeIndex, hpicfSyslogOperationsStartTime=hpicfSyslogOperationsStartTime, hpicfSyslogControlGroup=hpicfSyslogControlGroup, hpicfSyslogPriorityGroup=hpicfSyslogPriorityGroup, hpicfSyslogServerStatisticsGroup=hpicfSyslogServerStatisticsGroup, hpicfSyslogNotifications=hpicfSyslogNotifications, hpicfSyslogOperationsLastMsgTransmittedTime=hpicfSyslogOperationsLastMsgTransmittedTime, HpicfSyslogFacility=HpicfSyslogFacility, hpicfSyslogPriorityGroup1=hpicfSyslogPriorityGroup1, hpicfSyslogPrefixStringCompliance=hpicfSyslogPrefixStringCompliance, hpicfSyslogServerLogBuffered=hpicfSyslogServerLogBuffered, hpicfSyslogSeverityStatistics=hpicfSyslogSeverityStatistics, hpicfSyslogStatusChanged=hpicfSyslogStatusChanged, hpicfSyslogCommandLoggingGroup1=hpicfSyslogCommandLoggingGroup1, hpicfSyslogControlGroupSmm=hpicfSyslogControlGroupSmm, hpicfSyslogPrioritySeverity=hpicfSyslogPrioritySeverity, hpicfSyslogCommandLogging=hpicfSyslogCommandLogging, hpicfSyslogNotificationGroup=hpicfSyslogNotificationGroup, hpicfSyslogGeneralLogSent=hpicfSyslogGeneralLogSent, hpicfSyslogServerLogResend=hpicfSyslogServerLogResend, hpicfSyslogControlBindAddrIsOobm=hpicfSyslogControlBindAddrIsOobm, hpicfSyslogGeneralLogRelay=hpicfSyslogGeneralLogRelay, hpicfSyslogServerLogRecv=hpicfSyslogServerLogRecv, hpicfSyslogSmmLogMsgCompliance2=hpicfSyslogSmmLogMsgCompliance2, hpicfSyslogServerSendError=hpicfSyslogServerSendError, hpicfSyslogServerStatisticsEntry=hpicfSyslogServerStatisticsEntry, hpicfSyslogAlerts=hpicfSyslogAlerts, hpicfSyslogServerLogRelay=hpicfSyslogServerLogRelay, hpicfSyslogStatisticsCompliance=hpicfSyslogStatisticsCompliance, hpicfSyslogfacilityCounterIndex=hpicfSyslogfacilityCounterIndex, hpicfSyslogFacilityStatistics=hpicfSyslogFacilityStatistics, hpicfSyslogNotificationCompliance=hpicfSyslogNotificationCompliance, hpicfSyslogPriorityFacility=hpicfSyslogPriorityFacility, HpicfSyslogOriginId=HpicfSyslogOriginId, hpicfSyslogOperations=hpicfSyslogOperations, hpicfSyslogAlertsEntry=hpicfSyslogAlertsEntry, hpicfSyslogPriorityCompliance=hpicfSyslogPriorityCompliance, hpicfSyslogCommandLoggingCompliance=hpicfSyslogCommandLoggingCompliance, hpicfSyslogControlTransportProtocol=hpicfSyslogControlTransportProtocol, hpicfSyslogOperationsCounterDiscontinuityTime=hpicfSyslogOperationsCounterDiscontinuityTime, hpicfSyslogObjects=hpicfSyslogObjects, hpicfSyslogFullCompliance1=hpicfSyslogFullCompliance1, hpicfSyslogFacilityCounterInfoEntry=hpicfSyslogFacilityCounterInfoEntry, hpicfSyslogMIB=hpicfSyslogMIB, hpicfSyslogControlGroupOobm=hpicfSyslogControlGroupOobm, hpicfSyslogControlFilterNameGroup=hpicfSyslogControlFilterNameGroup, hpicfSyslogControlFilterName=hpicfSyslogControlFilterName, hpicfSyslogSeverityType=hpicfSyslogSeverityType, hpicfSyslogFullCompliance2=hpicfSyslogFullCompliance2, hpicfSyslogLogMsgOptionsGroup=hpicfSyslogLogMsgOptionsGroup, hpicfSyslogOperationsMsgsTransmitted=hpicfSyslogOperationsMsgsTransmitted, hpicfSyslogControlRowStatus=hpicfSyslogControlRowStatus, hpicfSyslogAlertsCompliance=hpicfSyslogAlertsCompliance, hpicfSyslogSeverityCounterInfoTable=hpicfSyslogSeverityCounterInfoTable, hpicfSyslogGroups=hpicfSyslogGroups, hpicfSyslogAlertsTable=hpicfSyslogAlertsTable, hpicfSyslogPrefixString=hpicfSyslogPrefixString, hpicfSyslogServerStatisticsCompliance=hpicfSyslogServerStatisticsCompliance, hpicfSyslogControlBindAddr=hpicfSyslogControlBindAddr, hpicfSyslogControlEntry=hpicfSyslogControlEntry, hpicfSyslogGeneralResendError=hpicfSyslogGeneralResendError, hpicfSyslogCompliances=hpicfSyslogCompliances, HpicfSyslogSeverity=HpicfSyslogSeverity, hpicfSyslogControlBindAddrType=hpicfSyslogControlBindAddrType, hpicfSyslogControlTable=hpicfSyslogControlTable, hpicfSyslogGeneralStatistics=hpicfSyslogGeneralStatistics, hpicfSyslogServerResendError=hpicfSyslogServerResendError, hpicfSyslogFacilityStatisticsGroup=hpicfSyslogFacilityStatisticsGroup, hpicfSyslogSmmLogMsgCompliance1=hpicfSyslogSmmLogMsgCompliance1, hpicfSyslogControlDestinationPort=hpicfSyslogControlDestinationPort, hpicfSyslogfacilityCounter=hpicfSyslogfacilityCounter, hpicfSyslogGeneralSendError=hpicfSyslogGeneralSendError, hpicfSyslogLogMsgOptions=hpicfSyslogLogMsgOptions, hpicfSyslogLogMsgOptionsGroup2=hpicfSyslogLogMsgOptionsGroup2, hpicfSyslogGeneralStatisticsGroup=hpicfSyslogGeneralStatisticsGroup, hpicfSyslogGeneralLogResend=hpicfSyslogGeneralLogResend, hpicfSyslogAlertIndex=hpicfSyslogAlertIndex, hpicfSyslogSystemModule=hpicfSyslogSystemModule, hpicfSyslogOriginIdGroup1=hpicfSyslogOriginIdGroup1, hpicfSyslogGeneralLogBuffered=hpicfSyslogGeneralLogBuffered, hpicfSyslogServerLogSent=hpicfSyslogServerLogSent, hpicfSyslogOperationsMsgsDropped=hpicfSyslogOperationsMsgsDropped, hpicfSyslogSeverityCounterInfoEntry=hpicfSyslogSeverityCounterInfoEntry, hpicfSyslogOperationsStatus=hpicfSyslogOperationsStatus, hpicfSyslogTransportFilterNameCompliance=hpicfSyslogTransportFilterNameCompliance, HpicfSyslogSystemModule=HpicfSyslogSystemModule, hpicfSyslogfacilityType=hpicfSyslogfacilityType, hpicfSyslogControlTransportGroup=hpicfSyslogControlTransportGroup, hpicfSyslogLogMsgOptionsGroup1=hpicfSyslogLogMsgOptionsGroup1, hpicfSyslogLogging=hpicfSyslogLogging, hpicfSyslogAlertsGroup=hpicfSyslogAlertsGroup, hpicfSyslogReadOnlyCompliance1=hpicfSyslogReadOnlyCompliance1, hpicfSyslogControlDescr=hpicfSyslogControlDescr, hpicfSyslogSeverityStatisticsGroup=hpicfSyslogSeverityStatisticsGroup, hpicfSyslogOriginIdCompliance=hpicfSyslogOriginIdCompliance, hpicfSyslogPriorityDescr=hpicfSyslogPriorityDescr, hpicfSyslogOperationsLastErrorTime=hpicfSyslogOperationsLastErrorTime, hpicfSyslogOperationsGroup=hpicfSyslogOperationsGroup, hpicfSyslogPriority=hpicfSyslogPriority, hpicfSyslogAlertAdminStatus=hpicfSyslogAlertAdminStatus, hpicfSyslogFacilityCounterInfoTable=hpicfSyslogFacilityCounterInfoTable, hpicfSyslogOperationsLastError=hpicfSyslogOperationsLastError)
