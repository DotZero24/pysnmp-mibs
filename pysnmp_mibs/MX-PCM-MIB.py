#
# PySNMP MIB module MX-PCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-PCM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:02 2025
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
pcmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 300))
if mibBuilder.loadTexts: pcmMIB.setLastUpdated('1910210000Z')
if mibBuilder.loadTexts: pcmMIB.setOrganization(' Mediatrix Telecom, Inc. ')
pcmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 300, 1))
notificationsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 300, 1, 60010))
minSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 300, 1, 60010, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 100, 200, 300, 400, 500))).clone(namedValues=NamedValues(("disable", 0), ("debug", 100), ("info", 200), ("warning", 300), ("error", 400), ("critical", 500))).clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: minSeverity.setStatus('current')
configurationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 300, 1, 60020))
needRestartInfo = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 300, 1, 60020, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 100))).clone(namedValues=NamedValues(("no", 0), ("yes", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: needRestartInfo.setStatus('current')
mibBuilder.exportSymbols("MX-PCM-MIB", needRestartInfo=needRestartInfo, pcmMIBObjects=pcmMIBObjects, configurationGroup=configurationGroup, pcmMIB=pcmMIB, PYSNMP_MODULE_ID=pcmMIB, notificationsGroup=notificationsGroup, minSeverity=minSeverity)
