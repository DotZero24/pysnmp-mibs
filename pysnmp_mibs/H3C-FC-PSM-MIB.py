# SNMP MIB module (H3C-FC-PSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FC-PSM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:29 2025
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

(H3cFcNameIdOrZero,) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcNameIdOrZero")

(h3cSan,) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cFcPsm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8)
)
if mibBuilder.loadTexts:
    h3cFcPsm.setRevisions(
        ("2013-10-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cFcPsmPortBindDevType(TextualConvention, Integer32):
    status = "current"
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
        *(("nWWN", 1),
          ("pWWN", 2),
          ("sWWN", 3),
          ("wildCard", 4))
    )



class H3cFcPsmClearEntryType(TextualConvention, Integer32):
    status = "current"
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
        *(("clearStatic", 1),
          ("clearAutoLearn", 2),
          ("clearAll", 3),
          ("noop", 4))
    )



# MIB Managed Objects in the order of their OIDs

_H3cFcPsmNotifications_ObjectIdentity = ObjectIdentity
h3cFcPsmNotifications = _H3cFcPsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 0)
)
_H3cFcPsmObjects_ObjectIdentity = ObjectIdentity
h3cFcPsmObjects = _H3cFcPsmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1)
)
_H3cFcPsmScalarObjects_ObjectIdentity = ObjectIdentity
h3cFcPsmScalarObjects = _H3cFcPsmScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 1)
)


class _H3cFcPsmNotifyEnable_Type(TruthValue):
    """Custom type h3cFcPsmNotifyEnable based on TruthValue"""
    defaultValue = 2


_H3cFcPsmNotifyEnable_Type.__name__ = "TruthValue"
_H3cFcPsmNotifyEnable_Object = MibScalar
h3cFcPsmNotifyEnable = _H3cFcPsmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 1, 1),
    _H3cFcPsmNotifyEnable_Type()
)
h3cFcPsmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcPsmNotifyEnable.setStatus("current")
_H3cFcPsmConfiguration_ObjectIdentity = ObjectIdentity
h3cFcPsmConfiguration = _H3cFcPsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2)
)
_H3cFcPsmEnableTable_Object = MibTable
h3cFcPsmEnableTable = _H3cFcPsmEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFcPsmEnableTable.setStatus("current")
_H3cFcPsmEnableEntry_Object = MibTableRow
h3cFcPsmEnableEntry = _H3cFcPsmEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 1, 1)
)
h3cFcPsmEnableEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmEnableEntry.setStatus("current")


class _H3cFcPsmEnableVsanIndex_Type(Unsigned32):
    """Custom type h3cFcPsmEnableVsanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_H3cFcPsmEnableVsanIndex_Type.__name__ = "Unsigned32"
_H3cFcPsmEnableVsanIndex_Object = MibTableColumn
h3cFcPsmEnableVsanIndex = _H3cFcPsmEnableVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 1, 1, 1),
    _H3cFcPsmEnableVsanIndex_Type()
)
h3cFcPsmEnableVsanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcPsmEnableVsanIndex.setStatus("current")


class _H3cFcPsmEnable_Type(Integer32):
    """Custom type h3cFcPsmEnable based on Integer32"""
    defaultValue = 4

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
        *(("enable", 1),
          ("enableWithAutoLearn", 2),
          ("disable", 3),
          ("noop", 4))
    )


_H3cFcPsmEnable_Type.__name__ = "Integer32"
_H3cFcPsmEnable_Object = MibTableColumn
h3cFcPsmEnable = _H3cFcPsmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 1, 1, 2),
    _H3cFcPsmEnable_Type()
)
h3cFcPsmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcPsmEnable.setStatus("current")


class _H3cFcPsmEnableState_Type(TruthValue):
    """Custom type h3cFcPsmEnableState based on TruthValue"""
    defaultValue = 2


_H3cFcPsmEnableState_Type.__name__ = "TruthValue"
_H3cFcPsmEnableState_Object = MibTableColumn
h3cFcPsmEnableState = _H3cFcPsmEnableState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 1, 1, 3),
    _H3cFcPsmEnableState_Type()
)
h3cFcPsmEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmEnableState.setStatus("current")
_H3cFcPsmConfigTable_Object = MibTable
h3cFcPsmConfigTable = _H3cFcPsmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cFcPsmConfigTable.setStatus("current")
_H3cFcPsmConfigEntry_Object = MibTableRow
h3cFcPsmConfigEntry = _H3cFcPsmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 2, 1)
)
h3cFcPsmConfigEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmConfigEntry.setStatus("current")


class _H3cFcPsmIndex_Type(Unsigned32):
    """Custom type h3cFcPsmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_H3cFcPsmIndex_Type.__name__ = "Unsigned32"
