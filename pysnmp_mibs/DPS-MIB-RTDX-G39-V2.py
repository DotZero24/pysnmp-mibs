# SNMP MIB module (DPS-MIB-RTDX-G39-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dps/DPS-MIB-RTDX-G39-V2
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:58 2025
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

dpsRTUrtdV2MI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 6)
)
if mibBuilder.loadTexts:
    dpsRTUrtdV2MI.setRevisions(
        ("2012-08-08 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

dpsRTUv2p10001Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10001)
)
dpsRTUv2p10001Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10001Set.setStatus(
        "current"
    )

dpsRTUv2p10002Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10002)
)
dpsRTUv2p10002Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10002Set.setStatus(
        "current"
    )

dpsRTUv2p10003Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10003)
)
dpsRTUv2p10003Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10003Set.setStatus(
        "current"
    )

dpsRTUv2p10004Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10004)
)
dpsRTUv2p10004Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10004Set.setStatus(
        "current"
    )

dpsRTUv2p10005Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10005)
)
dpsRTUv2p10005Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10005Set.setStatus(
        "current"
    )

dpsRTUv2p10006Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10006)
)
dpsRTUv2p10006Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10006Set.setStatus(
        "current"
    )

dpsRTUv2p10007Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10007)
)
dpsRTUv2p10007Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10007Set.setStatus(
        "current"
    )

dpsRTUv2p10008Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10008)
)
dpsRTUv2p10008Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10008Set.setStatus(
        "current"
    )

dpsRTUv2p10009Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10009)
)
dpsRTUv2p10009Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10009Set.setStatus(
        "current"
    )

dpsRTUv2p10010Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10010)
)
dpsRTUv2p10010Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10010Set.setStatus(
        "current"
    )

dpsRTUv2p10011Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10011)
)
dpsRTUv2p10011Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10011Set.setStatus(
        "current"
    )

dpsRTUv2p10012Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10012)
)
dpsRTUv2p10012Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10012Set.setStatus(
        "current"
    )

dpsRTUv2p10013Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10013)
)
dpsRTUv2p10013Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10013Set.setStatus(
        "current"
    )

dpsRTUv2p10014Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10014)
)
dpsRTUv2p10014Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10014Set.setStatus(
        "current"
    )

dpsRTUv2p10015Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10015)
)
dpsRTUv2p10015Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10015Set.setStatus(
        "current"
    )

dpsRTUv2p10016Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10016)
)
dpsRTUv2p10016Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10016Set.setStatus(
        "current"
    )

dpsRTUv2p10017Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10017)
)
dpsRTUv2p10017Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10017Set.setStatus(
        "current"
    )

dpsRTUv2p10018Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10018)
)
dpsRTUv2p10018Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10018Set.setStatus(
        "current"
    )

dpsRTUv2p10019Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10019)
)
dpsRTUv2p10019Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10019Set.setStatus(
        "current"
    )

dpsRTUv2p10020Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10020)
)
dpsRTUv2p10020Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10020Set.setStatus(
        "current"
    )

dpsRTUv2p10021Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10021)
)
dpsRTUv2p10021Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10021Set.setStatus(
        "current"
    )

dpsRTUv2p10022Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10022)
)
dpsRTUv2p10022Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10022Set.setStatus(
        "current"
    )

dpsRTUv2p10023Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10023)
)
dpsRTUv2p10023Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10023Set.setStatus(
        "current"
    )

dpsRTUv2p10024Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10024)
)
dpsRTUv2p10024Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10024Set.setStatus(
        "current"
    )

dpsRTUv2p10025Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10025)
)
dpsRTUv2p10025Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10025Set.setStatus(
        "current"
    )

dpsRTUv2p10026Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10026)
)
dpsRTUv2p10026Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10026Set.setStatus(
        "current"
    )

dpsRTUv2p10027Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10027)
)
dpsRTUv2p10027Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10027Set.setStatus(
        "current"
    )

dpsRTUv2p10028Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10028)
)
dpsRTUv2p10028Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10028Set.setStatus(
        "current"
    )

dpsRTUv2p10029Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10029)
)
dpsRTUv2p10029Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10029Set.setStatus(
        "current"
    )

dpsRTUv2p10030Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10030)
)
dpsRTUv2p10030Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10030Set.setStatus(
        "current"
    )

dpsRTUv2p10031Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10031)
)
dpsRTUv2p10031Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10031Set.setStatus(
        "current"
    )

dpsRTUv2p10032Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10032)
)
dpsRTUv2p10032Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10032Set.setStatus(
        "current"
    )

dpsRTUv2p10033Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10033)
)
dpsRTUv2p10033Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10033Set.setStatus(
        "current"
    )

dpsRTUv2p10034Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10034)
)
dpsRTUv2p10034Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10034Set.setStatus(
        "current"
    )

dpsRTUv2p10035Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10035)
)
dpsRTUv2p10035Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10035Set.setStatus(
        "current"
    )

dpsRTUv2p10036Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10036)
)
dpsRTUv2p10036Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10036Set.setStatus(
        "current"
    )

dpsRTUv2p10037Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10037)
)
dpsRTUv2p10037Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10037Set.setStatus(
        "current"
    )

dpsRTUv2p10038Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10038)
)
dpsRTUv2p10038Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10038Set.setStatus(
        "current"
    )

dpsRTUv2p10039Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10039)
)
dpsRTUv2p10039Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10039Set.setStatus(
        "current"
    )

dpsRTUv2p10040Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10040)
)
dpsRTUv2p10040Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10040Set.setStatus(
        "current"
    )

dpsRTUv2p10041Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10041)
)
dpsRTUv2p10041Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10041Set.setStatus(
        "current"
    )

dpsRTUv2p10042Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10042)
)
dpsRTUv2p10042Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10042Set.setStatus(
        "current"
    )

dpsRTUv2p10043Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10043)
)
dpsRTUv2p10043Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10043Set.setStatus(
        "current"
    )

dpsRTUv2p10044Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10044)
)
dpsRTUv2p10044Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10044Set.setStatus(
        "current"
    )

dpsRTUv2p10045Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10045)
)
dpsRTUv2p10045Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10045Set.setStatus(
        "current"
    )

dpsRTUv2p10046Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10046)
)
dpsRTUv2p10046Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10046Set.setStatus(
        "current"
    )

dpsRTUv2p10047Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10047)
)
dpsRTUv2p10047Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10047Set.setStatus(
        "current"
    )

dpsRTUv2p10048Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10048)
)
dpsRTUv2p10048Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10048Set.setStatus(
        "current"
    )

dpsRTUv2p10049Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10049)
)
dpsRTUv2p10049Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10049Set.setStatus(
        "current"
    )

dpsRTUv2p10050Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10050)
)
dpsRTUv2p10050Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10050Set.setStatus(
        "current"
    )

dpsRTUv2p10051Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10051)
)
dpsRTUv2p10051Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10051Set.setStatus(
        "current"
    )

dpsRTUv2p10052Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10052)
)
dpsRTUv2p10052Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10052Set.setStatus(
        "current"
    )

dpsRTUv2p10053Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10053)
)
dpsRTUv2p10053Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10053Set.setStatus(
        "current"
    )

dpsRTUv2p10054Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10054)
)
dpsRTUv2p10054Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10054Set.setStatus(
        "current"
    )

dpsRTUv2p10055Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10055)
)
dpsRTUv2p10055Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10055Set.setStatus(
        "current"
    )

dpsRTUv2p10056Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10056)
)
dpsRTUv2p10056Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10056Set.setStatus(
        "current"
    )

dpsRTUv2p10057Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10057)
)
dpsRTUv2p10057Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10057Set.setStatus(
        "current"
    )

dpsRTUv2p10058Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10058)
)
dpsRTUv2p10058Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10058Set.setStatus(
        "current"
    )

dpsRTUv2p10059Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10059)
)
dpsRTUv2p10059Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10059Set.setStatus(
        "current"
    )

dpsRTUv2p10060Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10060)
)
dpsRTUv2p10060Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10060Set.setStatus(
        "current"
    )

dpsRTUv2p10061Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10061)
)
dpsRTUv2p10061Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10061Set.setStatus(
        "current"
    )

dpsRTUv2p10062Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10062)
)
dpsRTUv2p10062Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10062Set.setStatus(
        "current"
    )

dpsRTUv2p10063Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10063)
)
dpsRTUv2p10063Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10063Set.setStatus(
        "current"
    )

dpsRTUv2p10064Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10064)
)
dpsRTUv2p10064Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10064Set.setStatus(
        "current"
    )

dpsRTUv2p10065Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10065)
)
dpsRTUv2p10065Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10065Set.setStatus(
        "current"
    )

dpsRTUv2p10066Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10066)
)
dpsRTUv2p10066Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10066Set.setStatus(
        "current"
    )

dpsRTUv2p10067Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10067)
)
dpsRTUv2p10067Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10067Set.setStatus(
        "current"
    )

dpsRTUv2p10068Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10068)
)
dpsRTUv2p10068Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10068Set.setStatus(
        "current"
    )

dpsRTUv2p10069Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10069)
)
dpsRTUv2p10069Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10069Set.setStatus(
        "current"
    )

dpsRTUv2p10070Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10070)
)
dpsRTUv2p10070Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10070Set.setStatus(
        "current"
    )

dpsRTUv2p10071Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10071)
)
dpsRTUv2p10071Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10071Set.setStatus(
        "current"
    )

dpsRTUv2p10072Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10072)
)
dpsRTUv2p10072Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10072Set.setStatus(
        "current"
    )

dpsRTUv2p10073Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10073)
)
dpsRTUv2p10073Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10073Set.setStatus(
        "current"
    )

dpsRTUv2p10074Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10074)
)
dpsRTUv2p10074Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10074Set.setStatus(
        "current"
    )

dpsRTUv2p10075Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10075)
)
dpsRTUv2p10075Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10075Set.setStatus(
        "current"
    )

dpsRTUv2p10076Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10076)
)
dpsRTUv2p10076Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10076Set.setStatus(
        "current"
    )

dpsRTUv2p10077Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10077)
)
dpsRTUv2p10077Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10077Set.setStatus(
        "current"
    )

dpsRTUv2p10078Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10078)
)
dpsRTUv2p10078Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10078Set.setStatus(
        "current"
    )

dpsRTUv2p10079Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10079)
)
dpsRTUv2p10079Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10079Set.setStatus(
        "current"
    )

dpsRTUv2p10080Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10080)
)
dpsRTUv2p10080Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10080Set.setStatus(
        "current"
    )

dpsRTUv2p10081Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10081)
)
dpsRTUv2p10081Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10081Set.setStatus(
        "current"
    )

dpsRTUv2p10082Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10082)
)
dpsRTUv2p10082Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10082Set.setStatus(
        "current"
    )

dpsRTUv2p10083Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10083)
)
dpsRTUv2p10083Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10083Set.setStatus(
        "current"
    )

dpsRTUv2p10084Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10084)
)
dpsRTUv2p10084Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10084Set.setStatus(
        "current"
    )

dpsRTUv2p10085Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10085)
)
dpsRTUv2p10085Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10085Set.setStatus(
        "current"
    )

dpsRTUv2p10086Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10086)
)
dpsRTUv2p10086Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10086Set.setStatus(
        "current"
    )

dpsRTUv2p10087Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10087)
)
dpsRTUv2p10087Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10087Set.setStatus(
        "current"
    )

dpsRTUv2p10088Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10088)
)
dpsRTUv2p10088Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10088Set.setStatus(
        "current"
    )

dpsRTUv2p10089Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10089)
)
dpsRTUv2p10089Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10089Set.setStatus(
        "current"
    )

dpsRTUv2p10090Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10090)
)
dpsRTUv2p10090Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10090Set.setStatus(
        "current"
    )

dpsRTUv2p10091Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10091)
)
dpsRTUv2p10091Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10091Set.setStatus(
        "current"
    )

dpsRTUv2p10092Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10092)
)
dpsRTUv2p10092Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10092Set.setStatus(
        "current"
    )

dpsRTUv2p10093Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10093)
)
dpsRTUv2p10093Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10093Set.setStatus(
        "current"
    )

dpsRTUv2p10094Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10094)
)
dpsRTUv2p10094Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10094Set.setStatus(
        "current"
    )

dpsRTUv2p10095Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10095)
)
dpsRTUv2p10095Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10095Set.setStatus(
        "current"
    )

dpsRTUv2p10096Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10096)
)
dpsRTUv2p10096Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10096Set.setStatus(
        "current"
    )

dpsRTUv2p10097Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10097)
)
dpsRTUv2p10097Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10097Set.setStatus(
        "current"
    )

dpsRTUv2p10098Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10098)
)
dpsRTUv2p10098Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10098Set.setStatus(
        "current"
    )

dpsRTUv2p10099Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10099)
)
dpsRTUv2p10099Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10099Set.setStatus(
        "current"
    )

dpsRTUv2p10100Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10100)
)
dpsRTUv2p10100Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10100Set.setStatus(
        "current"
    )

dpsRTUv2p10101Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10101)
)
dpsRTUv2p10101Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10101Set.setStatus(
        "current"
    )

dpsRTUv2p10102Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10102)
)
dpsRTUv2p10102Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10102Set.setStatus(
        "current"
    )

dpsRTUv2p10103Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10103)
)
dpsRTUv2p10103Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10103Set.setStatus(
        "current"
    )

dpsRTUv2p10104Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10104)
)
dpsRTUv2p10104Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10104Set.setStatus(
        "current"
    )

dpsRTUv2p10105Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10105)
)
dpsRTUv2p10105Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10105Set.setStatus(
        "current"
    )

dpsRTUv2p10106Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10106)
)
dpsRTUv2p10106Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10106Set.setStatus(
        "current"
    )

dpsRTUv2p10107Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10107)
)
dpsRTUv2p10107Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10107Set.setStatus(
        "current"
    )

dpsRTUv2p10108Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10108)
)
dpsRTUv2p10108Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10108Set.setStatus(
        "current"
    )

dpsRTUv2p10109Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10109)
)
dpsRTUv2p10109Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10109Set.setStatus(
        "current"
    )

dpsRTUv2p10110Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10110)
)
dpsRTUv2p10110Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10110Set.setStatus(
        "current"
    )

dpsRTUv2p10111Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10111)
)
dpsRTUv2p10111Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10111Set.setStatus(
        "current"
    )

dpsRTUv2p10112Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10112)
)
dpsRTUv2p10112Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10112Set.setStatus(
        "current"
    )

dpsRTUv2p10113Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10113)
)
dpsRTUv2p10113Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10113Set.setStatus(
        "current"
    )

dpsRTUv2p10114Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10114)
)
dpsRTUv2p10114Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10114Set.setStatus(
        "current"
    )

dpsRTUv2p10115Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10115)
)
dpsRTUv2p10115Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10115Set.setStatus(
        "current"
    )

dpsRTUv2p10116Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10116)
)
dpsRTUv2p10116Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10116Set.setStatus(
        "current"
    )

dpsRTUv2p10117Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10117)
)
dpsRTUv2p10117Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10117Set.setStatus(
        "current"
    )

dpsRTUv2p10118Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10118)
)
dpsRTUv2p10118Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10118Set.setStatus(
        "current"
    )

dpsRTUv2p10119Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10119)
)
dpsRTUv2p10119Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10119Set.setStatus(
        "current"
    )

dpsRTUv2p10120Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10120)
)
dpsRTUv2p10120Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10120Set.setStatus(
        "current"
    )

dpsRTUv2p10121Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10121)
)
dpsRTUv2p10121Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10121Set.setStatus(
        "current"
    )

dpsRTUv2p10122Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10122)
)
dpsRTUv2p10122Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10122Set.setStatus(
        "current"
    )

dpsRTUv2p10123Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10123)
)
dpsRTUv2p10123Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10123Set.setStatus(
        "current"
    )

dpsRTUv2p10124Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10124)
)
dpsRTUv2p10124Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10124Set.setStatus(
        "current"
    )

dpsRTUv2p10125Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10125)
)
dpsRTUv2p10125Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10125Set.setStatus(
        "current"
    )

dpsRTUv2p10126Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10126)
)
dpsRTUv2p10126Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10126Set.setStatus(
        "current"
    )

dpsRTUv2p10127Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10127)
)
dpsRTUv2p10127Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10127Set.setStatus(
        "current"
    )

dpsRTUv2p10128Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10128)
)
dpsRTUv2p10128Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10128Set.setStatus(
        "current"
    )

dpsRTUv2p10129Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10129)
)
dpsRTUv2p10129Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10129Set.setStatus(
        "current"
    )

dpsRTUv2p10130Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10130)
)
dpsRTUv2p10130Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10130Set.setStatus(
        "current"
    )

