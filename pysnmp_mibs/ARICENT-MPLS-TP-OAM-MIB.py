# SNMP MIB module (ARICENT-MPLS-TP-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MPLS-TP-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:38 2025
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

(fsMplsTpContextId,) = mibBuilder.importSymbols(
    "ARICENT-MPLS-TP-MIB",
    "fsMplsTpContextId")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMplsTpOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9)
)
if mibBuilder.loadTexts:
    fsMplsTpOamMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsTpOamNotifications_ObjectIdentity = ObjectIdentity
fsMplsTpOamNotifications = _FsMplsTpOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 0)
)
_FsMplsTpOamObjects_ObjectIdentity = ObjectIdentity
fsMplsTpOamObjects = _FsMplsTpOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1)
)
_FsMplsTpOamScalarObjects_ObjectIdentity = ObjectIdentity
fsMplsTpOamScalarObjects = _FsMplsTpOamScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 1)
)
_FsMplsTpMegTable_Object = MibTable
fsMplsTpMegTable = _FsMplsTpMegTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2)
)
if mibBuilder.loadTexts:
    fsMplsTpMegTable.setStatus("current")
_FsMplsTpMegEntry_Object = MibTableRow
fsMplsTpMegEntry = _FsMplsTpMegEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1)
)
fsMplsTpMegEntry.setIndexNames(
    (0, "ARICENT-MPLS-TP-MIB", "fsMplsTpContextId"),
    (0, "ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpMegIndex"),
)
if mibBuilder.loadTexts:
    fsMplsTpMegEntry.setStatus("current")
_FsMplsTpMegIndex_Type = Unsigned32
_FsMplsTpMegIndex_Object = MibTableColumn
fsMplsTpMegIndex = _FsMplsTpMegIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 1),
    _FsMplsTpMegIndex_Type()
)
fsMplsTpMegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsTpMegIndex.setStatus("current")


class _FsMplsTpMegName_Type(DisplayString):
    """Custom type fsMplsTpMegName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_FsMplsTpMegName_Type.__name__ = "DisplayString"
_FsMplsTpMegName_Object = MibTableColumn
fsMplsTpMegName = _FsMplsTpMegName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 2),
    _FsMplsTpMegName_Type()
)
fsMplsTpMegName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMegName.setStatus("current")


class _FsMplsTpMegOperatorType_Type(Integer32):
    """Custom type fsMplsTpMegOperatorType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipCompatible", 1),
          ("iccBased", 2))
    )


_FsMplsTpMegOperatorType_Type.__name__ = "Integer32"
_FsMplsTpMegOperatorType_Object = MibTableColumn
fsMplsTpMegOperatorType = _FsMplsTpMegOperatorType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 3),
    _FsMplsTpMegOperatorType_Type()
)
fsMplsTpMegOperatorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMegOperatorType.setStatus("current")


class _FsMplsTpMegIdIcc_Type(DisplayString):
    """Custom type fsMplsTpMegIdIcc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_FsMplsTpMegIdIcc_Type.__name__ = "DisplayString"
_FsMplsTpMegIdIcc_Object = MibTableColumn
fsMplsTpMegIdIcc = _FsMplsTpMegIdIcc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 4),
    _FsMplsTpMegIdIcc_Type()
)
fsMplsTpMegIdIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpMegIdIcc.setStatus("current")


class _FsMplsTpMegIdUmc_Type(DisplayString):
    """Custom type fsMplsTpMegIdUmc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_FsMplsTpMegIdUmc_Type.__name__ = "DisplayString"
_FsMplsTpMegIdUmc_Object = MibTableColumn
fsMplsTpMegIdUmc = _FsMplsTpMegIdUmc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 5),
    _FsMplsTpMegIdUmc_Type()
)
fsMplsTpMegIdUmc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpMegIdUmc.setStatus("current")


class _FsMplsTpMegServiceType_Type(Integer32):
    """Custom type fsMplsTpMegServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lsp", 1),
          ("pseudowire", 2),
          ("section", 3))
    )


_FsMplsTpMegServiceType_Type.__name__ = "Integer32"
_FsMplsTpMegServiceType_Object = MibTableColumn
fsMplsTpMegServiceType = _FsMplsTpMegServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 6),
    _FsMplsTpMegServiceType_Type()
)
fsMplsTpMegServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMegServiceType.setStatus("current")


class _FsMplsTpMegMpLocation_Type(Integer32):
    """Custom type fsMplsTpMegMpLocation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perNode", 1),
          ("perInterface", 2))
    )


