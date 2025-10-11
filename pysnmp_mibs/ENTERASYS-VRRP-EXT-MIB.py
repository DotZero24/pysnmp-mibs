# SNMP MIB module (ENTERASYS-VRRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-VRRP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:27 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(VrId,
 vrrpOperationsInetAddrType) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId",
    "vrrpOperationsInetAddrType")


# MODULE-IDENTITY

etsysVrrpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64)
)
if mibBuilder.loadTexts:
    etsysVrrpExtMIB.setRevisions(
        ("2011-10-27 14:29",
         "2009-08-10 19:43")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysVrrpExtOperations_ObjectIdentity = ObjectIdentity
etsysVrrpExtOperations = _EtsysVrrpExtOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1)
)
_EtsysVrrpExtOperTable_Object = MibTable
etsysVrrpExtOperTable = _EtsysVrrpExtOperTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1)
)
if mibBuilder.loadTexts:
    etsysVrrpExtOperTable.setStatus("current")
_EtsysVrrpExtOperEntry_Object = MibTableRow
etsysVrrpExtOperEntry = _EtsysVrrpExtOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1)
)
etsysVrrpExtOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperVrId"),
)
if mibBuilder.loadTexts:
    etsysVrrpExtOperEntry.setStatus("current")
_EtsysVrrpExtOperVrId_Type = VrId
_EtsysVrrpExtOperVrId_Object = MibTableColumn
etsysVrrpExtOperVrId = _EtsysVrrpExtOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 1),
    _EtsysVrrpExtOperVrId_Type()
)
etsysVrrpExtOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysVrrpExtOperVrId.setStatus("current")


class _EtsysVrrpExtOperState_Type(Integer32):
    """Custom type etsysVrrpExtOperState based on Integer32"""
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
        *(("initialize", 1),
          ("backup", 2),
          ("master", 3),
          ("ifDown", 4),
          ("preemptDelay", 5))
    )


_EtsysVrrpExtOperState_Type.__name__ = "Integer32"
_EtsysVrrpExtOperState_Object = MibTableColumn
etsysVrrpExtOperState = _EtsysVrrpExtOperState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 2),
    _EtsysVrrpExtOperState_Type()
)
etsysVrrpExtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVrrpExtOperState.setStatus("current")


class _EtsysVrrpExtOperAcceptMode_Type(Integer32):
    """Custom type etsysVrrpExtOperAcceptMode based on Integer32"""
    defaultValue = 2

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


_EtsysVrrpExtOperAcceptMode_Type.__name__ = "Integer32"
_EtsysVrrpExtOperAcceptMode_Object = MibTableColumn
etsysVrrpExtOperAcceptMode = _EtsysVrrpExtOperAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 3),
    _EtsysVrrpExtOperAcceptMode_Type()
)
etsysVrrpExtOperAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVrrpExtOperAcceptMode.setStatus("current")


class _EtsysVrrpExtOperPreemptModeDelay_Type(Integer32):
    """Custom type etsysVrrpExtOperPreemptModeDelay based on Integer32"""
    defaultValue = 0


_EtsysVrrpExtOperPreemptModeDelay_Type.__name__ = "Integer32"
_EtsysVrrpExtOperPreemptModeDelay_Object = MibTableColumn
etsysVrrpExtOperPreemptModeDelay = _EtsysVrrpExtOperPreemptModeDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 4),
    _EtsysVrrpExtOperPreemptModeDelay_Type()
)
etsysVrrpExtOperPreemptModeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVrrpExtOperPreemptModeDelay.setStatus("current")
_EtsysVrrpExtOperCriticalIpAddrCount_Type = Integer32
_EtsysVrrpExtOperCriticalIpAddrCount_Object = MibTableColumn
etsysVrrpExtOperCriticalIpAddrCount = _EtsysVrrpExtOperCriticalIpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 5),
    _EtsysVrrpExtOperCriticalIpAddrCount_Type()
)
etsysVrrpExtOperCriticalIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVrrpExtOperCriticalIpAddrCount.setStatus("current")


class _EtsysVrrpExtOperFabricRouteMode_Type(Integer32):
    """Custom type etsysVrrpExtOperFabricRouteMode based on Integer32"""
    defaultValue = 2

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


