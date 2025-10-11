# SNMP MIB module (ACE202-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/ACE202-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:05 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(aal5VccEntry,
 atmVclEntry,
 atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "aal5VccEntry",
    "atmVclEntry",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(dsx1CurrentIndex,
 dsx1IntervalIndex,
 dsx1IntervalNumber,
 dsx1LineIndex,
 dsx1LineStatus,
 dsx1LineStatusLastChange,
 dsx1LoopbackStatus,
 dsx1TotalIndex) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1CurrentIndex",
    "dsx1IntervalIndex",
    "dsx1IntervalNumber",
    "dsx1LineIndex",
    "dsx1LineStatus",
    "dsx1LineStatusLastChange",
    "dsx1LoopbackStatus",
    "dsx1TotalIndex")

(frAtmIwfConnectionEntry,) = mibBuilder.importSymbols(
    "FR-ATM-PVC-SERVICE-IWF-MIB",
    "frAtmIwfConnectionEntry")

(InterfaceIndex,
 ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias",
    "ifIndex")

(imaGroupFailureStatus,
 imaGroupIndex,
 imaLinkIfIndex) = mibBuilder.importSymbols(
    "IMA-MIB",
    "imaGroupFailureStatus",
    "imaGroupIndex",
    "imaLinkIfIndex")

(isdnSignalingEntry,) = mibBuilder.importSymbols(
    "ISDN-MIB",
    "isdnSignalingEntry")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class GenAddress(OctetString):
    """Custom type GenAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rad_ObjectIdentity = ObjectIdentity
rad = _Rad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164)
)
_RadTokenRing_ObjectIdentity = ObjectIdentity
radTokenRing = _RadTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 1)
)
_RadFddi_ObjectIdentity = ObjectIdentity
radFddi = _RadFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 2)
)
_RadWan_ObjectIdentity = ObjectIdentity
radWan = _RadWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3)
)
_WanGen_ObjectIdentity = ObjectIdentity
wanGen = _WanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1)
)
_DiverseIfWanGen_ObjectIdentity = ObjectIdentity
diverseIfWanGen = _DiverseIfWanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6)
)
_SonetInterface_ObjectIdentity = ObjectIdentity
sonetInterface = _SonetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2)
)
_PrtSonetPerfHistory_ObjectIdentity = ObjectIdentity
prtSonetPerfHistory = _PrtSonetPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1)
)
_PrtSonetMediumTable_Object = MibTable
prtSonetMediumTable = _PrtSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    prtSonetMediumTable.setStatus("current")
_PrtSonetMediumEntry_Object = MibTableRow
prtSonetMediumEntry = _PrtSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1, 1)
)
prtSonetMediumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtSonetMediumEntry.setStatus("current")


class _PrtSonetMediumTimeElapsed_Type(Integer32):
    """Custom type prtSonetMediumTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_PrtSonetMediumTimeElapsed_Type.__name__ = "Integer32"
_PrtSonetMediumTimeElapsed_Object = MibTableColumn
prtSonetMediumTimeElapsed = _PrtSonetMediumTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1, 1, 1),
    _PrtSonetMediumTimeElapsed_Type()
)
prtSonetMediumTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetMediumTimeElapsed.setStatus("current")


class _PrtSonetMediumValidIntervals_Type(Integer32):
    """Custom type prtSonetMediumValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PrtSonetMediumValidIntervals_Type.__name__ = "Integer32"
_PrtSonetMediumValidIntervals_Object = MibTableColumn
prtSonetMediumValidIntervals = _PrtSonetMediumValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 1, 1, 2),
    _PrtSonetMediumValidIntervals_Type()
)
prtSonetMediumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetMediumValidIntervals.setStatus("current")
_PrtSonetSectionLineCurrentTable_Object = MibTable
prtSonetSectionLineCurrentTable = _PrtSonetSectionLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    prtSonetSectionLineCurrentTable.setStatus("current")
_PrtSectionLineCurrentEntry_Object = MibTableRow
prtSectionLineCurrentEntry = _PrtSectionLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1)
)
prtSectionLineCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtSectionLineCurrentEntry.setStatus("current")
_PrtSonetCurrentLOS_Type = Gauge32
_PrtSonetCurrentLOS_Object = MibTableColumn
prtSonetCurrentLOS = _PrtSonetCurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 1),
    _PrtSonetCurrentLOS_Type()
)
prtSonetCurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOS.setStatus("current")
_PrtSonetCurrentLOF_Type = Gauge32
_PrtSonetCurrentLOF_Object = MibTableColumn
prtSonetCurrentLOF = _PrtSonetCurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 2),
    _PrtSonetCurrentLOF_Type()
)
prtSonetCurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOF.setStatus("current")
_PrtSonetCurrentLineAIS_Type = Gauge32
_PrtSonetCurrentLineAIS_Object = MibTableColumn
prtSonetCurrentLineAIS = _PrtSonetCurrentLineAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 3),
    _PrtSonetCurrentLineAIS_Type()
)
prtSonetCurrentLineAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineAIS.setStatus("current")
_PrtSonetCurrentLineFERF_Type = Gauge32
_PrtSonetCurrentLineFERF_Object = MibTableColumn
prtSonetCurrentLineFERF = _PrtSonetCurrentLineFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 4),
    _PrtSonetCurrentLineFERF_Type()
)
prtSonetCurrentLineFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineFERF.setStatus("current")
_PrtSonetCurrentSectionBIP_Type = Gauge32
_PrtSonetCurrentSectionBIP_Object = MibTableColumn
prtSonetCurrentSectionBIP = _PrtSonetCurrentSectionBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 5),
    _PrtSonetCurrentSectionBIP_Type()
)
prtSonetCurrentSectionBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentSectionBIP.setStatus("current")
_PrtSonetCurrentLineBIP_Type = Gauge32
_PrtSonetCurrentLineBIP_Object = MibTableColumn
prtSonetCurrentLineBIP = _PrtSonetCurrentLineBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 6),
    _PrtSonetCurrentLineBIP_Type()
)
prtSonetCurrentLineBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineBIP.setStatus("current")
_PrtSonetCurrentLineFEBE_Type = Gauge32
_PrtSonetCurrentLineFEBE_Object = MibTableColumn
prtSonetCurrentLineFEBE = _PrtSonetCurrentLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 7),
    _PrtSonetCurrentLineFEBE_Type()
)
prtSonetCurrentLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLineFEBE.setStatus("current")
_PrtSonetCurrentUAS_Type = Gauge32
_PrtSonetCurrentUAS_Object = MibTableColumn
prtSonetCurrentUAS = _PrtSonetCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 8),
    _PrtSonetCurrentUAS_Type()
)
prtSonetCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentUAS.setStatus("current")
_PrtSonetCurrentSES_Type = Gauge32
_PrtSonetCurrentSES_Object = MibTableColumn
prtSonetCurrentSES = _PrtSonetCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 9),
    _PrtSonetCurrentSES_Type()
)
prtSonetCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentSES.setStatus("current")
_PrtSonetCurrentES_Type = Gauge32
_PrtSonetCurrentES_Object = MibTableColumn
prtSonetCurrentES = _PrtSonetCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 10),
    _PrtSonetCurrentES_Type()
)
prtSonetCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentES.setStatus("current")


class _PrtSonetCurrentStatus_Type(OctetString):
    """Custom type prtSonetCurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtSonetCurrentStatus_Type.__name__ = "OctetString"
_PrtSonetCurrentStatus_Object = MibTableColumn
prtSonetCurrentStatus = _PrtSonetCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 11),
    _PrtSonetCurrentStatus_Type()
)
prtSonetCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentStatus.setStatus("current")
_PrtSonetCurrentLSV_Type = Gauge32
_PrtSonetCurrentLSV_Object = MibTableColumn
prtSonetCurrentLSV = _PrtSonetCurrentLSV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 2, 1, 12),
    _PrtSonetCurrentLSV_Type()
)
prtSonetCurrentLSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLSV.setStatus("current")
_PrtSonetSectionLineIntervalTable_Object = MibTable
prtSonetSectionLineIntervalTable = _PrtSonetSectionLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    prtSonetSectionLineIntervalTable.setStatus("current")
_PrtSectionLineIntervalEntry_Object = MibTableRow
prtSectionLineIntervalEntry = _PrtSectionLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1)
)
prtSectionLineIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "prtSonetLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    prtSectionLineIntervalEntry.setStatus("current")


class _PrtSonetLineIntervalNumber_Type(Integer32):
    """Custom type prtSonetLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PrtSonetLineIntervalNumber_Type.__name__ = "Integer32"
_PrtSonetLineIntervalNumber_Object = MibTableColumn
prtSonetLineIntervalNumber = _PrtSonetLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 1),
    _PrtSonetLineIntervalNumber_Type()
)
prtSonetLineIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetLineIntervalNumber.setStatus("current")
_PrtSonetIntervalLOS_Type = Gauge32
_PrtSonetIntervalLOS_Object = MibTableColumn
prtSonetIntervalLOS = _PrtSonetIntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 2),
    _PrtSonetIntervalLOS_Type()
)
prtSonetIntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOS.setStatus("current")
_PrtSonetIntervalLOF_Type = Gauge32
_PrtSonetIntervalLOF_Object = MibTableColumn
prtSonetIntervalLOF = _PrtSonetIntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 3),
    _PrtSonetIntervalLOF_Type()
)
prtSonetIntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOF.setStatus("current")
_PrtSonetIntervalLineAIS_Type = Gauge32
_PrtSonetIntervalLineAIS_Object = MibTableColumn
prtSonetIntervalLineAIS = _PrtSonetIntervalLineAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 4),
    _PrtSonetIntervalLineAIS_Type()
)
prtSonetIntervalLineAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineAIS.setStatus("current")
_PrtSonetIntervalLineFERF_Type = Gauge32
_PrtSonetIntervalLineFERF_Object = MibTableColumn
prtSonetIntervalLineFERF = _PrtSonetIntervalLineFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 5),
    _PrtSonetIntervalLineFERF_Type()
)
prtSonetIntervalLineFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineFERF.setStatus("current")
_PrtSonetIntervalSectionBIP_Type = Gauge32
_PrtSonetIntervalSectionBIP_Object = MibTableColumn
prtSonetIntervalSectionBIP = _PrtSonetIntervalSectionBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 6),
    _PrtSonetIntervalSectionBIP_Type()
)
prtSonetIntervalSectionBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalSectionBIP.setStatus("current")
_PrtSonetIntervalLineBIP_Type = Gauge32
_PrtSonetIntervalLineBIP_Object = MibTableColumn
prtSonetIntervalLineBIP = _PrtSonetIntervalLineBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 7),
    _PrtSonetIntervalLineBIP_Type()
)
prtSonetIntervalLineBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineBIP.setStatus("current")
_PrtSonetIntervalLineFEBE_Type = Gauge32
_PrtSonetIntervalLineFEBE_Object = MibTableColumn
prtSonetIntervalLineFEBE = _PrtSonetIntervalLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 8),
    _PrtSonetIntervalLineFEBE_Type()
)
prtSonetIntervalLineFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLineFEBE.setStatus("current")
_PrtSonetIntervalUAS_Type = Gauge32
_PrtSonetIntervalUAS_Object = MibTableColumn
prtSonetIntervalUAS = _PrtSonetIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 9),
    _PrtSonetIntervalUAS_Type()
)
prtSonetIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalUAS.setStatus("current")
_PrtSonetIntervalSES_Type = Gauge32
_PrtSonetIntervalSES_Object = MibTableColumn
prtSonetIntervalSES = _PrtSonetIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 10),
    _PrtSonetIntervalSES_Type()
)
prtSonetIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalSES.setStatus("current")
_PrtSonetIntervalES_Type = Gauge32
_PrtSonetIntervalES_Object = MibTableColumn
prtSonetIntervalES = _PrtSonetIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 11),
    _PrtSonetIntervalES_Type()
)
prtSonetIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalES.setStatus("current")


class _PrtSonetIntervalStatus_Type(OctetString):
    """Custom type prtSonetIntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtSonetIntervalStatus_Type.__name__ = "OctetString"
_PrtSonetIntervalStatus_Object = MibTableColumn
prtSonetIntervalStatus = _PrtSonetIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 12),
    _PrtSonetIntervalStatus_Type()
)
prtSonetIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalStatus.setStatus("current")
_PrtSonetIntervalLSV_Type = Gauge32
_PrtSonetIntervalLSV_Object = MibTableColumn
prtSonetIntervalLSV = _PrtSonetIntervalLSV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 3, 1, 13),
    _PrtSonetIntervalLSV_Type()
)
prtSonetIntervalLSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLSV.setStatus("current")
_PrtSonetPathCurrentTable_Object = MibTable
prtSonetPathCurrentTable = _PrtSonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    prtSonetPathCurrentTable.setStatus("current")
_PrtPathCurrentEntry_Object = MibTableRow
prtPathCurrentEntry = _PrtPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1)
)
prtPathCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtPathCurrentEntry.setStatus("current")
_PrtSonetCurrentPathAIS_Type = Gauge32
_PrtSonetCurrentPathAIS_Object = MibTableColumn
prtSonetCurrentPathAIS = _PrtSonetCurrentPathAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 1),
    _PrtSonetCurrentPathAIS_Type()
)
prtSonetCurrentPathAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathAIS.setStatus("current")
_PrtSonetCurrentPathFERF_Type = Gauge32
_PrtSonetCurrentPathFERF_Object = MibTableColumn
prtSonetCurrentPathFERF = _PrtSonetCurrentPathFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 2),
    _PrtSonetCurrentPathFERF_Type()
)
prtSonetCurrentPathFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathFERF.setStatus("current")
_PrtSonetCurrentLOP_Type = Gauge32
_PrtSonetCurrentLOP_Object = MibTableColumn
prtSonetCurrentLOP = _PrtSonetCurrentLOP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 3),
    _PrtSonetCurrentLOP_Type()
)
prtSonetCurrentLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOP.setStatus("current")
_PrtSonetCurrentSLM_Type = Gauge32
_PrtSonetCurrentSLM_Object = MibTableColumn
prtSonetCurrentSLM = _PrtSonetCurrentSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 4),
    _PrtSonetCurrentSLM_Type()
)
prtSonetCurrentSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentSLM.setStatus("current")
_PrtSonetCurrentLOC_Type = Gauge32
_PrtSonetCurrentLOC_Object = MibTableColumn
prtSonetCurrentLOC = _PrtSonetCurrentLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 5),
    _PrtSonetCurrentLOC_Type()
)
prtSonetCurrentLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentLOC.setStatus("current")
_PrtSonetCurrentPathBIP_Type = Gauge32
_PrtSonetCurrentPathBIP_Object = MibTableColumn
prtSonetCurrentPathBIP = _PrtSonetCurrentPathBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 6),
    _PrtSonetCurrentPathBIP_Type()
)
prtSonetCurrentPathBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathBIP.setStatus("current")
_PrtSonetCurrentPathFEBE_Type = Gauge32
_PrtSonetCurrentPathFEBE_Object = MibTableColumn
prtSonetCurrentPathFEBE = _PrtSonetCurrentPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 4, 1, 7),
    _PrtSonetCurrentPathFEBE_Type()
)
prtSonetCurrentPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetCurrentPathFEBE.setStatus("current")
_PrtSonetPathIntervalTable_Object = MibTable
prtSonetPathIntervalTable = _PrtSonetPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    prtSonetPathIntervalTable.setStatus("current")
_PrtPathIntervalEntry_Object = MibTableRow
prtPathIntervalEntry = _PrtPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1)
)
prtPathIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "prtSonetPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    prtPathIntervalEntry.setStatus("current")


class _PrtSonetPathIntervalNumber_Type(Integer32):
    """Custom type prtSonetPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PrtSonetPathIntervalNumber_Type.__name__ = "Integer32"
_PrtSonetPathIntervalNumber_Object = MibTableColumn
prtSonetPathIntervalNumber = _PrtSonetPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 1),
    _PrtSonetPathIntervalNumber_Type()
)
prtSonetPathIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetPathIntervalNumber.setStatus("current")
_PrtSonetIntervalPathAIS_Type = Gauge32
_PrtSonetIntervalPathAIS_Object = MibTableColumn
prtSonetIntervalPathAIS = _PrtSonetIntervalPathAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 2),
    _PrtSonetIntervalPathAIS_Type()
)
prtSonetIntervalPathAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathAIS.setStatus("current")
_PrtSonetIntervalPathFERF_Type = Gauge32
_PrtSonetIntervalPathFERF_Object = MibTableColumn
prtSonetIntervalPathFERF = _PrtSonetIntervalPathFERF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 3),
    _PrtSonetIntervalPathFERF_Type()
)
prtSonetIntervalPathFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathFERF.setStatus("current")
_PrtSonetIntervalLOP_Type = Gauge32
_PrtSonetIntervalLOP_Object = MibTableColumn
prtSonetIntervalLOP = _PrtSonetIntervalLOP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 4),
    _PrtSonetIntervalLOP_Type()
)
prtSonetIntervalLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOP.setStatus("current")
_PrtSonetIntervalSLM_Type = Gauge32
_PrtSonetIntervalSLM_Object = MibTableColumn
prtSonetIntervalSLM = _PrtSonetIntervalSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 5),
    _PrtSonetIntervalSLM_Type()
)
prtSonetIntervalSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalSLM.setStatus("current")
_PrtSonetIntervalLOC_Type = Gauge32
_PrtSonetIntervalLOC_Object = MibTableColumn
prtSonetIntervalLOC = _PrtSonetIntervalLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 6),
    _PrtSonetIntervalLOC_Type()
)
prtSonetIntervalLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalLOC.setStatus("current")
_PrtSonetIntervalPathBIP_Type = Gauge32
_PrtSonetIntervalPathBIP_Object = MibTableColumn
prtSonetIntervalPathBIP = _PrtSonetIntervalPathBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 7),
    _PrtSonetIntervalPathBIP_Type()
)
prtSonetIntervalPathBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathBIP.setStatus("current")
_PrtSonetIntervalPathFEBE_Type = Gauge32
_PrtSonetIntervalPathFEBE_Object = MibTableColumn
prtSonetIntervalPathFEBE = _PrtSonetIntervalPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 1, 5, 1, 8),
    _PrtSonetIntervalPathFEBE_Type()
)
prtSonetIntervalPathFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetIntervalPathFEBE.setStatus("current")
_PrtSonetConfig_ObjectIdentity = ObjectIdentity
prtSonetConfig = _PrtSonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2)
)
_PrtSonetGen_ObjectIdentity = ObjectIdentity
prtSonetGen = _PrtSonetGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1)
)
_PrtSonetGenTable_Object = MibTable
prtSonetGenTable = _PrtSonetGenTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    prtSonetGenTable.setStatus("current")
_PrtSonetGenEntry_Object = MibTableRow
prtSonetGenEntry = _PrtSonetGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1)
)
prtSonetGenEntry.setIndexNames(
    (0, "ACE202-MIB", "prtSonetGenCnfgIdx"),
    (0, "ACE202-MIB", "prtSonetGenIdx"),
)
if mibBuilder.loadTexts:
    prtSonetGenEntry.setStatus("current")


class _PrtSonetGenCnfgIdx_Type(Integer32):
    """Custom type prtSonetGenCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetGenCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetGenCnfgIdx_Object = MibTableColumn
prtSonetGenCnfgIdx = _PrtSonetGenCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 1),
    _PrtSonetGenCnfgIdx_Type()
)
prtSonetGenCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetGenCnfgIdx.setStatus("current")
_PrtSonetGenIdx_Type = Integer32
_PrtSonetGenIdx_Object = MibTableColumn
prtSonetGenIdx = _PrtSonetGenIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 2),
    _PrtSonetGenIdx_Type()
)
prtSonetGenIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetGenIdx.setStatus("current")


class _PrtSonetGenSdThreshold_Type(Integer32):
    """Custom type prtSonetGenSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_PrtSonetGenSdThreshold_Type.__name__ = "Integer32"
_PrtSonetGenSdThreshold_Object = MibTableColumn
prtSonetGenSdThreshold = _PrtSonetGenSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 3),
    _PrtSonetGenSdThreshold_Type()
)
prtSonetGenSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetGenSdThreshold.setStatus("current")


class _PrtSonetGenEedThreshold_Type(Integer32):
    """Custom type prtSonetGenEedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_PrtSonetGenEedThreshold_Type.__name__ = "Integer32"
_PrtSonetGenEedThreshold_Object = MibTableColumn
prtSonetGenEedThreshold = _PrtSonetGenEedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 1, 1, 1, 4),
    _PrtSonetGenEedThreshold_Type()
)
prtSonetGenEedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetGenEedThreshold.setStatus("current")
_PrtSonetStm1_ObjectIdentity = ObjectIdentity
prtSonetStm1 = _PrtSonetStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2)
)
_PrtSonetStm1Table_Object = MibTable
prtSonetStm1Table = _PrtSonetStm1Table_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    prtSonetStm1Table.setStatus("current")
_PrtSonetStm1Entry_Object = MibTableRow
prtSonetStm1Entry = _PrtSonetStm1Entry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1)
)
prtSonetStm1Entry.setIndexNames(
    (0, "ACE202-MIB", "prtSonetStm1CnfgIdx"),
    (0, "ACE202-MIB", "prtSonetStm1Idx"),
)
if mibBuilder.loadTexts:
    prtSonetStm1Entry.setStatus("current")


class _PrtSonetStm1CnfgIdx_Type(Integer32):
    """Custom type prtSonetStm1CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetStm1CnfgIdx_Type.__name__ = "Integer32"
_PrtSonetStm1CnfgIdx_Object = MibTableColumn
prtSonetStm1CnfgIdx = _PrtSonetStm1CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 1),
    _PrtSonetStm1CnfgIdx_Type()
)
prtSonetStm1CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetStm1CnfgIdx.setStatus("current")
_PrtSonetStm1Idx_Type = Integer32
_PrtSonetStm1Idx_Object = MibTableColumn
prtSonetStm1Idx = _PrtSonetStm1Idx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 2),
    _PrtSonetStm1Idx_Type()
)
prtSonetStm1Idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetStm1Idx.setStatus("current")


class _PrtSonetStm1ClockSrc_Type(Integer32):
    """Custom type prtSonetStm1ClockSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("internal", 2),
          ("lbt", 3))
    )


_PrtSonetStm1ClockSrc_Type.__name__ = "Integer32"
_PrtSonetStm1ClockSrc_Object = MibTableColumn
prtSonetStm1ClockSrc = _PrtSonetStm1ClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 3),
    _PrtSonetStm1ClockSrc_Type()
)
prtSonetStm1ClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1ClockSrc.setStatus("current")


class _PrtSonetStm1DccMode_Type(Integer32):
    """Custom type prtSonetStm1DccMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("none", 2),
          ("d1ToD3", 3),
          ("d4ToD12", 4))
    )


_PrtSonetStm1DccMode_Type.__name__ = "Integer32"
_PrtSonetStm1DccMode_Object = MibTableColumn
prtSonetStm1DccMode = _PrtSonetStm1DccMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 4),
    _PrtSonetStm1DccMode_Type()
)
prtSonetStm1DccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1DccMode.setStatus("current")


class _PrtSonetStm1RoutingProt_Type(Integer32):
    """Custom type prtSonetStm1RoutingProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3),
          ("rip2", 4))
    )


_PrtSonetStm1RoutingProt_Type.__name__ = "Integer32"
_PrtSonetStm1RoutingProt_Object = MibTableColumn
prtSonetStm1RoutingProt = _PrtSonetStm1RoutingProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 5),
    _PrtSonetStm1RoutingProt_Type()
)
prtSonetStm1RoutingProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1RoutingProt.setStatus("current")


class _PrtSonetStm1MngProt_Type(Integer32):
    """Custom type prtSonetStm1MngProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("proprietary", 3),
          ("ppp", 5),
          ("frameRelay", 6))
    )


_PrtSonetStm1MngProt_Type.__name__ = "Integer32"
_PrtSonetStm1MngProt_Object = MibTableColumn
prtSonetStm1MngProt = _PrtSonetStm1MngProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 2, 1, 1, 6),
    _PrtSonetStm1MngProt_Type()
)
prtSonetStm1MngProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetStm1MngProt.setStatus("current")
_PrtSonetVc_ObjectIdentity = ObjectIdentity
prtSonetVc = _PrtSonetVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3)
)
_PrtSonetVcTable_Object = MibTable
prtSonetVcTable = _PrtSonetVcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    prtSonetVcTable.setStatus("current")
_PrtSonetVcEntry_Object = MibTableRow
prtSonetVcEntry = _PrtSonetVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1)
)
prtSonetVcEntry.setIndexNames(
    (0, "ACE202-MIB", "prtSonetVcCnfgIdx"),
    (0, "ACE202-MIB", "prtSonetVcIdx"),
)
if mibBuilder.loadTexts:
    prtSonetVcEntry.setStatus("current")


class _PrtSonetVcCnfgIdx_Type(Integer32):
    """Custom type prtSonetVcCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetVcCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetVcCnfgIdx_Object = MibTableColumn
prtSonetVcCnfgIdx = _PrtSonetVcCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 1),
    _PrtSonetVcCnfgIdx_Type()
)
prtSonetVcCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcCnfgIdx.setStatus("current")
_PrtSonetVcIdx_Type = Integer32
_PrtSonetVcIdx_Object = MibTableColumn
prtSonetVcIdx = _PrtSonetVcIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 2),
    _PrtSonetVcIdx_Type()
)
prtSonetVcIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetVcIdx.setStatus("current")


class _PrtSonetVcJTxPathTraceEnable_Type(Integer32):
    """Custom type prtSonetVcJTxPathTraceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PrtSonetVcJTxPathTraceEnable_Type.__name__ = "Integer32"
_PrtSonetVcJTxPathTraceEnable_Object = MibTableColumn
prtSonetVcJTxPathTraceEnable = _PrtSonetVcJTxPathTraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 3),
    _PrtSonetVcJTxPathTraceEnable_Type()
)
prtSonetVcJTxPathTraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcJTxPathTraceEnable.setStatus("current")


class _PrtSonetVcJRxPathTraceEnable_Type(Integer32):
    """Custom type prtSonetVcJRxPathTraceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PrtSonetVcJRxPathTraceEnable_Type.__name__ = "Integer32"
_PrtSonetVcJRxPathTraceEnable_Object = MibTableColumn
prtSonetVcJRxPathTraceEnable = _PrtSonetVcJRxPathTraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 4),
    _PrtSonetVcJRxPathTraceEnable_Type()
)
prtSonetVcJRxPathTraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcJRxPathTraceEnable.setStatus("current")


class _PrtSonetVcJPathTrace_Type(DisplayString):
    """Custom type prtSonetVcJPathTrace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PrtSonetVcJPathTrace_Type.__name__ = "DisplayString"
_PrtSonetVcJPathTrace_Object = MibTableColumn
prtSonetVcJPathTrace = _PrtSonetVcJPathTrace_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 5),
    _PrtSonetVcJPathTrace_Type()
)
prtSonetVcJPathTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcJPathTrace.setStatus("current")


class _PrtSonetVcConnect_Type(Integer32):
    """Custom type prtSonetVcConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_PrtSonetVcConnect_Type.__name__ = "Integer32"
_PrtSonetVcConnect_Object = MibTableColumn
prtSonetVcConnect = _PrtSonetVcConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 1, 1, 6),
    _PrtSonetVcConnect_Type()
)
prtSonetVcConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSonetVcConnect.setStatus("current")
_PrtSonetTuTable_Object = MibTable
prtSonetTuTable = _PrtSonetTuTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    prtSonetTuTable.setStatus("current")
_PrtSonetTuEntry_Object = MibTableRow
prtSonetTuEntry = _PrtSonetTuEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1)
)
prtSonetTuEntry.setIndexNames(
    (0, "ACE202-MIB", "prtSonetTuCnfgIdx"),
    (0, "ACE202-MIB", "prtSonetTuPrtIdx"),
    (0, "ACE202-MIB", "prtSonetTuIdx"),
    (0, "ACE202-MIB", "prtSonetTuConPrtIdx"),
)
if mibBuilder.loadTexts:
    prtSonetTuEntry.setStatus("current")


class _PrtSonetTuCnfgIdx_Type(Integer32):
    """Custom type prtSonetTuCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetTuCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetTuCnfgIdx_Object = MibTableColumn
prtSonetTuCnfgIdx = _PrtSonetTuCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 1),
    _PrtSonetTuCnfgIdx_Type()
)
prtSonetTuCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuCnfgIdx.setStatus("current")
_PrtSonetTuPrtIdx_Type = Integer32
_PrtSonetTuPrtIdx_Object = MibTableColumn
prtSonetTuPrtIdx = _PrtSonetTuPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 2),
    _PrtSonetTuPrtIdx_Type()
)
prtSonetTuPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuPrtIdx.setStatus("current")
_PrtSonetTuIdx_Type = Integer32
_PrtSonetTuIdx_Object = MibTableColumn
prtSonetTuIdx = _PrtSonetTuIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 3),
    _PrtSonetTuIdx_Type()
)
prtSonetTuIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuIdx.setStatus("current")
_PrtSonetTuConPrtIdx_Type = Integer32
_PrtSonetTuConPrtIdx_Object = MibTableColumn
prtSonetTuConPrtIdx = _PrtSonetTuConPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 4),
    _PrtSonetTuConPrtIdx_Type()
)
prtSonetTuConPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetTuConPrtIdx.setStatus("current")


class _PrtSonetTuType_Type(Integer32):
    """Custom type prtSonetTuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("connect", 2)
    )


_PrtSonetTuType_Type.__name__ = "Integer32"
_PrtSonetTuType_Object = MibTableColumn
prtSonetTuType = _PrtSonetTuType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 5),
    _PrtSonetTuType_Type()
)
prtSonetTuType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetTuType.setStatus("current")


class _PrtSonetTuMode_Type(Integer32):
    """Custom type prtSonetTuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("addAndDrop", 2),
          ("add", 3))
    )


_PrtSonetTuMode_Type.__name__ = "Integer32"
_PrtSonetTuMode_Object = MibTableColumn
prtSonetTuMode = _PrtSonetTuMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 6),
    _PrtSonetTuMode_Type()
)
prtSonetTuMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetTuMode.setStatus("current")
_PrtSonetTuRowStatus_Type = RowStatus
_PrtSonetTuRowStatus_Object = MibTableColumn
prtSonetTuRowStatus = _PrtSonetTuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 2, 3, 2, 1, 7),
    _PrtSonetTuRowStatus_Type()
)
prtSonetTuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetTuRowStatus.setStatus("current")
_PrtSonetXConnect_ObjectIdentity = ObjectIdentity
prtSonetXConnect = _PrtSonetXConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3)
)
_PrtSonetXConnectTable_Object = MibTable
prtSonetXConnectTable = _PrtSonetXConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1)
)
if mibBuilder.loadTexts:
    prtSonetXConnectTable.setStatus("current")
_PrtSonetXConnectEntry_Object = MibTableRow
prtSonetXConnectEntry = _PrtSonetXConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1)
)
prtSonetXConnectEntry.setIndexNames(
    (0, "ACE202-MIB", "prtSonetXConnectCnfgIdx"),
    (0, "ACE202-MIB", "prtSonetXConnectPrtIdx"),
    (0, "ACE202-MIB", "prtSonetXConnectConPrtIdx"),
    (0, "ACE202-MIB", "prtSonetXConnectAUGIdx"),
    (0, "ACE202-MIB", "prtSonetXConnectTUG3Idx"),
    (0, "ACE202-MIB", "prtSonetXConnectTUG2Idx"),
    (0, "ACE202-MIB", "prtSonetXConnectTUnIdx"),
)
if mibBuilder.loadTexts:
    prtSonetXConnectEntry.setStatus("current")


class _PrtSonetXConnectCnfgIdx_Type(Integer32):
    """Custom type prtSonetXConnectCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSonetXConnectCnfgIdx_Type.__name__ = "Integer32"
_PrtSonetXConnectCnfgIdx_Object = MibTableColumn
prtSonetXConnectCnfgIdx = _PrtSonetXConnectCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 1),
    _PrtSonetXConnectCnfgIdx_Type()
)
prtSonetXConnectCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectCnfgIdx.setStatus("current")
_PrtSonetXConnectPrtIdx_Type = Integer32
_PrtSonetXConnectPrtIdx_Object = MibTableColumn
prtSonetXConnectPrtIdx = _PrtSonetXConnectPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 2),
    _PrtSonetXConnectPrtIdx_Type()
)
prtSonetXConnectPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectPrtIdx.setStatus("current")
_PrtSonetXConnectConPrtIdx_Type = Integer32
_PrtSonetXConnectConPrtIdx_Object = MibTableColumn
prtSonetXConnectConPrtIdx = _PrtSonetXConnectConPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 3),
    _PrtSonetXConnectConPrtIdx_Type()
)
prtSonetXConnectConPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectConPrtIdx.setStatus("current")
_PrtSonetXConnectAUGIdx_Type = Integer32
_PrtSonetXConnectAUGIdx_Object = MibTableColumn
prtSonetXConnectAUGIdx = _PrtSonetXConnectAUGIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 4),
    _PrtSonetXConnectAUGIdx_Type()
)
prtSonetXConnectAUGIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectAUGIdx.setStatus("current")
_PrtSonetXConnectTUG3Idx_Type = Integer32
_PrtSonetXConnectTUG3Idx_Object = MibTableColumn
prtSonetXConnectTUG3Idx = _PrtSonetXConnectTUG3Idx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 5),
    _PrtSonetXConnectTUG3Idx_Type()
)
prtSonetXConnectTUG3Idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectTUG3Idx.setStatus("current")
_PrtSonetXConnectTUG2Idx_Type = Integer32
_PrtSonetXConnectTUG2Idx_Object = MibTableColumn
prtSonetXConnectTUG2Idx = _PrtSonetXConnectTUG2Idx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 6),
    _PrtSonetXConnectTUG2Idx_Type()
)
prtSonetXConnectTUG2Idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectTUG2Idx.setStatus("current")
_PrtSonetXConnectTUnIdx_Type = Integer32
_PrtSonetXConnectTUnIdx_Object = MibTableColumn
prtSonetXConnectTUnIdx = _PrtSonetXConnectTUnIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 7),
    _PrtSonetXConnectTUnIdx_Type()
)
prtSonetXConnectTUnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSonetXConnectTUnIdx.setStatus("current")
_PrtSonetXConnectRowStatus_Type = RowStatus
_PrtSonetXConnectRowStatus_Object = MibTableColumn
prtSonetXConnectRowStatus = _PrtSonetXConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 8),
    _PrtSonetXConnectRowStatus_Type()
)
prtSonetXConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetXConnectRowStatus.setStatus("current")


class _PrtSonetXConnectDirection_Type(Integer32):
    """Custom type prtSonetXConnectDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("rx", 2),
          ("tx", 3),
          ("both", 4))
    )


_PrtSonetXConnectDirection_Type.__name__ = "Integer32"
_PrtSonetXConnectDirection_Object = MibTableColumn
prtSonetXConnectDirection = _PrtSonetXConnectDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 9),
    _PrtSonetXConnectDirection_Type()
)
prtSonetXConnectDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetXConnectDirection.setStatus("current")


class _PrtSonetXConnectTuNumber_Type(Integer32):
    """Custom type prtSonetXConnectTuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("tu2", 2),
          ("tu3", 3),
          ("tu11", 4),
          ("tu12", 5))
    )


_PrtSonetXConnectTuNumber_Type.__name__ = "Integer32"
_PrtSonetXConnectTuNumber_Object = MibTableColumn
prtSonetXConnectTuNumber = _PrtSonetXConnectTuNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 2, 3, 1, 1, 10),
    _PrtSonetXConnectTuNumber_Type()
)
prtSonetXConnectTuNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtSonetXConnectTuNumber.setStatus("current")
_Ds3Interface_ObjectIdentity = ObjectIdentity
ds3Interface = _Ds3Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3)
)
_PrtDs3PerfHistory_ObjectIdentity = ObjectIdentity
prtDs3PerfHistory = _PrtDs3PerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1)
)
_PrtSDs3IfTable_Object = MibTable
prtSDs3IfTable = _PrtSDs3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    prtSDs3IfTable.setStatus("current")
_PrtDs3IfEntry_Object = MibTableRow
prtDs3IfEntry = _PrtDs3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1, 1)
)
prtDs3IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtDs3IfEntry.setStatus("current")


class _PrtDs3IfTimeElapsed_Type(Integer32):
    """Custom type prtDs3IfTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_PrtDs3IfTimeElapsed_Type.__name__ = "Integer32"
_PrtDs3IfTimeElapsed_Object = MibTableColumn
prtDs3IfTimeElapsed = _PrtDs3IfTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1, 1, 1),
    _PrtDs3IfTimeElapsed_Type()
)
prtDs3IfTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IfTimeElapsed.setStatus("current")


class _PrtDs3IfValidIntervals_Type(Integer32):
    """Custom type prtDs3IfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PrtDs3IfValidIntervals_Type.__name__ = "Integer32"
_PrtDs3IfValidIntervals_Object = MibTableColumn
prtDs3IfValidIntervals = _PrtDs3IfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1, 1, 2),
    _PrtDs3IfValidIntervals_Type()
)
prtDs3IfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IfValidIntervals.setStatus("current")
_PrtDs3CurrentTable_Object = MibTable
prtDs3CurrentTable = _PrtDs3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    prtDs3CurrentTable.setStatus("current")
_PrtDs3CurrentEntry_Object = MibTableRow
prtDs3CurrentEntry = _PrtDs3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1)
)
prtDs3CurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtDs3CurrentEntry.setStatus("current")
_PrtDs3CurrentLOS_Type = Gauge32
_PrtDs3CurrentLOS_Object = MibTableColumn
prtDs3CurrentLOS = _PrtDs3CurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 1),
    _PrtDs3CurrentLOS_Type()
)
prtDs3CurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentLOS.setStatus("current")
_PrtDs3CurrentOOF_Type = Gauge32
_PrtDs3CurrentOOF_Object = MibTableColumn
prtDs3CurrentOOF = _PrtDs3CurrentOOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 2),
    _PrtDs3CurrentOOF_Type()
)
prtDs3CurrentOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentOOF.setStatus("current")
_PrtDs3CurrentLOC_Type = Gauge32
_PrtDs3CurrentLOC_Object = MibTableColumn
prtDs3CurrentLOC = _PrtDs3CurrentLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 3),
    _PrtDs3CurrentLOC_Type()
)
prtDs3CurrentLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentLOC.setStatus("current")
_PrtDs3CurrentAIS_Type = Gauge32
_PrtDs3CurrentAIS_Object = MibTableColumn
prtDs3CurrentAIS = _PrtDs3CurrentAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 4),
    _PrtDs3CurrentAIS_Type()
)
prtDs3CurrentAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentAIS.setStatus("current")
_PrtDs3CurrentRDI_Type = Gauge32
_PrtDs3CurrentRDI_Object = MibTableColumn
prtDs3CurrentRDI = _PrtDs3CurrentRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 5),
    _PrtDs3CurrentRDI_Type()
)
prtDs3CurrentRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentRDI.setStatus("current")
_PrtDs3CurrentUAS_Type = Gauge32
_PrtDs3CurrentUAS_Object = MibTableColumn
prtDs3CurrentUAS = _PrtDs3CurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 6),
    _PrtDs3CurrentUAS_Type()
)
prtDs3CurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentUAS.setStatus("current")
_PrtDs3CurrentBIP_Type = Gauge32
_PrtDs3CurrentBIP_Object = MibTableColumn
prtDs3CurrentBIP = _PrtDs3CurrentBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 7),
    _PrtDs3CurrentBIP_Type()
)
prtDs3CurrentBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentBIP.setStatus("current")
_PrtDs3CurrentFEBE_Type = Gauge32
_PrtDs3CurrentFEBE_Object = MibTableColumn
prtDs3CurrentFEBE = _PrtDs3CurrentFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 8),
    _PrtDs3CurrentFEBE_Type()
)
prtDs3CurrentFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentFEBE.setStatus("current")
_PrtDs3CurrentSLM_Type = Gauge32
_PrtDs3CurrentSLM_Object = MibTableColumn
prtDs3CurrentSLM = _PrtDs3CurrentSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 9),
    _PrtDs3CurrentSLM_Type()
)
prtDs3CurrentSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentSLM.setStatus("current")
_PrtDs3CurrentSES_Type = Gauge32
_PrtDs3CurrentSES_Object = MibTableColumn
prtDs3CurrentSES = _PrtDs3CurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 10),
    _PrtDs3CurrentSES_Type()
)
prtDs3CurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentSES.setStatus("current")
_PrtDs3CurrentES_Type = Gauge32
_PrtDs3CurrentES_Object = MibTableColumn
prtDs3CurrentES = _PrtDs3CurrentES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 11),
    _PrtDs3CurrentES_Type()
)
prtDs3CurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentES.setStatus("current")
_PrtDs3CurrentBitParity_Type = Gauge32
_PrtDs3CurrentBitParity_Object = MibTableColumn
prtDs3CurrentBitParity = _PrtDs3CurrentBitParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 12),
    _PrtDs3CurrentBitParity_Type()
)
prtDs3CurrentBitParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentBitParity.setStatus("current")
_PrtDs3CurrentPlcpLOF_Type = Gauge32
_PrtDs3CurrentPlcpLOF_Object = MibTableColumn
prtDs3CurrentPlcpLOF = _PrtDs3CurrentPlcpLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 13),
    _PrtDs3CurrentPlcpLOF_Type()
)
prtDs3CurrentPlcpLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpLOF.setStatus("current")
_PrtDs3CurrentPlcpRAI_Type = Gauge32
_PrtDs3CurrentPlcpRAI_Object = MibTableColumn
prtDs3CurrentPlcpRAI = _PrtDs3CurrentPlcpRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 14),
    _PrtDs3CurrentPlcpRAI_Type()
)
prtDs3CurrentPlcpRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpRAI.setStatus("current")
_PrtDs3CurrentPlcpBIP_Type = Gauge32
_PrtDs3CurrentPlcpBIP_Object = MibTableColumn
prtDs3CurrentPlcpBIP = _PrtDs3CurrentPlcpBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 15),
    _PrtDs3CurrentPlcpBIP_Type()
)
prtDs3CurrentPlcpBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpBIP.setStatus("current")
_PrtDs3CurrentPlcpFEBE_Type = Gauge32
_PrtDs3CurrentPlcpFEBE_Object = MibTableColumn
prtDs3CurrentPlcpFEBE = _PrtDs3CurrentPlcpFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 16),
    _PrtDs3CurrentPlcpFEBE_Type()
)
prtDs3CurrentPlcpFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpFEBE.setStatus("current")
_PrtDs3CurrentBPV_Type = Gauge32
_PrtDs3CurrentBPV_Object = MibTableColumn
prtDs3CurrentBPV = _PrtDs3CurrentBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 17),
    _PrtDs3CurrentBPV_Type()
)
prtDs3CurrentBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentBPV.setStatus("current")
_PrtDs3CurrentLCE_Type = Gauge32
_PrtDs3CurrentLCE_Object = MibTableColumn
prtDs3CurrentLCE = _PrtDs3CurrentLCE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 18),
    _PrtDs3CurrentLCE_Type()
)
prtDs3CurrentLCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentLCE.setStatus("current")


class _PrtDs3CurrentStatus_Type(OctetString):
    """Custom type prtDs3CurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtDs3CurrentStatus_Type.__name__ = "OctetString"
_PrtDs3CurrentStatus_Object = MibTableColumn
prtDs3CurrentStatus = _PrtDs3CurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 19),
    _PrtDs3CurrentStatus_Type()
)
prtDs3CurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentStatus.setStatus("current")
_PrtDs3IntervalTable_Object = MibTable
prtDs3IntervalTable = _PrtDs3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3)
)
if mibBuilder.loadTexts:
    prtDs3IntervalTable.setStatus("current")
_PrtDs3IntervalEntry_Object = MibTableRow
prtDs3IntervalEntry = _PrtDs3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1)
)
prtDs3IntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "prtDs3IntervalNumber"),
)
if mibBuilder.loadTexts:
    prtDs3IntervalEntry.setStatus("current")


class _PrtDs3IntervalNumber_Type(Integer32):
    """Custom type prtDs3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PrtDs3IntervalNumber_Type.__name__ = "Integer32"
_PrtDs3IntervalNumber_Object = MibTableColumn
prtDs3IntervalNumber = _PrtDs3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 1),
    _PrtDs3IntervalNumber_Type()
)
prtDs3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalNumber.setStatus("current")
_PrtDs3IntervalLOS_Type = Gauge32
_PrtDs3IntervalLOS_Object = MibTableColumn
prtDs3IntervalLOS = _PrtDs3IntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 2),
    _PrtDs3IntervalLOS_Type()
)
prtDs3IntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalLOS.setStatus("current")
_PrtDs3IntervalOOF_Type = Gauge32
_PrtDs3IntervalOOF_Object = MibTableColumn
prtDs3IntervalOOF = _PrtDs3IntervalOOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 3),
    _PrtDs3IntervalOOF_Type()
)
prtDs3IntervalOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalOOF.setStatus("current")
_PrtDs3IntervalLOC_Type = Gauge32
_PrtDs3IntervalLOC_Object = MibTableColumn
prtDs3IntervalLOC = _PrtDs3IntervalLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 4),
    _PrtDs3IntervalLOC_Type()
)
prtDs3IntervalLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalLOC.setStatus("current")
_PrtDs3IntervalAIS_Type = Gauge32
_PrtDs3IntervalAIS_Object = MibTableColumn
prtDs3IntervalAIS = _PrtDs3IntervalAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 5),
    _PrtDs3IntervalAIS_Type()
)
prtDs3IntervalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalAIS.setStatus("current")
_PrtDs3IntervalRDI_Type = Gauge32
_PrtDs3IntervalRDI_Object = MibTableColumn
prtDs3IntervalRDI = _PrtDs3IntervalRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 6),
    _PrtDs3IntervalRDI_Type()
)
prtDs3IntervalRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalRDI.setStatus("current")
_PrtDs3IntervalUAS_Type = Gauge32
_PrtDs3IntervalUAS_Object = MibTableColumn
prtDs3IntervalUAS = _PrtDs3IntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 7),
    _PrtDs3IntervalUAS_Type()
)
prtDs3IntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalUAS.setStatus("current")
_PrtDs3IntervalBIP_Type = Gauge32
_PrtDs3IntervalBIP_Object = MibTableColumn
prtDs3IntervalBIP = _PrtDs3IntervalBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 8),
    _PrtDs3IntervalBIP_Type()
)
prtDs3IntervalBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalBIP.setStatus("current")
_PrtDs3IntervalFEBE_Type = Gauge32
_PrtDs3IntervalFEBE_Object = MibTableColumn
prtDs3IntervalFEBE = _PrtDs3IntervalFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 9),
    _PrtDs3IntervalFEBE_Type()
)
prtDs3IntervalFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalFEBE.setStatus("current")
_PrtDs3IntervalSLM_Type = Gauge32
_PrtDs3IntervalSLM_Object = MibTableColumn
prtDs3IntervalSLM = _PrtDs3IntervalSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 10),
    _PrtDs3IntervalSLM_Type()
)
prtDs3IntervalSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalSLM.setStatus("current")
_PrtDs3IntervalSES_Type = Gauge32
_PrtDs3IntervalSES_Object = MibTableColumn
prtDs3IntervalSES = _PrtDs3IntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 11),
    _PrtDs3IntervalSES_Type()
)
prtDs3IntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalSES.setStatus("current")
_PrtDs3IntervalES_Type = Gauge32
_PrtDs3IntervalES_Object = MibTableColumn
prtDs3IntervalES = _PrtDs3IntervalES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 12),
    _PrtDs3IntervalES_Type()
)
prtDs3IntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalES.setStatus("current")
_PrtDs3IntervalBitParity_Type = Gauge32
_PrtDs3IntervalBitParity_Object = MibTableColumn
prtDs3IntervalBitParity = _PrtDs3IntervalBitParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 13),
    _PrtDs3IntervalBitParity_Type()
)
prtDs3IntervalBitParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalBitParity.setStatus("current")
_PrtDs3IntervalPlcpLOF_Type = Gauge32
_PrtDs3IntervalPlcpLOF_Object = MibTableColumn
prtDs3IntervalPlcpLOF = _PrtDs3IntervalPlcpLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 14),
    _PrtDs3IntervalPlcpLOF_Type()
)
prtDs3IntervalPlcpLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpLOF.setStatus("current")
_PrtDs3IntervalPlcpRAI_Type = Gauge32
_PrtDs3IntervalPlcpRAI_Object = MibTableColumn
prtDs3IntervalPlcpRAI = _PrtDs3IntervalPlcpRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 15),
    _PrtDs3IntervalPlcpRAI_Type()
)
prtDs3IntervalPlcpRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpRAI.setStatus("current")
_PrtDs3IntervalPlcpBIP_Type = Gauge32
_PrtDs3IntervalPlcpBIP_Object = MibTableColumn
prtDs3IntervalPlcpBIP = _PrtDs3IntervalPlcpBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 16),
    _PrtDs3IntervalPlcpBIP_Type()
)
prtDs3IntervalPlcpBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpBIP.setStatus("current")
_PrtDs3IntervalPlcpFEBE_Type = Gauge32
_PrtDs3IntervalPlcpFEBE_Object = MibTableColumn
prtDs3IntervalPlcpFEBE = _PrtDs3IntervalPlcpFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 17),
    _PrtDs3IntervalPlcpFEBE_Type()
)
prtDs3IntervalPlcpFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpFEBE.setStatus("current")
_PrtDs3IntervalBPV_Type = Gauge32
_PrtDs3IntervalBPV_Object = MibTableColumn
prtDs3IntervalBPV = _PrtDs3IntervalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 18),
    _PrtDs3IntervalBPV_Type()
)
prtDs3IntervalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalBPV.setStatus("current")
_PrtDs3IntervalLCE_Type = Gauge32
_PrtDs3IntervalLCE_Object = MibTableColumn
prtDs3IntervalLCE = _PrtDs3IntervalLCE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 19),
    _PrtDs3IntervalLCE_Type()
)
prtDs3IntervalLCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalLCE.setStatus("current")


class _PrtDs3IntervalStatus_Type(OctetString):
    """Custom type prtDs3IntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtDs3IntervalStatus_Type.__name__ = "OctetString"
_PrtDs3IntervalStatus_Object = MibTableColumn
prtDs3IntervalStatus = _PrtDs3IntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 20),
    _PrtDs3IntervalStatus_Type()
)
prtDs3IntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalStatus.setStatus("current")
_PrtDs3TotalTable_Object = MibTable
prtDs3TotalTable = _PrtDs3TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4)
)
if mibBuilder.loadTexts:
    prtDs3TotalTable.setStatus("current")
_PrtDs3TotalEntry_Object = MibTableRow
prtDs3TotalEntry = _PrtDs3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1)
)
prtDs3TotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtDs3TotalEntry.setStatus("current")
_PrtDs3TotalUAS_Type = Gauge32
_PrtDs3TotalUAS_Object = MibTableColumn
prtDs3TotalUAS = _PrtDs3TotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1, 6),
    _PrtDs3TotalUAS_Type()
)
prtDs3TotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3TotalUAS.setStatus("current")
_PrtDs3TotalBPV_Type = Gauge32
_PrtDs3TotalBPV_Object = MibTableColumn
prtDs3TotalBPV = _PrtDs3TotalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1, 17),
    _PrtDs3TotalBPV_Type()
)
prtDs3TotalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3TotalBPV.setStatus("current")
_PrtDs3TotalLCE_Type = Gauge32
_PrtDs3TotalLCE_Object = MibTableColumn
prtDs3TotalLCE = _PrtDs3TotalLCE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1, 18),
    _PrtDs3TotalLCE_Type()
)
prtDs3TotalLCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3TotalLCE.setStatus("current")
_Ds1Interface_ObjectIdentity = ObjectIdentity
ds1Interface = _Ds1Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4)
)
_PrtDs1PerfHistory_ObjectIdentity = ObjectIdentity
prtDs1PerfHistory = _PrtDs1PerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1)
)
_Dsx1XCurrentTable_Object = MibTable
dsx1XCurrentTable = _Dsx1XCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dsx1XCurrentTable.setStatus("current")
_Dsx1XCurrentEntry_Object = MibTableRow
dsx1XCurrentEntry = _Dsx1XCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1)
)
dsx1XCurrentEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1CurrentIndex"),
)
if mibBuilder.loadTexts:
    dsx1XCurrentEntry.setStatus("current")
_Dsx1CurrentLOS_Type = PerfCurrentCount
_Dsx1CurrentLOS_Object = MibTableColumn
dsx1CurrentLOS = _Dsx1CurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 1),
    _Dsx1CurrentLOS_Type()
)
dsx1CurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOS.setStatus("current")
_Dsx1CurrentLOF_Type = PerfCurrentCount
_Dsx1CurrentLOF_Object = MibTableColumn
dsx1CurrentLOF = _Dsx1CurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 2),
    _Dsx1CurrentLOF_Type()
)
dsx1CurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOF.setStatus("current")
_Dsx1CurrentLOC_Type = PerfCurrentCount
_Dsx1CurrentLOC_Object = MibTableColumn
dsx1CurrentLOC = _Dsx1CurrentLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 3),
    _Dsx1CurrentLOC_Type()
)
dsx1CurrentLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOC.setStatus("current")
_Dsx1CurrentAIS_Type = PerfCurrentCount
_Dsx1CurrentAIS_Object = MibTableColumn
dsx1CurrentAIS = _Dsx1CurrentAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 4),
    _Dsx1CurrentAIS_Type()
)
dsx1CurrentAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentAIS.setStatus("current")
_Dsx1CurrentRAI_Type = PerfCurrentCount
_Dsx1CurrentRAI_Object = MibTableColumn
dsx1CurrentRAI = _Dsx1CurrentRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 5),
    _Dsx1CurrentRAI_Type()
)
dsx1CurrentRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentRAI.setStatus("current")
_Dsx1CurrentLOMF_Type = PerfCurrentCount
_Dsx1CurrentLOMF_Object = MibTableColumn
dsx1CurrentLOMF = _Dsx1CurrentLOMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 6),
    _Dsx1CurrentLOMF_Type()
)
dsx1CurrentLOMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOMF.setStatus("current")
_Dsx1CurrentFEBE_Type = PerfCurrentCount
_Dsx1CurrentFEBE_Object = MibTableColumn
dsx1CurrentFEBE = _Dsx1CurrentFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 7),
    _Dsx1CurrentFEBE_Type()
)
dsx1CurrentFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentFEBE.setStatus("current")


class _Dsx1CurrentStatus_Type(OctetString):
    """Custom type dsx1CurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dsx1CurrentStatus_Type.__name__ = "OctetString"
_Dsx1CurrentStatus_Object = MibTableColumn
dsx1CurrentStatus = _Dsx1CurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 8),
    _Dsx1CurrentStatus_Type()
)
dsx1CurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentStatus.setStatus("current")
_Dsx1CurrentBPV_Type = PerfCurrentCount
_Dsx1CurrentBPV_Object = MibTableColumn
dsx1CurrentBPV = _Dsx1CurrentBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 9),
    _Dsx1CurrentBPV_Type()
)
dsx1CurrentBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentBPV.setStatus("current")
_Dsx1CurrentLOCRCMF_Type = PerfCurrentCount
_Dsx1CurrentLOCRCMF_Object = MibTableColumn
dsx1CurrentLOCRCMF = _Dsx1CurrentLOCRCMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 10),
    _Dsx1CurrentLOCRCMF_Type()
)
dsx1CurrentLOCRCMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOCRCMF.setStatus("current")
_Dsx1CurrentLOFC_Type = PerfCurrentCount
_Dsx1CurrentLOFC_Object = MibTableColumn
dsx1CurrentLOFC = _Dsx1CurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 11),
    _Dsx1CurrentLOFC_Type()
)
dsx1CurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOFC.setStatus("current")
_Dsx1XIntervalTable_Object = MibTable
dsx1XIntervalTable = _Dsx1XIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    dsx1XIntervalTable.setStatus("current")
_Dsx1XIntervalEntry_Object = MibTableRow
dsx1XIntervalEntry = _Dsx1XIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1)
)
dsx1XIntervalEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1IntervalIndex"),
    (0, "DS1-MIB", "dsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx1XIntervalEntry.setStatus("current")
_Dsx1IntervalLOS_Type = PerfIntervalCount
_Dsx1IntervalLOS_Object = MibTableColumn
dsx1IntervalLOS = _Dsx1IntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 1),
    _Dsx1IntervalLOS_Type()
)
dsx1IntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOS.setStatus("current")
_Dsx1IntervalLOF_Type = PerfIntervalCount
_Dsx1IntervalLOF_Object = MibTableColumn
dsx1IntervalLOF = _Dsx1IntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 2),
    _Dsx1IntervalLOF_Type()
)
dsx1IntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOF.setStatus("current")
_Dsx1IntervalLOC_Type = PerfIntervalCount
_Dsx1IntervalLOC_Object = MibTableColumn
dsx1IntervalLOC = _Dsx1IntervalLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 3),
    _Dsx1IntervalLOC_Type()
)
dsx1IntervalLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOC.setStatus("current")
_Dsx1IntervalAIS_Type = PerfIntervalCount
_Dsx1IntervalAIS_Object = MibTableColumn
dsx1IntervalAIS = _Dsx1IntervalAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 4),
    _Dsx1IntervalAIS_Type()
)
dsx1IntervalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalAIS.setStatus("current")
_Dsx1IntervalRAI_Type = PerfIntervalCount
_Dsx1IntervalRAI_Object = MibTableColumn
dsx1IntervalRAI = _Dsx1IntervalRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 5),
    _Dsx1IntervalRAI_Type()
)
dsx1IntervalRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalRAI.setStatus("current")
_Dsx1IntervalLOMF_Type = PerfIntervalCount
_Dsx1IntervalLOMF_Object = MibTableColumn
dsx1IntervalLOMF = _Dsx1IntervalLOMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 6),
    _Dsx1IntervalLOMF_Type()
)
dsx1IntervalLOMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOMF.setStatus("current")
_Dsx1IntervalFEBE_Type = PerfIntervalCount
_Dsx1IntervalFEBE_Object = MibTableColumn
dsx1IntervalFEBE = _Dsx1IntervalFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 7),
    _Dsx1IntervalFEBE_Type()
)
dsx1IntervalFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalFEBE.setStatus("current")


class _Dsx1IntervalStatus_Type(OctetString):
    """Custom type dsx1IntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dsx1IntervalStatus_Type.__name__ = "OctetString"
_Dsx1IntervalStatus_Object = MibTableColumn
dsx1IntervalStatus = _Dsx1IntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 8),
    _Dsx1IntervalStatus_Type()
)
dsx1IntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalStatus.setStatus("current")
_Dsx1IntervalBPV_Type = PerfIntervalCount
_Dsx1IntervalBPV_Object = MibTableColumn
dsx1IntervalBPV = _Dsx1IntervalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 9),
    _Dsx1IntervalBPV_Type()
)
dsx1IntervalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalBPV.setStatus("current")
_Dsx1IntervalLOCRCMF_Type = PerfIntervalCount
_Dsx1IntervalLOCRCMF_Object = MibTableColumn
dsx1IntervalLOCRCMF = _Dsx1IntervalLOCRCMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 10),
    _Dsx1IntervalLOCRCMF_Type()
)
dsx1IntervalLOCRCMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOCRCMF.setStatus("current")
_Dsx1IntervalLOFC_Type = PerfIntervalCount
_Dsx1IntervalLOFC_Object = MibTableColumn
dsx1IntervalLOFC = _Dsx1IntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 11),
    _Dsx1IntervalLOFC_Type()
)
dsx1IntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOFC.setStatus("current")
_Dsx1XTotalTable_Object = MibTable
dsx1XTotalTable = _Dsx1XTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4)
)
if mibBuilder.loadTexts:
    dsx1XTotalTable.setStatus("current")
_Dsx1XTotalEntry_Object = MibTableRow
dsx1XTotalEntry = _Dsx1XTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1)
)
dsx1XTotalEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1TotalIndex"),
)
if mibBuilder.loadTexts:
    dsx1XTotalEntry.setStatus("current")
_Dsx1TotalBPV_Type = PerfTotalCount
_Dsx1TotalBPV_Object = MibTableColumn
dsx1TotalBPV = _Dsx1TotalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 9),
    _Dsx1TotalBPV_Type()
)
dsx1TotalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalBPV.setStatus("current")
_Dsx1TotalLOFC_Type = PerfTotalCount
_Dsx1TotalLOFC_Object = MibTableColumn
dsx1TotalLOFC = _Dsx1TotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 11),
    _Dsx1TotalLOFC_Type()
)
dsx1TotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLOFC.setStatus("current")
_Dsx1XConfigTable_Object = MibTable
dsx1XConfigTable = _Dsx1XConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    dsx1XConfigTable.setStatus("current")
_Dsx1XConfigEntry_Object = MibTableRow
dsx1XConfigEntry = _Dsx1XConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1)
)
dsx1XConfigEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    dsx1XConfigEntry.setStatus("current")
_Dsx1IdleCode_Type = Integer32
_Dsx1IdleCode_Object = MibTableColumn
dsx1IdleCode = _Dsx1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 1),
    _Dsx1IdleCode_Type()
)
dsx1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1IdleCode.setStatus("current")


class _Dsx1LineMode_Type(Integer32):
    """Custom type dsx1LineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 1),
          ("dsu", 2))
    )


_Dsx1LineMode_Type.__name__ = "Integer32"
_Dsx1LineMode_Object = MibTableColumn
dsx1LineMode = _Dsx1LineMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 2),
    _Dsx1LineMode_Type()
)
dsx1LineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineMode.setStatus("current")


class _Dsx1dBTxGain_Type(Integer32):
    """Custom type dsx1dBTxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("neg75dB", 2),
          ("neg15dB", 3),
          ("neg225dB", 4),
          ("zerodB", 5))
    )


_Dsx1dBTxGain_Type.__name__ = "Integer32"
_Dsx1dBTxGain_Object = MibTableColumn
dsx1dBTxGain = _Dsx1dBTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 3),
    _Dsx1dBTxGain_Type()
)
dsx1dBTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1dBTxGain.setStatus("current")


class _Dsx1RxSensitivity_Type(Integer32):
    """Custom type dsx1RxSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("neg10dB", 2),
          ("neg32dB", 3))
    )


_Dsx1RxSensitivity_Type.__name__ = "Integer32"
_Dsx1RxSensitivity_Object = MibTableColumn
dsx1RxSensitivity = _Dsx1RxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 4),
    _Dsx1RxSensitivity_Type()
)
dsx1RxSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1RxSensitivity.setStatus("current")


class _Dsx1RestoreTime_Type(Integer32):
    """Custom type dsx1RestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sec1", 2),
          ("sec10", 3))
    )


_Dsx1RestoreTime_Type.__name__ = "Integer32"
_Dsx1RestoreTime_Object = MibTableColumn
dsx1RestoreTime = _Dsx1RestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 5),
    _Dsx1RestoreTime_Type()
)
dsx1RestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1RestoreTime.setStatus("current")
_Dsx1TcFirstSignal_Type = Integer32
_Dsx1TcFirstSignal_Object = MibTableColumn
dsx1TcFirstSignal = _Dsx1TcFirstSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 6),
    _Dsx1TcFirstSignal_Type()
)
dsx1TcFirstSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcFirstSignal.setStatus("current")
_Dsx1TcSignal_Type = Integer32
_Dsx1TcSignal_Object = MibTableColumn
dsx1TcSignal = _Dsx1TcSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 7),
    _Dsx1TcSignal_Type()
)
dsx1TcSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcSignal.setStatus("current")
_Dsx1TcPattern_Type = Integer32
_Dsx1TcPattern_Object = MibTableColumn
dsx1TcPattern = _Dsx1TcPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 8),
    _Dsx1TcPattern_Type()
)
dsx1TcPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcPattern.setStatus("current")


class _Dsx1Scramble_Type(Integer32):
    """Custom type dsx1Scramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("notActive", 2),
          ("active", 3))
    )


_Dsx1Scramble_Type.__name__ = "Integer32"
_Dsx1Scramble_Object = MibTableColumn
dsx1Scramble = _Dsx1Scramble_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 9),
    _Dsx1Scramble_Type()
)
dsx1Scramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1Scramble.setStatus("current")


class _Dsx1LineAdaptiveTimingMode_Type(Integer32):
    """Custom type dsx1LineAdaptiveTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Dsx1LineAdaptiveTimingMode_Type.__name__ = "Integer32"
_Dsx1LineAdaptiveTimingMode_Object = MibTableColumn
dsx1LineAdaptiveTimingMode = _Dsx1LineAdaptiveTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 10),
    _Dsx1LineAdaptiveTimingMode_Type()
)
dsx1LineAdaptiveTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineAdaptiveTimingMode.setStatus("current")


class _Dsx1TxClockSource_Type(Integer32):
    """Custom type dsx1TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4))
    )


_Dsx1TxClockSource_Type.__name__ = "Integer32"
_Dsx1TxClockSource_Object = MibTableColumn
dsx1TxClockSource = _Dsx1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 11),
    _Dsx1TxClockSource_Type()
)
dsx1TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TxClockSource.setStatus("current")


class _Dsx1AisEnable_Type(Integer32):
    """Custom type dsx1AisEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Dsx1AisEnable_Type.__name__ = "Integer32"
_Dsx1AisEnable_Object = MibTableColumn
dsx1AisEnable = _Dsx1AisEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 12),
    _Dsx1AisEnable_Type()
)
dsx1AisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1AisEnable.setStatus("current")


class _Dsx1TsEchoCancel_Type(OctetString):
    """Custom type dsx1TsEchoCancel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dsx1TsEchoCancel_Type.__name__ = "OctetString"
_Dsx1TsEchoCancel_Object = MibTableColumn
dsx1TsEchoCancel = _Dsx1TsEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 13),
    _Dsx1TsEchoCancel_Type()
)
dsx1TsEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TsEchoCancel.setStatus("current")


class _Dsx1EchoCancelerModule_Type(Integer32):
    """Custom type dsx1EchoCancelerModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notExist", 2),
          ("exist", 3))
    )


_Dsx1EchoCancelerModule_Type.__name__ = "Integer32"
_Dsx1EchoCancelerModule_Object = MibTableColumn
dsx1EchoCancelerModule = _Dsx1EchoCancelerModule_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 14),
    _Dsx1EchoCancelerModule_Type()
)
dsx1EchoCancelerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EchoCancelerModule.setStatus("current")
_HdlcMibObjects_ObjectIdentity = ObjectIdentity
hdlcMibObjects = _HdlcMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5)
)
_HdlcTable_Object = MibTable
hdlcTable = _HdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    hdlcTable.setStatus("current")
_HdlcEntry_Object = MibTableRow
hdlcEntry = _HdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1)
)
hdlcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hdlcEntry.setStatus("current")


class _HdlcProtocol_Type(Integer32):
    """Custom type hdlcProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("v35", 2),
          ("x21", 3),
          ("rs530", 4))
    )


_HdlcProtocol_Type.__name__ = "Integer32"
_HdlcProtocol_Object = MibTableColumn
hdlcProtocol = _HdlcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 1),
    _HdlcProtocol_Type()
)
hdlcProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcProtocol.setStatus("current")


class _HdlcRateResolution_Type(Integer32):
    """Custom type hdlcRateResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("nx56Kbps", 2),
          ("nx64Kbps", 3))
    )


_HdlcRateResolution_Type.__name__ = "Integer32"
_HdlcRateResolution_Object = MibTableColumn
hdlcRateResolution = _HdlcRateResolution_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 2),
    _HdlcRateResolution_Type()
)
hdlcRateResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcRateResolution.setStatus("current")


class _HdlcTxClockSource_Type(Integer32):
    """Custom type hdlcTxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_HdlcTxClockSource_Type.__name__ = "Integer32"
_HdlcTxClockSource_Object = MibTableColumn
hdlcTxClockSource = _HdlcTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 3),
    _HdlcTxClockSource_Type()
)
hdlcTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcTxClockSource.setStatus("current")


class _HdlcTerminalMode_Type(Integer32):
    """Custom type hdlcTerminalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_HdlcTerminalMode_Type.__name__ = "Integer32"
_HdlcTerminalMode_Object = MibTableColumn
hdlcTerminalMode = _HdlcTerminalMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 4),
    _HdlcTerminalMode_Type()
)
hdlcTerminalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcTerminalMode.setStatus("current")


class _HdlcLoopbackState_Type(Integer32):
    """Custom type hdlcLoopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("internal", 2),
          ("external", 3),
          ("disable", 4))
    )


_HdlcLoopbackState_Type.__name__ = "Integer32"
_HdlcLoopbackState_Object = MibTableColumn
hdlcLoopbackState = _HdlcLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 5),
    _HdlcLoopbackState_Type()
)
hdlcLoopbackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcLoopbackState.setStatus("current")


class _HdlcTxClockPolarity_Type(Integer32):
    """Custom type hdlcTxClockPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("inverse", 2))
    )


_HdlcTxClockPolarity_Type.__name__ = "Integer32"
_HdlcTxClockPolarity_Object = MibTableColumn
hdlcTxClockPolarity = _HdlcTxClockPolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 6),
    _HdlcTxClockPolarity_Type()
)
hdlcTxClockPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcTxClockPolarity.setStatus("current")


class _HdlcFlowControl_Type(Integer32):
    """Custom type hdlcFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HdlcFlowControl_Type.__name__ = "Integer32"
_HdlcFlowControl_Object = MibTableColumn
hdlcFlowControl = _HdlcFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 7),
    _HdlcFlowControl_Type()
)
hdlcFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcFlowControl.setStatus("current")
_HdlcLineRate_Type = Integer32
_HdlcLineRate_Object = MibTableColumn
hdlcLineRate = _HdlcLineRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 8),
    _HdlcLineRate_Type()
)
hdlcLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcLineRate.setStatus("current")


class _HdlcRxClockMode_Type(Integer32):
    """Custom type hdlcRxClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("internal", 2),
          ("external", 3))
    )


_HdlcRxClockMode_Type.__name__ = "Integer32"
_HdlcRxClockMode_Object = MibTableColumn
hdlcRxClockMode = _HdlcRxClockMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 9),
    _HdlcRxClockMode_Type()
)
hdlcRxClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcRxClockMode.setStatus("current")
_HdlcLOF_Type = Gauge32
_HdlcLOF_Object = MibTableColumn
hdlcLOF = _HdlcLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 10),
    _HdlcLOF_Type()
)
hdlcLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLOF.setStatus("current")


class _HdlcRxClockPolarity_Type(Integer32):
    """Custom type hdlcRxClockPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("inverse", 2))
    )


_HdlcRxClockPolarity_Type.__name__ = "Integer32"
_HdlcRxClockPolarity_Object = MibTableColumn
hdlcRxClockPolarity = _HdlcRxClockPolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 5, 1, 1, 11),
    _HdlcRxClockPolarity_Type()
)
hdlcRxClockPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcRxClockPolarity.setStatus("current")
_DacsMux_ObjectIdentity = ObjectIdentity
dacsMux = _DacsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3)
)
_SystemDacsMux_ObjectIdentity = ObjectIdentity
systemDacsMux = _SystemDacsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1)
)
_SysStatus_ObjectIdentity = ObjectIdentity
sysStatus = _SysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3)
)


class _SysSClkSrc_Type(Integer32):
    """Custom type sysSClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("fallback", 2),
          ("internal", 3),
          ("ml", 4))
    )


_SysSClkSrc_Type.__name__ = "Integer32"
_SysSClkSrc_Object = MibScalar
sysSClkSrc = _SysSClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 7),
    _SysSClkSrc_Type()
)
sysSClkSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSClkSrc.setStatus("current")
_SysConfig_ObjectIdentity = ObjectIdentity
sysConfig = _SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6)
)
_SysCClkSrcTable_Object = MibTable
sysCClkSrcTable = _SysCClkSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sysCClkSrcTable.setStatus("current")
_SysCClkSrcEntry_Object = MibTableRow
sysCClkSrcEntry = _SysCClkSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1)
)
sysCClkSrcEntry.setIndexNames(
    (0, "ACE202-MIB", "sysCClkCnfgIdx"),
    (0, "ACE202-MIB", "sysCClkSrcIdx"),
)
if mibBuilder.loadTexts:
    sysCClkSrcEntry.setStatus("current")


class _SysCClkCnfgIdx_Type(Integer32):
    """Custom type sysCClkCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysCClkCnfgIdx_Type.__name__ = "Integer32"
_SysCClkCnfgIdx_Object = MibTableColumn
sysCClkCnfgIdx = _SysCClkCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 1),
    _SysCClkCnfgIdx_Type()
)
sysCClkCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCClkCnfgIdx.setStatus("current")


class _SysCClkSrcIdx_Type(Integer32):
    """Custom type sysCClkSrcIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("fallback", 2))
    )


_SysCClkSrcIdx_Type.__name__ = "Integer32"
_SysCClkSrcIdx_Object = MibTableColumn
sysCClkSrcIdx = _SysCClkSrcIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 2),
    _SysCClkSrcIdx_Type()
)
sysCClkSrcIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCClkSrcIdx.setStatus("current")


class _SysCClkSrcMode_Type(Integer32):
    """Custom type sysCClkSrcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("internal", 2),
          ("rxClk", 3),
          ("station", 4),
          ("lbt", 5),
          ("ntr", 6),
          ("adaptive", 7),
          ("notApplicable", 255))
    )


_SysCClkSrcMode_Type.__name__ = "Integer32"
_SysCClkSrcMode_Object = MibTableColumn
sysCClkSrcMode = _SysCClkSrcMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 3),
    _SysCClkSrcMode_Type()
)
sysCClkSrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkSrcMode.setStatus("current")
_SysCClkSrcPrt_Type = Integer32
_SysCClkSrcPrt_Object = MibTableColumn
sysCClkSrcPrt = _SysCClkSrcPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 4),
    _SysCClkSrcPrt_Type()
)
sysCClkSrcPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkSrcPrt.setStatus("current")


class _SysCClkStationFreq_Type(Integer32):
    """Custom type sysCClkStationFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("f1544Khz", 2),
          ("f2048Khz", 3))
    )


_SysCClkStationFreq_Type.__name__ = "Integer32"
_SysCClkStationFreq_Object = MibTableColumn
sysCClkStationFreq = _SysCClkStationFreq_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 5),
    _SysCClkStationFreq_Type()
)
sysCClkStationFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkStationFreq.setStatus("current")
_SysCClkRevertiveTimeout_Type = Integer32
_SysCClkRevertiveTimeout_Object = MibTableColumn
sysCClkRevertiveTimeout = _SysCClkRevertiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 6),
    _SysCClkRevertiveTimeout_Type()
)
sysCClkRevertiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkRevertiveTimeout.setStatus("current")
_RadBridges_ObjectIdentity = ObjectIdentity
radBridges = _RadBridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4)
)
_GenBridge_ObjectIdentity = ObjectIdentity
genBridge = _GenBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1)
)


class _RadBridgeAction_Type(Integer32):
    """Custom type radBridgeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("sendNetworkTab", 2),
          ("deleteNetworkTab", 3),
          ("sendRoutingTab", 4),
          ("deleteRoutinTab", 5),
          ("sendLanTab", 6),
          ("deleteLanTab", 7),
          ("deleteArpTab", 8),
          ("sendArpTab", 9),
          ("deleteRouteTab", 10),
          ("sendRouteTab", 11),
          ("deactivateAllMasks", 12),
          ("saveAllActiveMasks", 13),
          ("loadAndActivateAllMasksFromNVRAM", 14),
          ("clearAllMasksFromNVRAM", 15),
          ("defaultConfig", 16),
          ("resetNVRAM", 17),
          ("clearIPNVRAM", 18),
          ("noOp", 255))
    )


_RadBridgeAction_Type.__name__ = "Integer32"
_RadBridgeAction_Object = MibScalar
radBridgeAction = _RadBridgeAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 1),
    _RadBridgeAction_Type()
)
radBridgeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeAction.setStatus("current")
_RadBridgeInactiveArpTimeOut_Type = Integer32
_RadBridgeInactiveArpTimeOut_Object = MibScalar
radBridgeInactiveArpTimeOut = _RadBridgeInactiveArpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 2),
    _RadBridgeInactiveArpTimeOut_Type()
)
radBridgeInactiveArpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeInactiveArpTimeOut.setStatus("current")
_RadBridgeMaskTable_Object = MibTable
radBridgeMaskTable = _RadBridgeMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3)
)
if mibBuilder.loadTexts:
    radBridgeMaskTable.setStatus("current")
_RadBridgeMaskEntry_Object = MibTableRow
radBridgeMaskEntry = _RadBridgeMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1)
)
radBridgeMaskEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeMaskType"),
    (0, "ACE202-MIB", "radBridgeMaskIfIndex"),
    (0, "ACE202-MIB", "radBridgeMaskNum"),
)
if mibBuilder.loadTexts:
    radBridgeMaskEntry.setStatus("current")


class _RadBridgeMaskType_Type(Integer32):
    """Custom type radBridgeMaskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2),
          ("compress", 3),
          ("priority", 4),
          ("loadSharing", 5),
          ("facs", 6),
          ("codConnect", 7),
          ("codDisconnect", 8))
    )


_RadBridgeMaskType_Type.__name__ = "Integer32"
_RadBridgeMaskType_Object = MibTableColumn
radBridgeMaskType = _RadBridgeMaskType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 1),
    _RadBridgeMaskType_Type()
)
radBridgeMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskType.setStatus("current")
_RadBridgeMaskIfIndex_Type = Integer32
_RadBridgeMaskIfIndex_Object = MibTableColumn
radBridgeMaskIfIndex = _RadBridgeMaskIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 2),
    _RadBridgeMaskIfIndex_Type()
)
radBridgeMaskIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskIfIndex.setStatus("current")
_RadBridgeMaskNum_Type = Integer32
_RadBridgeMaskNum_Object = MibTableColumn
radBridgeMaskNum = _RadBridgeMaskNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 3),
    _RadBridgeMaskNum_Type()
)
radBridgeMaskNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskNum.setStatus("current")


class _RadBridgeMaskDest_Type(Integer32):
    """Custom type radBridgeMaskDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unassigned-cond", 1),
          ("broadcast-msge", 2),
          ("multicast-msge", 3),
          ("all-msge", 4),
          ("none", 5))
    )


_RadBridgeMaskDest_Type.__name__ = "Integer32"
_RadBridgeMaskDest_Object = MibTableColumn
radBridgeMaskDest = _RadBridgeMaskDest_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 4),
    _RadBridgeMaskDest_Type()
)
radBridgeMaskDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskDest.setStatus("current")
_RadBridgeMaskPat1_Type = OctetString
_RadBridgeMaskPat1_Object = MibTableColumn
radBridgeMaskPat1 = _RadBridgeMaskPat1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 5),
    _RadBridgeMaskPat1_Type()
)
radBridgeMaskPat1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskPat1.setStatus("current")
_RadBridgeMaskActiveBit1_Type = OctetString
_RadBridgeMaskActiveBit1_Object = MibTableColumn
radBridgeMaskActiveBit1 = _RadBridgeMaskActiveBit1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 6),
    _RadBridgeMaskActiveBit1_Type()
)
radBridgeMaskActiveBit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskActiveBit1.setStatus("current")


class _RadBridgeMaskFrom1_Type(Integer32):
    """Custom type radBridgeMaskFrom1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("llc", 2),
          ("net", 3))
    )


_RadBridgeMaskFrom1_Type.__name__ = "Integer32"
_RadBridgeMaskFrom1_Object = MibTableColumn
radBridgeMaskFrom1 = _RadBridgeMaskFrom1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 7),
    _RadBridgeMaskFrom1_Type()
)
radBridgeMaskFrom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskFrom1.setStatus("current")
_RadBridgeMaskOffset1_Type = Integer32
_RadBridgeMaskOffset1_Object = MibTableColumn
radBridgeMaskOffset1 = _RadBridgeMaskOffset1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 8),
    _RadBridgeMaskOffset1_Type()
)
radBridgeMaskOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOffset1.setStatus("current")


class _RadBridgeMaskCond1_Type(Integer32):
    """Custom type radBridgeMaskCond1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RadBridgeMaskCond1_Type.__name__ = "Integer32"
_RadBridgeMaskCond1_Object = MibTableColumn
radBridgeMaskCond1 = _RadBridgeMaskCond1_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 9),
    _RadBridgeMaskCond1_Type()
)
radBridgeMaskCond1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskCond1.setStatus("current")
_RadBridgeMaskPat2_Type = OctetString
_RadBridgeMaskPat2_Object = MibTableColumn
radBridgeMaskPat2 = _RadBridgeMaskPat2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 10),
    _RadBridgeMaskPat2_Type()
)
radBridgeMaskPat2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskPat2.setStatus("current")
_RadBridgeMaskActiveBit2_Type = OctetString
_RadBridgeMaskActiveBit2_Object = MibTableColumn
radBridgeMaskActiveBit2 = _RadBridgeMaskActiveBit2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 11),
    _RadBridgeMaskActiveBit2_Type()
)
radBridgeMaskActiveBit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskActiveBit2.setStatus("current")


class _RadBridgeMaskFrom2_Type(Integer32):
    """Custom type radBridgeMaskFrom2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("llc", 2),
          ("net", 3))
    )


_RadBridgeMaskFrom2_Type.__name__ = "Integer32"
_RadBridgeMaskFrom2_Object = MibTableColumn
radBridgeMaskFrom2 = _RadBridgeMaskFrom2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 12),
    _RadBridgeMaskFrom2_Type()
)
radBridgeMaskFrom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskFrom2.setStatus("current")
_RadBridgeMaskOffset2_Type = Integer32
_RadBridgeMaskOffset2_Object = MibTableColumn
radBridgeMaskOffset2 = _RadBridgeMaskOffset2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 13),
    _RadBridgeMaskOffset2_Type()
)
radBridgeMaskOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOffset2.setStatus("current")


class _RadBridgeMaskCond2_Type(Integer32):
    """Custom type radBridgeMaskCond2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RadBridgeMaskCond2_Type.__name__ = "Integer32"
_RadBridgeMaskCond2_Object = MibTableColumn
radBridgeMaskCond2 = _RadBridgeMaskCond2_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 14),
    _RadBridgeMaskCond2_Type()
)
radBridgeMaskCond2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskCond2.setStatus("current")
_RadBridgeMaskPat3_Type = OctetString
_RadBridgeMaskPat3_Object = MibTableColumn
radBridgeMaskPat3 = _RadBridgeMaskPat3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 15),
    _RadBridgeMaskPat3_Type()
)
radBridgeMaskPat3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskPat3.setStatus("current")
_RadBridgeMaskActiveBit3_Type = OctetString
_RadBridgeMaskActiveBit3_Object = MibTableColumn
radBridgeMaskActiveBit3 = _RadBridgeMaskActiveBit3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 16),
    _RadBridgeMaskActiveBit3_Type()
)
radBridgeMaskActiveBit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskActiveBit3.setStatus("current")


class _RadBridgeMaskFrom3_Type(Integer32):
    """Custom type radBridgeMaskFrom3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("llc", 2),
          ("net", 3))
    )


_RadBridgeMaskFrom3_Type.__name__ = "Integer32"
_RadBridgeMaskFrom3_Object = MibTableColumn
radBridgeMaskFrom3 = _RadBridgeMaskFrom3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 17),
    _RadBridgeMaskFrom3_Type()
)
radBridgeMaskFrom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskFrom3.setStatus("current")
_RadBridgeMaskOffset3_Type = Integer32
_RadBridgeMaskOffset3_Object = MibTableColumn
radBridgeMaskOffset3 = _RadBridgeMaskOffset3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 18),
    _RadBridgeMaskOffset3_Type()
)
radBridgeMaskOffset3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOffset3.setStatus("current")


class _RadBridgeMaskCond3_Type(Integer32):
    """Custom type radBridgeMaskCond3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RadBridgeMaskCond3_Type.__name__ = "Integer32"
_RadBridgeMaskCond3_Object = MibTableColumn
radBridgeMaskCond3 = _RadBridgeMaskCond3_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 19),
    _RadBridgeMaskCond3_Type()
)
radBridgeMaskCond3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskCond3.setStatus("current")


class _RadBridgeMaskOper_Type(Integer32):
    """Custom type radBridgeMaskOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("route", 3),
          ("forward-route", 4),
          ("high-priority", 5),
          ("noOp", 6),
          ("delete", 7))
    )


_RadBridgeMaskOper_Type.__name__ = "Integer32"
_RadBridgeMaskOper_Object = MibTableColumn
radBridgeMaskOper = _RadBridgeMaskOper_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 3, 1, 20),
    _RadBridgeMaskOper_Type()
)
radBridgeMaskOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeMaskOper.setStatus("current")
_RadBridgeCOD_ObjectIdentity = ObjectIdentity
radBridgeCOD = _RadBridgeCOD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4)
)
_RadBridgeCODParamTable_Object = MibTable
radBridgeCODParamTable = _RadBridgeCODParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    radBridgeCODParamTable.setStatus("current")
_RadBridgeCODEntry_Object = MibTableRow
radBridgeCODEntry = _RadBridgeCODEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1)
)
radBridgeCODEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeCODIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeCODEntry.setStatus("current")
_RadBridgeCODIfIndex_Type = Integer32
_RadBridgeCODIfIndex_Object = MibTableColumn
radBridgeCODIfIndex = _RadBridgeCODIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 1),
    _RadBridgeCODIfIndex_Type()
)
radBridgeCODIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODIfIndex.setStatus("current")


class _RadBridgeCODManualConnect_Type(Integer32):
    """Custom type radBridgeCODManualConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2))
    )


_RadBridgeCODManualConnect_Type.__name__ = "Integer32"
_RadBridgeCODManualConnect_Object = MibTableColumn
radBridgeCODManualConnect = _RadBridgeCODManualConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 2),
    _RadBridgeCODManualConnect_Type()
)
radBridgeCODManualConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODManualConnect.setStatus("current")


class _RadBridgeCODMode_Type(Integer32):
    """Custom type radBridgeCODMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2),
          ("disable", 3),
          ("answerAndOriginate", 4))
    )


_RadBridgeCODMode_Type.__name__ = "Integer32"
_RadBridgeCODMode_Object = MibTableColumn
radBridgeCODMode = _RadBridgeCODMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 3),
    _RadBridgeCODMode_Type()
)
radBridgeCODMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODMode.setStatus("current")
_RadBridgeCODConnectDelay_Type = Integer32
_RadBridgeCODConnectDelay_Object = MibTableColumn
radBridgeCODConnectDelay = _RadBridgeCODConnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 4),
    _RadBridgeCODConnectDelay_Type()
)
radBridgeCODConnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODConnectDelay.setStatus("current")
_RadBridgeCODisConnectDelay_Type = Integer32
_RadBridgeCODisConnectDelay_Object = MibTableColumn
radBridgeCODisConnectDelay = _RadBridgeCODisConnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 5),
    _RadBridgeCODisConnectDelay_Type()
)
radBridgeCODisConnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODisConnectDelay.setStatus("current")


class _RadBridgeCODImplicitSwitch_Type(Integer32):
    """Custom type radBridgeCODImplicitSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RadBridgeCODImplicitSwitch_Type.__name__ = "Integer32"
_RadBridgeCODImplicitSwitch_Object = MibTableColumn
radBridgeCODImplicitSwitch = _RadBridgeCODImplicitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 6),
    _RadBridgeCODImplicitSwitch_Type()
)
radBridgeCODImplicitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODImplicitSwitch.setStatus("current")
_RadBridgeCODNumAccess_Type = Counter32
_RadBridgeCODNumAccess_Object = MibTableColumn
radBridgeCODNumAccess = _RadBridgeCODNumAccess_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 7),
    _RadBridgeCODNumAccess_Type()
)
radBridgeCODNumAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODNumAccess.setStatus("current")
_RadBridgeCODTotalConnecTime_Type = Integer32
_RadBridgeCODTotalConnecTime_Object = MibTableColumn
radBridgeCODTotalConnecTime = _RadBridgeCODTotalConnecTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 1, 1, 8),
    _RadBridgeCODTotalConnecTime_Type()
)
radBridgeCODTotalConnecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODTotalConnecTime.setStatus("current")
_RadBridgeCODTimeTriggerTable_Object = MibTable
radBridgeCODTimeTriggerTable = _RadBridgeCODTimeTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerTable.setStatus("current")
_RadBridgeCODTimeTriggerEntry_Object = MibTableRow
radBridgeCODTimeTriggerEntry = _RadBridgeCODTimeTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1)
)
radBridgeCODTimeTriggerEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeCODTimeIfIndex"),
    (0, "ACE202-MIB", "radBridgeCODDay"),
    (0, "ACE202-MIB", "radBridgeCODTimeTriggerNum"),
)
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerEntry.setStatus("current")
_RadBridgeCODTimeIfIndex_Type = Integer32
_RadBridgeCODTimeIfIndex_Object = MibTableColumn
radBridgeCODTimeIfIndex = _RadBridgeCODTimeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 1),
    _RadBridgeCODTimeIfIndex_Type()
)
radBridgeCODTimeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODTimeIfIndex.setStatus("current")


class _RadBridgeCODDay_Type(Integer32):
    """Custom type radBridgeCODDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6),
          ("sun", 7))
    )


_RadBridgeCODDay_Type.__name__ = "Integer32"
_RadBridgeCODDay_Object = MibTableColumn
radBridgeCODDay = _RadBridgeCODDay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 2),
    _RadBridgeCODDay_Type()
)
radBridgeCODDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODDay.setStatus("current")


class _RadBridgeCODTimeTriggerNum_Type(Integer32):
    """Custom type radBridgeCODTimeTriggerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RadBridgeCODTimeTriggerNum_Type.__name__ = "Integer32"
_RadBridgeCODTimeTriggerNum_Object = MibTableColumn
radBridgeCODTimeTriggerNum = _RadBridgeCODTimeTriggerNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 3),
    _RadBridgeCODTimeTriggerNum_Type()
)
radBridgeCODTimeTriggerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerNum.setStatus("current")
_RadBridgeCODTimeTriggerFrom_Type = DisplayString
_RadBridgeCODTimeTriggerFrom_Object = MibTableColumn
radBridgeCODTimeTriggerFrom = _RadBridgeCODTimeTriggerFrom_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 4),
    _RadBridgeCODTimeTriggerFrom_Type()
)
radBridgeCODTimeTriggerFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerFrom.setStatus("current")
_RadBridgeCODTimeTriggerTo_Type = DisplayString
_RadBridgeCODTimeTriggerTo_Object = MibTableColumn
radBridgeCODTimeTriggerTo = _RadBridgeCODTimeTriggerTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 5),
    _RadBridgeCODTimeTriggerTo_Type()
)
radBridgeCODTimeTriggerTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerTo.setStatus("current")


class _RadBridgeCODTimeTriggerStatus_Type(Integer32):
    """Custom type radBridgeCODTimeTriggerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RadBridgeCODTimeTriggerStatus_Type.__name__ = "Integer32"
_RadBridgeCODTimeTriggerStatus_Object = MibTableColumn
radBridgeCODTimeTriggerStatus = _RadBridgeCODTimeTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 2, 1, 6),
    _RadBridgeCODTimeTriggerStatus_Type()
)
radBridgeCODTimeTriggerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTimeTriggerStatus.setStatus("current")
_RadBridgeCODTraffic_ObjectIdentity = ObjectIdentity
radBridgeCODTraffic = _RadBridgeCODTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3)
)
_RadBridgeCODTrafficTable_Object = MibTable
radBridgeCODTrafficTable = _RadBridgeCODTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    radBridgeCODTrafficTable.setStatus("current")
_RadBridgeCODTrafficEntry_Object = MibTableRow
radBridgeCODTrafficEntry = _RadBridgeCODTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1, 1)
)
radBridgeCODTrafficEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeCODProtocolType"),
)
if mibBuilder.loadTexts:
    radBridgeCODTrafficEntry.setStatus("current")


class _RadBridgeCODProtocolType_Type(Integer32):
    """Custom type radBridgeCODProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2),
          ("other", 3))
    )


_RadBridgeCODProtocolType_Type.__name__ = "Integer32"
_RadBridgeCODProtocolType_Object = MibTableColumn
radBridgeCODProtocolType = _RadBridgeCODProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1, 1, 1),
    _RadBridgeCODProtocolType_Type()
)
radBridgeCODProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODProtocolType.setStatus("current")


class _RadBridgeCODTrafficTriggerStatus_Type(Integer32):
    """Custom type radBridgeCODTrafficTriggerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RadBridgeCODTrafficTriggerStatus_Type.__name__ = "Integer32"
_RadBridgeCODTrafficTriggerStatus_Object = MibTableColumn
radBridgeCODTrafficTriggerStatus = _RadBridgeCODTrafficTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 1, 1, 2),
    _RadBridgeCODTrafficTriggerStatus_Type()
)
radBridgeCODTrafficTriggerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTrafficTriggerStatus.setStatus("current")
_RadBridgeCODRemoteIPAddr_Type = IpAddress
_RadBridgeCODRemoteIPAddr_Object = MibScalar
radBridgeCODRemoteIPAddr = _RadBridgeCODRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 2),
    _RadBridgeCODRemoteIPAddr_Type()
)
radBridgeCODRemoteIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODRemoteIPAddr.setStatus("current")
_RadBridgeCODIPMask_Type = IpAddress
_RadBridgeCODIPMask_Object = MibScalar
radBridgeCODIPMask = _RadBridgeCODIPMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 3),
    _RadBridgeCODIPMask_Type()
)
radBridgeCODIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODIPMask.setStatus("current")
_RadBridgeCODTrafficTriggerProtType_Type = OctetString
_RadBridgeCODTrafficTriggerProtType_Object = MibScalar
radBridgeCODTrafficTriggerProtType = _RadBridgeCODTrafficTriggerProtType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 3, 4),
    _RadBridgeCODTrafficTriggerProtType_Type()
)
radBridgeCODTrafficTriggerProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODTrafficTriggerProtType.setStatus("current")
_RadBridgeCODCondTable_Object = MibTable
radBridgeCODCondTable = _RadBridgeCODCondTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    radBridgeCODCondTable.setStatus("current")
_RadBridgeCODCondEntry_Object = MibTableRow
radBridgeCODCondEntry = _RadBridgeCODCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1)
)
radBridgeCODCondEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeCODCondIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeCODCondEntry.setStatus("current")
_RadBridgeCODCondIfIndex_Type = Integer32
_RadBridgeCODCondIfIndex_Object = MibTableColumn
radBridgeCODCondIfIndex = _RadBridgeCODCondIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 1),
    _RadBridgeCODCondIfIndex_Type()
)
radBridgeCODCondIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODCondIfIndex.setStatus("current")


class _RadBridgeCODOriginateConnectCondition_Type(Integer32):
    """Custom type radBridgeCODOriginateConnectCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("onPowerOn", 1),
          ("whenAnyStationOnLan", 2),
          ("onTraffic", 3),
          ("onManualConnect", 4))
    )


_RadBridgeCODOriginateConnectCondition_Type.__name__ = "Integer32"
_RadBridgeCODOriginateConnectCondition_Object = MibTableColumn
radBridgeCODOriginateConnectCondition = _RadBridgeCODOriginateConnectCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 2),
    _RadBridgeCODOriginateConnectCondition_Type()
)
radBridgeCODOriginateConnectCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODOriginateConnectCondition.setStatus("current")


class _RadBridgeCODOriginateDisConnectCondition_Type(Integer32):
    """Custom type radBridgeCODOriginateDisConnectCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noStationOnLan", 1),
          ("onTraffic", 2),
          ("onDelayFromConnectionOnRequest", 3),
          ("onManualDisConnect", 4))
    )


_RadBridgeCODOriginateDisConnectCondition_Type.__name__ = "Integer32"
_RadBridgeCODOriginateDisConnectCondition_Object = MibTableColumn
radBridgeCODOriginateDisConnectCondition = _RadBridgeCODOriginateDisConnectCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 3),
    _RadBridgeCODOriginateDisConnectCondition_Type()
)
radBridgeCODOriginateDisConnectCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODOriginateDisConnectCondition.setStatus("current")
_RadBridgeCODOriginateDisConnectDelay_Type = Integer32
_RadBridgeCODOriginateDisConnectDelay_Object = MibTableColumn
radBridgeCODOriginateDisConnectDelay = _RadBridgeCODOriginateDisConnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 4),
    _RadBridgeCODOriginateDisConnectDelay_Type()
)
radBridgeCODOriginateDisConnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODOriginateDisConnectDelay.setStatus("current")


class _RadBridgeCODAnswerConnectCondition_Type(Integer32):
    """Custom type radBridgeCODAnswerConnectCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("onPowerOn", 1),
          ("whenAnyStationOnLan", 2),
          ("onTraffic", 3),
          ("onManualConnect", 4))
    )


_RadBridgeCODAnswerConnectCondition_Type.__name__ = "Integer32"
_RadBridgeCODAnswerConnectCondition_Object = MibTableColumn
radBridgeCODAnswerConnectCondition = _RadBridgeCODAnswerConnectCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 5),
    _RadBridgeCODAnswerConnectCondition_Type()
)
radBridgeCODAnswerConnectCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODAnswerConnectCondition.setStatus("current")
_RadBridgeCODSpecificOnTrafficOIDCondition_Type = ObjectIdentifier
_RadBridgeCODSpecificOnTrafficOIDCondition_Object = MibTableColumn
radBridgeCODSpecificOnTrafficOIDCondition = _RadBridgeCODSpecificOnTrafficOIDCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 6),
    _RadBridgeCODSpecificOnTrafficOIDCondition_Type()
)
radBridgeCODSpecificOnTrafficOIDCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeCODSpecificOnTrafficOIDCondition.setStatus("current")
_RadBridgeCODDisConnectMinimunFramesNumber_Type = Integer32
_RadBridgeCODDisConnectMinimunFramesNumber_Object = MibTableColumn
radBridgeCODDisConnectMinimunFramesNumber = _RadBridgeCODDisConnectMinimunFramesNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 4, 4, 1, 7),
    _RadBridgeCODDisConnectMinimunFramesNumber_Type()
)
radBridgeCODDisConnectMinimunFramesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeCODDisConnectMinimunFramesNumber.setStatus("current")
_RadBridgeIPX_ObjectIdentity = ObjectIdentity
radBridgeIPX = _RadBridgeIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5)
)
_RadBridgeIPXdriver_ObjectIdentity = ObjectIdentity
radBridgeIPXdriver = _RadBridgeIPXdriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 1)
)


class _RadBridgeIPXForwarding_Type(Integer32):
    """Custom type radBridgeIPXForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_RadBridgeIPXForwarding_Type.__name__ = "Integer32"
_RadBridgeIPXForwarding_Object = MibScalar
radBridgeIPXForwarding = _RadBridgeIPXForwarding_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 1, 1),
    _RadBridgeIPXForwarding_Type()
)
radBridgeIPXForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXForwarding.setStatus("current")
_RadBridgeIPXRip_ObjectIdentity = ObjectIdentity
radBridgeIPXRip = _RadBridgeIPXRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2)
)
_RadBridgeIPXRipOutPackets_Type = Counter32
_RadBridgeIPXRipOutPackets_Object = MibScalar
radBridgeIPXRipOutPackets = _RadBridgeIPXRipOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 1),
    _RadBridgeIPXRipOutPackets_Type()
)
radBridgeIPXRipOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipOutPackets.setStatus("current")
_RadBridgeIPXRipInPackets_Type = Counter32
_RadBridgeIPXRipInPackets_Object = MibScalar
radBridgeIPXRipInPackets = _RadBridgeIPXRipInPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 2),
    _RadBridgeIPXRipInPackets_Type()
)
radBridgeIPXRipInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipInPackets.setStatus("current")
_RadBridgeIPXRipInDiscards_Type = Counter32
_RadBridgeIPXRipInDiscards_Object = MibScalar
radBridgeIPXRipInDiscards = _RadBridgeIPXRipInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 3),
    _RadBridgeIPXRipInDiscards_Type()
)
radBridgeIPXRipInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipInDiscards.setStatus("current")
_RadBridgeIPXRipTblNoOfEntries_Type = Integer32
_RadBridgeIPXRipTblNoOfEntries_Object = MibScalar
radBridgeIPXRipTblNoOfEntries = _RadBridgeIPXRipTblNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 4),
    _RadBridgeIPXRipTblNoOfEntries_Type()
)
radBridgeIPXRipTblNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipTblNoOfEntries.setStatus("current")
_RadBridgeIPXRipTblBcastTrigUpdateInterval_Type = Integer32
_RadBridgeIPXRipTblBcastTrigUpdateInterval_Object = MibScalar
radBridgeIPXRipTblBcastTrigUpdateInterval = _RadBridgeIPXRipTblBcastTrigUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 5),
    _RadBridgeIPXRipTblBcastTrigUpdateInterval_Type()
)
radBridgeIPXRipTblBcastTrigUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipTblBcastTrigUpdateInterval.setStatus("current")
_RadBridgeIPXRipTable_Object = MibTable
radBridgeIPXRipTable = _RadBridgeIPXRipTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    radBridgeIPXRipTable.setStatus("current")
_RadBridgeIPXRipTableEntry_Object = MibTableRow
radBridgeIPXRipTableEntry = _RadBridgeIPXRipTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1)
)
radBridgeIPXRipTableEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeIPXRipDestNetwork"),
    (0, "ACE202-MIB", "radBridgeIPXRipPolicy"),
)
if mibBuilder.loadTexts:
    radBridgeIPXRipTableEntry.setStatus("current")


class _RadBridgeIPXRipDestNetwork_Type(OctetString):
    """Custom type radBridgeIPXRipDestNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RadBridgeIPXRipDestNetwork_Type.__name__ = "OctetString"
_RadBridgeIPXRipDestNetwork_Object = MibTableColumn
radBridgeIPXRipDestNetwork = _RadBridgeIPXRipDestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 1),
    _RadBridgeIPXRipDestNetwork_Type()
)
radBridgeIPXRipDestNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipDestNetwork.setStatus("current")


class _RadBridgeIPXRipPolicy_Type(Integer32):
    """Custom type radBridgeIPXRipPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("alternate", 2))
    )


_RadBridgeIPXRipPolicy_Type.__name__ = "Integer32"
_RadBridgeIPXRipPolicy_Object = MibTableColumn
radBridgeIPXRipPolicy = _RadBridgeIPXRipPolicy_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 2),
    _RadBridgeIPXRipPolicy_Type()
)
radBridgeIPXRipPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipPolicy.setStatus("current")


class _RadBridgeIPXRipForwardingRouter_Type(OctetString):
    """Custom type radBridgeIPXRipForwardingRouter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RadBridgeIPXRipForwardingRouter_Type.__name__ = "OctetString"
_RadBridgeIPXRipForwardingRouter_Object = MibTableColumn
radBridgeIPXRipForwardingRouter = _RadBridgeIPXRipForwardingRouter_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 3),
    _RadBridgeIPXRipForwardingRouter_Type()
)
radBridgeIPXRipForwardingRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipForwardingRouter.setStatus("current")
_RadBridgeIPXRipNIC_Type = Integer32
_RadBridgeIPXRipNIC_Object = MibTableColumn
radBridgeIPXRipNIC = _RadBridgeIPXRipNIC_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 4),
    _RadBridgeIPXRipNIC_Type()
)
radBridgeIPXRipNIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipNIC.setStatus("current")
_RadBridgeIPXRipTickMetric_Type = Integer32
_RadBridgeIPXRipTickMetric_Object = MibTableColumn
radBridgeIPXRipTickMetric = _RadBridgeIPXRipTickMetric_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 5),
    _RadBridgeIPXRipTickMetric_Type()
)
radBridgeIPXRipTickMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipTickMetric.setStatus("current")
_RadBridgeIPXRipHopMetric_Type = Integer32
_RadBridgeIPXRipHopMetric_Object = MibTableColumn
radBridgeIPXRipHopMetric = _RadBridgeIPXRipHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 6),
    _RadBridgeIPXRipHopMetric_Type()
)
radBridgeIPXRipHopMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipHopMetric.setStatus("current")
_RadBridgeIPXRipAgingTime_Type = TimeTicks
_RadBridgeIPXRipAgingTime_Object = MibTableColumn
radBridgeIPXRipAgingTime = _RadBridgeIPXRipAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 7),
    _RadBridgeIPXRipAgingTime_Type()
)
radBridgeIPXRipAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipAgingTime.setStatus("current")


class _RadBridgeIPXRipValueStatus_Type(Integer32):
    """Custom type radBridgeIPXRipValueStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("invalid", 3),
          ("semiDynamic", 4))
    )


_RadBridgeIPXRipValueStatus_Type.__name__ = "Integer32"
_RadBridgeIPXRipValueStatus_Object = MibTableColumn
radBridgeIPXRipValueStatus = _RadBridgeIPXRipValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 8),
    _RadBridgeIPXRipValueStatus_Type()
)
radBridgeIPXRipValueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipValueStatus.setStatus("current")


class _RadBridgeIPXRipForwardType_Type(Integer32):
    """Custom type radBridgeIPXRipForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("remote", 3))
    )


_RadBridgeIPXRipForwardType_Type.__name__ = "Integer32"
_RadBridgeIPXRipForwardType_Object = MibTableColumn
radBridgeIPXRipForwardType = _RadBridgeIPXRipForwardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 6, 1, 9),
    _RadBridgeIPXRipForwardType_Type()
)
radBridgeIPXRipForwardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipForwardType.setStatus("current")
_RadBridgeIPXRipInfTable_Object = MibTable
radBridgeIPXRipInfTable = _RadBridgeIPXRipInfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    radBridgeIPXRipInfTable.setStatus("current")
_RadBridgeIPXRipInfEntry_Object = MibTableRow
radBridgeIPXRipInfEntry = _RadBridgeIPXRipInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1)
)
radBridgeIPXRipInfEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeIPXRipInfIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeIPXRipInfEntry.setStatus("current")
_RadBridgeIPXRipInfIfIndex_Type = Integer32
_RadBridgeIPXRipInfIfIndex_Object = MibTableColumn
radBridgeIPXRipInfIfIndex = _RadBridgeIPXRipInfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1, 1),
    _RadBridgeIPXRipInfIfIndex_Type()
)
radBridgeIPXRipInfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXRipInfIfIndex.setStatus("current")
_RadBridgeIPXRipInfBcastUpdate_Type = Integer32
_RadBridgeIPXRipInfBcastUpdate_Object = MibTableColumn
radBridgeIPXRipInfBcastUpdate = _RadBridgeIPXRipInfBcastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1, 2),
    _RadBridgeIPXRipInfBcastUpdate_Type()
)
radBridgeIPXRipInfBcastUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipInfBcastUpdate.setStatus("current")
_RadBridgeIPXRipInfAgeMultiplier_Type = Integer32
_RadBridgeIPXRipInfAgeMultiplier_Object = MibTableColumn
radBridgeIPXRipInfAgeMultiplier = _RadBridgeIPXRipInfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 2, 7, 1, 3),
    _RadBridgeIPXRipInfAgeMultiplier_Type()
)
radBridgeIPXRipInfAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXRipInfAgeMultiplier.setStatus("current")
_RadBridgeIPXSap_ObjectIdentity = ObjectIdentity
radBridgeIPXSap = _RadBridgeIPXSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3)
)
_RadBridgeIPXSapOutPackets_Type = Counter32
_RadBridgeIPXSapOutPackets_Object = MibScalar
radBridgeIPXSapOutPackets = _RadBridgeIPXSapOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 1),
    _RadBridgeIPXSapOutPackets_Type()
)
radBridgeIPXSapOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapOutPackets.setStatus("current")
_RadBridgeIPXSapInPackets_Type = Counter32
_RadBridgeIPXSapInPackets_Object = MibScalar
radBridgeIPXSapInPackets = _RadBridgeIPXSapInPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 2),
    _RadBridgeIPXSapInPackets_Type()
)
radBridgeIPXSapInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapInPackets.setStatus("current")
_RadBridgeIPXSapInDiscards_Type = Counter32
_RadBridgeIPXSapInDiscards_Object = MibScalar
radBridgeIPXSapInDiscards = _RadBridgeIPXSapInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 3),
    _RadBridgeIPXSapInDiscards_Type()
)
radBridgeIPXSapInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapInDiscards.setStatus("current")
_RadBridgeIPXSapTblNoOfEntries_Type = Integer32
_RadBridgeIPXSapTblNoOfEntries_Object = MibScalar
radBridgeIPXSapTblNoOfEntries = _RadBridgeIPXSapTblNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 4),
    _RadBridgeIPXSapTblNoOfEntries_Type()
)
radBridgeIPXSapTblNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapTblNoOfEntries.setStatus("current")
_RadBridgeIPXSapTblBcastTrigUpdateInterval_Type = Integer32
_RadBridgeIPXSapTblBcastTrigUpdateInterval_Object = MibScalar
radBridgeIPXSapTblBcastTrigUpdateInterval = _RadBridgeIPXSapTblBcastTrigUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 5),
    _RadBridgeIPXSapTblBcastTrigUpdateInterval_Type()
)
radBridgeIPXSapTblBcastTrigUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapTblBcastTrigUpdateInterval.setStatus("current")
_RadBridgeIPXSapTable_Object = MibTable
radBridgeIPXSapTable = _RadBridgeIPXSapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    radBridgeIPXSapTable.setStatus("current")
_RadBridgeIPXSapTableEntry_Object = MibTableRow
radBridgeIPXSapTableEntry = _RadBridgeIPXSapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1)
)
radBridgeIPXSapTableEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeIPXSapServerType"),
    (0, "ACE202-MIB", "radBridgeIPXSapName"),
)
if mibBuilder.loadTexts:
    radBridgeIPXSapTableEntry.setStatus("current")
_RadBridgeIPXSapServerType_Type = Integer32
_RadBridgeIPXSapServerType_Object = MibTableColumn
radBridgeIPXSapServerType = _RadBridgeIPXSapServerType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 1),
    _RadBridgeIPXSapServerType_Type()
)
radBridgeIPXSapServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapServerType.setStatus("current")


class _RadBridgeIPXSapName_Type(DisplayString):
    """Custom type radBridgeIPXSapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixed_length = 48


_RadBridgeIPXSapName_Type.__name__ = "DisplayString"
_RadBridgeIPXSapName_Object = MibTableColumn
radBridgeIPXSapName = _RadBridgeIPXSapName_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 2),
    _RadBridgeIPXSapName_Type()
)
radBridgeIPXSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapName.setStatus("current")


class _RadBridgeIPXSapNetwork_Type(OctetString):
    """Custom type radBridgeIPXSapNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RadBridgeIPXSapNetwork_Type.__name__ = "OctetString"
_RadBridgeIPXSapNetwork_Object = MibTableColumn
radBridgeIPXSapNetwork = _RadBridgeIPXSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 3),
    _RadBridgeIPXSapNetwork_Type()
)
radBridgeIPXSapNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapNetwork.setStatus("current")


class _RadBridgeIPXSapNode_Type(OctetString):
    """Custom type radBridgeIPXSapNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RadBridgeIPXSapNode_Type.__name__ = "OctetString"
_RadBridgeIPXSapNode_Object = MibTableColumn
radBridgeIPXSapNode = _RadBridgeIPXSapNode_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 4),
    _RadBridgeIPXSapNode_Type()
)
radBridgeIPXSapNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapNode.setStatus("current")
_RadBridgeIPXSapSocket_Type = Integer32
_RadBridgeIPXSapSocket_Object = MibTableColumn
radBridgeIPXSapSocket = _RadBridgeIPXSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 5),
    _RadBridgeIPXSapSocket_Type()
)
radBridgeIPXSapSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapSocket.setStatus("current")


class _RadBridgeIPXSapHopsToServer_Type(Integer32):
    """Custom type radBridgeIPXSapHopsToServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RadBridgeIPXSapHopsToServer_Type.__name__ = "Integer32"
_RadBridgeIPXSapHopsToServer_Object = MibTableColumn
radBridgeIPXSapHopsToServer = _RadBridgeIPXSapHopsToServer_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 6),
    _RadBridgeIPXSapHopsToServer_Type()
)
radBridgeIPXSapHopsToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapHopsToServer.setStatus("current")
_RadBridgeIPXSapNIC_Type = Integer32
_RadBridgeIPXSapNIC_Object = MibTableColumn
radBridgeIPXSapNIC = _RadBridgeIPXSapNIC_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 7),
    _RadBridgeIPXSapNIC_Type()
)
radBridgeIPXSapNIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapNIC.setStatus("current")
_RadBridgeIPXSapAgingTime_Type = TimeTicks
_RadBridgeIPXSapAgingTime_Object = MibTableColumn
radBridgeIPXSapAgingTime = _RadBridgeIPXSapAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 8),
    _RadBridgeIPXSapAgingTime_Type()
)
radBridgeIPXSapAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapAgingTime.setStatus("current")


class _RadBridgeIPXSapStatus_Type(Integer32):
    """Custom type radBridgeIPXSapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("dynamic", 2),
          ("invalid", 3),
          ("semiDynamic", 4))
    )


_RadBridgeIPXSapStatus_Type.__name__ = "Integer32"
_RadBridgeIPXSapStatus_Object = MibTableColumn
radBridgeIPXSapStatus = _RadBridgeIPXSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 6, 1, 9),
    _RadBridgeIPXSapStatus_Type()
)
radBridgeIPXSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapStatus.setStatus("current")
_RadBridgeIPXSapInfTable_Object = MibTable
radBridgeIPXSapInfTable = _RadBridgeIPXSapInfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    radBridgeIPXSapInfTable.setStatus("current")
_RadBridgeIPXSapInfEntry_Object = MibTableRow
radBridgeIPXSapInfEntry = _RadBridgeIPXSapInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1)
)
radBridgeIPXSapInfEntry.setIndexNames(
    (0, "ACE202-MIB", "radBridgeIPXSapInfIfIndex"),
)
if mibBuilder.loadTexts:
    radBridgeIPXSapInfEntry.setStatus("current")
_RadBridgeIPXSapInfIfIndex_Type = Integer32
_RadBridgeIPXSapInfIfIndex_Object = MibTableColumn
radBridgeIPXSapInfIfIndex = _RadBridgeIPXSapInfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1, 1),
    _RadBridgeIPXSapInfIfIndex_Type()
)
radBridgeIPXSapInfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radBridgeIPXSapInfIfIndex.setStatus("current")
_RadBridgeIPXSapInfBcastUpdate_Type = Integer32
_RadBridgeIPXSapInfBcastUpdate_Object = MibTableColumn
radBridgeIPXSapInfBcastUpdate = _RadBridgeIPXSapInfBcastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1, 2),
    _RadBridgeIPXSapInfBcastUpdate_Type()
)
radBridgeIPXSapInfBcastUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapInfBcastUpdate.setStatus("current")
_RadBridgeIPXSapInfAgeMultiplier_Type = Integer32
_RadBridgeIPXSapInfAgeMultiplier_Object = MibTableColumn
radBridgeIPXSapInfAgeMultiplier = _RadBridgeIPXSapInfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 5, 3, 7, 1, 3),
    _RadBridgeIPXSapInfAgeMultiplier_Type()
)
radBridgeIPXSapInfAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radBridgeIPXSapInfAgeMultiplier.setStatus("current")
_NewMasking_ObjectIdentity = ObjectIdentity
newMasking = _NewMasking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6)
)
_MaskingMaxEntries_Type = Integer32
_MaskingMaxEntries_Object = MibScalar
maskingMaxEntries = _MaskingMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 1),
    _MaskingMaxEntries_Type()
)
maskingMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingMaxEntries.setStatus("current")
_MaskingCurrentEntries_Type = Integer32
_MaskingCurrentEntries_Object = MibScalar
maskingCurrentEntries = _MaskingCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 2),
    _MaskingCurrentEntries_Type()
)
maskingCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingCurrentEntries.setStatus("current")
_MaskingTable_Object = MibTable
maskingTable = _MaskingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    maskingTable.setStatus("current")
_MaskingEntry_Object = MibTableRow
maskingEntry = _MaskingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1)
)
maskingEntry.setIndexNames(
    (0, "ACE202-MIB", "maskingType"),
    (0, "ACE202-MIB", "maskingIfIndex"),
    (0, "ACE202-MIB", "maskingIndex"),
)
if mibBuilder.loadTexts:
    maskingEntry.setStatus("current")


class _MaskingType_Type(Integer32):
    """Custom type maskingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2),
          ("compress", 3),
          ("priority", 4),
          ("loadSharing", 5),
          ("facs", 6),
          ("codConnect", 7),
          ("codDisconnect", 8))
    )


_MaskingType_Type.__name__ = "Integer32"
_MaskingType_Object = MibTableColumn
maskingType = _MaskingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 1),
    _MaskingType_Type()
)
maskingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingType.setStatus("current")
_MaskingIfIndex_Type = Integer32
_MaskingIfIndex_Object = MibTableColumn
maskingIfIndex = _MaskingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 2),
    _MaskingIfIndex_Type()
)
maskingIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingIfIndex.setStatus("current")
_MaskingIndex_Type = Integer32
_MaskingIndex_Object = MibTableColumn
maskingIndex = _MaskingIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 3),
    _MaskingIndex_Type()
)
maskingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingIndex.setStatus("current")


class _MaskingProtocolType_Type(Integer32):
    """Custom type maskingProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ip", 2),
          ("ipx", 3),
          ("sna", 4),
          ("netbios", 5),
          ("apple", 6),
          ("dec", 7),
          ("all", 255))
    )


_MaskingProtocolType_Type.__name__ = "Integer32"
_MaskingProtocolType_Object = MibTableColumn
maskingProtocolType = _MaskingProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 4),
    _MaskingProtocolType_Type()
)
maskingProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingProtocolType.setStatus("current")
_MaskingSmartMaskOID_Type = ObjectIdentifier
_MaskingSmartMaskOID_Object = MibTableColumn
maskingSmartMaskOID = _MaskingSmartMaskOID_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 5),
    _MaskingSmartMaskOID_Type()
)
maskingSmartMaskOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskingSmartMaskOID.setStatus("current")


class _MaskingFrameType_Type(Integer32):
    """Custom type maskingFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("all", 2),
          ("broadcast", 3),
          ("multicast", 4))
    )


_MaskingFrameType_Type.__name__ = "Integer32"
_MaskingFrameType_Object = MibTableColumn
maskingFrameType = _MaskingFrameType_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 6),
    _MaskingFrameType_Type()
)
maskingFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingFrameType.setStatus("current")


class _MaskingFrameTypeCondition_Type(Integer32):
    """Custom type maskingFrameTypeCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingFrameTypeCondition_Type.__name__ = "Integer32"
_MaskingFrameTypeCondition_Object = MibTableColumn
maskingFrameTypeCondition = _MaskingFrameTypeCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 7),
    _MaskingFrameTypeCondition_Type()
)
maskingFrameTypeCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingFrameTypeCondition.setStatus("current")
_MaskingSourceAddress_Type = GenAddress
_MaskingSourceAddress_Object = MibTableColumn
maskingSourceAddress = _MaskingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 8),
    _MaskingSourceAddress_Type()
)
maskingSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceAddress.setStatus("current")
_MaskingSourceActiveBits_Type = GenAddress
_MaskingSourceActiveBits_Object = MibTableColumn
maskingSourceActiveBits = _MaskingSourceActiveBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 9),
    _MaskingSourceActiveBits_Type()
)
maskingSourceActiveBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceActiveBits.setStatus("current")


class _MaskingSourceMacOrNet_Type(Integer32):
    """Custom type maskingSourceMacOrNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("netAddress", 2),
          ("ipRange", 3),
          ("appleAddress", 4))
    )


_MaskingSourceMacOrNet_Type.__name__ = "Integer32"
_MaskingSourceMacOrNet_Object = MibTableColumn
maskingSourceMacOrNet = _MaskingSourceMacOrNet_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 10),
    _MaskingSourceMacOrNet_Type()
)
maskingSourceMacOrNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceMacOrNet.setStatus("current")


class _MaskingSourceCondition_Type(Integer32):
    """Custom type maskingSourceCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingSourceCondition_Type.__name__ = "Integer32"
_MaskingSourceCondition_Object = MibTableColumn
maskingSourceCondition = _MaskingSourceCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 11),
    _MaskingSourceCondition_Type()
)
maskingSourceCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSourceCondition.setStatus("current")
_MaskingDestAddress_Type = GenAddress
_MaskingDestAddress_Object = MibTableColumn
maskingDestAddress = _MaskingDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 12),
    _MaskingDestAddress_Type()
)
maskingDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestAddress.setStatus("current")
_MaskingDestActiveBits_Type = GenAddress
_MaskingDestActiveBits_Object = MibTableColumn
maskingDestActiveBits = _MaskingDestActiveBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 13),
    _MaskingDestActiveBits_Type()
)
maskingDestActiveBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestActiveBits.setStatus("current")


class _MaskingDestMacOrNet_Type(Integer32):
    """Custom type maskingDestMacOrNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("netAddress", 2),
          ("ipRange", 3),
          ("appleAddress", 4))
    )


_MaskingDestMacOrNet_Type.__name__ = "Integer32"
_MaskingDestMacOrNet_Object = MibTableColumn
maskingDestMacOrNet = _MaskingDestMacOrNet_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 14),
    _MaskingDestMacOrNet_Type()
)
maskingDestMacOrNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestMacOrNet.setStatus("current")


class _MaskingDestCondition_Type(Integer32):
    """Custom type maskingDestCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingDestCondition_Type.__name__ = "Integer32"
_MaskingDestCondition_Object = MibTableColumn
maskingDestCondition = _MaskingDestCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 15),
    _MaskingDestCondition_Type()
)
maskingDestCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingDestCondition.setStatus("current")


class _MaskingLowLevelProt_Type(Integer32):
    """Custom type maskingLowLevelProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ipxRip", 2),
          ("ipxSap", 3),
          ("ipxSpx", 4),
          ("ipUdp", 5),
          ("ipTcp", 6),
          ("ipIcmp", 7),
          ("ipxNcp", 8),
          ("ipxWan", 9),
          ("ipxEco", 10),
          ("ipxErr", 11),
          ("ipxPep", 12))
    )


_MaskingLowLevelProt_Type.__name__ = "Integer32"
_MaskingLowLevelProt_Object = MibTableColumn
maskingLowLevelProt = _MaskingLowLevelProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 16),
    _MaskingLowLevelProt_Type()
)
maskingLowLevelProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingLowLevelProt.setStatus("current")


class _MaskingLowLevelProtCondition_Type(Integer32):
    """Custom type maskingLowLevelProtCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingLowLevelProtCondition_Type.__name__ = "Integer32"
_MaskingLowLevelProtCondition_Object = MibTableColumn
maskingLowLevelProtCondition = _MaskingLowLevelProtCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 17),
    _MaskingLowLevelProtCondition_Type()
)
maskingLowLevelProtCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingLowLevelProtCondition.setStatus("current")
_MaskingHighLevelProt_Type = Integer32
_MaskingHighLevelProt_Object = MibTableColumn
maskingHighLevelProt = _MaskingHighLevelProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 18),
    _MaskingHighLevelProt_Type()
)
maskingHighLevelProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingHighLevelProt.setStatus("current")


class _MaskingHighLevelProtCondition_Type(Integer32):
    """Custom type maskingHighLevelProtCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingHighLevelProtCondition_Type.__name__ = "Integer32"
_MaskingHighLevelProtCondition_Object = MibTableColumn
maskingHighLevelProtCondition = _MaskingHighLevelProtCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 19),
    _MaskingHighLevelProtCondition_Type()
)
maskingHighLevelProtCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingHighLevelProtCondition.setStatus("current")
_MaskingPortNum_Type = Integer32
_MaskingPortNum_Object = MibTableColumn
maskingPortNum = _MaskingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 20),
    _MaskingPortNum_Type()
)
maskingPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingPortNum.setStatus("current")


class _MaskingPortNumCondition_Type(Integer32):
    """Custom type maskingPortNumCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingPortNumCondition_Type.__name__ = "Integer32"
_MaskingPortNumCondition_Object = MibTableColumn
maskingPortNumCondition = _MaskingPortNumCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 21),
    _MaskingPortNumCondition_Type()
)
maskingPortNumCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingPortNumCondition.setStatus("current")


class _MaskingOperation_Type(Integer32):
    """Custom type maskingOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("route", 3),
          ("forward-route", 4),
          ("high-priority", 5),
          ("noOp", 6),
          ("delete", 7),
          ("smartMask", 8))
    )


_MaskingOperation_Type.__name__ = "Integer32"
_MaskingOperation_Object = MibTableColumn
maskingOperation = _MaskingOperation_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 22),
    _MaskingOperation_Type()
)
maskingOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingOperation.setStatus("current")
_MaskingSrcPortNum_Type = Integer32
_MaskingSrcPortNum_Object = MibTableColumn
maskingSrcPortNum = _MaskingSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 23),
    _MaskingSrcPortNum_Type()
)
maskingSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSrcPortNum.setStatus("current")


class _MaskingSrcPortNumCondition_Type(Integer32):
    """Custom type maskingSrcPortNumCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MaskingSrcPortNumCondition_Type.__name__ = "Integer32"
_MaskingSrcPortNumCondition_Object = MibTableColumn
maskingSrcPortNumCondition = _MaskingSrcPortNumCondition_Object(
    (1, 3, 6, 1, 4, 1, 164, 4, 1, 6, 3, 1, 24),
    _MaskingSrcPortNumCondition_Type()
)
maskingSrcPortNumCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskingSrcPortNumCondition.setStatus("current")
_RadConverters_ObjectIdentity = ObjectIdentity
radConverters = _RadConverters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 5)
)
_RadGen_ObjectIdentity = ObjectIdentity
radGen = _RadGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1)
)
_SystemsEvents_ObjectIdentity = ObjectIdentity
systemsEvents = _SystemsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0)
)
if mibBuilder.loadTexts:
    systemsEvents.setStatus("current")
_RadSysTR_ObjectIdentity = ObjectIdentity
radSysTR = _RadSysTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 1)
)
_RadRADring_ObjectIdentity = ObjectIdentity
radRADring = _RadRADring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 1, 1)
)
_RadTMA_ObjectIdentity = ObjectIdentity
radTMA = _RadTMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 1, 2)
)
_RadRingMonitor_ObjectIdentity = ObjectIdentity
radRingMonitor = _RadRingMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 1, 3)
)
_RadSysFddi_ObjectIdentity = ObjectIdentity
radSysFddi = _RadSysFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 2)
)
_RadFDX100_ObjectIdentity = ObjectIdentity
radFDX100 = _RadFDX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 2, 1)
)
_RadSysWan_ObjectIdentity = ObjectIdentity
radSysWan = _RadSysWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3)
)
_RadSysWanEvents_ObjectIdentity = ObjectIdentity
radSysWanEvents = _RadSysWanEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0)
)
if mibBuilder.loadTexts:
    radSysWanEvents.setStatus("current")
_RadMP2100_ObjectIdentity = ObjectIdentity
radMP2100 = _RadMP2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 1)
)
_RadMP2104_ObjectIdentity = ObjectIdentity
radMP2104 = _RadMP2104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 2)
)
_RadMP2100B_ObjectIdentity = ObjectIdentity
radMP2100B = _RadMP2100B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 3)
)
_RadMP2100F_ObjectIdentity = ObjectIdentity
radMP2100F = _RadMP2100F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 4)
)
_RadMP2100H_ObjectIdentity = ObjectIdentity
radMP2100H = _RadMP2100H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 5)
)
_RadMP2104H_ObjectIdentity = ObjectIdentity
radMP2104H = _RadMP2104H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 6)
)
_RadMP2200B_ObjectIdentity = ObjectIdentity
radMP2200B = _RadMP2200B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 7)
)
_RadMP2200F_ObjectIdentity = ObjectIdentity
radMP2200F = _RadMP2200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 8)
)
_RadMX3000_ObjectIdentity = ObjectIdentity
radMX3000 = _RadMX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 9)
)
_RadMX3004_ObjectIdentity = ObjectIdentity
radMX3004 = _RadMX3004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 10)
)
_RadMX30_ObjectIdentity = ObjectIdentity
radMX30 = _RadMX30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 11)
)
_RadMX300_ObjectIdentity = ObjectIdentity
radMX300 = _RadMX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 12)
)
_RadVOIP_ObjectIdentity = ObjectIdentity
radVOIP = _RadVOIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 13)
)
_RadKM2100_ObjectIdentity = ObjectIdentity
radKM2100 = _RadKM2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 15)
)
_RadKM2104_ObjectIdentity = ObjectIdentity
radKM2104 = _RadKM2104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 16)
)
_RadDXC30_ObjectIdentity = ObjectIdentity
radDXC30 = _RadDXC30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 20)
)
_RadDXC10A_ObjectIdentity = ObjectIdentity
radDXC10A = _RadDXC10A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 21)
)
_RadDXC8R_ObjectIdentity = ObjectIdentity
radDXC8R = _RadDXC8R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 22)
)
_RadDXC30E_ObjectIdentity = ObjectIdentity
radDXC30E = _RadDXC30E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 23)
)
_RadDXC3000_ObjectIdentity = ObjectIdentity
radDXC3000 = _RadDXC3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 24)
)
_RadDXC8RNew_ObjectIdentity = ObjectIdentity
radDXC8RNew = _RadDXC8RNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 25)
)
_RadFcdE1L_ObjectIdentity = ObjectIdentity
radFcdE1L = _RadFcdE1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 29)
)
_RadFcdT1_ObjectIdentity = ObjectIdentity
radFcdT1 = _RadFcdT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 30)
)
_RadFcdE1_ObjectIdentity = ObjectIdentity
radFcdE1 = _RadFcdE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 31)
)
_RadFcdE1I_ObjectIdentity = ObjectIdentity
radFcdE1I = _RadFcdE1I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 32)
)
_RadFcdT1M_ObjectIdentity = ObjectIdentity
radFcdT1M = _RadFcdT1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 33)
)
_RadFcdE1M_ObjectIdentity = ObjectIdentity
radFcdE1M = _RadFcdE1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 34)
)
_RadFcdIP_ObjectIdentity = ObjectIdentity
radFcdIP = _RadFcdIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 35)
)
_RadFcdT1A_ObjectIdentity = ObjectIdentity
radFcdT1A = _RadFcdT1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 36)
)
_RadFcdE1A_ObjectIdentity = ObjectIdentity
radFcdE1A = _RadFcdE1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 37)
)
_RadFcdW_ObjectIdentity = ObjectIdentity
radFcdW = _RadFcdW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 38)
)
_RadFcdSTM_ObjectIdentity = ObjectIdentity
radFcdSTM = _RadFcdSTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 39)
)
_RadHtuE1Sa_ObjectIdentity = ObjectIdentity
radHtuE1Sa = _RadHtuE1Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 40)
)
_RadHtuE1_ObjectIdentity = ObjectIdentity
radHtuE1 = _RadHtuE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 41)
)
_RadHtu2Sa_ObjectIdentity = ObjectIdentity
radHtu2Sa = _RadHtu2Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 42)
)
_RadHtu2_ObjectIdentity = ObjectIdentity
radHtu2 = _RadHtu2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 43)
)
_RadAsmi450R768Sa_ObjectIdentity = ObjectIdentity
radAsmi450R768Sa = _RadAsmi450R768Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 44)
)
_RadAsmi450R768_ObjectIdentity = ObjectIdentity
radAsmi450R768 = _RadAsmi450R768_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 45)
)
_RadAsmi450R1152Sa_ObjectIdentity = ObjectIdentity
radAsmi450R1152Sa = _RadAsmi450R1152Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 46)
)
_RadAsmi450R1152_ObjectIdentity = ObjectIdentity
radAsmi450R1152 = _RadAsmi450R1152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 47)
)
_RadLrs12F_ObjectIdentity = ObjectIdentity
radLrs12F = _RadLrs12F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 48)
)
_RadLrs12B_ObjectIdentity = ObjectIdentity
radLrs12B = _RadLrs12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 49)
)
_RadHcdE1Sa_ObjectIdentity = ObjectIdentity
radHcdE1Sa = _RadHcdE1Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 51)
)
_RadHcdE1_ObjectIdentity = ObjectIdentity
radHcdE1 = _RadHcdE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 52)
)
_RadHtuT1Sa_ObjectIdentity = ObjectIdentity
radHtuT1Sa = _RadHtuT1Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 53)
)
_RadHtuT1_ObjectIdentity = ObjectIdentity
radHtuT1 = _RadHtuT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 54)
)
_RadOptimux4E1_ObjectIdentity = ObjectIdentity
radOptimux4E1 = _RadOptimux4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 55)
)
_RadOptimux4T1_ObjectIdentity = ObjectIdentity
radOptimux4T1 = _RadOptimux4T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 56)
)
_RadOptimuxXLE1_ObjectIdentity = ObjectIdentity
radOptimuxXLE1 = _RadOptimuxXLE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 57)
)
_RadOptimuxXLT1_ObjectIdentity = ObjectIdentity
radOptimuxXLT1 = _RadOptimuxXLT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 58)
)
_RadOptimuxXL16E1_ObjectIdentity = ObjectIdentity
radOptimuxXL16E1 = _RadOptimuxXL16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 59)
)
_RadImx64_ObjectIdentity = ObjectIdentity
radImx64 = _RadImx64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 60)
)
_RadImx6L_ObjectIdentity = ObjectIdentity
radImx6L = _RadImx6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 61)
)
_RadImx2_ObjectIdentity = ObjectIdentity
radImx2 = _RadImx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 62)
)
_RadImx4T1_ObjectIdentity = ObjectIdentity
radImx4T1 = _RadImx4T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 63)
)
_RadImx4E1_ObjectIdentity = ObjectIdentity
radImx4E1 = _RadImx4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 64)
)
_RadImx2T1E1_ObjectIdentity = ObjectIdentity
radImx2T1E1 = _RadImx2T1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 65)
)
_RadOptimux4T1L_ObjectIdentity = ObjectIdentity
radOptimux4T1L = _RadOptimux4T1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 68)
)
_RadOptimux4E1L_ObjectIdentity = ObjectIdentity
radOptimux4E1L = _RadOptimux4E1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 69)
)
_RadHtuE1SaV2_ObjectIdentity = ObjectIdentity
radHtuE1SaV2 = _RadHtuE1SaV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 70)
)
_RadHtuE1V2_ObjectIdentity = ObjectIdentity
radHtuE1V2 = _RadHtuE1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 71)
)
_RadFomiE3_ObjectIdentity = ObjectIdentity
radFomiE3 = _RadFomiE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 72)
)
_RadFomiT3_ObjectIdentity = ObjectIdentity
radFomiT3 = _RadFomiT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 73)
)
_RadOpt4E1C_ObjectIdentity = ObjectIdentity
radOpt4E1C = _RadOpt4E1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 74)
)
_RadOpt4T1C_ObjectIdentity = ObjectIdentity
radOpt4T1C = _RadOpt4T1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 75)
)
_RadPrbiE3_ObjectIdentity = ObjectIdentity
radPrbiE3 = _RadPrbiE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 76)
)
_RadPrbiT3_ObjectIdentity = ObjectIdentity
radPrbiT3 = _RadPrbiT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 77)
)
_RadHcd4Sa_ObjectIdentity = ObjectIdentity
radHcd4Sa = _RadHcd4Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 78)
)
_RadOptimuxT3_ObjectIdentity = ObjectIdentity
radOptimuxT3 = _RadOptimuxT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 79)
)
_RadFRmon_ObjectIdentity = ObjectIdentity
radFRmon = _RadFRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 80)
)
_RadIpMux4_ObjectIdentity = ObjectIdentity
radIpMux4 = _RadIpMux4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 81)
)
_RadIpMux1_ObjectIdentity = ObjectIdentity
radIpMux1 = _RadIpMux1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 82)
)
_RadIpMux16_ObjectIdentity = ObjectIdentity
radIpMux16 = _RadIpMux16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 83)
)
_RadIpMux1E_ObjectIdentity = ObjectIdentity
radIpMux1E = _RadIpMux1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 84)
)
_RadVmux2100_ObjectIdentity = ObjectIdentity
radVmux2100 = _RadVmux2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 85)
)
_RadSysBRG_ObjectIdentity = ObjectIdentity
radSysBRG = _RadSysBRG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4)
)
_RadTRE1_ObjectIdentity = ObjectIdentity
radTRE1 = _RadTRE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 1)
)
_RadTRE1D_ObjectIdentity = ObjectIdentity
radTRE1D = _RadTRE1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 2)
)
_RadTRE8_ObjectIdentity = ObjectIdentity
radTRE8 = _RadTRE8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 3)
)
_RadTRE8D_ObjectIdentity = ObjectIdentity
radTRE8D = _RadTRE8D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 4)
)
_RadMBE1_ObjectIdentity = ObjectIdentity
radMBE1 = _RadMBE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 5)
)
_RadMBE1D_ObjectIdentity = ObjectIdentity
radMBE1D = _RadMBE1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 6)
)
_RadMBE8_ObjectIdentity = ObjectIdentity
radMBE8 = _RadMBE8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 7)
)
_RadMBE8D_ObjectIdentity = ObjectIdentity
radMBE8D = _RadMBE8D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 8)
)
_RadMLBT_ObjectIdentity = ObjectIdentity
radMLBT = _RadMLBT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 9)
)
_RadFEB4DAS_ObjectIdentity = ObjectIdentity
radFEB4DAS = _RadFEB4DAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 10)
)
_RadTrimBrg10_ObjectIdentity = ObjectIdentity
radTrimBrg10 = _RadTrimBrg10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 11)
)
_RadTrimBrg16_ObjectIdentity = ObjectIdentity
radTrimBrg16 = _RadTrimBrg16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 12)
)
_RadRRTRE8_ObjectIdentity = ObjectIdentity
radRRTRE8 = _RadRRTRE8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 13)
)
_RadRRTRE8D_ObjectIdentity = ObjectIdentity
radRRTRE8D = _RadRRTRE8D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 14)
)
_RadRRMLBT_ObjectIdentity = ObjectIdentity
radRRMLBT = _RadRRMLBT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 15)
)
_RadRRMLBTF_ObjectIdentity = ObjectIdentity
radRRMLBTF = _RadRRMLBTF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 16)
)
_RadRRTRE1D_ObjectIdentity = ObjectIdentity
radRRTRE1D = _RadRRTRE1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 17)
)
_RadTRERAS_ObjectIdentity = ObjectIdentity
radTRERAS = _RadTRERAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 18)
)
_RadTRERASa_ObjectIdentity = ObjectIdentity
radTRERASa = _RadTRERASa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 19)
)
_RadMBERAS_ObjectIdentity = ObjectIdentity
radMBERAS = _RadMBERAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 20)
)
_RadMBERASa_ObjectIdentity = ObjectIdentity
radMBERASa = _RadMBERASa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 21)
)
_RadFEB4FDX_ObjectIdentity = ObjectIdentity
radFEB4FDX = _RadFEB4FDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 22)
)
_RadFEB4SAS_ObjectIdentity = ObjectIdentity
radFEB4SAS = _RadFEB4SAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 23)
)
_RadRRFTBDAS_ObjectIdentity = ObjectIdentity
radRRFTBDAS = _RadRRFTBDAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 24)
)
_RadRRFTBSAS_ObjectIdentity = ObjectIdentity
radRRFTBSAS = _RadRRFTBSAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 25)
)
_RadFTBDAS_ObjectIdentity = ObjectIdentity
radFTBDAS = _RadFTBDAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 26)
)
_RadFTBSAS_ObjectIdentity = ObjectIdentity
radFTBSAS = _RadFTBSAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 27)
)
_RadFastWay100_ObjectIdentity = ObjectIdentity
radFastWay100 = _RadFastWay100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 4, 28)
)
_RadSysCnvrtr_ObjectIdentity = ObjectIdentity
radSysCnvrtr = _RadSysCnvrtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5)
)
_RadSTC1_ObjectIdentity = ObjectIdentity
radSTC1 = _RadSTC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 1)
)
_RadSTC2_ObjectIdentity = ObjectIdentity
radSTC2 = _RadSTC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 3)
)
_RadSTC1UDP_ObjectIdentity = ObjectIdentity
radSTC1UDP = _RadSTC1UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 4)
)
_RadSTC2UDP_ObjectIdentity = ObjectIdentity
radSTC2UDP = _RadSTC2UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 6)
)
_RadFTC1_ObjectIdentity = ObjectIdentity
radFTC1 = _RadFTC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 10)
)
_RadFTC2_ObjectIdentity = ObjectIdentity
radFTC2 = _RadFTC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 12)
)
_RadFTC1UDP_ObjectIdentity = ObjectIdentity
radFTC1UDP = _RadFTC1UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 13)
)
_RadFTC2UDP_ObjectIdentity = ObjectIdentity
radFTC2UDP = _RadFTC2UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 15)
)
_RadSEC1_ObjectIdentity = ObjectIdentity
radSEC1 = _RadSEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 20)
)
_RadSEC2_ObjectIdentity = ObjectIdentity
radSEC2 = _RadSEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 22)
)
_RadSEC1UDP_ObjectIdentity = ObjectIdentity
radSEC1UDP = _RadSEC1UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 23)
)
_RadSEC2UDP_ObjectIdentity = ObjectIdentity
radSEC2UDP = _RadSEC2UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 25)
)
_RadFEC1_ObjectIdentity = ObjectIdentity
radFEC1 = _RadFEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 30)
)
_RadFEC2_ObjectIdentity = ObjectIdentity
radFEC2 = _RadFEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 32)
)
_RadFEC1UDP_ObjectIdentity = ObjectIdentity
radFEC1UDP = _RadFEC1UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 33)
)
_RadFEC2UDP_ObjectIdentity = ObjectIdentity
radFEC2UDP = _RadFEC2UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 5, 35)
)
_RadSysStkHub_ObjectIdentity = ObjectIdentity
radSysStkHub = _RadSysStkHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7)
)
_RadRBHE_ObjectIdentity = ObjectIdentity
radRBHE = _RadRBHE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 1)
)
_RadRBHEEvents_ObjectIdentity = ObjectIdentity
radRBHEEvents = _RadRBHEEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 1, 0)
)
if mibBuilder.loadTexts:
    radRBHEEvents.setStatus("current")
_RadRBHT_ObjectIdentity = ObjectIdentity
radRBHT = _RadRBHT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 2)
)
_RadRBHTEvents_ObjectIdentity = ObjectIdentity
radRBHTEvents = _RadRBHTEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 2, 0)
)
if mibBuilder.loadTexts:
    radRBHTEvents.setStatus("current")
_RadETS4fddiDAS_ObjectIdentity = ObjectIdentity
radETS4fddiDAS = _RadETS4fddiDAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 3)
)
_RadETS4fddiSAS_ObjectIdentity = ObjectIdentity
radETS4fddiSAS = _RadETS4fddiSAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 4)
)
_RadSAHEMX_ObjectIdentity = ObjectIdentity
radSAHEMX = _RadSAHEMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 5)
)
_RadSAHTM_ObjectIdentity = ObjectIdentity
radSAHTM = _RadSAHTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 6)
)
_RadETS4_ObjectIdentity = ObjectIdentity
radETS4 = _RadETS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 7)
)
_RadSAHEMU_ObjectIdentity = ObjectIdentity
radSAHEMU = _RadSAHEMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 8)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 9)
)
_RadSAH16Eint_ObjectIdentity = ObjectIdentity
radSAH16Eint = _RadSAH16Eint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 10)
)
_RadSAH16Tint_ObjectIdentity = ObjectIdentity
radSAH16Tint = _RadSAH16Tint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 11)
)
_RadSAH16Eext_ObjectIdentity = ObjectIdentity
radSAH16Eext = _RadSAH16Eext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 12)
)
_RadSAH16Text_ObjectIdentity = ObjectIdentity
radSAH16Text = _RadSAH16Text_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 7, 13)
)
_RadSysPS_ObjectIdentity = ObjectIdentity
radSysPS = _RadSysPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8)
)
_RadSysPSEvents_ObjectIdentity = ObjectIdentity
radSysPSEvents = _RadSysPSEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 0)
)
if mibBuilder.loadTexts:
    radSysPSEvents.setStatus("current")
_RadSPS2_ObjectIdentity = ObjectIdentity
radSPS2 = _RadSPS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 1)
)
_RadSPS3_ObjectIdentity = ObjectIdentity
radSPS3 = _RadSPS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 2)
)
_RadSPS6_ObjectIdentity = ObjectIdentity
radSPS6 = _RadSPS6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 3)
)
_RadSPS9_ObjectIdentity = ObjectIdentity
radSPS9 = _RadSPS9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 4)
)
_RadSPS12_ObjectIdentity = ObjectIdentity
radSPS12 = _RadSPS12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 5)
)
_RadAPD2_ObjectIdentity = ObjectIdentity
radAPD2 = _RadAPD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 6)
)
_RadAPD8_ObjectIdentity = ObjectIdentity
radAPD8 = _RadAPD8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 7)
)
_RadAPS8_ObjectIdentity = ObjectIdentity
radAPS8 = _RadAPS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 8)
)
_RadAPS16_ObjectIdentity = ObjectIdentity
radAPS16 = _RadAPS16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 9)
)
_RadAPS24_ObjectIdentity = ObjectIdentity
radAPS24 = _RadAPS24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 10)
)
_RadSPS3S_ObjectIdentity = ObjectIdentity
radSPS3S = _RadSPS3S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 11)
)
_RadFPS8_ObjectIdentity = ObjectIdentity
radFPS8 = _RadFPS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 12)
)
_RadFPS12_ObjectIdentity = ObjectIdentity
radFPS12 = _RadFPS12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 13)
)
_RadSPS3ScSL_ObjectIdentity = ObjectIdentity
radSPS3ScSL = _RadSPS3ScSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 14)
)
_RadSPS3Sc2S_ObjectIdentity = ObjectIdentity
radSPS3Sc2S = _RadSPS3Sc2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 15)
)
_RadFPS8c_ObjectIdentity = ObjectIdentity
radFPS8c = _RadFPS8c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 16)
)
_RadFPS4_ObjectIdentity = ObjectIdentity
radFPS4 = _RadFPS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 8, 17)
)
_RadSysEth_ObjectIdentity = ObjectIdentity
radSysEth = _RadSysEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9)
)
_RadEP8T_ObjectIdentity = ObjectIdentity
radEP8T = _RadEP8T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 1)
)
_RadEP4TAUI_ObjectIdentity = ObjectIdentity
radEP4TAUI = _RadEP4TAUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 2)
)
_RadEP4T2FL_ObjectIdentity = ObjectIdentity
radEP4T2FL = _RadEP4T2FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 3)
)
_RadEP4TFL_ObjectIdentity = ObjectIdentity
radEP4TFL = _RadEP4TFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 4)
)
_RadEP4FL_ObjectIdentity = ObjectIdentity
radEP4FL = _RadEP4FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 5)
)
_RadEPR8T_ObjectIdentity = ObjectIdentity
radEPR8T = _RadEPR8T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 7)
)
_RadEPR4TAUI_ObjectIdentity = ObjectIdentity
radEPR4TAUI = _RadEPR4TAUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 8)
)
_RadEPR4T2FL_ObjectIdentity = ObjectIdentity
radEPR4T2FL = _RadEPR4T2FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 9)
)
_RadEPR4TFL_ObjectIdentity = ObjectIdentity
radEPR4TFL = _RadEPR4TFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 10)
)
_RadEPR4FL_ObjectIdentity = ObjectIdentity
radEPR4FL = _RadEPR4FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 9, 11)
)
_RadSysRtr_ObjectIdentity = ObjectIdentity
radSysRtr = _RadSysRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11)
)
_RadSysRtrEvents_ObjectIdentity = ObjectIdentity
radSysRtrEvents = _RadSysRtrEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0)
)
if mibBuilder.loadTexts:
    radSysRtrEvents.setStatus("current")
_RadRTED_ObjectIdentity = ObjectIdentity
radRTED = _RadRTED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 1)
)
_RadRTEM_ObjectIdentity = ObjectIdentity
radRTEM = _RadRTEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 2)
)
_RadRTEC_ObjectIdentity = ObjectIdentity
radRTEC = _RadRTEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 3)
)
_RadWebRanger_ObjectIdentity = ObjectIdentity
radWebRanger = _RadWebRanger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 4)
)
_RadTinyRouter_ObjectIdentity = ObjectIdentity
radTinyRouter = _RadTinyRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 5)
)
_RadLA240_ObjectIdentity = ObjectIdentity
radLA240 = _RadLA240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 6)
)
_RadSuperLan_ObjectIdentity = ObjectIdentity
radSuperLan = _RadSuperLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 7)
)
_RadLA240I_ObjectIdentity = ObjectIdentity
radLA240I = _RadLA240I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 8)
)
_RadFcdIsdn_ObjectIdentity = ObjectIdentity
radFcdIsdn = _RadFcdIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 9)
)
_RadEFcdIp_ObjectIdentity = ObjectIdentity
radEFcdIp = _RadEFcdIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 10)
)
_RadFcdIpD_ObjectIdentity = ObjectIdentity
radFcdIpD = _RadFcdIpD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 11)
)
_RadFcdIpM_ObjectIdentity = ObjectIdentity
radFcdIpM = _RadFcdIpM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 12)
)
_RadSysAtm_ObjectIdentity = ObjectIdentity
radSysAtm = _RadSysAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12)
)
_RadSysAtmEvents_ObjectIdentity = ObjectIdentity
radSysAtmEvents = _RadSysAtmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0)
)
if mibBuilder.loadTexts:
    radSysAtmEvents.setStatus("current")
_RadStarSwitch_ObjectIdentity = ObjectIdentity
radStarSwitch = _RadStarSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 1)
)
_RadStarSwitchATM25_ObjectIdentity = ObjectIdentity
radStarSwitchATM25 = _RadStarSwitchATM25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 1, 1)
)
_RadStarSwitchATM25L_ObjectIdentity = ObjectIdentity
radStarSwitchATM25L = _RadStarSwitchATM25L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 1, 2)
)
_RadStarSwitchATM155_ObjectIdentity = ObjectIdentity
radStarSwitchATM155 = _RadStarSwitchATM155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 1, 3)
)
_RadAtmCsuDsu_ObjectIdentity = ObjectIdentity
radAtmCsuDsu = _RadAtmCsuDsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2)
)
_RadAmcdE1_ObjectIdentity = ObjectIdentity
radAmcdE1 = _RadAmcdE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 1)
)
_RadAmcdT1_ObjectIdentity = ObjectIdentity
radAmcdT1 = _RadAmcdT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 2)
)
_RadAce20E_ObjectIdentity = ObjectIdentity
radAce20E = _RadAce20E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 3)
)
_RadAce20T_ObjectIdentity = ObjectIdentity
radAce20T = _RadAce20T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 4)
)
_RadAce2005_ObjectIdentity = ObjectIdentity
radAce2005 = _RadAce2005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 5)
)
_RadAce2002_ObjectIdentity = ObjectIdentity
radAce2002 = _RadAce2002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 6)
)
_RadAce2002E_ObjectIdentity = ObjectIdentity
radAce2002E = _RadAce2002E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 7)
)
_RadAce2E_ObjectIdentity = ObjectIdentity
radAce2E = _RadAce2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 8)
)
_RadAce2T_ObjectIdentity = ObjectIdentity
radAce2T = _RadAce2T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 9)
)
_RadMlAtmE1_ObjectIdentity = ObjectIdentity
radMlAtmE1 = _RadMlAtmE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 10)
)
_RadMlAtmT1_ObjectIdentity = ObjectIdentity
radMlAtmT1 = _RadMlAtmT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 11)
)
_RadAmc102_ObjectIdentity = ObjectIdentity
radAmc102 = _RadAmc102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 12)
)
_RadAmc102c_ObjectIdentity = ObjectIdentity
radAmc102c = _RadAmc102c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 13)
)
_RadAce202_ObjectIdentity = ObjectIdentity
radAce202 = _RadAce202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 2, 14)
)
_RadAce_ObjectIdentity = ObjectIdentity
radAce = _RadAce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 3)
)
_RadAce101_ObjectIdentity = ObjectIdentity
radAce101 = _RadAce101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 3, 1)
)
_RadAce102_ObjectIdentity = ObjectIdentity
radAce102 = _RadAce102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 3, 2)
)
_RadAce50_ObjectIdentity = ObjectIdentity
radAce50 = _RadAce50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 3, 3)
)
_RadSysLA_ObjectIdentity = ObjectIdentity
radSysLA = _RadSysLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 13)
)
_RadLA140_ObjectIdentity = ObjectIdentity
radLA140 = _RadLA140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 13, 1)
)
_RadLA110_ObjectIdentity = ObjectIdentity
radLA110 = _RadLA110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 13, 2)
)
_Agnt_ObjectIdentity = ObjectIdentity
agnt = _Agnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2)
)
_AgnHwVersion_Type = DisplayString
_AgnHwVersion_Object = MibScalar
agnHwVersion = _AgnHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 1),
    _AgnHwVersion_Type()
)
agnHwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnHwVersion.setStatus("current")
_AgnTrapMask_Type = Integer32
_AgnTrapMask_Object = MibScalar
agnTrapMask = _AgnTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 2),
    _AgnTrapMask_Type()
)
agnTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnTrapMask.setStatus("current")
_AgnTrapValue_Type = OctetString
_AgnTrapValue_Object = MibScalar
agnTrapValue = _AgnTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 3),
    _AgnTrapValue_Type()
)
agnTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTrapValue.setStatus("deprecated")
_AgnChangeCnt_Type = Counter32
_AgnChangeCnt_Object = MibScalar
agnChangeCnt = _AgnChangeCnt_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 4),
    _AgnChangeCnt_Type()
)
agnChangeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnChangeCnt.setStatus("current")
_AgnSpecific_Type = ObjectIdentifier
_AgnSpecific_Object = MibScalar
agnSpecific = _AgnSpecific_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 5),
    _AgnSpecific_Type()
)
agnSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSpecific.setStatus("current")
_AgnConfigMsg_Type = OctetString
_AgnConfigMsg_Object = MibScalar
agnConfigMsg = _AgnConfigMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 6),
    _AgnConfigMsg_Type()
)
agnConfigMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnConfigMsg.setStatus("current")
_MngTrapIpTable_Object = MibTable
mngTrapIpTable = _MngTrapIpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7)
)
if mibBuilder.loadTexts:
    mngTrapIpTable.setStatus("current")
_MngEntry_Object = MibTableRow
mngEntry = _MngEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1)
)
mngEntry.setIndexNames(
    (0, "ACE202-MIB", "mngID"),
)
if mibBuilder.loadTexts:
    mngEntry.setStatus("current")
_MngID_Type = Integer32
_MngID_Object = MibTableColumn
mngID = _MngID_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 1),
    _MngID_Type()
)
mngID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mngID.setStatus("current")
_MngIP_Type = IpAddress
_MngIP_Object = MibTableColumn
mngIP = _MngIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 2),
    _MngIP_Type()
)
mngIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngIP.setStatus("current")
_MngIPMask_Type = IpAddress
_MngIPMask_Object = MibTableColumn
mngIPMask = _MngIPMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 3),
    _MngIPMask_Type()
)
mngIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngIPMask.setStatus("deprecated")
_MngTrapMask_Type = Integer32
_MngTrapMask_Object = MibTableColumn
mngTrapMask = _MngTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 4),
    _MngTrapMask_Type()
)
mngTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngTrapMask.setStatus("current")


class _AgnIndication_Type(Integer32):
    """Custom type agnIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 1),
          ("warning", 2),
          ("normal", 3),
          ("minor", 4),
          ("major", 5),
          ("event", 6),
          ("critical", 7))
    )


_AgnIndication_Type.__name__ = "Integer32"
_AgnIndication_Object = MibScalar
agnIndication = _AgnIndication_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 8),
    _AgnIndication_Type()
)
agnIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnIndication.setStatus("current")


class _AgnMonitorModeCmd_Type(Integer32):
    """Custom type agnMonitorModeCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_AgnMonitorModeCmd_Type.__name__ = "Integer32"
_AgnMonitorModeCmd_Object = MibScalar
agnMonitorModeCmd = _AgnMonitorModeCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 9),
    _AgnMonitorModeCmd_Type()
)
agnMonitorModeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnMonitorModeCmd.setStatus("current")
_AgnLed_Type = OctetString
_AgnLed_Object = MibScalar
agnLed = _AgnLed_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 10),
    _AgnLed_Type()
)
agnLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnLed.setStatus("current")
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("current")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1)
)
trapEntry.setIndexNames(
    (0, "ACE202-MIB", "trapID"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("current")
_TrapID_Type = Integer32
_TrapID_Object = MibTableColumn
trapID = _TrapID_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1, 1),
    _TrapID_Type()
)
trapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapID.setStatus("current")
_TrapVal_Type = DisplayString
_TrapVal_Object = MibTableColumn
trapVal = _TrapVal_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1, 2),
    _TrapVal_Type()
)
trapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapVal.setStatus("current")
_TrapTimeSinceOccurrence_Type = TimeTicks
_TrapTimeSinceOccurrence_Object = MibTableColumn
trapTimeSinceOccurrence = _TrapTimeSinceOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1, 3),
    _TrapTimeSinceOccurrence_Type()
)
trapTimeSinceOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTimeSinceOccurrence.setStatus("current")
_FileTransfer_ObjectIdentity = ObjectIdentity
fileTransfer = _FileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12)
)
_FileServerIP_Type = IpAddress
_FileServerIP_Object = MibScalar
fileServerIP = _FileServerIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 1),
    _FileServerIP_Type()
)
fileServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServerIP.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileName.setStatus("current")


class _FileTransCmd_Type(Integer32):
    """Custom type fileTransCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("swDwnLoad", 1),
          ("configDwnLoad", 2),
          ("configUpLoad", 3),
          ("coProcDwnLoad", 4),
          ("stateUpLoad", 5),
          ("dwnLoadUserFile", 6),
          ("upLoadUserFile", 7),
          ("swDwnLoadAndReset", 8),
          ("noOp", 255))
    )


_FileTransCmd_Type.__name__ = "Integer32"
_FileTransCmd_Object = MibScalar
fileTransCmd = _FileTransCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 3),
    _FileTransCmd_Type()
)
fileTransCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransCmd.setStatus("current")
_TftpRetryTimeOut_Type = Integer32
_TftpRetryTimeOut_Object = MibScalar
tftpRetryTimeOut = _TftpRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 4),
    _TftpRetryTimeOut_Type()
)
tftpRetryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRetryTimeOut.setStatus("current")
_TftpTotalTimeOut_Type = Integer32
_TftpTotalTimeOut_Object = MibScalar
tftpTotalTimeOut = _TftpTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 5),
    _TftpTotalTimeOut_Type()
)
tftpTotalTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpTotalTimeOut.setStatus("current")


class _TftpStatus_Type(Integer32):
    """Custom type tftpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 2),
          ("connecting", 3),
          ("transferringData", 4),
          ("endedTimeOut", 5),
          ("endedOk", 6),
          ("error", 7))
    )


_TftpStatus_Type.__name__ = "Integer32"
_TftpStatus_Object = MibScalar
tftpStatus = _TftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 6),
    _TftpStatus_Type()
)
tftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpStatus.setStatus("current")


class _TftpError_Type(OctetString):
    """Custom type tftpError based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TftpError_Type.__name__ = "OctetString"
_TftpError_Object = MibScalar
tftpError = _TftpError_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 7),
    _TftpError_Type()
)
tftpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpError.setStatus("current")
_FileTransferToSubSystems_Type = OctetString
_FileTransferToSubSystems_Object = MibScalar
fileTransferToSubSystems = _FileTransferToSubSystems_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 8),
    _FileTransferToSubSystems_Type()
)
fileTransferToSubSystems.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferToSubSystems.setStatus("current")
_FileNameWithinProduct_Type = DisplayString
_FileNameWithinProduct_Object = MibScalar
fileNameWithinProduct = _FileNameWithinProduct_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 9),
    _FileNameWithinProduct_Type()
)
fileNameWithinProduct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileNameWithinProduct.setStatus("current")
_IntSwdlTable_Object = MibTable
intSwdlTable = _IntSwdlTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10)
)
if mibBuilder.loadTexts:
    intSwdlTable.setStatus("current")
_IntSwdlEntry_Object = MibTableRow
intSwdlEntry = _IntSwdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1)
)
intSwdlEntry.setIndexNames(
    (0, "ACE202-MIB", "intSwdlObjIdx"),
    (0, "ACE202-MIB", "intSwdlFileIdx"),
)
if mibBuilder.loadTexts:
    intSwdlEntry.setStatus("current")
_IntSwdlObjIdx_Type = Integer32
_IntSwdlObjIdx_Object = MibTableColumn
intSwdlObjIdx = _IntSwdlObjIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 1),
    _IntSwdlObjIdx_Type()
)
intSwdlObjIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlObjIdx.setStatus("current")
_IntSwdlFileIdx_Type = Integer32
_IntSwdlFileIdx_Object = MibTableColumn
intSwdlFileIdx = _IntSwdlFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 2),
    _IntSwdlFileIdx_Type()
)
intSwdlFileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlFileIdx.setStatus("current")
_IntSwdlFileName_Type = DisplayString
_IntSwdlFileName_Object = MibTableColumn
intSwdlFileName = _IntSwdlFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 3),
    _IntSwdlFileName_Type()
)
intSwdlFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlFileName.setStatus("current")
_IntSwdlFileSwVer_Type = DisplayString
_IntSwdlFileSwVer_Object = MibTableColumn
intSwdlFileSwVer = _IntSwdlFileSwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 4),
    _IntSwdlFileSwVer_Type()
)
intSwdlFileSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlFileSwVer.setStatus("current")
_IntSwdlSwDate_Type = DisplayString
_IntSwdlSwDate_Object = MibTableColumn
intSwdlSwDate = _IntSwdlSwDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 5),
    _IntSwdlSwDate_Type()
)
intSwdlSwDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlSwDate.setStatus("current")
_IntSwdlSize_Type = DisplayString
_IntSwdlSize_Object = MibTableColumn
intSwdlSize = _IntSwdlSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 6),
    _IntSwdlSize_Type()
)
intSwdlSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlSize.setStatus("current")


class _IntSwdlCmd_Type(Integer32):
    """Custom type intSwdlCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_IntSwdlCmd_Type.__name__ = "Integer32"
_IntSwdlCmd_Object = MibTableColumn
intSwdlCmd = _IntSwdlCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 7),
    _IntSwdlCmd_Type()
)
intSwdlCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intSwdlCmd.setStatus("current")
_IntSwdlToSubSystem_Type = OctetString
_IntSwdlToSubSystem_Object = MibTableColumn
intSwdlToSubSystem = _IntSwdlToSubSystem_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 8),
    _IntSwdlToSubSystem_Type()
)
intSwdlToSubSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intSwdlToSubSystem.setStatus("current")
_SwdlStatusTable_Object = MibTable
swdlStatusTable = _SwdlStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11)
)
if mibBuilder.loadTexts:
    swdlStatusTable.setStatus("current")
_SwdlStatusEntry_Object = MibTableRow
swdlStatusEntry = _SwdlStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1)
)
swdlStatusEntry.setIndexNames(
    (0, "ACE202-MIB", "swdlStatusTypeIdx"),
    (0, "ACE202-MIB", "swdlStatusIdx"),
)
if mibBuilder.loadTexts:
    swdlStatusEntry.setStatus("current")
_SwdlStatusTypeIdx_Type = Integer32
_SwdlStatusTypeIdx_Object = MibTableColumn
swdlStatusTypeIdx = _SwdlStatusTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 1),
    _SwdlStatusTypeIdx_Type()
)
swdlStatusTypeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusTypeIdx.setStatus("current")
_SwdlStatusIdx_Type = Integer32
_SwdlStatusIdx_Object = MibTableColumn
swdlStatusIdx = _SwdlStatusIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 2),
    _SwdlStatusIdx_Type()
)
swdlStatusIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusIdx.setStatus("current")
_SwdlStatusFileName_Type = DisplayString
_SwdlStatusFileName_Object = MibTableColumn
swdlStatusFileName = _SwdlStatusFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 3),
    _SwdlStatusFileName_Type()
)
swdlStatusFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusFileName.setStatus("current")
_SwdlStatusSlot_Type = DisplayString
_SwdlStatusSlot_Object = MibTableColumn
swdlStatusSlot = _SwdlStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 4),
    _SwdlStatusSlot_Type()
)
swdlStatusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusSlot.setStatus("current")
_SwdlStatusSubSystem_Type = DisplayString
_SwdlStatusSubSystem_Object = MibTableColumn
swdlStatusSubSystem = _SwdlStatusSubSystem_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 5),
    _SwdlStatusSubSystem_Type()
)
swdlStatusSubSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusSubSystem.setStatus("current")
_SwdlStatusStatus_Type = Integer32
_SwdlStatusStatus_Object = MibTableColumn
swdlStatusStatus = _SwdlStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 6),
    _SwdlStatusStatus_Type()
)
swdlStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusStatus.setStatus("current")
_SwdlStatusTime_Type = DisplayString
_SwdlStatusTime_Object = MibTableColumn
swdlStatusTime = _SwdlStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 7),
    _SwdlStatusTime_Type()
)
swdlStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusTime.setStatus("current")
_ClearDwldStatusLog_Type = Integer32
_ClearDwldStatusLog_Object = MibScalar
clearDwldStatusLog = _ClearDwldStatusLog_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 12),
    _ClearDwldStatusLog_Type()
)
clearDwldStatusLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearDwldStatusLog.setStatus("current")


class _SystemReset_Type(Integer32):
    """Custom type systemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("resetConfig", 4))
    )


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 13),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_SystemTiming_ObjectIdentity = ObjectIdentity
systemTiming = _SystemTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 14)
)
_SystemDate_Type = DisplayString
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 14, 1),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 14, 2),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_SystemPort_ObjectIdentity = ObjectIdentity
systemPort = _SystemPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15)
)
_PhysicalConnectorTable_Object = MibTable
physicalConnectorTable = _PhysicalConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 1)
)
if mibBuilder.loadTexts:
    physicalConnectorTable.setStatus("current")
_PhysicalConnectorEntry_Object = MibTableRow
physicalConnectorEntry = _PhysicalConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 1, 1)
)
physicalConnectorEntry.setIndexNames(
    (0, "ACE202-MIB", "portIdx"),
)
if mibBuilder.loadTexts:
    physicalConnectorEntry.setStatus("current")
_PortIdx_Type = Integer32
_PortIdx_Object = MibTableColumn
portIdx = _PortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 1, 1, 1),
    _PortIdx_Type()
)
portIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIdx.setStatus("current")


class _PhysicalConnector_Type(Integer32):
    """Custom type physicalConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              255)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("v35", 2),
          ("rs530", 3),
          ("x21", 4),
          ("bnc", 5),
          ("utp", 6),
          ("aui", 7),
          ("rs422", 8),
          ("crossUtp", 9),
          ("rj45", 10),
          ("v24", 11),
          ("g703", 12),
          ("termBlock3AndRj45", 13),
          ("terminalBlock3", 14),
          ("terminalBlock5", 15),
          ("terminalBlock7", 16),
          ("db25", 17),
          ("db15", 18),
          ("rj45ethernet", 19),
          ("termBlock5AndRj45", 20),
          ("db9", 21),
          ("g703E1", 22),
          ("g703E1-LTU", 23),
          ("sc", 24),
          ("st", 25),
          ("stl", 26),
          ("fc", 27),
          ("tb5w", 28),
          ("termBlock6AndRj45", 29),
          ("ethBnc", 30),
          ("scsi26", 31),
          ("eth4381", 32),
          ("twoBnc", 33),
          ("scsi50", 34),
          ("twoMiniBnc", 35),
          ("sf1", 36),
          ("terminalBlock4", 37),
          ("sf2", 38),
          ("db25Balanced", 39),
          ("v36", 40),
          ("block4W", 41),
          ("iripRj45", 42),
          ("irEthQRj45", 43),
          ("iripBnc", 44),
          ("rs530WA", 45),
          ("v35WA", 46),
          ("irEthQBnc", 47),
          ("v35Db25", 48),
          ("rj11", 49),
          ("mtrj", 50),
          ("lc", 51),
          ("terminalBlock2", 52),
          ("irEth10s100", 53),
          ("scsi68", 54),
          ("none", 255))
    )


_PhysicalConnector_Type.__name__ = "Integer32"
_PhysicalConnector_Object = MibTableColumn
physicalConnector = _PhysicalConnector_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 1, 1, 2),
    _PhysicalConnector_Type()
)
physicalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalConnector.setStatus("current")


class _PortOptWaveLength_Type(Integer32):
    """Custom type portOptWaveLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("nm850", 2),
          ("nm1300", 3),
          ("nm1300Laser", 4),
          ("nm1550Laser", 5))
    )


_PortOptWaveLength_Type.__name__ = "Integer32"
_PortOptWaveLength_Object = MibTableColumn
portOptWaveLength = _PortOptWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 1, 1, 3),
    _PortOptWaveLength_Type()
)
portOptWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOptWaveLength.setStatus("current")


class _PortOptMode_Type(Integer32):
    """Custom type portOptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("singleMode", 2),
          ("multiMode", 3))
    )


_PortOptMode_Type.__name__ = "Integer32"
_PortOptMode_Object = MibTableColumn
portOptMode = _PortOptMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 1, 1, 4),
    _PortOptMode_Type()
)
portOptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOptMode.setStatus("current")
_PrtSupervisory_ObjectIdentity = ObjectIdentity
prtSupervisory = _PrtSupervisory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2)
)
_PrtSpTable_Object = MibTable
prtSpTable = _PrtSpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    prtSpTable.setStatus("current")
_PrtSpEntry_Object = MibTableRow
prtSpEntry = _PrtSpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1)
)
prtSpEntry.setIndexNames(
    (0, "ACE202-MIB", "prtSupervisoryIndex"),
)
if mibBuilder.loadTexts:
    prtSpEntry.setStatus("current")
_PrtSupervisoryIndex_Type = Integer32
_PrtSupervisoryIndex_Object = MibTableColumn
prtSupervisoryIndex = _PrtSupervisoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 1),
    _PrtSupervisoryIndex_Type()
)
prtSupervisoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSupervisoryIndex.setStatus("current")


class _PrtSupervisoryRate_Type(Integer32):
    """Custom type prtSupervisoryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("s300bps", 2),
          ("s1200bps", 3),
          ("s2400bps", 4),
          ("s4800bps", 5),
          ("s9600bps", 6),
          ("s19200bps", 7),
          ("s38400bps", 8),
          ("s57600bps", 9),
          ("s115200bps", 10))
    )


_PrtSupervisoryRate_Type.__name__ = "Integer32"
_PrtSupervisoryRate_Object = MibTableColumn
prtSupervisoryRate = _PrtSupervisoryRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 2),
    _PrtSupervisoryRate_Type()
)
prtSupervisoryRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryRate.setStatus("current")


class _PrtSupervisoryDataBits_Type(Integer32):
    """Custom type prtSupervisoryDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataBits7", 1),
          ("dataBits8", 2))
    )


_PrtSupervisoryDataBits_Type.__name__ = "Integer32"
_PrtSupervisoryDataBits_Object = MibTableColumn
prtSupervisoryDataBits = _PrtSupervisoryDataBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 3),
    _PrtSupervisoryDataBits_Type()
)
prtSupervisoryDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryDataBits.setStatus("current")


class _PrtSupervisoryParity_Type(Integer32):
    """Custom type prtSupervisoryParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("odd", 2),
          ("even", 3))
    )


_PrtSupervisoryParity_Type.__name__ = "Integer32"
_PrtSupervisoryParity_Object = MibTableColumn
prtSupervisoryParity = _PrtSupervisoryParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 4),
    _PrtSupervisoryParity_Type()
)
prtSupervisoryParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryParity.setStatus("current")


class _PrtSupervisoryStopBits_Type(Integer32):
    """Custom type prtSupervisoryStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("stopBits1", 2),
          ("stopBits1dot5", 3),
          ("stopBits2", 4))
    )


_PrtSupervisoryStopBits_Type.__name__ = "Integer32"
_PrtSupervisoryStopBits_Object = MibTableColumn
prtSupervisoryStopBits = _PrtSupervisoryStopBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 5),
    _PrtSupervisoryStopBits_Type()
)
prtSupervisoryStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSupervisoryStopBits.setStatus("current")


class _PrtSupervisoryUsage_Type(Integer32):
    """Custom type prtSupervisoryUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("noUse", 2),
          ("terminal", 3),
          ("nmsSlip", 4),
          ("nmsPpp", 5),
          ("muxSlip", 6),
          ("muxPpp", 7),
          ("dialOut", 8))
    )


_PrtSupervisoryUsage_Type.__name__ = "Integer32"
_PrtSupervisoryUsage_Object = MibTableColumn
prtSupervisoryUsage = _PrtSupervisoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 6),
    _PrtSupervisoryUsage_Type()
)
prtSupervisoryUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryUsage.setStatus("current")


class _PrtSupervisoryInterface_Type(Integer32):
    """Custom type prtSupervisoryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("dce", 2),
          ("dte", 3))
    )


_PrtSupervisoryInterface_Type.__name__ = "Integer32"
_PrtSupervisoryInterface_Object = MibTableColumn
prtSupervisoryInterface = _PrtSupervisoryInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 7),
    _PrtSupervisoryInterface_Type()
)
prtSupervisoryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryInterface.setStatus("current")


class _PrtSupervisoryCTS_Type(Integer32):
    """Custom type prtSupervisoryCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("on", 2),
          ("rts", 3),
          ("dteWait", 4),
          ("dteIgnore", 5))
    )


_PrtSupervisoryCTS_Type.__name__ = "Integer32"
_PrtSupervisoryCTS_Object = MibTableColumn
prtSupervisoryCTS = _PrtSupervisoryCTS_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 8),
    _PrtSupervisoryCTS_Type()
)
prtSupervisoryCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryCTS.setStatus("current")


class _PrtSupervisoryDcdDelay_Type(Integer32):
    """Custom type prtSupervisoryDcdDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("d0", 2),
          ("d10", 3),
          ("d50", 4),
          ("d100", 5),
          ("d200", 6),
          ("d300", 7))
    )


_PrtSupervisoryDcdDelay_Type.__name__ = "Integer32"
_PrtSupervisoryDcdDelay_Object = MibTableColumn
prtSupervisoryDcdDelay = _PrtSupervisoryDcdDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 9),
    _PrtSupervisoryDcdDelay_Type()
)
prtSupervisoryDcdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryDcdDelay.setStatus("current")


class _PrtSupervisoryDSR_Type(Integer32):
    """Custom type prtSupervisoryDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("on", 2),
          ("dtr", 3))
    )


_PrtSupervisoryDSR_Type.__name__ = "Integer32"
_PrtSupervisoryDSR_Object = MibTableColumn
prtSupervisoryDSR = _PrtSupervisoryDSR_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 10),
    _PrtSupervisoryDSR_Type()
)
prtSupervisoryDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryDSR.setStatus("current")


class _PrtSupervisoryRoutProtocol_Type(Integer32):
    """Custom type prtSupervisoryRoutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3),
          ("rip2", 4))
    )


_PrtSupervisoryRoutProtocol_Type.__name__ = "Integer32"
_PrtSupervisoryRoutProtocol_Object = MibTableColumn
prtSupervisoryRoutProtocol = _PrtSupervisoryRoutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 2, 1, 1, 11),
    _PrtSupervisoryRoutProtocol_Type()
)
prtSupervisoryRoutProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSupervisoryRoutProtocol.setStatus("current")
_PrtPerformance_ObjectIdentity = ObjectIdentity
prtPerformance = _PrtPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3)
)
_PrtPerfTable_Object = MibTable
prtPerfTable = _PrtPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    prtPerfTable.setStatus("current")
_PrtPerfEntry_Object = MibTableRow
prtPerfEntry = _PrtPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1)
)
prtPerfEntry.setIndexNames(
    (0, "ACE202-MIB", "prtPerfIdx"),
    (0, "ACE202-MIB", "prtPerfPeriodRef"),
)
if mibBuilder.loadTexts:
    prtPerfEntry.setStatus("current")
_PrtPerfIdx_Type = Integer32
_PrtPerfIdx_Object = MibTableColumn
prtPerfIdx = _PrtPerfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 1),
    _PrtPerfIdx_Type()
)
prtPerfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfIdx.setStatus("current")


class _PrtPerfPeriodRef_Type(Integer32):
    """Custom type prtPerfPeriodRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentPeriod", 1),
          ("lastPeriod", 2))
    )


_PrtPerfPeriodRef_Type.__name__ = "Integer32"
_PrtPerfPeriodRef_Object = MibTableColumn
prtPerfPeriodRef = _PrtPerfPeriodRef_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 2),
    _PrtPerfPeriodRef_Type()
)
prtPerfPeriodRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfPeriodRef.setStatus("current")
_PrtPerfElapsedTime_Type = Integer32
_PrtPerfElapsedTime_Object = MibTableColumn
prtPerfElapsedTime = _PrtPerfElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 3),
    _PrtPerfElapsedTime_Type()
)
prtPerfElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfElapsedTime.setStatus("current")
_PrtPerfUAS_Type = Integer32
_PrtPerfUAS_Object = MibTableColumn
prtPerfUAS = _PrtPerfUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 4),
    _PrtPerfUAS_Type()
)
prtPerfUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfUAS.setStatus("current")
_PrtPerfES_Type = Integer32
_PrtPerfES_Object = MibTableColumn
prtPerfES = _PrtPerfES_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 5),
    _PrtPerfES_Type()
)
prtPerfES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfES.setStatus("current")
_PrtPerfSES_Type = Integer32
_PrtPerfSES_Object = MibTableColumn
prtPerfSES = _PrtPerfSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 6),
    _PrtPerfSES_Type()
)
prtPerfSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfSES.setStatus("current")
_PrtPerfBBE_Type = Integer32
_PrtPerfBBE_Object = MibTableColumn
prtPerfBBE = _PrtPerfBBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 7),
    _PrtPerfBBE_Type()
)
prtPerfBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfBBE.setStatus("current")
_PrtPerfBlocksPerSec_Type = Integer32
_PrtPerfBlocksPerSec_Object = MibTableColumn
prtPerfBlocksPerSec = _PrtPerfBlocksPerSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 8),
    _PrtPerfBlocksPerSec_Type()
)
prtPerfBlocksPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfBlocksPerSec.setStatus("current")
_PrtPerfTimeTag_Type = TimeTicks
_PrtPerfTimeTag_Object = MibTableColumn
prtPerfTimeTag = _PrtPerfTimeTag_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 9),
    _PrtPerfTimeTag_Type()
)
prtPerfTimeTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPerfTimeTag.setStatus("current")


class _PrtPerfSaveAndResetCmd_Type(Integer32):
    """Custom type prtPerfSaveAndResetCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtPerfSaveAndResetCmd_Type.__name__ = "Integer32"
_PrtPerfSaveAndResetCmd_Object = MibTableColumn
prtPerfSaveAndResetCmd = _PrtPerfSaveAndResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 3, 1, 1, 10),
    _PrtPerfSaveAndResetCmd_Type()
)
prtPerfSaveAndResetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPerfSaveAndResetCmd.setStatus("current")
_PrtTest_ObjectIdentity = ObjectIdentity
prtTest = _PrtTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 4)
)
_PrtTestTable_Object = MibTable
prtTestTable = _PrtTestTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 4, 1)
)
if mibBuilder.loadTexts:
    prtTestTable.setStatus("current")
_PrtTestEntry_Object = MibTableRow
prtTestEntry = _PrtTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 4, 1, 1)
)
prtTestEntry.setIndexNames(
    (0, "ACE202-MIB", "prtTestIdx"),
)
if mibBuilder.loadTexts:
    prtTestEntry.setStatus("current")
_PrtTestIdx_Type = Integer32
_PrtTestIdx_Object = MibTableColumn
prtTestIdx = _PrtTestIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 4, 1, 1, 1),
    _PrtTestIdx_Type()
)
prtTestIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtTestIdx.setStatus("current")
_PrtTestCmdAndStatus_Type = Integer32
_PrtTestCmdAndStatus_Object = MibTableColumn
prtTestCmdAndStatus = _PrtTestCmdAndStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 4, 1, 1, 2),
    _PrtTestCmdAndStatus_Type()
)
prtTestCmdAndStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtTestCmdAndStatus.setStatus("current")
_PrtBertCounter_Type = Integer32
_PrtBertCounter_Object = MibTableColumn
prtBertCounter = _PrtBertCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 4, 1, 1, 3),
    _PrtBertCounter_Type()
)
prtBertCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertCounter.setStatus("current")


class _PrtTestInitiator_Type(Integer32):
    """Custom type prtTestInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("user", 2),
          ("remoteUnit", 3),
          ("dteRouter", 4))
    )


_PrtTestInitiator_Type.__name__ = "Integer32"
_PrtTestInitiator_Object = MibTableColumn
prtTestInitiator = _PrtTestInitiator_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 4, 1, 1, 4),
    _PrtTestInitiator_Type()
)
prtTestInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtTestInitiator.setStatus("current")
_PrtParam_ObjectIdentity = ObjectIdentity
prtParam = _PrtParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5)
)
_PrtParamTable_Object = MibTable
prtParamTable = _PrtParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1)
)
if mibBuilder.loadTexts:
    prtParamTable.setStatus("current")
_PrtParamEntry_Object = MibTableRow
prtParamEntry = _PrtParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1, 1)
)
prtParamEntry.setIndexNames(
    (0, "ACE202-MIB", "prtParamIdx"),
)
if mibBuilder.loadTexts:
    prtParamEntry.setStatus("current")
_PrtParamIdx_Type = Integer32
_PrtParamIdx_Object = MibTableColumn
prtParamIdx = _PrtParamIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1, 1, 1),
    _PrtParamIdx_Type()
)
prtParamIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtParamIdx.setStatus("current")
_PrtControlCnfg_Type = Integer32
_PrtControlCnfg_Object = MibTableColumn
prtControlCnfg = _PrtControlCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1, 1, 2),
    _PrtControlCnfg_Type()
)
prtControlCnfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtControlCnfg.setStatus("current")


class _PrtParamClkSrc_Type(Integer32):
    """Custom type prtParamClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4),
          ("notApplicable", 255))
    )


_PrtParamClkSrc_Type.__name__ = "Integer32"
_PrtParamClkSrc_Object = MibTableColumn
prtParamClkSrc = _PrtParamClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1, 1, 3),
    _PrtParamClkSrc_Type()
)
prtParamClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtParamClkSrc.setStatus("current")


class _PrtParamPhantom_Type(Integer32):
    """Custom type prtParamPhantom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PrtParamPhantom_Type.__name__ = "Integer32"
_PrtParamPhantom_Object = MibTableColumn
prtParamPhantom = _PrtParamPhantom_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1, 1, 4),
    _PrtParamPhantom_Type()
)
prtParamPhantom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtParamPhantom.setStatus("current")


class _PrtParamResetStatsCmd_Type(Integer32):
    """Custom type prtParamResetStatsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtParamResetStatsCmd_Type.__name__ = "Integer32"
_PrtParamResetStatsCmd_Object = MibTableColumn
prtParamResetStatsCmd = _PrtParamResetStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1, 1, 5),
    _PrtParamResetStatsCmd_Type()
)
prtParamResetStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtParamResetStatsCmd.setStatus("current")
_PrtParamLastResetStatsTime_Type = TimeStamp
_PrtParamLastResetStatsTime_Object = MibTableColumn
prtParamLastResetStatsTime = _PrtParamLastResetStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 5, 1, 1, 6),
    _PrtParamLastResetStatsTime_Type()
)
prtParamLastResetStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtParamLastResetStatsTime.setStatus("current")
_PrtIP_ObjectIdentity = ObjectIdentity
prtIP = _PrtIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6)
)
_PrtIpParamTable_Object = MibTable
prtIpParamTable = _PrtIpParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1)
)
if mibBuilder.loadTexts:
    prtIpParamTable.setStatus("current")
_PrtIpParamEntry_Object = MibTableRow
prtIpParamEntry = _PrtIpParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1)
)
prtIpParamEntry.setIndexNames(
    (0, "ACE202-MIB", "prtIpParamConfigIdx"),
    (0, "ACE202-MIB", "prtIpParamSlotIdx"),
    (0, "ACE202-MIB", "prtIpParamIdx"),
)
if mibBuilder.loadTexts:
    prtIpParamEntry.setStatus("current")
_PrtIpParamConfigIdx_Type = Integer32
_PrtIpParamConfigIdx_Object = MibTableColumn
prtIpParamConfigIdx = _PrtIpParamConfigIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 1),
    _PrtIpParamConfigIdx_Type()
)
prtIpParamConfigIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIpParamConfigIdx.setStatus("current")
_PrtIpParamSlotIdx_Type = Integer32
_PrtIpParamSlotIdx_Object = MibTableColumn
prtIpParamSlotIdx = _PrtIpParamSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 2),
    _PrtIpParamSlotIdx_Type()
)
prtIpParamSlotIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIpParamSlotIdx.setStatus("current")
_PrtIpParamIdx_Type = Integer32
_PrtIpParamIdx_Object = MibTableColumn
prtIpParamIdx = _PrtIpParamIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 3),
    _PrtIpParamIdx_Type()
)
prtIpParamIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIpParamIdx.setStatus("current")
_PrtIpParamHostIP_Type = IpAddress
_PrtIpParamHostIP_Object = MibTableColumn
prtIpParamHostIP = _PrtIpParamHostIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 4),
    _PrtIpParamHostIP_Type()
)
prtIpParamHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIpParamHostIP.setStatus("current")
_PrtIpParamHostMask_Type = IpAddress
_PrtIpParamHostMask_Object = MibTableColumn
prtIpParamHostMask = _PrtIpParamHostMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 5),
    _PrtIpParamHostMask_Type()
)
prtIpParamHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIpParamHostMask.setStatus("current")
_PrtIpParamDefaultGateway_Type = IpAddress
_PrtIpParamDefaultGateway_Object = MibTableColumn
prtIpParamDefaultGateway = _PrtIpParamDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 6),
    _PrtIpParamDefaultGateway_Type()
)
prtIpParamDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIpParamDefaultGateway.setStatus("current")


class _PrtIpParamMediaMode_Type(Integer32):
    """Custom type prtIpParamMediaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_PrtIpParamMediaMode_Type.__name__ = "Integer32"
_PrtIpParamMediaMode_Object = MibTableColumn
prtIpParamMediaMode = _PrtIpParamMediaMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 7),
    _PrtIpParamMediaMode_Type()
)
prtIpParamMediaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIpParamMediaMode.setStatus("current")


class _PrtIpParamMediaRate_Type(Integer32):
    """Custom type prtIpParamMediaRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("r10Mbps", 2),
          ("r100Mbps", 3))
    )


_PrtIpParamMediaRate_Type.__name__ = "Integer32"
_PrtIpParamMediaRate_Object = MibTableColumn
prtIpParamMediaRate = _PrtIpParamMediaRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 8),
    _PrtIpParamMediaRate_Type()
)
prtIpParamMediaRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIpParamMediaRate.setStatus("current")


class _PrtIpParamMngVlanSupport_Type(Integer32):
    """Custom type prtIpParamMngVlanSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_PrtIpParamMngVlanSupport_Type.__name__ = "Integer32"
_PrtIpParamMngVlanSupport_Object = MibTableColumn
prtIpParamMngVlanSupport = _PrtIpParamMngVlanSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 9),
    _PrtIpParamMngVlanSupport_Type()
)
prtIpParamMngVlanSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIpParamMngVlanSupport.setStatus("current")
_PrtIpParamMngVlanId_Type = Integer32
_PrtIpParamMngVlanId_Object = MibTableColumn
prtIpParamMngVlanId = _PrtIpParamMngVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 10),
    _PrtIpParamMngVlanId_Type()
)
prtIpParamMngVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIpParamMngVlanId.setStatus("current")
_PrtIpParamMngVlanPriority_Type = Integer32
_PrtIpParamMngVlanPriority_Object = MibTableColumn
prtIpParamMngVlanPriority = _PrtIpParamMngVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 11),
    _PrtIpParamMngVlanPriority_Type()
)
prtIpParamMngVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIpParamMngVlanPriority.setStatus("current")


class _PrtIpParamRingMode_Type(Integer32):
    """Custom type prtIpParamRingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PrtIpParamRingMode_Type.__name__ = "Integer32"
_PrtIpParamRingMode_Object = MibTableColumn
prtIpParamRingMode = _PrtIpParamRingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 15, 6, 1, 1, 12),
    _PrtIpParamRingMode_Type()
)
prtIpParamRingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIpParamRingMode.setStatus("current")


class _SystemResetAllStatsCmd_Type(Integer32):
    """Custom type systemResetAllStatsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SystemResetAllStatsCmd_Type.__name__ = "Integer32"
_SystemResetAllStatsCmd_Object = MibScalar
systemResetAllStatsCmd = _SystemResetAllStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 16),
    _SystemResetAllStatsCmd_Type()
)
systemResetAllStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResetAllStatsCmd.setStatus("current")


class _SystemClearTablesCmd_Type(Integer32):
    """Custom type systemClearTablesCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("tempCnfgTables", 3))
    )


_SystemClearTablesCmd_Type.__name__ = "Integer32"
_SystemClearTablesCmd_Object = MibScalar
systemClearTablesCmd = _SystemClearTablesCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 17),
    _SystemClearTablesCmd_Type()
)
systemClearTablesCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemClearTablesCmd.setStatus("current")
_SystemParameter_Type = Integer32
_SystemParameter_Object = MibScalar
systemParameter = _SystemParameter_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 18),
    _SystemParameter_Type()
)
systemParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemParameter.setStatus("current")
_AgnGlobalAlarmMask_Type = OctetString
_AgnGlobalAlarmMask_Object = MibScalar
agnGlobalAlarmMask = _AgnGlobalAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 19),
    _AgnGlobalAlarmMask_Type()
)
agnGlobalAlarmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnGlobalAlarmMask.setStatus("current")


class _AlarmSeverity_Type(Integer32):
    """Custom type alarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AlarmSeverity_Type.__name__ = "Integer32"
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 20),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")


class _AlarmState_Type(Integer32):
    """Custom type alarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AlarmState_Type.__name__ = "Integer32"
_AlarmState_Object = MibScalar
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 21),
    _AlarmState_Type()
)
alarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")


class _AgnTestStatus_Type(Integer32):
    """Custom type agnTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnTestStatus_Type.__name__ = "Integer32"
_AgnTestStatus_Object = MibScalar
agnTestStatus = _AgnTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 22),
    _AgnTestStatus_Type()
)
agnTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTestStatus.setStatus("current")


class _SystemSaveAndResetAllStatsCmd_Type(Integer32):
    """Custom type systemSaveAndResetAllStatsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SystemSaveAndResetAllStatsCmd_Type.__name__ = "Integer32"
_SystemSaveAndResetAllStatsCmd_Object = MibScalar
systemSaveAndResetAllStatsCmd = _SystemSaveAndResetAllStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 23),
    _SystemSaveAndResetAllStatsCmd_Type()
)
systemSaveAndResetAllStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSaveAndResetAllStatsCmd.setStatus("current")
_SystemDefaultGateway_Type = IpAddress
_SystemDefaultGateway_Object = MibScalar
systemDefaultGateway = _SystemDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 24),
    _SystemDefaultGateway_Type()
)
systemDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDefaultGateway.setStatus("current")
_SystemPsTable_Object = MibTable
systemPsTable = _SystemPsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 25)
)
if mibBuilder.loadTexts:
    systemPsTable.setStatus("current")
_SystemPsEntry_Object = MibTableRow
systemPsEntry = _SystemPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 25, 1)
)
systemPsEntry.setIndexNames(
    (0, "ACE202-MIB", "systemPsIndex1"),
    (0, "ACE202-MIB", "systemPsIndex2"),
)
if mibBuilder.loadTexts:
    systemPsEntry.setStatus("current")
_SystemPsIndex1_Type = Integer32
_SystemPsIndex1_Object = MibTableColumn
systemPsIndex1 = _SystemPsIndex1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 25, 1, 1),
    _SystemPsIndex1_Type()
)
systemPsIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPsIndex1.setStatus("current")
_SystemPsIndex2_Type = Integer32
_SystemPsIndex2_Object = MibTableColumn
systemPsIndex2 = _SystemPsIndex2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 25, 1, 2),
    _SystemPsIndex2_Type()
)
systemPsIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPsIndex2.setStatus("current")


class _SystemPsType_Type(Integer32):
    """Custom type systemPsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ac", 2),
          ("dc", 3),
          ("acDc", 4),
          ("acPF", 5),
          ("dcPF", 6))
    )


_SystemPsType_Type.__name__ = "Integer32"
_SystemPsType_Object = MibTableColumn
systemPsType = _SystemPsType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 25, 1, 3),
    _SystemPsType_Type()
)
systemPsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPsType.setStatus("current")


class _SystemPsStatus_Type(Integer32):
    """Custom type systemPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("failed", 2),
          ("ok", 3))
    )


_SystemPsStatus_Type.__name__ = "Integer32"
_SystemPsStatus_Object = MibTableColumn
systemPsStatus = _SystemPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 25, 1, 4),
    _SystemPsStatus_Type()
)
systemPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPsStatus.setStatus("current")


class _XcIndexNext_Type(Integer32):
    """Custom type xcIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XcIndexNext_Type.__name__ = "Integer32"
_XcIndexNext_Object = MibScalar
xcIndexNext = _XcIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 30),
    _XcIndexNext_Type()
)
xcIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcIndexNext.setStatus("current")
_XcTable_Object = MibTable
xcTable = _XcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31)
)
if mibBuilder.loadTexts:
    xcTable.setStatus("current")
_XcEntry_Object = MibTableRow
xcEntry = _XcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1)
)
xcEntry.setIndexNames(
    (0, "ACE202-MIB", "xcIndex"),
    (0, "ACE202-MIB", "xcIfIndex1"),
    (0, "ACE202-MIB", "xcVpi"),
    (0, "ACE202-MIB", "xcVci"),
    (0, "ACE202-MIB", "xcIfIndex2"),
)
if mibBuilder.loadTexts:
    xcEntry.setStatus("current")
_XcIndex_Type = Integer32
_XcIndex_Object = MibTableColumn
xcIndex = _XcIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 1),
    _XcIndex_Type()
)
xcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcIndex.setStatus("current")
_XcIfIndex1_Type = Integer32
_XcIfIndex1_Object = MibTableColumn
xcIfIndex1 = _XcIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 2),
    _XcIfIndex1_Type()
)
xcIfIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcIfIndex1.setStatus("current")
_XcVpi_Type = Integer32
_XcVpi_Object = MibTableColumn
xcVpi = _XcVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 3),
    _XcVpi_Type()
)
xcVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcVpi.setStatus("current")
_XcVci_Type = Integer32
_XcVci_Object = MibTableColumn
xcVci = _XcVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 4),
    _XcVci_Type()
)
xcVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcVci.setStatus("current")
_XcIfIndex2_Type = Integer32
_XcIfIndex2_Object = MibTableColumn
xcIfIndex2 = _XcIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 5),
    _XcIfIndex2_Type()
)
xcIfIndex2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcIfIndex2.setStatus("current")
_XcRowStatus_Type = RowStatus
_XcRowStatus_Object = MibTableColumn
xcRowStatus = _XcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 6),
    _XcRowStatus_Type()
)
xcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcRowStatus.setStatus("current")
_XcDescr_Type = DisplayString
_XcDescr_Object = MibTableColumn
xcDescr = _XcDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 7),
    _XcDescr_Type()
)
xcDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcDescr.setStatus("current")


class _XcAdminStatus_Type(Integer32):
    """Custom type xcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_XcAdminStatus_Type.__name__ = "Integer32"
_XcAdminStatus_Object = MibTableColumn
xcAdminStatus = _XcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 8),
    _XcAdminStatus_Type()
)
xcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcAdminStatus.setStatus("current")


class _XcOperStatus_Type(Integer32):
    """Custom type xcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_XcOperStatus_Type.__name__ = "Integer32"
_XcOperStatus_Object = MibTableColumn
xcOperStatus = _XcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 31, 1, 9),
    _XcOperStatus_Type()
)
xcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcOperStatus.setStatus("current")
_SystemModule_ObjectIdentity = ObjectIdentity
systemModule = _SystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 32)
)
_ModlParam_ObjectIdentity = ObjectIdentity
modlParam = _ModlParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 32, 1)
)
_ModlParamTable_Object = MibTable
modlParamTable = _ModlParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 32, 1, 1)
)
if mibBuilder.loadTexts:
    modlParamTable.setStatus("current")
_ModlParamEntry_Object = MibTableRow
modlParamEntry = _ModlParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 32, 1, 1, 1)
)
modlParamEntry.setIndexNames(
    (0, "ACE202-MIB", "modlParamIndex"),
)
if mibBuilder.loadTexts:
    modlParamEntry.setStatus("current")
_ModlParamIndex_Type = Integer32
_ModlParamIndex_Object = MibTableColumn
modlParamIndex = _ModlParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 32, 1, 1, 1, 1),
    _ModlParamIndex_Type()
)
modlParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modlParamIndex.setStatus("current")


class _ModlParamReset_Type(Integer32):
    """Custom type modlParamReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("factory", 4))
    )


_ModlParamReset_Type.__name__ = "Integer32"
_ModlParamReset_Object = MibTableColumn
modlParamReset = _ModlParamReset_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 32, 1, 1, 1, 2),
    _ModlParamReset_Type()
)
modlParamReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modlParamReset.setStatus("current")


class _ModlParamSwdlStatus_Type(Integer32):
    """Custom type modlParamSwdlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("inProcess", 3))
    )


_ModlParamSwdlStatus_Type.__name__ = "Integer32"
_ModlParamSwdlStatus_Object = MibTableColumn
modlParamSwdlStatus = _ModlParamSwdlStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 32, 1, 1, 1, 3),
    _ModlParamSwdlStatus_Type()
)
modlParamSwdlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modlParamSwdlStatus.setStatus("current")


class _AgnNearFarConnection_Type(Integer32):
    """Custom type agnNearFarConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disconnected", 2),
          ("connected", 3))
    )


_AgnNearFarConnection_Type.__name__ = "Integer32"
_AgnNearFarConnection_Object = MibScalar
agnNearFarConnection = _AgnNearFarConnection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 33),
    _AgnNearFarConnection_Type()
)
agnNearFarConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnNearFarConnection.setStatus("current")
_RadStkHub_ObjectIdentity = ObjectIdentity
radStkHub = _RadStkHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 7)
)
_RadRouter_ObjectIdentity = ObjectIdentity
radRouter = _RadRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11)
)
_RtrBridge_ObjectIdentity = ObjectIdentity
rtrBridge = _RtrBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 7)
)
_IpRouter_ObjectIdentity = ObjectIdentity
ipRouter = _IpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3)
)
_RtrIfIpTable_Object = MibTable
rtrIfIpTable = _RtrIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 1)
)
if mibBuilder.loadTexts:
    rtrIfIpTable.setStatus("current")
_RtrIfIpEntry_Object = MibTableRow
rtrIfIpEntry = _RtrIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 1, 1)
)
rtrIfIpEntry.setIndexNames(
    (0, "ACE202-MIB", "rtrIfIp"),
)
if mibBuilder.loadTexts:
    rtrIfIpEntry.setStatus("current")
_RtrIfIp_Type = IpAddress
_RtrIfIp_Object = MibTableColumn
rtrIfIp = _RtrIfIp_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 1, 1, 1),
    _RtrIfIp_Type()
)
rtrIfIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfIp.setStatus("current")
_RtrIfRowStatus_Type = RowStatus
_RtrIfRowStatus_Object = MibTableColumn
rtrIfRowStatus = _RtrIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 1, 1, 2),
    _RtrIfRowStatus_Type()
)
rtrIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfRowStatus.setStatus("current")
_RtrIfIpMask_Type = IpAddress
_RtrIfIpMask_Object = MibTableColumn
rtrIfIpMask = _RtrIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 1, 1, 3),
    _RtrIfIpMask_Type()
)
rtrIfIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfIpMask.setStatus("current")
_RtrIfIndex_Type = Integer32
_RtrIfIndex_Object = MibTableColumn
rtrIfIndex = _RtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 1, 1, 4),
    _RtrIfIndex_Type()
)
rtrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfIndex.setStatus("current")


class _RtrIfMng_Type(Integer32):
    """Custom type rtrIfMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RtrIfMng_Type.__name__ = "Integer32"
_RtrIfMng_Object = MibTableColumn
rtrIfMng = _RtrIfMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 1, 1, 5),
    _RtrIfMng_Type()
)
rtrIfMng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfMng.setStatus("current")
_BrtrIfTable_Object = MibTable
brtrIfTable = _BrtrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 2)
)
if mibBuilder.loadTexts:
    brtrIfTable.setStatus("current")
_BrtrIfEntry_Object = MibTableRow
brtrIfEntry = _BrtrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 2, 1)
)
brtrIfEntry.setIndexNames(
    (0, "ACE202-MIB", "brtrIfIndex"),
)
if mibBuilder.loadTexts:
    brtrIfEntry.setStatus("current")
_BrtrIfIndex_Type = Integer32
_BrtrIfIndex_Object = MibTableColumn
brtrIfIndex = _BrtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 2, 1, 1),
    _BrtrIfIndex_Type()
)
brtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brtrIfIndex.setStatus("current")


class _BrtrIfMode_Type(Integer32):
    """Custom type brtrIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("router", 2),
          ("brouter", 3),
          ("off", 4))
    )


_BrtrIfMode_Type.__name__ = "Integer32"
_BrtrIfMode_Object = MibTableColumn
brtrIfMode = _BrtrIfMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 2, 1, 2),
    _BrtrIfMode_Type()
)
brtrIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtrIfMode.setStatus("current")
_BrtrIfMaxFrameSize_Type = Integer32
_BrtrIfMaxFrameSize_Object = MibTableColumn
brtrIfMaxFrameSize = _BrtrIfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 2, 1, 3),
    _BrtrIfMaxFrameSize_Type()
)
brtrIfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtrIfMaxFrameSize.setStatus("current")
_RtrArpAgingTime_Type = Integer32
_RtrArpAgingTime_Object = MibScalar
rtrArpAgingTime = _RtrArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 3),
    _RtrArpAgingTime_Type()
)
rtrArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrArpAgingTime.setStatus("current")
_BrtrLanIfTable_Object = MibTable
brtrLanIfTable = _BrtrLanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4)
)
if mibBuilder.loadTexts:
    brtrLanIfTable.setStatus("current")
_BrtrLanIfEntry_Object = MibTableRow
brtrLanIfEntry = _BrtrLanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1)
)
brtrLanIfEntry.setIndexNames(
    (0, "ACE202-MIB", "brtrLanIfIndex"),
)
if mibBuilder.loadTexts:
    brtrLanIfEntry.setStatus("current")
_BrtrLanIfIndex_Type = Integer32
_BrtrLanIfIndex_Object = MibTableColumn
brtrLanIfIndex = _BrtrLanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1, 1),
    _BrtrLanIfIndex_Type()
)
brtrLanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brtrLanIfIndex.setStatus("current")
_BrtrLanIpAddress_Type = IpAddress
_BrtrLanIpAddress_Object = MibTableColumn
brtrLanIpAddress = _BrtrLanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1, 2),
    _BrtrLanIpAddress_Type()
)
brtrLanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtrLanIpAddress.setStatus("current")
_BrtrLanIpMask_Type = IpAddress
_BrtrLanIpMask_Object = MibTableColumn
brtrLanIpMask = _BrtrLanIpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1, 3),
    _BrtrLanIpMask_Type()
)
brtrLanIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtrLanIpMask.setStatus("current")


class _BrtrLanMaxRateEnable_Type(Integer32):
    """Custom type brtrLanMaxRateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrtrLanMaxRateEnable_Type.__name__ = "Integer32"
_BrtrLanMaxRateEnable_Object = MibTableColumn
brtrLanMaxRateEnable = _BrtrLanMaxRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1, 4),
    _BrtrLanMaxRateEnable_Type()
)
brtrLanMaxRateEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brtrLanMaxRateEnable.setStatus("current")
_BrtrLanMaxRate_Type = Integer32
_BrtrLanMaxRate_Object = MibTableColumn
brtrLanMaxRate = _BrtrLanMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1, 5),
    _BrtrLanMaxRate_Type()
)
brtrLanMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtrLanMaxRate.setStatus("current")


class _BrtrLanMng_Type(Integer32):
    """Custom type brtrLanMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrtrLanMng_Type.__name__ = "Integer32"
_BrtrLanMng_Object = MibTableColumn
brtrLanMng = _BrtrLanMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1, 6),
    _BrtrLanMng_Type()
)
brtrLanMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtrLanMng.setStatus("current")
_BrtrLanDefaultRouter_Type = IpAddress
_BrtrLanDefaultRouter_Object = MibTableColumn
brtrLanDefaultRouter = _BrtrLanDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 4, 1, 7),
    _BrtrLanDefaultRouter_Type()
)
brtrLanDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtrLanDefaultRouter.setStatus("current")
_RtrIsdnIfTable_Object = MibTable
rtrIsdnIfTable = _RtrIsdnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 5)
)
if mibBuilder.loadTexts:
    rtrIsdnIfTable.setStatus("current")
_RtrIsdnIfEntry_Object = MibTableRow
rtrIsdnIfEntry = _RtrIsdnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 5, 1)
)
if mibBuilder.loadTexts:
    rtrIsdnIfEntry.setStatus("current")
_RtrIsdnIfMinNumBchans_Type = Integer32
_RtrIsdnIfMinNumBchans_Object = MibTableColumn
rtrIsdnIfMinNumBchans = _RtrIsdnIfMinNumBchans_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 5, 1, 1),
    _RtrIsdnIfMinNumBchans_Type()
)
rtrIsdnIfMinNumBchans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIsdnIfMinNumBchans.setStatus("current")
_RtrIsdnIfMaxNumBchans_Type = Integer32
_RtrIsdnIfMaxNumBchans_Object = MibTableColumn
rtrIsdnIfMaxNumBchans = _RtrIsdnIfMaxNumBchans_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 5, 1, 2),
    _RtrIsdnIfMaxNumBchans_Type()
)
rtrIsdnIfMaxNumBchans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIsdnIfMaxNumBchans.setStatus("current")
_RtrLcrTable_Object = MibTable
rtrLcrTable = _RtrLcrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 6)
)
if mibBuilder.loadTexts:
    rtrLcrTable.setStatus("current")
_RtrLcrEntry_Object = MibTableRow
rtrLcrEntry = _RtrLcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 6, 1)
)
rtrLcrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "rtrLcrOutIfIndex"),
)
if mibBuilder.loadTexts:
    rtrLcrEntry.setStatus("current")
_RtrLcrOutIfIndex_Type = InterfaceIndex
_RtrLcrOutIfIndex_Object = MibTableColumn
rtrLcrOutIfIndex = _RtrLcrOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 6, 1, 1),
    _RtrLcrOutIfIndex_Type()
)
rtrLcrOutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrLcrOutIfIndex.setStatus("current")
_RtrLcrRowStatus_Type = RowStatus
_RtrLcrRowStatus_Object = MibTableColumn
rtrLcrRowStatus = _RtrLcrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 6, 1, 2),
    _RtrLcrRowStatus_Type()
)
rtrLcrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrLcrRowStatus.setStatus("current")
_RtrLcrInPrefix_Type = DisplayString
_RtrLcrInPrefix_Object = MibTableColumn
rtrLcrInPrefix = _RtrLcrInPrefix_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 6, 1, 3),
    _RtrLcrInPrefix_Type()
)
rtrLcrInPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrLcrInPrefix.setStatus("current")
_RtrLcrOutPrefix_Type = DisplayString
_RtrLcrOutPrefix_Object = MibTableColumn
rtrLcrOutPrefix = _RtrLcrOutPrefix_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 3, 6, 1, 4),
    _RtrLcrOutPrefix_Type()
)
rtrLcrOutPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrLcrOutPrefix.setStatus("current")
_MulticastGen_ObjectIdentity = ObjectIdentity
multicastGen = _MulticastGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 8)
)


class _MulticastMode_Type(Integer32):
    """Custom type multicastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("wanToLan", 3),
          ("wanToLanIgmp", 4),
          ("lanToWan", 5),
          ("bidirectional", 6),
          ("transparent", 7))
    )


_MulticastMode_Type.__name__ = "Integer32"
_MulticastMode_Object = MibScalar
multicastMode = _MulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 8, 1),
    _MulticastMode_Type()
)
multicastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastMode.setStatus("current")
_RadAtm_ObjectIdentity = ObjectIdentity
radAtm = _RadAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12)
)
_AtmGen_ObjectIdentity = ObjectIdentity
atmGen = _AtmGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2)
)
_AtmPerfHistory_ObjectIdentity = ObjectIdentity
atmPerfHistory = _AtmPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1)
)
_AtmIfPerformance_ObjectIdentity = ObjectIdentity
atmIfPerformance = _AtmIfPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1)
)
_AtmIfDataTable_Object = MibTable
atmIfDataTable = _AtmIfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmIfDataTable.setStatus("current")
_AtmIfDataEntry_Object = MibTableRow
atmIfDataEntry = _AtmIfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 1, 1)
)
atmIfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmIfDataEntry.setStatus("current")


class _AtmIfTimeElapsed_Type(Integer32):
    """Custom type atmIfTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AtmIfTimeElapsed_Type.__name__ = "Integer32"
_AtmIfTimeElapsed_Object = MibTableColumn
atmIfTimeElapsed = _AtmIfTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 1, 1, 1),
    _AtmIfTimeElapsed_Type()
)
atmIfTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfTimeElapsed.setStatus("current")


class _AtmIfValidIntervals_Type(Integer32):
    """Custom type atmIfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AtmIfValidIntervals_Type.__name__ = "Integer32"
_AtmIfValidIntervals_Object = MibTableColumn
atmIfValidIntervals = _AtmIfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 1, 1, 2),
    _AtmIfValidIntervals_Type()
)
atmIfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfValidIntervals.setStatus("current")
_AtmIfCurrentTable_Object = MibTable
atmIfCurrentTable = _AtmIfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmIfCurrentTable.setStatus("current")
_AtmIfCurrentEntry_Object = MibTableRow
atmIfCurrentEntry = _AtmIfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 2, 1)
)
atmIfCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmIfCurrentEntry.setStatus("current")
_AtmIfCurrentTxCells_Type = Gauge32
_AtmIfCurrentTxCells_Object = MibTableColumn
atmIfCurrentTxCells = _AtmIfCurrentTxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 2, 1, 1),
    _AtmIfCurrentTxCells_Type()
)
atmIfCurrentTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfCurrentTxCells.setStatus("current")
_AtmIfCurrentRxCells_Type = Gauge32
_AtmIfCurrentRxCells_Object = MibTableColumn
atmIfCurrentRxCells = _AtmIfCurrentRxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 2, 1, 2),
    _AtmIfCurrentRxCells_Type()
)
atmIfCurrentRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfCurrentRxCells.setStatus("current")
_AtmIfCurrentCorrectedHecs_Type = Gauge32
_AtmIfCurrentCorrectedHecs_Object = MibTableColumn
atmIfCurrentCorrectedHecs = _AtmIfCurrentCorrectedHecs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 2, 1, 3),
    _AtmIfCurrentCorrectedHecs_Type()
)
atmIfCurrentCorrectedHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfCurrentCorrectedHecs.setStatus("current")
_AtmIfCurrentUncorrectedHecs_Type = Gauge32
_AtmIfCurrentUncorrectedHecs_Object = MibTableColumn
atmIfCurrentUncorrectedHecs = _AtmIfCurrentUncorrectedHecs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 2, 1, 4),
    _AtmIfCurrentUncorrectedHecs_Type()
)
atmIfCurrentUncorrectedHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfCurrentUncorrectedHecs.setStatus("current")
_AtmIfIntervalTable_Object = MibTable
atmIfIntervalTable = _AtmIfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmIfIntervalTable.setStatus("current")
_AtmIfIntervalEntry_Object = MibTableRow
atmIfIntervalEntry = _AtmIfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 3, 1)
)
atmIfIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmIfIntervalNumber"),
)
if mibBuilder.loadTexts:
    atmIfIntervalEntry.setStatus("current")


class _AtmIfIntervalNumber_Type(Integer32):
    """Custom type atmIfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmIfIntervalNumber_Type.__name__ = "Integer32"
_AtmIfIntervalNumber_Object = MibTableColumn
atmIfIntervalNumber = _AtmIfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 3, 1, 1),
    _AtmIfIntervalNumber_Type()
)
atmIfIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIntervalNumber.setStatus("current")
_AtmIfIntervalTxCells_Type = Gauge32
_AtmIfIntervalTxCells_Object = MibTableColumn
atmIfIntervalTxCells = _AtmIfIntervalTxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 3, 1, 2),
    _AtmIfIntervalTxCells_Type()
)
atmIfIntervalTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIntervalTxCells.setStatus("current")
_AtmIfIntervalRxCells_Type = Gauge32
_AtmIfIntervalRxCells_Object = MibTableColumn
atmIfIntervalRxCells = _AtmIfIntervalRxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 3, 1, 3),
    _AtmIfIntervalRxCells_Type()
)
atmIfIntervalRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIntervalRxCells.setStatus("current")
_AtmIfIntervalCorrectedHecs_Type = Gauge32
_AtmIfIntervalCorrectedHecs_Object = MibTableColumn
atmIfIntervalCorrectedHecs = _AtmIfIntervalCorrectedHecs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 3, 1, 4),
    _AtmIfIntervalCorrectedHecs_Type()
)
atmIfIntervalCorrectedHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIntervalCorrectedHecs.setStatus("current")
_AtmIfIntervalUncorrectedHecs_Type = Gauge32
_AtmIfIntervalUncorrectedHecs_Object = MibTableColumn
atmIfIntervalUncorrectedHecs = _AtmIfIntervalUncorrectedHecs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 3, 1, 5),
    _AtmIfIntervalUncorrectedHecs_Type()
)
atmIfIntervalUncorrectedHecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIntervalUncorrectedHecs.setStatus("current")
_Aal5VccXTable_Object = MibTable
aal5VccXTable = _Aal5VccXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    aal5VccXTable.setStatus("current")
_Aal5VccXEntry_Object = MibTableRow
aal5VccXEntry = _Aal5VccXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aal5VccXEntry.setStatus("current")
_Aal5VccInFrames_Type = Counter32
_Aal5VccInFrames_Object = MibTableColumn
aal5VccInFrames = _Aal5VccInFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 4, 1, 1),
    _Aal5VccInFrames_Type()
)
aal5VccInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccInFrames.setStatus("current")
_Aal5VccOutFrames_Type = Counter32
_Aal5VccOutFrames_Object = MibTableColumn
aal5VccOutFrames = _Aal5VccOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 4, 1, 2),
    _Aal5VccOutFrames_Type()
)
aal5VccOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccOutFrames.setStatus("current")
_Aal5VccUnknownProtocolFrames_Type = Counter32
_Aal5VccUnknownProtocolFrames_Object = MibTableColumn
aal5VccUnknownProtocolFrames = _Aal5VccUnknownProtocolFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 1, 4, 1, 3),
    _Aal5VccUnknownProtocolFrames_Type()
)
aal5VccUnknownProtocolFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccUnknownProtocolFrames.setStatus("current")
_AtmPvcPerformance_ObjectIdentity = ObjectIdentity
atmPvcPerformance = _AtmPvcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2)
)
_AtmVpPerformance_ObjectIdentity = ObjectIdentity
atmVpPerformance = _AtmVpPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1)
)
_AtmVpCurrentTable_Object = MibTable
atmVpCurrentTable = _AtmVpCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmVpCurrentTable.setStatus("current")
_AtmVpCurrentEntry_Object = MibTableRow
atmVpCurrentEntry = _AtmVpCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1)
)
atmVpCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVpCurrentVpi"),
)
if mibBuilder.loadTexts:
    atmVpCurrentEntry.setStatus("current")
_AtmVpCurrentVpi_Type = Integer32
_AtmVpCurrentVpi_Object = MibTableColumn
atmVpCurrentVpi = _AtmVpCurrentVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 1),
    _AtmVpCurrentVpi_Type()
)
atmVpCurrentVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentVpi.setStatus("current")
_AtmVpCurrentRxCellsClp01_Type = Gauge32
_AtmVpCurrentRxCellsClp01_Object = MibTableColumn
atmVpCurrentRxCellsClp01 = _AtmVpCurrentRxCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 2),
    _AtmVpCurrentRxCellsClp01_Type()
)
atmVpCurrentRxCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentRxCellsClp01.setStatus("current")
_AtmVpCurrentRxCellsClp0_Type = Gauge32
_AtmVpCurrentRxCellsClp0_Object = MibTableColumn
atmVpCurrentRxCellsClp0 = _AtmVpCurrentRxCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 3),
    _AtmVpCurrentRxCellsClp0_Type()
)
atmVpCurrentRxCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentRxCellsClp0.setStatus("current")
_AtmVpCurrentGcra0Violations_Type = Gauge32
_AtmVpCurrentGcra0Violations_Object = MibTableColumn
atmVpCurrentGcra0Violations = _AtmVpCurrentGcra0Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 4),
    _AtmVpCurrentGcra0Violations_Type()
)
atmVpCurrentGcra0Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentGcra0Violations.setStatus("current")
_AtmVpCurrentGcra1Violations_Type = Gauge32
_AtmVpCurrentGcra1Violations_Object = MibTableColumn
atmVpCurrentGcra1Violations = _AtmVpCurrentGcra1Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 5),
    _AtmVpCurrentGcra1Violations_Type()
)
atmVpCurrentGcra1Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentGcra1Violations.setStatus("current")
_AtmVpCurrentRxAIS_Type = Gauge32
_AtmVpCurrentRxAIS_Object = MibTableColumn
atmVpCurrentRxAIS = _AtmVpCurrentRxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 6),
    _AtmVpCurrentRxAIS_Type()
)
atmVpCurrentRxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentRxAIS.setStatus("current")
_AtmVpCurrentTxAIS_Type = Gauge32
_AtmVpCurrentTxAIS_Object = MibTableColumn
atmVpCurrentTxAIS = _AtmVpCurrentTxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 7),
    _AtmVpCurrentTxAIS_Type()
)
atmVpCurrentTxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentTxAIS.setStatus("current")
_AtmVpCurrentRxRDI_Type = Gauge32
_AtmVpCurrentRxRDI_Object = MibTableColumn
atmVpCurrentRxRDI = _AtmVpCurrentRxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 8),
    _AtmVpCurrentRxRDI_Type()
)
atmVpCurrentRxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentRxRDI.setStatus("current")
_AtmVpCurrentTxRDI_Type = Gauge32
_AtmVpCurrentTxRDI_Object = MibTableColumn
atmVpCurrentTxRDI = _AtmVpCurrentTxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 9),
    _AtmVpCurrentTxRDI_Type()
)
atmVpCurrentTxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentTxRDI.setStatus("current")
_AtmVpCurrentContinuityLoss_Type = Gauge32
_AtmVpCurrentContinuityLoss_Object = MibTableColumn
atmVpCurrentContinuityLoss = _AtmVpCurrentContinuityLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 10),
    _AtmVpCurrentContinuityLoss_Type()
)
atmVpCurrentContinuityLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentContinuityLoss.setStatus("current")
_AtmVpCurrentUAS_Type = Gauge32
_AtmVpCurrentUAS_Object = MibTableColumn
atmVpCurrentUAS = _AtmVpCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 11),
    _AtmVpCurrentUAS_Type()
)
atmVpCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentUAS.setStatus("current")
_AtmVpCurrentSES_Type = Gauge32
_AtmVpCurrentSES_Object = MibTableColumn
atmVpCurrentSES = _AtmVpCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 12),
    _AtmVpCurrentSES_Type()
)
atmVpCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentSES.setStatus("current")
_AtmVpCurrentCDC_Type = Gauge32
_AtmVpCurrentCDC_Object = MibTableColumn
atmVpCurrentCDC = _AtmVpCurrentCDC_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 13),
    _AtmVpCurrentCDC_Type()
)
atmVpCurrentCDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentCDC.setStatus("current")
_AtmVpCurrentTotalDiscards_Type = Gauge32
_AtmVpCurrentTotalDiscards_Object = MibTableColumn
atmVpCurrentTotalDiscards = _AtmVpCurrentTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 14),
    _AtmVpCurrentTotalDiscards_Type()
)
atmVpCurrentTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentTotalDiscards.setStatus("current")
_AtmVpCurrentClp0Discards_Type = Gauge32
_AtmVpCurrentClp0Discards_Object = MibTableColumn
atmVpCurrentClp0Discards = _AtmVpCurrentClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 15),
    _AtmVpCurrentClp0Discards_Type()
)
atmVpCurrentClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentClp0Discards.setStatus("current")
_AtmVpCurrentTotalCellOuts_Type = Gauge32
_AtmVpCurrentTotalCellOuts_Object = MibTableColumn
atmVpCurrentTotalCellOuts = _AtmVpCurrentTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 16),
    _AtmVpCurrentTotalCellOuts_Type()
)
atmVpCurrentTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentTotalCellOuts.setStatus("current")
_AtmVpCurrentClp0CellOuts_Type = Gauge32
_AtmVpCurrentClp0CellOuts_Object = MibTableColumn
atmVpCurrentClp0CellOuts = _AtmVpCurrentClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 17),
    _AtmVpCurrentClp0CellOuts_Type()
)
atmVpCurrentClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentClp0CellOuts.setStatus("current")
_AtmVpCurrentTaggedOuts_Type = Gauge32
_AtmVpCurrentTaggedOuts_Object = MibTableColumn
atmVpCurrentTaggedOuts = _AtmVpCurrentTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 18),
    _AtmVpCurrentTaggedOuts_Type()
)
atmVpCurrentTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentTaggedOuts.setStatus("current")
_AtmVpCurrentPCR_Type = Gauge32
_AtmVpCurrentPCR_Object = MibTableColumn
atmVpCurrentPCR = _AtmVpCurrentPCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 19),
    _AtmVpCurrentPCR_Type()
)
atmVpCurrentPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentPCR.setStatus("current")
_AtmVpCurrentSCR_Type = Gauge32
_AtmVpCurrentSCR_Object = MibTableColumn
atmVpCurrentSCR = _AtmVpCurrentSCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 20),
    _AtmVpCurrentSCR_Type()
)
atmVpCurrentSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentSCR.setStatus("current")
_AtmVpCurrentMCR_Type = Gauge32
_AtmVpCurrentMCR_Object = MibTableColumn
atmVpCurrentMCR = _AtmVpCurrentMCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 1, 1, 21),
    _AtmVpCurrentMCR_Type()
)
atmVpCurrentMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCurrentMCR.setStatus("current")
_AtmVpPMCurrentTable_Object = MibTable
atmVpPMCurrentTable = _AtmVpPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    atmVpPMCurrentTable.setStatus("current")
_AtmVpPMCurrentEntry_Object = MibTableRow
atmVpPMCurrentEntry = _AtmVpPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1)
)
atmVpPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVpPMCurrentVpi"),
    (0, "ACE202-MIB", "atmVpPMCurrentDir"),
)
if mibBuilder.loadTexts:
    atmVpPMCurrentEntry.setStatus("current")
_AtmVpPMCurrentVpi_Type = Integer32
_AtmVpPMCurrentVpi_Object = MibTableColumn
atmVpPMCurrentVpi = _AtmVpPMCurrentVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 1),
    _AtmVpPMCurrentVpi_Type()
)
atmVpPMCurrentVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentVpi.setStatus("current")


class _AtmVpPMCurrentDir_Type(Integer32):
    """Custom type atmVpPMCurrentDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 2),
          ("backward", 3))
    )


_AtmVpPMCurrentDir_Type.__name__ = "Integer32"
_AtmVpPMCurrentDir_Object = MibTableColumn
atmVpPMCurrentDir = _AtmVpPMCurrentDir_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 2),
    _AtmVpPMCurrentDir_Type()
)
atmVpPMCurrentDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentDir.setStatus("current")
_AtmVpPMCurrentTxClp01_Type = Gauge32
_AtmVpPMCurrentTxClp01_Object = MibTableColumn
atmVpPMCurrentTxClp01 = _AtmVpPMCurrentTxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 3),
    _AtmVpPMCurrentTxClp01_Type()
)
atmVpPMCurrentTxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentTxClp01.setStatus("current")
_AtmVpPMCurrentTxClp0_Type = Gauge32
_AtmVpPMCurrentTxClp0_Object = MibTableColumn
atmVpPMCurrentTxClp0 = _AtmVpPMCurrentTxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 4),
    _AtmVpPMCurrentTxClp0_Type()
)
atmVpPMCurrentTxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentTxClp0.setStatus("current")
_AtmVpPMCurrentRxClp01_Type = Gauge32
_AtmVpPMCurrentRxClp01_Object = MibTableColumn
atmVpPMCurrentRxClp01 = _AtmVpPMCurrentRxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 5),
    _AtmVpPMCurrentRxClp01_Type()
)
atmVpPMCurrentRxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentRxClp01.setStatus("current")
_AtmVpPMCurrentRxClp0_Type = Gauge32
_AtmVpPMCurrentRxClp0_Object = MibTableColumn
atmVpPMCurrentRxClp0 = _AtmVpPMCurrentRxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 6),
    _AtmVpPMCurrentRxClp0_Type()
)
atmVpPMCurrentRxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentRxClp0.setStatus("current")
_AtmVpPMCurrentErroredCells_Type = Gauge32
_AtmVpPMCurrentErroredCells_Object = MibTableColumn
atmVpPMCurrentErroredCells = _AtmVpPMCurrentErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 7),
    _AtmVpPMCurrentErroredCells_Type()
)
atmVpPMCurrentErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentErroredCells.setStatus("current")
_AtmVpPMCurrentLostCells_Type = Gauge32
_AtmVpPMCurrentLostCells_Object = MibTableColumn
atmVpPMCurrentLostCells = _AtmVpPMCurrentLostCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 8),
    _AtmVpPMCurrentLostCells_Type()
)
atmVpPMCurrentLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentLostCells.setStatus("current")
_AtmVpPMCurrentMisinsertedCells_Type = Gauge32
_AtmVpPMCurrentMisinsertedCells_Object = MibTableColumn
atmVpPMCurrentMisinsertedCells = _AtmVpPMCurrentMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 9),
    _AtmVpPMCurrentMisinsertedCells_Type()
)
atmVpPMCurrentMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentMisinsertedCells.setStatus("current")
_AtmVpPMCurrentECB_Type = Gauge32
_AtmVpPMCurrentECB_Object = MibTableColumn
atmVpPMCurrentECB = _AtmVpPMCurrentECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 10),
    _AtmVpPMCurrentECB_Type()
)
atmVpPMCurrentECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentECB.setStatus("current")
_AtmVpPMCurrentSECB_Type = Gauge32
_AtmVpPMCurrentSECB_Object = MibTableColumn
atmVpPMCurrentSECB = _AtmVpPMCurrentSECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 11),
    _AtmVpPMCurrentSECB_Type()
)
atmVpPMCurrentSECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentSECB.setStatus("current")
_AtmVpPMCurrentES_Type = Gauge32
_AtmVpPMCurrentES_Object = MibTableColumn
atmVpPMCurrentES = _AtmVpPMCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 12),
    _AtmVpPMCurrentES_Type()
)
atmVpPMCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentES.setStatus("current")
_AtmVpPMCurrentSES_Type = Gauge32
_AtmVpPMCurrentSES_Object = MibTableColumn
atmVpPMCurrentSES = _AtmVpPMCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 13),
    _AtmVpPMCurrentSES_Type()
)
atmVpPMCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentSES.setStatus("current")
_AtmVpPMCurrentUAS_Type = Gauge32
_AtmVpPMCurrentUAS_Object = MibTableColumn
atmVpPMCurrentUAS = _AtmVpPMCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 14),
    _AtmVpPMCurrentUAS_Type()
)
atmVpPMCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentUAS.setStatus("current")


class _AtmVpPMCurrentIntervalQuality_Type(Integer32):
    """Custom type atmVpPMCurrentIntervalQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("unacceptable", 3))
    )


_AtmVpPMCurrentIntervalQuality_Type.__name__ = "Integer32"
_AtmVpPMCurrentIntervalQuality_Object = MibTableColumn
atmVpPMCurrentIntervalQuality = _AtmVpPMCurrentIntervalQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 15),
    _AtmVpPMCurrentIntervalQuality_Type()
)
atmVpPMCurrentIntervalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentIntervalQuality.setStatus("current")


class _AtmVpPMCurrentLastDayQuality_Type(Integer32):
    """Custom type atmVpPMCurrentLastDayQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("degraded", 4))
    )


_AtmVpPMCurrentLastDayQuality_Type.__name__ = "Integer32"
_AtmVpPMCurrentLastDayQuality_Object = MibTableColumn
atmVpPMCurrentLastDayQuality = _AtmVpPMCurrentLastDayQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 2, 1, 16),
    _AtmVpPMCurrentLastDayQuality_Type()
)
atmVpPMCurrentLastDayQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMCurrentLastDayQuality.setStatus("current")
_AtmVpIntervalTable_Object = MibTable
atmVpIntervalTable = _AtmVpIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmVpIntervalTable.setStatus("current")
_AtmVpIntervalEntry_Object = MibTableRow
atmVpIntervalEntry = _AtmVpIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1)
)
atmVpIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVpIntervalVpi"),
    (0, "ACE202-MIB", "atmVpIntervalNumber"),
)
if mibBuilder.loadTexts:
    atmVpIntervalEntry.setStatus("current")
_AtmVpIntervalVpi_Type = Integer32
_AtmVpIntervalVpi_Object = MibTableColumn
atmVpIntervalVpi = _AtmVpIntervalVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 1),
    _AtmVpIntervalVpi_Type()
)
atmVpIntervalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalVpi.setStatus("current")


class _AtmVpIntervalNumber_Type(Integer32):
    """Custom type atmVpIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmVpIntervalNumber_Type.__name__ = "Integer32"
_AtmVpIntervalNumber_Object = MibTableColumn
atmVpIntervalNumber = _AtmVpIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 2),
    _AtmVpIntervalNumber_Type()
)
atmVpIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalNumber.setStatus("current")
_AtmVpIntervalRxCellsClp01_Type = Gauge32
_AtmVpIntervalRxCellsClp01_Object = MibTableColumn
atmVpIntervalRxCellsClp01 = _AtmVpIntervalRxCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 3),
    _AtmVpIntervalRxCellsClp01_Type()
)
atmVpIntervalRxCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalRxCellsClp01.setStatus("current")
_AtmVpIntervalRxCellsClp0_Type = Gauge32
_AtmVpIntervalRxCellsClp0_Object = MibTableColumn
atmVpIntervalRxCellsClp0 = _AtmVpIntervalRxCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 4),
    _AtmVpIntervalRxCellsClp0_Type()
)
atmVpIntervalRxCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalRxCellsClp0.setStatus("current")
_AtmVpIntervalGcra0Violations_Type = Gauge32
_AtmVpIntervalGcra0Violations_Object = MibTableColumn
atmVpIntervalGcra0Violations = _AtmVpIntervalGcra0Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 5),
    _AtmVpIntervalGcra0Violations_Type()
)
atmVpIntervalGcra0Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalGcra0Violations.setStatus("current")
_AtmVpIntervalGcra1Violations_Type = Gauge32
_AtmVpIntervalGcra1Violations_Object = MibTableColumn
atmVpIntervalGcra1Violations = _AtmVpIntervalGcra1Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 6),
    _AtmVpIntervalGcra1Violations_Type()
)
atmVpIntervalGcra1Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalGcra1Violations.setStatus("current")
_AtmVpIntervalRxAIS_Type = Gauge32
_AtmVpIntervalRxAIS_Object = MibTableColumn
atmVpIntervalRxAIS = _AtmVpIntervalRxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 7),
    _AtmVpIntervalRxAIS_Type()
)
atmVpIntervalRxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalRxAIS.setStatus("current")
_AtmVpIntervalTxAIS_Type = Gauge32
_AtmVpIntervalTxAIS_Object = MibTableColumn
atmVpIntervalTxAIS = _AtmVpIntervalTxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 8),
    _AtmVpIntervalTxAIS_Type()
)
atmVpIntervalTxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalTxAIS.setStatus("current")
_AtmVpIntervalRxRDI_Type = Gauge32
_AtmVpIntervalRxRDI_Object = MibTableColumn
atmVpIntervalRxRDI = _AtmVpIntervalRxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 9),
    _AtmVpIntervalRxRDI_Type()
)
atmVpIntervalRxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalRxRDI.setStatus("current")
_AtmVpIntervalTxRDI_Type = Gauge32
_AtmVpIntervalTxRDI_Object = MibTableColumn
atmVpIntervalTxRDI = _AtmVpIntervalTxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 10),
    _AtmVpIntervalTxRDI_Type()
)
atmVpIntervalTxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalTxRDI.setStatus("current")
_AtmVpIntervalContinuityLoss_Type = Gauge32
_AtmVpIntervalContinuityLoss_Object = MibTableColumn
atmVpIntervalContinuityLoss = _AtmVpIntervalContinuityLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 11),
    _AtmVpIntervalContinuityLoss_Type()
)
atmVpIntervalContinuityLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalContinuityLoss.setStatus("current")
_AtmVpIntervalUAS_Type = Gauge32
_AtmVpIntervalUAS_Object = MibTableColumn
atmVpIntervalUAS = _AtmVpIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 12),
    _AtmVpIntervalUAS_Type()
)
atmVpIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalUAS.setStatus("current")
_AtmVpIntervalSES_Type = Gauge32
_AtmVpIntervalSES_Object = MibTableColumn
atmVpIntervalSES = _AtmVpIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 13),
    _AtmVpIntervalSES_Type()
)
atmVpIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalSES.setStatus("current")
_AtmVpIntervalCDC_Type = Gauge32
_AtmVpIntervalCDC_Object = MibTableColumn
atmVpIntervalCDC = _AtmVpIntervalCDC_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 14),
    _AtmVpIntervalCDC_Type()
)
atmVpIntervalCDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalCDC.setStatus("current")
_AtmVpIntervalTotalDiscards_Type = Gauge32
_AtmVpIntervalTotalDiscards_Object = MibTableColumn
atmVpIntervalTotalDiscards = _AtmVpIntervalTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 15),
    _AtmVpIntervalTotalDiscards_Type()
)
atmVpIntervalTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalTotalDiscards.setStatus("current")
_AtmVpIntervalClp0Discards_Type = Gauge32
_AtmVpIntervalClp0Discards_Object = MibTableColumn
atmVpIntervalClp0Discards = _AtmVpIntervalClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 16),
    _AtmVpIntervalClp0Discards_Type()
)
atmVpIntervalClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalClp0Discards.setStatus("current")
_AtmVpIntervalTotalCellOuts_Type = Gauge32
_AtmVpIntervalTotalCellOuts_Object = MibTableColumn
atmVpIntervalTotalCellOuts = _AtmVpIntervalTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 17),
    _AtmVpIntervalTotalCellOuts_Type()
)
atmVpIntervalTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalTotalCellOuts.setStatus("current")
_AtmVpIntervalClp0CellOuts_Type = Gauge32
_AtmVpIntervalClp0CellOuts_Object = MibTableColumn
atmVpIntervalClp0CellOuts = _AtmVpIntervalClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 18),
    _AtmVpIntervalClp0CellOuts_Type()
)
atmVpIntervalClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalClp0CellOuts.setStatus("current")
_AtmVpIntervalTaggedOuts_Type = Gauge32
_AtmVpIntervalTaggedOuts_Object = MibTableColumn
atmVpIntervalTaggedOuts = _AtmVpIntervalTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 19),
    _AtmVpIntervalTaggedOuts_Type()
)
atmVpIntervalTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalTaggedOuts.setStatus("current")
_AtmVpIntervalPCR_Type = Gauge32
_AtmVpIntervalPCR_Object = MibTableColumn
atmVpIntervalPCR = _AtmVpIntervalPCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 20),
    _AtmVpIntervalPCR_Type()
)
atmVpIntervalPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalPCR.setStatus("current")
_AtmVpIntervalSCR_Type = Gauge32
_AtmVpIntervalSCR_Object = MibTableColumn
atmVpIntervalSCR = _AtmVpIntervalSCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 21),
    _AtmVpIntervalSCR_Type()
)
atmVpIntervalSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalSCR.setStatus("current")
_AtmVpIntervalMCR_Type = Gauge32
_AtmVpIntervalMCR_Object = MibTableColumn
atmVpIntervalMCR = _AtmVpIntervalMCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 3, 1, 22),
    _AtmVpIntervalMCR_Type()
)
atmVpIntervalMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpIntervalMCR.setStatus("current")
_AtmVpPMIntervalTable_Object = MibTable
atmVpPMIntervalTable = _AtmVpPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    atmVpPMIntervalTable.setStatus("current")
_AtmVpPMIntervalEntry_Object = MibTableRow
atmVpPMIntervalEntry = _AtmVpPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1)
)
atmVpPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVpPMIntervalVpi"),
    (0, "ACE202-MIB", "atmVpPMIntervalDir"),
    (0, "ACE202-MIB", "atmVpPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    atmVpPMIntervalEntry.setStatus("current")
_AtmVpPMIntervalVpi_Type = Integer32
_AtmVpPMIntervalVpi_Object = MibTableColumn
atmVpPMIntervalVpi = _AtmVpPMIntervalVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 1),
    _AtmVpPMIntervalVpi_Type()
)
atmVpPMIntervalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalVpi.setStatus("current")


class _AtmVpPMIntervalDir_Type(Integer32):
    """Custom type atmVpPMIntervalDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 2),
          ("backward", 3))
    )


_AtmVpPMIntervalDir_Type.__name__ = "Integer32"
_AtmVpPMIntervalDir_Object = MibTableColumn
atmVpPMIntervalDir = _AtmVpPMIntervalDir_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 2),
    _AtmVpPMIntervalDir_Type()
)
atmVpPMIntervalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalDir.setStatus("current")


class _AtmVpPMIntervalNumber_Type(Integer32):
    """Custom type atmVpPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmVpPMIntervalNumber_Type.__name__ = "Integer32"
_AtmVpPMIntervalNumber_Object = MibTableColumn
atmVpPMIntervalNumber = _AtmVpPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 3),
    _AtmVpPMIntervalNumber_Type()
)
atmVpPMIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalNumber.setStatus("current")
_AtmVpPMIntervalTxClp01_Type = Gauge32
_AtmVpPMIntervalTxClp01_Object = MibTableColumn
atmVpPMIntervalTxClp01 = _AtmVpPMIntervalTxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 4),
    _AtmVpPMIntervalTxClp01_Type()
)
atmVpPMIntervalTxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalTxClp01.setStatus("current")
_AtmVpPMIntervalTxClp0_Type = Gauge32
_AtmVpPMIntervalTxClp0_Object = MibTableColumn
atmVpPMIntervalTxClp0 = _AtmVpPMIntervalTxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 5),
    _AtmVpPMIntervalTxClp0_Type()
)
atmVpPMIntervalTxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalTxClp0.setStatus("current")
_AtmVpPMIntervalRxClp01_Type = Gauge32
_AtmVpPMIntervalRxClp01_Object = MibTableColumn
atmVpPMIntervalRxClp01 = _AtmVpPMIntervalRxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 6),
    _AtmVpPMIntervalRxClp01_Type()
)
atmVpPMIntervalRxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalRxClp01.setStatus("current")
_AtmVpPMIntervalRxClp0_Type = Gauge32
_AtmVpPMIntervalRxClp0_Object = MibTableColumn
atmVpPMIntervalRxClp0 = _AtmVpPMIntervalRxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 7),
    _AtmVpPMIntervalRxClp0_Type()
)
atmVpPMIntervalRxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalRxClp0.setStatus("current")
_AtmVpPMIntervalErroredCells_Type = Gauge32
_AtmVpPMIntervalErroredCells_Object = MibTableColumn
atmVpPMIntervalErroredCells = _AtmVpPMIntervalErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 8),
    _AtmVpPMIntervalErroredCells_Type()
)
atmVpPMIntervalErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalErroredCells.setStatus("current")
_AtmVpPMIntervalLostCells_Type = Gauge32
_AtmVpPMIntervalLostCells_Object = MibTableColumn
atmVpPMIntervalLostCells = _AtmVpPMIntervalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 9),
    _AtmVpPMIntervalLostCells_Type()
)
atmVpPMIntervalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalLostCells.setStatus("current")
_AtmVpPMIntervalMisinsertedCells_Type = Gauge32
_AtmVpPMIntervalMisinsertedCells_Object = MibTableColumn
atmVpPMIntervalMisinsertedCells = _AtmVpPMIntervalMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 10),
    _AtmVpPMIntervalMisinsertedCells_Type()
)
atmVpPMIntervalMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalMisinsertedCells.setStatus("current")
_AtmVpPMIntervalECB_Type = Gauge32
_AtmVpPMIntervalECB_Object = MibTableColumn
atmVpPMIntervalECB = _AtmVpPMIntervalECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 11),
    _AtmVpPMIntervalECB_Type()
)
atmVpPMIntervalECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalECB.setStatus("current")
_AtmVpPMIntervalSECB_Type = Gauge32
_AtmVpPMIntervalSECB_Object = MibTableColumn
atmVpPMIntervalSECB = _AtmVpPMIntervalSECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 12),
    _AtmVpPMIntervalSECB_Type()
)
atmVpPMIntervalSECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalSECB.setStatus("current")
_AtmVpPMIntervalES_Type = Gauge32
_AtmVpPMIntervalES_Object = MibTableColumn
atmVpPMIntervalES = _AtmVpPMIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 13),
    _AtmVpPMIntervalES_Type()
)
atmVpPMIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalES.setStatus("current")
_AtmVpPMIntervalSES_Type = Gauge32
_AtmVpPMIntervalSES_Object = MibTableColumn
atmVpPMIntervalSES = _AtmVpPMIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 14),
    _AtmVpPMIntervalSES_Type()
)
atmVpPMIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalSES.setStatus("current")
_AtmVpPMIntervalUAS_Type = Gauge32
_AtmVpPMIntervalUAS_Object = MibTableColumn
atmVpPMIntervalUAS = _AtmVpPMIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 15),
    _AtmVpPMIntervalUAS_Type()
)
atmVpPMIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalUAS.setStatus("current")


class _AtmVpPMIntervalQuality_Type(Integer32):
    """Custom type atmVpPMIntervalQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("unacceptable", 3))
    )


_AtmVpPMIntervalQuality_Type.__name__ = "Integer32"
_AtmVpPMIntervalQuality_Object = MibTableColumn
atmVpPMIntervalQuality = _AtmVpPMIntervalQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 16),
    _AtmVpPMIntervalQuality_Type()
)
atmVpPMIntervalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalQuality.setStatus("current")


class _AtmVpPMIntervalLastDayQuality_Type(Integer32):
    """Custom type atmVpPMIntervalLastDayQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("degraded", 4))
    )


_AtmVpPMIntervalLastDayQuality_Type.__name__ = "Integer32"
_AtmVpPMIntervalLastDayQuality_Object = MibTableColumn
atmVpPMIntervalLastDayQuality = _AtmVpPMIntervalLastDayQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 4, 1, 17),
    _AtmVpPMIntervalLastDayQuality_Type()
)
atmVpPMIntervalLastDayQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMIntervalLastDayQuality.setStatus("current")
_AtmVpQoSTable_Object = MibTable
atmVpQoSTable = _AtmVpQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    atmVpQoSTable.setStatus("current")
_AtmVpQoSEntry_Object = MibTableRow
atmVpQoSEntry = _AtmVpQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 5, 1)
)
atmVpQoSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ACE202-MIB", "atmVpQoSPeriodRef"),
)
if mibBuilder.loadTexts:
    atmVpQoSEntry.setStatus("current")


class _AtmVpQoSPeriodRef_Type(Integer32):
    """Custom type atmVpQoSPeriodRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentPeriod", 1),
          ("lastPeriod", 2))
    )


_AtmVpQoSPeriodRef_Type.__name__ = "Integer32"
_AtmVpQoSPeriodRef_Object = MibTableColumn
atmVpQoSPeriodRef = _AtmVpQoSPeriodRef_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 5, 1, 1),
    _AtmVpQoSPeriodRef_Type()
)
atmVpQoSPeriodRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpQoSPeriodRef.setStatus("current")
_AtmVpQoSElapsedTime_Type = Integer32
_AtmVpQoSElapsedTime_Object = MibTableColumn
atmVpQoSElapsedTime = _AtmVpQoSElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 5, 1, 2),
    _AtmVpQoSElapsedTime_Type()
)
atmVpQoSElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpQoSElapsedTime.setStatus("current")
_AtmVpQoSUAS_Type = Gauge32
_AtmVpQoSUAS_Object = MibTableColumn
atmVpQoSUAS = _AtmVpQoSUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 5, 1, 3),
    _AtmVpQoSUAS_Type()
)
atmVpQoSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpQoSUAS.setStatus("current")
_AtmVpPMQoSTable_Object = MibTable
atmVpPMQoSTable = _AtmVpPMQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    atmVpPMQoSTable.setStatus("current")
_AtmVpPMQoSEntry_Object = MibTableRow
atmVpPMQoSEntry = _AtmVpPMQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 6, 1)
)
atmVpPMQoSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ACE202-MIB", "atmVpPMQoSDirection"),
    (0, "ACE202-MIB", "atmVpPMQoSPeriodRef"),
)
if mibBuilder.loadTexts:
    atmVpPMQoSEntry.setStatus("current")


class _AtmVpPMQoSDirection_Type(Integer32):
    """Custom type atmVpPMQoSDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 2),
          ("backward", 3))
    )


_AtmVpPMQoSDirection_Type.__name__ = "Integer32"
_AtmVpPMQoSDirection_Object = MibTableColumn
atmVpPMQoSDirection = _AtmVpPMQoSDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 6, 1, 1),
    _AtmVpPMQoSDirection_Type()
)
atmVpPMQoSDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMQoSDirection.setStatus("current")


class _AtmVpPMQoSPeriodRef_Type(Integer32):
    """Custom type atmVpPMQoSPeriodRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentPeriod", 1),
          ("lastPeriod", 2))
    )


_AtmVpPMQoSPeriodRef_Type.__name__ = "Integer32"
_AtmVpPMQoSPeriodRef_Object = MibTableColumn
atmVpPMQoSPeriodRef = _AtmVpPMQoSPeriodRef_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 6, 1, 2),
    _AtmVpPMQoSPeriodRef_Type()
)
atmVpPMQoSPeriodRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMQoSPeriodRef.setStatus("current")
_AtmVpPMQoSCLR_Type = Gauge32
_AtmVpPMQoSCLR_Object = MibTableColumn
atmVpPMQoSCLR = _AtmVpPMQoSCLR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 6, 1, 3),
    _AtmVpPMQoSCLR_Type()
)
atmVpPMQoSCLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMQoSCLR.setStatus("current")
_AtmVpPMQoSCER_Type = Gauge32
_AtmVpPMQoSCER_Object = MibTableColumn
atmVpPMQoSCER = _AtmVpPMQoSCER_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 6, 1, 4),
    _AtmVpPMQoSCER_Type()
)
atmVpPMQoSCER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMQoSCER.setStatus("current")
_AtmVpPMQoSCMR_Type = Gauge32
_AtmVpPMQoSCMR_Object = MibTableColumn
atmVpPMQoSCMR = _AtmVpPMQoSCMR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 6, 1, 5),
    _AtmVpPMQoSCMR_Type()
)
atmVpPMQoSCMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPMQoSCMR.setStatus("current")
_AtmVpShaperStatTable_Object = MibTable
atmVpShaperStatTable = _AtmVpShaperStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    atmVpShaperStatTable.setStatus("current")
_AtmVpShaperStatEntry_Object = MibTableRow
atmVpShaperStatEntry = _AtmVpShaperStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7, 1)
)
atmVpShaperStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmVpShaperStatEntry.setStatus("current")
_AtmVpShaperDiscarded_Type = Counter32
_AtmVpShaperDiscarded_Object = MibTableColumn
atmVpShaperDiscarded = _AtmVpShaperDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7, 1, 1),
    _AtmVpShaperDiscarded_Type()
)
atmVpShaperDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpShaperDiscarded.setStatus("current")
_AtmVpShaperOccupation_Type = Integer32
_AtmVpShaperOccupation_Object = MibTableColumn
atmVpShaperOccupation = _AtmVpShaperOccupation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7, 1, 2),
    _AtmVpShaperOccupation_Type()
)
atmVpShaperOccupation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpShaperOccupation.setStatus("current")
_AtmVpShaperMaxOccupation_Type = Integer32
_AtmVpShaperMaxOccupation_Object = MibTableColumn
atmVpShaperMaxOccupation = _AtmVpShaperMaxOccupation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7, 1, 3),
    _AtmVpShaperMaxOccupation_Type()
)
atmVpShaperMaxOccupation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpShaperMaxOccupation.setStatus("current")


class _AtmVpShaperLevel_Type(Integer32):
    """Custom type atmVpShaperLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("full", 2),
          ("below", 3),
          ("above", 4))
    )


_AtmVpShaperLevel_Type.__name__ = "Integer32"
_AtmVpShaperLevel_Object = MibTableColumn
atmVpShaperLevel = _AtmVpShaperLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7, 1, 4),
    _AtmVpShaperLevel_Type()
)
atmVpShaperLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpShaperLevel.setStatus("current")
_AtmVpShaperEpdDropped_Type = Counter32
_AtmVpShaperEpdDropped_Object = MibTableColumn
atmVpShaperEpdDropped = _AtmVpShaperEpdDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7, 1, 5),
    _AtmVpShaperEpdDropped_Type()
)
atmVpShaperEpdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpShaperEpdDropped.setStatus("current")
_AtmVpShaperTotalEpdDropped_Type = Counter32
_AtmVpShaperTotalEpdDropped_Object = MibTableColumn
atmVpShaperTotalEpdDropped = _AtmVpShaperTotalEpdDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 1, 7, 1, 6),
    _AtmVpShaperTotalEpdDropped_Type()
)
atmVpShaperTotalEpdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpShaperTotalEpdDropped.setStatus("current")
_AtmVcPerformance_ObjectIdentity = ObjectIdentity
atmVcPerformance = _AtmVcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2)
)
_AtmVcCurrentTable_Object = MibTable
atmVcCurrentTable = _AtmVcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmVcCurrentTable.setStatus("current")
_AtmVcCurrentEntry_Object = MibTableRow
atmVcCurrentEntry = _AtmVcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1)
)
atmVcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVcCurrentVpi"),
    (0, "ACE202-MIB", "atmVcCurrentVci"),
)
if mibBuilder.loadTexts:
    atmVcCurrentEntry.setStatus("current")
_AtmVcCurrentVpi_Type = Integer32
_AtmVcCurrentVpi_Object = MibTableColumn
atmVcCurrentVpi = _AtmVcCurrentVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 1),
    _AtmVcCurrentVpi_Type()
)
atmVcCurrentVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentVpi.setStatus("current")
_AtmVcCurrentVci_Type = Integer32
_AtmVcCurrentVci_Object = MibTableColumn
atmVcCurrentVci = _AtmVcCurrentVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 2),
    _AtmVcCurrentVci_Type()
)
atmVcCurrentVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentVci.setStatus("current")
_AtmVcCurrentRxCellsClp01_Type = Gauge32
_AtmVcCurrentRxCellsClp01_Object = MibTableColumn
atmVcCurrentRxCellsClp01 = _AtmVcCurrentRxCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 3),
    _AtmVcCurrentRxCellsClp01_Type()
)
atmVcCurrentRxCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentRxCellsClp01.setStatus("current")
_AtmVcCurrentRxCellsClp0_Type = Gauge32
_AtmVcCurrentRxCellsClp0_Object = MibTableColumn
atmVcCurrentRxCellsClp0 = _AtmVcCurrentRxCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 4),
    _AtmVcCurrentRxCellsClp0_Type()
)
atmVcCurrentRxCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentRxCellsClp0.setStatus("current")
_AtmVcCurrentGcra0Violations_Type = Gauge32
_AtmVcCurrentGcra0Violations_Object = MibTableColumn
atmVcCurrentGcra0Violations = _AtmVcCurrentGcra0Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 5),
    _AtmVcCurrentGcra0Violations_Type()
)
atmVcCurrentGcra0Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentGcra0Violations.setStatus("current")
_AtmVcCurrentGcra1Violations_Type = Gauge32
_AtmVcCurrentGcra1Violations_Object = MibTableColumn
atmVcCurrentGcra1Violations = _AtmVcCurrentGcra1Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 6),
    _AtmVcCurrentGcra1Violations_Type()
)
atmVcCurrentGcra1Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentGcra1Violations.setStatus("current")
_AtmVcCurrentRxAIS_Type = Gauge32
_AtmVcCurrentRxAIS_Object = MibTableColumn
atmVcCurrentRxAIS = _AtmVcCurrentRxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 7),
    _AtmVcCurrentRxAIS_Type()
)
atmVcCurrentRxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentRxAIS.setStatus("current")
_AtmVcCurrentTxAIS_Type = Gauge32
_AtmVcCurrentTxAIS_Object = MibTableColumn
atmVcCurrentTxAIS = _AtmVcCurrentTxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 8),
    _AtmVcCurrentTxAIS_Type()
)
atmVcCurrentTxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentTxAIS.setStatus("current")
_AtmVcCurrentRxRDI_Type = Gauge32
_AtmVcCurrentRxRDI_Object = MibTableColumn
atmVcCurrentRxRDI = _AtmVcCurrentRxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 9),
    _AtmVcCurrentRxRDI_Type()
)
atmVcCurrentRxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentRxRDI.setStatus("current")
_AtmVcCurrentTxRDI_Type = Gauge32
_AtmVcCurrentTxRDI_Object = MibTableColumn
atmVcCurrentTxRDI = _AtmVcCurrentTxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 10),
    _AtmVcCurrentTxRDI_Type()
)
atmVcCurrentTxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentTxRDI.setStatus("current")
_AtmVcCurrentContinuityLoss_Type = Gauge32
_AtmVcCurrentContinuityLoss_Object = MibTableColumn
atmVcCurrentContinuityLoss = _AtmVcCurrentContinuityLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 11),
    _AtmVcCurrentContinuityLoss_Type()
)
atmVcCurrentContinuityLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentContinuityLoss.setStatus("current")
_AtmVcCurrentUAS_Type = Gauge32
_AtmVcCurrentUAS_Object = MibTableColumn
atmVcCurrentUAS = _AtmVcCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 12),
    _AtmVcCurrentUAS_Type()
)
atmVcCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentUAS.setStatus("current")
_AtmVcCurrentSES_Type = Gauge32
_AtmVcCurrentSES_Object = MibTableColumn
atmVcCurrentSES = _AtmVcCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 13),
    _AtmVcCurrentSES_Type()
)
atmVcCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentSES.setStatus("current")
_AtmVcCurrentCDC_Type = Gauge32
_AtmVcCurrentCDC_Object = MibTableColumn
atmVcCurrentCDC = _AtmVcCurrentCDC_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 14),
    _AtmVcCurrentCDC_Type()
)
atmVcCurrentCDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentCDC.setStatus("current")
_AtmVcCurrentTotalDiscards_Type = Gauge32
_AtmVcCurrentTotalDiscards_Object = MibTableColumn
atmVcCurrentTotalDiscards = _AtmVcCurrentTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 15),
    _AtmVcCurrentTotalDiscards_Type()
)
atmVcCurrentTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentTotalDiscards.setStatus("current")
_AtmVcCurrentClp0Discards_Type = Gauge32
_AtmVcCurrentClp0Discards_Object = MibTableColumn
atmVcCurrentClp0Discards = _AtmVcCurrentClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 16),
    _AtmVcCurrentClp0Discards_Type()
)
atmVcCurrentClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentClp0Discards.setStatus("current")
_AtmVcCurrentTotalCellOuts_Type = Gauge32
_AtmVcCurrentTotalCellOuts_Object = MibTableColumn
atmVcCurrentTotalCellOuts = _AtmVcCurrentTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 17),
    _AtmVcCurrentTotalCellOuts_Type()
)
atmVcCurrentTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentTotalCellOuts.setStatus("current")
_AtmVcCurrentClp0CellOuts_Type = Gauge32
_AtmVcCurrentClp0CellOuts_Object = MibTableColumn
atmVcCurrentClp0CellOuts = _AtmVcCurrentClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 18),
    _AtmVcCurrentClp0CellOuts_Type()
)
atmVcCurrentClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentClp0CellOuts.setStatus("current")
_AtmVcCurrentTaggedOuts_Type = Gauge32
_AtmVcCurrentTaggedOuts_Object = MibTableColumn
atmVcCurrentTaggedOuts = _AtmVcCurrentTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 19),
    _AtmVcCurrentTaggedOuts_Type()
)
atmVcCurrentTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentTaggedOuts.setStatus("current")
_AtmVcCurrentPCR_Type = Gauge32
_AtmVcCurrentPCR_Object = MibTableColumn
atmVcCurrentPCR = _AtmVcCurrentPCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 20),
    _AtmVcCurrentPCR_Type()
)
atmVcCurrentPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentPCR.setStatus("current")
_AtmVcCurrentSCR_Type = Gauge32
_AtmVcCurrentSCR_Object = MibTableColumn
atmVcCurrentSCR = _AtmVcCurrentSCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 21),
    _AtmVcCurrentSCR_Type()
)
atmVcCurrentSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentSCR.setStatus("current")
_AtmVcCurrentMCR_Type = Gauge32
_AtmVcCurrentMCR_Object = MibTableColumn
atmVcCurrentMCR = _AtmVcCurrentMCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 1, 1, 22),
    _AtmVcCurrentMCR_Type()
)
atmVcCurrentMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCurrentMCR.setStatus("current")
_AtmVcPMCurrentTable_Object = MibTable
atmVcPMCurrentTable = _AtmVcPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    atmVcPMCurrentTable.setStatus("current")
_AtmVcPMCurrentEntry_Object = MibTableRow
atmVcPMCurrentEntry = _AtmVcPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1)
)
atmVcPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVcPMCurrentVpi"),
    (0, "ACE202-MIB", "atmVcPMCurrentVci"),
    (0, "ACE202-MIB", "atmVcPMCurrentDir"),
)
if mibBuilder.loadTexts:
    atmVcPMCurrentEntry.setStatus("current")
_AtmVcPMCurrentVpi_Type = Integer32
_AtmVcPMCurrentVpi_Object = MibTableColumn
atmVcPMCurrentVpi = _AtmVcPMCurrentVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 1),
    _AtmVcPMCurrentVpi_Type()
)
atmVcPMCurrentVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentVpi.setStatus("current")
_AtmVcPMCurrentVci_Type = Integer32
_AtmVcPMCurrentVci_Object = MibTableColumn
atmVcPMCurrentVci = _AtmVcPMCurrentVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 2),
    _AtmVcPMCurrentVci_Type()
)
atmVcPMCurrentVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentVci.setStatus("current")
_AtmVcPMCurrentDir_Type = Integer32
_AtmVcPMCurrentDir_Object = MibTableColumn
atmVcPMCurrentDir = _AtmVcPMCurrentDir_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 3),
    _AtmVcPMCurrentDir_Type()
)
atmVcPMCurrentDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentDir.setStatus("current")
_AtmVcPMCurrentTxClp01_Type = Gauge32
_AtmVcPMCurrentTxClp01_Object = MibTableColumn
atmVcPMCurrentTxClp01 = _AtmVcPMCurrentTxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 4),
    _AtmVcPMCurrentTxClp01_Type()
)
atmVcPMCurrentTxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentTxClp01.setStatus("current")
_AtmVcPMCurrentTxClp0_Type = Gauge32
_AtmVcPMCurrentTxClp0_Object = MibTableColumn
atmVcPMCurrentTxClp0 = _AtmVcPMCurrentTxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 5),
    _AtmVcPMCurrentTxClp0_Type()
)
atmVcPMCurrentTxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentTxClp0.setStatus("current")
_AtmVcPMCurrentRxClp01_Type = Gauge32
_AtmVcPMCurrentRxClp01_Object = MibTableColumn
atmVcPMCurrentRxClp01 = _AtmVcPMCurrentRxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 6),
    _AtmVcPMCurrentRxClp01_Type()
)
atmVcPMCurrentRxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentRxClp01.setStatus("current")
_AtmVcPMCurrentRxClp0_Type = Gauge32
_AtmVcPMCurrentRxClp0_Object = MibTableColumn
atmVcPMCurrentRxClp0 = _AtmVcPMCurrentRxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 7),
    _AtmVcPMCurrentRxClp0_Type()
)
atmVcPMCurrentRxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentRxClp0.setStatus("current")
_AtmVcPMCurrentErroredCells_Type = Gauge32
_AtmVcPMCurrentErroredCells_Object = MibTableColumn
atmVcPMCurrentErroredCells = _AtmVcPMCurrentErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 8),
    _AtmVcPMCurrentErroredCells_Type()
)
atmVcPMCurrentErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentErroredCells.setStatus("current")
_AtmVcPMCurrentLostCells_Type = Gauge32
_AtmVcPMCurrentLostCells_Object = MibTableColumn
atmVcPMCurrentLostCells = _AtmVcPMCurrentLostCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 9),
    _AtmVcPMCurrentLostCells_Type()
)
atmVcPMCurrentLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentLostCells.setStatus("current")
_AtmVcPMCurrentMisinsertedCells_Type = Gauge32
_AtmVcPMCurrentMisinsertedCells_Object = MibTableColumn
atmVcPMCurrentMisinsertedCells = _AtmVcPMCurrentMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 10),
    _AtmVcPMCurrentMisinsertedCells_Type()
)
atmVcPMCurrentMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentMisinsertedCells.setStatus("current")
_AtmVcPMCurrentECB_Type = Gauge32
_AtmVcPMCurrentECB_Object = MibTableColumn
atmVcPMCurrentECB = _AtmVcPMCurrentECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 11),
    _AtmVcPMCurrentECB_Type()
)
atmVcPMCurrentECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentECB.setStatus("current")
_AtmVcPMCurrentSECB_Type = Gauge32
_AtmVcPMCurrentSECB_Object = MibTableColumn
atmVcPMCurrentSECB = _AtmVcPMCurrentSECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 12),
    _AtmVcPMCurrentSECB_Type()
)
atmVcPMCurrentSECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentSECB.setStatus("current")
_AtmVcPMCurrentES_Type = Gauge32
_AtmVcPMCurrentES_Object = MibTableColumn
atmVcPMCurrentES = _AtmVcPMCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 13),
    _AtmVcPMCurrentES_Type()
)
atmVcPMCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentES.setStatus("current")
_AtmVcPMCurrentSES_Type = Gauge32
_AtmVcPMCurrentSES_Object = MibTableColumn
atmVcPMCurrentSES = _AtmVcPMCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 14),
    _AtmVcPMCurrentSES_Type()
)
atmVcPMCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentSES.setStatus("current")
_AtmVcPMCurrentUAS_Type = Gauge32
_AtmVcPMCurrentUAS_Object = MibTableColumn
atmVcPMCurrentUAS = _AtmVcPMCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 15),
    _AtmVcPMCurrentUAS_Type()
)
atmVcPMCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentUAS.setStatus("current")


class _AtmVcPMCurrentIntervalQuality_Type(Integer32):
    """Custom type atmVcPMCurrentIntervalQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("unacceptable", 3))
    )


_AtmVcPMCurrentIntervalQuality_Type.__name__ = "Integer32"
_AtmVcPMCurrentIntervalQuality_Object = MibTableColumn
atmVcPMCurrentIntervalQuality = _AtmVcPMCurrentIntervalQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 16),
    _AtmVcPMCurrentIntervalQuality_Type()
)
atmVcPMCurrentIntervalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentIntervalQuality.setStatus("current")


class _AtmVcPMCurrentLastDayQuality_Type(Integer32):
    """Custom type atmVcPMCurrentLastDayQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("degraded", 4))
    )


_AtmVcPMCurrentLastDayQuality_Type.__name__ = "Integer32"
_AtmVcPMCurrentLastDayQuality_Object = MibTableColumn
atmVcPMCurrentLastDayQuality = _AtmVcPMCurrentLastDayQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 2, 1, 17),
    _AtmVcPMCurrentLastDayQuality_Type()
)
atmVcPMCurrentLastDayQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMCurrentLastDayQuality.setStatus("current")
_AtmVcIntervalTable_Object = MibTable
atmVcIntervalTable = _AtmVcIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    atmVcIntervalTable.setStatus("current")
_AtmVcIntervalEntry_Object = MibTableRow
atmVcIntervalEntry = _AtmVcIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1)
)
atmVcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVcIntervalVpi"),
    (0, "ACE202-MIB", "atmVcIntervalVci"),
    (0, "ACE202-MIB", "atmVcIntervalNumber"),
)
if mibBuilder.loadTexts:
    atmVcIntervalEntry.setStatus("current")
_AtmVcIntervalVpi_Type = Integer32
_AtmVcIntervalVpi_Object = MibTableColumn
atmVcIntervalVpi = _AtmVcIntervalVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 1),
    _AtmVcIntervalVpi_Type()
)
atmVcIntervalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalVpi.setStatus("current")
_AtmVcIntervalVci_Type = Integer32
_AtmVcIntervalVci_Object = MibTableColumn
atmVcIntervalVci = _AtmVcIntervalVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 2),
    _AtmVcIntervalVci_Type()
)
atmVcIntervalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalVci.setStatus("current")


class _AtmVcIntervalNumber_Type(Integer32):
    """Custom type atmVcIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmVcIntervalNumber_Type.__name__ = "Integer32"
_AtmVcIntervalNumber_Object = MibTableColumn
atmVcIntervalNumber = _AtmVcIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 3),
    _AtmVcIntervalNumber_Type()
)
atmVcIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalNumber.setStatus("current")
_AtmVcIntervalRxCellsClp01_Type = Gauge32
_AtmVcIntervalRxCellsClp01_Object = MibTableColumn
atmVcIntervalRxCellsClp01 = _AtmVcIntervalRxCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 4),
    _AtmVcIntervalRxCellsClp01_Type()
)
atmVcIntervalRxCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalRxCellsClp01.setStatus("current")
_AtmVcIntervalRxCellsClp0_Type = Gauge32
_AtmVcIntervalRxCellsClp0_Object = MibTableColumn
atmVcIntervalRxCellsClp0 = _AtmVcIntervalRxCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 5),
    _AtmVcIntervalRxCellsClp0_Type()
)
atmVcIntervalRxCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalRxCellsClp0.setStatus("current")
_AtmVcIntervalGcra0Violations_Type = Gauge32
_AtmVcIntervalGcra0Violations_Object = MibTableColumn
atmVcIntervalGcra0Violations = _AtmVcIntervalGcra0Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 6),
    _AtmVcIntervalGcra0Violations_Type()
)
atmVcIntervalGcra0Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalGcra0Violations.setStatus("current")
_AtmVcIntervalGcra1Violations_Type = Gauge32
_AtmVcIntervalGcra1Violations_Object = MibTableColumn
atmVcIntervalGcra1Violations = _AtmVcIntervalGcra1Violations_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 7),
    _AtmVcIntervalGcra1Violations_Type()
)
atmVcIntervalGcra1Violations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalGcra1Violations.setStatus("current")
_AtmVcIntervalRxAIS_Type = Gauge32
_AtmVcIntervalRxAIS_Object = MibTableColumn
atmVcIntervalRxAIS = _AtmVcIntervalRxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 8),
    _AtmVcIntervalRxAIS_Type()
)
atmVcIntervalRxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalRxAIS.setStatus("current")
_AtmVcIntervalTxAIS_Type = Gauge32
_AtmVcIntervalTxAIS_Object = MibTableColumn
atmVcIntervalTxAIS = _AtmVcIntervalTxAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 9),
    _AtmVcIntervalTxAIS_Type()
)
atmVcIntervalTxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalTxAIS.setStatus("current")
_AtmVcIntervalRxRDI_Type = Gauge32
_AtmVcIntervalRxRDI_Object = MibTableColumn
atmVcIntervalRxRDI = _AtmVcIntervalRxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 10),
    _AtmVcIntervalRxRDI_Type()
)
atmVcIntervalRxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalRxRDI.setStatus("current")
_AtmVcIntervalTxRDI_Type = Gauge32
_AtmVcIntervalTxRDI_Object = MibTableColumn
atmVcIntervalTxRDI = _AtmVcIntervalTxRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 11),
    _AtmVcIntervalTxRDI_Type()
)
atmVcIntervalTxRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalTxRDI.setStatus("current")
_AtmVcIntervalContinuityLoss_Type = Gauge32
_AtmVcIntervalContinuityLoss_Object = MibTableColumn
atmVcIntervalContinuityLoss = _AtmVcIntervalContinuityLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 12),
    _AtmVcIntervalContinuityLoss_Type()
)
atmVcIntervalContinuityLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalContinuityLoss.setStatus("current")
_AtmVcIntervalUAS_Type = Gauge32
_AtmVcIntervalUAS_Object = MibTableColumn
atmVcIntervalUAS = _AtmVcIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 13),
    _AtmVcIntervalUAS_Type()
)
atmVcIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalUAS.setStatus("current")
_AtmVcIntervalSES_Type = Gauge32
_AtmVcIntervalSES_Object = MibTableColumn
atmVcIntervalSES = _AtmVcIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 14),
    _AtmVcIntervalSES_Type()
)
atmVcIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalSES.setStatus("current")
_AtmVcIntervalCDC_Type = Gauge32
_AtmVcIntervalCDC_Object = MibTableColumn
atmVcIntervalCDC = _AtmVcIntervalCDC_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 15),
    _AtmVcIntervalCDC_Type()
)
atmVcIntervalCDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalCDC.setStatus("current")
_AtmVcIntervalTotalDiscards_Type = Gauge32
_AtmVcIntervalTotalDiscards_Object = MibTableColumn
atmVcIntervalTotalDiscards = _AtmVcIntervalTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 16),
    _AtmVcIntervalTotalDiscards_Type()
)
atmVcIntervalTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalTotalDiscards.setStatus("current")
_AtmVcIntervalClp0Discards_Type = Gauge32
_AtmVcIntervalClp0Discards_Object = MibTableColumn
atmVcIntervalClp0Discards = _AtmVcIntervalClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 17),
    _AtmVcIntervalClp0Discards_Type()
)
atmVcIntervalClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalClp0Discards.setStatus("current")
_AtmVcIntervalTotalCellOuts_Type = Gauge32
_AtmVcIntervalTotalCellOuts_Object = MibTableColumn
atmVcIntervalTotalCellOuts = _AtmVcIntervalTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 18),
    _AtmVcIntervalTotalCellOuts_Type()
)
atmVcIntervalTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalTotalCellOuts.setStatus("current")
_AtmVcIntervalClp0CellOuts_Type = Gauge32
_AtmVcIntervalClp0CellOuts_Object = MibTableColumn
atmVcIntervalClp0CellOuts = _AtmVcIntervalClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 19),
    _AtmVcIntervalClp0CellOuts_Type()
)
atmVcIntervalClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalClp0CellOuts.setStatus("current")
_AtmVcIntervalTaggedOuts_Type = Gauge32
_AtmVcIntervalTaggedOuts_Object = MibTableColumn
atmVcIntervalTaggedOuts = _AtmVcIntervalTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 20),
    _AtmVcIntervalTaggedOuts_Type()
)
atmVcIntervalTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalTaggedOuts.setStatus("current")
_AtmVcIntervalPCR_Type = Gauge32
_AtmVcIntervalPCR_Object = MibTableColumn
atmVcIntervalPCR = _AtmVcIntervalPCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 21),
    _AtmVcIntervalPCR_Type()
)
atmVcIntervalPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalPCR.setStatus("current")
_AtmVcIntervalSCR_Type = Gauge32
_AtmVcIntervalSCR_Object = MibTableColumn
atmVcIntervalSCR = _AtmVcIntervalSCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 22),
    _AtmVcIntervalSCR_Type()
)
atmVcIntervalSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalSCR.setStatus("current")
_AtmVcIntervalMCR_Type = Gauge32
_AtmVcIntervalMCR_Object = MibTableColumn
atmVcIntervalMCR = _AtmVcIntervalMCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 3, 1, 23),
    _AtmVcIntervalMCR_Type()
)
atmVcIntervalMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIntervalMCR.setStatus("current")
_AtmVcPMIntervalTable_Object = MibTable
atmVcPMIntervalTable = _AtmVcPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    atmVcPMIntervalTable.setStatus("current")
_AtmVcPMIntervalEntry_Object = MibTableRow
atmVcPMIntervalEntry = _AtmVcPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1)
)
atmVcPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmVcPMIntervalVpi"),
    (0, "ACE202-MIB", "atmVcPMIntervalVci"),
    (0, "ACE202-MIB", "atmVcPMIntervalDir"),
    (0, "ACE202-MIB", "atmVcPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    atmVcPMIntervalEntry.setStatus("current")
_AtmVcPMIntervalVpi_Type = Integer32
_AtmVcPMIntervalVpi_Object = MibTableColumn
atmVcPMIntervalVpi = _AtmVcPMIntervalVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 1),
    _AtmVcPMIntervalVpi_Type()
)
atmVcPMIntervalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalVpi.setStatus("current")
_AtmVcPMIntervalVci_Type = Integer32
_AtmVcPMIntervalVci_Object = MibTableColumn
atmVcPMIntervalVci = _AtmVcPMIntervalVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 2),
    _AtmVcPMIntervalVci_Type()
)
atmVcPMIntervalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalVci.setStatus("current")


class _AtmVcPMIntervalDir_Type(Integer32):
    """Custom type atmVcPMIntervalDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 2),
          ("backward", 3))
    )


_AtmVcPMIntervalDir_Type.__name__ = "Integer32"
_AtmVcPMIntervalDir_Object = MibTableColumn
atmVcPMIntervalDir = _AtmVcPMIntervalDir_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 3),
    _AtmVcPMIntervalDir_Type()
)
atmVcPMIntervalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalDir.setStatus("current")


class _AtmVcPMIntervalNumber_Type(Integer32):
    """Custom type atmVcPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmVcPMIntervalNumber_Type.__name__ = "Integer32"
_AtmVcPMIntervalNumber_Object = MibTableColumn
atmVcPMIntervalNumber = _AtmVcPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 4),
    _AtmVcPMIntervalNumber_Type()
)
atmVcPMIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalNumber.setStatus("current")
_AtmVcPMIntervalTxClp01_Type = Gauge32
_AtmVcPMIntervalTxClp01_Object = MibTableColumn
atmVcPMIntervalTxClp01 = _AtmVcPMIntervalTxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 5),
    _AtmVcPMIntervalTxClp01_Type()
)
atmVcPMIntervalTxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalTxClp01.setStatus("current")
_AtmVcPMIntervalTxClp0_Type = Gauge32
_AtmVcPMIntervalTxClp0_Object = MibTableColumn
atmVcPMIntervalTxClp0 = _AtmVcPMIntervalTxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 6),
    _AtmVcPMIntervalTxClp0_Type()
)
atmVcPMIntervalTxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalTxClp0.setStatus("current")
_AtmVcPMIntervalRxClp01_Type = Gauge32
_AtmVcPMIntervalRxClp01_Object = MibTableColumn
atmVcPMIntervalRxClp01 = _AtmVcPMIntervalRxClp01_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 7),
    _AtmVcPMIntervalRxClp01_Type()
)
atmVcPMIntervalRxClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalRxClp01.setStatus("current")
_AtmVcPMIntervalRxClp0_Type = Gauge32
_AtmVcPMIntervalRxClp0_Object = MibTableColumn
atmVcPMIntervalRxClp0 = _AtmVcPMIntervalRxClp0_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 8),
    _AtmVcPMIntervalRxClp0_Type()
)
atmVcPMIntervalRxClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalRxClp0.setStatus("current")
_AtmVcPMIntervalErroredCells_Type = Gauge32
_AtmVcPMIntervalErroredCells_Object = MibTableColumn
atmVcPMIntervalErroredCells = _AtmVcPMIntervalErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 9),
    _AtmVcPMIntervalErroredCells_Type()
)
atmVcPMIntervalErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalErroredCells.setStatus("current")
_AtmVcPMIntervalLostCells_Type = Gauge32
_AtmVcPMIntervalLostCells_Object = MibTableColumn
atmVcPMIntervalLostCells = _AtmVcPMIntervalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 10),
    _AtmVcPMIntervalLostCells_Type()
)
atmVcPMIntervalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalLostCells.setStatus("current")
_AtmVcPMIntervalMisinsertedCells_Type = Gauge32
_AtmVcPMIntervalMisinsertedCells_Object = MibTableColumn
atmVcPMIntervalMisinsertedCells = _AtmVcPMIntervalMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 11),
    _AtmVcPMIntervalMisinsertedCells_Type()
)
atmVcPMIntervalMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalMisinsertedCells.setStatus("current")
_AtmVcPMIntervalECB_Type = Gauge32
_AtmVcPMIntervalECB_Object = MibTableColumn
atmVcPMIntervalECB = _AtmVcPMIntervalECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 12),
    _AtmVcPMIntervalECB_Type()
)
atmVcPMIntervalECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalECB.setStatus("current")
_AtmVcPMIntervalSECB_Type = Gauge32
_AtmVcPMIntervalSECB_Object = MibTableColumn
atmVcPMIntervalSECB = _AtmVcPMIntervalSECB_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 13),
    _AtmVcPMIntervalSECB_Type()
)
atmVcPMIntervalSECB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalSECB.setStatus("current")
_AtmVcPMIntervalES_Type = Gauge32
_AtmVcPMIntervalES_Object = MibTableColumn
atmVcPMIntervalES = _AtmVcPMIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 14),
    _AtmVcPMIntervalES_Type()
)
atmVcPMIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalES.setStatus("current")
_AtmVcPMIntervalSES_Type = Gauge32
_AtmVcPMIntervalSES_Object = MibTableColumn
atmVcPMIntervalSES = _AtmVcPMIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 15),
    _AtmVcPMIntervalSES_Type()
)
atmVcPMIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalSES.setStatus("current")
_AtmVcPMIntervalUAS_Type = Gauge32
_AtmVcPMIntervalUAS_Object = MibTableColumn
atmVcPMIntervalUAS = _AtmVcPMIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 16),
    _AtmVcPMIntervalUAS_Type()
)
atmVcPMIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalUAS.setStatus("current")


class _AtmVcPMIntervalQuality_Type(Integer32):
    """Custom type atmVcPMIntervalQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("unacceptable", 3))
    )


_AtmVcPMIntervalQuality_Type.__name__ = "Integer32"
_AtmVcPMIntervalQuality_Object = MibTableColumn
atmVcPMIntervalQuality = _AtmVcPMIntervalQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 17),
    _AtmVcPMIntervalQuality_Type()
)
atmVcPMIntervalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalQuality.setStatus("current")


class _AtmVcPMIntervalLastDayQuality_Type(Integer32):
    """Custom type atmVcPMIntervalLastDayQuality based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("degraded", 4))
    )


_AtmVcPMIntervalLastDayQuality_Type.__name__ = "Integer32"
_AtmVcPMIntervalLastDayQuality_Object = MibTableColumn
atmVcPMIntervalLastDayQuality = _AtmVcPMIntervalLastDayQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 4, 1, 18),
    _AtmVcPMIntervalLastDayQuality_Type()
)
atmVcPMIntervalLastDayQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMIntervalLastDayQuality.setStatus("current")
_AtmVcQoSTable_Object = MibTable
atmVcQoSTable = _AtmVcQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    atmVcQoSTable.setStatus("current")
_AtmVcQoSEntry_Object = MibTableRow
atmVcQoSEntry = _AtmVcQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 6, 1)
)
atmVcQoSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ACE202-MIB", "atmVcQoSPeriodRef"),
)
if mibBuilder.loadTexts:
    atmVcQoSEntry.setStatus("current")


class _AtmVcQoSPeriodRef_Type(Integer32):
    """Custom type atmVcQoSPeriodRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentPeriod", 1),
          ("lastPeriod", 2))
    )


_AtmVcQoSPeriodRef_Type.__name__ = "Integer32"
_AtmVcQoSPeriodRef_Object = MibTableColumn
atmVcQoSPeriodRef = _AtmVcQoSPeriodRef_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 6, 1, 1),
    _AtmVcQoSPeriodRef_Type()
)
atmVcQoSPeriodRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcQoSPeriodRef.setStatus("current")
_AtmVcQoSElapsedTime_Type = Integer32
_AtmVcQoSElapsedTime_Object = MibTableColumn
atmVcQoSElapsedTime = _AtmVcQoSElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 6, 1, 2),
    _AtmVcQoSElapsedTime_Type()
)
atmVcQoSElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcQoSElapsedTime.setStatus("current")
_AtmVcQoSUAS_Type = Gauge32
_AtmVcQoSUAS_Object = MibTableColumn
atmVcQoSUAS = _AtmVcQoSUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 6, 1, 3),
    _AtmVcQoSUAS_Type()
)
atmVcQoSUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcQoSUAS.setStatus("current")
_AtmVcPMQoSTable_Object = MibTable
atmVcPMQoSTable = _AtmVcPMQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    atmVcPMQoSTable.setStatus("current")
_AtmVcPMQoSEntry_Object = MibTableRow
atmVcPMQoSEntry = _AtmVcPMQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 7, 1)
)
atmVcPMQoSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ACE202-MIB", "atmVcPMQoSDirection"),
    (0, "ACE202-MIB", "atmVcPMQoSPeriodRef"),
)
if mibBuilder.loadTexts:
    atmVcPMQoSEntry.setStatus("current")


class _AtmVcPMQoSDirection_Type(Integer32):
    """Custom type atmVcPMQoSDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 2),
          ("backward", 3))
    )


_AtmVcPMQoSDirection_Type.__name__ = "Integer32"
_AtmVcPMQoSDirection_Object = MibTableColumn
atmVcPMQoSDirection = _AtmVcPMQoSDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 7, 1, 1),
    _AtmVcPMQoSDirection_Type()
)
atmVcPMQoSDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMQoSDirection.setStatus("current")


class _AtmVcPMQoSPeriodRef_Type(Integer32):
    """Custom type atmVcPMQoSPeriodRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentPeriod", 1),
          ("lastPeriod", 2))
    )


_AtmVcPMQoSPeriodRef_Type.__name__ = "Integer32"
_AtmVcPMQoSPeriodRef_Object = MibTableColumn
atmVcPMQoSPeriodRef = _AtmVcPMQoSPeriodRef_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 7, 1, 2),
    _AtmVcPMQoSPeriodRef_Type()
)
atmVcPMQoSPeriodRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMQoSPeriodRef.setStatus("current")
_AtmVcPMQoSCLR_Type = Gauge32
_AtmVcPMQoSCLR_Object = MibTableColumn
atmVcPMQoSCLR = _AtmVcPMQoSCLR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 7, 1, 3),
    _AtmVcPMQoSCLR_Type()
)
atmVcPMQoSCLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMQoSCLR.setStatus("current")
_AtmVcPMQoSCER_Type = Gauge32
_AtmVcPMQoSCER_Object = MibTableColumn
atmVcPMQoSCER = _AtmVcPMQoSCER_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 7, 1, 4),
    _AtmVcPMQoSCER_Type()
)
atmVcPMQoSCER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMQoSCER.setStatus("current")
_AtmVcPMQoSCMR_Type = Gauge32
_AtmVcPMQoSCMR_Object = MibTableColumn
atmVcPMQoSCMR = _AtmVcPMQoSCMR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 7, 1, 5),
    _AtmVcPMQoSCMR_Type()
)
atmVcPMQoSCMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPMQoSCMR.setStatus("current")
_AtmVcShaperStatTable_Object = MibTable
atmVcShaperStatTable = _AtmVcShaperStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    atmVcShaperStatTable.setStatus("current")
_AtmVcShaperStatEntry_Object = MibTableRow
atmVcShaperStatEntry = _AtmVcShaperStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8, 1)
)
atmVcShaperStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmVcShaperStatEntry.setStatus("current")
_AtmVcShaperDiscarded_Type = Counter32
_AtmVcShaperDiscarded_Object = MibTableColumn
atmVcShaperDiscarded = _AtmVcShaperDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8, 1, 1),
    _AtmVcShaperDiscarded_Type()
)
atmVcShaperDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcShaperDiscarded.setStatus("current")
_AtmVcShaperOccupation_Type = Integer32
_AtmVcShaperOccupation_Object = MibTableColumn
atmVcShaperOccupation = _AtmVcShaperOccupation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8, 1, 2),
    _AtmVcShaperOccupation_Type()
)
atmVcShaperOccupation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcShaperOccupation.setStatus("current")
_AtmVcShaperMaxOccupation_Type = Integer32
_AtmVcShaperMaxOccupation_Object = MibTableColumn
atmVcShaperMaxOccupation = _AtmVcShaperMaxOccupation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8, 1, 3),
    _AtmVcShaperMaxOccupation_Type()
)
atmVcShaperMaxOccupation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcShaperMaxOccupation.setStatus("current")


class _AtmVcShaperLevel_Type(Integer32):
    """Custom type atmVcShaperLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("full", 2),
          ("below", 3),
          ("above", 4))
    )


_AtmVcShaperLevel_Type.__name__ = "Integer32"
_AtmVcShaperLevel_Object = MibTableColumn
atmVcShaperLevel = _AtmVcShaperLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8, 1, 4),
    _AtmVcShaperLevel_Type()
)
atmVcShaperLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcShaperLevel.setStatus("current")
_AtmVcShaperEpdDropped_Type = Counter32
_AtmVcShaperEpdDropped_Object = MibTableColumn
atmVcShaperEpdDropped = _AtmVcShaperEpdDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8, 1, 5),
    _AtmVcShaperEpdDropped_Type()
)
atmVcShaperEpdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcShaperEpdDropped.setStatus("current")
_AtmVcShaperTotalEpdDropped_Type = Counter32
_AtmVcShaperTotalEpdDropped_Object = MibTableColumn
atmVcShaperTotalEpdDropped = _AtmVcShaperTotalEpdDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 2, 2, 8, 1, 6),
    _AtmVcShaperTotalEpdDropped_Type()
)
atmVcShaperTotalEpdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcShaperTotalEpdDropped.setStatus("current")
_AtmIntervalDateTable_Object = MibTable
atmIntervalDateTable = _AtmIntervalDateTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmIntervalDateTable.setStatus("current")
_AtmIntervalDateEntry_Object = MibTableRow
atmIntervalDateEntry = _AtmIntervalDateEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 3, 1)
)
atmIntervalDateEntry.setIndexNames(
    (0, "ACE202-MIB", "atmIntervalDateInterval"),
)
if mibBuilder.loadTexts:
    atmIntervalDateEntry.setStatus("current")


class _AtmIntervalDateInterval_Type(Integer32):
    """Custom type atmIntervalDateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmIntervalDateInterval_Type.__name__ = "Integer32"
_AtmIntervalDateInterval_Object = MibTableColumn
atmIntervalDateInterval = _AtmIntervalDateInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 3, 1, 1),
    _AtmIntervalDateInterval_Type()
)
atmIntervalDateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntervalDateInterval.setStatus("current")
_AtmIntervalDateDate_Type = DisplayString
_AtmIntervalDateDate_Object = MibTableColumn
atmIntervalDateDate = _AtmIntervalDateDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 3, 1, 2),
    _AtmIntervalDateDate_Type()
)
atmIntervalDateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntervalDateDate.setStatus("current")
_AtmIntervalDateTime_Type = DisplayString
_AtmIntervalDateTime_Object = MibTableColumn
atmIntervalDateTime = _AtmIntervalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 1, 3, 1, 3),
    _AtmIntervalDateTime_Type()
)
atmIntervalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntervalDateTime.setStatus("current")
_AtmGenSystem_ObjectIdentity = ObjectIdentity
atmGenSystem = _AtmGenSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2)
)
_AtmGenSysGen_ObjectIdentity = ObjectIdentity
atmGenSysGen = _AtmGenSysGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1)
)
_AtmGenSysSelfTestTable_Object = MibTable
atmGenSysSelfTestTable = _AtmGenSysSelfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmGenSysSelfTestTable.setStatus("current")
_AtmGenSysSelfTestEntry_Object = MibTableRow
atmGenSysSelfTestEntry = _AtmGenSysSelfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 1, 1)
)
atmGenSysSelfTestEntry.setIndexNames(
    (0, "ACE202-MIB", "atmGenSysSelfTestIndex"),
)
if mibBuilder.loadTexts:
    atmGenSysSelfTestEntry.setStatus("current")
_AtmGenSysSelfTestIndex_Type = Integer32
_AtmGenSysSelfTestIndex_Object = MibTableColumn
atmGenSysSelfTestIndex = _AtmGenSysSelfTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 1, 1, 1),
    _AtmGenSysSelfTestIndex_Type()
)
atmGenSysSelfTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenSysSelfTestIndex.setStatus("current")
_AtmGenSysSelfTestResult_Type = DisplayString
_AtmGenSysSelfTestResult_Object = MibTableColumn
atmGenSysSelfTestResult = _AtmGenSysSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 1, 1, 2),
    _AtmGenSysSelfTestResult_Type()
)
atmGenSysSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenSysSelfTestResult.setStatus("current")


class _AtmGenSysLogClearAll_Type(Integer32):
    """Custom type atmGenSysLogClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("clear", 3))
    )


_AtmGenSysLogClearAll_Type.__name__ = "Integer32"
_AtmGenSysLogClearAll_Object = MibScalar
atmGenSysLogClearAll = _AtmGenSysLogClearAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 2),
    _AtmGenSysLogClearAll_Type()
)
atmGenSysLogClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenSysLogClearAll.setStatus("current")
_AtmGenSysLogTable_Object = MibTable
atmGenSysLogTable = _AtmGenSysLogTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmGenSysLogTable.setStatus("current")
_AtmGenSysLogEntry_Object = MibTableRow
atmGenSysLogEntry = _AtmGenSysLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 3, 1)
)
atmGenSysLogEntry.setIndexNames(
    (0, "ACE202-MIB", "atmGenSysLogIndex"),
)
if mibBuilder.loadTexts:
    atmGenSysLogEntry.setStatus("current")


class _AtmGenSysLogIndex_Type(Integer32):
    """Custom type atmGenSysLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_AtmGenSysLogIndex_Type.__name__ = "Integer32"
_AtmGenSysLogIndex_Object = MibTableColumn
atmGenSysLogIndex = _AtmGenSysLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 3, 1, 1),
    _AtmGenSysLogIndex_Type()
)
atmGenSysLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenSysLogIndex.setStatus("current")


class _AtmGenSysLogMessage_Type(DisplayString):
    """Custom type atmGenSysLogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_AtmGenSysLogMessage_Type.__name__ = "DisplayString"
_AtmGenSysLogMessage_Object = MibTableColumn
atmGenSysLogMessage = _AtmGenSysLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 3, 1, 2),
    _AtmGenSysLogMessage_Type()
)
atmGenSysLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenSysLogMessage.setStatus("current")


class _AtmGenSysSetDefaultConfg_Type(Integer32):
    """Custom type atmGenSysSetDefaultConfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AtmGenSysSetDefaultConfg_Type.__name__ = "Integer32"
_AtmGenSysSetDefaultConfg_Object = MibScalar
atmGenSysSetDefaultConfg = _AtmGenSysSetDefaultConfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 4),
    _AtmGenSysSetDefaultConfg_Type()
)
atmGenSysSetDefaultConfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmGenSysSetDefaultConfg.setStatus("current")
_AtmGenSysCxRefTable_Object = MibTable
atmGenSysCxRefTable = _AtmGenSysCxRefTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    atmGenSysCxRefTable.setStatus("current")
_AtmGenSysCxRefEntry_Object = MibTableRow
atmGenSysCxRefEntry = _AtmGenSysCxRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 5, 1)
)
atmGenSysCxRefEntry.setIndexNames(
    (0, "ACE202-MIB", "atmGenSysCxRefIndex"),
)
if mibBuilder.loadTexts:
    atmGenSysCxRefEntry.setStatus("current")
_AtmGenSysCxRefIndex_Type = Integer32
_AtmGenSysCxRefIndex_Object = MibTableColumn
atmGenSysCxRefIndex = _AtmGenSysCxRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 5, 1, 1),
    _AtmGenSysCxRefIndex_Type()
)
atmGenSysCxRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenSysCxRefIndex.setStatus("current")
_AtmGenSysCxRefCounter_Type = Gauge32
_AtmGenSysCxRefCounter_Object = MibTableColumn
atmGenSysCxRefCounter = _AtmGenSysCxRefCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 2, 2, 1, 5, 1, 2),
    _AtmGenSysCxRefCounter_Type()
)
atmGenSysCxRefCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmGenSysCxRefCounter.setStatus("current")
_AtmNte_ObjectIdentity = ObjectIdentity
atmNte = _AtmNte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3)
)
_AtmNteEvents_ObjectIdentity = ObjectIdentity
atmNteEvents = _AtmNteEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 0)
)
if mibBuilder.loadTexts:
    atmNteEvents.setStatus("current")
_AtmNteSys_ObjectIdentity = ObjectIdentity
atmNteSys = _AtmNteSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1)
)
_AtmNteSysConfig_ObjectIdentity = ObjectIdentity
atmNteSysConfig = _AtmNteSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1)
)
_AtmNteManagerTable_Object = MibTable
atmNteManagerTable = _AtmNteManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmNteManagerTable.setStatus("current")
_AtmNteManagerEntry_Object = MibTableRow
atmNteManagerEntry = _AtmNteManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1)
)
atmNteManagerEntry.setIndexNames(
    (0, "ACE202-MIB", "atmNteManagerIP"),
    (0, "ACE202-MIB", "atmNteManagerPvc"),
)
if mibBuilder.loadTexts:
    atmNteManagerEntry.setStatus("current")
_AtmNteManagerIP_Type = IpAddress
_AtmNteManagerIP_Object = MibTableColumn
atmNteManagerIP = _AtmNteManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 1),
    _AtmNteManagerIP_Type()
)
atmNteManagerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteManagerIP.setStatus("current")
_AtmNteManagerPvc_Type = Integer32
_AtmNteManagerPvc_Object = MibTableColumn
atmNteManagerPvc = _AtmNteManagerPvc_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 2),
    _AtmNteManagerPvc_Type()
)
atmNteManagerPvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteManagerPvc.setStatus("current")
_AtmNteManagerIfIndex_Type = Integer32
_AtmNteManagerIfIndex_Object = MibTableColumn
atmNteManagerIfIndex = _AtmNteManagerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 3),
    _AtmNteManagerIfIndex_Type()
)
atmNteManagerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerIfIndex.setStatus("current")
_AtmNteManagerVpi_Type = Integer32
_AtmNteManagerVpi_Object = MibTableColumn
atmNteManagerVpi = _AtmNteManagerVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 4),
    _AtmNteManagerVpi_Type()
)
atmNteManagerVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerVpi.setStatus("current")
_AtmNteManagerVci_Type = Integer32
_AtmNteManagerVci_Object = MibTableColumn
atmNteManagerVci = _AtmNteManagerVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 5),
    _AtmNteManagerVci_Type()
)
atmNteManagerVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerVci.setStatus("current")
_AtmNteManagerTrapMask_Type = Integer32
_AtmNteManagerTrapMask_Object = MibTableColumn
atmNteManagerTrapMask = _AtmNteManagerTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 6),
    _AtmNteManagerTrapMask_Type()
)
atmNteManagerTrapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerTrapMask.setStatus("current")
_AtmNteManagerRowStatus_Type = RowStatus
_AtmNteManagerRowStatus_Object = MibTableColumn
atmNteManagerRowStatus = _AtmNteManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 7),
    _AtmNteManagerRowStatus_Type()
)
atmNteManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerRowStatus.setStatus("current")
_AtmNteManagerNextHop_Type = IpAddress
_AtmNteManagerNextHop_Object = MibTableColumn
atmNteManagerNextHop = _AtmNteManagerNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 8),
    _AtmNteManagerNextHop_Type()
)
atmNteManagerNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerNextHop.setStatus("current")


class _AtmNteManagerVlanSupport_Type(Integer32):
    """Custom type atmNteManagerVlanSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AtmNteManagerVlanSupport_Type.__name__ = "Integer32"
_AtmNteManagerVlanSupport_Object = MibTableColumn
atmNteManagerVlanSupport = _AtmNteManagerVlanSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 9),
    _AtmNteManagerVlanSupport_Type()
)
atmNteManagerVlanSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerVlanSupport.setStatus("current")
_AtmNteManagerVlanIdentifier_Type = Integer32
_AtmNteManagerVlanIdentifier_Object = MibTableColumn
atmNteManagerVlanIdentifier = _AtmNteManagerVlanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 10),
    _AtmNteManagerVlanIdentifier_Type()
)
atmNteManagerVlanIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerVlanIdentifier.setStatus("current")
_AtmNteManagerVlanFramePriority_Type = Integer32
_AtmNteManagerVlanFramePriority_Object = MibTableColumn
atmNteManagerVlanFramePriority = _AtmNteManagerVlanFramePriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 1, 1, 11),
    _AtmNteManagerVlanFramePriority_Type()
)
atmNteManagerVlanFramePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteManagerVlanFramePriority.setStatus("current")
_AtmNteUPLTCR_Type = Integer32
_AtmNteUPLTCR_Object = MibScalar
atmNteUPLTCR = _AtmNteUPLTCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 2),
    _AtmNteUPLTCR_Type()
)
atmNteUPLTCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteUPLTCR.setStatus("current")
_AtmNteDPLTCR_Type = Integer32
_AtmNteDPLTCR_Object = MibScalar
atmNteDPLTCR = _AtmNteDPLTCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 3),
    _AtmNteDPLTCR_Type()
)
atmNteDPLTCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteDPLTCR.setStatus("current")


class _AtmNteSysLogClearAll_Type(Integer32):
    """Custom type atmNteSysLogClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("clear", 3))
    )


_AtmNteSysLogClearAll_Type.__name__ = "Integer32"
_AtmNteSysLogClearAll_Object = MibScalar
atmNteSysLogClearAll = _AtmNteSysLogClearAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 4),
    _AtmNteSysLogClearAll_Type()
)
atmNteSysLogClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteSysLogClearAll.setStatus("current")
_AtmNteUSESLTCR_Type = Integer32
_AtmNteUSESLTCR_Object = MibScalar
atmNteUSESLTCR = _AtmNteUSESLTCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 5),
    _AtmNteUSESLTCR_Type()
)
atmNteUSESLTCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteUSESLTCR.setStatus("current")
_AtmNteDSESLTCR_Type = Integer32
_AtmNteDSESLTCR_Object = MibScalar
atmNteDSESLTCR = _AtmNteDSESLTCR_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 6),
    _AtmNteDSESLTCR_Type()
)
atmNteDSESLTCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteDSESLTCR.setStatus("current")
_AtmNteProtection_ObjectIdentity = ObjectIdentity
atmNteProtection = _AtmNteProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 8)
)


class _AtmNteProtectionMode_Type(Integer32):
    """Custom type atmNteProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("mspOn", 2),
          ("pathOn", 3),
          ("mspUniOn", 4),
          ("mspOneToN", 5))
    )


_AtmNteProtectionMode_Type.__name__ = "Integer32"
_AtmNteProtectionMode_Object = MibScalar
atmNteProtectionMode = _AtmNteProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 8, 1),
    _AtmNteProtectionMode_Type()
)
atmNteProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteProtectionMode.setStatus("current")


class _AtmNteProtectionWorkingLink_Type(Integer32):
    """Custom type atmNteProtectionWorkingLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trunk1", 2),
          ("trunk2", 3))
    )


_AtmNteProtectionWorkingLink_Type.__name__ = "Integer32"
_AtmNteProtectionWorkingLink_Object = MibScalar
atmNteProtectionWorkingLink = _AtmNteProtectionWorkingLink_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 8, 2),
    _AtmNteProtectionWorkingLink_Type()
)
atmNteProtectionWorkingLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteProtectionWorkingLink.setStatus("current")


class _AtmNteProtectionSwitchLink_Type(Integer32):
    """Custom type atmNteProtectionSwitchLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("forceSwitch", 2))
    )


_AtmNteProtectionSwitchLink_Type.__name__ = "Integer32"
_AtmNteProtectionSwitchLink_Object = MibScalar
atmNteProtectionSwitchLink = _AtmNteProtectionSwitchLink_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 8, 3),
    _AtmNteProtectionSwitchLink_Type()
)
atmNteProtectionSwitchLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteProtectionSwitchLink.setStatus("current")
_AtmNteConfOam_ObjectIdentity = ObjectIdentity
atmNteConfOam = _AtmNteConfOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9)
)


class _AtmNteConfOamSupport_Type(Integer32):
    """Custom type atmNteConfOamSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("segmentTermination", 2),
          ("endToEndTermination", 3),
          ("vpEndToEndVcSegment", 4))
    )


_AtmNteConfOamSupport_Type.__name__ = "Integer32"
_AtmNteConfOamSupport_Object = MibScalar
atmNteConfOamSupport = _AtmNteConfOamSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 1),
    _AtmNteConfOamSupport_Type()
)
atmNteConfOamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConfOamSupport.setStatus("current")
_AtmNteConfOamTransmission_ObjectIdentity = ObjectIdentity
atmNteConfOamTransmission = _AtmNteConfOamTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 2)
)


class _AtmNteConfOamAIS_Type(Integer32):
    """Custom type atmNteConfOamAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("user", 2),
          ("network", 3),
          ("both", 4))
    )


_AtmNteConfOamAIS_Type.__name__ = "Integer32"
_AtmNteConfOamAIS_Object = MibScalar
atmNteConfOamAIS = _AtmNteConfOamAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 2, 1),
    _AtmNteConfOamAIS_Type()
)
atmNteConfOamAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConfOamAIS.setStatus("current")


class _AtmNteConfOamRDI_Type(Integer32):
    """Custom type atmNteConfOamRDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("user", 2),
          ("network", 3),
          ("both", 4))
    )


_AtmNteConfOamRDI_Type.__name__ = "Integer32"
_AtmNteConfOamRDI_Object = MibScalar
atmNteConfOamRDI = _AtmNteConfOamRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 2, 2),
    _AtmNteConfOamRDI_Type()
)
atmNteConfOamRDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConfOamRDI.setStatus("current")
_AtmNteConfOamAddressing_ObjectIdentity = ObjectIdentity
atmNteConfOamAddressing = _AtmNteConfOamAddressing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 3)
)


class _AtmNteConfLoopbackAddMode_Type(Integer32):
    """Custom type atmNteConfLoopbackAddMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtmNteConfLoopbackAddMode_Type.__name__ = "Integer32"
_AtmNteConfLoopbackAddMode_Object = MibScalar
atmNteConfLoopbackAddMode = _AtmNteConfLoopbackAddMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 3, 1),
    _AtmNteConfLoopbackAddMode_Type()
)
atmNteConfLoopbackAddMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConfLoopbackAddMode.setStatus("current")


class _AtmNteConfLoopbackSourceAdd_Type(OctetString):
    """Custom type atmNteConfLoopbackSourceAdd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 20),
    )


_AtmNteConfLoopbackSourceAdd_Type.__name__ = "OctetString"
_AtmNteConfLoopbackSourceAdd_Object = MibScalar
atmNteConfLoopbackSourceAdd = _AtmNteConfLoopbackSourceAdd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 3, 2),
    _AtmNteConfLoopbackSourceAdd_Type()
)
atmNteConfLoopbackSourceAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConfLoopbackSourceAdd.setStatus("current")
_AtmNteConfOamIfTable_Object = MibTable
atmNteConfOamIfTable = _AtmNteConfOamIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    atmNteConfOamIfTable.setStatus("current")
_AtmNteConfOamIfEntry_Object = MibTableRow
atmNteConfOamIfEntry = _AtmNteConfOamIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 4, 1)
)
atmNteConfOamIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmNteConfOamIfEntry.setStatus("current")


class _AtmNteConfOamIfAisRdi_Type(Integer32):
    """Custom type atmNteConfOamIfAisRdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtmNteConfOamIfAisRdi_Type.__name__ = "Integer32"
_AtmNteConfOamIfAisRdi_Object = MibTableColumn
atmNteConfOamIfAisRdi = _AtmNteConfOamIfAisRdi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 9, 4, 1, 1),
    _AtmNteConfOamIfAisRdi_Type()
)
atmNteConfOamIfAisRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConfOamIfAisRdi.setStatus("current")
_AtmNteConfCAC_ObjectIdentity = ObjectIdentity
atmNteConfCAC = _AtmNteConfCAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 10)
)


class _AtmNteConfCACMode_Type(Integer32):
    """Custom type atmNteConfCACMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtmNteConfCACMode_Type.__name__ = "Integer32"
_AtmNteConfCACMode_Object = MibScalar
atmNteConfCACMode = _AtmNteConfCACMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 10, 1),
    _AtmNteConfCACMode_Type()
)
atmNteConfCACMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConfCACMode.setStatus("current")
_AtmNteHostIfTable_Object = MibTable
atmNteHostIfTable = _AtmNteHostIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    atmNteHostIfTable.setStatus("current")
_AtmNteHostIfEntry_Object = MibTableRow
atmNteHostIfEntry = _AtmNteHostIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1)
)
atmNteHostIfEntry.setIndexNames(
    (0, "ACE202-MIB", "atmNteHostPvcIndex"),
)
if mibBuilder.loadTexts:
    atmNteHostIfEntry.setStatus("current")
_AtmNteHostPvcIndex_Type = Integer32
_AtmNteHostPvcIndex_Object = MibTableColumn
atmNteHostPvcIndex = _AtmNteHostPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 1),
    _AtmNteHostPvcIndex_Type()
)
atmNteHostPvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteHostPvcIndex.setStatus("current")
_AtmNteHostIP_Type = IpAddress
_AtmNteHostIP_Object = MibTableColumn
atmNteHostIP = _AtmNteHostIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 2),
    _AtmNteHostIP_Type()
)
atmNteHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostIP.setStatus("current")
_AtmNteHostMask_Type = IpAddress
_AtmNteHostMask_Object = MibTableColumn
atmNteHostMask = _AtmNteHostMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 3),
    _AtmNteHostMask_Type()
)
atmNteHostMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostMask.setStatus("current")
_AtmNteHostAtmIfIndex_Type = Integer32
_AtmNteHostAtmIfIndex_Object = MibTableColumn
atmNteHostAtmIfIndex = _AtmNteHostAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 4),
    _AtmNteHostAtmIfIndex_Type()
)
atmNteHostAtmIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostAtmIfIndex.setStatus("current")
_AtmNteHostVpi_Type = Integer32
_AtmNteHostVpi_Object = MibTableColumn
atmNteHostVpi = _AtmNteHostVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 5),
    _AtmNteHostVpi_Type()
)
atmNteHostVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostVpi.setStatus("current")
_AtmNteHostVci_Type = Integer32
_AtmNteHostVci_Object = MibTableColumn
atmNteHostVci = _AtmNteHostVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 6),
    _AtmNteHostVci_Type()
)
atmNteHostVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostVci.setStatus("current")
_AtmNteHostRowStatus_Type = RowStatus
_AtmNteHostRowStatus_Object = MibTableColumn
atmNteHostRowStatus = _AtmNteHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 7),
    _AtmNteHostRowStatus_Type()
)
atmNteHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostRowStatus.setStatus("current")
_AtmNteHostRdnVpi_Type = Integer32
_AtmNteHostRdnVpi_Object = MibTableColumn
atmNteHostRdnVpi = _AtmNteHostRdnVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 8),
    _AtmNteHostRdnVpi_Type()
)
atmNteHostRdnVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostRdnVpi.setStatus("current")
_AtmNteHostRdnVci_Type = Integer32
_AtmNteHostRdnVci_Object = MibTableColumn
atmNteHostRdnVci = _AtmNteHostRdnVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 11, 1, 9),
    _AtmNteHostRdnVci_Type()
)
atmNteHostRdnVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmNteHostRdnVci.setStatus("current")


class _AtmNteShaperMode_Type(Integer32):
    """Custom type atmNteShaperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("group", 2),
          ("aggregate", 3),
          ("vpInbandMng", 4))
    )


_AtmNteShaperMode_Type.__name__ = "Integer32"
_AtmNteShaperMode_Object = MibScalar
atmNteShaperMode = _AtmNteShaperMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 12),
    _AtmNteShaperMode_Type()
)
atmNteShaperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteShaperMode.setStatus("current")
_AtmNteOutputRate_Type = Integer32
_AtmNteOutputRate_Object = MibScalar
atmNteOutputRate = _AtmNteOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 13),
    _AtmNteOutputRate_Type()
)
atmNteOutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteOutputRate.setStatus("current")


class _AtmNteTosMode_Type(Integer32):
    """Custom type atmNteTosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_AtmNteTosMode_Type.__name__ = "Integer32"
_AtmNteTosMode_Object = MibScalar
atmNteTosMode = _AtmNteTosMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 14),
    _AtmNteTosMode_Type()
)
atmNteTosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteTosMode.setStatus("current")


class _AtmNteTosMask_Type(OctetString):
    """Custom type atmNteTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AtmNteTosMask_Type.__name__ = "OctetString"
_AtmNteTosMask_Object = MibScalar
atmNteTosMask = _AtmNteTosMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 15),
    _AtmNteTosMask_Type()
)
atmNteTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteTosMask.setStatus("current")


class _AtmNteTosHighPriority_Type(OctetString):
    """Custom type atmNteTosHighPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AtmNteTosHighPriority_Type.__name__ = "OctetString"
_AtmNteTosHighPriority_Object = MibScalar
atmNteTosHighPriority = _AtmNteTosHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 16),
    _AtmNteTosHighPriority_Type()
)
atmNteTosHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteTosHighPriority.setStatus("current")


class _AtmNtePlugAndPlayActivity_Type(Integer32):
    """Custom type atmNtePlugAndPlayActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("offline", 2),
          ("online", 3))
    )


_AtmNtePlugAndPlayActivity_Type.__name__ = "Integer32"
_AtmNtePlugAndPlayActivity_Object = MibScalar
atmNtePlugAndPlayActivity = _AtmNtePlugAndPlayActivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 17),
    _AtmNtePlugAndPlayActivity_Type()
)
atmNtePlugAndPlayActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNtePlugAndPlayActivity.setStatus("current")


class _AtmNteSlotUsage_Type(Integer32):
    """Custom type atmNteSlotUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("user", 2),
          ("network", 3))
    )


_AtmNteSlotUsage_Type.__name__ = "Integer32"
_AtmNteSlotUsage_Object = MibScalar
atmNteSlotUsage = _AtmNteSlotUsage_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 18),
    _AtmNteSlotUsage_Type()
)
atmNteSlotUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteSlotUsage.setStatus("current")


class _AtmNteConnectionsMaxNumber_Type(Integer32):
    """Custom type atmNteConnectionsMaxNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("max1024", 2),
          ("max2048", 3))
    )


_AtmNteConnectionsMaxNumber_Type.__name__ = "Integer32"
_AtmNteConnectionsMaxNumber_Object = MibScalar
atmNteConnectionsMaxNumber = _AtmNteConnectionsMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 19),
    _AtmNteConnectionsMaxNumber_Type()
)
atmNteConnectionsMaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteConnectionsMaxNumber.setStatus("current")
_AtmNteDefaultVpi_Type = Integer32
_AtmNteDefaultVpi_Object = MibScalar
atmNteDefaultVpi = _AtmNteDefaultVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 20),
    _AtmNteDefaultVpi_Type()
)
atmNteDefaultVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteDefaultVpi.setStatus("current")
_AtmNteDefaultVci_Type = Integer32
_AtmNteDefaultVci_Object = MibScalar
atmNteDefaultVci = _AtmNteDefaultVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 21),
    _AtmNteDefaultVci_Type()
)
atmNteDefaultVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteDefaultVci.setStatus("current")


class _AtmNteReservedVpi_Type(Integer32):
    """Custom type atmNteReservedVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmNteReservedVpi_Type.__name__ = "Integer32"
_AtmNteReservedVpi_Object = MibScalar
atmNteReservedVpi = _AtmNteReservedVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 22),
    _AtmNteReservedVpi_Type()
)
atmNteReservedVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteReservedVpi.setStatus("current")


class _AtmNteRdnManagement_Type(Integer32):
    """Custom type atmNteRdnManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_AtmNteRdnManagement_Type.__name__ = "Integer32"
_AtmNteRdnManagement_Object = MibScalar
atmNteRdnManagement = _AtmNteRdnManagement_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 23),
    _AtmNteRdnManagement_Type()
)
atmNteRdnManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteRdnManagement.setStatus("current")
_AtmNtePlugAndPlayIfIndex_Type = InterfaceIndex
_AtmNtePlugAndPlayIfIndex_Object = MibScalar
atmNtePlugAndPlayIfIndex = _AtmNtePlugAndPlayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 24),
    _AtmNtePlugAndPlayIfIndex_Type()
)
atmNtePlugAndPlayIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNtePlugAndPlayIfIndex.setStatus("current")
_AtmNteLoopbackTimeout_Type = Integer32
_AtmNteLoopbackTimeout_Object = MibScalar
atmNteLoopbackTimeout = _AtmNteLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 25),
    _AtmNteLoopbackTimeout_Type()
)
atmNteLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteLoopbackTimeout.setStatus("current")
_AtmNteOamTable_Object = MibTable
atmNteOamTable = _AtmNteOamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 26)
)
if mibBuilder.loadTexts:
    atmNteOamTable.setStatus("current")
_AtmNteOamEntry_Object = MibTableRow
atmNteOamEntry = _AtmNteOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 26, 1)
)
atmNteOamEntry.setIndexNames(
    (0, "ACE202-MIB", "atmNteOamMode"),
    (0, "ACE202-MIB", "atmNteOamCellType"),
    (0, "ACE202-MIB", "atmNteOamLevel"),
)
if mibBuilder.loadTexts:
    atmNteOamEntry.setStatus("current")


class _AtmNteOamMode_Type(Integer32):
    """Custom type atmNteOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("endToEnd", 1)
    )


_AtmNteOamMode_Type.__name__ = "Integer32"
_AtmNteOamMode_Object = MibTableColumn
atmNteOamMode = _AtmNteOamMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 26, 1, 1),
    _AtmNteOamMode_Type()
)
atmNteOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteOamMode.setStatus("current")


class _AtmNteOamCellType_Type(Integer32):
    """Custom type atmNteOamCellType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aisAndRdi", 1),
          ("loopback", 2))
    )


_AtmNteOamCellType_Type.__name__ = "Integer32"
_AtmNteOamCellType_Object = MibTableColumn
atmNteOamCellType = _AtmNteOamCellType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 26, 1, 2),
    _AtmNteOamCellType_Type()
)
atmNteOamCellType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteOamCellType.setStatus("current")


class _AtmNteOamLevel_Type(Integer32):
    """Custom type atmNteOamLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("f5", 3)
    )


_AtmNteOamLevel_Type.__name__ = "Integer32"
_AtmNteOamLevel_Object = MibTableColumn
atmNteOamLevel = _AtmNteOamLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 26, 1, 3),
    _AtmNteOamLevel_Type()
)
atmNteOamLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteOamLevel.setStatus("current")


class _AtmNteOamEnable_Type(Integer32):
    """Custom type atmNteOamEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_AtmNteOamEnable_Type.__name__ = "Integer32"
_AtmNteOamEnable_Object = MibTableColumn
atmNteOamEnable = _AtmNteOamEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 1, 26, 1, 4),
    _AtmNteOamEnable_Type()
)
atmNteOamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteOamEnable.setStatus("current")
_AtmNteSysInfo_ObjectIdentity = ObjectIdentity
atmNteSysInfo = _AtmNteSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2)
)
_AtmNteIdTable_Object = MibTable
atmNteIdTable = _AtmNteIdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmNteIdTable.setStatus("current")
_AtmNteIdEntry_Object = MibTableRow
atmNteIdEntry = _AtmNteIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 1, 1)
)
atmNteIdEntry.setIndexNames(
    (0, "ACE202-MIB", "atmNteIdIndex"),
)
if mibBuilder.loadTexts:
    atmNteIdEntry.setStatus("current")
_AtmNteIdIndex_Type = Integer32
_AtmNteIdIndex_Object = MibTableColumn
atmNteIdIndex = _AtmNteIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 1, 1, 1),
    _AtmNteIdIndex_Type()
)
atmNteIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteIdIndex.setStatus("current")
_AtmNteUnitId_Type = Integer32
_AtmNteUnitId_Object = MibTableColumn
atmNteUnitId = _AtmNteUnitId_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 1, 1, 2),
    _AtmNteUnitId_Type()
)
atmNteUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteUnitId.setStatus("current")
_AtmNteUnitVersion_Type = DisplayString
_AtmNteUnitVersion_Object = MibTableColumn
atmNteUnitVersion = _AtmNteUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 1, 1, 3),
    _AtmNteUnitVersion_Type()
)
atmNteUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteUnitVersion.setStatus("current")


class _AtmNteCardType_Type(Integer32):
    """Custom type atmNteCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              73,
              74,
              76,
              77,
              78,
              79,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("sc13mR155", 2),
          ("st13sR155", 3),
          ("st13lR155", 4),
          ("utpR155", 5),
          ("cxBncR155", 6),
          ("e3", 7),
          ("t3", 8),
          ("e1", 9),
          ("e1Ltu", 10),
          ("fc13lR155", 11),
          ("fc13lhR155", 12),
          ("fc15lhR155", 13),
          ("fc13lE3", 14),
          ("fc13lhE3", 15),
          ("fc15lhE3", 16),
          ("fc13lT3", 17),
          ("fc13lhT3", 18),
          ("fc15lhT3", 19),
          ("t1", 20),
          ("eth", 21),
          ("ethE1CesBnc", 22),
          ("ethE1CesRj45", 23),
          ("ethT1CesRj45", 24),
          ("e1CesRj45", 25),
          ("e1CesBnc", 26),
          ("t1CesRj45", 27),
          ("e14Ces", 28),
          ("e14CesRj45", 29),
          ("t14CesRj45", 30),
          ("hdlc4port", 31),
          ("hdlcE14CesBnc", 32),
          ("hdlcE14CesRj45", 33),
          ("hdlcT14CesRj45", 34),
          ("e1Rj45", 35),
          ("e1Bnc", 36),
          ("ethE14CesBnc", 37),
          ("ethE14CesRj45", 38),
          ("ethT14CesRj45", 39),
          ("hdlc1portHssi", 40),
          ("hdlcHssiE14CesBnc", 41),
          ("hdlcHssiE14CesRj45", 42),
          ("hdlcHssiT14CesRj45", 43),
          ("e14ImaRj45", 44),
          ("e14ImaBnc", 45),
          ("t14ImaRj45", 46),
          ("ethE3CesBnc", 47),
          ("ethT3CesBnc", 48),
          ("smSf1R155", 49),
          ("smSf2R155", 50),
          ("sc13sR155", 51),
          ("sc13lR155", 52),
          ("utp25", 53),
          ("sc13lhR155", 54),
          ("sc15lhR155", 55),
          ("sc13ljR155", 56),
          ("sc13lhjR155", 57),
          ("sc15lhjR155", 58),
          ("e18Ces", 59),
          ("e18CesRj45", 60),
          ("t18CesRj45", 61),
          ("sc13mR622", 62),
          ("sc13lR622", 73),
          ("sc13lhR622", 74),
          ("fr4Port", 76),
          ("t3j", 77),
          ("fr1Port", 78),
          ("hdlc1Port", 79),
          ("empty", 255))
    )


_AtmNteCardType_Type.__name__ = "Integer32"
_AtmNteCardType_Object = MibTableColumn
atmNteCardType = _AtmNteCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 1, 1, 4),
    _AtmNteCardType_Type()
)
atmNteCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteCardType.setStatus("current")
_AtmSysPSunits_Type = Integer32
_AtmSysPSunits_Object = MibScalar
atmSysPSunits = _AtmSysPSunits_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 2),
    _AtmSysPSunits_Type()
)
atmSysPSunits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysPSunits.setStatus("current")


class _AtmSysPSunitsInUse_Type(Integer32):
    """Custom type atmSysPSunitsInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ps1", 2),
          ("ps2", 3))
    )


_AtmSysPSunitsInUse_Type.__name__ = "Integer32"
_AtmSysPSunitsInUse_Object = MibScalar
atmSysPSunitsInUse = _AtmSysPSunitsInUse_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 3),
    _AtmSysPSunitsInUse_Type()
)
atmSysPSunitsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysPSunitsInUse.setStatus("current")
_AtmSysFanUnits_Type = Integer32
_AtmSysFanUnits_Object = MibScalar
atmSysFanUnits = _AtmSysFanUnits_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 4),
    _AtmSysFanUnits_Type()
)
atmSysFanUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysFanUnits.setStatus("current")
_AtmSysNetPrts_Type = Integer32
_AtmSysNetPrts_Object = MibScalar
atmSysNetPrts = _AtmSysNetPrts_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 5),
    _AtmSysNetPrts_Type()
)
atmSysNetPrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysNetPrts.setStatus("current")


class _AtmSysNetPrtInUse_Type(Integer32):
    """Custom type atmSysNetPrtInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trunk1", 2),
          ("trunk2", 3))
    )


_AtmSysNetPrtInUse_Type.__name__ = "Integer32"
_AtmSysNetPrtInUse_Object = MibScalar
atmSysNetPrtInUse = _AtmSysNetPrtInUse_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 6),
    _AtmSysNetPrtInUse_Type()
)
atmSysNetPrtInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysNetPrtInUse.setStatus("current")


class _AtmNteBridgingMode_Type(Integer32):
    """Custom type atmNteBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessOnly", 1),
          ("accessAndSwitching", 2))
    )


_AtmNteBridgingMode_Type.__name__ = "Integer32"
_AtmNteBridgingMode_Object = MibScalar
atmNteBridgingMode = _AtmNteBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 7),
    _AtmNteBridgingMode_Type()
)
atmNteBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmNteBridgingMode.setStatus("current")
_AtmSysStats_ObjectIdentity = ObjectIdentity
atmSysStats = _AtmSysStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 8)
)
_AtmSysCurrentCdc_Type = Gauge32
_AtmSysCurrentCdc_Object = MibScalar
atmSysCurrentCdc = _AtmSysCurrentCdc_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 8, 1),
    _AtmSysCurrentCdc_Type()
)
atmSysCurrentCdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysCurrentCdc.setStatus("current")
_AtmSysIntervalTable_Object = MibTable
atmSysIntervalTable = _AtmSysIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    atmSysIntervalTable.setStatus("current")
_AtmSysIntervalEntry_Object = MibTableRow
atmSysIntervalEntry = _AtmSysIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 8, 2, 1)
)
atmSysIntervalEntry.setIndexNames(
    (0, "ACE202-MIB", "atmSysIntervalNumber"),
)
if mibBuilder.loadTexts:
    atmSysIntervalEntry.setStatus("current")


class _AtmSysIntervalNumber_Type(Integer32):
    """Custom type atmSysIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmSysIntervalNumber_Type.__name__ = "Integer32"
_AtmSysIntervalNumber_Object = MibTableColumn
atmSysIntervalNumber = _AtmSysIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 8, 2, 1, 1),
    _AtmSysIntervalNumber_Type()
)
atmSysIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysIntervalNumber.setStatus("current")
_AtmSysIntervalCdc_Type = Gauge32
_AtmSysIntervalCdc_Object = MibTableColumn
atmSysIntervalCdc = _AtmSysIntervalCdc_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 8, 2, 1, 2),
    _AtmSysIntervalCdc_Type()
)
atmSysIntervalCdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSysIntervalCdc.setStatus("current")


class _AtmNteEventType_Type(Integer32):
    """Custom type atmNteEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("ps1NotActive", 3),
          ("ps1Active", 4),
          ("ps2NotActive", 5),
          ("ps2Active", 6),
          ("heatAlarmOff", 7),
          ("heatAlarmOn", 8),
          ("inputAlarm1Off", 9),
          ("inputAlarm1On", 10),
          ("inputAlarm2Off", 11),
          ("inputAlarm2On", 12),
          ("inputAlarm3Off", 13),
          ("inputAlarm3On", 14),
          ("inputAlarm4Off", 15),
          ("inputAlarm4On", 16),
          ("fan1Ok", 17),
          ("fan1Fail", 18),
          ("fan2Ok", 19),
          ("fan2Fail", 20),
          ("invalidLogin", 21),
          ("validLogin", 22),
          ("powerFailure", 23))
    )


_AtmNteEventType_Type.__name__ = "Integer32"
_AtmNteEventType_Object = MibScalar
atmNteEventType = _AtmNteEventType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 9),
    _AtmNteEventType_Type()
)
atmNteEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteEventType.setStatus("current")


class _AtmNteIntervalMaxNumber_Type(Integer32):
    """Custom type atmNteIntervalMaxNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmNteIntervalMaxNumber_Type.__name__ = "Integer32"
_AtmNteIntervalMaxNumber_Object = MibScalar
atmNteIntervalMaxNumber = _AtmNteIntervalMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 10),
    _AtmNteIntervalMaxNumber_Type()
)
atmNteIntervalMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteIntervalMaxNumber.setStatus("current")


class _AtmNteAlarmType_Type(Integer32):
    """Custom type atmNteAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("ais", 2),
          ("rdi", 3),
          ("continuityLoss", 4),
          ("loopback", 5))
    )


_AtmNteAlarmType_Type.__name__ = "Integer32"
_AtmNteAlarmType_Object = MibScalar
atmNteAlarmType = _AtmNteAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 11),
    _AtmNteAlarmType_Type()
)
atmNteAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteAlarmType.setStatus("current")


class _AtmNteLevel_Type(Integer32):
    """Custom type atmNteLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vp", 2),
          ("vc", 3))
    )


_AtmNteLevel_Type.__name__ = "Integer32"
_AtmNteLevel_Object = MibScalar
atmNteLevel = _AtmNteLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 12),
    _AtmNteLevel_Type()
)
atmNteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteLevel.setStatus("current")
_AtmNteConnectionsNumber_Type = Integer32
_AtmNteConnectionsNumber_Object = MibScalar
atmNteConnectionsNumber = _AtmNteConnectionsNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 1, 2, 13),
    _AtmNteConnectionsNumber_Type()
)
atmNteConnectionsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteConnectionsNumber.setStatus("current")
_AtmNtePrt_ObjectIdentity = ObjectIdentity
atmNtePrt = _AtmNtePrt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2)
)
_AtmNtePrtConfig_ObjectIdentity = ObjectIdentity
atmNtePrtConfig = _AtmNtePrtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1)
)
_AtmNteConfIfTable_Object = MibTable
atmNteConfIfTable = _AtmNteConfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmNteConfIfTable.setStatus("current")
_AtmNteConfIfEntry_Object = MibTableRow
atmNteConfIfEntry = _AtmNteConfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1)
)
atmNteConfIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmNteConfIfEntry.setStatus("current")


class _AtmConfIfTransmitClk_Type(Integer32):
    """Custom type atmConfIfTransmitClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("external", 3),
          ("loopback", 4),
          ("adaptive", 5))
    )


_AtmConfIfTransmitClk_Type.__name__ = "Integer32"
_AtmConfIfTransmitClk_Object = MibTableColumn
atmConfIfTransmitClk = _AtmConfIfTransmitClk_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 1),
    _AtmConfIfTransmitClk_Type()
)
atmConfIfTransmitClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfTransmitClk.setStatus("current")


class _AtmConfIfLoopback_Type(Integer32):
    """Custom type atmConfIfLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("external", 3),
          ("disable", 4))
    )


_AtmConfIfLoopback_Type.__name__ = "Integer32"
_AtmConfIfLoopback_Object = MibTableColumn
atmConfIfLoopback = _AtmConfIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 2),
    _AtmConfIfLoopback_Type()
)
atmConfIfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfLoopback.setStatus("current")


class _AtmConfIfFrameType_Type(Integer32):
    """Custom type atmConfIfFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sonet", 2),
          ("sdh", 3),
          ("direct", 4),
          ("plcpInternal", 5),
          ("plcpExternal", 6),
          ("e3", 7),
          ("ethCrcTrans", 8),
          ("ethCrcNotTrans", 9),
          ("directNoScrmbling", 10),
          ("plcpInternalNoScrmbling", 11),
          ("plcpExternalNoScrmbling", 12))
    )


_AtmConfIfFrameType_Type.__name__ = "Integer32"
_AtmConfIfFrameType_Object = MibTableColumn
atmConfIfFrameType = _AtmConfIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 3),
    _AtmConfIfFrameType_Type()
)
atmConfIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfFrameType.setStatus("current")


class _AtmConfIfCardType_Type(Integer32):
    """Custom type atmConfIfCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("sc13m-155", 2),
          ("st13s-155", 3),
          ("st13l-155", 4),
          ("utp-155", 5),
          ("cx-bnc-155", 6),
          ("e3", 7),
          ("t3", 8),
          ("e1", 9),
          ("e1-ltu", 10),
          ("fc13l-155", 11),
          ("fc13lh-155", 12),
          ("fc15lh-155", 13),
          ("fc13l-e3", 14),
          ("fc13lh-e3", 15),
          ("fc15lh-e3", 16),
          ("fc13l-t3", 17),
          ("fc13lh-t3", 18),
          ("fc15lh-t3", 19))
    )


_AtmConfIfCardType_Type.__name__ = "Integer32"
_AtmConfIfCardType_Object = MibTableColumn
atmConfIfCardType = _AtmConfIfCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 4),
    _AtmConfIfCardType_Type()
)
atmConfIfCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfIfCardType.setStatus("deprecated")


class _AtmConfAtmIfVpiVciLimit_Type(Integer32):
    """Custom type atmConfAtmIfVpiVciLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits15", 2),
          ("bits17", 3))
    )


_AtmConfAtmIfVpiVciLimit_Type.__name__ = "Integer32"
_AtmConfAtmIfVpiVciLimit_Object = MibTableColumn
atmConfAtmIfVpiVciLimit = _AtmConfAtmIfVpiVciLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 5),
    _AtmConfAtmIfVpiVciLimit_Type()
)
atmConfAtmIfVpiVciLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfAtmIfVpiVciLimit.setStatus("current")


class _AtmConfIfHwFeatures_Type(Integer32):
    """Custom type atmConfIfHwFeatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtmConfIfHwFeatures_Type.__name__ = "Integer32"
_AtmConfIfHwFeatures_Object = MibTableColumn
atmConfIfHwFeatures = _AtmConfIfHwFeatures_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 6),
    _AtmConfIfHwFeatures_Type()
)
atmConfIfHwFeatures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfHwFeatures.setStatus("current")
_AtmConfIfOutputRate_Type = Integer32
_AtmConfIfOutputRate_Object = MibTableColumn
atmConfIfOutputRate = _AtmConfIfOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 7),
    _AtmConfIfOutputRate_Type()
)
atmConfIfOutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfOutputRate.setStatus("current")
_AtmConfIfInputRate_Type = Integer32
_AtmConfIfInputRate_Object = MibTableColumn
atmConfIfInputRate = _AtmConfIfInputRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 8),
    _AtmConfIfInputRate_Type()
)
atmConfIfInputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfIfInputRate.setStatus("current")


class _AtmConfAlarmForwarding_Type(Integer32):
    """Custom type atmConfAlarmForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_AtmConfAlarmForwarding_Type.__name__ = "Integer32"
_AtmConfAlarmForwarding_Object = MibTableColumn
atmConfAlarmForwarding = _AtmConfAlarmForwarding_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 1, 1, 9),
    _AtmConfAlarmForwarding_Type()
)
atmConfAlarmForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfAlarmForwarding.setStatus("current")
_AtmNteAlarmIfTable_Object = MibTable
atmNteAlarmIfTable = _AtmNteAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    atmNteAlarmIfTable.setStatus("current")
_AtmNteAlarmIfEntry_Object = MibTableRow
atmNteAlarmIfEntry = _AtmNteAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1)
)
atmNteAlarmIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmNteAlarmIfEntry.setStatus("current")
_AtmInterfaceActiveAlarms_Type = Integer32
_AtmInterfaceActiveAlarms_Object = MibTableColumn
atmInterfaceActiveAlarms = _AtmInterfaceActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 1),
    _AtmInterfaceActiveAlarms_Type()
)
atmInterfaceActiveAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceActiveAlarms.setStatus("current")
_AtmThresholdSectionBIP_Type = Integer32
_AtmThresholdSectionBIP_Object = MibTableColumn
atmThresholdSectionBIP = _AtmThresholdSectionBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 2),
    _AtmThresholdSectionBIP_Type()
)
atmThresholdSectionBIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdSectionBIP.setStatus("current")
_AtmThresholdLineBIP_Type = Integer32
_AtmThresholdLineBIP_Object = MibTableColumn
atmThresholdLineBIP = _AtmThresholdLineBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 3),
    _AtmThresholdLineBIP_Type()
)
atmThresholdLineBIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdLineBIP.setStatus("current")
_AtmThresholdLineFEBE_Type = Integer32
_AtmThresholdLineFEBE_Object = MibTableColumn
atmThresholdLineFEBE = _AtmThresholdLineFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 4),
    _AtmThresholdLineFEBE_Type()
)
atmThresholdLineFEBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdLineFEBE.setStatus("current")
_AtmThresholdPathBIP_Type = Integer32
_AtmThresholdPathBIP_Object = MibTableColumn
atmThresholdPathBIP = _AtmThresholdPathBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 5),
    _AtmThresholdPathBIP_Type()
)
atmThresholdPathBIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdPathBIP.setStatus("current")
_AtmThresholdPathFEBE_Type = Integer32
_AtmThresholdPathFEBE_Object = MibTableColumn
atmThresholdPathFEBE = _AtmThresholdPathFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 6),
    _AtmThresholdPathFEBE_Type()
)
atmThresholdPathFEBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdPathFEBE.setStatus("current")
_AtmThresholdErroredCells_Type = Integer32
_AtmThresholdErroredCells_Object = MibTableColumn
atmThresholdErroredCells = _AtmThresholdErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 7),
    _AtmThresholdErroredCells_Type()
)
atmThresholdErroredCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdErroredCells.setStatus("current")
_AtmThresholdLostCells_Type = Integer32
_AtmThresholdLostCells_Object = MibTableColumn
atmThresholdLostCells = _AtmThresholdLostCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 8),
    _AtmThresholdLostCells_Type()
)
atmThresholdLostCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdLostCells.setStatus("current")
_AtmThresholdMisinsertedCells_Type = Integer32
_AtmThresholdMisinsertedCells_Object = MibTableColumn
atmThresholdMisinsertedCells = _AtmThresholdMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 9),
    _AtmThresholdMisinsertedCells_Type()
)
atmThresholdMisinsertedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmThresholdMisinsertedCells.setStatus("current")


class _AtmInterfaceAlarmStatus_Type(Integer32):
    """Custom type atmInterfaceAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AtmInterfaceAlarmStatus_Type.__name__ = "Integer32"
_AtmInterfaceAlarmStatus_Object = MibTableColumn
atmInterfaceAlarmStatus = _AtmInterfaceAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 10),
    _AtmInterfaceAlarmStatus_Type()
)
atmInterfaceAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceAlarmStatus.setStatus("current")
_AtmInterfaceMaskAlarms_Type = Integer32
_AtmInterfaceMaskAlarms_Object = MibTableColumn
atmInterfaceMaskAlarms = _AtmInterfaceMaskAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 2, 1, 11),
    _AtmInterfaceMaskAlarms_Type()
)
atmInterfaceMaskAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaskAlarms.setStatus("current")
_AtmNteConfVpTable_Object = MibTable
atmNteConfVpTable = _AtmNteConfVpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmNteConfVpTable.setStatus("current")
_AtmNteConfVpEntry_Object = MibTableRow
atmNteConfVpEntry = _AtmNteConfVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1)
)
atmNteConfVpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmNteConfVpEntry.setStatus("current")


class _AtmConfVpPolicing_Type(Integer32):
    """Custom type atmConfVpPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("police", 2),
          ("monitor", 3),
          ("shaping", 4),
          ("policingAndShaping", 5))
    )


_AtmConfVpPolicing_Type.__name__ = "Integer32"
_AtmConfVpPolicing_Object = MibTableColumn
atmConfVpPolicing = _AtmConfVpPolicing_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 1),
    _AtmConfVpPolicing_Type()
)
atmConfVpPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpPolicing.setStatus("current")


class _AtmConfVpCCAdminStatus_Type(Integer32):
    """Custom type atmConfVpCCAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("source", 4),
          ("sink", 5),
          ("listenToActivationCells", 6),
          ("originateActivationCells", 7))
    )


_AtmConfVpCCAdminStatus_Type.__name__ = "Integer32"
_AtmConfVpCCAdminStatus_Object = MibTableColumn
atmConfVpCCAdminStatus = _AtmConfVpCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 2),
    _AtmConfVpCCAdminStatus_Type()
)
atmConfVpCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpCCAdminStatus.setStatus("current")


class _AtmConfVpLoopbackAdminStatus_Type(Integer32):
    """Custom type atmConfVpLoopbackAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("llid", 4),
          ("segment", 5),
          ("endToEnd", 6),
          ("segmentLlid", 7),
          ("endToEndLlid", 8))
    )


_AtmConfVpLoopbackAdminStatus_Type.__name__ = "Integer32"
_AtmConfVpLoopbackAdminStatus_Object = MibTableColumn
atmConfVpLoopbackAdminStatus = _AtmConfVpLoopbackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 3),
    _AtmConfVpLoopbackAdminStatus_Type()
)
atmConfVpLoopbackAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackAdminStatus.setStatus("current")


class _AtmConfVpLoopbackSinkAddress_Type(OctetString):
    """Custom type atmConfVpLoopbackSinkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmConfVpLoopbackSinkAddress_Type.__name__ = "OctetString"
_AtmConfVpLoopbackSinkAddress_Object = MibTableColumn
atmConfVpLoopbackSinkAddress = _AtmConfVpLoopbackSinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 4),
    _AtmConfVpLoopbackSinkAddress_Type()
)
atmConfVpLoopbackSinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackSinkAddress.setStatus("current")
_AtmConfVpCongestionControl_Type = OctetString
_AtmConfVpCongestionControl_Object = MibTableColumn
atmConfVpCongestionControl = _AtmConfVpCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 5),
    _AtmConfVpCongestionControl_Type()
)
atmConfVpCongestionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpCongestionControl.setStatus("current")


class _AtmConfVpCCDirection_Type(Integer32):
    """Custom type atmConfVpCCDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("source", 4),
          ("sink", 5))
    )


_AtmConfVpCCDirection_Type.__name__ = "Integer32"
_AtmConfVpCCDirection_Object = MibTableColumn
atmConfVpCCDirection = _AtmConfVpCCDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 6),
    _AtmConfVpCCDirection_Type()
)
atmConfVpCCDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpCCDirection.setStatus("current")
_AtmConfVpCreationTime_Type = DateAndTime
_AtmConfVpCreationTime_Object = MibTableColumn
atmConfVpCreationTime = _AtmConfVpCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 7),
    _AtmConfVpCreationTime_Type()
)
atmConfVpCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVpCreationTime.setStatus("current")


class _AtmConfVpOamSupport_Type(Integer32):
    """Custom type atmConfVpOamSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("segmentTermination", 2),
          ("endToEndTermination", 3))
    )


_AtmConfVpOamSupport_Type.__name__ = "Integer32"
_AtmConfVpOamSupport_Object = MibTableColumn
atmConfVpOamSupport = _AtmConfVpOamSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 8),
    _AtmConfVpOamSupport_Type()
)
atmConfVpOamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpOamSupport.setStatus("current")


class _AtmConfVpCCOperStatus_Type(Integer32):
    """Custom type atmConfVpCCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("source", 4),
          ("sink", 5),
          ("both", 8),
          ("timeout", 9),
          ("denied", 10),
          ("conflict", 11),
          ("manual", 12))
    )


_AtmConfVpCCOperStatus_Type.__name__ = "Integer32"
_AtmConfVpCCOperStatus_Object = MibTableColumn
atmConfVpCCOperStatus = _AtmConfVpCCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 9),
    _AtmConfVpCCOperStatus_Type()
)
atmConfVpCCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVpCCOperStatus.setStatus("current")


class _AtmConfVpLoopbackTraffic_Type(Integer32):
    """Custom type atmConfVpLoopbackTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AtmConfVpLoopbackTraffic_Type.__name__ = "Integer32"
_AtmConfVpLoopbackTraffic_Object = MibTableColumn
atmConfVpLoopbackTraffic = _AtmConfVpLoopbackTraffic_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 10),
    _AtmConfVpLoopbackTraffic_Type()
)
atmConfVpLoopbackTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackTraffic.setStatus("current")


class _AtmConfVpLoopbackFailureInd_Type(Integer32):
    """Custom type atmConfVpLoopbackFailureInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("segmentAis", 3),
          ("segmentRdi", 4),
          ("segmentAisAndRdi", 5),
          ("endToEndAis", 6),
          ("endToEndRdi", 7),
          ("endToEndAisAndRdi", 8))
    )


_AtmConfVpLoopbackFailureInd_Type.__name__ = "Integer32"
_AtmConfVpLoopbackFailureInd_Object = MibTableColumn
atmConfVpLoopbackFailureInd = _AtmConfVpLoopbackFailureInd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 11),
    _AtmConfVpLoopbackFailureInd_Type()
)
atmConfVpLoopbackFailureInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackFailureInd.setStatus("current")
_AtmConfVpLoopbackFailureThreshold_Type = Integer32
_AtmConfVpLoopbackFailureThreshold_Object = MibTableColumn
atmConfVpLoopbackFailureThreshold = _AtmConfVpLoopbackFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 12),
    _AtmConfVpLoopbackFailureThreshold_Type()
)
atmConfVpLoopbackFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpLoopbackFailureThreshold.setStatus("current")


class _AtmConfVpOamDirection_Type(Integer32):
    """Custom type atmConfVpOamDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("downStream", 2),
          ("upStream", 3))
    )


_AtmConfVpOamDirection_Type.__name__ = "Integer32"
_AtmConfVpOamDirection_Object = MibTableColumn
atmConfVpOamDirection = _AtmConfVpOamDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 3, 1, 13),
    _AtmConfVpOamDirection_Type()
)
atmConfVpOamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVpOamDirection.setStatus("current")
_AtmNteConfVcTable_Object = MibTable
atmNteConfVcTable = _AtmNteConfVcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    atmNteConfVcTable.setStatus("current")
_AtmNteConfVcEntry_Object = MibTableRow
atmNteConfVcEntry = _AtmNteConfVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1)
)
atmNteConfVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmNteConfVcEntry.setStatus("current")


class _AtmConfVcPolicing_Type(Integer32):
    """Custom type atmConfVcPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("police", 2),
          ("monitor", 3),
          ("shaping", 4),
          ("policingAndShaping", 5),
          ("notApplicable", 255))
    )


_AtmConfVcPolicing_Type.__name__ = "Integer32"
_AtmConfVcPolicing_Object = MibTableColumn
atmConfVcPolicing = _AtmConfVcPolicing_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 1),
    _AtmConfVcPolicing_Type()
)
atmConfVcPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcPolicing.setStatus("current")


class _AtmConfVcCCAdminStatus_Type(Integer32):
    """Custom type atmConfVcCCAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("source", 4),
          ("sink", 5),
          ("listenToActivationCells", 6),
          ("originateActivationCells", 7))
    )


_AtmConfVcCCAdminStatus_Type.__name__ = "Integer32"
_AtmConfVcCCAdminStatus_Object = MibTableColumn
atmConfVcCCAdminStatus = _AtmConfVcCCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 2),
    _AtmConfVcCCAdminStatus_Type()
)
atmConfVcCCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCCAdminStatus.setStatus("current")


class _AtmConfVcLoopbackAdminStatus_Type(Integer32):
    """Custom type atmConfVcLoopbackAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("llid", 4),
          ("segment", 5),
          ("endToEnd", 6),
          ("segmentLlid", 7),
          ("endToEndLlid", 8))
    )


_AtmConfVcLoopbackAdminStatus_Type.__name__ = "Integer32"
_AtmConfVcLoopbackAdminStatus_Object = MibTableColumn
atmConfVcLoopbackAdminStatus = _AtmConfVcLoopbackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 3),
    _AtmConfVcLoopbackAdminStatus_Type()
)
atmConfVcLoopbackAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackAdminStatus.setStatus("current")


class _AtmConfVcLoopbackSinkAddress_Type(OctetString):
    """Custom type atmConfVcLoopbackSinkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 20),
    )


_AtmConfVcLoopbackSinkAddress_Type.__name__ = "OctetString"
_AtmConfVcLoopbackSinkAddress_Object = MibTableColumn
atmConfVcLoopbackSinkAddress = _AtmConfVcLoopbackSinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 4),
    _AtmConfVcLoopbackSinkAddress_Type()
)
atmConfVcLoopbackSinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackSinkAddress.setStatus("current")
_AtmConfVcCongestionControl_Type = OctetString
_AtmConfVcCongestionControl_Object = MibTableColumn
atmConfVcCongestionControl = _AtmConfVcCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 5),
    _AtmConfVcCongestionControl_Type()
)
atmConfVcCongestionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCongestionControl.setStatus("current")


class _AtmConfVcCCDirection_Type(Integer32):
    """Custom type atmConfVcCCDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("source", 4),
          ("sink", 5))
    )


_AtmConfVcCCDirection_Type.__name__ = "Integer32"
_AtmConfVcCCDirection_Object = MibTableColumn
atmConfVcCCDirection = _AtmConfVcCCDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 6),
    _AtmConfVcCCDirection_Type()
)
atmConfVcCCDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCCDirection.setStatus("current")
_AtmConfVcCreationTime_Type = DateAndTime
_AtmConfVcCreationTime_Object = MibTableColumn
atmConfVcCreationTime = _AtmConfVcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 7),
    _AtmConfVcCreationTime_Type()
)
atmConfVcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVcCreationTime.setStatus("current")


class _AtmConfVcOamSupport_Type(Integer32):
    """Custom type atmConfVcOamSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("segmentTermination", 2),
          ("endToEndTermination", 3))
    )


_AtmConfVcOamSupport_Type.__name__ = "Integer32"
_AtmConfVcOamSupport_Object = MibTableColumn
atmConfVcOamSupport = _AtmConfVcOamSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 8),
    _AtmConfVcOamSupport_Type()
)
atmConfVcOamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcOamSupport.setStatus("current")


class _AtmConfVcCCActivationCtrl_Type(Integer32):
    """Custom type atmConfVcCCActivationCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("activator", 2),
          ("listener", 3))
    )


_AtmConfVcCCActivationCtrl_Type.__name__ = "Integer32"
_AtmConfVcCCActivationCtrl_Object = MibTableColumn
atmConfVcCCActivationCtrl = _AtmConfVcCCActivationCtrl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 9),
    _AtmConfVcCCActivationCtrl_Type()
)
atmConfVcCCActivationCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcCCActivationCtrl.setStatus("current")


class _AtmConfVcCCOperStatus_Type(Integer32):
    """Custom type atmConfVcCCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("up", 2),
          ("down", 3),
          ("source", 4),
          ("sink", 5),
          ("both", 8),
          ("timeout", 9),
          ("denied", 10),
          ("conflict", 11),
          ("manual", 12))
    )


_AtmConfVcCCOperStatus_Type.__name__ = "Integer32"
_AtmConfVcCCOperStatus_Object = MibTableColumn
atmConfVcCCOperStatus = _AtmConfVcCCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 10),
    _AtmConfVcCCOperStatus_Type()
)
atmConfVcCCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConfVcCCOperStatus.setStatus("current")


class _AtmConfVcLoopbackTraffic_Type(Integer32):
    """Custom type atmConfVcLoopbackTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AtmConfVcLoopbackTraffic_Type.__name__ = "Integer32"
_AtmConfVcLoopbackTraffic_Object = MibTableColumn
atmConfVcLoopbackTraffic = _AtmConfVcLoopbackTraffic_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 11),
    _AtmConfVcLoopbackTraffic_Type()
)
atmConfVcLoopbackTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackTraffic.setStatus("current")


class _AtmConfVcLoopbackFailureInd_Type(Integer32):
    """Custom type atmConfVcLoopbackFailureInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("segmentAis", 3),
          ("segmentRdi", 4),
          ("segmentAisAndRdi", 5),
          ("endToEndAis", 6),
          ("endToEndRdi", 7),
          ("endToEndAisAndRdi", 8))
    )


_AtmConfVcLoopbackFailureInd_Type.__name__ = "Integer32"
_AtmConfVcLoopbackFailureInd_Object = MibTableColumn
atmConfVcLoopbackFailureInd = _AtmConfVcLoopbackFailureInd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 12),
    _AtmConfVcLoopbackFailureInd_Type()
)
atmConfVcLoopbackFailureInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackFailureInd.setStatus("current")
_AtmConfVcLoopbackFailureThreshold_Type = Integer32
_AtmConfVcLoopbackFailureThreshold_Object = MibTableColumn
atmConfVcLoopbackFailureThreshold = _AtmConfVcLoopbackFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 13),
    _AtmConfVcLoopbackFailureThreshold_Type()
)
atmConfVcLoopbackFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcLoopbackFailureThreshold.setStatus("current")


class _AtmConfVcOamDirection_Type(Integer32):
    """Custom type atmConfVcOamDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("downStream", 2),
          ("upStream", 3))
    )


_AtmConfVcOamDirection_Type.__name__ = "Integer32"
_AtmConfVcOamDirection_Object = MibTableColumn
atmConfVcOamDirection = _AtmConfVcOamDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 4, 1, 14),
    _AtmConfVcOamDirection_Type()
)
atmConfVcOamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmConfVcOamDirection.setStatus("current")
_AtmNteAlarmVpTable_Object = MibTable
atmNteAlarmVpTable = _AtmNteAlarmVpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    atmNteAlarmVpTable.setStatus("current")
_AtmNteAlarmVpEntry_Object = MibTableRow
atmNteAlarmVpEntry = _AtmNteAlarmVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5, 1)
)
atmNteAlarmVpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmNteVpAlarmVpi"),
)
if mibBuilder.loadTexts:
    atmNteAlarmVpEntry.setStatus("current")
_AtmNteVpAlarmVpi_Type = Integer32
_AtmNteVpAlarmVpi_Object = MibTableColumn
atmNteVpAlarmVpi = _AtmNteVpAlarmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5, 1, 1),
    _AtmNteVpAlarmVpi_Type()
)
atmNteVpAlarmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVpAlarmVpi.setStatus("current")
_AtmNteVpActiveAlarms_Type = Integer32
_AtmNteVpActiveAlarms_Object = MibTableColumn
atmNteVpActiveAlarms = _AtmNteVpActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 5, 1, 2),
    _AtmNteVpActiveAlarms_Type()
)
atmNteVpActiveAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVpActiveAlarms.setStatus("current")
_AtmNteAlarmVcTable_Object = MibTable
atmNteAlarmVcTable = _AtmNteAlarmVcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    atmNteAlarmVcTable.setStatus("current")
_AtmNteAlarmVcEntry_Object = MibTableRow
atmNteAlarmVcEntry = _AtmNteAlarmVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1)
)
atmNteAlarmVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ACE202-MIB", "atmNteVcAlarmVpi"),
    (0, "ACE202-MIB", "atmNteVcAlarmVci"),
)
if mibBuilder.loadTexts:
    atmNteAlarmVcEntry.setStatus("current")
_AtmNteVcAlarmVpi_Type = Integer32
_AtmNteVcAlarmVpi_Object = MibTableColumn
atmNteVcAlarmVpi = _AtmNteVcAlarmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1, 1),
    _AtmNteVcAlarmVpi_Type()
)
atmNteVcAlarmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVcAlarmVpi.setStatus("current")
_AtmNteVcAlarmVci_Type = Integer32
_AtmNteVcAlarmVci_Object = MibTableColumn
atmNteVcAlarmVci = _AtmNteVcAlarmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1, 2),
    _AtmNteVcAlarmVci_Type()
)
atmNteVcAlarmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVcAlarmVci.setStatus("current")
_AtmNteVcActiveAlarms_Type = Integer32
_AtmNteVcActiveAlarms_Object = MibTableColumn
atmNteVcActiveAlarms = _AtmNteVcActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 1, 6, 1, 3),
    _AtmNteVcActiveAlarms_Type()
)
atmNteVcActiveAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNteVcActiveAlarms.setStatus("current")
_AtmNteLoopback_ObjectIdentity = ObjectIdentity
atmNteLoopback = _AtmNteLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2)
)
_AtmLoopbackVpTable_Object = MibTable
atmLoopbackVpTable = _AtmLoopbackVpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmLoopbackVpTable.setStatus("current")
_AtmLoopbackVpEntry_Object = MibTableRow
atmLoopbackVpEntry = _AtmLoopbackVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1)
)
atmLoopbackVpEntry.setIndexNames(
    (0, "ACE202-MIB", "atmLoopbackVpIfIndex"),
    (0, "ACE202-MIB", "atmLoopbackVpVpi"),
)
if mibBuilder.loadTexts:
    atmLoopbackVpEntry.setStatus("current")
_AtmLoopbackVpIfIndex_Type = Integer32
_AtmLoopbackVpIfIndex_Object = MibTableColumn
atmLoopbackVpIfIndex = _AtmLoopbackVpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 1),
    _AtmLoopbackVpIfIndex_Type()
)
atmLoopbackVpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIfIndex.setStatus("current")
_AtmLoopbackVpVpi_Type = Integer32
_AtmLoopbackVpVpi_Object = MibTableColumn
atmLoopbackVpVpi = _AtmLoopbackVpVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 2),
    _AtmLoopbackVpVpi_Type()
)
atmLoopbackVpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpVpi.setStatus("current")


class _AtmLoopbackVpOperStatus_Type(Integer32):
    """Custom type atmLoopbackVpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noActive", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("endSuccessfully", 4))
    )


_AtmLoopbackVpOperStatus_Type.__name__ = "Integer32"
_AtmLoopbackVpOperStatus_Object = MibTableColumn
atmLoopbackVpOperStatus = _AtmLoopbackVpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 3),
    _AtmLoopbackVpOperStatus_Type()
)
atmLoopbackVpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpOperStatus.setStatus("current")
_AtmLoopbackVpCDV_Type = Integer32
_AtmLoopbackVpCDV_Object = MibTableColumn
atmLoopbackVpCDV = _AtmLoopbackVpCDV_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 4),
    _AtmLoopbackVpCDV_Type()
)
atmLoopbackVpCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpCDV.setStatus("current")
_AtmLoopbackVpAverageDelay_Type = Integer32
_AtmLoopbackVpAverageDelay_Object = MibTableColumn
atmLoopbackVpAverageDelay = _AtmLoopbackVpAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 5),
    _AtmLoopbackVpAverageDelay_Type()
)
atmLoopbackVpAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpAverageDelay.setStatus("current")
_AtmLoopbackVpMaxDelay_Type = Integer32
_AtmLoopbackVpMaxDelay_Object = MibTableColumn
atmLoopbackVpMaxDelay = _AtmLoopbackVpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 6),
    _AtmLoopbackVpMaxDelay_Type()
)
atmLoopbackVpMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpMaxDelay.setStatus("current")
_AtmLoopbackVpMinDelay_Type = Integer32
_AtmLoopbackVpMinDelay_Object = MibTableColumn
atmLoopbackVpMinDelay = _AtmLoopbackVpMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 7),
    _AtmLoopbackVpMinDelay_Type()
)
atmLoopbackVpMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpMinDelay.setStatus("current")
_AtmLoopbackVpErrSessions_Type = Integer32
_AtmLoopbackVpErrSessions_Object = MibTableColumn
atmLoopbackVpErrSessions = _AtmLoopbackVpErrSessions_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 1, 1, 8),
    _AtmLoopbackVpErrSessions_Type()
)
atmLoopbackVpErrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpErrSessions.setStatus("current")
_AtmLoopbackVcTable_Object = MibTable
atmLoopbackVcTable = _AtmLoopbackVcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    atmLoopbackVcTable.setStatus("current")
_AtmLoopbackVcEntry_Object = MibTableRow
atmLoopbackVcEntry = _AtmLoopbackVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1)
)
atmLoopbackVcEntry.setIndexNames(
    (0, "ACE202-MIB", "atmLoopbackVcIfIndex"),
    (0, "ACE202-MIB", "atmLoopbackVcVpi"),
    (0, "ACE202-MIB", "atmLoopbackVcVci"),
)
if mibBuilder.loadTexts:
    atmLoopbackVcEntry.setStatus("current")
_AtmLoopbackVcIfIndex_Type = Integer32
_AtmLoopbackVcIfIndex_Object = MibTableColumn
atmLoopbackVcIfIndex = _AtmLoopbackVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 1),
    _AtmLoopbackVcIfIndex_Type()
)
atmLoopbackVcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIfIndex.setStatus("current")
_AtmLoopbackVcVpi_Type = Integer32
_AtmLoopbackVcVpi_Object = MibTableColumn
atmLoopbackVcVpi = _AtmLoopbackVcVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 2),
    _AtmLoopbackVcVpi_Type()
)
atmLoopbackVcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcVpi.setStatus("current")
_AtmLoopbackVcVci_Type = Integer32
_AtmLoopbackVcVci_Object = MibTableColumn
atmLoopbackVcVci = _AtmLoopbackVcVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 3),
    _AtmLoopbackVcVci_Type()
)
atmLoopbackVcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcVci.setStatus("current")


class _AtmLoopbackVcOperStatus_Type(Integer32):
    """Custom type atmLoopbackVcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noActive", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("endSuccessfully", 4))
    )


_AtmLoopbackVcOperStatus_Type.__name__ = "Integer32"
_AtmLoopbackVcOperStatus_Object = MibTableColumn
atmLoopbackVcOperStatus = _AtmLoopbackVcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 4),
    _AtmLoopbackVcOperStatus_Type()
)
atmLoopbackVcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcOperStatus.setStatus("current")
_AtmLoopbackVcCDV_Type = Integer32
_AtmLoopbackVcCDV_Object = MibTableColumn
atmLoopbackVcCDV = _AtmLoopbackVcCDV_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 5),
    _AtmLoopbackVcCDV_Type()
)
atmLoopbackVcCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcCDV.setStatus("current")
_AtmLoopbackVcAverageDelay_Type = Integer32
_AtmLoopbackVcAverageDelay_Object = MibTableColumn
atmLoopbackVcAverageDelay = _AtmLoopbackVcAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 6),
    _AtmLoopbackVcAverageDelay_Type()
)
atmLoopbackVcAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcAverageDelay.setStatus("current")
_AtmLoopbackVcMaxDelay_Type = Integer32
_AtmLoopbackVcMaxDelay_Object = MibTableColumn
atmLoopbackVcMaxDelay = _AtmLoopbackVcMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 7),
    _AtmLoopbackVcMaxDelay_Type()
)
atmLoopbackVcMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcMaxDelay.setStatus("current")
_AtmLoopbackVcMinDelay_Type = Integer32
_AtmLoopbackVcMinDelay_Object = MibTableColumn
atmLoopbackVcMinDelay = _AtmLoopbackVcMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 8),
    _AtmLoopbackVcMinDelay_Type()
)
atmLoopbackVcMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcMinDelay.setStatus("current")
_AtmLoopbackVcErrSessions_Type = Integer32
_AtmLoopbackVcErrSessions_Object = MibTableColumn
atmLoopbackVcErrSessions = _AtmLoopbackVcErrSessions_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 2, 1, 9),
    _AtmLoopbackVcErrSessions_Type()
)
atmLoopbackVcErrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcErrSessions.setStatus("current")
_AtmLoopbackVpIvlTable_Object = MibTable
atmLoopbackVpIvlTable = _AtmLoopbackVpIvlTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    atmLoopbackVpIvlTable.setStatus("current")
_AtmLoopbackVpIvlEntry_Object = MibTableRow
atmLoopbackVpIvlEntry = _AtmLoopbackVpIvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1)
)
atmLoopbackVpIvlEntry.setIndexNames(
    (0, "ACE202-MIB", "atmLoopbackVpIvlIfIndex"),
    (0, "ACE202-MIB", "atmLoopbackVpIvlVpi"),
    (0, "ACE202-MIB", "atmLoopbackVpIvlIvl"),
)
if mibBuilder.loadTexts:
    atmLoopbackVpIvlEntry.setStatus("current")
_AtmLoopbackVpIvlIfIndex_Type = Integer32
_AtmLoopbackVpIvlIfIndex_Object = MibTableColumn
atmLoopbackVpIvlIfIndex = _AtmLoopbackVpIvlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 1),
    _AtmLoopbackVpIvlIfIndex_Type()
)
atmLoopbackVpIvlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlIfIndex.setStatus("current")
_AtmLoopbackVpIvlVpi_Type = Integer32
_AtmLoopbackVpIvlVpi_Object = MibTableColumn
atmLoopbackVpIvlVpi = _AtmLoopbackVpIvlVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 2),
    _AtmLoopbackVpIvlVpi_Type()
)
atmLoopbackVpIvlVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlVpi.setStatus("current")


class _AtmLoopbackVpIvlIvl_Type(Integer32):
    """Custom type atmLoopbackVpIvlIvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmLoopbackVpIvlIvl_Type.__name__ = "Integer32"
_AtmLoopbackVpIvlIvl_Object = MibTableColumn
atmLoopbackVpIvlIvl = _AtmLoopbackVpIvlIvl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 3),
    _AtmLoopbackVpIvlIvl_Type()
)
atmLoopbackVpIvlIvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlIvl.setStatus("current")


class _AtmLoopbackVpIvlOperStatus_Type(Integer32):
    """Custom type atmLoopbackVpIvlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noActive", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("endSuccessfully", 4))
    )


_AtmLoopbackVpIvlOperStatus_Type.__name__ = "Integer32"
_AtmLoopbackVpIvlOperStatus_Object = MibTableColumn
atmLoopbackVpIvlOperStatus = _AtmLoopbackVpIvlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 4),
    _AtmLoopbackVpIvlOperStatus_Type()
)
atmLoopbackVpIvlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlOperStatus.setStatus("current")
_AtmLoopbackVpIvlCDV_Type = Integer32
_AtmLoopbackVpIvlCDV_Object = MibTableColumn
atmLoopbackVpIvlCDV = _AtmLoopbackVpIvlCDV_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 5),
    _AtmLoopbackVpIvlCDV_Type()
)
atmLoopbackVpIvlCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlCDV.setStatus("current")
_AtmLoopbackVpIvlAverageDelay_Type = Integer32
_AtmLoopbackVpIvlAverageDelay_Object = MibTableColumn
atmLoopbackVpIvlAverageDelay = _AtmLoopbackVpIvlAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 6),
    _AtmLoopbackVpIvlAverageDelay_Type()
)
atmLoopbackVpIvlAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlAverageDelay.setStatus("current")
_AtmLoopbackVpIvlMaxDelay_Type = Integer32
_AtmLoopbackVpIvlMaxDelay_Object = MibTableColumn
atmLoopbackVpIvlMaxDelay = _AtmLoopbackVpIvlMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 7),
    _AtmLoopbackVpIvlMaxDelay_Type()
)
atmLoopbackVpIvlMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlMaxDelay.setStatus("current")
_AtmLoopbackVpIvlMinDelay_Type = Integer32
_AtmLoopbackVpIvlMinDelay_Object = MibTableColumn
atmLoopbackVpIvlMinDelay = _AtmLoopbackVpIvlMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 8),
    _AtmLoopbackVpIvlMinDelay_Type()
)
atmLoopbackVpIvlMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlMinDelay.setStatus("current")
_AtmLoopbackVpIvlErrSessions_Type = Integer32
_AtmLoopbackVpIvlErrSessions_Object = MibTableColumn
atmLoopbackVpIvlErrSessions = _AtmLoopbackVpIvlErrSessions_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 3, 1, 9),
    _AtmLoopbackVpIvlErrSessions_Type()
)
atmLoopbackVpIvlErrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVpIvlErrSessions.setStatus("current")
_AtmLoopbackVcIvlTable_Object = MibTable
atmLoopbackVcIvlTable = _AtmLoopbackVcIvlTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    atmLoopbackVcIvlTable.setStatus("current")
_AtmLoopbackVcIvlEntry_Object = MibTableRow
atmLoopbackVcIvlEntry = _AtmLoopbackVcIvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1)
)
atmLoopbackVcIvlEntry.setIndexNames(
    (0, "ACE202-MIB", "atmLoopbackVcIvlIfIndex"),
    (0, "ACE202-MIB", "atmLoopbackVcIvlVpi"),
    (0, "ACE202-MIB", "atmLoopbackVcIvlVci"),
    (0, "ACE202-MIB", "atmLoopbackVcIvlIvl"),
)
if mibBuilder.loadTexts:
    atmLoopbackVcIvlEntry.setStatus("current")
_AtmLoopbackVcIvlIfIndex_Type = Integer32
_AtmLoopbackVcIvlIfIndex_Object = MibTableColumn
atmLoopbackVcIvlIfIndex = _AtmLoopbackVcIvlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 1),
    _AtmLoopbackVcIvlIfIndex_Type()
)
atmLoopbackVcIvlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlIfIndex.setStatus("current")
_AtmLoopbackVcIvlVpi_Type = Integer32
_AtmLoopbackVcIvlVpi_Object = MibTableColumn
atmLoopbackVcIvlVpi = _AtmLoopbackVcIvlVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 2),
    _AtmLoopbackVcIvlVpi_Type()
)
atmLoopbackVcIvlVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlVpi.setStatus("current")
_AtmLoopbackVcIvlVci_Type = Integer32
_AtmLoopbackVcIvlVci_Object = MibTableColumn
atmLoopbackVcIvlVci = _AtmLoopbackVcIvlVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 3),
    _AtmLoopbackVcIvlVci_Type()
)
atmLoopbackVcIvlVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlVci.setStatus("current")


class _AtmLoopbackVcIvlIvl_Type(Integer32):
    """Custom type atmLoopbackVcIvlIvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmLoopbackVcIvlIvl_Type.__name__ = "Integer32"
_AtmLoopbackVcIvlIvl_Object = MibTableColumn
atmLoopbackVcIvlIvl = _AtmLoopbackVcIvlIvl_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 4),
    _AtmLoopbackVcIvlIvl_Type()
)
atmLoopbackVcIvlIvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlIvl.setStatus("current")


class _AtmLoopbackVcIvlOperStatus_Type(Integer32):
    """Custom type atmLoopbackVcIvlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noActive", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("endSuccessfully", 4))
    )


_AtmLoopbackVcIvlOperStatus_Type.__name__ = "Integer32"
_AtmLoopbackVcIvlOperStatus_Object = MibTableColumn
atmLoopbackVcIvlOperStatus = _AtmLoopbackVcIvlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 5),
    _AtmLoopbackVcIvlOperStatus_Type()
)
atmLoopbackVcIvlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlOperStatus.setStatus("current")
_AtmLoopbackVcIvlCDV_Type = Integer32
_AtmLoopbackVcIvlCDV_Object = MibTableColumn
atmLoopbackVcIvlCDV = _AtmLoopbackVcIvlCDV_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 6),
    _AtmLoopbackVcIvlCDV_Type()
)
atmLoopbackVcIvlCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlCDV.setStatus("current")
_AtmLoopbackVcIvlAverageDelay_Type = Integer32
_AtmLoopbackVcIvlAverageDelay_Object = MibTableColumn
atmLoopbackVcIvlAverageDelay = _AtmLoopbackVcIvlAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 7),
    _AtmLoopbackVcIvlAverageDelay_Type()
)
atmLoopbackVcIvlAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlAverageDelay.setStatus("current")
_AtmLoopbackVcIvlMaxDelay_Type = Integer32
_AtmLoopbackVcIvlMaxDelay_Object = MibTableColumn
atmLoopbackVcIvlMaxDelay = _AtmLoopbackVcIvlMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 8),
    _AtmLoopbackVcIvlMaxDelay_Type()
)
atmLoopbackVcIvlMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlMaxDelay.setStatus("current")
_AtmLoopbackVcIvlMinDelay_Type = Integer32
_AtmLoopbackVcIvlMinDelay_Object = MibTableColumn
atmLoopbackVcIvlMinDelay = _AtmLoopbackVcIvlMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 9),
    _AtmLoopbackVcIvlMinDelay_Type()
)
atmLoopbackVcIvlMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlMinDelay.setStatus("current")
_AtmLoopbackVcIvlErrSessions_Type = Integer32
_AtmLoopbackVcIvlErrSessions_Object = MibTableColumn
atmLoopbackVcIvlErrSessions = _AtmLoopbackVcIvlErrSessions_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 2, 4, 1, 10),
    _AtmLoopbackVcIvlErrSessions_Type()
)
atmLoopbackVcIvlErrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLoopbackVcIvlErrSessions.setStatus("current")
_AtmNtePM_ObjectIdentity = ObjectIdentity
atmNtePM = _AtmNtePM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3)
)
_AtmVpPmTable_Object = MibTable
atmVpPmTable = _AtmVpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    atmVpPmTable.setStatus("current")
_AtmVpPmEntry_Object = MibTableRow
atmVpPmEntry = _AtmVpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1)
)
atmVpPmEntry.setIndexNames(
    (0, "ACE202-MIB", "atmVpPmIfIndex"),
    (0, "ACE202-MIB", "atmVpPmVpi"),
)
if mibBuilder.loadTexts:
    atmVpPmEntry.setStatus("current")
_AtmVpPmIfIndex_Type = Integer32
_AtmVpPmIfIndex_Object = MibTableColumn
atmVpPmIfIndex = _AtmVpPmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 1),
    _AtmVpPmIfIndex_Type()
)
atmVpPmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPmIfIndex.setStatus("current")
_AtmVpPmVpi_Type = Integer32
_AtmVpPmVpi_Object = MibTableColumn
atmVpPmVpi = _AtmVpPmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 2),
    _AtmVpPmVpi_Type()
)
atmVpPmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpPmVpi.setStatus("current")


class _AtmVpPmAdminStatus_Type(Integer32):
    """Custom type atmVpPmAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("listenToActivationCells", 4),
          ("originateActivationCells", 5))
    )


_AtmVpPmAdminStatus_Type.__name__ = "Integer32"
_AtmVpPmAdminStatus_Object = MibTableColumn
atmVpPmAdminStatus = _AtmVpPmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 3),
    _AtmVpPmAdminStatus_Type()
)
atmVpPmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpPmAdminStatus.setStatus("current")


class _AtmVpPmDirection_Type(Integer32):
    """Custom type atmVpPmDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("source", 2),
          ("destination", 3),
          ("bidirectional", 4))
    )


_AtmVpPmDirection_Type.__name__ = "Integer32"
_AtmVpPmDirection_Object = MibTableColumn
atmVpPmDirection = _AtmVpPmDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 4),
    _AtmVpPmDirection_Type()
)
atmVpPmDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpPmDirection.setStatus("current")
_AtmVpPmBlockSize_Type = Integer32
_AtmVpPmBlockSize_Object = MibTableColumn
atmVpPmBlockSize = _AtmVpPmBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 5),
    _AtmVpPmBlockSize_Type()
)
atmVpPmBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpPmBlockSize.setStatus("current")
_AtmVpPmRowStatus_Type = RowStatus
_AtmVpPmRowStatus_Object = MibTableColumn
atmVpPmRowStatus = _AtmVpPmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 6),
    _AtmVpPmRowStatus_Type()
)
atmVpPmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpPmRowStatus.setStatus("current")


class _AtmVpPmSink_Type(Integer32):
    """Custom type atmVpPmSink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("fwd", 2),
          ("fwdAndBwdReport", 3))
    )


_AtmVpPmSink_Type.__name__ = "Integer32"
_AtmVpPmSink_Object = MibTableColumn
atmVpPmSink = _AtmVpPmSink_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 7),
    _AtmVpPmSink_Type()
)
atmVpPmSink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpPmSink.setStatus("current")


class _AtmVpPmSource_Type(Integer32):
    """Custom type atmVpPmSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("fwd", 2),
          ("fwdAndBwdReport", 3))
    )


_AtmVpPmSource_Type.__name__ = "Integer32"
_AtmVpPmSource_Object = MibTableColumn
atmVpPmSource = _AtmVpPmSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 1, 1, 8),
    _AtmVpPmSource_Type()
)
atmVpPmSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpPmSource.setStatus("current")
_AtmVcPmTable_Object = MibTable
atmVcPmTable = _AtmVcPmTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    atmVcPmTable.setStatus("current")
_AtmVcPmEntry_Object = MibTableRow
atmVcPmEntry = _AtmVcPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1)
)
atmVcPmEntry.setIndexNames(
    (0, "ACE202-MIB", "atmVcPmIfIndex"),
    (0, "ACE202-MIB", "atmVcPmVpi"),
    (0, "ACE202-MIB", "atmVcPmVci"),
)
if mibBuilder.loadTexts:
    atmVcPmEntry.setStatus("current")
_AtmVcPmIfIndex_Type = Integer32
_AtmVcPmIfIndex_Object = MibTableColumn
atmVcPmIfIndex = _AtmVcPmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 1),
    _AtmVcPmIfIndex_Type()
)
atmVcPmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPmIfIndex.setStatus("current")
_AtmVcPmVpi_Type = Integer32
_AtmVcPmVpi_Object = MibTableColumn
atmVcPmVpi = _AtmVcPmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 2),
    _AtmVcPmVpi_Type()
)
atmVcPmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPmVpi.setStatus("current")
_AtmVcPmVci_Type = Integer32
_AtmVcPmVci_Object = MibTableColumn
atmVcPmVci = _AtmVcPmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 3),
    _AtmVcPmVci_Type()
)
atmVcPmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcPmVci.setStatus("current")


class _AtmVcPmAdminStatus_Type(Integer32):
    """Custom type atmVcPmAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 2),
          ("down", 3),
          ("listenToActivationCells", 4),
          ("originateActivationCells", 5))
    )


_AtmVcPmAdminStatus_Type.__name__ = "Integer32"
_AtmVcPmAdminStatus_Object = MibTableColumn
atmVcPmAdminStatus = _AtmVcPmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 4),
    _AtmVcPmAdminStatus_Type()
)
atmVcPmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcPmAdminStatus.setStatus("current")


class _AtmVcPmDirection_Type(Integer32):
    """Custom type atmVcPmDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("source", 2),
          ("destination", 3),
          ("bidirectional", 4))
    )


_AtmVcPmDirection_Type.__name__ = "Integer32"
_AtmVcPmDirection_Object = MibTableColumn
atmVcPmDirection = _AtmVcPmDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 5),
    _AtmVcPmDirection_Type()
)
atmVcPmDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcPmDirection.setStatus("current")
_AtmVcPmBlockSize_Type = Integer32
_AtmVcPmBlockSize_Object = MibTableColumn
atmVcPmBlockSize = _AtmVcPmBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 6),
    _AtmVcPmBlockSize_Type()
)
atmVcPmBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcPmBlockSize.setStatus("current")
_AtmVcPmRowStatus_Type = RowStatus
_AtmVcPmRowStatus_Object = MibTableColumn
atmVcPmRowStatus = _AtmVcPmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 7),
    _AtmVcPmRowStatus_Type()
)
atmVcPmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcPmRowStatus.setStatus("current")


class _AtmVcPmSink_Type(Integer32):
    """Custom type atmVcPmSink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("fwd", 2),
          ("fwdAndBwdReport", 3))
    )


_AtmVcPmSink_Type.__name__ = "Integer32"
_AtmVcPmSink_Object = MibTableColumn
atmVcPmSink = _AtmVcPmSink_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 8),
    _AtmVcPmSink_Type()
)
atmVcPmSink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcPmSink.setStatus("current")


class _AtmVcPmSource_Type(Integer32):
    """Custom type atmVcPmSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("fwd", 2),
          ("fwdAndBwdReport", 3))
    )


_AtmVcPmSource_Type.__name__ = "Integer32"
_AtmVcPmSource_Object = MibTableColumn
atmVcPmSource = _AtmVcPmSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 2, 3, 2, 1, 9),
    _AtmVcPmSource_Type()
)
atmVcPmSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcPmSource.setStatus("current")
_RadAtmIma_ObjectIdentity = ObjectIdentity
radAtmIma = _RadAtmIma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 5)
)


class _ImaPrimaryClk_Type(Integer32):
    """Custom type imaPrimaryClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("link1", 2),
          ("link2", 3),
          ("link3", 4),
          ("link4", 5),
          ("automatic", 6))
    )


_ImaPrimaryClk_Type.__name__ = "Integer32"
_ImaPrimaryClk_Object = MibScalar
imaPrimaryClk = _ImaPrimaryClk_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 1),
    _ImaPrimaryClk_Type()
)
imaPrimaryClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaPrimaryClk.setStatus("current")
_ImaXLinkTable_Object = MibTable
imaXLinkTable = _ImaXLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 2)
)
if mibBuilder.loadTexts:
    imaXLinkTable.setStatus("current")
_ImaXLinkEntry_Object = MibTableRow
imaXLinkEntry = _ImaXLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 2, 1)
)
imaXLinkEntry.setIndexNames(
    (0, "IMA-MIB", "imaLinkIfIndex"),
)
if mibBuilder.loadTexts:
    imaXLinkEntry.setStatus("current")


class _ImaLinkDirection_Type(Integer32):
    """Custom type imaLinkDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2),
          ("both", 3))
    )


_ImaLinkDirection_Type.__name__ = "Integer32"
_ImaLinkDirection_Object = MibTableColumn
imaLinkDirection = _ImaLinkDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 2, 1, 1),
    _ImaLinkDirection_Type()
)
imaLinkDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaLinkDirection.setStatus("current")


class _ImaLinkItcLBClkSrc_Type(Integer32):
    """Custom type imaLinkItcLBClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("link1", 1),
          ("link2", 2),
          ("link3", 3),
          ("link4", 4),
          ("internal", 5),
          ("external", 6),
          ("automatic", 7))
    )


_ImaLinkItcLBClkSrc_Type.__name__ = "Integer32"
_ImaLinkItcLBClkSrc_Object = MibTableColumn
imaLinkItcLBClkSrc = _ImaLinkItcLBClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 2, 1, 2),
    _ImaLinkItcLBClkSrc_Type()
)
imaLinkItcLBClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaLinkItcLBClkSrc.setStatus("current")
_ImaXGroupTable_Object = MibTable
imaXGroupTable = _ImaXGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 3)
)
if mibBuilder.loadTexts:
    imaXGroupTable.setStatus("current")
_ImaXGroupEntry_Object = MibTableRow
imaXGroupEntry = _ImaXGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 3, 1)
)
imaXGroupEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaXGroupEntry.setStatus("current")


class _ImaGroupVersion_Type(Integer32):
    """Custom type imaGroupVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ver10", 1),
          ("ver11", 2))
    )


_ImaGroupVersion_Type.__name__ = "Integer32"
_ImaGroupVersion_Object = MibTableColumn
imaGroupVersion = _ImaGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 3, 1, 1),
    _ImaGroupVersion_Type()
)
imaGroupVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupVersion.setStatus("current")


class _ImaGroupCtcTxClkSrc_Type(Integer32):
    """Custom type imaGroupCtcTxClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("link1", 1),
          ("link2", 2),
          ("link3", 3),
          ("link4", 4),
          ("internal", 5),
          ("external", 6),
          ("automatic", 7),
          ("notApplicable", 255))
    )


_ImaGroupCtcTxClkSrc_Type.__name__ = "Integer32"
_ImaGroupCtcTxClkSrc_Object = MibTableColumn
imaGroupCtcTxClkSrc = _ImaGroupCtcTxClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 5, 3, 1, 2),
    _ImaGroupCtcTxClkSrc_Type()
)
imaGroupCtcTxClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupCtcTxClkSrc.setStatus("current")
_AtmLayer2_ObjectIdentity = ObjectIdentity
atmLayer2 = _AtmLayer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 7)
)
_AtmLayer2XVclTable_Object = MibTable
atmLayer2XVclTable = _AtmLayer2XVclTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 1)
)
if mibBuilder.loadTexts:
    atmLayer2XVclTable.setStatus("current")
_AtmLayer2XVclEntry_Object = MibTableRow
atmLayer2XVclEntry = _AtmLayer2XVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 1, 1)
)
if mibBuilder.loadTexts:
    atmLayer2XVclEntry.setStatus("current")


class _AtmLayer2XVclConnMode_Type(Integer32):
    """Custom type atmLayer2XVclConnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("sub", 2))
    )


_AtmLayer2XVclConnMode_Type.__name__ = "Integer32"
_AtmLayer2XVclConnMode_Object = MibTableColumn
atmLayer2XVclConnMode = _AtmLayer2XVclConnMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 1, 1, 1),
    _AtmLayer2XVclConnMode_Type()
)
atmLayer2XVclConnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmLayer2XVclConnMode.setStatus("current")
_AtmLayer2XVclGroupIdx_Type = Integer32
_AtmLayer2XVclGroupIdx_Object = MibTableColumn
atmLayer2XVclGroupIdx = _AtmLayer2XVclGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 1, 1, 2),
    _AtmLayer2XVclGroupIdx_Type()
)
atmLayer2XVclGroupIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLayer2XVclGroupIdx.setStatus("current")
_AtmLayer2GroupTable_Object = MibTable
atmLayer2GroupTable = _AtmLayer2GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 2)
)
if mibBuilder.loadTexts:
    atmLayer2GroupTable.setStatus("current")
_AtmLayer2GroupEntry_Object = MibTableRow
atmLayer2GroupEntry = _AtmLayer2GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 2, 1)
)
atmLayer2GroupEntry.setIndexNames(
    (0, "ACE202-MIB", "atmLayer2GroupIdx"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmLayer2GroupEntry.setStatus("current")
_AtmLayer2GroupIdx_Type = Integer32
_AtmLayer2GroupIdx_Object = MibTableColumn
atmLayer2GroupIdx = _AtmLayer2GroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 2, 1, 1),
    _AtmLayer2GroupIdx_Type()
)
atmLayer2GroupIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLayer2GroupIdx.setStatus("current")
_AtmLayer2GroupRowStatus_Type = RowStatus
_AtmLayer2GroupRowStatus_Object = MibTableColumn
atmLayer2GroupRowStatus = _AtmLayer2GroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 2, 1, 2),
    _AtmLayer2GroupRowStatus_Type()
)
atmLayer2GroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmLayer2GroupRowStatus.setStatus("current")


class _AtmLayer2GroupConnMode_Type(Integer32):
    """Custom type atmLayer2GroupConnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("sub", 2))
    )


_AtmLayer2GroupConnMode_Type.__name__ = "Integer32"
_AtmLayer2GroupConnMode_Object = MibTableColumn
atmLayer2GroupConnMode = _AtmLayer2GroupConnMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 2, 1, 3),
    _AtmLayer2GroupConnMode_Type()
)
atmLayer2GroupConnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLayer2GroupConnMode.setStatus("current")


class _AtmLayer2GroupConnPriority_Type(OctetString):
    """Custom type atmLayer2GroupConnPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AtmLayer2GroupConnPriority_Type.__name__ = "OctetString"
_AtmLayer2GroupConnPriority_Object = MibTableColumn
atmLayer2GroupConnPriority = _AtmLayer2GroupConnPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 2, 1, 4),
    _AtmLayer2GroupConnPriority_Type()
)
atmLayer2GroupConnPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLayer2GroupConnPriority.setStatus("current")


class _AtmLayer2GroupName_Type(SnmpAdminString):
    """Custom type atmLayer2GroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtmLayer2GroupName_Type.__name__ = "SnmpAdminString"
_AtmLayer2GroupName_Object = MibTableColumn
atmLayer2GroupName = _AtmLayer2GroupName_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 2, 1, 5),
    _AtmLayer2GroupName_Type()
)
atmLayer2GroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmLayer2GroupName.setStatus("current")
_AtmLayer2PriorityTable_Object = MibTable
atmLayer2PriorityTable = _AtmLayer2PriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 3)
)
if mibBuilder.loadTexts:
    atmLayer2PriorityTable.setStatus("current")
_AtmLayer2PriorityEntry_Object = MibTableRow
atmLayer2PriorityEntry = _AtmLayer2PriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 3, 1)
)
atmLayer2PriorityEntry.setIndexNames(
    (0, "ACE202-MIB", "atmLayer2PriorityGroupIdx"),
    (0, "ACE202-MIB", "atmLayer2PriorityRx"),
)
if mibBuilder.loadTexts:
    atmLayer2PriorityEntry.setStatus("current")
_AtmLayer2PriorityGroupIdx_Type = Integer32
_AtmLayer2PriorityGroupIdx_Object = MibTableColumn
atmLayer2PriorityGroupIdx = _AtmLayer2PriorityGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 3, 1, 1),
    _AtmLayer2PriorityGroupIdx_Type()
)
atmLayer2PriorityGroupIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLayer2PriorityGroupIdx.setStatus("current")


class _AtmLayer2PriorityRx_Type(Integer32):
    """Custom type atmLayer2PriorityRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmLayer2PriorityRx_Type.__name__ = "Integer32"
_AtmLayer2PriorityRx_Object = MibTableColumn
atmLayer2PriorityRx = _AtmLayer2PriorityRx_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 3, 1, 2),
    _AtmLayer2PriorityRx_Type()
)
atmLayer2PriorityRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLayer2PriorityRx.setStatus("current")
_AtmLayer2PriorityIfIndex_Type = InterfaceIndex
_AtmLayer2PriorityIfIndex_Object = MibTableColumn
atmLayer2PriorityIfIndex = _AtmLayer2PriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 3, 1, 3),
    _AtmLayer2PriorityIfIndex_Type()
)
atmLayer2PriorityIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmLayer2PriorityIfIndex.setStatus("current")
_AtmLayer2PriorityVclVpi_Type = Integer32
_AtmLayer2PriorityVclVpi_Object = MibTableColumn
atmLayer2PriorityVclVpi = _AtmLayer2PriorityVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 3, 1, 4),
    _AtmLayer2PriorityVclVpi_Type()
)
atmLayer2PriorityVclVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmLayer2PriorityVclVpi.setStatus("current")
_AtmLayer2PriorityVclVci_Type = Integer32
_AtmLayer2PriorityVclVci_Object = MibTableColumn
atmLayer2PriorityVclVci = _AtmLayer2PriorityVclVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 3, 1, 5),
    _AtmLayer2PriorityVclVci_Type()
)
atmLayer2PriorityVclVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmLayer2PriorityVclVci.setStatus("current")


class _AtmLayer2GroupIndexNext_Type(Integer32):
    """Custom type atmLayer2GroupIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmLayer2GroupIndexNext_Type.__name__ = "Integer32"
_AtmLayer2GroupIndexNext_Object = MibScalar
atmLayer2GroupIndexNext = _AtmLayer2GroupIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 7, 4),
    _AtmLayer2GroupIndexNext_Type()
)
atmLayer2GroupIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmLayer2GroupIndexNext.setStatus("current")
_RadAtmFr_ObjectIdentity = ObjectIdentity
radAtmFr = _RadAtmFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 8)
)
_FrAtmIwfXConnectionTable_Object = MibTable
frAtmIwfXConnectionTable = _FrAtmIwfXConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 8, 1)
)
if mibBuilder.loadTexts:
    frAtmIwfXConnectionTable.setStatus("current")
_FrAtmIwfXConnectionEntry_Object = MibTableRow
frAtmIwfXConnectionEntry = _FrAtmIwfXConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 8, 1, 1)
)
if mibBuilder.loadTexts:
    frAtmIwfXConnectionEntry.setStatus("current")


class _FrAtmIwfXConnMode_Type(Integer32):
    """Custom type frAtmIwfXConnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("service", 1),
          ("network", 2))
    )


_FrAtmIwfXConnMode_Type.__name__ = "Integer32"
_FrAtmIwfXConnMode_Object = MibTableColumn
frAtmIwfXConnMode = _FrAtmIwfXConnMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 8, 1, 1, 1),
    _FrAtmIwfXConnMode_Type()
)
frAtmIwfXConnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfXConnMode.setStatus("current")
_FrAtmIwfXConnSscsDlci_Type = Integer32
_FrAtmIwfXConnSscsDlci_Object = MibTableColumn
frAtmIwfXConnSscsDlci = _FrAtmIwfXConnSscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 8, 1, 1, 2),
    _FrAtmIwfXConnSscsDlci_Type()
)
frAtmIwfXConnSscsDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfXConnSscsDlci.setStatus("current")
_RadExperimental_ObjectIdentity = ObjectIdentity
radExperimental = _RadExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20)
)
isdnSignalingEntry.registerAugmentions(
    ("ACE202-MIB",
     "rtrIsdnIfEntry")
)
rtrIsdnIfEntry.setIndexNames(*isdnSignalingEntry.getIndexNames())
aal5VccEntry.registerAugmentions(
    ("ACE202-MIB",
     "aal5VccXEntry")
)
aal5VccXEntry.setIndexNames(*aal5VccEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("ACE202-MIB",
     "atmLayer2XVclEntry")
)
atmLayer2XVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
frAtmIwfConnectionEntry.registerAugmentions(
    ("ACE202-MIB",
     "frAtmIwfXConnectionEntry")
)
frAtmIwfXConnectionEntry.setIndexNames(*frAtmIwfConnectionEntry.getIndexNames())

# Managed Objects groups


# Notification objects

tftpStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 1)
)
tftpStatusChangeTrap.setObjects(
    ("ACE202-MIB", "tftpStatus")
)
if mibBuilder.loadTexts:
    tftpStatusChangeTrap.setStatus(
        "current"
    )

agnStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 2)
)
agnStatusChangeTrap.setObjects(
    ("ACE202-MIB", "agnIndication")
)
if mibBuilder.loadTexts:
    agnStatusChangeTrap.setStatus(
        "current"
    )

prtStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 3)
)
if mibBuilder.loadTexts:
    prtStatusChangeTrap.setStatus(
        "current"
    )

swdlStatusResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 4)
)
swdlStatusResult.setObjects(
    ("ACE202-MIB", "swdlStatusFileName")
)
if mibBuilder.loadTexts:
    swdlStatusResult.setStatus(
        "current"
    )

intSwdlSlotFileMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 5)
)
intSwdlSlotFileMismatch.setObjects(
    ("ACE202-MIB", "intSwdlFileName")
)
if mibBuilder.loadTexts:
    intSwdlSlotFileMismatch.setStatus(
        "current"
    )

agnCounterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 6)
)
if mibBuilder.loadTexts:
    agnCounterChange.setStatus(
        "current"
    )

prtClkSrcChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 7)
)
if mibBuilder.loadTexts:
    prtClkSrcChangeTrap.setStatus(
        "current"
    )

moduleFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 8)
)
if mibBuilder.loadTexts:
    moduleFailTrap.setStatus(
        "current"
    )

moduleInitFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 9)
)
if mibBuilder.loadTexts:
    moduleInitFailTrap.setStatus(
        "current"
    )

clkSrcChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 10)
)
if mibBuilder.loadTexts:
    clkSrcChangeTrap.setStatus(
        "current"
    )

agnUploadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 11)
)
if mibBuilder.loadTexts:
    agnUploadDataTrap.setStatus(
        "current"
    )

enrollmentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 12)
)
if mibBuilder.loadTexts:
    enrollmentTrap.setStatus(
        "current"
    )

agnPowerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 13)
)
if mibBuilder.loadTexts:
    agnPowerFailureTrap.setStatus(
        "current"
    )

atmAceSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 6)
)
atmAceSystemTrap.setObjects(
      *(("ACE202-MIB", "atmNteEventType"),
        ("ACE202-MIB", "agnLed"),
        ("ACE202-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    atmAceSystemTrap.setStatus(
        "current"
    )

atmAceAlarmLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 16)
)
atmAceAlarmLOS.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLOS.setStatus(
        "current"
    )

atmAceAlarmLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 17)
)
atmAceAlarmLOF.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLOF.setStatus(
        "current"
    )

atmAceAlarmLCD = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 18)
)
atmAceAlarmLCD.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLCD.setStatus(
        "current"
    )

atmAceAlarmSLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 19)
)
atmAceAlarmSLM.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmSLM.setStatus(
        "current"
    )

atmAceAlarmLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 20)
)
atmAceAlarmLOP.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLOP.setStatus(
        "current"
    )

atmAceAlarmLineAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 21)
)
atmAceAlarmLineAIS.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLineAIS.setStatus(
        "current"
    )

atmAceAlarmPathAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 22)
)
atmAceAlarmPathAIS.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPathAIS.setStatus(
        "current"
    )

atmAceAlarmLineRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 23)
)
atmAceAlarmLineRDI.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLineRDI.setStatus(
        "current"
    )

atmAceAlarmPathRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 24)
)
atmAceAlarmPathRDI.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPathRDI.setStatus(
        "current"
    )

atmAceAlarmSectionBIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 25)
)
atmAceAlarmSectionBIP.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmSectionBIP.setStatus(
        "current"
    )

atmAceAlarmLineBIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 26)
)
atmAceAlarmLineBIP.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLineBIP.setStatus(
        "current"
    )

atmAceAlarmPathBIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 27)
)
atmAceAlarmPathBIP.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPathBIP.setStatus(
        "current"
    )

atmAceAlarmLineFEBE = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 28)
)
atmAceAlarmLineFEBE.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmLineFEBE.setStatus(
        "current"
    )

atmAceAlarmPathFEBE = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 29)
)
atmAceAlarmPathFEBE.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPathFEBE.setStatus(
        "current"
    )

atmAceAlarmPlcpLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 30)
)
atmAceAlarmPlcpLOF.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPlcpLOF.setStatus(
        "current"
    )

atmAceAlarmPlcpYELLOW = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 31)
)
atmAceAlarmPlcpYELLOW.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPlcpYELLOW.setStatus(
        "current"
    )

atmAceAlarmPlcpBIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 32)
)
atmAceAlarmPlcpBIP.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPlcpBIP.setStatus(
        "current"
    )

atmAceAlarmPlcpFEBE = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 33)
)
atmAceAlarmPlcpFEBE.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPlcpFEBE.setStatus(
        "current"
    )

atmAceAlarmPlcpP1P2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 34)
)
atmAceAlarmPlcpP1P2.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmPlcpP1P2.setStatus(
        "current"
    )

atmAceAlarmUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 35)
)
atmAceAlarmUAS.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmUAS.setStatus(
        "current"
    )

atmAceAlarmCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 36)
)
atmAceAlarmCluster.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("ACE202-MIB", "atmNteAlarmType"),
        ("ACE202-MIB", "atmNteLevel"))
)
if mibBuilder.loadTexts:
    atmAceAlarmCluster.setStatus(
        "current"
    )

atmAceAlarmVpContinuityLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 40)
)
atmAceAlarmVpContinuityLoss.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpContinuityLoss.setStatus(
        "current"
    )

atmAceAlarmVpAISReception = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 41)
)
atmAceAlarmVpAISReception.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpAISReception.setStatus(
        "current"
    )

atmAceAlarmVpRDIReception = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 42)
)
atmAceAlarmVpRDIReception.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpRDIReception.setStatus(
        "current"
    )

atmAceAlarmVpErroredCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 43)
)
atmAceAlarmVpErroredCells.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpErroredCells.setStatus(
        "current"
    )

atmAceAlarmVpLostCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 44)
)
atmAceAlarmVpLostCells.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpLostCells.setStatus(
        "current"
    )

atmAceAlarmVpMisinsertedCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 45)
)
atmAceAlarmVpMisinsertedCells.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpMisinsertedCells.setStatus(
        "current"
    )

atmAceAlarmVpUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 46)
)
atmAceAlarmVpUAS.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpUAS.setStatus(
        "current"
    )

atmAceAlarmVpLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 47)
)
atmAceAlarmVpLoopback.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpLoopback.setStatus(
        "current"
    )

atmAceAlarmVpGCRAViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 48)
)
atmAceAlarmVpGCRAViolation.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVpGCRAViolation.setStatus(
        "current"
    )

atmAceAlarmVcContinuityLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 56)
)
atmAceAlarmVcContinuityLoss.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcContinuityLoss.setStatus(
        "current"
    )

atmAceAlarmVcAISReception = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 57)
)
atmAceAlarmVcAISReception.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcAISReception.setStatus(
        "current"
    )

atmAceAlarmVcRDIReception = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 58)
)
atmAceAlarmVcRDIReception.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcRDIReception.setStatus(
        "current"
    )

atmAceAlarmVcErroredCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 59)
)
atmAceAlarmVcErroredCells.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcErroredCells.setStatus(
        "current"
    )

atmAceAlarmVcLostCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 60)
)
atmAceAlarmVcLostCells.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcLostCells.setStatus(
        "current"
    )

atmAceAlarmVcMisinsertedCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 61)
)
atmAceAlarmVcMisinsertedCells.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcMisinsertedCells.setStatus(
        "current"
    )

atmAceAlarmVcUnexpectedCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 62)
)
atmAceAlarmVcUnexpectedCell.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcUnexpectedCell.setStatus(
        "current"
    )

atmAceAlarmVcUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 63)
)
atmAceAlarmVcUAS.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcUAS.setStatus(
        "current"
    )

atmAceAlarmVcLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 64)
)
atmAceAlarmVcLoopback.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcLoopback.setStatus(
        "current"
    )

atmAceAlarmVcGCRAViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 65)
)
atmAceAlarmVcGCRAViolation.setObjects(
      *(("ACE202-MIB", "alarmSeverity"),
        ("ACE202-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmAceAlarmVcGCRAViolation.setStatus(
        "current"
    )

atmImaGroupStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 12, 0, 80)
)
atmImaGroupStatusChangeTrap.setObjects(
    ("IMA-MIB", "imaGroupFailureStatus")
)
if mibBuilder.loadTexts:
    atmImaGroupStatusChangeTrap.setStatus(
        "current"
    )

atmAceStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 0, 1)
)
atmAceStatusChange.setObjects(
      *(("ACE202-MIB", "agnLed"),
        ("ACE202-MIB", "agnIndication"))
)
if mibBuilder.loadTexts:
    atmAceStatusChange.setStatus(
        "current"
    )

atmAceAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 0, 2)
)
atmAceAlarmTrap.setObjects(
    ("ACE202-MIB", "atmInterfaceAlarmStatus")
)
if mibBuilder.loadTexts:
    atmAceAlarmTrap.setStatus(
        "current"
    )

atmAceModuleChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 0, 3)
)
atmAceModuleChangeTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    atmAceModuleChangeTrap.setStatus(
        "current"
    )

atmAceRedundancyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 3, 0, 4)
)
atmAceRedundancyTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    atmAceRedundancyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACE202-MIB",
    **{"MacAddress": MacAddress,
       "GenAddress": GenAddress,
       "rad": rad,
       "radTokenRing": radTokenRing,
       "radFddi": radFddi,
       "radWan": radWan,
       "wanGen": wanGen,
       "diverseIfWanGen": diverseIfWanGen,
       "sonetInterface": sonetInterface,
       "prtSonetPerfHistory": prtSonetPerfHistory,
       "prtSonetMediumTable": prtSonetMediumTable,
       "prtSonetMediumEntry": prtSonetMediumEntry,
       "prtSonetMediumTimeElapsed": prtSonetMediumTimeElapsed,
       "prtSonetMediumValidIntervals": prtSonetMediumValidIntervals,
       "prtSonetSectionLineCurrentTable": prtSonetSectionLineCurrentTable,
       "prtSectionLineCurrentEntry": prtSectionLineCurrentEntry,
       "prtSonetCurrentLOS": prtSonetCurrentLOS,
       "prtSonetCurrentLOF": prtSonetCurrentLOF,
       "prtSonetCurrentLineAIS": prtSonetCurrentLineAIS,
       "prtSonetCurrentLineFERF": prtSonetCurrentLineFERF,
       "prtSonetCurrentSectionBIP": prtSonetCurrentSectionBIP,
       "prtSonetCurrentLineBIP": prtSonetCurrentLineBIP,
       "prtSonetCurrentLineFEBE": prtSonetCurrentLineFEBE,
       "prtSonetCurrentUAS": prtSonetCurrentUAS,
       "prtSonetCurrentSES": prtSonetCurrentSES,
       "prtSonetCurrentES": prtSonetCurrentES,
       "prtSonetCurrentStatus": prtSonetCurrentStatus,
       "prtSonetCurrentLSV": prtSonetCurrentLSV,
       "prtSonetSectionLineIntervalTable": prtSonetSectionLineIntervalTable,
       "prtSectionLineIntervalEntry": prtSectionLineIntervalEntry,
       "prtSonetLineIntervalNumber": prtSonetLineIntervalNumber,
       "prtSonetIntervalLOS": prtSonetIntervalLOS,
       "prtSonetIntervalLOF": prtSonetIntervalLOF,
       "prtSonetIntervalLineAIS": prtSonetIntervalLineAIS,
       "prtSonetIntervalLineFERF": prtSonetIntervalLineFERF,
       "prtSonetIntervalSectionBIP": prtSonetIntervalSectionBIP,
       "prtSonetIntervalLineBIP": prtSonetIntervalLineBIP,
       "prtSonetIntervalLineFEBE": prtSonetIntervalLineFEBE,
       "prtSonetIntervalUAS": prtSonetIntervalUAS,
       "prtSonetIntervalSES": prtSonetIntervalSES,
       "prtSonetIntervalES": prtSonetIntervalES,
       "prtSonetIntervalStatus": prtSonetIntervalStatus,
       "prtSonetIntervalLSV": prtSonetIntervalLSV,
       "prtSonetPathCurrentTable": prtSonetPathCurrentTable,
       "prtPathCurrentEntry": prtPathCurrentEntry,
       "prtSonetCurrentPathAIS": prtSonetCurrentPathAIS,
       "prtSonetCurrentPathFERF": prtSonetCurrentPathFERF,
       "prtSonetCurrentLOP": prtSonetCurrentLOP,
       "prtSonetCurrentSLM": prtSonetCurrentSLM,
       "prtSonetCurrentLOC": prtSonetCurrentLOC,
       "prtSonetCurrentPathBIP": prtSonetCurrentPathBIP,
       "prtSonetCurrentPathFEBE": prtSonetCurrentPathFEBE,
       "prtSonetPathIntervalTable": prtSonetPathIntervalTable,
       "prtPathIntervalEntry": prtPathIntervalEntry,
       "prtSonetPathIntervalNumber": prtSonetPathIntervalNumber,
       "prtSonetIntervalPathAIS": prtSonetIntervalPathAIS,
       "prtSonetIntervalPathFERF": prtSonetIntervalPathFERF,
       "prtSonetIntervalLOP": prtSonetIntervalLOP,
       "prtSonetIntervalSLM": prtSonetIntervalSLM,
       "prtSonetIntervalLOC": prtSonetIntervalLOC,
       "prtSonetIntervalPathBIP": prtSonetIntervalPathBIP,
       "prtSonetIntervalPathFEBE": prtSonetIntervalPathFEBE,
       "prtSonetConfig": prtSonetConfig,
       "prtSonetGen": prtSonetGen,
       "prtSonetGenTable": prtSonetGenTable,
       "prtSonetGenEntry": prtSonetGenEntry,
       "prtSonetGenCnfgIdx": prtSonetGenCnfgIdx,
       "prtSonetGenIdx": prtSonetGenIdx,
       "prtSonetGenSdThreshold": prtSonetGenSdThreshold,
       "prtSonetGenEedThreshold": prtSonetGenEedThreshold,
       "prtSonetStm1": prtSonetStm1,
       "prtSonetStm1Table": prtSonetStm1Table,
       "prtSonetStm1Entry": prtSonetStm1Entry,
       "prtSonetStm1CnfgIdx": prtSonetStm1CnfgIdx,
       "prtSonetStm1Idx": prtSonetStm1Idx,
       "prtSonetStm1ClockSrc": prtSonetStm1ClockSrc,
       "prtSonetStm1DccMode": prtSonetStm1DccMode,
       "prtSonetStm1RoutingProt": prtSonetStm1RoutingProt,
       "prtSonetStm1MngProt": prtSonetStm1MngProt,
       "prtSonetVc": prtSonetVc,
       "prtSonetVcTable": prtSonetVcTable,
       "prtSonetVcEntry": prtSonetVcEntry,
       "prtSonetVcCnfgIdx": prtSonetVcCnfgIdx,
       "prtSonetVcIdx": prtSonetVcIdx,
       "prtSonetVcJTxPathTraceEnable": prtSonetVcJTxPathTraceEnable,
       "prtSonetVcJRxPathTraceEnable": prtSonetVcJRxPathTraceEnable,
       "prtSonetVcJPathTrace": prtSonetVcJPathTrace,
       "prtSonetVcConnect": prtSonetVcConnect,
       "prtSonetTuTable": prtSonetTuTable,
       "prtSonetTuEntry": prtSonetTuEntry,
       "prtSonetTuCnfgIdx": prtSonetTuCnfgIdx,
       "prtSonetTuPrtIdx": prtSonetTuPrtIdx,
       "prtSonetTuIdx": prtSonetTuIdx,
       "prtSonetTuConPrtIdx": prtSonetTuConPrtIdx,
       "prtSonetTuType": prtSonetTuType,
       "prtSonetTuMode": prtSonetTuMode,
       "prtSonetTuRowStatus": prtSonetTuRowStatus,
       "prtSonetXConnect": prtSonetXConnect,
       "prtSonetXConnectTable": prtSonetXConnectTable,
       "prtSonetXConnectEntry": prtSonetXConnectEntry,
       "prtSonetXConnectCnfgIdx": prtSonetXConnectCnfgIdx,
       "prtSonetXConnectPrtIdx": prtSonetXConnectPrtIdx,
       "prtSonetXConnectConPrtIdx": prtSonetXConnectConPrtIdx,
       "prtSonetXConnectAUGIdx": prtSonetXConnectAUGIdx,
       "prtSonetXConnectTUG3Idx": prtSonetXConnectTUG3Idx,
       "prtSonetXConnectTUG2Idx": prtSonetXConnectTUG2Idx,
       "prtSonetXConnectTUnIdx": prtSonetXConnectTUnIdx,
       "prtSonetXConnectRowStatus": prtSonetXConnectRowStatus,
       "prtSonetXConnectDirection": prtSonetXConnectDirection,
       "prtSonetXConnectTuNumber": prtSonetXConnectTuNumber,
       "ds3Interface": ds3Interface,
       "prtDs3PerfHistory": prtDs3PerfHistory,
       "prtSDs3IfTable": prtSDs3IfTable,
       "prtDs3IfEntry": prtDs3IfEntry,
       "prtDs3IfTimeElapsed": prtDs3IfTimeElapsed,
       "prtDs3IfValidIntervals": prtDs3IfValidIntervals,
       "prtDs3CurrentTable": prtDs3CurrentTable,
       "prtDs3CurrentEntry": prtDs3CurrentEntry,
       "prtDs3CurrentLOS": prtDs3CurrentLOS,
       "prtDs3CurrentOOF": prtDs3CurrentOOF,
       "prtDs3CurrentLOC": prtDs3CurrentLOC,
       "prtDs3CurrentAIS": prtDs3CurrentAIS,
       "prtDs3CurrentRDI": prtDs3CurrentRDI,
       "prtDs3CurrentUAS": prtDs3CurrentUAS,
       "prtDs3CurrentBIP": prtDs3CurrentBIP,
       "prtDs3CurrentFEBE": prtDs3CurrentFEBE,
       "prtDs3CurrentSLM": prtDs3CurrentSLM,
       "prtDs3CurrentSES": prtDs3CurrentSES,
       "prtDs3CurrentES": prtDs3CurrentES,
       "prtDs3CurrentBitParity": prtDs3CurrentBitParity,
       "prtDs3CurrentPlcpLOF": prtDs3CurrentPlcpLOF,
       "prtDs3CurrentPlcpRAI": prtDs3CurrentPlcpRAI,
       "prtDs3CurrentPlcpBIP": prtDs3CurrentPlcpBIP,
       "prtDs3CurrentPlcpFEBE": prtDs3CurrentPlcpFEBE,
       "prtDs3CurrentBPV": prtDs3CurrentBPV,
       "prtDs3CurrentLCE": prtDs3CurrentLCE,
       "prtDs3CurrentStatus": prtDs3CurrentStatus,
       "prtDs3IntervalTable": prtDs3IntervalTable,
       "prtDs3IntervalEntry": prtDs3IntervalEntry,
       "prtDs3IntervalNumber": prtDs3IntervalNumber,
       "prtDs3IntervalLOS": prtDs3IntervalLOS,
       "prtDs3IntervalOOF": prtDs3IntervalOOF,
       "prtDs3IntervalLOC": prtDs3IntervalLOC,
       "prtDs3IntervalAIS": prtDs3IntervalAIS,
       "prtDs3IntervalRDI": prtDs3IntervalRDI,
       "prtDs3IntervalUAS": prtDs3IntervalUAS,
       "prtDs3IntervalBIP": prtDs3IntervalBIP,
       "prtDs3IntervalFEBE": prtDs3IntervalFEBE,
       "prtDs3IntervalSLM": prtDs3IntervalSLM,
       "prtDs3IntervalSES": prtDs3IntervalSES,
       "prtDs3IntervalES": prtDs3IntervalES,
       "prtDs3IntervalBitParity": prtDs3IntervalBitParity,
       "prtDs3IntervalPlcpLOF": prtDs3IntervalPlcpLOF,
       "prtDs3IntervalPlcpRAI": prtDs3IntervalPlcpRAI,
       "prtDs3IntervalPlcpBIP": prtDs3IntervalPlcpBIP,
       "prtDs3IntervalPlcpFEBE": prtDs3IntervalPlcpFEBE,
       "prtDs3IntervalBPV": prtDs3IntervalBPV,
       "prtDs3IntervalLCE": prtDs3IntervalLCE,
       "prtDs3IntervalStatus": prtDs3IntervalStatus,
       "prtDs3TotalTable": prtDs3TotalTable,
       "prtDs3TotalEntry": prtDs3TotalEntry,
       "prtDs3TotalUAS": prtDs3TotalUAS,
       "prtDs3TotalBPV": prtDs3TotalBPV,
       "prtDs3TotalLCE": prtDs3TotalLCE,
       "ds1Interface": ds1Interface,
       "prtDs1PerfHistory": prtDs1PerfHistory,
       "dsx1XCurrentTable": dsx1XCurrentTable,
       "dsx1XCurrentEntry": dsx1XCurrentEntry,
       "dsx1CurrentLOS": dsx1CurrentLOS,
       "dsx1CurrentLOF": dsx1CurrentLOF,
       "dsx1CurrentLOC": dsx1CurrentLOC,
       "dsx1CurrentAIS": dsx1CurrentAIS,
       "dsx1CurrentRAI": dsx1CurrentRAI,
       "dsx1CurrentLOMF": dsx1CurrentLOMF,
       "dsx1CurrentFEBE": dsx1CurrentFEBE,
       "dsx1CurrentStatus": dsx1CurrentStatus,
       "dsx1CurrentBPV": dsx1CurrentBPV,
       "dsx1CurrentLOCRCMF": dsx1CurrentLOCRCMF,
       "dsx1CurrentLOFC": dsx1CurrentLOFC,
       "dsx1XIntervalTable": dsx1XIntervalTable,
       "dsx1XIntervalEntry": dsx1XIntervalEntry,
       "dsx1IntervalLOS": dsx1IntervalLOS,
       "dsx1IntervalLOF": dsx1IntervalLOF,
       "dsx1IntervalLOC": dsx1IntervalLOC,
       "dsx1IntervalAIS": dsx1IntervalAIS,
       "dsx1IntervalRAI": dsx1IntervalRAI,
       "dsx1IntervalLOMF": dsx1IntervalLOMF,
       "dsx1IntervalFEBE": dsx1IntervalFEBE,
       "dsx1IntervalStatus": dsx1IntervalStatus,
       "dsx1IntervalBPV": dsx1IntervalBPV,
       "dsx1IntervalLOCRCMF": dsx1IntervalLOCRCMF,
       "dsx1IntervalLOFC": dsx1IntervalLOFC,
       "dsx1XTotalTable": dsx1XTotalTable,
       "dsx1XTotalEntry": dsx1XTotalEntry,
       "dsx1TotalBPV": dsx1TotalBPV,
       "dsx1TotalLOFC": dsx1TotalLOFC,
       "dsx1XConfigTable": dsx1XConfigTable,
       "dsx1XConfigEntry": dsx1XConfigEntry,
       "dsx1IdleCode": dsx1IdleCode,
       "dsx1LineMode": dsx1LineMode,
       "dsx1dBTxGain": dsx1dBTxGain,
       "dsx1RxSensitivity": dsx1RxSensitivity,
       "dsx1RestoreTime": dsx1RestoreTime,
       "dsx1TcFirstSignal": dsx1TcFirstSignal,
       "dsx1TcSignal": dsx1TcSignal,
       "dsx1TcPattern": dsx1TcPattern,
       "dsx1Scramble": dsx1Scramble,
       "dsx1LineAdaptiveTimingMode": dsx1LineAdaptiveTimingMode,
       "dsx1TxClockSource": dsx1TxClockSource,
       "dsx1AisEnable": dsx1AisEnable,
       "dsx1TsEchoCancel": dsx1TsEchoCancel,
       "dsx1EchoCancelerModule": dsx1EchoCancelerModule,
       "hdlcMibObjects": hdlcMibObjects,
       "hdlcTable": hdlcTable,
       "hdlcEntry": hdlcEntry,
       "hdlcProtocol": hdlcProtocol,
       "hdlcRateResolution": hdlcRateResolution,
       "hdlcTxClockSource": hdlcTxClockSource,
       "hdlcTerminalMode": hdlcTerminalMode,
       "hdlcLoopbackState": hdlcLoopbackState,
       "hdlcTxClockPolarity": hdlcTxClockPolarity,
       "hdlcFlowControl": hdlcFlowControl,
       "hdlcLineRate": hdlcLineRate,
       "hdlcRxClockMode": hdlcRxClockMode,
       "hdlcLOF": hdlcLOF,
       "hdlcRxClockPolarity": hdlcRxClockPolarity,
       "dacsMux": dacsMux,
       "systemDacsMux": systemDacsMux,
       "sysStatus": sysStatus,
       "sysSClkSrc": sysSClkSrc,
       "sysConfig": sysConfig,
       "sysCClkSrcTable": sysCClkSrcTable,
       "sysCClkSrcEntry": sysCClkSrcEntry,
       "sysCClkCnfgIdx": sysCClkCnfgIdx,
       "sysCClkSrcIdx": sysCClkSrcIdx,
       "sysCClkSrcMode": sysCClkSrcMode,
       "sysCClkSrcPrt": sysCClkSrcPrt,
       "sysCClkStationFreq": sysCClkStationFreq,
       "sysCClkRevertiveTimeout": sysCClkRevertiveTimeout,
       "radBridges": radBridges,
       "genBridge": genBridge,
       "radBridgeAction": radBridgeAction,
       "radBridgeInactiveArpTimeOut": radBridgeInactiveArpTimeOut,
       "radBridgeMaskTable": radBridgeMaskTable,
       "radBridgeMaskEntry": radBridgeMaskEntry,
       "radBridgeMaskType": radBridgeMaskType,
       "radBridgeMaskIfIndex": radBridgeMaskIfIndex,
       "radBridgeMaskNum": radBridgeMaskNum,
       "radBridgeMaskDest": radBridgeMaskDest,
       "radBridgeMaskPat1": radBridgeMaskPat1,
       "radBridgeMaskActiveBit1": radBridgeMaskActiveBit1,
       "radBridgeMaskFrom1": radBridgeMaskFrom1,
       "radBridgeMaskOffset1": radBridgeMaskOffset1,
       "radBridgeMaskCond1": radBridgeMaskCond1,
       "radBridgeMaskPat2": radBridgeMaskPat2,
       "radBridgeMaskActiveBit2": radBridgeMaskActiveBit2,
       "radBridgeMaskFrom2": radBridgeMaskFrom2,
       "radBridgeMaskOffset2": radBridgeMaskOffset2,
       "radBridgeMaskCond2": radBridgeMaskCond2,
       "radBridgeMaskPat3": radBridgeMaskPat3,
       "radBridgeMaskActiveBit3": radBridgeMaskActiveBit3,
       "radBridgeMaskFrom3": radBridgeMaskFrom3,
       "radBridgeMaskOffset3": radBridgeMaskOffset3,
       "radBridgeMaskCond3": radBridgeMaskCond3,
       "radBridgeMaskOper": radBridgeMaskOper,
       "radBridgeCOD": radBridgeCOD,
       "radBridgeCODParamTable": radBridgeCODParamTable,
       "radBridgeCODEntry": radBridgeCODEntry,
       "radBridgeCODIfIndex": radBridgeCODIfIndex,
       "radBridgeCODManualConnect": radBridgeCODManualConnect,
       "radBridgeCODMode": radBridgeCODMode,
       "radBridgeCODConnectDelay": radBridgeCODConnectDelay,
       "radBridgeCODisConnectDelay": radBridgeCODisConnectDelay,
       "radBridgeCODImplicitSwitch": radBridgeCODImplicitSwitch,
       "radBridgeCODNumAccess": radBridgeCODNumAccess,
       "radBridgeCODTotalConnecTime": radBridgeCODTotalConnecTime,
       "radBridgeCODTimeTriggerTable": radBridgeCODTimeTriggerTable,
       "radBridgeCODTimeTriggerEntry": radBridgeCODTimeTriggerEntry,
       "radBridgeCODTimeIfIndex": radBridgeCODTimeIfIndex,
       "radBridgeCODDay": radBridgeCODDay,
       "radBridgeCODTimeTriggerNum": radBridgeCODTimeTriggerNum,
       "radBridgeCODTimeTriggerFrom": radBridgeCODTimeTriggerFrom,
       "radBridgeCODTimeTriggerTo": radBridgeCODTimeTriggerTo,
       "radBridgeCODTimeTriggerStatus": radBridgeCODTimeTriggerStatus,
       "radBridgeCODTraffic": radBridgeCODTraffic,
       "radBridgeCODTrafficTable": radBridgeCODTrafficTable,
       "radBridgeCODTrafficEntry": radBridgeCODTrafficEntry,
       "radBridgeCODProtocolType": radBridgeCODProtocolType,
       "radBridgeCODTrafficTriggerStatus": radBridgeCODTrafficTriggerStatus,
       "radBridgeCODRemoteIPAddr": radBridgeCODRemoteIPAddr,
       "radBridgeCODIPMask": radBridgeCODIPMask,
       "radBridgeCODTrafficTriggerProtType": radBridgeCODTrafficTriggerProtType,
       "radBridgeCODCondTable": radBridgeCODCondTable,
       "radBridgeCODCondEntry": radBridgeCODCondEntry,
       "radBridgeCODCondIfIndex": radBridgeCODCondIfIndex,
       "radBridgeCODOriginateConnectCondition": radBridgeCODOriginateConnectCondition,
       "radBridgeCODOriginateDisConnectCondition": radBridgeCODOriginateDisConnectCondition,
       "radBridgeCODOriginateDisConnectDelay": radBridgeCODOriginateDisConnectDelay,
       "radBridgeCODAnswerConnectCondition": radBridgeCODAnswerConnectCondition,
       "radBridgeCODSpecificOnTrafficOIDCondition": radBridgeCODSpecificOnTrafficOIDCondition,
       "radBridgeCODDisConnectMinimunFramesNumber": radBridgeCODDisConnectMinimunFramesNumber,
       "radBridgeIPX": radBridgeIPX,
       "radBridgeIPXdriver": radBridgeIPXdriver,
       "radBridgeIPXForwarding": radBridgeIPXForwarding,
       "radBridgeIPXRip": radBridgeIPXRip,
       "radBridgeIPXRipOutPackets": radBridgeIPXRipOutPackets,
       "radBridgeIPXRipInPackets": radBridgeIPXRipInPackets,
       "radBridgeIPXRipInDiscards": radBridgeIPXRipInDiscards,
       "radBridgeIPXRipTblNoOfEntries": radBridgeIPXRipTblNoOfEntries,
       "radBridgeIPXRipTblBcastTrigUpdateInterval": radBridgeIPXRipTblBcastTrigUpdateInterval,
       "radBridgeIPXRipTable": radBridgeIPXRipTable,
       "radBridgeIPXRipTableEntry": radBridgeIPXRipTableEntry,
       "radBridgeIPXRipDestNetwork": radBridgeIPXRipDestNetwork,
       "radBridgeIPXRipPolicy": radBridgeIPXRipPolicy,
       "radBridgeIPXRipForwardingRouter": radBridgeIPXRipForwardingRouter,
       "radBridgeIPXRipNIC": radBridgeIPXRipNIC,
       "radBridgeIPXRipTickMetric": radBridgeIPXRipTickMetric,
       "radBridgeIPXRipHopMetric": radBridgeIPXRipHopMetric,
       "radBridgeIPXRipAgingTime": radBridgeIPXRipAgingTime,
       "radBridgeIPXRipValueStatus": radBridgeIPXRipValueStatus,
       "radBridgeIPXRipForwardType": radBridgeIPXRipForwardType,
       "radBridgeIPXRipInfTable": radBridgeIPXRipInfTable,
       "radBridgeIPXRipInfEntry": radBridgeIPXRipInfEntry,
       "radBridgeIPXRipInfIfIndex": radBridgeIPXRipInfIfIndex,
       "radBridgeIPXRipInfBcastUpdate": radBridgeIPXRipInfBcastUpdate,
       "radBridgeIPXRipInfAgeMultiplier": radBridgeIPXRipInfAgeMultiplier,
       "radBridgeIPXSap": radBridgeIPXSap,
       "radBridgeIPXSapOutPackets": radBridgeIPXSapOutPackets,
       "radBridgeIPXSapInPackets": radBridgeIPXSapInPackets,
       "radBridgeIPXSapInDiscards": radBridgeIPXSapInDiscards,
       "radBridgeIPXSapTblNoOfEntries": radBridgeIPXSapTblNoOfEntries,
       "radBridgeIPXSapTblBcastTrigUpdateInterval": radBridgeIPXSapTblBcastTrigUpdateInterval,
       "radBridgeIPXSapTable": radBridgeIPXSapTable,
       "radBridgeIPXSapTableEntry": radBridgeIPXSapTableEntry,
       "radBridgeIPXSapServerType": radBridgeIPXSapServerType,
       "radBridgeIPXSapName": radBridgeIPXSapName,
       "radBridgeIPXSapNetwork": radBridgeIPXSapNetwork,
       "radBridgeIPXSapNode": radBridgeIPXSapNode,
       "radBridgeIPXSapSocket": radBridgeIPXSapSocket,
       "radBridgeIPXSapHopsToServer": radBridgeIPXSapHopsToServer,
       "radBridgeIPXSapNIC": radBridgeIPXSapNIC,
       "radBridgeIPXSapAgingTime": radBridgeIPXSapAgingTime,
       "radBridgeIPXSapStatus": radBridgeIPXSapStatus,
       "radBridgeIPXSapInfTable": radBridgeIPXSapInfTable,
       "radBridgeIPXSapInfEntry": radBridgeIPXSapInfEntry,
       "radBridgeIPXSapInfIfIndex": radBridgeIPXSapInfIfIndex,
       "radBridgeIPXSapInfBcastUpdate": radBridgeIPXSapInfBcastUpdate,
       "radBridgeIPXSapInfAgeMultiplier": radBridgeIPXSapInfAgeMultiplier,
       "newMasking": newMasking,
       "maskingMaxEntries": maskingMaxEntries,
       "maskingCurrentEntries": maskingCurrentEntries,
       "maskingTable": maskingTable,
       "maskingEntry": maskingEntry,
       "maskingType": maskingType,
       "maskingIfIndex": maskingIfIndex,
       "maskingIndex": maskingIndex,
       "maskingProtocolType": maskingProtocolType,
       "maskingSmartMaskOID": maskingSmartMaskOID,
       "maskingFrameType": maskingFrameType,
       "maskingFrameTypeCondition": maskingFrameTypeCondition,
       "maskingSourceAddress": maskingSourceAddress,
       "maskingSourceActiveBits": maskingSourceActiveBits,
       "maskingSourceMacOrNet": maskingSourceMacOrNet,
       "maskingSourceCondition": maskingSourceCondition,
       "maskingDestAddress": maskingDestAddress,
       "maskingDestActiveBits": maskingDestActiveBits,
       "maskingDestMacOrNet": maskingDestMacOrNet,
       "maskingDestCondition": maskingDestCondition,
       "maskingLowLevelProt": maskingLowLevelProt,
       "maskingLowLevelProtCondition": maskingLowLevelProtCondition,
       "maskingHighLevelProt": maskingHighLevelProt,
       "maskingHighLevelProtCondition": maskingHighLevelProtCondition,
       "maskingPortNum": maskingPortNum,
       "maskingPortNumCondition": maskingPortNumCondition,
       "maskingOperation": maskingOperation,
       "maskingSrcPortNum": maskingSrcPortNum,
       "maskingSrcPortNumCondition": maskingSrcPortNumCondition,
       "radConverters": radConverters,
       "radGen": radGen,
       "systems": systems,
       "systemsEvents": systemsEvents,
       "tftpStatusChangeTrap": tftpStatusChangeTrap,
       "agnStatusChangeTrap": agnStatusChangeTrap,
       "prtStatusChangeTrap": prtStatusChangeTrap,
       "swdlStatusResult": swdlStatusResult,
       "intSwdlSlotFileMismatch": intSwdlSlotFileMismatch,
       "agnCounterChange": agnCounterChange,
       "prtClkSrcChangeTrap": prtClkSrcChangeTrap,
       "moduleFailTrap": moduleFailTrap,
       "moduleInitFailTrap": moduleInitFailTrap,
       "clkSrcChangeTrap": clkSrcChangeTrap,
       "agnUploadDataTrap": agnUploadDataTrap,
       "enrollmentTrap": enrollmentTrap,
       "agnPowerFailureTrap": agnPowerFailureTrap,
       "radSysTR": radSysTR,
       "radRADring": radRADring,
       "radTMA": radTMA,
       "radRingMonitor": radRingMonitor,
       "radSysFddi": radSysFddi,
       "radFDX100": radFDX100,
       "radSysWan": radSysWan,
       "radSysWanEvents": radSysWanEvents,
       "radMP2100": radMP2100,
       "radMP2104": radMP2104,
       "radMP2100B": radMP2100B,
       "radMP2100F": radMP2100F,
       "radMP2100H": radMP2100H,
       "radMP2104H": radMP2104H,
       "radMP2200B": radMP2200B,
       "radMP2200F": radMP2200F,
       "radMX3000": radMX3000,
       "radMX3004": radMX3004,
       "radMX30": radMX30,
       "radMX300": radMX300,
       "radVOIP": radVOIP,
       "radKM2100": radKM2100,
       "radKM2104": radKM2104,
       "radDXC30": radDXC30,
       "radDXC10A": radDXC10A,
       "radDXC8R": radDXC8R,
       "radDXC30E": radDXC30E,
       "radDXC3000": radDXC3000,
       "radDXC8RNew": radDXC8RNew,
       "radFcdE1L": radFcdE1L,
       "radFcdT1": radFcdT1,
       "radFcdE1": radFcdE1,
       "radFcdE1I": radFcdE1I,
       "radFcdT1M": radFcdT1M,
       "radFcdE1M": radFcdE1M,
       "radFcdIP": radFcdIP,
       "radFcdT1A": radFcdT1A,
       "radFcdE1A": radFcdE1A,
       "radFcdW": radFcdW,
       "radFcdSTM": radFcdSTM,
       "radHtuE1Sa": radHtuE1Sa,
       "radHtuE1": radHtuE1,
       "radHtu2Sa": radHtu2Sa,
       "radHtu2": radHtu2,
       "radAsmi450R768Sa": radAsmi450R768Sa,
       "radAsmi450R768": radAsmi450R768,
       "radAsmi450R1152Sa": radAsmi450R1152Sa,
       "radAsmi450R1152": radAsmi450R1152,
       "radLrs12F": radLrs12F,
       "radLrs12B": radLrs12B,
       "radHcdE1Sa": radHcdE1Sa,
       "radHcdE1": radHcdE1,
       "radHtuT1Sa": radHtuT1Sa,
       "radHtuT1": radHtuT1,
       "radOptimux4E1": radOptimux4E1,
       "radOptimux4T1": radOptimux4T1,
       "radOptimuxXLE1": radOptimuxXLE1,
       "radOptimuxXLT1": radOptimuxXLT1,
       "radOptimuxXL16E1": radOptimuxXL16E1,
       "radImx64": radImx64,
       "radImx6L": radImx6L,
       "radImx2": radImx2,
       "radImx4T1": radImx4T1,
       "radImx4E1": radImx4E1,
       "radImx2T1E1": radImx2T1E1,
       "radOptimux4T1L": radOptimux4T1L,
       "radOptimux4E1L": radOptimux4E1L,
       "radHtuE1SaV2": radHtuE1SaV2,
       "radHtuE1V2": radHtuE1V2,
       "radFomiE3": radFomiE3,
       "radFomiT3": radFomiT3,
       "radOpt4E1C": radOpt4E1C,
       "radOpt4T1C": radOpt4T1C,
       "radPrbiE3": radPrbiE3,
       "radPrbiT3": radPrbiT3,
       "radHcd4Sa": radHcd4Sa,
       "radOptimuxT3": radOptimuxT3,
       "radFRmon": radFRmon,
       "radIpMux4": radIpMux4,
       "radIpMux1": radIpMux1,
       "radIpMux16": radIpMux16,
       "radIpMux1E": radIpMux1E,
       "radVmux2100": radVmux2100,
       "radSysBRG": radSysBRG,
       "radTRE1": radTRE1,
       "radTRE1D": radTRE1D,
       "radTRE8": radTRE8,
       "radTRE8D": radTRE8D,
       "radMBE1": radMBE1,
       "radMBE1D": radMBE1D,
       "radMBE8": radMBE8,
       "radMBE8D": radMBE8D,
       "radMLBT": radMLBT,
       "radFEB4DAS": radFEB4DAS,
       "radTrimBrg10": radTrimBrg10,
       "radTrimBrg16": radTrimBrg16,
       "radRRTRE8": radRRTRE8,
       "radRRTRE8D": radRRTRE8D,
       "radRRMLBT": radRRMLBT,
       "radRRMLBTF": radRRMLBTF,
       "radRRTRE1D": radRRTRE1D,
       "radTRERAS": radTRERAS,
       "radTRERASa": radTRERASa,
       "radMBERAS": radMBERAS,
       "radMBERASa": radMBERASa,
       "radFEB4FDX": radFEB4FDX,
       "radFEB4SAS": radFEB4SAS,
       "radRRFTBDAS": radRRFTBDAS,
       "radRRFTBSAS": radRRFTBSAS,
       "radFTBDAS": radFTBDAS,
       "radFTBSAS": radFTBSAS,
       "radFastWay100": radFastWay100,
       "radSysCnvrtr": radSysCnvrtr,
       "radSTC1": radSTC1,
       "radSTC2": radSTC2,
       "radSTC1UDP": radSTC1UDP,
       "radSTC2UDP": radSTC2UDP,
       "radFTC1": radFTC1,
       "radFTC2": radFTC2,
       "radFTC1UDP": radFTC1UDP,
       "radFTC2UDP": radFTC2UDP,
       "radSEC1": radSEC1,
       "radSEC2": radSEC2,
       "radSEC1UDP": radSEC1UDP,
       "radSEC2UDP": radSEC2UDP,
       "radFEC1": radFEC1,
       "radFEC2": radFEC2,
       "radFEC1UDP": radFEC1UDP,
       "radFEC2UDP": radFEC2UDP,
       "radSysStkHub": radSysStkHub,
       "radRBHE": radRBHE,
       "radRBHEEvents": radRBHEEvents,
       "radRBHT": radRBHT,
       "radRBHTEvents": radRBHTEvents,
       "radETS4fddiDAS": radETS4fddiDAS,
       "radETS4fddiSAS": radETS4fddiSAS,
       "radSAHEMX": radSAHEMX,
       "radSAHTM": radSAHTM,
       "radETS4": radETS4,
       "radSAHEMU": radSAHEMU,
       "unknown": unknown,
       "radSAH16Eint": radSAH16Eint,
       "radSAH16Tint": radSAH16Tint,
       "radSAH16Eext": radSAH16Eext,
       "radSAH16Text": radSAH16Text,
       "radSysPS": radSysPS,
       "radSysPSEvents": radSysPSEvents,
       "radSPS2": radSPS2,
       "radSPS3": radSPS3,
       "radSPS6": radSPS6,
       "radSPS9": radSPS9,
       "radSPS12": radSPS12,
       "radAPD2": radAPD2,
       "radAPD8": radAPD8,
       "radAPS8": radAPS8,
       "radAPS16": radAPS16,
       "radAPS24": radAPS24,
       "radSPS3S": radSPS3S,
       "radFPS8": radFPS8,
       "radFPS12": radFPS12,
       "radSPS3ScSL": radSPS3ScSL,
       "radSPS3Sc2S": radSPS3Sc2S,
       "radFPS8c": radFPS8c,
       "radFPS4": radFPS4,
       "radSysEth": radSysEth,
       "radEP8T": radEP8T,
       "radEP4TAUI": radEP4TAUI,
       "radEP4T2FL": radEP4T2FL,
       "radEP4TFL": radEP4TFL,
       "radEP4FL": radEP4FL,
       "radEPR8T": radEPR8T,
       "radEPR4TAUI": radEPR4TAUI,
       "radEPR4T2FL": radEPR4T2FL,
       "radEPR4TFL": radEPR4TFL,
       "radEPR4FL": radEPR4FL,
       "radSysRtr": radSysRtr,
       "radSysRtrEvents": radSysRtrEvents,
       "radRTED": radRTED,
       "radRTEM": radRTEM,
       "radRTEC": radRTEC,
       "radWebRanger": radWebRanger,
       "radTinyRouter": radTinyRouter,
       "radLA240": radLA240,
       "radSuperLan": radSuperLan,
       "radLA240I": radLA240I,
       "radFcdIsdn": radFcdIsdn,
       "radEFcdIp": radEFcdIp,
       "radFcdIpD": radFcdIpD,
       "radFcdIpM": radFcdIpM,
       "radSysAtm": radSysAtm,
       "radSysAtmEvents": radSysAtmEvents,
       "atmAceSystemTrap": atmAceSystemTrap,
       "atmAceAlarmLOS": atmAceAlarmLOS,
       "atmAceAlarmLOF": atmAceAlarmLOF,
       "atmAceAlarmLCD": atmAceAlarmLCD,
       "atmAceAlarmSLM": atmAceAlarmSLM,
       "atmAceAlarmLOP": atmAceAlarmLOP,
       "atmAceAlarmLineAIS": atmAceAlarmLineAIS,
       "atmAceAlarmPathAIS": atmAceAlarmPathAIS,
       "atmAceAlarmLineRDI": atmAceAlarmLineRDI,
       "atmAceAlarmPathRDI": atmAceAlarmPathRDI,
       "atmAceAlarmSectionBIP": atmAceAlarmSectionBIP,
       "atmAceAlarmLineBIP": atmAceAlarmLineBIP,
       "atmAceAlarmPathBIP": atmAceAlarmPathBIP,
       "atmAceAlarmLineFEBE": atmAceAlarmLineFEBE,
       "atmAceAlarmPathFEBE": atmAceAlarmPathFEBE,
       "atmAceAlarmPlcpLOF": atmAceAlarmPlcpLOF,
       "atmAceAlarmPlcpYELLOW": atmAceAlarmPlcpYELLOW,
       "atmAceAlarmPlcpBIP": atmAceAlarmPlcpBIP,
       "atmAceAlarmPlcpFEBE": atmAceAlarmPlcpFEBE,
       "atmAceAlarmPlcpP1P2": atmAceAlarmPlcpP1P2,
       "atmAceAlarmUAS": atmAceAlarmUAS,
       "atmAceAlarmCluster": atmAceAlarmCluster,
       "atmAceAlarmVpContinuityLoss": atmAceAlarmVpContinuityLoss,
       "atmAceAlarmVpAISReception": atmAceAlarmVpAISReception,
       "atmAceAlarmVpRDIReception": atmAceAlarmVpRDIReception,
       "atmAceAlarmVpErroredCells": atmAceAlarmVpErroredCells,
       "atmAceAlarmVpLostCells": atmAceAlarmVpLostCells,
       "atmAceAlarmVpMisinsertedCells": atmAceAlarmVpMisinsertedCells,
       "atmAceAlarmVpUAS": atmAceAlarmVpUAS,
       "atmAceAlarmVpLoopback": atmAceAlarmVpLoopback,
       "atmAceAlarmVpGCRAViolation": atmAceAlarmVpGCRAViolation,
       "atmAceAlarmVcContinuityLoss": atmAceAlarmVcContinuityLoss,
       "atmAceAlarmVcAISReception": atmAceAlarmVcAISReception,
       "atmAceAlarmVcRDIReception": atmAceAlarmVcRDIReception,
       "atmAceAlarmVcErroredCells": atmAceAlarmVcErroredCells,
       "atmAceAlarmVcLostCells": atmAceAlarmVcLostCells,
       "atmAceAlarmVcMisinsertedCells": atmAceAlarmVcMisinsertedCells,
       "atmAceAlarmVcUnexpectedCell": atmAceAlarmVcUnexpectedCell,
       "atmAceAlarmVcUAS": atmAceAlarmVcUAS,
       "atmAceAlarmVcLoopback": atmAceAlarmVcLoopback,
       "atmAceAlarmVcGCRAViolation": atmAceAlarmVcGCRAViolation,
       "atmImaGroupStatusChangeTrap": atmImaGroupStatusChangeTrap,
       "radStarSwitch": radStarSwitch,
       "radStarSwitchATM25": radStarSwitchATM25,
       "radStarSwitchATM25L": radStarSwitchATM25L,
       "radStarSwitchATM155": radStarSwitchATM155,
       "radAtmCsuDsu": radAtmCsuDsu,
       "radAmcdE1": radAmcdE1,
       "radAmcdT1": radAmcdT1,
       "radAce20E": radAce20E,
       "radAce20T": radAce20T,
       "radAce2005": radAce2005,
       "radAce2002": radAce2002,
       "radAce2002E": radAce2002E,
       "radAce2E": radAce2E,
       "radAce2T": radAce2T,
       "radMlAtmE1": radMlAtmE1,
       "radMlAtmT1": radMlAtmT1,
       "radAmc102": radAmc102,
       "radAmc102c": radAmc102c,
       "radAce202": radAce202,
       "radAce": radAce,
       "radAce101": radAce101,
       "radAce102": radAce102,
       "radAce50": radAce50,
       "radSysLA": radSysLA,
       "radLA140": radLA140,
       "radLA110": radLA110,
       "agnt": agnt,
       "agnHwVersion": agnHwVersion,
       "agnTrapMask": agnTrapMask,
       "agnTrapValue": agnTrapValue,
       "agnChangeCnt": agnChangeCnt,
       "agnSpecific": agnSpecific,
       "agnConfigMsg": agnConfigMsg,
       "mngTrapIpTable": mngTrapIpTable,
       "mngEntry": mngEntry,
       "mngID": mngID,
       "mngIP": mngIP,
       "mngIPMask": mngIPMask,
       "mngTrapMask": mngTrapMask,
       "agnIndication": agnIndication,
       "agnMonitorModeCmd": agnMonitorModeCmd,
       "agnLed": agnLed,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapID": trapID,
       "trapVal": trapVal,
       "trapTimeSinceOccurrence": trapTimeSinceOccurrence,
       "fileTransfer": fileTransfer,
       "fileServerIP": fileServerIP,
       "fileName": fileName,
       "fileTransCmd": fileTransCmd,
       "tftpRetryTimeOut": tftpRetryTimeOut,
       "tftpTotalTimeOut": tftpTotalTimeOut,
       "tftpStatus": tftpStatus,
       "tftpError": tftpError,
       "fileTransferToSubSystems": fileTransferToSubSystems,
       "fileNameWithinProduct": fileNameWithinProduct,
       "intSwdlTable": intSwdlTable,
       "intSwdlEntry": intSwdlEntry,
       "intSwdlObjIdx": intSwdlObjIdx,
       "intSwdlFileIdx": intSwdlFileIdx,
       "intSwdlFileName": intSwdlFileName,
       "intSwdlFileSwVer": intSwdlFileSwVer,
       "intSwdlSwDate": intSwdlSwDate,
       "intSwdlSize": intSwdlSize,
       "intSwdlCmd": intSwdlCmd,
       "intSwdlToSubSystem": intSwdlToSubSystem,
       "swdlStatusTable": swdlStatusTable,
       "swdlStatusEntry": swdlStatusEntry,
       "swdlStatusTypeIdx": swdlStatusTypeIdx,
       "swdlStatusIdx": swdlStatusIdx,
       "swdlStatusFileName": swdlStatusFileName,
       "swdlStatusSlot": swdlStatusSlot,
       "swdlStatusSubSystem": swdlStatusSubSystem,
       "swdlStatusStatus": swdlStatusStatus,
       "swdlStatusTime": swdlStatusTime,
       "clearDwldStatusLog": clearDwldStatusLog,
       "systemReset": systemReset,
       "systemTiming": systemTiming,
       "systemDate": systemDate,
       "systemTime": systemTime,
       "systemPort": systemPort,
       "physicalConnectorTable": physicalConnectorTable,
       "physicalConnectorEntry": physicalConnectorEntry,
       "portIdx": portIdx,
       "physicalConnector": physicalConnector,
       "portOptWaveLength": portOptWaveLength,
       "portOptMode": portOptMode,
       "prtSupervisory": prtSupervisory,
       "prtSpTable": prtSpTable,
       "prtSpEntry": prtSpEntry,
       "prtSupervisoryIndex": prtSupervisoryIndex,
       "prtSupervisoryRate": prtSupervisoryRate,
       "prtSupervisoryDataBits": prtSupervisoryDataBits,
       "prtSupervisoryParity": prtSupervisoryParity,
       "prtSupervisoryStopBits": prtSupervisoryStopBits,
       "prtSupervisoryUsage": prtSupervisoryUsage,
       "prtSupervisoryInterface": prtSupervisoryInterface,
       "prtSupervisoryCTS": prtSupervisoryCTS,
       "prtSupervisoryDcdDelay": prtSupervisoryDcdDelay,
       "prtSupervisoryDSR": prtSupervisoryDSR,
       "prtSupervisoryRoutProtocol": prtSupervisoryRoutProtocol,
       "prtPerformance": prtPerformance,
       "prtPerfTable": prtPerfTable,
       "prtPerfEntry": prtPerfEntry,
       "prtPerfIdx": prtPerfIdx,
       "prtPerfPeriodRef": prtPerfPeriodRef,
       "prtPerfElapsedTime": prtPerfElapsedTime,
       "prtPerfUAS": prtPerfUAS,
       "prtPerfES": prtPerfES,
       "prtPerfSES": prtPerfSES,
       "prtPerfBBE": prtPerfBBE,
       "prtPerfBlocksPerSec": prtPerfBlocksPerSec,
       "prtPerfTimeTag": prtPerfTimeTag,
       "prtPerfSaveAndResetCmd": prtPerfSaveAndResetCmd,
       "prtTest": prtTest,
       "prtTestTable": prtTestTable,
       "prtTestEntry": prtTestEntry,
       "prtTestIdx": prtTestIdx,
       "prtTestCmdAndStatus": prtTestCmdAndStatus,
       "prtBertCounter": prtBertCounter,
       "prtTestInitiator": prtTestInitiator,
       "prtParam": prtParam,
       "prtParamTable": prtParamTable,
       "prtParamEntry": prtParamEntry,
       "prtParamIdx": prtParamIdx,
       "prtControlCnfg": prtControlCnfg,
       "prtParamClkSrc": prtParamClkSrc,
       "prtParamPhantom": prtParamPhantom,
       "prtParamResetStatsCmd": prtParamResetStatsCmd,
       "prtParamLastResetStatsTime": prtParamLastResetStatsTime,
       "prtIP": prtIP,
       "prtIpParamTable": prtIpParamTable,
       "prtIpParamEntry": prtIpParamEntry,
       "prtIpParamConfigIdx": prtIpParamConfigIdx,
       "prtIpParamSlotIdx": prtIpParamSlotIdx,
       "prtIpParamIdx": prtIpParamIdx,
       "prtIpParamHostIP": prtIpParamHostIP,
       "prtIpParamHostMask": prtIpParamHostMask,
       "prtIpParamDefaultGateway": prtIpParamDefaultGateway,
       "prtIpParamMediaMode": prtIpParamMediaMode,
       "prtIpParamMediaRate": prtIpParamMediaRate,
       "prtIpParamMngVlanSupport": prtIpParamMngVlanSupport,
       "prtIpParamMngVlanId": prtIpParamMngVlanId,
       "prtIpParamMngVlanPriority": prtIpParamMngVlanPriority,
       "prtIpParamRingMode": prtIpParamRingMode,
       "systemResetAllStatsCmd": systemResetAllStatsCmd,
       "systemClearTablesCmd": systemClearTablesCmd,
       "systemParameter": systemParameter,
       "agnGlobalAlarmMask": agnGlobalAlarmMask,
       "alarmSeverity": alarmSeverity,
       "alarmState": alarmState,
       "agnTestStatus": agnTestStatus,
       "systemSaveAndResetAllStatsCmd": systemSaveAndResetAllStatsCmd,
       "systemDefaultGateway": systemDefaultGateway,
       "systemPsTable": systemPsTable,
       "systemPsEntry": systemPsEntry,
       "systemPsIndex1": systemPsIndex1,
       "systemPsIndex2": systemPsIndex2,
       "systemPsType": systemPsType,
       "systemPsStatus": systemPsStatus,
       "xcIndexNext": xcIndexNext,
       "xcTable": xcTable,
       "xcEntry": xcEntry,
       "xcIndex": xcIndex,
       "xcIfIndex1": xcIfIndex1,
       "xcVpi": xcVpi,
       "xcVci": xcVci,
       "xcIfIndex2": xcIfIndex2,
       "xcRowStatus": xcRowStatus,
       "xcDescr": xcDescr,
       "xcAdminStatus": xcAdminStatus,
       "xcOperStatus": xcOperStatus,
       "systemModule": systemModule,
       "modlParam": modlParam,
       "modlParamTable": modlParamTable,
       "modlParamEntry": modlParamEntry,
       "modlParamIndex": modlParamIndex,
       "modlParamReset": modlParamReset,
       "modlParamSwdlStatus": modlParamSwdlStatus,
       "agnNearFarConnection": agnNearFarConnection,
       "radStkHub": radStkHub,
       "radRouter": radRouter,
       "rtrBridge": rtrBridge,
       "ipRouter": ipRouter,
       "rtrIfIpTable": rtrIfIpTable,
       "rtrIfIpEntry": rtrIfIpEntry,
       "rtrIfIp": rtrIfIp,
       "rtrIfRowStatus": rtrIfRowStatus,
       "rtrIfIpMask": rtrIfIpMask,
       "rtrIfIndex": rtrIfIndex,
       "rtrIfMng": rtrIfMng,
       "brtrIfTable": brtrIfTable,
       "brtrIfEntry": brtrIfEntry,
       "brtrIfIndex": brtrIfIndex,
       "brtrIfMode": brtrIfMode,
       "brtrIfMaxFrameSize": brtrIfMaxFrameSize,
       "rtrArpAgingTime": rtrArpAgingTime,
       "brtrLanIfTable": brtrLanIfTable,
       "brtrLanIfEntry": brtrLanIfEntry,
       "brtrLanIfIndex": brtrLanIfIndex,
       "brtrLanIpAddress": brtrLanIpAddress,
       "brtrLanIpMask": brtrLanIpMask,
       "brtrLanMaxRateEnable": brtrLanMaxRateEnable,
       "brtrLanMaxRate": brtrLanMaxRate,
       "brtrLanMng": brtrLanMng,
       "brtrLanDefaultRouter": brtrLanDefaultRouter,
       "rtrIsdnIfTable": rtrIsdnIfTable,
       "rtrIsdnIfEntry": rtrIsdnIfEntry,
       "rtrIsdnIfMinNumBchans": rtrIsdnIfMinNumBchans,
       "rtrIsdnIfMaxNumBchans": rtrIsdnIfMaxNumBchans,
       "rtrLcrTable": rtrLcrTable,
       "rtrLcrEntry": rtrLcrEntry,
       "rtrLcrOutIfIndex": rtrLcrOutIfIndex,
       "rtrLcrRowStatus": rtrLcrRowStatus,
       "rtrLcrInPrefix": rtrLcrInPrefix,
       "rtrLcrOutPrefix": rtrLcrOutPrefix,
       "multicastGen": multicastGen,
       "multicastMode": multicastMode,
       "radAtm": radAtm,
       "atmGen": atmGen,
       "atmPerfHistory": atmPerfHistory,
       "atmIfPerformance": atmIfPerformance,
       "atmIfDataTable": atmIfDataTable,
       "atmIfDataEntry": atmIfDataEntry,
       "atmIfTimeElapsed": atmIfTimeElapsed,
       "atmIfValidIntervals": atmIfValidIntervals,
       "atmIfCurrentTable": atmIfCurrentTable,
       "atmIfCurrentEntry": atmIfCurrentEntry,
       "atmIfCurrentTxCells": atmIfCurrentTxCells,
       "atmIfCurrentRxCells": atmIfCurrentRxCells,
       "atmIfCurrentCorrectedHecs": atmIfCurrentCorrectedHecs,
       "atmIfCurrentUncorrectedHecs": atmIfCurrentUncorrectedHecs,
       "atmIfIntervalTable": atmIfIntervalTable,
       "atmIfIntervalEntry": atmIfIntervalEntry,
       "atmIfIntervalNumber": atmIfIntervalNumber,
       "atmIfIntervalTxCells": atmIfIntervalTxCells,
       "atmIfIntervalRxCells": atmIfIntervalRxCells,
       "atmIfIntervalCorrectedHecs": atmIfIntervalCorrectedHecs,
       "atmIfIntervalUncorrectedHecs": atmIfIntervalUncorrectedHecs,
       "aal5VccXTable": aal5VccXTable,
       "aal5VccXEntry": aal5VccXEntry,
       "aal5VccInFrames": aal5VccInFrames,
       "aal5VccOutFrames": aal5VccOutFrames,
       "aal5VccUnknownProtocolFrames": aal5VccUnknownProtocolFrames,
       "atmPvcPerformance": atmPvcPerformance,
       "atmVpPerformance": atmVpPerformance,
       "atmVpCurrentTable": atmVpCurrentTable,
       "atmVpCurrentEntry": atmVpCurrentEntry,
       "atmVpCurrentVpi": atmVpCurrentVpi,
       "atmVpCurrentRxCellsClp01": atmVpCurrentRxCellsClp01,
       "atmVpCurrentRxCellsClp0": atmVpCurrentRxCellsClp0,
       "atmVpCurrentGcra0Violations": atmVpCurrentGcra0Violations,
       "atmVpCurrentGcra1Violations": atmVpCurrentGcra1Violations,
       "atmVpCurrentRxAIS": atmVpCurrentRxAIS,
       "atmVpCurrentTxAIS": atmVpCurrentTxAIS,
       "atmVpCurrentRxRDI": atmVpCurrentRxRDI,
       "atmVpCurrentTxRDI": atmVpCurrentTxRDI,
       "atmVpCurrentContinuityLoss": atmVpCurrentContinuityLoss,
       "atmVpCurrentUAS": atmVpCurrentUAS,
       "atmVpCurrentSES": atmVpCurrentSES,
       "atmVpCurrentCDC": atmVpCurrentCDC,
       "atmVpCurrentTotalDiscards": atmVpCurrentTotalDiscards,
       "atmVpCurrentClp0Discards": atmVpCurrentClp0Discards,
       "atmVpCurrentTotalCellOuts": atmVpCurrentTotalCellOuts,
       "atmVpCurrentClp0CellOuts": atmVpCurrentClp0CellOuts,
       "atmVpCurrentTaggedOuts": atmVpCurrentTaggedOuts,
       "atmVpCurrentPCR": atmVpCurrentPCR,
       "atmVpCurrentSCR": atmVpCurrentSCR,
       "atmVpCurrentMCR": atmVpCurrentMCR,
       "atmVpPMCurrentTable": atmVpPMCurrentTable,
       "atmVpPMCurrentEntry": atmVpPMCurrentEntry,
       "atmVpPMCurrentVpi": atmVpPMCurrentVpi,
       "atmVpPMCurrentDir": atmVpPMCurrentDir,
       "atmVpPMCurrentTxClp01": atmVpPMCurrentTxClp01,
       "atmVpPMCurrentTxClp0": atmVpPMCurrentTxClp0,
       "atmVpPMCurrentRxClp01": atmVpPMCurrentRxClp01,
       "atmVpPMCurrentRxClp0": atmVpPMCurrentRxClp0,
       "atmVpPMCurrentErroredCells": atmVpPMCurrentErroredCells,
       "atmVpPMCurrentLostCells": atmVpPMCurrentLostCells,
       "atmVpPMCurrentMisinsertedCells": atmVpPMCurrentMisinsertedCells,
       "atmVpPMCurrentECB": atmVpPMCurrentECB,
       "atmVpPMCurrentSECB": atmVpPMCurrentSECB,
       "atmVpPMCurrentES": atmVpPMCurrentES,
       "atmVpPMCurrentSES": atmVpPMCurrentSES,
       "atmVpPMCurrentUAS": atmVpPMCurrentUAS,
       "atmVpPMCurrentIntervalQuality": atmVpPMCurrentIntervalQuality,
       "atmVpPMCurrentLastDayQuality": atmVpPMCurrentLastDayQuality,
       "atmVpIntervalTable": atmVpIntervalTable,
       "atmVpIntervalEntry": atmVpIntervalEntry,
       "atmVpIntervalVpi": atmVpIntervalVpi,
       "atmVpIntervalNumber": atmVpIntervalNumber,
       "atmVpIntervalRxCellsClp01": atmVpIntervalRxCellsClp01,
       "atmVpIntervalRxCellsClp0": atmVpIntervalRxCellsClp0,
       "atmVpIntervalGcra0Violations": atmVpIntervalGcra0Violations,
       "atmVpIntervalGcra1Violations": atmVpIntervalGcra1Violations,
       "atmVpIntervalRxAIS": atmVpIntervalRxAIS,
       "atmVpIntervalTxAIS": atmVpIntervalTxAIS,
       "atmVpIntervalRxRDI": atmVpIntervalRxRDI,
       "atmVpIntervalTxRDI": atmVpIntervalTxRDI,
       "atmVpIntervalContinuityLoss": atmVpIntervalContinuityLoss,
       "atmVpIntervalUAS": atmVpIntervalUAS,
       "atmVpIntervalSES": atmVpIntervalSES,
       "atmVpIntervalCDC": atmVpIntervalCDC,
       "atmVpIntervalTotalDiscards": atmVpIntervalTotalDiscards,
       "atmVpIntervalClp0Discards": atmVpIntervalClp0Discards,
       "atmVpIntervalTotalCellOuts": atmVpIntervalTotalCellOuts,
       "atmVpIntervalClp0CellOuts": atmVpIntervalClp0CellOuts,
       "atmVpIntervalTaggedOuts": atmVpIntervalTaggedOuts,
       "atmVpIntervalPCR": atmVpIntervalPCR,
       "atmVpIntervalSCR": atmVpIntervalSCR,
       "atmVpIntervalMCR": atmVpIntervalMCR,
       "atmVpPMIntervalTable": atmVpPMIntervalTable,
       "atmVpPMIntervalEntry": atmVpPMIntervalEntry,
       "atmVpPMIntervalVpi": atmVpPMIntervalVpi,
       "atmVpPMIntervalDir": atmVpPMIntervalDir,
       "atmVpPMIntervalNumber": atmVpPMIntervalNumber,
       "atmVpPMIntervalTxClp01": atmVpPMIntervalTxClp01,
       "atmVpPMIntervalTxClp0": atmVpPMIntervalTxClp0,
       "atmVpPMIntervalRxClp01": atmVpPMIntervalRxClp01,
       "atmVpPMIntervalRxClp0": atmVpPMIntervalRxClp0,
       "atmVpPMIntervalErroredCells": atmVpPMIntervalErroredCells,
       "atmVpPMIntervalLostCells": atmVpPMIntervalLostCells,
       "atmVpPMIntervalMisinsertedCells": atmVpPMIntervalMisinsertedCells,
       "atmVpPMIntervalECB": atmVpPMIntervalECB,
       "atmVpPMIntervalSECB": atmVpPMIntervalSECB,
       "atmVpPMIntervalES": atmVpPMIntervalES,
       "atmVpPMIntervalSES": atmVpPMIntervalSES,
       "atmVpPMIntervalUAS": atmVpPMIntervalUAS,
       "atmVpPMIntervalQuality": atmVpPMIntervalQuality,
       "atmVpPMIntervalLastDayQuality": atmVpPMIntervalLastDayQuality,
       "atmVpQoSTable": atmVpQoSTable,
       "atmVpQoSEntry": atmVpQoSEntry,
       "atmVpQoSPeriodRef": atmVpQoSPeriodRef,
       "atmVpQoSElapsedTime": atmVpQoSElapsedTime,
       "atmVpQoSUAS": atmVpQoSUAS,
       "atmVpPMQoSTable": atmVpPMQoSTable,
       "atmVpPMQoSEntry": atmVpPMQoSEntry,
       "atmVpPMQoSDirection": atmVpPMQoSDirection,
       "atmVpPMQoSPeriodRef": atmVpPMQoSPeriodRef,
       "atmVpPMQoSCLR": atmVpPMQoSCLR,
       "atmVpPMQoSCER": atmVpPMQoSCER,
       "atmVpPMQoSCMR": atmVpPMQoSCMR,
       "atmVpShaperStatTable": atmVpShaperStatTable,
       "atmVpShaperStatEntry": atmVpShaperStatEntry,
       "atmVpShaperDiscarded": atmVpShaperDiscarded,
       "atmVpShaperOccupation": atmVpShaperOccupation,
       "atmVpShaperMaxOccupation": atmVpShaperMaxOccupation,
       "atmVpShaperLevel": atmVpShaperLevel,
       "atmVpShaperEpdDropped": atmVpShaperEpdDropped,
       "atmVpShaperTotalEpdDropped": atmVpShaperTotalEpdDropped,
       "atmVcPerformance": atmVcPerformance,
       "atmVcCurrentTable": atmVcCurrentTable,
       "atmVcCurrentEntry": atmVcCurrentEntry,
       "atmVcCurrentVpi": atmVcCurrentVpi,
       "atmVcCurrentVci": atmVcCurrentVci,
       "atmVcCurrentRxCellsClp01": atmVcCurrentRxCellsClp01,
       "atmVcCurrentRxCellsClp0": atmVcCurrentRxCellsClp0,
       "atmVcCurrentGcra0Violations": atmVcCurrentGcra0Violations,
       "atmVcCurrentGcra1Violations": atmVcCurrentGcra1Violations,
       "atmVcCurrentRxAIS": atmVcCurrentRxAIS,
       "atmVcCurrentTxAIS": atmVcCurrentTxAIS,
       "atmVcCurrentRxRDI": atmVcCurrentRxRDI,
       "atmVcCurrentTxRDI": atmVcCurrentTxRDI,
       "atmVcCurrentContinuityLoss": atmVcCurrentContinuityLoss,
       "atmVcCurrentUAS": atmVcCurrentUAS,
       "atmVcCurrentSES": atmVcCurrentSES,
       "atmVcCurrentCDC": atmVcCurrentCDC,
       "atmVcCurrentTotalDiscards": atmVcCurrentTotalDiscards,
       "atmVcCurrentClp0Discards": atmVcCurrentClp0Discards,
       "atmVcCurrentTotalCellOuts": atmVcCurrentTotalCellOuts,
       "atmVcCurrentClp0CellOuts": atmVcCurrentClp0CellOuts,
       "atmVcCurrentTaggedOuts": atmVcCurrentTaggedOuts,
       "atmVcCurrentPCR": atmVcCurrentPCR,
       "atmVcCurrentSCR": atmVcCurrentSCR,
       "atmVcCurrentMCR": atmVcCurrentMCR,
       "atmVcPMCurrentTable": atmVcPMCurrentTable,
       "atmVcPMCurrentEntry": atmVcPMCurrentEntry,
       "atmVcPMCurrentVpi": atmVcPMCurrentVpi,
       "atmVcPMCurrentVci": atmVcPMCurrentVci,
       "atmVcPMCurrentDir": atmVcPMCurrentDir,
       "atmVcPMCurrentTxClp01": atmVcPMCurrentTxClp01,
       "atmVcPMCurrentTxClp0": atmVcPMCurrentTxClp0,
       "atmVcPMCurrentRxClp01": atmVcPMCurrentRxClp01,
       "atmVcPMCurrentRxClp0": atmVcPMCurrentRxClp0,
       "atmVcPMCurrentErroredCells": atmVcPMCurrentErroredCells,
       "atmVcPMCurrentLostCells": atmVcPMCurrentLostCells,
       "atmVcPMCurrentMisinsertedCells": atmVcPMCurrentMisinsertedCells,
       "atmVcPMCurrentECB": atmVcPMCurrentECB,
       "atmVcPMCurrentSECB": atmVcPMCurrentSECB,
       "atmVcPMCurrentES": atmVcPMCurrentES,
       "atmVcPMCurrentSES": atmVcPMCurrentSES,
       "atmVcPMCurrentUAS": atmVcPMCurrentUAS,
       "atmVcPMCurrentIntervalQuality": atmVcPMCurrentIntervalQuality,
       "atmVcPMCurrentLastDayQuality": atmVcPMCurrentLastDayQuality,
       "atmVcIntervalTable": atmVcIntervalTable,
       "atmVcIntervalEntry": atmVcIntervalEntry,
       "atmVcIntervalVpi": atmVcIntervalVpi,
       "atmVcIntervalVci": atmVcIntervalVci,
       "atmVcIntervalNumber": atmVcIntervalNumber,
       "atmVcIntervalRxCellsClp01": atmVcIntervalRxCellsClp01,
       "atmVcIntervalRxCellsClp0": atmVcIntervalRxCellsClp0,
       "atmVcIntervalGcra0Violations": atmVcIntervalGcra0Violations,
       "atmVcIntervalGcra1Violations": atmVcIntervalGcra1Violations,
       "atmVcIntervalRxAIS": atmVcIntervalRxAIS,
       "atmVcIntervalTxAIS": atmVcIntervalTxAIS,
       "atmVcIntervalRxRDI": atmVcIntervalRxRDI,
       "atmVcIntervalTxRDI": atmVcIntervalTxRDI,
       "atmVcIntervalContinuityLoss": atmVcIntervalContinuityLoss,
       "atmVcIntervalUAS": atmVcIntervalUAS,
       "atmVcIntervalSES": atmVcIntervalSES,
       "atmVcIntervalCDC": atmVcIntervalCDC,
       "atmVcIntervalTotalDiscards": atmVcIntervalTotalDiscards,
       "atmVcIntervalClp0Discards": atmVcIntervalClp0Discards,
       "atmVcIntervalTotalCellOuts": atmVcIntervalTotalCellOuts,
       "atmVcIntervalClp0CellOuts": atmVcIntervalClp0CellOuts,
       "atmVcIntervalTaggedOuts": atmVcIntervalTaggedOuts,
       "atmVcIntervalPCR": atmVcIntervalPCR,
       "atmVcIntervalSCR": atmVcIntervalSCR,
       "atmVcIntervalMCR": atmVcIntervalMCR,
       "atmVcPMIntervalTable": atmVcPMIntervalTable,
       "atmVcPMIntervalEntry": atmVcPMIntervalEntry,
       "atmVcPMIntervalVpi": atmVcPMIntervalVpi,
       "atmVcPMIntervalVci": atmVcPMIntervalVci,
       "atmVcPMIntervalDir": atmVcPMIntervalDir,
       "atmVcPMIntervalNumber": atmVcPMIntervalNumber,
       "atmVcPMIntervalTxClp01": atmVcPMIntervalTxClp01,
       "atmVcPMIntervalTxClp0": atmVcPMIntervalTxClp0,
       "atmVcPMIntervalRxClp01": atmVcPMIntervalRxClp01,
       "atmVcPMIntervalRxClp0": atmVcPMIntervalRxClp0,
       "atmVcPMIntervalErroredCells": atmVcPMIntervalErroredCells,
       "atmVcPMIntervalLostCells": atmVcPMIntervalLostCells,
       "atmVcPMIntervalMisinsertedCells": atmVcPMIntervalMisinsertedCells,
       "atmVcPMIntervalECB": atmVcPMIntervalECB,
       "atmVcPMIntervalSECB": atmVcPMIntervalSECB,
       "atmVcPMIntervalES": atmVcPMIntervalES,
       "atmVcPMIntervalSES": atmVcPMIntervalSES,
       "atmVcPMIntervalUAS": atmVcPMIntervalUAS,
       "atmVcPMIntervalQuality": atmVcPMIntervalQuality,
       "atmVcPMIntervalLastDayQuality": atmVcPMIntervalLastDayQuality,
       "atmVcQoSTable": atmVcQoSTable,
       "atmVcQoSEntry": atmVcQoSEntry,
       "atmVcQoSPeriodRef": atmVcQoSPeriodRef,
       "atmVcQoSElapsedTime": atmVcQoSElapsedTime,
       "atmVcQoSUAS": atmVcQoSUAS,
       "atmVcPMQoSTable": atmVcPMQoSTable,
       "atmVcPMQoSEntry": atmVcPMQoSEntry,
       "atmVcPMQoSDirection": atmVcPMQoSDirection,
       "atmVcPMQoSPeriodRef": atmVcPMQoSPeriodRef,
       "atmVcPMQoSCLR": atmVcPMQoSCLR,
       "atmVcPMQoSCER": atmVcPMQoSCER,
       "atmVcPMQoSCMR": atmVcPMQoSCMR,
       "atmVcShaperStatTable": atmVcShaperStatTable,
       "atmVcShaperStatEntry": atmVcShaperStatEntry,
       "atmVcShaperDiscarded": atmVcShaperDiscarded,
       "atmVcShaperOccupation": atmVcShaperOccupation,
       "atmVcShaperMaxOccupation": atmVcShaperMaxOccupation,
       "atmVcShaperLevel": atmVcShaperLevel,
       "atmVcShaperEpdDropped": atmVcShaperEpdDropped,
       "atmVcShaperTotalEpdDropped": atmVcShaperTotalEpdDropped,
       "atmIntervalDateTable": atmIntervalDateTable,
       "atmIntervalDateEntry": atmIntervalDateEntry,
       "atmIntervalDateInterval": atmIntervalDateInterval,
       "atmIntervalDateDate": atmIntervalDateDate,
       "atmIntervalDateTime": atmIntervalDateTime,
       "atmGenSystem": atmGenSystem,
       "atmGenSysGen": atmGenSysGen,
       "atmGenSysSelfTestTable": atmGenSysSelfTestTable,
       "atmGenSysSelfTestEntry": atmGenSysSelfTestEntry,
       "atmGenSysSelfTestIndex": atmGenSysSelfTestIndex,
       "atmGenSysSelfTestResult": atmGenSysSelfTestResult,
       "atmGenSysLogClearAll": atmGenSysLogClearAll,
       "atmGenSysLogTable": atmGenSysLogTable,
       "atmGenSysLogEntry": atmGenSysLogEntry,
       "atmGenSysLogIndex": atmGenSysLogIndex,
       "atmGenSysLogMessage": atmGenSysLogMessage,
       "atmGenSysSetDefaultConfg": atmGenSysSetDefaultConfg,
       "atmGenSysCxRefTable": atmGenSysCxRefTable,
       "atmGenSysCxRefEntry": atmGenSysCxRefEntry,
       "atmGenSysCxRefIndex": atmGenSysCxRefIndex,
       "atmGenSysCxRefCounter": atmGenSysCxRefCounter,
       "atmNte": atmNte,
       "atmNteEvents": atmNteEvents,
       "atmAceStatusChange": atmAceStatusChange,
       "atmAceAlarmTrap": atmAceAlarmTrap,
       "atmAceModuleChangeTrap": atmAceModuleChangeTrap,
       "atmAceRedundancyTrap": atmAceRedundancyTrap,
       "atmNteSys": atmNteSys,
       "atmNteSysConfig": atmNteSysConfig,
       "atmNteManagerTable": atmNteManagerTable,
       "atmNteManagerEntry": atmNteManagerEntry,
       "atmNteManagerIP": atmNteManagerIP,
       "atmNteManagerPvc": atmNteManagerPvc,
       "atmNteManagerIfIndex": atmNteManagerIfIndex,
       "atmNteManagerVpi": atmNteManagerVpi,
       "atmNteManagerVci": atmNteManagerVci,
       "atmNteManagerTrapMask": atmNteManagerTrapMask,
       "atmNteManagerRowStatus": atmNteManagerRowStatus,
       "atmNteManagerNextHop": atmNteManagerNextHop,
       "atmNteManagerVlanSupport": atmNteManagerVlanSupport,
       "atmNteManagerVlanIdentifier": atmNteManagerVlanIdentifier,
       "atmNteManagerVlanFramePriority": atmNteManagerVlanFramePriority,
       "atmNteUPLTCR": atmNteUPLTCR,
       "atmNteDPLTCR": atmNteDPLTCR,
       "atmNteSysLogClearAll": atmNteSysLogClearAll,
       "atmNteUSESLTCR": atmNteUSESLTCR,
       "atmNteDSESLTCR": atmNteDSESLTCR,
       "atmNteProtection": atmNteProtection,
       "atmNteProtectionMode": atmNteProtectionMode,
       "atmNteProtectionWorkingLink": atmNteProtectionWorkingLink,
       "atmNteProtectionSwitchLink": atmNteProtectionSwitchLink,
       "atmNteConfOam": atmNteConfOam,
       "atmNteConfOamSupport": atmNteConfOamSupport,
       "atmNteConfOamTransmission": atmNteConfOamTransmission,
       "atmNteConfOamAIS": atmNteConfOamAIS,
       "atmNteConfOamRDI": atmNteConfOamRDI,
       "atmNteConfOamAddressing": atmNteConfOamAddressing,
       "atmNteConfLoopbackAddMode": atmNteConfLoopbackAddMode,
       "atmNteConfLoopbackSourceAdd": atmNteConfLoopbackSourceAdd,
       "atmNteConfOamIfTable": atmNteConfOamIfTable,
       "atmNteConfOamIfEntry": atmNteConfOamIfEntry,
       "atmNteConfOamIfAisRdi": atmNteConfOamIfAisRdi,
       "atmNteConfCAC": atmNteConfCAC,
       "atmNteConfCACMode": atmNteConfCACMode,
       "atmNteHostIfTable": atmNteHostIfTable,
       "atmNteHostIfEntry": atmNteHostIfEntry,
       "atmNteHostPvcIndex": atmNteHostPvcIndex,
       "atmNteHostIP": atmNteHostIP,
       "atmNteHostMask": atmNteHostMask,
       "atmNteHostAtmIfIndex": atmNteHostAtmIfIndex,
       "atmNteHostVpi": atmNteHostVpi,
       "atmNteHostVci": atmNteHostVci,
       "atmNteHostRowStatus": atmNteHostRowStatus,
       "atmNteHostRdnVpi": atmNteHostRdnVpi,
       "atmNteHostRdnVci": atmNteHostRdnVci,
       "atmNteShaperMode": atmNteShaperMode,
       "atmNteOutputRate": atmNteOutputRate,
       "atmNteTosMode": atmNteTosMode,
       "atmNteTosMask": atmNteTosMask,
       "atmNteTosHighPriority": atmNteTosHighPriority,
       "atmNtePlugAndPlayActivity": atmNtePlugAndPlayActivity,
       "atmNteSlotUsage": atmNteSlotUsage,
       "atmNteConnectionsMaxNumber": atmNteConnectionsMaxNumber,
       "atmNteDefaultVpi": atmNteDefaultVpi,
       "atmNteDefaultVci": atmNteDefaultVci,
       "atmNteReservedVpi": atmNteReservedVpi,
       "atmNteRdnManagement": atmNteRdnManagement,
       "atmNtePlugAndPlayIfIndex": atmNtePlugAndPlayIfIndex,
       "atmNteLoopbackTimeout": atmNteLoopbackTimeout,
       "atmNteOamTable": atmNteOamTable,
       "atmNteOamEntry": atmNteOamEntry,
       "atmNteOamMode": atmNteOamMode,
       "atmNteOamCellType": atmNteOamCellType,
       "atmNteOamLevel": atmNteOamLevel,
       "atmNteOamEnable": atmNteOamEnable,
       "atmNteSysInfo": atmNteSysInfo,
       "atmNteIdTable": atmNteIdTable,
       "atmNteIdEntry": atmNteIdEntry,
       "atmNteIdIndex": atmNteIdIndex,
       "atmNteUnitId": atmNteUnitId,
       "atmNteUnitVersion": atmNteUnitVersion,
       "atmNteCardType": atmNteCardType,
       "atmSysPSunits": atmSysPSunits,
       "atmSysPSunitsInUse": atmSysPSunitsInUse,
       "atmSysFanUnits": atmSysFanUnits,
       "atmSysNetPrts": atmSysNetPrts,
       "atmSysNetPrtInUse": atmSysNetPrtInUse,
       "atmNteBridgingMode": atmNteBridgingMode,
       "atmSysStats": atmSysStats,
       "atmSysCurrentCdc": atmSysCurrentCdc,
       "atmSysIntervalTable": atmSysIntervalTable,
       "atmSysIntervalEntry": atmSysIntervalEntry,
       "atmSysIntervalNumber": atmSysIntervalNumber,
       "atmSysIntervalCdc": atmSysIntervalCdc,
       "atmNteEventType": atmNteEventType,
       "atmNteIntervalMaxNumber": atmNteIntervalMaxNumber,
       "atmNteAlarmType": atmNteAlarmType,
       "atmNteLevel": atmNteLevel,
       "atmNteConnectionsNumber": atmNteConnectionsNumber,
       "atmNtePrt": atmNtePrt,
       "atmNtePrtConfig": atmNtePrtConfig,
       "atmNteConfIfTable": atmNteConfIfTable,
       "atmNteConfIfEntry": atmNteConfIfEntry,
       "atmConfIfTransmitClk": atmConfIfTransmitClk,
       "atmConfIfLoopback": atmConfIfLoopback,
       "atmConfIfFrameType": atmConfIfFrameType,
       "atmConfIfCardType": atmConfIfCardType,
       "atmConfAtmIfVpiVciLimit": atmConfAtmIfVpiVciLimit,
       "atmConfIfHwFeatures": atmConfIfHwFeatures,
       "atmConfIfOutputRate": atmConfIfOutputRate,
       "atmConfIfInputRate": atmConfIfInputRate,
       "atmConfAlarmForwarding": atmConfAlarmForwarding,
       "atmNteAlarmIfTable": atmNteAlarmIfTable,
       "atmNteAlarmIfEntry": atmNteAlarmIfEntry,
       "atmInterfaceActiveAlarms": atmInterfaceActiveAlarms,
       "atmThresholdSectionBIP": atmThresholdSectionBIP,
       "atmThresholdLineBIP": atmThresholdLineBIP,
       "atmThresholdLineFEBE": atmThresholdLineFEBE,
       "atmThresholdPathBIP": atmThresholdPathBIP,
       "atmThresholdPathFEBE": atmThresholdPathFEBE,
       "atmThresholdErroredCells": atmThresholdErroredCells,
       "atmThresholdLostCells": atmThresholdLostCells,
       "atmThresholdMisinsertedCells": atmThresholdMisinsertedCells,
       "atmInterfaceAlarmStatus": atmInterfaceAlarmStatus,
       "atmInterfaceMaskAlarms": atmInterfaceMaskAlarms,
       "atmNteConfVpTable": atmNteConfVpTable,
       "atmNteConfVpEntry": atmNteConfVpEntry,
       "atmConfVpPolicing": atmConfVpPolicing,
       "atmConfVpCCAdminStatus": atmConfVpCCAdminStatus,
       "atmConfVpLoopbackAdminStatus": atmConfVpLoopbackAdminStatus,
       "atmConfVpLoopbackSinkAddress": atmConfVpLoopbackSinkAddress,
       "atmConfVpCongestionControl": atmConfVpCongestionControl,
       "atmConfVpCCDirection": atmConfVpCCDirection,
       "atmConfVpCreationTime": atmConfVpCreationTime,
       "atmConfVpOamSupport": atmConfVpOamSupport,
       "atmConfVpCCOperStatus": atmConfVpCCOperStatus,
       "atmConfVpLoopbackTraffic": atmConfVpLoopbackTraffic,
       "atmConfVpLoopbackFailureInd": atmConfVpLoopbackFailureInd,
       "atmConfVpLoopbackFailureThreshold": atmConfVpLoopbackFailureThreshold,
       "atmConfVpOamDirection": atmConfVpOamDirection,
       "atmNteConfVcTable": atmNteConfVcTable,
       "atmNteConfVcEntry": atmNteConfVcEntry,
       "atmConfVcPolicing": atmConfVcPolicing,
       "atmConfVcCCAdminStatus": atmConfVcCCAdminStatus,
       "atmConfVcLoopbackAdminStatus": atmConfVcLoopbackAdminStatus,
       "atmConfVcLoopbackSinkAddress": atmConfVcLoopbackSinkAddress,
       "atmConfVcCongestionControl": atmConfVcCongestionControl,
       "atmConfVcCCDirection": atmConfVcCCDirection,
       "atmConfVcCreationTime": atmConfVcCreationTime,
       "atmConfVcOamSupport": atmConfVcOamSupport,
       "atmConfVcCCActivationCtrl": atmConfVcCCActivationCtrl,
       "atmConfVcCCOperStatus": atmConfVcCCOperStatus,
       "atmConfVcLoopbackTraffic": atmConfVcLoopbackTraffic,
       "atmConfVcLoopbackFailureInd": atmConfVcLoopbackFailureInd,
       "atmConfVcLoopbackFailureThreshold": atmConfVcLoopbackFailureThreshold,
       "atmConfVcOamDirection": atmConfVcOamDirection,
       "atmNteAlarmVpTable": atmNteAlarmVpTable,
       "atmNteAlarmVpEntry": atmNteAlarmVpEntry,
       "atmNteVpAlarmVpi": atmNteVpAlarmVpi,
       "atmNteVpActiveAlarms": atmNteVpActiveAlarms,
       "atmNteAlarmVcTable": atmNteAlarmVcTable,
       "atmNteAlarmVcEntry": atmNteAlarmVcEntry,
       "atmNteVcAlarmVpi": atmNteVcAlarmVpi,
       "atmNteVcAlarmVci": atmNteVcAlarmVci,
       "atmNteVcActiveAlarms": atmNteVcActiveAlarms,
       "atmNteLoopback": atmNteLoopback,
       "atmLoopbackVpTable": atmLoopbackVpTable,
       "atmLoopbackVpEntry": atmLoopbackVpEntry,
       "atmLoopbackVpIfIndex": atmLoopbackVpIfIndex,
       "atmLoopbackVpVpi": atmLoopbackVpVpi,
       "atmLoopbackVpOperStatus": atmLoopbackVpOperStatus,
       "atmLoopbackVpCDV": atmLoopbackVpCDV,
       "atmLoopbackVpAverageDelay": atmLoopbackVpAverageDelay,
       "atmLoopbackVpMaxDelay": atmLoopbackVpMaxDelay,
       "atmLoopbackVpMinDelay": atmLoopbackVpMinDelay,
       "atmLoopbackVpErrSessions": atmLoopbackVpErrSessions,
       "atmLoopbackVcTable": atmLoopbackVcTable,
       "atmLoopbackVcEntry": atmLoopbackVcEntry,
       "atmLoopbackVcIfIndex": atmLoopbackVcIfIndex,
       "atmLoopbackVcVpi": atmLoopbackVcVpi,
       "atmLoopbackVcVci": atmLoopbackVcVci,
       "atmLoopbackVcOperStatus": atmLoopbackVcOperStatus,
       "atmLoopbackVcCDV": atmLoopbackVcCDV,
       "atmLoopbackVcAverageDelay": atmLoopbackVcAverageDelay,
       "atmLoopbackVcMaxDelay": atmLoopbackVcMaxDelay,
       "atmLoopbackVcMinDelay": atmLoopbackVcMinDelay,
       "atmLoopbackVcErrSessions": atmLoopbackVcErrSessions,
       "atmLoopbackVpIvlTable": atmLoopbackVpIvlTable,
       "atmLoopbackVpIvlEntry": atmLoopbackVpIvlEntry,
       "atmLoopbackVpIvlIfIndex": atmLoopbackVpIvlIfIndex,
       "atmLoopbackVpIvlVpi": atmLoopbackVpIvlVpi,
       "atmLoopbackVpIvlIvl": atmLoopbackVpIvlIvl,
       "atmLoopbackVpIvlOperStatus": atmLoopbackVpIvlOperStatus,
       "atmLoopbackVpIvlCDV": atmLoopbackVpIvlCDV,
       "atmLoopbackVpIvlAverageDelay": atmLoopbackVpIvlAverageDelay,
       "atmLoopbackVpIvlMaxDelay": atmLoopbackVpIvlMaxDelay,
       "atmLoopbackVpIvlMinDelay": atmLoopbackVpIvlMinDelay,
       "atmLoopbackVpIvlErrSessions": atmLoopbackVpIvlErrSessions,
       "atmLoopbackVcIvlTable": atmLoopbackVcIvlTable,
       "atmLoopbackVcIvlEntry": atmLoopbackVcIvlEntry,
       "atmLoopbackVcIvlIfIndex": atmLoopbackVcIvlIfIndex,
       "atmLoopbackVcIvlVpi": atmLoopbackVcIvlVpi,
       "atmLoopbackVcIvlVci": atmLoopbackVcIvlVci,
       "atmLoopbackVcIvlIvl": atmLoopbackVcIvlIvl,
       "atmLoopbackVcIvlOperStatus": atmLoopbackVcIvlOperStatus,
       "atmLoopbackVcIvlCDV": atmLoopbackVcIvlCDV,
       "atmLoopbackVcIvlAverageDelay": atmLoopbackVcIvlAverageDelay,
       "atmLoopbackVcIvlMaxDelay": atmLoopbackVcIvlMaxDelay,
       "atmLoopbackVcIvlMinDelay": atmLoopbackVcIvlMinDelay,
       "atmLoopbackVcIvlErrSessions": atmLoopbackVcIvlErrSessions,
       "atmNtePM": atmNtePM,
       "atmVpPmTable": atmVpPmTable,
       "atmVpPmEntry": atmVpPmEntry,
       "atmVpPmIfIndex": atmVpPmIfIndex,
       "atmVpPmVpi": atmVpPmVpi,
       "atmVpPmAdminStatus": atmVpPmAdminStatus,
       "atmVpPmDirection": atmVpPmDirection,
       "atmVpPmBlockSize": atmVpPmBlockSize,
       "atmVpPmRowStatus": atmVpPmRowStatus,
       "atmVpPmSink": atmVpPmSink,
       "atmVpPmSource": atmVpPmSource,
       "atmVcPmTable": atmVcPmTable,
       "atmVcPmEntry": atmVcPmEntry,
       "atmVcPmIfIndex": atmVcPmIfIndex,
       "atmVcPmVpi": atmVcPmVpi,
       "atmVcPmVci": atmVcPmVci,
       "atmVcPmAdminStatus": atmVcPmAdminStatus,
       "atmVcPmDirection": atmVcPmDirection,
       "atmVcPmBlockSize": atmVcPmBlockSize,
       "atmVcPmRowStatus": atmVcPmRowStatus,
       "atmVcPmSink": atmVcPmSink,
       "atmVcPmSource": atmVcPmSource,
       "radAtmIma": radAtmIma,
       "imaPrimaryClk": imaPrimaryClk,
       "imaXLinkTable": imaXLinkTable,
       "imaXLinkEntry": imaXLinkEntry,
       "imaLinkDirection": imaLinkDirection,
       "imaLinkItcLBClkSrc": imaLinkItcLBClkSrc,
       "imaXGroupTable": imaXGroupTable,
       "imaXGroupEntry": imaXGroupEntry,
       "imaGroupVersion": imaGroupVersion,
       "imaGroupCtcTxClkSrc": imaGroupCtcTxClkSrc,
       "atmLayer2": atmLayer2,
       "atmLayer2XVclTable": atmLayer2XVclTable,
       "atmLayer2XVclEntry": atmLayer2XVclEntry,
       "atmLayer2XVclConnMode": atmLayer2XVclConnMode,
       "atmLayer2XVclGroupIdx": atmLayer2XVclGroupIdx,
       "atmLayer2GroupTable": atmLayer2GroupTable,
       "atmLayer2GroupEntry": atmLayer2GroupEntry,
       "atmLayer2GroupIdx": atmLayer2GroupIdx,
       "atmLayer2GroupRowStatus": atmLayer2GroupRowStatus,
       "atmLayer2GroupConnMode": atmLayer2GroupConnMode,
       "atmLayer2GroupConnPriority": atmLayer2GroupConnPriority,
       "atmLayer2GroupName": atmLayer2GroupName,
       "atmLayer2PriorityTable": atmLayer2PriorityTable,
       "atmLayer2PriorityEntry": atmLayer2PriorityEntry,
       "atmLayer2PriorityGroupIdx": atmLayer2PriorityGroupIdx,
       "atmLayer2PriorityRx": atmLayer2PriorityRx,
       "atmLayer2PriorityIfIndex": atmLayer2PriorityIfIndex,
       "atmLayer2PriorityVclVpi": atmLayer2PriorityVclVpi,
       "atmLayer2PriorityVclVci": atmLayer2PriorityVclVci,
       "atmLayer2GroupIndexNext": atmLayer2GroupIndexNext,
       "radAtmFr": radAtmFr,
       "frAtmIwfXConnectionTable": frAtmIwfXConnectionTable,
       "frAtmIwfXConnectionEntry": frAtmIwfXConnectionEntry,
       "frAtmIwfXConnMode": frAtmIwfXConnMode,
       "frAtmIwfXConnSscsDlci": frAtmIwfXConnSscsDlci,
       "radExperimental": radExperimental}
)
