# SNMP MIB module (VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:21 2025
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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class PortsBitmap(OctetString):
    """Custom type PortsBitmap based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbVlans_ObjectIdentity = ObjectIdentity
nbVlans = _NbVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3)
)
_NbVlansRun_ObjectIdentity = ObjectIdentity
nbVlansRun = _NbVlansRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1)
)


class _NbVlansRunVlansMode_Type(Integer32):
    """Custom type nbVlansRunVlansMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noneVlan", 1),
          ("vbcMode", 2),
          ("isvpMode", 3))
    )


_NbVlansRunVlansMode_Type.__name__ = "Integer32"
_NbVlansRunVlansMode_Object = MibScalar
nbVlansRunVlansMode = _NbVlansRunVlansMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 1),
    _NbVlansRunVlansMode_Type()
)
nbVlansRunVlansMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunVlansMode.setStatus("mandatory")


class _NbVlansRunIngressType_Type(Integer32):
    """Custom type nbVlansRunIngressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonControl", 1),
          ("perDeviceOnly", 2),
          ("perPort", 3))
    )


_NbVlansRunIngressType_Type.__name__ = "Integer32"
_NbVlansRunIngressType_Object = MibScalar
nbVlansRunIngressType = _NbVlansRunIngressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 2),
    _NbVlansRunIngressType_Type()
)
nbVlansRunIngressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunIngressType.setStatus("mandatory")


class _NbVlansRunIngressMode_Type(Integer32):
    """Custom type nbVlansRunIngressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NbVlansRunIngressMode_Type.__name__ = "Integer32"
_NbVlansRunIngressMode_Object = MibScalar
nbVlansRunIngressMode = _NbVlansRunIngressMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 3),
    _NbVlansRunIngressMode_Type()
)
nbVlansRunIngressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunIngressMode.setStatus("mandatory")
_NbVlansRunIngressPorts_Type = PortsBitmap
_NbVlansRunIngressPorts_Object = MibScalar
nbVlansRunIngressPorts = _NbVlansRunIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 4),
    _NbVlansRunIngressPorts_Type()
)
nbVlansRunIngressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunIngressPorts.setStatus("mandatory")


class _NbVlansRunEgressType_Type(Integer32):
    """Custom type nbVlansRunEgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonControl", 1),
          ("perDeviceOnly", 2),
          ("perPort", 3))
    )


_NbVlansRunEgressType_Type.__name__ = "Integer32"
_NbVlansRunEgressType_Object = MibScalar
nbVlansRunEgressType = _NbVlansRunEgressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 5),
    _NbVlansRunEgressType_Type()
)
nbVlansRunEgressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunEgressType.setStatus("mandatory")


class _NbVlansRunEgressMode_Type(Integer32):
    """Custom type nbVlansRunEgressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NbVlansRunEgressMode_Type.__name__ = "Integer32"
_NbVlansRunEgressMode_Object = MibScalar
nbVlansRunEgressMode = _NbVlansRunEgressMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 6),
    _NbVlansRunEgressMode_Type()
)
nbVlansRunEgressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunEgressMode.setStatus("mandatory")
_NbVlansRunEgressPorts_Type = PortsBitmap
_NbVlansRunEgressPorts_Object = MibScalar
nbVlansRunEgressPorts = _NbVlansRunEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 7),
    _NbVlansRunEgressPorts_Type()
)
nbVlansRunEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunEgressPorts.setStatus("mandatory")
_NbVlansRunMgmtTable_Object = MibTable
nbVlansRunMgmtTable = _NbVlansRunMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 8)
)
if mibBuilder.loadTexts:
    nbVlansRunMgmtTable.setStatus("mandatory")
_NbVlansRunMgmtEntry_Object = MibTableRow
nbVlansRunMgmtEntry = _NbVlansRunMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 8, 1)
)
nbVlansRunMgmtEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunMgmtTag"),
)
if mibBuilder.loadTexts:
    nbVlansRunMgmtEntry.setStatus("mandatory")


class _NbVlansRunMgmtTag_Type(Integer32):
    """Custom type nbVlansRunMgmtTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbVlansRunMgmtTag_Type.__name__ = "Integer32"
_NbVlansRunMgmtTag_Object = MibTableColumn
nbVlansRunMgmtTag = _NbVlansRunMgmtTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 8, 1, 1),
    _NbVlansRunMgmtTag_Type()
)
nbVlansRunMgmtTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunMgmtTag.setStatus("mandatory")
_NbVlansRunMgmtList_Type = PortsBitmap
_NbVlansRunMgmtList_Object = MibTableColumn
nbVlansRunMgmtList = _NbVlansRunMgmtList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 8, 1, 2),
    _NbVlansRunMgmtList_Type()
)
nbVlansRunMgmtList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunMgmtList.setStatus("mandatory")


class _NbVlansRunMgmtName_Type(DisplayString):
    """Custom type nbVlansRunMgmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NbVlansRunMgmtName_Type.__name__ = "DisplayString"
_NbVlansRunMgmtName_Object = MibTableColumn
nbVlansRunMgmtName = _NbVlansRunMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 8, 1, 3),
    _NbVlansRunMgmtName_Type()
)
nbVlansRunMgmtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunMgmtName.setStatus("mandatory")


class _NbVlansRunMgmtTagStatus_Type(Integer32):
    """Custom type nbVlansRunMgmtTagStatus based on Integer32"""
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


_NbVlansRunMgmtTagStatus_Type.__name__ = "Integer32"
_NbVlansRunMgmtTagStatus_Object = MibTableColumn
nbVlansRunMgmtTagStatus = _NbVlansRunMgmtTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 8, 1, 4),
    _NbVlansRunMgmtTagStatus_Type()
)
nbVlansRunMgmtTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunMgmtTagStatus.setStatus("mandatory")
_NbVlansRunSrvrTable_Object = MibTable
nbVlansRunSrvrTable = _NbVlansRunSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 9)
)
if mibBuilder.loadTexts:
    nbVlansRunSrvrTable.setStatus("mandatory")
_NbVlansRunSrvrEntry_Object = MibTableRow
nbVlansRunSrvrEntry = _NbVlansRunSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 9, 1)
)
nbVlansRunSrvrEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunSrvrPort"),
)
if mibBuilder.loadTexts:
    nbVlansRunSrvrEntry.setStatus("mandatory")
_NbVlansRunSrvrPort_Type = Integer32
_NbVlansRunSrvrPort_Object = MibTableColumn
nbVlansRunSrvrPort = _NbVlansRunSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 9, 1, 1),
    _NbVlansRunSrvrPort_Type()
)
nbVlansRunSrvrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunSrvrPort.setStatus("mandatory")


class _NbVlansRunSrvrPortStatus_Type(Integer32):
    """Custom type nbVlansRunSrvrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonServer", 1),
          ("server", 2))
    )


_NbVlansRunSrvrPortStatus_Type.__name__ = "Integer32"
_NbVlansRunSrvrPortStatus_Object = MibTableColumn
nbVlansRunSrvrPortStatus = _NbVlansRunSrvrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 9, 1, 2),
    _NbVlansRunSrvrPortStatus_Type()
)
nbVlansRunSrvrPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunSrvrPortStatus.setStatus("mandatory")


class _NbVlansRunSrvrPortTag_Type(Integer32):
    """Custom type nbVlansRunSrvrPortTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbVlansRunSrvrPortTag_Type.__name__ = "Integer32"
_NbVlansRunSrvrPortTag_Object = MibTableColumn
nbVlansRunSrvrPortTag = _NbVlansRunSrvrPortTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 9, 1, 3),
    _NbVlansRunSrvrPortTag_Type()
)
nbVlansRunSrvrPortTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunSrvrPortTag.setStatus("mandatory")
_NbVlansRunPortsCfgTable_Object = MibTable
nbVlansRunPortsCfgTable = _NbVlansRunPortsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 10)
)
if mibBuilder.loadTexts:
    nbVlansRunPortsCfgTable.setStatus("mandatory")
_NbVlansRunPortsCfgEntry_Object = MibTableRow
nbVlansRunPortsCfgEntry = _NbVlansRunPortsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 10, 1)
)
nbVlansRunPortsCfgEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunPort"),
)
if mibBuilder.loadTexts:
    nbVlansRunPortsCfgEntry.setStatus("mandatory")
