# SNMP MIB module (GREENTECH-MASTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/gcom/GREENTECH-MASTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:50 2025
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

greentech = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464)
)
if mibBuilder.loadTexts:
    greentech.setRevisions(
        ("1900-08-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DataCom_ObjectIdentity = ObjectIdentity
dataCom = _DataCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1)
)
_Gbn_ObjectIdentity = ObjectIdentity
gbn = _Gbn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2)
)
_GbnPlatform_ObjectIdentity = ObjectIdentity
gbnPlatform = _GbnPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1)
)
_GbnDevice_ObjectIdentity = ObjectIdentity
gbnDevice = _GbnDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2)
)
_GbnService_ObjectIdentity = ObjectIdentity
gbnService = _GbnService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3)
)
_GbnServiceAAA_ObjectIdentity = ObjectIdentity
gbnServiceAAA = _GbnServiceAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 1)
)
_RmonMib_ObjectIdentity = ObjectIdentity
rmonMib = _RmonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2)
)
_GbnL2_ObjectIdentity = ObjectIdentity
gbnL2 = _GbnL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4)
)
_GbnL3_ObjectIdentity = ObjectIdentity
gbnL3 = _GbnL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5)
)
_GbnLS_ObjectIdentity = ObjectIdentity
gbnLS = _GbnLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 6)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GREENTECH-MASTER-MIB",
    **{"greentech": greentech,
       "dataCom": dataCom,
       "gbn": gbn,
       "gbnPlatform": gbnPlatform,
       "gbnDevice": gbnDevice,
       "gbnService": gbnService,
       "gbnServiceAAA": gbnServiceAAA,
       "rmonMib": rmonMib,
       "gbnL2": gbnL2,
       "gbnL3": gbnL3,
       "gbnLS": gbnLS,
       "switch": switch}
)
