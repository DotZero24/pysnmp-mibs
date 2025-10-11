# SNMP MIB module (DPS-MIB-NGD-V10-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dps/DPS-MIB-NGD-V10-V2
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:53 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

dpsRTUv2p8001Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8001)
)
dpsRTUv2p8001Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8001Set.setStatus(
        "current"
    )

dpsRTUv2p8002Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8002)
)
dpsRTUv2p8002Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8002Set.setStatus(
        "current"
    )

dpsRTUv2p8003Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8003)
)
dpsRTUv2p8003Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8003Set.setStatus(
        "current"
    )

dpsRTUv2p8004Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8004)
)
dpsRTUv2p8004Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8004Set.setStatus(
        "current"
    )

dpsRTUv2p8005Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8005)
)
dpsRTUv2p8005Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8005Set.setStatus(
        "current"
    )

dpsRTUv2p8006Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8006)
)
dpsRTUv2p8006Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8006Set.setStatus(
        "current"
    )

dpsRTUv2p8007Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8007)
)
dpsRTUv2p8007Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8007Set.setStatus(
        "current"
    )

dpsRTUv2p8008Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8008)
)
dpsRTUv2p8008Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8008Set.setStatus(
        "current"
    )

dpsRTUv2p8009Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8009)
)
dpsRTUv2p8009Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8009Set.setStatus(
        "current"
    )

dpsRTUv2p8010Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8010)
)
dpsRTUv2p8010Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8010Set.setStatus(
        "current"
    )

dpsRTUv2p8011Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8011)
)
dpsRTUv2p8011Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8011Set.setStatus(
        "current"
    )

dpsRTUv2p8012Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8012)
)
dpsRTUv2p8012Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8012Set.setStatus(
        "current"
    )

dpsRTUv2p8013Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8013)
)
dpsRTUv2p8013Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8013Set.setStatus(
        "current"
    )

dpsRTUv2p8014Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8014)
)
dpsRTUv2p8014Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8014Set.setStatus(
        "current"
    )

dpsRTUv2p8015Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8015)
)
dpsRTUv2p8015Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8015Set.setStatus(
        "current"
    )

dpsRTUv2p8016Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8016)
)
dpsRTUv2p8016Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8016Set.setStatus(
        "current"
    )

dpsRTUv2p8017Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8017)
)
dpsRTUv2p8017Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8017Set.setStatus(
        "current"
    )

dpsRTUv2p8018Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8018)
)
dpsRTUv2p8018Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8018Set.setStatus(
        "current"
    )

dpsRTUv2p8019Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8019)
)
dpsRTUv2p8019Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8019Set.setStatus(
        "current"
    )

dpsRTUv2p8020Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8020)
)
dpsRTUv2p8020Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8020Set.setStatus(
        "current"
    )

dpsRTUv2p8021Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8021)
)
dpsRTUv2p8021Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8021Set.setStatus(
        "current"
    )

dpsRTUv2p8022Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8022)
)
dpsRTUv2p8022Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8022Set.setStatus(
        "current"
    )

dpsRTUv2p8023Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8023)
)
dpsRTUv2p8023Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8023Set.setStatus(
        "current"
    )

dpsRTUv2p8024Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8024)
)
dpsRTUv2p8024Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8024Set.setStatus(
        "current"
    )

dpsRTUv2p8025Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8025)
)
dpsRTUv2p8025Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8025Set.setStatus(
        "current"
    )

dpsRTUv2p8026Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8026)
)
dpsRTUv2p8026Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8026Set.setStatus(
        "current"
    )

dpsRTUv2p8027Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8027)
)
dpsRTUv2p8027Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8027Set.setStatus(
        "current"
    )

dpsRTUv2p8028Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8028)
)
dpsRTUv2p8028Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8028Set.setStatus(
        "current"
    )

dpsRTUv2p8029Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8029)
)
dpsRTUv2p8029Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8029Set.setStatus(
        "current"
    )

dpsRTUv2p8030Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8030)
)
dpsRTUv2p8030Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8030Set.setStatus(
        "current"
    )

dpsRTUv2p8031Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8031)
)
dpsRTUv2p8031Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8031Set.setStatus(
        "current"
    )

dpsRTUv2p8032Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8032)
)
dpsRTUv2p8032Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8032Set.setStatus(
        "current"
    )

dpsRTUv2p8033Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8033)
)
dpsRTUv2p8033Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8033Set.setStatus(
        "current"
    )

dpsRTUv2p8034Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8034)
)
dpsRTUv2p8034Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8034Set.setStatus(
        "current"
    )

dpsRTUv2p8035Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8035)
)
dpsRTUv2p8035Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8035Set.setStatus(
        "current"
    )

dpsRTUv2p8036Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8036)
)
dpsRTUv2p8036Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8036Set.setStatus(
        "current"
    )

dpsRTUv2p8037Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8037)
)
dpsRTUv2p8037Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8037Set.setStatus(
        "current"
    )

dpsRTUv2p8038Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8038)
)
dpsRTUv2p8038Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8038Set.setStatus(
        "current"
    )

dpsRTUv2p8039Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8039)
)
dpsRTUv2p8039Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8039Set.setStatus(
        "current"
    )

dpsRTUv2p8040Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8040)
)
dpsRTUv2p8040Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8040Set.setStatus(
        "current"
    )

dpsRTUv2p8041Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8041)
)
dpsRTUv2p8041Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8041Set.setStatus(
        "current"
    )

dpsRTUv2p8042Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8042)
)
dpsRTUv2p8042Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8042Set.setStatus(
        "current"
    )

dpsRTUv2p8043Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8043)
)
dpsRTUv2p8043Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8043Set.setStatus(
        "current"
    )

dpsRTUv2p8044Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8044)
)
dpsRTUv2p8044Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8044Set.setStatus(
        "current"
    )

dpsRTUv2p8045Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8045)
)
dpsRTUv2p8045Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8045Set.setStatus(
        "current"
    )

dpsRTUv2p8046Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8046)
)
dpsRTUv2p8046Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8046Set.setStatus(
        "current"
    )

dpsRTUv2p8047Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8047)
)
dpsRTUv2p8047Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8047Set.setStatus(
        "current"
    )

dpsRTUv2p8048Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8048)
)
dpsRTUv2p8048Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8048Set.setStatus(
        "current"
    )

dpsRTUv2p8049Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8049)
)
dpsRTUv2p8049Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8049Set.setStatus(
        "current"
    )

dpsRTUv2p8050Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8050)
)
dpsRTUv2p8050Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8050Set.setStatus(
        "current"
    )

dpsRTUv2p8051Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8051)
)
dpsRTUv2p8051Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8051Set.setStatus(
        "current"
    )

dpsRTUv2p8052Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8052)
)
dpsRTUv2p8052Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8052Set.setStatus(
        "current"
    )

dpsRTUv2p8053Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8053)
)
dpsRTUv2p8053Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8053Set.setStatus(
        "current"
    )

dpsRTUv2p8054Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8054)
)
dpsRTUv2p8054Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8054Set.setStatus(
        "current"
    )

dpsRTUv2p8055Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8055)
)
dpsRTUv2p8055Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8055Set.setStatus(
        "current"
    )

dpsRTUv2p8056Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8056)
)
dpsRTUv2p8056Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8056Set.setStatus(
        "current"
    )

dpsRTUv2p8057Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8057)
)
dpsRTUv2p8057Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8057Set.setStatus(
        "current"
    )

dpsRTUv2p8058Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8058)
)
dpsRTUv2p8058Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8058Set.setStatus(
        "current"
    )

dpsRTUv2p8059Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8059)
)
dpsRTUv2p8059Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8059Set.setStatus(
        "current"
    )

dpsRTUv2p8060Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8060)
)
dpsRTUv2p8060Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8060Set.setStatus(
        "current"
    )

dpsRTUv2p8061Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8061)
)
dpsRTUv2p8061Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8061Set.setStatus(
        "current"
    )

dpsRTUv2p8062Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8062)
)
dpsRTUv2p8062Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8062Set.setStatus(
        "current"
    )

dpsRTUv2p8063Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8063)
)
dpsRTUv2p8063Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8063Set.setStatus(
        "current"
    )

dpsRTUv2p8064Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8064)
)
dpsRTUv2p8064Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8064Set.setStatus(
        "current"
    )

dpsRTUv2p8065Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8065)
)
dpsRTUv2p8065Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8065Set.setStatus(
        "current"
    )

dpsRTUv2p8066Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8066)
)
dpsRTUv2p8066Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8066Set.setStatus(
        "current"
    )

dpsRTUv2p8067Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8067)
)
dpsRTUv2p8067Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8067Set.setStatus(
        "current"
    )

dpsRTUv2p8068Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8068)
)
dpsRTUv2p8068Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8068Set.setStatus(
        "current"
    )

dpsRTUv2p8069Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8069)
)
dpsRTUv2p8069Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8069Set.setStatus(
        "current"
    )

dpsRTUv2p8070Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8070)
)
dpsRTUv2p8070Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8070Set.setStatus(
        "current"
    )

dpsRTUv2p8071Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8071)
)
dpsRTUv2p8071Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8071Set.setStatus(
        "current"
    )

dpsRTUv2p8072Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8072)
)
dpsRTUv2p8072Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8072Set.setStatus(
        "current"
    )

dpsRTUv2p8073Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8073)
)
dpsRTUv2p8073Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8073Set.setStatus(
        "current"
    )

dpsRTUv2p8074Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8074)
)
dpsRTUv2p8074Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8074Set.setStatus(
        "current"
    )

dpsRTUv2p8075Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8075)
)
dpsRTUv2p8075Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8075Set.setStatus(
        "current"
    )

dpsRTUv2p8076Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8076)
)
dpsRTUv2p8076Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8076Set.setStatus(
        "current"
    )

dpsRTUv2p8077Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8077)
)
dpsRTUv2p8077Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8077Set.setStatus(
        "current"
    )

dpsRTUv2p8078Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8078)
)
dpsRTUv2p8078Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8078Set.setStatus(
        "current"
    )

dpsRTUv2p8079Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8079)
)
dpsRTUv2p8079Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8079Set.setStatus(
        "current"
    )

dpsRTUv2p8080Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8080)
)
dpsRTUv2p8080Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8080Set.setStatus(
        "current"
    )

dpsRTUv2p8081Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8081)
)
dpsRTUv2p8081Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8081Set.setStatus(
        "current"
    )

dpsRTUv2p8082Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8082)
)
dpsRTUv2p8082Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8082Set.setStatus(
        "current"
    )

dpsRTUv2p8083Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8083)
)
dpsRTUv2p8083Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8083Set.setStatus(
        "current"
    )

dpsRTUv2p8084Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8084)
)
dpsRTUv2p8084Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8084Set.setStatus(
        "current"
    )

dpsRTUv2p8085Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8085)
)
dpsRTUv2p8085Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8085Set.setStatus(
        "current"
    )

dpsRTUv2p8086Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8086)
)
dpsRTUv2p8086Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8086Set.setStatus(
        "current"
    )

dpsRTUv2p8087Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8087)
)
dpsRTUv2p8087Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8087Set.setStatus(
        "current"
    )

dpsRTUv2p8088Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8088)
)
dpsRTUv2p8088Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8088Set.setStatus(
        "current"
    )

dpsRTUv2p8089Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8089)
)
dpsRTUv2p8089Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8089Set.setStatus(
        "current"
    )

dpsRTUv2p8090Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8090)
)
dpsRTUv2p8090Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8090Set.setStatus(
        "current"
    )

dpsRTUv2p8091Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8091)
)
dpsRTUv2p8091Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8091Set.setStatus(
        "current"
    )

dpsRTUv2p8092Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8092)
)
dpsRTUv2p8092Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8092Set.setStatus(
        "current"
    )

dpsRTUv2p8093Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8093)
)
dpsRTUv2p8093Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8093Set.setStatus(
        "current"
    )

dpsRTUv2p8094Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8094)
)
dpsRTUv2p8094Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8094Set.setStatus(
        "current"
    )

dpsRTUv2p8095Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8095)
)
dpsRTUv2p8095Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8095Set.setStatus(
        "current"
    )

dpsRTUv2p8096Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8096)
)
dpsRTUv2p8096Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8096Set.setStatus(
        "current"
    )

dpsRTUv2p8097Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8097)
)
dpsRTUv2p8097Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8097Set.setStatus(
        "current"
    )

dpsRTUv2p8098Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8098)
)
dpsRTUv2p8098Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8098Set.setStatus(
        "current"
    )

dpsRTUv2p8099Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8099)
)
dpsRTUv2p8099Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8099Set.setStatus(
        "current"
    )

dpsRTUv2p8100Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8100)
)
dpsRTUv2p8100Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8100Set.setStatus(
        "current"
    )

dpsRTUv2p8101Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8101)
)
dpsRTUv2p8101Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8101Set.setStatus(
        "current"
    )

dpsRTUv2p8102Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8102)
)
dpsRTUv2p8102Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8102Set.setStatus(
        "current"
    )

dpsRTUv2p8103Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8103)
)
dpsRTUv2p8103Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8103Set.setStatus(
        "current"
    )

dpsRTUv2p8104Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8104)
)
dpsRTUv2p8104Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8104Set.setStatus(
        "current"
    )

dpsRTUv2p8105Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8105)
)
dpsRTUv2p8105Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8105Set.setStatus(
        "current"
    )

dpsRTUv2p8106Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8106)
)
dpsRTUv2p8106Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8106Set.setStatus(
        "current"
    )

dpsRTUv2p8107Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8107)
)
dpsRTUv2p8107Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8107Set.setStatus(
        "current"
    )

dpsRTUv2p8108Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8108)
)
dpsRTUv2p8108Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8108Set.setStatus(
        "current"
    )

dpsRTUv2p8109Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8109)
)
dpsRTUv2p8109Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8109Set.setStatus(
        "current"
    )

dpsRTUv2p8110Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8110)
)
dpsRTUv2p8110Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8110Set.setStatus(
        "current"
    )

dpsRTUv2p8111Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8111)
)
dpsRTUv2p8111Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8111Set.setStatus(
        "current"
    )

dpsRTUv2p8112Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8112)
)
dpsRTUv2p8112Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8112Set.setStatus(
        "current"
    )

dpsRTUv2p8113Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8113)
)
dpsRTUv2p8113Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8113Set.setStatus(
        "current"
    )

dpsRTUv2p8114Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8114)
)
dpsRTUv2p8114Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8114Set.setStatus(
        "current"
    )

dpsRTUv2p8115Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8115)
)
dpsRTUv2p8115Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8115Set.setStatus(
        "current"
    )

dpsRTUv2p8116Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8116)
)
dpsRTUv2p8116Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8116Set.setStatus(
        "current"
    )

dpsRTUv2p8117Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8117)
)
dpsRTUv2p8117Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8117Set.setStatus(
        "current"
    )

dpsRTUv2p8118Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8118)
)
dpsRTUv2p8118Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8118Set.setStatus(
        "current"
    )

dpsRTUv2p8119Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8119)
)
dpsRTUv2p8119Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8119Set.setStatus(
        "current"
    )

