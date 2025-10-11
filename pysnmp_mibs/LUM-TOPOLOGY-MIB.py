# SNMP MIB module (LUM-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-TOPOLOGY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:02 2025
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
 lumTopologyMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumTopologyMIB")

(CommandString,
 LambdaFrequency,
 LambdaType,
 MgmtNameString,
 PortNumber,
 PortType,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "LambdaFrequency",
    "LambdaType",
    "MgmtNameString",
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

lumTopologyMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 10)
)
if mibBuilder.loadTexts:
    lumTopologyMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-03-15 00:00",
         "2002-09-26 00:00",
         "2001-12-11 00:00",
         "2001-11-08 00:00",
         "2001-10-26 00:00",
         "2001-10-22 00:00",
         "2001-10-11 00:00",
         "2001-08-14 00:00",
         "2001-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SegmentEndPoint(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("trunc", 1),
          ("client", 2),
          ("crossConnect", 3),
          ("incomplete", 4))
    )



class ConnSegmentDirType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("rx", 1),
          ("tx", 2),
          ("biDi", 3),
          ("unused", 4),
          ("txRx", 5))
    )



# MIB Managed Objects in the order of their OIDs

_LumTopologyConfs_ObjectIdentity = ObjectIdentity
lumTopologyConfs = _LumTopologyConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1)
)
_LumTopologyGroups_ObjectIdentity = ObjectIdentity
lumTopologyGroups = _LumTopologyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1)
)
_LumTopologyCompl_ObjectIdentity = ObjectIdentity
lumTopologyCompl = _LumTopologyCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2)
)
_LumTopologyMIBObjects_ObjectIdentity = ObjectIdentity
lumTopologyMIBObjects = _LumTopologyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2)
)
_TopoGeneral_ObjectIdentity = ObjectIdentity
topoGeneral = _TopoGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1)
)
_TopoGeneralTestAndIncr_Type = TestAndIncr
_TopoGeneralTestAndIncr_Object = MibScalar
topoGeneralTestAndIncr = _TopoGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 1),
    _TopoGeneralTestAndIncr_Type()
)
topoGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoGeneralTestAndIncr.setStatus("current")


class _TopoGeneralMibSpecVersion_Type(DisplayString):
    """Custom type topoGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_TopoGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_TopoGeneralMibSpecVersion_Object = MibScalar
topoGeneralMibSpecVersion = _TopoGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 2),
    _TopoGeneralMibSpecVersion_Type()
)
topoGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoGeneralMibSpecVersion.setStatus("current")


class _TopoGeneralMibImplVersion_Type(DisplayString):
    """Custom type topoGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_TopoGeneralMibImplVersion_Type.__name__ = "DisplayString"
_TopoGeneralMibImplVersion_Object = MibScalar
topoGeneralMibImplVersion = _TopoGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 3),
    _TopoGeneralMibImplVersion_Type()
)
topoGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoGeneralMibImplVersion.setStatus("current")
_TopoGeneralLastChangeTime_Type = DateAndTime
_TopoGeneralLastChangeTime_Object = MibScalar
topoGeneralLastChangeTime = _TopoGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 4),
    _TopoGeneralLastChangeTime_Type()
)
topoGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoGeneralLastChangeTime.setStatus("current")
_TopoGeneralStateLastChangeTime_Type = DateAndTime
_TopoGeneralStateLastChangeTime_Object = MibScalar
topoGeneralStateLastChangeTime = _TopoGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 5),
    _TopoGeneralStateLastChangeTime_Type()
)
topoGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoGeneralStateLastChangeTime.setStatus("current")
_TopoGeneralTopoClientTableSize_Type = Unsigned32
_TopoGeneralTopoClientTableSize_Object = MibScalar
topoGeneralTopoClientTableSize = _TopoGeneralTopoClientTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 6),
    _TopoGeneralTopoClientTableSize_Type()
)
topoGeneralTopoClientTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoGeneralTopoClientTableSize.setStatus("current")
_TopoGeneralTopoPeerTableSize_Type = Unsigned32
_TopoGeneralTopoPeerTableSize_Object = MibScalar
topoGeneralTopoPeerTableSize = _TopoGeneralTopoPeerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 7),
    _TopoGeneralTopoPeerTableSize_Type()
)
topoGeneralTopoPeerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoGeneralTopoPeerTableSize.setStatus("current")
_TopoGeneralTopoInternalTableSize_Type = Unsigned32
_TopoGeneralTopoInternalTableSize_Object = MibScalar
topoGeneralTopoInternalTableSize = _TopoGeneralTopoInternalTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 8),
    _TopoGeneralTopoInternalTableSize_Type()
)
topoGeneralTopoInternalTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoGeneralTopoInternalTableSize.setStatus("current")
_TopoGeneralTopoSegmentTableSize_Type = Unsigned32
_TopoGeneralTopoSegmentTableSize_Object = MibScalar
topoGeneralTopoSegmentTableSize = _TopoGeneralTopoSegmentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 1, 9),
    _TopoGeneralTopoSegmentTableSize_Type()
)
topoGeneralTopoSegmentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoGeneralTopoSegmentTableSize.setStatus("current")
_TopoIntList_ObjectIdentity = ObjectIdentity
topoIntList = _TopoIntList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2)
)
_TopoIntTable_Object = MibTable
topoIntTable = _TopoIntTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    topoIntTable.setStatus("current")
_TopoIntEntry_Object = MibTableRow
topoIntEntry = _TopoIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1)
)
topoIntEntry.setIndexNames(
    (0, "LUM-TOPOLOGY-MIB", "topoIntIndex"),
)
if mibBuilder.loadTexts:
    topoIntEntry.setStatus("current")


