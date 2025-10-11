# SNMP MIB module (NEWTEC-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:15 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcNetworkAddress) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcNetworkAddress")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcIp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400)
)
if mibBuilder.loadTexts:
    ntcIp.setRevisions(
        ("2017-07-10 12:00",
         "2014-02-03 12:00",
         "2013-01-08 12:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcIpObjects_ObjectIdentity = ObjectIdentity
ntcIpObjects = _NtcIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1)
)
if mibBuilder.loadTexts:
    ntcIpObjects.setStatus("current")
_NtcIpMgmtInterfaceTable_Object = MibTable
ntcIpMgmtInterfaceTable = _NtcIpMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 1)
)
if mibBuilder.loadTexts:
    ntcIpMgmtInterfaceTable.setStatus("current")
_NtcIpMgmtInterfaceEntry_Object = MibTableRow
ntcIpMgmtInterfaceEntry = _NtcIpMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 1, 1)
)
ntcIpMgmtInterfaceEntry.setIndexNames(
    (0, "NEWTEC-IP-MIB", "ntcIpMgmtInterfaceName"),
)
if mibBuilder.loadTexts:
    ntcIpMgmtInterfaceEntry.setStatus("current")


class _NtcIpMgmtInterfaceName_Type(Integer32):
    """Custom type ntcIpMgmtInterfaceName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgmt1", 0),
          ("mgmt2", 1),
          ("mgmtfp", 2),
          ("mgmt", 3))
    )


_NtcIpMgmtInterfaceName_Type.__name__ = "Integer32"
_NtcIpMgmtInterfaceName_Object = MibTableColumn
ntcIpMgmtInterfaceName = _NtcIpMgmtInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 1, 1, 1),
    _NtcIpMgmtInterfaceName_Type()
)
ntcIpMgmtInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcIpMgmtInterfaceName.setStatus("current")


class _NtcIpMgmtInterfaceIpAddress_Type(NtcNetworkAddress):
    """Custom type ntcIpMgmtInterfaceIpAddress based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0/24")


_NtcIpMgmtInterfaceIpAddress_Type.__name__ = "NtcNetworkAddress"
_NtcIpMgmtInterfaceIpAddress_Object = MibTableColumn
ntcIpMgmtInterfaceIpAddress = _NtcIpMgmtInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 1, 1, 2),
    _NtcIpMgmtInterfaceIpAddress_Type()
)
ntcIpMgmtInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcIpMgmtInterfaceIpAddress.setStatus("current")


class _NtcIpMgmtInterfaceState_Type(Integer32):
    """Custom type ntcIpMgmtInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcIpMgmtInterfaceState_Type.__name__ = "Integer32"
_NtcIpMgmtInterfaceState_Object = MibTableColumn
ntcIpMgmtInterfaceState = _NtcIpMgmtInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 1, 1, 3),
    _NtcIpMgmtInterfaceState_Type()
)
ntcIpMgmtInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIpMgmtInterfaceState.setStatus("current")


class _NtcIpMgmtInterfaceVirtualIpAddr_Type(NtcNetworkAddress):
    """Custom type ntcIpMgmtInterfaceVirtualIpAddr based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0/24")


_NtcIpMgmtInterfaceVirtualIpAddr_Type.__name__ = "NtcNetworkAddress"
_NtcIpMgmtInterfaceVirtualIpAddr_Object = MibTableColumn
ntcIpMgmtInterfaceVirtualIpAddr = _NtcIpMgmtInterfaceVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 1, 1, 4),
    _NtcIpMgmtInterfaceVirtualIpAddr_Type()
)
ntcIpMgmtInterfaceVirtualIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcIpMgmtInterfaceVirtualIpAddr.setStatus("current")


class _NtcMgmtGateway_Type(IpAddress):
    """Custom type ntcMgmtGateway based on IpAddress"""
    defaultHexValue = "00000000"


