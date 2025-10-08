#
# PySNMP MIB module ZYXEL-CLIENT-PROXY-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-CLIENT-PROXY-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelClientProxyServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121))
if mibBuilder.loadTexts: zyxelClientProxyServer.setLastUpdated('201909300900Z')
if mibBuilder.loadTexts: zyxelClientProxyServer.setOrganization('Enterprise Solution ZyXEL')
zyxelClientProxyServerSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1))
zyClientProxyServerHttpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyClientProxyServerHttpState.setStatus('current')
zyClientProxyServerHttpServer = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyClientProxyServerHttpServer.setStatus('current')
zyClientProxyServerHttpPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyClientProxyServerHttpPort.setStatus('current')
zyClientProxyServerHttpAuthenticationState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 4), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyClientProxyServerHttpAuthenticationState.setStatus('current')
zyClientProxyServerHttpUsername = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyClientProxyServerHttpUsername.setStatus('current')
zyClientProxyServerHttpPassword = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyClientProxyServerHttpPassword.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-CLIENT-PROXY-SERVER-MIB", zyClientProxyServerHttpPort=zyClientProxyServerHttpPort, zyClientProxyServerHttpState=zyClientProxyServerHttpState, zyClientProxyServerHttpServer=zyClientProxyServerHttpServer, zyClientProxyServerHttpUsername=zyClientProxyServerHttpUsername, zyxelClientProxyServer=zyxelClientProxyServer, zyClientProxyServerHttpAuthenticationState=zyClientProxyServerHttpAuthenticationState, zyClientProxyServerHttpPassword=zyClientProxyServerHttpPassword, zyxelClientProxyServerSetup=zyxelClientProxyServerSetup, PYSNMP_MODULE_ID=zyxelClientProxyServer)
