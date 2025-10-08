#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-HARDWARE-IP-VERIFY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHardwareIpVerifyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 804))
ciscoHardwareIpVerifyMIB.setRevisions(('2012-09-04 00:00',))
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setOrganization('Cisco Systems, Inc.')
ciscoHardwareIpVerifyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 0))
ciscoHardwareIpVerifyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 1))
ciscoHardwareIpVerifyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2))
chivIpVerifyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1), )
if mibBuilder.loadTexts: chivIpVerifyTable.setStatus('current')
chivIpVerifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1), ).setIndexNames((0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckIpType"), (0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckTypeName"))
if mibBuilder.loadTexts: chivIpVerifyEntry.setStatus('current')
chivIpVerifyCheckIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: chivIpVerifyCheckIpType.setStatus('current')
chivIpVerifyCheckTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("addressSrcBroadcast", 1), ("addressSrcMulticast", 2), ("addressDestZero", 3), ("addressIdentical", 4), ("addressSrcReserved", 5), ("addressClassE", 6), ("checksum", 7), ("protocol", 8), ("fragment", 9), ("lengthMinimum", 10), ("lengthConsistent", 11), ("lengthMaximumFragment", 12), ("lengthMaximumUdp", 13), ("lengthMaximumTcp", 14), ("tcpFlags", 15), ("tcpTinyFlags", 16), ("version", 17))))
if mibBuilder.loadTexts: chivIpVerifyCheckTypeName.setStatus('current')
chivIpVerifyCheckStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chivIpVerifyCheckStatus.setStatus('current')
chivIpVerifyPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chivIpVerifyPacketsDropped.setStatus('current')
ciscoHardwareIpVerifyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1))
ciscoHardwareIpVerifyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2))
ciscoHardwareIpVerifyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1, 1)).setObjects(("CISCO-HARDWARE-IP-VERIFY-MIB", "ciscoHardwareIpVerifyMIBStatisticGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHardwareIpVerifyMIBCompliance = ciscoHardwareIpVerifyMIBCompliance.setStatus('current')
ciscoHardwareIpVerifyMIBStatisticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2, 1)).setObjects(("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckStatus"), ("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyPacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHardwareIpVerifyMIBStatisticGroup = ciscoHardwareIpVerifyMIBStatisticGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-MIB", ciscoHardwareIpVerifyMIB=ciscoHardwareIpVerifyMIB, PYSNMP_MODULE_ID=ciscoHardwareIpVerifyMIB, chivIpVerifyEntry=chivIpVerifyEntry, chivIpVerifyCheckStatus=chivIpVerifyCheckStatus, ciscoHardwareIpVerifyMIBCompliances=ciscoHardwareIpVerifyMIBCompliances, ciscoHardwareIpVerifyMIBObjects=ciscoHardwareIpVerifyMIBObjects, chivIpVerifyTable=chivIpVerifyTable, ciscoHardwareIpVerifyMIBNotifs=ciscoHardwareIpVerifyMIBNotifs, ciscoHardwareIpVerifyMIBStatisticGroup=ciscoHardwareIpVerifyMIBStatisticGroup, chivIpVerifyPacketsDropped=chivIpVerifyPacketsDropped, ciscoHardwareIpVerifyMIBCompliance=ciscoHardwareIpVerifyMIBCompliance, chivIpVerifyCheckIpType=chivIpVerifyCheckIpType, ciscoHardwareIpVerifyMIBConform=ciscoHardwareIpVerifyMIBConform, ciscoHardwareIpVerifyMIBGroups=ciscoHardwareIpVerifyMIBGroups, chivIpVerifyCheckTypeName=chivIpVerifyCheckTypeName)
