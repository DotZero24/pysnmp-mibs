#
# PySNMP MIB module ARICENT-BEEP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aricent/ARICENT-BEEP-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:56:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsBeepServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 29601, 2, 18))
fsBeepServer.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsBeepServer.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsBeepServer.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
fsBeepServerScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 29601, 2, 18, 1))
fsBeepServerAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBeepServerAdminStatus.setStatus('current')
fsBeepServerRawProfile = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBeepServerRawProfile.setStatus('current')
fsBeepServerIpv4PortNum = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 18, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(601)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBeepServerIpv4PortNum.setStatus('current')
fsBeepServerIpv6PortNum = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 18, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(601)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBeepServerIpv6PortNum.setStatus('current')
mibBuilder.exportSymbols("ARICENT-BEEP-SERVER-MIB", PYSNMP_MODULE_ID=fsBeepServer, fsBeepServer=fsBeepServer, fsBeepServerRawProfile=fsBeepServerRawProfile, fsBeepServerIpv6PortNum=fsBeepServerIpv6PortNum, fsBeepServerAdminStatus=fsBeepServerAdminStatus, fsBeepServerScalars=fsBeepServerScalars, fsBeepServerIpv4PortNum=fsBeepServerIpv4PortNum)
