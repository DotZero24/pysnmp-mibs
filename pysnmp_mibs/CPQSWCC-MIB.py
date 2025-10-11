# SNMP MIB module (CPQSWCC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQSWCC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:39:12 2025
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqSwcc_ObjectIdentity = ObjectIdentity
cpqSwcc = _CpqSwcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 132)
)
_CpqSwccMibRev_ObjectIdentity = ObjectIdentity
cpqSwccMibRev = _CpqSwccMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 132, 1)
)


class _CpqSwccMibRevMajor_Type(Integer32):
    """Custom type cpqSwccMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSwccMibRevMajor_Type.__name__ = "Integer32"
_CpqSwccMibRevMajor_Object = MibScalar
cpqSwccMibRevMajor = _CpqSwccMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 1, 1),
    _CpqSwccMibRevMajor_Type()
)
cpqSwccMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccMibRevMajor.setStatus("mandatory")


class _CpqSwccMibRevMinor_Type(Integer32):
    """Custom type cpqSwccMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSwccMibRevMinor_Type.__name__ = "Integer32"
_CpqSwccMibRevMinor_Object = MibScalar
cpqSwccMibRevMinor = _CpqSwccMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 1, 2),
    _CpqSwccMibRevMinor_Type()
)
cpqSwccMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccMibRevMinor.setStatus("mandatory")


class _CpqSwccMibCondition_Type(Integer32):
    """Custom type cpqSwccMibCondition based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqSwccMibCondition_Type.__name__ = "Integer32"
_CpqSwccMibCondition_Object = MibScalar
cpqSwccMibCondition = _CpqSwccMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 1, 3),
    _CpqSwccMibCondition_Type()
)
cpqSwccMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccMibCondition.setStatus("mandatory")
_CpqSwccFibre_ObjectIdentity = ObjectIdentity
cpqSwccFibre = _CpqSwccFibre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 132, 2)
)


class _CpqSwccFibreDevName_Type(DisplayString):
    """Custom type cpqSwccFibreDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqSwccFibreDevName_Type.__name__ = "DisplayString"
_CpqSwccFibreDevName_Object = MibScalar
cpqSwccFibreDevName = _CpqSwccFibreDevName_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 2, 1),
    _CpqSwccFibreDevName_Type()
)
cpqSwccFibreDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccFibreDevName.setStatus("mandatory")


class _CpqSwccFibreDevState_Type(Integer32):
    """Custom type cpqSwccFibreDevState based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqSwccFibreDevState_Type.__name__ = "Integer32"
_CpqSwccFibreDevState_Object = MibScalar
cpqSwccFibreDevState = _CpqSwccFibreDevState_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 2, 2),
    _CpqSwccFibreDevState_Type()
)
cpqSwccFibreDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccFibreDevState.setStatus("mandatory")


class _CpqSwccFibreEventDescription_Type(DisplayString):
    """Custom type cpqSwccFibreEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqSwccFibreEventDescription_Type.__name__ = "DisplayString"
_CpqSwccFibreEventDescription_Object = MibScalar
cpqSwccFibreEventDescription = _CpqSwccFibreEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 2, 3),
    _CpqSwccFibreEventDescription_Type()
)
cpqSwccFibreEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccFibreEventDescription.setStatus("mandatory")
_CpqSwccEmuDev_ObjectIdentity = ObjectIdentity
cpqSwccEmuDev = _CpqSwccEmuDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 132, 3)
)


class _CpqSwccEmuDevDevName_Type(DisplayString):
    """Custom type cpqSwccEmuDevDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqSwccEmuDevDevName_Type.__name__ = "DisplayString"
_CpqSwccEmuDevDevName_Object = MibScalar
cpqSwccEmuDevDevName = _CpqSwccEmuDevDevName_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 3, 1),
    _CpqSwccEmuDevDevName_Type()
)
cpqSwccEmuDevDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccEmuDevDevName.setStatus("mandatory")


class _CpqSwccEmuDevDevState_Type(Integer32):
    """Custom type cpqSwccEmuDevDevState based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqSwccEmuDevDevState_Type.__name__ = "Integer32"