_NbVlansRunPort_Type = Integer32
_NbVlansRunPort_Object = MibTableColumn
nbVlansRunPort = _NbVlansRunPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 10, 1, 1),
    _NbVlansRunPort_Type()
)
nbVlansRunPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunPort.setStatus("mandatory")


class _NbVlansRunPortPriority_Type(Integer32):
    """Custom type nbVlansRunPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NbVlansRunPortPriority_Type.__name__ = "Integer32"
_NbVlansRunPortPriority_Object = MibTableColumn
nbVlansRunPortPriority = _NbVlansRunPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 10, 1, 2),
    _NbVlansRunPortPriority_Type()
)
nbVlansRunPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunPortPriority.setStatus("mandatory")


class _NbVlansRunPortTagOutMode_Type(Integer32):
    """Custom type nbVlansRunPortTagOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("tagAware", 2),
          ("nonIsvp", 3))
    )


_NbVlansRunPortTagOutMode_Type.__name__ = "Integer32"
_NbVlansRunPortTagOutMode_Object = MibTableColumn
nbVlansRunPortTagOutMode = _NbVlansRunPortTagOutMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 10, 1, 3),
    _NbVlansRunPortTagOutMode_Type()
)
nbVlansRunPortTagOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunPortTagOutMode.setStatus("mandatory")


class _NbVlansRunPriorityPolicy_Type(Integer32):
    """Custom type nbVlansRunPriorityPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NbVlansRunPriorityPolicy_Type.__name__ = "Integer32"
_NbVlansRunPriorityPolicy_Object = MibScalar
nbVlansRunPriorityPolicy = _NbVlansRunPriorityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 11),
    _NbVlansRunPriorityPolicy_Type()
)
nbVlansRunPriorityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunPriorityPolicy.setStatus("mandatory")
_NbVlansRunIsvMaxNum_Type = Integer32
_NbVlansRunIsvMaxNum_Object = MibScalar
nbVlansRunIsvMaxNum = _NbVlansRunIsvMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 12),
    _NbVlansRunIsvMaxNum_Type()
)
nbVlansRunIsvMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunIsvMaxNum.setStatus("mandatory")
_NbVlansRunIsvTable_Object = MibTable
nbVlansRunIsvTable = _NbVlansRunIsvTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13)
)
if mibBuilder.loadTexts:
    nbVlansRunIsvTable.setStatus("mandatory")
_NbVlansRunIsvEntry_Object = MibTableRow
nbVlansRunIsvEntry = _NbVlansRunIsvEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1)
)
nbVlansRunIsvEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunIsvIndex"),
)
if mibBuilder.loadTexts:
    nbVlansRunIsvEntry.setStatus("mandatory")
_NbVlansRunIsvIndex_Type = Integer32
_NbVlansRunIsvIndex_Object = MibTableColumn
nbVlansRunIsvIndex = _NbVlansRunIsvIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1, 1),
    _NbVlansRunIsvIndex_Type()
)
nbVlansRunIsvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunIsvIndex.setStatus("mandatory")


class _NbVlansRunIsvStatus_Type(Integer32):
    """Custom type nbVlansRunIsvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("mcast", 3))
    )


_NbVlansRunIsvStatus_Type.__name__ = "Integer32"
_NbVlansRunIsvStatus_Object = MibTableColumn
nbVlansRunIsvStatus = _NbVlansRunIsvStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1, 2),
    _NbVlansRunIsvStatus_Type()
)
nbVlansRunIsvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunIsvStatus.setStatus("mandatory")


class _NbVlansRunIsvList_Type(OctetString):
    """Custom type nbVlansRunIsvList based on OctetString"""
    defaultHexValue = "ffff"


_NbVlansRunIsvList_Type.__name__ = "OctetString"
_NbVlansRunIsvList_Object = MibTableColumn
nbVlansRunIsvList = _NbVlansRunIsvList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1, 3),
    _NbVlansRunIsvList_Type()
)
nbVlansRunIsvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunIsvList.setStatus("mandatory")


class _NbVlansRunIsvName_Type(DisplayString):
    """Custom type nbVlansRunIsvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NbVlansRunIsvName_Type.__name__ = "DisplayString"
_NbVlansRunIsvName_Object = MibTableColumn
nbVlansRunIsvName = _NbVlansRunIsvName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1, 4),
    _NbVlansRunIsvName_Type()
)
nbVlansRunIsvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunIsvName.setStatus("mandatory")


class _NbVlansRunIsvTag_Type(Integer32):
    """Custom type nbVlansRunIsvTag based on Integer32"""
    defaultValue = 1


_NbVlansRunIsvTag_Type.__name__ = "Integer32"
_NbVlansRunIsvTag_Object = MibTableColumn
nbVlansRunIsvTag = _NbVlansRunIsvTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1, 5),
    _NbVlansRunIsvTag_Type()
)
nbVlansRunIsvTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunIsvTag.setStatus("mandatory")
_NbVlansRunIsvVlanIndex_Type = Integer32
_NbVlansRunIsvVlanIndex_Object = MibTableColumn
nbVlansRunIsvVlanIndex = _NbVlansRunIsvVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1, 6),
    _NbVlansRunIsvVlanIndex_Type()
)
nbVlansRunIsvVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunIsvVlanIndex.setStatus("mandatory")


class _NbVlansRunIsvVlanPriority_Type(Integer32):
    """Custom type nbVlansRunIsvVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NbVlansRunIsvVlanPriority_Type.__name__ = "Integer32"
_NbVlansRunIsvVlanPriority_Object = MibTableColumn
nbVlansRunIsvVlanPriority = _NbVlansRunIsvVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 13, 1, 7),
    _NbVlansRunIsvVlanPriority_Type()
)
nbVlansRunIsvVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunIsvVlanPriority.setStatus("mandatory")
_NbVlansRunVPT2PriorityTable_Object = MibTable
nbVlansRunVPT2PriorityTable = _NbVlansRunVPT2PriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 15)
)
if mibBuilder.loadTexts:
    nbVlansRunVPT2PriorityTable.setStatus("mandatory")
_NbVlansRunVPT2PriorityEntry_Object = MibTableRow
nbVlansRunVPT2PriorityEntry = _NbVlansRunVPT2PriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 15, 1)
)
nbVlansRunVPT2PriorityEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunVPT2PriorVPTNumber"),
)
if mibBuilder.loadTexts:
    nbVlansRunVPT2PriorityEntry.setStatus("mandatory")


class _NbVlansRunVPT2PriorVPTNumber_Type(Integer32):
    """Custom type nbVlansRunVPT2PriorVPTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbVlansRunVPT2PriorVPTNumber_Type.__name__ = "Integer32"
_NbVlansRunVPT2PriorVPTNumber_Object = MibTableColumn
nbVlansRunVPT2PriorVPTNumber = _NbVlansRunVPT2PriorVPTNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 15, 1, 1),
    _NbVlansRunVPT2PriorVPTNumber_Type()
)
nbVlansRunVPT2PriorVPTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunVPT2PriorVPTNumber.setStatus("mandatory")


class _NbVlansRunVPT2PriorPriorNumber_Type(Integer32):
    """Custom type nbVlansRunVPT2PriorPriorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NbVlansRunVPT2PriorPriorNumber_Type.__name__ = "Integer32"
_NbVlansRunVPT2PriorPriorNumber_Object = MibTableColumn
nbVlansRunVPT2PriorPriorNumber = _NbVlansRunVPT2PriorPriorNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 15, 1, 2),
    _NbVlansRunVPT2PriorPriorNumber_Type()
)
nbVlansRunVPT2PriorPriorNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunVPT2PriorPriorNumber.setStatus("mandatory")
_NbVlansRunPriority2VPTTable_Object = MibTable
nbVlansRunPriority2VPTTable = _NbVlansRunPriority2VPTTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 16)
)
if mibBuilder.loadTexts:
    nbVlansRunPriority2VPTTable.setStatus("mandatory")