dpsRTUv2p8120Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8120)
)
dpsRTUv2p8120Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8120Set.setStatus(
        "current"
    )

dpsRTUv2p8121Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8121)
)
dpsRTUv2p8121Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8121Set.setStatus(
        "current"
    )

dpsRTUv2p8122Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8122)
)
dpsRTUv2p8122Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8122Set.setStatus(
        "current"
    )

dpsRTUv2p8123Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8123)
)
dpsRTUv2p8123Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8123Set.setStatus(
        "current"
    )

dpsRTUv2p8124Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8124)
)
dpsRTUv2p8124Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8124Set.setStatus(
        "current"
    )

dpsRTUv2p8125Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8125)
)
dpsRTUv2p8125Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8125Set.setStatus(
        "current"
    )

dpsRTUv2p8126Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8126)
)
dpsRTUv2p8126Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8126Set.setStatus(
        "current"
    )

dpsRTUv2p8127Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8127)
)
dpsRTUv2p8127Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8127Set.setStatus(
        "current"
    )

dpsRTUv2p8128Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8128)
)
dpsRTUv2p8128Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8128Set.setStatus(
        "current"
    )

dpsRTUv2p8129Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8129)
)
dpsRTUv2p8129Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8129Set.setStatus(
        "current"
    )

dpsRTUv2p8130Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8130)
)
dpsRTUv2p8130Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8130Set.setStatus(
        "current"
    )

dpsRTUv2p8131Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8131)
)
dpsRTUv2p8131Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8131Set.setStatus(
        "current"
    )

dpsRTUv2p8132Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8132)
)
dpsRTUv2p8132Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8132Set.setStatus(
        "current"
    )

dpsRTUv2p8133Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8133)
)
dpsRTUv2p8133Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8133Set.setStatus(
        "current"
    )

dpsRTUv2p8134Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8134)
)
dpsRTUv2p8134Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8134Set.setStatus(
        "current"
    )

dpsRTUv2p8135Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8135)
)
dpsRTUv2p8135Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8135Set.setStatus(
        "current"
    )

dpsRTUv2p8136Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8136)
)
dpsRTUv2p8136Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8136Set.setStatus(
        "current"
    )

dpsRTUv2p8137Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8137)
)
dpsRTUv2p8137Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8137Set.setStatus(
        "current"
    )

dpsRTUv2p8138Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8138)
)
dpsRTUv2p8138Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8138Set.setStatus(
        "current"
    )

dpsRTUv2p8139Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8139)
)
dpsRTUv2p8139Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8139Set.setStatus(
        "current"
    )

dpsRTUv2p8140Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8140)
)
dpsRTUv2p8140Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8140Set.setStatus(
        "current"
    )

dpsRTUv2p8141Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8141)
)
dpsRTUv2p8141Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8141Set.setStatus(
        "current"
    )

dpsRTUv2p8142Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8142)
)
dpsRTUv2p8142Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8142Set.setStatus(
        "current"
    )

dpsRTUv2p8143Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8143)
)
dpsRTUv2p8143Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8143Set.setStatus(
        "current"
    )

dpsRTUv2p8144Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8144)
)
dpsRTUv2p8144Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8144Set.setStatus(
        "current"
    )

dpsRTUv2p8145Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8145)
)
dpsRTUv2p8145Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8145Set.setStatus(
        "current"
    )

dpsRTUv2p8146Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8146)
)
dpsRTUv2p8146Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8146Set.setStatus(
        "current"
    )

dpsRTUv2p8147Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8147)
)
dpsRTUv2p8147Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8147Set.setStatus(
        "current"
    )

dpsRTUv2p8148Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8148)
)
dpsRTUv2p8148Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8148Set.setStatus(
        "current"
    )

dpsRTUv2p8149Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8149)
)
dpsRTUv2p8149Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8149Set.setStatus(
        "current"
    )

dpsRTUv2p8150Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8150)
)
dpsRTUv2p8150Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8150Set.setStatus(
        "current"
    )

dpsRTUv2p8151Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8151)
)
dpsRTUv2p8151Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8151Set.setStatus(
        "current"
    )

dpsRTUv2p8152Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8152)
)
dpsRTUv2p8152Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8152Set.setStatus(
        "current"
    )

dpsRTUv2p8153Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8153)
)
dpsRTUv2p8153Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8153Set.setStatus(
        "current"
    )

dpsRTUv2p8154Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8154)
)
dpsRTUv2p8154Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8154Set.setStatus(
        "current"
    )

dpsRTUv2p8155Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8155)
)
dpsRTUv2p8155Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8155Set.setStatus(
        "current"
    )

dpsRTUv2p8156Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8156)
)
dpsRTUv2p8156Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8156Set.setStatus(
        "current"
    )

dpsRTUv2p8157Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8157)
)
dpsRTUv2p8157Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8157Set.setStatus(
        "current"
    )

dpsRTUv2p8158Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8158)
)
dpsRTUv2p8158Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8158Set.setStatus(
        "current"
    )

dpsRTUv2p8159Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8159)
)
dpsRTUv2p8159Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8159Set.setStatus(
        "current"
    )

dpsRTUv2p8160Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8160)
)
dpsRTUv2p8160Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8160Set.setStatus(
        "current"
    )

dpsRTUv2p8161Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8161)
)
dpsRTUv2p8161Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8161Set.setStatus(
        "current"
    )

dpsRTUv2p8162Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8162)
)
dpsRTUv2p8162Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8162Set.setStatus(
        "current"
    )

dpsRTUv2p8163Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8163)
)
dpsRTUv2p8163Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8163Set.setStatus(
        "current"
    )

dpsRTUv2p8164Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8164)
)
dpsRTUv2p8164Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8164Set.setStatus(
        "current"
    )

dpsRTUv2p8165Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8165)
)
dpsRTUv2p8165Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8165Set.setStatus(
        "current"
    )

dpsRTUv2p8166Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8166)
)
dpsRTUv2p8166Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8166Set.setStatus(
        "current"
    )

dpsRTUv2p8167Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8167)
)
dpsRTUv2p8167Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8167Set.setStatus(
        "current"
    )

dpsRTUv2p8168Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8168)
)
dpsRTUv2p8168Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8168Set.setStatus(
        "current"
    )

dpsRTUv2p8169Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8169)
)
dpsRTUv2p8169Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8169Set.setStatus(
        "current"
    )

dpsRTUv2p8170Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8170)
)
dpsRTUv2p8170Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8170Set.setStatus(
        "current"
    )

dpsRTUv2p8171Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8171)
)
dpsRTUv2p8171Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8171Set.setStatus(
        "current"
    )

dpsRTUv2p8172Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8172)
)
dpsRTUv2p8172Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8172Set.setStatus(
        "current"
    )

dpsRTUv2p8173Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8173)
)
dpsRTUv2p8173Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8173Set.setStatus(
        "current"
    )

dpsRTUv2p8174Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8174)
)
dpsRTUv2p8174Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8174Set.setStatus(
        "current"
    )

dpsRTUv2p8175Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8175)
)
dpsRTUv2p8175Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8175Set.setStatus(
        "current"
    )

dpsRTUv2p8176Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8176)
)
dpsRTUv2p8176Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8176Set.setStatus(
        "current"
    )

dpsRTUv2p8193Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8193)
)
dpsRTUv2p8193Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8193Set.setStatus(
        "current"
    )

dpsRTUv2p8194Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8194)
)
dpsRTUv2p8194Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8194Set.setStatus(
        "current"
    )

dpsRTUv2p8195Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8195)
)
dpsRTUv2p8195Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8195Set.setStatus(
        "current"
    )

dpsRTUv2p8196Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8196)
)
dpsRTUv2p8196Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8196Set.setStatus(
        "current"
    )

dpsRTUv2p8197Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8197)
)
dpsRTUv2p8197Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8197Set.setStatus(
        "current"
    )

dpsRTUv2p8198Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8198)
)
dpsRTUv2p8198Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8198Set.setStatus(
        "current"
    )

dpsRTUv2p8199Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8199)
)
dpsRTUv2p8199Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8199Set.setStatus(
        "current"
    )

dpsRTUv2p8200Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8200)
)
dpsRTUv2p8200Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8200Set.setStatus(
        "current"
    )

dpsRTUv2p8201Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8201)
)
dpsRTUv2p8201Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8201Set.setStatus(
        "current"
    )

dpsRTUv2p8202Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8202)
)
dpsRTUv2p8202Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8202Set.setStatus(
        "current"
    )

dpsRTUv2p8203Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8203)
)
dpsRTUv2p8203Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8203Set.setStatus(
        "current"
    )

dpsRTUv2p8204Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8204)
)
dpsRTUv2p8204Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8204Set.setStatus(
        "current"
    )

dpsRTUv2p8205Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8205)
)
dpsRTUv2p8205Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8205Set.setStatus(
        "current"
    )

dpsRTUv2p8206Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8206)
)
dpsRTUv2p8206Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8206Set.setStatus(
        "current"
    )

dpsRTUv2p8207Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8207)
)
dpsRTUv2p8207Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8207Set.setStatus(
        "current"
    )

dpsRTUv2p8208Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8208)
)
dpsRTUv2p8208Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8208Set.setStatus(
        "current"
    )

dpsRTUv2p8209Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8209)
)
dpsRTUv2p8209Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8209Set.setStatus(
        "current"
    )

dpsRTUv2p8210Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8210)
)
dpsRTUv2p8210Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8210Set.setStatus(
        "current"
    )

dpsRTUv2p8211Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8211)
)
dpsRTUv2p8211Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8211Set.setStatus(
        "current"
    )

dpsRTUv2p8212Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8212)
)
dpsRTUv2p8212Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8212Set.setStatus(
        "current"
    )

dpsRTUv2p8213Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8213)
)
dpsRTUv2p8213Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8213Set.setStatus(
        "current"
    )

dpsRTUv2p8214Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8214)
)
dpsRTUv2p8214Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8214Set.setStatus(
        "current"
    )

dpsRTUv2p8215Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8215)
)
dpsRTUv2p8215Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8215Set.setStatus(
        "current"
    )

dpsRTUv2p8216Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8216)
)
dpsRTUv2p8216Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8216Set.setStatus(
        "current"
    )

dpsRTUv2p8217Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8217)
)
dpsRTUv2p8217Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8217Set.setStatus(
        "current"
    )

dpsRTUv2p8218Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8218)
)
dpsRTUv2p8218Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8218Set.setStatus(
        "current"
    )

dpsRTUv2p8219Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8219)
)
dpsRTUv2p8219Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8219Set.setStatus(
        "current"
    )

dpsRTUv2p8220Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8220)
)
dpsRTUv2p8220Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8220Set.setStatus(
        "current"
    )

dpsRTUv2p8221Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8221)
)
dpsRTUv2p8221Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8221Set.setStatus(
        "current"
    )

dpsRTUv2p8222Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8222)
)
dpsRTUv2p8222Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8222Set.setStatus(
        "current"
    )

dpsRTUv2p8223Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8223)
)
dpsRTUv2p8223Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8223Set.setStatus(
        "current"
    )

dpsRTUv2p8224Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8224)
)
dpsRTUv2p8224Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8224Set.setStatus(
        "current"
    )

dpsRTUv2p8225Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8225)
)
dpsRTUv2p8225Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8225Set.setStatus(
        "current"
    )

dpsRTUv2p8226Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8226)
)
dpsRTUv2p8226Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8226Set.setStatus(
        "current"
    )

dpsRTUv2p8227Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8227)
)
dpsRTUv2p8227Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8227Set.setStatus(
        "current"
    )

dpsRTUv2p8228Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8228)
)
dpsRTUv2p8228Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8228Set.setStatus(
        "current"
    )

dpsRTUv2p8229Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8229)
)
dpsRTUv2p8229Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8229Set.setStatus(
        "current"
    )

dpsRTUv2p8230Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8230)
)
dpsRTUv2p8230Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8230Set.setStatus(
        "current"
    )

dpsRTUv2p8231Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8231)
)
dpsRTUv2p8231Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8231Set.setStatus(
        "current"
    )

dpsRTUv2p8232Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8232)
)
dpsRTUv2p8232Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8232Set.setStatus(
        "current"
    )

dpsRTUv2p8233Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8233)
)
dpsRTUv2p8233Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8233Set.setStatus(
        "current"
    )

dpsRTUv2p8234Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8234)
)
dpsRTUv2p8234Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8234Set.setStatus(
        "current"
    )

dpsRTUv2p8235Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8235)
)
dpsRTUv2p8235Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8235Set.setStatus(
        "current"
    )

dpsRTUv2p8236Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8236)
)
dpsRTUv2p8236Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8236Set.setStatus(
        "current"
    )

dpsRTUv2p8237Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8237)
)
dpsRTUv2p8237Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8237Set.setStatus(
        "current"
    )

dpsRTUv2p8238Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8238)
)
dpsRTUv2p8238Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8238Set.setStatus(
        "current"
    )

dpsRTUv2p8239Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8239)
)
dpsRTUv2p8239Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8239Set.setStatus(
        "current"
    )

dpsRTUv2p8240Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8240)
)
dpsRTUv2p8240Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8240Set.setStatus(
        "current"
    )

dpsRTUv2p8241Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8241)
)
dpsRTUv2p8241Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8241Set.setStatus(
        "current"
    )

dpsRTUv2p8242Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8242)
)
dpsRTUv2p8242Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8242Set.setStatus(
        "current"
    )

dpsRTUv2p8243Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8243)
)
dpsRTUv2p8243Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8243Set.setStatus(
        "current"
    )

dpsRTUv2p8244Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8244)
)
dpsRTUv2p8244Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8244Set.setStatus(
        "current"
    )

dpsRTUv2p8245Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8245)
)
dpsRTUv2p8245Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8245Set.setStatus(
        "current"
    )

dpsRTUv2p8246Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8246)
)
dpsRTUv2p8246Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8246Set.setStatus(
        "current"
    )

dpsRTUv2p8247Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8247)
)
dpsRTUv2p8247Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8247Set.setStatus(
        "current"
    )

dpsRTUv2p8248Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8248)
)
dpsRTUv2p8248Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8248Set.setStatus(
        "current"
    )

dpsRTUv2p8249Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8249)
)
dpsRTUv2p8249Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8249Set.setStatus(
        "current"
    )

dpsRTUv2p8250Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8250)
)
dpsRTUv2p8250Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8250Set.setStatus(
        "current"
    )

dpsRTUv2p8251Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8251)
)
dpsRTUv2p8251Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8251Set.setStatus(
        "current"
    )

dpsRTUv2p8252Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8252)
)
dpsRTUv2p8252Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8252Set.setStatus(
        "current"
    )

dpsRTUv2p8253Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8253)
)
dpsRTUv2p8253Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8253Set.setStatus(
        "current"
    )

dpsRTUv2p8254Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8254)
)
dpsRTUv2p8254Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8254Set.setStatus(
        "current"
    )

dpsRTUv2p8255Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8255)
)
dpsRTUv2p8255Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8255Set.setStatus(
        "current"
    )

