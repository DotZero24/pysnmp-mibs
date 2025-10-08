#
# PySNMP MIB module ADTRAN-GENERIC-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-GENERIC-LLDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adTrapInformSeqNum, = mibBuilder.importSymbols("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum")
adGenLldp, adGenLldpID = mibBuilder.importSymbols("ADTRAN-SHARED-CND-SYSTEM-MIB", "adGenLldp", "adGenLldpID")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
adGenLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 46, 1))
adGenLldpMIB.setRevisions(('2013-09-18 00:00', '2011-10-18 00:00',))
if mibBuilder.loadTexts: adGenLldpMIB.setLastUpdated('201309180000Z')
if mibBuilder.loadTexts: adGenLldpMIB.setOrganization('Adtran, Inc.')
adGenLldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1))
adGenLldpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 2))
adGenLldpLocalSystemData = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 3))
adGenLldpRemoteSystemData = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4))
adGenLldpExtentsions = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 5))
adGenLldpEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6))
adGenLldpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6, 0))
class AdGenChassisIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class AdGenChassisId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class AdGenPortIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class AdGenPortId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class AdGenManAddrIfSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3))

class AdGenManAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class AdGenSystemCapabilitiesMap(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("other", 0), ("repeater", 1), ("bridge", 2), ("wlanAccessPoint", 3), ("router", 4), ("telephone", 5), ("docsisCableDevice", 6), ("stationOnly", 7))

adGenLldpProvTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1, 1), )
if mibBuilder.loadTexts: adGenLldpProvTable.setStatus('current')
adGenLldpProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenLldpProvEntry.setStatus('current')
adGenLldpConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenLldpConfigState.setStatus('current')
adGenLldpRemSysDataTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1), )
if mibBuilder.loadTexts: adGenLldpRemSysDataTable.setStatus('current')
adGenLldpRemSysDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenLldpRemSysDataEntry.setStatus('current')
adGenLldpRemChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 1), AdGenChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemChassisIdSubtype.setStatus('current')
adGenLldpRemChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 2), AdGenChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemChassisId.setStatus('current')
adGenLldpRemPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 3), AdGenPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemPortIdSubtype.setStatus('current')
adGenLldpRemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 4), AdGenPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemPortId.setStatus('current')
adGenLldpRemPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemPortDesc.setStatus('current')
adGenLldpRemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemSysName.setStatus('current')
adGenLldpRemSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemSysDesc.setStatus('current')
adGenLldpRemSysCapSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 8), AdGenSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemSysCapSupported.setStatus('current')
adGenLldpRemSysCapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 9), AdGenSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemSysCapEnabled.setStatus('current')
adGenLldpRemManAddrSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 10), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemManAddrSubtype.setStatus('current')
adGenLldpRemManAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 11), AdGenManAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemManAddr.setStatus('current')
adGenLldpRemManAddrIfSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 12), AdGenManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemManAddrIfSubtype.setStatus('current')
adGenLldpRemManAddrIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 4, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenLldpRemManAddrIfId.setStatus('current')
adGenLldpPeerRemoved = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6, 0, 1)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenLldpPeerRemoved.setStatus('current')
adGenLldpPeerAdded = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 70, 46, 6, 0, 2)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenLldpPeerAdded.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-GENERIC-LLDP-MIB", AdGenManAddrIfSubtype=AdGenManAddrIfSubtype, adGenLldpPeerAdded=adGenLldpPeerAdded, AdGenSystemCapabilitiesMap=AdGenSystemCapabilitiesMap, AdGenChassisId=AdGenChassisId, adGenLldpRemManAddr=adGenLldpRemManAddr, adGenLldpProvEntry=adGenLldpProvEntry, adGenLldpRemPortDesc=adGenLldpRemPortDesc, adGenLldpRemChassisIdSubtype=adGenLldpRemChassisIdSubtype, adGenLldpRemManAddrIfSubtype=adGenLldpRemManAddrIfSubtype, AdGenPortIdSubtype=AdGenPortIdSubtype, adGenLldpEvents=adGenLldpEvents, adGenLldpRemSysCapEnabled=adGenLldpRemSysCapEnabled, adGenLldpConfiguration=adGenLldpConfiguration, AdGenPortId=AdGenPortId, adGenLldpExtentsions=adGenLldpExtentsions, adGenLldpRemSysName=adGenLldpRemSysName, adGenLldpRemSysDesc=adGenLldpRemSysDesc, adGenLldpRemManAddrIfId=adGenLldpRemManAddrIfId, AdGenManAddress=AdGenManAddress, adGenLldpPeerRemoved=adGenLldpPeerRemoved, adGenLldpStatistics=adGenLldpStatistics, adGenLldpRemSysDataTable=adGenLldpRemSysDataTable, adGenLldpLocalSystemData=adGenLldpLocalSystemData, adGenLldpRemPortIdSubtype=adGenLldpRemPortIdSubtype, adGenLldpRemoteSystemData=adGenLldpRemoteSystemData, adGenLldpTraps=adGenLldpTraps, adGenLldpRemPortId=adGenLldpRemPortId, adGenLldpRemManAddrSubtype=adGenLldpRemManAddrSubtype, adGenLldpProvTable=adGenLldpProvTable, adGenLldpMIB=adGenLldpMIB, adGenLldpRemSysDataEntry=adGenLldpRemSysDataEntry, AdGenChassisIdSubtype=AdGenChassisIdSubtype, PYSNMP_MODULE_ID=adGenLldpMIB, adGenLldpRemSysCapSupported=adGenLldpRemSysCapSupported, adGenLldpRemChassisId=adGenLldpRemChassisId, adGenLldpConfigState=adGenLldpConfigState)