_NbVlansRunPriority2VPTEntry_Object = MibTableRow
nbVlansRunPriority2VPTEntry = _NbVlansRunPriority2VPTEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 16, 1)
)
nbVlansRunPriority2VPTEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunPrior2VPTPriorNumber"),
)
if mibBuilder.loadTexts:
    nbVlansRunPriority2VPTEntry.setStatus("mandatory")


class _NbVlansRunPrior2VPTPriorNumber_Type(Integer32):
    """Custom type nbVlansRunPrior2VPTPriorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NbVlansRunPrior2VPTPriorNumber_Type.__name__ = "Integer32"
_NbVlansRunPrior2VPTPriorNumber_Object = MibTableColumn
nbVlansRunPrior2VPTPriorNumber = _NbVlansRunPrior2VPTPriorNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 16, 1, 1),
    _NbVlansRunPrior2VPTPriorNumber_Type()
)
nbVlansRunPrior2VPTPriorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunPrior2VPTPriorNumber.setStatus("mandatory")


class _NbVlansRunPrior2VPTVPTNumber_Type(Integer32):
    """Custom type nbVlansRunPrior2VPTVPTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbVlansRunPrior2VPTVPTNumber_Type.__name__ = "Integer32"
_NbVlansRunPrior2VPTVPTNumber_Object = MibTableColumn
nbVlansRunPrior2VPTVPTNumber = _NbVlansRunPrior2VPTVPTNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 16, 1, 2),
    _NbVlansRunPrior2VPTVPTNumber_Type()
)
nbVlansRunPrior2VPTVPTNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunPrior2VPTVPTNumber.setStatus("mandatory")
_NbVlansRunSlotEtherTypeTable_Object = MibTable
nbVlansRunSlotEtherTypeTable = _NbVlansRunSlotEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 20)
)
if mibBuilder.loadTexts:
    nbVlansRunSlotEtherTypeTable.setStatus("mandatory")
_NbVlansRunSlotEtherTypeEntry_Object = MibTableRow
nbVlansRunSlotEtherTypeEntry = _NbVlansRunSlotEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 20, 1)
)
nbVlansRunSlotEtherTypeEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunSlotNumber"),
)
if mibBuilder.loadTexts:
    nbVlansRunSlotEtherTypeEntry.setStatus("mandatory")
_NbVlansRunSlotNumber_Type = Integer32
_NbVlansRunSlotNumber_Object = MibTableColumn
nbVlansRunSlotNumber = _NbVlansRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 20, 1, 1),
    _NbVlansRunSlotNumber_Type()
)
nbVlansRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunSlotNumber.setStatus("mandatory")


class _NbVlansRunSlotEtherType_Type(Integer32):
    """Custom type nbVlansRunSlotEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbVlansRunSlotEtherType_Type.__name__ = "Integer32"
_NbVlansRunSlotEtherType_Object = MibTableColumn
nbVlansRunSlotEtherType = _NbVlansRunSlotEtherType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 20, 1, 2),
    _NbVlansRunSlotEtherType_Type()
)
nbVlansRunSlotEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunSlotEtherType.setStatus("mandatory")
_NbVlansRunVMANPortTable_Object = MibTable
nbVlansRunVMANPortTable = _NbVlansRunVMANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 22)
)
if mibBuilder.loadTexts:
    nbVlansRunVMANPortTable.setStatus("mandatory")
_NbVlansRunVMANPortEntry_Object = MibTableRow
nbVlansRunVMANPortEntry = _NbVlansRunVMANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 22, 1)
)
nbVlansRunVMANPortEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunVMANPortNumber"),
)
if mibBuilder.loadTexts:
    nbVlansRunVMANPortEntry.setStatus("mandatory")
_NbVlansRunVMANPortNumber_Type = Integer32
_NbVlansRunVMANPortNumber_Object = MibTableColumn
nbVlansRunVMANPortNumber = _NbVlansRunVMANPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 22, 1, 1),
    _NbVlansRunVMANPortNumber_Type()
)
nbVlansRunVMANPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunVMANPortNumber.setStatus("mandatory")


class _NbVlansRunVMANPortMode_Type(Integer32):
    """Custom type nbVlansRunVMANPortMode based on Integer32"""
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
          ("enable", 2),
          ("disable", 3))
    )


_NbVlansRunVMANPortMode_Type.__name__ = "Integer32"
_NbVlansRunVMANPortMode_Object = MibTableColumn
nbVlansRunVMANPortMode = _NbVlansRunVMANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 22, 1, 2),
    _NbVlansRunVMANPortMode_Type()
)
nbVlansRunVMANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunVMANPortMode.setStatus("mandatory")


class _NbVlansRunCPUEtherType_Type(Integer32):
    """Custom type nbVlansRunCPUEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbVlansRunCPUEtherType_Type.__name__ = "Integer32"
_NbVlansRunCPUEtherType_Object = MibScalar
nbVlansRunCPUEtherType = _NbVlansRunCPUEtherType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 23),
    _NbVlansRunCPUEtherType_Type()
)
nbVlansRunCPUEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunCPUEtherType.setStatus("mandatory")
_NbVlansRunMacLimitGroup_ObjectIdentity = ObjectIdentity
nbVlansRunMacLimitGroup = _NbVlansRunMacLimitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 24)
)


class _NbVlansRunPortMacLimitActionMode_Type(Integer32):
    """Custom type nbVlansRunPortMacLimitActionMode based on Integer32"""
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
          ("trapOnly", 2),
          ("portDisable", 3),
          ("discardExceeded", 4))
    )


_NbVlansRunPortMacLimitActionMode_Type.__name__ = "Integer32"
_NbVlansRunPortMacLimitActionMode_Object = MibScalar
nbVlansRunPortMacLimitActionMode = _NbVlansRunPortMacLimitActionMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 24, 1),
    _NbVlansRunPortMacLimitActionMode_Type()
)
nbVlansRunPortMacLimitActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunPortMacLimitActionMode.setStatus("mandatory")
_NbVlansRunPortMacLimitActionDescription_Type = DisplayString
_NbVlansRunPortMacLimitActionDescription_Object = MibScalar
nbVlansRunPortMacLimitActionDescription = _NbVlansRunPortMacLimitActionDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 24, 2),
    _NbVlansRunPortMacLimitActionDescription_Type()
)
nbVlansRunPortMacLimitActionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunPortMacLimitActionDescription.setStatus("mandatory")
_NbVlansRunPortMacLimitTable_Object = MibTable
nbVlansRunPortMacLimitTable = _NbVlansRunPortMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 24, 10)
)
if mibBuilder.loadTexts:
    nbVlansRunPortMacLimitTable.setStatus("mandatory")
_NbVlansRunPortMacLimitEntry_Object = MibTableRow
nbVlansRunPortMacLimitEntry = _NbVlansRunPortMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 24, 10, 1)
)
nbVlansRunPortMacLimitEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansRunPortMacLimitPortNumber"),
)
if mibBuilder.loadTexts:
    nbVlansRunPortMacLimitEntry.setStatus("mandatory")
_NbVlansRunPortMacLimitPortNumber_Type = Integer32
_NbVlansRunPortMacLimitPortNumber_Object = MibTableColumn
nbVlansRunPortMacLimitPortNumber = _NbVlansRunPortMacLimitPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 24, 10, 1, 1),
    _NbVlansRunPortMacLimitPortNumber_Type()
)
nbVlansRunPortMacLimitPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansRunPortMacLimitPortNumber.setStatus("mandatory")
_NbVlansRunPortMacLimitValue_Type = Integer32
_NbVlansRunPortMacLimitValue_Object = MibTableColumn
nbVlansRunPortMacLimitValue = _NbVlansRunPortMacLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 1, 24, 10, 1, 2),
    _NbVlansRunPortMacLimitValue_Type()
)
nbVlansRunPortMacLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansRunPortMacLimitValue.setStatus("mandatory")
_NbVlansPerm_ObjectIdentity = ObjectIdentity
nbVlansPerm = _NbVlansPerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2)
)


