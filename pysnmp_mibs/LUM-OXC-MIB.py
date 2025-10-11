# SNMP MIB module (LUM-OXC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-OXC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:12 2025
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

(lumModules,
 lumOxcMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumOxcMIB")

(FaultStatus,
 MgmtNameString,
 ObjectProperty,
 PortNumber,
 PortType,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "PortNumber",
    "PortType",
    "SlotNumber",
    "SubrackNumber")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumOxcMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 11)
)
if mibBuilder.loadTexts:
    lumOxcMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2008-05-12 00:00",
         "2002-03-26 00:00",
         "2001-12-11 00:00",
         "2001-10-30 00:00",
         "2001-10-11 00:00",
         "2001-09-04 00:00",
         "2001-08-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumOxcConfs_ObjectIdentity = ObjectIdentity
lumOxcConfs = _LumOxcConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1)
)
_LumOxcGroups_ObjectIdentity = ObjectIdentity
lumOxcGroups = _LumOxcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1)
)
_LumOxcCompl_ObjectIdentity = ObjectIdentity
lumOxcCompl = _LumOxcCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2)
)
_LumOxcMIBObjects_ObjectIdentity = ObjectIdentity
lumOxcMIBObjects = _LumOxcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2)
)
_OxcGeneral_ObjectIdentity = ObjectIdentity
oxcGeneral = _OxcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1)
)
_OxcGeneralTestAndIncr_Type = TestAndIncr
_OxcGeneralTestAndIncr_Object = MibScalar
oxcGeneralTestAndIncr = _OxcGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 1),
    _OxcGeneralTestAndIncr_Type()
)
oxcGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcGeneralTestAndIncr.setStatus("current")


class _OxcGeneralMibSpecVersion_Type(DisplayString):
    """Custom type oxcGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_OxcGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_OxcGeneralMibSpecVersion_Object = MibScalar
oxcGeneralMibSpecVersion = _OxcGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 2),
    _OxcGeneralMibSpecVersion_Type()
)
oxcGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcGeneralMibSpecVersion.setStatus("current")


class _OxcGeneralMibImplVersion_Type(DisplayString):
    """Custom type oxcGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_OxcGeneralMibImplVersion_Type.__name__ = "DisplayString"
_OxcGeneralMibImplVersion_Object = MibScalar
oxcGeneralMibImplVersion = _OxcGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 3),
    _OxcGeneralMibImplVersion_Type()
)
oxcGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcGeneralMibImplVersion.setStatus("current")
_OxcGeneralLastChangeTime_Type = DateAndTime
_OxcGeneralLastChangeTime_Object = MibScalar
oxcGeneralLastChangeTime = _OxcGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 4),
    _OxcGeneralLastChangeTime_Type()
)
oxcGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcGeneralLastChangeTime.setStatus("current")
_OxcGeneralStateLastChangeTime_Type = DateAndTime
_OxcGeneralStateLastChangeTime_Object = MibScalar
oxcGeneralStateLastChangeTime = _OxcGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 5),
    _OxcGeneralStateLastChangeTime_Type()
)
oxcGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcGeneralStateLastChangeTime.setStatus("current")
_OxcGeneralOxcIfTableSize_Type = Unsigned32
_OxcGeneralOxcIfTableSize_Object = MibScalar
oxcGeneralOxcIfTableSize = _OxcGeneralOxcIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 6),
    _OxcGeneralOxcIfTableSize_Type()
)
oxcGeneralOxcIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcGeneralOxcIfTableSize.setStatus("current")
_OxcGeneralOxcConfTableSize_Type = Unsigned32
_OxcGeneralOxcConfTableSize_Object = MibScalar
oxcGeneralOxcConfTableSize = _OxcGeneralOxcConfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 7),
    _OxcGeneralOxcConfTableSize_Type()
)
oxcGeneralOxcConfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcGeneralOxcConfTableSize.setStatus("current")
_OxcIfList_ObjectIdentity = ObjectIdentity
oxcIfList = _OxcIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2)
)
_OxcIfTable_Object = MibTable
oxcIfTable = _OxcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oxcIfTable.setStatus("current")
_OxcIfEntry_Object = MibTableRow
oxcIfEntry = _OxcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1)
)
oxcIfEntry.setIndexNames(
    (0, "LUM-OXC-MIB", "oxcIfIndex"),
)
if mibBuilder.loadTexts:
    oxcIfEntry.setStatus("current")


