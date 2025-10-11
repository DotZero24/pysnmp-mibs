# SNMP MIB module (OA-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-SONET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:35 2025
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

(oaDevTrapsPortsIfAlias,) = mibBuilder.importSymbols(
    "OA-TRAP-MESSAGES-MIB",
    "oaDevTrapsPortsIfAlias")

(oaLdCardPortsPortNumber,
 oaLdCardPortsSlotNumber) = mibBuilder.importSymbols(
    "OADWDM-MIB",
    "oaLdCardPortsPortNumber",
    "oaLdCardPortsSlotNumber")

(PerfIntervalCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfIntervalCount")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oaSonetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81)
)
if mibBuilder.loadTexts:
    oaSonetMib.setRevisions(
        ("2008-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaSonetNotifications_ObjectIdentity = ObjectIdentity
oaSonetNotifications = _OaSonetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0)
)
_OaSonetSection_ObjectIdentity = ObjectIdentity
oaSonetSection = _OaSonetSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1)
)
_OaSonetSecTcaTable_Object = MibTable
oaSonetSecTcaTable = _OaSonetSecTcaTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1)
)
if mibBuilder.loadTexts:
    oaSonetSecTcaTable.setStatus("current")
_OaSonetSecTcaEntry_Object = MibTableRow
oaSonetSecTcaEntry = _OaSonetSecTcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1)
)
oaSonetSecTcaEntry.setIndexNames(
    (0, "OA-SONET-MIB", "oaSonetSecIfIndex"),
)
if mibBuilder.loadTexts:
    oaSonetSecTcaEntry.setStatus("current")


class _OaSonetSecIfIndex_Type(Integer32):
    """Custom type oaSonetSecIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_OaSonetSecIfIndex_Type.__name__ = "Integer32"
_OaSonetSecIfIndex_Object = MibTableColumn
oaSonetSecIfIndex = _OaSonetSecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 1),
    _OaSonetSecIfIndex_Type()
)
oaSonetSecIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oaSonetSecIfIndex.setStatus("current")


class _OaSonetSec15MinESsTca_Type(Unsigned32):
    """Custom type oaSonetSec15MinESsTca based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSec15MinESsTca_Type.__name__ = "Unsigned32"
_OaSonetSec15MinESsTca_Object = MibTableColumn
oaSonetSec15MinESsTca = _OaSonetSec15MinESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 2),
    _OaSonetSec15MinESsTca_Type()
)
oaSonetSec15MinESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSec15MinESsTca.setStatus("current")


class _OaSonetSecDayESsTca_Type(Unsigned32):
    """Custom type oaSonetSecDayESsTca based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSecDayESsTca_Type.__name__ = "Unsigned32"
_OaSonetSecDayESsTca_Object = MibTableColumn
oaSonetSecDayESsTca = _OaSonetSecDayESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 3),
    _OaSonetSecDayESsTca_Type()
)
oaSonetSecDayESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSecDayESsTca.setStatus("current")


class _OaSonetSec15MinSESsTca_Type(Unsigned32):
    """Custom type oaSonetSec15MinSESsTca based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSec15MinSESsTca_Type.__name__ = "Unsigned32"
_OaSonetSec15MinSESsTca_Object = MibTableColumn
oaSonetSec15MinSESsTca = _OaSonetSec15MinSESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 4),
    _OaSonetSec15MinSESsTca_Type()
)
oaSonetSec15MinSESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSec15MinSESsTca.setStatus("current")


class _OaSonetSecDaySESsTca_Type(Unsigned32):
    """Custom type oaSonetSecDaySESsTca based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSecDaySESsTca_Type.__name__ = "Unsigned32"
_OaSonetSecDaySESsTca_Object = MibTableColumn
oaSonetSecDaySESsTca = _OaSonetSecDaySESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 5),
    _OaSonetSecDaySESsTca_Type()
)
oaSonetSecDaySESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSecDaySESsTca.setStatus("current")


class _OaSonetSec15MinSEFSsTca_Type(Unsigned32):
    """Custom type oaSonetSec15MinSEFSsTca based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSec15MinSEFSsTca_Type.__name__ = "Unsigned32"
_OaSonetSec15MinSEFSsTca_Object = MibTableColumn
oaSonetSec15MinSEFSsTca = _OaSonetSec15MinSEFSsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 6),
    _OaSonetSec15MinSEFSsTca_Type()
)
oaSonetSec15MinSEFSsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSec15MinSEFSsTca.setStatus("current")


class _OaSonetSecDaySEFSsTca_Type(Unsigned32):
    """Custom type oaSonetSecDaySEFSsTca based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSecDaySEFSsTca_Type.__name__ = "Unsigned32"
_OaSonetSecDaySEFSsTca_Object = MibTableColumn
oaSonetSecDaySEFSsTca = _OaSonetSecDaySEFSsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 7),
    _OaSonetSecDaySEFSsTca_Type()
)
oaSonetSecDaySEFSsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSecDaySEFSsTca.setStatus("current")


class _OaSonetSec15MinCVsTca_Type(Unsigned32):
    """Custom type oaSonetSec15MinCVsTca based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSec15MinCVsTca_Type.__name__ = "Unsigned32"
_OaSonetSec15MinCVsTca_Object = MibTableColumn
oaSonetSec15MinCVsTca = _OaSonetSec15MinCVsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 8),
    _OaSonetSec15MinCVsTca_Type()
)
oaSonetSec15MinCVsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSec15MinCVsTca.setStatus("current")


class _OaSonetSecDayCVsTca_Type(Unsigned32):
    """Custom type oaSonetSecDayCVsTca based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSecDayCVsTca_Type.__name__ = "Unsigned32"
_OaSonetSecDayCVsTca_Object = MibTableColumn
oaSonetSecDayCVsTca = _OaSonetSecDayCVsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 9),
    _OaSonetSecDayCVsTca_Type()
)
oaSonetSecDayCVsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSecDayCVsTca.setStatus("current")


class _OaSonetSec15MinUASsTca_Type(Unsigned32):
    """Custom type oaSonetSec15MinUASsTca based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSec15MinUASsTca_Type.__name__ = "Unsigned32"
_OaSonetSec15MinUASsTca_Object = MibTableColumn
oaSonetSec15MinUASsTca = _OaSonetSec15MinUASsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 10),
    _OaSonetSec15MinUASsTca_Type()
)
oaSonetSec15MinUASsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSec15MinUASsTca.setStatus("current")


class _OaSonetSecDayUASsTca_Type(Unsigned32):
    """Custom type oaSonetSecDayUASsTca based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetSecDayUASsTca_Type.__name__ = "Unsigned32"
_OaSonetSecDayUASsTca_Object = MibTableColumn
oaSonetSecDayUASsTca = _OaSonetSecDayUASsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 1, 1, 11),
    _OaSonetSecDayUASsTca_Type()
)
oaSonetSecDayUASsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetSecDayUASsTca.setStatus("current")
_OaSonetSecCurrDayTable_Object = MibTable
oaSonetSecCurrDayTable = _OaSonetSecCurrDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 2)
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDayTable.setStatus("current")
_OaSonetSecCurrDayEntry_Object = MibTableRow
oaSonetSecCurrDayEntry = _OaSonetSecCurrDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 2, 1)
)
oaSonetSecCurrDayEntry.setIndexNames(
    (0, "OA-SONET-MIB", "oaSonetSecCurrDayIfIndex"),
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDayEntry.setStatus("current")


class _OaSonetSecCurrDayIfIndex_Type(Integer32):
    """Custom type oaSonetSecCurrDayIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_OaSonetSecCurrDayIfIndex_Type.__name__ = "Integer32"