class _NbVlansPermVlansMode_Type(Integer32):
    """Custom type nbVlansPermVlansMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noneVlan", 1),
          ("vbcMode", 2),
          ("isvpMode", 3))
    )


_NbVlansPermVlansMode_Type.__name__ = "Integer32"
_NbVlansPermVlansMode_Object = MibScalar
nbVlansPermVlansMode = _NbVlansPermVlansMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 1),
    _NbVlansPermVlansMode_Type()
)
nbVlansPermVlansMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermVlansMode.setStatus("mandatory")


class _NbVlansPermIngressType_Type(Integer32):
    """Custom type nbVlansPermIngressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonControl", 1),
          ("perDeviceOnly", 2),
          ("perPort", 3))
    )


_NbVlansPermIngressType_Type.__name__ = "Integer32"
_NbVlansPermIngressType_Object = MibScalar
nbVlansPermIngressType = _NbVlansPermIngressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 2),
    _NbVlansPermIngressType_Type()
)
nbVlansPermIngressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermIngressType.setStatus("mandatory")


class _NbVlansPermIngressMode_Type(Integer32):
    """Custom type nbVlansPermIngressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NbVlansPermIngressMode_Type.__name__ = "Integer32"
_NbVlansPermIngressMode_Object = MibScalar
nbVlansPermIngressMode = _NbVlansPermIngressMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 3),
    _NbVlansPermIngressMode_Type()
)
nbVlansPermIngressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermIngressMode.setStatus("mandatory")
_NbVlansPermIngressPorts_Type = PortsBitmap
_NbVlansPermIngressPorts_Object = MibScalar
nbVlansPermIngressPorts = _NbVlansPermIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 4),
    _NbVlansPermIngressPorts_Type()
)
nbVlansPermIngressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermIngressPorts.setStatus("mandatory")


class _NbVlansPermEgressType_Type(Integer32):
    """Custom type nbVlansPermEgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonControl", 1),
          ("perDeviceOnly", 2),
          ("perPort", 3))
    )


_NbVlansPermEgressType_Type.__name__ = "Integer32"
_NbVlansPermEgressType_Object = MibScalar
nbVlansPermEgressType = _NbVlansPermEgressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 5),
    _NbVlansPermEgressType_Type()
)
nbVlansPermEgressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermEgressType.setStatus("mandatory")


class _NbVlansPermEgressMode_Type(Integer32):
    """Custom type nbVlansPermEgressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NbVlansPermEgressMode_Type.__name__ = "Integer32"
_NbVlansPermEgressMode_Object = MibScalar
nbVlansPermEgressMode = _NbVlansPermEgressMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 6),
    _NbVlansPermEgressMode_Type()
)
nbVlansPermEgressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermEgressMode.setStatus("mandatory")
_NbVlansPermEgressPorts_Type = PortsBitmap
_NbVlansPermEgressPorts_Object = MibScalar
nbVlansPermEgressPorts = _NbVlansPermEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 7),
    _NbVlansPermEgressPorts_Type()
)
nbVlansPermEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermEgressPorts.setStatus("mandatory")
_NbVlansPermMgmtTable_Object = MibTable
nbVlansPermMgmtTable = _NbVlansPermMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 8)
)
if mibBuilder.loadTexts:
    nbVlansPermMgmtTable.setStatus("mandatory")
_NbVlansPermMgmtEntry_Object = MibTableRow
nbVlansPermMgmtEntry = _NbVlansPermMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 8, 1)
)
nbVlansPermMgmtEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermMgmtTag"),
)
if mibBuilder.loadTexts:
    nbVlansPermMgmtEntry.setStatus("mandatory")


class _NbVlansPermMgmtTag_Type(Integer32):
    """Custom type nbVlansPermMgmtTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbVlansPermMgmtTag_Type.__name__ = "Integer32"
_NbVlansPermMgmtTag_Object = MibTableColumn
nbVlansPermMgmtTag = _NbVlansPermMgmtTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 8, 1, 1),
    _NbVlansPermMgmtTag_Type()
)
nbVlansPermMgmtTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermMgmtTag.setStatus("mandatory")
_NbVlansPermMgmtList_Type = PortsBitmap
_NbVlansPermMgmtList_Object = MibTableColumn
nbVlansPermMgmtList = _NbVlansPermMgmtList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 8, 1, 2),
    _NbVlansPermMgmtList_Type()
)
nbVlansPermMgmtList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermMgmtList.setStatus("mandatory")


class _NbVlansPermMgmtName_Type(DisplayString):
    """Custom type nbVlansPermMgmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NbVlansPermMgmtName_Type.__name__ = "DisplayString"
_NbVlansPermMgmtName_Object = MibTableColumn
nbVlansPermMgmtName = _NbVlansPermMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 8, 1, 3),
    _NbVlansPermMgmtName_Type()
)
nbVlansPermMgmtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermMgmtName.setStatus("mandatory")


class _NbVlansPermMgmtTagStatus_Type(Integer32):
    """Custom type nbVlansPermMgmtTagStatus based on Integer32"""
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


_NbVlansPermMgmtTagStatus_Type.__name__ = "Integer32"
_NbVlansPermMgmtTagStatus_Object = MibTableColumn
nbVlansPermMgmtTagStatus = _NbVlansPermMgmtTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 8, 1, 4),
    _NbVlansPermMgmtTagStatus_Type()
)
nbVlansPermMgmtTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermMgmtTagStatus.setStatus("mandatory")
_NbVlansPermSrvrTable_Object = MibTable
nbVlansPermSrvrTable = _NbVlansPermSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 9)
)
if mibBuilder.loadTexts:
    nbVlansPermSrvrTable.setStatus("mandatory")
_NbVlansPermSrvrEntry_Object = MibTableRow
nbVlansPermSrvrEntry = _NbVlansPermSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 9, 1)
)
nbVlansPermSrvrEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermSrvrPort"),
)
if mibBuilder.loadTexts:
    nbVlansPermSrvrEntry.setStatus("mandatory")
_NbVlansPermSrvrPort_Type = Integer32
_NbVlansPermSrvrPort_Object = MibTableColumn
nbVlansPermSrvrPort = _NbVlansPermSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 9, 1, 1),
    _NbVlansPermSrvrPort_Type()
)
nbVlansPermSrvrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermSrvrPort.setStatus("mandatory")


class _NbVlansPermSrvrPortStatus_Type(Integer32):
    """Custom type nbVlansPermSrvrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonServer", 1),
          ("server", 2))
    )


_NbVlansPermSrvrPortStatus_Type.__name__ = "Integer32"
_NbVlansPermSrvrPortStatus_Object = MibTableColumn
nbVlansPermSrvrPortStatus = _NbVlansPermSrvrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 9, 1, 2),
    _NbVlansPermSrvrPortStatus_Type()
)
nbVlansPermSrvrPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermSrvrPortStatus.setStatus("mandatory")


class _NbVlansPermSrvrPortTag_Type(Integer32):
    """Custom type nbVlansPermSrvrPortTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbVlansPermSrvrPortTag_Type.__name__ = "Integer32"
_NbVlansPermSrvrPortTag_Object = MibTableColumn
nbVlansPermSrvrPortTag = _NbVlansPermSrvrPortTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 9, 1, 3),
    _NbVlansPermSrvrPortTag_Type()
)
nbVlansPermSrvrPortTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermSrvrPortTag.setStatus("mandatory")
_NbVlansPermPortsCfgTable_Object = MibTable
nbVlansPermPortsCfgTable = _NbVlansPermPortsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 10)
)
if mibBuilder.loadTexts:
    nbVlansPermPortsCfgTable.setStatus("mandatory")
_NbVlansPermPortsCfgEntry_Object = MibTableRow
nbVlansPermPortsCfgEntry = _NbVlansPermPortsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 10, 1)
)
nbVlansPermPortsCfgEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermPort"),
)
if mibBuilder.loadTexts:
    nbVlansPermPortsCfgEntry.setStatus("mandatory")
_NbVlansPermPort_Type = Integer32
_NbVlansPermPort_Object = MibTableColumn
nbVlansPermPort = _NbVlansPermPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 10, 1, 1),
    _NbVlansPermPort_Type()
)
nbVlansPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermPort.setStatus("mandatory")


class _NbVlansPermPortPriority_Type(Integer32):
    """Custom type nbVlansPermPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NbVlansPermPortPriority_Type.__name__ = "Integer32"
