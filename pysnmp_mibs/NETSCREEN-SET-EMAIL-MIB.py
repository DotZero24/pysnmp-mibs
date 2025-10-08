#
# PySNMP MIB module NETSCREEN-SET-EMAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netscreen/NETSCREEN-SET-EMAIL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenSetEmailMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 7))
netscreenSetEmailMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setOrganization('Juniper Networks, Inc.')
nsSetEmail = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 7))
nsSetEmailEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailEnable.setStatus('current')
nsSetEmailSMTP = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailSMTP.setStatus('current')
nsSetEmailLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailLog.setStatus('current')
nsSetEmailAddr1 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr1.setStatus('current')
nsSetEmailAddr2 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr2.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SET-EMAIL-MIB", netscreenSetEmailMibModule=netscreenSetEmailMibModule, nsSetEmail=nsSetEmail, nsSetEmailEnable=nsSetEmailEnable, PYSNMP_MODULE_ID=netscreenSetEmailMibModule, nsSetEmailAddr1=nsSetEmailAddr1, nsSetEmailAddr2=nsSetEmailAddr2, nsSetEmailLog=nsSetEmailLog, nsSetEmailSMTP=nsSetEmailSMTP)
