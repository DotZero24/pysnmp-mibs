#
# PySNMP MIB module CISCO-VOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VOA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
OpticalIfDirection, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalIfDirection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
ciscoVoaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 262))
ciscoVoaMIB.setRevisions(('2002-05-07 00:00',))
if mibBuilder.loadTexts: ciscoVoaMIB.setLastUpdated('200205070000Z')
if mibBuilder.loadTexts: ciscoVoaMIB.setOrganization('Cisco Systems, Inc.')
class OpticalPowerInDbm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-400, 250), ValueRangeConstraint(-1000, -1000), )
class OpticalAttenInDb(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 400)

cVoaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1))
cVoaBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1))
cVoaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1), )
if mibBuilder.loadTexts: cVoaTable.setStatus('current')
cVoaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-VOA-MIB", "cVoaDirection"))
if mibBuilder.loadTexts: cVoaEntry.setStatus('current')
cVoaDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 1), OpticalIfDirection())
if mibBuilder.loadTexts: cVoaDirection.setStatus('current')
cVoaAttenuationControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("automatic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuationControlMode.setStatus('current')
cVoaAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 3), OpticalAttenInDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuation.setStatus('current')
cVoaAttenuationLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVoaAttenuationLastChange.setStatus('current')
cVoaDesiredPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 5), OpticalPowerInDbm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaDesiredPower.setStatus('current')
cVoaMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3))
cVoaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1))
cVoaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2))
cVoaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1, 1)).setObjects(("CISCO-VOA-MIB", "cVoaMIBBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBCompliance = cVoaMIBCompliance.setStatus('current')
cVoaMIBBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2, 1)).setObjects(("CISCO-VOA-MIB", "cVoaAttenuationControlMode"), ("CISCO-VOA-MIB", "cVoaAttenuation"), ("CISCO-VOA-MIB", "cVoaAttenuationLastChange"), ("CISCO-VOA-MIB", "cVoaDesiredPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBBaseGroup = cVoaMIBBaseGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOA-MIB", OpticalPowerInDbm=OpticalPowerInDbm, PYSNMP_MODULE_ID=ciscoVoaMIB, cVoaAttenuation=cVoaAttenuation, cVoaMIBCompliances=cVoaMIBCompliances, cVoaMIBBaseGroup=cVoaMIBBaseGroup, OpticalAttenInDb=OpticalAttenInDb, cVoaMIBCompliance=cVoaMIBCompliance, cVoaDesiredPower=cVoaDesiredPower, cVoaBaseGroup=cVoaBaseGroup, cVoaMIBObjects=cVoaMIBObjects, cVoaAttenuationControlMode=cVoaAttenuationControlMode, cVoaTable=cVoaTable, cVoaEntry=cVoaEntry, cVoaMIBGroups=cVoaMIBGroups, cVoaAttenuationLastChange=cVoaAttenuationLastChange, cVoaDirection=cVoaDirection, ciscoVoaMIB=ciscoVoaMIB, cVoaMIBConformance=cVoaMIBConformance)