_NbVlansPermPortPriority_Object = MibTableColumn
nbVlansPermPortPriority = _NbVlansPermPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 10, 1, 2),
    _NbVlansPermPortPriority_Type()
)
nbVlansPermPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermPortPriority.setStatus("mandatory")


class _NbVlansPermPortTagOutMode_Type(Integer32):
    """Custom type nbVlansPermPortTagOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("tagAware", 2),
          ("nonIsvp", 3))
    )


_NbVlansPermPortTagOutMode_Type.__name__ = "Integer32"
_NbVlansPermPortTagOutMode_Object = MibTableColumn
nbVlansPermPortTagOutMode = _NbVlansPermPortTagOutMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 10, 1, 3),
    _NbVlansPermPortTagOutMode_Type()
)
nbVlansPermPortTagOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermPortTagOutMode.setStatus("mandatory")


class _NbVlansPermPriorityPolicy_Type(Integer32):
    """Custom type nbVlansPermPriorityPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NbVlansPermPriorityPolicy_Type.__name__ = "Integer32"
_NbVlansPermPriorityPolicy_Object = MibScalar
nbVlansPermPriorityPolicy = _NbVlansPermPriorityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 11),
    _NbVlansPermPriorityPolicy_Type()
)
nbVlansPermPriorityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermPriorityPolicy.setStatus("mandatory")
_NbVlansPermIsvMaxNum_Type = Integer32
_NbVlansPermIsvMaxNum_Object = MibScalar
nbVlansPermIsvMaxNum = _NbVlansPermIsvMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 12),
    _NbVlansPermIsvMaxNum_Type()
)
nbVlansPermIsvMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermIsvMaxNum.setStatus("mandatory")
_NbVlansPermIsvTable_Object = MibTable
nbVlansPermIsvTable = _NbVlansPermIsvTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13)
)
if mibBuilder.loadTexts:
    nbVlansPermIsvTable.setStatus("mandatory")
_NbVlansPermIsvEntry_Object = MibTableRow
nbVlansPermIsvEntry = _NbVlansPermIsvEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13, 1)
)
nbVlansPermIsvEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermIsvIndex"),
)
if mibBuilder.loadTexts:
    nbVlansPermIsvEntry.setStatus("mandatory")
_NbVlansPermIsvIndex_Type = Integer32
_NbVlansPermIsvIndex_Object = MibTableColumn
nbVlansPermIsvIndex = _NbVlansPermIsvIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13, 1, 1),
    _NbVlansPermIsvIndex_Type()
)
nbVlansPermIsvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermIsvIndex.setStatus("mandatory")


class _NbVlansPermIsvStatus_Type(Integer32):
    """Custom type nbVlansPermIsvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("mcast", 3))
    )


_NbVlansPermIsvStatus_Type.__name__ = "Integer32"
_NbVlansPermIsvStatus_Object = MibTableColumn
nbVlansPermIsvStatus = _NbVlansPermIsvStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13, 1, 2),
    _NbVlansPermIsvStatus_Type()
)
nbVlansPermIsvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermIsvStatus.setStatus("mandatory")


class _NbVlansPermIsvList_Type(OctetString):
    """Custom type nbVlansPermIsvList based on OctetString"""
    defaultHexValue = "ffff"


_NbVlansPermIsvList_Type.__name__ = "OctetString"
_NbVlansPermIsvList_Object = MibTableColumn
nbVlansPermIsvList = _NbVlansPermIsvList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13, 1, 3),
    _NbVlansPermIsvList_Type()
)
nbVlansPermIsvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermIsvList.setStatus("mandatory")


class _NbVlansPermIsvName_Type(DisplayString):
    """Custom type nbVlansPermIsvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NbVlansPermIsvName_Type.__name__ = "DisplayString"
_NbVlansPermIsvName_Object = MibTableColumn
nbVlansPermIsvName = _NbVlansPermIsvName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13, 1, 4),
    _NbVlansPermIsvName_Type()
)
nbVlansPermIsvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermIsvName.setStatus("mandatory")


class _NbVlansPermIsvTag_Type(Integer32):
    """Custom type nbVlansPermIsvTag based on Integer32"""
    defaultValue = 1


_NbVlansPermIsvTag_Type.__name__ = "Integer32"
_NbVlansPermIsvTag_Object = MibTableColumn
nbVlansPermIsvTag = _NbVlansPermIsvTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13, 1, 5),
    _NbVlansPermIsvTag_Type()
)
nbVlansPermIsvTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermIsvTag.setStatus("mandatory")


class _NbVlansPermIsvVlanPriority_Type(Integer32):
    """Custom type nbVlansPermIsvVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NbVlansPermIsvVlanPriority_Type.__name__ = "Integer32"
_NbVlansPermIsvVlanPriority_Object = MibTableColumn
nbVlansPermIsvVlanPriority = _NbVlansPermIsvVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 13, 1, 6),
    _NbVlansPermIsvVlanPriority_Type()
)
nbVlansPermIsvVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermIsvVlanPriority.setStatus("mandatory")
_NbVlansPermVPT2PriorityTable_Object = MibTable
nbVlansPermVPT2PriorityTable = _NbVlansPermVPT2PriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 15)
)
if mibBuilder.loadTexts:
    nbVlansPermVPT2PriorityTable.setStatus("mandatory")
_NbVlansPermVPT2PriorityEntry_Object = MibTableRow
nbVlansPermVPT2PriorityEntry = _NbVlansPermVPT2PriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 15, 1)
)
nbVlansPermVPT2PriorityEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermVPT2PriorVPTNumber"),
)
if mibBuilder.loadTexts:
    nbVlansPermVPT2PriorityEntry.setStatus("mandatory")


class _NbVlansPermVPT2PriorVPTNumber_Type(Integer32):
    """Custom type nbVlansPermVPT2PriorVPTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbVlansPermVPT2PriorVPTNumber_Type.__name__ = "Integer32"
_NbVlansPermVPT2PriorVPTNumber_Object = MibTableColumn
nbVlansPermVPT2PriorVPTNumber = _NbVlansPermVPT2PriorVPTNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 15, 1, 1),
    _NbVlansPermVPT2PriorVPTNumber_Type()
)
nbVlansPermVPT2PriorVPTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermVPT2PriorVPTNumber.setStatus("mandatory")


class _NbVlansPermVPT2PriorPriorNumber_Type(Integer32):
    """Custom type nbVlansPermVPT2PriorPriorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NbVlansPermVPT2PriorPriorNumber_Type.__name__ = "Integer32"
_NbVlansPermVPT2PriorPriorNumber_Object = MibTableColumn
nbVlansPermVPT2PriorPriorNumber = _NbVlansPermVPT2PriorPriorNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 15, 1, 2),
    _NbVlansPermVPT2PriorPriorNumber_Type()
)
nbVlansPermVPT2PriorPriorNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermVPT2PriorPriorNumber.setStatus("mandatory")
_NbVlansPermPriority2VPTTable_Object = MibTable
nbVlansPermPriority2VPTTable = _NbVlansPermPriority2VPTTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 16)
)
if mibBuilder.loadTexts:
    nbVlansPermPriority2VPTTable.setStatus("mandatory")
_NbVlansPermPriority2VPTEntry_Object = MibTableRow
nbVlansPermPriority2VPTEntry = _NbVlansPermPriority2VPTEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 16, 1)
)
nbVlansPermPriority2VPTEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermPrior2VPTPriorNumber"),
)
if mibBuilder.loadTexts:
    nbVlansPermPriority2VPTEntry.setStatus("mandatory")


class _NbVlansPermPrior2VPTPriorNumber_Type(Integer32):
    """Custom type nbVlansPermPrior2VPTPriorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NbVlansPermPrior2VPTPriorNumber_Type.__name__ = "Integer32"
_NbVlansPermPrior2VPTPriorNumber_Object = MibTableColumn
nbVlansPermPrior2VPTPriorNumber = _NbVlansPermPrior2VPTPriorNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 16, 1, 1),
    _NbVlansPermPrior2VPTPriorNumber_Type()
)
nbVlansPermPrior2VPTPriorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermPrior2VPTPriorNumber.setStatus("mandatory")


