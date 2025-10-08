#
# PySNMP MIB module FS-ANTI-ARPCHEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
IfIndex, = mibBuilder.importSymbols("FS-TC", "IfIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-ANTI-ARPCHEAT-MIB", trustedArpOperationType=trustedArpOperationType, fsAntiArpcheatMIBGroups=fsAntiArpcheatMIBGroups, trustedArpIfIndex=trustedArpIfIndex, fsTrustedArpDelete=fsTrustedArpDelete, fsAntiArpcheatMIBCompliances=fsAntiArpcheatMIBCompliances, fsTrustedArpTable=fsTrustedArpTable, trustedArpIp=trustedArpIp, fsAntiArpcheatMIBConformance=fsAntiArpcheatMIBConformance, fsAntiArpcheatMIBCompliance=fsAntiArpcheatMIBCompliance, PYSNMP_MODULE_ID=fsAntiArpcheatMIB, trustedArpVlan=trustedArpVlan, trustedArpMediaPhysAddress=trustedArpMediaPhysAddress, fsAntiArpcheatMIB=fsAntiArpcheatMIB, fsAntiArpcheatMIBGroup=fsAntiArpcheatMIBGroup, fsTrustedArpEntry=fsTrustedArpEntry, fsAntiArpcheatMIBObjects=fsAntiArpcheatMIBObjects)