_FsMplsTpMegMpLocation_Type.__name__ = "Integer32"
_FsMplsTpMegMpLocation_Object = MibTableColumn
fsMplsTpMegMpLocation = _FsMplsTpMegMpLocation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 7),
    _FsMplsTpMegMpLocation_Type()
)
fsMplsTpMegMpLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMegMpLocation.setStatus("current")
_FsMplsTpMegRowStatus_Type = RowStatus
_FsMplsTpMegRowStatus_Object = MibTableColumn
fsMplsTpMegRowStatus = _FsMplsTpMegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 2, 1, 8),
    _FsMplsTpMegRowStatus_Type()
)
fsMplsTpMegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMegRowStatus.setStatus("current")
_FsMplsTpMeTable_Object = MibTable
fsMplsTpMeTable = _FsMplsTpMeTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3)
)
if mibBuilder.loadTexts:
    fsMplsTpMeTable.setStatus("current")
_FsMplsTpMeEntry_Object = MibTableRow
fsMplsTpMeEntry = _FsMplsTpMeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1)
)
fsMplsTpMeEntry.setIndexNames(
    (0, "ARICENT-MPLS-TP-MIB", "fsMplsTpContextId"),
    (0, "ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpMegIndex"),
    (0, "ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpMeIndex"),
    (0, "ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpMeMpIndex"),
)
if mibBuilder.loadTexts:
    fsMplsTpMeEntry.setStatus("current")
_FsMplsTpMeIndex_Type = Unsigned32
_FsMplsTpMeIndex_Object = MibTableColumn
fsMplsTpMeIndex = _FsMplsTpMeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 1),
    _FsMplsTpMeIndex_Type()
)
fsMplsTpMeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsTpMeIndex.setStatus("current")
_FsMplsTpMeMpIndex_Type = Unsigned32
_FsMplsTpMeMpIndex_Object = MibTableColumn
fsMplsTpMeMpIndex = _FsMplsTpMeMpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 2),
    _FsMplsTpMeMpIndex_Type()
)
fsMplsTpMeMpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsTpMeMpIndex.setStatus("current")


class _FsMplsTpMeName_Type(DisplayString):
    """Custom type fsMplsTpMeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_FsMplsTpMeName_Type.__name__ = "DisplayString"
_FsMplsTpMeName_Object = MibTableColumn
fsMplsTpMeName = _FsMplsTpMeName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 3),
    _FsMplsTpMeName_Type()
)
fsMplsTpMeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeName.setStatus("current")


class _FsMplsTpMeMpIfIndex_Type(InterfaceIndexOrZero):
    """Custom type fsMplsTpMeMpIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsMplsTpMeMpIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_FsMplsTpMeMpIfIndex_Object = MibTableColumn
fsMplsTpMeMpIfIndex = _FsMplsTpMeMpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 4),
    _FsMplsTpMeMpIfIndex_Type()
)
fsMplsTpMeMpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeMpIfIndex.setStatus("current")


class _FsMplsTpMeSourceMepIndex_Type(Unsigned32):
    """Custom type fsMplsTpMeSourceMepIndex based on Unsigned32"""
    defaultValue = 0


_FsMplsTpMeSourceMepIndex_Type.__name__ = "Unsigned32"
_FsMplsTpMeSourceMepIndex_Object = MibTableColumn
fsMplsTpMeSourceMepIndex = _FsMplsTpMeSourceMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 5),
    _FsMplsTpMeSourceMepIndex_Type()
)
fsMplsTpMeSourceMepIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeSourceMepIndex.setStatus("current")


class _FsMplsTpMeSinkMepIndex_Type(Unsigned32):
    """Custom type fsMplsTpMeSinkMepIndex based on Unsigned32"""
    defaultValue = 0


_FsMplsTpMeSinkMepIndex_Type.__name__ = "Unsigned32"
_FsMplsTpMeSinkMepIndex_Object = MibTableColumn
fsMplsTpMeSinkMepIndex = _FsMplsTpMeSinkMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 6),
    _FsMplsTpMeSinkMepIndex_Type()
)
fsMplsTpMeSinkMepIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeSinkMepIndex.setStatus("current")


