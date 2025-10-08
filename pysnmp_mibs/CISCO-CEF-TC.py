#
# PySNMP MIB module CISCO-CEF-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-CEF-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCefTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 493))
ciscoCefTextualConventions.setRevisions(('2005-09-30 00:00',))
if mibBuilder.loadTexts: ciscoCefTextualConventions.setLastUpdated('200509300000Z')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setOrganization('Cisco Systems, Inc.')
class CefIpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class CefAdjLinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("mpls", 3), ("raw", 4), ("unknown", 5))

class CefAdjacencySource(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("atom", 0), ("linkRawAdj", 1), ("ipPseudowireAdj", 2), ("arp", 3), ("p2pAdj", 4), ("frMap", 5), ("atmPVC", 6), ("atmSVC", 7), ("atmTVC", 8), ("nbma", 9), ("mpoa", 10), ("atmBundle", 11), ("lec", 12), ("nhrp", 13), ("ipv6ND", 14), ("cmcc", 15), ("ipv6SixtoFourTunnel", 16), ("ipv6IsaTapTunnel", 17), ("ipv6AutoTunnel", 18), ("fibLc", 19), ("virtual", 20), ("multicast", 21), ("unknown", 22))

class CefPathType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("receive", 1), ("connectedPrefix", 2), ("attachedPrefix", 3), ("attachedHost", 4), ("attachedNexthop", 5), ("recursiveNexthop", 6), ("adjacencyPrefix", 7), ("specialPrefix", 8), ("unknown", 9))

class CefPrefixSearchState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("running", 1), ("matchFound", 2), ("noMatchFound", 3))

class CefForwardingElementSpecialType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("illegal", 1), ("punt", 2), ("drop", 3), ("discard", 4), ("null", 5), ("glean", 6), ("unresolved", 7), ("noRoute", 8), ("none", 9))

class CefMplsLabelList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CefAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CefOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class CefFailureReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("mallocFailure", 2), ("hwFailure", 3), ("keepaliveFailure", 4), ("noMsgBuffer", 5), ("invalidMsgSize", 6), ("internalError", 7))

class CefCCType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("lcDetect", 1), ("scanFibLcRp", 2), ("scanFibRpLc", 3), ("scanRibFib", 4), ("scanFibRib", 5), ("scanFibHwSw", 6), ("scanFibSwHw", 7), ("fullScanRibFib", 8), ("fullScanFibRib", 9), ("fullScanFibRpLc", 10), ("fullScanFibLcRp", 11), ("fullScanFibHwSw", 12), ("fullScanFibSwHw", 13))

class CefCCAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccActionStart", 1), ("ccActionAbort", 2), ("ccActionNone", 3))

class CefCCStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccStatusIdle", 1), ("ccStatusRunning", 2), ("ccStatusDone", 3))

mibBuilder.exportSymbols("CISCO-CEF-TC", CefOperStatus=CefOperStatus, CefCCType=CefCCType, ciscoCefTextualConventions=ciscoCefTextualConventions, CefAdjLinkType=CefAdjLinkType, CefCCStatus=CefCCStatus, CefIpVersion=CefIpVersion, CefPrefixSearchState=CefPrefixSearchState, CefForwardingElementSpecialType=CefForwardingElementSpecialType, CefFailureReason=CefFailureReason, CefAdjacencySource=CefAdjacencySource, CefMplsLabelList=CefMplsLabelList, CefCCAction=CefCCAction, CefPathType=CefPathType, CefAdminStatus=CefAdminStatus, PYSNMP_MODULE_ID=ciscoCefTextualConventions)
