# SNMP MIB module (DPS-MIB-NGX-G39-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dps/DPS-MIB-NGX-G39-V2
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:55 2025
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

(dpsAlarmControl,) = mibBuilder.importSymbols(
    "DPS-MIB-V38",
    "dpsAlarmControl")

(dpsRTUv2,
 dpsRTUv2ADisplay,
 dpsRTUv2APntDesc,
 dpsRTUv2APoint,
 dpsRTUv2APort,
 dpsRTUv2AState,
 dpsRTUv2CAddress,
 dpsRTUv2DateTime) = mibBuilder.importSymbols(
    "DPS-MIB-V38-V2",
    "dpsRTUv2",
    "dpsRTUv2ADisplay",
    "dpsRTUv2APntDesc",
    "dpsRTUv2APoint",
    "dpsRTUv2APort",
    "dpsRTUv2AState",
    "dpsRTUv2CAddress",
    "dpsRTUv2DateTime")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysLocation) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysLocation")

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

dpsRTUxV2MI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5)
)
if mibBuilder.loadTexts:
    dpsRTUxV2MI.setRevisions(
        ("2012-08-08 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

dpsRTUv2p6001Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6001)
)
dpsRTUv2p6001Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6001Set.setStatus(
        "current"
    )

dpsRTUv2p6002Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6002)
)
dpsRTUv2p6002Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6002Set.setStatus(
        "current"
    )

dpsRTUv2p6003Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6003)
)
dpsRTUv2p6003Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6003Set.setStatus(
        "current"
    )

dpsRTUv2p6004Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6004)
)
dpsRTUv2p6004Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6004Set.setStatus(
        "current"
    )

dpsRTUv2p6005Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6005)
)
dpsRTUv2p6005Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6005Set.setStatus(
        "current"
    )

dpsRTUv2p6006Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6006)
)
dpsRTUv2p6006Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6006Set.setStatus(
        "current"
    )

dpsRTUv2p6007Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6007)
)
dpsRTUv2p6007Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6007Set.setStatus(
        "current"
    )

dpsRTUv2p6008Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6008)
)
dpsRTUv2p6008Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6008Set.setStatus(
        "current"
    )

dpsRTUv2p6009Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6009)
)
dpsRTUv2p6009Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6009Set.setStatus(
        "current"
    )

dpsRTUv2p6010Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6010)
)
dpsRTUv2p6010Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6010Set.setStatus(
        "current"
    )

dpsRTUv2p6011Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6011)
)
dpsRTUv2p6011Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6011Set.setStatus(
        "current"
    )

dpsRTUv2p6012Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6012)
)
dpsRTUv2p6012Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6012Set.setStatus(
        "current"
    )

dpsRTUv2p6013Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6013)
)
dpsRTUv2p6013Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6013Set.setStatus(
        "current"
    )

dpsRTUv2p6014Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6014)
)
dpsRTUv2p6014Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6014Set.setStatus(
        "current"
    )

dpsRTUv2p6015Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6015)
)
dpsRTUv2p6015Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6015Set.setStatus(
        "current"
    )

dpsRTUv2p6016Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6016)
)
dpsRTUv2p6016Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6016Set.setStatus(
        "current"
    )

dpsRTUv2p6017Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6017)
)
dpsRTUv2p6017Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6017Set.setStatus(
        "current"
    )

dpsRTUv2p6018Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6018)
)
dpsRTUv2p6018Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6018Set.setStatus(
        "current"
    )

dpsRTUv2p6019Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6019)
)
dpsRTUv2p6019Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6019Set.setStatus(
        "current"
    )

dpsRTUv2p6020Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6020)
)
dpsRTUv2p6020Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6020Set.setStatus(
        "current"
    )

dpsRTUv2p6021Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6021)
)
dpsRTUv2p6021Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6021Set.setStatus(
        "current"
    )

dpsRTUv2p6022Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6022)
)
dpsRTUv2p6022Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6022Set.setStatus(
        "current"
    )

dpsRTUv2p6023Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6023)
)
dpsRTUv2p6023Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6023Set.setStatus(
        "current"
    )

dpsRTUv2p6024Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6024)
)
dpsRTUv2p6024Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6024Set.setStatus(
        "current"
    )

dpsRTUv2p6025Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6025)
)
dpsRTUv2p6025Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6025Set.setStatus(
        "current"
    )

dpsRTUv2p6026Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6026)
)
dpsRTUv2p6026Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6026Set.setStatus(
        "current"
    )

dpsRTUv2p6027Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6027)
)
dpsRTUv2p6027Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6027Set.setStatus(
        "current"
    )

dpsRTUv2p6028Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6028)
)
dpsRTUv2p6028Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6028Set.setStatus(
        "current"
    )

dpsRTUv2p6029Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6029)
)
dpsRTUv2p6029Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6029Set.setStatus(
        "current"
    )

dpsRTUv2p6030Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6030)
)
dpsRTUv2p6030Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6030Set.setStatus(
        "current"
    )

dpsRTUv2p6031Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6031)
)
dpsRTUv2p6031Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6031Set.setStatus(
        "current"
    )

dpsRTUv2p6032Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6032)
)
dpsRTUv2p6032Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6032Set.setStatus(
        "current"
    )

dpsRTUv2p6033Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6033)
)
dpsRTUv2p6033Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6033Set.setStatus(
        "current"
    )

dpsRTUv2p6034Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6034)
)
dpsRTUv2p6034Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6034Set.setStatus(
        "current"
    )

dpsRTUv2p6035Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6035)
)
dpsRTUv2p6035Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6035Set.setStatus(
        "current"
    )

dpsRTUv2p6036Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6036)
)
dpsRTUv2p6036Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6036Set.setStatus(
        "current"
    )

dpsRTUv2p6037Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6037)
)
dpsRTUv2p6037Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6037Set.setStatus(
        "current"
    )

dpsRTUv2p6038Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6038)
)
dpsRTUv2p6038Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6038Set.setStatus(
        "current"
    )

dpsRTUv2p6039Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6039)
)
dpsRTUv2p6039Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6039Set.setStatus(
        "current"
    )

dpsRTUv2p6040Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6040)
)
dpsRTUv2p6040Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6040Set.setStatus(
        "current"
    )

dpsRTUv2p6041Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6041)
)
dpsRTUv2p6041Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6041Set.setStatus(
        "current"
    )

dpsRTUv2p6042Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6042)
)
dpsRTUv2p6042Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6042Set.setStatus(
        "current"
    )

dpsRTUv2p6043Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6043)
)
dpsRTUv2p6043Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6043Set.setStatus(
        "current"
    )

dpsRTUv2p6044Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6044)
)
dpsRTUv2p6044Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6044Set.setStatus(
        "current"
    )

dpsRTUv2p6045Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6045)
)
dpsRTUv2p6045Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6045Set.setStatus(
        "current"
    )

dpsRTUv2p6046Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6046)
)
dpsRTUv2p6046Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6046Set.setStatus(
        "current"
    )

dpsRTUv2p6047Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6047)
)
dpsRTUv2p6047Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6047Set.setStatus(
        "current"
    )

dpsRTUv2p6048Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6048)
)
dpsRTUv2p6048Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6048Set.setStatus(
        "current"
    )

dpsRTUv2p6049Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6049)
)
dpsRTUv2p6049Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6049Set.setStatus(
        "current"
    )

dpsRTUv2p6050Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6050)
)
dpsRTUv2p6050Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6050Set.setStatus(
        "current"
    )

dpsRTUv2p6051Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6051)
)
dpsRTUv2p6051Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6051Set.setStatus(
        "current"
    )

dpsRTUv2p6052Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6052)
)
dpsRTUv2p6052Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6052Set.setStatus(
        "current"
    )

dpsRTUv2p6053Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6053)
)
dpsRTUv2p6053Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6053Set.setStatus(
        "current"
    )

dpsRTUv2p6054Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6054)
)
dpsRTUv2p6054Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6054Set.setStatus(
        "current"
    )

dpsRTUv2p6055Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6055)
)
dpsRTUv2p6055Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6055Set.setStatus(
        "current"
    )

dpsRTUv2p6056Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6056)
)
dpsRTUv2p6056Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6056Set.setStatus(
        "current"
    )

dpsRTUv2p6057Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6057)
)
dpsRTUv2p6057Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6057Set.setStatus(
        "current"
    )

dpsRTUv2p6058Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6058)
)
dpsRTUv2p6058Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6058Set.setStatus(
        "current"
    )

dpsRTUv2p6059Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6059)
)
dpsRTUv2p6059Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6059Set.setStatus(
        "current"
    )

dpsRTUv2p6060Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6060)
)
dpsRTUv2p6060Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6060Set.setStatus(
        "current"
    )

dpsRTUv2p6061Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6061)
)
dpsRTUv2p6061Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6061Set.setStatus(
        "current"
    )

dpsRTUv2p6062Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6062)
)
dpsRTUv2p6062Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6062Set.setStatus(
        "current"
    )

dpsRTUv2p6063Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6063)
)
dpsRTUv2p6063Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6063Set.setStatus(
        "current"
    )

dpsRTUv2p6064Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6064)
)
dpsRTUv2p6064Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6064Set.setStatus(
        "current"
    )

dpsRTUv2p6065Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6065)
)
dpsRTUv2p6065Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6065Set.setStatus(
        "current"
    )

dpsRTUv2p6066Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6066)
)
dpsRTUv2p6066Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6066Set.setStatus(
        "current"
    )

dpsRTUv2p6067Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6067)
)
dpsRTUv2p6067Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6067Set.setStatus(
        "current"
    )

dpsRTUv2p6068Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6068)
)
dpsRTUv2p6068Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6068Set.setStatus(
        "current"
    )

dpsRTUv2p6069Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6069)
)
dpsRTUv2p6069Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6069Set.setStatus(
        "current"
    )

dpsRTUv2p6070Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6070)
)
dpsRTUv2p6070Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6070Set.setStatus(
        "current"
    )

dpsRTUv2p6071Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6071)
)
dpsRTUv2p6071Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6071Set.setStatus(
        "current"
    )

dpsRTUv2p6072Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6072)
)
dpsRTUv2p6072Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6072Set.setStatus(
        "current"
    )

dpsRTUv2p6081Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6081)
)
dpsRTUv2p6081Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6081Set.setStatus(
        "current"
    )

dpsRTUv2p6082Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6082)
)
dpsRTUv2p6082Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6082Set.setStatus(
        "current"
    )

dpsRTUv2p6083Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6083)
)
dpsRTUv2p6083Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6083Set.setStatus(
        "current"
    )

dpsRTUv2p6084Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6084)
)
dpsRTUv2p6084Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6084Set.setStatus(
        "current"
    )

dpsRTUv2p6085Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6085)
)
dpsRTUv2p6085Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6085Set.setStatus(
        "current"
    )

dpsRTUv2p6086Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6086)
)
dpsRTUv2p6086Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6086Set.setStatus(
        "current"
    )

dpsRTUv2p6087Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6087)
)
dpsRTUv2p6087Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6087Set.setStatus(
        "current"
    )

dpsRTUv2p6088Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6088)
)
dpsRTUv2p6088Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6088Set.setStatus(
        "current"
    )

dpsRTUv2p6089Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6089)
)
dpsRTUv2p6089Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6089Set.setStatus(
        "current"
    )

dpsRTUv2p6090Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6090)
)
dpsRTUv2p6090Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6090Set.setStatus(
        "current"
    )

dpsRTUv2p6091Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6091)
)
dpsRTUv2p6091Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6091Set.setStatus(
        "current"
    )

dpsRTUv2p6092Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6092)
)
dpsRTUv2p6092Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6092Set.setStatus(
        "current"
    )

dpsRTUv2p6093Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6093)
)
dpsRTUv2p6093Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6093Set.setStatus(
        "current"
    )

dpsRTUv2p6094Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6094)
)
dpsRTUv2p6094Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6094Set.setStatus(
        "current"
    )

dpsRTUv2p6095Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6095)
)
dpsRTUv2p6095Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6095Set.setStatus(
        "current"
    )

dpsRTUv2p6096Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6096)
)
dpsRTUv2p6096Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6096Set.setStatus(
        "current"
    )

dpsRTUv2p6129Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6129)
)
dpsRTUv2p6129Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6129Set.setStatus(
        "current"
    )

dpsRTUv2p6130Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6130)
)
dpsRTUv2p6130Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6130Set.setStatus(
        "current"
    )

dpsRTUv2p6131Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6131)
)
dpsRTUv2p6131Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6131Set.setStatus(
        "current"
    )

dpsRTUv2p6132Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6132)
)
dpsRTUv2p6132Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6132Set.setStatus(
        "current"
    )

dpsRTUv2p6133Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6133)
)
dpsRTUv2p6133Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6133Set.setStatus(
        "current"
    )

dpsRTUv2p6134Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6134)
)
dpsRTUv2p6134Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6134Set.setStatus(
        "current"
    )

dpsRTUv2p6135Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6135)
)
dpsRTUv2p6135Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6135Set.setStatus(
        "current"
    )

dpsRTUv2p6136Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6136)
)
dpsRTUv2p6136Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6136Set.setStatus(
        "current"
    )

dpsRTUv2p6137Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6137)
)
dpsRTUv2p6137Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6137Set.setStatus(
        "current"
    )

dpsRTUv2p6138Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6138)
)
dpsRTUv2p6138Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6138Set.setStatus(
        "current"
    )

dpsRTUv2p6139Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6139)
)
dpsRTUv2p6139Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6139Set.setStatus(
        "current"
    )

dpsRTUv2p6140Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6140)
)
dpsRTUv2p6140Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6140Set.setStatus(
        "current"
    )

dpsRTUv2p6141Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6141)
)
dpsRTUv2p6141Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6141Set.setStatus(
        "current"
    )

dpsRTUv2p6142Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6142)
)
dpsRTUv2p6142Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6142Set.setStatus(
        "current"
    )

dpsRTUv2p6143Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6143)
)
dpsRTUv2p6143Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6143Set.setStatus(
        "current"
    )

dpsRTUv2p6144Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6144)
)
dpsRTUv2p6144Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6144Set.setStatus(
        "current"
    )

dpsRTUv2p6145Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6145)
)
dpsRTUv2p6145Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6145Set.setStatus(
        "current"
    )

dpsRTUv2p6146Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6146)
)
dpsRTUv2p6146Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6146Set.setStatus(
        "current"
    )

dpsRTUv2p6147Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6147)
)
dpsRTUv2p6147Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6147Set.setStatus(
        "current"
    )

dpsRTUv2p6148Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6148)
)
dpsRTUv2p6148Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6148Set.setStatus(
        "current"
    )

dpsRTUv2p6149Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6149)
)
dpsRTUv2p6149Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6149Set.setStatus(
        "current"
    )

dpsRTUv2p6150Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6150)
)
dpsRTUv2p6150Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6150Set.setStatus(
        "current"
    )

dpsRTUv2p6151Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6151)
)
dpsRTUv2p6151Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6151Set.setStatus(
        "current"
    )

dpsRTUv2p6152Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6152)
)
dpsRTUv2p6152Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6152Set.setStatus(
        "current"
    )

dpsRTUv2p6153Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6153)
)
dpsRTUv2p6153Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6153Set.setStatus(
        "current"
    )

dpsRTUv2p6154Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6154)
)
dpsRTUv2p6154Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6154Set.setStatus(
        "current"
    )

dpsRTUv2p6155Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6155)
)
dpsRTUv2p6155Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6155Set.setStatus(
        "current"
    )