_OaSonetSecCurrDayIfIndex_Object = MibTableColumn
oaSonetSecCurrDayIfIndex = _OaSonetSecCurrDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 2, 1, 1),
    _OaSonetSecCurrDayIfIndex_Type()
)
oaSonetSecCurrDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSonetSecCurrDayIfIndex.setStatus("current")
_OaSonetSecCurrDayESs_Type = PerfIntervalCount
_OaSonetSecCurrDayESs_Object = MibTableColumn
oaSonetSecCurrDayESs = _OaSonetSecCurrDayESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 2, 1, 2),
    _OaSonetSecCurrDayESs_Type()
)
oaSonetSecCurrDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecCurrDayESs.setStatus("current")
_OaSonetSecCurrDaySESs_Type = PerfIntervalCount
_OaSonetSecCurrDaySESs_Object = MibTableColumn
oaSonetSecCurrDaySESs = _OaSonetSecCurrDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 2, 1, 3),
    _OaSonetSecCurrDaySESs_Type()
)
oaSonetSecCurrDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecCurrDaySESs.setStatus("current")
_OaSonetSecCurrDaySEFSs_Type = PerfIntervalCount
_OaSonetSecCurrDaySEFSs_Object = MibTableColumn
oaSonetSecCurrDaySEFSs = _OaSonetSecCurrDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 2, 1, 4),
    _OaSonetSecCurrDaySEFSs_Type()
)
oaSonetSecCurrDaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecCurrDaySEFSs.setStatus("current")
_OaSonetSecCurrDayCVs_Type = PerfIntervalCount
_OaSonetSecCurrDayCVs_Object = MibTableColumn
oaSonetSecCurrDayCVs = _OaSonetSecCurrDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 2, 1, 5),
    _OaSonetSecCurrDayCVs_Type()
)
oaSonetSecCurrDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecCurrDayCVs.setStatus("current")
_OaSonetSecPrevDayTable_Object = MibTable
oaSonetSecPrevDayTable = _OaSonetSecPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3)
)
if mibBuilder.loadTexts:
    oaSonetSecPrevDayTable.setStatus("current")
_OaSonetSecPrevDayEntry_Object = MibTableRow
oaSonetSecPrevDayEntry = _OaSonetSecPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3, 1)
)
oaSonetSecPrevDayEntry.setIndexNames(
    (0, "OA-SONET-MIB", "oaSonetSecPrevDayIfIndex"),
)
if mibBuilder.loadTexts:
    oaSonetSecPrevDayEntry.setStatus("current")


class _OaSonetSecPrevDayIfIndex_Type(Integer32):
    """Custom type oaSonetSecPrevDayIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_OaSonetSecPrevDayIfIndex_Type.__name__ = "Integer32"
_OaSonetSecPrevDayIfIndex_Object = MibTableColumn
oaSonetSecPrevDayIfIndex = _OaSonetSecPrevDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3, 1, 1),
    _OaSonetSecPrevDayIfIndex_Type()
)
oaSonetSecPrevDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSonetSecPrevDayIfIndex.setStatus("current")
_OaSonetSecPrevDayESs_Type = PerfIntervalCount
_OaSonetSecPrevDayESs_Object = MibTableColumn
oaSonetSecPrevDayESs = _OaSonetSecPrevDayESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3, 1, 2),
    _OaSonetSecPrevDayESs_Type()
)
oaSonetSecPrevDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecPrevDayESs.setStatus("current")
_OaSonetSecPrevDaySESs_Type = PerfIntervalCount
_OaSonetSecPrevDaySESs_Object = MibTableColumn
oaSonetSecPrevDaySESs = _OaSonetSecPrevDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3, 1, 3),
    _OaSonetSecPrevDaySESs_Type()
)
oaSonetSecPrevDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecPrevDaySESs.setStatus("current")
_OaSonetSecPrevDaySEFSs_Type = PerfIntervalCount
_OaSonetSecPrevDaySEFSs_Object = MibTableColumn
oaSonetSecPrevDaySEFSs = _OaSonetSecPrevDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3, 1, 4),
    _OaSonetSecPrevDaySEFSs_Type()
)
oaSonetSecPrevDaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecPrevDaySEFSs.setStatus("current")
_OaSonetSecPrevDayCVs_Type = PerfIntervalCount
_OaSonetSecPrevDayCVs_Object = MibTableColumn
oaSonetSecPrevDayCVs = _OaSonetSecPrevDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3, 1, 5),
    _OaSonetSecPrevDayCVs_Type()
)
oaSonetSecPrevDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecPrevDayCVs.setStatus("current")
_OaSonetSecPrevDayValidData_Type = TruthValue
_OaSonetSecPrevDayValidData_Object = MibTableColumn
oaSonetSecPrevDayValidData = _OaSonetSecPrevDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 1, 3, 1, 6),
    _OaSonetSecPrevDayValidData_Type()
)
oaSonetSecPrevDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetSecPrevDayValidData.setStatus("current")
_OaSonetLine_ObjectIdentity = ObjectIdentity
oaSonetLine = _OaSonetLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2)
)
_OaSonetLineTcaTable_Object = MibTable
oaSonetLineTcaTable = _OaSonetLineTcaTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1)
)
if mibBuilder.loadTexts:
    oaSonetLineTcaTable.setStatus("current")
_OaSonetLineTcaEntry_Object = MibTableRow
oaSonetLineTcaEntry = _OaSonetLineTcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1)
)
oaSonetLineTcaEntry.setIndexNames(
    (0, "OA-SONET-MIB", "oaSonetLineIfIndex"),
)
if mibBuilder.loadTexts:
    oaSonetLineTcaEntry.setStatus("current")


class _OaSonetLineIfIndex_Type(Integer32):
    """Custom type oaSonetLineIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_OaSonetLineIfIndex_Type.__name__ = "Integer32"
_OaSonetLineIfIndex_Object = MibTableColumn
oaSonetLineIfIndex = _OaSonetLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 1),
    _OaSonetLineIfIndex_Type()
)
oaSonetLineIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oaSonetLineIfIndex.setStatus("current")


class _OaSonetLine15MinESsTca_Type(Unsigned32):
    """Custom type oaSonetLine15MinESsTca based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLine15MinESsTca_Type.__name__ = "Unsigned32"
_OaSonetLine15MinESsTca_Object = MibTableColumn
oaSonetLine15MinESsTca = _OaSonetLine15MinESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 2),
    _OaSonetLine15MinESsTca_Type()
)
oaSonetLine15MinESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLine15MinESsTca.setStatus("current")


class _OaSonetLineDayESsTca_Type(Unsigned32):
    """Custom type oaSonetLineDayESsTca based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLineDayESsTca_Type.__name__ = "Unsigned32"
_OaSonetLineDayESsTca_Object = MibTableColumn
oaSonetLineDayESsTca = _OaSonetLineDayESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 3),
    _OaSonetLineDayESsTca_Type()
)
oaSonetLineDayESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLineDayESsTca.setStatus("current")


class _OaSonetLine15MinSESsTca_Type(Unsigned32):
    """Custom type oaSonetLine15MinSESsTca based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLine15MinSESsTca_Type.__name__ = "Unsigned32"
_OaSonetLine15MinSESsTca_Object = MibTableColumn
oaSonetLine15MinSESsTca = _OaSonetLine15MinSESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 4),
    _OaSonetLine15MinSESsTca_Type()
)
oaSonetLine15MinSESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLine15MinSESsTca.setStatus("current")


class _OaSonetLineDaySESsTca_Type(Unsigned32):
    """Custom type oaSonetLineDaySESsTca based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLineDaySESsTca_Type.__name__ = "Unsigned32"
