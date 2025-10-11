# SNMP MIB module (FS-NMSTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-NMSTRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:21 2025
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

(adslCPULoad,
 adslConfigAddr,
 adslLineUser,
 adslMemLoad,
 adslProductID,
 adslPtInCRC,
 adslPtInDrop,
 adslPtInError,
 adslPtInPkts,
 adslPtInSpeed,
 adslPtOutDrop,
 adslPtOutError,
 adslPtOutPkts,
 adslPtOutSpeed,
 adslPtSpeed,
 adslPtStatus) = mibBuilder.importSymbols(
    "FS-NMS-1705",
    "adslCPULoad",
    "adslConfigAddr",
    "adslLineUser",
    "adslMemLoad",
    "adslProductID",
    "adslPtInCRC",
    "adslPtInDrop",
    "adslPtInError",
    "adslPtInPkts",
    "adslPtInSpeed",
    "adslPtOutDrop",
    "adslPtOutError",
    "adslPtOutPkts",
    "adslPtOutSpeed",
    "adslPtSpeed",
    "adslPtStatus")

(nms,) = mibBuilder.importSymbols(
    "FS-NMS-SMI",
    "nms")

(ifDescr,
 ifIndex,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex",
    "ifType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
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

adslConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 0, 0)
)
adslConnection.setObjects(
      *(("FS-NMS-1705", "adslLineUser"),
        ("FS-NMS-1705", "adslProductID"),
        ("FS-NMS-1705", "adslConfigAddr"))
)
if mibBuilder.loadTexts:
    adslConnection.setStatus(
        ""
    )

adslPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 0, 1)
)
adslPeriod.setObjects(
      *(("FS-NMS-1705", "adslMemLoad"),
        ("FS-NMS-1705", "adslCPULoad"),
        ("FS-NMS-1705", "adslPtInCRC"),
        ("FS-NMS-1705", "adslPtStatus"),
        ("FS-NMS-1705", "adslPtSpeed"),
        ("FS-NMS-1705", "adslPtOutPkts"),
        ("FS-NMS-1705", "adslPtInPkts"),
        ("FS-NMS-1705", "adslPtOutError"),
        ("FS-NMS-1705", "adslPtInError"),
        ("FS-NMS-1705", "adslPtOutSpeed"),
        ("FS-NMS-1705", "adslPtInSpeed"),
        ("FS-NMS-1705", "adslPtOutDrop"),
        ("FS-NMS-1705", "adslPtInDrop"))
)
if mibBuilder.loadTexts:
    adslPeriod.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-NMSTRAP-MIB",
    **{"adslConnection": adslConnection,
       "adslPeriod": adslPeriod}
)