dpsRTUv2p10131Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10131)
)
dpsRTUv2p10131Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10131Set.setStatus(
        "current"
    )

dpsRTUv2p10132Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10132)
)
dpsRTUv2p10132Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10132Set.setStatus(
        "current"
    )

dpsRTUv2p10133Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10133)
)
dpsRTUv2p10133Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10133Set.setStatus(
        "current"
    )

dpsRTUv2p10134Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10134)
)
dpsRTUv2p10134Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10134Set.setStatus(
        "current"
    )

dpsRTUv2p10135Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10135)
)
dpsRTUv2p10135Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10135Set.setStatus(
        "current"
    )

dpsRTUv2p10136Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10136)
)
dpsRTUv2p10136Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10136Set.setStatus(
        "current"
    )

dpsRTUv2p10137Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10137)
)
dpsRTUv2p10137Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10137Set.setStatus(
        "current"
    )

dpsRTUv2p10138Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10138)
)
dpsRTUv2p10138Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10138Set.setStatus(
        "current"
    )

dpsRTUv2p10139Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10139)
)
dpsRTUv2p10139Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10139Set.setStatus(
        "current"
    )

dpsRTUv2p10140Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10140)
)
dpsRTUv2p10140Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10140Set.setStatus(
        "current"
    )

dpsRTUv2p10141Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10141)
)
dpsRTUv2p10141Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10141Set.setStatus(
        "current"
    )

dpsRTUv2p10142Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10142)
)
dpsRTUv2p10142Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10142Set.setStatus(
        "current"
    )

dpsRTUv2p10143Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10143)
)
dpsRTUv2p10143Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10143Set.setStatus(
        "current"
    )

dpsRTUv2p10144Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10144)
)
dpsRTUv2p10144Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10144Set.setStatus(
        "current"
    )

dpsRTUv2p10145Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10145)
)
dpsRTUv2p10145Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10145Set.setStatus(
        "current"
    )

dpsRTUv2p10146Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10146)
)
dpsRTUv2p10146Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10146Set.setStatus(
        "current"
    )

dpsRTUv2p10147Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10147)
)
dpsRTUv2p10147Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10147Set.setStatus(
        "current"
    )

dpsRTUv2p10148Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10148)
)
dpsRTUv2p10148Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10148Set.setStatus(
        "current"
    )

dpsRTUv2p10149Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10149)
)
dpsRTUv2p10149Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10149Set.setStatus(
        "current"
    )

dpsRTUv2p10150Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10150)
)
dpsRTUv2p10150Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10150Set.setStatus(
        "current"
    )

dpsRTUv2p10151Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10151)
)
dpsRTUv2p10151Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10151Set.setStatus(
        "current"
    )

dpsRTUv2p10152Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10152)
)
dpsRTUv2p10152Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10152Set.setStatus(
        "current"
    )

dpsRTUv2p10153Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10153)
)
dpsRTUv2p10153Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10153Set.setStatus(
        "current"
    )

dpsRTUv2p10154Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10154)
)
dpsRTUv2p10154Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10154Set.setStatus(
        "current"
    )

dpsRTUv2p10155Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10155)
)
dpsRTUv2p10155Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10155Set.setStatus(
        "current"
    )

dpsRTUv2p10156Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10156)
)
dpsRTUv2p10156Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10156Set.setStatus(
        "current"
    )

dpsRTUv2p10157Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10157)
)
dpsRTUv2p10157Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10157Set.setStatus(
        "current"
    )

dpsRTUv2p10158Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10158)
)
dpsRTUv2p10158Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10158Set.setStatus(
        "current"
    )

dpsRTUv2p10159Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10159)
)
dpsRTUv2p10159Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10159Set.setStatus(
        "current"
    )

dpsRTUv2p10160Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10160)
)
dpsRTUv2p10160Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10160Set.setStatus(
        "current"
    )

dpsRTUv2p10161Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10161)
)
dpsRTUv2p10161Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10161Set.setStatus(
        "current"
    )

dpsRTUv2p10162Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10162)
)
dpsRTUv2p10162Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10162Set.setStatus(
        "current"
    )

dpsRTUv2p10163Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10163)
)
dpsRTUv2p10163Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10163Set.setStatus(
        "current"
    )

dpsRTUv2p10164Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10164)
)
dpsRTUv2p10164Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10164Set.setStatus(
        "current"
    )

dpsRTUv2p10165Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10165)
)
dpsRTUv2p10165Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10165Set.setStatus(
        "current"
    )

dpsRTUv2p10166Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10166)
)
dpsRTUv2p10166Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10166Set.setStatus(
        "current"
    )

dpsRTUv2p10167Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10167)
)
dpsRTUv2p10167Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10167Set.setStatus(
        "current"
    )

dpsRTUv2p10168Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10168)
)
dpsRTUv2p10168Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10168Set.setStatus(
        "current"
    )

dpsRTUv2p10169Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10169)
)
dpsRTUv2p10169Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10169Set.setStatus(
        "current"
    )

dpsRTUv2p10170Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10170)
)
dpsRTUv2p10170Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10170Set.setStatus(
        "current"
    )

dpsRTUv2p10171Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10171)
)
dpsRTUv2p10171Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10171Set.setStatus(
        "current"
    )

dpsRTUv2p10172Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10172)
)
dpsRTUv2p10172Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10172Set.setStatus(
        "current"
    )

dpsRTUv2p10173Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10173)
)
dpsRTUv2p10173Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10173Set.setStatus(
        "current"
    )

dpsRTUv2p10174Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10174)
)
dpsRTUv2p10174Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10174Set.setStatus(
        "current"
    )

dpsRTUv2p10175Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10175)
)
dpsRTUv2p10175Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10175Set.setStatus(
        "current"
    )

dpsRTUv2p10176Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10176)
)
dpsRTUv2p10176Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10176Set.setStatus(
        "current"
    )

dpsRTUv2p10177Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10177)
)
dpsRTUv2p10177Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10177Set.setStatus(
        "current"
    )

dpsRTUv2p10178Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10178)
)
dpsRTUv2p10178Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10178Set.setStatus(
        "current"
    )

dpsRTUv2p10179Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10179)
)
dpsRTUv2p10179Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10179Set.setStatus(
        "current"
    )

dpsRTUv2p10180Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10180)
)
dpsRTUv2p10180Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10180Set.setStatus(
        "current"
    )

dpsRTUv2p10181Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10181)
)
dpsRTUv2p10181Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10181Set.setStatus(
        "current"
    )

dpsRTUv2p10182Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10182)
)
dpsRTUv2p10182Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10182Set.setStatus(
        "current"
    )

dpsRTUv2p10183Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10183)
)
dpsRTUv2p10183Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10183Set.setStatus(
        "current"
    )

dpsRTUv2p10184Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10184)
)
dpsRTUv2p10184Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10184Set.setStatus(
        "current"
    )

dpsRTUv2p10185Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10185)
)
dpsRTUv2p10185Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10185Set.setStatus(
        "current"
    )

dpsRTUv2p10186Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10186)
)
dpsRTUv2p10186Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10186Set.setStatus(
        "current"
    )

dpsRTUv2p10187Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10187)
)
dpsRTUv2p10187Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10187Set.setStatus(
        "current"
    )

dpsRTUv2p10188Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10188)
)
dpsRTUv2p10188Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10188Set.setStatus(
        "current"
    )

dpsRTUv2p10189Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10189)
)
dpsRTUv2p10189Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10189Set.setStatus(
        "current"
    )

dpsRTUv2p10190Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10190)
)
dpsRTUv2p10190Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10190Set.setStatus(
        "current"
    )

dpsRTUv2p10191Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10191)
)
dpsRTUv2p10191Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10191Set.setStatus(
        "current"
    )

dpsRTUv2p10192Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10192)
)
dpsRTUv2p10192Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10192Set.setStatus(
        "current"
    )

dpsRTUv2p10193Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10193)
)
dpsRTUv2p10193Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10193Set.setStatus(
        "current"
    )

dpsRTUv2p10194Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10194)
)
dpsRTUv2p10194Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10194Set.setStatus(
        "current"
    )

dpsRTUv2p10195Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10195)
)
dpsRTUv2p10195Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10195Set.setStatus(
        "current"
    )

dpsRTUv2p10196Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10196)
)
dpsRTUv2p10196Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10196Set.setStatus(
        "current"
    )

dpsRTUv2p10197Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10197)
)
dpsRTUv2p10197Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10197Set.setStatus(
        "current"
    )

dpsRTUv2p10198Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10198)
)
dpsRTUv2p10198Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10198Set.setStatus(
        "current"
    )

dpsRTUv2p10199Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10199)
)
dpsRTUv2p10199Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10199Set.setStatus(
        "current"
    )

dpsRTUv2p10200Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10200)
)
dpsRTUv2p10200Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10200Set.setStatus(
        "current"
    )

dpsRTUv2p10201Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10201)
)
dpsRTUv2p10201Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10201Set.setStatus(
        "current"
    )

dpsRTUv2p10202Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10202)
)
dpsRTUv2p10202Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10202Set.setStatus(
        "current"
    )

dpsRTUv2p10203Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10203)
)
dpsRTUv2p10203Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10203Set.setStatus(
        "current"
    )

dpsRTUv2p10204Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10204)
)
dpsRTUv2p10204Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10204Set.setStatus(
        "current"
    )

dpsRTUv2p10205Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10205)
)
dpsRTUv2p10205Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10205Set.setStatus(
        "current"
    )

dpsRTUv2p10206Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10206)
)
dpsRTUv2p10206Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10206Set.setStatus(
        "current"
    )

dpsRTUv2p10207Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10207)
)
dpsRTUv2p10207Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10207Set.setStatus(
        "current"
    )

dpsRTUv2p10208Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10208)
)
dpsRTUv2p10208Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10208Set.setStatus(
        "current"
    )

dpsRTUv2p10209Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10209)
)
dpsRTUv2p10209Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10209Set.setStatus(
        "current"
    )

dpsRTUv2p10210Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10210)
)
dpsRTUv2p10210Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10210Set.setStatus(
        "current"
    )

dpsRTUv2p10211Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10211)
)
dpsRTUv2p10211Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10211Set.setStatus(
        "current"
    )

dpsRTUv2p10212Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10212)
)
dpsRTUv2p10212Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10212Set.setStatus(
        "current"
    )

dpsRTUv2p10213Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10213)
)
dpsRTUv2p10213Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10213Set.setStatus(
        "current"
    )

dpsRTUv2p10214Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10214)
)
dpsRTUv2p10214Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10214Set.setStatus(
        "current"
    )

dpsRTUv2p10215Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10215)
)
dpsRTUv2p10215Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10215Set.setStatus(
        "current"
    )

dpsRTUv2p10216Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10216)
)
dpsRTUv2p10216Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10216Set.setStatus(
        "current"
    )

dpsRTUv2p10217Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10217)
)
dpsRTUv2p10217Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10217Set.setStatus(
        "current"
    )

dpsRTUv2p10218Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10218)
)
dpsRTUv2p10218Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10218Set.setStatus(
        "current"
    )

dpsRTUv2p10219Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10219)
)
dpsRTUv2p10219Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10219Set.setStatus(
        "current"
    )

dpsRTUv2p10220Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10220)
)
dpsRTUv2p10220Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10220Set.setStatus(
        "current"
    )

dpsRTUv2p10221Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10221)
)
dpsRTUv2p10221Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10221Set.setStatus(
        "current"
    )

dpsRTUv2p10222Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10222)
)
dpsRTUv2p10222Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10222Set.setStatus(
        "current"
    )

dpsRTUv2p10223Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10223)
)
dpsRTUv2p10223Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10223Set.setStatus(
        "current"
    )

dpsRTUv2p10224Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10224)
)
dpsRTUv2p10224Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10224Set.setStatus(
        "current"
    )

dpsRTUv2p10225Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10225)
)
dpsRTUv2p10225Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10225Set.setStatus(
        "current"
    )

dpsRTUv2p10226Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10226)
)
dpsRTUv2p10226Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10226Set.setStatus(
        "current"
    )

dpsRTUv2p10227Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10227)
)
dpsRTUv2p10227Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10227Set.setStatus(
        "current"
    )

dpsRTUv2p10228Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10228)
)
dpsRTUv2p10228Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10228Set.setStatus(
        "current"
    )

dpsRTUv2p10229Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10229)
)
dpsRTUv2p10229Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10229Set.setStatus(
        "current"
    )

dpsRTUv2p10230Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10230)
)
dpsRTUv2p10230Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10230Set.setStatus(
        "current"
    )

dpsRTUv2p10231Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10231)
)
dpsRTUv2p10231Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10231Set.setStatus(
        "current"
    )

dpsRTUv2p10232Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10232)
)
dpsRTUv2p10232Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10232Set.setStatus(
        "current"
    )

dpsRTUv2p10233Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10233)
)
dpsRTUv2p10233Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10233Set.setStatus(
        "current"
    )

dpsRTUv2p10234Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10234)
)
dpsRTUv2p10234Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10234Set.setStatus(
        "current"
    )

dpsRTUv2p10235Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10235)
)
dpsRTUv2p10235Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10235Set.setStatus(
        "current"
    )

dpsRTUv2p10236Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10236)
)
dpsRTUv2p10236Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10236Set.setStatus(
        "current"
    )

dpsRTUv2p10237Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10237)
)
dpsRTUv2p10237Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10237Set.setStatus(
        "current"
    )

dpsRTUv2p10238Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10238)
)
dpsRTUv2p10238Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10238Set.setStatus(
        "current"
    )

dpsRTUv2p10239Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10239)
)
dpsRTUv2p10239Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10239Set.setStatus(
        "current"
    )

dpsRTUv2p10240Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10240)
)
dpsRTUv2p10240Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10240Set.setStatus(
        "current"
    )

dpsRTUv2p10241Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10241)
)
dpsRTUv2p10241Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10241Set.setStatus(
        "current"
    )

dpsRTUv2p10242Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10242)
)
dpsRTUv2p10242Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10242Set.setStatus(
        "current"
    )

dpsRTUv2p10243Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10243)
)
dpsRTUv2p10243Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10243Set.setStatus(
        "current"
    )

dpsRTUv2p10244Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10244)
)
dpsRTUv2p10244Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10244Set.setStatus(
        "current"
    )

dpsRTUv2p10245Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10245)
)
dpsRTUv2p10245Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10245Set.setStatus(
        "current"
    )

dpsRTUv2p10246Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10246)
)
dpsRTUv2p10246Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10246Set.setStatus(
        "current"
    )

dpsRTUv2p10247Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10247)
)
dpsRTUv2p10247Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10247Set.setStatus(
        "current"
    )

dpsRTUv2p10248Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10248)
)
dpsRTUv2p10248Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10248Set.setStatus(
        "current"
    )

dpsRTUv2p10249Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10249)
)
dpsRTUv2p10249Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10249Set.setStatus(
        "current"
    )

dpsRTUv2p10250Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10250)
)
dpsRTUv2p10250Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10250Set.setStatus(
        "current"
    )

dpsRTUv2p10251Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10251)
)
dpsRTUv2p10251Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10251Set.setStatus(
        "current"
    )

dpsRTUv2p10252Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10252)
)
dpsRTUv2p10252Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10252Set.setStatus(
        "current"
    )

dpsRTUv2p10253Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10253)
)
dpsRTUv2p10253Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10253Set.setStatus(
        "current"
    )

dpsRTUv2p10254Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10254)
)
dpsRTUv2p10254Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10254Set.setStatus(
        "current"
    )

dpsRTUv2p10255Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10255)
)
dpsRTUv2p10255Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10255Set.setStatus(
        "current"
    )

dpsRTUv2p10256Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10256)
)
dpsRTUv2p10256Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10256Set.setStatus(
        "current"
    )

dpsRTUv2p10257Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10257)
)
dpsRTUv2p10257Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10257Set.setStatus(
        "current"
    )

dpsRTUv2p10258Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10258)
)
dpsRTUv2p10258Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10258Set.setStatus(
        "current"
    )

dpsRTUv2p10259Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10259)
)
dpsRTUv2p10259Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10259Set.setStatus(
        "current"
    )

dpsRTUv2p10260Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10260)
)
dpsRTUv2p10260Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10260Set.setStatus(
        "current"
    )

dpsRTUv2p10261Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10261)
)
dpsRTUv2p10261Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10261Set.setStatus(
        "current"
    )

dpsRTUv2p10262Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10262)
)
dpsRTUv2p10262Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10262Set.setStatus(
        "current"
    )

dpsRTUv2p10263Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10263)
)
dpsRTUv2p10263Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10263Set.setStatus(
        "current"
    )

dpsRTUv2p10264Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10264)
)
dpsRTUv2p10264Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10264Set.setStatus(
        "current"
    )