_OaSonetLineDaySESsTca_Object = MibTableColumn
oaSonetLineDaySESsTca = _OaSonetLineDaySESsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 5),
    _OaSonetLineDaySESsTca_Type()
)
oaSonetLineDaySESsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLineDaySESsTca.setStatus("current")


class _OaSonetLine15MinCVsTca_Type(Unsigned32):
    """Custom type oaSonetLine15MinCVsTca based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLine15MinCVsTca_Type.__name__ = "Unsigned32"
_OaSonetLine15MinCVsTca_Object = MibTableColumn
oaSonetLine15MinCVsTca = _OaSonetLine15MinCVsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 6),
    _OaSonetLine15MinCVsTca_Type()
)
oaSonetLine15MinCVsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLine15MinCVsTca.setStatus("current")


class _OaSonetLineDayCVsTca_Type(Unsigned32):
    """Custom type oaSonetLineDayCVsTca based on Unsigned32"""
    defaultValue = 750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLineDayCVsTca_Type.__name__ = "Unsigned32"
_OaSonetLineDayCVsTca_Object = MibTableColumn
oaSonetLineDayCVsTca = _OaSonetLineDayCVsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 7),
    _OaSonetLineDayCVsTca_Type()
)
oaSonetLineDayCVsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLineDayCVsTca.setStatus("current")


class _OaSonetLine15MinUASsTca_Type(Unsigned32):
    """Custom type oaSonetLine15MinUASsTca based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLine15MinUASsTca_Type.__name__ = "Unsigned32"
_OaSonetLine15MinUASsTca_Object = MibTableColumn
oaSonetLine15MinUASsTca = _OaSonetLine15MinUASsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 8),
    _OaSonetLine15MinUASsTca_Type()
)
oaSonetLine15MinUASsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLine15MinUASsTca.setStatus("current")


class _OaSonetLineDayUASsTca_Type(Unsigned32):
    """Custom type oaSonetLineDayUASsTca based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OaSonetLineDayUASsTca_Type.__name__ = "Unsigned32"
_OaSonetLineDayUASsTca_Object = MibTableColumn
oaSonetLineDayUASsTca = _OaSonetLineDayUASsTca_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 1, 1, 9),
    _OaSonetLineDayUASsTca_Type()
)
oaSonetLineDayUASsTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSonetLineDayUASsTca.setStatus("current")
_OaSonetLineCurrDayTable_Object = MibTable
oaSonetLineCurrDayTable = _OaSonetLineCurrDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2)
)
if mibBuilder.loadTexts:
    oaSonetLineCurrDayTable.setStatus("current")
_OaSonetLineCurrDayEntry_Object = MibTableRow
oaSonetLineCurrDayEntry = _OaSonetLineCurrDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1)
)
oaSonetLineCurrDayEntry.setIndexNames(
    (0, "OA-SONET-MIB", "oaSonetLineCurrDayIfIndex"),
)
if mibBuilder.loadTexts:
    oaSonetLineCurrDayEntry.setStatus("current")


class _OaSonetLineCurrDayIfIndex_Type(Integer32):
    """Custom type oaSonetLineCurrDayIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_OaSonetLineCurrDayIfIndex_Type.__name__ = "Integer32"
_OaSonetLineCurrDayIfIndex_Object = MibTableColumn
oaSonetLineCurrDayIfIndex = _OaSonetLineCurrDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 1),
    _OaSonetLineCurrDayIfIndex_Type()
)
oaSonetLineCurrDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSonetLineCurrDayIfIndex.setStatus("current")
_OaSonetNELineCurrDayESs_Type = PerfIntervalCount
_OaSonetNELineCurrDayESs_Object = MibTableColumn
oaSonetNELineCurrDayESs = _OaSonetNELineCurrDayESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 2),
    _OaSonetNELineCurrDayESs_Type()
)
oaSonetNELineCurrDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayESs.setStatus("current")
_OaSonetNELineCurrDaySESs_Type = PerfIntervalCount
_OaSonetNELineCurrDaySESs_Object = MibTableColumn
oaSonetNELineCurrDaySESs = _OaSonetNELineCurrDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 3),
    _OaSonetNELineCurrDaySESs_Type()
)
oaSonetNELineCurrDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELineCurrDaySESs.setStatus("current")
_OaSonetNELineCurrDayCVs_Type = PerfIntervalCount
_OaSonetNELineCurrDayCVs_Object = MibTableColumn
oaSonetNELineCurrDayCVs = _OaSonetNELineCurrDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 4),
    _OaSonetNELineCurrDayCVs_Type()
)
oaSonetNELineCurrDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayCVs.setStatus("current")
_OaSonetNELineCurrDayUASs_Type = PerfIntervalCount
_OaSonetNELineCurrDayUASs_Object = MibTableColumn
oaSonetNELineCurrDayUASs = _OaSonetNELineCurrDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 5),
    _OaSonetNELineCurrDayUASs_Type()
)
oaSonetNELineCurrDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayUASs.setStatus("current")
_OaSonetFELineCurrDayESs_Type = PerfIntervalCount
_OaSonetFELineCurrDayESs_Object = MibTableColumn
oaSonetFELineCurrDayESs = _OaSonetFELineCurrDayESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 6),
    _OaSonetFELineCurrDayESs_Type()
)
oaSonetFELineCurrDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayESs.setStatus("current")
_OaSonetFELineCurrDaySESs_Type = PerfIntervalCount
_OaSonetFELineCurrDaySESs_Object = MibTableColumn
oaSonetFELineCurrDaySESs = _OaSonetFELineCurrDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 7),
    _OaSonetFELineCurrDaySESs_Type()
)
oaSonetFELineCurrDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELineCurrDaySESs.setStatus("current")
_OaSonetFELineCurrDayCVs_Type = PerfIntervalCount
_OaSonetFELineCurrDayCVs_Object = MibTableColumn
oaSonetFELineCurrDayCVs = _OaSonetFELineCurrDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 8),
    _OaSonetFELineCurrDayCVs_Type()
)
oaSonetFELineCurrDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayCVs.setStatus("current")
_OaSonetFELineCurrDayUASs_Type = PerfIntervalCount
_OaSonetFELineCurrDayUASs_Object = MibTableColumn
oaSonetFELineCurrDayUASs = _OaSonetFELineCurrDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 2, 1, 9),
    _OaSonetFELineCurrDayUASs_Type()
)
oaSonetFELineCurrDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayUASs.setStatus("current")
_OaSonetLinePrevDayTable_Object = MibTable
oaSonetLinePrevDayTable = _OaSonetLinePrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3)
)
if mibBuilder.loadTexts:
    oaSonetLinePrevDayTable.setStatus("current")
_OaSonetLinePrevDayEntry_Object = MibTableRow
oaSonetLinePrevDayEntry = _OaSonetLinePrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1)
)
oaSonetLinePrevDayEntry.setIndexNames(
    (0, "OA-SONET-MIB", "oaSonetLinePrevDayIfIndex"),
)
if mibBuilder.loadTexts:
    oaSonetLinePrevDayEntry.setStatus("current")