class _TopoIntIndex_Type(Unsigned32):
    """Custom type topoIntIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TopoIntIndex_Type.__name__ = "Unsigned32"
_TopoIntIndex_Object = MibTableColumn
topoIntIndex = _TopoIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 1),
    _TopoIntIndex_Type()
)
topoIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoIntIndex.setStatus("current")


class _TopoIntFromSubrack_Type(SubrackNumber):
    """Custom type topoIntFromSubrack based on SubrackNumber"""
    defaultValue = 0


_TopoIntFromSubrack_Type.__name__ = "SubrackNumber"
_TopoIntFromSubrack_Object = MibTableColumn
topoIntFromSubrack = _TopoIntFromSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 2),
    _TopoIntFromSubrack_Type()
)
topoIntFromSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntFromSubrack.setStatus("current")


class _TopoIntFromSlot_Type(SlotNumber):
    """Custom type topoIntFromSlot based on SlotNumber"""
    defaultValue = 0


_TopoIntFromSlot_Type.__name__ = "SlotNumber"
_TopoIntFromSlot_Object = MibTableColumn
topoIntFromSlot = _TopoIntFromSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 3),
    _TopoIntFromSlot_Type()
)
topoIntFromSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntFromSlot.setStatus("current")


class _TopoIntFromPort_Type(PortNumber):
    """Custom type topoIntFromPort based on PortNumber"""
    defaultValue = 0


_TopoIntFromPort_Type.__name__ = "PortNumber"
_TopoIntFromPort_Object = MibTableColumn
topoIntFromPort = _TopoIntFromPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 4),
    _TopoIntFromPort_Type()
)
topoIntFromPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntFromPort.setStatus("current")


class _TopoIntToSubrack_Type(SubrackNumber):
    """Custom type topoIntToSubrack based on SubrackNumber"""
    defaultValue = 0


_TopoIntToSubrack_Type.__name__ = "SubrackNumber"
_TopoIntToSubrack_Object = MibTableColumn
topoIntToSubrack = _TopoIntToSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 5),
    _TopoIntToSubrack_Type()
)
topoIntToSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntToSubrack.setStatus("current")


class _TopoIntToSlot_Type(SlotNumber):
    """Custom type topoIntToSlot based on SlotNumber"""
    defaultValue = 0


_TopoIntToSlot_Type.__name__ = "SlotNumber"
_TopoIntToSlot_Object = MibTableColumn
topoIntToSlot = _TopoIntToSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 6),
    _TopoIntToSlot_Type()
)
topoIntToSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntToSlot.setStatus("current")


class _TopoIntToPort_Type(PortNumber):
    """Custom type topoIntToPort based on PortNumber"""
    defaultValue = 0


_TopoIntToPort_Type.__name__ = "PortNumber"
_TopoIntToPort_Object = MibTableColumn
topoIntToPort = _TopoIntToPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 7),
    _TopoIntToPort_Type()
)
topoIntToPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntToPort.setStatus("current")


class _TopoIntDescr_Type(DisplayString):
    """Custom type topoIntDescr based on DisplayString"""
    defaultValue = OctetString("")


_TopoIntDescr_Type.__name__ = "DisplayString"
_TopoIntDescr_Object = MibTableColumn
topoIntDescr = _TopoIntDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 8),
    _TopoIntDescr_Type()
)
topoIntDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoIntDescr.setStatus("current")
_TopoIntDirection_Type = PortType
_TopoIntDirection_Object = MibTableColumn
topoIntDirection = _TopoIntDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 9),
    _TopoIntDirection_Type()
)
topoIntDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoIntDirection.setStatus("deprecated")
_TopoIntRowStatus_Type = RowStatus
_TopoIntRowStatus_Object = MibTableColumn
topoIntRowStatus = _TopoIntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 10),
    _TopoIntRowStatus_Type()
)
topoIntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntRowStatus.setStatus("current")
_TopoIntName_Type = DisplayString
_TopoIntName_Object = MibTableColumn
topoIntName = _TopoIntName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 11),
    _TopoIntName_Type()
)
topoIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoIntName.setStatus("current")


class _TopoIntFromIfNo_Type(PortNumber):
    """Custom type topoIntFromIfNo based on PortNumber"""
    defaultValue = 0


_TopoIntFromIfNo_Type.__name__ = "PortNumber"
_TopoIntFromIfNo_Object = MibTableColumn
topoIntFromIfNo = _TopoIntFromIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 12),
    _TopoIntFromIfNo_Type()
)
topoIntFromIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntFromIfNo.setStatus("current")


class _TopoIntToIfNo_Type(PortNumber):
    """Custom type topoIntToIfNo based on PortNumber"""
    defaultValue = 0


_TopoIntToIfNo_Type.__name__ = "PortNumber"
_TopoIntToIfNo_Object = MibTableColumn
topoIntToIfNo = _TopoIntToIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 2, 1, 1, 13),
    _TopoIntToIfNo_Type()
)
topoIntToIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoIntToIfNo.setStatus("current")
_TopoPeerList_ObjectIdentity = ObjectIdentity
topoPeerList = _TopoPeerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3)
)
_TopoPeerTable_Object = MibTable
topoPeerTable = _TopoPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    topoPeerTable.setStatus("current")
_TopoPeerEntry_Object = MibTableRow
topoPeerEntry = _TopoPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1)
)
topoPeerEntry.setIndexNames(
    (0, "LUM-TOPOLOGY-MIB", "topoPeerIndex"),
)
if mibBuilder.loadTexts:
    topoPeerEntry.setStatus("current")


class _TopoPeerIndex_Type(Unsigned32):
    """Custom type topoPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TopoPeerIndex_Type.__name__ = "Unsigned32"
_TopoPeerIndex_Object = MibTableColumn
topoPeerIndex = _TopoPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 1),
    _TopoPeerIndex_Type()
)
topoPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoPeerIndex.setStatus("current")


class _TopoPeerLocalSubrack_Type(SubrackNumber):
    """Custom type topoPeerLocalSubrack based on SubrackNumber"""
    defaultValue = 0


_TopoPeerLocalSubrack_Type.__name__ = "SubrackNumber"
_TopoPeerLocalSubrack_Object = MibTableColumn
topoPeerLocalSubrack = _TopoPeerLocalSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 2),
    _TopoPeerLocalSubrack_Type()
)
topoPeerLocalSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerLocalSubrack.setStatus("current")


class _TopoPeerLocalSlot_Type(SlotNumber):
    """Custom type topoPeerLocalSlot based on SlotNumber"""
    defaultValue = 0


_TopoPeerLocalSlot_Type.__name__ = "SlotNumber"
_TopoPeerLocalSlot_Object = MibTableColumn
topoPeerLocalSlot = _TopoPeerLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 3),
    _TopoPeerLocalSlot_Type()
)
topoPeerLocalSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerLocalSlot.setStatus("current")


class _TopoPeerLocalPort_Type(PortNumber):
    """Custom type topoPeerLocalPort based on PortNumber"""
    defaultValue = 0


_TopoPeerLocalPort_Type.__name__ = "PortNumber"
_TopoPeerLocalPort_Object = MibTableColumn
topoPeerLocalPort = _TopoPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 4),
    _TopoPeerLocalPort_Type()
)
topoPeerLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerLocalPort.setStatus("current")


