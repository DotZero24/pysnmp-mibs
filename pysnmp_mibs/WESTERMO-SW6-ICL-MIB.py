# SNMP MIB module (WESTERMO-SW6-ICL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-SW6-ICL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:32 2025
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

icl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5)
)
if mibBuilder.loadTexts:
    icl.setRevisions(
        ("2019-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1)
)
_CfgIcl_ObjectIdentity = ObjectIdentity
cfgIcl = _CfgIcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1)
)


class _CfgIclEnabled_Type(Integer32):
    """Custom type cfgIclEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgIclEnabled_Type.__name__ = "Integer32"
_CfgIclEnabled_Object = MibScalar
cfgIclEnabled = _CfgIclEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 1),
    _CfgIclEnabled_Type()
)
cfgIclEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclEnabled.setStatus("current")


class _CfgIclConnectionDelay_Type(Integer32):
    """Custom type cfgIclConnectionDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CfgIclConnectionDelay_Type.__name__ = "Integer32"
_CfgIclConnectionDelay_Object = MibScalar
cfgIclConnectionDelay = _CfgIclConnectionDelay_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 2),
    _CfgIclConnectionDelay_Type()
)
cfgIclConnectionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclConnectionDelay.setStatus("current")


class _CfgIclConnectionThreshold_Type(Integer32):
    """Custom type cfgIclConnectionThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_CfgIclConnectionThreshold_Type.__name__ = "Integer32"
_CfgIclConnectionThreshold_Object = MibScalar
cfgIclConnectionThreshold = _CfgIclConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 3),
    _CfgIclConnectionThreshold_Type()
)
cfgIclConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclConnectionThreshold.setStatus("current")


class _CfgIclDisconnectionDelay_Type(Integer32):
    """Custom type cfgIclDisconnectionDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CfgIclDisconnectionDelay_Type.__name__ = "Integer32"
_CfgIclDisconnectionDelay_Object = MibScalar
cfgIclDisconnectionDelay = _CfgIclDisconnectionDelay_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 4),
    _CfgIclDisconnectionDelay_Type()
)
cfgIclDisconnectionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclDisconnectionDelay.setStatus("current")


class _CfgIclDisconnectionThreshold_Type(Integer32):
    """Custom type cfgIclDisconnectionThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_CfgIclDisconnectionThreshold_Type.__name__ = "Integer32"
_CfgIclDisconnectionThreshold_Object = MibScalar
cfgIclDisconnectionThreshold = _CfgIclDisconnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 5),
    _CfgIclDisconnectionThreshold_Type()
)
cfgIclDisconnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclDisconnectionThreshold.setStatus("current")


class _CfgIclInterfaceName_Type(DisplayString):
    """Custom type cfgIclInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgIclInterfaceName_Type.__name__ = "DisplayString"
_CfgIclInterfaceName_Object = MibScalar
cfgIclInterfaceName = _CfgIclInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 6),
    _CfgIclInterfaceName_Type()
)
cfgIclInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclInterfaceName.setStatus("current")


class _CfgIclCycleTime_Type(Integer32):
    """Custom type cfgIclCycleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_CfgIclCycleTime_Type.__name__ = "Integer32"
_CfgIclCycleTime_Object = MibScalar
cfgIclCycleTime = _CfgIclCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 7),
    _CfgIclCycleTime_Type()
)
cfgIclCycleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclCycleTime.setStatus("current")


class _CfgIclBlacklistTime_Type(Integer32):
    """Custom type cfgIclBlacklistTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CfgIclBlacklistTime_Type.__name__ = "Integer32"
_CfgIclBlacklistTime_Object = MibScalar
cfgIclBlacklistTime = _CfgIclBlacklistTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 8),
    _CfgIclBlacklistTime_Type()
)
cfgIclBlacklistTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclBlacklistTime.setStatus("current")


class _CfgIclSuspended_Type(Integer32):
    """Custom type cfgIclSuspended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resumed", 0),
          ("suspended", 1))
    )


_CfgIclSuspended_Type.__name__ = "Integer32"
_CfgIclSuspended_Object = MibScalar
cfgIclSuspended = _CfgIclSuspended_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 1, 1, 9),
    _CfgIclSuspended_Type()
)
cfgIclSuspended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIclSuspended.setStatus("current")
_Rpc_ObjectIdentity = ObjectIdentity
rpc = _Rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 3)
)
_RpcIcl_ObjectIdentity = ObjectIdentity
rpcIcl = _RpcIcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 3, 1)
)


class _RpcIclForceDisconnect_Type(Integer32):
    """Custom type rpcIclForceDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("disconnect", 1))
    )


_RpcIclForceDisconnect_Type.__name__ = "Integer32"
_RpcIclForceDisconnect_Object = MibScalar
rpcIclForceDisconnect = _RpcIclForceDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 3, 1, 1),
    _RpcIclForceDisconnect_Type()
)
rpcIclForceDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcIclForceDisconnect.setStatus("current")