class _OxcIfIndex_Type(Unsigned32):
    """Custom type oxcIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OxcIfIndex_Type.__name__ = "Unsigned32"
_OxcIfIndex_Object = MibTableColumn
oxcIfIndex = _OxcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 1),
    _OxcIfIndex_Type()
)
oxcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfIndex.setStatus("current")
_OxcIfName_Type = MgmtNameString
_OxcIfName_Object = MibTableColumn
oxcIfName = _OxcIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 2),
    _OxcIfName_Type()
)
oxcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfName.setStatus("current")


class _OxcIfDescr_Type(DisplayString):
    """Custom type oxcIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_OxcIfDescr_Type.__name__ = "DisplayString"
_OxcIfDescr_Object = MibTableColumn
oxcIfDescr = _OxcIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 3),
    _OxcIfDescr_Type()
)
oxcIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcIfDescr.setStatus("current")
_OxcIfSubrack_Type = SubrackNumber
_OxcIfSubrack_Object = MibTableColumn
oxcIfSubrack = _OxcIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 4),
    _OxcIfSubrack_Type()
)
oxcIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfSubrack.setStatus("current")
_OxcIfSlot_Type = SlotNumber
_OxcIfSlot_Object = MibTableColumn
oxcIfSlot = _OxcIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 5),
    _OxcIfSlot_Type()
)
oxcIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfSlot.setStatus("current")
_OxcIfPort_Type = PortNumber
_OxcIfPort_Object = MibTableColumn
oxcIfPort = _OxcIfPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 6),
    _OxcIfPort_Type()
)
oxcIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfPort.setStatus("current")


class _OxcIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type oxcIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OxcIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_OxcIfInvPhysIndexOrZero_Object = MibTableColumn
oxcIfInvPhysIndexOrZero = _OxcIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 7),
    _OxcIfInvPhysIndexOrZero_Type()
)
oxcIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfInvPhysIndexOrZero.setStatus("current")
_OxcIfDirection_Type = PortType
_OxcIfDirection_Object = MibTableColumn
oxcIfDirection = _OxcIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 8),
    _OxcIfDirection_Type()
)
oxcIfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfDirection.setStatus("current")


class _OxcIfAdminStatus_Type(Integer32):
    """Custom type oxcIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("down", 1),
          ("up", 2))
    )


_OxcIfAdminStatus_Type.__name__ = "Integer32"
_OxcIfAdminStatus_Object = MibTableColumn
oxcIfAdminStatus = _OxcIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 9),
    _OxcIfAdminStatus_Type()
)
oxcIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcIfAdminStatus.setStatus("deprecated")


class _OxcIfOperStatus_Type(Integer32):
    """Custom type oxcIfOperStatus based on Integer32"""
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
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_OxcIfOperStatus_Type.__name__ = "Integer32"
_OxcIfOperStatus_Object = MibTableColumn
oxcIfOperStatus = _OxcIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 10),
    _OxcIfOperStatus_Type()
)
oxcIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfOperStatus.setStatus("current")


class _OxcIfIsReserved_Type(Integer32):
    """Custom type oxcIfIsReserved based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_OxcIfIsReserved_Type.__name__ = "Integer32"
