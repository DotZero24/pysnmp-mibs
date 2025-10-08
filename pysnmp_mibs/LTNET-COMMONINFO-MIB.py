#
# PySNMP MIB module LTNET-COMMONINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cdata/LTNET-COMMONINFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ltnetRoot, = mibBuilder.importSymbols("LTNET-ROOT", "ltnetRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LTNET-COMMONINFO-MIB", ltnetIpDns=ltnetIpDns, ltnetIpSimpleInfo=ltnetIpSimpleInfo, ltnetIpNetAddress=ltnetIpNetAddress, ltnetIpPhysicalAddress=ltnetIpPhysicalAddress, ltnetAlarmDelayTime=ltnetAlarmDelayTime, ltnetCommIdentifyNum=ltnetCommIdentifyNum, ltnetSubJoinedInfo=ltnetSubJoinedInfo, ltnetCommonInfoGroup=ltnetCommonInfoGroup, ltnetIpDefaultGateway=ltnetIpDefaultGateway, ltnetCommonTime=ltnetCommonTime, ltnetIpMask=ltnetIpMask)
