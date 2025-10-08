#
# PySNMP MIB module ENTERASYS-JUMBO-ETHERNET-FRAME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-JUMBO-ETHERNET-FRAME-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysJumboEthernetFrameMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34))
etsysJumboEthernetFrameMIB.setRevisions(('2003-01-24 21:26', '2002-12-20 21:56',))
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setLastUpdated('200301242126Z')
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setOrganization('Enterasys Networks, Inc')
etsysJumboEthernetFrame = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1))
etsysJumboEnetFrameControl = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1))
etsysJumboEnetFrameTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: etsysJumboEnetFrameTable.setStatus('current')
etsysJumboEnetFrameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysJumboEnetFrameEntry.setStatus('current')
etsysJumboEnetFrameEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysJumboEnetFrameEnable.setStatus('obsolete')
etsysJumboEnetFrameMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysJumboEnetFrameMtu.setStatus('current')
etsysJumboEnetFrameAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysJumboEnetFrameAdminStatus.setStatus('current')
etsysJumboEnetFrameOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysJumboEnetFrameOperStatus.setStatus('current')
etsysJumboEnetFrameConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2))
etsysJumboEnetFrameGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1))
etsysJumboEnetFrameCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2))
etsysJumboEnetFrameControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 1)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameEnable"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameControlGroup = etsysJumboEnetFrameControlGroup.setStatus('obsolete')
etsysJumboEnetFrameControlGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 2)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameAdminStatus"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameControlGroup2 = etsysJumboEnetFrameControlGroup2.setStatus('current')
etsysJumboEnetFrameCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 1)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameCompliance = etsysJumboEnetFrameCompliance.setStatus('obsolete')
etsysJumboEnetFrameCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 2)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameControlGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameCompliance2 = etsysJumboEnetFrameCompliance2.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", etsysJumboEnetFrameOperStatus=etsysJumboEnetFrameOperStatus, etsysJumboEnetFrameGroups=etsysJumboEnetFrameGroups, etsysJumboEnetFrameAdminStatus=etsysJumboEnetFrameAdminStatus, PYSNMP_MODULE_ID=etsysJumboEthernetFrameMIB, etsysJumboEnetFrameTable=etsysJumboEnetFrameTable, etsysJumboEnetFrameConformance=etsysJumboEnetFrameConformance, etsysJumboEnetFrameControlGroup=etsysJumboEnetFrameControlGroup, etsysJumboEnetFrameCompliances=etsysJumboEnetFrameCompliances, etsysJumboEnetFrameControl=etsysJumboEnetFrameControl, etsysJumboEthernetFrameMIB=etsysJumboEthernetFrameMIB, etsysJumboEnetFrameEnable=etsysJumboEnetFrameEnable, etsysJumboEnetFrameMtu=etsysJumboEnetFrameMtu, etsysJumboEnetFrameCompliance2=etsysJumboEnetFrameCompliance2, etsysJumboEnetFrameCompliance=etsysJumboEnetFrameCompliance, etsysJumboEnetFrameEntry=etsysJumboEnetFrameEntry, etsysJumboEnetFrameControlGroup2=etsysJumboEnetFrameControlGroup2, etsysJumboEthernetFrame=etsysJumboEthernetFrame)
