# SNMP MIB module (CPQICA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQICA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:10 2025
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqICA_ObjectIdentity = ObjectIdentity
cpqICA = _CpqICA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 140)
)
_CpqICAMibRev_ObjectIdentity = ObjectIdentity
cpqICAMibRev = _CpqICAMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 140, 1)
)


class _CpqICAMibRevMajor_Type(Integer32):
    """Custom type cpqICAMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqICAMibRevMajor_Type.__name__ = "Integer32"
_CpqICAMibRevMajor_Object = MibScalar
cpqICAMibRevMajor = _CpqICAMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 1, 1),
    _CpqICAMibRevMajor_Type()
)
cpqICAMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAMibRevMajor.setStatus("mandatory")


class _CpqICAMibRevMinor_Type(Integer32):
    """Custom type cpqICAMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqICAMibRevMinor_Type.__name__ = "Integer32"
_CpqICAMibRevMinor_Object = MibScalar
cpqICAMibRevMinor = _CpqICAMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 1, 2),
    _CpqICAMibRevMinor_Type()
)
cpqICAMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAMibRevMinor.setStatus("mandatory")


class _CpqICAMibCondition_Type(Integer32):
    """Custom type cpqICAMibCondition based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqICAMibCondition_Type.__name__ = "Integer32"
_CpqICAMibCondition_Object = MibScalar
cpqICAMibCondition = _CpqICAMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 1, 3),
    _CpqICAMibCondition_Type()
)
cpqICAMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAMibCondition.setStatus("mandatory")
_CpqICAComponent_ObjectIdentity = ObjectIdentity
cpqICAComponent = _CpqICAComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 140, 2)
)
_CpqICAInterface_ObjectIdentity = ObjectIdentity
cpqICAInterface = _CpqICAInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1)
)
_CpqICAOsCommon_ObjectIdentity = ObjectIdentity
cpqICAOsCommon = _CpqICAOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4)
)


class _CpqICAOsCommonPollFreq_Type(Integer32):
    """Custom type cpqICAOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqICAOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqICAOsCommonPollFreq_Object = MibScalar
cpqICAOsCommonPollFreq = _CpqICAOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 1),
    _CpqICAOsCommonPollFreq_Type()
)
cpqICAOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqICAOsCommonPollFreq.setStatus("mandatory")
_CpqICAOsCommonModuleTable_Object = MibTable
cpqICAOsCommonModuleTable = _CpqICAOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqICAOsCommonModuleTable.setStatus("mandatory")
_CpqICAOsCommonModuleEntry_Object = MibTableRow
cpqICAOsCommonModuleEntry = _CpqICAOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 2, 1)
)
cpqICAOsCommonModuleEntry.setIndexNames(
    (0, "CPQICA-MIB", "cpqICAOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqICAOsCommonModuleEntry.setStatus("mandatory")


class _CpqICAOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqICAOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqICAOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqICAOsCommonModuleIndex_Object = MibTableColumn
cpqICAOsCommonModuleIndex = _CpqICAOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 2, 1, 1),
    _CpqICAOsCommonModuleIndex_Type()
)
cpqICAOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAOsCommonModuleIndex.setStatus("mandatory")


class _CpqICAOsCommonModuleName_Type(DisplayString):
    """Custom type cpqICAOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqICAOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqICAOsCommonModuleName_Object = MibTableColumn
cpqICAOsCommonModuleName = _CpqICAOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 2, 1, 2),
    _CpqICAOsCommonModuleName_Type()
)
cpqICAOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAOsCommonModuleName.setStatus("mandatory")


class _CpqICAOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqICAOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqICAOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqICAOsCommonModuleVersion_Object = MibTableColumn
cpqICAOsCommonModuleVersion = _CpqICAOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 2, 1, 3),
    _CpqICAOsCommonModuleVersion_Type()
)
cpqICAOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAOsCommonModuleVersion.setStatus("mandatory")


class _CpqICAOsCommonModuleDate_Type(OctetString):
    """Custom type cpqICAOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_CpqICAOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqICAOsCommonModuleDate_Object = MibTableColumn
cpqICAOsCommonModuleDate = _CpqICAOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 2, 1, 4),
    _CpqICAOsCommonModuleDate_Type()
)
cpqICAOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAOsCommonModuleDate.setStatus("mandatory")


class _CpqICAOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqICAOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqICAOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqICAOsCommonModulePurpose_Object = MibTableColumn
cpqICAOsCommonModulePurpose = _CpqICAOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 1, 4, 2, 1, 5),
    _CpqICAOsCommonModulePurpose_Type()
)
cpqICAOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqICAOsCommonModulePurpose.setStatus("mandatory")
_CpqICAICA_ObjectIdentity = ObjectIdentity
cpqICAICA = _CpqICAICA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 140, 2, 2)
)

# Managed Objects groups


# Notification objects

cpqICAAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 140001)
)
if mibBuilder.loadTexts:
    cpqICAAdd.setStatus(
        ""
    )

cpqICADelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 140002)
)
if mibBuilder.loadTexts:
    cpqICADelete.setStatus(
        ""
    )

cpqICAPropertyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 140003)
)
if mibBuilder.loadTexts:
    cpqICAPropertyChange.setStatus(
        ""
    )

cpqICAMove = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 140004)
)
if mibBuilder.loadTexts:
    cpqICAMove.setStatus(
        ""
    )

cpqICAImportRestoreStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 140005)
)
if mibBuilder.loadTexts:
    cpqICAImportRestoreStart.setStatus(
        ""
    )

cpqICAImportRestoreEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 140006)
)
if mibBuilder.loadTexts:
    cpqICAImportRestoreEnd.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQICA-MIB",
    **{"cpqICAAdd": cpqICAAdd,
       "cpqICADelete": cpqICADelete,
       "cpqICAPropertyChange": cpqICAPropertyChange,
       "cpqICAMove": cpqICAMove,
       "cpqICAImportRestoreStart": cpqICAImportRestoreStart,
       "cpqICAImportRestoreEnd": cpqICAImportRestoreEnd,
       "cpqICA": cpqICA,
       "cpqICAMibRev": cpqICAMibRev,
       "cpqICAMibRevMajor": cpqICAMibRevMajor,
       "cpqICAMibRevMinor": cpqICAMibRevMinor,
       "cpqICAMibCondition": cpqICAMibCondition,
       "cpqICAComponent": cpqICAComponent,
       "cpqICAInterface": cpqICAInterface,
       "cpqICAOsCommon": cpqICAOsCommon,
       "cpqICAOsCommonPollFreq": cpqICAOsCommonPollFreq,
       "cpqICAOsCommonModuleTable": cpqICAOsCommonModuleTable,
       "cpqICAOsCommonModuleEntry": cpqICAOsCommonModuleEntry,
       "cpqICAOsCommonModuleIndex": cpqICAOsCommonModuleIndex,
       "cpqICAOsCommonModuleName": cpqICAOsCommonModuleName,
       "cpqICAOsCommonModuleVersion": cpqICAOsCommonModuleVersion,
       "cpqICAOsCommonModuleDate": cpqICAOsCommonModuleDate,
       "cpqICAOsCommonModulePurpose": cpqICAOsCommonModulePurpose,
       "cpqICAICA": cpqICAICA}
)
