#
# PySNMP MIB module FS-ANTI-ARPCHEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
IfIndex, = mibBuilder.importSymbols("FS-TC", "IfIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
fsAntiArpcheatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41))
fsAntiArpcheatMIB.setRevisions(('2007-01-29 00:00',))
if mibBuilder.loadTexts: fsAntiArpcheatMIB.setLastUpdated('200701290000Z')
if mibBuilder.loadTexts: fsAntiArpcheatMIB.setOrganization('FS.COM Inc..')
fsAntiArpcheatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1))
fsTrustedArpDelete = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsTrustedArpDelete.setStatus('current')
fsTrustedArpTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2), )
if mibBuilder.loadTexts: fsTrustedArpTable.setStatus('current')
fsTrustedArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1), ).setIndexNames((0, "FS-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"), (0, "FS-ANTI-ARPCHEAT-MIB", "trustedArpIp"))
if mibBuilder.loadTexts: fsTrustedArpEntry.setStatus('current')
trustedArpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 1), IfIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpIfIndex.setStatus('current')
trustedArpIp = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpIp.setStatus('current')
trustedArpMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpMediaPhysAddress.setStatus('current')
trustedArpVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpVlan.setStatus('current')
trustedArpOperationType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpOperationType.setStatus('current')
fsAntiArpcheatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2))
fsAntiArpcheatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 1))
fsAntiArpcheatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 2))
fsAntiArpcheatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 1, 1)).setObjects(("FS-ANTI-ARPCHEAT-MIB", "fsAntiArpcheatMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsAntiArpcheatMIBCompliance = fsAntiArpcheatMIBCompliance.setStatus('current')
fsAntiArpcheatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 2, 1)).setObjects(("FS-ANTI-ARPCHEAT-MIB", "fsTrustedArpDelete"), ("FS-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"), ("FS-ANTI-ARPCHEAT-MIB", "trustedArpIp"), ("FS-ANTI-ARPCHEAT-MIB", "trustedArpMediaPhysAddress"), ("FS-ANTI-ARPCHEAT-MIB", "trustedArpVlan"), ("FS-ANTI-ARPCHEAT-MIB", "trustedArpOperationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsAntiArpcheatMIBGroup = fsAntiArpcheatMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-ANTI-ARPCHEAT-MIB", fsAntiArpcheatMIBConformance=fsAntiArpcheatMIBConformance, fsAntiArpcheatMIBCompliance=fsAntiArpcheatMIBCompliance, trustedArpIp=trustedArpIp, fsAntiArpcheatMIBGroups=fsAntiArpcheatMIBGroups, trustedArpIfIndex=trustedArpIfIndex, trustedArpOperationType=trustedArpOperationType, fsAntiArpcheatMIBCompliances=fsAntiArpcheatMIBCompliances, trustedArpVlan=trustedArpVlan, fsTrustedArpEntry=fsTrustedArpEntry, PYSNMP_MODULE_ID=fsAntiArpcheatMIB, fsAntiArpcheatMIBGroup=fsAntiArpcheatMIBGroup, fsTrustedArpDelete=fsTrustedArpDelete, fsTrustedArpTable=fsTrustedArpTable, fsAntiArpcheatMIBObjects=fsAntiArpcheatMIBObjects, trustedArpMediaPhysAddress=trustedArpMediaPhysAddress, fsAntiArpcheatMIB=fsAntiArpcheatMIB)
