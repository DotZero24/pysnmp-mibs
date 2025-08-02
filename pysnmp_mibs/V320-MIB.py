_P='terminalTemperatureLowTrap'
_O='terminalTemperatureHighTrap'
_N='terminalLinkQualityReducedTrap'
_M='terminalLinkQualityImprovedTrap'
_L='terminalAuxVoltage'
_K='terminalFirmwareversion'
_J='terminalLockDetector'
_I='terminalLinkQuality'
_H='terminalReceivePower'
_G='terminalLinkQualityImproved'
_F='terminalLinkQualityReduced'
_E='terminalTemperature'
_D='Integer32'
_C='read-only'
_B='current'
_A='V320-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sub10OID=ModuleIdentity((1,3,6,1,4,1,39003))
if mibBuilder.loadTexts:sub10OID.setRevisions(('2011-11-29 00:00',))
_Terminal2_ObjectIdentity=ObjectIdentity
terminal2=_Terminal2_ObjectIdentity((1,3,6,1,4,1,39003,2))
class _TerminalLinkQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10)));namedValues=NamedValues(*(('green',1),('yellow',2),('red',3),('unknown',10)))
_TerminalLinkQuality_Type.__name__=_D
_TerminalLinkQuality_Object=MibScalar
terminalLinkQuality=_TerminalLinkQuality_Object((1,3,6,1,4,1,39003,2,1),_TerminalLinkQuality_Type())
terminalLinkQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalLinkQuality.setStatus(_B)
_TerminalReceivePower_Type=Integer32
_TerminalReceivePower_Object=MibScalar
terminalReceivePower=_TerminalReceivePower_Object((1,3,6,1,4,1,39003,2,10),_TerminalReceivePower_Type())
terminalReceivePower.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalReceivePower.setStatus(_B)
_TerminalTemperature_Type=Integer32
_TerminalTemperature_Object=MibScalar
terminalTemperature=_TerminalTemperature_Object((1,3,6,1,4,1,39003,2,11),_TerminalTemperature_Type())
terminalTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalTemperature.setStatus(_B)
_TerminalLockDetector_Type=Integer32
_TerminalLockDetector_Object=MibScalar
terminalLockDetector=_TerminalLockDetector_Object((1,3,6,1,4,1,39003,2,12),_TerminalLockDetector_Type())
terminalLockDetector.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalLockDetector.setStatus(_B)
class _TerminalLinkQualityImproved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('red2green',1),('red2yellow',2),('yellow2green',3)))
_TerminalLinkQualityImproved_Type.__name__=_D
_TerminalLinkQualityImproved_Object=MibScalar
terminalLinkQualityImproved=_TerminalLinkQualityImproved_Object((1,3,6,1,4,1,39003,2,13),_TerminalLinkQualityImproved_Type())
terminalLinkQualityImproved.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalLinkQualityImproved.setStatus(_B)
class _TerminalLinkQualityReduced_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green2yellow',1),('green2red',2),('yellow2red',3)))
_TerminalLinkQualityReduced_Type.__name__=_D
_TerminalLinkQualityReduced_Object=MibScalar
terminalLinkQualityReduced=_TerminalLinkQualityReduced_Object((1,3,6,1,4,1,39003,2,14),_TerminalLinkQualityReduced_Type())
terminalLinkQualityReduced.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalLinkQualityReduced.setStatus(_B)
_TerminalFirmwareversion_Type=OctetString
_TerminalFirmwareversion_Object=MibScalar
terminalFirmwareversion=_TerminalFirmwareversion_Object((1,3,6,1,4,1,39003,2,21),_TerminalFirmwareversion_Type())
terminalFirmwareversion.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalFirmwareversion.setStatus(_B)
_TerminalTraps_ObjectIdentity=ObjectIdentity
terminalTraps=_TerminalTraps_ObjectIdentity((1,3,6,1,4,1,39003,2,22))
_TerminalAuxVoltage_Type=OctetString
_TerminalAuxVoltage_Object=MibScalar
terminalAuxVoltage=_TerminalAuxVoltage_Object((1,3,6,1,4,1,39003,2,25),_TerminalAuxVoltage_Type())
terminalAuxVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:terminalAuxVoltage.setStatus(_B)
terminalObjectGroup=ObjectGroup((1,3,6,1,4,1,39003,2,24))
terminalObjectGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_E),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:terminalObjectGroup.setStatus(_B)
terminalLinkQualityImprovedTrap=NotificationType((1,3,6,1,4,1,39003,2,22,1))
terminalLinkQualityImprovedTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:terminalLinkQualityImprovedTrap.setStatus(_B)
terminalLinkQualityReducedTrap=NotificationType((1,3,6,1,4,1,39003,2,22,2))
terminalLinkQualityReducedTrap.setObjects((_A,_F))
if mibBuilder.loadTexts:terminalLinkQualityReducedTrap.setStatus(_B)
terminalTemperatureHighTrap=NotificationType((1,3,6,1,4,1,39003,2,22,3))
terminalTemperatureHighTrap.setObjects((_A,_E))
if mibBuilder.loadTexts:terminalTemperatureHighTrap.setStatus(_B)
terminalTemperatureLowTrap=NotificationType((1,3,6,1,4,1,39003,2,22,4))
terminalTemperatureLowTrap.setObjects((_A,_E))
if mibBuilder.loadTexts:terminalTemperatureLowTrap.setStatus(_B)
terminalNotificationGroup=NotificationGroup((1,3,6,1,4,1,39003,2,23))
terminalNotificationGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:terminalNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'sub10OID':sub10OID,'terminal2':terminal2,_I:terminalLinkQuality,_H:terminalReceivePower,_E:terminalTemperature,_J:terminalLockDetector,_G:terminalLinkQualityImproved,_F:terminalLinkQualityReduced,_K:terminalFirmwareversion,'terminalTraps':terminalTraps,_M:terminalLinkQualityImprovedTrap,_N:terminalLinkQualityReducedTrap,_O:terminalTemperatureHighTrap,_P:terminalTemperatureLowTrap,'terminalNotificationGroup':terminalNotificationGroup,'terminalObjectGroup':terminalObjectGroup,_L:terminalAuxVoltage})