class _FsMplsTpMeMpType_Type(Integer32):
    """Custom type fsMplsTpMeMpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mep", 1),
          ("mip", 2))
    )


_FsMplsTpMeMpType_Type.__name__ = "Integer32"
_FsMplsTpMeMpType_Object = MibTableColumn
fsMplsTpMeMpType = _FsMplsTpMeMpType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 7),
    _FsMplsTpMeMpType_Type()
)
fsMplsTpMeMpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeMpType.setStatus("current")


class _FsMplsTpMeMepDirection_Type(Integer32):
    """Custom type fsMplsTpMeMepDirection based on Integer32"""
    defaultValue = 2

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


_FsMplsTpMeMepDirection_Type.__name__ = "Integer32"
_FsMplsTpMeMepDirection_Object = MibTableColumn
fsMplsTpMeMepDirection = _FsMplsTpMeMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 8),
    _FsMplsTpMeMepDirection_Type()
)
fsMplsTpMeMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeMepDirection.setStatus("current")


class _FsMplsTpMeProactiveOamSessIndex_Type(Unsigned32):
    """Custom type fsMplsTpMeProactiveOamSessIndex based on Unsigned32"""
    defaultValue = 0


_FsMplsTpMeProactiveOamSessIndex_Type.__name__ = "Unsigned32"
_FsMplsTpMeProactiveOamSessIndex_Object = MibTableColumn
fsMplsTpMeProactiveOamSessIndex = _FsMplsTpMeProactiveOamSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 9),
    _FsMplsTpMeProactiveOamSessIndex_Type()
)
fsMplsTpMeProactiveOamSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsTpMeProactiveOamSessIndex.setStatus("current")


class _FsMplsTpMeProactiveOamPhbTCValue_Type(Integer32):
    """Custom type fsMplsTpMeProactiveOamPhbTCValue based on Integer32"""
    defaultValue = 1

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
        *(("ef1", 1),
          ("ef2", 2),
          ("af1", 3),
          ("af2", 4),
          ("af3", 5),
          ("be", 6))
    )


_FsMplsTpMeProactiveOamPhbTCValue_Type.__name__ = "Integer32"
_FsMplsTpMeProactiveOamPhbTCValue_Object = MibTableColumn
fsMplsTpMeProactiveOamPhbTCValue = _FsMplsTpMeProactiveOamPhbTCValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 10),
    _FsMplsTpMeProactiveOamPhbTCValue_Type()
)
fsMplsTpMeProactiveOamPhbTCValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeProactiveOamPhbTCValue.setStatus("current")


class _FsMplsTpMeOnDemandOamPhbTCValue_Type(Integer32):
    """Custom type fsMplsTpMeOnDemandOamPhbTCValue based on Integer32"""
    defaultValue = 1

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
        *(("ef1", 1),
          ("ef2", 2),
          ("af1", 3),
          ("af2", 4),
          ("af3", 5),
          ("be", 6))
    )


_FsMplsTpMeOnDemandOamPhbTCValue_Type.__name__ = "Integer32"
_FsMplsTpMeOnDemandOamPhbTCValue_Object = MibTableColumn
fsMplsTpMeOnDemandOamPhbTCValue = _FsMplsTpMeOnDemandOamPhbTCValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 11),
    _FsMplsTpMeOnDemandOamPhbTCValue_Type()
)
fsMplsTpMeOnDemandOamPhbTCValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeOnDemandOamPhbTCValue.setStatus("current")


class _FsMplsTpMeServiceSignaled_Type(TruthValue):
    """Custom type fsMplsTpMeServiceSignaled based on TruthValue"""
    defaultValue = 2


_FsMplsTpMeServiceSignaled_Type.__name__ = "TruthValue"
_FsMplsTpMeServiceSignaled_Object = MibTableColumn
fsMplsTpMeServiceSignaled = _FsMplsTpMeServiceSignaled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 12),
    _FsMplsTpMeServiceSignaled_Type()
)
fsMplsTpMeServiceSignaled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeServiceSignaled.setStatus("current")


class _FsMplsTpMeServicePointer_Type(RowPointer):
    """Custom type fsMplsTpMeServicePointer based on RowPointer"""
    defaultValue = (0, 0)


_FsMplsTpMeServicePointer_Type.__name__ = "RowPointer"
_FsMplsTpMeServicePointer_Object = MibTableColumn
fsMplsTpMeServicePointer = _FsMplsTpMeServicePointer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 13),
    _FsMplsTpMeServicePointer_Type()
)
fsMplsTpMeServicePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeServicePointer.setStatus("current")
_FsMplsTpMeRowStatus_Type = RowStatus
_FsMplsTpMeRowStatus_Object = MibTableColumn
fsMplsTpMeRowStatus = _FsMplsTpMeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 3, 1, 14),
    _FsMplsTpMeRowStatus_Type()
)
fsMplsTpMeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpMeRowStatus.setStatus("current")


class _FsMplsTpOamContextName_Type(DisplayString):
    """Custom type fsMplsTpOamContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsMplsTpOamContextName_Type.__name__ = "DisplayString"
_FsMplsTpOamContextName_Object = MibScalar
fsMplsTpOamContextName = _FsMplsTpOamContextName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 4),
    _FsMplsTpOamContextName_Type()
)
fsMplsTpOamContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMplsTpOamContextName.setStatus("current")


class _FsMplsTpOamMegOperStatus_Type(Integer32):
    """Custom type fsMplsTpOamMegOperStatus based on Integer32"""
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


