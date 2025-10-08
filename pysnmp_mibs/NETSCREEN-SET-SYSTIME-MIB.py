#
# PySNMP MIB module NETSCREEN-SET-SYSTIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netscreen/NETSCREEN-SET-SYSTIME-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenSetSystimeMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 6))
netscreenSetSystimeMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-12 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenSetSystimeMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetSystimeMibModule.setOrganization('Juniper Networks, Inc.')
nsSetSysTime = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 6))
nsSetSysTimeGmtOffset = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetSysTimeGmtOffset.setStatus('current')
nsSetSysTimeDaySaving = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetSysTimeDaySaving.setStatus('current')
nsSetSysTimeNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3))
nsSetNtpEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetNtpEnable.setStatus('current')
nsSetNtpServer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetNtpServer.setStatus('current')
nsSetNtpUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetNtpUpdateInterval.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SET-SYSTIME-MIB", nsSetNtpEnable=nsSetNtpEnable, PYSNMP_MODULE_ID=netscreenSetSystimeMibModule, nsSetSysTimeNTP=nsSetSysTimeNTP, nsSetSysTimeDaySaving=nsSetSysTimeDaySaving, nsSetNtpServer=nsSetNtpServer, nsSetSysTimeGmtOffset=nsSetSysTimeGmtOffset, nsSetNtpUpdateInterval=nsSetNtpUpdateInterval, nsSetSysTime=nsSetSysTime, netscreenSetSystimeMibModule=netscreenSetSystimeMibModule)
