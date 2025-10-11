# SNMP MIB module (TN-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:49:54 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")

(TNamedItem,) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TNamedItem")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnBfdMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 85)
)
if mibBuilder.loadTexts:
    tnBfdMIBModule.setRevisions(
        ("2015-09-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnBfdObjects_ObjectIdentity = ObjectIdentity
tnBfdObjects = _TnBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85)
)
_TnBfdOperObjects_ObjectIdentity = ObjectIdentity
tnBfdOperObjects = _TnBfdOperObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1)
)
_TnBfdOperValueObjects_ObjectIdentity = ObjectIdentity
tnBfdOperValueObjects = _TnBfdOperValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1)
)
_TnBfdOperTemplateTable_Object = MibTable
tnBfdOperTemplateTable = _TnBfdOperTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnBfdOperTemplateTable.setStatus("current")
_TnBfdOperTemplateEntry_Object = MibTableRow
tnBfdOperTemplateEntry = _TnBfdOperTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1)
)
tnBfdOperTemplateEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-BFD-MIB", "tnBfdOperTemplateName"),
)
if mibBuilder.loadTexts:
    tnBfdOperTemplateEntry.setStatus("current")
_TnBfdOperTemplateName_Type = TNamedItem
_TnBfdOperTemplateName_Object = MibTableColumn
tnBfdOperTemplateName = _TnBfdOperTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1, 1),
    _TnBfdOperTemplateName_Type()
)
tnBfdOperTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnBfdOperTemplateName.setStatus("current")
_TnBfdOperTemplateRowStatus_Type = RowStatus
_TnBfdOperTemplateRowStatus_Object = MibTableColumn
tnBfdOperTemplateRowStatus = _TnBfdOperTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1, 2),
    _TnBfdOperTemplateRowStatus_Type()
)
tnBfdOperTemplateRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdOperTemplateRowStatus.setStatus("current")


class _TnBfdOperTemplateTxInt_Type(Unsigned32):
    """Custom type tnBfdOperTemplateTxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TnBfdOperTemplateTxInt_Type.__name__ = "Unsigned32"
_TnBfdOperTemplateTxInt_Object = MibTableColumn
tnBfdOperTemplateTxInt = _TnBfdOperTemplateTxInt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1, 3),
    _TnBfdOperTemplateTxInt_Type()
)
tnBfdOperTemplateTxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdOperTemplateTxInt.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdOperTemplateTxInt.setUnits("milliseconds")


class _TnBfdOperTemplateRxInt_Type(Unsigned32):
    """Custom type tnBfdOperTemplateRxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TnBfdOperTemplateRxInt_Type.__name__ = "Unsigned32"
_TnBfdOperTemplateRxInt_Object = MibTableColumn
tnBfdOperTemplateRxInt = _TnBfdOperTemplateRxInt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1, 4),
    _TnBfdOperTemplateRxInt_Type()
)
tnBfdOperTemplateRxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdOperTemplateRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdOperTemplateRxInt.setUnits("milliseconds")


class _TnBfdOperTemplateMultiplier_Type(Unsigned32):
    """Custom type tnBfdOperTemplateMultiplier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_TnBfdOperTemplateMultiplier_Type.__name__ = "Unsigned32"
_TnBfdOperTemplateMultiplier_Object = MibTableColumn
tnBfdOperTemplateMultiplier = _TnBfdOperTemplateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1, 5),
    _TnBfdOperTemplateMultiplier_Type()
)
tnBfdOperTemplateMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdOperTemplateMultiplier.setStatus("current")


class _TnBfdOperTemplateEchoRxInt_Type(Unsigned32):
    """Custom type tnBfdOperTemplateEchoRxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_TnBfdOperTemplateEchoRxInt_Type.__name__ = "Unsigned32"
_TnBfdOperTemplateEchoRxInt_Object = MibTableColumn
tnBfdOperTemplateEchoRxInt = _TnBfdOperTemplateEchoRxInt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1, 6),
    _TnBfdOperTemplateEchoRxInt_Type()
)
tnBfdOperTemplateEchoRxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdOperTemplateEchoRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdOperTemplateEchoRxInt.setUnits("milliseconds")


class _TnBfdOperTemplateType_Type(Integer32):
    """Custom type tnBfdOperTemplateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpmNp", 1),
          ("auto", 2),
          ("iomHw", 3))
    )


_TnBfdOperTemplateType_Type.__name__ = "Integer32"
_TnBfdOperTemplateType_Object = MibTableColumn
tnBfdOperTemplateType = _TnBfdOperTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 1, 1, 1, 1, 7),
    _TnBfdOperTemplateType_Type()
)
tnBfdOperTemplateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdOperTemplateType.setStatus("current")
_TnBfdAdminObjects_ObjectIdentity = ObjectIdentity
tnBfdAdminObjects = _TnBfdAdminObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2)
)
_TnBfdAdminControlObjects_ObjectIdentity = ObjectIdentity
tnBfdAdminControlObjects = _TnBfdAdminControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 1)
)


class _TnBfdAdminOwner_Type(DisplayString):
    """Custom type tnBfdAdminOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnBfdAdminOwner_Type.__name__ = "DisplayString"
