if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rdnDefinitions,=mibBuilder.importSymbols('RDN-DEFINITIONS-MIB','rdnDefinitions')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdnChassisTypes=ModuleIdentity((1,3,6,1,4,1,4981,4,2))
if mibBuilder.loadTexts:rdnChassisTypes.setRevisions(('2008-08-08 00:00','2003-11-05 00:00','2003-04-29 00:00','2001-04-18 00:00'))
_RdnChassisTypesUnknown_ObjectIdentity=ObjectIdentity
rdnChassisTypesUnknown=_RdnChassisTypesUnknown_ObjectIdentity((1,3,6,1,4,1,4981,4,2,0))
_RdnChassisTypesBSR64000_ObjectIdentity=ObjectIdentity
rdnChassisTypesBSR64000=_RdnChassisTypesBSR64000_ObjectIdentity((1,3,6,1,4,1,4981,4,2,1))
_RdnChassisTypesBSR1000_ObjectIdentity=ObjectIdentity
rdnChassisTypesBSR1000=_RdnChassisTypesBSR1000_ObjectIdentity((1,3,6,1,4,1,4981,4,2,2))
_RdnChassisTypesOSR2000_ObjectIdentity=ObjectIdentity
rdnChassisTypesOSR2000=_RdnChassisTypesOSR2000_ObjectIdentity((1,3,6,1,4,1,4981,4,2,3))
mibBuilder.exportSymbols('RDN-CHASSIS-TYPE-MIB',**{'rdnChassisTypes':rdnChassisTypes,'rdnChassisTypesUnknown':rdnChassisTypesUnknown,'rdnChassisTypesBSR64000':rdnChassisTypesBSR64000,'rdnChassisTypesBSR1000':rdnChassisTypesBSR1000,'rdnChassisTypesOSR2000':rdnChassisTypesOSR2000})