_H3cFcPsmIndex_Object = MibTableColumn
h3cFcPsmIndex = _H3cFcPsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 2, 1, 1),
    _H3cFcPsmIndex_Type()
)
h3cFcPsmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcPsmIndex.setStatus("current")
_H3cFcPsmLoginDevType_Type = H3cFcPsmPortBindDevType
_H3cFcPsmLoginDevType_Object = MibTableColumn
h3cFcPsmLoginDevType = _H3cFcPsmLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 2, 1, 2),
    _H3cFcPsmLoginDevType_Type()
)
h3cFcPsmLoginDevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPsmLoginDevType.setStatus("current")
_H3cFcPsmLoginDev_Type = H3cFcNameIdOrZero
_H3cFcPsmLoginDev_Object = MibTableColumn
h3cFcPsmLoginDev = _H3cFcPsmLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 2, 1, 3),
    _H3cFcPsmLoginDev_Type()
)
h3cFcPsmLoginDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPsmLoginDev.setStatus("current")
_H3cFcPsmLoginPoint_Type = InterfaceIndexOrZero
_H3cFcPsmLoginPoint_Object = MibTableColumn
h3cFcPsmLoginPoint = _H3cFcPsmLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 2, 1, 4),
    _H3cFcPsmLoginPoint_Type()
)
h3cFcPsmLoginPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPsmLoginPoint.setStatus("current")
_H3cFcPsmRowStatus_Type = RowStatus
_H3cFcPsmRowStatus_Object = MibTableColumn
h3cFcPsmRowStatus = _H3cFcPsmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 2, 1, 5),
    _H3cFcPsmRowStatus_Type()
)
h3cFcPsmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPsmRowStatus.setStatus("current")
_H3cFcPsmEnfTable_Object = MibTable
h3cFcPsmEnfTable = _H3cFcPsmEnfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cFcPsmEnfTable.setStatus("current")
_H3cFcPsmEnfEntry_Object = MibTableRow
h3cFcPsmEnfEntry = _H3cFcPsmEnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 3, 1)
)
h3cFcPsmEnfEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnfIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmEnfEntry.setStatus("current")


class _H3cFcPsmEnfIndex_Type(Unsigned32):
    """Custom type h3cFcPsmEnfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_H3cFcPsmEnfIndex_Type.__name__ = "Unsigned32"
_H3cFcPsmEnfIndex_Object = MibTableColumn
h3cFcPsmEnfIndex = _H3cFcPsmEnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 3, 1, 1),
    _H3cFcPsmEnfIndex_Type()
)
h3cFcPsmEnfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcPsmEnfIndex.setStatus("current")
_H3cFcPsmEnfLoginDevType_Type = H3cFcPsmPortBindDevType
_H3cFcPsmEnfLoginDevType_Object = MibTableColumn
h3cFcPsmEnfLoginDevType = _H3cFcPsmEnfLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 3, 1, 2),
    _H3cFcPsmEnfLoginDevType_Type()
)
h3cFcPsmEnfLoginDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmEnfLoginDevType.setStatus("current")
_H3cFcPsmEnfLoginDev_Type = H3cFcNameIdOrZero
_H3cFcPsmEnfLoginDev_Object = MibTableColumn
h3cFcPsmEnfLoginDev = _H3cFcPsmEnfLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 3, 1, 3),
    _H3cFcPsmEnfLoginDev_Type()
)
h3cFcPsmEnfLoginDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmEnfLoginDev.setStatus("current")
_H3cFcPsmEnfLoginPoint_Type = InterfaceIndexOrZero
_H3cFcPsmEnfLoginPoint_Object = MibTableColumn
h3cFcPsmEnfLoginPoint = _H3cFcPsmEnfLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 3, 1, 4),
    _H3cFcPsmEnfLoginPoint_Type()
)
h3cFcPsmEnfLoginPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmEnfLoginPoint.setStatus("current")


class _H3cFcPsmEnfEntryType_Type(Integer32):
    """Custom type h3cFcPsmEnfEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learning", 1),
          ("learned", 2),
          ("static", 3))
    )


_H3cFcPsmEnfEntryType_Type.__name__ = "Integer32"
_H3cFcPsmEnfEntryType_Object = MibTableColumn
h3cFcPsmEnfEntryType = _H3cFcPsmEnfEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 3, 1, 5),
    _H3cFcPsmEnfEntryType_Type()
)
h3cFcPsmEnfEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmEnfEntryType.setStatus("current")
_H3cFcPsmCopyToConfigTable_Object = MibTable
h3cFcPsmCopyToConfigTable = _H3cFcPsmCopyToConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cFcPsmCopyToConfigTable.setStatus("current")
_H3cFcPsmCopyToConfigEntry_Object = MibTableRow
h3cFcPsmCopyToConfigEntry = _H3cFcPsmCopyToConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 4, 1)
)
h3cFcPsmCopyToConfigEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmCopyToConfigEntry.setStatus("current")


