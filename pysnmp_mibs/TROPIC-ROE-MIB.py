# SNMP MIB module (TROPIC-ROE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-ROE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:53:20 2025
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
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(TItemDescription,
 TmnxPortID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TmnxPortID")

(tnPortModules,
 tnRoeMib) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnPortModules",
    "tnRoeMib")


# MODULE-IDENTITY

tnRoeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 10)
)
if mibBuilder.loadTexts:
    tnRoeMibModule.setRevisions(
        ("2021-04-30 12:00",
         "2021-01-08 12:00",
         "2020-12-18 12:00",
         "2020-10-23 12:00",
         "2020-06-19 12:00",
         "2020-04-03 12:00",
         "2020-02-28 12:00",
         "2020-01-24 12:00",
         "2019-09-13 12:00",
         "2018-08-24 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicRoeCardType(TextualConvention, Integer32):
    status = "current"
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
        *(("t24PS1", 1),
          ("t24PS2", 2),
          ("t12PS", 3),
          ("s24PS1", 4),
          ("s24PS2", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TnRoeNotifications_ObjectIdentity = ObjectIdentity
tnRoeNotifications = _TnRoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 0)
)
_TnRoeObjects_ObjectIdentity = ObjectIdentity
tnRoeObjects = _TnRoeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1)
)
_TnRoeParameters_ObjectIdentity = ObjectIdentity
tnRoeParameters = _TnRoeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1)
)
_TnRoeSeqProfTable_Object = MibTable
tnRoeSeqProfTable = _TnRoeSeqProfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnRoeSeqProfTable.setStatus("current")
_TnRoeSeqProfEntry_Object = MibTableRow
tnRoeSeqProfEntry = _TnRoeSeqProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1)
)
tnRoeSeqProfEntry.setIndexNames(
    (0, "TROPIC-ROE-MIB", "tnRoeSeqProfCardType"),
    (0, "TROPIC-ROE-MIB", "tnRoeSeqProfPortID"),
    (0, "TROPIC-ROE-MIB", "tnRoeSeqProfID"),
)
if mibBuilder.loadTexts:
    tnRoeSeqProfEntry.setStatus("current")
_TnRoeSeqProfCardType_Type = TropicRoeCardType
_TnRoeSeqProfCardType_Object = MibTableColumn
tnRoeSeqProfCardType = _TnRoeSeqProfCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 1),
    _TnRoeSeqProfCardType_Type()
)
tnRoeSeqProfCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeSeqProfCardType.setStatus("current")
_TnRoeSeqProfPortID_Type = TmnxPortID
_TnRoeSeqProfPortID_Object = MibTableColumn
tnRoeSeqProfPortID = _TnRoeSeqProfPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 2),
    _TnRoeSeqProfPortID_Type()
)
tnRoeSeqProfPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeSeqProfPortID.setStatus("current")


class _TnRoeSeqProfID_Type(Integer32):
    """Custom type tnRoeSeqProfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeSeqProfID_Type.__name__ = "Integer32"
_TnRoeSeqProfID_Object = MibTableColumn
tnRoeSeqProfID = _TnRoeSeqProfID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 3),
    _TnRoeSeqProfID_Type()
)
tnRoeSeqProfID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeSeqProfID.setStatus("current")
_TnRoeSeqProfDescription_Type = TItemDescription
_TnRoeSeqProfDescription_Object = MibTableColumn
tnRoeSeqProfDescription = _TnRoeSeqProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 4),
    _TnRoeSeqProfDescription_Type()
)
tnRoeSeqProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfDescription.setStatus("current")


class _TnRoeSeqProfType_Type(Integer32):
    """Custom type tnRoeSeqProfType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("frmrnum", 0),
          ("seqnum", 1))
    )


_TnRoeSeqProfType_Type.__name__ = "Integer32"
_TnRoeSeqProfType_Object = MibTableColumn
tnRoeSeqProfType = _TnRoeSeqProfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 5),
    _TnRoeSeqProfType_Type()
)
tnRoeSeqProfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfType.setStatus("current")


class _TnRoeSeqProfPMax_Type(Unsigned32):
    """Custom type tnRoeSeqProfPMax based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TnRoeSeqProfPMax_Type.__name__ = "Unsigned32"
_TnRoeSeqProfPMax_Object = MibTableColumn
tnRoeSeqProfPMax = _TnRoeSeqProfPMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 6),
    _TnRoeSeqProfPMax_Type()
)
tnRoeSeqProfPMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfPMax.setStatus("current")


class _TnRoeSeqProfPIncProp_Type(Integer32):
    """Custom type tnRoeSeqProfPIncProp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("payloadsize", 1))
    )


_TnRoeSeqProfPIncProp_Type.__name__ = "Integer32"
_TnRoeSeqProfPIncProp_Object = MibTableColumn
tnRoeSeqProfPIncProp = _TnRoeSeqProfPIncProp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 7),
    _TnRoeSeqProfPIncProp_Type()
)
tnRoeSeqProfPIncProp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfPIncProp.setStatus("current")


class _TnRoeSeqProfPInc_Type(Unsigned32):
    """Custom type tnRoeSeqProfPInc based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnRoeSeqProfPInc_Type.__name__ = "Unsigned32"
_TnRoeSeqProfPInc_Object = MibTableColumn
tnRoeSeqProfPInc = _TnRoeSeqProfPInc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 8),
    _TnRoeSeqProfPInc_Type()
)
tnRoeSeqProfPInc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfPInc.setStatus("current")


class _TnRoeSeqProfQMax_Type(Unsigned32):
    """Custom type tnRoeSeqProfQMax based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TnRoeSeqProfQMax_Type.__name__ = "Unsigned32"
_TnRoeSeqProfQMax_Object = MibTableColumn
tnRoeSeqProfQMax = _TnRoeSeqProfQMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 9),
    _TnRoeSeqProfQMax_Type()
)
tnRoeSeqProfQMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfQMax.setStatus("current")


class _TnRoeSeqProfQIncProp_Type(Integer32):
    """Custom type tnRoeSeqProfQIncProp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("payloadsize", 1))
    )


_TnRoeSeqProfQIncProp_Type.__name__ = "Integer32"
_TnRoeSeqProfQIncProp_Object = MibTableColumn
tnRoeSeqProfQIncProp = _TnRoeSeqProfQIncProp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 10),
    _TnRoeSeqProfQIncProp_Type()
)
tnRoeSeqProfQIncProp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfQIncProp.setStatus("current")


class _TnRoeSeqProfQInc_Type(Unsigned32):
    """Custom type tnRoeSeqProfQInc based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnRoeSeqProfQInc_Type.__name__ = "Unsigned32"
_TnRoeSeqProfQInc_Object = MibTableColumn
tnRoeSeqProfQInc = _TnRoeSeqProfQInc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 11),
    _TnRoeSeqProfQInc_Type()
)
tnRoeSeqProfQInc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfQInc.setStatus("current")
_TnRoeSeqProfRowStatus_Type = RowStatus
_TnRoeSeqProfRowStatus_Object = MibTableColumn
tnRoeSeqProfRowStatus = _TnRoeSeqProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 1, 1, 12),
    _TnRoeSeqProfRowStatus_Type()
)
tnRoeSeqProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqProfRowStatus.setStatus("current")
_TnRoeTable_Object = MibTable
tnRoeTable = _TnRoeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnRoeTable.setStatus("current")
_TnRoeEntry_Object = MibTableRow
tnRoeEntry = _TnRoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1)
)
tnRoeEntry.setIndexNames(
    (0, "TROPIC-ROE-MIB", "tnRoeCardType"),
    (0, "TROPIC-ROE-MIB", "tnRoePortID"),
)
if mibBuilder.loadTexts:
    tnRoeEntry.setStatus("current")
_TnRoeCardType_Type = TropicRoeCardType
_TnRoeCardType_Object = MibTableColumn
tnRoeCardType = _TnRoeCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 1),
    _TnRoeCardType_Type()
)
tnRoeCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeCardType.setStatus("current")
_TnRoePortID_Type = TmnxPortID
_TnRoePortID_Object = MibTableColumn
tnRoePortID = _TnRoePortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 2),
    _TnRoePortID_Type()
)
tnRoePortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoePortID.setStatus("current")
_TnRoeDescription_Type = TItemDescription
_TnRoeDescription_Object = MibTableColumn
tnRoeDescription = _TnRoeDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 3),
    _TnRoeDescription_Type()
)
tnRoeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDescription.setStatus("current")