dpsRTUv2p8256Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8256)
)
dpsRTUv2p8256Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8256Set.setStatus(
        "current"
    )

dpsRTUv2p8257Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8257)
)
dpsRTUv2p8257Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8257Set.setStatus(
        "current"
    )

dpsRTUv2p8258Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8258)
)
dpsRTUv2p8258Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8258Set.setStatus(
        "current"
    )

dpsRTUv2p8259Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8259)
)
dpsRTUv2p8259Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8259Set.setStatus(
        "current"
    )

dpsRTUv2p8260Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8260)
)
dpsRTUv2p8260Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8260Set.setStatus(
        "current"
    )

dpsRTUv2p8321Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8321)
)
dpsRTUv2p8321Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8321Set.setStatus(
        "current"
    )

dpsRTUv2p8322Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8322)
)
dpsRTUv2p8322Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8322Set.setStatus(
        "current"
    )

dpsRTUv2p8323Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8323)
)
dpsRTUv2p8323Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8323Set.setStatus(
        "current"
    )

dpsRTUv2p8324Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8324)
)
dpsRTUv2p8324Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8324Set.setStatus(
        "current"
    )

dpsRTUv2p8385Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8385)
)
dpsRTUv2p8385Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8385Set.setStatus(
        "current"
    )

dpsRTUv2p8386Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8386)
)
dpsRTUv2p8386Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8386Set.setStatus(
        "current"
    )

dpsRTUv2p8387Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8387)
)
dpsRTUv2p8387Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8387Set.setStatus(
        "current"
    )

dpsRTUv2p8388Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8388)
)
dpsRTUv2p8388Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8388Set.setStatus(
        "current"
    )

dpsRTUv2p8449Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8449)
)
dpsRTUv2p8449Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8449Set.setStatus(
        "current"
    )

dpsRTUv2p8450Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8450)
)
dpsRTUv2p8450Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8450Set.setStatus(
        "current"
    )

dpsRTUv2p8451Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8451)
)
dpsRTUv2p8451Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8451Set.setStatus(
        "current"
    )

dpsRTUv2p8452Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8452)
)
dpsRTUv2p8452Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8452Set.setStatus(
        "current"
    )

dpsRTUv2p8513Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8513)
)
dpsRTUv2p8513Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8513Set.setStatus(
        "current"
    )

dpsRTUv2p8514Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8514)
)
dpsRTUv2p8514Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8514Set.setStatus(
        "current"
    )

dpsRTUv2p8515Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8515)
)
dpsRTUv2p8515Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8515Set.setStatus(
        "current"
    )

dpsRTUv2p8516Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8516)
)
dpsRTUv2p8516Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8516Set.setStatus(
        "current"
    )

dpsRTUv2p8577Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8577)
)
dpsRTUv2p8577Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8577Set.setStatus(
        "current"
    )

dpsRTUv2p8578Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8578)
)
dpsRTUv2p8578Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8578Set.setStatus(
        "current"
    )

dpsRTUv2p8579Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8579)
)
dpsRTUv2p8579Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8579Set.setStatus(
        "current"
    )

dpsRTUv2p8580Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8580)
)
dpsRTUv2p8580Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8580Set.setStatus(
        "current"
    )

dpsRTUv2p8641Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8641)
)
dpsRTUv2p8641Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8641Set.setStatus(
        "current"
    )

dpsRTUv2p8642Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8642)
)
dpsRTUv2p8642Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8642Set.setStatus(
        "current"
    )

dpsRTUv2p8657Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8657)
)
dpsRTUv2p8657Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8657Set.setStatus(
        "current"
    )

dpsRTUv2p8659Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8659)
)
dpsRTUv2p8659Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8659Set.setStatus(
        "current"
    )

dpsRTUv2p8660Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8660)
)
dpsRTUv2p8660Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8660Set.setStatus(
        "current"
    )

dpsRTUv2p8661Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8661)
)
dpsRTUv2p8661Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8661Set.setStatus(
        "current"
    )

dpsRTUv2p8662Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8662)
)
dpsRTUv2p8662Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8662Set.setStatus(
        "current"
    )

dpsRTUv2p8673Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8673)
)
dpsRTUv2p8673Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8673Set.setStatus(
        "current"
    )

dpsRTUv2p8676Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8676)
)
dpsRTUv2p8676Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8676Set.setStatus(
        "current"
    )

dpsRTUv2p8677Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8677)
)
dpsRTUv2p8677Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8677Set.setStatus(
        "current"
    )

dpsRTUv2p8678Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8678)
)
dpsRTUv2p8678Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8678Set.setStatus(
        "current"
    )

dpsRTUv2p8679Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8679)
)
dpsRTUv2p8679Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8679Set.setStatus(
        "current"
    )

dpsRTUv2p8680Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8680)
)
dpsRTUv2p8680Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8680Set.setStatus(
        "current"
    )

dpsRTUv2p8683Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8683)
)
dpsRTUv2p8683Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8683Set.setStatus(
        "current"
    )

dpsRTUv2p8684Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8684)
)
dpsRTUv2p8684Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8684Set.setStatus(
        "current"
    )

dpsRTUv2p8685Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8685)
)
dpsRTUv2p8685Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8685Set.setStatus(
        "current"
    )

dpsRTUv2p8686Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8686)
)
dpsRTUv2p8686Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8686Set.setStatus(
        "current"
    )

dpsRTUv2p8688Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8688)
)
dpsRTUv2p8688Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8688Set.setStatus(
        "current"
    )

dpsRTUv2p8696Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8696)
)
dpsRTUv2p8696Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8696Set.setStatus(
        "current"
    )

dpsRTUv2p8697Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8697)
)
dpsRTUv2p8697Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8697Set.setStatus(
        "current"
    )

dpsRTUv2p8698Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8698)
)
dpsRTUv2p8698Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8698Set.setStatus(
        "current"
    )

dpsRTUv2p8703Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8703)
)
dpsRTUv2p8703Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8703Set.setStatus(
        "current"
    )

dpsRTUv2p8704Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 8704)
)
dpsRTUv2p8704Set.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p8704Set.setStatus(
        "current"
    )

dpsRTUv2p9001Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9001)
)
dpsRTUv2p9001Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9001Clr.setStatus(
        "current"
    )

dpsRTUv2p9002Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9002)
)
dpsRTUv2p9002Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9002Clr.setStatus(
        "current"
    )

dpsRTUv2p9003Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9003)
)
dpsRTUv2p9003Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9003Clr.setStatus(
        "current"
    )

dpsRTUv2p9004Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9004)
)
dpsRTUv2p9004Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9004Clr.setStatus(
        "current"
    )

dpsRTUv2p9005Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9005)
)
dpsRTUv2p9005Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9005Clr.setStatus(
        "current"
    )

dpsRTUv2p9006Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9006)
)
dpsRTUv2p9006Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9006Clr.setStatus(
        "current"
    )

dpsRTUv2p9007Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9007)
)
dpsRTUv2p9007Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9007Clr.setStatus(
        "current"
    )

dpsRTUv2p9008Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9008)
)
dpsRTUv2p9008Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9008Clr.setStatus(
        "current"
    )

dpsRTUv2p9009Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9009)
)
dpsRTUv2p9009Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9009Clr.setStatus(
        "current"
    )

dpsRTUv2p9010Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9010)
)
dpsRTUv2p9010Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9010Clr.setStatus(
        "current"
    )

dpsRTUv2p9011Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9011)
)
dpsRTUv2p9011Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9011Clr.setStatus(
        "current"
    )

dpsRTUv2p9012Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9012)
)
dpsRTUv2p9012Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9012Clr.setStatus(
        "current"
    )

dpsRTUv2p9013Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9013)
)
dpsRTUv2p9013Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9013Clr.setStatus(
        "current"
    )

dpsRTUv2p9014Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9014)
)
dpsRTUv2p9014Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9014Clr.setStatus(
        "current"
    )

dpsRTUv2p9015Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9015)
)
dpsRTUv2p9015Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9015Clr.setStatus(
        "current"
    )

dpsRTUv2p9016Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9016)
)
dpsRTUv2p9016Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9016Clr.setStatus(
        "current"
    )

dpsRTUv2p9017Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9017)
)
dpsRTUv2p9017Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9017Clr.setStatus(
        "current"
    )

dpsRTUv2p9018Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9018)
)
dpsRTUv2p9018Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9018Clr.setStatus(
        "current"
    )

dpsRTUv2p9019Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9019)
)
dpsRTUv2p9019Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9019Clr.setStatus(
        "current"
    )

dpsRTUv2p9020Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9020)
)
dpsRTUv2p9020Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9020Clr.setStatus(
        "current"
    )

dpsRTUv2p9021Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9021)
)
dpsRTUv2p9021Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9021Clr.setStatus(
        "current"
    )

dpsRTUv2p9022Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9022)
)
dpsRTUv2p9022Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9022Clr.setStatus(
        "current"
    )

dpsRTUv2p9023Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9023)
)
dpsRTUv2p9023Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9023Clr.setStatus(
        "current"
    )

dpsRTUv2p9024Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9024)
)
dpsRTUv2p9024Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9024Clr.setStatus(
        "current"
    )

dpsRTUv2p9025Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9025)
)
dpsRTUv2p9025Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9025Clr.setStatus(
        "current"
    )

dpsRTUv2p9026Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9026)
)
dpsRTUv2p9026Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9026Clr.setStatus(
        "current"
    )

dpsRTUv2p9027Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9027)
)
dpsRTUv2p9027Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9027Clr.setStatus(
        "current"
    )

dpsRTUv2p9028Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9028)
)
dpsRTUv2p9028Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9028Clr.setStatus(
        "current"
    )

dpsRTUv2p9029Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9029)
)
dpsRTUv2p9029Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9029Clr.setStatus(
        "current"
    )

dpsRTUv2p9030Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9030)
)
dpsRTUv2p9030Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9030Clr.setStatus(
        "current"
    )

dpsRTUv2p9031Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9031)
)
dpsRTUv2p9031Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9031Clr.setStatus(
        "current"
    )

dpsRTUv2p9032Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9032)
)
dpsRTUv2p9032Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9032Clr.setStatus(
        "current"
    )

dpsRTUv2p9033Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9033)
)
dpsRTUv2p9033Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9033Clr.setStatus(
        "current"
    )

dpsRTUv2p9034Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9034)
)
dpsRTUv2p9034Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9034Clr.setStatus(
        "current"
    )

dpsRTUv2p9035Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9035)
)
dpsRTUv2p9035Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9035Clr.setStatus(
        "current"
    )

dpsRTUv2p9036Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9036)
)
dpsRTUv2p9036Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9036Clr.setStatus(
        "current"
    )

dpsRTUv2p9037Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9037)
)
dpsRTUv2p9037Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9037Clr.setStatus(
        "current"
    )

dpsRTUv2p9038Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9038)
)
dpsRTUv2p9038Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9038Clr.setStatus(
        "current"
    )

dpsRTUv2p9039Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9039)
)
dpsRTUv2p9039Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9039Clr.setStatus(
        "current"
    )

dpsRTUv2p9040Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9040)
)
dpsRTUv2p9040Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9040Clr.setStatus(
        "current"
    )

dpsRTUv2p9041Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9041)
)
dpsRTUv2p9041Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9041Clr.setStatus(
        "current"
    )

dpsRTUv2p9042Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9042)
)
dpsRTUv2p9042Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9042Clr.setStatus(
        "current"
    )

dpsRTUv2p9043Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9043)
)
dpsRTUv2p9043Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9043Clr.setStatus(
        "current"
    )

dpsRTUv2p9044Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9044)
)
dpsRTUv2p9044Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9044Clr.setStatus(
        "current"
    )

dpsRTUv2p9045Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9045)
)
dpsRTUv2p9045Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9045Clr.setStatus(
        "current"
    )

dpsRTUv2p9046Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9046)
)
dpsRTUv2p9046Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9046Clr.setStatus(
        "current"
    )

dpsRTUv2p9047Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9047)
)
dpsRTUv2p9047Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9047Clr.setStatus(
        "current"
    )

dpsRTUv2p9048Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9048)
)
dpsRTUv2p9048Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9048Clr.setStatus(
        "current"
    )

dpsRTUv2p9049Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9049)
)
dpsRTUv2p9049Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9049Clr.setStatus(
        "current"
    )

dpsRTUv2p9050Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9050)
)
dpsRTUv2p9050Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9050Clr.setStatus(
        "current"
    )

dpsRTUv2p9051Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9051)
)
dpsRTUv2p9051Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9051Clr.setStatus(
        "current"
    )

dpsRTUv2p9052Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9052)
)
dpsRTUv2p9052Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9052Clr.setStatus(
        "current"
    )

dpsRTUv2p9053Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9053)
)
dpsRTUv2p9053Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9053Clr.setStatus(
        "current"
    )

dpsRTUv2p9054Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9054)
)
dpsRTUv2p9054Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9054Clr.setStatus(
        "current"
    )

dpsRTUv2p9055Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9055)
)
dpsRTUv2p9055Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9055Clr.setStatus(
        "current"
    )

dpsRTUv2p9056Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9056)
)
dpsRTUv2p9056Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9056Clr.setStatus(
        "current"
    )

dpsRTUv2p9057Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9057)
)
dpsRTUv2p9057Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9057Clr.setStatus(
        "current"
    )

dpsRTUv2p9058Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9058)
)
dpsRTUv2p9058Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9058Clr.setStatus(
        "current"
    )

dpsRTUv2p9059Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9059)
)
dpsRTUv2p9059Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9059Clr.setStatus(
        "current"
    )

dpsRTUv2p9060Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9060)
)
dpsRTUv2p9060Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9060Clr.setStatus(
        "current"
    )

dpsRTUv2p9061Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9061)
)
dpsRTUv2p9061Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9061Clr.setStatus(
        "current"
    )

dpsRTUv2p9062Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9062)
)
dpsRTUv2p9062Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9062Clr.setStatus(
        "current"
    )

dpsRTUv2p9063Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9063)
)
dpsRTUv2p9063Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9063Clr.setStatus(
        "current"
    )

dpsRTUv2p9064Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9064)
)
dpsRTUv2p9064Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9064Clr.setStatus(
        "current"
    )

dpsRTUv2p9065Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9065)
)
dpsRTUv2p9065Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9065Clr.setStatus(
        "current"
    )

dpsRTUv2p9066Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9066)
)
dpsRTUv2p9066Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9066Clr.setStatus(
        "current"
    )

dpsRTUv2p9067Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9067)
)
dpsRTUv2p9067Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9067Clr.setStatus(
        "current"
    )

dpsRTUv2p9068Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9068)
)
dpsRTUv2p9068Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9068Clr.setStatus(
        "current"
    )

dpsRTUv2p9069Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9069)
)
dpsRTUv2p9069Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9069Clr.setStatus(
        "current"
    )

dpsRTUv2p9070Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9070)
)
dpsRTUv2p9070Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9070Clr.setStatus(
        "current"
    )

