#
# PySNMP MIB module HP-SWITCH-ERROR-MSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-SWITCH-ERROR-MSG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
hpSwitchErrorMsgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68))
hpSwitchErrorMsgMIB.setRevisions(('2009-04-06 00:00',))
if mibBuilder.loadTexts: hpSwitchErrorMsgMIB.setLastUpdated('200904060000Z')
if mibBuilder.loadTexts: hpSwitchErrorMsgMIB.setOrganization('HP Networking')
hpSwitchErrorMsgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1))
hpSwitchErrorMsgTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1), )
if mibBuilder.loadTexts: hpSwitchErrorMsgTable.setStatus('current')
hpSwitchErrorMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1), ).setIndexNames((0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorEntityType"), (0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorEntityHandle"), (0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorSnmpSeqCode"))
if mibBuilder.loadTexts: hpSwitchErrorMsgEntry.setStatus('current')
hpSwitchErrorEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("others", 1), ("cliSession", 2), ("webSession", 3), ("ipV4Address", 4), ("ipV6Address", 5), ("oaApplication", 6))))
if mibBuilder.loadTexts: hpSwitchErrorEntityType.setStatus('current')
hpSwitchErrorEntityHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 96)))
if mibBuilder.loadTexts: hpSwitchErrorEntityHandle.setStatus('current')
hpSwitchErrorSnmpSeqCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpSwitchErrorSnmpSeqCode.setStatus('current')
hpSwitchErrorTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchErrorTime.setStatus('current')
hpSwitchErrorFailedOID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchErrorFailedOID.setStatus('current')
hpSwitchEntityErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchEntityErrorMsg.setStatus('current')
hpSwitchSnmpErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchSnmpErrorCode.setStatus('current')
hpSwitchErrorMsgMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2))
hpSwitchErrorMsgMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 1))
hpSwitchErrorMsgMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 2))
hpSwitchErrorMsgMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 1, 1)).setObjects(("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorMsgMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchErrorMsgMIBCompliance = hpSwitchErrorMsgMIBCompliance.setStatus('current')
hpSwitchErrorMsgMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 2, 1)).setObjects(("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorTime"), ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorFailedOID"), ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchEntityErrorMsg"), ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchSnmpErrorCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchErrorMsgMIBGroup = hpSwitchErrorMsgMIBGroup.setStatus('current')
mibBuilder.exportSymbols("HP-SWITCH-ERROR-MSG-MIB", PYSNMP_MODULE_ID=hpSwitchErrorMsgMIB, hpSwitchErrorMsgMIBCompliances=hpSwitchErrorMsgMIBCompliances, hpSwitchErrorEntityHandle=hpSwitchErrorEntityHandle, hpSwitchEntityErrorMsg=hpSwitchEntityErrorMsg, hpSwitchErrorMsgMIBGroups=hpSwitchErrorMsgMIBGroups, hpSwitchErrorSnmpSeqCode=hpSwitchErrorSnmpSeqCode, hpSwitchErrorMsgEntry=hpSwitchErrorMsgEntry, hpSwitchErrorMsgMIB=hpSwitchErrorMsgMIB, hpSwitchErrorMsgMIBGroup=hpSwitchErrorMsgMIBGroup, hpSwitchErrorTime=hpSwitchErrorTime, hpSwitchErrorMsgTable=hpSwitchErrorMsgTable, hpSwitchErrorMsgMIBCompliance=hpSwitchErrorMsgMIBCompliance, hpSwitchErrorMsgObjects=hpSwitchErrorMsgObjects, hpSwitchErrorFailedOID=hpSwitchErrorFailedOID, hpSwitchErrorEntityType=hpSwitchErrorEntityType, hpSwitchSnmpErrorCode=hpSwitchSnmpErrorCode, hpSwitchErrorMsgMIBConformance=hpSwitchErrorMsgMIBConformance)
