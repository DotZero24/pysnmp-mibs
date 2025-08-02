_J='cesOverWlanUnit0PortMap'
_I='cesOverWlanUnit0BandwithLimit'
_H='cesOverWlanUnit0FramesPerPacket'
_G='cesOverWlanUnit0MaxJitter'
_F='cesOverWlanUnit0Mode'
_E='cesOverWlanUnit0Enabled'
_D='Integer32'
_C='read-write'
_B='INFINET-EXTCES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
externalDevices,=mibBuilder.importSymbols('INFINET-EXTDEVICES-MIB','externalDevices')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cesOverWlan=ModuleIdentity((1,3,6,1,4,1,3942,2,1))
if mibBuilder.loadTexts:cesOverWlan.setRevisions(('2007-06-18 19:10',))
_CesOverWlanUnit0_ObjectIdentity=ObjectIdentity
cesOverWlanUnit0=_CesOverWlanUnit0_ObjectIdentity((1,3,6,1,4,1,3942,2,1,1))
_CesOverWlanUnit0Settings_ObjectIdentity=ObjectIdentity
cesOverWlanUnit0Settings=_CesOverWlanUnit0Settings_ObjectIdentity((1,3,6,1,4,1,3942,2,1,1,1))
class _CesOverWlanUnit0Enabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CesOverWlanUnit0Enabled_Type.__name__=_D
_CesOverWlanUnit0Enabled_Object=MibScalar
cesOverWlanUnit0Enabled=_CesOverWlanUnit0Enabled_Object((1,3,6,1,4,1,3942,2,1,1,1,1),_CesOverWlanUnit0Enabled_Type())
cesOverWlanUnit0Enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0Enabled.setStatus(_A)
class _CesOverWlanUnit0Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,6,8,9,10)));namedValues=NamedValues(*(('e1-internal',0),('e1-loopback',2),('e1-recovery',3),('e1-line',4),('t1-internal',6),('t1-loopback',8),('t1-recovery',9),('t1-line',10)))
_CesOverWlanUnit0Mode_Type.__name__=_D
_CesOverWlanUnit0Mode_Object=MibScalar
cesOverWlanUnit0Mode=_CesOverWlanUnit0Mode_Object((1,3,6,1,4,1,3942,2,1,1,1,2),_CesOverWlanUnit0Mode_Type())
cesOverWlanUnit0Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0Mode.setStatus(_A)
class _CesOverWlanUnit0MaxJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_CesOverWlanUnit0MaxJitter_Type.__name__=_D
_CesOverWlanUnit0MaxJitter_Object=MibScalar
cesOverWlanUnit0MaxJitter=_CesOverWlanUnit0MaxJitter_Object((1,3,6,1,4,1,3942,2,1,1,1,3),_CesOverWlanUnit0MaxJitter_Type())
cesOverWlanUnit0MaxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0MaxJitter.setStatus(_A)
if mibBuilder.loadTexts:cesOverWlanUnit0MaxJitter.setUnits('milliseconds')
class _CesOverWlanUnit0FramesPerPacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CesOverWlanUnit0FramesPerPacket_Type.__name__=_D
_CesOverWlanUnit0FramesPerPacket_Object=MibScalar
cesOverWlanUnit0FramesPerPacket=_CesOverWlanUnit0FramesPerPacket_Object((1,3,6,1,4,1,3942,2,1,1,1,4),_CesOverWlanUnit0FramesPerPacket_Type())
cesOverWlanUnit0FramesPerPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0FramesPerPacket.setStatus(_A)
if mibBuilder.loadTexts:cesOverWlanUnit0FramesPerPacket.setUnits('frames')
_CesOverWlanUnit0BandwithLimit_Type=Unsigned32
_CesOverWlanUnit0BandwithLimit_Object=MibScalar
cesOverWlanUnit0BandwithLimit=_CesOverWlanUnit0BandwithLimit_Object((1,3,6,1,4,1,3942,2,1,1,1,5),_CesOverWlanUnit0BandwithLimit_Type())
cesOverWlanUnit0BandwithLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0BandwithLimit.setStatus(_A)
_CesOverWlanUnit0PortMap_Type=Unsigned32
_CesOverWlanUnit0PortMap_Object=MibScalar
cesOverWlanUnit0PortMap=_CesOverWlanUnit0PortMap_Object((1,3,6,1,4,1,3942,2,1,1,1,6),_CesOverWlanUnit0PortMap_Type())
cesOverWlanUnit0PortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOverWlanUnit0PortMap.setStatus(_A)
_CesOverWlanMIBConformance_ObjectIdentity=ObjectIdentity
cesOverWlanMIBConformance=_CesOverWlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,2,1,2))
cesOverWlanGroups=ObjectGroup((1,3,6,1,4,1,3942,2,1,2,1))
cesOverWlanGroups.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cesOverWlanGroups.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cesOverWlan':cesOverWlan,'cesOverWlanUnit0':cesOverWlanUnit0,'cesOverWlanUnit0Settings':cesOverWlanUnit0Settings,_E:cesOverWlanUnit0Enabled,_F:cesOverWlanUnit0Mode,_G:cesOverWlanUnit0MaxJitter,_H:cesOverWlanUnit0FramesPerPacket,_I:cesOverWlanUnit0BandwithLimit,_J:cesOverWlanUnit0PortMap,'cesOverWlanMIBConformance':cesOverWlanMIBConformance,'cesOverWlanGroups':cesOverWlanGroups})