dpsRTUv2p9071Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9071)
)
dpsRTUv2p9071Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9071Clr.setStatus(
        "current"
    )

dpsRTUv2p9072Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9072)
)
dpsRTUv2p9072Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9072Clr.setStatus(
        "current"
    )

dpsRTUv2p9073Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9073)
)
dpsRTUv2p9073Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9073Clr.setStatus(
        "current"
    )

dpsRTUv2p9074Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9074)
)
dpsRTUv2p9074Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9074Clr.setStatus(
        "current"
    )

dpsRTUv2p9075Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9075)
)
dpsRTUv2p9075Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9075Clr.setStatus(
        "current"
    )

dpsRTUv2p9076Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9076)
)
dpsRTUv2p9076Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9076Clr.setStatus(
        "current"
    )

dpsRTUv2p9077Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9077)
)
dpsRTUv2p9077Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9077Clr.setStatus(
        "current"
    )

dpsRTUv2p9078Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9078)
)
dpsRTUv2p9078Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9078Clr.setStatus(
        "current"
    )

dpsRTUv2p9079Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9079)
)
dpsRTUv2p9079Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9079Clr.setStatus(
        "current"
    )

dpsRTUv2p9080Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9080)
)
dpsRTUv2p9080Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9080Clr.setStatus(
        "current"
    )

dpsRTUv2p9081Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9081)
)
dpsRTUv2p9081Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9081Clr.setStatus(
        "current"
    )

dpsRTUv2p9082Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9082)
)
dpsRTUv2p9082Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9082Clr.setStatus(
        "current"
    )

dpsRTUv2p9083Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9083)
)
dpsRTUv2p9083Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9083Clr.setStatus(
        "current"
    )

dpsRTUv2p9084Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9084)
)
dpsRTUv2p9084Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9084Clr.setStatus(
        "current"
    )

dpsRTUv2p9085Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9085)
)
dpsRTUv2p9085Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9085Clr.setStatus(
        "current"
    )

dpsRTUv2p9086Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9086)
)
dpsRTUv2p9086Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9086Clr.setStatus(
        "current"
    )

dpsRTUv2p9087Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9087)
)
dpsRTUv2p9087Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9087Clr.setStatus(
        "current"
    )

dpsRTUv2p9088Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9088)
)
dpsRTUv2p9088Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9088Clr.setStatus(
        "current"
    )

dpsRTUv2p9089Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9089)
)
dpsRTUv2p9089Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9089Clr.setStatus(
        "current"
    )

dpsRTUv2p9090Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9090)
)
dpsRTUv2p9090Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9090Clr.setStatus(
        "current"
    )

dpsRTUv2p9091Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9091)
)
dpsRTUv2p9091Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9091Clr.setStatus(
        "current"
    )

dpsRTUv2p9092Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9092)
)
dpsRTUv2p9092Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9092Clr.setStatus(
        "current"
    )

dpsRTUv2p9093Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9093)
)
dpsRTUv2p9093Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9093Clr.setStatus(
        "current"
    )

dpsRTUv2p9094Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9094)
)
dpsRTUv2p9094Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9094Clr.setStatus(
        "current"
    )

dpsRTUv2p9095Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9095)
)
dpsRTUv2p9095Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9095Clr.setStatus(
        "current"
    )

dpsRTUv2p9096Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9096)
)
dpsRTUv2p9096Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9096Clr.setStatus(
        "current"
    )

dpsRTUv2p9097Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9097)
)
dpsRTUv2p9097Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9097Clr.setStatus(
        "current"
    )

dpsRTUv2p9098Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9098)
)
dpsRTUv2p9098Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9098Clr.setStatus(
        "current"
    )

dpsRTUv2p9099Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9099)
)
dpsRTUv2p9099Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9099Clr.setStatus(
        "current"
    )

dpsRTUv2p9100Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9100)
)
dpsRTUv2p9100Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9100Clr.setStatus(
        "current"
    )

dpsRTUv2p9101Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9101)
)
dpsRTUv2p9101Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9101Clr.setStatus(
        "current"
    )

dpsRTUv2p9102Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9102)
)
dpsRTUv2p9102Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9102Clr.setStatus(
        "current"
    )

dpsRTUv2p9103Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9103)
)
dpsRTUv2p9103Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9103Clr.setStatus(
        "current"
    )

dpsRTUv2p9104Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9104)
)
dpsRTUv2p9104Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9104Clr.setStatus(
        "current"
    )

dpsRTUv2p9105Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9105)
)
dpsRTUv2p9105Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9105Clr.setStatus(
        "current"
    )

dpsRTUv2p9106Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9106)
)
dpsRTUv2p9106Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9106Clr.setStatus(
        "current"
    )

dpsRTUv2p9107Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9107)
)
dpsRTUv2p9107Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9107Clr.setStatus(
        "current"
    )

dpsRTUv2p9108Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9108)
)
dpsRTUv2p9108Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9108Clr.setStatus(
        "current"
    )

dpsRTUv2p9109Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9109)
)
dpsRTUv2p9109Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9109Clr.setStatus(
        "current"
    )

dpsRTUv2p9110Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9110)
)
dpsRTUv2p9110Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9110Clr.setStatus(
        "current"
    )

dpsRTUv2p9111Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9111)
)
dpsRTUv2p9111Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9111Clr.setStatus(
        "current"
    )

dpsRTUv2p9112Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9112)
)
dpsRTUv2p9112Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9112Clr.setStatus(
        "current"
    )

dpsRTUv2p9113Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9113)
)
dpsRTUv2p9113Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9113Clr.setStatus(
        "current"
    )

dpsRTUv2p9114Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9114)
)
dpsRTUv2p9114Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9114Clr.setStatus(
        "current"
    )

dpsRTUv2p9115Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9115)
)
dpsRTUv2p9115Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9115Clr.setStatus(
        "current"
    )

dpsRTUv2p9116Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9116)
)
dpsRTUv2p9116Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9116Clr.setStatus(
        "current"
    )

dpsRTUv2p9117Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9117)
)
dpsRTUv2p9117Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9117Clr.setStatus(
        "current"
    )

dpsRTUv2p9118Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9118)
)
dpsRTUv2p9118Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9118Clr.setStatus(
        "current"
    )

dpsRTUv2p9119Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9119)
)
dpsRTUv2p9119Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9119Clr.setStatus(
        "current"
    )

dpsRTUv2p9120Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9120)
)
dpsRTUv2p9120Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9120Clr.setStatus(
        "current"
    )

dpsRTUv2p9121Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9121)
)
dpsRTUv2p9121Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9121Clr.setStatus(
        "current"
    )

dpsRTUv2p9122Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9122)
)
dpsRTUv2p9122Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9122Clr.setStatus(
        "current"
    )

dpsRTUv2p9123Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9123)
)
dpsRTUv2p9123Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9123Clr.setStatus(
        "current"
    )

dpsRTUv2p9124Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9124)
)
dpsRTUv2p9124Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9124Clr.setStatus(
        "current"
    )

dpsRTUv2p9125Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9125)
)
dpsRTUv2p9125Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9125Clr.setStatus(
        "current"
    )

dpsRTUv2p9126Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9126)
)
dpsRTUv2p9126Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9126Clr.setStatus(
        "current"
    )

dpsRTUv2p9127Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9127)
)
dpsRTUv2p9127Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9127Clr.setStatus(
        "current"
    )

dpsRTUv2p9128Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9128)
)
dpsRTUv2p9128Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9128Clr.setStatus(
        "current"
    )

dpsRTUv2p9129Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9129)
)
dpsRTUv2p9129Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9129Clr.setStatus(
        "current"
    )

dpsRTUv2p9130Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9130)
)
dpsRTUv2p9130Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9130Clr.setStatus(
        "current"
    )

dpsRTUv2p9131Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9131)
)
dpsRTUv2p9131Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9131Clr.setStatus(
        "current"
    )

dpsRTUv2p9132Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9132)
)
dpsRTUv2p9132Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9132Clr.setStatus(
        "current"
    )

dpsRTUv2p9133Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9133)
)
dpsRTUv2p9133Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9133Clr.setStatus(
        "current"
    )

dpsRTUv2p9134Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9134)
)
dpsRTUv2p9134Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9134Clr.setStatus(
        "current"
    )

dpsRTUv2p9135Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9135)
)
dpsRTUv2p9135Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9135Clr.setStatus(
        "current"
    )

dpsRTUv2p9136Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9136)
)
dpsRTUv2p9136Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9136Clr.setStatus(
        "current"
    )

dpsRTUv2p9137Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9137)
)
dpsRTUv2p9137Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9137Clr.setStatus(
        "current"
    )

dpsRTUv2p9138Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9138)
)
dpsRTUv2p9138Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9138Clr.setStatus(
        "current"
    )

dpsRTUv2p9139Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9139)
)
dpsRTUv2p9139Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9139Clr.setStatus(
        "current"
    )

dpsRTUv2p9140Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9140)
)
dpsRTUv2p9140Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9140Clr.setStatus(
        "current"
    )

dpsRTUv2p9141Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9141)
)
dpsRTUv2p9141Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9141Clr.setStatus(
        "current"
    )

dpsRTUv2p9142Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9142)
)
dpsRTUv2p9142Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9142Clr.setStatus(
        "current"
    )

dpsRTUv2p9143Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9143)
)
dpsRTUv2p9143Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9143Clr.setStatus(
        "current"
    )

dpsRTUv2p9144Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9144)
)
dpsRTUv2p9144Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9144Clr.setStatus(
        "current"
    )

dpsRTUv2p9145Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9145)
)
dpsRTUv2p9145Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9145Clr.setStatus(
        "current"
    )

dpsRTUv2p9146Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9146)
)
dpsRTUv2p9146Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9146Clr.setStatus(
        "current"
    )

dpsRTUv2p9147Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9147)
)
dpsRTUv2p9147Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9147Clr.setStatus(
        "current"
    )

dpsRTUv2p9148Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9148)
)
dpsRTUv2p9148Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9148Clr.setStatus(
        "current"
    )

dpsRTUv2p9149Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9149)
)
dpsRTUv2p9149Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9149Clr.setStatus(
        "current"
    )

dpsRTUv2p9150Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9150)
)
dpsRTUv2p9150Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9150Clr.setStatus(
        "current"
    )

dpsRTUv2p9151Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9151)
)
dpsRTUv2p9151Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9151Clr.setStatus(
        "current"
    )

dpsRTUv2p9152Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9152)
)
dpsRTUv2p9152Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9152Clr.setStatus(
        "current"
    )

dpsRTUv2p9153Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9153)
)
dpsRTUv2p9153Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9153Clr.setStatus(
        "current"
    )

dpsRTUv2p9154Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9154)
)
dpsRTUv2p9154Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9154Clr.setStatus(
        "current"
    )

dpsRTUv2p9155Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9155)
)
dpsRTUv2p9155Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9155Clr.setStatus(
        "current"
    )

dpsRTUv2p9156Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9156)
)
dpsRTUv2p9156Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9156Clr.setStatus(
        "current"
    )

dpsRTUv2p9157Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9157)
)
dpsRTUv2p9157Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9157Clr.setStatus(
        "current"
    )

dpsRTUv2p9158Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9158)
)
dpsRTUv2p9158Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9158Clr.setStatus(
        "current"
    )

dpsRTUv2p9159Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9159)
)
dpsRTUv2p9159Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9159Clr.setStatus(
        "current"
    )

dpsRTUv2p9160Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9160)
)
dpsRTUv2p9160Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9160Clr.setStatus(
        "current"
    )

dpsRTUv2p9161Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9161)
)
dpsRTUv2p9161Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9161Clr.setStatus(
        "current"
    )

dpsRTUv2p9162Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9162)
)
dpsRTUv2p9162Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9162Clr.setStatus(
        "current"
    )

dpsRTUv2p9163Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9163)
)
dpsRTUv2p9163Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9163Clr.setStatus(
        "current"
    )

dpsRTUv2p9164Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9164)
)
dpsRTUv2p9164Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9164Clr.setStatus(
        "current"
    )

dpsRTUv2p9165Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9165)
)
dpsRTUv2p9165Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9165Clr.setStatus(
        "current"
    )

dpsRTUv2p9166Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9166)
)
dpsRTUv2p9166Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9166Clr.setStatus(
        "current"
    )

dpsRTUv2p9167Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9167)
)
dpsRTUv2p9167Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9167Clr.setStatus(
        "current"
    )

dpsRTUv2p9168Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9168)
)
dpsRTUv2p9168Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9168Clr.setStatus(
        "current"
    )

dpsRTUv2p9169Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9169)
)
dpsRTUv2p9169Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9169Clr.setStatus(
        "current"
    )

dpsRTUv2p9170Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9170)
)
dpsRTUv2p9170Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9170Clr.setStatus(
        "current"
    )

dpsRTUv2p9171Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9171)
)
dpsRTUv2p9171Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9171Clr.setStatus(
        "current"
    )

dpsRTUv2p9172Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9172)
)
dpsRTUv2p9172Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9172Clr.setStatus(
        "current"
    )

dpsRTUv2p9173Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9173)
)
dpsRTUv2p9173Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9173Clr.setStatus(
        "current"
    )

dpsRTUv2p9174Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9174)
)
dpsRTUv2p9174Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9174Clr.setStatus(
        "current"
    )

dpsRTUv2p9175Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9175)
)
dpsRTUv2p9175Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9175Clr.setStatus(
        "current"
    )

dpsRTUv2p9176Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9176)
)
dpsRTUv2p9176Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9176Clr.setStatus(
        "current"
    )

dpsRTUv2p9193Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9193)
)
dpsRTUv2p9193Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9193Clr.setStatus(
        "current"
    )

dpsRTUv2p9194Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9194)
)
dpsRTUv2p9194Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9194Clr.setStatus(
        "current"
    )

dpsRTUv2p9195Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9195)
)
dpsRTUv2p9195Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9195Clr.setStatus(
        "current"
    )

dpsRTUv2p9196Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9196)
)
dpsRTUv2p9196Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9196Clr.setStatus(
        "current"
    )

dpsRTUv2p9197Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9197)
)
dpsRTUv2p9197Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9197Clr.setStatus(
        "current"
    )

dpsRTUv2p9198Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9198)
)
dpsRTUv2p9198Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9198Clr.setStatus(
        "current"
    )

dpsRTUv2p9199Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9199)
)
dpsRTUv2p9199Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9199Clr.setStatus(
        "current"
    )

dpsRTUv2p9200Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9200)
)
dpsRTUv2p9200Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9200Clr.setStatus(
        "current"
    )

dpsRTUv2p9201Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9201)
)
dpsRTUv2p9201Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9201Clr.setStatus(
        "current"
    )

dpsRTUv2p9202Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9202)
)
dpsRTUv2p9202Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9202Clr.setStatus(
        "current"
    )

dpsRTUv2p9203Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9203)
)
dpsRTUv2p9203Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9203Clr.setStatus(
        "current"
    )

dpsRTUv2p9204Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9204)
)
dpsRTUv2p9204Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9204Clr.setStatus(
        "current"
    )

