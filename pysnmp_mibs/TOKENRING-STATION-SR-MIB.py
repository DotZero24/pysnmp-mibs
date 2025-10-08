#
# PySNMP MIB module TOKENRING-STATION-SR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/TOKENRING-STATION-SR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
MacAddress, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "DisplayString", "TextualConvention")
dot5SrMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 42))
if mibBuilder.loadTexts: dot5SrMIB.setLastUpdated('9412161000Z')
if mibBuilder.loadTexts: dot5SrMIB.setOrganization('IETF Interfaces MIB Working Group')
dot5SrMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 1))
class SourceRoute(TextualConvention, OctetString):
    reference = 'Annex C of ISO/IEC 10038: 1993, [ANSI/IEEE Std 802.1D, 1993]'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

dot5SrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 42, 1, 1), )
if mibBuilder.loadTexts: dot5SrRouteTable.setStatus('current')
dot5SrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 42, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TOKENRING-STATION-SR-MIB", "dot5SrRouteDestination"))
if mibBuilder.loadTexts: dot5SrRouteEntry.setStatus('current')
dot5SrRouteDestination = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: dot5SrRouteDestination.setStatus('current')
dot5SrRouteControl = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteControl.setStatus('current')
dot5SrRouteDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 4), SourceRoute()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteDescr.setStatus('current')
dot5SrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteStatus.setStatus('current')
dot5SrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2))
dot5SrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 1))
dot5SrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 2))
dot5SrCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 42, 2, 2, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrCompliance = dot5SrCompliance.setStatus('current')
dot5SrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 42, 2, 1, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteControl"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteDescr"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrRouteGroup = dot5SrRouteGroup.setStatus('current')
mibBuilder.exportSymbols("TOKENRING-STATION-SR-MIB", PYSNMP_MODULE_ID=dot5SrMIB, dot5SrCompliance=dot5SrCompliance, dot5SrRouteControl=dot5SrRouteControl, dot5SrRouteDescr=dot5SrRouteDescr, SourceRoute=SourceRoute, dot5SrConformance=dot5SrConformance, dot5SrRouteEntry=dot5SrRouteEntry, dot5SrCompliances=dot5SrCompliances, dot5SrMIB=dot5SrMIB, dot5SrRouteStatus=dot5SrRouteStatus, dot5SrGroups=dot5SrGroups, dot5SrRouteGroup=dot5SrRouteGroup, dot5SrRouteTable=dot5SrRouteTable, dot5SrRouteDestination=dot5SrRouteDestination, dot5SrMIBObjects=dot5SrMIBObjects)
