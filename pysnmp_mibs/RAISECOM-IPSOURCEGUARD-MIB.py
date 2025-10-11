# SNMP MIB module (RAISECOM-IPSOURCEGUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-IPSOURCEGUARD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:54 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcIpSourceGuard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37)
)
if mibBuilder.loadTexts:
    rcIpSourceGuard.setRevisions(
        ("2009-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RcIpVerifySource_Type(EnableVar):
    """Custom type rcIpVerifySource based on EnableVar"""
    defaultValue = 2


_RcIpVerifySource_Type.__name__ = "EnableVar"
_RcIpVerifySource_Object = MibScalar
rcIpVerifySource = _RcIpVerifySource_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 1),
    _RcIpVerifySource_Type()
)
rcIpVerifySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpVerifySource.setStatus("current")


class _RcIpVerifySourceDhcpsnooping_Type(EnableVar):
    """Custom type rcIpVerifySourceDhcpsnooping based on EnableVar"""
    defaultValue = 2


_RcIpVerifySourceDhcpsnooping_Type.__name__ = "EnableVar"
_RcIpVerifySourceDhcpsnooping_Object = MibScalar
rcIpVerifySourceDhcpsnooping = _RcIpVerifySourceDhcpsnooping_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 2),
    _RcIpVerifySourceDhcpsnooping_Type()
)
rcIpVerifySourceDhcpsnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpVerifySourceDhcpsnooping.setStatus("current")


class _RcIpVerifySourceMaxEntryNum_Type(Integer32):
    """Custom type rcIpVerifySourceMaxEntryNum based on Integer32"""
    defaultValue = 0


_RcIpVerifySourceMaxEntryNum_Type.__name__ = "Integer32"
_RcIpVerifySourceMaxEntryNum_Object = MibScalar
rcIpVerifySourceMaxEntryNum = _RcIpVerifySourceMaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 3),
    _RcIpVerifySourceMaxEntryNum_Type()
)
rcIpVerifySourceMaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpVerifySourceMaxEntryNum.setStatus("current")


class _RcIpVerifySourceCurrentEntryNum_Type(Integer32):
    """Custom type rcIpVerifySourceCurrentEntryNum based on Integer32"""
    defaultValue = 0


_RcIpVerifySourceCurrentEntryNum_Type.__name__ = "Integer32"
_RcIpVerifySourceCurrentEntryNum_Object = MibScalar
rcIpVerifySourceCurrentEntryNum = _RcIpVerifySourceCurrentEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 4),
    _RcIpVerifySourceCurrentEntryNum_Type()
)
rcIpVerifySourceCurrentEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpVerifySourceCurrentEntryNum.setStatus("current")
_RcPortTrustTable_Object = MibTable
rcPortTrustTable = _RcPortTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 5)
)
if mibBuilder.loadTexts:
    rcPortTrustTable.setStatus("current")
_RcPortTrustEntry_Object = MibTableRow
rcPortTrustEntry = _RcPortTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 5, 1)
)
rcPortTrustEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    rcPortTrustEntry.setStatus("current")


class _RcPortIpVerifySourceTrust_Type(EnableVar):
    """Custom type rcPortIpVerifySourceTrust based on EnableVar"""
    defaultValue = 2


_RcPortIpVerifySourceTrust_Type.__name__ = "EnableVar"
_RcPortIpVerifySourceTrust_Object = MibTableColumn
rcPortIpVerifySourceTrust = _RcPortIpVerifySourceTrust_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 5, 1, 1),
    _RcPortIpVerifySourceTrust_Type()
)
rcPortIpVerifySourceTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortIpVerifySourceTrust.setStatus("current")
_RcIpSourceGuardTable_Object = MibTable
rcIpSourceGuardTable = _RcIpSourceGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6)
)
if mibBuilder.loadTexts:
    rcIpSourceGuardTable.setStatus("current")
_RcIpSourceGuardEntry_Object = MibTableRow
rcIpSourceGuardEntry = _RcIpSourceGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1)
)
rcIpSourceGuardEntry.setIndexNames(
    (0, "RAISECOM-IPSOURCEGUARD-MIB", "rcPortBindIp"),
)
if mibBuilder.loadTexts:
    rcIpSourceGuardEntry.setStatus("current")
