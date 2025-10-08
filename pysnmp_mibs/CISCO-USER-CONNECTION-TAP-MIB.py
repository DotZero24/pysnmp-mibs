#
# PySNMP MIB module CISCO-USER-CONNECTION-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-USER-CONNECTION-TAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2StreamIndex, cTap2MediationContentId = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2StreamIndex", "cTap2MediationContentId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoUserConnectionTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 400))
ciscoUserConnectionTapMIB.setRevisions(('2007-08-09 00:00', '2004-03-11 00:00',))
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setLastUpdated('200708090000Z')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setOrganization('Cisco Systems, Inc.')
cUserConnectionTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1))
cUserConnectionTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2))
cuctTapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1))
cuctTapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("acctSessionId", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuctTapStreamCapabilities.setStatus('current')
cuctTapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2), )
if mibBuilder.loadTexts: cuctTapStreamTable.setStatus('current')
cuctTapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cuctTapStreamEntry.setStatus('current')
cuctTapStreamAcctSessID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setStatus('current')
cuctTapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamStatus.setStatus('current')
cUserConnectionTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1))
cUserConnectionTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2))
cUserConnectionTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cUserConnectionTapMIBCompliance = cUserConnectionTapMIBCompliance.setStatus('current')
cuctTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamCapabilities"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamAcctSessID"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cuctTapStreamComplianceGroup = cuctTapStreamComplianceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-USER-CONNECTION-TAP-MIB", cuctTapStreamStatus=cuctTapStreamStatus, ciscoUserConnectionTapMIB=ciscoUserConnectionTapMIB, cUserConnectionTapMIBCompliance=cUserConnectionTapMIBCompliance, cUserConnectionTapMIBGroups=cUserConnectionTapMIBGroups, cuctTapStreamEncodePacket=cuctTapStreamEncodePacket, PYSNMP_MODULE_ID=ciscoUserConnectionTapMIB, cuctTapStreamEntry=cuctTapStreamEntry, cuctTapStreamComplianceGroup=cuctTapStreamComplianceGroup, cUserConnectionTapMIBObjects=cUserConnectionTapMIBObjects, cuctTapStreamCapabilities=cuctTapStreamCapabilities, cUserConnectionTapMIBCompliances=cUserConnectionTapMIBCompliances, cuctTapStreamAcctSessID=cuctTapStreamAcctSessID, cUserConnectionTapMIBConform=cUserConnectionTapMIBConform, cuctTapStreamTable=cuctTapStreamTable)
