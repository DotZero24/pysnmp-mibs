#
# PySNMP MIB module ENTERASYS-DOT3-LLDP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-DOT3-LLDP-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
lldpV2LocPortIfIndex, = mibBuilder.importSymbols("LLDP-V2-MIB", "lldpV2LocPortIfIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysDot3LldpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104))
etsysDot3LldpExtMIB.setRevisions(('2013-08-28 17:51',))
if mibBuilder.loadTexts: etsysDot3LldpExtMIB.setLastUpdated('201308281751Z')
if mibBuilder.loadTexts: etsysDot3LldpExtMIB.setOrganization('Enterasys Networks, Inc')
etsysDot3LldpExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1))
etsysDot3LldpExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2))
etsysDot3LldpExtEeePort = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2))
etsysDot3LldpExtEeeConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1), )
if mibBuilder.loadTexts: etsysDot3LldpExtEeeConfigTable.setStatus('current')
etsysDot3LldpExtEeeConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: etsysDot3LldpExtEeeConfigEntry.setStatus('current')
etsysDot3LldpExtEeeAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3LldpExtEeeAdminStatus.setStatus('current')
etsysDot3LldpExtEeeOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDot3LldpExtEeeOperStatus.setStatus('current')
etsysDot3LldpExtEeeTLVTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3LldpExtEeeTLVTxEnable.setStatus('current')
etsysDot3LldpExtEeeLocRxTwSys = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3LldpExtEeeLocRxTwSys.setStatus('current')
etsysDot3LldpExtEeeLocFbTwSys = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3LldpExtEeeLocFbTwSys.setStatus('current')
etsysDot3LldpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 1))
etsysDot3LldpExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 2))
etsysDot3LldpExtEeePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 1, 1)).setObjects(("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeAdminStatus"), ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeOperStatus"), ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeTLVTxEnable"), ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeLocRxTwSys"), ("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeeLocFbTwSys"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3LldpExtEeePortGroup = etsysDot3LldpExtEeePortGroup.setStatus('current')
etsysDot3LldpExtEeePortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 104, 2, 2, 1)).setObjects(("ENTERASYS-DOT3-LLDP-EXT-MIB", "etsysDot3LldpExtEeePortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3LldpExtEeePortCompliance = etsysDot3LldpExtEeePortCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-DOT3-LLDP-EXT-MIB", etsysDot3LldpExtConformance=etsysDot3LldpExtConformance, PYSNMP_MODULE_ID=etsysDot3LldpExtMIB, etsysDot3LldpExtEeeLocRxTwSys=etsysDot3LldpExtEeeLocRxTwSys, etsysDot3LldpExtGroups=etsysDot3LldpExtGroups, etsysDot3LldpExtEeePortGroup=etsysDot3LldpExtEeePortGroup, etsysDot3LldpExtEeeTLVTxEnable=etsysDot3LldpExtEeeTLVTxEnable, etsysDot3LldpExtMIB=etsysDot3LldpExtMIB, etsysDot3LldpExtObjects=etsysDot3LldpExtObjects, etsysDot3LldpExtEeeAdminStatus=etsysDot3LldpExtEeeAdminStatus, etsysDot3LldpExtEeeConfigEntry=etsysDot3LldpExtEeeConfigEntry, etsysDot3LldpExtEeePortCompliance=etsysDot3LldpExtEeePortCompliance, etsysDot3LldpExtEeeConfigTable=etsysDot3LldpExtEeeConfigTable, etsysDot3LldpExtEeePort=etsysDot3LldpExtEeePort, etsysDot3LldpExtEeeLocFbTwSys=etsysDot3LldpExtEeeLocFbTwSys, etsysDot3LldpExtEeeOperStatus=etsysDot3LldpExtEeeOperStatus, etsysDot3LldpExtCompliances=etsysDot3LldpExtCompliances)