dpsRTUv2p10265Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10265)
)
dpsRTUv2p10265Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10265Set.setStatus(
        "current"
    )

dpsRTUv2p10266Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10266)
)
dpsRTUv2p10266Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10266Set.setStatus(
        "current"
    )

dpsRTUv2p10267Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10267)
)
dpsRTUv2p10267Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10267Set.setStatus(
        "current"
    )

dpsRTUv2p10268Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10268)
)
dpsRTUv2p10268Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10268Set.setStatus(
        "current"
    )

dpsRTUv2p10269Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10269)
)
dpsRTUv2p10269Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10269Set.setStatus(
        "current"
    )

dpsRTUv2p10270Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10270)
)
dpsRTUv2p10270Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10270Set.setStatus(
        "current"
    )

dpsRTUv2p10271Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10271)
)
dpsRTUv2p10271Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10271Set.setStatus(
        "current"
    )

dpsRTUv2p10272Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10272)
)
dpsRTUv2p10272Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10272Set.setStatus(
        "current"
    )

dpsRTUv2p10273Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10273)
)
dpsRTUv2p10273Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10273Set.setStatus(
        "current"
    )

dpsRTUv2p10274Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10274)
)
dpsRTUv2p10274Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10274Set.setStatus(
        "current"
    )

dpsRTUv2p10275Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10275)
)
dpsRTUv2p10275Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10275Set.setStatus(
        "current"
    )

dpsRTUv2p10276Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10276)
)
dpsRTUv2p10276Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10276Set.setStatus(
        "current"
    )

dpsRTUv2p10277Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10277)
)
dpsRTUv2p10277Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10277Set.setStatus(
        "current"
    )

dpsRTUv2p10278Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10278)
)
dpsRTUv2p10278Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10278Set.setStatus(
        "current"
    )

dpsRTUv2p10279Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10279)
)
dpsRTUv2p10279Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10279Set.setStatus(
        "current"
    )

dpsRTUv2p10280Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10280)
)
dpsRTUv2p10280Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10280Set.setStatus(
        "current"
    )

dpsRTUv2p10281Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10281)
)
dpsRTUv2p10281Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10281Set.setStatus(
        "current"
    )

dpsRTUv2p10282Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10282)
)
dpsRTUv2p10282Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10282Set.setStatus(
        "current"
    )

dpsRTUv2p10283Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10283)
)
dpsRTUv2p10283Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10283Set.setStatus(
        "current"
    )

dpsRTUv2p10284Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10284)
)
dpsRTUv2p10284Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10284Set.setStatus(
        "current"
    )

dpsRTUv2p10285Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10285)
)
dpsRTUv2p10285Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10285Set.setStatus(
        "current"
    )

dpsRTUv2p10286Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10286)
)
dpsRTUv2p10286Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10286Set.setStatus(
        "current"
    )

dpsRTUv2p10287Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10287)
)
dpsRTUv2p10287Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10287Set.setStatus(
        "current"
    )

dpsRTUv2p10288Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10288)
)
dpsRTUv2p10288Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10288Set.setStatus(
        "current"
    )

dpsRTUv2p10289Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10289)
)
dpsRTUv2p10289Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10289Set.setStatus(
        "current"
    )

dpsRTUv2p10290Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10290)
)
dpsRTUv2p10290Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10290Set.setStatus(
        "current"
    )

dpsRTUv2p10291Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10291)
)
dpsRTUv2p10291Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10291Set.setStatus(
        "current"
    )

dpsRTUv2p10292Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10292)
)
dpsRTUv2p10292Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10292Set.setStatus(
        "current"
    )

dpsRTUv2p10293Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10293)
)
dpsRTUv2p10293Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10293Set.setStatus(
        "current"
    )

dpsRTUv2p10294Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10294)
)
dpsRTUv2p10294Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10294Set.setStatus(
        "current"
    )

dpsRTUv2p10295Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10295)
)
dpsRTUv2p10295Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10295Set.setStatus(
        "current"
    )

dpsRTUv2p10296Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10296)
)
dpsRTUv2p10296Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10296Set.setStatus(
        "current"
    )

dpsRTUv2p10297Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10297)
)
dpsRTUv2p10297Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10297Set.setStatus(
        "current"
    )

dpsRTUv2p10298Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10298)
)
dpsRTUv2p10298Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10298Set.setStatus(
        "current"
    )

dpsRTUv2p10299Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10299)
)
dpsRTUv2p10299Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10299Set.setStatus(
        "current"
    )

dpsRTUv2p10300Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10300)
)
dpsRTUv2p10300Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10300Set.setStatus(
        "current"
    )

dpsRTUv2p10301Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10301)
)
dpsRTUv2p10301Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10301Set.setStatus(
        "current"
    )

dpsRTUv2p10302Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10302)
)
dpsRTUv2p10302Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10302Set.setStatus(
        "current"
    )

dpsRTUv2p10303Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10303)
)
dpsRTUv2p10303Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10303Set.setStatus(
        "current"
    )

dpsRTUv2p10304Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10304)
)
dpsRTUv2p10304Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10304Set.setStatus(
        "current"
    )

dpsRTUv2p10305Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10305)
)
dpsRTUv2p10305Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10305Set.setStatus(
        "current"
    )

dpsRTUv2p10306Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10306)
)
dpsRTUv2p10306Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10306Set.setStatus(
        "current"
    )

dpsRTUv2p10307Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10307)
)
dpsRTUv2p10307Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10307Set.setStatus(
        "current"
    )

dpsRTUv2p10308Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10308)
)
dpsRTUv2p10308Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10308Set.setStatus(
        "current"
    )

dpsRTUv2p10309Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10309)
)
dpsRTUv2p10309Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10309Set.setStatus(
        "current"
    )

dpsRTUv2p10310Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10310)
)
dpsRTUv2p10310Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10310Set.setStatus(
        "current"
    )

dpsRTUv2p10311Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10311)
)
dpsRTUv2p10311Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10311Set.setStatus(
        "current"
    )

dpsRTUv2p10312Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10312)
)
dpsRTUv2p10312Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10312Set.setStatus(
        "current"
    )

dpsRTUv2p10313Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10313)
)
dpsRTUv2p10313Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10313Set.setStatus(
        "current"
    )

dpsRTUv2p10314Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10314)
)
dpsRTUv2p10314Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10314Set.setStatus(
        "current"
    )

dpsRTUv2p10315Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10315)
)
dpsRTUv2p10315Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10315Set.setStatus(
        "current"
    )

dpsRTUv2p10316Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10316)
)
dpsRTUv2p10316Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10316Set.setStatus(
        "current"
    )

dpsRTUv2p10317Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10317)
)
dpsRTUv2p10317Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10317Set.setStatus(
        "current"
    )

dpsRTUv2p10318Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10318)
)
dpsRTUv2p10318Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10318Set.setStatus(
        "current"
    )

dpsRTUv2p10319Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10319)
)
dpsRTUv2p10319Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10319Set.setStatus(
        "current"
    )

dpsRTUv2p10320Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 10320)
)
dpsRTUv2p10320Set.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p10320Set.setStatus(
        "current"
    )

dpsRTUv2p11001Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11001)
)
dpsRTUv2p11001Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11001Clr.setStatus(
        "current"
    )

dpsRTUv2p11002Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11002)
)
dpsRTUv2p11002Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11002Clr.setStatus(
        "current"
    )

dpsRTUv2p11003Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11003)
)
dpsRTUv2p11003Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11003Clr.setStatus(
        "current"
    )

dpsRTUv2p11004Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11004)
)
dpsRTUv2p11004Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11004Clr.setStatus(
        "current"
    )

dpsRTUv2p11005Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11005)
)
dpsRTUv2p11005Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11005Clr.setStatus(
        "current"
    )

dpsRTUv2p11006Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11006)
)
dpsRTUv2p11006Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11006Clr.setStatus(
        "current"
    )

dpsRTUv2p11007Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11007)
)
dpsRTUv2p11007Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11007Clr.setStatus(
        "current"
    )

dpsRTUv2p11008Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11008)
)
dpsRTUv2p11008Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11008Clr.setStatus(
        "current"
    )

dpsRTUv2p11009Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11009)
)
dpsRTUv2p11009Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11009Clr.setStatus(
        "current"
    )

dpsRTUv2p11010Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11010)
)
dpsRTUv2p11010Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11010Clr.setStatus(
        "current"
    )

dpsRTUv2p11011Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11011)
)
dpsRTUv2p11011Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11011Clr.setStatus(
        "current"
    )

dpsRTUv2p11012Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11012)
)
dpsRTUv2p11012Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11012Clr.setStatus(
        "current"
    )

dpsRTUv2p11013Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11013)
)
dpsRTUv2p11013Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11013Clr.setStatus(
        "current"
    )

dpsRTUv2p11014Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11014)
)
dpsRTUv2p11014Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11014Clr.setStatus(
        "current"
    )

dpsRTUv2p11015Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11015)
)
dpsRTUv2p11015Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11015Clr.setStatus(
        "current"
    )

dpsRTUv2p11016Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11016)
)
dpsRTUv2p11016Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11016Clr.setStatus(
        "current"
    )

dpsRTUv2p11017Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11017)
)
dpsRTUv2p11017Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11017Clr.setStatus(
        "current"
    )

dpsRTUv2p11018Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11018)
)
dpsRTUv2p11018Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11018Clr.setStatus(
        "current"
    )

dpsRTUv2p11019Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11019)
)
dpsRTUv2p11019Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11019Clr.setStatus(
        "current"
    )

dpsRTUv2p11020Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11020)
)
dpsRTUv2p11020Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11020Clr.setStatus(
        "current"
    )

dpsRTUv2p11021Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11021)
)
dpsRTUv2p11021Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11021Clr.setStatus(
        "current"
    )

dpsRTUv2p11022Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11022)
)
dpsRTUv2p11022Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11022Clr.setStatus(
        "current"
    )

dpsRTUv2p11023Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11023)
)
dpsRTUv2p11023Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11023Clr.setStatus(
        "current"
    )

dpsRTUv2p11024Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11024)
)
dpsRTUv2p11024Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11024Clr.setStatus(
        "current"
    )

dpsRTUv2p11025Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11025)
)
dpsRTUv2p11025Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11025Clr.setStatus(
        "current"
    )

dpsRTUv2p11026Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11026)
)
dpsRTUv2p11026Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11026Clr.setStatus(
        "current"
    )

dpsRTUv2p11027Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11027)
)
dpsRTUv2p11027Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11027Clr.setStatus(
        "current"
    )

dpsRTUv2p11028Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11028)
)
dpsRTUv2p11028Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11028Clr.setStatus(
        "current"
    )

dpsRTUv2p11029Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11029)
)
dpsRTUv2p11029Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11029Clr.setStatus(
        "current"
    )

dpsRTUv2p11030Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11030)
)
dpsRTUv2p11030Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11030Clr.setStatus(
        "current"
    )

dpsRTUv2p11031Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11031)
)
dpsRTUv2p11031Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11031Clr.setStatus(
        "current"
    )

dpsRTUv2p11032Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11032)
)
dpsRTUv2p11032Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11032Clr.setStatus(
        "current"
    )

dpsRTUv2p11033Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11033)
)
dpsRTUv2p11033Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11033Clr.setStatus(
        "current"
    )

dpsRTUv2p11034Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11034)
)
dpsRTUv2p11034Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11034Clr.setStatus(
        "current"
    )

dpsRTUv2p11035Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11035)
)
dpsRTUv2p11035Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11035Clr.setStatus(
        "current"
    )

dpsRTUv2p11036Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11036)
)
dpsRTUv2p11036Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11036Clr.setStatus(
        "current"
    )

dpsRTUv2p11037Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11037)
)
dpsRTUv2p11037Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11037Clr.setStatus(
        "current"
    )

dpsRTUv2p11038Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11038)
)
dpsRTUv2p11038Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11038Clr.setStatus(
        "current"
    )

dpsRTUv2p11039Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11039)
)
dpsRTUv2p11039Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11039Clr.setStatus(
        "current"
    )

dpsRTUv2p11040Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11040)
)
dpsRTUv2p11040Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11040Clr.setStatus(
        "current"
    )

dpsRTUv2p11041Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11041)
)
dpsRTUv2p11041Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11041Clr.setStatus(
        "current"
    )

dpsRTUv2p11042Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11042)
)
dpsRTUv2p11042Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11042Clr.setStatus(
        "current"
    )

dpsRTUv2p11043Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11043)
)
dpsRTUv2p11043Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11043Clr.setStatus(
        "current"
    )

dpsRTUv2p11044Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11044)
)
dpsRTUv2p11044Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11044Clr.setStatus(
        "current"
    )

dpsRTUv2p11045Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11045)
)
dpsRTUv2p11045Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11045Clr.setStatus(
        "current"
    )

dpsRTUv2p11046Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11046)
)
dpsRTUv2p11046Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11046Clr.setStatus(
        "current"
    )

dpsRTUv2p11047Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11047)
)
dpsRTUv2p11047Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11047Clr.setStatus(
        "current"
    )

dpsRTUv2p11048Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11048)
)
dpsRTUv2p11048Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11048Clr.setStatus(
        "current"
    )

dpsRTUv2p11049Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11049)
)
dpsRTUv2p11049Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11049Clr.setStatus(
        "current"
    )

dpsRTUv2p11050Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11050)
)
dpsRTUv2p11050Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11050Clr.setStatus(
        "current"
    )

dpsRTUv2p11051Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11051)
)
dpsRTUv2p11051Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11051Clr.setStatus(
        "current"
    )

dpsRTUv2p11052Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11052)
)
dpsRTUv2p11052Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11052Clr.setStatus(
        "current"
    )

dpsRTUv2p11053Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11053)
)
dpsRTUv2p11053Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11053Clr.setStatus(
        "current"
    )

dpsRTUv2p11054Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11054)
)
dpsRTUv2p11054Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11054Clr.setStatus(
        "current"
    )

dpsRTUv2p11055Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11055)
)
dpsRTUv2p11055Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11055Clr.setStatus(
        "current"
    )

dpsRTUv2p11056Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11056)
)
dpsRTUv2p11056Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11056Clr.setStatus(
        "current"
    )

dpsRTUv2p11057Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11057)
)
dpsRTUv2p11057Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11057Clr.setStatus(
        "current"
    )

dpsRTUv2p11058Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11058)
)
dpsRTUv2p11058Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11058Clr.setStatus(
        "current"
    )

dpsRTUv2p11059Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11059)
)
dpsRTUv2p11059Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11059Clr.setStatus(
        "current"
    )

dpsRTUv2p11060Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11060)
)
dpsRTUv2p11060Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11060Clr.setStatus(
        "current"
    )

dpsRTUv2p11061Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11061)
)
dpsRTUv2p11061Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11061Clr.setStatus(
        "current"
    )

dpsRTUv2p11062Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11062)
)
dpsRTUv2p11062Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11062Clr.setStatus(
        "current"
    )

dpsRTUv2p11063Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11063)
)
dpsRTUv2p11063Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11063Clr.setStatus(
        "current"
    )

dpsRTUv2p11064Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11064)
)
dpsRTUv2p11064Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11064Clr.setStatus(
        "current"
    )

dpsRTUv2p11065Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11065)
)
dpsRTUv2p11065Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11065Clr.setStatus(
        "current"
    )

dpsRTUv2p11066Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11066)
)
dpsRTUv2p11066Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11066Clr.setStatus(
        "current"
    )

dpsRTUv2p11067Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11067)
)
dpsRTUv2p11067Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11067Clr.setStatus(
        "current"
    )

dpsRTUv2p11068Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11068)
)
dpsRTUv2p11068Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11068Clr.setStatus(
        "current"
    )

dpsRTUv2p11069Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11069)
)
dpsRTUv2p11069Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11069Clr.setStatus(
        "current"
    )

dpsRTUv2p11070Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11070)
)
dpsRTUv2p11070Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11070Clr.setStatus(
        "current"
    )

dpsRTUv2p11071Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11071)
)
dpsRTUv2p11071Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11071Clr.setStatus(
        "current"
    )

dpsRTUv2p11072Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11072)
)
dpsRTUv2p11072Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11072Clr.setStatus(
        "current"
    )

dpsRTUv2p11073Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11073)
)
dpsRTUv2p11073Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11073Clr.setStatus(
        "current"
    )

dpsRTUv2p11074Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11074)
)
dpsRTUv2p11074Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11074Clr.setStatus(
        "current"
    )

dpsRTUv2p11075Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11075)
)
dpsRTUv2p11075Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11075Clr.setStatus(
        "current"
    )

dpsRTUv2p11076Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11076)
)
dpsRTUv2p11076Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11076Clr.setStatus(
        "current"
    )

