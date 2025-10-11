# SNMP MIB module (CPQN54NN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQN54NN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:38:12 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqGigaSwitch_ObjectIdentity = ObjectIdentity
cpqGigaSwitch = _CpqGigaSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111)
)
_CpqGigaSwitchProd_ObjectIdentity = ObjectIdentity
cpqGigaSwitchProd = _CpqGigaSwitchProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 1)
)
_CpqGigaSwitchId5422_ObjectIdentity = ObjectIdentity
cpqGigaSwitchId5422 = _CpqGigaSwitchId5422_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 1, 1)
)
_CpqGigaSwitchId5411_ObjectIdentity = ObjectIdentity
cpqGigaSwitchId5411 = _CpqGigaSwitchId5411_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 1, 2)
)
_CpqOids_ObjectIdentity = ObjectIdentity
cpqOids = _CpqOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2)
)
_CpqMauType_ObjectIdentity = ObjectIdentity
cpqMauType = _CpqMauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2, 1)
)
_CpqMauType1000BaseSX_ObjectIdentity = ObjectIdentity
cpqMauType1000BaseSX = _CpqMauType1000BaseSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2, 1, 1)
)
_CpqMauType1000BaseLX_ObjectIdentity = ObjectIdentity
cpqMauType1000BaseLX = _CpqMauType1000BaseLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2, 1, 2)
)
_CpqMauType1000BaseCX_ObjectIdentity = ObjectIdentity
cpqMauType1000BaseCX = _CpqMauType1000BaseCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2, 1, 3)
)
_CpqMauType1000BaseSXFD_ObjectIdentity = ObjectIdentity
cpqMauType1000BaseSXFD = _CpqMauType1000BaseSXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2, 1, 4)
)
_CpqMauType1000BaseLXFD_ObjectIdentity = ObjectIdentity
cpqMauType1000BaseLXFD = _CpqMauType1000BaseLXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2, 1, 5)
)
_CpqMauType1000BaseCXFD_ObjectIdentity = ObjectIdentity
cpqMauType1000BaseCXFD = _CpqMauType1000BaseCXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 2, 1, 6)
)
_CpqGigaSwitchMib_ObjectIdentity = ObjectIdentity
cpqGigaSwitchMib = _CpqGigaSwitchMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 3)
)
_CpqGigaSwitchSystem_ObjectIdentity = ObjectIdentity
cpqGigaSwitchSystem = _CpqGigaSwitchSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 111, 3, 1)
)


class _CpqSaveConfiguration_Type(Integer32):
    """Custom type cpqSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveToPrimary", 1),
          ("saveToSecondary", 2))
    )


_CpqSaveConfiguration_Type.__name__ = "Integer32"
_CpqSaveConfiguration_Object = MibScalar
cpqSaveConfiguration = _CpqSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 232, 111, 3, 1, 3),
    _CpqSaveConfiguration_Type()
)
cpqSaveConfiguration.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cpqSaveConfiguration.setStatus("mandatory")


class _CpqSaveStatus_Type(Integer32):
    """Custom type cpqSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveInProgress", 1),
          ("saveNotInProgress", 2))
    )


_CpqSaveStatus_Type.__name__ = "Integer32"
_CpqSaveStatus_Object = MibScalar
cpqSaveStatus = _CpqSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 111, 3, 1, 4),
    _CpqSaveStatus_Type()
)
cpqSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSaveStatus.setStatus("mandatory")


class _CpqCurrentConfigInUse_Type(Integer32):
    """Custom type cpqCurrentConfigInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_CpqCurrentConfigInUse_Type.__name__ = "Integer32"
_CpqCurrentConfigInUse_Object = MibScalar
cpqCurrentConfigInUse = _CpqCurrentConfigInUse_Object(
    (1, 3, 6, 1, 4, 1, 232, 111, 3, 1, 5),
    _CpqCurrentConfigInUse_Type()
)
cpqCurrentConfigInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCurrentConfigInUse.setStatus("mandatory")


class _CpqConfigToUseOnReboot_Type(Integer32):
    """Custom type cpqConfigToUseOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_CpqConfigToUseOnReboot_Type.__name__ = "Integer32"
_CpqConfigToUseOnReboot_Object = MibScalar
cpqConfigToUseOnReboot = _CpqConfigToUseOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 232, 111, 3, 1, 6),
    _CpqConfigToUseOnReboot_Type()
)
cpqConfigToUseOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqConfigToUseOnReboot.setStatus("mandatory")

# Managed Objects groups


# Notification objects

overheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 6)
)
overheat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    overheat.setStatus(
        ""
    )

fanfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 7)
)
fanfailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanfailed.setStatus(
        ""
    )

fanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 8)
)
fanOK.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanOK.setStatus(
        ""
    )

invalidLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 9)
)
invalidLoginAttempt.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    invalidLoginAttempt.setStatus(
        ""
    )

powerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 10)
)
powerSupplyFail.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    powerSupplyFail.setStatus(
        ""
    )

powerSupplyGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 11)
)
powerSupplyGood.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    powerSupplyGood.setStatus(
        ""
    )

rpsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 12)
)
rpsAlarm.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    rpsAlarm.setStatus(
        ""
    )

rpsNoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 111, 0, 13)
)
rpsNoAlarm.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    rpsNoAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQN54NN-MIB",
    **{"compaq": compaq,
       "cpqGigaSwitch": cpqGigaSwitch,
       "overheat": overheat,
       "fanfailed": fanfailed,
       "fanOK": fanOK,
       "invalidLoginAttempt": invalidLoginAttempt,
       "powerSupplyFail": powerSupplyFail,
       "powerSupplyGood": powerSupplyGood,
       "rpsAlarm": rpsAlarm,
       "rpsNoAlarm": rpsNoAlarm,
       "cpqGigaSwitchProd": cpqGigaSwitchProd,
       "cpqGigaSwitchId5422": cpqGigaSwitchId5422,
       "cpqGigaSwitchId5411": cpqGigaSwitchId5411,
       "cpqOids": cpqOids,
       "cpqMauType": cpqMauType,
       "cpqMauType1000BaseSX": cpqMauType1000BaseSX,
       "cpqMauType1000BaseLX": cpqMauType1000BaseLX,
       "cpqMauType1000BaseCX": cpqMauType1000BaseCX,
       "cpqMauType1000BaseSXFD": cpqMauType1000BaseSXFD,
       "cpqMauType1000BaseLXFD": cpqMauType1000BaseLXFD,
       "cpqMauType1000BaseCXFD": cpqMauType1000BaseCXFD,
       "cpqGigaSwitchMib": cpqGigaSwitchMib,
       "cpqGigaSwitchSystem": cpqGigaSwitchSystem,
       "cpqSaveConfiguration": cpqSaveConfiguration,
       "cpqSaveStatus": cpqSaveStatus,
       "cpqCurrentConfigInUse": cpqCurrentConfigInUse,
       "cpqConfigToUseOnReboot": cpqConfigToUseOnReboot}
)