dpsRTUv2p6156Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6156)
)
dpsRTUv2p6156Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6156Set.setStatus(
        "current"
    )

dpsRTUv2p6157Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6157)
)
dpsRTUv2p6157Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6157Set.setStatus(
        "current"
    )

dpsRTUv2p6158Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6158)
)
dpsRTUv2p6158Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6158Set.setStatus(
        "current"
    )

dpsRTUv2p6159Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6159)
)
dpsRTUv2p6159Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6159Set.setStatus(
        "current"
    )

dpsRTUv2p6160Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6160)
)
dpsRTUv2p6160Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6160Set.setStatus(
        "current"
    )

dpsRTUv2p6161Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6161)
)
dpsRTUv2p6161Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6161Set.setStatus(
        "current"
    )

dpsRTUv2p6162Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6162)
)
dpsRTUv2p6162Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6162Set.setStatus(
        "current"
    )

dpsRTUv2p6163Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6163)
)
dpsRTUv2p6163Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6163Set.setStatus(
        "current"
    )

dpsRTUv2p6164Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6164)
)
dpsRTUv2p6164Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6164Set.setStatus(
        "current"
    )

dpsRTUv2p6165Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6165)
)
dpsRTUv2p6165Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6165Set.setStatus(
        "current"
    )

dpsRTUv2p6166Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6166)
)
dpsRTUv2p6166Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6166Set.setStatus(
        "current"
    )

dpsRTUv2p6167Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6167)
)
dpsRTUv2p6167Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6167Set.setStatus(
        "current"
    )

dpsRTUv2p6168Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6168)
)
dpsRTUv2p6168Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6168Set.setStatus(
        "current"
    )

dpsRTUv2p6169Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6169)
)
dpsRTUv2p6169Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6169Set.setStatus(
        "current"
    )

dpsRTUv2p6170Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6170)
)
dpsRTUv2p6170Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6170Set.setStatus(
        "current"
    )

dpsRTUv2p6171Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6171)
)
dpsRTUv2p6171Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6171Set.setStatus(
        "current"
    )

dpsRTUv2p6172Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6172)
)
dpsRTUv2p6172Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6172Set.setStatus(
        "current"
    )

dpsRTUv2p6173Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6173)
)
dpsRTUv2p6173Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6173Set.setStatus(
        "current"
    )

dpsRTUv2p6174Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6174)
)
dpsRTUv2p6174Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6174Set.setStatus(
        "current"
    )

dpsRTUv2p6175Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6175)
)
dpsRTUv2p6175Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6175Set.setStatus(
        "current"
    )

dpsRTUv2p6176Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6176)
)
dpsRTUv2p6176Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6176Set.setStatus(
        "current"
    )

dpsRTUv2p6193Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6193)
)
dpsRTUv2p6193Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6193Set.setStatus(
        "current"
    )

dpsRTUv2p6194Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6194)
)
dpsRTUv2p6194Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6194Set.setStatus(
        "current"
    )

dpsRTUv2p6195Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6195)
)
dpsRTUv2p6195Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6195Set.setStatus(
        "current"
    )

dpsRTUv2p6196Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6196)
)
dpsRTUv2p6196Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6196Set.setStatus(
        "current"
    )

dpsRTUv2p6197Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6197)
)
dpsRTUv2p6197Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6197Set.setStatus(
        "current"
    )

dpsRTUv2p6198Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6198)
)
dpsRTUv2p6198Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6198Set.setStatus(
        "current"
    )

dpsRTUv2p6199Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6199)
)
dpsRTUv2p6199Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6199Set.setStatus(
        "current"
    )

dpsRTUv2p6200Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6200)
)
dpsRTUv2p6200Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6200Set.setStatus(
        "current"
    )

dpsRTUv2p6257Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6257)
)
dpsRTUv2p6257Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6257Set.setStatus(
        "current"
    )

dpsRTUv2p6258Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6258)
)
dpsRTUv2p6258Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6258Set.setStatus(
        "current"
    )

dpsRTUv2p6259Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6259)
)
dpsRTUv2p6259Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6259Set.setStatus(
        "current"
    )

dpsRTUv2p6260Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6260)
)
dpsRTUv2p6260Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6260Set.setStatus(
        "current"
    )

dpsRTUv2p6261Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6261)
)
dpsRTUv2p6261Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6261Set.setStatus(
        "current"
    )

dpsRTUv2p6262Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6262)
)
dpsRTUv2p6262Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6262Set.setStatus(
        "current"
    )

dpsRTUv2p6263Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6263)
)
dpsRTUv2p6263Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6263Set.setStatus(
        "current"
    )

dpsRTUv2p6264Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6264)
)
dpsRTUv2p6264Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6264Set.setStatus(
        "current"
    )

dpsRTUv2p6265Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6265)
)
dpsRTUv2p6265Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6265Set.setStatus(
        "current"
    )

dpsRTUv2p6266Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6266)
)
dpsRTUv2p6266Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6266Set.setStatus(
        "current"
    )

dpsRTUv2p6267Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6267)
)
dpsRTUv2p6267Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6267Set.setStatus(
        "current"
    )

dpsRTUv2p6268Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6268)
)
dpsRTUv2p6268Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6268Set.setStatus(
        "current"
    )

dpsRTUv2p6269Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6269)
)
dpsRTUv2p6269Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6269Set.setStatus(
        "current"
    )

dpsRTUv2p6270Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6270)
)
dpsRTUv2p6270Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6270Set.setStatus(
        "current"
    )

dpsRTUv2p6271Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6271)
)
dpsRTUv2p6271Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6271Set.setStatus(
        "current"
    )

dpsRTUv2p6272Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6272)
)
dpsRTUv2p6272Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6272Set.setStatus(
        "current"
    )

dpsRTUv2p6273Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6273)
)
dpsRTUv2p6273Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6273Set.setStatus(
        "current"
    )

dpsRTUv2p6274Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6274)
)
dpsRTUv2p6274Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6274Set.setStatus(
        "current"
    )

dpsRTUv2p6275Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6275)
)
dpsRTUv2p6275Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6275Set.setStatus(
        "current"
    )

dpsRTUv2p6276Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6276)
)
dpsRTUv2p6276Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6276Set.setStatus(
        "current"
    )

dpsRTUv2p6277Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6277)
)
dpsRTUv2p6277Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6277Set.setStatus(
        "current"
    )

dpsRTUv2p6278Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6278)
)
dpsRTUv2p6278Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6278Set.setStatus(
        "current"
    )

dpsRTUv2p6279Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6279)
)
dpsRTUv2p6279Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6279Set.setStatus(
        "current"
    )

dpsRTUv2p6280Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6280)
)
dpsRTUv2p6280Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6280Set.setStatus(
        "current"
    )

dpsRTUv2p6281Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6281)
)
dpsRTUv2p6281Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6281Set.setStatus(
        "current"
    )

dpsRTUv2p6282Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6282)
)
dpsRTUv2p6282Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6282Set.setStatus(
        "current"
    )

dpsRTUv2p6283Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6283)
)
dpsRTUv2p6283Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6283Set.setStatus(
        "current"
    )

dpsRTUv2p6284Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6284)
)
dpsRTUv2p6284Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6284Set.setStatus(
        "current"
    )

dpsRTUv2p6285Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6285)
)
dpsRTUv2p6285Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6285Set.setStatus(
        "current"
    )

dpsRTUv2p6286Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6286)
)
dpsRTUv2p6286Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6286Set.setStatus(
        "current"
    )

dpsRTUv2p6287Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6287)
)
dpsRTUv2p6287Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6287Set.setStatus(
        "current"
    )

dpsRTUv2p6288Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6288)
)
dpsRTUv2p6288Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6288Set.setStatus(
        "current"
    )

dpsRTUv2p6289Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6289)
)
dpsRTUv2p6289Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6289Set.setStatus(
        "current"
    )

dpsRTUv2p6290Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6290)
)
dpsRTUv2p6290Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6290Set.setStatus(
        "current"
    )

dpsRTUv2p6291Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6291)
)
dpsRTUv2p6291Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6291Set.setStatus(
        "current"
    )

dpsRTUv2p6292Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6292)
)
dpsRTUv2p6292Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6292Set.setStatus(
        "current"
    )

dpsRTUv2p6293Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6293)
)
dpsRTUv2p6293Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6293Set.setStatus(
        "current"
    )

dpsRTUv2p6294Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6294)
)
dpsRTUv2p6294Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6294Set.setStatus(
        "current"
    )

dpsRTUv2p6295Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6295)
)
dpsRTUv2p6295Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6295Set.setStatus(
        "current"
    )

dpsRTUv2p6296Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6296)
)
dpsRTUv2p6296Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6296Set.setStatus(
        "current"
    )

dpsRTUv2p6297Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6297)
)
dpsRTUv2p6297Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6297Set.setStatus(
        "current"
    )

dpsRTUv2p6298Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6298)
)
dpsRTUv2p6298Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6298Set.setStatus(
        "current"
    )

dpsRTUv2p6299Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6299)
)
dpsRTUv2p6299Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6299Set.setStatus(
        "current"
    )

dpsRTUv2p6300Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6300)
)
dpsRTUv2p6300Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6300Set.setStatus(
        "current"
    )

dpsRTUv2p6301Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6301)
)
dpsRTUv2p6301Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6301Set.setStatus(
        "current"
    )

dpsRTUv2p6302Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6302)
)
dpsRTUv2p6302Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6302Set.setStatus(
        "current"
    )

dpsRTUv2p6303Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6303)
)
dpsRTUv2p6303Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6303Set.setStatus(
        "current"
    )

dpsRTUv2p6304Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6304)
)
dpsRTUv2p6304Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6304Set.setStatus(
        "current"
    )

dpsRTUv2p6321Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6321)
)
dpsRTUv2p6321Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6321Set.setStatus(
        "current"
    )

dpsRTUv2p6322Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6322)
)
dpsRTUv2p6322Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6322Set.setStatus(
        "current"
    )

dpsRTUv2p6323Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6323)
)
dpsRTUv2p6323Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6323Set.setStatus(
        "current"
    )

dpsRTUv2p6324Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6324)
)
dpsRTUv2p6324Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6324Set.setStatus(
        "current"
    )

dpsRTUv2p6325Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6325)
)
dpsRTUv2p6325Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6325Set.setStatus(
        "current"
    )

dpsRTUv2p6326Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6326)
)
dpsRTUv2p6326Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6326Set.setStatus(
        "current"
    )

dpsRTUv2p6327Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6327)
)
dpsRTUv2p6327Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6327Set.setStatus(
        "current"
    )

dpsRTUv2p6328Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6328)
)
dpsRTUv2p6328Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6328Set.setStatus(
        "current"
    )

dpsRTUv2p6385Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6385)
)
dpsRTUv2p6385Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6385Set.setStatus(
        "current"
    )

dpsRTUv2p6386Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6386)
)
dpsRTUv2p6386Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6386Set.setStatus(
        "current"
    )

dpsRTUv2p6387Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6387)
)
dpsRTUv2p6387Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6387Set.setStatus(
        "current"
    )

dpsRTUv2p6388Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6388)
)
dpsRTUv2p6388Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6388Set.setStatus(
        "current"
    )

dpsRTUv2p6389Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6389)
)
dpsRTUv2p6389Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6389Set.setStatus(
        "current"
    )

dpsRTUv2p6390Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6390)
)
dpsRTUv2p6390Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6390Set.setStatus(
        "current"
    )

dpsRTUv2p6391Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6391)
)
dpsRTUv2p6391Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6391Set.setStatus(
        "current"
    )

dpsRTUv2p6392Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6392)
)
dpsRTUv2p6392Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6392Set.setStatus(
        "current"
    )

dpsRTUv2p6393Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6393)
)
dpsRTUv2p6393Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6393Set.setStatus(
        "current"
    )

dpsRTUv2p6394Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6394)
)
dpsRTUv2p6394Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6394Set.setStatus(
        "current"
    )

dpsRTUv2p6395Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6395)
)
dpsRTUv2p6395Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6395Set.setStatus(
        "current"
    )

dpsRTUv2p6396Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6396)
)
dpsRTUv2p6396Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6396Set.setStatus(
        "current"
    )

dpsRTUv2p6397Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6397)
)
dpsRTUv2p6397Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6397Set.setStatus(
        "current"
    )

dpsRTUv2p6398Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6398)
)
dpsRTUv2p6398Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6398Set.setStatus(
        "current"
    )

dpsRTUv2p6399Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6399)
)
dpsRTUv2p6399Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6399Set.setStatus(
        "current"
    )

dpsRTUv2p6400Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6400)
)
dpsRTUv2p6400Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6400Set.setStatus(
        "current"
    )

dpsRTUv2p6401Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6401)
)
dpsRTUv2p6401Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6401Set.setStatus(
        "current"
    )

dpsRTUv2p6402Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6402)
)
dpsRTUv2p6402Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6402Set.setStatus(
        "current"
    )

dpsRTUv2p6403Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6403)
)
dpsRTUv2p6403Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6403Set.setStatus(
        "current"
    )

dpsRTUv2p6404Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6404)
)
dpsRTUv2p6404Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6404Set.setStatus(
        "current"
    )

dpsRTUv2p6405Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6405)
)
dpsRTUv2p6405Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6405Set.setStatus(
        "current"
    )

dpsRTUv2p6406Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6406)
)
dpsRTUv2p6406Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6406Set.setStatus(
        "current"
    )

dpsRTUv2p6407Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6407)
)
dpsRTUv2p6407Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6407Set.setStatus(
        "current"
    )

dpsRTUv2p6408Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6408)
)
dpsRTUv2p6408Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6408Set.setStatus(
        "current"
    )

dpsRTUv2p6409Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6409)
)
dpsRTUv2p6409Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6409Set.setStatus(
        "current"
    )

dpsRTUv2p6410Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6410)
)
dpsRTUv2p6410Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6410Set.setStatus(
        "current"
    )

dpsRTUv2p6411Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6411)
)
dpsRTUv2p6411Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6411Set.setStatus(
        "current"
    )

dpsRTUv2p6412Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6412)
)
dpsRTUv2p6412Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6412Set.setStatus(
        "current"
    )

dpsRTUv2p6413Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6413)
)
dpsRTUv2p6413Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6413Set.setStatus(
        "current"
    )

dpsRTUv2p6414Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6414)
)
dpsRTUv2p6414Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6414Set.setStatus(
        "current"
    )

dpsRTUv2p6415Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6415)
)
dpsRTUv2p6415Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6415Set.setStatus(
        "current"
    )

dpsRTUv2p6416Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6416)
)
dpsRTUv2p6416Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6416Set.setStatus(
        "current"
    )

dpsRTUv2p6417Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6417)
)
dpsRTUv2p6417Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6417Set.setStatus(
        "current"
    )

dpsRTUv2p6418Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6418)
)
dpsRTUv2p6418Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6418Set.setStatus(
        "current"
    )

dpsRTUv2p6419Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6419)
)
dpsRTUv2p6419Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6419Set.setStatus(
        "current"
    )

dpsRTUv2p6420Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6420)
)
dpsRTUv2p6420Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6420Set.setStatus(
        "current"
    )

dpsRTUv2p6421Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6421)
)
dpsRTUv2p6421Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6421Set.setStatus(
        "current"
    )

dpsRTUv2p6422Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6422)
)
dpsRTUv2p6422Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6422Set.setStatus(
        "current"
    )

dpsRTUv2p6423Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6423)
)
dpsRTUv2p6423Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6423Set.setStatus(
        "current"
    )

