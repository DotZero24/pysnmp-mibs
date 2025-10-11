# SNMP MIB module (QTECH-AUTH-GATEWAY-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-AUTH-GATEWAY-CONTEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:07 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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


# MODULE-IDENTITY

qtechWebAuthVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67)
)
if mibBuilder.loadTexts:
    qtechWebAuthVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechWebAuthVCMIBObjects_ObjectIdentity = ObjectIdentity
qtechWebAuthVCMIBObjects = _QtechWebAuthVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1)
)
_QtechWebAuthUserVCTable_Object = MibTable
qtechWebAuthUserVCTable = _QtechWebAuthUserVCTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1)
)
if mibBuilder.loadTexts:
    qtechWebAuthUserVCTable.setStatus("current")
_QtechWebAuthUserVCEntry_Object = MibTableRow
qtechWebAuthUserVCEntry = _QtechWebAuthUserVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1)
)
qtechWebAuthUserVCEntry.setIndexNames(
    (0, "QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"),
    (0, "QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"),
)
if mibBuilder.loadTexts:
    qtechWebAuthUserVCEntry.setStatus("current")


class _AuthUserContextNameVC_Type(DisplayString):
    """Custom type authUserContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AuthUserContextNameVC_Type.__name__ = "DisplayString"
_AuthUserContextNameVC_Object = MibTableColumn
authUserContextNameVC = _AuthUserContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 1),
    _AuthUserContextNameVC_Type()
)
authUserContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserContextNameVC.setStatus("current")
_AuthUserIpAddrVC_Type = IpAddress
_AuthUserIpAddrVC_Object = MibTableColumn
authUserIpAddrVC = _AuthUserIpAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 2),
    _AuthUserIpAddrVC_Type()
)
authUserIpAddrVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserIpAddrVC.setStatus("current")
_AuthUserOnlineFlagVC_Type = Gauge32
_AuthUserOnlineFlagVC_Object = MibTableColumn
authUserOnlineFlagVC = _AuthUserOnlineFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 3),
    _AuthUserOnlineFlagVC_Type()
)
authUserOnlineFlagVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserOnlineFlagVC.setStatus("current")
_AuthUserTimeLimitVC_Type = Gauge32
_AuthUserTimeLimitVC_Object = MibTableColumn
authUserTimeLimitVC = _AuthUserTimeLimitVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 4),
    _AuthUserTimeLimitVC_Type()
)
authUserTimeLimitVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserTimeLimitVC.setStatus("current")
_AuthUserTimeUsedVC_Type = Gauge32
_AuthUserTimeUsedVC_Object = MibTableColumn
authUserTimeUsedVC = _AuthUserTimeUsedVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 5),
    _AuthUserTimeUsedVC_Type()
)
authUserTimeUsedVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTimeUsedVC.setStatus("current")
_AuthUserStatusVC_Type = RowStatus
_AuthUserStatusVC_Object = MibTableColumn
authUserStatusVC = _AuthUserStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 1, 1, 1, 6),
    _AuthUserStatusVC_Type()
)
authUserStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserStatusVC.setStatus("current")
_QtechWebAuthVCMIBConformance_ObjectIdentity = ObjectIdentity
qtechWebAuthVCMIBConformance = _QtechWebAuthVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3)
)
_QtechWebAuthVCMIBCompliances_ObjectIdentity = ObjectIdentity
qtechWebAuthVCMIBCompliances = _QtechWebAuthVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 1)
)
_QtechWebAuthVCMIBGroups_ObjectIdentity = ObjectIdentity
qtechWebAuthVCMIBGroups = _QtechWebAuthVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 2)
)

# Managed Objects groups

qtechWebAuthVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 2, 1)
)
qtechWebAuthVCMIBGroup.setObjects(
      *(("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserContextNameVC"),
        ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserIpAddrVC"),
        ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserOnlineFlagVC"),
        ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeLimitVC"),
        ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserTimeUsedVC"),
        ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "authUserStatusVC"))
)
if mibBuilder.loadTexts:
    qtechWebAuthVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechWebAuthVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 67, 3, 1, 1)
)
qtechWebAuthVCMIBCompliance.setObjects(
    ("QTECH-AUTH-GATEWAY-CONTEXT-MIB", "qtechWebAuthVCMIBGroup")
)
if mibBuilder.loadTexts:
    qtechWebAuthVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-AUTH-GATEWAY-CONTEXT-MIB",
    **{"qtechWebAuthVCMIB": qtechWebAuthVCMIB,
       "qtechWebAuthVCMIBObjects": qtechWebAuthVCMIBObjects,
       "qtechWebAuthUserVCTable": qtechWebAuthUserVCTable,
       "qtechWebAuthUserVCEntry": qtechWebAuthUserVCEntry,
       "authUserContextNameVC": authUserContextNameVC,
       "authUserIpAddrVC": authUserIpAddrVC,
       "authUserOnlineFlagVC": authUserOnlineFlagVC,
       "authUserTimeLimitVC": authUserTimeLimitVC,
       "authUserTimeUsedVC": authUserTimeUsedVC,
       "authUserStatusVC": authUserStatusVC,
       "qtechWebAuthVCMIBConformance": qtechWebAuthVCMIBConformance,
       "qtechWebAuthVCMIBCompliances": qtechWebAuthVCMIBCompliances,
       "qtechWebAuthVCMIBCompliance": qtechWebAuthVCMIBCompliance,
       "qtechWebAuthVCMIBGroups": qtechWebAuthVCMIBGroups,
       "qtechWebAuthVCMIBGroup": qtechWebAuthVCMIBGroup}
)