_TnBfdAdminOwner_Object = MibScalar
tnBfdAdminOwner = _TnBfdAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 1, 1),
    _TnBfdAdminOwner_Type()
)
tnBfdAdminOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnBfdAdminOwner.setStatus("current")


class _TnBfdAdminControlApply_Type(Integer32):
    """Custom type tnBfdAdminControlApply based on Integer32"""
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
        *(("none", 1),
          ("initialize", 2),
          ("commit", 3))
    )


_TnBfdAdminControlApply_Type.__name__ = "Integer32"
_TnBfdAdminControlApply_Object = MibScalar
tnBfdAdminControlApply = _TnBfdAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 1, 2),
    _TnBfdAdminControlApply_Type()
)
tnBfdAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnBfdAdminControlApply.setStatus("current")
_TnBfdAdminLastSetTimer_Type = TimeInterval
_TnBfdAdminLastSetTimer_Object = MibScalar
tnBfdAdminLastSetTimer = _TnBfdAdminLastSetTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 1, 3),
    _TnBfdAdminLastSetTimer_Type()
)
tnBfdAdminLastSetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdAdminLastSetTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdAdminLastSetTimer.setUnits("centiseconds")


class _TnBfdAdminLastSetTimeout_Type(TimeInterval):
    """Custom type tnBfdAdminLastSetTimeout based on TimeInterval"""
    defaultValue = 180000


_TnBfdAdminLastSetTimeout_Type.__name__ = "TimeInterval"
_TnBfdAdminLastSetTimeout_Object = MibScalar
tnBfdAdminLastSetTimeout = _TnBfdAdminLastSetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 1, 4),
    _TnBfdAdminLastSetTimeout_Type()
)
tnBfdAdminLastSetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnBfdAdminLastSetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdAdminLastSetTimeout.setUnits("centiseconds")
_TnBfdAdminValueObjects_ObjectIdentity = ObjectIdentity
tnBfdAdminValueObjects = _TnBfdAdminValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2)
)
_TnBfdAdminTemplateTable_Object = MibTable
tnBfdAdminTemplateTable = _TnBfdAdminTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnBfdAdminTemplateTable.setStatus("current")
_TnBfdAdminTemplateEntry_Object = MibTableRow
tnBfdAdminTemplateEntry = _TnBfdAdminTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1)
)
tnBfdAdminTemplateEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-BFD-MIB", "tnBfdAdminTemplateName"),
)
if mibBuilder.loadTexts:
    tnBfdAdminTemplateEntry.setStatus("current")
_TnBfdAdminTemplateName_Type = TNamedItem
_TnBfdAdminTemplateName_Object = MibTableColumn
tnBfdAdminTemplateName = _TnBfdAdminTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1, 1),
    _TnBfdAdminTemplateName_Type()
)
tnBfdAdminTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateName.setStatus("current")
_TnBfdAdminTemplateRowStatus_Type = RowStatus
_TnBfdAdminTemplateRowStatus_Object = MibTableColumn
tnBfdAdminTemplateRowStatus = _TnBfdAdminTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1, 2),
    _TnBfdAdminTemplateRowStatus_Type()
)
tnBfdAdminTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateRowStatus.setStatus("current")


class _TnBfdAdminTemplateTxInt_Type(Unsigned32):
    """Custom type tnBfdAdminTemplateTxInt based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(10, 100000),
    )


_TnBfdAdminTemplateTxInt_Type.__name__ = "Unsigned32"
_TnBfdAdminTemplateTxInt_Object = MibTableColumn
tnBfdAdminTemplateTxInt = _TnBfdAdminTemplateTxInt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1, 3),
    _TnBfdAdminTemplateTxInt_Type()
)
tnBfdAdminTemplateTxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateTxInt.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateTxInt.setUnits("milliseconds")


class _TnBfdAdminTemplateRxInt_Type(Unsigned32):
    """Custom type tnBfdAdminTemplateRxInt based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(10, 100000),
    )


_TnBfdAdminTemplateRxInt_Type.__name__ = "Unsigned32"
_TnBfdAdminTemplateRxInt_Object = MibTableColumn
tnBfdAdminTemplateRxInt = _TnBfdAdminTemplateRxInt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1, 4),
    _TnBfdAdminTemplateRxInt_Type()
)
tnBfdAdminTemplateRxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateRxInt.setUnits("milliseconds")


