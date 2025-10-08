#
# PySNMP MIB module MX-CDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-CDR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixServices, = mibBuilder.importSymbols("MX-SMI2", "mediatrixServices")
MxActivationState, MxAdvancedIpPort, MxIpPort, MxDigitMap, MxEnableState, MxIpSubnetMask, MxIpHostName, MxIpAddress = mibBuilder.importSymbols("MX-TC", "MxActivationState", "MxAdvancedIpPort", "MxIpPort", "MxDigitMap", "MxEnableState", "MxIpSubnetMask", "MxIpHostName", "MxIpAddress")
MxUrl, MxUInt64, MxIpAddr, MxIpAddrMask, MxUri, MxIpAddrPort, MxFloat32, MxIpHostNamePort = mibBuilder.importSymbols("MX-TC2", "MxUrl", "MxUInt64", "MxIpAddr", "MxIpAddrMask", "MxUri", "MxIpAddrPort", "MxFloat32", "MxIpHostNamePort")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-CDR-MIB", needRestartInfo=needRestartInfo, syslogGroup=syslogGroup, notificationsGroup=notificationsGroup, cdrMIB=cdrMIB, syslogFormat=syslogFormat, configurationGroup=configurationGroup, PYSNMP_MODULE_ID=cdrMIB, syslogRemoteHost=syslogRemoteHost, syslogFacility=syslogFacility, cdrMIBObjects=cdrMIBObjects, minSeverity=minSeverity)