class _TopoPeerRemoteIpAddress_Type(DisplayString):
    """Custom type topoPeerRemoteIpAddress based on DisplayString"""
    defaultValue = OctetString("")


_TopoPeerRemoteIpAddress_Type.__name__ = "DisplayString"
_TopoPeerRemoteIpAddress_Object = MibTableColumn
topoPeerRemoteIpAddress = _TopoPeerRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 5),
    _TopoPeerRemoteIpAddress_Type()
)
topoPeerRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoPeerRemoteIpAddress.setStatus("current")


class _TopoPeerRemoteSubrack_Type(SubrackNumber):
    """Custom type topoPeerRemoteSubrack based on SubrackNumber"""
    defaultValue = 0


_TopoPeerRemoteSubrack_Type.__name__ = "SubrackNumber"
_TopoPeerRemoteSubrack_Object = MibTableColumn
topoPeerRemoteSubrack = _TopoPeerRemoteSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 6),
    _TopoPeerRemoteSubrack_Type()
)
topoPeerRemoteSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerRemoteSubrack.setStatus("current")


class _TopoPeerRemoteSlot_Type(SlotNumber):
    """Custom type topoPeerRemoteSlot based on SlotNumber"""
    defaultValue = 0


_TopoPeerRemoteSlot_Type.__name__ = "SlotNumber"
_TopoPeerRemoteSlot_Object = MibTableColumn
topoPeerRemoteSlot = _TopoPeerRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 7),
    _TopoPeerRemoteSlot_Type()
)
topoPeerRemoteSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerRemoteSlot.setStatus("current")


class _TopoPeerRemotePort_Type(PortNumber):
    """Custom type topoPeerRemotePort based on PortNumber"""
    defaultValue = 0


_TopoPeerRemotePort_Type.__name__ = "PortNumber"
_TopoPeerRemotePort_Object = MibTableColumn
topoPeerRemotePort = _TopoPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 8),
    _TopoPeerRemotePort_Type()
)
topoPeerRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerRemotePort.setStatus("current")
_TopoPeerDescr_Type = DisplayString
_TopoPeerDescr_Object = MibTableColumn
topoPeerDescr = _TopoPeerDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 9),
    _TopoPeerDescr_Type()
)
topoPeerDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoPeerDescr.setStatus("current")
_TopoPeerDirection_Type = PortType
_TopoPeerDirection_Object = MibTableColumn
topoPeerDirection = _TopoPeerDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 10),
    _TopoPeerDirection_Type()
)
topoPeerDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoPeerDirection.setStatus("deprecated")
_TopoPeerRowStatus_Type = RowStatus
_TopoPeerRowStatus_Object = MibTableColumn
topoPeerRowStatus = _TopoPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 11),
    _TopoPeerRowStatus_Type()
)
topoPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerRowStatus.setStatus("current")
_TopoPeerName_Type = DisplayString
_TopoPeerName_Object = MibTableColumn
topoPeerName = _TopoPeerName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 12),
    _TopoPeerName_Type()
)
topoPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoPeerName.setStatus("current")


class _TopoPeerLinkAttenuation_Type(Unsigned32):
    """Custom type topoPeerLinkAttenuation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TopoPeerLinkAttenuation_Type.__name__ = "Unsigned32"
_TopoPeerLinkAttenuation_Object = MibTableColumn
topoPeerLinkAttenuation = _TopoPeerLinkAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 13),
    _TopoPeerLinkAttenuation_Type()
)
topoPeerLinkAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoPeerLinkAttenuation.setStatus("current")
_TopoPeerLocalLabel_Type = DisplayString
_TopoPeerLocalLabel_Object = MibTableColumn
topoPeerLocalLabel = _TopoPeerLocalLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 14),
    _TopoPeerLocalLabel_Type()
)
topoPeerLocalLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoPeerLocalLabel.setStatus("current")
_TopoPeerRemoteLabel_Type = DisplayString
_TopoPeerRemoteLabel_Object = MibTableColumn
topoPeerRemoteLabel = _TopoPeerRemoteLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 15),
    _TopoPeerRemoteLabel_Type()
)
topoPeerRemoteLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoPeerRemoteLabel.setStatus("current")


class _TopoPeerLocalIfNo_Type(PortNumber):
    """Custom type topoPeerLocalIfNo based on PortNumber"""
    defaultValue = 0


_TopoPeerLocalIfNo_Type.__name__ = "PortNumber"
_TopoPeerLocalIfNo_Object = MibTableColumn
topoPeerLocalIfNo = _TopoPeerLocalIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 16),
    _TopoPeerLocalIfNo_Type()
)
topoPeerLocalIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerLocalIfNo.setStatus("current")


class _TopoPeerRemoteIfNo_Type(PortNumber):
    """Custom type topoPeerRemoteIfNo based on PortNumber"""
    defaultValue = 0


_TopoPeerRemoteIfNo_Type.__name__ = "PortNumber"
_TopoPeerRemoteIfNo_Object = MibTableColumn
topoPeerRemoteIfNo = _TopoPeerRemoteIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 3, 1, 1, 17),
    _TopoPeerRemoteIfNo_Type()
)
topoPeerRemoteIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoPeerRemoteIfNo.setStatus("current")
_TopoClientList_ObjectIdentity = ObjectIdentity
topoClientList = _TopoClientList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4)
)
_TopoClientTable_Object = MibTable
topoClientTable = _TopoClientTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1)
)
if mibBuilder.loadTexts:
    topoClientTable.setStatus("current")
_TopoClientEntry_Object = MibTableRow
topoClientEntry = _TopoClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1)
)
topoClientEntry.setIndexNames(
    (0, "LUM-TOPOLOGY-MIB", "topoClientIndex"),
)
if mibBuilder.loadTexts:
    topoClientEntry.setStatus("current")


class _TopoClientIndex_Type(Unsigned32):
    """Custom type topoClientIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TopoClientIndex_Type.__name__ = "Unsigned32"
_TopoClientIndex_Object = MibTableColumn
topoClientIndex = _TopoClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 1),
    _TopoClientIndex_Type()
)
topoClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoClientIndex.setStatus("current")


class _TopoClientLocalInSubrack_Type(SubrackNumber):
    """Custom type topoClientLocalInSubrack based on SubrackNumber"""
    defaultValue = 0


