if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rdnDefinitions,=mibBuilder.importSymbols('RDN-DEFINITIONS-MIB','rdnDefinitions')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdnSlots=ModuleIdentity((1,3,6,1,4,1,4981,4,3))
if mibBuilder.loadTexts:rdnSlots.setRevisions(('2008-08-08 00:00','2003-11-05 00:00','2003-04-29 00:00','2001-04-18 00:00'))
_RdnSlotsUnknown_ObjectIdentity=ObjectIdentity
rdnSlotsUnknown=_RdnSlotsUnknown_ObjectIdentity((1,3,6,1,4,1,4981,4,3,0))
_RdnSlotsBSR64000Master_ObjectIdentity=ObjectIdentity
rdnSlotsBSR64000Master=_RdnSlotsBSR64000Master_ObjectIdentity((1,3,6,1,4,1,4981,4,3,1))
_RdnSlotsBSR64000IO_ObjectIdentity=ObjectIdentity
rdnSlotsBSR64000IO=_RdnSlotsBSR64000IO_ObjectIdentity((1,3,6,1,4,1,4981,4,3,2))
_RdnSlotsBSR1000_ObjectIdentity=ObjectIdentity
rdnSlotsBSR1000=_RdnSlotsBSR1000_ObjectIdentity((1,3,6,1,4,1,4981,4,3,3))
_RdnSlotsOSR2000_ObjectIdentity=ObjectIdentity
rdnSlotsOSR2000=_RdnSlotsOSR2000_ObjectIdentity((1,3,6,1,4,1,4981,4,3,4))
mibBuilder.exportSymbols('RDN-SLOTS-MIB',**{'rdnSlots':rdnSlots,'rdnSlotsUnknown':rdnSlotsUnknown,'rdnSlotsBSR64000Master':rdnSlotsBSR64000Master,'rdnSlotsBSR64000IO':rdnSlotsBSR64000IO,'rdnSlotsBSR1000':rdnSlotsBSR1000,'rdnSlotsOSR2000':rdnSlotsOSR2000})