class _TnRoeOrderInfoType_Type(Integer32):
    """Custom type tnRoeOrderInfoType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prestime", 0),
          ("seqnum", 1))
    )


_TnRoeOrderInfoType_Type.__name__ = "Integer32"
_TnRoeOrderInfoType_Object = MibTableColumn
tnRoeOrderInfoType = _TnRoeOrderInfoType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 4),
    _TnRoeOrderInfoType_Type()
)
tnRoeOrderInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeOrderInfoType.setStatus("current")


class _TnRoePresTimeOffset_Type(Integer32):
    """Custom type tnRoePresTimeOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1677721600),
    )


_TnRoePresTimeOffset_Type.__name__ = "Integer32"
_TnRoePresTimeOffset_Object = MibTableColumn
tnRoePresTimeOffset = _TnRoePresTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 5),
    _TnRoePresTimeOffset_Type()
)
tnRoePresTimeOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoePresTimeOffset.setStatus("current")


class _TnRoeCpriTxGenOffset_Type(OctetString):
    """Custom type tnRoeCpriTxGenOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_TnRoeCpriTxGenOffset_Type.__name__ = "OctetString"
_TnRoeCpriTxGenOffset_Object = MibTableColumn
tnRoeCpriTxGenOffset = _TnRoeCpriTxGenOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 6),
    _TnRoeCpriTxGenOffset_Type()
)
tnRoeCpriTxGenOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeCpriTxGenOffset.setStatus("current")


class _TnRoeAutoUponChange_Type(Integer32):
    """Custom type tnRoeAutoUponChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TnRoeAutoUponChange_Type.__name__ = "Integer32"
_TnRoeAutoUponChange_Object = MibTableColumn
tnRoeAutoUponChange = _TnRoeAutoUponChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 7),
    _TnRoeAutoUponChange_Type()
)
tnRoeAutoUponChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeAutoUponChange.setStatus("current")


class _TnRoeSeqNumProfID_Type(Integer32):
    """Custom type tnRoeSeqNumProfID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeSeqNumProfID_Type.__name__ = "Integer32"
_TnRoeSeqNumProfID_Object = MibTableColumn
tnRoeSeqNumProfID = _TnRoeSeqNumProfID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 8),
    _TnRoeSeqNumProfID_Type()
)
tnRoeSeqNumProfID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSeqNumProfID.setStatus("current")


class _TnRoeInitialTxBFN_Type(Integer32):
    """Custom type tnRoeInitialTxBFN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TnRoeInitialTxBFN_Type.__name__ = "Integer32"
_TnRoeInitialTxBFN_Object = MibTableColumn
tnRoeInitialTxBFN = _TnRoeInitialTxBFN_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 9),
    _TnRoeInitialTxBFN_Type()
)
tnRoeInitialTxBFN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeInitialTxBFN.setStatus("current")


class _TnRoeInitialTxHFN_Type(Integer32):
    """Custom type tnRoeInitialTxHFN based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 149),
    )


_TnRoeInitialTxHFN_Type.__name__ = "Integer32"
_TnRoeInitialTxHFN_Object = MibTableColumn
tnRoeInitialTxHFN = _TnRoeInitialTxHFN_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 10),
    _TnRoeInitialTxHFN_Type()
)
tnRoeInitialTxHFN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeInitialTxHFN.setStatus("current")


class _TnRoeEncapMode_Type(Integer32):
    """Custom type tnRoeEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("tunneling", 6),
          ("linecodeAware", 7),
          ("structureAware", 8),
          ("structureAwareControl", 9))
    )


_TnRoeEncapMode_Type.__name__ = "Integer32"
_TnRoeEncapMode_Object = MibTableColumn
tnRoeEncapMode = _TnRoeEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 11),
    _TnRoeEncapMode_Type()
)
tnRoeEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeEncapMode.setStatus("current")


class _TnRoeAdminState_Type(Integer32):
    """Custom type tnRoeAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 3))
    )


_TnRoeAdminState_Type.__name__ = "Integer32"
_TnRoeAdminState_Object = MibTableColumn
tnRoeAdminState = _TnRoeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 12),
    _TnRoeAdminState_Type()
)
tnRoeAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeAdminState.setStatus("current")


class _TnRoePmonPolicy_Type(Integer32):
    """Custom type tnRoePmonPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnRoePmonPolicy_Type.__name__ = "Integer32"
_TnRoePmonPolicy_Object = MibTableColumn
tnRoePmonPolicy = _TnRoePmonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 13),
    _TnRoePmonPolicy_Type()
)
tnRoePmonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoePmonPolicy.setStatus("current")
_TnRoeRowStatus_Type = RowStatus
_TnRoeRowStatus_Object = MibTableColumn
tnRoeRowStatus = _TnRoeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 14),
    _TnRoeRowStatus_Type()
)
tnRoeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeRowStatus.setStatus("current")


class _TnRoeAlmProfName_Type(OctetString):
    """Custom type tnRoeAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnRoeAlmProfName_Type.__name__ = "OctetString"
_TnRoeAlmProfName_Object = MibTableColumn
tnRoeAlmProfName = _TnRoeAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 15),
    _TnRoeAlmProfName_Type()
)
tnRoeAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeAlmProfName.setStatus("current")


class _TnRoePresTimeOffsetSubNano_Type(Integer32):
    """Custom type tnRoePresTimeOffsetSubNano based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnRoePresTimeOffsetSubNano_Type.__name__ = "Integer32"
_TnRoePresTimeOffsetSubNano_Object = MibTableColumn
tnRoePresTimeOffsetSubNano = _TnRoePresTimeOffsetSubNano_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 16),
    _TnRoePresTimeOffsetSubNano_Type()
)
tnRoePresTimeOffsetSubNano.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoePresTimeOffsetSubNano.setStatus("current")


class _TnRoePresTimeOffsetNano_Type(Integer32):
    """Custom type tnRoePresTimeOffsetNano based on Integer32"""
    defaultValue = 100000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 16777216),
    )


_TnRoePresTimeOffsetNano_Type.__name__ = "Integer32"
_TnRoePresTimeOffsetNano_Object = MibTableColumn
tnRoePresTimeOffsetNano = _TnRoePresTimeOffsetNano_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 17),
    _TnRoePresTimeOffsetNano_Type()
)
tnRoePresTimeOffsetNano.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoePresTimeOffsetNano.setStatus("current")


class _TnRoeTargetOffsetSubNano_Type(Integer32):
    """Custom type tnRoeTargetOffsetSubNano based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnRoeTargetOffsetSubNano_Type.__name__ = "Integer32"
_TnRoeTargetOffsetSubNano_Object = MibTableColumn
tnRoeTargetOffsetSubNano = _TnRoeTargetOffsetSubNano_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 18),
    _TnRoeTargetOffsetSubNano_Type()
)
tnRoeTargetOffsetSubNano.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeTargetOffsetSubNano.setStatus("current")


class _TnRoeTargetOffsetNano_Type(Integer32):
    """Custom type tnRoeTargetOffsetNano based on Integer32"""
    defaultValue = 100000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 16777216),
    )


_TnRoeTargetOffsetNano_Type.__name__ = "Integer32"
_TnRoeTargetOffsetNano_Object = MibTableColumn
tnRoeTargetOffsetNano = _TnRoeTargetOffsetNano_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 19),
    _TnRoeTargetOffsetNano_Type()
)
tnRoeTargetOffsetNano.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeTargetOffsetNano.setStatus("current")


class _TnRoeMapperSampleWidth_Type(Integer32):
    """Custom type tnRoeMapperSampleWidth based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_TnRoeMapperSampleWidth_Type.__name__ = "Integer32"
_TnRoeMapperSampleWidth_Object = MibTableColumn
tnRoeMapperSampleWidth = _TnRoeMapperSampleWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 20),
    _TnRoeMapperSampleWidth_Type()
)
tnRoeMapperSampleWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperSampleWidth.setStatus("current")


class _TnRoeDeMapperSampleWidth_Type(Integer32):
    """Custom type tnRoeDeMapperSampleWidth based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_TnRoeDeMapperSampleWidth_Type.__name__ = "Integer32"
_TnRoeDeMapperSampleWidth_Object = MibTableColumn
tnRoeDeMapperSampleWidth = _TnRoeDeMapperSampleWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 21),
    _TnRoeDeMapperSampleWidth_Type()
)
tnRoeDeMapperSampleWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperSampleWidth.setStatus("current")


class _TnRoePPointer_Type(Integer32):
    """Custom type tnRoePPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 63),
    )


_TnRoePPointer_Type.__name__ = "Integer32"
_TnRoePPointer_Object = MibTableColumn
tnRoePPointer = _TnRoePPointer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 24),
    _TnRoePPointer_Type()
)
tnRoePPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoePPointer.setStatus("current")