_TopoClientLocalInSubrack_Type.__name__ = "SubrackNumber"
_TopoClientLocalInSubrack_Object = MibTableColumn
topoClientLocalInSubrack = _TopoClientLocalInSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 2),
    _TopoClientLocalInSubrack_Type()
)
topoClientLocalInSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalInSubrack.setStatus("current")


class _TopoClientLocalInSlot_Type(SlotNumber):
    """Custom type topoClientLocalInSlot based on SlotNumber"""
    defaultValue = 0


_TopoClientLocalInSlot_Type.__name__ = "SlotNumber"
_TopoClientLocalInSlot_Object = MibTableColumn
topoClientLocalInSlot = _TopoClientLocalInSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 3),
    _TopoClientLocalInSlot_Type()
)
topoClientLocalInSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalInSlot.setStatus("current")


class _TopoClientLocalInPort_Type(PortNumber):
    """Custom type topoClientLocalInPort based on PortNumber"""
    defaultValue = 0


_TopoClientLocalInPort_Type.__name__ = "PortNumber"
_TopoClientLocalInPort_Object = MibTableColumn
topoClientLocalInPort = _TopoClientLocalInPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 4),
    _TopoClientLocalInPort_Type()
)
topoClientLocalInPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalInPort.setStatus("current")


class _TopoClientRemoteIpAddress_Type(DisplayString):
    """Custom type topoClientRemoteIpAddress based on DisplayString"""
    defaultValue = OctetString("")


_TopoClientRemoteIpAddress_Type.__name__ = "DisplayString"
_TopoClientRemoteIpAddress_Object = MibTableColumn
topoClientRemoteIpAddress = _TopoClientRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 5),
    _TopoClientRemoteIpAddress_Type()
)
topoClientRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoClientRemoteIpAddress.setStatus("current")


class _TopoClientRemoteIfIndex_Type(Unsigned32):
    """Custom type topoClientRemoteIfIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TopoClientRemoteIfIndex_Type.__name__ = "Unsigned32"
_TopoClientRemoteIfIndex_Object = MibTableColumn
topoClientRemoteIfIndex = _TopoClientRemoteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 6),
    _TopoClientRemoteIfIndex_Type()
)
topoClientRemoteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoClientRemoteIfIndex.setStatus("current")


class _TopoClientDescr_Type(DisplayString):
    """Custom type topoClientDescr based on DisplayString"""
    defaultValue = OctetString("")


_TopoClientDescr_Type.__name__ = "DisplayString"
_TopoClientDescr_Object = MibTableColumn
topoClientDescr = _TopoClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 7),
    _TopoClientDescr_Type()
)
topoClientDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoClientDescr.setStatus("current")
_TopoClientDirection_Type = PortType
_TopoClientDirection_Object = MibTableColumn
topoClientDirection = _TopoClientDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 8),
    _TopoClientDirection_Type()
)
topoClientDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoClientDirection.setStatus("deprecated")
_TopoClientRowStatus_Type = RowStatus
_TopoClientRowStatus_Object = MibTableColumn
topoClientRowStatus = _TopoClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 9),
    _TopoClientRowStatus_Type()
)
topoClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientRowStatus.setStatus("current")
_TopoClientName_Type = DisplayString
_TopoClientName_Object = MibTableColumn
topoClientName = _TopoClientName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 10),
    _TopoClientName_Type()
)
topoClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoClientName.setStatus("current")


class _TopoClientLocalOutSubrack_Type(SubrackNumber):
    """Custom type topoClientLocalOutSubrack based on SubrackNumber"""
    defaultValue = 0


_TopoClientLocalOutSubrack_Type.__name__ = "SubrackNumber"
_TopoClientLocalOutSubrack_Object = MibTableColumn
topoClientLocalOutSubrack = _TopoClientLocalOutSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 11),
    _TopoClientLocalOutSubrack_Type()
)
topoClientLocalOutSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalOutSubrack.setStatus("current")


class _TopoClientLocalOutSlot_Type(SlotNumber):
    """Custom type topoClientLocalOutSlot based on SlotNumber"""
    defaultValue = 0


_TopoClientLocalOutSlot_Type.__name__ = "SlotNumber"
_TopoClientLocalOutSlot_Object = MibTableColumn
topoClientLocalOutSlot = _TopoClientLocalOutSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 12),
    _TopoClientLocalOutSlot_Type()
)
topoClientLocalOutSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalOutSlot.setStatus("current")


class _TopoClientLocalOutPort_Type(PortNumber):
    """Custom type topoClientLocalOutPort based on PortNumber"""
    defaultValue = 0


_TopoClientLocalOutPort_Type.__name__ = "PortNumber"
_TopoClientLocalOutPort_Object = MibTableColumn
topoClientLocalOutPort = _TopoClientLocalOutPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 13),
    _TopoClientLocalOutPort_Type()
)
topoClientLocalOutPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalOutPort.setStatus("current")


class _TopoClientChannelId_Type(Unsigned32):
    """Custom type topoClientChannelId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TopoClientChannelId_Type.__name__ = "Unsigned32"
_TopoClientChannelId_Object = MibTableColumn
topoClientChannelId = _TopoClientChannelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 14),
    _TopoClientChannelId_Type()
)
topoClientChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientChannelId.setStatus("current")


class _TopoClientInterfaceRepresentation_Type(Unsigned32):
    """Custom type topoClientInterfaceRepresentation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TopoClientInterfaceRepresentation_Type.__name__ = "Unsigned32"
_TopoClientInterfaceRepresentation_Object = MibTableColumn
topoClientInterfaceRepresentation = _TopoClientInterfaceRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 15),
    _TopoClientInterfaceRepresentation_Type()
)
topoClientInterfaceRepresentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientInterfaceRepresentation.setStatus("current")


class _TopoClientLocalOutIfNo_Type(PortNumber):
    """Custom type topoClientLocalOutIfNo based on PortNumber"""
    defaultValue = 0


_TopoClientLocalOutIfNo_Type.__name__ = "PortNumber"
_TopoClientLocalOutIfNo_Object = MibTableColumn
topoClientLocalOutIfNo = _TopoClientLocalOutIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 16),
    _TopoClientLocalOutIfNo_Type()
)
topoClientLocalOutIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalOutIfNo.setStatus("current")


class _TopoClientLocalInIfNo_Type(PortNumber):
    """Custom type topoClientLocalInIfNo based on PortNumber"""
    defaultValue = 0


_TopoClientLocalInIfNo_Type.__name__ = "PortNumber"
_TopoClientLocalInIfNo_Object = MibTableColumn
topoClientLocalInIfNo = _TopoClientLocalInIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 4, 1, 1, 17),
    _TopoClientLocalInIfNo_Type()
)
topoClientLocalInIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    topoClientLocalInIfNo.setStatus("current")
_TopoSegmentList_ObjectIdentity = ObjectIdentity
topoSegmentList = _TopoSegmentList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5)
)
_TopoSegmentTable_Object = MibTable
topoSegmentTable = _TopoSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1)
)
if mibBuilder.loadTexts:
    topoSegmentTable.setStatus("current")
_TopoSegmentEntry_Object = MibTableRow
topoSegmentEntry = _TopoSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1)
)
topoSegmentEntry.setIndexNames(
    (0, "LUM-TOPOLOGY-MIB", "topoSegmentIndex"),
)
if mibBuilder.loadTexts:
    topoSegmentEntry.setStatus("current")


class _TopoSegmentIndex_Type(Unsigned32):
    """Custom type topoSegmentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TopoSegmentIndex_Type.__name__ = "Unsigned32"