dpsRTUv2p6424Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6424)
)
dpsRTUv2p6424Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6424Set.setStatus(
        "current"
    )

dpsRTUv2p6425Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6425)
)
dpsRTUv2p6425Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6425Set.setStatus(
        "current"
    )

dpsRTUv2p6426Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6426)
)
dpsRTUv2p6426Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6426Set.setStatus(
        "current"
    )

dpsRTUv2p6427Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6427)
)
dpsRTUv2p6427Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6427Set.setStatus(
        "current"
    )

dpsRTUv2p6428Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6428)
)
dpsRTUv2p6428Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6428Set.setStatus(
        "current"
    )

dpsRTUv2p6429Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6429)
)
dpsRTUv2p6429Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6429Set.setStatus(
        "current"
    )

dpsRTUv2p6430Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6430)
)
dpsRTUv2p6430Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6430Set.setStatus(
        "current"
    )

dpsRTUv2p6431Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6431)
)
dpsRTUv2p6431Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6431Set.setStatus(
        "current"
    )

dpsRTUv2p6432Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6432)
)
dpsRTUv2p6432Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6432Set.setStatus(
        "current"
    )

dpsRTUv2p6433Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6433)
)
dpsRTUv2p6433Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6433Set.setStatus(
        "current"
    )

dpsRTUv2p6434Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6434)
)
dpsRTUv2p6434Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6434Set.setStatus(
        "current"
    )

dpsRTUv2p6435Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6435)
)
dpsRTUv2p6435Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6435Set.setStatus(
        "current"
    )

dpsRTUv2p6436Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6436)
)
dpsRTUv2p6436Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6436Set.setStatus(
        "current"
    )

dpsRTUv2p6437Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6437)
)
dpsRTUv2p6437Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6437Set.setStatus(
        "current"
    )

dpsRTUv2p6438Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6438)
)
dpsRTUv2p6438Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6438Set.setStatus(
        "current"
    )

dpsRTUv2p6439Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6439)
)
dpsRTUv2p6439Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6439Set.setStatus(
        "current"
    )

dpsRTUv2p6440Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6440)
)
dpsRTUv2p6440Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6440Set.setStatus(
        "current"
    )

dpsRTUv2p6441Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6441)
)
dpsRTUv2p6441Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6441Set.setStatus(
        "current"
    )

dpsRTUv2p6442Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6442)
)
dpsRTUv2p6442Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6442Set.setStatus(
        "current"
    )

dpsRTUv2p6443Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6443)
)
dpsRTUv2p6443Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6443Set.setStatus(
        "current"
    )

dpsRTUv2p6444Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6444)
)
dpsRTUv2p6444Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6444Set.setStatus(
        "current"
    )

dpsRTUv2p6445Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6445)
)
dpsRTUv2p6445Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6445Set.setStatus(
        "current"
    )

dpsRTUv2p6446Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6446)
)
dpsRTUv2p6446Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6446Set.setStatus(
        "current"
    )

dpsRTUv2p6447Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6447)
)
dpsRTUv2p6447Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6447Set.setStatus(
        "current"
    )

dpsRTUv2p6448Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6448)
)
dpsRTUv2p6448Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6448Set.setStatus(
        "current"
    )

dpsRTUv2p6449Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6449)
)
dpsRTUv2p6449Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6449Set.setStatus(
        "current"
    )

dpsRTUv2p6450Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6450)
)
dpsRTUv2p6450Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6450Set.setStatus(
        "current"
    )

dpsRTUv2p6451Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6451)
)
dpsRTUv2p6451Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6451Set.setStatus(
        "current"
    )

dpsRTUv2p6452Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6452)
)
dpsRTUv2p6452Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6452Set.setStatus(
        "current"
    )

dpsRTUv2p6453Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6453)
)
dpsRTUv2p6453Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6453Set.setStatus(
        "current"
    )

dpsRTUv2p6454Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6454)
)
dpsRTUv2p6454Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6454Set.setStatus(
        "current"
    )

dpsRTUv2p6455Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6455)
)
dpsRTUv2p6455Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6455Set.setStatus(
        "current"
    )

dpsRTUv2p6456Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6456)
)
dpsRTUv2p6456Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6456Set.setStatus(
        "current"
    )

dpsRTUv2p6457Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6457)
)
dpsRTUv2p6457Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6457Set.setStatus(
        "current"
    )

dpsRTUv2p6458Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6458)
)
dpsRTUv2p6458Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6458Set.setStatus(
        "current"
    )

dpsRTUv2p6459Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6459)
)
dpsRTUv2p6459Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6459Set.setStatus(
        "current"
    )

dpsRTUv2p6460Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6460)
)
dpsRTUv2p6460Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6460Set.setStatus(
        "current"
    )

dpsRTUv2p6461Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6461)
)
dpsRTUv2p6461Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6461Set.setStatus(
        "current"
    )

dpsRTUv2p6462Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6462)
)
dpsRTUv2p6462Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6462Set.setStatus(
        "current"
    )

dpsRTUv2p6463Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6463)
)
dpsRTUv2p6463Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6463Set.setStatus(
        "current"
    )

dpsRTUv2p6464Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6464)
)
dpsRTUv2p6464Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6464Set.setStatus(
        "current"
    )

dpsRTUv2p6465Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6465)
)
dpsRTUv2p6465Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6465Set.setStatus(
        "current"
    )

dpsRTUv2p6466Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6466)
)
dpsRTUv2p6466Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6466Set.setStatus(
        "current"
    )

dpsRTUv2p6467Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6467)
)
dpsRTUv2p6467Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6467Set.setStatus(
        "current"
    )

dpsRTUv2p6468Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6468)
)
dpsRTUv2p6468Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6468Set.setStatus(
        "current"
    )

dpsRTUv2p6469Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6469)
)
dpsRTUv2p6469Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6469Set.setStatus(
        "current"
    )

dpsRTUv2p6470Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6470)
)
dpsRTUv2p6470Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6470Set.setStatus(
        "current"
    )

dpsRTUv2p6471Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6471)
)
dpsRTUv2p6471Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6471Set.setStatus(
        "current"
    )

dpsRTUv2p6472Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6472)
)
dpsRTUv2p6472Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6472Set.setStatus(
        "current"
    )

dpsRTUv2p6473Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6473)
)
dpsRTUv2p6473Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6473Set.setStatus(
        "current"
    )

dpsRTUv2p6474Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6474)
)
dpsRTUv2p6474Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6474Set.setStatus(
        "current"
    )

dpsRTUv2p6475Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6475)
)
dpsRTUv2p6475Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6475Set.setStatus(
        "current"
    )

dpsRTUv2p6476Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6476)
)
dpsRTUv2p6476Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6476Set.setStatus(
        "current"
    )

dpsRTUv2p6477Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6477)
)
dpsRTUv2p6477Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6477Set.setStatus(
        "current"
    )

dpsRTUv2p6478Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6478)
)
dpsRTUv2p6478Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6478Set.setStatus(
        "current"
    )

dpsRTUv2p6479Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6479)
)
dpsRTUv2p6479Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6479Set.setStatus(
        "current"
    )

dpsRTUv2p6480Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6480)
)
dpsRTUv2p6480Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p6480Set.setStatus(
        "current"
    )

dpsRTUv2p7001Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7001)
)
dpsRTUv2p7001Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7001Clr.setStatus(
        "current"
    )

dpsRTUv2p7002Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7002)
)
dpsRTUv2p7002Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7002Clr.setStatus(
        "current"
    )

dpsRTUv2p7003Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7003)
)
dpsRTUv2p7003Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7003Clr.setStatus(
        "current"
    )

dpsRTUv2p7004Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7004)
)
dpsRTUv2p7004Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7004Clr.setStatus(
        "current"
    )

dpsRTUv2p7005Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7005)
)
dpsRTUv2p7005Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7005Clr.setStatus(
        "current"
    )

dpsRTUv2p7006Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7006)
)
dpsRTUv2p7006Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7006Clr.setStatus(
        "current"
    )

dpsRTUv2p7007Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7007)
)
dpsRTUv2p7007Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7007Clr.setStatus(
        "current"
    )

dpsRTUv2p7008Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7008)
)
dpsRTUv2p7008Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7008Clr.setStatus(
        "current"
    )

dpsRTUv2p7009Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7009)
)
dpsRTUv2p7009Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7009Clr.setStatus(
        "current"
    )

dpsRTUv2p7010Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7010)
)
dpsRTUv2p7010Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7010Clr.setStatus(
        "current"
    )

dpsRTUv2p7011Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7011)
)
dpsRTUv2p7011Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7011Clr.setStatus(
        "current"
    )

dpsRTUv2p7012Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7012)
)
dpsRTUv2p7012Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7012Clr.setStatus(
        "current"
    )

dpsRTUv2p7013Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7013)
)
dpsRTUv2p7013Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7013Clr.setStatus(
        "current"
    )

dpsRTUv2p7014Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7014)
)
dpsRTUv2p7014Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7014Clr.setStatus(
        "current"
    )

dpsRTUv2p7015Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7015)
)
dpsRTUv2p7015Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7015Clr.setStatus(
        "current"
    )

dpsRTUv2p7016Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7016)
)
dpsRTUv2p7016Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7016Clr.setStatus(
        "current"
    )

dpsRTUv2p7017Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7017)
)
dpsRTUv2p7017Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7017Clr.setStatus(
        "current"
    )

dpsRTUv2p7018Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7018)
)
dpsRTUv2p7018Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7018Clr.setStatus(
        "current"
    )

dpsRTUv2p7019Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7019)
)
dpsRTUv2p7019Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7019Clr.setStatus(
        "current"
    )

dpsRTUv2p7020Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7020)
)
dpsRTUv2p7020Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7020Clr.setStatus(
        "current"
    )

dpsRTUv2p7021Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7021)
)
dpsRTUv2p7021Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7021Clr.setStatus(
        "current"
    )

dpsRTUv2p7022Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7022)
)
dpsRTUv2p7022Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7022Clr.setStatus(
        "current"
    )

dpsRTUv2p7023Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7023)
)
dpsRTUv2p7023Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7023Clr.setStatus(
        "current"
    )

dpsRTUv2p7024Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7024)
)
dpsRTUv2p7024Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7024Clr.setStatus(
        "current"
    )

dpsRTUv2p7025Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7025)
)
dpsRTUv2p7025Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7025Clr.setStatus(
        "current"
    )

dpsRTUv2p7026Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7026)
)
dpsRTUv2p7026Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7026Clr.setStatus(
        "current"
    )

dpsRTUv2p7027Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7027)
)
dpsRTUv2p7027Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7027Clr.setStatus(
        "current"
    )

dpsRTUv2p7028Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7028)
)
dpsRTUv2p7028Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7028Clr.setStatus(
        "current"
    )

dpsRTUv2p7029Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7029)
)
dpsRTUv2p7029Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7029Clr.setStatus(
        "current"
    )

dpsRTUv2p7030Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7030)
)
dpsRTUv2p7030Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7030Clr.setStatus(
        "current"
    )

dpsRTUv2p7031Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7031)
)
dpsRTUv2p7031Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7031Clr.setStatus(
        "current"
    )

dpsRTUv2p7032Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7032)
)
dpsRTUv2p7032Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7032Clr.setStatus(
        "current"
    )

dpsRTUv2p7033Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7033)
)
dpsRTUv2p7033Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7033Clr.setStatus(
        "current"
    )

dpsRTUv2p7034Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7034)
)
dpsRTUv2p7034Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7034Clr.setStatus(
        "current"
    )

dpsRTUv2p7035Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7035)
)
dpsRTUv2p7035Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7035Clr.setStatus(
        "current"
    )

dpsRTUv2p7036Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7036)
)
dpsRTUv2p7036Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7036Clr.setStatus(
        "current"
    )

dpsRTUv2p7037Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7037)
)
dpsRTUv2p7037Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7037Clr.setStatus(
        "current"
    )

dpsRTUv2p7038Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7038)
)
dpsRTUv2p7038Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7038Clr.setStatus(
        "current"
    )

dpsRTUv2p7039Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7039)
)
dpsRTUv2p7039Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7039Clr.setStatus(
        "current"
    )

dpsRTUv2p7040Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7040)
)
dpsRTUv2p7040Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7040Clr.setStatus(
        "current"
    )

dpsRTUv2p7041Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7041)
)
dpsRTUv2p7041Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7041Clr.setStatus(
        "current"
    )

dpsRTUv2p7042Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7042)
)
dpsRTUv2p7042Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7042Clr.setStatus(
        "current"
    )

dpsRTUv2p7043Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7043)
)
dpsRTUv2p7043Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7043Clr.setStatus(
        "current"
    )

dpsRTUv2p7044Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7044)
)
dpsRTUv2p7044Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7044Clr.setStatus(
        "current"
    )

dpsRTUv2p7045Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7045)
)
dpsRTUv2p7045Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7045Clr.setStatus(
        "current"
    )

dpsRTUv2p7046Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7046)
)
dpsRTUv2p7046Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7046Clr.setStatus(
        "current"
    )

dpsRTUv2p7047Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7047)
)
dpsRTUv2p7047Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7047Clr.setStatus(
        "current"
    )

dpsRTUv2p7048Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7048)
)
dpsRTUv2p7048Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7048Clr.setStatus(
        "current"
    )

dpsRTUv2p7049Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7049)
)
dpsRTUv2p7049Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7049Clr.setStatus(
        "current"
    )

dpsRTUv2p7050Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7050)
)
dpsRTUv2p7050Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7050Clr.setStatus(
        "current"
    )

dpsRTUv2p7051Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7051)
)
dpsRTUv2p7051Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7051Clr.setStatus(
        "current"
    )

dpsRTUv2p7052Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7052)
)
dpsRTUv2p7052Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7052Clr.setStatus(
        "current"
    )

dpsRTUv2p7053Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7053)
)
dpsRTUv2p7053Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7053Clr.setStatus(
        "current"
    )

dpsRTUv2p7054Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7054)
)
dpsRTUv2p7054Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7054Clr.setStatus(
        "current"
    )

dpsRTUv2p7055Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7055)
)
dpsRTUv2p7055Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7055Clr.setStatus(
        "current"
    )

dpsRTUv2p7056Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7056)
)
dpsRTUv2p7056Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7056Clr.setStatus(
        "current"
    )

dpsRTUv2p7057Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7057)
)
dpsRTUv2p7057Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7057Clr.setStatus(
        "current"
    )

dpsRTUv2p7058Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7058)
)
dpsRTUv2p7058Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7058Clr.setStatus(
        "current"
    )

dpsRTUv2p7059Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7059)
)
dpsRTUv2p7059Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7059Clr.setStatus(
        "current"
    )

dpsRTUv2p7060Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7060)
)
dpsRTUv2p7060Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7060Clr.setStatus(
        "current"
    )

dpsRTUv2p7061Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7061)
)
dpsRTUv2p7061Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7061Clr.setStatus(
        "current"
    )

dpsRTUv2p7062Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7062)
)
dpsRTUv2p7062Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7062Clr.setStatus(
        "current"
    )

dpsRTUv2p7063Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7063)
)
dpsRTUv2p7063Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7063Clr.setStatus(
        "current"
    )

dpsRTUv2p7064Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7064)
)
dpsRTUv2p7064Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7064Clr.setStatus(
        "current"
    )

dpsRTUv2p7065Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7065)
)
dpsRTUv2p7065Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7065Clr.setStatus(
        "current"
    )

dpsRTUv2p7066Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7066)
)
dpsRTUv2p7066Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7066Clr.setStatus(
        "current"
    )