class _NbVlansPermPrior2VPTVPTNumber_Type(Integer32):
    """Custom type nbVlansPermPrior2VPTVPTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbVlansPermPrior2VPTVPTNumber_Type.__name__ = "Integer32"
_NbVlansPermPrior2VPTVPTNumber_Object = MibTableColumn
nbVlansPermPrior2VPTVPTNumber = _NbVlansPermPrior2VPTVPTNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 16, 1, 2),
    _NbVlansPermPrior2VPTVPTNumber_Type()
)
nbVlansPermPrior2VPTVPTNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermPrior2VPTVPTNumber.setStatus("mandatory")
_NbVlansPermSlotEtherTypeTable_Object = MibTable
nbVlansPermSlotEtherTypeTable = _NbVlansPermSlotEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 20)
)
if mibBuilder.loadTexts:
    nbVlansPermSlotEtherTypeTable.setStatus("mandatory")
_NbVlansPermSlotEtherTypeEntry_Object = MibTableRow
nbVlansPermSlotEtherTypeEntry = _NbVlansPermSlotEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 20, 1)
)
nbVlansPermSlotEtherTypeEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermSlotNumber"),
)
if mibBuilder.loadTexts:
    nbVlansPermSlotEtherTypeEntry.setStatus("mandatory")
_NbVlansPermSlotNumber_Type = Integer32
_NbVlansPermSlotNumber_Object = MibTableColumn
nbVlansPermSlotNumber = _NbVlansPermSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 20, 1, 1),
    _NbVlansPermSlotNumber_Type()
)
nbVlansPermSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermSlotNumber.setStatus("mandatory")


class _NbVlansPermSlotEtherType_Type(Integer32):
    """Custom type nbVlansPermSlotEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbVlansPermSlotEtherType_Type.__name__ = "Integer32"
_NbVlansPermSlotEtherType_Object = MibTableColumn
nbVlansPermSlotEtherType = _NbVlansPermSlotEtherType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 20, 1, 2),
    _NbVlansPermSlotEtherType_Type()
)
nbVlansPermSlotEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermSlotEtherType.setStatus("mandatory")
_NbVlansPermVMANPortTable_Object = MibTable
nbVlansPermVMANPortTable = _NbVlansPermVMANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 22)
)
if mibBuilder.loadTexts:
    nbVlansPermVMANPortTable.setStatus("mandatory")
_NbVlansPermVMANPortEntry_Object = MibTableRow
nbVlansPermVMANPortEntry = _NbVlansPermVMANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 22, 1)
)
nbVlansPermVMANPortEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermVMANPortNumber"),
)
if mibBuilder.loadTexts:
    nbVlansPermVMANPortEntry.setStatus("mandatory")
_NbVlansPermVMANPortNumber_Type = Integer32
_NbVlansPermVMANPortNumber_Object = MibTableColumn
nbVlansPermVMANPortNumber = _NbVlansPermVMANPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 22, 1, 1),
    _NbVlansPermVMANPortNumber_Type()
)
nbVlansPermVMANPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermVMANPortNumber.setStatus("mandatory")


class _NbVlansPermVMANPortMode_Type(Integer32):
    """Custom type nbVlansPermVMANPortMode based on Integer32"""
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
          ("enable", 2),
          ("disable", 3))
    )


_NbVlansPermVMANPortMode_Type.__name__ = "Integer32"
_NbVlansPermVMANPortMode_Object = MibTableColumn
nbVlansPermVMANPortMode = _NbVlansPermVMANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 22, 1, 2),
    _NbVlansPermVMANPortMode_Type()
)
nbVlansPermVMANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermVMANPortMode.setStatus("mandatory")


class _NbVlansPermCPUEtherType_Type(Integer32):
    """Custom type nbVlansPermCPUEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbVlansPermCPUEtherType_Type.__name__ = "Integer32"
_NbVlansPermCPUEtherType_Object = MibScalar
nbVlansPermCPUEtherType = _NbVlansPermCPUEtherType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 23),
    _NbVlansPermCPUEtherType_Type()
)
nbVlansPermCPUEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermCPUEtherType.setStatus("mandatory")
_NbVlansPermMacLimitGroup_ObjectIdentity = ObjectIdentity
nbVlansPermMacLimitGroup = _NbVlansPermMacLimitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 24)
)


class _NbVlansPermPortMacLimitActionMode_Type(Integer32):
    """Custom type nbVlansPermPortMacLimitActionMode based on Integer32"""
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
          ("trapOnly", 2),
          ("portDisable", 3),
          ("discardExceeded", 4))
    )


_NbVlansPermPortMacLimitActionMode_Type.__name__ = "Integer32"
_NbVlansPermPortMacLimitActionMode_Object = MibScalar
nbVlansPermPortMacLimitActionMode = _NbVlansPermPortMacLimitActionMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 24, 1),
    _NbVlansPermPortMacLimitActionMode_Type()
)
nbVlansPermPortMacLimitActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermPortMacLimitActionMode.setStatus("mandatory")
_NbVlansPermPortMacLimitTable_Object = MibTable
nbVlansPermPortMacLimitTable = _NbVlansPermPortMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 24, 10)
)
if mibBuilder.loadTexts:
    nbVlansPermPortMacLimitTable.setStatus("mandatory")
_NbVlansPermPortMacLimitEntry_Object = MibTableRow
nbVlansPermPortMacLimitEntry = _NbVlansPermPortMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 24, 10, 1)
)
nbVlansPermPortMacLimitEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansPermPortMacLimitPortNumber"),
)
if mibBuilder.loadTexts:
    nbVlansPermPortMacLimitEntry.setStatus("mandatory")
_NbVlansPermPortMacLimitPortNumber_Type = Integer32
_NbVlansPermPortMacLimitPortNumber_Object = MibTableColumn
nbVlansPermPortMacLimitPortNumber = _NbVlansPermPortMacLimitPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 24, 10, 1, 1),
    _NbVlansPermPortMacLimitPortNumber_Type()
)
nbVlansPermPortMacLimitPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansPermPortMacLimitPortNumber.setStatus("mandatory")
_NbVlansPermPortMacLimitValue_Type = Integer32
_NbVlansPermPortMacLimitValue_Object = MibTableColumn
nbVlansPermPortMacLimitValue = _NbVlansPermPortMacLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 2, 24, 10, 1, 2),
    _NbVlansPermPortMacLimitValue_Type()
)
nbVlansPermPortMacLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansPermPortMacLimitValue.setStatus("mandatory")
_NbVlansMacTable_Object = MibTable
nbVlansMacTable = _NbVlansMacTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3)
)
if mibBuilder.loadTexts:
    nbVlansMacTable.setStatus("mandatory")
_NbVlansMacEntry_Object = MibTableRow
nbVlansMacEntry = _NbVlansMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1)
)
nbVlansMacEntry.setIndexNames(
    (0, "VLAN-MIB", "nbVlansMacGetViewIndex"),
)
if mibBuilder.loadTexts:
    nbVlansMacEntry.setStatus("mandatory")
_NbVlansMacGetViewIndex_Type = Integer32
_NbVlansMacGetViewIndex_Object = MibTableColumn
nbVlansMacGetViewIndex = _NbVlansMacGetViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 1),
    _NbVlansMacGetViewIndex_Type()
)
nbVlansMacGetViewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansMacGetViewIndex.setStatus("mandatory")
_NbVlansMac_Type = MacAddress
_NbVlansMac_Object = MibTableColumn
nbVlansMac = _NbVlansMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 2),
    _NbVlansMac_Type()
)
nbVlansMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMac.setStatus("mandatory")


class _NbVlansMacVid_Type(Integer32):
    """Custom type nbVlansMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbVlansMacVid_Type.__name__ = "Integer32"
_NbVlansMacVid_Object = MibTableColumn
nbVlansMacVid = _NbVlansMacVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 3),
    _NbVlansMacVid_Type()
)
nbVlansMacVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacVid.setStatus("mandatory")


