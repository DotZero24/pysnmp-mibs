#
# PySNMP MIB module Dot1xMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/Dot1xMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swdot1xMGMTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 30))
if mibBuilder.loadTexts: swdot1xMGMTMIB.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swdot1xMGMTMIB.setOrganization(' ')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

dot1xGuestVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 30, 1))
dot1xGuestVlanName = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xGuestVlanName.setStatus('current')
dot1xGuestVlanPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xGuestVlanPort.setStatus('current')
dot1xGuestVlanDelState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xGuestVlanDelState.setStatus('current')
mibBuilder.exportSymbols("Dot1xMGMT-MIB", PYSNMP_MODULE_ID=swdot1xMGMTMIB, dot1xGuestVlan=dot1xGuestVlan, swdot1xMGMTMIB=swdot1xMGMTMIB, dot1xGuestVlanPort=dot1xGuestVlanPort, dot1xGuestVlanDelState=dot1xGuestVlanDelState, dot1xGuestVlanName=dot1xGuestVlanName, PortList=PortList)