_OxcIfIsReserved_Object = MibTableColumn
oxcIfIsReserved = _OxcIfIsReserved_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 11),
    _OxcIfIsReserved_Type()
)
oxcIfIsReserved.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oxcIfIsReserved.setStatus("current")
_OxcIfObjectProperty_Type = ObjectProperty
_OxcIfObjectProperty_Object = MibTableColumn
oxcIfObjectProperty = _OxcIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 12),
    _OxcIfObjectProperty_Type()
)
oxcIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcIfObjectProperty.setStatus("current")
_OxcConfList_ObjectIdentity = ObjectIdentity
oxcConfList = _OxcConfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3)
)
_OxcConfTable_Object = MibTable
oxcConfTable = _OxcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1)
)
if mibBuilder.loadTexts:
    oxcConfTable.setStatus("current")
_OxcConfEntry_Object = MibTableRow
oxcConfEntry = _OxcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1)
)
oxcConfEntry.setIndexNames(
    (0, "LUM-OXC-MIB", "oxcConfIndex"),
)
if mibBuilder.loadTexts:
    oxcConfEntry.setStatus("current")


class _OxcConfIndex_Type(Unsigned32):
    """Custom type oxcConfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OxcConfIndex_Type.__name__ = "Unsigned32"
_OxcConfIndex_Object = MibTableColumn
oxcConfIndex = _OxcConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 1),
    _OxcConfIndex_Type()
)
oxcConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfIndex.setStatus("current")
_OxcConfName_Type = MgmtNameString
_OxcConfName_Object = MibTableColumn
oxcConfName = _OxcConfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 2),
    _OxcConfName_Type()
)
oxcConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfName.setStatus("current")


class _OxcConfDescr_Type(DisplayString):
    """Custom type oxcConfDescr based on DisplayString"""
    defaultValue = OctetString("")


_OxcConfDescr_Type.__name__ = "DisplayString"
_OxcConfDescr_Object = MibTableColumn
oxcConfDescr = _OxcConfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 3),
    _OxcConfDescr_Type()
)
oxcConfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcConfDescr.setStatus("current")
_OxcConfSubrack_Type = SubrackNumber
_OxcConfSubrack_Object = MibTableColumn
oxcConfSubrack = _OxcConfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 4),
    _OxcConfSubrack_Type()
)
oxcConfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfSubrack.setStatus("current")
_OxcConfSlot_Type = SlotNumber
_OxcConfSlot_Object = MibTableColumn
oxcConfSlot = _OxcConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 5),
    _OxcConfSlot_Type()
)
oxcConfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfSlot.setStatus("current")
_OxcConfInPort_Type = PortNumber
_OxcConfInPort_Object = MibTableColumn
oxcConfInPort = _OxcConfInPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 6),
    _OxcConfInPort_Type()
)
oxcConfInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfInPort.setStatus("current")


class _OxcConfOutPort_Type(PortNumber):
    """Custom type oxcConfOutPort based on PortNumber"""
    defaultValue = 0


_OxcConfOutPort_Type.__name__ = "PortNumber"
_OxcConfOutPort_Object = MibTableColumn
oxcConfOutPort = _OxcConfOutPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 7),
    _OxcConfOutPort_Type()
)
oxcConfOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcConfOutPort.setStatus("current")
_OxcConfLastChangeTime_Type = DateAndTime
_OxcConfLastChangeTime_Object = MibTableColumn
oxcConfLastChangeTime = _OxcConfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 8),
    _OxcConfLastChangeTime_Type()
)
oxcConfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfLastChangeTime.setStatus("current")


class _OxcConfAdminStatus_Type(Integer32):
    """Custom type oxcConfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_OxcConfAdminStatus_Type.__name__ = "Integer32"
_OxcConfAdminStatus_Object = MibTableColumn
oxcConfAdminStatus = _OxcConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 9),
    _OxcConfAdminStatus_Type()
)
oxcConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oxcConfAdminStatus.setStatus("current")


