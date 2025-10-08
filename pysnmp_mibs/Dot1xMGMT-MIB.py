#
# PySNMP MIB module Dot1xMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/Dot1xMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("Dot1xMGMT-MIB", dot1xGuestVlanName=dot1xGuestVlanName, swdot1xMGMTMIB=swdot1xMGMTMIB, PYSNMP_MODULE_ID=swdot1xMGMTMIB, dot1xGuestVlanPort=dot1xGuestVlanPort, dot1xGuestVlan=dot1xGuestVlan, PortList=PortList, dot1xGuestVlanDelState=dot1xGuestVlanDelState)
