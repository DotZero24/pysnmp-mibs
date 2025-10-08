#
# PySNMP MIB module DES7200-ANTI-ARPCHEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
IfIndex, = mibBuilder.importSymbols("DES7200-TC", "IfIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
myAntiArpcheatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41))
myAntiArpcheatMIB.setRevisions(('2007-01-29 00:00',))
if mibBuilder.loadTexts: myAntiArpcheatMIB.setLastUpdated('200701290000Z')
if mibBuilder.loadTexts: myAntiArpcheatMIB.setOrganization('D-Link Crop.')
myAntiArpcheatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1))
myTrustedArpDelete = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myTrustedArpDelete.setStatus('current')
myTrustedArpTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2), )
if mibBuilder.loadTexts: myTrustedArpTable.setStatus('current')
myTrustedArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1), ).setIndexNames((0, "DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"), (0, "DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIp"))
if mibBuilder.loadTexts: myTrustedArpEntry.setStatus('current')
trustedArpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 1), IfIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: trustedArpIfIndex.setStatus('current')
trustedArpIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: trustedArpIp.setStatus('current')
trustedArpMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpMediaPhysAddress.setStatus('current')
trustedArpVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpVlan.setStatus('current')
trustedArpOperationType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpOperationType.setStatus('current')
myAntiArpcheatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2))
myAntiArpcheatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 1))
myAntiArpcheatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 2))
myAntiArpcheatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 1, 1)).setObjects(("DES7200-ANTI-ARPCHEAT-MIB", "myAntiArpcheatMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myAntiArpcheatMIBCompliance = myAntiArpcheatMIBCompliance.setStatus('current')
myAntiArpcheatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 2, 1)).setObjects(("DES7200-ANTI-ARPCHEAT-MIB", "myTrustedArpDelete"), ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"), ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIp"), ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpMediaPhysAddress"), ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpVlan"), ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpOperationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myAntiArpcheatMIBGroup = myAntiArpcheatMIBGroup.setStatus('current')
mibBuilder.exportSymbols("DES7200-ANTI-ARPCHEAT-MIB", myAntiArpcheatMIBObjects=myAntiArpcheatMIBObjects, PYSNMP_MODULE_ID=myAntiArpcheatMIB, trustedArpIp=trustedArpIp, myTrustedArpEntry=myTrustedArpEntry, trustedArpIfIndex=trustedArpIfIndex, myAntiArpcheatMIBConformance=myAntiArpcheatMIBConformance, myAntiArpcheatMIB=myAntiArpcheatMIB, myTrustedArpTable=myTrustedArpTable, trustedArpOperationType=trustedArpOperationType, myAntiArpcheatMIBCompliance=myAntiArpcheatMIBCompliance, myAntiArpcheatMIBCompliances=myAntiArpcheatMIBCompliances, trustedArpVlan=trustedArpVlan, myAntiArpcheatMIBGroup=myAntiArpcheatMIBGroup, myAntiArpcheatMIBGroups=myAntiArpcheatMIBGroups, myTrustedArpDelete=myTrustedArpDelete, trustedArpMediaPhysAddress=trustedArpMediaPhysAddress)