_RcPortBindIp_Type = IpAddress
_RcPortBindIp_Object = MibTableColumn
rcPortBindIp = _RcPortBindIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1, 1),
    _RcPortBindIp_Type()
)
rcPortBindIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPortBindIp.setStatus("current")
_RcPortBindPortid_Type = Integer32
_RcPortBindPortid_Object = MibTableColumn
rcPortBindPortid = _RcPortBindPortid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1, 2),
    _RcPortBindPortid_Type()
)
rcPortBindPortid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortBindPortid.setStatus("current")


class _RcPortBindType_Type(Integer32):
    """Custom type rcPortBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("statis", 1),
          ("dynamic", 2))
    )


_RcPortBindType_Type.__name__ = "Integer32"
_RcPortBindType_Object = MibTableColumn
rcPortBindType = _RcPortBindType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1, 3),
    _RcPortBindType_Type()
)
rcPortBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortBindType.setStatus("current")
_RcPortBindMac_Type = MacAddress
_RcPortBindMac_Object = MibTableColumn
rcPortBindMac = _RcPortBindMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1, 4),
    _RcPortBindMac_Type()
)
rcPortBindMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortBindMac.setStatus("current")


class _RcPortBindVlan_Type(Integer32):
    """Custom type rcPortBindVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcPortBindVlan_Type.__name__ = "Integer32"
_RcPortBindVlan_Object = MibTableColumn
rcPortBindVlan = _RcPortBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1, 5),
    _RcPortBindVlan_Type()
)
rcPortBindVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortBindVlan.setStatus("current")
_RcPortBindHwStatus_Type = EnableVar
_RcPortBindHwStatus_Object = MibTableColumn
rcPortBindHwStatus = _RcPortBindHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1, 6),
    _RcPortBindHwStatus_Type()
)
rcPortBindHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortBindHwStatus.setStatus("current")
_RcPortBindRowStatus_Type = RowStatus
_RcPortBindRowStatus_Object = MibTableColumn
rcPortBindRowStatus = _RcPortBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 6, 1, 7),
    _RcPortBindRowStatus_Type()
)
rcPortBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortBindRowStatus.setStatus("current")


class _RcIpVerifySourceAutoUpdate_Type(EnableVar):
    """Custom type rcIpVerifySourceAutoUpdate based on EnableVar"""
    defaultValue = 2


_RcIpVerifySourceAutoUpdate_Type.__name__ = "EnableVar"
_RcIpVerifySourceAutoUpdate_Object = MibScalar
rcIpVerifySourceAutoUpdate = _RcIpVerifySourceAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 37, 7),
    _RcIpVerifySourceAutoUpdate_Type()
)
rcIpVerifySourceAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpVerifySourceAutoUpdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-IPSOURCEGUARD-MIB",
    **{"rcIpSourceGuard": rcIpSourceGuard,
       "rcIpVerifySource": rcIpVerifySource,
       "rcIpVerifySourceDhcpsnooping": rcIpVerifySourceDhcpsnooping,
       "rcIpVerifySourceMaxEntryNum": rcIpVerifySourceMaxEntryNum,
       "rcIpVerifySourceCurrentEntryNum": rcIpVerifySourceCurrentEntryNum,
       "rcPortTrustTable": rcPortTrustTable,
       "rcPortTrustEntry": rcPortTrustEntry,
       "rcPortIpVerifySourceTrust": rcPortIpVerifySourceTrust,
       "rcIpSourceGuardTable": rcIpSourceGuardTable,
       "rcIpSourceGuardEntry": rcIpSourceGuardEntry,
       "rcPortBindIp": rcPortBindIp,
       "rcPortBindPortid": rcPortBindPortid,
       "rcPortBindType": rcPortBindType,
       "rcPortBindMac": rcPortBindMac,
       "rcPortBindVlan": rcPortBindVlan,
       "rcPortBindHwStatus": rcPortBindHwStatus,
       "rcPortBindRowStatus": rcPortBindRowStatus,
       "rcIpVerifySourceAutoUpdate": rcIpVerifySourceAutoUpdate}
)