class _TnRoeCpriProtocolVer_Type(Integer32):
    """Custom type tnRoeCpriProtocolVer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnRoeCpriProtocolVer_Type.__name__ = "Integer32"
_TnRoeCpriProtocolVer_Object = MibTableColumn
tnRoeCpriProtocolVer = _TnRoeCpriProtocolVer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 25),
    _TnRoeCpriProtocolVer_Type()
)
tnRoeCpriProtocolVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeCpriProtocolVer.setStatus("current")


class _TnRoeMapperStatusEnable_Type(Integer32):
    """Custom type tnRoeMapperStatusEnable based on Integer32"""
    defaultValue = 2

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


_TnRoeMapperStatusEnable_Type.__name__ = "Integer32"
_TnRoeMapperStatusEnable_Object = MibTableColumn
tnRoeMapperStatusEnable = _TnRoeMapperStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 26),
    _TnRoeMapperStatusEnable_Type()
)
tnRoeMapperStatusEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperStatusEnable.setStatus("current")


class _TnRoeSlowcmRate_Type(Integer32):
    """Custom type tnRoeSlowcmRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnRoeSlowcmRate_Type.__name__ = "Integer32"
_TnRoeSlowcmRate_Object = MibTableColumn
tnRoeSlowcmRate = _TnRoeSlowcmRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 2, 1, 27),
    _TnRoeSlowcmRate_Type()
)
tnRoeSlowcmRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeSlowcmRate.setStatus("current")
_TnRoeMapperTable_Object = MibTable
tnRoeMapperTable = _TnRoeMapperTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnRoeMapperTable.setStatus("current")
_TnRoeMapperEntry_Object = MibTableRow
tnRoeMapperEntry = _TnRoeMapperEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1)
)
tnRoeMapperEntry.setIndexNames(
    (0, "TROPIC-ROE-MIB", "tnRoeMapperCardType"),
    (0, "TROPIC-ROE-MIB", "tnRoeMapperPortID"),
    (0, "TROPIC-ROE-MIB", "tnRoeMapperID"),
)
if mibBuilder.loadTexts:
    tnRoeMapperEntry.setStatus("current")
_TnRoeMapperCardType_Type = TropicRoeCardType
_TnRoeMapperCardType_Object = MibTableColumn
tnRoeMapperCardType = _TnRoeMapperCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 1),
    _TnRoeMapperCardType_Type()
)
tnRoeMapperCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperCardType.setStatus("current")
_TnRoeMapperPortID_Type = TmnxPortID
_TnRoeMapperPortID_Object = MibTableColumn
tnRoeMapperPortID = _TnRoeMapperPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 2),
    _TnRoeMapperPortID_Type()
)
tnRoeMapperPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperPortID.setStatus("current")


class _TnRoeMapperID_Type(Integer32):
    """Custom type tnRoeMapperID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeMapperID_Type.__name__ = "Integer32"
_TnRoeMapperID_Object = MibTableColumn
tnRoeMapperID = _TnRoeMapperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 3),
    _TnRoeMapperID_Type()
)
tnRoeMapperID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeMapperID.setStatus("current")
_TnRoeMapperDescription_Type = TItemDescription
_TnRoeMapperDescription_Object = MibTableColumn
tnRoeMapperDescription = _TnRoeMapperDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 4),
    _TnRoeMapperDescription_Type()
)
tnRoeMapperDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperDescription.setStatus("current")


class _TnRoeMapperFlowID_Type(Integer32):
    """Custom type tnRoeMapperFlowID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TnRoeMapperFlowID_Type.__name__ = "Integer32"
_TnRoeMapperFlowID_Object = MibTableColumn
tnRoeMapperFlowID = _TnRoeMapperFlowID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 5),
    _TnRoeMapperFlowID_Type()
)
tnRoeMapperFlowID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperFlowID.setStatus("current")


class _TnRoeMappeEtherlinkID_Type(Integer32):
    """Custom type tnRoeMappeEtherlinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeMappeEtherlinkID_Type.__name__ = "Integer32"
_TnRoeMappeEtherlinkID_Object = MibTableColumn
tnRoeMappeEtherlinkID = _TnRoeMappeEtherlinkID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 6),
    _TnRoeMappeEtherlinkID_Type()
)
tnRoeMappeEtherlinkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMappeEtherlinkID.setStatus("current")


class _TnRoeMapperPayloadLen_Type(Integer32):
    """Custom type tnRoeMapperPayloadLen based on Integer32"""
    defaultValue = 640

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_TnRoeMapperPayloadLen_Type.__name__ = "Integer32"
_TnRoeMapperPayloadLen_Object = MibTableColumn
tnRoeMapperPayloadLen = _TnRoeMapperPayloadLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 7),
    _TnRoeMapperPayloadLen_Type()
)
tnRoeMapperPayloadLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperPayloadLen.setStatus("current")


class _TnRoeMapperSyncMode_Type(Integer32):
    """Custom type tnRoeMapperSyncMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hyper", 0),
          ("radio", 1),
          ("basic", 2))
    )


_TnRoeMapperSyncMode_Type.__name__ = "Integer32"
_TnRoeMapperSyncMode_Object = MibTableColumn
tnRoeMapperSyncMode = _TnRoeMapperSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 8),
    _TnRoeMapperSyncMode_Type()
)
tnRoeMapperSyncMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperSyncMode.setStatus("current")


class _TnRoeMapperBfn_Type(Integer32):
    """Custom type tnRoeMapperBfn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TnRoeMapperBfn_Type.__name__ = "Integer32"
_TnRoeMapperBfn_Object = MibTableColumn
tnRoeMapperBfn = _TnRoeMapperBfn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 9),
    _TnRoeMapperBfn_Type()
)
tnRoeMapperBfn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperBfn.setStatus("current")


class _TnRoeMapperHfn_Type(Integer32):
    """Custom type tnRoeMapperHfn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 149),
    )


_TnRoeMapperHfn_Type.__name__ = "Integer32"
_TnRoeMapperHfn_Object = MibTableColumn
tnRoeMapperHfn = _TnRoeMapperHfn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 10),
    _TnRoeMapperHfn_Type()
)
tnRoeMapperHfn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperHfn.setStatus("current")


class _TnRoeMapperBfrm_Type(Integer32):
    """Custom type tnRoeMapperBfrm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnRoeMapperBfrm_Type.__name__ = "Integer32"
_TnRoeMapperBfrm_Object = MibTableColumn
tnRoeMapperBfrm = _TnRoeMapperBfrm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 11),
    _TnRoeMapperBfrm_Type()
)
tnRoeMapperBfrm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperBfrm.setStatus("current")


class _TnRoeMapperShutdown_Type(Integer32):
    """Custom type tnRoeMapperShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("no-shutdwn", 3))
    )


_TnRoeMapperShutdown_Type.__name__ = "Integer32"
_TnRoeMapperShutdown_Object = MibTableColumn
tnRoeMapperShutdown = _TnRoeMapperShutdown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 12),
    _TnRoeMapperShutdown_Type()
)
tnRoeMapperShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperShutdown.setStatus("current")


class _TnRoeMapperType_Type(Integer32):
    """Custom type tnRoeMapperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("tunneling", 6),
          ("linecodeAware", 7),
          ("structureAware", 8),
          ("structureAwareControl", 9))
    )


_TnRoeMapperType_Type.__name__ = "Integer32"
_TnRoeMapperType_Object = MibTableColumn
tnRoeMapperType = _TnRoeMapperType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 13),
    _TnRoeMapperType_Type()
)
tnRoeMapperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperType.setStatus("current")


class _TnRoeMapperOrderInfoType_Type(Integer32):
    """Custom type tnRoeMapperOrderInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prestime", 0),
          ("seqnum", 1))
    )


_TnRoeMapperOrderInfoType_Type.__name__ = "Integer32"
_TnRoeMapperOrderInfoType_Object = MibTableColumn
tnRoeMapperOrderInfoType = _TnRoeMapperOrderInfoType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 14),
    _TnRoeMapperOrderInfoType_Type()
)
tnRoeMapperOrderInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperOrderInfoType.setStatus("current")


class _TnRoeMapperPmonPolicy_Type(Integer32):
    """Custom type tnRoeMapperPmonPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnRoeMapperPmonPolicy_Type.__name__ = "Integer32"
_TnRoeMapperPmonPolicy_Object = MibTableColumn
tnRoeMapperPmonPolicy = _TnRoeMapperPmonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 15),
    _TnRoeMapperPmonPolicy_Type()
)
tnRoeMapperPmonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperPmonPolicy.setStatus("current")
_TnRoeMapperRowStatus_Type = RowStatus
_TnRoeMapperRowStatus_Object = MibTableColumn
tnRoeMapperRowStatus = _TnRoeMapperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 16),
    _TnRoeMapperRowStatus_Type()
)
tnRoeMapperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperRowStatus.setStatus("current")


class _TnRoeMapperAlmProfName_Type(OctetString):
    """Custom type tnRoeMapperAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnRoeMapperAlmProfName_Type.__name__ = "OctetString"
