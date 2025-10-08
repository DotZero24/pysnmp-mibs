#
# PySNMP MIB module OS-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-ACL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osAcl = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 3))
osAcl.setRevisions(('2014-05-27 00:00', '2008-01-08 00:00',))
if mibBuilder.loadTexts: osAcl.setLastUpdated('201405270000Z')
if mibBuilder.loadTexts: osAcl.setOrganization('MRV Communications, Inc.')
osAclGenConfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 3, 50))
osAclSupportGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 3, 100))
osAclConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 3, 101))
osAclMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 1))
osAclMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 2))
class SupportValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notSupported", 1), ("supported", 2))

class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3))
    namedValues = NamedValues(("valid", 2), ("invalid", 3))

class ParamType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("integer", 2), ("octetString", 3), ("displayString", 4), ("noParam", 5))

class ConditionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("eq", 2), ("neq", 3), ("lt", 4), ("gt", 5), ("le", 6), ("ge", 7), ("mask", 8), ("none", 9))

class VlanIdOrNone(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 4095), ValueRangeConstraint(5000, 5000), )
class PortIndexOrNone(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 4999), ValueRangeConstraint(5000, 5000), )
osAclTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1), )
if mibBuilder.loadTexts: osAclTable.setStatus('current')
osAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1), ).setIndexNames((0, "OS-ACL-MIB", "osAclName"))
if mibBuilder.loadTexts: osAclEntry.setStatus('current')
osAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19)))
if mibBuilder.loadTexts: osAclName.setStatus('current')
osAclType = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("extended", 2), ("flow", 3), ("protocols", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclType.setStatus('current')
osAclDefaultPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("deny", 2), ("permit", 3), ("notSupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclDefaultPolicy.setStatus('current')
osAclRemark = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRemark.setStatus('current')
osAclActive = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("notActive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osAclActive.setStatus('current')
osAclAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 6), AdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclAdminStatus.setStatus('current')
osAclRuleTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 3, 2), )
if mibBuilder.loadTexts: osAclRuleTable.setStatus('current')
osAclRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 3, 2, 1), ).setIndexNames((0, "OS-ACL-MIB", "osAclName"), (0, "OS-ACL-MIB", "osAclRuleIndex"))
if mibBuilder.loadTexts: osAclRuleEntry.setStatus('current')
osAclRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: osAclRuleIndex.setStatus('current')
osAclRuleAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("enable", 2), ("disable", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRuleAdminStatus.setStatus('current')
osAclRuleActionTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 3, 3), )
if mibBuilder.loadTexts: osAclRuleActionTable.setStatus('current')
osAclRuleActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1), ).setIndexNames((0, "OS-ACL-MIB", "osAclName"), (0, "OS-ACL-MIB", "osAclRuleIndex"), (0, "OS-ACL-MIB", "osAclRuleActionType"))
if mibBuilder.loadTexts: osAclRuleActionEntry.setStatus('current')
osAclRuleActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("osAclRuleActionDeny", 2), ("osAclRuleActionPermit", 3), ("osAclRuleActionLayer2Loopback", 4), ("osAclRuleActionTrapToCpu", 5), ("osAclRuleActionMirrorToCpu", 6), ("osAclRuleActionMirrorToAnalyser", 7), ("osAclRuleActionRedirectPort", 8), ("osAclRuleActionRedirectTag", 9), ("osAclRuleActionWithActionList", 10), ("osAclRuleActionMarkServiceLevel", 11), ("osAclRuleActionMarkDscp", 12), ("osAclRuleActionMarkVpt", 13), ("osAclRuleActionMarkByDiffserv", 14), ("osAclRuleActionMarkSlByDscp", 15), ("osAclRuleActionSwapVlan", 16), ("osAclRuleActionNestedVlan", 17), ("osAclRuleActionSwapToClientTag", 18), ("osAclRuleActionSwapToServerTag", 19), ("osAclRuleActionRedirectToCpu", 20))))
if mibBuilder.loadTexts: osAclRuleActionType.setStatus('current')
osAclRuleActionParamType = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 2), ParamType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRuleActionParamType.setStatus('current')
osAclRuleActionParamValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRuleActionParamValue.setStatus('current')
osAclRuleActionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 4), AdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRuleActionAdminStatus.setStatus('current')
osAclRuleClassTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 3, 4), )
if mibBuilder.loadTexts: osAclRuleClassTable.setStatus('current')
osAclRuleClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1), ).setIndexNames((0, "OS-ACL-MIB", "osAclName"), (0, "OS-ACL-MIB", "osAclRuleIndex"), (0, "OS-ACL-MIB", "osAclRuleClassType"), (0, "OS-ACL-MIB", "osAclRuleClassCondition"))
if mibBuilder.loadTexts: osAclRuleClassEntry.setStatus('current')
osAclRuleClassType = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("osAclRuleClassSrcIp", 2), ("osAclRuleClassDestIp", 3), ("osAclRuleClassSrcPort", 4), ("osAclRuleClassDestPort", 5), ("osAclRuleClassProtocol", 6), ("osAclRuleClassMacLookupResults", 7), ("osAclRuleClassMacDaType", 8), ("osAclRuleClassVpt", 9), ("osAclRuleClassClientVpt", 10), ("osAclRuleClassDscp", 11), ("osAclRuleClassMplsExp", 12), ("osAclRuleClassMplsExpTagged", 13), ("osAclRuleClassTag", 14), ("osAclRuleClassClientTag", 15), ("osAclRuleClassEthertype", 16), ("osAclRuleClassClientEthertype", 17), ("osAclRuleClassSrcMac", 18), ("osAclRuleClassDestMac", 19), ("osAclRuleClassSrcPhyPort", 20), ("osAclRuleClassArp", 21), ("osAclRuleClassTaggedArp", 22))))
if mibBuilder.loadTexts: osAclRuleClassType.setStatus('current')
osAclRuleClassCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 2), ConditionType())
if mibBuilder.loadTexts: osAclRuleClassCondition.setStatus('current')
osAclRuleClassParamType = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 3), ParamType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRuleClassParamType.setStatus('current')
osAclRuleClassParamValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRuleClassParamValue.setStatus('current')
osAclRuleClassAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 5), AdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclRuleClassAdminStatus.setStatus('current')
osAclBindingTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 3, 5), )
if mibBuilder.loadTexts: osAclBindingTable.setStatus('current')
osAclBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1), ).setIndexNames((0, "OS-ACL-MIB", "osAclBindingPort"), (0, "OS-ACL-MIB", "osAclBindingTag"))
if mibBuilder.loadTexts: osAclBindingEntry.setStatus('current')
osAclBindingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 1), PortIndexOrNone())
if mibBuilder.loadTexts: osAclBindingPort.setStatus('current')
osAclBindingTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 2), VlanIdOrNone())
if mibBuilder.loadTexts: osAclBindingTag.setStatus('current')
osAclBindingAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclBindingAclName.setStatus('current')
osAclBindingAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 4), AdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclBindingAdminStatus.setStatus('current')
osAclMatchingCounterTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 3, 6), )
if mibBuilder.loadTexts: osAclMatchingCounterTable.setStatus('current')
osAclMatchingCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1), ).setIndexNames((0, "OS-ACL-MIB", "osAclMatchingCounterIndex"))
if mibBuilder.loadTexts: osAclMatchingCounterEntry.setStatus('current')
osAclMatchingCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)))
if mibBuilder.loadTexts: osAclMatchingCounterIndex.setStatus('current')
osAclMatchingCounterPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osAclMatchingCounterPackets.setStatus('current')
osAclMatchingCounterBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osAclMatchingCounterBytes.setStatus('current')
osAclMatchingCounterAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 98), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nothing", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclMatchingCounterAdminStatus.setStatus('current')
osAclMatchingCounterOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 99), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osAclMatchingCounterOperStatus.setStatus('current')
osAclGenConfExtendedProfile = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 3, 50, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 0), ("normal", 1), ("doubleTag", 2), ("mplsExp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAclGenConfExtendedProfile.setStatus('current')
osAclMibSupport = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 3, 100, 1), SupportValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osAclMibSupport.setStatus('current')
osAclMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 1, 1)).setObjects(("OS-ACL-MIB", "osAclMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osAclMIBCompliance = osAclMIBCompliance.setStatus('current')
osAclMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 2, 1)).setObjects(("OS-ACL-MIB", "osAclType"), ("OS-ACL-MIB", "osAclDefaultPolicy"), ("OS-ACL-MIB", "osAclRemark"), ("OS-ACL-MIB", "osAclActive"), ("OS-ACL-MIB", "osAclAdminStatus"), ("OS-ACL-MIB", "osAclRuleAdminStatus"), ("OS-ACL-MIB", "osAclRuleActionParamType"), ("OS-ACL-MIB", "osAclRuleActionParamValue"), ("OS-ACL-MIB", "osAclRuleActionAdminStatus"), ("OS-ACL-MIB", "osAclRuleClassParamType"), ("OS-ACL-MIB", "osAclRuleClassParamValue"), ("OS-ACL-MIB", "osAclRuleClassAdminStatus"), ("OS-ACL-MIB", "osAclBindingAclName"), ("OS-ACL-MIB", "osAclBindingAdminStatus"), ("OS-ACL-MIB", "osAclMatchingCounterPackets"), ("OS-ACL-MIB", "osAclMatchingCounterBytes"), ("OS-ACL-MIB", "osAclMatchingCounterAdminStatus"), ("OS-ACL-MIB", "osAclMatchingCounterOperStatus"), ("OS-ACL-MIB", "osAclMibSupport"), ("OS-ACL-MIB", "osAclGenConfExtendedProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osAclMandatoryGroup = osAclMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OS-ACL-MIB", osAclMIBGroups=osAclMIBGroups, osAclRuleActionParamValue=osAclRuleActionParamValue, osAclRuleClassEntry=osAclRuleClassEntry, osAclMIBCompliances=osAclMIBCompliances, osAclRuleActionAdminStatus=osAclRuleActionAdminStatus, PortIndexOrNone=PortIndexOrNone, osAclRemark=osAclRemark, osAclRuleActionParamType=osAclRuleActionParamType, osAclSupportGrp=osAclSupportGrp, osAclGenConfExtendedProfile=osAclGenConfExtendedProfile, osAclMIBCompliance=osAclMIBCompliance, osAclMandatoryGroup=osAclMandatoryGroup, osAclGenConfGrp=osAclGenConfGrp, ParamType=ParamType, osAclMatchingCounterPackets=osAclMatchingCounterPackets, osAclRuleClassCondition=osAclRuleClassCondition, osAclMatchingCounterTable=osAclMatchingCounterTable, osAclRuleIndex=osAclRuleIndex, osAclRuleActionEntry=osAclRuleActionEntry, osAclMatchingCounterIndex=osAclMatchingCounterIndex, osAclRuleTable=osAclRuleTable, osAclRuleClassTable=osAclRuleClassTable, osAclBindingTable=osAclBindingTable, osAcl=osAcl, osAclMibSupport=osAclMibSupport, osAclRuleClassParamValue=osAclRuleClassParamValue, osAclTable=osAclTable, osAclConformance=osAclConformance, osAclMatchingCounterBytes=osAclMatchingCounterBytes, osAclRuleEntry=osAclRuleEntry, osAclEntry=osAclEntry, osAclName=osAclName, VlanIdOrNone=VlanIdOrNone, osAclRuleClassParamType=osAclRuleClassParamType, ConditionType=ConditionType, osAclMatchingCounterOperStatus=osAclMatchingCounterOperStatus, osAclDefaultPolicy=osAclDefaultPolicy, PYSNMP_MODULE_ID=osAcl, osAclRuleActionType=osAclRuleActionType, osAclRuleClassAdminStatus=osAclRuleClassAdminStatus, osAclBindingPort=osAclBindingPort, osAclBindingAdminStatus=osAclBindingAdminStatus, osAclMatchingCounterAdminStatus=osAclMatchingCounterAdminStatus, osAclType=osAclType, osAclBindingAclName=osAclBindingAclName, osAclRuleClassType=osAclRuleClassType, osAclBindingEntry=osAclBindingEntry, osAclMatchingCounterEntry=osAclMatchingCounterEntry, SupportValue=SupportValue, osAclAdminStatus=osAclAdminStatus, osAclRuleActionTable=osAclRuleActionTable, osAclBindingTag=osAclBindingTag, osAclRuleAdminStatus=osAclRuleAdminStatus, AdminStatus=AdminStatus, osAclActive=osAclActive)