dpsRTUv2p11077Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11077)
)
dpsRTUv2p11077Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11077Clr.setStatus(
        "current"
    )

dpsRTUv2p11078Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11078)
)
dpsRTUv2p11078Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11078Clr.setStatus(
        "current"
    )

dpsRTUv2p11079Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11079)
)
dpsRTUv2p11079Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11079Clr.setStatus(
        "current"
    )

dpsRTUv2p11080Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11080)
)
dpsRTUv2p11080Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11080Clr.setStatus(
        "current"
    )

dpsRTUv2p11081Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11081)
)
dpsRTUv2p11081Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11081Clr.setStatus(
        "current"
    )

dpsRTUv2p11082Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11082)
)
dpsRTUv2p11082Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11082Clr.setStatus(
        "current"
    )

dpsRTUv2p11083Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11083)
)
dpsRTUv2p11083Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11083Clr.setStatus(
        "current"
    )

dpsRTUv2p11084Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11084)
)
dpsRTUv2p11084Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11084Clr.setStatus(
        "current"
    )

dpsRTUv2p11085Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11085)
)
dpsRTUv2p11085Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11085Clr.setStatus(
        "current"
    )

dpsRTUv2p11086Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11086)
)
dpsRTUv2p11086Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11086Clr.setStatus(
        "current"
    )

dpsRTUv2p11087Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11087)
)
dpsRTUv2p11087Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11087Clr.setStatus(
        "current"
    )

dpsRTUv2p11088Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11088)
)
dpsRTUv2p11088Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11088Clr.setStatus(
        "current"
    )

dpsRTUv2p11089Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11089)
)
dpsRTUv2p11089Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11089Clr.setStatus(
        "current"
    )

dpsRTUv2p11090Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11090)
)
dpsRTUv2p11090Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11090Clr.setStatus(
        "current"
    )

dpsRTUv2p11091Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11091)
)
dpsRTUv2p11091Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11091Clr.setStatus(
        "current"
    )

dpsRTUv2p11092Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11092)
)
dpsRTUv2p11092Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11092Clr.setStatus(
        "current"
    )

dpsRTUv2p11093Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11093)
)
dpsRTUv2p11093Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11093Clr.setStatus(
        "current"
    )

dpsRTUv2p11094Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11094)
)
dpsRTUv2p11094Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11094Clr.setStatus(
        "current"
    )

dpsRTUv2p11095Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11095)
)
dpsRTUv2p11095Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11095Clr.setStatus(
        "current"
    )

dpsRTUv2p11096Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11096)
)
dpsRTUv2p11096Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11096Clr.setStatus(
        "current"
    )

dpsRTUv2p11097Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11097)
)
dpsRTUv2p11097Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11097Clr.setStatus(
        "current"
    )

dpsRTUv2p11098Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11098)
)
dpsRTUv2p11098Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11098Clr.setStatus(
        "current"
    )

dpsRTUv2p11099Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11099)
)
dpsRTUv2p11099Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11099Clr.setStatus(
        "current"
    )

dpsRTUv2p11100Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11100)
)
dpsRTUv2p11100Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11100Clr.setStatus(
        "current"
    )

dpsRTUv2p11101Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11101)
)
dpsRTUv2p11101Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11101Clr.setStatus(
        "current"
    )

dpsRTUv2p11102Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11102)
)
dpsRTUv2p11102Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11102Clr.setStatus(
        "current"
    )

dpsRTUv2p11103Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11103)
)
dpsRTUv2p11103Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11103Clr.setStatus(
        "current"
    )

dpsRTUv2p11104Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11104)
)
dpsRTUv2p11104Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11104Clr.setStatus(
        "current"
    )

dpsRTUv2p11105Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11105)
)
dpsRTUv2p11105Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11105Clr.setStatus(
        "current"
    )

dpsRTUv2p11106Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11106)
)
dpsRTUv2p11106Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11106Clr.setStatus(
        "current"
    )

dpsRTUv2p11107Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11107)
)
dpsRTUv2p11107Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11107Clr.setStatus(
        "current"
    )

dpsRTUv2p11108Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11108)
)
dpsRTUv2p11108Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11108Clr.setStatus(
        "current"
    )

dpsRTUv2p11109Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11109)
)
dpsRTUv2p11109Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11109Clr.setStatus(
        "current"
    )

dpsRTUv2p11110Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11110)
)
dpsRTUv2p11110Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11110Clr.setStatus(
        "current"
    )

dpsRTUv2p11111Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11111)
)
dpsRTUv2p11111Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11111Clr.setStatus(
        "current"
    )

dpsRTUv2p11112Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11112)
)
dpsRTUv2p11112Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11112Clr.setStatus(
        "current"
    )

dpsRTUv2p11113Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11113)
)
dpsRTUv2p11113Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11113Clr.setStatus(
        "current"
    )

dpsRTUv2p11114Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11114)
)
dpsRTUv2p11114Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11114Clr.setStatus(
        "current"
    )

dpsRTUv2p11115Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11115)
)
dpsRTUv2p11115Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11115Clr.setStatus(
        "current"
    )

dpsRTUv2p11116Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11116)
)
dpsRTUv2p11116Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11116Clr.setStatus(
        "current"
    )

dpsRTUv2p11117Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11117)
)
dpsRTUv2p11117Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11117Clr.setStatus(
        "current"
    )

dpsRTUv2p11118Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11118)
)
dpsRTUv2p11118Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11118Clr.setStatus(
        "current"
    )

dpsRTUv2p11119Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11119)
)
dpsRTUv2p11119Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11119Clr.setStatus(
        "current"
    )

dpsRTUv2p11120Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11120)
)
dpsRTUv2p11120Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11120Clr.setStatus(
        "current"
    )

dpsRTUv2p11121Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11121)
)
dpsRTUv2p11121Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11121Clr.setStatus(
        "current"
    )

dpsRTUv2p11122Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11122)
)
dpsRTUv2p11122Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11122Clr.setStatus(
        "current"
    )

dpsRTUv2p11123Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11123)
)
dpsRTUv2p11123Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11123Clr.setStatus(
        "current"
    )

dpsRTUv2p11124Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11124)
)
dpsRTUv2p11124Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11124Clr.setStatus(
        "current"
    )

dpsRTUv2p11125Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11125)
)
dpsRTUv2p11125Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11125Clr.setStatus(
        "current"
    )

dpsRTUv2p11126Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11126)
)
dpsRTUv2p11126Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11126Clr.setStatus(
        "current"
    )

dpsRTUv2p11127Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11127)
)
dpsRTUv2p11127Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11127Clr.setStatus(
        "current"
    )

dpsRTUv2p11128Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11128)
)
dpsRTUv2p11128Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11128Clr.setStatus(
        "current"
    )

dpsRTUv2p11129Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11129)
)
dpsRTUv2p11129Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11129Clr.setStatus(
        "current"
    )

dpsRTUv2p11130Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11130)
)
dpsRTUv2p11130Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11130Clr.setStatus(
        "current"
    )

dpsRTUv2p11131Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11131)
)
dpsRTUv2p11131Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11131Clr.setStatus(
        "current"
    )

dpsRTUv2p11132Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11132)
)
dpsRTUv2p11132Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11132Clr.setStatus(
        "current"
    )

dpsRTUv2p11133Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11133)
)
dpsRTUv2p11133Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11133Clr.setStatus(
        "current"
    )

dpsRTUv2p11134Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11134)
)
dpsRTUv2p11134Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11134Clr.setStatus(
        "current"
    )

dpsRTUv2p11135Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11135)
)
dpsRTUv2p11135Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11135Clr.setStatus(
        "current"
    )

dpsRTUv2p11136Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11136)
)
dpsRTUv2p11136Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11136Clr.setStatus(
        "current"
    )

dpsRTUv2p11137Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11137)
)
dpsRTUv2p11137Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11137Clr.setStatus(
        "current"
    )

dpsRTUv2p11138Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11138)
)
dpsRTUv2p11138Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11138Clr.setStatus(
        "current"
    )

dpsRTUv2p11139Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11139)
)
dpsRTUv2p11139Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11139Clr.setStatus(
        "current"
    )

dpsRTUv2p11140Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11140)
)
dpsRTUv2p11140Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11140Clr.setStatus(
        "current"
    )

dpsRTUv2p11141Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11141)
)
dpsRTUv2p11141Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11141Clr.setStatus(
        "current"
    )

dpsRTUv2p11142Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11142)
)
dpsRTUv2p11142Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11142Clr.setStatus(
        "current"
    )

dpsRTUv2p11143Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11143)
)
dpsRTUv2p11143Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11143Clr.setStatus(
        "current"
    )

dpsRTUv2p11144Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11144)
)
dpsRTUv2p11144Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11144Clr.setStatus(
        "current"
    )

dpsRTUv2p11145Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11145)
)
dpsRTUv2p11145Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11145Clr.setStatus(
        "current"
    )

dpsRTUv2p11146Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11146)
)
dpsRTUv2p11146Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11146Clr.setStatus(
        "current"
    )

dpsRTUv2p11147Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11147)
)
dpsRTUv2p11147Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11147Clr.setStatus(
        "current"
    )

dpsRTUv2p11148Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11148)
)
dpsRTUv2p11148Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11148Clr.setStatus(
        "current"
    )

dpsRTUv2p11149Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11149)
)
dpsRTUv2p11149Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11149Clr.setStatus(
        "current"
    )

dpsRTUv2p11150Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11150)
)
dpsRTUv2p11150Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11150Clr.setStatus(
        "current"
    )

dpsRTUv2p11151Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11151)
)
dpsRTUv2p11151Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11151Clr.setStatus(
        "current"
    )

dpsRTUv2p11152Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11152)
)
dpsRTUv2p11152Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11152Clr.setStatus(
        "current"
    )

dpsRTUv2p11153Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11153)
)
dpsRTUv2p11153Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11153Clr.setStatus(
        "current"
    )

dpsRTUv2p11154Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11154)
)
dpsRTUv2p11154Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11154Clr.setStatus(
        "current"
    )

dpsRTUv2p11155Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11155)
)
dpsRTUv2p11155Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11155Clr.setStatus(
        "current"
    )

dpsRTUv2p11156Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11156)
)
dpsRTUv2p11156Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11156Clr.setStatus(
        "current"
    )

dpsRTUv2p11157Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11157)
)
dpsRTUv2p11157Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11157Clr.setStatus(
        "current"
    )

dpsRTUv2p11158Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11158)
)
dpsRTUv2p11158Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11158Clr.setStatus(
        "current"
    )

dpsRTUv2p11159Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11159)
)
dpsRTUv2p11159Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11159Clr.setStatus(
        "current"
    )

dpsRTUv2p11160Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11160)
)
dpsRTUv2p11160Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11160Clr.setStatus(
        "current"
    )

dpsRTUv2p11161Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11161)
)
dpsRTUv2p11161Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11161Clr.setStatus(
        "current"
    )

dpsRTUv2p11162Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11162)
)
dpsRTUv2p11162Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11162Clr.setStatus(
        "current"
    )

dpsRTUv2p11163Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11163)
)
dpsRTUv2p11163Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11163Clr.setStatus(
        "current"
    )

dpsRTUv2p11164Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11164)
)
dpsRTUv2p11164Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11164Clr.setStatus(
        "current"
    )

dpsRTUv2p11165Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11165)
)
dpsRTUv2p11165Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11165Clr.setStatus(
        "current"
    )

dpsRTUv2p11166Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11166)
)
dpsRTUv2p11166Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11166Clr.setStatus(
        "current"
    )

dpsRTUv2p11167Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11167)
)
dpsRTUv2p11167Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11167Clr.setStatus(
        "current"
    )

dpsRTUv2p11168Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11168)
)
dpsRTUv2p11168Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11168Clr.setStatus(
        "current"
    )

dpsRTUv2p11169Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11169)
)
dpsRTUv2p11169Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11169Clr.setStatus(
        "current"
    )

dpsRTUv2p11170Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11170)
)
dpsRTUv2p11170Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11170Clr.setStatus(
        "current"
    )

dpsRTUv2p11171Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11171)
)
dpsRTUv2p11171Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11171Clr.setStatus(
        "current"
    )

dpsRTUv2p11172Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11172)
)
dpsRTUv2p11172Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11172Clr.setStatus(
        "current"
    )

dpsRTUv2p11173Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11173)
)
dpsRTUv2p11173Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11173Clr.setStatus(
        "current"
    )

dpsRTUv2p11174Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11174)
)
dpsRTUv2p11174Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11174Clr.setStatus(
        "current"
    )

dpsRTUv2p11175Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11175)
)
dpsRTUv2p11175Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11175Clr.setStatus(
        "current"
    )

dpsRTUv2p11176Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11176)
)
dpsRTUv2p11176Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11176Clr.setStatus(
        "current"
    )

dpsRTUv2p11177Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11177)
)
dpsRTUv2p11177Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11177Clr.setStatus(
        "current"
    )

dpsRTUv2p11178Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11178)
)
dpsRTUv2p11178Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11178Clr.setStatus(
        "current"
    )

dpsRTUv2p11179Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11179)
)
dpsRTUv2p11179Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11179Clr.setStatus(
        "current"
    )

dpsRTUv2p11180Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11180)
)
dpsRTUv2p11180Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11180Clr.setStatus(
        "current"
    )

dpsRTUv2p11181Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11181)
)
dpsRTUv2p11181Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11181Clr.setStatus(
        "current"
    )

dpsRTUv2p11182Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11182)
)
dpsRTUv2p11182Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11182Clr.setStatus(
        "current"
    )

dpsRTUv2p11183Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11183)
)
dpsRTUv2p11183Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11183Clr.setStatus(
        "current"
    )

dpsRTUv2p11184Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11184)
)
dpsRTUv2p11184Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11184Clr.setStatus(
        "current"
    )

dpsRTUv2p11185Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11185)
)
dpsRTUv2p11185Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11185Clr.setStatus(
        "current"
    )

dpsRTUv2p11186Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11186)
)
dpsRTUv2p11186Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11186Clr.setStatus(
        "current"
    )

dpsRTUv2p11187Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11187)
)
dpsRTUv2p11187Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11187Clr.setStatus(
        "current"
    )

dpsRTUv2p11188Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11188)
)
dpsRTUv2p11188Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11188Clr.setStatus(
        "current"
    )

dpsRTUv2p11189Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11189)
)
dpsRTUv2p11189Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11189Clr.setStatus(
        "current"
    )

dpsRTUv2p11190Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11190)
)
dpsRTUv2p11190Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11190Clr.setStatus(
        "current"
    )

dpsRTUv2p11191Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11191)
)
dpsRTUv2p11191Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11191Clr.setStatus(
        "current"
    )

dpsRTUv2p11192Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11192)
)
dpsRTUv2p11192Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11192Clr.setStatus(
        "current"
    )

dpsRTUv2p11193Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11193)
)
dpsRTUv2p11193Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11193Clr.setStatus(
        "current"
    )

dpsRTUv2p11194Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11194)
)
dpsRTUv2p11194Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11194Clr.setStatus(
        "current"
    )

dpsRTUv2p11195Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11195)
)
dpsRTUv2p11195Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11195Clr.setStatus(
        "current"
    )

dpsRTUv2p11196Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11196)
)
dpsRTUv2p11196Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11196Clr.setStatus(
        "current"
    )

dpsRTUv2p11197Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11197)
)
dpsRTUv2p11197Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11197Clr.setStatus(
        "current"
    )

dpsRTUv2p11198Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11198)
)
dpsRTUv2p11198Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11198Clr.setStatus(
        "current"
    )

dpsRTUv2p11199Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11199)
)
dpsRTUv2p11199Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11199Clr.setStatus(
        "current"
    )

dpsRTUv2p11200Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11200)
)
dpsRTUv2p11200Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11200Clr.setStatus(
        "current"
    )

dpsRTUv2p11201Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11201)
)
dpsRTUv2p11201Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11201Clr.setStatus(
        "current"
    )

dpsRTUv2p11202Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11202)
)
dpsRTUv2p11202Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11202Clr.setStatus(
        "current"
    )

dpsRTUv2p11203Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11203)
)
dpsRTUv2p11203Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11203Clr.setStatus(
        "current"
    )

dpsRTUv2p11204Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11204)
)
dpsRTUv2p11204Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11204Clr.setStatus(
        "current"
    )

dpsRTUv2p11205Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11205)
)
dpsRTUv2p11205Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11205Clr.setStatus(
        "current"
    )

dpsRTUv2p11206Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11206)
)
dpsRTUv2p11206Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11206Clr.setStatus(
        "current"
    )

dpsRTUv2p11207Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11207)
)
dpsRTUv2p11207Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11207Clr.setStatus(
        "current"
    )

