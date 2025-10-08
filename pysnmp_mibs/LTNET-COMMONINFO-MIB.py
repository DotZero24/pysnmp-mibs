#
# PySNMP MIB module LTNET-COMMONINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cdata/LTNET-COMMONINFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ltnetRoot, = mibBuilder.importSymbols("LTNET-ROOT", "ltnetRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ltnetCommonInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 33826, 3))
ltnetIpSimpleInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 33826, 3, 1))
ltnetSubJoinedInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 33826, 3, 4))
ltnetIpNetAddress = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltnetIpNetAddress.setStatus('mandatory')
ltnetIpMask = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltnetIpMask.setStatus('mandatory')
ltnetIpDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltnetIpDefaultGateway.setStatus('mandatory')
ltnetIpDns = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltnetIpDns.setStatus('optional')
ltnetIpPhysicalAddress = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltnetIpPhysicalAddress.setStatus('mandatory')
ltnetCommIdentifyNum = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 4, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltnetCommIdentifyNum.setStatus('optional')
ltnetCommonTime = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltnetCommonTime.setStatus('mandatory')
ltnetAlarmDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 33826, 3, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltnetAlarmDelayTime.setStatus('mandatory')
mibBuilder.exportSymbols("LTNET-COMMONINFO-MIB", ltnetCommonInfoGroup=ltnetCommonInfoGroup, ltnetIpMask=ltnetIpMask, ltnetIpSimpleInfo=ltnetIpSimpleInfo, ltnetSubJoinedInfo=ltnetSubJoinedInfo, ltnetIpDefaultGateway=ltnetIpDefaultGateway, ltnetAlarmDelayTime=ltnetAlarmDelayTime, ltnetIpDns=ltnetIpDns, ltnetIpNetAddress=ltnetIpNetAddress, ltnetCommIdentifyNum=ltnetCommIdentifyNum, ltnetIpPhysicalAddress=ltnetIpPhysicalAddress, ltnetCommonTime=ltnetCommonTime)