_NtcMgmtGateway_Type.__name__ = "IpAddress"
_NtcMgmtGateway_Object = MibScalar
ntcMgmtGateway = _NtcMgmtGateway_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 2),
    _NtcMgmtGateway_Type()
)
ntcMgmtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMgmtGateway.setStatus("current")
_NtcDataInterfaceTable_Object = MibTable
ntcDataInterfaceTable = _NtcDataInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 3)
)
if mibBuilder.loadTexts:
    ntcDataInterfaceTable.setStatus("current")
_NtcDataInterfaceEntry_Object = MibTableRow
ntcDataInterfaceEntry = _NtcDataInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 3, 1)
)
ntcDataInterfaceEntry.setIndexNames(
    (0, "NEWTEC-IP-MIB", "ntcDataInterfaceName"),
)
if mibBuilder.loadTexts:
    ntcDataInterfaceEntry.setStatus("current")


class _NtcDataInterfaceName_Type(Integer32):
    """Custom type ntcDataInterfaceName based on Integer32"""
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
        *(("data1", 0),
          ("data2", 1),
          ("data", 2),
          ("sat1", 3),
          ("sat2", 4),
          ("sat", 5))
    )


_NtcDataInterfaceName_Type.__name__ = "Integer32"
_NtcDataInterfaceName_Object = MibTableColumn
ntcDataInterfaceName = _NtcDataInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 3, 1, 1),
    _NtcDataInterfaceName_Type()
)
ntcDataInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcDataInterfaceName.setStatus("current")


class _NtcDataInterfaceIpAddress_Type(NtcNetworkAddress):
    """Custom type ntcDataInterfaceIpAddress based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0/24")


_NtcDataInterfaceIpAddress_Type.__name__ = "NtcNetworkAddress"
_NtcDataInterfaceIpAddress_Object = MibTableColumn
ntcDataInterfaceIpAddress = _NtcDataInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 3, 1, 2),
    _NtcDataInterfaceIpAddress_Type()
)
ntcDataInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDataInterfaceIpAddress.setStatus("current")


class _NtcDataInterfaceState_Type(Integer32):
    """Custom type ntcDataInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDataInterfaceState_Type.__name__ = "Integer32"
_NtcDataInterfaceState_Object = MibTableColumn
ntcDataInterfaceState = _NtcDataInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 3, 1, 3),
    _NtcDataInterfaceState_Type()
)
ntcDataInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDataInterfaceState.setStatus("current")


