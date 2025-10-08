#
# PySNMP MIB module TOKENRING-STATION-SR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/TOKENRING-STATION-SR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("TOKENRING-STATION-SR-MIB", dot5SrRouteStatus=dot5SrRouteStatus, dot5SrRouteDescr=dot5SrRouteDescr, dot5SrRouteGroup=dot5SrRouteGroup, dot5SrRouteDestination=dot5SrRouteDestination, dot5SrRouteEntry=dot5SrRouteEntry, dot5SrConformance=dot5SrConformance, dot5SrRouteTable=dot5SrRouteTable, dot5SrMIB=dot5SrMIB, dot5SrCompliance=dot5SrCompliance, SourceRoute=SourceRoute, dot5SrRouteControl=dot5SrRouteControl, dot5SrGroups=dot5SrGroups, dot5SrCompliances=dot5SrCompliances, dot5SrMIBObjects=dot5SrMIBObjects, PYSNMP_MODULE_ID=dot5SrMIB)