_FsMplsTpOamMegOperStatus_Type.__name__ = "Integer32"
_FsMplsTpOamMegOperStatus_Object = MibScalar
fsMplsTpOamMegOperStatus = _FsMplsTpOamMegOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 5),
    _FsMplsTpOamMegOperStatus_Type()
)
fsMplsTpOamMegOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMplsTpOamMegOperStatus.setStatus("current")


class _FsMplsTpOamMegSubOperStatus_Type(Bits):
    """Custom type fsMplsTpOamMegSubOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("megDown", 0),
          ("meDown", 1),
          ("oamAppDown", 2),
          ("pathDown", 3))
    )

_FsMplsTpOamMegSubOperStatus_Type.__name__ = "Bits"
_FsMplsTpOamMegSubOperStatus_Object = MibScalar
fsMplsTpOamMegSubOperStatus = _FsMplsTpOamMegSubOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 1, 6),
    _FsMplsTpOamMegSubOperStatus_Type()
)
fsMplsTpOamMegSubOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMplsTpOamMegSubOperStatus.setStatus("current")
_FsMplsTpOamConformance_ObjectIdentity = ObjectIdentity
fsMplsTpOamConformance = _FsMplsTpOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 2)
)

# Managed Objects groups


# Notification objects

fsMplsTpOamDefectCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 13, 9, 0, 1)
)
fsMplsTpOamDefectCondition.setObjects(
      *(("ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpOamContextName"),
        ("ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpMegName"),
        ("ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpMeName"),
        ("ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpOamMegOperStatus"),
        ("ARICENT-MPLS-TP-OAM-MIB", "fsMplsTpOamMegSubOperStatus"))
)
if mibBuilder.loadTexts:
    fsMplsTpOamDefectCondition.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MPLS-TP-OAM-MIB",
    **{"fsMplsTpOamMIB": fsMplsTpOamMIB,
       "fsMplsTpOamNotifications": fsMplsTpOamNotifications,
       "fsMplsTpOamDefectCondition": fsMplsTpOamDefectCondition,
       "fsMplsTpOamObjects": fsMplsTpOamObjects,
       "fsMplsTpOamScalarObjects": fsMplsTpOamScalarObjects,
       "fsMplsTpMegTable": fsMplsTpMegTable,
       "fsMplsTpMegEntry": fsMplsTpMegEntry,
       "fsMplsTpMegIndex": fsMplsTpMegIndex,
       "fsMplsTpMegName": fsMplsTpMegName,
       "fsMplsTpMegOperatorType": fsMplsTpMegOperatorType,
       "fsMplsTpMegIdIcc": fsMplsTpMegIdIcc,
       "fsMplsTpMegIdUmc": fsMplsTpMegIdUmc,
       "fsMplsTpMegServiceType": fsMplsTpMegServiceType,
       "fsMplsTpMegMpLocation": fsMplsTpMegMpLocation,
       "fsMplsTpMegRowStatus": fsMplsTpMegRowStatus,
       "fsMplsTpMeTable": fsMplsTpMeTable,
       "fsMplsTpMeEntry": fsMplsTpMeEntry,
       "fsMplsTpMeIndex": fsMplsTpMeIndex,
       "fsMplsTpMeMpIndex": fsMplsTpMeMpIndex,
       "fsMplsTpMeName": fsMplsTpMeName,
       "fsMplsTpMeMpIfIndex": fsMplsTpMeMpIfIndex,
       "fsMplsTpMeSourceMepIndex": fsMplsTpMeSourceMepIndex,
       "fsMplsTpMeSinkMepIndex": fsMplsTpMeSinkMepIndex,
       "fsMplsTpMeMpType": fsMplsTpMeMpType,
       "fsMplsTpMeMepDirection": fsMplsTpMeMepDirection,
       "fsMplsTpMeProactiveOamSessIndex": fsMplsTpMeProactiveOamSessIndex,
       "fsMplsTpMeProactiveOamPhbTCValue": fsMplsTpMeProactiveOamPhbTCValue,
       "fsMplsTpMeOnDemandOamPhbTCValue": fsMplsTpMeOnDemandOamPhbTCValue,
       "fsMplsTpMeServiceSignaled": fsMplsTpMeServiceSignaled,
       "fsMplsTpMeServicePointer": fsMplsTpMeServicePointer,
       "fsMplsTpMeRowStatus": fsMplsTpMeRowStatus,
       "fsMplsTpOamContextName": fsMplsTpOamContextName,
       "fsMplsTpOamMegOperStatus": fsMplsTpOamMegOperStatus,
       "fsMplsTpOamMegSubOperStatus": fsMplsTpOamMegSubOperStatus,
       "fsMplsTpOamConformance": fsMplsTpOamConformance}
)