class _NtcDataInterfaceFysIpAddress_Type(NtcNetworkAddress):
    """Custom type ntcDataInterfaceFysIpAddress based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0/24")


_NtcDataInterfaceFysIpAddress_Type.__name__ = "NtcNetworkAddress"
_NtcDataInterfaceFysIpAddress_Object = MibTableColumn
ntcDataInterfaceFysIpAddress = _NtcDataInterfaceFysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 3, 1, 4),
    _NtcDataInterfaceFysIpAddress_Type()
)
ntcDataInterfaceFysIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDataInterfaceFysIpAddress.setStatus("current")


class _NtcDataGateway_Type(IpAddress):
    """Custom type ntcDataGateway based on IpAddress"""
    defaultHexValue = "00000000"


_NtcDataGateway_Type.__name__ = "IpAddress"
_NtcDataGateway_Object = MibScalar
ntcDataGateway = _NtcDataGateway_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 4),
    _NtcDataGateway_Type()
)
ntcDataGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDataGateway.setStatus("current")
_NtcIpAlarm_ObjectIdentity = ObjectIdentity
ntcIpAlarm = _NtcIpAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 5)
)
if mibBuilder.loadTexts:
    ntcIpAlarm.setStatus("current")
_NtcIpAlmGwUnreachable_Type = NtcAlarmState
_NtcIpAlmGwUnreachable_Object = MibScalar
ntcIpAlmGwUnreachable = _NtcIpAlmGwUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 1, 5, 1),
    _NtcIpAlmGwUnreachable_Type()
)
ntcIpAlmGwUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIpAlmGwUnreachable.setStatus("current")
_NtcIpConformance_ObjectIdentity = ObjectIdentity
ntcIpConformance = _NtcIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 2)
)
if mibBuilder.loadTexts:
    ntcIpConformance.setStatus("current")
_NtcIpConfCompliance_ObjectIdentity = ObjectIdentity
ntcIpConfCompliance = _NtcIpConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 2, 1)
)
if mibBuilder.loadTexts:
    ntcIpConfCompliance.setStatus("current")
_NtcIpConfGroup_ObjectIdentity = ObjectIdentity
ntcIpConfGroup = _NtcIpConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 2, 2)
)
if mibBuilder.loadTexts:
    ntcIpConfGroup.setStatus("current")

# Managed Objects groups

ntcIpConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 2, 2, 1)
)
ntcIpConfGrpV1Standard.setObjects(
      *(("NEWTEC-IP-MIB", "ntcIpMgmtInterfaceIpAddress"),
        ("NEWTEC-IP-MIB", "ntcIpMgmtInterfaceState"),
        ("NEWTEC-IP-MIB", "ntcIpMgmtInterfaceVirtualIpAddr"),
        ("NEWTEC-IP-MIB", "ntcMgmtGateway"),
        ("NEWTEC-IP-MIB", "ntcDataInterfaceIpAddress"),
        ("NEWTEC-IP-MIB", "ntcDataInterfaceState"),
        ("NEWTEC-IP-MIB", "ntcDataInterfaceFysIpAddress"),
        ("NEWTEC-IP-MIB", "ntcDataGateway"),
        ("NEWTEC-IP-MIB", "ntcIpAlmGwUnreachable"))
)
if mibBuilder.loadTexts:
    ntcIpConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcIpConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 400, 2, 1, 1)
)
ntcIpConfCompV1Standard.setObjects(
    ("NEWTEC-IP-MIB", "ntcIpConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcIpConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-IP-MIB",
    **{"ntcIp": ntcIp,
       "ntcIpObjects": ntcIpObjects,
       "ntcIpMgmtInterfaceTable": ntcIpMgmtInterfaceTable,
       "ntcIpMgmtInterfaceEntry": ntcIpMgmtInterfaceEntry,
       "ntcIpMgmtInterfaceName": ntcIpMgmtInterfaceName,
       "ntcIpMgmtInterfaceIpAddress": ntcIpMgmtInterfaceIpAddress,
       "ntcIpMgmtInterfaceState": ntcIpMgmtInterfaceState,
       "ntcIpMgmtInterfaceVirtualIpAddr": ntcIpMgmtInterfaceVirtualIpAddr,
       "ntcMgmtGateway": ntcMgmtGateway,
       "ntcDataInterfaceTable": ntcDataInterfaceTable,
       "ntcDataInterfaceEntry": ntcDataInterfaceEntry,
       "ntcDataInterfaceName": ntcDataInterfaceName,
       "ntcDataInterfaceIpAddress": ntcDataInterfaceIpAddress,
       "ntcDataInterfaceState": ntcDataInterfaceState,
       "ntcDataInterfaceFysIpAddress": ntcDataInterfaceFysIpAddress,
       "ntcDataGateway": ntcDataGateway,
       "ntcIpAlarm": ntcIpAlarm,
       "ntcIpAlmGwUnreachable": ntcIpAlmGwUnreachable,
       "ntcIpConformance": ntcIpConformance,
       "ntcIpConfCompliance": ntcIpConfCompliance,
       "ntcIpConfCompV1Standard": ntcIpConfCompV1Standard,
       "ntcIpConfGroup": ntcIpConfGroup,
       "ntcIpConfGrpV1Standard": ntcIpConfGrpV1Standard}
)