dpsRTUv2p11208Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11208)
)
dpsRTUv2p11208Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11208Clr.setStatus(
        "current"
    )

dpsRTUv2p11209Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11209)
)
dpsRTUv2p11209Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11209Clr.setStatus(
        "current"
    )

dpsRTUv2p11210Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11210)
)
dpsRTUv2p11210Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11210Clr.setStatus(
        "current"
    )

dpsRTUv2p11211Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11211)
)
dpsRTUv2p11211Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11211Clr.setStatus(
        "current"
    )

dpsRTUv2p11212Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11212)
)
dpsRTUv2p11212Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11212Clr.setStatus(
        "current"
    )

dpsRTUv2p11213Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11213)
)
dpsRTUv2p11213Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11213Clr.setStatus(
        "current"
    )

dpsRTUv2p11214Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11214)
)
dpsRTUv2p11214Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11214Clr.setStatus(
        "current"
    )

dpsRTUv2p11215Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11215)
)
dpsRTUv2p11215Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11215Clr.setStatus(
        "current"
    )

dpsRTUv2p11216Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11216)
)
dpsRTUv2p11216Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11216Clr.setStatus(
        "current"
    )

dpsRTUv2p11217Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11217)
)
dpsRTUv2p11217Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11217Clr.setStatus(
        "current"
    )

dpsRTUv2p11218Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11218)
)
dpsRTUv2p11218Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11218Clr.setStatus(
        "current"
    )

dpsRTUv2p11219Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11219)
)
dpsRTUv2p11219Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11219Clr.setStatus(
        "current"
    )

dpsRTUv2p11220Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11220)
)
dpsRTUv2p11220Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11220Clr.setStatus(
        "current"
    )

dpsRTUv2p11221Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11221)
)
dpsRTUv2p11221Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11221Clr.setStatus(
        "current"
    )

dpsRTUv2p11222Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11222)
)
dpsRTUv2p11222Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11222Clr.setStatus(
        "current"
    )

dpsRTUv2p11223Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11223)
)
dpsRTUv2p11223Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11223Clr.setStatus(
        "current"
    )

dpsRTUv2p11224Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11224)
)
dpsRTUv2p11224Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11224Clr.setStatus(
        "current"
    )

dpsRTUv2p11225Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11225)
)
dpsRTUv2p11225Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11225Clr.setStatus(
        "current"
    )

dpsRTUv2p11226Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11226)
)
dpsRTUv2p11226Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11226Clr.setStatus(
        "current"
    )

dpsRTUv2p11227Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11227)
)
dpsRTUv2p11227Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11227Clr.setStatus(
        "current"
    )

dpsRTUv2p11228Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11228)
)
dpsRTUv2p11228Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11228Clr.setStatus(
        "current"
    )

dpsRTUv2p11229Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11229)
)
dpsRTUv2p11229Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11229Clr.setStatus(
        "current"
    )

dpsRTUv2p11230Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11230)
)
dpsRTUv2p11230Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11230Clr.setStatus(
        "current"
    )

dpsRTUv2p11231Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11231)
)
dpsRTUv2p11231Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11231Clr.setStatus(
        "current"
    )

dpsRTUv2p11232Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11232)
)
dpsRTUv2p11232Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11232Clr.setStatus(
        "current"
    )

dpsRTUv2p11233Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11233)
)
dpsRTUv2p11233Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11233Clr.setStatus(
        "current"
    )

dpsRTUv2p11234Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11234)
)
dpsRTUv2p11234Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11234Clr.setStatus(
        "current"
    )

dpsRTUv2p11235Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11235)
)
dpsRTUv2p11235Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11235Clr.setStatus(
        "current"
    )

dpsRTUv2p11236Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11236)
)
dpsRTUv2p11236Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11236Clr.setStatus(
        "current"
    )

dpsRTUv2p11237Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11237)
)
dpsRTUv2p11237Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11237Clr.setStatus(
        "current"
    )

dpsRTUv2p11238Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11238)
)
dpsRTUv2p11238Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11238Clr.setStatus(
        "current"
    )

dpsRTUv2p11239Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11239)
)
dpsRTUv2p11239Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11239Clr.setStatus(
        "current"
    )

dpsRTUv2p11240Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11240)
)
dpsRTUv2p11240Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11240Clr.setStatus(
        "current"
    )

dpsRTUv2p11241Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11241)
)
dpsRTUv2p11241Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11241Clr.setStatus(
        "current"
    )

dpsRTUv2p11242Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11242)
)
dpsRTUv2p11242Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11242Clr.setStatus(
        "current"
    )

dpsRTUv2p11243Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11243)
)
dpsRTUv2p11243Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11243Clr.setStatus(
        "current"
    )

dpsRTUv2p11244Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11244)
)
dpsRTUv2p11244Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11244Clr.setStatus(
        "current"
    )

dpsRTUv2p11245Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11245)
)
dpsRTUv2p11245Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11245Clr.setStatus(
        "current"
    )

dpsRTUv2p11246Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11246)
)
dpsRTUv2p11246Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11246Clr.setStatus(
        "current"
    )

dpsRTUv2p11247Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11247)
)
dpsRTUv2p11247Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11247Clr.setStatus(
        "current"
    )

dpsRTUv2p11248Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11248)
)
dpsRTUv2p11248Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11248Clr.setStatus(
        "current"
    )

dpsRTUv2p11249Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11249)
)
dpsRTUv2p11249Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11249Clr.setStatus(
        "current"
    )

dpsRTUv2p11250Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11250)
)
dpsRTUv2p11250Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11250Clr.setStatus(
        "current"
    )

dpsRTUv2p11251Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11251)
)
dpsRTUv2p11251Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11251Clr.setStatus(
        "current"
    )

dpsRTUv2p11252Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11252)
)
dpsRTUv2p11252Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11252Clr.setStatus(
        "current"
    )

dpsRTUv2p11253Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11253)
)
dpsRTUv2p11253Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11253Clr.setStatus(
        "current"
    )

dpsRTUv2p11254Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11254)
)
dpsRTUv2p11254Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11254Clr.setStatus(
        "current"
    )

dpsRTUv2p11255Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11255)
)
dpsRTUv2p11255Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11255Clr.setStatus(
        "current"
    )

dpsRTUv2p11256Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11256)
)
dpsRTUv2p11256Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11256Clr.setStatus(
        "current"
    )

dpsRTUv2p11257Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11257)
)
dpsRTUv2p11257Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11257Clr.setStatus(
        "current"
    )

dpsRTUv2p11258Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11258)
)
dpsRTUv2p11258Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11258Clr.setStatus(
        "current"
    )

dpsRTUv2p11259Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11259)
)
dpsRTUv2p11259Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11259Clr.setStatus(
        "current"
    )

dpsRTUv2p11260Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11260)
)
dpsRTUv2p11260Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11260Clr.setStatus(
        "current"
    )

dpsRTUv2p11261Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11261)
)
dpsRTUv2p11261Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11261Clr.setStatus(
        "current"
    )

dpsRTUv2p11262Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11262)
)
dpsRTUv2p11262Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11262Clr.setStatus(
        "current"
    )

dpsRTUv2p11263Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11263)
)
dpsRTUv2p11263Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11263Clr.setStatus(
        "current"
    )

dpsRTUv2p11264Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11264)
)
dpsRTUv2p11264Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11264Clr.setStatus(
        "current"
    )

dpsRTUv2p11265Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11265)
)
dpsRTUv2p11265Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11265Clr.setStatus(
        "current"
    )

dpsRTUv2p11266Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11266)
)
dpsRTUv2p11266Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11266Clr.setStatus(
        "current"
    )

dpsRTUv2p11267Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11267)
)
dpsRTUv2p11267Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11267Clr.setStatus(
        "current"
    )

dpsRTUv2p11268Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11268)
)
dpsRTUv2p11268Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11268Clr.setStatus(
        "current"
    )

dpsRTUv2p11269Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11269)
)
dpsRTUv2p11269Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11269Clr.setStatus(
        "current"
    )

dpsRTUv2p11270Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11270)
)
dpsRTUv2p11270Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11270Clr.setStatus(
        "current"
    )

dpsRTUv2p11271Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11271)
)
dpsRTUv2p11271Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11271Clr.setStatus(
        "current"
    )

dpsRTUv2p11272Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11272)
)
dpsRTUv2p11272Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11272Clr.setStatus(
        "current"
    )

dpsRTUv2p11273Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11273)
)
dpsRTUv2p11273Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11273Clr.setStatus(
        "current"
    )

dpsRTUv2p11274Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11274)
)
dpsRTUv2p11274Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11274Clr.setStatus(
        "current"
    )

dpsRTUv2p11275Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11275)
)
dpsRTUv2p11275Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11275Clr.setStatus(
        "current"
    )

dpsRTUv2p11276Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11276)
)
dpsRTUv2p11276Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11276Clr.setStatus(
        "current"
    )

dpsRTUv2p11277Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11277)
)
dpsRTUv2p11277Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11277Clr.setStatus(
        "current"
    )

dpsRTUv2p11278Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11278)
)
dpsRTUv2p11278Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11278Clr.setStatus(
        "current"
    )

dpsRTUv2p11279Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11279)
)
dpsRTUv2p11279Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11279Clr.setStatus(
        "current"
    )

dpsRTUv2p11280Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11280)
)
dpsRTUv2p11280Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11280Clr.setStatus(
        "current"
    )

dpsRTUv2p11281Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11281)
)
dpsRTUv2p11281Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11281Clr.setStatus(
        "current"
    )

dpsRTUv2p11282Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11282)
)
dpsRTUv2p11282Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11282Clr.setStatus(
        "current"
    )

dpsRTUv2p11283Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11283)
)
dpsRTUv2p11283Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11283Clr.setStatus(
        "current"
    )

dpsRTUv2p11284Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11284)
)
dpsRTUv2p11284Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11284Clr.setStatus(
        "current"
    )

dpsRTUv2p11285Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11285)
)
dpsRTUv2p11285Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11285Clr.setStatus(
        "current"
    )

dpsRTUv2p11286Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11286)
)
dpsRTUv2p11286Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11286Clr.setStatus(
        "current"
    )

dpsRTUv2p11287Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11287)
)
dpsRTUv2p11287Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11287Clr.setStatus(
        "current"
    )

dpsRTUv2p11288Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11288)
)
dpsRTUv2p11288Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11288Clr.setStatus(
        "current"
    )

dpsRTUv2p11289Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11289)
)
dpsRTUv2p11289Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11289Clr.setStatus(
        "current"
    )

dpsRTUv2p11290Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11290)
)
dpsRTUv2p11290Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11290Clr.setStatus(
        "current"
    )

dpsRTUv2p11291Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11291)
)
dpsRTUv2p11291Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11291Clr.setStatus(
        "current"
    )

dpsRTUv2p11292Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11292)
)
dpsRTUv2p11292Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11292Clr.setStatus(
        "current"
    )

dpsRTUv2p11293Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11293)
)
dpsRTUv2p11293Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11293Clr.setStatus(
        "current"
    )

dpsRTUv2p11294Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11294)
)
dpsRTUv2p11294Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11294Clr.setStatus(
        "current"
    )

dpsRTUv2p11295Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11295)
)
dpsRTUv2p11295Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11295Clr.setStatus(
        "current"
    )

dpsRTUv2p11296Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11296)
)
dpsRTUv2p11296Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11296Clr.setStatus(
        "current"
    )

dpsRTUv2p11297Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11297)
)
dpsRTUv2p11297Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11297Clr.setStatus(
        "current"
    )

dpsRTUv2p11298Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11298)
)
dpsRTUv2p11298Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11298Clr.setStatus(
        "current"
    )

dpsRTUv2p11299Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11299)
)
dpsRTUv2p11299Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11299Clr.setStatus(
        "current"
    )

dpsRTUv2p11300Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11300)
)
dpsRTUv2p11300Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11300Clr.setStatus(
        "current"
    )

dpsRTUv2p11301Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11301)
)
dpsRTUv2p11301Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11301Clr.setStatus(
        "current"
    )

dpsRTUv2p11302Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11302)
)
dpsRTUv2p11302Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11302Clr.setStatus(
        "current"
    )

dpsRTUv2p11303Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11303)
)
dpsRTUv2p11303Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11303Clr.setStatus(
        "current"
    )

dpsRTUv2p11304Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11304)
)
dpsRTUv2p11304Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11304Clr.setStatus(
        "current"
    )

dpsRTUv2p11305Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11305)
)
dpsRTUv2p11305Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11305Clr.setStatus(
        "current"
    )

dpsRTUv2p11306Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11306)
)
dpsRTUv2p11306Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11306Clr.setStatus(
        "current"
    )

dpsRTUv2p11307Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11307)
)
dpsRTUv2p11307Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11307Clr.setStatus(
        "current"
    )

dpsRTUv2p11308Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11308)
)
dpsRTUv2p11308Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11308Clr.setStatus(
        "current"
    )

dpsRTUv2p11309Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11309)
)
dpsRTUv2p11309Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11309Clr.setStatus(
        "current"
    )

dpsRTUv2p11310Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11310)
)
dpsRTUv2p11310Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11310Clr.setStatus(
        "current"
    )

dpsRTUv2p11311Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11311)
)
dpsRTUv2p11311Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11311Clr.setStatus(
        "current"
    )

dpsRTUv2p11312Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11312)
)
dpsRTUv2p11312Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11312Clr.setStatus(
        "current"
    )

dpsRTUv2p11313Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11313)
)
dpsRTUv2p11313Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11313Clr.setStatus(
        "current"
    )

dpsRTUv2p11314Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11314)
)
dpsRTUv2p11314Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11314Clr.setStatus(
        "current"
    )

dpsRTUv2p11315Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11315)
)
dpsRTUv2p11315Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11315Clr.setStatus(
        "current"
    )

dpsRTUv2p11316Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11316)
)
dpsRTUv2p11316Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11316Clr.setStatus(
        "current"
    )

dpsRTUv2p11317Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11317)
)
dpsRTUv2p11317Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11317Clr.setStatus(
        "current"
    )

dpsRTUv2p11318Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11318)
)
dpsRTUv2p11318Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11318Clr.setStatus(
        "current"
    )

dpsRTUv2p11319Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11319)
)
dpsRTUv2p11319Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11319Clr.setStatus(
        "current"
    )