_TnRoeMapperAlmProfName_Object = MibTableColumn
tnRoeMapperAlmProfName = _TnRoeMapperAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 17),
    _TnRoeMapperAlmProfName_Type()
)
tnRoeMapperAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperAlmProfName.setStatus("current")


class _TnRoeMapperSaType_Type(Integer32):
    """Custom type tnRoeMapperSaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnRoeMapperSaType_Type.__name__ = "Integer32"
_TnRoeMapperSaType_Object = MibTableColumn
tnRoeMapperSaType = _TnRoeMapperSaType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 18),
    _TnRoeMapperSaType_Type()
)
tnRoeMapperSaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperSaType.setStatus("current")


class _TnRoeMapperBwID_Type(Integer32):
    """Custom type tnRoeMapperBwID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TnRoeMapperBwID_Type.__name__ = "Integer32"
_TnRoeMapperBwID_Object = MibTableColumn
tnRoeMapperBwID = _TnRoeMapperBwID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 19),
    _TnRoeMapperBwID_Type()
)
tnRoeMapperBwID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperBwID.setStatus("current")


class _TnRoeMapperPosition_Type(Integer32):
    """Custom type tnRoeMapperPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6143),
    )


_TnRoeMapperPosition_Type.__name__ = "Integer32"
_TnRoeMapperPosition_Object = MibTableColumn
tnRoeMapperPosition = _TnRoeMapperPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 20),
    _TnRoeMapperPosition_Type()
)
tnRoeMapperPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperPosition.setStatus("current")


class _TnRoeMapperFrameStartOffset_Type(Integer32):
    """Custom type tnRoeMapperFrameStartOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6143),
    )


_TnRoeMapperFrameStartOffset_Type.__name__ = "Integer32"
_TnRoeMapperFrameStartOffset_Object = MibTableColumn
tnRoeMapperFrameStartOffset = _TnRoeMapperFrameStartOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 21),
    _TnRoeMapperFrameStartOffset_Type()
)
tnRoeMapperFrameStartOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperFrameStartOffset.setStatus("current")


class _TnRoeMapperSchanStart_Type(Integer32):
    """Custom type tnRoeMapperSchanStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 19),
    )


_TnRoeMapperSchanStart_Type.__name__ = "Integer32"
_TnRoeMapperSchanStart_Object = MibTableColumn
tnRoeMapperSchanStart = _TnRoeMapperSchanStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 22),
    _TnRoeMapperSchanStart_Type()
)
tnRoeMapperSchanStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperSchanStart.setStatus("current")


class _TnRoeMapperSchanSize_Type(Integer32):
    """Custom type tnRoeMapperSchanSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TnRoeMapperSchanSize_Type.__name__ = "Integer32"
_TnRoeMapperSchanSize_Object = MibTableColumn
tnRoeMapperSchanSize = _TnRoeMapperSchanSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 23),
    _TnRoeMapperSchanSize_Type()
)
tnRoeMapperSchanSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeMapperSchanSize.setStatus("current")
_TnRoeMapperPincrement_Type = Integer32
_TnRoeMapperPincrement_Object = MibTableColumn
tnRoeMapperPincrement = _TnRoeMapperPincrement_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 24),
    _TnRoeMapperPincrement_Type()
)
tnRoeMapperPincrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperPincrement.setStatus("current")
_TnRoeMapperNa_Type = Integer32
_TnRoeMapperNa_Object = MibTableColumn
tnRoeMapperNa = _TnRoeMapperNa_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 25),
    _TnRoeMapperNa_Type()
)
tnRoeMapperNa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperNa.setStatus("current")
_TnRoeMapperS_Type = Integer32
_TnRoeMapperS_Object = MibTableColumn
tnRoeMapperS = _TnRoeMapperS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 26),
    _TnRoeMapperS_Type()
)
tnRoeMapperS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperS.setStatus("current")
_TnRoeMapperK_Type = Integer32
_TnRoeMapperK_Object = MibTableColumn
tnRoeMapperK = _TnRoeMapperK_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 27),
    _TnRoeMapperK_Type()
)
tnRoeMapperK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperK.setStatus("current")
_TnRoeMapperNc_Type = Integer32
_TnRoeMapperNc_Object = MibTableColumn
tnRoeMapperNc = _TnRoeMapperNc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 28),
    _TnRoeMapperNc_Type()
)
tnRoeMapperNc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperNc.setStatus("current")
_TnRoeMapperNv_Type = Integer32
_TnRoeMapperNv_Object = MibTableColumn
tnRoeMapperNv = _TnRoeMapperNv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 3, 1, 29),
    _TnRoeMapperNv_Type()
)
tnRoeMapperNv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeMapperNv.setStatus("current")
_TnRoeDeMapperTable_Object = MibTable
tnRoeDeMapperTable = _TnRoeDeMapperTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnRoeDeMapperTable.setStatus("current")
_TnRoeDeMapperEntry_Object = MibTableRow
tnRoeDeMapperEntry = _TnRoeDeMapperEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1)
)
tnRoeDeMapperEntry.setIndexNames(
    (0, "TROPIC-ROE-MIB", "tnRoeDeMapperCardType"),
    (0, "TROPIC-ROE-MIB", "tnRoePortID"),
    (0, "TROPIC-ROE-MIB", "tnRoeDeMapperID"),
)
if mibBuilder.loadTexts:
    tnRoeDeMapperEntry.setStatus("current")
_TnRoeDeMapperCardType_Type = TropicRoeCardType
_TnRoeDeMapperCardType_Object = MibTableColumn
tnRoeDeMapperCardType = _TnRoeDeMapperCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 1),
    _TnRoeDeMapperCardType_Type()
)
tnRoeDeMapperCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperCardType.setStatus("current")
_TnRoeDeMapperPortID_Type = TmnxPortID
_TnRoeDeMapperPortID_Object = MibTableColumn
tnRoeDeMapperPortID = _TnRoeDeMapperPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 2),
    _TnRoeDeMapperPortID_Type()
)
tnRoeDeMapperPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperPortID.setStatus("current")


class _TnRoeDeMapperID_Type(Integer32):
    """Custom type tnRoeDeMapperID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeDeMapperID_Type.__name__ = "Integer32"
_TnRoeDeMapperID_Object = MibTableColumn
tnRoeDeMapperID = _TnRoeDeMapperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 3),
    _TnRoeDeMapperID_Type()
)
tnRoeDeMapperID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeDeMapperID.setStatus("current")
_TnRoeDeMapperDescription_Type = TItemDescription
_TnRoeDeMapperDescription_Object = MibTableColumn
tnRoeDeMapperDescription = _TnRoeDeMapperDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 4),
    _TnRoeDeMapperDescription_Type()
)
tnRoeDeMapperDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperDescription.setStatus("current")


class _TnRoeDeMappeEtherlinkID_Type(Integer32):
    """Custom type tnRoeDeMappeEtherlinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeDeMappeEtherlinkID_Type.__name__ = "Integer32"
_TnRoeDeMappeEtherlinkID_Object = MibTableColumn
tnRoeDeMappeEtherlinkID = _TnRoeDeMappeEtherlinkID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 5),
    _TnRoeDeMappeEtherlinkID_Type()
)
tnRoeDeMappeEtherlinkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMappeEtherlinkID.setStatus("current")


class _TnRoeDeMapperPayloadLen_Type(Integer32):
    """Custom type tnRoeDeMapperPayloadLen based on Integer32"""
    defaultValue = 640

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_TnRoeDeMapperPayloadLen_Type.__name__ = "Integer32"
_TnRoeDeMapperPayloadLen_Object = MibTableColumn
tnRoeDeMapperPayloadLen = _TnRoeDeMapperPayloadLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 6),
    _TnRoeDeMapperPayloadLen_Type()
)
tnRoeDeMapperPayloadLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperPayloadLen.setStatus("current")


class _TnRoeDeMapperSyncMode_Type(Integer32):
    """Custom type tnRoeDeMapperSyncMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hyper", 0),
          ("radio", 1),
          ("basic", 2))
    )


_TnRoeDeMapperSyncMode_Type.__name__ = "Integer32"
_TnRoeDeMapperSyncMode_Object = MibTableColumn
tnRoeDeMapperSyncMode = _TnRoeDeMapperSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 7),
    _TnRoeDeMapperSyncMode_Type()
)
tnRoeDeMapperSyncMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperSyncMode.setStatus("current")


class _TnRoeDeMapperBfn_Type(Integer32):
    """Custom type tnRoeDeMapperBfn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TnRoeDeMapperBfn_Type.__name__ = "Integer32"