class _NbVlansMacVidx_Type(Integer32):
    """Custom type nbVlansMacVidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NbVlansMacVidx_Type.__name__ = "Integer32"
_NbVlansMacVidx_Object = MibTableColumn
nbVlansMacVidx = _NbVlansMacVidx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 4),
    _NbVlansMacVidx_Type()
)
nbVlansMacVidx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacVidx.setStatus("mandatory")


class _NbVlansMacPort_Type(Integer32):
    """Custom type nbVlansMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbVlansMacPort_Type.__name__ = "Integer32"
_NbVlansMacPort_Object = MibTableColumn
nbVlansMacPort = _NbVlansMacPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 5),
    _NbVlansMacPort_Type()
)
nbVlansMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacPort.setStatus("mandatory")


class _NbVlansMacStatus_Type(Integer32):
    """Custom type nbVlansMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_NbVlansMacStatus_Type.__name__ = "Integer32"
_NbVlansMacStatus_Object = MibTableColumn
nbVlansMacStatus = _NbVlansMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 6),
    _NbVlansMacStatus_Type()
)
nbVlansMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacStatus.setStatus("mandatory")


class _NbVlansMacTagged_Type(Integer32):
    """Custom type nbVlansMacTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NbVlansMacTagged_Type.__name__ = "Integer32"
_NbVlansMacTagged_Object = MibTableColumn
nbVlansMacTagged = _NbVlansMacTagged_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 7),
    _NbVlansMacTagged_Type()
)
nbVlansMacTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacTagged.setStatus("mandatory")


class _NbVlansMacState_Type(Integer32):
    """Custom type nbVlansMacState based on Integer32"""
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


_NbVlansMacState_Type.__name__ = "Integer32"
_NbVlansMacState_Object = MibTableColumn
nbVlansMacState = _NbVlansMacState_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 8),
    _NbVlansMacState_Type()
)
nbVlansMacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacState.setStatus("mandatory")


class _NbVlansMacPriority_Type(Integer32):
    """Custom type nbVlansMacPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_NbVlansMacPriority_Type.__name__ = "Integer32"
_NbVlansMacPriority_Object = MibTableColumn
nbVlansMacPriority = _NbVlansMacPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 9),
    _NbVlansMacPriority_Type()
)
nbVlansMacPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacPriority.setStatus("mandatory")


class _NbVlansMacFlags_Type(Integer32):
    """Custom type nbVlansMacFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("route", 1))
    )


_NbVlansMacFlags_Type.__name__ = "Integer32"
_NbVlansMacFlags_Object = MibTableColumn
nbVlansMacFlags = _NbVlansMacFlags_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 3, 1, 10),
    _NbVlansMacFlags_Type()
)
nbVlansMacFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacFlags.setStatus("mandatory")
_NbVlansMaxNumMgmtVlans_Type = Integer32
_NbVlansMaxNumMgmtVlans_Object = MibScalar
nbVlansMaxNumMgmtVlans = _NbVlansMaxNumMgmtVlans_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 4),
    _NbVlansMaxNumMgmtVlans_Type()
)
nbVlansMaxNumMgmtVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansMaxNumMgmtVlans.setStatus("mandatory")


class _NbVlansNewVlanIdMode_Type(Integer32):
    """Custom type nbVlansNewVlanIdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enableAddVlanWithoutId", 2))
    )


_NbVlansNewVlanIdMode_Type.__name__ = "Integer32"
_NbVlansNewVlanIdMode_Object = MibScalar
nbVlansNewVlanIdMode = _NbVlansNewVlanIdMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 5),
    _NbVlansNewVlanIdMode_Type()
)
nbVlansNewVlanIdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansNewVlanIdMode.setStatus("mandatory")


class _NbVlansSaveMode_Type(Integer32):
    """Custom type nbVlansSaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("allVlansConfig", 2))
    )


_NbVlansSaveMode_Type.__name__ = "Integer32"
_NbVlansSaveMode_Object = MibScalar
nbVlansSaveMode = _NbVlansSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 6),
    _NbVlansSaveMode_Type()
)
nbVlansSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansSaveMode.setStatus("mandatory")


class _NbVlansDevEtherType_Type(Integer32):
    """Custom type nbVlansDevEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbVlansDevEtherType_Type.__name__ = "Integer32"
_NbVlansDevEtherType_Object = MibScalar
nbVlansDevEtherType = _NbVlansDevEtherType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 7),
    _NbVlansDevEtherType_Type()
)
nbVlansDevEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbVlansDevEtherType.setStatus("mandatory")


class _NbVlansMacLimitSaveCfg_Type(Integer32):
    """Custom type nbVlansMacLimitSaveCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("allPortMacLimit", 2))
    )


_NbVlansMacLimitSaveCfg_Type.__name__ = "Integer32"
_NbVlansMacLimitSaveCfg_Object = MibScalar
nbVlansMacLimitSaveCfg = _NbVlansMacLimitSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 8),
    _NbVlansMacLimitSaveCfg_Type()
)
nbVlansMacLimitSaveCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbVlansMacLimitSaveCfg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

portMacLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 3, 0, 32)
)
portMacLimitExceeded.setObjects(
      *(("VLAN-MIB", "nbVlansRunPortMacLimitPortNumber"),
        ("VLAN-MIB", "nbVlansRunPortMacLimitValue"),
        ("VLAN-MIB", "nbVlansRunPortMacLimitActionDescription"))
)
if mibBuilder.loadTexts:
    portMacLimitExceeded.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VLAN-MIB",
    **{"MacAddress": MacAddress,
       "PortsBitmap": PortsBitmap,
       "nbVlans": nbVlans,
       "portMacLimitExceeded": portMacLimitExceeded,
       "nbVlansRun": nbVlansRun,
       "nbVlansRunVlansMode": nbVlansRunVlansMode,
       "nbVlansRunIngressType": nbVlansRunIngressType,
       "nbVlansRunIngressMode": nbVlansRunIngressMode,
       "nbVlansRunIngressPorts": nbVlansRunIngressPorts,
       "nbVlansRunEgressType": nbVlansRunEgressType,
       "nbVlansRunEgressMode": nbVlansRunEgressMode,
       "nbVlansRunEgressPorts": nbVlansRunEgressPorts,
       "nbVlansRunMgmtTable": nbVlansRunMgmtTable,
       "nbVlansRunMgmtEntry": nbVlansRunMgmtEntry,
       "nbVlansRunMgmtTag": nbVlansRunMgmtTag,
       "nbVlansRunMgmtList": nbVlansRunMgmtList,
       "nbVlansRunMgmtName": nbVlansRunMgmtName,
       "nbVlansRunMgmtTagStatus": nbVlansRunMgmtTagStatus,
       "nbVlansRunSrvrTable": nbVlansRunSrvrTable,
       "nbVlansRunSrvrEntry": nbVlansRunSrvrEntry,
       "nbVlansRunSrvrPort": nbVlansRunSrvrPort,
       "nbVlansRunSrvrPortStatus": nbVlansRunSrvrPortStatus,
       "nbVlansRunSrvrPortTag": nbVlansRunSrvrPortTag,
       "nbVlansRunPortsCfgTable": nbVlansRunPortsCfgTable,
       "nbVlansRunPortsCfgEntry": nbVlansRunPortsCfgEntry,
       "nbVlansRunPort": nbVlansRunPort,
       "nbVlansRunPortPriority": nbVlansRunPortPriority,
       "nbVlansRunPortTagOutMode": nbVlansRunPortTagOutMode,
       "nbVlansRunPriorityPolicy": nbVlansRunPriorityPolicy,
       "nbVlansRunIsvMaxNum": nbVlansRunIsvMaxNum,
       "nbVlansRunIsvTable": nbVlansRunIsvTable,
       "nbVlansRunIsvEntry": nbVlansRunIsvEntry,
       "nbVlansRunIsvIndex": nbVlansRunIsvIndex,
       "nbVlansRunIsvStatus": nbVlansRunIsvStatus,
       "nbVlansRunIsvList": nbVlansRunIsvList,
       "nbVlansRunIsvName": nbVlansRunIsvName,
       "nbVlansRunIsvTag": nbVlansRunIsvTag,
       "nbVlansRunIsvVlanIndex": nbVlansRunIsvVlanIndex,
       "nbVlansRunIsvVlanPriority": nbVlansRunIsvVlanPriority,
       "nbVlansRunVPT2PriorityTable": nbVlansRunVPT2PriorityTable,
       "nbVlansRunVPT2PriorityEntry": nbVlansRunVPT2PriorityEntry,
       "nbVlansRunVPT2PriorVPTNumber": nbVlansRunVPT2PriorVPTNumber,
       "nbVlansRunVPT2PriorPriorNumber": nbVlansRunVPT2PriorPriorNumber,
       "nbVlansRunPriority2VPTTable": nbVlansRunPriority2VPTTable,
       "nbVlansRunPriority2VPTEntry": nbVlansRunPriority2VPTEntry,
       "nbVlansRunPrior2VPTPriorNumber": nbVlansRunPrior2VPTPriorNumber,
       "nbVlansRunPrior2VPTVPTNumber": nbVlansRunPrior2VPTVPTNumber,
       "nbVlansRunSlotEtherTypeTable": nbVlansRunSlotEtherTypeTable,
       "nbVlansRunSlotEtherTypeEntry": nbVlansRunSlotEtherTypeEntry,
       "nbVlansRunSlotNumber": nbVlansRunSlotNumber,
       "nbVlansRunSlotEtherType": nbVlansRunSlotEtherType,
       "nbVlansRunVMANPortTable": nbVlansRunVMANPortTable,
       "nbVlansRunVMANPortEntry": nbVlansRunVMANPortEntry,
       "nbVlansRunVMANPortNumber": nbVlansRunVMANPortNumber,
       "nbVlansRunVMANPortMode": nbVlansRunVMANPortMode,
       "nbVlansRunCPUEtherType": nbVlansRunCPUEtherType,
       "nbVlansRunMacLimitGroup": nbVlansRunMacLimitGroup,
       "nbVlansRunPortMacLimitActionMode": nbVlansRunPortMacLimitActionMode,
       "nbVlansRunPortMacLimitActionDescription": nbVlansRunPortMacLimitActionDescription,
       "nbVlansRunPortMacLimitTable": nbVlansRunPortMacLimitTable,
       "nbVlansRunPortMacLimitEntry": nbVlansRunPortMacLimitEntry,
       "nbVlansRunPortMacLimitPortNumber": nbVlansRunPortMacLimitPortNumber,
       "nbVlansRunPortMacLimitValue": nbVlansRunPortMacLimitValue,
       "nbVlansPerm": nbVlansPerm,
       "nbVlansPermVlansMode": nbVlansPermVlansMode,
       "nbVlansPermIngressType": nbVlansPermIngressType,
       "nbVlansPermIngressMode": nbVlansPermIngressMode,
       "nbVlansPermIngressPorts": nbVlansPermIngressPorts,
       "nbVlansPermEgressType": nbVlansPermEgressType,
       "nbVlansPermEgressMode": nbVlansPermEgressMode,
       "nbVlansPermEgressPorts": nbVlansPermEgressPorts,
       "nbVlansPermMgmtTable": nbVlansPermMgmtTable,
       "nbVlansPermMgmtEntry": nbVlansPermMgmtEntry,
       "nbVlansPermMgmtTag": nbVlansPermMgmtTag,
       "nbVlansPermMgmtList": nbVlansPermMgmtList,
       "nbVlansPermMgmtName": nbVlansPermMgmtName,
       "nbVlansPermMgmtTagStatus": nbVlansPermMgmtTagStatus,
       "nbVlansPermSrvrTable": nbVlansPermSrvrTable,
       "nbVlansPermSrvrEntry": nbVlansPermSrvrEntry,
       "nbVlansPermSrvrPort": nbVlansPermSrvrPort,
       "nbVlansPermSrvrPortStatus": nbVlansPermSrvrPortStatus,
       "nbVlansPermSrvrPortTag": nbVlansPermSrvrPortTag,
       "nbVlansPermPortsCfgTable": nbVlansPermPortsCfgTable,
       "nbVlansPermPortsCfgEntry": nbVlansPermPortsCfgEntry,
       "nbVlansPermPort": nbVlansPermPort,
       "nbVlansPermPortPriority": nbVlansPermPortPriority,
       "nbVlansPermPortTagOutMode": nbVlansPermPortTagOutMode,
       "nbVlansPermPriorityPolicy": nbVlansPermPriorityPolicy,
       "nbVlansPermIsvMaxNum": nbVlansPermIsvMaxNum,
       "nbVlansPermIsvTable": nbVlansPermIsvTable,
       "nbVlansPermIsvEntry": nbVlansPermIsvEntry,
       "nbVlansPermIsvIndex": nbVlansPermIsvIndex,
       "nbVlansPermIsvStatus": nbVlansPermIsvStatus,
       "nbVlansPermIsvList": nbVlansPermIsvList,
       "nbVlansPermIsvName": nbVlansPermIsvName,
       "nbVlansPermIsvTag": nbVlansPermIsvTag,
       "nbVlansPermIsvVlanPriority": nbVlansPermIsvVlanPriority,
       "nbVlansPermVPT2PriorityTable": nbVlansPermVPT2PriorityTable,
       "nbVlansPermVPT2PriorityEntry": nbVlansPermVPT2PriorityEntry,
       "nbVlansPermVPT2PriorVPTNumber": nbVlansPermVPT2PriorVPTNumber,
       "nbVlansPermVPT2PriorPriorNumber": nbVlansPermVPT2PriorPriorNumber,
       "nbVlansPermPriority2VPTTable": nbVlansPermPriority2VPTTable,
       "nbVlansPermPriority2VPTEntry": nbVlansPermPriority2VPTEntry,
       "nbVlansPermPrior2VPTPriorNumber": nbVlansPermPrior2VPTPriorNumber,
       "nbVlansPermPrior2VPTVPTNumber": nbVlansPermPrior2VPTVPTNumber,
       "nbVlansPermSlotEtherTypeTable": nbVlansPermSlotEtherTypeTable,
       "nbVlansPermSlotEtherTypeEntry": nbVlansPermSlotEtherTypeEntry,
       "nbVlansPermSlotNumber": nbVlansPermSlotNumber,
       "nbVlansPermSlotEtherType": nbVlansPermSlotEtherType,
       "nbVlansPermVMANPortTable": nbVlansPermVMANPortTable,
       "nbVlansPermVMANPortEntry": nbVlansPermVMANPortEntry,
       "nbVlansPermVMANPortNumber": nbVlansPermVMANPortNumber,
       "nbVlansPermVMANPortMode": nbVlansPermVMANPortMode,
       "nbVlansPermCPUEtherType": nbVlansPermCPUEtherType,
       "nbVlansPermMacLimitGroup": nbVlansPermMacLimitGroup,
       "nbVlansPermPortMacLimitActionMode": nbVlansPermPortMacLimitActionMode,
       "nbVlansPermPortMacLimitTable": nbVlansPermPortMacLimitTable,
       "nbVlansPermPortMacLimitEntry": nbVlansPermPortMacLimitEntry,
       "nbVlansPermPortMacLimitPortNumber": nbVlansPermPortMacLimitPortNumber,
       "nbVlansPermPortMacLimitValue": nbVlansPermPortMacLimitValue,
       "nbVlansMacTable": nbVlansMacTable,
       "nbVlansMacEntry": nbVlansMacEntry,
       "nbVlansMacGetViewIndex": nbVlansMacGetViewIndex,
       "nbVlansMac": nbVlansMac,
       "nbVlansMacVid": nbVlansMacVid,
       "nbVlansMacVidx": nbVlansMacVidx,
       "nbVlansMacPort": nbVlansMacPort,
       "nbVlansMacStatus": nbVlansMacStatus,
       "nbVlansMacTagged": nbVlansMacTagged,
       "nbVlansMacState": nbVlansMacState,
       "nbVlansMacPriority": nbVlansMacPriority,
       "nbVlansMacFlags": nbVlansMacFlags,
       "nbVlansMaxNumMgmtVlans": nbVlansMaxNumMgmtVlans,
       "nbVlansNewVlanIdMode": nbVlansNewVlanIdMode,
       "nbVlansSaveMode": nbVlansSaveMode,
       "nbVlansDevEtherType": nbVlansDevEtherType,
       "nbVlansMacLimitSaveCfg": nbVlansMacLimitSaveCfg}
)