_EtsysVrrpExtOperFabricRouteMode_Type.__name__ = "Integer32"
_EtsysVrrpExtOperFabricRouteMode_Object = MibTableColumn
etsysVrrpExtOperFabricRouteMode = _EtsysVrrpExtOperFabricRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 6),
    _EtsysVrrpExtOperFabricRouteMode_Type()
)
etsysVrrpExtOperFabricRouteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVrrpExtOperFabricRouteMode.setStatus("current")
_EtsysVrrpExtCriticalIpAddrTable_Object = MibTable
etsysVrrpExtCriticalIpAddrTable = _EtsysVrrpExtCriticalIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2)
)
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrTable.setStatus("current")
_EtsysVrrpExtCriticalIpAddrEntry_Object = MibTableRow
etsysVrrpExtCriticalIpAddrEntry = _EtsysVrrpExtCriticalIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1)
)
etsysVrrpExtCriticalIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperVrId"),
    (0, "VRRP-MIB", "vrrpOperationsInetAddrType"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddr"),
)
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrEntry.setStatus("current")


class _EtsysVrrpExtCriticalIpAddr_Type(InetAddress):
    """Custom type etsysVrrpExtCriticalIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysVrrpExtCriticalIpAddr_Type.__name__ = "InetAddress"
_EtsysVrrpExtCriticalIpAddr_Object = MibTableColumn
etsysVrrpExtCriticalIpAddr = _EtsysVrrpExtCriticalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 1),
    _EtsysVrrpExtCriticalIpAddr_Type()
)
etsysVrrpExtCriticalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddr.setStatus("current")


class _EtsysVrrpExtCriticalIpAddrPriority_Type(Integer32):
    """Custom type etsysVrrpExtCriticalIpAddrPriority based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_EtsysVrrpExtCriticalIpAddrPriority_Type.__name__ = "Integer32"
_EtsysVrrpExtCriticalIpAddrPriority_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrPriority = _EtsysVrrpExtCriticalIpAddrPriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 2),
    _EtsysVrrpExtCriticalIpAddrPriority_Type()
)
etsysVrrpExtCriticalIpAddrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrPriority.setStatus("current")


class _EtsysVrrpExtCriticalIpAddrState_Type(Integer32):
    """Custom type etsysVrrpExtCriticalIpAddrState based on Integer32"""
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


_EtsysVrrpExtCriticalIpAddrState_Type.__name__ = "Integer32"
_EtsysVrrpExtCriticalIpAddrState_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrState = _EtsysVrrpExtCriticalIpAddrState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 3),
    _EtsysVrrpExtCriticalIpAddrState_Type()
)
etsysVrrpExtCriticalIpAddrState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrState.setStatus("current")
_EtsysVrrpExtCriticalIpAddrRowStatus_Type = RowStatus
_EtsysVrrpExtCriticalIpAddrRowStatus_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrRowStatus = _EtsysVrrpExtCriticalIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 4),
    _EtsysVrrpExtCriticalIpAddrRowStatus_Type()
)
etsysVrrpExtCriticalIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrRowStatus.setStatus("current")


class _EtsysVrrpExtCriticalIpAddrProbe_Type(Integer32):
    """Custom type etsysVrrpExtCriticalIpAddrProbe based on Integer32"""
    defaultValue = 2

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


_EtsysVrrpExtCriticalIpAddrProbe_Type.__name__ = "Integer32"
_EtsysVrrpExtCriticalIpAddrProbe_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrProbe = _EtsysVrrpExtCriticalIpAddrProbe_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 5),
    _EtsysVrrpExtCriticalIpAddrProbe_Type()
)
etsysVrrpExtCriticalIpAddrProbe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrProbe.setStatus("current")


class _EtsysVrrpExtCriticalIpAddrProbeName_Type(SnmpAdminString):
    """Custom type etsysVrrpExtCriticalIpAddrProbeName based on SnmpAdminString"""
    defaultValue = OctetString("$vrrp_default")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysVrrpExtCriticalIpAddrProbeName_Type.__name__ = "SnmpAdminString"