class _OxcConfOperStatus_Type(Integer32):
    """Custom type oxcConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_OxcConfOperStatus_Type.__name__ = "Integer32"
_OxcConfOperStatus_Object = MibTableColumn
oxcConfOperStatus = _OxcConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 10),
    _OxcConfOperStatus_Type()
)
oxcConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfOperStatus.setStatus("deprecated")
_OxcConfRowStatus_Type = RowStatus
_OxcConfRowStatus_Object = MibTableColumn
oxcConfRowStatus = _OxcConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 11),
    _OxcConfRowStatus_Type()
)
oxcConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oxcConfRowStatus.setStatus("deprecated")
_OxcConfServiceFailure_Type = FaultStatus
_OxcConfServiceFailure_Object = MibTableColumn
oxcConfServiceFailure = _OxcConfServiceFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 12),
    _OxcConfServiceFailure_Type()
)
oxcConfServiceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfServiceFailure.setStatus("current")
_OxcConfObjectProperty_Type = ObjectProperty
_OxcConfObjectProperty_Object = MibTableColumn
oxcConfObjectProperty = _OxcConfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 13),
    _OxcConfObjectProperty_Type()
)
oxcConfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oxcConfObjectProperty.setStatus("current")

# Managed Objects groups

oxcGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 1)
)
oxcGeneralGroup.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralTestAndIncr"),
        ("LUM-OXC-MIB", "oxcGeneralMibSpecVersion"),
        ("LUM-OXC-MIB", "oxcGeneralMibImplVersion"),
        ("LUM-OXC-MIB", "oxcGeneralLastChangeTime"))
)
if mibBuilder.loadTexts:
    oxcGeneralGroup.setStatus("deprecated")

oxcIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 2)
)
oxcIfGroup.setObjects(
      *(("LUM-OXC-MIB", "oxcIfIndex"),
        ("LUM-OXC-MIB", "oxcIfName"),
        ("LUM-OXC-MIB", "oxcIfDescr"),
        ("LUM-OXC-MIB", "oxcIfSubrack"),
        ("LUM-OXC-MIB", "oxcIfSlot"),
        ("LUM-OXC-MIB", "oxcIfPort"),
        ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"),
        ("LUM-OXC-MIB", "oxcIfDirection"),
        ("LUM-OXC-MIB", "oxcIfAdminStatus"),
        ("LUM-OXC-MIB", "oxcIfOperStatus"))
)
if mibBuilder.loadTexts:
    oxcIfGroup.setStatus("deprecated")

oxcConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 3)
)
oxcConfGroup.setObjects(
      *(("LUM-OXC-MIB", "oxcConfIndex"),
        ("LUM-OXC-MIB", "oxcConfName"),
        ("LUM-OXC-MIB", "oxcConfDescr"),
        ("LUM-OXC-MIB", "oxcConfSubrack"),
        ("LUM-OXC-MIB", "oxcConfSlot"),
        ("LUM-OXC-MIB", "oxcConfInPort"),
        ("LUM-OXC-MIB", "oxcConfOutPort"),
        ("LUM-OXC-MIB", "oxcConfLastChangeTime"),
        ("LUM-OXC-MIB", "oxcConfAdminStatus"),
        ("LUM-OXC-MIB", "oxcConfOperStatus"),
        ("LUM-OXC-MIB", "oxcConfRowStatus"))
)
if mibBuilder.loadTexts:
    oxcConfGroup.setStatus("deprecated")

oxcIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 4)
)
oxcIfGroupV2.setObjects(
      *(("LUM-OXC-MIB", "oxcIfIndex"),
        ("LUM-OXC-MIB", "oxcIfName"),
        ("LUM-OXC-MIB", "oxcIfDescr"),
        ("LUM-OXC-MIB", "oxcIfSubrack"),
        ("LUM-OXC-MIB", "oxcIfSlot"),
        ("LUM-OXC-MIB", "oxcIfPort"),
        ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"),
        ("LUM-OXC-MIB", "oxcIfDirection"),
        ("LUM-OXC-MIB", "oxcIfOperStatus"))
)
if mibBuilder.loadTexts:
    oxcIfGroupV2.setStatus("deprecated")

oxcConfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 5)
)
oxcConfGroupV2.setObjects(
      *(("LUM-OXC-MIB", "oxcConfIndex"),
        ("LUM-OXC-MIB", "oxcConfName"),
        ("LUM-OXC-MIB", "oxcConfDescr"),
        ("LUM-OXC-MIB", "oxcConfSubrack"),
        ("LUM-OXC-MIB", "oxcConfSlot"),
        ("LUM-OXC-MIB", "oxcConfInPort"),
        ("LUM-OXC-MIB", "oxcConfOutPort"),
        ("LUM-OXC-MIB", "oxcConfLastChangeTime"),
        ("LUM-OXC-MIB", "oxcConfAdminStatus"),
        ("LUM-OXC-MIB", "oxcConfOperStatus"),
        ("LUM-OXC-MIB", "oxcConfServiceFailure"))
)
if mibBuilder.loadTexts:
    oxcConfGroupV2.setStatus("deprecated")

oxcGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 6)
)
oxcGeneralGroupV2.setObjects(
    ("LUM-OXC-MIB", "oxcGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    oxcGeneralGroupV2.setStatus("deprecated")

oxcConfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 7)
)
oxcConfGroupV3.setObjects(
      *(("LUM-OXC-MIB", "oxcConfIndex"),
        ("LUM-OXC-MIB", "oxcConfName"),
        ("LUM-OXC-MIB", "oxcConfDescr"),
        ("LUM-OXC-MIB", "oxcConfSubrack"),
        ("LUM-OXC-MIB", "oxcConfSlot"),
        ("LUM-OXC-MIB", "oxcConfInPort"),
        ("LUM-OXC-MIB", "oxcConfOutPort"),
        ("LUM-OXC-MIB", "oxcConfLastChangeTime"),
        ("LUM-OXC-MIB", "oxcConfAdminStatus"),
        ("LUM-OXC-MIB", "oxcConfServiceFailure"))
)
if mibBuilder.loadTexts:
    oxcConfGroupV3.setStatus("deprecated")

oxcGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 8)
)
oxcGeneralGroupV3.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralLastChangeTime"),
        ("LUM-OXC-MIB", "oxcGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    oxcGeneralGroupV3.setStatus("deprecated")

oxcIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 9)
)
oxcIfGroupV3.setObjects(
      *(("LUM-OXC-MIB", "oxcIfIndex"),
        ("LUM-OXC-MIB", "oxcIfName"),
        ("LUM-OXC-MIB", "oxcIfDescr"),
        ("LUM-OXC-MIB", "oxcIfSubrack"),
        ("LUM-OXC-MIB", "oxcIfSlot"),
        ("LUM-OXC-MIB", "oxcIfPort"),
        ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"),
        ("LUM-OXC-MIB", "oxcIfDirection"),
        ("LUM-OXC-MIB", "oxcIfOperStatus"),
        ("LUM-OXC-MIB", "oxcIfIsReserved"))
)
if mibBuilder.loadTexts:
    oxcIfGroupV3.setStatus("deprecated")

oxcGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 10)
)
oxcGeneralGroupV4.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralLastChangeTime"),
        ("LUM-OXC-MIB", "oxcGeneralStateLastChangeTime"),
        ("LUM-OXC-MIB", "oxcGeneralOxcIfTableSize"),
        ("LUM-OXC-MIB", "oxcGeneralOxcConfTableSize"))
)
if mibBuilder.loadTexts:
    oxcGeneralGroupV4.setStatus("current")

oxcIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 11)
)
oxcIfGroupV4.setObjects(
      *(("LUM-OXC-MIB", "oxcIfIndex"),
        ("LUM-OXC-MIB", "oxcIfName"),
        ("LUM-OXC-MIB", "oxcIfDescr"),
        ("LUM-OXC-MIB", "oxcIfSubrack"),
        ("LUM-OXC-MIB", "oxcIfSlot"),
        ("LUM-OXC-MIB", "oxcIfPort"),
        ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"),
        ("LUM-OXC-MIB", "oxcIfDirection"),
        ("LUM-OXC-MIB", "oxcIfOperStatus"),
        ("LUM-OXC-MIB", "oxcIfIsReserved"),
        ("LUM-OXC-MIB", "oxcIfObjectProperty"))
)
if mibBuilder.loadTexts:
    oxcIfGroupV4.setStatus("current")

oxcConfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 12)
)
oxcConfGroupV4.setObjects(
      *(("LUM-OXC-MIB", "oxcConfIndex"),
        ("LUM-OXC-MIB", "oxcConfName"),
        ("LUM-OXC-MIB", "oxcConfDescr"),
        ("LUM-OXC-MIB", "oxcConfSubrack"),
        ("LUM-OXC-MIB", "oxcConfSlot"),
        ("LUM-OXC-MIB", "oxcConfInPort"),
        ("LUM-OXC-MIB", "oxcConfOutPort"),
        ("LUM-OXC-MIB", "oxcConfLastChangeTime"),
        ("LUM-OXC-MIB", "oxcConfAdminStatus"),
        ("LUM-OXC-MIB", "oxcConfServiceFailure"),
        ("LUM-OXC-MIB", "oxcConfObjectProperty"))
)
if mibBuilder.loadTexts:
    oxcConfGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumOxcBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 1)
)
lumOxcBasicComplV1.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralGroup"),
        ("LUM-OXC-MIB", "oxcIfGroup"),
        ("LUM-OXC-MIB", "oxcConfGroup"))
)
if mibBuilder.loadTexts:
    lumOxcBasicComplV1.setStatus(
        "deprecated"
    )

lumOxcBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 2)
)
lumOxcBasicComplV2.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralGroup"),
        ("LUM-OXC-MIB", "oxcIfGroupV2"),
        ("LUM-OXC-MIB", "oxcConfGroupV2"))
)
if mibBuilder.loadTexts:
    lumOxcBasicComplV2.setStatus(
        "deprecated"
    )

lumOxcBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 3)
)
lumOxcBasicComplV3.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralGroupV2"),
        ("LUM-OXC-MIB", "oxcIfGroupV2"),
        ("LUM-OXC-MIB", "oxcConfGroupV2"))
)
if mibBuilder.loadTexts:
    lumOxcBasicComplV3.setStatus(
        "deprecated"
    )

lumOxcBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 4)
)
lumOxcBasicComplV4.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralGroupV2"),
        ("LUM-OXC-MIB", "oxcIfGroupV2"),
        ("LUM-OXC-MIB", "oxcConfGroupV3"))
)
if mibBuilder.loadTexts:
    lumOxcBasicComplV4.setStatus(
        "deprecated"
    )

lumOxcBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 5)
)
lumOxcBasicComplV5.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralGroupV3"),
        ("LUM-OXC-MIB", "oxcIfGroupV2"),
        ("LUM-OXC-MIB", "oxcConfGroupV3"))
)
if mibBuilder.loadTexts:
    lumOxcBasicComplV5.setStatus(
        "deprecated"
    )

lumOxcBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 6)
)
lumOxcBasicComplV6.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralGroupV4"),
        ("LUM-OXC-MIB", "oxcIfGroupV3"),
        ("LUM-OXC-MIB", "oxcConfGroupV3"))
)
if mibBuilder.loadTexts:
    lumOxcBasicComplV6.setStatus(
        "deprecated"
    )

lumOxcBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 7)
)
lumOxcBasicComplV7.setObjects(
      *(("LUM-OXC-MIB", "oxcGeneralGroupV4"),
        ("LUM-OXC-MIB", "oxcIfGroupV4"),
        ("LUM-OXC-MIB", "oxcConfGroupV4"))
)
if mibBuilder.loadTexts:
    lumOxcBasicComplV7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-OXC-MIB",
    **{"lumOxcMIBModule": lumOxcMIBModule,
       "lumOxcConfs": lumOxcConfs,
       "lumOxcGroups": lumOxcGroups,
       "oxcGeneralGroup": oxcGeneralGroup,
       "oxcIfGroup": oxcIfGroup,
       "oxcConfGroup": oxcConfGroup,
       "oxcIfGroupV2": oxcIfGroupV2,
       "oxcConfGroupV2": oxcConfGroupV2,
       "oxcGeneralGroupV2": oxcGeneralGroupV2,
       "oxcConfGroupV3": oxcConfGroupV3,
       "oxcGeneralGroupV3": oxcGeneralGroupV3,
       "oxcIfGroupV3": oxcIfGroupV3,
       "oxcGeneralGroupV4": oxcGeneralGroupV4,
       "oxcIfGroupV4": oxcIfGroupV4,
       "oxcConfGroupV4": oxcConfGroupV4,
       "lumOxcCompl": lumOxcCompl,
       "lumOxcBasicComplV1": lumOxcBasicComplV1,
       "lumOxcBasicComplV2": lumOxcBasicComplV2,
       "lumOxcBasicComplV3": lumOxcBasicComplV3,
       "lumOxcBasicComplV4": lumOxcBasicComplV4,
       "lumOxcBasicComplV5": lumOxcBasicComplV5,
       "lumOxcBasicComplV6": lumOxcBasicComplV6,
       "lumOxcBasicComplV7": lumOxcBasicComplV7,
       "lumOxcMIBObjects": lumOxcMIBObjects,
       "oxcGeneral": oxcGeneral,
       "oxcGeneralTestAndIncr": oxcGeneralTestAndIncr,
       "oxcGeneralMibSpecVersion": oxcGeneralMibSpecVersion,
       "oxcGeneralMibImplVersion": oxcGeneralMibImplVersion,
       "oxcGeneralLastChangeTime": oxcGeneralLastChangeTime,
       "oxcGeneralStateLastChangeTime": oxcGeneralStateLastChangeTime,
       "oxcGeneralOxcIfTableSize": oxcGeneralOxcIfTableSize,
       "oxcGeneralOxcConfTableSize": oxcGeneralOxcConfTableSize,
       "oxcIfList": oxcIfList,
       "oxcIfTable": oxcIfTable,
       "oxcIfEntry": oxcIfEntry,
       "oxcIfIndex": oxcIfIndex,
       "oxcIfName": oxcIfName,
       "oxcIfDescr": oxcIfDescr,
       "oxcIfSubrack": oxcIfSubrack,
       "oxcIfSlot": oxcIfSlot,
       "oxcIfPort": oxcIfPort,
       "oxcIfInvPhysIndexOrZero": oxcIfInvPhysIndexOrZero,
       "oxcIfDirection": oxcIfDirection,
       "oxcIfAdminStatus": oxcIfAdminStatus,
       "oxcIfOperStatus": oxcIfOperStatus,
       "oxcIfIsReserved": oxcIfIsReserved,
       "oxcIfObjectProperty": oxcIfObjectProperty,
       "oxcConfList": oxcConfList,
       "oxcConfTable": oxcConfTable,
       "oxcConfEntry": oxcConfEntry,
       "oxcConfIndex": oxcConfIndex,
       "oxcConfName": oxcConfName,
       "oxcConfDescr": oxcConfDescr,
       "oxcConfSubrack": oxcConfSubrack,
       "oxcConfSlot": oxcConfSlot,
       "oxcConfInPort": oxcConfInPort,
       "oxcConfOutPort": oxcConfOutPort,
       "oxcConfLastChangeTime": oxcConfLastChangeTime,
       "oxcConfAdminStatus": oxcConfAdminStatus,
       "oxcConfOperStatus": oxcConfOperStatus,
       "oxcConfRowStatus": oxcConfRowStatus,
       "oxcConfServiceFailure": oxcConfServiceFailure,
       "oxcConfObjectProperty": oxcConfObjectProperty}
)