_TnRoeDeMapperBfn_Object = MibTableColumn
tnRoeDeMapperBfn = _TnRoeDeMapperBfn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 8),
    _TnRoeDeMapperBfn_Type()
)
tnRoeDeMapperBfn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperBfn.setStatus("current")


class _TnRoeDeMapperHfn_Type(Integer32):
    """Custom type tnRoeDeMapperHfn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 149),
    )


_TnRoeDeMapperHfn_Type.__name__ = "Integer32"
_TnRoeDeMapperHfn_Object = MibTableColumn
tnRoeDeMapperHfn = _TnRoeDeMapperHfn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 9),
    _TnRoeDeMapperHfn_Type()
)
tnRoeDeMapperHfn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperHfn.setStatus("current")


class _TnRoeDeMapperBfrm_Type(Integer32):
    """Custom type tnRoeDeMapperBfrm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnRoeDeMapperBfrm_Type.__name__ = "Integer32"
_TnRoeDeMapperBfrm_Object = MibTableColumn
tnRoeDeMapperBfrm = _TnRoeDeMapperBfrm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 10),
    _TnRoeDeMapperBfrm_Type()
)
tnRoeDeMapperBfrm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperBfrm.setStatus("current")


class _TnRoeDeMapperJitterBufferDepth_Type(Integer32):
    """Custom type tnRoeDeMapperJitterBufferDepth based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 128),
    )


_TnRoeDeMapperJitterBufferDepth_Type.__name__ = "Integer32"
_TnRoeDeMapperJitterBufferDepth_Object = MibTableColumn
tnRoeDeMapperJitterBufferDepth = _TnRoeDeMapperJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 11),
    _TnRoeDeMapperJitterBufferDepth_Type()
)
tnRoeDeMapperJitterBufferDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperJitterBufferDepth.setStatus("current")


class _TnRoeDeMapperShutdown_Type(Integer32):
    """Custom type tnRoeDeMapperShutdown based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("no-shutdwn", 3))
    )


_TnRoeDeMapperShutdown_Type.__name__ = "Integer32"
_TnRoeDeMapperShutdown_Object = MibTableColumn
tnRoeDeMapperShutdown = _TnRoeDeMapperShutdown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 12),
    _TnRoeDeMapperShutdown_Type()
)
tnRoeDeMapperShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperShutdown.setStatus("current")


class _TnRoeDeMapperType_Type(Integer32):
    """Custom type tnRoeDeMapperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("tunneling", 6),
          ("linecodeAware", 7),
          ("structureAware", 8),
          ("structureAwareControl", 9))
    )


_TnRoeDeMapperType_Type.__name__ = "Integer32"
_TnRoeDeMapperType_Object = MibTableColumn
tnRoeDeMapperType = _TnRoeDeMapperType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 13),
    _TnRoeDeMapperType_Type()
)
tnRoeDeMapperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperType.setStatus("current")


class _TnRoeDeMapperFlowID_Type(Integer32):
    """Custom type tnRoeDeMapperFlowID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TnRoeDeMapperFlowID_Type.__name__ = "Integer32"
_TnRoeDeMapperFlowID_Object = MibTableColumn
tnRoeDeMapperFlowID = _TnRoeDeMapperFlowID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 14),
    _TnRoeDeMapperFlowID_Type()
)
tnRoeDeMapperFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperFlowID.setStatus("current")


class _TnRoeDeMapperOrderInfoType_Type(Integer32):
    """Custom type tnRoeDeMapperOrderInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prestime", 0),
          ("seqnum", 1))
    )


_TnRoeDeMapperOrderInfoType_Type.__name__ = "Integer32"
_TnRoeDeMapperOrderInfoType_Object = MibTableColumn
tnRoeDeMapperOrderInfoType = _TnRoeDeMapperOrderInfoType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 15),
    _TnRoeDeMapperOrderInfoType_Type()
)
tnRoeDeMapperOrderInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperOrderInfoType.setStatus("current")


class _TnRoeDeMapperPmonPolicy_Type(Integer32):
    """Custom type tnRoeDeMapperPmonPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnRoeDeMapperPmonPolicy_Type.__name__ = "Integer32"
_TnRoeDeMapperPmonPolicy_Object = MibTableColumn
tnRoeDeMapperPmonPolicy = _TnRoeDeMapperPmonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 16),
    _TnRoeDeMapperPmonPolicy_Type()
)
tnRoeDeMapperPmonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperPmonPolicy.setStatus("current")
_TnRoeDeMapperRowStatus_Type = RowStatus
_TnRoeDeMapperRowStatus_Object = MibTableColumn
tnRoeDeMapperRowStatus = _TnRoeDeMapperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 17),
    _TnRoeDeMapperRowStatus_Type()
)
tnRoeDeMapperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperRowStatus.setStatus("current")


class _TnRoeDeMapperAlmProfName_Type(OctetString):
    """Custom type tnRoeDeMapperAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnRoeDeMapperAlmProfName_Type.__name__ = "OctetString"
_TnRoeDeMapperAlmProfName_Object = MibTableColumn
tnRoeDeMapperAlmProfName = _TnRoeDeMapperAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 18),
    _TnRoeDeMapperAlmProfName_Type()
)
tnRoeDeMapperAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperAlmProfName.setStatus("current")


class _TnRoeDeMapperSaType_Type(Integer32):
    """Custom type tnRoeDeMapperSaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnRoeDeMapperSaType_Type.__name__ = "Integer32"
_TnRoeDeMapperSaType_Object = MibTableColumn
tnRoeDeMapperSaType = _TnRoeDeMapperSaType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 19),
    _TnRoeDeMapperSaType_Type()
)
tnRoeDeMapperSaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperSaType.setStatus("current")


class _TnRoeDeMapperBwID_Type(Integer32):
    """Custom type tnRoeDeMapperBwID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TnRoeDeMapperBwID_Type.__name__ = "Integer32"
_TnRoeDeMapperBwID_Object = MibTableColumn
tnRoeDeMapperBwID = _TnRoeDeMapperBwID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 20),
    _TnRoeDeMapperBwID_Type()
)
tnRoeDeMapperBwID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperBwID.setStatus("current")


class _TnRoeDeMapperPosition_Type(Integer32):
    """Custom type tnRoeDeMapperPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6143),
    )


_TnRoeDeMapperPosition_Type.__name__ = "Integer32"
_TnRoeDeMapperPosition_Object = MibTableColumn
tnRoeDeMapperPosition = _TnRoeDeMapperPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 21),
    _TnRoeDeMapperPosition_Type()
)
tnRoeDeMapperPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperPosition.setStatus("current")


class _TnRoeDeMapperFrameStartOffset_Type(Integer32):
    """Custom type tnRoeDeMapperFrameStartOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6143),
    )


_TnRoeDeMapperFrameStartOffset_Type.__name__ = "Integer32"
_TnRoeDeMapperFrameStartOffset_Object = MibTableColumn
tnRoeDeMapperFrameStartOffset = _TnRoeDeMapperFrameStartOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 22),
    _TnRoeDeMapperFrameStartOffset_Type()
)
tnRoeDeMapperFrameStartOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperFrameStartOffset.setStatus("current")


class _TnRoeDeMapperSchanStart_Type(Integer32):
    """Custom type tnRoeDeMapperSchanStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 19),
    )


_TnRoeDeMapperSchanStart_Type.__name__ = "Integer32"
_TnRoeDeMapperSchanStart_Object = MibTableColumn
tnRoeDeMapperSchanStart = _TnRoeDeMapperSchanStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 23),
    _TnRoeDeMapperSchanStart_Type()
)
tnRoeDeMapperSchanStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperSchanStart.setStatus("current")


