# SNMP MIB module (ZXPW-TC-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXPW-TC-STD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:43 2025
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

(zxAnCesMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnCesMib")


# MODULE-IDENTITY

zxPwTcStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwGroupID(TextualConvention, Unsigned32):
    status = "current"


class PwIDType(TextualConvention, Unsigned32):
    status = "current"


class PwIndexType(TextualConvention, Unsigned32):
    status = "current"


class PwVlanCfg(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )



class PwOperStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )



class PwAttachmentIdentifierType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PwCwStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("waitingForNextMsg", 1),
          ("sentWrongBitErrorCode", 2),
          ("rxWithdrawWithWrongBitErrorCode", 3),
          ("illegalReceivedBit", 4),
          ("cwPresent", 5),
          ("cwNotPresent", 6),
          ("notYetKnown", 7))
    )



class PwCapabilities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("pwStatusIndication", 0)
    )


class PwStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pwNotForwarding", 0),
          ("customerFacingPwRxFault", 1),
          ("customerFacingPwTxFault", 2),
          ("psnFacingPwRxFault", 3),
          ("psnFacingPwTxFault", 4))
    )


class PwFragSize(TextualConvention, Unsigned32):
    status = "current"


class PwFragStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("noFrag", 0),
          ("cfgFragGreaterThanPsnMtu", 1),
          ("cfgFragButRemoteIncapable", 2),
          ("remoteFragCapable", 3),
          ("fragEnabled", 4))
    )


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXPW-TC-STD-MIB",
    **{"PwGroupID": PwGroupID,
       "PwIDType": PwIDType,
       "PwIndexType": PwIndexType,
       "PwVlanCfg": PwVlanCfg,
       "PwOperStatusTC": PwOperStatusTC,
       "PwAttachmentIdentifierType": PwAttachmentIdentifierType,
       "PwCwStatusTC": PwCwStatusTC,
       "PwCapabilities": PwCapabilities,
       "PwStatus": PwStatus,
       "PwFragSize": PwFragSize,
       "PwFragStatus": PwFragStatus,
       "zxPwTcStdMIB": zxPwTcStdMIB}
)
