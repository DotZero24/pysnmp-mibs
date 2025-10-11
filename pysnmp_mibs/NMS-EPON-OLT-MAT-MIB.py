# SNMP MIB module (NMS-EPON-OLT-MAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bdcom/NMS-EPON-OLT-MAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:05:20 2025
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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

_NmsEponOltMat_ObjectIdentity = ObjectIdentity
nmsEponOltMat = _NmsEponOltMat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 101, 200)
)
_OltFtpServerIpAddr_Type = IpAddress
_OltFtpServerIpAddr_Object = MibScalar
oltFtpServerIpAddr = _OltFtpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 101, 200, 1),
    _OltFtpServerIpAddr_Type()
)
oltFtpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltFtpServerIpAddr.setStatus("mandatory")
_OltFtpServerPort_Type = Integer32
_OltFtpServerPort_Object = MibScalar
oltFtpServerPort = _OltFtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3320, 101, 200, 2),
    _OltFtpServerPort_Type()
)
oltFtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltFtpServerPort.setStatus("mandatory")
_OltMatInsideIpAddr_Type = IpAddress
_OltMatInsideIpAddr_Object = MibScalar
oltMatInsideIpAddr = _OltMatInsideIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 101, 200, 3),
    _OltMatInsideIpAddr_Type()
)
oltMatInsideIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltMatInsideIpAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-OLT-MAT-MIB",
    **{"nmsEponOltMat": nmsEponOltMat,
       "oltFtpServerIpAddr": oltFtpServerIpAddr,
       "oltFtpServerPort": oltFtpServerPort,
       "oltMatInsideIpAddr": oltMatInsideIpAddr}
)
