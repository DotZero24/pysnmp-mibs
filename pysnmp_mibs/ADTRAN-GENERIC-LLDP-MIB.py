#
# PySNMP MIB module ADTRAN-GENERIC-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-GENERIC-LLDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adTrapInformSeqNum, = mibBuilder.importSymbols("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum")
adGenLldp, adGenLldpID = mibBuilder.importSymbols("ADTRAN-SHARED-CND-SYSTEM-MIB", "adGenLldp", "adGenLldpID")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-GENERIC-LLDP-MIB", adGenLldpRemManAddrIfSubtype=adGenLldpRemManAddrIfSubtype, AdGenManAddrIfSubtype=AdGenManAddrIfSubtype, adGenLldpRemoteSystemData=adGenLldpRemoteSystemData, adGenLldpProvEntry=adGenLldpProvEntry, AdGenChassisIdSubtype=AdGenChassisIdSubtype, adGenLldpRemPortDesc=adGenLldpRemPortDesc, adGenLldpPeerRemoved=adGenLldpPeerRemoved, adGenLldpEvents=adGenLldpEvents, adGenLldpRemChassisId=adGenLldpRemChassisId, adGenLldpRemChassisIdSubtype=adGenLldpRemChassisIdSubtype, adGenLldpStatistics=adGenLldpStatistics, adGenLldpExtentsions=adGenLldpExtentsions, adGenLldpRemSysName=adGenLldpRemSysName, PYSNMP_MODULE_ID=adGenLldpMIB, AdGenPortIdSubtype=AdGenPortIdSubtype, AdGenManAddress=AdGenManAddress, AdGenPortId=AdGenPortId, adGenLldpRemSysDataTable=adGenLldpRemSysDataTable, adGenLldpRemManAddrSubtype=adGenLldpRemManAddrSubtype, adGenLldpPeerAdded=adGenLldpPeerAdded, adGenLldpTraps=adGenLldpTraps, AdGenSystemCapabilitiesMap=AdGenSystemCapabilitiesMap, adGenLldpRemManAddr=adGenLldpRemManAddr, adGenLldpRemPortId=adGenLldpRemPortId, adGenLldpConfiguration=adGenLldpConfiguration, adGenLldpRemSysCapEnabled=adGenLldpRemSysCapEnabled, adGenLldpRemPortIdSubtype=adGenLldpRemPortIdSubtype, adGenLldpLocalSystemData=adGenLldpLocalSystemData, adGenLldpRemSysCapSupported=adGenLldpRemSysCapSupported, AdGenChassisId=AdGenChassisId, adGenLldpMIB=adGenLldpMIB, adGenLldpProvTable=adGenLldpProvTable, adGenLldpRemManAddrIfId=adGenLldpRemManAddrIfId, adGenLldpRemSysDesc=adGenLldpRemSysDesc, adGenLldpConfigState=adGenLldpConfigState, adGenLldpRemSysDataEntry=adGenLldpRemSysDataEntry)
