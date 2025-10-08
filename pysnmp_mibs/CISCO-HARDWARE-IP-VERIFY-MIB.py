#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-HARDWARE-IP-VERIFY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-MIB", chivIpVerifyCheckTypeName=chivIpVerifyCheckTypeName, chivIpVerifyTable=chivIpVerifyTable, chivIpVerifyEntry=chivIpVerifyEntry, ciscoHardwareIpVerifyMIBObjects=ciscoHardwareIpVerifyMIBObjects, PYSNMP_MODULE_ID=ciscoHardwareIpVerifyMIB, chivIpVerifyCheckStatus=chivIpVerifyCheckStatus, ciscoHardwareIpVerifyMIBCompliances=ciscoHardwareIpVerifyMIBCompliances, chivIpVerifyPacketsDropped=chivIpVerifyPacketsDropped, ciscoHardwareIpVerifyMIBNotifs=ciscoHardwareIpVerifyMIBNotifs, ciscoHardwareIpVerifyMIBConform=ciscoHardwareIpVerifyMIBConform, ciscoHardwareIpVerifyMIBGroups=ciscoHardwareIpVerifyMIBGroups, ciscoHardwareIpVerifyMIBCompliance=ciscoHardwareIpVerifyMIBCompliance, chivIpVerifyCheckIpType=chivIpVerifyCheckIpType, ciscoHardwareIpVerifyMIBStatisticGroup=ciscoHardwareIpVerifyMIBStatisticGroup, ciscoHardwareIpVerifyMIB=ciscoHardwareIpVerifyMIB)