class _RpcIclClearBlacklist_Type(Integer32):
    """Custom type rpcIclClearBlacklist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("clear", 1))
    )


_RpcIclClearBlacklist_Type.__name__ = "Integer32"
_RpcIclClearBlacklist_Object = MibScalar
rpcIclClearBlacklist = _RpcIclClearBlacklist_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 3, 1, 2),
    _RpcIclClearBlacklist_Type()
)
rpcIclClearBlacklist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcIclClearBlacklist.setStatus("current")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 4)
)
_SetIcl_ObjectIdentity = ObjectIdentity
setIcl = _SetIcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 4, 1)
)


class _SetIclSuspended_Type(Integer32):
    """Custom type setIclSuspended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resumed", 0),
          ("suspended", 1))
    )


_SetIclSuspended_Type.__name__ = "Integer32"
_SetIclSuspended_Object = MibScalar
setIclSuspended = _SetIclSuspended_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 4, 1, 1),
    _SetIclSuspended_Type()
)
setIclSuspended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIclSuspended.setStatus("current")
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 6)
)
_SwIcl_ObjectIdentity = ObjectIdentity
swIcl = _SwIcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 6, 1)
)


class _SwIclStatus_Type(Integer32):
    """Custom type swIclStatus based on Integer32"""
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
        *(("disabled", 0),
          ("scanning", 1),
          ("connected", 2),
          ("suspended", 3))
    )


_SwIclStatus_Type.__name__ = "Integer32"
_SwIclStatus_Object = MibScalar
swIclStatus = _SwIclStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 6, 1, 1),
    _SwIclStatus_Type()
)
swIclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIclStatus.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1)
)
_GroupConfiguration_ObjectIdentity = ObjectIdentity
groupConfiguration = _GroupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 1)
)
_GroupRpc_ObjectIdentity = ObjectIdentity
groupRpc = _GroupRpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 2)
)
_GroupSettings_ObjectIdentity = ObjectIdentity
groupSettings = _GroupSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 3)
)
_GroupSoftware_ObjectIdentity = ObjectIdentity
groupSoftware = _GroupSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 4)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 2)
)

# Managed Objects groups

groupCfgIcl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 1, 1)
)
groupCfgIcl.setObjects(
      *(("WESTERMO-SW6-ICL-MIB", "cfgIclEnabled"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclConnectionDelay"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclConnectionThreshold"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclDisconnectionDelay"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclDisconnectionThreshold"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclInterfaceName"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclCycleTime"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclBlacklistTime"),
        ("WESTERMO-SW6-ICL-MIB", "cfgIclSuspended"))
)
if mibBuilder.loadTexts:
    groupCfgIcl.setStatus("current")

groupRpcIcl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 2, 1)
)
groupRpcIcl.setObjects(
      *(("WESTERMO-SW6-ICL-MIB", "rpcIclForceDisconnect"),
        ("WESTERMO-SW6-ICL-MIB", "rpcIclClearBlacklist"))
)
if mibBuilder.loadTexts:
    groupRpcIcl.setStatus("current")

groupSetIcl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 3, 1)
)
groupSetIcl.setObjects(
    ("WESTERMO-SW6-ICL-MIB", "setIclSuspended")
)
if mibBuilder.loadTexts:
    groupSetIcl.setStatus("current")

groupSwIcl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 1, 4, 1)
)
groupSwIcl.setObjects(
    ("WESTERMO-SW6-ICL-MIB", "swIclStatus")
)
if mibBuilder.loadTexts:
    groupSwIcl.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 5, 10000, 2, 1)
)
compliance.setObjects(
      *(("WESTERMO-SW6-ICL-MIB", "groupCfgIcl"),
        ("WESTERMO-SW6-ICL-MIB", "groupRpcIcl"),
        ("WESTERMO-SW6-ICL-MIB", "groupSetIcl"),
        ("WESTERMO-SW6-ICL-MIB", "groupSwIcl"))
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-SW6-ICL-MIB",
    **{"icl": icl,
       "configuration": configuration,
       "cfgIcl": cfgIcl,
       "cfgIclEnabled": cfgIclEnabled,
       "cfgIclConnectionDelay": cfgIclConnectionDelay,
       "cfgIclConnectionThreshold": cfgIclConnectionThreshold,
       "cfgIclDisconnectionDelay": cfgIclDisconnectionDelay,
       "cfgIclDisconnectionThreshold": cfgIclDisconnectionThreshold,
       "cfgIclInterfaceName": cfgIclInterfaceName,
       "cfgIclCycleTime": cfgIclCycleTime,
       "cfgIclBlacklistTime": cfgIclBlacklistTime,
       "cfgIclSuspended": cfgIclSuspended,
       "rpc": rpc,
       "rpcIcl": rpcIcl,
       "rpcIclForceDisconnect": rpcIclForceDisconnect,
       "rpcIclClearBlacklist": rpcIclClearBlacklist,
       "settings": settings,
       "setIcl": setIcl,
       "setIclSuspended": setIclSuspended,
       "software": software,
       "swIcl": swIcl,
       "swIclStatus": swIclStatus,
       "conformance": conformance,
       "groups": groups,
       "groupConfiguration": groupConfiguration,
       "groupCfgIcl": groupCfgIcl,
       "groupRpc": groupRpc,
       "groupRpcIcl": groupRpcIcl,
       "groupSettings": groupSettings,
       "groupSetIcl": groupSetIcl,
       "groupSoftware": groupSoftware,
       "groupSwIcl": groupSwIcl,
       "compliances": compliances,
       "compliance": compliance}
)