dpsRTUv2p7067Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7067)
)
dpsRTUv2p7067Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7067Clr.setStatus(
        "current"
    )

dpsRTUv2p7068Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7068)
)
dpsRTUv2p7068Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7068Clr.setStatus(
        "current"
    )

dpsRTUv2p7069Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7069)
)
dpsRTUv2p7069Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7069Clr.setStatus(
        "current"
    )

dpsRTUv2p7070Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7070)
)
dpsRTUv2p7070Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7070Clr.setStatus(
        "current"
    )

dpsRTUv2p7071Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7071)
)
dpsRTUv2p7071Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7071Clr.setStatus(
        "current"
    )

dpsRTUv2p7072Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7072)
)
dpsRTUv2p7072Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7072Clr.setStatus(
        "current"
    )

dpsRTUv2p7081Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7081)
)
dpsRTUv2p7081Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7081Clr.setStatus(
        "current"
    )

dpsRTUv2p7082Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7082)
)
dpsRTUv2p7082Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7082Clr.setStatus(
        "current"
    )

dpsRTUv2p7083Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7083)
)
dpsRTUv2p7083Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7083Clr.setStatus(
        "current"
    )

dpsRTUv2p7084Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7084)
)
dpsRTUv2p7084Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7084Clr.setStatus(
        "current"
    )

dpsRTUv2p7085Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7085)
)
dpsRTUv2p7085Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7085Clr.setStatus(
        "current"
    )

dpsRTUv2p7086Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7086)
)
dpsRTUv2p7086Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7086Clr.setStatus(
        "current"
    )

dpsRTUv2p7087Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7087)
)
dpsRTUv2p7087Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7087Clr.setStatus(
        "current"
    )

dpsRTUv2p7088Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7088)
)
dpsRTUv2p7088Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7088Clr.setStatus(
        "current"
    )

dpsRTUv2p7089Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7089)
)
dpsRTUv2p7089Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7089Clr.setStatus(
        "current"
    )

dpsRTUv2p7090Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7090)
)
dpsRTUv2p7090Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7090Clr.setStatus(
        "current"
    )

dpsRTUv2p7091Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7091)
)
dpsRTUv2p7091Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7091Clr.setStatus(
        "current"
    )

dpsRTUv2p7092Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7092)
)
dpsRTUv2p7092Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7092Clr.setStatus(
        "current"
    )

dpsRTUv2p7093Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7093)
)
dpsRTUv2p7093Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7093Clr.setStatus(
        "current"
    )

dpsRTUv2p7094Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7094)
)
dpsRTUv2p7094Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7094Clr.setStatus(
        "current"
    )

dpsRTUv2p7095Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7095)
)
dpsRTUv2p7095Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7095Clr.setStatus(
        "current"
    )

dpsRTUv2p7096Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7096)
)
dpsRTUv2p7096Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7096Clr.setStatus(
        "current"
    )

dpsRTUv2p7129Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7129)
)
dpsRTUv2p7129Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7129Clr.setStatus(
        "current"
    )

dpsRTUv2p7130Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7130)
)
dpsRTUv2p7130Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7130Clr.setStatus(
        "current"
    )

dpsRTUv2p7131Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7131)
)
dpsRTUv2p7131Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7131Clr.setStatus(
        "current"
    )

dpsRTUv2p7132Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7132)
)
dpsRTUv2p7132Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7132Clr.setStatus(
        "current"
    )

dpsRTUv2p7133Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7133)
)
dpsRTUv2p7133Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7133Clr.setStatus(
        "current"
    )

dpsRTUv2p7134Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7134)
)
dpsRTUv2p7134Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7134Clr.setStatus(
        "current"
    )

dpsRTUv2p7135Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7135)
)
dpsRTUv2p7135Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7135Clr.setStatus(
        "current"
    )

dpsRTUv2p7136Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7136)
)
dpsRTUv2p7136Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7136Clr.setStatus(
        "current"
    )

dpsRTUv2p7137Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7137)
)
dpsRTUv2p7137Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7137Clr.setStatus(
        "current"
    )

dpsRTUv2p7138Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7138)
)
dpsRTUv2p7138Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7138Clr.setStatus(
        "current"
    )

dpsRTUv2p7139Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7139)
)
dpsRTUv2p7139Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7139Clr.setStatus(
        "current"
    )

dpsRTUv2p7140Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7140)
)
dpsRTUv2p7140Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7140Clr.setStatus(
        "current"
    )

dpsRTUv2p7141Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7141)
)
dpsRTUv2p7141Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7141Clr.setStatus(
        "current"
    )

dpsRTUv2p7142Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7142)
)
dpsRTUv2p7142Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7142Clr.setStatus(
        "current"
    )

dpsRTUv2p7143Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7143)
)
dpsRTUv2p7143Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7143Clr.setStatus(
        "current"
    )

dpsRTUv2p7144Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7144)
)
dpsRTUv2p7144Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7144Clr.setStatus(
        "current"
    )

dpsRTUv2p7145Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7145)
)
dpsRTUv2p7145Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7145Clr.setStatus(
        "current"
    )

dpsRTUv2p7146Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7146)
)
dpsRTUv2p7146Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7146Clr.setStatus(
        "current"
    )

dpsRTUv2p7147Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7147)
)
dpsRTUv2p7147Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7147Clr.setStatus(
        "current"
    )

dpsRTUv2p7148Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7148)
)
dpsRTUv2p7148Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7148Clr.setStatus(
        "current"
    )

dpsRTUv2p7149Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7149)
)
dpsRTUv2p7149Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7149Clr.setStatus(
        "current"
    )

dpsRTUv2p7150Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7150)
)
dpsRTUv2p7150Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7150Clr.setStatus(
        "current"
    )

dpsRTUv2p7151Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7151)
)
dpsRTUv2p7151Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7151Clr.setStatus(
        "current"
    )

dpsRTUv2p7152Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7152)
)
dpsRTUv2p7152Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7152Clr.setStatus(
        "current"
    )

dpsRTUv2p7153Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7153)
)
dpsRTUv2p7153Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7153Clr.setStatus(
        "current"
    )

dpsRTUv2p7154Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7154)
)
dpsRTUv2p7154Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7154Clr.setStatus(
        "current"
    )

dpsRTUv2p7155Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7155)
)
dpsRTUv2p7155Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7155Clr.setStatus(
        "current"
    )

dpsRTUv2p7156Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7156)
)
dpsRTUv2p7156Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7156Clr.setStatus(
        "current"
    )

dpsRTUv2p7157Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7157)
)
dpsRTUv2p7157Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7157Clr.setStatus(
        "current"
    )

dpsRTUv2p7158Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7158)
)
dpsRTUv2p7158Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7158Clr.setStatus(
        "current"
    )

dpsRTUv2p7159Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7159)
)
dpsRTUv2p7159Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7159Clr.setStatus(
        "current"
    )

dpsRTUv2p7160Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7160)
)
dpsRTUv2p7160Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7160Clr.setStatus(
        "current"
    )

dpsRTUv2p7161Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7161)
)
dpsRTUv2p7161Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7161Clr.setStatus(
        "current"
    )

dpsRTUv2p7162Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7162)
)
dpsRTUv2p7162Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7162Clr.setStatus(
        "current"
    )

dpsRTUv2p7163Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7163)
)
dpsRTUv2p7163Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7163Clr.setStatus(
        "current"
    )

dpsRTUv2p7164Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7164)
)
dpsRTUv2p7164Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7164Clr.setStatus(
        "current"
    )

dpsRTUv2p7165Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7165)
)
dpsRTUv2p7165Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7165Clr.setStatus(
        "current"
    )

dpsRTUv2p7166Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7166)
)
dpsRTUv2p7166Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7166Clr.setStatus(
        "current"
    )

dpsRTUv2p7167Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7167)
)
dpsRTUv2p7167Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7167Clr.setStatus(
        "current"
    )

dpsRTUv2p7168Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7168)
)
dpsRTUv2p7168Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7168Clr.setStatus(
        "current"
    )

dpsRTUv2p7169Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7169)
)
dpsRTUv2p7169Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7169Clr.setStatus(
        "current"
    )

dpsRTUv2p7170Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7170)
)
dpsRTUv2p7170Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7170Clr.setStatus(
        "current"
    )

dpsRTUv2p7171Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7171)
)
dpsRTUv2p7171Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7171Clr.setStatus(
        "current"
    )

dpsRTUv2p7172Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7172)
)
dpsRTUv2p7172Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7172Clr.setStatus(
        "current"
    )

dpsRTUv2p7173Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7173)
)
dpsRTUv2p7173Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7173Clr.setStatus(
        "current"
    )

dpsRTUv2p7174Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7174)
)
dpsRTUv2p7174Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7174Clr.setStatus(
        "current"
    )

dpsRTUv2p7175Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7175)
)
dpsRTUv2p7175Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7175Clr.setStatus(
        "current"
    )

dpsRTUv2p7176Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7176)
)
dpsRTUv2p7176Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7176Clr.setStatus(
        "current"
    )

dpsRTUv2p7193Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7193)
)
dpsRTUv2p7193Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7193Clr.setStatus(
        "current"
    )

dpsRTUv2p7194Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7194)
)
dpsRTUv2p7194Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7194Clr.setStatus(
        "current"
    )

dpsRTUv2p7195Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7195)
)
dpsRTUv2p7195Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7195Clr.setStatus(
        "current"
    )

dpsRTUv2p7196Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7196)
)
dpsRTUv2p7196Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7196Clr.setStatus(
        "current"
    )

dpsRTUv2p7197Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7197)
)
dpsRTUv2p7197Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7197Clr.setStatus(
        "current"
    )

dpsRTUv2p7198Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7198)
)
dpsRTUv2p7198Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7198Clr.setStatus(
        "current"
    )

dpsRTUv2p7199Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7199)
)
dpsRTUv2p7199Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7199Clr.setStatus(
        "current"
    )

dpsRTUv2p7200Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7200)
)
dpsRTUv2p7200Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7200Clr.setStatus(
        "current"
    )

dpsRTUv2p7257Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7257)
)
dpsRTUv2p7257Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7257Clr.setStatus(
        "current"
    )

dpsRTUv2p7258Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7258)
)
dpsRTUv2p7258Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7258Clr.setStatus(
        "current"
    )

dpsRTUv2p7259Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7259)
)
dpsRTUv2p7259Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7259Clr.setStatus(
        "current"
    )

dpsRTUv2p7260Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7260)
)
dpsRTUv2p7260Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7260Clr.setStatus(
        "current"
    )

dpsRTUv2p7261Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7261)
)
dpsRTUv2p7261Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7261Clr.setStatus(
        "current"
    )

dpsRTUv2p7262Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7262)
)
dpsRTUv2p7262Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7262Clr.setStatus(
        "current"
    )

dpsRTUv2p7263Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7263)
)
dpsRTUv2p7263Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7263Clr.setStatus(
        "current"
    )

dpsRTUv2p7264Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7264)
)
dpsRTUv2p7264Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7264Clr.setStatus(
        "current"
    )

dpsRTUv2p7265Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7265)
)
dpsRTUv2p7265Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7265Clr.setStatus(
        "current"
    )

dpsRTUv2p7266Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7266)
)
dpsRTUv2p7266Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7266Clr.setStatus(
        "current"
    )

dpsRTUv2p7267Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7267)
)
dpsRTUv2p7267Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7267Clr.setStatus(
        "current"
    )

dpsRTUv2p7268Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7268)
)
dpsRTUv2p7268Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7268Clr.setStatus(
        "current"
    )

dpsRTUv2p7269Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7269)
)
dpsRTUv2p7269Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7269Clr.setStatus(
        "current"
    )

dpsRTUv2p7270Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7270)
)
dpsRTUv2p7270Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7270Clr.setStatus(
        "current"
    )

dpsRTUv2p7271Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7271)
)
dpsRTUv2p7271Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7271Clr.setStatus(
        "current"
    )

dpsRTUv2p7272Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7272)
)
dpsRTUv2p7272Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7272Clr.setStatus(
        "current"
    )

dpsRTUv2p7273Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7273)
)
dpsRTUv2p7273Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7273Clr.setStatus(
        "current"
    )

dpsRTUv2p7274Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7274)
)
dpsRTUv2p7274Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7274Clr.setStatus(
        "current"
    )

dpsRTUv2p7275Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7275)
)
dpsRTUv2p7275Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7275Clr.setStatus(
        "current"
    )

dpsRTUv2p7276Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7276)
)
dpsRTUv2p7276Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7276Clr.setStatus(
        "current"
    )

dpsRTUv2p7277Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7277)
)
dpsRTUv2p7277Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7277Clr.setStatus(
        "current"
    )

dpsRTUv2p7278Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7278)
)
dpsRTUv2p7278Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7278Clr.setStatus(
        "current"
    )

dpsRTUv2p7279Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7279)
)
dpsRTUv2p7279Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7279Clr.setStatus(
        "current"
    )

dpsRTUv2p7280Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7280)
)
dpsRTUv2p7280Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7280Clr.setStatus(
        "current"
    )

dpsRTUv2p7281Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7281)
)
dpsRTUv2p7281Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7281Clr.setStatus(
        "current"
    )

dpsRTUv2p7282Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7282)
)
dpsRTUv2p7282Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7282Clr.setStatus(
        "current"
    )

dpsRTUv2p7283Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7283)
)
dpsRTUv2p7283Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7283Clr.setStatus(
        "current"
    )

dpsRTUv2p7284Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7284)
)
dpsRTUv2p7284Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7284Clr.setStatus(
        "current"
    )

dpsRTUv2p7285Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7285)
)
dpsRTUv2p7285Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7285Clr.setStatus(
        "current"
    )

dpsRTUv2p7286Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7286)
)
dpsRTUv2p7286Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7286Clr.setStatus(
        "current"
    )

dpsRTUv2p7287Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7287)
)
dpsRTUv2p7287Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7287Clr.setStatus(
        "current"
    )

dpsRTUv2p7288Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7288)
)
dpsRTUv2p7288Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7288Clr.setStatus(
        "current"
    )

dpsRTUv2p7289Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7289)
)
dpsRTUv2p7289Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7289Clr.setStatus(
        "current"
    )

dpsRTUv2p7290Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7290)
)
dpsRTUv2p7290Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7290Clr.setStatus(
        "current"
    )

dpsRTUv2p7291Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7291)
)
dpsRTUv2p7291Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7291Clr.setStatus(
        "current"
    )

dpsRTUv2p7292Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7292)
)
dpsRTUv2p7292Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7292Clr.setStatus(
        "current"
    )

dpsRTUv2p7293Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7293)
)
dpsRTUv2p7293Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7293Clr.setStatus(
        "current"
    )

dpsRTUv2p7294Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7294)
)
dpsRTUv2p7294Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7294Clr.setStatus(
        "current"
    )

dpsRTUv2p7295Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7295)
)
dpsRTUv2p7295Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7295Clr.setStatus(
        "current"
    )

dpsRTUv2p7296Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7296)
)
dpsRTUv2p7296Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7296Clr.setStatus(
        "current"
    )

dpsRTUv2p7297Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7297)
)
dpsRTUv2p7297Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7297Clr.setStatus(
        "current"
    )

dpsRTUv2p7298Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7298)
)
dpsRTUv2p7298Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7298Clr.setStatus(
        "current"
    )

dpsRTUv2p7299Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7299)
)
dpsRTUv2p7299Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7299Clr.setStatus(
        "current"
    )

dpsRTUv2p7300Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7300)
)
dpsRTUv2p7300Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7300Clr.setStatus(
        "current"
    )

