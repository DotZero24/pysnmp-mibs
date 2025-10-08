#
# PySNMP MIB module NETSCREEN-SET-EMAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netscreen/NETSCREEN-SET-EMAIL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("NETSCREEN-SET-EMAIL-MIB", nsSetEmailAddr2=nsSetEmailAddr2, nsSetEmailLog=nsSetEmailLog, nsSetEmailAddr1=nsSetEmailAddr1, nsSetEmailSMTP=nsSetEmailSMTP, netscreenSetEmailMibModule=netscreenSetEmailMibModule, nsSetEmailEnable=nsSetEmailEnable, PYSNMP_MODULE_ID=netscreenSetEmailMibModule, nsSetEmail=nsSetEmail)
