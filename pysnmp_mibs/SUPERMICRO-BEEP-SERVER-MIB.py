#
# PySNMP MIB module SUPERMICRO-BEEP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-BEEP-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsBeepServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 2, 18))
fsBeepServer.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsBeepServer.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsBeepServer.setOrganization('Super Micro Computer Inc.')
fsBeepServerScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1))
fsBeepServerAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBeepServerAdminStatus.setStatus('current')
fsBeepServerRawProfile = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBeepServerRawProfile.setStatus('current')
fsBeepServerIpv4PortNum = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(601)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBeepServerIpv4PortNum.setStatus('current')
fsBeepServerIpv6PortNum = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(601)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBeepServerIpv6PortNum.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-BEEP-SERVER-MIB", fsBeepServerAdminStatus=fsBeepServerAdminStatus, fsBeepServerScalars=fsBeepServerScalars, fsBeepServerRawProfile=fsBeepServerRawProfile, fsBeepServerIpv4PortNum=fsBeepServerIpv4PortNum, fsBeepServerIpv6PortNum=fsBeepServerIpv6PortNum, fsBeepServer=fsBeepServer, PYSNMP_MODULE_ID=fsBeepServer)