dpsRTUv2p7301Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7301)
)
dpsRTUv2p7301Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7301Clr.setStatus(
        "current"
    )

dpsRTUv2p7302Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7302)
)
dpsRTUv2p7302Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7302Clr.setStatus(
        "current"
    )

dpsRTUv2p7303Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7303)
)
dpsRTUv2p7303Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7303Clr.setStatus(
        "current"
    )

dpsRTUv2p7304Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7304)
)
dpsRTUv2p7304Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7304Clr.setStatus(
        "current"
    )

dpsRTUv2p7321Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7321)
)
dpsRTUv2p7321Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7321Clr.setStatus(
        "current"
    )

dpsRTUv2p7322Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7322)
)
dpsRTUv2p7322Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7322Clr.setStatus(
        "current"
    )

dpsRTUv2p7323Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7323)
)
dpsRTUv2p7323Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7323Clr.setStatus(
        "current"
    )

dpsRTUv2p7324Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7324)
)
dpsRTUv2p7324Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7324Clr.setStatus(
        "current"
    )

dpsRTUv2p7325Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7325)
)
dpsRTUv2p7325Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7325Clr.setStatus(
        "current"
    )

dpsRTUv2p7326Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7326)
)
dpsRTUv2p7326Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7326Clr.setStatus(
        "current"
    )

dpsRTUv2p7327Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7327)
)
dpsRTUv2p7327Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7327Clr.setStatus(
        "current"
    )

dpsRTUv2p7328Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7328)
)
dpsRTUv2p7328Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7328Clr.setStatus(
        "current"
    )

dpsRTUv2p7385Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7385)
)
dpsRTUv2p7385Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7385Clr.setStatus(
        "current"
    )

dpsRTUv2p7386Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7386)
)
dpsRTUv2p7386Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7386Clr.setStatus(
        "current"
    )

dpsRTUv2p7387Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7387)
)
dpsRTUv2p7387Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7387Clr.setStatus(
        "current"
    )

dpsRTUv2p7388Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7388)
)
dpsRTUv2p7388Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7388Clr.setStatus(
        "current"
    )

dpsRTUv2p7389Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7389)
)
dpsRTUv2p7389Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7389Clr.setStatus(
        "current"
    )

dpsRTUv2p7390Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7390)
)
dpsRTUv2p7390Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7390Clr.setStatus(
        "current"
    )

dpsRTUv2p7391Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7391)
)
dpsRTUv2p7391Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7391Clr.setStatus(
        "current"
    )

dpsRTUv2p7392Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7392)
)
dpsRTUv2p7392Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7392Clr.setStatus(
        "current"
    )

dpsRTUv2p7393Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7393)
)
dpsRTUv2p7393Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7393Clr.setStatus(
        "current"
    )

dpsRTUv2p7394Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7394)
)
dpsRTUv2p7394Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7394Clr.setStatus(
        "current"
    )

dpsRTUv2p7395Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7395)
)
dpsRTUv2p7395Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7395Clr.setStatus(
        "current"
    )

dpsRTUv2p7396Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7396)
)
dpsRTUv2p7396Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7396Clr.setStatus(
        "current"
    )

dpsRTUv2p7397Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7397)
)
dpsRTUv2p7397Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7397Clr.setStatus(
        "current"
    )

dpsRTUv2p7398Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7398)
)
dpsRTUv2p7398Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7398Clr.setStatus(
        "current"
    )

dpsRTUv2p7399Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7399)
)
dpsRTUv2p7399Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7399Clr.setStatus(
        "current"
    )

dpsRTUv2p7400Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7400)
)
dpsRTUv2p7400Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7400Clr.setStatus(
        "current"
    )

dpsRTUv2p7401Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7401)
)
dpsRTUv2p7401Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7401Clr.setStatus(
        "current"
    )

dpsRTUv2p7402Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7402)
)
dpsRTUv2p7402Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7402Clr.setStatus(
        "current"
    )

dpsRTUv2p7403Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7403)
)
dpsRTUv2p7403Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7403Clr.setStatus(
        "current"
    )

dpsRTUv2p7404Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7404)
)
dpsRTUv2p7404Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7404Clr.setStatus(
        "current"
    )

dpsRTUv2p7405Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7405)
)
dpsRTUv2p7405Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7405Clr.setStatus(
        "current"
    )

dpsRTUv2p7406Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7406)
)
dpsRTUv2p7406Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7406Clr.setStatus(
        "current"
    )

dpsRTUv2p7407Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7407)
)
dpsRTUv2p7407Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7407Clr.setStatus(
        "current"
    )

dpsRTUv2p7408Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7408)
)
dpsRTUv2p7408Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7408Clr.setStatus(
        "current"
    )

dpsRTUv2p7409Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7409)
)
dpsRTUv2p7409Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7409Clr.setStatus(
        "current"
    )

dpsRTUv2p7410Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7410)
)
dpsRTUv2p7410Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7410Clr.setStatus(
        "current"
    )

dpsRTUv2p7411Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7411)
)
dpsRTUv2p7411Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7411Clr.setStatus(
        "current"
    )

dpsRTUv2p7412Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7412)
)
dpsRTUv2p7412Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7412Clr.setStatus(
        "current"
    )

dpsRTUv2p7413Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7413)
)
dpsRTUv2p7413Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7413Clr.setStatus(
        "current"
    )

dpsRTUv2p7414Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7414)
)
dpsRTUv2p7414Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7414Clr.setStatus(
        "current"
    )

dpsRTUv2p7415Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7415)
)
dpsRTUv2p7415Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7415Clr.setStatus(
        "current"
    )

dpsRTUv2p7416Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7416)
)
dpsRTUv2p7416Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7416Clr.setStatus(
        "current"
    )

dpsRTUv2p7417Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7417)
)
dpsRTUv2p7417Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7417Clr.setStatus(
        "current"
    )

dpsRTUv2p7418Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7418)
)
dpsRTUv2p7418Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7418Clr.setStatus(
        "current"
    )

dpsRTUv2p7419Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7419)
)
dpsRTUv2p7419Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7419Clr.setStatus(
        "current"
    )

dpsRTUv2p7420Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7420)
)
dpsRTUv2p7420Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7420Clr.setStatus(
        "current"
    )

dpsRTUv2p7421Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7421)
)
dpsRTUv2p7421Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7421Clr.setStatus(
        "current"
    )

dpsRTUv2p7422Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7422)
)
dpsRTUv2p7422Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7422Clr.setStatus(
        "current"
    )

dpsRTUv2p7423Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7423)
)
dpsRTUv2p7423Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7423Clr.setStatus(
        "current"
    )

dpsRTUv2p7424Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7424)
)
dpsRTUv2p7424Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7424Clr.setStatus(
        "current"
    )

dpsRTUv2p7425Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7425)
)
dpsRTUv2p7425Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7425Clr.setStatus(
        "current"
    )

dpsRTUv2p7426Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7426)
)
dpsRTUv2p7426Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7426Clr.setStatus(
        "current"
    )

dpsRTUv2p7427Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7427)
)
dpsRTUv2p7427Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7427Clr.setStatus(
        "current"
    )

dpsRTUv2p7428Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7428)
)
dpsRTUv2p7428Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7428Clr.setStatus(
        "current"
    )

dpsRTUv2p7429Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7429)
)
dpsRTUv2p7429Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7429Clr.setStatus(
        "current"
    )

dpsRTUv2p7430Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7430)
)
dpsRTUv2p7430Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7430Clr.setStatus(
        "current"
    )

dpsRTUv2p7431Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7431)
)
dpsRTUv2p7431Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7431Clr.setStatus(
        "current"
    )

dpsRTUv2p7432Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7432)
)
dpsRTUv2p7432Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7432Clr.setStatus(
        "current"
    )

dpsRTUv2p7433Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7433)
)
dpsRTUv2p7433Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7433Clr.setStatus(
        "current"
    )

dpsRTUv2p7434Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7434)
)
dpsRTUv2p7434Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7434Clr.setStatus(
        "current"
    )

dpsRTUv2p7435Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7435)
)
dpsRTUv2p7435Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7435Clr.setStatus(
        "current"
    )

dpsRTUv2p7436Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7436)
)
dpsRTUv2p7436Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7436Clr.setStatus(
        "current"
    )

dpsRTUv2p7437Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7437)
)
dpsRTUv2p7437Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7437Clr.setStatus(
        "current"
    )

dpsRTUv2p7438Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7438)
)
dpsRTUv2p7438Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7438Clr.setStatus(
        "current"
    )

dpsRTUv2p7439Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7439)
)
dpsRTUv2p7439Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7439Clr.setStatus(
        "current"
    )

dpsRTUv2p7440Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7440)
)
dpsRTUv2p7440Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7440Clr.setStatus(
        "current"
    )

dpsRTUv2p7441Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7441)
)
dpsRTUv2p7441Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7441Clr.setStatus(
        "current"
    )

dpsRTUv2p7442Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7442)
)
dpsRTUv2p7442Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7442Clr.setStatus(
        "current"
    )

dpsRTUv2p7443Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7443)
)
dpsRTUv2p7443Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7443Clr.setStatus(
        "current"
    )

dpsRTUv2p7444Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7444)
)
dpsRTUv2p7444Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7444Clr.setStatus(
        "current"
    )

dpsRTUv2p7445Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7445)
)
dpsRTUv2p7445Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7445Clr.setStatus(
        "current"
    )

dpsRTUv2p7446Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7446)
)
dpsRTUv2p7446Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7446Clr.setStatus(
        "current"
    )

dpsRTUv2p7447Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7447)
)
dpsRTUv2p7447Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7447Clr.setStatus(
        "current"
    )

dpsRTUv2p7448Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7448)
)
dpsRTUv2p7448Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7448Clr.setStatus(
        "current"
    )

dpsRTUv2p7449Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7449)
)
dpsRTUv2p7449Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7449Clr.setStatus(
        "current"
    )

dpsRTUv2p7450Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7450)
)
dpsRTUv2p7450Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7450Clr.setStatus(
        "current"
    )

dpsRTUv2p7451Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7451)
)
dpsRTUv2p7451Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7451Clr.setStatus(
        "current"
    )

dpsRTUv2p7452Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7452)
)
dpsRTUv2p7452Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7452Clr.setStatus(
        "current"
    )

dpsRTUv2p7453Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7453)
)
dpsRTUv2p7453Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7453Clr.setStatus(
        "current"
    )

dpsRTUv2p7454Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7454)
)
dpsRTUv2p7454Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7454Clr.setStatus(
        "current"
    )

dpsRTUv2p7455Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7455)
)
dpsRTUv2p7455Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7455Clr.setStatus(
        "current"
    )

dpsRTUv2p7456Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7456)
)
dpsRTUv2p7456Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7456Clr.setStatus(
        "current"
    )

dpsRTUv2p7457Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7457)
)
dpsRTUv2p7457Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7457Clr.setStatus(
        "current"
    )

dpsRTUv2p7458Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7458)
)
dpsRTUv2p7458Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7458Clr.setStatus(
        "current"
    )

dpsRTUv2p7459Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7459)
)
dpsRTUv2p7459Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7459Clr.setStatus(
        "current"
    )

dpsRTUv2p7460Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7460)
)
dpsRTUv2p7460Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7460Clr.setStatus(
        "current"
    )

dpsRTUv2p7461Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7461)
)
dpsRTUv2p7461Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7461Clr.setStatus(
        "current"
    )

dpsRTUv2p7462Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7462)
)
dpsRTUv2p7462Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7462Clr.setStatus(
        "current"
    )

dpsRTUv2p7463Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7463)
)
dpsRTUv2p7463Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7463Clr.setStatus(
        "current"
    )

dpsRTUv2p7464Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7464)
)
dpsRTUv2p7464Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7464Clr.setStatus(
        "current"
    )

dpsRTUv2p7465Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7465)
)
dpsRTUv2p7465Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7465Clr.setStatus(
        "current"
    )

dpsRTUv2p7466Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7466)
)
dpsRTUv2p7466Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7466Clr.setStatus(
        "current"
    )

dpsRTUv2p7467Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7467)
)
dpsRTUv2p7467Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7467Clr.setStatus(
        "current"
    )

dpsRTUv2p7468Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7468)
)
dpsRTUv2p7468Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7468Clr.setStatus(
        "current"
    )

dpsRTUv2p7469Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7469)
)
dpsRTUv2p7469Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7469Clr.setStatus(
        "current"
    )

dpsRTUv2p7470Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7470)
)
dpsRTUv2p7470Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7470Clr.setStatus(
        "current"
    )

dpsRTUv2p7471Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7471)
)
dpsRTUv2p7471Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7471Clr.setStatus(
        "current"
    )

dpsRTUv2p7472Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7472)
)
dpsRTUv2p7472Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7472Clr.setStatus(
        "current"
    )

dpsRTUv2p7473Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7473)
)
dpsRTUv2p7473Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7473Clr.setStatus(
        "current"
    )

dpsRTUv2p7474Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7474)
)
dpsRTUv2p7474Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7474Clr.setStatus(
        "current"
    )

dpsRTUv2p7475Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7475)
)
dpsRTUv2p7475Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7475Clr.setStatus(
        "current"
    )

dpsRTUv2p7476Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7476)
)
dpsRTUv2p7476Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7476Clr.setStatus(
        "current"
    )

dpsRTUv2p7477Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7477)
)
dpsRTUv2p7477Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7477Clr.setStatus(
        "current"
    )

dpsRTUv2p7478Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7478)
)
dpsRTUv2p7478Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7478Clr.setStatus(
        "current"
    )

dpsRTUv2p7479Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7479)
)
dpsRTUv2p7479Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7479Clr.setStatus(
        "current"
    )