dpsRTUv2p9205Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9205)
)
dpsRTUv2p9205Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9205Clr.setStatus(
        "current"
    )

dpsRTUv2p9206Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9206)
)
dpsRTUv2p9206Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9206Clr.setStatus(
        "current"
    )

dpsRTUv2p9207Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9207)
)
dpsRTUv2p9207Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9207Clr.setStatus(
        "current"
    )

dpsRTUv2p9208Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9208)
)
dpsRTUv2p9208Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9208Clr.setStatus(
        "current"
    )

dpsRTUv2p9209Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9209)
)
dpsRTUv2p9209Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9209Clr.setStatus(
        "current"
    )

dpsRTUv2p9210Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9210)
)
dpsRTUv2p9210Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9210Clr.setStatus(
        "current"
    )

dpsRTUv2p9211Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9211)
)
dpsRTUv2p9211Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9211Clr.setStatus(
        "current"
    )

dpsRTUv2p9212Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9212)
)
dpsRTUv2p9212Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9212Clr.setStatus(
        "current"
    )

dpsRTUv2p9213Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9213)
)
dpsRTUv2p9213Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9213Clr.setStatus(
        "current"
    )

dpsRTUv2p9214Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9214)
)
dpsRTUv2p9214Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9214Clr.setStatus(
        "current"
    )

dpsRTUv2p9215Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9215)
)
dpsRTUv2p9215Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9215Clr.setStatus(
        "current"
    )

dpsRTUv2p9216Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9216)
)
dpsRTUv2p9216Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9216Clr.setStatus(
        "current"
    )

dpsRTUv2p9217Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9217)
)
dpsRTUv2p9217Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9217Clr.setStatus(
        "current"
    )

dpsRTUv2p9218Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9218)
)
dpsRTUv2p9218Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9218Clr.setStatus(
        "current"
    )

dpsRTUv2p9219Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9219)
)
dpsRTUv2p9219Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9219Clr.setStatus(
        "current"
    )

dpsRTUv2p9220Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9220)
)
dpsRTUv2p9220Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9220Clr.setStatus(
        "current"
    )

dpsRTUv2p9221Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9221)
)
dpsRTUv2p9221Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9221Clr.setStatus(
        "current"
    )

dpsRTUv2p9222Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9222)
)
dpsRTUv2p9222Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9222Clr.setStatus(
        "current"
    )

dpsRTUv2p9223Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9223)
)
dpsRTUv2p9223Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9223Clr.setStatus(
        "current"
    )

dpsRTUv2p9224Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9224)
)
dpsRTUv2p9224Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9224Clr.setStatus(
        "current"
    )

dpsRTUv2p9225Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9225)
)
dpsRTUv2p9225Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9225Clr.setStatus(
        "current"
    )

dpsRTUv2p9226Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9226)
)
dpsRTUv2p9226Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9226Clr.setStatus(
        "current"
    )

dpsRTUv2p9227Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9227)
)
dpsRTUv2p9227Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9227Clr.setStatus(
        "current"
    )

dpsRTUv2p9228Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9228)
)
dpsRTUv2p9228Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9228Clr.setStatus(
        "current"
    )

dpsRTUv2p9229Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9229)
)
dpsRTUv2p9229Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9229Clr.setStatus(
        "current"
    )

dpsRTUv2p9230Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9230)
)
dpsRTUv2p9230Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9230Clr.setStatus(
        "current"
    )

dpsRTUv2p9231Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9231)
)
dpsRTUv2p9231Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9231Clr.setStatus(
        "current"
    )

dpsRTUv2p9232Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9232)
)
dpsRTUv2p9232Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9232Clr.setStatus(
        "current"
    )

dpsRTUv2p9233Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9233)
)
dpsRTUv2p9233Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9233Clr.setStatus(
        "current"
    )

dpsRTUv2p9234Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9234)
)
dpsRTUv2p9234Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9234Clr.setStatus(
        "current"
    )

dpsRTUv2p9235Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9235)
)
dpsRTUv2p9235Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9235Clr.setStatus(
        "current"
    )

dpsRTUv2p9236Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9236)
)
dpsRTUv2p9236Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9236Clr.setStatus(
        "current"
    )

dpsRTUv2p9237Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9237)
)
dpsRTUv2p9237Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9237Clr.setStatus(
        "current"
    )

dpsRTUv2p9238Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9238)
)
dpsRTUv2p9238Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9238Clr.setStatus(
        "current"
    )

dpsRTUv2p9239Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9239)
)
dpsRTUv2p9239Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9239Clr.setStatus(
        "current"
    )

dpsRTUv2p9240Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9240)
)
dpsRTUv2p9240Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9240Clr.setStatus(
        "current"
    )

dpsRTUv2p9241Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9241)
)
dpsRTUv2p9241Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9241Clr.setStatus(
        "current"
    )

dpsRTUv2p9242Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9242)
)
dpsRTUv2p9242Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9242Clr.setStatus(
        "current"
    )

dpsRTUv2p9243Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9243)
)
dpsRTUv2p9243Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9243Clr.setStatus(
        "current"
    )

dpsRTUv2p9244Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9244)
)
dpsRTUv2p9244Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9244Clr.setStatus(
        "current"
    )

dpsRTUv2p9245Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9245)
)
dpsRTUv2p9245Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9245Clr.setStatus(
        "current"
    )

dpsRTUv2p9246Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9246)
)
dpsRTUv2p9246Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9246Clr.setStatus(
        "current"
    )

dpsRTUv2p9247Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9247)
)
dpsRTUv2p9247Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9247Clr.setStatus(
        "current"
    )

dpsRTUv2p9248Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9248)
)
dpsRTUv2p9248Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9248Clr.setStatus(
        "current"
    )

dpsRTUv2p9249Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9249)
)
dpsRTUv2p9249Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9249Clr.setStatus(
        "current"
    )

dpsRTUv2p9250Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9250)
)
dpsRTUv2p9250Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9250Clr.setStatus(
        "current"
    )

dpsRTUv2p9251Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9251)
)
dpsRTUv2p9251Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9251Clr.setStatus(
        "current"
    )

dpsRTUv2p9252Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9252)
)
dpsRTUv2p9252Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9252Clr.setStatus(
        "current"
    )

dpsRTUv2p9253Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9253)
)
dpsRTUv2p9253Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9253Clr.setStatus(
        "current"
    )

dpsRTUv2p9254Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9254)
)
dpsRTUv2p9254Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9254Clr.setStatus(
        "current"
    )

dpsRTUv2p9255Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9255)
)
dpsRTUv2p9255Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9255Clr.setStatus(
        "current"
    )

dpsRTUv2p9256Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9256)
)
dpsRTUv2p9256Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9256Clr.setStatus(
        "current"
    )

dpsRTUv2p9257Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9257)
)
dpsRTUv2p9257Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9257Clr.setStatus(
        "current"
    )

dpsRTUv2p9258Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9258)
)
dpsRTUv2p9258Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9258Clr.setStatus(
        "current"
    )

dpsRTUv2p9259Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9259)
)
dpsRTUv2p9259Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9259Clr.setStatus(
        "current"
    )

dpsRTUv2p9260Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9260)
)
dpsRTUv2p9260Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9260Clr.setStatus(
        "current"
    )

dpsRTUv2p9321Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9321)
)
dpsRTUv2p9321Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9321Clr.setStatus(
        "current"
    )

dpsRTUv2p9322Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9322)
)
dpsRTUv2p9322Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9322Clr.setStatus(
        "current"
    )

dpsRTUv2p9323Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9323)
)
dpsRTUv2p9323Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9323Clr.setStatus(
        "current"
    )

dpsRTUv2p9324Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9324)
)
dpsRTUv2p9324Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9324Clr.setStatus(
        "current"
    )

dpsRTUv2p9385Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9385)
)
dpsRTUv2p9385Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9385Clr.setStatus(
        "current"
    )

dpsRTUv2p9386Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9386)
)
dpsRTUv2p9386Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9386Clr.setStatus(
        "current"
    )

dpsRTUv2p9387Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9387)
)
dpsRTUv2p9387Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9387Clr.setStatus(
        "current"
    )

dpsRTUv2p9388Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9388)
)
dpsRTUv2p9388Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9388Clr.setStatus(
        "current"
    )

dpsRTUv2p9449Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9449)
)
dpsRTUv2p9449Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9449Clr.setStatus(
        "current"
    )

dpsRTUv2p9450Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9450)
)
dpsRTUv2p9450Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9450Clr.setStatus(
        "current"
    )

dpsRTUv2p9451Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9451)
)
dpsRTUv2p9451Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9451Clr.setStatus(
        "current"
    )

dpsRTUv2p9452Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9452)
)
dpsRTUv2p9452Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9452Clr.setStatus(
        "current"
    )

dpsRTUv2p9513Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9513)
)
dpsRTUv2p9513Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9513Clr.setStatus(
        "current"
    )

dpsRTUv2p9514Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9514)
)
dpsRTUv2p9514Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9514Clr.setStatus(
        "current"
    )

dpsRTUv2p9515Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9515)
)
dpsRTUv2p9515Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9515Clr.setStatus(
        "current"
    )

dpsRTUv2p9516Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9516)
)
dpsRTUv2p9516Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9516Clr.setStatus(
        "current"
    )

dpsRTUv2p9577Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9577)
)
dpsRTUv2p9577Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9577Clr.setStatus(
        "current"
    )

dpsRTUv2p9578Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9578)
)
dpsRTUv2p9578Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9578Clr.setStatus(
        "current"
    )

dpsRTUv2p9579Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9579)
)
dpsRTUv2p9579Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9579Clr.setStatus(
        "current"
    )

dpsRTUv2p9580Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9580)
)
dpsRTUv2p9580Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9580Clr.setStatus(
        "current"
    )

dpsRTUv2p9641Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9641)
)
dpsRTUv2p9641Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9641Clr.setStatus(
        "current"
    )

dpsRTUv2p9642Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9642)
)
dpsRTUv2p9642Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9642Clr.setStatus(
        "current"
    )

dpsRTUv2p9657Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9657)
)
dpsRTUv2p9657Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9657Clr.setStatus(
        "current"
    )

dpsRTUv2p9659Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9659)
)
dpsRTUv2p9659Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9659Clr.setStatus(
        "current"
    )

dpsRTUv2p9660Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9660)
)
dpsRTUv2p9660Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9660Clr.setStatus(
        "current"
    )

dpsRTUv2p9661Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9661)
)
dpsRTUv2p9661Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9661Clr.setStatus(
        "current"
    )

dpsRTUv2p9662Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9662)
)
dpsRTUv2p9662Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9662Clr.setStatus(
        "current"
    )

dpsRTUv2p9673Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9673)
)
dpsRTUv2p9673Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9673Clr.setStatus(
        "current"
    )

dpsRTUv2p9676Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9676)
)
dpsRTUv2p9676Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9676Clr.setStatus(
        "current"
    )

dpsRTUv2p9677Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9677)
)
dpsRTUv2p9677Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9677Clr.setStatus(
        "current"
    )

dpsRTUv2p9678Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9678)
)
dpsRTUv2p9678Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9678Clr.setStatus(
        "current"
    )

dpsRTUv2p9679Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9679)
)
dpsRTUv2p9679Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9679Clr.setStatus(
        "current"
    )

dpsRTUv2p9680Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9680)
)
dpsRTUv2p9680Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9680Clr.setStatus(
        "current"
    )

dpsRTUv2p9683Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9683)
)
dpsRTUv2p9683Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9683Clr.setStatus(
        "current"
    )

dpsRTUv2p9684Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9684)
)
dpsRTUv2p9684Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9684Clr.setStatus(
        "current"
    )

dpsRTUv2p9685Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9685)
)
dpsRTUv2p9685Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9685Clr.setStatus(
        "current"
    )

dpsRTUv2p9686Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9686)
)
dpsRTUv2p9686Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9686Clr.setStatus(
        "current"
    )

dpsRTUv2p9688Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9688)
)
dpsRTUv2p9688Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9688Clr.setStatus(
        "current"
    )

dpsRTUv2p9696Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9696)
)
dpsRTUv2p9696Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9696Clr.setStatus(
        "current"
    )

dpsRTUv2p9697Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9697)
)
dpsRTUv2p9697Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9697Clr.setStatus(
        "current"
    )

dpsRTUv2p9698Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9698)
)
dpsRTUv2p9698Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9698Clr.setStatus(
        "current"
    )

dpsRTUv2p9703Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9703)
)
dpsRTUv2p9703Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9703Clr.setStatus(
        "current"
    )