class _H3cFcPsmCopyToConfig_Type(Integer32):
    """Custom type h3cFcPsmCopyToConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("noop", 2))
    )


_H3cFcPsmCopyToConfig_Type.__name__ = "Integer32"
_H3cFcPsmCopyToConfig_Object = MibTableColumn
h3cFcPsmCopyToConfig = _H3cFcPsmCopyToConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 4, 1, 1),
    _H3cFcPsmCopyToConfig_Type()
)
h3cFcPsmCopyToConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcPsmCopyToConfig.setStatus("current")
_H3cFcPsmAutoLearnTable_Object = MibTable
h3cFcPsmAutoLearnTable = _H3cFcPsmAutoLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    h3cFcPsmAutoLearnTable.setStatus("current")
_H3cFcPsmAutoLearnEntry_Object = MibTableRow
h3cFcPsmAutoLearnEntry = _H3cFcPsmAutoLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 5, 1)
)
h3cFcPsmAutoLearnEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmAutoLearnEntry.setStatus("current")


class _H3cFcPsmAutoLearnEnable_Type(TruthValue):
    """Custom type h3cFcPsmAutoLearnEnable based on TruthValue"""
    defaultValue = 2


_H3cFcPsmAutoLearnEnable_Type.__name__ = "TruthValue"
_H3cFcPsmAutoLearnEnable_Object = MibTableColumn
h3cFcPsmAutoLearnEnable = _H3cFcPsmAutoLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 5, 1, 1),
    _H3cFcPsmAutoLearnEnable_Type()
)
h3cFcPsmAutoLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcPsmAutoLearnEnable.setStatus("current")
_H3cFcPsmClearTable_Object = MibTable
h3cFcPsmClearTable = _H3cFcPsmClearTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    h3cFcPsmClearTable.setStatus("current")
_H3cFcPsmClearEntry_Object = MibTableRow
h3cFcPsmClearEntry = _H3cFcPsmClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 6, 1)
)
h3cFcPsmClearEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmClearEntry.setStatus("current")


class _H3cFcPsmClearType_Type(H3cFcPsmClearEntryType):
    """Custom type h3cFcPsmClearType based on H3cFcPsmClearEntryType"""
    defaultValue = 4


_H3cFcPsmClearType_Type.__name__ = "H3cFcPsmClearEntryType"
_H3cFcPsmClearType_Object = MibTableColumn
h3cFcPsmClearType = _H3cFcPsmClearType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 6, 1, 1),
    _H3cFcPsmClearType_Type()
)
h3cFcPsmClearType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcPsmClearType.setStatus("current")
_H3cFcPsmClearIntf_Type = InterfaceIndexOrZero
_H3cFcPsmClearIntf_Object = MibTableColumn
h3cFcPsmClearIntf = _H3cFcPsmClearIntf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 2, 6, 1, 2),
    _H3cFcPsmClearIntf_Type()
)
h3cFcPsmClearIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcPsmClearIntf.setStatus("current")
_H3cFcPsmStats_ObjectIdentity = ObjectIdentity
h3cFcPsmStats = _H3cFcPsmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3)
)
_H3cFcPsmStatsTable_Object = MibTable
h3cFcPsmStatsTable = _H3cFcPsmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cFcPsmStatsTable.setStatus("current")
_H3cFcPsmStatsEntry_Object = MibTableRow
h3cFcPsmStatsEntry = _H3cFcPsmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 1, 1)
)
h3cFcPsmStatsEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmStatsEntry.setStatus("current")
_H3cFcPsmAllowedLogins_Type = Counter32
_H3cFcPsmAllowedLogins_Object = MibTableColumn
h3cFcPsmAllowedLogins = _H3cFcPsmAllowedLogins_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 1, 1, 1),
    _H3cFcPsmAllowedLogins_Type()
)
h3cFcPsmAllowedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmAllowedLogins.setStatus("current")
_H3cFcPsmDeniedLogins_Type = Counter32
_H3cFcPsmDeniedLogins_Object = MibTableColumn
h3cFcPsmDeniedLogins = _H3cFcPsmDeniedLogins_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 1, 1, 2),
    _H3cFcPsmDeniedLogins_Type()
)
h3cFcPsmDeniedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmDeniedLogins.setStatus("current")


class _H3cFcPsmStatsClear_Type(Integer32):
    """Custom type h3cFcPsmStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noop", 2))
    )


