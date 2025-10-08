#
# PySNMP MIB module MX-CDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-CDR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixServices, = mibBuilder.importSymbols("MX-SMI2", "mediatrixServices")
MxActivationState, MxEnableState, MxIpAddress, MxAdvancedIpPort, MxDigitMap, MxIpPort, MxIpHostName, MxIpSubnetMask = mibBuilder.importSymbols("MX-TC", "MxActivationState", "MxEnableState", "MxIpAddress", "MxAdvancedIpPort", "MxDigitMap", "MxIpPort", "MxIpHostName", "MxIpSubnetMask")
MxIpHostNamePort, MxIpAddrMask, MxUri, MxIpAddr, MxIpAddrPort, MxUrl, MxUInt64, MxFloat32 = mibBuilder.importSymbols("MX-TC2", "MxIpHostNamePort", "MxIpAddrMask", "MxUri", "MxIpAddr", "MxIpAddrPort", "MxUrl", "MxUInt64", "MxFloat32")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cdrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200))
if mibBuilder.loadTexts: cdrMIB.setLastUpdated('1910210000Z')
if mibBuilder.loadTexts: cdrMIB.setOrganization(' Mediatrix Telecom, Inc. ')
cdrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1))
syslogGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 400))
syslogRemoteHost = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 400, 100), MxIpHostNamePort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogRemoteHost.setStatus('current')
syslogFormat = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 400, 200), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogFormat.setStatus('current')
syslogFacility = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 400, 300), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(100, 200, 300, 400, 500, 600, 700, 800))).clone(namedValues=NamedValues(("local0", 100), ("local1", 200), ("local2", 300), ("local3", 400), ("local4", 500), ("local5", 600), ("local6", 700), ("local7", 800))).clone('local0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogFacility.setStatus('current')
notificationsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 60010))
minSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 60010, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 100, 200, 300, 400, 500))).clone(namedValues=NamedValues(("disable", 0), ("debug", 100), ("info", 200), ("warning", 300), ("error", 400), ("critical", 500))).clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: minSeverity.setStatus('current')
configurationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 60020))
needRestartInfo = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4200, 1, 60020, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 100))).clone(namedValues=NamedValues(("no", 0), ("yes", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: needRestartInfo.setStatus('current')
mibBuilder.exportSymbols("MX-CDR-MIB", syslogFacility=syslogFacility, syslogRemoteHost=syslogRemoteHost, notificationsGroup=notificationsGroup, syslogGroup=syslogGroup, cdrMIB=cdrMIB, minSeverity=minSeverity, configurationGroup=configurationGroup, cdrMIBObjects=cdrMIBObjects, needRestartInfo=needRestartInfo, syslogFormat=syslogFormat, PYSNMP_MODULE_ID=cdrMIB)