class _OaSonetLinePrevDayIfIndex_Type(Integer32):
    """Custom type oaSonetLinePrevDayIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_OaSonetLinePrevDayIfIndex_Type.__name__ = "Integer32"
_OaSonetLinePrevDayIfIndex_Object = MibTableColumn
oaSonetLinePrevDayIfIndex = _OaSonetLinePrevDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 1),
    _OaSonetLinePrevDayIfIndex_Type()
)
oaSonetLinePrevDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSonetLinePrevDayIfIndex.setStatus("current")
_OaSonetNELinePrevDayESs_Type = PerfIntervalCount
_OaSonetNELinePrevDayESs_Object = MibTableColumn
oaSonetNELinePrevDayESs = _OaSonetNELinePrevDayESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 2),
    _OaSonetNELinePrevDayESs_Type()
)
oaSonetNELinePrevDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELinePrevDayESs.setStatus("current")
_OaSonetNELinePrevDaySESs_Type = PerfIntervalCount
_OaSonetNELinePrevDaySESs_Object = MibTableColumn
oaSonetNELinePrevDaySESs = _OaSonetNELinePrevDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 3),
    _OaSonetNELinePrevDaySESs_Type()
)
oaSonetNELinePrevDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELinePrevDaySESs.setStatus("current")
_OaSonetNELinePrevDayCVs_Type = PerfIntervalCount
_OaSonetNELinePrevDayCVs_Object = MibTableColumn
oaSonetNELinePrevDayCVs = _OaSonetNELinePrevDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 4),
    _OaSonetNELinePrevDayCVs_Type()
)
oaSonetNELinePrevDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELinePrevDayCVs.setStatus("current")
_OaSonetNELinePrevDayUASs_Type = PerfIntervalCount
_OaSonetNELinePrevDayUASs_Object = MibTableColumn
oaSonetNELinePrevDayUASs = _OaSonetNELinePrevDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 5),
    _OaSonetNELinePrevDayUASs_Type()
)
oaSonetNELinePrevDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetNELinePrevDayUASs.setStatus("current")
_OaSonetFELinePrevDayESs_Type = PerfIntervalCount
_OaSonetFELinePrevDayESs_Object = MibTableColumn
oaSonetFELinePrevDayESs = _OaSonetFELinePrevDayESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 6),
    _OaSonetFELinePrevDayESs_Type()
)
oaSonetFELinePrevDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELinePrevDayESs.setStatus("current")
_OaSonetFELinePrevDaySESs_Type = PerfIntervalCount
_OaSonetFELinePrevDaySESs_Object = MibTableColumn
oaSonetFELinePrevDaySESs = _OaSonetFELinePrevDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 7),
    _OaSonetFELinePrevDaySESs_Type()
)
oaSonetFELinePrevDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELinePrevDaySESs.setStatus("current")
_OaSonetFELinePrevDayCVs_Type = PerfIntervalCount
_OaSonetFELinePrevDayCVs_Object = MibTableColumn
oaSonetFELinePrevDayCVs = _OaSonetFELinePrevDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 8),
    _OaSonetFELinePrevDayCVs_Type()
)
oaSonetFELinePrevDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELinePrevDayCVs.setStatus("current")
_OaSonetFELinePrevDayUASs_Type = PerfIntervalCount
_OaSonetFELinePrevDayUASs_Object = MibTableColumn
oaSonetFELinePrevDayUASs = _OaSonetFELinePrevDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 9),
    _OaSonetFELinePrevDayUASs_Type()
)
oaSonetFELinePrevDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetFELinePrevDayUASs.setStatus("current")
_OaSonetLinePrevDayValidData_Type = TruthValue
_OaSonetLinePrevDayValidData_Object = MibTableColumn
oaSonetLinePrevDayValidData = _OaSonetLinePrevDayValidData_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 2, 3, 1, 10),
    _OaSonetLinePrevDayValidData_Type()
)
oaSonetLinePrevDayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetLinePrevDayValidData.setStatus("current")
_OaSonetMIBConformance_ObjectIdentity = ObjectIdentity
oaSonetMIBConformance = _OaSonetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3)
)
_OaSonetMIBGroups_ObjectIdentity = ObjectIdentity
oaSonetMIBGroups = _OaSonetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1)
)
_OaSonetMIBCompliances_ObjectIdentity = ObjectIdentity
oaSonetMIBCompliances = _OaSonetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 2)
)
_OaSonetGenParams_ObjectIdentity = ObjectIdentity
oaSonetGenParams = _OaSonetGenParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 4)
)
_OaSonetMibImplementRevision_Type = Integer32
_OaSonetMibImplementRevision_Object = MibScalar
oaSonetMibImplementRevision = _OaSonetMibImplementRevision_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 4, 2),
    _OaSonetMibImplementRevision_Type()
)
oaSonetMibImplementRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSonetMibImplementRevision.setStatus("current")

# Managed Objects groups

oaSonetSecTcaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 1)
)
oaSonetSecTcaGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-SONET-MIB", "oaSonetSec15MinESsTca"),
        ("OA-SONET-MIB", "oaSonetSecDayESsTca"),
        ("OA-SONET-MIB", "oaSonetSec15MinSESsTca"),
        ("OA-SONET-MIB", "oaSonetSecDaySESsTca"),
        ("OA-SONET-MIB", "oaSonetSec15MinSEFSsTca"),
        ("OA-SONET-MIB", "oaSonetSecDaySEFSsTca"),
        ("OA-SONET-MIB", "oaSonetSec15MinCVsTca"),
        ("OA-SONET-MIB", "oaSonetSecDayCVsTca"),
        ("OA-SONET-MIB", "oaSonetSec15MinUASsTca"),
        ("OA-SONET-MIB", "oaSonetSecDayUASsTca"))
)
if mibBuilder.loadTexts:
    oaSonetSecTcaGroup.setStatus("current")

oaSonetLineTcaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 2)
)
oaSonetLineTcaGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-SONET-MIB", "oaSonetLine15MinESsTca"),
        ("OA-SONET-MIB", "oaSonetLineDayESsTca"),
        ("OA-SONET-MIB", "oaSonetLine15MinSESsTca"),
        ("OA-SONET-MIB", "oaSonetLineDaySESsTca"),
        ("OA-SONET-MIB", "oaSonetLine15MinCVsTca"),
        ("OA-SONET-MIB", "oaSonetLineDayCVsTca"),
        ("OA-SONET-MIB", "oaSonetLine15MinUASsTca"),
        ("OA-SONET-MIB", "oaSonetLineDayUASsTca"))
)
if mibBuilder.loadTexts:
    oaSonetLineTcaGroup.setStatus("current")

oaSonetSecCurrDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 3)
)
oaSonetSecCurrDayGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetSecCurrDayESs"),
        ("OA-SONET-MIB", "oaSonetSecCurrDaySESs"),
        ("OA-SONET-MIB", "oaSonetSecCurrDaySEFSs"),
        ("OA-SONET-MIB", "oaSonetSecCurrDayCVs"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDayGroup.setStatus("current")

oaSonetSecPrevDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 4)
)
oaSonetSecPrevDayGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetSecPrevDayESs"),
        ("OA-SONET-MIB", "oaSonetSecPrevDaySESs"),
        ("OA-SONET-MIB", "oaSonetSecPrevDaySEFSs"),
        ("OA-SONET-MIB", "oaSonetSecPrevDayCVs"),
        ("OA-SONET-MIB", "oaSonetSecPrevDayValidData"))
)
if mibBuilder.loadTexts:
    oaSonetSecPrevDayGroup.setStatus("current")

oaSonetNELineCurrDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 5)
)
oaSonetNELineCurrDayGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetNELineCurrDayESs"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDaySESs"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayCVs"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayUASs"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayGroup.setStatus("current")

oaSonetNELinePrevDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 6)
)
oaSonetNELinePrevDayGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetNELinePrevDayESs"),
        ("OA-SONET-MIB", "oaSonetNELinePrevDaySESs"),
        ("OA-SONET-MIB", "oaSonetNELinePrevDayCVs"),
        ("OA-SONET-MIB", "oaSonetNELinePrevDayUASs"),
        ("OA-SONET-MIB", "oaSonetLinePrevDayValidData"))
)
if mibBuilder.loadTexts:
    oaSonetNELinePrevDayGroup.setStatus("current")

oaSonetFELineCurrDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 7)
)
oaSonetFELineCurrDayGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetFELineCurrDayESs"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDaySESs"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayCVs"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayUASs"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayGroup.setStatus("current")

oaSonetFELinePrevDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 8)
)
oaSonetFELinePrevDayGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetFELinePrevDayESs"),
        ("OA-SONET-MIB", "oaSonetFELinePrevDaySESs"),
        ("OA-SONET-MIB", "oaSonetFELinePrevDayCVs"),
        ("OA-SONET-MIB", "oaSonetFELinePrevDayUASs"),
        ("OA-SONET-MIB", "oaSonetLinePrevDayValidData"))
)
if mibBuilder.loadTexts:
    oaSonetFELinePrevDayGroup.setStatus("current")

oaSonetGenParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 15)
)
oaSonetGenParamsGroup.setObjects(
    ("OA-SONET-MIB", "oaSonetMibImplementRevision")
)
if mibBuilder.loadTexts:
    oaSonetGenParamsGroup.setStatus("current")


# Notification objects

oaSonetSec15MinESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 99)
)
oaSonetSec15MinESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinESsOn.setStatus(
        "current"
    )

oaSonetSec15MinESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 100)
)
oaSonetSec15MinESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinESsOff.setStatus(
        "current"
    )

oaSonetSec15MinSESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 104)
)
oaSonetSec15MinSESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinSESsOn.setStatus(
        "current"
    )

oaSonetSec15MinSESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 105)
)
oaSonetSec15MinSESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinSESsOff.setStatus(
        "current"
    )

oaSonetSec15MinSEFSsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 106)
)
oaSonetSec15MinSEFSsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinSEFSsOn.setStatus(
        "current"
    )

oaSonetSec15MinSEFSsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 107)
)
oaSonetSec15MinSEFSsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinSEFSsOff.setStatus(
        "current"
    )

oaSonetSec15MinCVsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 108)
)
oaSonetSec15MinCVsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinCVsOn.setStatus(
        "current"
    )

oaSonetSec15MinCVsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 109)
)
oaSonetSec15MinCVsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSec15MinCVsOff.setStatus(
        "current"
    )

oaSonetSecCurrDayESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 110)
)
oaSonetSecCurrDayESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDayESsOn.setStatus(
        "current"
    )

oaSonetSecCurrDayESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 111)
)
oaSonetSecCurrDayESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDayESsOff.setStatus(
        "current"
    )

oaSonetSecCurrDaySESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 112)
)
oaSonetSecCurrDaySESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDaySESsOn.setStatus(
        "current"
    )

oaSonetSecCurrDaySESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 113)
)
oaSonetSecCurrDaySESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDaySESsOff.setStatus(
        "current"
    )

oaSonetSecCurrDaySEFSsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 114)
)
oaSonetSecCurrDaySEFSsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDaySEFSsOn.setStatus(
        "current"
    )

oaSonetSecCurrDaySEFSsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 115)
)
oaSonetSecCurrDaySEFSsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDaySEFSsOff.setStatus(
        "current"
    )

oaSonetSecCurrDayCVsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 116)
)
oaSonetSecCurrDayCVsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDayCVsOn.setStatus(
        "current"
    )

oaSonetSecCurrDayCVsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 117)
)
oaSonetSecCurrDayCVsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecCurrDayCVsOff.setStatus(
        "current"
    )

oaSonetNELine15MinESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 118)
)
oaSonetNELine15MinESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinESsOn.setStatus(
        "current"
    )

oaSonetNELine15MinESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 119)
)
oaSonetNELine15MinESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinESsOff.setStatus(
        "current"
    )

oaSonetNELine15MinSESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 120)
)
oaSonetNELine15MinSESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinSESsOn.setStatus(
        "current"
    )

oaSonetNELine15MinSESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 121)
)
oaSonetNELine15MinSESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinSESsOff.setStatus(
        "current"
    )

oaSonetNELine15MinCVsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 122)
)
oaSonetNELine15MinCVsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinCVsOn.setStatus(
        "current"
    )

oaSonetNELine15MinCVsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 123)
)
oaSonetNELine15MinCVsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinCVsOff.setStatus(
        "current"
    )

oaSonetNELine15MinUASsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 124)
)
oaSonetNELine15MinUASsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinUASsOn.setStatus(
        "current"
    )

oaSonetNELine15MinUASsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 125)
)
oaSonetNELine15MinUASsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELine15MinUASsOff.setStatus(
        "current"
    )

oaSonetFELine15MinESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 126)
)
oaSonetFELine15MinESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinESsOn.setStatus(
        "current"
    )

oaSonetFELine15MinESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 127)
)
oaSonetFELine15MinESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinESsOff.setStatus(
        "current"
    )

oaSonetFELine15MinSESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 128)
)
oaSonetFELine15MinSESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinSESsOn.setStatus(
        "current"
    )

oaSonetFELine15MinSESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 129)
)
oaSonetFELine15MinSESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinSESsOff.setStatus(
        "current"
    )

oaSonetFELine15MinCVsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 130)
)
oaSonetFELine15MinCVsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinCVsOn.setStatus(
        "current"
    )

oaSonetFELine15MinCVsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 131)
)
oaSonetFELine15MinCVsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinCVsOff.setStatus(
        "current"
    )

oaSonetFELine15MinUASsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 132)
)
oaSonetFELine15MinUASsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinUASsOn.setStatus(
        "current"
    )

oaSonetFELine15MinUASsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 133)
)
oaSonetFELine15MinUASsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELine15MinUASsOff.setStatus(
        "current"
    )

oaSonetNELineCurrDayESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 134)
)
oaSonetNELineCurrDayESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayESsOn.setStatus(
        "current"
    )

oaSonetNELineCurrDayESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 135)
)
oaSonetNELineCurrDayESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayESsOff.setStatus(
        "current"
    )

oaSonetNELineCurrDaySESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 136)
)
oaSonetNELineCurrDaySESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDaySESsOn.setStatus(
        "current"
    )

oaSonetNELineCurrDaySESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 137)
)
oaSonetNELineCurrDaySESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDaySESsOff.setStatus(
        "current"
    )

oaSonetNELineCurrDayCVsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 138)
)
oaSonetNELineCurrDayCVsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayCVsOn.setStatus(
        "current"
    )

oaSonetNELineCurrDayCVsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 139)
)
oaSonetNELineCurrDayCVsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayCVsOff.setStatus(
        "current"
    )

oaSonetNELineCurrDayUASsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 140)
)
oaSonetNELineCurrDayUASsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayUASsOn.setStatus(
        "current"
    )

oaSonetNELineCurrDayUASsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 141)
)
oaSonetNELineCurrDayUASsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetNELineCurrDayUASsOff.setStatus(
        "current"
    )

oaSonetFELineCurrDayESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 142)
)
oaSonetFELineCurrDayESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayESsOn.setStatus(
        "current"
    )

oaSonetFELineCurrDayESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 143)
)
oaSonetFELineCurrDayESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayESsOff.setStatus(
        "current"
    )

oaSonetFELineCurrDaySESsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 144)
)
oaSonetFELineCurrDaySESsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDaySESsOn.setStatus(
        "current"
    )

oaSonetFELineCurrDaySESsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 145)
)
oaSonetFELineCurrDaySESsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDaySESsOff.setStatus(
        "current"
    )

oaSonetFELineCurrDayCVsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 146)
)
oaSonetFELineCurrDayCVsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayCVsOn.setStatus(
        "current"
    )

oaSonetFELineCurrDayCVsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 147)
)
oaSonetFELineCurrDayCVsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayCVsOff.setStatus(
        "current"
    )

oaSonetFELineCurrDayUASsOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 148)
)
oaSonetFELineCurrDayUASsOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayUASsOn.setStatus(
        "current"
    )

oaSonetFELineCurrDayUASsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 149)
)
oaSonetFELineCurrDayUASsOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetLineIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetFELineCurrDayUASsOff.setStatus(
        "current"
    )

oaSonetSecLosAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 151)
)
oaSonetSecLosAlarmOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecLosAlarmOn.setStatus(
        "current"
    )

oaSonetSecLosAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 152)
)
oaSonetSecLosAlarmOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetSecLosAlarmOff.setStatus(
        "current"
    )

oaSonetLineAisAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 153)
)
oaSonetLineAisAlarmOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineAisAlarmOn.setStatus(
        "current"
    )

oaSonetLineAisAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 154)
)
oaSonetLineAisAlarmOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineAisAlarmOff.setStatus(
        "current"
    )

oaSonetLineRdiAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 155)
)
oaSonetLineRdiAlarmOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineRdiAlarmOn.setStatus(
        "current"
    )

oaSonetLineRdiAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 156)
)
oaSonetLineRdiAlarmOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineRdiAlarmOff.setStatus(
        "current"
    )

oaSonetLineSideOtuLosAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 157)
)
oaSonetLineSideOtuLosAlarmOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineSideOtuLosAlarmOn.setStatus(
        "current"
    )

oaSonetLineSideOtuLosAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 158)
)
oaSonetLineSideOtuLosAlarmOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineSideOtuLosAlarmOff.setStatus(
        "current"
    )

oaSonetLineSideOtuAisAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 159)
)
oaSonetLineSideOtuAisAlarmOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineSideOtuAisAlarmOn.setStatus(
        "current"
    )

oaSonetLineSideOtuAisAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 160)
)
oaSonetLineSideOtuAisAlarmOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineSideOtuAisAlarmOff.setStatus(
        "current"
    )

oaSonetLineSideOtuIaeAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 161)
)
oaSonetLineSideOtuIaeAlarmOn.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineSideOtuIaeAlarmOn.setStatus(
        "current"
    )

oaSonetLineSideOtuIaeAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 0, 162)
)
oaSonetLineSideOtuIaeAlarmOff.setObjects(
      *(("OADWDM-MIB", "oaLdCardPortsSlotNumber"),
        ("OADWDM-MIB", "oaLdCardPortsPortNumber"),
        ("OA-SONET-MIB", "oaSonetSecIfIndex"),
        ("OA-TRAP-MESSAGES-MIB", "oaDevTrapsPortsIfAlias"))
)
if mibBuilder.loadTexts:
    oaSonetLineSideOtuIaeAlarmOff.setStatus(
        "current"
    )


# Notifications groups

oaSonetSecTcaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 9)
)
oaSonetSecTcaNotificationsGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetSec15MinESsOn"),
        ("OA-SONET-MIB", "oaSonetSec15MinESsOff"),
        ("OA-SONET-MIB", "oaSonetSec15MinSESsOn"),
        ("OA-SONET-MIB", "oaSonetSec15MinSESsOff"),
        ("OA-SONET-MIB", "oaSonetSec15MinSEFSsOn"),
        ("OA-SONET-MIB", "oaSonetSec15MinSEFSsOff"),
        ("OA-SONET-MIB", "oaSonetSec15MinCVsOn"),
        ("OA-SONET-MIB", "oaSonetSec15MinCVsOff"),
        ("OA-SONET-MIB", "oaSonetSecCurrDayESsOn"),
        ("OA-SONET-MIB", "oaSonetSecCurrDayESsOff"),
        ("OA-SONET-MIB", "oaSonetSecCurrDaySESsOn"),
        ("OA-SONET-MIB", "oaSonetSecCurrDaySESsOff"),
        ("OA-SONET-MIB", "oaSonetSecCurrDaySEFSsOn"),
        ("OA-SONET-MIB", "oaSonetSecCurrDaySEFSsOff"),
        ("OA-SONET-MIB", "oaSonetSecCurrDayCVsOn"),
        ("OA-SONET-MIB", "oaSonetSecCurrDayCVsOff"))
)
if mibBuilder.loadTexts:
    oaSonetSecTcaNotificationsGroup.setStatus(
        "current"
    )

oaSonetNELineTcaNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 10)
)
oaSonetNELineTcaNotifGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetNELine15MinESsOn"),
        ("OA-SONET-MIB", "oaSonetNELine15MinESsOff"),
        ("OA-SONET-MIB", "oaSonetNELine15MinSESsOn"),
        ("OA-SONET-MIB", "oaSonetNELine15MinSESsOff"),
        ("OA-SONET-MIB", "oaSonetNELine15MinCVsOn"),
        ("OA-SONET-MIB", "oaSonetNELine15MinCVsOff"),
        ("OA-SONET-MIB", "oaSonetNELine15MinUASsOn"),
        ("OA-SONET-MIB", "oaSonetNELine15MinUASsOff"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayESsOn"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayESsOff"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDaySESsOn"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDaySESsOff"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayCVsOn"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayCVsOff"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayUASsOn"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayUASsOff"))
)
if mibBuilder.loadTexts:
    oaSonetNELineTcaNotifGroup.setStatus(
        "current"
    )

oaSonetFELineTcaNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 11)
)
oaSonetFELineTcaNotifGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetFELine15MinESsOn"),
        ("OA-SONET-MIB", "oaSonetFELine15MinESsOff"),
        ("OA-SONET-MIB", "oaSonetFELine15MinSESsOn"),
        ("OA-SONET-MIB", "oaSonetFELine15MinSESsOff"),
        ("OA-SONET-MIB", "oaSonetFELine15MinCVsOn"),
        ("OA-SONET-MIB", "oaSonetFELine15MinCVsOff"),
        ("OA-SONET-MIB", "oaSonetFELine15MinUASsOn"),
        ("OA-SONET-MIB", "oaSonetFELine15MinUASsOff"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayESsOn"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayESsOff"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDaySESsOn"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDaySESsOff"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayCVsOn"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayCVsOff"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayUASsOn"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayUASsOff"))
)
if mibBuilder.loadTexts:
    oaSonetFELineTcaNotifGroup.setStatus(
        "current"
    )

oaSonetSecNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 12)
)
oaSonetSecNotificationsGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetSecLosAlarmOn"),
        ("OA-SONET-MIB", "oaSonetSecLosAlarmOff"))
)
if mibBuilder.loadTexts:
    oaSonetSecNotificationsGroup.setStatus(
        "current"
    )

oaSonetLineNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 13)
)
oaSonetLineNotificationsGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetLineAisAlarmOn"),
        ("OA-SONET-MIB", "oaSonetLineAisAlarmOff"),
        ("OA-SONET-MIB", "oaSonetLineRdiAlarmOn"),
        ("OA-SONET-MIB", "oaSonetLineRdiAlarmOff"))
)
if mibBuilder.loadTexts:
    oaSonetLineNotificationsGroup.setStatus(
        "current"
    )

oaOtuLineNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 1, 14)
)
oaOtuLineNotificationsGroup.setObjects(
      *(("OA-SONET-MIB", "oaSonetLineSideOtuLosAlarmOn"),
        ("OA-SONET-MIB", "oaSonetLineSideOtuLosAlarmOff"),
        ("OA-SONET-MIB", "oaSonetLineSideOtuAisAlarmOn"),
        ("OA-SONET-MIB", "oaSonetLineSideOtuAisAlarmOff"),
        ("OA-SONET-MIB", "oaSonetLineSideOtuIaeAlarmOn"),
        ("OA-SONET-MIB", "oaSonetLineSideOtuIaeAlarmOff"))
)
if mibBuilder.loadTexts:
    oaOtuLineNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

oaSonetMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 81, 3, 2, 1)
)
oaSonetMIBCompliance.setObjects(
      *(("OA-SONET-MIB", "oaSonetSecTcaGroup"),
        ("OA-SONET-MIB", "oaSonetLineTcaGroup"),
        ("OA-SONET-MIB", "oaSonetSecCurrDayGroup"),
        ("OA-SONET-MIB", "oaSonetSecPrevDayGroup"),
        ("OA-SONET-MIB", "oaSonetNELineCurrDayGroup"),
        ("OA-SONET-MIB", "oaSonetNELinePrevDayGroup"),
        ("OA-SONET-MIB", "oaSonetGenParamsGroup"),
        ("OA-SONET-MIB", "oaSonetFELineCurrDayGroup"),
        ("OA-SONET-MIB", "oaSonetFELinePrevDayGroup"))
)
if mibBuilder.loadTexts:
    oaSonetMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-SONET-MIB",
    **{"oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaSonetMib": oaSonetMib,
       "oaSonetNotifications": oaSonetNotifications,
       "oaSonetSec15MinESsOn": oaSonetSec15MinESsOn,
       "oaSonetSec15MinESsOff": oaSonetSec15MinESsOff,
       "oaSonetSec15MinSESsOn": oaSonetSec15MinSESsOn,
       "oaSonetSec15MinSESsOff": oaSonetSec15MinSESsOff,
       "oaSonetSec15MinSEFSsOn": oaSonetSec15MinSEFSsOn,
       "oaSonetSec15MinSEFSsOff": oaSonetSec15MinSEFSsOff,
       "oaSonetSec15MinCVsOn": oaSonetSec15MinCVsOn,
       "oaSonetSec15MinCVsOff": oaSonetSec15MinCVsOff,
       "oaSonetSecCurrDayESsOn": oaSonetSecCurrDayESsOn,
       "oaSonetSecCurrDayESsOff": oaSonetSecCurrDayESsOff,
       "oaSonetSecCurrDaySESsOn": oaSonetSecCurrDaySESsOn,
       "oaSonetSecCurrDaySESsOff": oaSonetSecCurrDaySESsOff,
       "oaSonetSecCurrDaySEFSsOn": oaSonetSecCurrDaySEFSsOn,
       "oaSonetSecCurrDaySEFSsOff": oaSonetSecCurrDaySEFSsOff,
       "oaSonetSecCurrDayCVsOn": oaSonetSecCurrDayCVsOn,
       "oaSonetSecCurrDayCVsOff": oaSonetSecCurrDayCVsOff,
       "oaSonetNELine15MinESsOn": oaSonetNELine15MinESsOn,
       "oaSonetNELine15MinESsOff": oaSonetNELine15MinESsOff,
       "oaSonetNELine15MinSESsOn": oaSonetNELine15MinSESsOn,
       "oaSonetNELine15MinSESsOff": oaSonetNELine15MinSESsOff,
       "oaSonetNELine15MinCVsOn": oaSonetNELine15MinCVsOn,
       "oaSonetNELine15MinCVsOff": oaSonetNELine15MinCVsOff,
       "oaSonetNELine15MinUASsOn": oaSonetNELine15MinUASsOn,
       "oaSonetNELine15MinUASsOff": oaSonetNELine15MinUASsOff,
       "oaSonetFELine15MinESsOn": oaSonetFELine15MinESsOn,
       "oaSonetFELine15MinESsOff": oaSonetFELine15MinESsOff,
       "oaSonetFELine15MinSESsOn": oaSonetFELine15MinSESsOn,
       "oaSonetFELine15MinSESsOff": oaSonetFELine15MinSESsOff,
       "oaSonetFELine15MinCVsOn": oaSonetFELine15MinCVsOn,
       "oaSonetFELine15MinCVsOff": oaSonetFELine15MinCVsOff,
       "oaSonetFELine15MinUASsOn": oaSonetFELine15MinUASsOn,
       "oaSonetFELine15MinUASsOff": oaSonetFELine15MinUASsOff,
       "oaSonetNELineCurrDayESsOn": oaSonetNELineCurrDayESsOn,
       "oaSonetNELineCurrDayESsOff": oaSonetNELineCurrDayESsOff,
       "oaSonetNELineCurrDaySESsOn": oaSonetNELineCurrDaySESsOn,
       "oaSonetNELineCurrDaySESsOff": oaSonetNELineCurrDaySESsOff,
       "oaSonetNELineCurrDayCVsOn": oaSonetNELineCurrDayCVsOn,
       "oaSonetNELineCurrDayCVsOff": oaSonetNELineCurrDayCVsOff,
       "oaSonetNELineCurrDayUASsOn": oaSonetNELineCurrDayUASsOn,
       "oaSonetNELineCurrDayUASsOff": oaSonetNELineCurrDayUASsOff,
       "oaSonetFELineCurrDayESsOn": oaSonetFELineCurrDayESsOn,
       "oaSonetFELineCurrDayESsOff": oaSonetFELineCurrDayESsOff,
       "oaSonetFELineCurrDaySESsOn": oaSonetFELineCurrDaySESsOn,
       "oaSonetFELineCurrDaySESsOff": oaSonetFELineCurrDaySESsOff,
       "oaSonetFELineCurrDayCVsOn": oaSonetFELineCurrDayCVsOn,
       "oaSonetFELineCurrDayCVsOff": oaSonetFELineCurrDayCVsOff,
       "oaSonetFELineCurrDayUASsOn": oaSonetFELineCurrDayUASsOn,
       "oaSonetFELineCurrDayUASsOff": oaSonetFELineCurrDayUASsOff,
       "oaSonetSecLosAlarmOn": oaSonetSecLosAlarmOn,
       "oaSonetSecLosAlarmOff": oaSonetSecLosAlarmOff,
       "oaSonetLineAisAlarmOn": oaSonetLineAisAlarmOn,
       "oaSonetLineAisAlarmOff": oaSonetLineAisAlarmOff,
       "oaSonetLineRdiAlarmOn": oaSonetLineRdiAlarmOn,
       "oaSonetLineRdiAlarmOff": oaSonetLineRdiAlarmOff,
       "oaSonetLineSideOtuLosAlarmOn": oaSonetLineSideOtuLosAlarmOn,
       "oaSonetLineSideOtuLosAlarmOff": oaSonetLineSideOtuLosAlarmOff,
       "oaSonetLineSideOtuAisAlarmOn": oaSonetLineSideOtuAisAlarmOn,
       "oaSonetLineSideOtuAisAlarmOff": oaSonetLineSideOtuAisAlarmOff,
       "oaSonetLineSideOtuIaeAlarmOn": oaSonetLineSideOtuIaeAlarmOn,
       "oaSonetLineSideOtuIaeAlarmOff": oaSonetLineSideOtuIaeAlarmOff,
       "oaSonetSection": oaSonetSection,
       "oaSonetSecTcaTable": oaSonetSecTcaTable,
       "oaSonetSecTcaEntry": oaSonetSecTcaEntry,
       "oaSonetSecIfIndex": oaSonetSecIfIndex,
       "oaSonetSec15MinESsTca": oaSonetSec15MinESsTca,
       "oaSonetSecDayESsTca": oaSonetSecDayESsTca,
       "oaSonetSec15MinSESsTca": oaSonetSec15MinSESsTca,
       "oaSonetSecDaySESsTca": oaSonetSecDaySESsTca,
       "oaSonetSec15MinSEFSsTca": oaSonetSec15MinSEFSsTca,
       "oaSonetSecDaySEFSsTca": oaSonetSecDaySEFSsTca,
       "oaSonetSec15MinCVsTca": oaSonetSec15MinCVsTca,
       "oaSonetSecDayCVsTca": oaSonetSecDayCVsTca,
       "oaSonetSec15MinUASsTca": oaSonetSec15MinUASsTca,
       "oaSonetSecDayUASsTca": oaSonetSecDayUASsTca,
       "oaSonetSecCurrDayTable": oaSonetSecCurrDayTable,
       "oaSonetSecCurrDayEntry": oaSonetSecCurrDayEntry,
       "oaSonetSecCurrDayIfIndex": oaSonetSecCurrDayIfIndex,
       "oaSonetSecCurrDayESs": oaSonetSecCurrDayESs,
       "oaSonetSecCurrDaySESs": oaSonetSecCurrDaySESs,
       "oaSonetSecCurrDaySEFSs": oaSonetSecCurrDaySEFSs,
       "oaSonetSecCurrDayCVs": oaSonetSecCurrDayCVs,
       "oaSonetSecPrevDayTable": oaSonetSecPrevDayTable,
       "oaSonetSecPrevDayEntry": oaSonetSecPrevDayEntry,
       "oaSonetSecPrevDayIfIndex": oaSonetSecPrevDayIfIndex,
       "oaSonetSecPrevDayESs": oaSonetSecPrevDayESs,
       "oaSonetSecPrevDaySESs": oaSonetSecPrevDaySESs,
       "oaSonetSecPrevDaySEFSs": oaSonetSecPrevDaySEFSs,
       "oaSonetSecPrevDayCVs": oaSonetSecPrevDayCVs,
       "oaSonetSecPrevDayValidData": oaSonetSecPrevDayValidData,
       "oaSonetLine": oaSonetLine,
       "oaSonetLineTcaTable": oaSonetLineTcaTable,
       "oaSonetLineTcaEntry": oaSonetLineTcaEntry,
       "oaSonetLineIfIndex": oaSonetLineIfIndex,
       "oaSonetLine15MinESsTca": oaSonetLine15MinESsTca,
       "oaSonetLineDayESsTca": oaSonetLineDayESsTca,
       "oaSonetLine15MinSESsTca": oaSonetLine15MinSESsTca,
       "oaSonetLineDaySESsTca": oaSonetLineDaySESsTca,
       "oaSonetLine15MinCVsTca": oaSonetLine15MinCVsTca,
       "oaSonetLineDayCVsTca": oaSonetLineDayCVsTca,
       "oaSonetLine15MinUASsTca": oaSonetLine15MinUASsTca,
       "oaSonetLineDayUASsTca": oaSonetLineDayUASsTca,
       "oaSonetLineCurrDayTable": oaSonetLineCurrDayTable,
       "oaSonetLineCurrDayEntry": oaSonetLineCurrDayEntry,
       "oaSonetLineCurrDayIfIndex": oaSonetLineCurrDayIfIndex,
       "oaSonetNELineCurrDayESs": oaSonetNELineCurrDayESs,
       "oaSonetNELineCurrDaySESs": oaSonetNELineCurrDaySESs,
       "oaSonetNELineCurrDayCVs": oaSonetNELineCurrDayCVs,
       "oaSonetNELineCurrDayUASs": oaSonetNELineCurrDayUASs,
       "oaSonetFELineCurrDayESs": oaSonetFELineCurrDayESs,
       "oaSonetFELineCurrDaySESs": oaSonetFELineCurrDaySESs,
       "oaSonetFELineCurrDayCVs": oaSonetFELineCurrDayCVs,
       "oaSonetFELineCurrDayUASs": oaSonetFELineCurrDayUASs,
       "oaSonetLinePrevDayTable": oaSonetLinePrevDayTable,
       "oaSonetLinePrevDayEntry": oaSonetLinePrevDayEntry,
       "oaSonetLinePrevDayIfIndex": oaSonetLinePrevDayIfIndex,
       "oaSonetNELinePrevDayESs": oaSonetNELinePrevDayESs,
       "oaSonetNELinePrevDaySESs": oaSonetNELinePrevDaySESs,
       "oaSonetNELinePrevDayCVs": oaSonetNELinePrevDayCVs,
       "oaSonetNELinePrevDayUASs": oaSonetNELinePrevDayUASs,
       "oaSonetFELinePrevDayESs": oaSonetFELinePrevDayESs,
       "oaSonetFELinePrevDaySESs": oaSonetFELinePrevDaySESs,
       "oaSonetFELinePrevDayCVs": oaSonetFELinePrevDayCVs,
       "oaSonetFELinePrevDayUASs": oaSonetFELinePrevDayUASs,
       "oaSonetLinePrevDayValidData": oaSonetLinePrevDayValidData,
       "oaSonetMIBConformance": oaSonetMIBConformance,
       "oaSonetMIBGroups": oaSonetMIBGroups,
       "oaSonetSecTcaGroup": oaSonetSecTcaGroup,
       "oaSonetLineTcaGroup": oaSonetLineTcaGroup,
       "oaSonetSecCurrDayGroup": oaSonetSecCurrDayGroup,
       "oaSonetSecPrevDayGroup": oaSonetSecPrevDayGroup,
       "oaSonetNELineCurrDayGroup": oaSonetNELineCurrDayGroup,
       "oaSonetNELinePrevDayGroup": oaSonetNELinePrevDayGroup,
       "oaSonetFELineCurrDayGroup": oaSonetFELineCurrDayGroup,
       "oaSonetFELinePrevDayGroup": oaSonetFELinePrevDayGroup,
       "oaSonetSecTcaNotificationsGroup": oaSonetSecTcaNotificationsGroup,
       "oaSonetNELineTcaNotifGroup": oaSonetNELineTcaNotifGroup,
       "oaSonetFELineTcaNotifGroup": oaSonetFELineTcaNotifGroup,
       "oaSonetSecNotificationsGroup": oaSonetSecNotificationsGroup,
       "oaSonetLineNotificationsGroup": oaSonetLineNotificationsGroup,
       "oaOtuLineNotificationsGroup": oaOtuLineNotificationsGroup,
       "oaSonetGenParamsGroup": oaSonetGenParamsGroup,
       "oaSonetMIBCompliances": oaSonetMIBCompliances,
       "oaSonetMIBCompliance": oaSonetMIBCompliance,
       "oaSonetGenParams": oaSonetGenParams,
       "oaSonetMibImplementRevision": oaSonetMibImplementRevision}
)
