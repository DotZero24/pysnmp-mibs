#
# PySNMP MIB module HPTCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPTCP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HPTCP-MIB", hpTcpObjects=hpTcpObjects, hpTcpOutRstsWithAck=hpTcpOutRstsWithAck, hpTcpCompliance=hpTcpCompliance, hpTcpConformance=hpTcpConformance, hpTcpGroups=hpTcpGroups, hpicfTcpMib=hpicfTcpMib, hpTcpBaseGroup=hpTcpBaseGroup, PYSNMP_MODULE_ID=hpicfTcpMib, hpTcpCompliances=hpTcpCompliances)