_EtsysVrrpExtCriticalIpAddrProbeName_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrProbeName = _EtsysVrrpExtCriticalIpAddrProbeName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 6),
    _EtsysVrrpExtCriticalIpAddrProbeName_Type()
)
etsysVrrpExtCriticalIpAddrProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrProbeName.setStatus("current")
_EtsysVrrpExtTrackedObjTable_Object = MibTable
etsysVrrpExtTrackedObjTable = _EtsysVrrpExtTrackedObjTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 3)
)
if mibBuilder.loadTexts:
    etsysVrrpExtTrackedObjTable.setStatus("current")
_EtsysVrrpExtTrackedObjEntry_Object = MibTableRow
etsysVrrpExtTrackedObjEntry = _EtsysVrrpExtTrackedObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 3, 1)
)
etsysVrrpExtTrackedObjEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperVrId"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtTrackedObjName"),
)
if mibBuilder.loadTexts:
    etsysVrrpExtTrackedObjEntry.setStatus("current")


class _EtsysVrrpExtTrackedObjName_Type(SnmpAdminString):
    """Custom type etsysVrrpExtTrackedObjName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysVrrpExtTrackedObjName_Type.__name__ = "SnmpAdminString"
_EtsysVrrpExtTrackedObjName_Object = MibTableColumn
etsysVrrpExtTrackedObjName = _EtsysVrrpExtTrackedObjName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 3, 1, 1),
    _EtsysVrrpExtTrackedObjName_Type()
)
etsysVrrpExtTrackedObjName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysVrrpExtTrackedObjName.setStatus("current")


class _EtsysVrrpExtTrackedObjPriority_Type(Integer32):
    """Custom type etsysVrrpExtTrackedObjPriority based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_EtsysVrrpExtTrackedObjPriority_Type.__name__ = "Integer32"
_EtsysVrrpExtTrackedObjPriority_Object = MibTableColumn
etsysVrrpExtTrackedObjPriority = _EtsysVrrpExtTrackedObjPriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 3, 1, 2),
    _EtsysVrrpExtTrackedObjPriority_Type()
)
etsysVrrpExtTrackedObjPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtTrackedObjPriority.setStatus("current")


class _EtsysVrrpExtTrackedObjState_Type(Integer32):
    """Custom type etsysVrrpExtTrackedObjState based on Integer32"""
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


_EtsysVrrpExtTrackedObjState_Type.__name__ = "Integer32"
_EtsysVrrpExtTrackedObjState_Object = MibTableColumn
etsysVrrpExtTrackedObjState = _EtsysVrrpExtTrackedObjState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 3, 1, 3),
    _EtsysVrrpExtTrackedObjState_Type()
)
etsysVrrpExtTrackedObjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVrrpExtTrackedObjState.setStatus("current")
_EtsysVrrpExtTrackedObjRowStatus_Type = RowStatus
_EtsysVrrpExtTrackedObjRowStatus_Object = MibTableColumn
etsysVrrpExtTrackedObjRowStatus = _EtsysVrrpExtTrackedObjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 3, 1, 4),
    _EtsysVrrpExtTrackedObjRowStatus_Type()
)
etsysVrrpExtTrackedObjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtTrackedObjRowStatus.setStatus("current")
_EtsysVrrpExtConformance_ObjectIdentity = ObjectIdentity
etsysVrrpExtConformance = _EtsysVrrpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2)
)
_EtsysVrrpExtMIBCompliances_ObjectIdentity = ObjectIdentity
etsysVrrpExtMIBCompliances = _EtsysVrrpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 1)
)
_EtsysVrrpExtMIBGroups_ObjectIdentity = ObjectIdentity
etsysVrrpExtMIBGroups = _EtsysVrrpExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 2)
)

# Managed Objects groups

etsysVrrpExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 2, 1)
)
etsysVrrpExtMIBGroup.setObjects(
      *(("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperState"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperAcceptMode"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperPreemptModeDelay"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperCriticalIpAddrCount"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrPriority"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrState"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    etsysVrrpExtMIBGroup.setStatus("deprecated")

etsysVrrpExtOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 2, 2)
)
etsysVrrpExtOperGroup.setObjects(
      *(("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperState"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperAcceptMode"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperPreemptModeDelay"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperCriticalIpAddrCount"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperFabricRouteMode"))
)
if mibBuilder.loadTexts:
    etsysVrrpExtOperGroup.setStatus("current")

etsysVrrpExtCriticalIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 2, 3)
)
etsysVrrpExtCriticalIpGroup.setObjects(
      *(("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrPriority"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrState"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrRowStatus"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrProbe"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrProbeName"))
)
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpGroup.setStatus("current")

etsysVrrpExtTrackedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 2, 4)
)
etsysVrrpExtTrackedObjectGroup.setObjects(
      *(("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtTrackedObjPriority"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtTrackedObjState"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtTrackedObjRowStatus"))
)
if mibBuilder.loadTexts:
    etsysVrrpExtTrackedObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysVrrpExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 1, 1)
)
etsysVrrpExtMIBCompliance.setObjects(
    ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtMIBGroup")
)
if mibBuilder.loadTexts:
    etsysVrrpExtMIBCompliance.setStatus(
        "deprecated"
    )

etsysVrrpExtMIBv2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 1, 2)
)
etsysVrrpExtMIBv2Compliance.setObjects(
      *(("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperGroup"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpGroup"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtTrackedObjectGroup"))
)
if mibBuilder.loadTexts:
    etsysVrrpExtMIBv2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-VRRP-EXT-MIB",
    **{"etsysVrrpExtMIB": etsysVrrpExtMIB,
       "etsysVrrpExtOperations": etsysVrrpExtOperations,
       "etsysVrrpExtOperTable": etsysVrrpExtOperTable,
       "etsysVrrpExtOperEntry": etsysVrrpExtOperEntry,
       "etsysVrrpExtOperVrId": etsysVrrpExtOperVrId,
       "etsysVrrpExtOperState": etsysVrrpExtOperState,
       "etsysVrrpExtOperAcceptMode": etsysVrrpExtOperAcceptMode,
       "etsysVrrpExtOperPreemptModeDelay": etsysVrrpExtOperPreemptModeDelay,
       "etsysVrrpExtOperCriticalIpAddrCount": etsysVrrpExtOperCriticalIpAddrCount,
       "etsysVrrpExtOperFabricRouteMode": etsysVrrpExtOperFabricRouteMode,
       "etsysVrrpExtCriticalIpAddrTable": etsysVrrpExtCriticalIpAddrTable,
       "etsysVrrpExtCriticalIpAddrEntry": etsysVrrpExtCriticalIpAddrEntry,
       "etsysVrrpExtCriticalIpAddr": etsysVrrpExtCriticalIpAddr,
       "etsysVrrpExtCriticalIpAddrPriority": etsysVrrpExtCriticalIpAddrPriority,
       "etsysVrrpExtCriticalIpAddrState": etsysVrrpExtCriticalIpAddrState,
       "etsysVrrpExtCriticalIpAddrRowStatus": etsysVrrpExtCriticalIpAddrRowStatus,
       "etsysVrrpExtCriticalIpAddrProbe": etsysVrrpExtCriticalIpAddrProbe,
       "etsysVrrpExtCriticalIpAddrProbeName": etsysVrrpExtCriticalIpAddrProbeName,
       "etsysVrrpExtTrackedObjTable": etsysVrrpExtTrackedObjTable,
       "etsysVrrpExtTrackedObjEntry": etsysVrrpExtTrackedObjEntry,
       "etsysVrrpExtTrackedObjName": etsysVrrpExtTrackedObjName,
       "etsysVrrpExtTrackedObjPriority": etsysVrrpExtTrackedObjPriority,
       "etsysVrrpExtTrackedObjState": etsysVrrpExtTrackedObjState,
       "etsysVrrpExtTrackedObjRowStatus": etsysVrrpExtTrackedObjRowStatus,
       "etsysVrrpExtConformance": etsysVrrpExtConformance,
       "etsysVrrpExtMIBCompliances": etsysVrrpExtMIBCompliances,
       "etsysVrrpExtMIBCompliance": etsysVrrpExtMIBCompliance,
       "etsysVrrpExtMIBv2Compliance": etsysVrrpExtMIBv2Compliance,
       "etsysVrrpExtMIBGroups": etsysVrrpExtMIBGroups,
       "etsysVrrpExtMIBGroup": etsysVrrpExtMIBGroup,
       "etsysVrrpExtOperGroup": etsysVrrpExtOperGroup,
       "etsysVrrpExtCriticalIpGroup": etsysVrrpExtCriticalIpGroup,
       "etsysVrrpExtTrackedObjectGroup": etsysVrrpExtTrackedObjectGroup}
)