dpsRTUv2p9704Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 9704)
)
dpsRTUv2p9704Clr.setObjects(
      *(("DPS-MIB-NGD-V10-V2", "sysDescr"),
        ("DPS-MIB-NGD-V10-V2", "sysLocation"),
        ("DPS-MIB-V38-V2", "dpsRTUv2DateTime"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APort"),
        ("DPS-MIB-V38-V2", "dpsRTUv2CAddress"),
        ("DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APoint"),
        ("DPS-MIB-V38-V2", "dpsRTUv2APntDesc"),
        ("DPS-MIB-V38-V2", "dpsRTUv2AState"))
)
if mibBuilder.loadTexts:
    dpsRTUv2p9704Clr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-MIB-NGD-V10-V2",
    **{"dpsRTUv2p8001Set": dpsRTUv2p8001Set,
       "dpsRTUv2p8002Set": dpsRTUv2p8002Set,
       "dpsRTUv2p8003Set": dpsRTUv2p8003Set,
       "dpsRTUv2p8004Set": dpsRTUv2p8004Set,
       "dpsRTUv2p8005Set": dpsRTUv2p8005Set,
       "dpsRTUv2p8006Set": dpsRTUv2p8006Set,
       "dpsRTUv2p8007Set": dpsRTUv2p8007Set,
       "dpsRTUv2p8008Set": dpsRTUv2p8008Set,
       "dpsRTUv2p8009Set": dpsRTUv2p8009Set,
       "dpsRTUv2p8010Set": dpsRTUv2p8010Set,
       "dpsRTUv2p8011Set": dpsRTUv2p8011Set,
       "dpsRTUv2p8012Set": dpsRTUv2p8012Set,
       "dpsRTUv2p8013Set": dpsRTUv2p8013Set,
       "dpsRTUv2p8014Set": dpsRTUv2p8014Set,
       "dpsRTUv2p8015Set": dpsRTUv2p8015Set,
       "dpsRTUv2p8016Set": dpsRTUv2p8016Set,
       "dpsRTUv2p8017Set": dpsRTUv2p8017Set,
       "dpsRTUv2p8018Set": dpsRTUv2p8018Set,
       "dpsRTUv2p8019Set": dpsRTUv2p8019Set,
       "dpsRTUv2p8020Set": dpsRTUv2p8020Set,
       "dpsRTUv2p8021Set": dpsRTUv2p8021Set,
       "dpsRTUv2p8022Set": dpsRTUv2p8022Set,
       "dpsRTUv2p8023Set": dpsRTUv2p8023Set,
       "dpsRTUv2p8024Set": dpsRTUv2p8024Set,
       "dpsRTUv2p8025Set": dpsRTUv2p8025Set,
       "dpsRTUv2p8026Set": dpsRTUv2p8026Set,
       "dpsRTUv2p8027Set": dpsRTUv2p8027Set,
       "dpsRTUv2p8028Set": dpsRTUv2p8028Set,
       "dpsRTUv2p8029Set": dpsRTUv2p8029Set,
       "dpsRTUv2p8030Set": dpsRTUv2p8030Set,
       "dpsRTUv2p8031Set": dpsRTUv2p8031Set,
       "dpsRTUv2p8032Set": dpsRTUv2p8032Set,
       "dpsRTUv2p8033Set": dpsRTUv2p8033Set,
       "dpsRTUv2p8034Set": dpsRTUv2p8034Set,
       "dpsRTUv2p8035Set": dpsRTUv2p8035Set,
       "dpsRTUv2p8036Set": dpsRTUv2p8036Set,
       "dpsRTUv2p8037Set": dpsRTUv2p8037Set,
       "dpsRTUv2p8038Set": dpsRTUv2p8038Set,
       "dpsRTUv2p8039Set": dpsRTUv2p8039Set,
       "dpsRTUv2p8040Set": dpsRTUv2p8040Set,
       "dpsRTUv2p8041Set": dpsRTUv2p8041Set,
       "dpsRTUv2p8042Set": dpsRTUv2p8042Set,
       "dpsRTUv2p8043Set": dpsRTUv2p8043Set,
       "dpsRTUv2p8044Set": dpsRTUv2p8044Set,
       "dpsRTUv2p8045Set": dpsRTUv2p8045Set,
       "dpsRTUv2p8046Set": dpsRTUv2p8046Set,
       "dpsRTUv2p8047Set": dpsRTUv2p8047Set,
       "dpsRTUv2p8048Set": dpsRTUv2p8048Set,
       "dpsRTUv2p8049Set": dpsRTUv2p8049Set,
       "dpsRTUv2p8050Set": dpsRTUv2p8050Set,
       "dpsRTUv2p8051Set": dpsRTUv2p8051Set,
       "dpsRTUv2p8052Set": dpsRTUv2p8052Set,
       "dpsRTUv2p8053Set": dpsRTUv2p8053Set,
       "dpsRTUv2p8054Set": dpsRTUv2p8054Set,
       "dpsRTUv2p8055Set": dpsRTUv2p8055Set,
       "dpsRTUv2p8056Set": dpsRTUv2p8056Set,
       "dpsRTUv2p8057Set": dpsRTUv2p8057Set,
       "dpsRTUv2p8058Set": dpsRTUv2p8058Set,
       "dpsRTUv2p8059Set": dpsRTUv2p8059Set,
       "dpsRTUv2p8060Set": dpsRTUv2p8060Set,
       "dpsRTUv2p8061Set": dpsRTUv2p8061Set,
       "dpsRTUv2p8062Set": dpsRTUv2p8062Set,
       "dpsRTUv2p8063Set": dpsRTUv2p8063Set,
       "dpsRTUv2p8064Set": dpsRTUv2p8064Set,
       "dpsRTUv2p8065Set": dpsRTUv2p8065Set,
       "dpsRTUv2p8066Set": dpsRTUv2p8066Set,
       "dpsRTUv2p8067Set": dpsRTUv2p8067Set,
       "dpsRTUv2p8068Set": dpsRTUv2p8068Set,
       "dpsRTUv2p8069Set": dpsRTUv2p8069Set,
       "dpsRTUv2p8070Set": dpsRTUv2p8070Set,
       "dpsRTUv2p8071Set": dpsRTUv2p8071Set,
       "dpsRTUv2p8072Set": dpsRTUv2p8072Set,
       "dpsRTUv2p8073Set": dpsRTUv2p8073Set,
       "dpsRTUv2p8074Set": dpsRTUv2p8074Set,
       "dpsRTUv2p8075Set": dpsRTUv2p8075Set,
       "dpsRTUv2p8076Set": dpsRTUv2p8076Set,
       "dpsRTUv2p8077Set": dpsRTUv2p8077Set,
       "dpsRTUv2p8078Set": dpsRTUv2p8078Set,
       "dpsRTUv2p8079Set": dpsRTUv2p8079Set,
       "dpsRTUv2p8080Set": dpsRTUv2p8080Set,
       "dpsRTUv2p8081Set": dpsRTUv2p8081Set,
       "dpsRTUv2p8082Set": dpsRTUv2p8082Set,
       "dpsRTUv2p8083Set": dpsRTUv2p8083Set,
       "dpsRTUv2p8084Set": dpsRTUv2p8084Set,
       "dpsRTUv2p8085Set": dpsRTUv2p8085Set,
       "dpsRTUv2p8086Set": dpsRTUv2p8086Set,
       "dpsRTUv2p8087Set": dpsRTUv2p8087Set,
       "dpsRTUv2p8088Set": dpsRTUv2p8088Set,
       "dpsRTUv2p8089Set": dpsRTUv2p8089Set,
       "dpsRTUv2p8090Set": dpsRTUv2p8090Set,
       "dpsRTUv2p8091Set": dpsRTUv2p8091Set,
       "dpsRTUv2p8092Set": dpsRTUv2p8092Set,
       "dpsRTUv2p8093Set": dpsRTUv2p8093Set,
       "dpsRTUv2p8094Set": dpsRTUv2p8094Set,
       "dpsRTUv2p8095Set": dpsRTUv2p8095Set,
       "dpsRTUv2p8096Set": dpsRTUv2p8096Set,
       "dpsRTUv2p8097Set": dpsRTUv2p8097Set,
       "dpsRTUv2p8098Set": dpsRTUv2p8098Set,
       "dpsRTUv2p8099Set": dpsRTUv2p8099Set,
       "dpsRTUv2p8100Set": dpsRTUv2p8100Set,
       "dpsRTUv2p8101Set": dpsRTUv2p8101Set,
       "dpsRTUv2p8102Set": dpsRTUv2p8102Set,
       "dpsRTUv2p8103Set": dpsRTUv2p8103Set,
       "dpsRTUv2p8104Set": dpsRTUv2p8104Set,
       "dpsRTUv2p8105Set": dpsRTUv2p8105Set,
       "dpsRTUv2p8106Set": dpsRTUv2p8106Set,
       "dpsRTUv2p8107Set": dpsRTUv2p8107Set,
       "dpsRTUv2p8108Set": dpsRTUv2p8108Set,
       "dpsRTUv2p8109Set": dpsRTUv2p8109Set,
       "dpsRTUv2p8110Set": dpsRTUv2p8110Set,
       "dpsRTUv2p8111Set": dpsRTUv2p8111Set,
       "dpsRTUv2p8112Set": dpsRTUv2p8112Set,
       "dpsRTUv2p8113Set": dpsRTUv2p8113Set,
       "dpsRTUv2p8114Set": dpsRTUv2p8114Set,
       "dpsRTUv2p8115Set": dpsRTUv2p8115Set,
       "dpsRTUv2p8116Set": dpsRTUv2p8116Set,
       "dpsRTUv2p8117Set": dpsRTUv2p8117Set,
       "dpsRTUv2p8118Set": dpsRTUv2p8118Set,
       "dpsRTUv2p8119Set": dpsRTUv2p8119Set,
       "dpsRTUv2p8120Set": dpsRTUv2p8120Set,
       "dpsRTUv2p8121Set": dpsRTUv2p8121Set,
       "dpsRTUv2p8122Set": dpsRTUv2p8122Set,
       "dpsRTUv2p8123Set": dpsRTUv2p8123Set,
       "dpsRTUv2p8124Set": dpsRTUv2p8124Set,
       "dpsRTUv2p8125Set": dpsRTUv2p8125Set,
       "dpsRTUv2p8126Set": dpsRTUv2p8126Set,
       "dpsRTUv2p8127Set": dpsRTUv2p8127Set,
       "dpsRTUv2p8128Set": dpsRTUv2p8128Set,
       "dpsRTUv2p8129Set": dpsRTUv2p8129Set,
       "dpsRTUv2p8130Set": dpsRTUv2p8130Set,
       "dpsRTUv2p8131Set": dpsRTUv2p8131Set,
       "dpsRTUv2p8132Set": dpsRTUv2p8132Set,
       "dpsRTUv2p8133Set": dpsRTUv2p8133Set,
       "dpsRTUv2p8134Set": dpsRTUv2p8134Set,
       "dpsRTUv2p8135Set": dpsRTUv2p8135Set,
       "dpsRTUv2p8136Set": dpsRTUv2p8136Set,
       "dpsRTUv2p8137Set": dpsRTUv2p8137Set,
       "dpsRTUv2p8138Set": dpsRTUv2p8138Set,
       "dpsRTUv2p8139Set": dpsRTUv2p8139Set,
       "dpsRTUv2p8140Set": dpsRTUv2p8140Set,
       "dpsRTUv2p8141Set": dpsRTUv2p8141Set,
       "dpsRTUv2p8142Set": dpsRTUv2p8142Set,
       "dpsRTUv2p8143Set": dpsRTUv2p8143Set,
       "dpsRTUv2p8144Set": dpsRTUv2p8144Set,
       "dpsRTUv2p8145Set": dpsRTUv2p8145Set,
       "dpsRTUv2p8146Set": dpsRTUv2p8146Set,
       "dpsRTUv2p8147Set": dpsRTUv2p8147Set,
       "dpsRTUv2p8148Set": dpsRTUv2p8148Set,
       "dpsRTUv2p8149Set": dpsRTUv2p8149Set,
       "dpsRTUv2p8150Set": dpsRTUv2p8150Set,
       "dpsRTUv2p8151Set": dpsRTUv2p8151Set,
       "dpsRTUv2p8152Set": dpsRTUv2p8152Set,
       "dpsRTUv2p8153Set": dpsRTUv2p8153Set,
       "dpsRTUv2p8154Set": dpsRTUv2p8154Set,
       "dpsRTUv2p8155Set": dpsRTUv2p8155Set,
       "dpsRTUv2p8156Set": dpsRTUv2p8156Set,
       "dpsRTUv2p8157Set": dpsRTUv2p8157Set,
       "dpsRTUv2p8158Set": dpsRTUv2p8158Set,
       "dpsRTUv2p8159Set": dpsRTUv2p8159Set,
       "dpsRTUv2p8160Set": dpsRTUv2p8160Set,
       "dpsRTUv2p8161Set": dpsRTUv2p8161Set,
       "dpsRTUv2p8162Set": dpsRTUv2p8162Set,
       "dpsRTUv2p8163Set": dpsRTUv2p8163Set,
       "dpsRTUv2p8164Set": dpsRTUv2p8164Set,
       "dpsRTUv2p8165Set": dpsRTUv2p8165Set,
       "dpsRTUv2p8166Set": dpsRTUv2p8166Set,
       "dpsRTUv2p8167Set": dpsRTUv2p8167Set,
       "dpsRTUv2p8168Set": dpsRTUv2p8168Set,
       "dpsRTUv2p8169Set": dpsRTUv2p8169Set,
       "dpsRTUv2p8170Set": dpsRTUv2p8170Set,
       "dpsRTUv2p8171Set": dpsRTUv2p8171Set,
       "dpsRTUv2p8172Set": dpsRTUv2p8172Set,
       "dpsRTUv2p8173Set": dpsRTUv2p8173Set,
       "dpsRTUv2p8174Set": dpsRTUv2p8174Set,
       "dpsRTUv2p8175Set": dpsRTUv2p8175Set,
       "dpsRTUv2p8176Set": dpsRTUv2p8176Set,
       "dpsRTUv2p8193Set": dpsRTUv2p8193Set,
       "dpsRTUv2p8194Set": dpsRTUv2p8194Set,
       "dpsRTUv2p8195Set": dpsRTUv2p8195Set,
       "dpsRTUv2p8196Set": dpsRTUv2p8196Set,
       "dpsRTUv2p8197Set": dpsRTUv2p8197Set,
       "dpsRTUv2p8198Set": dpsRTUv2p8198Set,
       "dpsRTUv2p8199Set": dpsRTUv2p8199Set,
       "dpsRTUv2p8200Set": dpsRTUv2p8200Set,
       "dpsRTUv2p8201Set": dpsRTUv2p8201Set,
       "dpsRTUv2p8202Set": dpsRTUv2p8202Set,
       "dpsRTUv2p8203Set": dpsRTUv2p8203Set,
       "dpsRTUv2p8204Set": dpsRTUv2p8204Set,
       "dpsRTUv2p8205Set": dpsRTUv2p8205Set,
       "dpsRTUv2p8206Set": dpsRTUv2p8206Set,
       "dpsRTUv2p8207Set": dpsRTUv2p8207Set,
       "dpsRTUv2p8208Set": dpsRTUv2p8208Set,
       "dpsRTUv2p8209Set": dpsRTUv2p8209Set,
       "dpsRTUv2p8210Set": dpsRTUv2p8210Set,
       "dpsRTUv2p8211Set": dpsRTUv2p8211Set,
       "dpsRTUv2p8212Set": dpsRTUv2p8212Set,
       "dpsRTUv2p8213Set": dpsRTUv2p8213Set,
       "dpsRTUv2p8214Set": dpsRTUv2p8214Set,
       "dpsRTUv2p8215Set": dpsRTUv2p8215Set,
       "dpsRTUv2p8216Set": dpsRTUv2p8216Set,
       "dpsRTUv2p8217Set": dpsRTUv2p8217Set,
       "dpsRTUv2p8218Set": dpsRTUv2p8218Set,
       "dpsRTUv2p8219Set": dpsRTUv2p8219Set,
       "dpsRTUv2p8220Set": dpsRTUv2p8220Set,
       "dpsRTUv2p8221Set": dpsRTUv2p8221Set,
       "dpsRTUv2p8222Set": dpsRTUv2p8222Set,
       "dpsRTUv2p8223Set": dpsRTUv2p8223Set,
       "dpsRTUv2p8224Set": dpsRTUv2p8224Set,
       "dpsRTUv2p8225Set": dpsRTUv2p8225Set,
       "dpsRTUv2p8226Set": dpsRTUv2p8226Set,
       "dpsRTUv2p8227Set": dpsRTUv2p8227Set,
       "dpsRTUv2p8228Set": dpsRTUv2p8228Set,
       "dpsRTUv2p8229Set": dpsRTUv2p8229Set,
       "dpsRTUv2p8230Set": dpsRTUv2p8230Set,
       "dpsRTUv2p8231Set": dpsRTUv2p8231Set,
       "dpsRTUv2p8232Set": dpsRTUv2p8232Set,
       "dpsRTUv2p8233Set": dpsRTUv2p8233Set,
       "dpsRTUv2p8234Set": dpsRTUv2p8234Set,
       "dpsRTUv2p8235Set": dpsRTUv2p8235Set,
       "dpsRTUv2p8236Set": dpsRTUv2p8236Set,
       "dpsRTUv2p8237Set": dpsRTUv2p8237Set,
       "dpsRTUv2p8238Set": dpsRTUv2p8238Set,
       "dpsRTUv2p8239Set": dpsRTUv2p8239Set,
       "dpsRTUv2p8240Set": dpsRTUv2p8240Set,
       "dpsRTUv2p8241Set": dpsRTUv2p8241Set,
       "dpsRTUv2p8242Set": dpsRTUv2p8242Set,
       "dpsRTUv2p8243Set": dpsRTUv2p8243Set,
       "dpsRTUv2p8244Set": dpsRTUv2p8244Set,
       "dpsRTUv2p8245Set": dpsRTUv2p8245Set,
       "dpsRTUv2p8246Set": dpsRTUv2p8246Set,
       "dpsRTUv2p8247Set": dpsRTUv2p8247Set,
       "dpsRTUv2p8248Set": dpsRTUv2p8248Set,
       "dpsRTUv2p8249Set": dpsRTUv2p8249Set,
       "dpsRTUv2p8250Set": dpsRTUv2p8250Set,
       "dpsRTUv2p8251Set": dpsRTUv2p8251Set,
       "dpsRTUv2p8252Set": dpsRTUv2p8252Set,
       "dpsRTUv2p8253Set": dpsRTUv2p8253Set,
       "dpsRTUv2p8254Set": dpsRTUv2p8254Set,
       "dpsRTUv2p8255Set": dpsRTUv2p8255Set,
       "dpsRTUv2p8256Set": dpsRTUv2p8256Set,
       "dpsRTUv2p8257Set": dpsRTUv2p8257Set,
       "dpsRTUv2p8258Set": dpsRTUv2p8258Set,
       "dpsRTUv2p8259Set": dpsRTUv2p8259Set,
       "dpsRTUv2p8260Set": dpsRTUv2p8260Set,
       "dpsRTUv2p8321Set": dpsRTUv2p8321Set,
       "dpsRTUv2p8322Set": dpsRTUv2p8322Set,
       "dpsRTUv2p8323Set": dpsRTUv2p8323Set,
       "dpsRTUv2p8324Set": dpsRTUv2p8324Set,
       "dpsRTUv2p8385Set": dpsRTUv2p8385Set,
       "dpsRTUv2p8386Set": dpsRTUv2p8386Set,
       "dpsRTUv2p8387Set": dpsRTUv2p8387Set,
       "dpsRTUv2p8388Set": dpsRTUv2p8388Set,
       "dpsRTUv2p8449Set": dpsRTUv2p8449Set,
       "dpsRTUv2p8450Set": dpsRTUv2p8450Set,
       "dpsRTUv2p8451Set": dpsRTUv2p8451Set,
       "dpsRTUv2p8452Set": dpsRTUv2p8452Set,
       "dpsRTUv2p8513Set": dpsRTUv2p8513Set,
       "dpsRTUv2p8514Set": dpsRTUv2p8514Set,
       "dpsRTUv2p8515Set": dpsRTUv2p8515Set,
       "dpsRTUv2p8516Set": dpsRTUv2p8516Set,
       "dpsRTUv2p8577Set": dpsRTUv2p8577Set,
       "dpsRTUv2p8578Set": dpsRTUv2p8578Set,
       "dpsRTUv2p8579Set": dpsRTUv2p8579Set,
       "dpsRTUv2p8580Set": dpsRTUv2p8580Set,
       "dpsRTUv2p8641Set": dpsRTUv2p8641Set,
       "dpsRTUv2p8642Set": dpsRTUv2p8642Set,
       "dpsRTUv2p8657Set": dpsRTUv2p8657Set,
       "dpsRTUv2p8659Set": dpsRTUv2p8659Set,
       "dpsRTUv2p8660Set": dpsRTUv2p8660Set,
       "dpsRTUv2p8661Set": dpsRTUv2p8661Set,
       "dpsRTUv2p8662Set": dpsRTUv2p8662Set,
       "dpsRTUv2p8673Set": dpsRTUv2p8673Set,
       "dpsRTUv2p8676Set": dpsRTUv2p8676Set,
       "dpsRTUv2p8677Set": dpsRTUv2p8677Set,
       "dpsRTUv2p8678Set": dpsRTUv2p8678Set,
       "dpsRTUv2p8679Set": dpsRTUv2p8679Set,
       "dpsRTUv2p8680Set": dpsRTUv2p8680Set,
       "dpsRTUv2p8683Set": dpsRTUv2p8683Set,
       "dpsRTUv2p8684Set": dpsRTUv2p8684Set,
       "dpsRTUv2p8685Set": dpsRTUv2p8685Set,
       "dpsRTUv2p8686Set": dpsRTUv2p8686Set,
       "dpsRTUv2p8688Set": dpsRTUv2p8688Set,
       "dpsRTUv2p8696Set": dpsRTUv2p8696Set,
       "dpsRTUv2p8697Set": dpsRTUv2p8697Set,
       "dpsRTUv2p8698Set": dpsRTUv2p8698Set,
       "dpsRTUv2p8703Set": dpsRTUv2p8703Set,
       "dpsRTUv2p8704Set": dpsRTUv2p8704Set,
       "dpsRTUv2p9001Clr": dpsRTUv2p9001Clr,
       "dpsRTUv2p9002Clr": dpsRTUv2p9002Clr,
       "dpsRTUv2p9003Clr": dpsRTUv2p9003Clr,
       "dpsRTUv2p9004Clr": dpsRTUv2p9004Clr,
       "dpsRTUv2p9005Clr": dpsRTUv2p9005Clr,
       "dpsRTUv2p9006Clr": dpsRTUv2p9006Clr,
       "dpsRTUv2p9007Clr": dpsRTUv2p9007Clr,
       "dpsRTUv2p9008Clr": dpsRTUv2p9008Clr,
       "dpsRTUv2p9009Clr": dpsRTUv2p9009Clr,
       "dpsRTUv2p9010Clr": dpsRTUv2p9010Clr,
       "dpsRTUv2p9011Clr": dpsRTUv2p9011Clr,
       "dpsRTUv2p9012Clr": dpsRTUv2p9012Clr,
       "dpsRTUv2p9013Clr": dpsRTUv2p9013Clr,
       "dpsRTUv2p9014Clr": dpsRTUv2p9014Clr,
       "dpsRTUv2p9015Clr": dpsRTUv2p9015Clr,
       "dpsRTUv2p9016Clr": dpsRTUv2p9016Clr,
       "dpsRTUv2p9017Clr": dpsRTUv2p9017Clr,
       "dpsRTUv2p9018Clr": dpsRTUv2p9018Clr,
       "dpsRTUv2p9019Clr": dpsRTUv2p9019Clr,
       "dpsRTUv2p9020Clr": dpsRTUv2p9020Clr,
       "dpsRTUv2p9021Clr": dpsRTUv2p9021Clr,
       "dpsRTUv2p9022Clr": dpsRTUv2p9022Clr,
       "dpsRTUv2p9023Clr": dpsRTUv2p9023Clr,
       "dpsRTUv2p9024Clr": dpsRTUv2p9024Clr,
       "dpsRTUv2p9025Clr": dpsRTUv2p9025Clr,
       "dpsRTUv2p9026Clr": dpsRTUv2p9026Clr,
       "dpsRTUv2p9027Clr": dpsRTUv2p9027Clr,
       "dpsRTUv2p9028Clr": dpsRTUv2p9028Clr,
       "dpsRTUv2p9029Clr": dpsRTUv2p9029Clr,
       "dpsRTUv2p9030Clr": dpsRTUv2p9030Clr,
       "dpsRTUv2p9031Clr": dpsRTUv2p9031Clr,
       "dpsRTUv2p9032Clr": dpsRTUv2p9032Clr,
       "dpsRTUv2p9033Clr": dpsRTUv2p9033Clr,
       "dpsRTUv2p9034Clr": dpsRTUv2p9034Clr,
       "dpsRTUv2p9035Clr": dpsRTUv2p9035Clr,
       "dpsRTUv2p9036Clr": dpsRTUv2p9036Clr,
       "dpsRTUv2p9037Clr": dpsRTUv2p9037Clr,
       "dpsRTUv2p9038Clr": dpsRTUv2p9038Clr,
       "dpsRTUv2p9039Clr": dpsRTUv2p9039Clr,
       "dpsRTUv2p9040Clr": dpsRTUv2p9040Clr,
       "dpsRTUv2p9041Clr": dpsRTUv2p9041Clr,
       "dpsRTUv2p9042Clr": dpsRTUv2p9042Clr,
       "dpsRTUv2p9043Clr": dpsRTUv2p9043Clr,
       "dpsRTUv2p9044Clr": dpsRTUv2p9044Clr,
       "dpsRTUv2p9045Clr": dpsRTUv2p9045Clr,
       "dpsRTUv2p9046Clr": dpsRTUv2p9046Clr,
       "dpsRTUv2p9047Clr": dpsRTUv2p9047Clr,
       "dpsRTUv2p9048Clr": dpsRTUv2p9048Clr,
       "dpsRTUv2p9049Clr": dpsRTUv2p9049Clr,
       "dpsRTUv2p9050Clr": dpsRTUv2p9050Clr,
       "dpsRTUv2p9051Clr": dpsRTUv2p9051Clr,
       "dpsRTUv2p9052Clr": dpsRTUv2p9052Clr,
       "dpsRTUv2p9053Clr": dpsRTUv2p9053Clr,
       "dpsRTUv2p9054Clr": dpsRTUv2p9054Clr,
       "dpsRTUv2p9055Clr": dpsRTUv2p9055Clr,
       "dpsRTUv2p9056Clr": dpsRTUv2p9056Clr,
       "dpsRTUv2p9057Clr": dpsRTUv2p9057Clr,
       "dpsRTUv2p9058Clr": dpsRTUv2p9058Clr,
       "dpsRTUv2p9059Clr": dpsRTUv2p9059Clr,
       "dpsRTUv2p9060Clr": dpsRTUv2p9060Clr,
       "dpsRTUv2p9061Clr": dpsRTUv2p9061Clr,
       "dpsRTUv2p9062Clr": dpsRTUv2p9062Clr,
       "dpsRTUv2p9063Clr": dpsRTUv2p9063Clr,
       "dpsRTUv2p9064Clr": dpsRTUv2p9064Clr,
       "dpsRTUv2p9065Clr": dpsRTUv2p9065Clr,
       "dpsRTUv2p9066Clr": dpsRTUv2p9066Clr,
       "dpsRTUv2p9067Clr": dpsRTUv2p9067Clr,
       "dpsRTUv2p9068Clr": dpsRTUv2p9068Clr,
       "dpsRTUv2p9069Clr": dpsRTUv2p9069Clr,
       "dpsRTUv2p9070Clr": dpsRTUv2p9070Clr,
       "dpsRTUv2p9071Clr": dpsRTUv2p9071Clr,
       "dpsRTUv2p9072Clr": dpsRTUv2p9072Clr,
       "dpsRTUv2p9073Clr": dpsRTUv2p9073Clr,
       "dpsRTUv2p9074Clr": dpsRTUv2p9074Clr,
       "dpsRTUv2p9075Clr": dpsRTUv2p9075Clr,
       "dpsRTUv2p9076Clr": dpsRTUv2p9076Clr,
       "dpsRTUv2p9077Clr": dpsRTUv2p9077Clr,
       "dpsRTUv2p9078Clr": dpsRTUv2p9078Clr,
       "dpsRTUv2p9079Clr": dpsRTUv2p9079Clr,
       "dpsRTUv2p9080Clr": dpsRTUv2p9080Clr,
       "dpsRTUv2p9081Clr": dpsRTUv2p9081Clr,
       "dpsRTUv2p9082Clr": dpsRTUv2p9082Clr,
       "dpsRTUv2p9083Clr": dpsRTUv2p9083Clr,
       "dpsRTUv2p9084Clr": dpsRTUv2p9084Clr,
       "dpsRTUv2p9085Clr": dpsRTUv2p9085Clr,
       "dpsRTUv2p9086Clr": dpsRTUv2p9086Clr,
       "dpsRTUv2p9087Clr": dpsRTUv2p9087Clr,
       "dpsRTUv2p9088Clr": dpsRTUv2p9088Clr,
       "dpsRTUv2p9089Clr": dpsRTUv2p9089Clr,
       "dpsRTUv2p9090Clr": dpsRTUv2p9090Clr,
       "dpsRTUv2p9091Clr": dpsRTUv2p9091Clr,
       "dpsRTUv2p9092Clr": dpsRTUv2p9092Clr,
       "dpsRTUv2p9093Clr": dpsRTUv2p9093Clr,
       "dpsRTUv2p9094Clr": dpsRTUv2p9094Clr,
       "dpsRTUv2p9095Clr": dpsRTUv2p9095Clr,
       "dpsRTUv2p9096Clr": dpsRTUv2p9096Clr,
       "dpsRTUv2p9097Clr": dpsRTUv2p9097Clr,
       "dpsRTUv2p9098Clr": dpsRTUv2p9098Clr,
       "dpsRTUv2p9099Clr": dpsRTUv2p9099Clr,
       "dpsRTUv2p9100Clr": dpsRTUv2p9100Clr,
       "dpsRTUv2p9101Clr": dpsRTUv2p9101Clr,
       "dpsRTUv2p9102Clr": dpsRTUv2p9102Clr,
       "dpsRTUv2p9103Clr": dpsRTUv2p9103Clr,
       "dpsRTUv2p9104Clr": dpsRTUv2p9104Clr,
       "dpsRTUv2p9105Clr": dpsRTUv2p9105Clr,
       "dpsRTUv2p9106Clr": dpsRTUv2p9106Clr,
       "dpsRTUv2p9107Clr": dpsRTUv2p9107Clr,
       "dpsRTUv2p9108Clr": dpsRTUv2p9108Clr,
       "dpsRTUv2p9109Clr": dpsRTUv2p9109Clr,
       "dpsRTUv2p9110Clr": dpsRTUv2p9110Clr,
       "dpsRTUv2p9111Clr": dpsRTUv2p9111Clr,
       "dpsRTUv2p9112Clr": dpsRTUv2p9112Clr,
       "dpsRTUv2p9113Clr": dpsRTUv2p9113Clr,
       "dpsRTUv2p9114Clr": dpsRTUv2p9114Clr,
       "dpsRTUv2p9115Clr": dpsRTUv2p9115Clr,
       "dpsRTUv2p9116Clr": dpsRTUv2p9116Clr,
       "dpsRTUv2p9117Clr": dpsRTUv2p9117Clr,
       "dpsRTUv2p9118Clr": dpsRTUv2p9118Clr,
       "dpsRTUv2p9119Clr": dpsRTUv2p9119Clr,
       "dpsRTUv2p9120Clr": dpsRTUv2p9120Clr,
       "dpsRTUv2p9121Clr": dpsRTUv2p9121Clr,
       "dpsRTUv2p9122Clr": dpsRTUv2p9122Clr,
       "dpsRTUv2p9123Clr": dpsRTUv2p9123Clr,
       "dpsRTUv2p9124Clr": dpsRTUv2p9124Clr,
       "dpsRTUv2p9125Clr": dpsRTUv2p9125Clr,
       "dpsRTUv2p9126Clr": dpsRTUv2p9126Clr,
       "dpsRTUv2p9127Clr": dpsRTUv2p9127Clr,
       "dpsRTUv2p9128Clr": dpsRTUv2p9128Clr,
       "dpsRTUv2p9129Clr": dpsRTUv2p9129Clr,
       "dpsRTUv2p9130Clr": dpsRTUv2p9130Clr,
       "dpsRTUv2p9131Clr": dpsRTUv2p9131Clr,
       "dpsRTUv2p9132Clr": dpsRTUv2p9132Clr,
       "dpsRTUv2p9133Clr": dpsRTUv2p9133Clr,
       "dpsRTUv2p9134Clr": dpsRTUv2p9134Clr,
       "dpsRTUv2p9135Clr": dpsRTUv2p9135Clr,
       "dpsRTUv2p9136Clr": dpsRTUv2p9136Clr,
       "dpsRTUv2p9137Clr": dpsRTUv2p9137Clr,
       "dpsRTUv2p9138Clr": dpsRTUv2p9138Clr,
       "dpsRTUv2p9139Clr": dpsRTUv2p9139Clr,
       "dpsRTUv2p9140Clr": dpsRTUv2p9140Clr,
       "dpsRTUv2p9141Clr": dpsRTUv2p9141Clr,
       "dpsRTUv2p9142Clr": dpsRTUv2p9142Clr,
       "dpsRTUv2p9143Clr": dpsRTUv2p9143Clr,
       "dpsRTUv2p9144Clr": dpsRTUv2p9144Clr,
       "dpsRTUv2p9145Clr": dpsRTUv2p9145Clr,
       "dpsRTUv2p9146Clr": dpsRTUv2p9146Clr,
       "dpsRTUv2p9147Clr": dpsRTUv2p9147Clr,
       "dpsRTUv2p9148Clr": dpsRTUv2p9148Clr,
       "dpsRTUv2p9149Clr": dpsRTUv2p9149Clr,
       "dpsRTUv2p9150Clr": dpsRTUv2p9150Clr,
       "dpsRTUv2p9151Clr": dpsRTUv2p9151Clr,
       "dpsRTUv2p9152Clr": dpsRTUv2p9152Clr,
       "dpsRTUv2p9153Clr": dpsRTUv2p9153Clr,
       "dpsRTUv2p9154Clr": dpsRTUv2p9154Clr,
       "dpsRTUv2p9155Clr": dpsRTUv2p9155Clr,
       "dpsRTUv2p9156Clr": dpsRTUv2p9156Clr,
       "dpsRTUv2p9157Clr": dpsRTUv2p9157Clr,
       "dpsRTUv2p9158Clr": dpsRTUv2p9158Clr,
       "dpsRTUv2p9159Clr": dpsRTUv2p9159Clr,
       "dpsRTUv2p9160Clr": dpsRTUv2p9160Clr,
       "dpsRTUv2p9161Clr": dpsRTUv2p9161Clr,
       "dpsRTUv2p9162Clr": dpsRTUv2p9162Clr,
       "dpsRTUv2p9163Clr": dpsRTUv2p9163Clr,
       "dpsRTUv2p9164Clr": dpsRTUv2p9164Clr,
       "dpsRTUv2p9165Clr": dpsRTUv2p9165Clr,
       "dpsRTUv2p9166Clr": dpsRTUv2p9166Clr,
       "dpsRTUv2p9167Clr": dpsRTUv2p9167Clr,
       "dpsRTUv2p9168Clr": dpsRTUv2p9168Clr,
       "dpsRTUv2p9169Clr": dpsRTUv2p9169Clr,
       "dpsRTUv2p9170Clr": dpsRTUv2p9170Clr,
       "dpsRTUv2p9171Clr": dpsRTUv2p9171Clr,
       "dpsRTUv2p9172Clr": dpsRTUv2p9172Clr,
       "dpsRTUv2p9173Clr": dpsRTUv2p9173Clr,
       "dpsRTUv2p9174Clr": dpsRTUv2p9174Clr,
       "dpsRTUv2p9175Clr": dpsRTUv2p9175Clr,
       "dpsRTUv2p9176Clr": dpsRTUv2p9176Clr,
       "dpsRTUv2p9193Clr": dpsRTUv2p9193Clr,
       "dpsRTUv2p9194Clr": dpsRTUv2p9194Clr,
       "dpsRTUv2p9195Clr": dpsRTUv2p9195Clr,
       "dpsRTUv2p9196Clr": dpsRTUv2p9196Clr,
       "dpsRTUv2p9197Clr": dpsRTUv2p9197Clr,
       "dpsRTUv2p9198Clr": dpsRTUv2p9198Clr,
       "dpsRTUv2p9199Clr": dpsRTUv2p9199Clr,
       "dpsRTUv2p9200Clr": dpsRTUv2p9200Clr,
       "dpsRTUv2p9201Clr": dpsRTUv2p9201Clr,
       "dpsRTUv2p9202Clr": dpsRTUv2p9202Clr,
       "dpsRTUv2p9203Clr": dpsRTUv2p9203Clr,
       "dpsRTUv2p9204Clr": dpsRTUv2p9204Clr,
       "dpsRTUv2p9205Clr": dpsRTUv2p9205Clr,
       "dpsRTUv2p9206Clr": dpsRTUv2p9206Clr,
       "dpsRTUv2p9207Clr": dpsRTUv2p9207Clr,
       "dpsRTUv2p9208Clr": dpsRTUv2p9208Clr,
       "dpsRTUv2p9209Clr": dpsRTUv2p9209Clr,
       "dpsRTUv2p9210Clr": dpsRTUv2p9210Clr,
       "dpsRTUv2p9211Clr": dpsRTUv2p9211Clr,
       "dpsRTUv2p9212Clr": dpsRTUv2p9212Clr,
       "dpsRTUv2p9213Clr": dpsRTUv2p9213Clr,
       "dpsRTUv2p9214Clr": dpsRTUv2p9214Clr,
       "dpsRTUv2p9215Clr": dpsRTUv2p9215Clr,
       "dpsRTUv2p9216Clr": dpsRTUv2p9216Clr,
       "dpsRTUv2p9217Clr": dpsRTUv2p9217Clr,
       "dpsRTUv2p9218Clr": dpsRTUv2p9218Clr,
       "dpsRTUv2p9219Clr": dpsRTUv2p9219Clr,
       "dpsRTUv2p9220Clr": dpsRTUv2p9220Clr,
       "dpsRTUv2p9221Clr": dpsRTUv2p9221Clr,
       "dpsRTUv2p9222Clr": dpsRTUv2p9222Clr,
       "dpsRTUv2p9223Clr": dpsRTUv2p9223Clr,
       "dpsRTUv2p9224Clr": dpsRTUv2p9224Clr,
       "dpsRTUv2p9225Clr": dpsRTUv2p9225Clr,
       "dpsRTUv2p9226Clr": dpsRTUv2p9226Clr,
       "dpsRTUv2p9227Clr": dpsRTUv2p9227Clr,
       "dpsRTUv2p9228Clr": dpsRTUv2p9228Clr,
       "dpsRTUv2p9229Clr": dpsRTUv2p9229Clr,
       "dpsRTUv2p9230Clr": dpsRTUv2p9230Clr,
       "dpsRTUv2p9231Clr": dpsRTUv2p9231Clr,
       "dpsRTUv2p9232Clr": dpsRTUv2p9232Clr,
       "dpsRTUv2p9233Clr": dpsRTUv2p9233Clr,
       "dpsRTUv2p9234Clr": dpsRTUv2p9234Clr,
       "dpsRTUv2p9235Clr": dpsRTUv2p9235Clr,
       "dpsRTUv2p9236Clr": dpsRTUv2p9236Clr,
       "dpsRTUv2p9237Clr": dpsRTUv2p9237Clr,
       "dpsRTUv2p9238Clr": dpsRTUv2p9238Clr,
       "dpsRTUv2p9239Clr": dpsRTUv2p9239Clr,
       "dpsRTUv2p9240Clr": dpsRTUv2p9240Clr,
       "dpsRTUv2p9241Clr": dpsRTUv2p9241Clr,
       "dpsRTUv2p9242Clr": dpsRTUv2p9242Clr,
       "dpsRTUv2p9243Clr": dpsRTUv2p9243Clr,
       "dpsRTUv2p9244Clr": dpsRTUv2p9244Clr,
       "dpsRTUv2p9245Clr": dpsRTUv2p9245Clr,
       "dpsRTUv2p9246Clr": dpsRTUv2p9246Clr,
       "dpsRTUv2p9247Clr": dpsRTUv2p9247Clr,
       "dpsRTUv2p9248Clr": dpsRTUv2p9248Clr,
       "dpsRTUv2p9249Clr": dpsRTUv2p9249Clr,
       "dpsRTUv2p9250Clr": dpsRTUv2p9250Clr,
       "dpsRTUv2p9251Clr": dpsRTUv2p9251Clr,
       "dpsRTUv2p9252Clr": dpsRTUv2p9252Clr,
       "dpsRTUv2p9253Clr": dpsRTUv2p9253Clr,
       "dpsRTUv2p9254Clr": dpsRTUv2p9254Clr,
       "dpsRTUv2p9255Clr": dpsRTUv2p9255Clr,
       "dpsRTUv2p9256Clr": dpsRTUv2p9256Clr,
       "dpsRTUv2p9257Clr": dpsRTUv2p9257Clr,
       "dpsRTUv2p9258Clr": dpsRTUv2p9258Clr,
       "dpsRTUv2p9259Clr": dpsRTUv2p9259Clr,
       "dpsRTUv2p9260Clr": dpsRTUv2p9260Clr,
       "dpsRTUv2p9321Clr": dpsRTUv2p9321Clr,
       "dpsRTUv2p9322Clr": dpsRTUv2p9322Clr,
       "dpsRTUv2p9323Clr": dpsRTUv2p9323Clr,
       "dpsRTUv2p9324Clr": dpsRTUv2p9324Clr,
       "dpsRTUv2p9385Clr": dpsRTUv2p9385Clr,
       "dpsRTUv2p9386Clr": dpsRTUv2p9386Clr,
       "dpsRTUv2p9387Clr": dpsRTUv2p9387Clr,
       "dpsRTUv2p9388Clr": dpsRTUv2p9388Clr,
       "dpsRTUv2p9449Clr": dpsRTUv2p9449Clr,
       "dpsRTUv2p9450Clr": dpsRTUv2p9450Clr,
       "dpsRTUv2p9451Clr": dpsRTUv2p9451Clr,
       "dpsRTUv2p9452Clr": dpsRTUv2p9452Clr,
       "dpsRTUv2p9513Clr": dpsRTUv2p9513Clr,
       "dpsRTUv2p9514Clr": dpsRTUv2p9514Clr,
       "dpsRTUv2p9515Clr": dpsRTUv2p9515Clr,
       "dpsRTUv2p9516Clr": dpsRTUv2p9516Clr,
       "dpsRTUv2p9577Clr": dpsRTUv2p9577Clr,
       "dpsRTUv2p9578Clr": dpsRTUv2p9578Clr,
       "dpsRTUv2p9579Clr": dpsRTUv2p9579Clr,
       "dpsRTUv2p9580Clr": dpsRTUv2p9580Clr,
       "dpsRTUv2p9641Clr": dpsRTUv2p9641Clr,
       "dpsRTUv2p9642Clr": dpsRTUv2p9642Clr,
       "dpsRTUv2p9657Clr": dpsRTUv2p9657Clr,
       "dpsRTUv2p9659Clr": dpsRTUv2p9659Clr,
       "dpsRTUv2p9660Clr": dpsRTUv2p9660Clr,
       "dpsRTUv2p9661Clr": dpsRTUv2p9661Clr,
       "dpsRTUv2p9662Clr": dpsRTUv2p9662Clr,
       "dpsRTUv2p9673Clr": dpsRTUv2p9673Clr,
       "dpsRTUv2p9676Clr": dpsRTUv2p9676Clr,
       "dpsRTUv2p9677Clr": dpsRTUv2p9677Clr,
       "dpsRTUv2p9678Clr": dpsRTUv2p9678Clr,
       "dpsRTUv2p9679Clr": dpsRTUv2p9679Clr,
       "dpsRTUv2p9680Clr": dpsRTUv2p9680Clr,
       "dpsRTUv2p9683Clr": dpsRTUv2p9683Clr,
       "dpsRTUv2p9684Clr": dpsRTUv2p9684Clr,
       "dpsRTUv2p9685Clr": dpsRTUv2p9685Clr,
       "dpsRTUv2p9686Clr": dpsRTUv2p9686Clr,
       "dpsRTUv2p9688Clr": dpsRTUv2p9688Clr,
       "dpsRTUv2p9696Clr": dpsRTUv2p9696Clr,
       "dpsRTUv2p9697Clr": dpsRTUv2p9697Clr,
       "dpsRTUv2p9698Clr": dpsRTUv2p9698Clr,
       "dpsRTUv2p9703Clr": dpsRTUv2p9703Clr,
       "dpsRTUv2p9704Clr": dpsRTUv2p9704Clr}
)