dpsRTUv2p11320Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 11320)
)
dpsRTUv2p11320Clr.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p11320Clr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-MIB-RTDX-G39-V2",
    **{"dpsRTUv2p10001Set": dpsRTUv2p10001Set,
       "dpsRTUv2p10002Set": dpsRTUv2p10002Set,
       "dpsRTUv2p10003Set": dpsRTUv2p10003Set,
       "dpsRTUv2p10004Set": dpsRTUv2p10004Set,
       "dpsRTUv2p10005Set": dpsRTUv2p10005Set,
       "dpsRTUv2p10006Set": dpsRTUv2p10006Set,
       "dpsRTUv2p10007Set": dpsRTUv2p10007Set,
       "dpsRTUv2p10008Set": dpsRTUv2p10008Set,
       "dpsRTUv2p10009Set": dpsRTUv2p10009Set,
       "dpsRTUv2p10010Set": dpsRTUv2p10010Set,
       "dpsRTUv2p10011Set": dpsRTUv2p10011Set,
       "dpsRTUv2p10012Set": dpsRTUv2p10012Set,
       "dpsRTUv2p10013Set": dpsRTUv2p10013Set,
       "dpsRTUv2p10014Set": dpsRTUv2p10014Set,
       "dpsRTUv2p10015Set": dpsRTUv2p10015Set,
       "dpsRTUv2p10016Set": dpsRTUv2p10016Set,
       "dpsRTUv2p10017Set": dpsRTUv2p10017Set,
       "dpsRTUv2p10018Set": dpsRTUv2p10018Set,
       "dpsRTUv2p10019Set": dpsRTUv2p10019Set,
       "dpsRTUv2p10020Set": dpsRTUv2p10020Set,
       "dpsRTUv2p10021Set": dpsRTUv2p10021Set,
       "dpsRTUv2p10022Set": dpsRTUv2p10022Set,
       "dpsRTUv2p10023Set": dpsRTUv2p10023Set,
       "dpsRTUv2p10024Set": dpsRTUv2p10024Set,
       "dpsRTUv2p10025Set": dpsRTUv2p10025Set,
       "dpsRTUv2p10026Set": dpsRTUv2p10026Set,
       "dpsRTUv2p10027Set": dpsRTUv2p10027Set,
       "dpsRTUv2p10028Set": dpsRTUv2p10028Set,
       "dpsRTUv2p10029Set": dpsRTUv2p10029Set,
       "dpsRTUv2p10030Set": dpsRTUv2p10030Set,
       "dpsRTUv2p10031Set": dpsRTUv2p10031Set,
       "dpsRTUv2p10032Set": dpsRTUv2p10032Set,
       "dpsRTUv2p10033Set": dpsRTUv2p10033Set,
       "dpsRTUv2p10034Set": dpsRTUv2p10034Set,
       "dpsRTUv2p10035Set": dpsRTUv2p10035Set,
       "dpsRTUv2p10036Set": dpsRTUv2p10036Set,
       "dpsRTUv2p10037Set": dpsRTUv2p10037Set,
       "dpsRTUv2p10038Set": dpsRTUv2p10038Set,
       "dpsRTUv2p10039Set": dpsRTUv2p10039Set,
       "dpsRTUv2p10040Set": dpsRTUv2p10040Set,
       "dpsRTUv2p10041Set": dpsRTUv2p10041Set,
       "dpsRTUv2p10042Set": dpsRTUv2p10042Set,
       "dpsRTUv2p10043Set": dpsRTUv2p10043Set,
       "dpsRTUv2p10044Set": dpsRTUv2p10044Set,
       "dpsRTUv2p10045Set": dpsRTUv2p10045Set,
       "dpsRTUv2p10046Set": dpsRTUv2p10046Set,
       "dpsRTUv2p10047Set": dpsRTUv2p10047Set,
       "dpsRTUv2p10048Set": dpsRTUv2p10048Set,
       "dpsRTUv2p10049Set": dpsRTUv2p10049Set,
       "dpsRTUv2p10050Set": dpsRTUv2p10050Set,
       "dpsRTUv2p10051Set": dpsRTUv2p10051Set,
       "dpsRTUv2p10052Set": dpsRTUv2p10052Set,
       "dpsRTUv2p10053Set": dpsRTUv2p10053Set,
       "dpsRTUv2p10054Set": dpsRTUv2p10054Set,
       "dpsRTUv2p10055Set": dpsRTUv2p10055Set,
       "dpsRTUv2p10056Set": dpsRTUv2p10056Set,
       "dpsRTUv2p10057Set": dpsRTUv2p10057Set,
       "dpsRTUv2p10058Set": dpsRTUv2p10058Set,
       "dpsRTUv2p10059Set": dpsRTUv2p10059Set,
       "dpsRTUv2p10060Set": dpsRTUv2p10060Set,
       "dpsRTUv2p10061Set": dpsRTUv2p10061Set,
       "dpsRTUv2p10062Set": dpsRTUv2p10062Set,
       "dpsRTUv2p10063Set": dpsRTUv2p10063Set,
       "dpsRTUv2p10064Set": dpsRTUv2p10064Set,
       "dpsRTUv2p10065Set": dpsRTUv2p10065Set,
       "dpsRTUv2p10066Set": dpsRTUv2p10066Set,
       "dpsRTUv2p10067Set": dpsRTUv2p10067Set,
       "dpsRTUv2p10068Set": dpsRTUv2p10068Set,
       "dpsRTUv2p10069Set": dpsRTUv2p10069Set,
       "dpsRTUv2p10070Set": dpsRTUv2p10070Set,
       "dpsRTUv2p10071Set": dpsRTUv2p10071Set,
       "dpsRTUv2p10072Set": dpsRTUv2p10072Set,
       "dpsRTUv2p10073Set": dpsRTUv2p10073Set,
       "dpsRTUv2p10074Set": dpsRTUv2p10074Set,
       "dpsRTUv2p10075Set": dpsRTUv2p10075Set,
       "dpsRTUv2p10076Set": dpsRTUv2p10076Set,
       "dpsRTUv2p10077Set": dpsRTUv2p10077Set,
       "dpsRTUv2p10078Set": dpsRTUv2p10078Set,
       "dpsRTUv2p10079Set": dpsRTUv2p10079Set,
       "dpsRTUv2p10080Set": dpsRTUv2p10080Set,
       "dpsRTUv2p10081Set": dpsRTUv2p10081Set,
       "dpsRTUv2p10082Set": dpsRTUv2p10082Set,
       "dpsRTUv2p10083Set": dpsRTUv2p10083Set,
       "dpsRTUv2p10084Set": dpsRTUv2p10084Set,
       "dpsRTUv2p10085Set": dpsRTUv2p10085Set,
       "dpsRTUv2p10086Set": dpsRTUv2p10086Set,
       "dpsRTUv2p10087Set": dpsRTUv2p10087Set,
       "dpsRTUv2p10088Set": dpsRTUv2p10088Set,
       "dpsRTUv2p10089Set": dpsRTUv2p10089Set,
       "dpsRTUv2p10090Set": dpsRTUv2p10090Set,
       "dpsRTUv2p10091Set": dpsRTUv2p10091Set,
       "dpsRTUv2p10092Set": dpsRTUv2p10092Set,
       "dpsRTUv2p10093Set": dpsRTUv2p10093Set,
       "dpsRTUv2p10094Set": dpsRTUv2p10094Set,
       "dpsRTUv2p10095Set": dpsRTUv2p10095Set,
       "dpsRTUv2p10096Set": dpsRTUv2p10096Set,
       "dpsRTUv2p10097Set": dpsRTUv2p10097Set,
       "dpsRTUv2p10098Set": dpsRTUv2p10098Set,
       "dpsRTUv2p10099Set": dpsRTUv2p10099Set,
       "dpsRTUv2p10100Set": dpsRTUv2p10100Set,
       "dpsRTUv2p10101Set": dpsRTUv2p10101Set,
       "dpsRTUv2p10102Set": dpsRTUv2p10102Set,
       "dpsRTUv2p10103Set": dpsRTUv2p10103Set,
       "dpsRTUv2p10104Set": dpsRTUv2p10104Set,
       "dpsRTUv2p10105Set": dpsRTUv2p10105Set,
       "dpsRTUv2p10106Set": dpsRTUv2p10106Set,
       "dpsRTUv2p10107Set": dpsRTUv2p10107Set,
       "dpsRTUv2p10108Set": dpsRTUv2p10108Set,
       "dpsRTUv2p10109Set": dpsRTUv2p10109Set,
       "dpsRTUv2p10110Set": dpsRTUv2p10110Set,
       "dpsRTUv2p10111Set": dpsRTUv2p10111Set,
       "dpsRTUv2p10112Set": dpsRTUv2p10112Set,
       "dpsRTUv2p10113Set": dpsRTUv2p10113Set,
       "dpsRTUv2p10114Set": dpsRTUv2p10114Set,
       "dpsRTUv2p10115Set": dpsRTUv2p10115Set,
       "dpsRTUv2p10116Set": dpsRTUv2p10116Set,
       "dpsRTUv2p10117Set": dpsRTUv2p10117Set,
       "dpsRTUv2p10118Set": dpsRTUv2p10118Set,
       "dpsRTUv2p10119Set": dpsRTUv2p10119Set,
       "dpsRTUv2p10120Set": dpsRTUv2p10120Set,
       "dpsRTUv2p10121Set": dpsRTUv2p10121Set,
       "dpsRTUv2p10122Set": dpsRTUv2p10122Set,
       "dpsRTUv2p10123Set": dpsRTUv2p10123Set,
       "dpsRTUv2p10124Set": dpsRTUv2p10124Set,
       "dpsRTUv2p10125Set": dpsRTUv2p10125Set,
       "dpsRTUv2p10126Set": dpsRTUv2p10126Set,
       "dpsRTUv2p10127Set": dpsRTUv2p10127Set,
       "dpsRTUv2p10128Set": dpsRTUv2p10128Set,
       "dpsRTUv2p10129Set": dpsRTUv2p10129Set,
       "dpsRTUv2p10130Set": dpsRTUv2p10130Set,
       "dpsRTUv2p10131Set": dpsRTUv2p10131Set,
       "dpsRTUv2p10132Set": dpsRTUv2p10132Set,
       "dpsRTUv2p10133Set": dpsRTUv2p10133Set,
       "dpsRTUv2p10134Set": dpsRTUv2p10134Set,
       "dpsRTUv2p10135Set": dpsRTUv2p10135Set,
       "dpsRTUv2p10136Set": dpsRTUv2p10136Set,
       "dpsRTUv2p10137Set": dpsRTUv2p10137Set,
       "dpsRTUv2p10138Set": dpsRTUv2p10138Set,
       "dpsRTUv2p10139Set": dpsRTUv2p10139Set,
       "dpsRTUv2p10140Set": dpsRTUv2p10140Set,
       "dpsRTUv2p10141Set": dpsRTUv2p10141Set,
       "dpsRTUv2p10142Set": dpsRTUv2p10142Set,
       "dpsRTUv2p10143Set": dpsRTUv2p10143Set,
       "dpsRTUv2p10144Set": dpsRTUv2p10144Set,
       "dpsRTUv2p10145Set": dpsRTUv2p10145Set,
       "dpsRTUv2p10146Set": dpsRTUv2p10146Set,
       "dpsRTUv2p10147Set": dpsRTUv2p10147Set,
       "dpsRTUv2p10148Set": dpsRTUv2p10148Set,
       "dpsRTUv2p10149Set": dpsRTUv2p10149Set,
       "dpsRTUv2p10150Set": dpsRTUv2p10150Set,
       "dpsRTUv2p10151Set": dpsRTUv2p10151Set,
       "dpsRTUv2p10152Set": dpsRTUv2p10152Set,
       "dpsRTUv2p10153Set": dpsRTUv2p10153Set,
       "dpsRTUv2p10154Set": dpsRTUv2p10154Set,
       "dpsRTUv2p10155Set": dpsRTUv2p10155Set,
       "dpsRTUv2p10156Set": dpsRTUv2p10156Set,
       "dpsRTUv2p10157Set": dpsRTUv2p10157Set,
       "dpsRTUv2p10158Set": dpsRTUv2p10158Set,
       "dpsRTUv2p10159Set": dpsRTUv2p10159Set,
       "dpsRTUv2p10160Set": dpsRTUv2p10160Set,
       "dpsRTUv2p10161Set": dpsRTUv2p10161Set,
       "dpsRTUv2p10162Set": dpsRTUv2p10162Set,
       "dpsRTUv2p10163Set": dpsRTUv2p10163Set,
       "dpsRTUv2p10164Set": dpsRTUv2p10164Set,
       "dpsRTUv2p10165Set": dpsRTUv2p10165Set,
       "dpsRTUv2p10166Set": dpsRTUv2p10166Set,
       "dpsRTUv2p10167Set": dpsRTUv2p10167Set,
       "dpsRTUv2p10168Set": dpsRTUv2p10168Set,
       "dpsRTUv2p10169Set": dpsRTUv2p10169Set,
       "dpsRTUv2p10170Set": dpsRTUv2p10170Set,
       "dpsRTUv2p10171Set": dpsRTUv2p10171Set,
       "dpsRTUv2p10172Set": dpsRTUv2p10172Set,
       "dpsRTUv2p10173Set": dpsRTUv2p10173Set,
       "dpsRTUv2p10174Set": dpsRTUv2p10174Set,
       "dpsRTUv2p10175Set": dpsRTUv2p10175Set,
       "dpsRTUv2p10176Set": dpsRTUv2p10176Set,
       "dpsRTUv2p10177Set": dpsRTUv2p10177Set,
       "dpsRTUv2p10178Set": dpsRTUv2p10178Set,
       "dpsRTUv2p10179Set": dpsRTUv2p10179Set,
       "dpsRTUv2p10180Set": dpsRTUv2p10180Set,
       "dpsRTUv2p10181Set": dpsRTUv2p10181Set,
       "dpsRTUv2p10182Set": dpsRTUv2p10182Set,
       "dpsRTUv2p10183Set": dpsRTUv2p10183Set,
       "dpsRTUv2p10184Set": dpsRTUv2p10184Set,
       "dpsRTUv2p10185Set": dpsRTUv2p10185Set,
       "dpsRTUv2p10186Set": dpsRTUv2p10186Set,
       "dpsRTUv2p10187Set": dpsRTUv2p10187Set,
       "dpsRTUv2p10188Set": dpsRTUv2p10188Set,
       "dpsRTUv2p10189Set": dpsRTUv2p10189Set,
       "dpsRTUv2p10190Set": dpsRTUv2p10190Set,
       "dpsRTUv2p10191Set": dpsRTUv2p10191Set,
       "dpsRTUv2p10192Set": dpsRTUv2p10192Set,
       "dpsRTUv2p10193Set": dpsRTUv2p10193Set,
       "dpsRTUv2p10194Set": dpsRTUv2p10194Set,
       "dpsRTUv2p10195Set": dpsRTUv2p10195Set,
       "dpsRTUv2p10196Set": dpsRTUv2p10196Set,
       "dpsRTUv2p10197Set": dpsRTUv2p10197Set,
       "dpsRTUv2p10198Set": dpsRTUv2p10198Set,
       "dpsRTUv2p10199Set": dpsRTUv2p10199Set,
       "dpsRTUv2p10200Set": dpsRTUv2p10200Set,
       "dpsRTUv2p10201Set": dpsRTUv2p10201Set,
       "dpsRTUv2p10202Set": dpsRTUv2p10202Set,
       "dpsRTUv2p10203Set": dpsRTUv2p10203Set,
       "dpsRTUv2p10204Set": dpsRTUv2p10204Set,
       "dpsRTUv2p10205Set": dpsRTUv2p10205Set,
       "dpsRTUv2p10206Set": dpsRTUv2p10206Set,
       "dpsRTUv2p10207Set": dpsRTUv2p10207Set,
       "dpsRTUv2p10208Set": dpsRTUv2p10208Set,
       "dpsRTUv2p10209Set": dpsRTUv2p10209Set,
       "dpsRTUv2p10210Set": dpsRTUv2p10210Set,
       "dpsRTUv2p10211Set": dpsRTUv2p10211Set,
       "dpsRTUv2p10212Set": dpsRTUv2p10212Set,
       "dpsRTUv2p10213Set": dpsRTUv2p10213Set,
       "dpsRTUv2p10214Set": dpsRTUv2p10214Set,
       "dpsRTUv2p10215Set": dpsRTUv2p10215Set,
       "dpsRTUv2p10216Set": dpsRTUv2p10216Set,
       "dpsRTUv2p10217Set": dpsRTUv2p10217Set,
       "dpsRTUv2p10218Set": dpsRTUv2p10218Set,
       "dpsRTUv2p10219Set": dpsRTUv2p10219Set,
       "dpsRTUv2p10220Set": dpsRTUv2p10220Set,
       "dpsRTUv2p10221Set": dpsRTUv2p10221Set,
       "dpsRTUv2p10222Set": dpsRTUv2p10222Set,
       "dpsRTUv2p10223Set": dpsRTUv2p10223Set,
       "dpsRTUv2p10224Set": dpsRTUv2p10224Set,
       "dpsRTUv2p10225Set": dpsRTUv2p10225Set,
       "dpsRTUv2p10226Set": dpsRTUv2p10226Set,
       "dpsRTUv2p10227Set": dpsRTUv2p10227Set,
       "dpsRTUv2p10228Set": dpsRTUv2p10228Set,
       "dpsRTUv2p10229Set": dpsRTUv2p10229Set,
       "dpsRTUv2p10230Set": dpsRTUv2p10230Set,
       "dpsRTUv2p10231Set": dpsRTUv2p10231Set,
       "dpsRTUv2p10232Set": dpsRTUv2p10232Set,
       "dpsRTUv2p10233Set": dpsRTUv2p10233Set,
       "dpsRTUv2p10234Set": dpsRTUv2p10234Set,
       "dpsRTUv2p10235Set": dpsRTUv2p10235Set,
       "dpsRTUv2p10236Set": dpsRTUv2p10236Set,
       "dpsRTUv2p10237Set": dpsRTUv2p10237Set,
       "dpsRTUv2p10238Set": dpsRTUv2p10238Set,
       "dpsRTUv2p10239Set": dpsRTUv2p10239Set,
       "dpsRTUv2p10240Set": dpsRTUv2p10240Set,
       "dpsRTUv2p10241Set": dpsRTUv2p10241Set,
       "dpsRTUv2p10242Set": dpsRTUv2p10242Set,
       "dpsRTUv2p10243Set": dpsRTUv2p10243Set,
       "dpsRTUv2p10244Set": dpsRTUv2p10244Set,
       "dpsRTUv2p10245Set": dpsRTUv2p10245Set,
       "dpsRTUv2p10246Set": dpsRTUv2p10246Set,
       "dpsRTUv2p10247Set": dpsRTUv2p10247Set,
       "dpsRTUv2p10248Set": dpsRTUv2p10248Set,
       "dpsRTUv2p10249Set": dpsRTUv2p10249Set,
       "dpsRTUv2p10250Set": dpsRTUv2p10250Set,
       "dpsRTUv2p10251Set": dpsRTUv2p10251Set,
       "dpsRTUv2p10252Set": dpsRTUv2p10252Set,
       "dpsRTUv2p10253Set": dpsRTUv2p10253Set,
       "dpsRTUv2p10254Set": dpsRTUv2p10254Set,
       "dpsRTUv2p10255Set": dpsRTUv2p10255Set,
       "dpsRTUv2p10256Set": dpsRTUv2p10256Set,
       "dpsRTUv2p10257Set": dpsRTUv2p10257Set,
       "dpsRTUv2p10258Set": dpsRTUv2p10258Set,
       "dpsRTUv2p10259Set": dpsRTUv2p10259Set,
       "dpsRTUv2p10260Set": dpsRTUv2p10260Set,
       "dpsRTUv2p10261Set": dpsRTUv2p10261Set,
       "dpsRTUv2p10262Set": dpsRTUv2p10262Set,
       "dpsRTUv2p10263Set": dpsRTUv2p10263Set,
       "dpsRTUv2p10264Set": dpsRTUv2p10264Set,
       "dpsRTUv2p10265Set": dpsRTUv2p10265Set,
       "dpsRTUv2p10266Set": dpsRTUv2p10266Set,
       "dpsRTUv2p10267Set": dpsRTUv2p10267Set,
       "dpsRTUv2p10268Set": dpsRTUv2p10268Set,
       "dpsRTUv2p10269Set": dpsRTUv2p10269Set,
       "dpsRTUv2p10270Set": dpsRTUv2p10270Set,
       "dpsRTUv2p10271Set": dpsRTUv2p10271Set,
       "dpsRTUv2p10272Set": dpsRTUv2p10272Set,
       "dpsRTUv2p10273Set": dpsRTUv2p10273Set,
       "dpsRTUv2p10274Set": dpsRTUv2p10274Set,
       "dpsRTUv2p10275Set": dpsRTUv2p10275Set,
       "dpsRTUv2p10276Set": dpsRTUv2p10276Set,
       "dpsRTUv2p10277Set": dpsRTUv2p10277Set,
       "dpsRTUv2p10278Set": dpsRTUv2p10278Set,
       "dpsRTUv2p10279Set": dpsRTUv2p10279Set,
       "dpsRTUv2p10280Set": dpsRTUv2p10280Set,
       "dpsRTUv2p10281Set": dpsRTUv2p10281Set,
       "dpsRTUv2p10282Set": dpsRTUv2p10282Set,
       "dpsRTUv2p10283Set": dpsRTUv2p10283Set,
       "dpsRTUv2p10284Set": dpsRTUv2p10284Set,
       "dpsRTUv2p10285Set": dpsRTUv2p10285Set,
       "dpsRTUv2p10286Set": dpsRTUv2p10286Set,
       "dpsRTUv2p10287Set": dpsRTUv2p10287Set,
       "dpsRTUv2p10288Set": dpsRTUv2p10288Set,
       "dpsRTUv2p10289Set": dpsRTUv2p10289Set,
       "dpsRTUv2p10290Set": dpsRTUv2p10290Set,
       "dpsRTUv2p10291Set": dpsRTUv2p10291Set,
       "dpsRTUv2p10292Set": dpsRTUv2p10292Set,
       "dpsRTUv2p10293Set": dpsRTUv2p10293Set,
       "dpsRTUv2p10294Set": dpsRTUv2p10294Set,
       "dpsRTUv2p10295Set": dpsRTUv2p10295Set,
       "dpsRTUv2p10296Set": dpsRTUv2p10296Set,
       "dpsRTUv2p10297Set": dpsRTUv2p10297Set,
       "dpsRTUv2p10298Set": dpsRTUv2p10298Set,
       "dpsRTUv2p10299Set": dpsRTUv2p10299Set,
       "dpsRTUv2p10300Set": dpsRTUv2p10300Set,
       "dpsRTUv2p10301Set": dpsRTUv2p10301Set,
       "dpsRTUv2p10302Set": dpsRTUv2p10302Set,
       "dpsRTUv2p10303Set": dpsRTUv2p10303Set,
       "dpsRTUv2p10304Set": dpsRTUv2p10304Set,
       "dpsRTUv2p10305Set": dpsRTUv2p10305Set,
       "dpsRTUv2p10306Set": dpsRTUv2p10306Set,
       "dpsRTUv2p10307Set": dpsRTUv2p10307Set,
       "dpsRTUv2p10308Set": dpsRTUv2p10308Set,
       "dpsRTUv2p10309Set": dpsRTUv2p10309Set,
       "dpsRTUv2p10310Set": dpsRTUv2p10310Set,
       "dpsRTUv2p10311Set": dpsRTUv2p10311Set,
       "dpsRTUv2p10312Set": dpsRTUv2p10312Set,
       "dpsRTUv2p10313Set": dpsRTUv2p10313Set,
       "dpsRTUv2p10314Set": dpsRTUv2p10314Set,
       "dpsRTUv2p10315Set": dpsRTUv2p10315Set,
       "dpsRTUv2p10316Set": dpsRTUv2p10316Set,
       "dpsRTUv2p10317Set": dpsRTUv2p10317Set,
       "dpsRTUv2p10318Set": dpsRTUv2p10318Set,
       "dpsRTUv2p10319Set": dpsRTUv2p10319Set,
       "dpsRTUv2p10320Set": dpsRTUv2p10320Set,
       "dpsRTUv2p11001Clr": dpsRTUv2p11001Clr,
       "dpsRTUv2p11002Clr": dpsRTUv2p11002Clr,
       "dpsRTUv2p11003Clr": dpsRTUv2p11003Clr,
       "dpsRTUv2p11004Clr": dpsRTUv2p11004Clr,
       "dpsRTUv2p11005Clr": dpsRTUv2p11005Clr,
       "dpsRTUv2p11006Clr": dpsRTUv2p11006Clr,
       "dpsRTUv2p11007Clr": dpsRTUv2p11007Clr,
       "dpsRTUv2p11008Clr": dpsRTUv2p11008Clr,
       "dpsRTUv2p11009Clr": dpsRTUv2p11009Clr,
       "dpsRTUv2p11010Clr": dpsRTUv2p11010Clr,
       "dpsRTUv2p11011Clr": dpsRTUv2p11011Clr,
       "dpsRTUv2p11012Clr": dpsRTUv2p11012Clr,
       "dpsRTUv2p11013Clr": dpsRTUv2p11013Clr,
       "dpsRTUv2p11014Clr": dpsRTUv2p11014Clr,
       "dpsRTUv2p11015Clr": dpsRTUv2p11015Clr,
       "dpsRTUv2p11016Clr": dpsRTUv2p11016Clr,
       "dpsRTUv2p11017Clr": dpsRTUv2p11017Clr,
       "dpsRTUv2p11018Clr": dpsRTUv2p11018Clr,
       "dpsRTUv2p11019Clr": dpsRTUv2p11019Clr,
       "dpsRTUv2p11020Clr": dpsRTUv2p11020Clr,
       "dpsRTUv2p11021Clr": dpsRTUv2p11021Clr,
       "dpsRTUv2p11022Clr": dpsRTUv2p11022Clr,
       "dpsRTUv2p11023Clr": dpsRTUv2p11023Clr,
       "dpsRTUv2p11024Clr": dpsRTUv2p11024Clr,
       "dpsRTUv2p11025Clr": dpsRTUv2p11025Clr,
       "dpsRTUv2p11026Clr": dpsRTUv2p11026Clr,
       "dpsRTUv2p11027Clr": dpsRTUv2p11027Clr,
       "dpsRTUv2p11028Clr": dpsRTUv2p11028Clr,
       "dpsRTUv2p11029Clr": dpsRTUv2p11029Clr,
       "dpsRTUv2p11030Clr": dpsRTUv2p11030Clr,
       "dpsRTUv2p11031Clr": dpsRTUv2p11031Clr,
       "dpsRTUv2p11032Clr": dpsRTUv2p11032Clr,
       "dpsRTUv2p11033Clr": dpsRTUv2p11033Clr,
       "dpsRTUv2p11034Clr": dpsRTUv2p11034Clr,
       "dpsRTUv2p11035Clr": dpsRTUv2p11035Clr,
       "dpsRTUv2p11036Clr": dpsRTUv2p11036Clr,
       "dpsRTUv2p11037Clr": dpsRTUv2p11037Clr,
       "dpsRTUv2p11038Clr": dpsRTUv2p11038Clr,
       "dpsRTUv2p11039Clr": dpsRTUv2p11039Clr,
       "dpsRTUv2p11040Clr": dpsRTUv2p11040Clr,
       "dpsRTUv2p11041Clr": dpsRTUv2p11041Clr,
       "dpsRTUv2p11042Clr": dpsRTUv2p11042Clr,
       "dpsRTUv2p11043Clr": dpsRTUv2p11043Clr,
       "dpsRTUv2p11044Clr": dpsRTUv2p11044Clr,
       "dpsRTUv2p11045Clr": dpsRTUv2p11045Clr,
       "dpsRTUv2p11046Clr": dpsRTUv2p11046Clr,
       "dpsRTUv2p11047Clr": dpsRTUv2p11047Clr,
       "dpsRTUv2p11048Clr": dpsRTUv2p11048Clr,
       "dpsRTUv2p11049Clr": dpsRTUv2p11049Clr,
       "dpsRTUv2p11050Clr": dpsRTUv2p11050Clr,
       "dpsRTUv2p11051Clr": dpsRTUv2p11051Clr,
       "dpsRTUv2p11052Clr": dpsRTUv2p11052Clr,
       "dpsRTUv2p11053Clr": dpsRTUv2p11053Clr,
       "dpsRTUv2p11054Clr": dpsRTUv2p11054Clr,
       "dpsRTUv2p11055Clr": dpsRTUv2p11055Clr,
       "dpsRTUv2p11056Clr": dpsRTUv2p11056Clr,
       "dpsRTUv2p11057Clr": dpsRTUv2p11057Clr,
       "dpsRTUv2p11058Clr": dpsRTUv2p11058Clr,
       "dpsRTUv2p11059Clr": dpsRTUv2p11059Clr,
       "dpsRTUv2p11060Clr": dpsRTUv2p11060Clr,
       "dpsRTUv2p11061Clr": dpsRTUv2p11061Clr,
       "dpsRTUv2p11062Clr": dpsRTUv2p11062Clr,
       "dpsRTUv2p11063Clr": dpsRTUv2p11063Clr,
       "dpsRTUv2p11064Clr": dpsRTUv2p11064Clr,
       "dpsRTUv2p11065Clr": dpsRTUv2p11065Clr,
       "dpsRTUv2p11066Clr": dpsRTUv2p11066Clr,
       "dpsRTUv2p11067Clr": dpsRTUv2p11067Clr,
       "dpsRTUv2p11068Clr": dpsRTUv2p11068Clr,
       "dpsRTUv2p11069Clr": dpsRTUv2p11069Clr,
       "dpsRTUv2p11070Clr": dpsRTUv2p11070Clr,
       "dpsRTUv2p11071Clr": dpsRTUv2p11071Clr,
       "dpsRTUv2p11072Clr": dpsRTUv2p11072Clr,
       "dpsRTUv2p11073Clr": dpsRTUv2p11073Clr,
       "dpsRTUv2p11074Clr": dpsRTUv2p11074Clr,
       "dpsRTUv2p11075Clr": dpsRTUv2p11075Clr,
       "dpsRTUv2p11076Clr": dpsRTUv2p11076Clr,
       "dpsRTUv2p11077Clr": dpsRTUv2p11077Clr,
       "dpsRTUv2p11078Clr": dpsRTUv2p11078Clr,
       "dpsRTUv2p11079Clr": dpsRTUv2p11079Clr,
       "dpsRTUv2p11080Clr": dpsRTUv2p11080Clr,
       "dpsRTUv2p11081Clr": dpsRTUv2p11081Clr,
       "dpsRTUv2p11082Clr": dpsRTUv2p11082Clr,
       "dpsRTUv2p11083Clr": dpsRTUv2p11083Clr,
       "dpsRTUv2p11084Clr": dpsRTUv2p11084Clr,
       "dpsRTUv2p11085Clr": dpsRTUv2p11085Clr,
       "dpsRTUv2p11086Clr": dpsRTUv2p11086Clr,
       "dpsRTUv2p11087Clr": dpsRTUv2p11087Clr,
       "dpsRTUv2p11088Clr": dpsRTUv2p11088Clr,
       "dpsRTUv2p11089Clr": dpsRTUv2p11089Clr,
       "dpsRTUv2p11090Clr": dpsRTUv2p11090Clr,
       "dpsRTUv2p11091Clr": dpsRTUv2p11091Clr,
       "dpsRTUv2p11092Clr": dpsRTUv2p11092Clr,
       "dpsRTUv2p11093Clr": dpsRTUv2p11093Clr,
       "dpsRTUv2p11094Clr": dpsRTUv2p11094Clr,
       "dpsRTUv2p11095Clr": dpsRTUv2p11095Clr,
       "dpsRTUv2p11096Clr": dpsRTUv2p11096Clr,
       "dpsRTUv2p11097Clr": dpsRTUv2p11097Clr,
       "dpsRTUv2p11098Clr": dpsRTUv2p11098Clr,
       "dpsRTUv2p11099Clr": dpsRTUv2p11099Clr,
       "dpsRTUv2p11100Clr": dpsRTUv2p11100Clr,
       "dpsRTUv2p11101Clr": dpsRTUv2p11101Clr,
       "dpsRTUv2p11102Clr": dpsRTUv2p11102Clr,
       "dpsRTUv2p11103Clr": dpsRTUv2p11103Clr,
       "dpsRTUv2p11104Clr": dpsRTUv2p11104Clr,
       "dpsRTUv2p11105Clr": dpsRTUv2p11105Clr,
       "dpsRTUv2p11106Clr": dpsRTUv2p11106Clr,
       "dpsRTUv2p11107Clr": dpsRTUv2p11107Clr,
       "dpsRTUv2p11108Clr": dpsRTUv2p11108Clr,
       "dpsRTUv2p11109Clr": dpsRTUv2p11109Clr,
       "dpsRTUv2p11110Clr": dpsRTUv2p11110Clr,
       "dpsRTUv2p11111Clr": dpsRTUv2p11111Clr,
       "dpsRTUv2p11112Clr": dpsRTUv2p11112Clr,
       "dpsRTUv2p11113Clr": dpsRTUv2p11113Clr,
       "dpsRTUv2p11114Clr": dpsRTUv2p11114Clr,
       "dpsRTUv2p11115Clr": dpsRTUv2p11115Clr,
       "dpsRTUv2p11116Clr": dpsRTUv2p11116Clr,
       "dpsRTUv2p11117Clr": dpsRTUv2p11117Clr,
       "dpsRTUv2p11118Clr": dpsRTUv2p11118Clr,
       "dpsRTUv2p11119Clr": dpsRTUv2p11119Clr,
       "dpsRTUv2p11120Clr": dpsRTUv2p11120Clr,
       "dpsRTUv2p11121Clr": dpsRTUv2p11121Clr,
       "dpsRTUv2p11122Clr": dpsRTUv2p11122Clr,
       "dpsRTUv2p11123Clr": dpsRTUv2p11123Clr,
       "dpsRTUv2p11124Clr": dpsRTUv2p11124Clr,
       "dpsRTUv2p11125Clr": dpsRTUv2p11125Clr,
       "dpsRTUv2p11126Clr": dpsRTUv2p11126Clr,
       "dpsRTUv2p11127Clr": dpsRTUv2p11127Clr,
       "dpsRTUv2p11128Clr": dpsRTUv2p11128Clr,
       "dpsRTUv2p11129Clr": dpsRTUv2p11129Clr,
       "dpsRTUv2p11130Clr": dpsRTUv2p11130Clr,
       "dpsRTUv2p11131Clr": dpsRTUv2p11131Clr,
       "dpsRTUv2p11132Clr": dpsRTUv2p11132Clr,
       "dpsRTUv2p11133Clr": dpsRTUv2p11133Clr,
       "dpsRTUv2p11134Clr": dpsRTUv2p11134Clr,
       "dpsRTUv2p11135Clr": dpsRTUv2p11135Clr,
       "dpsRTUv2p11136Clr": dpsRTUv2p11136Clr,
       "dpsRTUv2p11137Clr": dpsRTUv2p11137Clr,
       "dpsRTUv2p11138Clr": dpsRTUv2p11138Clr,
       "dpsRTUv2p11139Clr": dpsRTUv2p11139Clr,
       "dpsRTUv2p11140Clr": dpsRTUv2p11140Clr,
       "dpsRTUv2p11141Clr": dpsRTUv2p11141Clr,
       "dpsRTUv2p11142Clr": dpsRTUv2p11142Clr,
       "dpsRTUv2p11143Clr": dpsRTUv2p11143Clr,
       "dpsRTUv2p11144Clr": dpsRTUv2p11144Clr,
       "dpsRTUv2p11145Clr": dpsRTUv2p11145Clr,
       "dpsRTUv2p11146Clr": dpsRTUv2p11146Clr,
       "dpsRTUv2p11147Clr": dpsRTUv2p11147Clr,
       "dpsRTUv2p11148Clr": dpsRTUv2p11148Clr,
       "dpsRTUv2p11149Clr": dpsRTUv2p11149Clr,
       "dpsRTUv2p11150Clr": dpsRTUv2p11150Clr,
       "dpsRTUv2p11151Clr": dpsRTUv2p11151Clr,
       "dpsRTUv2p11152Clr": dpsRTUv2p11152Clr,
       "dpsRTUv2p11153Clr": dpsRTUv2p11153Clr,
       "dpsRTUv2p11154Clr": dpsRTUv2p11154Clr,
       "dpsRTUv2p11155Clr": dpsRTUv2p11155Clr,
       "dpsRTUv2p11156Clr": dpsRTUv2p11156Clr,
       "dpsRTUv2p11157Clr": dpsRTUv2p11157Clr,
       "dpsRTUv2p11158Clr": dpsRTUv2p11158Clr,
       "dpsRTUv2p11159Clr": dpsRTUv2p11159Clr,
       "dpsRTUv2p11160Clr": dpsRTUv2p11160Clr,
       "dpsRTUv2p11161Clr": dpsRTUv2p11161Clr,
       "dpsRTUv2p11162Clr": dpsRTUv2p11162Clr,
       "dpsRTUv2p11163Clr": dpsRTUv2p11163Clr,
       "dpsRTUv2p11164Clr": dpsRTUv2p11164Clr,
       "dpsRTUv2p11165Clr": dpsRTUv2p11165Clr,
       "dpsRTUv2p11166Clr": dpsRTUv2p11166Clr,
       "dpsRTUv2p11167Clr": dpsRTUv2p11167Clr,
       "dpsRTUv2p11168Clr": dpsRTUv2p11168Clr,
       "dpsRTUv2p11169Clr": dpsRTUv2p11169Clr,
       "dpsRTUv2p11170Clr": dpsRTUv2p11170Clr,
       "dpsRTUv2p11171Clr": dpsRTUv2p11171Clr,
       "dpsRTUv2p11172Clr": dpsRTUv2p11172Clr,
       "dpsRTUv2p11173Clr": dpsRTUv2p11173Clr,
       "dpsRTUv2p11174Clr": dpsRTUv2p11174Clr,
       "dpsRTUv2p11175Clr": dpsRTUv2p11175Clr,
       "dpsRTUv2p11176Clr": dpsRTUv2p11176Clr,
       "dpsRTUv2p11177Clr": dpsRTUv2p11177Clr,
       "dpsRTUv2p11178Clr": dpsRTUv2p11178Clr,
       "dpsRTUv2p11179Clr": dpsRTUv2p11179Clr,
       "dpsRTUv2p11180Clr": dpsRTUv2p11180Clr,
       "dpsRTUv2p11181Clr": dpsRTUv2p11181Clr,
       "dpsRTUv2p11182Clr": dpsRTUv2p11182Clr,
       "dpsRTUv2p11183Clr": dpsRTUv2p11183Clr,
       "dpsRTUv2p11184Clr": dpsRTUv2p11184Clr,
       "dpsRTUv2p11185Clr": dpsRTUv2p11185Clr,
       "dpsRTUv2p11186Clr": dpsRTUv2p11186Clr,
       "dpsRTUv2p11187Clr": dpsRTUv2p11187Clr,
       "dpsRTUv2p11188Clr": dpsRTUv2p11188Clr,
       "dpsRTUv2p11189Clr": dpsRTUv2p11189Clr,
       "dpsRTUv2p11190Clr": dpsRTUv2p11190Clr,
       "dpsRTUv2p11191Clr": dpsRTUv2p11191Clr,
       "dpsRTUv2p11192Clr": dpsRTUv2p11192Clr,
       "dpsRTUv2p11193Clr": dpsRTUv2p11193Clr,
       "dpsRTUv2p11194Clr": dpsRTUv2p11194Clr,
       "dpsRTUv2p11195Clr": dpsRTUv2p11195Clr,
       "dpsRTUv2p11196Clr": dpsRTUv2p11196Clr,
       "dpsRTUv2p11197Clr": dpsRTUv2p11197Clr,
       "dpsRTUv2p11198Clr": dpsRTUv2p11198Clr,
       "dpsRTUv2p11199Clr": dpsRTUv2p11199Clr,
       "dpsRTUv2p11200Clr": dpsRTUv2p11200Clr,
       "dpsRTUv2p11201Clr": dpsRTUv2p11201Clr,
       "dpsRTUv2p11202Clr": dpsRTUv2p11202Clr,
       "dpsRTUv2p11203Clr": dpsRTUv2p11203Clr,
       "dpsRTUv2p11204Clr": dpsRTUv2p11204Clr,
       "dpsRTUv2p11205Clr": dpsRTUv2p11205Clr,
       "dpsRTUv2p11206Clr": dpsRTUv2p11206Clr,
       "dpsRTUv2p11207Clr": dpsRTUv2p11207Clr,
       "dpsRTUv2p11208Clr": dpsRTUv2p11208Clr,
       "dpsRTUv2p11209Clr": dpsRTUv2p11209Clr,
       "dpsRTUv2p11210Clr": dpsRTUv2p11210Clr,
       "dpsRTUv2p11211Clr": dpsRTUv2p11211Clr,
       "dpsRTUv2p11212Clr": dpsRTUv2p11212Clr,
       "dpsRTUv2p11213Clr": dpsRTUv2p11213Clr,
       "dpsRTUv2p11214Clr": dpsRTUv2p11214Clr,
       "dpsRTUv2p11215Clr": dpsRTUv2p11215Clr,
       "dpsRTUv2p11216Clr": dpsRTUv2p11216Clr,
       "dpsRTUv2p11217Clr": dpsRTUv2p11217Clr,
       "dpsRTUv2p11218Clr": dpsRTUv2p11218Clr,
       "dpsRTUv2p11219Clr": dpsRTUv2p11219Clr,
       "dpsRTUv2p11220Clr": dpsRTUv2p11220Clr,
       "dpsRTUv2p11221Clr": dpsRTUv2p11221Clr,
       "dpsRTUv2p11222Clr": dpsRTUv2p11222Clr,
       "dpsRTUv2p11223Clr": dpsRTUv2p11223Clr,
       "dpsRTUv2p11224Clr": dpsRTUv2p11224Clr,
       "dpsRTUv2p11225Clr": dpsRTUv2p11225Clr,
       "dpsRTUv2p11226Clr": dpsRTUv2p11226Clr,
       "dpsRTUv2p11227Clr": dpsRTUv2p11227Clr,
       "dpsRTUv2p11228Clr": dpsRTUv2p11228Clr,
       "dpsRTUv2p11229Clr": dpsRTUv2p11229Clr,
       "dpsRTUv2p11230Clr": dpsRTUv2p11230Clr,
       "dpsRTUv2p11231Clr": dpsRTUv2p11231Clr,
       "dpsRTUv2p11232Clr": dpsRTUv2p11232Clr,
       "dpsRTUv2p11233Clr": dpsRTUv2p11233Clr,
       "dpsRTUv2p11234Clr": dpsRTUv2p11234Clr,
       "dpsRTUv2p11235Clr": dpsRTUv2p11235Clr,
       "dpsRTUv2p11236Clr": dpsRTUv2p11236Clr,
       "dpsRTUv2p11237Clr": dpsRTUv2p11237Clr,
       "dpsRTUv2p11238Clr": dpsRTUv2p11238Clr,
       "dpsRTUv2p11239Clr": dpsRTUv2p11239Clr,
       "dpsRTUv2p11240Clr": dpsRTUv2p11240Clr,
       "dpsRTUv2p11241Clr": dpsRTUv2p11241Clr,
       "dpsRTUv2p11242Clr": dpsRTUv2p11242Clr,
       "dpsRTUv2p11243Clr": dpsRTUv2p11243Clr,
       "dpsRTUv2p11244Clr": dpsRTUv2p11244Clr,
       "dpsRTUv2p11245Clr": dpsRTUv2p11245Clr,
       "dpsRTUv2p11246Clr": dpsRTUv2p11246Clr,
       "dpsRTUv2p11247Clr": dpsRTUv2p11247Clr,
       "dpsRTUv2p11248Clr": dpsRTUv2p11248Clr,
       "dpsRTUv2p11249Clr": dpsRTUv2p11249Clr,
       "dpsRTUv2p11250Clr": dpsRTUv2p11250Clr,
       "dpsRTUv2p11251Clr": dpsRTUv2p11251Clr,
       "dpsRTUv2p11252Clr": dpsRTUv2p11252Clr,
       "dpsRTUv2p11253Clr": dpsRTUv2p11253Clr,
       "dpsRTUv2p11254Clr": dpsRTUv2p11254Clr,
       "dpsRTUv2p11255Clr": dpsRTUv2p11255Clr,
       "dpsRTUv2p11256Clr": dpsRTUv2p11256Clr,
       "dpsRTUv2p11257Clr": dpsRTUv2p11257Clr,
       "dpsRTUv2p11258Clr": dpsRTUv2p11258Clr,
       "dpsRTUv2p11259Clr": dpsRTUv2p11259Clr,
       "dpsRTUv2p11260Clr": dpsRTUv2p11260Clr,
       "dpsRTUv2p11261Clr": dpsRTUv2p11261Clr,
       "dpsRTUv2p11262Clr": dpsRTUv2p11262Clr,
       "dpsRTUv2p11263Clr": dpsRTUv2p11263Clr,
       "dpsRTUv2p11264Clr": dpsRTUv2p11264Clr,
       "dpsRTUv2p11265Clr": dpsRTUv2p11265Clr,
       "dpsRTUv2p11266Clr": dpsRTUv2p11266Clr,
       "dpsRTUv2p11267Clr": dpsRTUv2p11267Clr,
       "dpsRTUv2p11268Clr": dpsRTUv2p11268Clr,
       "dpsRTUv2p11269Clr": dpsRTUv2p11269Clr,
       "dpsRTUv2p11270Clr": dpsRTUv2p11270Clr,
       "dpsRTUv2p11271Clr": dpsRTUv2p11271Clr,
       "dpsRTUv2p11272Clr": dpsRTUv2p11272Clr,
       "dpsRTUv2p11273Clr": dpsRTUv2p11273Clr,
       "dpsRTUv2p11274Clr": dpsRTUv2p11274Clr,
       "dpsRTUv2p11275Clr": dpsRTUv2p11275Clr,
       "dpsRTUv2p11276Clr": dpsRTUv2p11276Clr,
       "dpsRTUv2p11277Clr": dpsRTUv2p11277Clr,
       "dpsRTUv2p11278Clr": dpsRTUv2p11278Clr,
       "dpsRTUv2p11279Clr": dpsRTUv2p11279Clr,
       "dpsRTUv2p11280Clr": dpsRTUv2p11280Clr,
       "dpsRTUv2p11281Clr": dpsRTUv2p11281Clr,
       "dpsRTUv2p11282Clr": dpsRTUv2p11282Clr,
       "dpsRTUv2p11283Clr": dpsRTUv2p11283Clr,
       "dpsRTUv2p11284Clr": dpsRTUv2p11284Clr,
       "dpsRTUv2p11285Clr": dpsRTUv2p11285Clr,
       "dpsRTUv2p11286Clr": dpsRTUv2p11286Clr,
       "dpsRTUv2p11287Clr": dpsRTUv2p11287Clr,
       "dpsRTUv2p11288Clr": dpsRTUv2p11288Clr,
       "dpsRTUv2p11289Clr": dpsRTUv2p11289Clr,
       "dpsRTUv2p11290Clr": dpsRTUv2p11290Clr,
       "dpsRTUv2p11291Clr": dpsRTUv2p11291Clr,
       "dpsRTUv2p11292Clr": dpsRTUv2p11292Clr,
       "dpsRTUv2p11293Clr": dpsRTUv2p11293Clr,
       "dpsRTUv2p11294Clr": dpsRTUv2p11294Clr,
       "dpsRTUv2p11295Clr": dpsRTUv2p11295Clr,
       "dpsRTUv2p11296Clr": dpsRTUv2p11296Clr,
       "dpsRTUv2p11297Clr": dpsRTUv2p11297Clr,
       "dpsRTUv2p11298Clr": dpsRTUv2p11298Clr,
       "dpsRTUv2p11299Clr": dpsRTUv2p11299Clr,
       "dpsRTUv2p11300Clr": dpsRTUv2p11300Clr,
       "dpsRTUv2p11301Clr": dpsRTUv2p11301Clr,
       "dpsRTUv2p11302Clr": dpsRTUv2p11302Clr,
       "dpsRTUv2p11303Clr": dpsRTUv2p11303Clr,
       "dpsRTUv2p11304Clr": dpsRTUv2p11304Clr,
       "dpsRTUv2p11305Clr": dpsRTUv2p11305Clr,
       "dpsRTUv2p11306Clr": dpsRTUv2p11306Clr,
       "dpsRTUv2p11307Clr": dpsRTUv2p11307Clr,
       "dpsRTUv2p11308Clr": dpsRTUv2p11308Clr,
       "dpsRTUv2p11309Clr": dpsRTUv2p11309Clr,
       "dpsRTUv2p11310Clr": dpsRTUv2p11310Clr,
       "dpsRTUv2p11311Clr": dpsRTUv2p11311Clr,
       "dpsRTUv2p11312Clr": dpsRTUv2p11312Clr,
       "dpsRTUv2p11313Clr": dpsRTUv2p11313Clr,
       "dpsRTUv2p11314Clr": dpsRTUv2p11314Clr,
       "dpsRTUv2p11315Clr": dpsRTUv2p11315Clr,
       "dpsRTUv2p11316Clr": dpsRTUv2p11316Clr,
       "dpsRTUv2p11317Clr": dpsRTUv2p11317Clr,
       "dpsRTUv2p11318Clr": dpsRTUv2p11318Clr,
       "dpsRTUv2p11319Clr": dpsRTUv2p11319Clr,
       "dpsRTUv2p11320Clr": dpsRTUv2p11320Clr,
       "dpsRTUrtdV2MI": dpsRTUrtdV2MI}
)