class _TnRoeDeMapperSchanSize_Type(Integer32):
    """Custom type tnRoeDeMapperSchanSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TnRoeDeMapperSchanSize_Type.__name__ = "Integer32"
_TnRoeDeMapperSchanSize_Object = MibTableColumn
tnRoeDeMapperSchanSize = _TnRoeDeMapperSchanSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 24),
    _TnRoeDeMapperSchanSize_Type()
)
tnRoeDeMapperSchanSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeDeMapperSchanSize.setStatus("current")
_TnRoeDeMapperPincrement_Type = Integer32
_TnRoeDeMapperPincrement_Object = MibTableColumn
tnRoeDeMapperPincrement = _TnRoeDeMapperPincrement_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 25),
    _TnRoeDeMapperPincrement_Type()
)
tnRoeDeMapperPincrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperPincrement.setStatus("current")
_TnRoeDeMapperNa_Type = Integer32
_TnRoeDeMapperNa_Object = MibTableColumn
tnRoeDeMapperNa = _TnRoeDeMapperNa_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 26),
    _TnRoeDeMapperNa_Type()
)
tnRoeDeMapperNa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperNa.setStatus("current")
_TnRoeDeMapperS_Type = Integer32
_TnRoeDeMapperS_Object = MibTableColumn
tnRoeDeMapperS = _TnRoeDeMapperS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 27),
    _TnRoeDeMapperS_Type()
)
tnRoeDeMapperS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperS.setStatus("current")
_TnRoeDeMapperK_Type = Integer32
_TnRoeDeMapperK_Object = MibTableColumn
tnRoeDeMapperK = _TnRoeDeMapperK_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 28),
    _TnRoeDeMapperK_Type()
)
tnRoeDeMapperK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperK.setStatus("current")
_TnRoeDeMapperNc_Type = Integer32
_TnRoeDeMapperNc_Object = MibTableColumn
tnRoeDeMapperNc = _TnRoeDeMapperNc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 29),
    _TnRoeDeMapperNc_Type()
)
tnRoeDeMapperNc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperNc.setStatus("current")
_TnRoeDeMapperNv_Type = Integer32
_TnRoeDeMapperNv_Object = MibTableColumn
tnRoeDeMapperNv = _TnRoeDeMapperNv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 4, 1, 30),
    _TnRoeDeMapperNv_Type()
)
tnRoeDeMapperNv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRoeDeMapperNv.setStatus("current")
_TnRoeEthlinkTable_Object = MibTable
tnRoeEthlinkTable = _TnRoeEthlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnRoeEthlinkTable.setStatus("current")
_TnRoeEthlinkEntry_Object = MibTableRow
tnRoeEthlinkEntry = _TnRoeEthlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1)
)
tnRoeEthlinkEntry.setIndexNames(
    (0, "TROPIC-ROE-MIB", "tnRoeEthlinkCardType"),
    (0, "TROPIC-ROE-MIB", "tnRoeEthlinkPortID"),
    (0, "TROPIC-ROE-MIB", "tnRoeEthlinkID"),
)
if mibBuilder.loadTexts:
    tnRoeEthlinkEntry.setStatus("current")
_TnRoeEthlinkCardType_Type = TropicRoeCardType
_TnRoeEthlinkCardType_Object = MibTableColumn
tnRoeEthlinkCardType = _TnRoeEthlinkCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 1),
    _TnRoeEthlinkCardType_Type()
)
tnRoeEthlinkCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeEthlinkCardType.setStatus("current")
_TnRoeEthlinkPortID_Type = TmnxPortID
_TnRoeEthlinkPortID_Object = MibTableColumn
tnRoeEthlinkPortID = _TnRoeEthlinkPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 2),
    _TnRoeEthlinkPortID_Type()
)
tnRoeEthlinkPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeEthlinkPortID.setStatus("current")


class _TnRoeEthlinkID_Type(Integer32):
    """Custom type tnRoeEthlinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_TnRoeEthlinkID_Type.__name__ = "Integer32"
_TnRoeEthlinkID_Object = MibTableColumn
tnRoeEthlinkID = _TnRoeEthlinkID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 3),
    _TnRoeEthlinkID_Type()
)
tnRoeEthlinkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRoeEthlinkID.setStatus("current")
_TnRoeEthlinkDescription_Type = TItemDescription
_TnRoeEthlinkDescription_Object = MibTableColumn
tnRoeEthlinkDescription = _TnRoeEthlinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 4),
    _TnRoeEthlinkDescription_Type()
)
tnRoeEthlinkDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkDescription.setStatus("current")
_TnRoeEthlinkDestMac_Type = MacAddress
_TnRoeEthlinkDestMac_Object = MibTableColumn
tnRoeEthlinkDestMac = _TnRoeEthlinkDestMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 5),
    _TnRoeEthlinkDestMac_Type()
)
tnRoeEthlinkDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkDestMac.setStatus("current")
_TnRoeEthlinkSourceMac_Type = MacAddress
_TnRoeEthlinkSourceMac_Object = MibTableColumn
tnRoeEthlinkSourceMac = _TnRoeEthlinkSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 6),
    _TnRoeEthlinkSourceMac_Type()
)
tnRoeEthlinkSourceMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkSourceMac.setStatus("current")


class _TnRoeEthlinkTagDepth_Type(Integer32):
    """Custom type tnRoeEthlinkTagDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 0),
          ("single", 1),
          ("double", 2))
    )


_TnRoeEthlinkTagDepth_Type.__name__ = "Integer32"
_TnRoeEthlinkTagDepth_Object = MibTableColumn
tnRoeEthlinkTagDepth = _TnRoeEthlinkTagDepth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 7),
    _TnRoeEthlinkTagDepth_Type()
)
tnRoeEthlinkTagDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkTagDepth.setStatus("current")


class _TnRoeEthlinkOuterEthertype_Type(Integer32):
    """Custom type tnRoeEthlinkOuterEthertype based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnRoeEthlinkOuterEthertype_Type.__name__ = "Integer32"
_TnRoeEthlinkOuterEthertype_Object = MibTableColumn
tnRoeEthlinkOuterEthertype = _TnRoeEthlinkOuterEthertype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 8),
    _TnRoeEthlinkOuterEthertype_Type()
)
tnRoeEthlinkOuterEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkOuterEthertype.setStatus("current")


class _TnRoeEthlinkOuterVid_Type(Integer32):
    """Custom type tnRoeEthlinkOuterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TnRoeEthlinkOuterVid_Type.__name__ = "Integer32"
_TnRoeEthlinkOuterVid_Object = MibTableColumn
tnRoeEthlinkOuterVid = _TnRoeEthlinkOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 9),
    _TnRoeEthlinkOuterVid_Type()
)
tnRoeEthlinkOuterVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkOuterVid.setStatus("current")


class _TnRoeEthlinkOuterPri_Type(Integer32):
    """Custom type tnRoeEthlinkOuterPri based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnRoeEthlinkOuterPri_Type.__name__ = "Integer32"
_TnRoeEthlinkOuterPri_Object = MibTableColumn
tnRoeEthlinkOuterPri = _TnRoeEthlinkOuterPri_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 10),
    _TnRoeEthlinkOuterPri_Type()
)
tnRoeEthlinkOuterPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkOuterPri.setStatus("current")


class _TnRoeEthlinkInnerEthertype_Type(Integer32):
    """Custom type tnRoeEthlinkInnerEthertype based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnRoeEthlinkInnerEthertype_Type.__name__ = "Integer32"
_TnRoeEthlinkInnerEthertype_Object = MibTableColumn
tnRoeEthlinkInnerEthertype = _TnRoeEthlinkInnerEthertype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 11),
    _TnRoeEthlinkInnerEthertype_Type()
)
tnRoeEthlinkInnerEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkInnerEthertype.setStatus("current")


class _TnRoeEthlinkInnerVid_Type(Integer32):
    """Custom type tnRoeEthlinkInnerVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TnRoeEthlinkInnerVid_Type.__name__ = "Integer32"
_TnRoeEthlinkInnerVid_Object = MibTableColumn
tnRoeEthlinkInnerVid = _TnRoeEthlinkInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 12),
    _TnRoeEthlinkInnerVid_Type()
)
tnRoeEthlinkInnerVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkInnerVid.setStatus("current")


