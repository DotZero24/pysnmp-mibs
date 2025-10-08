#
# PySNMP MIB module HPICF-AMP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPICF-AMP-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
hpicfAMPServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125))
hpicfAMPServerMIB.setRevisions(('2020-01-17 00:00', '2017-03-07 00:00', '2017-01-04 00:00', '2016-12-16 00:00', '2016-09-15 00:00', '2016-04-19 00:00', '2016-03-03 00:00', '2015-12-14 00:00',))
if mibBuilder.loadTexts: hpicfAMPServerMIB.setLastUpdated('202001170000Z')
if mibBuilder.loadTexts: hpicfAMPServerMIB.setOrganization('HP Networking')
hpicfAMPServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1))
hpicfAMPServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2))
hpicfArubaVPNObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3))
hpicfArubaVPNDefaultGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 4))
class HpicfArubaVPNType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("amp", 2), ("any", 3))

hpicfArubaVPNTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1), )
if mibBuilder.loadTexts: hpicfArubaVPNTable.setStatus('current')
hpicfArubaVPNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1), ).setIndexNames((0, "HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIndex"))
if mibBuilder.loadTexts: hpicfArubaVPNEntry.setStatus('current')
hpicfArubaVPNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 1), HpicfArubaVPNType())
if mibBuilder.loadTexts: hpicfArubaVPNIndex.setStatus('current')
hpicfArubaVPNRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfArubaVPNRowStatus.setStatus('current')
hpicfArubaVPNIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNIPType.setStatus('current')
hpicfArubaVPNIP = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNIP.setStatus('current')
hpicfArubaVPNTos = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNTos.setStatus('current')
hpicfArubaVPNTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNTtl.setStatus('current')
hpicfArubaVPNBkpIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 7), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNBkpIPType.setStatus('current')
hpicfArubaVPNBkpIP = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 8), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNBkpIP.setStatus('current')
hpicfArubaVPNGateway = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNGateway.setStatus('current')
hpicfAMPServerIPType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerIPType.setStatus('current')
hpicfAMPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerIP.setStatus('current')
hpicfAMPServerGroup = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerGroup.setStatus('current')
hpicfAMPServerFolder = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerFolder.setStatus('current')
hpicfAMPServerSecret = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerSecret.setStatus('current')
hpicfAMPServerConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configured", 1), ("notConfigured", 2))).clone('notConfigured')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerConfigStatus.setStatus('current')
hpicfAMPServerRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 7), Integer32()).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerRetryInterval.setStatus('current')
hpicfAMPServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1))
hpicfAMPServerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2))
hpicfAMPServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 1)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerMIBCompliance = hpicfAMPServerMIBCompliance.setStatus('deprecated')
hpicfAMPServerMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 2)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfDefaultGatewayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerMIBCompliance1 = hpicfAMPServerMIBCompliance1.setStatus('deprecated')
hpicfAMPServerMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 3)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNConfigGroup1"), ("HPICF-AMP-SERVER-MIB", "hpicfDefaultGatewayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerMIBCompliance2 = hpicfAMPServerMIBCompliance2.setStatus('current')
hpicfAMPServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 1)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerIP"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerFolder"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerSecret"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigStatus"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerRetryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerConfigGroup = hpicfAMPServerConfigGroup.setStatus('current')
hpicfArubaVPNConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 2)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNRowStatus"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIP"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTos"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTtl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfArubaVPNConfigGroup = hpicfArubaVPNConfigGroup.setStatus('deprecated')
hpicfDefaultGatewayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 3)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNGateway"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDefaultGatewayGroup = hpicfDefaultGatewayGroup.setStatus('current')
hpicfArubaVPNConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 4)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNRowStatus"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIP"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTos"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTtl"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNBkpIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNBkpIP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfArubaVPNConfigGroup1 = hpicfArubaVPNConfigGroup1.setStatus('current')
mibBuilder.exportSymbols("HPICF-AMP-SERVER-MIB", hpicfAMPServerMIBCompliance1=hpicfAMPServerMIBCompliance1, hpicfDefaultGatewayGroup=hpicfDefaultGatewayGroup, hpicfAMPServerMIBGroups=hpicfAMPServerMIBGroups, hpicfArubaVPNIP=hpicfArubaVPNIP, hpicfArubaVPNDefaultGateway=hpicfArubaVPNDefaultGateway, hpicfAMPServerMIBCompliance=hpicfAMPServerMIBCompliance, hpicfAMPServerObjects=hpicfAMPServerObjects, hpicfAMPServerConformance=hpicfAMPServerConformance, hpicfAMPServerMIBCompliance2=hpicfAMPServerMIBCompliance2, hpicfAMPServerRetryInterval=hpicfAMPServerRetryInterval, hpicfArubaVPNEntry=hpicfArubaVPNEntry, hpicfAMPServerConfigGroup=hpicfAMPServerConfigGroup, hpicfAMPServerFolder=hpicfAMPServerFolder, hpicfArubaVPNConfigGroup=hpicfArubaVPNConfigGroup, hpicfArubaVPNBkpIP=hpicfArubaVPNBkpIP, hpicfAMPServerIPType=hpicfAMPServerIPType, hpicfArubaVPNGateway=hpicfArubaVPNGateway, hpicfArubaVPNConfigGroup1=hpicfArubaVPNConfigGroup1, hpicfAMPServerIP=hpicfAMPServerIP, hpicfAMPServerMIBCompliances=hpicfAMPServerMIBCompliances, hpicfAMPServerGroup=hpicfAMPServerGroup, hpicfAMPServerConfigStatus=hpicfAMPServerConfigStatus, hpicfArubaVPNIPType=hpicfArubaVPNIPType, hpicfAMPServerMIB=hpicfAMPServerMIB, hpicfArubaVPNTos=hpicfArubaVPNTos, hpicfArubaVPNObjects=hpicfArubaVPNObjects, PYSNMP_MODULE_ID=hpicfAMPServerMIB, hpicfAMPServerSecret=hpicfAMPServerSecret, hpicfArubaVPNTable=hpicfArubaVPNTable, hpicfArubaVPNBkpIPType=hpicfArubaVPNBkpIPType, HpicfArubaVPNType=HpicfArubaVPNType, hpicfArubaVPNTtl=hpicfArubaVPNTtl, hpicfArubaVPNIndex=hpicfArubaVPNIndex, hpicfArubaVPNRowStatus=hpicfArubaVPNRowStatus)
