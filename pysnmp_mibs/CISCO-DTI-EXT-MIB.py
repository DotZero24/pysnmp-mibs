#
# PySNMP MIB module CISCO-DTI-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DTI-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dtiProtocolServerStatusFlag, dtiProtocolClientStatusFlag = mibBuilder.importSymbols("DTI-MIB", "dtiProtocolServerStatusFlag", "dtiProtocolClientStatusFlag")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-DTI-EXT-MIB", ciscoDtiExtCompliances=ciscoDtiExtCompliances, cdeServerStatusChange=cdeServerStatusChange, ciscoDtiExtNotifsControlGroup=ciscoDtiExtNotifsControlGroup, ciscoDtiExtConform=ciscoDtiExtConform, ciscoDtiExtGroups=ciscoDtiExtGroups, cdeServerStatusChangeEnable=cdeServerStatusChangeEnable, PYSNMP_MODULE_ID=ciscoDtiExtMIB, ciscoDtiExtCompliance=ciscoDtiExtCompliance, ciscoDtiExtObjects=ciscoDtiExtObjects, cdeClientStatusChangeEnable=cdeClientStatusChangeEnable, ciscoDtiExtNotifs=ciscoDtiExtNotifs, cdeClientStatusChange=cdeClientStatusChange, ciscoDtiExtMIB=ciscoDtiExtMIB, ciscoDtiExtNotifsGroup=ciscoDtiExtNotifsGroup)
