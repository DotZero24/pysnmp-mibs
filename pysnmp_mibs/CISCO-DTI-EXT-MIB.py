#
# PySNMP MIB module CISCO-DTI-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-DTI-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dtiProtocolClientStatusFlag, dtiProtocolServerStatusFlag = mibBuilder.importSymbols("DTI-MIB", "dtiProtocolClientStatusFlag", "dtiProtocolServerStatusFlag")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoDtiExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 822))
ciscoDtiExtMIB.setRevisions(('2014-08-22 00:00',))
if mibBuilder.loadTexts: ciscoDtiExtMIB.setLastUpdated('201408220000Z')
if mibBuilder.loadTexts: ciscoDtiExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoDtiExtNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 0))
ciscoDtiExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 1))
ciscoDtiExtConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2))
cdeServerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 1)).setObjects(("DTI-MIB", "dtiProtocolServerStatusFlag"))
if mibBuilder.loadTexts: cdeServerStatusChange.setStatus('current')
cdeClientStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 2)).setObjects(("DTI-MIB", "dtiProtocolClientStatusFlag"))
if mibBuilder.loadTexts: cdeClientStatusChange.setStatus('current')
ciscoDtiExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1))
cdeServerStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeServerStatusChangeEnable.setStatus('current')
cdeClientStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeClientStatusChangeEnable.setStatus('current')
ciscoDtiExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2))
ciscoDtiExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1, 1)).setObjects(("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsControlGroup"), ("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtCompliance = ciscoDtiExtCompliance.setStatus('current')
ciscoDtiExtNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 1)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChangeEnable"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChangeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsControlGroup = ciscoDtiExtNotifsControlGroup.setStatus('current')
ciscoDtiExtNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 2)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChange"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsGroup = ciscoDtiExtNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DTI-EXT-MIB", ciscoDtiExtGroups=ciscoDtiExtGroups, cdeServerStatusChangeEnable=cdeServerStatusChangeEnable, PYSNMP_MODULE_ID=ciscoDtiExtMIB, ciscoDtiExtMIB=ciscoDtiExtMIB, ciscoDtiExtNotifsGroup=ciscoDtiExtNotifsGroup, ciscoDtiExtObjects=ciscoDtiExtObjects, ciscoDtiExtConform=ciscoDtiExtConform, cdeClientStatusChange=cdeClientStatusChange, ciscoDtiExtNotifs=ciscoDtiExtNotifs, cdeClientStatusChangeEnable=cdeClientStatusChangeEnable, cdeServerStatusChange=cdeServerStatusChange, ciscoDtiExtNotifsControlGroup=ciscoDtiExtNotifsControlGroup, ciscoDtiExtCompliance=ciscoDtiExtCompliance, ciscoDtiExtCompliances=ciscoDtiExtCompliances)
