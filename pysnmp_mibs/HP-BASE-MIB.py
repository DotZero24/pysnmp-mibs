#
# PySNMP MIB module HP-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-BASE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfAccess = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 6))
hpicfAccess.setRevisions(('2005-01-31 13:55',))
if mibBuilder.loadTexts: hpicfAccess.setLastUpdated('200501311355Z')
if mibBuilder.loadTexts: hpicfAccess.setOrganization('Hewlett Packard Company, ProCurve Networking Business')
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
icf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14))
hpicfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11))
hpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3))
netElement = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7))
hpEtherSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11))
hpSwitchJ4819A = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17))
hpSwitchModuleJ8162A = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7))
hpProcurveCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1))
mibBuilder.exportSymbols("HP-BASE-MIB", hpicfObjects=hpicfObjects, hpSwitchJ4819A=hpSwitchJ4819A, PYSNMP_MODULE_ID=hpicfAccess, hp=hp, hpProcurveCommon=hpProcurveCommon, nm=nm, netElement=netElement, hpSwitchModuleJ8162A=hpSwitchModuleJ8162A, icf=icf, hpSystem=hpSystem, hpEtherSwitch=hpEtherSwitch, hpicfAccess=hpicfAccess)