dpsRTUv2p7480Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 7480)
)
dpsRTUv2p7480Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p7480Clr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-MIB-NGX-G39-V2",
    **{"dpsRTUv2p6001Set": dpsRTUv2p6001Set,
       "dpsRTUv2p6002Set": dpsRTUv2p6002Set,
       "dpsRTUv2p6003Set": dpsRTUv2p6003Set,
       "dpsRTUv2p6004Set": dpsRTUv2p6004Set,
       "dpsRTUv2p6005Set": dpsRTUv2p6005Set,
       "dpsRTUv2p6006Set": dpsRTUv2p6006Set,
       "dpsRTUv2p6007Set": dpsRTUv2p6007Set,
       "dpsRTUv2p6008Set": dpsRTUv2p6008Set,
       "dpsRTUv2p6009Set": dpsRTUv2p6009Set,
       "dpsRTUv2p6010Set": dpsRTUv2p6010Set,
       "dpsRTUv2p6011Set": dpsRTUv2p6011Set,
       "dpsRTUv2p6012Set": dpsRTUv2p6012Set,
       "dpsRTUv2p6013Set": dpsRTUv2p6013Set,
       "dpsRTUv2p6014Set": dpsRTUv2p6014Set,
       "dpsRTUv2p6015Set": dpsRTUv2p6015Set,
       "dpsRTUv2p6016Set": dpsRTUv2p6016Set,
       "dpsRTUv2p6017Set": dpsRTUv2p6017Set,
       "dpsRTUv2p6018Set": dpsRTUv2p6018Set,
       "dpsRTUv2p6019Set": dpsRTUv2p6019Set,
       "dpsRTUv2p6020Set": dpsRTUv2p6020Set,
       "dpsRTUv2p6021Set": dpsRTUv2p6021Set,
       "dpsRTUv2p6022Set": dpsRTUv2p6022Set,
       "dpsRTUv2p6023Set": dpsRTUv2p6023Set,
       "dpsRTUv2p6024Set": dpsRTUv2p6024Set,
       "dpsRTUv2p6025Set": dpsRTUv2p6025Set,
       "dpsRTUv2p6026Set": dpsRTUv2p6026Set,
       "dpsRTUv2p6027Set": dpsRTUv2p6027Set,
       "dpsRTUv2p6028Set": dpsRTUv2p6028Set,
       "dpsRTUv2p6029Set": dpsRTUv2p6029Set,
       "dpsRTUv2p6030Set": dpsRTUv2p6030Set,
       "dpsRTUv2p6031Set": dpsRTUv2p6031Set,
       "dpsRTUv2p6032Set": dpsRTUv2p6032Set,
       "dpsRTUv2p6033Set": dpsRTUv2p6033Set,
       "dpsRTUv2p6034Set": dpsRTUv2p6034Set,
       "dpsRTUv2p6035Set": dpsRTUv2p6035Set,
       "dpsRTUv2p6036Set": dpsRTUv2p6036Set,
       "dpsRTUv2p6037Set": dpsRTUv2p6037Set,
       "dpsRTUv2p6038Set": dpsRTUv2p6038Set,
       "dpsRTUv2p6039Set": dpsRTUv2p6039Set,
       "dpsRTUv2p6040Set": dpsRTUv2p6040Set,
       "dpsRTUv2p6041Set": dpsRTUv2p6041Set,
       "dpsRTUv2p6042Set": dpsRTUv2p6042Set,
       "dpsRTUv2p6043Set": dpsRTUv2p6043Set,
       "dpsRTUv2p6044Set": dpsRTUv2p6044Set,
       "dpsRTUv2p6045Set": dpsRTUv2p6045Set,
       "dpsRTUv2p6046Set": dpsRTUv2p6046Set,
       "dpsRTUv2p6047Set": dpsRTUv2p6047Set,
       "dpsRTUv2p6048Set": dpsRTUv2p6048Set,
       "dpsRTUv2p6049Set": dpsRTUv2p6049Set,
       "dpsRTUv2p6050Set": dpsRTUv2p6050Set,
       "dpsRTUv2p6051Set": dpsRTUv2p6051Set,
       "dpsRTUv2p6052Set": dpsRTUv2p6052Set,
       "dpsRTUv2p6053Set": dpsRTUv2p6053Set,
       "dpsRTUv2p6054Set": dpsRTUv2p6054Set,
       "dpsRTUv2p6055Set": dpsRTUv2p6055Set,
       "dpsRTUv2p6056Set": dpsRTUv2p6056Set,
       "dpsRTUv2p6057Set": dpsRTUv2p6057Set,
       "dpsRTUv2p6058Set": dpsRTUv2p6058Set,
       "dpsRTUv2p6059Set": dpsRTUv2p6059Set,
       "dpsRTUv2p6060Set": dpsRTUv2p6060Set,
       "dpsRTUv2p6061Set": dpsRTUv2p6061Set,
       "dpsRTUv2p6062Set": dpsRTUv2p6062Set,
       "dpsRTUv2p6063Set": dpsRTUv2p6063Set,
       "dpsRTUv2p6064Set": dpsRTUv2p6064Set,
       "dpsRTUv2p6065Set": dpsRTUv2p6065Set,
       "dpsRTUv2p6066Set": dpsRTUv2p6066Set,
       "dpsRTUv2p6067Set": dpsRTUv2p6067Set,
       "dpsRTUv2p6068Set": dpsRTUv2p6068Set,
       "dpsRTUv2p6069Set": dpsRTUv2p6069Set,
       "dpsRTUv2p6070Set": dpsRTUv2p6070Set,
       "dpsRTUv2p6071Set": dpsRTUv2p6071Set,
       "dpsRTUv2p6072Set": dpsRTUv2p6072Set,
       "dpsRTUv2p6081Set": dpsRTUv2p6081Set,
       "dpsRTUv2p6082Set": dpsRTUv2p6082Set,
       "dpsRTUv2p6083Set": dpsRTUv2p6083Set,
       "dpsRTUv2p6084Set": dpsRTUv2p6084Set,
       "dpsRTUv2p6085Set": dpsRTUv2p6085Set,
       "dpsRTUv2p6086Set": dpsRTUv2p6086Set,
       "dpsRTUv2p6087Set": dpsRTUv2p6087Set,
       "dpsRTUv2p6088Set": dpsRTUv2p6088Set,
       "dpsRTUv2p6089Set": dpsRTUv2p6089Set,
       "dpsRTUv2p6090Set": dpsRTUv2p6090Set,
       "dpsRTUv2p6091Set": dpsRTUv2p6091Set,
       "dpsRTUv2p6092Set": dpsRTUv2p6092Set,
       "dpsRTUv2p6093Set": dpsRTUv2p6093Set,
       "dpsRTUv2p6094Set": dpsRTUv2p6094Set,
       "dpsRTUv2p6095Set": dpsRTUv2p6095Set,
       "dpsRTUv2p6096Set": dpsRTUv2p6096Set,
       "dpsRTUv2p6129Set": dpsRTUv2p6129Set,
       "dpsRTUv2p6130Set": dpsRTUv2p6130Set,
       "dpsRTUv2p6131Set": dpsRTUv2p6131Set,
       "dpsRTUv2p6132Set": dpsRTUv2p6132Set,
       "dpsRTUv2p6133Set": dpsRTUv2p6133Set,
       "dpsRTUv2p6134Set": dpsRTUv2p6134Set,
       "dpsRTUv2p6135Set": dpsRTUv2p6135Set,
       "dpsRTUv2p6136Set": dpsRTUv2p6136Set,
       "dpsRTUv2p6137Set": dpsRTUv2p6137Set,
       "dpsRTUv2p6138Set": dpsRTUv2p6138Set,
       "dpsRTUv2p6139Set": dpsRTUv2p6139Set,
       "dpsRTUv2p6140Set": dpsRTUv2p6140Set,
       "dpsRTUv2p6141Set": dpsRTUv2p6141Set,
       "dpsRTUv2p6142Set": dpsRTUv2p6142Set,
       "dpsRTUv2p6143Set": dpsRTUv2p6143Set,
       "dpsRTUv2p6144Set": dpsRTUv2p6144Set,
       "dpsRTUv2p6145Set": dpsRTUv2p6145Set,
       "dpsRTUv2p6146Set": dpsRTUv2p6146Set,
       "dpsRTUv2p6147Set": dpsRTUv2p6147Set,
       "dpsRTUv2p6148Set": dpsRTUv2p6148Set,
       "dpsRTUv2p6149Set": dpsRTUv2p6149Set,
       "dpsRTUv2p6150Set": dpsRTUv2p6150Set,
       "dpsRTUv2p6151Set": dpsRTUv2p6151Set,
       "dpsRTUv2p6152Set": dpsRTUv2p6152Set,
       "dpsRTUv2p6153Set": dpsRTUv2p6153Set,
       "dpsRTUv2p6154Set": dpsRTUv2p6154Set,
       "dpsRTUv2p6155Set": dpsRTUv2p6155Set,
       "dpsRTUv2p6156Set": dpsRTUv2p6156Set,
       "dpsRTUv2p6157Set": dpsRTUv2p6157Set,
       "dpsRTUv2p6158Set": dpsRTUv2p6158Set,
       "dpsRTUv2p6159Set": dpsRTUv2p6159Set,
       "dpsRTUv2p6160Set": dpsRTUv2p6160Set,
       "dpsRTUv2p6161Set": dpsRTUv2p6161Set,
       "dpsRTUv2p6162Set": dpsRTUv2p6162Set,
       "dpsRTUv2p6163Set": dpsRTUv2p6163Set,
       "dpsRTUv2p6164Set": dpsRTUv2p6164Set,
       "dpsRTUv2p6165Set": dpsRTUv2p6165Set,
       "dpsRTUv2p6166Set": dpsRTUv2p6166Set,
       "dpsRTUv2p6167Set": dpsRTUv2p6167Set,
       "dpsRTUv2p6168Set": dpsRTUv2p6168Set,
       "dpsRTUv2p6169Set": dpsRTUv2p6169Set,
       "dpsRTUv2p6170Set": dpsRTUv2p6170Set,
       "dpsRTUv2p6171Set": dpsRTUv2p6171Set,
       "dpsRTUv2p6172Set": dpsRTUv2p6172Set,
       "dpsRTUv2p6173Set": dpsRTUv2p6173Set,
       "dpsRTUv2p6174Set": dpsRTUv2p6174Set,
       "dpsRTUv2p6175Set": dpsRTUv2p6175Set,
       "dpsRTUv2p6176Set": dpsRTUv2p6176Set,
       "dpsRTUv2p6193Set": dpsRTUv2p6193Set,
       "dpsRTUv2p6194Set": dpsRTUv2p6194Set,
       "dpsRTUv2p6195Set": dpsRTUv2p6195Set,
       "dpsRTUv2p6196Set": dpsRTUv2p6196Set,
       "dpsRTUv2p6197Set": dpsRTUv2p6197Set,
       "dpsRTUv2p6198Set": dpsRTUv2p6198Set,
       "dpsRTUv2p6199Set": dpsRTUv2p6199Set,
       "dpsRTUv2p6200Set": dpsRTUv2p6200Set,
       "dpsRTUv2p6257Set": dpsRTUv2p6257Set,
       "dpsRTUv2p6258Set": dpsRTUv2p6258Set,
       "dpsRTUv2p6259Set": dpsRTUv2p6259Set,
       "dpsRTUv2p6260Set": dpsRTUv2p6260Set,
       "dpsRTUv2p6261Set": dpsRTUv2p6261Set,
       "dpsRTUv2p6262Set": dpsRTUv2p6262Set,
       "dpsRTUv2p6263Set": dpsRTUv2p6263Set,
       "dpsRTUv2p6264Set": dpsRTUv2p6264Set,
       "dpsRTUv2p6265Set": dpsRTUv2p6265Set,
       "dpsRTUv2p6266Set": dpsRTUv2p6266Set,
       "dpsRTUv2p6267Set": dpsRTUv2p6267Set,
       "dpsRTUv2p6268Set": dpsRTUv2p6268Set,
       "dpsRTUv2p6269Set": dpsRTUv2p6269Set,
       "dpsRTUv2p6270Set": dpsRTUv2p6270Set,
       "dpsRTUv2p6271Set": dpsRTUv2p6271Set,
       "dpsRTUv2p6272Set": dpsRTUv2p6272Set,
       "dpsRTUv2p6273Set": dpsRTUv2p6273Set,
       "dpsRTUv2p6274Set": dpsRTUv2p6274Set,
       "dpsRTUv2p6275Set": dpsRTUv2p6275Set,
       "dpsRTUv2p6276Set": dpsRTUv2p6276Set,
       "dpsRTUv2p6277Set": dpsRTUv2p6277Set,
       "dpsRTUv2p6278Set": dpsRTUv2p6278Set,
       "dpsRTUv2p6279Set": dpsRTUv2p6279Set,
       "dpsRTUv2p6280Set": dpsRTUv2p6280Set,
       "dpsRTUv2p6281Set": dpsRTUv2p6281Set,
       "dpsRTUv2p6282Set": dpsRTUv2p6282Set,
       "dpsRTUv2p6283Set": dpsRTUv2p6283Set,
       "dpsRTUv2p6284Set": dpsRTUv2p6284Set,
       "dpsRTUv2p6285Set": dpsRTUv2p6285Set,
       "dpsRTUv2p6286Set": dpsRTUv2p6286Set,
       "dpsRTUv2p6287Set": dpsRTUv2p6287Set,
       "dpsRTUv2p6288Set": dpsRTUv2p6288Set,
       "dpsRTUv2p6289Set": dpsRTUv2p6289Set,
       "dpsRTUv2p6290Set": dpsRTUv2p6290Set,
       "dpsRTUv2p6291Set": dpsRTUv2p6291Set,
       "dpsRTUv2p6292Set": dpsRTUv2p6292Set,
       "dpsRTUv2p6293Set": dpsRTUv2p6293Set,
       "dpsRTUv2p6294Set": dpsRTUv2p6294Set,
       "dpsRTUv2p6295Set": dpsRTUv2p6295Set,
       "dpsRTUv2p6296Set": dpsRTUv2p6296Set,
       "dpsRTUv2p6297Set": dpsRTUv2p6297Set,
       "dpsRTUv2p6298Set": dpsRTUv2p6298Set,
       "dpsRTUv2p6299Set": dpsRTUv2p6299Set,
       "dpsRTUv2p6300Set": dpsRTUv2p6300Set,
       "dpsRTUv2p6301Set": dpsRTUv2p6301Set,
       "dpsRTUv2p6302Set": dpsRTUv2p6302Set,
       "dpsRTUv2p6303Set": dpsRTUv2p6303Set,
       "dpsRTUv2p6304Set": dpsRTUv2p6304Set,
       "dpsRTUv2p6321Set": dpsRTUv2p6321Set,
       "dpsRTUv2p6322Set": dpsRTUv2p6322Set,
       "dpsRTUv2p6323Set": dpsRTUv2p6323Set,
       "dpsRTUv2p6324Set": dpsRTUv2p6324Set,
       "dpsRTUv2p6325Set": dpsRTUv2p6325Set,
       "dpsRTUv2p6326Set": dpsRTUv2p6326Set,
       "dpsRTUv2p6327Set": dpsRTUv2p6327Set,
       "dpsRTUv2p6328Set": dpsRTUv2p6328Set,
       "dpsRTUv2p6385Set": dpsRTUv2p6385Set,
       "dpsRTUv2p6386Set": dpsRTUv2p6386Set,
       "dpsRTUv2p6387Set": dpsRTUv2p6387Set,
       "dpsRTUv2p6388Set": dpsRTUv2p6388Set,
       "dpsRTUv2p6389Set": dpsRTUv2p6389Set,
       "dpsRTUv2p6390Set": dpsRTUv2p6390Set,
       "dpsRTUv2p6391Set": dpsRTUv2p6391Set,
       "dpsRTUv2p6392Set": dpsRTUv2p6392Set,
       "dpsRTUv2p6393Set": dpsRTUv2p6393Set,
       "dpsRTUv2p6394Set": dpsRTUv2p6394Set,
       "dpsRTUv2p6395Set": dpsRTUv2p6395Set,
       "dpsRTUv2p6396Set": dpsRTUv2p6396Set,
       "dpsRTUv2p6397Set": dpsRTUv2p6397Set,
       "dpsRTUv2p6398Set": dpsRTUv2p6398Set,
       "dpsRTUv2p6399Set": dpsRTUv2p6399Set,
       "dpsRTUv2p6400Set": dpsRTUv2p6400Set,
       "dpsRTUv2p6401Set": dpsRTUv2p6401Set,
       "dpsRTUv2p6402Set": dpsRTUv2p6402Set,
       "dpsRTUv2p6403Set": dpsRTUv2p6403Set,
       "dpsRTUv2p6404Set": dpsRTUv2p6404Set,
       "dpsRTUv2p6405Set": dpsRTUv2p6405Set,
       "dpsRTUv2p6406Set": dpsRTUv2p6406Set,
       "dpsRTUv2p6407Set": dpsRTUv2p6407Set,
       "dpsRTUv2p6408Set": dpsRTUv2p6408Set,
       "dpsRTUv2p6409Set": dpsRTUv2p6409Set,
       "dpsRTUv2p6410Set": dpsRTUv2p6410Set,
       "dpsRTUv2p6411Set": dpsRTUv2p6411Set,
       "dpsRTUv2p6412Set": dpsRTUv2p6412Set,
       "dpsRTUv2p6413Set": dpsRTUv2p6413Set,
       "dpsRTUv2p6414Set": dpsRTUv2p6414Set,
       "dpsRTUv2p6415Set": dpsRTUv2p6415Set,
       "dpsRTUv2p6416Set": dpsRTUv2p6416Set,
       "dpsRTUv2p6417Set": dpsRTUv2p6417Set,
       "dpsRTUv2p6418Set": dpsRTUv2p6418Set,
       "dpsRTUv2p6419Set": dpsRTUv2p6419Set,
       "dpsRTUv2p6420Set": dpsRTUv2p6420Set,
       "dpsRTUv2p6421Set": dpsRTUv2p6421Set,
       "dpsRTUv2p6422Set": dpsRTUv2p6422Set,
       "dpsRTUv2p6423Set": dpsRTUv2p6423Set,
       "dpsRTUv2p6424Set": dpsRTUv2p6424Set,
       "dpsRTUv2p6425Set": dpsRTUv2p6425Set,
       "dpsRTUv2p6426Set": dpsRTUv2p6426Set,
       "dpsRTUv2p6427Set": dpsRTUv2p6427Set,
       "dpsRTUv2p6428Set": dpsRTUv2p6428Set,
       "dpsRTUv2p6429Set": dpsRTUv2p6429Set,
       "dpsRTUv2p6430Set": dpsRTUv2p6430Set,
       "dpsRTUv2p6431Set": dpsRTUv2p6431Set,
       "dpsRTUv2p6432Set": dpsRTUv2p6432Set,
       "dpsRTUv2p6433Set": dpsRTUv2p6433Set,
       "dpsRTUv2p6434Set": dpsRTUv2p6434Set,
       "dpsRTUv2p6435Set": dpsRTUv2p6435Set,
       "dpsRTUv2p6436Set": dpsRTUv2p6436Set,
       "dpsRTUv2p6437Set": dpsRTUv2p6437Set,
       "dpsRTUv2p6438Set": dpsRTUv2p6438Set,
       "dpsRTUv2p6439Set": dpsRTUv2p6439Set,
       "dpsRTUv2p6440Set": dpsRTUv2p6440Set,
       "dpsRTUv2p6441Set": dpsRTUv2p6441Set,
       "dpsRTUv2p6442Set": dpsRTUv2p6442Set,
       "dpsRTUv2p6443Set": dpsRTUv2p6443Set,
       "dpsRTUv2p6444Set": dpsRTUv2p6444Set,
       "dpsRTUv2p6445Set": dpsRTUv2p6445Set,
       "dpsRTUv2p6446Set": dpsRTUv2p6446Set,
       "dpsRTUv2p6447Set": dpsRTUv2p6447Set,
       "dpsRTUv2p6448Set": dpsRTUv2p6448Set,
       "dpsRTUv2p6449Set": dpsRTUv2p6449Set,
       "dpsRTUv2p6450Set": dpsRTUv2p6450Set,
       "dpsRTUv2p6451Set": dpsRTUv2p6451Set,
       "dpsRTUv2p6452Set": dpsRTUv2p6452Set,
       "dpsRTUv2p6453Set": dpsRTUv2p6453Set,
       "dpsRTUv2p6454Set": dpsRTUv2p6454Set,
       "dpsRTUv2p6455Set": dpsRTUv2p6455Set,
       "dpsRTUv2p6456Set": dpsRTUv2p6456Set,
       "dpsRTUv2p6457Set": dpsRTUv2p6457Set,
       "dpsRTUv2p6458Set": dpsRTUv2p6458Set,
       "dpsRTUv2p6459Set": dpsRTUv2p6459Set,
       "dpsRTUv2p6460Set": dpsRTUv2p6460Set,
       "dpsRTUv2p6461Set": dpsRTUv2p6461Set,
       "dpsRTUv2p6462Set": dpsRTUv2p6462Set,
       "dpsRTUv2p6463Set": dpsRTUv2p6463Set,
       "dpsRTUv2p6464Set": dpsRTUv2p6464Set,
       "dpsRTUv2p6465Set": dpsRTUv2p6465Set,
       "dpsRTUv2p6466Set": dpsRTUv2p6466Set,
       "dpsRTUv2p6467Set": dpsRTUv2p6467Set,
       "dpsRTUv2p6468Set": dpsRTUv2p6468Set,
       "dpsRTUv2p6469Set": dpsRTUv2p6469Set,
       "dpsRTUv2p6470Set": dpsRTUv2p6470Set,
       "dpsRTUv2p6471Set": dpsRTUv2p6471Set,
       "dpsRTUv2p6472Set": dpsRTUv2p6472Set,
       "dpsRTUv2p6473Set": dpsRTUv2p6473Set,
       "dpsRTUv2p6474Set": dpsRTUv2p6474Set,
       "dpsRTUv2p6475Set": dpsRTUv2p6475Set,
       "dpsRTUv2p6476Set": dpsRTUv2p6476Set,
       "dpsRTUv2p6477Set": dpsRTUv2p6477Set,
       "dpsRTUv2p6478Set": dpsRTUv2p6478Set,
       "dpsRTUv2p6479Set": dpsRTUv2p6479Set,
       "dpsRTUv2p6480Set": dpsRTUv2p6480Set,
       "dpsRTUv2p7001Clr": dpsRTUv2p7001Clr,
       "dpsRTUv2p7002Clr": dpsRTUv2p7002Clr,
       "dpsRTUv2p7003Clr": dpsRTUv2p7003Clr,
       "dpsRTUv2p7004Clr": dpsRTUv2p7004Clr,
       "dpsRTUv2p7005Clr": dpsRTUv2p7005Clr,
       "dpsRTUv2p7006Clr": dpsRTUv2p7006Clr,
       "dpsRTUv2p7007Clr": dpsRTUv2p7007Clr,
       "dpsRTUv2p7008Clr": dpsRTUv2p7008Clr,
       "dpsRTUv2p7009Clr": dpsRTUv2p7009Clr,
       "dpsRTUv2p7010Clr": dpsRTUv2p7010Clr,
       "dpsRTUv2p7011Clr": dpsRTUv2p7011Clr,
       "dpsRTUv2p7012Clr": dpsRTUv2p7012Clr,
       "dpsRTUv2p7013Clr": dpsRTUv2p7013Clr,
       "dpsRTUv2p7014Clr": dpsRTUv2p7014Clr,
       "dpsRTUv2p7015Clr": dpsRTUv2p7015Clr,
       "dpsRTUv2p7016Clr": dpsRTUv2p7016Clr,
       "dpsRTUv2p7017Clr": dpsRTUv2p7017Clr,
       "dpsRTUv2p7018Clr": dpsRTUv2p7018Clr,
       "dpsRTUv2p7019Clr": dpsRTUv2p7019Clr,
       "dpsRTUv2p7020Clr": dpsRTUv2p7020Clr,
       "dpsRTUv2p7021Clr": dpsRTUv2p7021Clr,
       "dpsRTUv2p7022Clr": dpsRTUv2p7022Clr,
       "dpsRTUv2p7023Clr": dpsRTUv2p7023Clr,
       "dpsRTUv2p7024Clr": dpsRTUv2p7024Clr,
       "dpsRTUv2p7025Clr": dpsRTUv2p7025Clr,
       "dpsRTUv2p7026Clr": dpsRTUv2p7026Clr,
       "dpsRTUv2p7027Clr": dpsRTUv2p7027Clr,
       "dpsRTUv2p7028Clr": dpsRTUv2p7028Clr,
       "dpsRTUv2p7029Clr": dpsRTUv2p7029Clr,
       "dpsRTUv2p7030Clr": dpsRTUv2p7030Clr,
       "dpsRTUv2p7031Clr": dpsRTUv2p7031Clr,
       "dpsRTUv2p7032Clr": dpsRTUv2p7032Clr,
       "dpsRTUv2p7033Clr": dpsRTUv2p7033Clr,
       "dpsRTUv2p7034Clr": dpsRTUv2p7034Clr,
       "dpsRTUv2p7035Clr": dpsRTUv2p7035Clr,
       "dpsRTUv2p7036Clr": dpsRTUv2p7036Clr,
       "dpsRTUv2p7037Clr": dpsRTUv2p7037Clr,
       "dpsRTUv2p7038Clr": dpsRTUv2p7038Clr,
       "dpsRTUv2p7039Clr": dpsRTUv2p7039Clr,
       "dpsRTUv2p7040Clr": dpsRTUv2p7040Clr,
       "dpsRTUv2p7041Clr": dpsRTUv2p7041Clr,
       "dpsRTUv2p7042Clr": dpsRTUv2p7042Clr,
       "dpsRTUv2p7043Clr": dpsRTUv2p7043Clr,
       "dpsRTUv2p7044Clr": dpsRTUv2p7044Clr,
       "dpsRTUv2p7045Clr": dpsRTUv2p7045Clr,
       "dpsRTUv2p7046Clr": dpsRTUv2p7046Clr,
       "dpsRTUv2p7047Clr": dpsRTUv2p7047Clr,
       "dpsRTUv2p7048Clr": dpsRTUv2p7048Clr,
       "dpsRTUv2p7049Clr": dpsRTUv2p7049Clr,
       "dpsRTUv2p7050Clr": dpsRTUv2p7050Clr,
       "dpsRTUv2p7051Clr": dpsRTUv2p7051Clr,
       "dpsRTUv2p7052Clr": dpsRTUv2p7052Clr,
       "dpsRTUv2p7053Clr": dpsRTUv2p7053Clr,
       "dpsRTUv2p7054Clr": dpsRTUv2p7054Clr,
       "dpsRTUv2p7055Clr": dpsRTUv2p7055Clr,
       "dpsRTUv2p7056Clr": dpsRTUv2p7056Clr,
       "dpsRTUv2p7057Clr": dpsRTUv2p7057Clr,
       "dpsRTUv2p7058Clr": dpsRTUv2p7058Clr,
       "dpsRTUv2p7059Clr": dpsRTUv2p7059Clr,
       "dpsRTUv2p7060Clr": dpsRTUv2p7060Clr,
       "dpsRTUv2p7061Clr": dpsRTUv2p7061Clr,
       "dpsRTUv2p7062Clr": dpsRTUv2p7062Clr,
       "dpsRTUv2p7063Clr": dpsRTUv2p7063Clr,
       "dpsRTUv2p7064Clr": dpsRTUv2p7064Clr,
       "dpsRTUv2p7065Clr": dpsRTUv2p7065Clr,
       "dpsRTUv2p7066Clr": dpsRTUv2p7066Clr,
       "dpsRTUv2p7067Clr": dpsRTUv2p7067Clr,
       "dpsRTUv2p7068Clr": dpsRTUv2p7068Clr,
       "dpsRTUv2p7069Clr": dpsRTUv2p7069Clr,
       "dpsRTUv2p7070Clr": dpsRTUv2p7070Clr,
       "dpsRTUv2p7071Clr": dpsRTUv2p7071Clr,
       "dpsRTUv2p7072Clr": dpsRTUv2p7072Clr,
       "dpsRTUv2p7081Clr": dpsRTUv2p7081Clr,
       "dpsRTUv2p7082Clr": dpsRTUv2p7082Clr,
       "dpsRTUv2p7083Clr": dpsRTUv2p7083Clr,
       "dpsRTUv2p7084Clr": dpsRTUv2p7084Clr,
       "dpsRTUv2p7085Clr": dpsRTUv2p7085Clr,
       "dpsRTUv2p7086Clr": dpsRTUv2p7086Clr,
       "dpsRTUv2p7087Clr": dpsRTUv2p7087Clr,
       "dpsRTUv2p7088Clr": dpsRTUv2p7088Clr,
       "dpsRTUv2p7089Clr": dpsRTUv2p7089Clr,
       "dpsRTUv2p7090Clr": dpsRTUv2p7090Clr,
       "dpsRTUv2p7091Clr": dpsRTUv2p7091Clr,
       "dpsRTUv2p7092Clr": dpsRTUv2p7092Clr,
       "dpsRTUv2p7093Clr": dpsRTUv2p7093Clr,
       "dpsRTUv2p7094Clr": dpsRTUv2p7094Clr,
       "dpsRTUv2p7095Clr": dpsRTUv2p7095Clr,
       "dpsRTUv2p7096Clr": dpsRTUv2p7096Clr,
       "dpsRTUv2p7129Clr": dpsRTUv2p7129Clr,
       "dpsRTUv2p7130Clr": dpsRTUv2p7130Clr,
       "dpsRTUv2p7131Clr": dpsRTUv2p7131Clr,
       "dpsRTUv2p7132Clr": dpsRTUv2p7132Clr,
       "dpsRTUv2p7133Clr": dpsRTUv2p7133Clr,
       "dpsRTUv2p7134Clr": dpsRTUv2p7134Clr,
       "dpsRTUv2p7135Clr": dpsRTUv2p7135Clr,
       "dpsRTUv2p7136Clr": dpsRTUv2p7136Clr,
       "dpsRTUv2p7137Clr": dpsRTUv2p7137Clr,
       "dpsRTUv2p7138Clr": dpsRTUv2p7138Clr,
       "dpsRTUv2p7139Clr": dpsRTUv2p7139Clr,
       "dpsRTUv2p7140Clr": dpsRTUv2p7140Clr,
       "dpsRTUv2p7141Clr": dpsRTUv2p7141Clr,
       "dpsRTUv2p7142Clr": dpsRTUv2p7142Clr,
       "dpsRTUv2p7143Clr": dpsRTUv2p7143Clr,
       "dpsRTUv2p7144Clr": dpsRTUv2p7144Clr,
       "dpsRTUv2p7145Clr": dpsRTUv2p7145Clr,
       "dpsRTUv2p7146Clr": dpsRTUv2p7146Clr,
       "dpsRTUv2p7147Clr": dpsRTUv2p7147Clr,
       "dpsRTUv2p7148Clr": dpsRTUv2p7148Clr,
       "dpsRTUv2p7149Clr": dpsRTUv2p7149Clr,
       "dpsRTUv2p7150Clr": dpsRTUv2p7150Clr,
       "dpsRTUv2p7151Clr": dpsRTUv2p7151Clr,
       "dpsRTUv2p7152Clr": dpsRTUv2p7152Clr,
       "dpsRTUv2p7153Clr": dpsRTUv2p7153Clr,
       "dpsRTUv2p7154Clr": dpsRTUv2p7154Clr,
       "dpsRTUv2p7155Clr": dpsRTUv2p7155Clr,
       "dpsRTUv2p7156Clr": dpsRTUv2p7156Clr,
       "dpsRTUv2p7157Clr": dpsRTUv2p7157Clr,
       "dpsRTUv2p7158Clr": dpsRTUv2p7158Clr,
       "dpsRTUv2p7159Clr": dpsRTUv2p7159Clr,
       "dpsRTUv2p7160Clr": dpsRTUv2p7160Clr,
       "dpsRTUv2p7161Clr": dpsRTUv2p7161Clr,
       "dpsRTUv2p7162Clr": dpsRTUv2p7162Clr,
       "dpsRTUv2p7163Clr": dpsRTUv2p7163Clr,
       "dpsRTUv2p7164Clr": dpsRTUv2p7164Clr,
       "dpsRTUv2p7165Clr": dpsRTUv2p7165Clr,
       "dpsRTUv2p7166Clr": dpsRTUv2p7166Clr,
       "dpsRTUv2p7167Clr": dpsRTUv2p7167Clr,
       "dpsRTUv2p7168Clr": dpsRTUv2p7168Clr,
       "dpsRTUv2p7169Clr": dpsRTUv2p7169Clr,
       "dpsRTUv2p7170Clr": dpsRTUv2p7170Clr,
       "dpsRTUv2p7171Clr": dpsRTUv2p7171Clr,
       "dpsRTUv2p7172Clr": dpsRTUv2p7172Clr,
       "dpsRTUv2p7173Clr": dpsRTUv2p7173Clr,
       "dpsRTUv2p7174Clr": dpsRTUv2p7174Clr,
       "dpsRTUv2p7175Clr": dpsRTUv2p7175Clr,
       "dpsRTUv2p7176Clr": dpsRTUv2p7176Clr,
       "dpsRTUv2p7193Clr": dpsRTUv2p7193Clr,
       "dpsRTUv2p7194Clr": dpsRTUv2p7194Clr,
       "dpsRTUv2p7195Clr": dpsRTUv2p7195Clr,
       "dpsRTUv2p7196Clr": dpsRTUv2p7196Clr,
       "dpsRTUv2p7197Clr": dpsRTUv2p7197Clr,
       "dpsRTUv2p7198Clr": dpsRTUv2p7198Clr,
       "dpsRTUv2p7199Clr": dpsRTUv2p7199Clr,
       "dpsRTUv2p7200Clr": dpsRTUv2p7200Clr,
       "dpsRTUv2p7257Clr": dpsRTUv2p7257Clr,
       "dpsRTUv2p7258Clr": dpsRTUv2p7258Clr,
       "dpsRTUv2p7259Clr": dpsRTUv2p7259Clr,
       "dpsRTUv2p7260Clr": dpsRTUv2p7260Clr,
       "dpsRTUv2p7261Clr": dpsRTUv2p7261Clr,
       "dpsRTUv2p7262Clr": dpsRTUv2p7262Clr,
       "dpsRTUv2p7263Clr": dpsRTUv2p7263Clr,
       "dpsRTUv2p7264Clr": dpsRTUv2p7264Clr,
       "dpsRTUv2p7265Clr": dpsRTUv2p7265Clr,
       "dpsRTUv2p7266Clr": dpsRTUv2p7266Clr,
       "dpsRTUv2p7267Clr": dpsRTUv2p7267Clr,
       "dpsRTUv2p7268Clr": dpsRTUv2p7268Clr,
       "dpsRTUv2p7269Clr": dpsRTUv2p7269Clr,
       "dpsRTUv2p7270Clr": dpsRTUv2p7270Clr,
       "dpsRTUv2p7271Clr": dpsRTUv2p7271Clr,
       "dpsRTUv2p7272Clr": dpsRTUv2p7272Clr,
       "dpsRTUv2p7273Clr": dpsRTUv2p7273Clr,
       "dpsRTUv2p7274Clr": dpsRTUv2p7274Clr,
       "dpsRTUv2p7275Clr": dpsRTUv2p7275Clr,
       "dpsRTUv2p7276Clr": dpsRTUv2p7276Clr,
       "dpsRTUv2p7277Clr": dpsRTUv2p7277Clr,
       "dpsRTUv2p7278Clr": dpsRTUv2p7278Clr,
       "dpsRTUv2p7279Clr": dpsRTUv2p7279Clr,
       "dpsRTUv2p7280Clr": dpsRTUv2p7280Clr,
       "dpsRTUv2p7281Clr": dpsRTUv2p7281Clr,
       "dpsRTUv2p7282Clr": dpsRTUv2p7282Clr,
       "dpsRTUv2p7283Clr": dpsRTUv2p7283Clr,
       "dpsRTUv2p7284Clr": dpsRTUv2p7284Clr,
       "dpsRTUv2p7285Clr": dpsRTUv2p7285Clr,
       "dpsRTUv2p7286Clr": dpsRTUv2p7286Clr,
       "dpsRTUv2p7287Clr": dpsRTUv2p7287Clr,
       "dpsRTUv2p7288Clr": dpsRTUv2p7288Clr,
       "dpsRTUv2p7289Clr": dpsRTUv2p7289Clr,
       "dpsRTUv2p7290Clr": dpsRTUv2p7290Clr,
       "dpsRTUv2p7291Clr": dpsRTUv2p7291Clr,
       "dpsRTUv2p7292Clr": dpsRTUv2p7292Clr,
       "dpsRTUv2p7293Clr": dpsRTUv2p7293Clr,
       "dpsRTUv2p7294Clr": dpsRTUv2p7294Clr,
       "dpsRTUv2p7295Clr": dpsRTUv2p7295Clr,
       "dpsRTUv2p7296Clr": dpsRTUv2p7296Clr,
       "dpsRTUv2p7297Clr": dpsRTUv2p7297Clr,
       "dpsRTUv2p7298Clr": dpsRTUv2p7298Clr,
       "dpsRTUv2p7299Clr": dpsRTUv2p7299Clr,
       "dpsRTUv2p7300Clr": dpsRTUv2p7300Clr,
       "dpsRTUv2p7301Clr": dpsRTUv2p7301Clr,
       "dpsRTUv2p7302Clr": dpsRTUv2p7302Clr,
       "dpsRTUv2p7303Clr": dpsRTUv2p7303Clr,
       "dpsRTUv2p7304Clr": dpsRTUv2p7304Clr,
       "dpsRTUv2p7321Clr": dpsRTUv2p7321Clr,
       "dpsRTUv2p7322Clr": dpsRTUv2p7322Clr,
       "dpsRTUv2p7323Clr": dpsRTUv2p7323Clr,
       "dpsRTUv2p7324Clr": dpsRTUv2p7324Clr,
       "dpsRTUv2p7325Clr": dpsRTUv2p7325Clr,
       "dpsRTUv2p7326Clr": dpsRTUv2p7326Clr,
       "dpsRTUv2p7327Clr": dpsRTUv2p7327Clr,
       "dpsRTUv2p7328Clr": dpsRTUv2p7328Clr,
       "dpsRTUv2p7385Clr": dpsRTUv2p7385Clr,
       "dpsRTUv2p7386Clr": dpsRTUv2p7386Clr,
       "dpsRTUv2p7387Clr": dpsRTUv2p7387Clr,
       "dpsRTUv2p7388Clr": dpsRTUv2p7388Clr,
       "dpsRTUv2p7389Clr": dpsRTUv2p7389Clr,
       "dpsRTUv2p7390Clr": dpsRTUv2p7390Clr,
       "dpsRTUv2p7391Clr": dpsRTUv2p7391Clr,
       "dpsRTUv2p7392Clr": dpsRTUv2p7392Clr,
       "dpsRTUv2p7393Clr": dpsRTUv2p7393Clr,
       "dpsRTUv2p7394Clr": dpsRTUv2p7394Clr,
       "dpsRTUv2p7395Clr": dpsRTUv2p7395Clr,
       "dpsRTUv2p7396Clr": dpsRTUv2p7396Clr,
       "dpsRTUv2p7397Clr": dpsRTUv2p7397Clr,
       "dpsRTUv2p7398Clr": dpsRTUv2p7398Clr,
       "dpsRTUv2p7399Clr": dpsRTUv2p7399Clr,
       "dpsRTUv2p7400Clr": dpsRTUv2p7400Clr,
       "dpsRTUv2p7401Clr": dpsRTUv2p7401Clr,
       "dpsRTUv2p7402Clr": dpsRTUv2p7402Clr,
       "dpsRTUv2p7403Clr": dpsRTUv2p7403Clr,
       "dpsRTUv2p7404Clr": dpsRTUv2p7404Clr,
       "dpsRTUv2p7405Clr": dpsRTUv2p7405Clr,
       "dpsRTUv2p7406Clr": dpsRTUv2p7406Clr,
       "dpsRTUv2p7407Clr": dpsRTUv2p7407Clr,
       "dpsRTUv2p7408Clr": dpsRTUv2p7408Clr,
       "dpsRTUv2p7409Clr": dpsRTUv2p7409Clr,
       "dpsRTUv2p7410Clr": dpsRTUv2p7410Clr,
       "dpsRTUv2p7411Clr": dpsRTUv2p7411Clr,
       "dpsRTUv2p7412Clr": dpsRTUv2p7412Clr,
       "dpsRTUv2p7413Clr": dpsRTUv2p7413Clr,
       "dpsRTUv2p7414Clr": dpsRTUv2p7414Clr,
       "dpsRTUv2p7415Clr": dpsRTUv2p7415Clr,
       "dpsRTUv2p7416Clr": dpsRTUv2p7416Clr,
       "dpsRTUv2p7417Clr": dpsRTUv2p7417Clr,
       "dpsRTUv2p7418Clr": dpsRTUv2p7418Clr,
       "dpsRTUv2p7419Clr": dpsRTUv2p7419Clr,
       "dpsRTUv2p7420Clr": dpsRTUv2p7420Clr,
       "dpsRTUv2p7421Clr": dpsRTUv2p7421Clr,
       "dpsRTUv2p7422Clr": dpsRTUv2p7422Clr,
       "dpsRTUv2p7423Clr": dpsRTUv2p7423Clr,
       "dpsRTUv2p7424Clr": dpsRTUv2p7424Clr,
       "dpsRTUv2p7425Clr": dpsRTUv2p7425Clr,
       "dpsRTUv2p7426Clr": dpsRTUv2p7426Clr,
       "dpsRTUv2p7427Clr": dpsRTUv2p7427Clr,
       "dpsRTUv2p7428Clr": dpsRTUv2p7428Clr,
       "dpsRTUv2p7429Clr": dpsRTUv2p7429Clr,
       "dpsRTUv2p7430Clr": dpsRTUv2p7430Clr,
       "dpsRTUv2p7431Clr": dpsRTUv2p7431Clr,
       "dpsRTUv2p7432Clr": dpsRTUv2p7432Clr,
       "dpsRTUv2p7433Clr": dpsRTUv2p7433Clr,
       "dpsRTUv2p7434Clr": dpsRTUv2p7434Clr,
       "dpsRTUv2p7435Clr": dpsRTUv2p7435Clr,
       "dpsRTUv2p7436Clr": dpsRTUv2p7436Clr,
       "dpsRTUv2p7437Clr": dpsRTUv2p7437Clr,
       "dpsRTUv2p7438Clr": dpsRTUv2p7438Clr,
       "dpsRTUv2p7439Clr": dpsRTUv2p7439Clr,
       "dpsRTUv2p7440Clr": dpsRTUv2p7440Clr,
       "dpsRTUv2p7441Clr": dpsRTUv2p7441Clr,
       "dpsRTUv2p7442Clr": dpsRTUv2p7442Clr,
       "dpsRTUv2p7443Clr": dpsRTUv2p7443Clr,
       "dpsRTUv2p7444Clr": dpsRTUv2p7444Clr,
       "dpsRTUv2p7445Clr": dpsRTUv2p7445Clr,
       "dpsRTUv2p7446Clr": dpsRTUv2p7446Clr,
       "dpsRTUv2p7447Clr": dpsRTUv2p7447Clr,
       "dpsRTUv2p7448Clr": dpsRTUv2p7448Clr,
       "dpsRTUv2p7449Clr": dpsRTUv2p7449Clr,
       "dpsRTUv2p7450Clr": dpsRTUv2p7450Clr,
       "dpsRTUv2p7451Clr": dpsRTUv2p7451Clr,
       "dpsRTUv2p7452Clr": dpsRTUv2p7452Clr,
       "dpsRTUv2p7453Clr": dpsRTUv2p7453Clr,
       "dpsRTUv2p7454Clr": dpsRTUv2p7454Clr,
       "dpsRTUv2p7455Clr": dpsRTUv2p7455Clr,
       "dpsRTUv2p7456Clr": dpsRTUv2p7456Clr,
       "dpsRTUv2p7457Clr": dpsRTUv2p7457Clr,
       "dpsRTUv2p7458Clr": dpsRTUv2p7458Clr,
       "dpsRTUv2p7459Clr": dpsRTUv2p7459Clr,
       "dpsRTUv2p7460Clr": dpsRTUv2p7460Clr,
       "dpsRTUv2p7461Clr": dpsRTUv2p7461Clr,
       "dpsRTUv2p7462Clr": dpsRTUv2p7462Clr,
       "dpsRTUv2p7463Clr": dpsRTUv2p7463Clr,
       "dpsRTUv2p7464Clr": dpsRTUv2p7464Clr,
       "dpsRTUv2p7465Clr": dpsRTUv2p7465Clr,
       "dpsRTUv2p7466Clr": dpsRTUv2p7466Clr,
       "dpsRTUv2p7467Clr": dpsRTUv2p7467Clr,
       "dpsRTUv2p7468Clr": dpsRTUv2p7468Clr,
       "dpsRTUv2p7469Clr": dpsRTUv2p7469Clr,
       "dpsRTUv2p7470Clr": dpsRTUv2p7470Clr,
       "dpsRTUv2p7471Clr": dpsRTUv2p7471Clr,
       "dpsRTUv2p7472Clr": dpsRTUv2p7472Clr,
       "dpsRTUv2p7473Clr": dpsRTUv2p7473Clr,
       "dpsRTUv2p7474Clr": dpsRTUv2p7474Clr,
       "dpsRTUv2p7475Clr": dpsRTUv2p7475Clr,
       "dpsRTUv2p7476Clr": dpsRTUv2p7476Clr,
       "dpsRTUv2p7477Clr": dpsRTUv2p7477Clr,
       "dpsRTUv2p7478Clr": dpsRTUv2p7478Clr,
       "dpsRTUv2p7479Clr": dpsRTUv2p7479Clr,
       "dpsRTUv2p7480Clr": dpsRTUv2p7480Clr,
       "dpsRTUxV2MI": dpsRTUxV2MI}
)
