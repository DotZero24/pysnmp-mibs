#
# PySNMP MIB module RUCKUS-DHCPCLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/RUCKUS-DHCPCLIENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
ruckusDhcpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 46))
ruckusDhcpClientMIB.setRevisions(('2020-07-29 00:00',))
if mibBuilder.loadTexts: ruckusDhcpClientMIB.setLastUpdated('202007290000Z')
if mibBuilder.loadTexts: ruckusDhcpClientMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusDhcpClientGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 46, 1))
ruckusDhcpClientGlobalConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 46, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDhcpClientGlobalConfigState.setStatus('current')
ruckusDhcpClientGlobalAutoUpdateConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 46, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDhcpClientGlobalAutoUpdateConfigState.setStatus('current')
ruckusDhcpClientSpecificVEPort = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 46, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDhcpClientSpecificVEPort.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-DHCPCLIENT-MIB", ruckusDhcpClientSpecificVEPort=ruckusDhcpClientSpecificVEPort, ruckusDhcpClientGlobalObjects=ruckusDhcpClientGlobalObjects, ruckusDhcpClientGlobalAutoUpdateConfigState=ruckusDhcpClientGlobalAutoUpdateConfigState, ruckusDhcpClientMIB=ruckusDhcpClientMIB, ruckusDhcpClientGlobalConfigState=ruckusDhcpClientGlobalConfigState, PYSNMP_MODULE_ID=ruckusDhcpClientMIB)