_CpqSwccEmuDevDevState_Object = MibScalar
cpqSwccEmuDevDevState = _CpqSwccEmuDevDevState_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 3, 2),
    _CpqSwccEmuDevDevState_Type()
)
cpqSwccEmuDevDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccEmuDevDevState.setStatus("mandatory")


class _CpqSwccEmuDevEventDescription_Type(DisplayString):
    """Custom type cpqSwccEmuDevEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqSwccEmuDevEventDescription_Type.__name__ = "DisplayString"
_CpqSwccEmuDevEventDescription_Object = MibScalar
cpqSwccEmuDevEventDescription = _CpqSwccEmuDevEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 3, 3),
    _CpqSwccEmuDevEventDescription_Type()
)
cpqSwccEmuDevEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSwccEmuDevEventDescription.setStatus("mandatory")
_CpqSwccKzpcc_ObjectIdentity = ObjectIdentity
cpqSwccKzpcc = _CpqSwccKzpcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 132, 4)
)
_CpqSwccKzpccTrap_ObjectIdentity = ObjectIdentity
cpqSwccKzpccTrap = _CpqSwccKzpccTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1)
)
_CpqSwccKzpccSytemName_Type = OctetString
_CpqSwccKzpccSytemName_Object = MibScalar
cpqSwccKzpccSytemName = _CpqSwccKzpccSytemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1, 1),
    _CpqSwccKzpccSytemName_Type()
)
cpqSwccKzpccSytemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpqSwccKzpccSytemName.setStatus("mandatory")
_CpqSwccKzpccSubsytemName_Type = OctetString
_CpqSwccKzpccSubsytemName_Object = MibScalar
cpqSwccKzpccSubsytemName = _CpqSwccKzpccSubsytemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1, 2),
    _CpqSwccKzpccSubsytemName_Type()
)
cpqSwccKzpccSubsytemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpqSwccKzpccSubsytemName.setStatus("mandatory")


class _CpqSwccKzpccEventSeverity_Type(Integer32):
    """Custom type cpqSwccKzpccEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("warning", 2),
          ("error", 3))
    )


_CpqSwccKzpccEventSeverity_Type.__name__ = "Integer32"
_CpqSwccKzpccEventSeverity_Object = MibScalar
cpqSwccKzpccEventSeverity = _CpqSwccKzpccEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1, 3),
    _CpqSwccKzpccEventSeverity_Type()
)
cpqSwccKzpccEventSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpqSwccKzpccEventSeverity.setStatus("mandatory")
_CpqSwccKzpccEventDescription_Type = OctetString
_CpqSwccKzpccEventDescription_Object = MibScalar
cpqSwccKzpccEventDescription = _CpqSwccKzpccEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1, 4),
    _CpqSwccKzpccEventDescription_Type()
)
cpqSwccKzpccEventDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpqSwccKzpccEventDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqSwccFibreDeviceStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 132, 2, 0, 1)
)
cpqSwccFibreDeviceStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQSWCC-MIB", "cpqSwccFibreDevName"),
        ("CPQSWCC-MIB", "cpqSwccFibreDevState"),
        ("CPQSWCC-MIB", "cpqSwccFibreEventDescription"))
)
if mibBuilder.loadTexts:
    cpqSwccFibreDeviceStatusChange.setStatus(
        ""
    )

cpqSwccTapeControllerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 132, 2, 0, 2)
)
cpqSwccTapeControllerStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQSWCC-MIB", "cpqSwccFibreDevName"),
        ("CPQSWCC-MIB", "cpqSwccFibreDevState"),
        ("CPQSWCC-MIB", "cpqSwccFibreEventDescription"))
)
if mibBuilder.loadTexts:
    cpqSwccTapeControllerStatusChange.setStatus(
        ""
    )

cpqSwccEmuDevDeviceStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 132, 3, 0, 1)
)
cpqSwccEmuDevDeviceStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQSWCC-MIB", "cpqSwccEmuDevDevName"),
        ("CPQSWCC-MIB", "cpqSwccEmuDevDevState"),
        ("CPQSWCC-MIB", "cpqSwccEmuDevEventDescription"))
)
if mibBuilder.loadTexts:
    cpqSwccEmuDevDeviceStatusChange.setStatus(
        ""
    )

cpqSwccKzpccPhyDeviceEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1, 0, 1)
)
cpqSwccKzpccPhyDeviceEventTrap.setObjects(
      *(("CPQSWCC-MIB", "cpqSwccKzpccSystemName"),
        ("CPQSWCC-MIB", "cpqSwccKzpccSubsystemName"),
        ("CPQSWCC-MIB", "cpqSwccKzpccEventSeverity"),
        ("CPQSWCC-MIB", "cpqSwccKzpccEventDescription"))
)
if mibBuilder.loadTexts:
    cpqSwccKzpccPhyDeviceEventTrap.setStatus(
        ""
    )

cpqSwccKzpccVirtualDeviceEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1, 0, 2)
)
cpqSwccKzpccVirtualDeviceEventTrap.setObjects(
      *(("CPQSWCC-MIB", "cpqSwccKzpccSystemName"),
        ("CPQSWCC-MIB", "cpqSwccKzpccSubsystemName"),
        ("CPQSWCC-MIB", "cpqSwccKzpccEventSeverity"),
        ("CPQSWCC-MIB", "cpqSwccKzpccEventDescription"))
)
if mibBuilder.loadTexts:
    cpqSwccKzpccVirtualDeviceEventTrap.setStatus(
        ""
    )

cpqSwccKzpccSubsystemEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 132, 4, 1, 0, 3)
)
cpqSwccKzpccSubsystemEventTrap.setObjects(
      *(("CPQSWCC-MIB", "cpqSwccKzpccSystemName"),
        ("CPQSWCC-MIB", "cpqSwccKzpccSubsystemName"),
        ("CPQSWCC-MIB", "cpqSwccKzpccEventSeverity"),
        ("CPQSWCC-MIB", "cpqSwccKzpccEventDescription"))
)
if mibBuilder.loadTexts:
    cpqSwccKzpccSubsystemEventTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSWCC-MIB",
    **{"cpqSwcc": cpqSwcc,
       "cpqSwccMibRev": cpqSwccMibRev,
       "cpqSwccMibRevMajor": cpqSwccMibRevMajor,
       "cpqSwccMibRevMinor": cpqSwccMibRevMinor,
       "cpqSwccMibCondition": cpqSwccMibCondition,
       "cpqSwccFibre": cpqSwccFibre,
       "cpqSwccFibreDeviceStatusChange": cpqSwccFibreDeviceStatusChange,
       "cpqSwccTapeControllerStatusChange": cpqSwccTapeControllerStatusChange,
       "cpqSwccFibreDevName": cpqSwccFibreDevName,
       "cpqSwccFibreDevState": cpqSwccFibreDevState,
       "cpqSwccFibreEventDescription": cpqSwccFibreEventDescription,
       "cpqSwccEmuDev": cpqSwccEmuDev,
       "cpqSwccEmuDevDeviceStatusChange": cpqSwccEmuDevDeviceStatusChange,
       "cpqSwccEmuDevDevName": cpqSwccEmuDevDevName,
       "cpqSwccEmuDevDevState": cpqSwccEmuDevDevState,
       "cpqSwccEmuDevEventDescription": cpqSwccEmuDevEventDescription,
       "cpqSwccKzpcc": cpqSwccKzpcc,
       "cpqSwccKzpccTrap": cpqSwccKzpccTrap,
       "cpqSwccKzpccPhyDeviceEventTrap": cpqSwccKzpccPhyDeviceEventTrap,
       "cpqSwccKzpccVirtualDeviceEventTrap": cpqSwccKzpccVirtualDeviceEventTrap,
       "cpqSwccKzpccSubsystemEventTrap": cpqSwccKzpccSubsystemEventTrap,
       "cpqSwccKzpccSytemName": cpqSwccKzpccSytemName,
       "cpqSwccKzpccSubsytemName": cpqSwccKzpccSubsytemName,
       "cpqSwccKzpccEventSeverity": cpqSwccKzpccEventSeverity,
       "cpqSwccKzpccEventDescription": cpqSwccKzpccEventDescription}
)