_TopoSegmentIndex_Object = MibTableColumn
topoSegmentIndex = _TopoSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 1),
    _TopoSegmentIndex_Type()
)
topoSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentIndex.setStatus("current")
_TopoSegmentName_Type = MgmtNameString
_TopoSegmentName_Object = MibTableColumn
topoSegmentName = _TopoSegmentName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 2),
    _TopoSegmentName_Type()
)
topoSegmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentName.setStatus("current")
_TopoSegmentInSubrack_Type = SubrackNumber
_TopoSegmentInSubrack_Object = MibTableColumn
topoSegmentInSubrack = _TopoSegmentInSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 3),
    _TopoSegmentInSubrack_Type()
)
topoSegmentInSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentInSubrack.setStatus("current")
_TopoSegmentInSlot_Type = SlotNumber
_TopoSegmentInSlot_Object = MibTableColumn
topoSegmentInSlot = _TopoSegmentInSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 4),
    _TopoSegmentInSlot_Type()
)
topoSegmentInSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentInSlot.setStatus("current")
_TopoSegmentInPort_Type = PortNumber
_TopoSegmentInPort_Object = MibTableColumn
topoSegmentInPort = _TopoSegmentInPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 5),
    _TopoSegmentInPort_Type()
)
topoSegmentInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentInPort.setStatus("current")
_TopoSegmentOutSubrack_Type = SubrackNumber
_TopoSegmentOutSubrack_Object = MibTableColumn
topoSegmentOutSubrack = _TopoSegmentOutSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 6),
    _TopoSegmentOutSubrack_Type()
)
topoSegmentOutSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentOutSubrack.setStatus("current")
_TopoSegmentOutSlot_Type = SlotNumber
_TopoSegmentOutSlot_Object = MibTableColumn
topoSegmentOutSlot = _TopoSegmentOutSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 7),
    _TopoSegmentOutSlot_Type()
)
topoSegmentOutSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentOutSlot.setStatus("current")
_TopoSegmentOutPort_Type = PortNumber
_TopoSegmentOutPort_Object = MibTableColumn
topoSegmentOutPort = _TopoSegmentOutPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 8),
    _TopoSegmentOutPort_Type()
)
topoSegmentOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentOutPort.setStatus("current")
_TopoSegmentFrequencyType_Type = LambdaType
_TopoSegmentFrequencyType_Object = MibTableColumn
topoSegmentFrequencyType = _TopoSegmentFrequencyType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 9),
    _TopoSegmentFrequencyType_Type()
)
topoSegmentFrequencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentFrequencyType.setStatus("current")
_TopoSegmentFrequency_Type = LambdaFrequency
_TopoSegmentFrequency_Object = MibTableColumn
topoSegmentFrequency = _TopoSegmentFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 10),
    _TopoSegmentFrequency_Type()
)
topoSegmentFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentFrequency.setStatus("current")
_TopoSegmentSubChannelId_Type = Unsigned32
_TopoSegmentSubChannelId_Object = MibTableColumn
topoSegmentSubChannelId = _TopoSegmentSubChannelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 11),
    _TopoSegmentSubChannelId_Type()
)
topoSegmentSubChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentSubChannelId.setStatus("current")
_TopoSegmentBegin_Type = SegmentEndPoint
_TopoSegmentBegin_Object = MibTableColumn
topoSegmentBegin = _TopoSegmentBegin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 12),
    _TopoSegmentBegin_Type()
)
topoSegmentBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentBegin.setStatus("current")
_TopoSegmentType_Type = SegmentEndPoint
_TopoSegmentType_Object = MibTableColumn
topoSegmentType = _TopoSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 13),
    _TopoSegmentType_Type()
)
topoSegmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentType.setStatus("current")
_TopoSegmentInEntityId_Type = Unsigned32
_TopoSegmentInEntityId_Object = MibTableColumn
topoSegmentInEntityId = _TopoSegmentInEntityId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 14),
    _TopoSegmentInEntityId_Type()
)
topoSegmentInEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentInEntityId.setStatus("current")
_TopoSegmentOutEntityId_Type = Unsigned32
_TopoSegmentOutEntityId_Object = MibTableColumn
topoSegmentOutEntityId = _TopoSegmentOutEntityId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 15),
    _TopoSegmentOutEntityId_Type()
)
topoSegmentOutEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentOutEntityId.setStatus("current")
_TopoSegmentEntityList_Type = DisplayString
_TopoSegmentEntityList_Object = MibTableColumn
topoSegmentEntityList = _TopoSegmentEntityList_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 16),
    _TopoSegmentEntityList_Type()
)
topoSegmentEntityList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentEntityList.setStatus("current")
_TopoSegmentObjectList_Type = DisplayString
_TopoSegmentObjectList_Object = MibTableColumn
topoSegmentObjectList = _TopoSegmentObjectList_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 17),
    _TopoSegmentObjectList_Type()
)
topoSegmentObjectList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentObjectList.setStatus("current")
_TopoSegmentDirection_Type = ConnSegmentDirType
_TopoSegmentDirection_Object = MibTableColumn
topoSegmentDirection = _TopoSegmentDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 18),
    _TopoSegmentDirection_Type()
)
topoSegmentDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentDirection.setStatus("current")
_TopoSegmentEntryPointsCommand_Type = CommandString
_TopoSegmentEntryPointsCommand_Object = MibTableColumn
topoSegmentEntryPointsCommand = _TopoSegmentEntryPointsCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 19),
    _TopoSegmentEntryPointsCommand_Type()
)
topoSegmentEntryPointsCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentEntryPointsCommand.setStatus("current")
_TopoSegmentSubSegmentsCommand_Type = CommandString
_TopoSegmentSubSegmentsCommand_Object = MibTableColumn
topoSegmentSubSegmentsCommand = _TopoSegmentSubSegmentsCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 20),
    _TopoSegmentSubSegmentsCommand_Type()
)
topoSegmentSubSegmentsCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentSubSegmentsCommand.setStatus("current")
_TopoSegmentUniqId_Type = Unsigned32
_TopoSegmentUniqId_Object = MibTableColumn
topoSegmentUniqId = _TopoSegmentUniqId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 2, 5, 1, 1, 21),
    _TopoSegmentUniqId_Type()
)
topoSegmentUniqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoSegmentUniqId.setStatus("current")