class _TnRoeEthlinkInnerPri_Type(Integer32):
    """Custom type tnRoeEthlinkInnerPri based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnRoeEthlinkInnerPri_Type.__name__ = "Integer32"
_TnRoeEthlinkInnerPri_Object = MibTableColumn
tnRoeEthlinkInnerPri = _TnRoeEthlinkInnerPri_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 13),
    _TnRoeEthlinkInnerPri_Type()
)
tnRoeEthlinkInnerPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkInnerPri.setStatus("current")


class _TnRoeEthlinkEthertype_Type(Integer32):
    """Custom type tnRoeEthlinkEthertype based on Integer32"""
    defaultValue = 64573

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnRoeEthlinkEthertype_Type.__name__ = "Integer32"
_TnRoeEthlinkEthertype_Object = MibTableColumn
tnRoeEthlinkEthertype = _TnRoeEthlinkEthertype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 14),
    _TnRoeEthlinkEthertype_Type()
)
tnRoeEthlinkEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkEthertype.setStatus("current")
_TnRoeEthlinkRowStatus_Type = RowStatus
_TnRoeEthlinkRowStatus_Object = MibTableColumn
tnRoeEthlinkRowStatus = _TnRoeEthlinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 1, 1, 5, 1, 15),
    _TnRoeEthlinkRowStatus_Type()
)
tnRoeEthlinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRoeEthlinkRowStatus.setStatus("current")
_TnRoeEConf_ObjectIdentity = ObjectIdentity
tnRoeEConf = _TnRoeEConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2)
)
_TnRoeGroups_ObjectIdentity = ObjectIdentity
tnRoeGroups = _TnRoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 1)
)
_TnEoeCompliances_ObjectIdentity = ObjectIdentity
tnEoeCompliances = _TnEoeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 2)
)

# Managed Objects groups

tnRoeSeqProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 1, 1)
)
tnRoeSeqProfGroup.setObjects(
      *(("TROPIC-ROE-MIB", "tnRoeSeqProfDescription"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfType"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfPMax"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfPIncProp"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfPInc"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfQMax"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfQIncProp"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfQInc"),
        ("TROPIC-ROE-MIB", "tnRoeSeqProfRowStatus"))
)
if mibBuilder.loadTexts:
    tnRoeSeqProfGroup.setStatus("current")

tnRoeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 1, 2)
)
tnRoeGroup.setObjects(
      *(("TROPIC-ROE-MIB", "tnRoeDescription"),
        ("TROPIC-ROE-MIB", "tnRoeOrderInfoType"),
        ("TROPIC-ROE-MIB", "tnRoePresTimeOffset"),
        ("TROPIC-ROE-MIB", "tnRoeCpriTxGenOffset"),
        ("TROPIC-ROE-MIB", "tnRoeAutoUponChange"),
        ("TROPIC-ROE-MIB", "tnRoeSeqNumProfID"),
        ("TROPIC-ROE-MIB", "tnRoeInitialTxBFN"),
        ("TROPIC-ROE-MIB", "tnRoeInitialTxHFN"),
        ("TROPIC-ROE-MIB", "tnRoeEncapMode"),
        ("TROPIC-ROE-MIB", "tnRoeAdminState"),
        ("TROPIC-ROE-MIB", "tnRoePmonPolicy"),
        ("TROPIC-ROE-MIB", "tnRoeRowStatus"),
        ("TROPIC-ROE-MIB", "tnRoeAlmProfName"),
        ("TROPIC-ROE-MIB", "tnRoePresTimeOffsetSubNano"),
        ("TROPIC-ROE-MIB", "tnRoePresTimeOffsetNano"),
        ("TROPIC-ROE-MIB", "tnRoeTargetOffsetSubNano"),
        ("TROPIC-ROE-MIB", "tnRoeTargetOffsetNano"),
        ("TROPIC-ROE-MIB", "tnRoeMapperSampleWidth"),
        ("TROPIC-ROE-MIB", "tnRoePPointer"),
        ("TROPIC-ROE-MIB", "tnRoeCpriProtocolVer"),
        ("TROPIC-ROE-MIB", "tnRoeMapperStatusEnable"),
        ("TROPIC-ROE-MIB", "tnRoeSlowcmRate"))
)
if mibBuilder.loadTexts:
    tnRoeGroup.setStatus("current")

tnRoeMapperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 1, 3)
)
tnRoeMapperGroup.setObjects(
      *(("TROPIC-ROE-MIB", "tnRoeMapperDescription"),
        ("TROPIC-ROE-MIB", "tnRoeMapperFlowID"),
        ("TROPIC-ROE-MIB", "tnRoeMappeEtherlinkID"),
        ("TROPIC-ROE-MIB", "tnRoeMapperPayloadLen"),
        ("TROPIC-ROE-MIB", "tnRoeMapperSyncMode"),
        ("TROPIC-ROE-MIB", "tnRoeMapperBfn"),
        ("TROPIC-ROE-MIB", "tnRoeMapperHfn"),
        ("TROPIC-ROE-MIB", "tnRoeMapperBfrm"),
        ("TROPIC-ROE-MIB", "tnRoeMapperShutdown"),
        ("TROPIC-ROE-MIB", "tnRoeMapperType"),
        ("TROPIC-ROE-MIB", "tnRoeMapperOrderInfoType"),
        ("TROPIC-ROE-MIB", "tnRoeMapperPmonPolicy"),
        ("TROPIC-ROE-MIB", "tnRoeMapperRowStatus"),
        ("TROPIC-ROE-MIB", "tnRoeMapperAlmProfName"),
        ("TROPIC-ROE-MIB", "tnRoeMapperSaType"),
        ("TROPIC-ROE-MIB", "tnRoeMapperBwID"),
        ("TROPIC-ROE-MIB", "tnRoeMapperPosition"),
        ("TROPIC-ROE-MIB", "tnRoeMapperFrameStartOffset"),
        ("TROPIC-ROE-MIB", "tnRoeMapperSchanStart"),
        ("TROPIC-ROE-MIB", "tnRoeMapperSchanSize"),
        ("TROPIC-ROE-MIB", "tnRoeMapperPincrement"),
        ("TROPIC-ROE-MIB", "tnRoeMapperNa"),
        ("TROPIC-ROE-MIB", "tnRoeMapperS"),
        ("TROPIC-ROE-MIB", "tnRoeMapperK"),
        ("TROPIC-ROE-MIB", "tnRoeMapperNc"),
        ("TROPIC-ROE-MIB", "tnRoeMapperNv"))
)
if mibBuilder.loadTexts:
    tnRoeMapperGroup.setStatus("current")

tnRoeDeMapperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 1, 4)
)
tnRoeDeMapperGroup.setObjects(
      *(("TROPIC-ROE-MIB", "tnRoeDeMapperDescription"),
        ("TROPIC-ROE-MIB", "tnRoeDeMappeEtherlinkID"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperPayloadLen"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperSyncMode"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperBfn"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperHfn"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperBfrm"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperJitterBufferDepth"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperShutdown"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperType"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperFlowID"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperOrderInfoType"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperPmonPolicy"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperRowStatus"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperAlmProfName"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperSaType"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperBwID"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperPosition"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperFrameStartOffset"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperSchanStart"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperSchanSize"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperPincrement"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperNa"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperS"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperK"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperNc"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperNv"))
)
if mibBuilder.loadTexts:
    tnRoeDeMapperGroup.setStatus("current")

tnRoeEthlinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 1, 5)
)
tnRoeEthlinkGroup.setObjects(
      *(("TROPIC-ROE-MIB", "tnRoeEthlinkDescription"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkDestMac"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkSourceMac"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkTagDepth"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkOuterEthertype"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkOuterVid"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkOuterPri"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkInnerEthertype"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkInnerVid"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkInnerPri"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkEthertype"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkRowStatus"))
)
if mibBuilder.loadTexts:
    tnRoeEthlinkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnRoeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12, 2, 2, 1)
)
tnRoeCompliance.setObjects(
      *(("TROPIC-ROE-MIB", "tnRoeSeqProfGroup"),
        ("TROPIC-ROE-MIB", "tnRoeGroup"),
        ("TROPIC-ROE-MIB", "tnRoeMapperGroup"),
        ("TROPIC-ROE-MIB", "tnRoeDeMapperGroup"),
        ("TROPIC-ROE-MIB", "tnRoeEthlinkGroup"))
)
if mibBuilder.loadTexts:
    tnRoeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-ROE-MIB",
    **{"TropicRoeCardType": TropicRoeCardType,
       "tnRoeMibModule": tnRoeMibModule,
       "tnRoeNotifications": tnRoeNotifications,
       "tnRoeObjects": tnRoeObjects,
       "tnRoeParameters": tnRoeParameters,
       "tnRoeSeqProfTable": tnRoeSeqProfTable,
       "tnRoeSeqProfEntry": tnRoeSeqProfEntry,
       "tnRoeSeqProfCardType": tnRoeSeqProfCardType,
       "tnRoeSeqProfPortID": tnRoeSeqProfPortID,
       "tnRoeSeqProfID": tnRoeSeqProfID,
       "tnRoeSeqProfDescription": tnRoeSeqProfDescription,
       "tnRoeSeqProfType": tnRoeSeqProfType,
       "tnRoeSeqProfPMax": tnRoeSeqProfPMax,
       "tnRoeSeqProfPIncProp": tnRoeSeqProfPIncProp,
       "tnRoeSeqProfPInc": tnRoeSeqProfPInc,
       "tnRoeSeqProfQMax": tnRoeSeqProfQMax,
       "tnRoeSeqProfQIncProp": tnRoeSeqProfQIncProp,
       "tnRoeSeqProfQInc": tnRoeSeqProfQInc,
       "tnRoeSeqProfRowStatus": tnRoeSeqProfRowStatus,
       "tnRoeTable": tnRoeTable,
       "tnRoeEntry": tnRoeEntry,
       "tnRoeCardType": tnRoeCardType,
       "tnRoePortID": tnRoePortID,
       "tnRoeDescription": tnRoeDescription,
       "tnRoeOrderInfoType": tnRoeOrderInfoType,
       "tnRoePresTimeOffset": tnRoePresTimeOffset,
       "tnRoeCpriTxGenOffset": tnRoeCpriTxGenOffset,
       "tnRoeAutoUponChange": tnRoeAutoUponChange,
       "tnRoeSeqNumProfID": tnRoeSeqNumProfID,
       "tnRoeInitialTxBFN": tnRoeInitialTxBFN,
       "tnRoeInitialTxHFN": tnRoeInitialTxHFN,
       "tnRoeEncapMode": tnRoeEncapMode,
       "tnRoeAdminState": tnRoeAdminState,
       "tnRoePmonPolicy": tnRoePmonPolicy,
       "tnRoeRowStatus": tnRoeRowStatus,
       "tnRoeAlmProfName": tnRoeAlmProfName,
       "tnRoePresTimeOffsetSubNano": tnRoePresTimeOffsetSubNano,
       "tnRoePresTimeOffsetNano": tnRoePresTimeOffsetNano,
       "tnRoeTargetOffsetSubNano": tnRoeTargetOffsetSubNano,
       "tnRoeTargetOffsetNano": tnRoeTargetOffsetNano,
       "tnRoeMapperSampleWidth": tnRoeMapperSampleWidth,
       "tnRoeDeMapperSampleWidth": tnRoeDeMapperSampleWidth,
       "tnRoePPointer": tnRoePPointer,
       "tnRoeCpriProtocolVer": tnRoeCpriProtocolVer,
       "tnRoeMapperStatusEnable": tnRoeMapperStatusEnable,
       "tnRoeSlowcmRate": tnRoeSlowcmRate,
       "tnRoeMapperTable": tnRoeMapperTable,
       "tnRoeMapperEntry": tnRoeMapperEntry,
       "tnRoeMapperCardType": tnRoeMapperCardType,
       "tnRoeMapperPortID": tnRoeMapperPortID,
       "tnRoeMapperID": tnRoeMapperID,
       "tnRoeMapperDescription": tnRoeMapperDescription,
       "tnRoeMapperFlowID": tnRoeMapperFlowID,
       "tnRoeMappeEtherlinkID": tnRoeMappeEtherlinkID,
       "tnRoeMapperPayloadLen": tnRoeMapperPayloadLen,
       "tnRoeMapperSyncMode": tnRoeMapperSyncMode,
       "tnRoeMapperBfn": tnRoeMapperBfn,
       "tnRoeMapperHfn": tnRoeMapperHfn,
       "tnRoeMapperBfrm": tnRoeMapperBfrm,
       "tnRoeMapperShutdown": tnRoeMapperShutdown,
       "tnRoeMapperType": tnRoeMapperType,
       "tnRoeMapperOrderInfoType": tnRoeMapperOrderInfoType,
       "tnRoeMapperPmonPolicy": tnRoeMapperPmonPolicy,
       "tnRoeMapperRowStatus": tnRoeMapperRowStatus,
       "tnRoeMapperAlmProfName": tnRoeMapperAlmProfName,
       "tnRoeMapperSaType": tnRoeMapperSaType,
       "tnRoeMapperBwID": tnRoeMapperBwID,
       "tnRoeMapperPosition": tnRoeMapperPosition,
       "tnRoeMapperFrameStartOffset": tnRoeMapperFrameStartOffset,
       "tnRoeMapperSchanStart": tnRoeMapperSchanStart,
       "tnRoeMapperSchanSize": tnRoeMapperSchanSize,
       "tnRoeMapperPincrement": tnRoeMapperPincrement,
       "tnRoeMapperNa": tnRoeMapperNa,
       "tnRoeMapperS": tnRoeMapperS,
       "tnRoeMapperK": tnRoeMapperK,
       "tnRoeMapperNc": tnRoeMapperNc,
       "tnRoeMapperNv": tnRoeMapperNv,
       "tnRoeDeMapperTable": tnRoeDeMapperTable,
       "tnRoeDeMapperEntry": tnRoeDeMapperEntry,
       "tnRoeDeMapperCardType": tnRoeDeMapperCardType,
       "tnRoeDeMapperPortID": tnRoeDeMapperPortID,
       "tnRoeDeMapperID": tnRoeDeMapperID,
       "tnRoeDeMapperDescription": tnRoeDeMapperDescription,
       "tnRoeDeMappeEtherlinkID": tnRoeDeMappeEtherlinkID,
       "tnRoeDeMapperPayloadLen": tnRoeDeMapperPayloadLen,
       "tnRoeDeMapperSyncMode": tnRoeDeMapperSyncMode,
       "tnRoeDeMapperBfn": tnRoeDeMapperBfn,
       "tnRoeDeMapperHfn": tnRoeDeMapperHfn,
       "tnRoeDeMapperBfrm": tnRoeDeMapperBfrm,
       "tnRoeDeMapperJitterBufferDepth": tnRoeDeMapperJitterBufferDepth,
       "tnRoeDeMapperShutdown": tnRoeDeMapperShutdown,
       "tnRoeDeMapperType": tnRoeDeMapperType,
       "tnRoeDeMapperFlowID": tnRoeDeMapperFlowID,
       "tnRoeDeMapperOrderInfoType": tnRoeDeMapperOrderInfoType,
       "tnRoeDeMapperPmonPolicy": tnRoeDeMapperPmonPolicy,
       "tnRoeDeMapperRowStatus": tnRoeDeMapperRowStatus,
       "tnRoeDeMapperAlmProfName": tnRoeDeMapperAlmProfName,
       "tnRoeDeMapperSaType": tnRoeDeMapperSaType,
       "tnRoeDeMapperBwID": tnRoeDeMapperBwID,
       "tnRoeDeMapperPosition": tnRoeDeMapperPosition,
       "tnRoeDeMapperFrameStartOffset": tnRoeDeMapperFrameStartOffset,
       "tnRoeDeMapperSchanStart": tnRoeDeMapperSchanStart,
       "tnRoeDeMapperSchanSize": tnRoeDeMapperSchanSize,
       "tnRoeDeMapperPincrement": tnRoeDeMapperPincrement,
       "tnRoeDeMapperNa": tnRoeDeMapperNa,
       "tnRoeDeMapperS": tnRoeDeMapperS,
       "tnRoeDeMapperK": tnRoeDeMapperK,
       "tnRoeDeMapperNc": tnRoeDeMapperNc,
       "tnRoeDeMapperNv": tnRoeDeMapperNv,
       "tnRoeEthlinkTable": tnRoeEthlinkTable,
       "tnRoeEthlinkEntry": tnRoeEthlinkEntry,
       "tnRoeEthlinkCardType": tnRoeEthlinkCardType,
       "tnRoeEthlinkPortID": tnRoeEthlinkPortID,
       "tnRoeEthlinkID": tnRoeEthlinkID,
       "tnRoeEthlinkDescription": tnRoeEthlinkDescription,
       "tnRoeEthlinkDestMac": tnRoeEthlinkDestMac,
       "tnRoeEthlinkSourceMac": tnRoeEthlinkSourceMac,
       "tnRoeEthlinkTagDepth": tnRoeEthlinkTagDepth,
       "tnRoeEthlinkOuterEthertype": tnRoeEthlinkOuterEthertype,
       "tnRoeEthlinkOuterVid": tnRoeEthlinkOuterVid,
       "tnRoeEthlinkOuterPri": tnRoeEthlinkOuterPri,
       "tnRoeEthlinkInnerEthertype": tnRoeEthlinkInnerEthertype,
       "tnRoeEthlinkInnerVid": tnRoeEthlinkInnerVid,
       "tnRoeEthlinkInnerPri": tnRoeEthlinkInnerPri,
       "tnRoeEthlinkEthertype": tnRoeEthlinkEthertype,
       "tnRoeEthlinkRowStatus": tnRoeEthlinkRowStatus,
       "tnRoeEConf": tnRoeEConf,
       "tnRoeGroups": tnRoeGroups,
       "tnRoeSeqProfGroup": tnRoeSeqProfGroup,
       "tnRoeGroup": tnRoeGroup,
       "tnRoeMapperGroup": tnRoeMapperGroup,
       "tnRoeDeMapperGroup": tnRoeDeMapperGroup,
       "tnRoeEthlinkGroup": tnRoeEthlinkGroup,
       "tnEoeCompliances": tnEoeCompliances,
       "tnRoeCompliance": tnRoeCompliance}
)