class _TnBfdAdminTemplateMultiplier_Type(Unsigned32):
    """Custom type tnBfdAdminTemplateMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_TnBfdAdminTemplateMultiplier_Type.__name__ = "Unsigned32"
_TnBfdAdminTemplateMultiplier_Object = MibTableColumn
tnBfdAdminTemplateMultiplier = _TnBfdAdminTemplateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1, 5),
    _TnBfdAdminTemplateMultiplier_Type()
)
tnBfdAdminTemplateMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateMultiplier.setStatus("current")


class _TnBfdAdminTemplateEchoRxInt_Type(Unsigned32):
    """Custom type tnBfdAdminTemplateEchoRxInt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_TnBfdAdminTemplateEchoRxInt_Type.__name__ = "Unsigned32"
_TnBfdAdminTemplateEchoRxInt_Object = MibTableColumn
tnBfdAdminTemplateEchoRxInt = _TnBfdAdminTemplateEchoRxInt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1, 6),
    _TnBfdAdminTemplateEchoRxInt_Type()
)
tnBfdAdminTemplateEchoRxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateEchoRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateEchoRxInt.setUnits("milliseconds")


class _TnBfdAdminTemplateType_Type(Integer32):
    """Custom type tnBfdAdminTemplateType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpmNp", 1),
          ("auto", 2),
          ("iomHw", 3))
    )


_TnBfdAdminTemplateType_Type.__name__ = "Integer32"
_TnBfdAdminTemplateType_Object = MibTableColumn
tnBfdAdminTemplateType = _TnBfdAdminTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 1, 1, 7),
    _TnBfdAdminTemplateType_Type()
)
tnBfdAdminTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBfdAdminTemplateType.setStatus("current")
_TnBfdAdminValueScalar1_Type = Unsigned32
_TnBfdAdminValueScalar1_Object = MibScalar
tnBfdAdminValueScalar1 = _TnBfdAdminValueScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 101),
    _TnBfdAdminValueScalar1_Type()
)
tnBfdAdminValueScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdAdminValueScalar1.setStatus("current")
_TnBfdAdminValueScalar2_Type = Unsigned32
_TnBfdAdminValueScalar2_Object = MibScalar
tnBfdAdminValueScalar2 = _TnBfdAdminValueScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 85, 2, 2, 102),
    _TnBfdAdminValueScalar2_Type()
)
tnBfdAdminValueScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnBfdAdminValueScalar2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-BFD-MIB",
    **{"tnBfdMIBModule": tnBfdMIBModule,
       "tnBfdObjects": tnBfdObjects,
       "tnBfdOperObjects": tnBfdOperObjects,
       "tnBfdOperValueObjects": tnBfdOperValueObjects,
       "tnBfdOperTemplateTable": tnBfdOperTemplateTable,
       "tnBfdOperTemplateEntry": tnBfdOperTemplateEntry,
       "tnBfdOperTemplateName": tnBfdOperTemplateName,
       "tnBfdOperTemplateRowStatus": tnBfdOperTemplateRowStatus,
       "tnBfdOperTemplateTxInt": tnBfdOperTemplateTxInt,
       "tnBfdOperTemplateRxInt": tnBfdOperTemplateRxInt,
       "tnBfdOperTemplateMultiplier": tnBfdOperTemplateMultiplier,
       "tnBfdOperTemplateEchoRxInt": tnBfdOperTemplateEchoRxInt,
       "tnBfdOperTemplateType": tnBfdOperTemplateType,
       "tnBfdAdminObjects": tnBfdAdminObjects,
       "tnBfdAdminControlObjects": tnBfdAdminControlObjects,
       "tnBfdAdminOwner": tnBfdAdminOwner,
       "tnBfdAdminControlApply": tnBfdAdminControlApply,
       "tnBfdAdminLastSetTimer": tnBfdAdminLastSetTimer,
       "tnBfdAdminLastSetTimeout": tnBfdAdminLastSetTimeout,
       "tnBfdAdminValueObjects": tnBfdAdminValueObjects,
       "tnBfdAdminTemplateTable": tnBfdAdminTemplateTable,
       "tnBfdAdminTemplateEntry": tnBfdAdminTemplateEntry,
       "tnBfdAdminTemplateName": tnBfdAdminTemplateName,
       "tnBfdAdminTemplateRowStatus": tnBfdAdminTemplateRowStatus,
       "tnBfdAdminTemplateTxInt": tnBfdAdminTemplateTxInt,
       "tnBfdAdminTemplateRxInt": tnBfdAdminTemplateRxInt,
       "tnBfdAdminTemplateMultiplier": tnBfdAdminTemplateMultiplier,
       "tnBfdAdminTemplateEchoRxInt": tnBfdAdminTemplateEchoRxInt,
       "tnBfdAdminTemplateType": tnBfdAdminTemplateType,
       "tnBfdAdminValueScalar1": tnBfdAdminValueScalar1,
       "tnBfdAdminValueScalar2": tnBfdAdminValueScalar2}
)