# Managed Objects groups

topoGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 1)
)
topoGeneralGroup.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralTestAndIncr"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralMibSpecVersion"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralMibImplVersion"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralLastChangeTime"))
)
if mibBuilder.loadTexts:
    topoGeneralGroup.setStatus("deprecated")

topoIntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 2)
)
topoIntGroup.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoIntIndex"),
        ("LUM-TOPOLOGY-MIB", "topoIntName"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntToPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntDescr"),
        ("LUM-TOPOLOGY-MIB", "topoIntDirection"),
        ("LUM-TOPOLOGY-MIB", "topoIntRowStatus"))
)
if mibBuilder.loadTexts:
    topoIntGroup.setStatus("deprecated")

topoPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 3)
)
topoPeerGroup.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoPeerIndex"),
        ("LUM-TOPOLOGY-MIB", "topoPeerName"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalPort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemotePort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerDescr"),
        ("LUM-TOPOLOGY-MIB", "topoPeerDirection"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRowStatus"))
)
if mibBuilder.loadTexts:
    topoPeerGroup.setStatus("deprecated")

topoClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 4)
)
topoClientGroup.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoClientIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientName"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIfIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientDescr"),
        ("LUM-TOPOLOGY-MIB", "topoClientDirection"),
        ("LUM-TOPOLOGY-MIB", "topoClientRowStatus"))
)
if mibBuilder.loadTexts:
    topoClientGroup.setStatus("deprecated")

topoGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 5)
)
topoGeneralGroupV2.setObjects(
    ("LUM-TOPOLOGY-MIB", "topoGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    topoGeneralGroupV2.setStatus("deprecated")

topoIntGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 6)
)
topoIntGroupV2.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoIntIndex"),
        ("LUM-TOPOLOGY-MIB", "topoIntName"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntToPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntDescr"),
        ("LUM-TOPOLOGY-MIB", "topoIntRowStatus"))
)
if mibBuilder.loadTexts:
    topoIntGroupV2.setStatus("deprecated")

topoPeerGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 7)
)
topoPeerGroupV2.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoPeerIndex"),
        ("LUM-TOPOLOGY-MIB", "topoPeerName"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalPort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemotePort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerDescr"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRowStatus"))
)
if mibBuilder.loadTexts:
    topoPeerGroupV2.setStatus("deprecated")

topoClientGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 8)
)
topoClientGroupV2.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoClientIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientName"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIfIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientDescr"),
        ("LUM-TOPOLOGY-MIB", "topoClientRowStatus"))
)
if mibBuilder.loadTexts:
    topoClientGroupV2.setStatus("deprecated")

topoClientGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 9)
)
topoClientGroupV3.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoClientIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientName"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIfIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientDescr"),
        ("LUM-TOPOLOGY-MIB", "topoClientRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutPort"))
)
if mibBuilder.loadTexts:
    topoClientGroupV3.setStatus("deprecated")

topoGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 10)
)
topoGeneralGroupV3.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralLastChangeTime"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    topoGeneralGroupV3.setStatus("deprecated")

topoClientGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 11)
)
topoClientGroupV4.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoClientIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientName"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIfIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientDescr"),
        ("LUM-TOPOLOGY-MIB", "topoClientRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientChannelId"))
)
if mibBuilder.loadTexts:
    topoClientGroupV4.setStatus("deprecated")

topoPeerGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 12)
)
topoPeerGroupV3.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoPeerIndex"),
        ("LUM-TOPOLOGY-MIB", "topoPeerName"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalPort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemotePort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerDescr"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLinkAttenuation"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalLabel"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteLabel"))
)
if mibBuilder.loadTexts:
    topoPeerGroupV3.setStatus("deprecated")

topoSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 13)
)
topoSegmentGroup.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoSegmentIndex"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentName"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInPort"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutSlot"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutPort"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentFrequencyType"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentFrequency"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentSubChannelId"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentBegin"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInEntityId"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutEntityId"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentEntityList"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentObjectList"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentDirection"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentEntryPointsCommand"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentSubSegmentsCommand"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentUniqId"))
)
if mibBuilder.loadTexts:
    topoSegmentGroup.setStatus("deprecated")

topoGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 14)
)
topoGeneralGroupV4.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralLastChangeTime"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralStateLastChangeTime"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralTopoClientTableSize"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralTopoPeerTableSize"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralTopoInternalTableSize"),
        ("LUM-TOPOLOGY-MIB", "topoGeneralTopoSegmentTableSize"))
)
if mibBuilder.loadTexts:
    topoGeneralGroupV4.setStatus("current")

topoSegmentGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 15)
)
topoSegmentGroupV2.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoSegmentIndex"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentName"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInPort"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutSlot"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutPort"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentFrequencyType"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentFrequency"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentSubChannelId"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentBegin"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentType"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentInEntityId"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentOutEntityId"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentEntityList"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentObjectList"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentDirection"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentEntryPointsCommand"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentSubSegmentsCommand"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentUniqId"))
)
if mibBuilder.loadTexts:
    topoSegmentGroupV2.setStatus("current")

topoClientGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 16)
)
topoClientGroupV5.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoClientIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientName"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIfIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientDescr"),
        ("LUM-TOPOLOGY-MIB", "topoClientRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientChannelId"),
        ("LUM-TOPOLOGY-MIB", "topoClientInterfaceRepresentation"))
)
if mibBuilder.loadTexts:
    topoClientGroupV5.setStatus("deprecated")

topoPeerGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 17)
)
topoPeerGroupV4.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoPeerIndex"),
        ("LUM-TOPOLOGY-MIB", "topoPeerName"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalPort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemotePort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerDescr"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLinkAttenuation"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalLabel"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteLabel"))
)
if mibBuilder.loadTexts:
    topoPeerGroupV4.setStatus("deprecated")

topoIntGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 18)
)
topoIntGroupV3.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoIntIndex"),
        ("LUM-TOPOLOGY-MIB", "topoIntName"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntToPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntDescr"),
        ("LUM-TOPOLOGY-MIB", "topoIntRowStatus"))
)
if mibBuilder.loadTexts:
    topoIntGroupV3.setStatus("deprecated")

topoClientGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 19)
)
topoClientGroupV6.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoClientIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientName"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoClientRemoteIfIndex"),
        ("LUM-TOPOLOGY-MIB", "topoClientDescr"),
        ("LUM-TOPOLOGY-MIB", "topoClientRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutSlot"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutPort"),
        ("LUM-TOPOLOGY-MIB", "topoClientChannelId"),
        ("LUM-TOPOLOGY-MIB", "topoClientInterfaceRepresentation"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalOutIfNo"),
        ("LUM-TOPOLOGY-MIB", "topoClientLocalInIfNo"))
)
if mibBuilder.loadTexts:
    topoClientGroupV6.setStatus("current")

topoIntGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 20)
)
topoIntGroupV4.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoIntIndex"),
        ("LUM-TOPOLOGY-MIB", "topoIntName"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoIntToSlot"),
        ("LUM-TOPOLOGY-MIB", "topoIntToPort"),
        ("LUM-TOPOLOGY-MIB", "topoIntDescr"),
        ("LUM-TOPOLOGY-MIB", "topoIntRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoIntFromIfNo"),
        ("LUM-TOPOLOGY-MIB", "topoIntToIfNo"))
)
if mibBuilder.loadTexts:
    topoIntGroupV4.setStatus("current")

topoPeerGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 1, 21)
)
topoPeerGroupV5.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoPeerIndex"),
        ("LUM-TOPOLOGY-MIB", "topoPeerName"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalPort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteIpAddress"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSubrack"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteSlot"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemotePort"),
        ("LUM-TOPOLOGY-MIB", "topoPeerDescr"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRowStatus"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLinkAttenuation"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalLabel"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteLabel"),
        ("LUM-TOPOLOGY-MIB", "topoPeerLocalIfNo"),
        ("LUM-TOPOLOGY-MIB", "topoPeerRemoteIfNo"))
)
if mibBuilder.loadTexts:
    topoPeerGroupV5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumTopoBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 1)
)
lumTopoBasicComplV1.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroup"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroup"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroup"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroup"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV1.setStatus(
        "deprecated"
    )

lumTopoBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 2)
)
lumTopoBasicComplV2.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroup"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroup"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroup"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV2.setStatus(
        "deprecated"
    )

lumTopoBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 3)
)
lumTopoBasicComplV3.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV2"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV3.setStatus(
        "deprecated"
    )

lumTopoBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 4)
)
lumTopoBasicComplV4.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV3"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV4.setStatus(
        "deprecated"
    )

lumTopoBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 5)
)
lumTopoBasicComplV5.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV3"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV3"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV5.setStatus(
        "deprecated"
    )

lumTopoBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 6)
)
lumTopoBasicComplV6.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV3"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV4"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV6.setStatus(
        "deprecated"
    )

lumTopoBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 7)
)
lumTopoBasicComplV7.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV3"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV3"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV4"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV7.setStatus(
        "deprecated"
    )

lumTopoBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 8)
)
lumTopoBasicComplV8.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV3"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentGroup"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV8.setStatus(
        "deprecated"
    )

lumTopoBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 9)
)
lumTopoBasicComplV9.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV2"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV3"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentGroupV2"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV9.setStatus(
        "deprecated"
    )

lumTopoBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 10)
)
lumTopoBasicComplV10.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV3"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV5"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentGroupV2"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV10.setStatus(
        "deprecated"
    )

lumTopoBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8, 1, 2, 11)
)
lumTopoBasicComplV11.setObjects(
      *(("LUM-TOPOLOGY-MIB", "topoGeneralGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoIntGroupV4"),
        ("LUM-TOPOLOGY-MIB", "topoPeerGroupV5"),
        ("LUM-TOPOLOGY-MIB", "topoClientGroupV6"),
        ("LUM-TOPOLOGY-MIB", "topoSegmentGroupV2"))
)
if mibBuilder.loadTexts:
    lumTopoBasicComplV11.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-TOPOLOGY-MIB",
    **{"SegmentEndPoint": SegmentEndPoint,
       "ConnSegmentDirType": ConnSegmentDirType,
       "lumTopologyMIBModule": lumTopologyMIBModule,
       "lumTopologyConfs": lumTopologyConfs,
       "lumTopologyGroups": lumTopologyGroups,
       "topoGeneralGroup": topoGeneralGroup,
       "topoIntGroup": topoIntGroup,
       "topoPeerGroup": topoPeerGroup,
       "topoClientGroup": topoClientGroup,
       "topoGeneralGroupV2": topoGeneralGroupV2,
       "topoIntGroupV2": topoIntGroupV2,
       "topoPeerGroupV2": topoPeerGroupV2,
       "topoClientGroupV2": topoClientGroupV2,
       "topoClientGroupV3": topoClientGroupV3,
       "topoGeneralGroupV3": topoGeneralGroupV3,
       "topoClientGroupV4": topoClientGroupV4,
       "topoPeerGroupV3": topoPeerGroupV3,
       "topoSegmentGroup": topoSegmentGroup,
       "topoGeneralGroupV4": topoGeneralGroupV4,
       "topoSegmentGroupV2": topoSegmentGroupV2,
       "topoClientGroupV5": topoClientGroupV5,
       "topoPeerGroupV4": topoPeerGroupV4,
       "topoIntGroupV3": topoIntGroupV3,
       "topoClientGroupV6": topoClientGroupV6,
       "topoIntGroupV4": topoIntGroupV4,
       "topoPeerGroupV5": topoPeerGroupV5,
       "lumTopologyCompl": lumTopologyCompl,
       "lumTopoBasicComplV1": lumTopoBasicComplV1,
       "lumTopoBasicComplV2": lumTopoBasicComplV2,
       "lumTopoBasicComplV3": lumTopoBasicComplV3,
       "lumTopoBasicComplV4": lumTopoBasicComplV4,
       "lumTopoBasicComplV5": lumTopoBasicComplV5,
       "lumTopoBasicComplV6": lumTopoBasicComplV6,
       "lumTopoBasicComplV7": lumTopoBasicComplV7,
       "lumTopoBasicComplV8": lumTopoBasicComplV8,
       "lumTopoBasicComplV9": lumTopoBasicComplV9,
       "lumTopoBasicComplV10": lumTopoBasicComplV10,
       "lumTopoBasicComplV11": lumTopoBasicComplV11,
       "lumTopologyMIBObjects": lumTopologyMIBObjects,
       "topoGeneral": topoGeneral,
       "topoGeneralTestAndIncr": topoGeneralTestAndIncr,
       "topoGeneralMibSpecVersion": topoGeneralMibSpecVersion,
       "topoGeneralMibImplVersion": topoGeneralMibImplVersion,
       "topoGeneralLastChangeTime": topoGeneralLastChangeTime,
       "topoGeneralStateLastChangeTime": topoGeneralStateLastChangeTime,
       "topoGeneralTopoClientTableSize": topoGeneralTopoClientTableSize,
       "topoGeneralTopoPeerTableSize": topoGeneralTopoPeerTableSize,
       "topoGeneralTopoInternalTableSize": topoGeneralTopoInternalTableSize,
       "topoGeneralTopoSegmentTableSize": topoGeneralTopoSegmentTableSize,
       "topoIntList": topoIntList,
       "topoIntTable": topoIntTable,
       "topoIntEntry": topoIntEntry,
       "topoIntIndex": topoIntIndex,
       "topoIntFromSubrack": topoIntFromSubrack,
       "topoIntFromSlot": topoIntFromSlot,
       "topoIntFromPort": topoIntFromPort,
       "topoIntToSubrack": topoIntToSubrack,
       "topoIntToSlot": topoIntToSlot,
       "topoIntToPort": topoIntToPort,
       "topoIntDescr": topoIntDescr,
       "topoIntDirection": topoIntDirection,
       "topoIntRowStatus": topoIntRowStatus,
       "topoIntName": topoIntName,
       "topoIntFromIfNo": topoIntFromIfNo,
       "topoIntToIfNo": topoIntToIfNo,
       "topoPeerList": topoPeerList,
       "topoPeerTable": topoPeerTable,
       "topoPeerEntry": topoPeerEntry,
       "topoPeerIndex": topoPeerIndex,
       "topoPeerLocalSubrack": topoPeerLocalSubrack,
       "topoPeerLocalSlot": topoPeerLocalSlot,
       "topoPeerLocalPort": topoPeerLocalPort,
       "topoPeerRemoteIpAddress": topoPeerRemoteIpAddress,
       "topoPeerRemoteSubrack": topoPeerRemoteSubrack,
       "topoPeerRemoteSlot": topoPeerRemoteSlot,
       "topoPeerRemotePort": topoPeerRemotePort,
       "topoPeerDescr": topoPeerDescr,
       "topoPeerDirection": topoPeerDirection,
       "topoPeerRowStatus": topoPeerRowStatus,
       "topoPeerName": topoPeerName,
       "topoPeerLinkAttenuation": topoPeerLinkAttenuation,
       "topoPeerLocalLabel": topoPeerLocalLabel,
       "topoPeerRemoteLabel": topoPeerRemoteLabel,
       "topoPeerLocalIfNo": topoPeerLocalIfNo,
       "topoPeerRemoteIfNo": topoPeerRemoteIfNo,
       "topoClientList": topoClientList,
       "topoClientTable": topoClientTable,
       "topoClientEntry": topoClientEntry,
       "topoClientIndex": topoClientIndex,
       "topoClientLocalInSubrack": topoClientLocalInSubrack,
       "topoClientLocalInSlot": topoClientLocalInSlot,
       "topoClientLocalInPort": topoClientLocalInPort,
       "topoClientRemoteIpAddress": topoClientRemoteIpAddress,
       "topoClientRemoteIfIndex": topoClientRemoteIfIndex,
       "topoClientDescr": topoClientDescr,
       "topoClientDirection": topoClientDirection,
       "topoClientRowStatus": topoClientRowStatus,
       "topoClientName": topoClientName,
       "topoClientLocalOutSubrack": topoClientLocalOutSubrack,
       "topoClientLocalOutSlot": topoClientLocalOutSlot,
       "topoClientLocalOutPort": topoClientLocalOutPort,
       "topoClientChannelId": topoClientChannelId,
       "topoClientInterfaceRepresentation": topoClientInterfaceRepresentation,
       "topoClientLocalOutIfNo": topoClientLocalOutIfNo,
       "topoClientLocalInIfNo": topoClientLocalInIfNo,
       "topoSegmentList": topoSegmentList,
       "topoSegmentTable": topoSegmentTable,
       "topoSegmentEntry": topoSegmentEntry,
       "topoSegmentIndex": topoSegmentIndex,
       "topoSegmentName": topoSegmentName,
       "topoSegmentInSubrack": topoSegmentInSubrack,
       "topoSegmentInSlot": topoSegmentInSlot,
       "topoSegmentInPort": topoSegmentInPort,
       "topoSegmentOutSubrack": topoSegmentOutSubrack,
       "topoSegmentOutSlot": topoSegmentOutSlot,
       "topoSegmentOutPort": topoSegmentOutPort,
       "topoSegmentFrequencyType": topoSegmentFrequencyType,
       "topoSegmentFrequency": topoSegmentFrequency,
       "topoSegmentSubChannelId": topoSegmentSubChannelId,
       "topoSegmentBegin": topoSegmentBegin,
       "topoSegmentType": topoSegmentType,
       "topoSegmentInEntityId": topoSegmentInEntityId,
       "topoSegmentOutEntityId": topoSegmentOutEntityId,
       "topoSegmentEntityList": topoSegmentEntityList,
       "topoSegmentObjectList": topoSegmentObjectList,
       "topoSegmentDirection": topoSegmentDirection,
       "topoSegmentEntryPointsCommand": topoSegmentEntryPointsCommand,
       "topoSegmentSubSegmentsCommand": topoSegmentSubSegmentsCommand,
       "topoSegmentUniqId": topoSegmentUniqId}
)
