#
# PySNMP MIB module CISCO-APPNAV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-APPNAV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAppNavMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 791))
ciscoAppNavMIB.setRevisions(('2012-06-07 00:00', '2012-05-22 00:00', '2012-04-10 00:00', '2012-03-26 00:00',))
if mibBuilder.loadTexts: ciscoAppNavMIB.setLastUpdated('201206070000Z')
if mibBuilder.loadTexts: ciscoAppNavMIB.setOrganization('Cisco Systems, Inc.')
class CAppNavServContextJoinStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("notConfigured", 2), ("started", 3), ("aborted", 4), ("completed", 5))

class CAppNavCMStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("dead", 1), ("alive", 2), ("excluded", 3), ("partial", 4), ("na", 5), ("zombie", 6), ("inactive", 7))

class CAppNavIRStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ready", 1), ("notReady", 2), ("na", 3))

class CAppNavServContextOpStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("initializing", 1), ("converging", 2), ("internalError", 3), ("degraded", 4), ("operational", 5), ("adminDisabled", 6), ("initializingJoining", 7), ("convergingJoining", 8), ("operationalJoining", 9), ("degradedJoining", 10))

ciscoAppNavMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0))
ciscoAppNavMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 1))
ciscoAppNavMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1))
cAppNavServContext = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1))
cAppNavACG = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2))
cAppNavSNG = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3))
cAppNavAC = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4))
cAppNavSN = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5))
cAppNavServContextTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1), )
if mibBuilder.loadTexts: cAppNavServContextTable.setStatus('current')
cAppNavServContextEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavServContextIndex"))
if mibBuilder.loadTexts: cAppNavServContextEntry.setStatus('current')
cAppNavServContextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavServContextIndex.setStatus('current')
cAppNavServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextName.setStatus('current')
cAppNavServContextCurrOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 3), CAppNavServContextOpStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextCurrOpState.setStatus('current')
cAppNavServContextLastOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 4), CAppNavServContextOpStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextLastOpState.setStatus('current')
cAppNavServContextIRState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 5), CAppNavIRStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextIRState.setStatus('current')
cAppNavServContextJoinState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 6), CAppNavServContextJoinStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextJoinState.setStatus('current')
cAppNavACGTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1), )
if mibBuilder.loadTexts: cAppNavACGTable.setStatus('current')
cAppNavACGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavACGIndex"))
if mibBuilder.loadTexts: cAppNavACGEntry.setStatus('current')
cAppNavACGIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavACGIndex.setStatus('current')
cAppNavACGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACGName.setStatus('current')
cAppNavACGServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACGServContextName.setStatus('current')
cAppNavSNGTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1), )
if mibBuilder.loadTexts: cAppNavSNGTable.setStatus('current')
cAppNavSNGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavSNGIndex"))
if mibBuilder.loadTexts: cAppNavSNGEntry.setStatus('current')
cAppNavSNGIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavSNGIndex.setStatus('current')
cAppNavSNGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNGName.setStatus('current')
cAppNavSNGServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNGServContextName.setStatus('current')
cAppNavACTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1), )
if mibBuilder.loadTexts: cAppNavACTable.setStatus('current')
cAppNavACEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavACIndex"))
if mibBuilder.loadTexts: cAppNavACEntry.setStatus('current')
cAppNavACIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavACIndex.setStatus('current')
cAppNavACIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACIpAddrType.setStatus('current')
cAppNavACIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACIpAddr.setStatus('current')
cAppNavACServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACServContextName.setStatus('current')
cAppNavACACGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACACGName.setStatus('current')
cAppNavACCurrentCMState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 6), CAppNavCMStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACCurrentCMState.setStatus('current')
cAppNavSNTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1), )
if mibBuilder.loadTexts: cAppNavSNTable.setStatus('current')
cAppNavSNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavSNIndex"))
if mibBuilder.loadTexts: cAppNavSNEntry.setStatus('current')
cAppNavSNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavSNIndex.setStatus('current')
cAppNavSNIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNIpAddrType.setStatus('current')
cAppNavSNIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNIpAddr.setStatus('current')
cAppNavSNServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNServContextName.setStatus('current')
cAppNavSNSNGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNSNGName.setStatus('current')
cAppNavSNCurrentCMState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 6), CAppNavCMStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNCurrentCMState.setStatus('current')
ciscoAppNavMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2))
ciscoAppNavMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1, 1)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServiceContextGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavMIBCompliance = ciscoAppNavMIBCompliance.setStatus('deprecated')
ciscoAppNavMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1, 2)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServiceContextGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGroup"), ("CISCO-APPNAV-MIB", "cAppNavServiceContextGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavMIBComplianceRev1 = ciscoAppNavMIBComplianceRev1.setStatus('current')
cAppNavServiceContextGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 1)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServContextCurrOpState"), ("CISCO-APPNAV-MIB", "cAppNavServContextLastOpState"), ("CISCO-APPNAV-MIB", "cAppNavServContextIRState"), ("CISCO-APPNAV-MIB", "cAppNavServContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavServiceContextGroup = cAppNavServiceContextGroup.setStatus('current')
cAppNavACGGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 2)).setObjects(("CISCO-APPNAV-MIB", "cAppNavACGServContextName"), ("CISCO-APPNAV-MIB", "cAppNavACGName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavACGGroup = cAppNavACGGroup.setStatus('current')
cAppNavSNGGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 3)).setObjects(("CISCO-APPNAV-MIB", "cAppNavSNGServContextName"), ("CISCO-APPNAV-MIB", "cAppNavSNGName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavSNGGroup = cAppNavSNGGroup.setStatus('current')
cAppNavACGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 4)).setObjects(("CISCO-APPNAV-MIB", "cAppNavACServContextName"), ("CISCO-APPNAV-MIB", "cAppNavACACGName"), ("CISCO-APPNAV-MIB", "cAppNavACCurrentCMState"), ("CISCO-APPNAV-MIB", "cAppNavACIpAddrType"), ("CISCO-APPNAV-MIB", "cAppNavACIpAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavACGroup = cAppNavACGroup.setStatus('current')
cAppNavSNGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 5)).setObjects(("CISCO-APPNAV-MIB", "cAppNavSNServContextName"), ("CISCO-APPNAV-MIB", "cAppNavSNSNGName"), ("CISCO-APPNAV-MIB", "cAppNavSNCurrentCMState"), ("CISCO-APPNAV-MIB", "cAppNavSNIpAddrType"), ("CISCO-APPNAV-MIB", "cAppNavSNIpAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavSNGroup = cAppNavSNGroup.setStatus('current')
cAppNavServiceContextGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 6)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServContextJoinState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavServiceContextGroupRev1 = cAppNavServiceContextGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPNAV-MIB", PYSNMP_MODULE_ID=ciscoAppNavMIB, cAppNavServContextIndex=cAppNavServContextIndex, cAppNavServContextLastOpState=cAppNavServContextLastOpState, cAppNavACTable=cAppNavACTable, cAppNavACEntry=cAppNavACEntry, cAppNavSNIndex=cAppNavSNIndex, cAppNavSNGEntry=cAppNavSNGEntry, cAppNavSNCurrentCMState=cAppNavSNCurrentCMState, ciscoAppNavMIB=ciscoAppNavMIB, cAppNavSNG=cAppNavSNG, cAppNavServContext=cAppNavServContext, cAppNavSNSNGName=cAppNavSNSNGName, cAppNavSNGIndex=cAppNavSNGIndex, ciscoAppNavMIBCompliance=ciscoAppNavMIBCompliance, cAppNavSNGServContextName=cAppNavSNGServContextName, cAppNavACIpAddrType=cAppNavACIpAddrType, cAppNavACServContextName=cAppNavACServContextName, ciscoAppNavMIBGroups=ciscoAppNavMIBGroups, cAppNavACGTable=cAppNavACGTable, cAppNavACACGName=cAppNavACACGName, cAppNavSNTable=cAppNavSNTable, CAppNavIRStates=CAppNavIRStates, cAppNavServContextIRState=cAppNavServContextIRState, cAppNavSNGTable=cAppNavSNGTable, ciscoAppNavMIBComplianceRev1=ciscoAppNavMIBComplianceRev1, cAppNavServContextName=cAppNavServContextName, cAppNavSNGGroup=cAppNavSNGGroup, cAppNavSNIpAddr=cAppNavSNIpAddr, cAppNavACGroup=cAppNavACGroup, cAppNavServiceContextGroup=cAppNavServiceContextGroup, cAppNavServContextJoinState=cAppNavServContextJoinState, ciscoAppNavMIBCompliances=ciscoAppNavMIBCompliances, cAppNavACCurrentCMState=cAppNavACCurrentCMState, cAppNavACGIndex=cAppNavACGIndex, cAppNavServContextTable=cAppNavServContextTable, cAppNavSNIpAddrType=cAppNavSNIpAddrType, cAppNavACGEntry=cAppNavACGEntry, cAppNavACIpAddr=cAppNavACIpAddr, ciscoAppNavMIBConform=ciscoAppNavMIBConform, cAppNavSN=cAppNavSN, cAppNavSNGName=cAppNavSNGName, cAppNavServiceContextGroupRev1=cAppNavServiceContextGroupRev1, cAppNavACG=cAppNavACG, CAppNavServContextOpStates=CAppNavServContextOpStates, cAppNavSNServContextName=cAppNavSNServContextName, CAppNavCMStates=CAppNavCMStates, cAppNavServContextCurrOpState=cAppNavServContextCurrOpState, cAppNavACGName=cAppNavACGName, cAppNavACIndex=cAppNavACIndex, cAppNavServContextEntry=cAppNavServContextEntry, cAppNavACGServContextName=cAppNavACGServContextName, cAppNavSNGroup=cAppNavSNGroup, cAppNavACGGroup=cAppNavACGGroup, cAppNavSNEntry=cAppNavSNEntry, ciscoAppNavMIBObjects=ciscoAppNavMIBObjects, CAppNavServContextJoinStates=CAppNavServContextJoinStates, cAppNavAC=cAppNavAC)
