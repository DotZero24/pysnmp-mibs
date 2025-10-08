#
# PySNMP MIB module HPTCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPTCP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfTcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79))
hpicfTcpMib.setRevisions(('2010-09-30 15:25',))
if mibBuilder.loadTexts: hpicfTcpMib.setLastUpdated('201009301525Z')
if mibBuilder.loadTexts: hpicfTcpMib.setOrganization('HP Networking')
hpTcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1))
hpTcpOutRstsWithAck = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpTcpOutRstsWithAck.setStatus('current')
hpTcpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2))
hpTcpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1))
hpTcpBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1, 1)).setObjects(("HPTCP-MIB", "hpTcpOutRstsWithAck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTcpBaseGroup = hpTcpBaseGroup.setStatus('current')
hpTcpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2))
hpTcpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2, 1)).setObjects(("HPTCP-MIB", "hpTcpBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpTcpCompliance = hpTcpCompliance.setStatus('current')
mibBuilder.exportSymbols("HPTCP-MIB", hpicfTcpMib=hpicfTcpMib, hpTcpObjects=hpTcpObjects, PYSNMP_MODULE_ID=hpicfTcpMib, hpTcpOutRstsWithAck=hpTcpOutRstsWithAck, hpTcpConformance=hpTcpConformance, hpTcpGroups=hpTcpGroups, hpTcpBaseGroup=hpTcpBaseGroup, hpTcpCompliances=hpTcpCompliances, hpTcpCompliance=hpTcpCompliance)
