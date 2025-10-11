# SNMP MIB module (MPSYSPERF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPSYSPERF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:05 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpSysPerfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 901)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _MpSysRamUsage_Type(Integer32):
    """Custom type mpSysRamUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpSysRamUsage_Type.__name__ = "Integer32"
_MpSysRamUsage_Object = MibScalar
mpSysRamUsage = _MpSysRamUsage_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 901, 1),
    _MpSysRamUsage_Type()
)
mpSysRamUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpSysRamUsage.setStatus("current")


class _MpSysCpuUsage_Type(Integer32):
    """Custom type mpSysCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpSysCpuUsage_Type.__name__ = "Integer32"
_MpSysCpuUsage_Object = MibScalar
mpSysCpuUsage = _MpSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 901, 2),
    _MpSysCpuUsage_Type()
)
mpSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpSysCpuUsage.setStatus("current")


class _MpSysCpuPeakLoad_Type(Integer32):
    """Custom type mpSysCpuPeakLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpSysCpuPeakLoad_Type.__name__ = "Integer32"
_MpSysCpuPeakLoad_Object = MibScalar
mpSysCpuPeakLoad = _MpSysCpuPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 901, 3),
    _MpSysCpuPeakLoad_Type()
)
mpSysCpuPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpSysCpuPeakLoad.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPSYSPERF-MIB",
    **{"mpSysPerfMib": mpSysPerfMib,
       "mpSysRamUsage": mpSysRamUsage,
       "mpSysCpuUsage": mpSysCpuUsage,
       "mpSysCpuPeakLoad": mpSysCpuPeakLoad}
)