_H3cFcPsmStatsClear_Type.__name__ = "Integer32"
_H3cFcPsmStatsClear_Object = MibTableColumn
h3cFcPsmStatsClear = _H3cFcPsmStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 1, 1, 3),
    _H3cFcPsmStatsClear_Type()
)
h3cFcPsmStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcPsmStatsClear.setStatus("current")
_H3cFcPsmViolationTable_Object = MibTable
h3cFcPsmViolationTable = _H3cFcPsmViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cFcPsmViolationTable.setStatus("current")
_H3cFcPsmViolationEntry_Object = MibTableRow
h3cFcPsmViolationEntry = _H3cFcPsmViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1)
)
h3cFcPsmViolationEntry.setIndexNames(
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmEnableVsanIndex"),
    (0, "H3C-FC-PSM-MIB", "h3cFcPsmViolationIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPsmViolationEntry.setStatus("current")


class _H3cFcPsmViolationIndex_Type(Unsigned32):
    """Custom type h3cFcPsmViolationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cFcPsmViolationIndex_Type.__name__ = "Unsigned32"
_H3cFcPsmViolationIndex_Object = MibTableColumn
h3cFcPsmViolationIndex = _H3cFcPsmViolationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1, 1),
    _H3cFcPsmViolationIndex_Type()
)
h3cFcPsmViolationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcPsmViolationIndex.setStatus("current")
_H3cFcPsmLoginPWWN_Type = H3cFcNameIdOrZero
_H3cFcPsmLoginPWWN_Object = MibTableColumn
h3cFcPsmLoginPWWN = _H3cFcPsmLoginPWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1, 2),
    _H3cFcPsmLoginPWWN_Type()
)
h3cFcPsmLoginPWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmLoginPWWN.setStatus("current")
_H3cFcPsmLoginNWWN_Type = H3cFcNameIdOrZero
_H3cFcPsmLoginNWWN_Object = MibTableColumn
h3cFcPsmLoginNWWN = _H3cFcPsmLoginNWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1, 3),
    _H3cFcPsmLoginNWWN_Type()
)
h3cFcPsmLoginNWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmLoginNWWN.setStatus("current")
_H3cFcPsmLoginSWWN_Type = H3cFcNameIdOrZero
_H3cFcPsmLoginSWWN_Object = MibTableColumn
h3cFcPsmLoginSWWN = _H3cFcPsmLoginSWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1, 4),
    _H3cFcPsmLoginSWWN_Type()
)
h3cFcPsmLoginSWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmLoginSWWN.setStatus("current")
_H3cFcPsmLoginIntf_Type = InterfaceIndex
_H3cFcPsmLoginIntf_Object = MibTableColumn
h3cFcPsmLoginIntf = _H3cFcPsmLoginIntf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1, 5),
    _H3cFcPsmLoginIntf_Type()
)
h3cFcPsmLoginIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmLoginIntf.setStatus("current")
_H3cFcPsmLoginTime_Type = DateAndTime
_H3cFcPsmLoginTime_Object = MibTableColumn
h3cFcPsmLoginTime = _H3cFcPsmLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1, 6),
    _H3cFcPsmLoginTime_Type()
)
h3cFcPsmLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmLoginTime.setStatus("current")
_H3cFcPsmLoginCount_Type = Counter32
_H3cFcPsmLoginCount_Object = MibTableColumn
h3cFcPsmLoginCount = _H3cFcPsmLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 1, 3, 2, 1, 7),
    _H3cFcPsmLoginCount_Type()
)
h3cFcPsmLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPsmLoginCount.setStatus("current")

# Managed Objects groups


# Notification objects

h3cFcPsmFPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 0, 1)
)
h3cFcPsmFPortDenyNotify.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("H3C-FC-PSM-MIB", "h3cFcPsmLoginPWWN"),
        ("H3C-FC-PSM-MIB", "h3cFcPsmLoginIntf"),
        ("H3C-FC-PSM-MIB", "h3cFcPsmLoginTime"))
)
if mibBuilder.loadTexts:
    h3cFcPsmFPortDenyNotify.setStatus(
        "current"
    )

h3cFcPsmEPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 8, 0, 2)
)
h3cFcPsmEPortDenyNotify.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("H3C-FC-PSM-MIB", "h3cFcPsmLoginSWWN"),
        ("H3C-FC-PSM-MIB", "h3cFcPsmLoginIntf"),
        ("H3C-FC-PSM-MIB", "h3cFcPsmLoginTime"))
)
if mibBuilder.loadTexts:
    h3cFcPsmEPortDenyNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FC-PSM-MIB",
    **{"H3cFcPsmPortBindDevType": H3cFcPsmPortBindDevType,
       "H3cFcPsmClearEntryType": H3cFcPsmClearEntryType,
       "h3cFcPsm": h3cFcPsm,
       "h3cFcPsmNotifications": h3cFcPsmNotifications,
       "h3cFcPsmFPortDenyNotify": h3cFcPsmFPortDenyNotify,
       "h3cFcPsmEPortDenyNotify": h3cFcPsmEPortDenyNotify,
       "h3cFcPsmObjects": h3cFcPsmObjects,
       "h3cFcPsmScalarObjects": h3cFcPsmScalarObjects,
       "h3cFcPsmNotifyEnable": h3cFcPsmNotifyEnable,
       "h3cFcPsmConfiguration": h3cFcPsmConfiguration,
       "h3cFcPsmEnableTable": h3cFcPsmEnableTable,
       "h3cFcPsmEnableEntry": h3cFcPsmEnableEntry,
       "h3cFcPsmEnableVsanIndex": h3cFcPsmEnableVsanIndex,
       "h3cFcPsmEnable": h3cFcPsmEnable,
       "h3cFcPsmEnableState": h3cFcPsmEnableState,
       "h3cFcPsmConfigTable": h3cFcPsmConfigTable,
       "h3cFcPsmConfigEntry": h3cFcPsmConfigEntry,
       "h3cFcPsmIndex": h3cFcPsmIndex,
       "h3cFcPsmLoginDevType": h3cFcPsmLoginDevType,
       "h3cFcPsmLoginDev": h3cFcPsmLoginDev,
       "h3cFcPsmLoginPoint": h3cFcPsmLoginPoint,
       "h3cFcPsmRowStatus": h3cFcPsmRowStatus,
       "h3cFcPsmEnfTable": h3cFcPsmEnfTable,
       "h3cFcPsmEnfEntry": h3cFcPsmEnfEntry,
       "h3cFcPsmEnfIndex": h3cFcPsmEnfIndex,
       "h3cFcPsmEnfLoginDevType": h3cFcPsmEnfLoginDevType,
       "h3cFcPsmEnfLoginDev": h3cFcPsmEnfLoginDev,
       "h3cFcPsmEnfLoginPoint": h3cFcPsmEnfLoginPoint,
       "h3cFcPsmEnfEntryType": h3cFcPsmEnfEntryType,
       "h3cFcPsmCopyToConfigTable": h3cFcPsmCopyToConfigTable,
       "h3cFcPsmCopyToConfigEntry": h3cFcPsmCopyToConfigEntry,
       "h3cFcPsmCopyToConfig": h3cFcPsmCopyToConfig,
       "h3cFcPsmAutoLearnTable": h3cFcPsmAutoLearnTable,
       "h3cFcPsmAutoLearnEntry": h3cFcPsmAutoLearnEntry,
       "h3cFcPsmAutoLearnEnable": h3cFcPsmAutoLearnEnable,
       "h3cFcPsmClearTable": h3cFcPsmClearTable,
       "h3cFcPsmClearEntry": h3cFcPsmClearEntry,
       "h3cFcPsmClearType": h3cFcPsmClearType,
       "h3cFcPsmClearIntf": h3cFcPsmClearIntf,
       "h3cFcPsmStats": h3cFcPsmStats,
       "h3cFcPsmStatsTable": h3cFcPsmStatsTable,
       "h3cFcPsmStatsEntry": h3cFcPsmStatsEntry,
       "h3cFcPsmAllowedLogins": h3cFcPsmAllowedLogins,
       "h3cFcPsmDeniedLogins": h3cFcPsmDeniedLogins,
       "h3cFcPsmStatsClear": h3cFcPsmStatsClear,
       "h3cFcPsmViolationTable": h3cFcPsmViolationTable,
       "h3cFcPsmViolationEntry": h3cFcPsmViolationEntry,
       "h3cFcPsmViolationIndex": h3cFcPsmViolationIndex,
       "h3cFcPsmLoginPWWN": h3cFcPsmLoginPWWN,
       "h3cFcPsmLoginNWWN": h3cFcPsmLoginNWWN,
       "h3cFcPsmLoginSWWN": h3cFcPsmLoginSWWN,
       "h3cFcPsmLoginIntf": h3cFcPsmLoginIntf,
       "h3cFcPsmLoginTime": h3cFcPsmLoginTime,
       "h3cFcPsmLoginCount": h3cFcPsmLoginCount}
)
