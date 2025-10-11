# SNMP MIB module (BRCM-SNMP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-SNMP-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:53 2025
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

(cableDataMgmtBase,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtBase")

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

snmpMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    snmpMgmt.setRevisions(
        ("2007-02-05 00:00",
         "2006-10-05 00:00",
         "2003-04-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SnmpUdpPort_Type(Unsigned32):
    """Custom type snmpUdpPort based on Unsigned32"""
    defaultValue = 161

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpUdpPort_Type.__name__ = "Unsigned32"
_SnmpUdpPort_Object = MibScalar
snmpUdpPort = _SnmpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2, 1),
    _SnmpUdpPort_Type()
)
snmpUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUdpPort.setStatus("current")


class _SnmpNotifyUdpPort_Type(Unsigned32):
    """Custom type snmpNotifyUdpPort based on Unsigned32"""
    defaultValue = 162

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpNotifyUdpPort_Type.__name__ = "Unsigned32"
_SnmpNotifyUdpPort_Object = MibScalar
snmpNotifyUdpPort = _SnmpNotifyUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2, 2),
    _SnmpNotifyUdpPort_Type()
)
snmpNotifyUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNotifyUdpPort.setStatus("current")


class _SnmpDscpTag_Type(Integer32):
    """Custom type snmpDscpTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SnmpDscpTag_Type.__name__ = "Integer32"
_SnmpDscpTag_Object = MibScalar
snmpDscpTag = _SnmpDscpTag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2, 3),
    _SnmpDscpTag_Type()
)
snmpDscpTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDscpTag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-SNMP-MGMT-MIB",
    **{"snmpMgmt": snmpMgmt,
       "snmpUdpPort": snmpUdpPort,
       "snmpNotifyUdpPort": snmpNotifyUdpPort,
       "snmpDscpTag": snmpDscpTag}
)
