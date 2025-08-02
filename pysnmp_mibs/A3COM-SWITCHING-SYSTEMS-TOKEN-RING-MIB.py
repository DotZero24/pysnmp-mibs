_H='a3ComSysTokenRingPortIndex'
_G='A3COM-SWITCHING-SYSTEMS-TOKEN-RING-MIB'
_F='DisplayString'
_E='NotificationType'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComSysTokenRingPort_ObjectIdentity=ObjectIdentity
a3ComSysTokenRingPort=_A3ComSysTokenRingPort_ObjectIdentity((1,3,6,1,4,1,43,29,4,13))
_A3ComSysTokenRingPortCount_Type=Integer32
_A3ComSysTokenRingPortCount_Object=MibScalar
a3ComSysTokenRingPortCount=_A3ComSysTokenRingPortCount_Object((1,3,6,1,4,1,43,29,4,13,1),_A3ComSysTokenRingPortCount_Type())
a3ComSysTokenRingPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortCount.setStatus(_A)
_A3ComSysTokenRingPortTable_Object=MibTable
a3ComSysTokenRingPortTable=_A3ComSysTokenRingPortTable_Object((1,3,6,1,4,1,43,29,4,13,2))
if mibBuilder.loadTexts:a3ComSysTokenRingPortTable.setStatus(_A)
_A3ComSysTokenRingPortEntry_Object=MibTableRow
a3ComSysTokenRingPortEntry=_A3ComSysTokenRingPortEntry_Object((1,3,6,1,4,1,43,29,4,13,2,1))
a3ComSysTokenRingPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:a3ComSysTokenRingPortEntry.setStatus(_A)
class _A3ComSysTokenRingPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysTokenRingPortIndex_Type.__name__=_C
_A3ComSysTokenRingPortIndex_Object=MibTableColumn
a3ComSysTokenRingPortIndex=_A3ComSysTokenRingPortIndex_Object((1,3,6,1,4,1,43,29,4,13,2,1,1),_A3ComSysTokenRingPortIndex_Type())
a3ComSysTokenRingPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortIndex.setStatus(_A)
class _A3ComSysTokenRingPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysTokenRingPortIfIndex_Type.__name__=_C
_A3ComSysTokenRingPortIfIndex_Object=MibTableColumn
a3ComSysTokenRingPortIfIndex=_A3ComSysTokenRingPortIfIndex_Object((1,3,6,1,4,1,43,29,4,13,2,1,2),_A3ComSysTokenRingPortIfIndex_Type())
a3ComSysTokenRingPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortIfIndex.setStatus(_A)
class _A3ComSysTokenRingPortLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_A3ComSysTokenRingPortLabel_Type.__name__=_F
_A3ComSysTokenRingPortLabel_Object=MibTableColumn
a3ComSysTokenRingPortLabel=_A3ComSysTokenRingPortLabel_Object((1,3,6,1,4,1,43,29,4,13,2,1,3),_A3ComSysTokenRingPortLabel_Type())
a3ComSysTokenRingPortLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysTokenRingPortLabel.setStatus(_A)
class _A3ComSysTokenRingPortInsertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inserted',1),('deinserted',2)))
_A3ComSysTokenRingPortInsertStatus_Type.__name__=_C
_A3ComSysTokenRingPortInsertStatus_Object=MibTableColumn
a3ComSysTokenRingPortInsertStatus=_A3ComSysTokenRingPortInsertStatus_Object((1,3,6,1,4,1,43,29,4,13,2,1,4),_A3ComSysTokenRingPortInsertStatus_Type())
a3ComSysTokenRingPortInsertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortInsertStatus.setStatus(_A)
class _A3ComSysTokenRingPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rj45',1),('other',2)))
_A3ComSysTokenRingPortType_Type.__name__=_C
_A3ComSysTokenRingPortType_Object=MibTableColumn
a3ComSysTokenRingPortType=_A3ComSysTokenRingPortType_Object((1,3,6,1,4,1,43,29,4,13,2,1,5),_A3ComSysTokenRingPortType_Type())
a3ComSysTokenRingPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortType.setStatus(_A)
class _A3ComSysTokenRingPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('station',1),('lobe',2)))
_A3ComSysTokenRingPortMode_Type.__name__=_C
_A3ComSysTokenRingPortMode_Object=MibTableColumn
a3ComSysTokenRingPortMode=_A3ComSysTokenRingPortMode_Object((1,3,6,1,4,1,43,29,4,13,2,1,6),_A3ComSysTokenRingPortMode_Type())
a3ComSysTokenRingPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysTokenRingPortMode.setStatus(_A)
class _A3ComSysTokenRingPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fourMegabit',1),('sixteenMegabit',2),('sixteenMegabitETR',3)))
_A3ComSysTokenRingPortSpeed_Type.__name__=_C
_A3ComSysTokenRingPortSpeed_Object=MibTableColumn
a3ComSysTokenRingPortSpeed=_A3ComSysTokenRingPortSpeed_Object((1,3,6,1,4,1,43,29,4,13,2,1,7),_A3ComSysTokenRingPortSpeed_Type())
a3ComSysTokenRingPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysTokenRingPortSpeed.setStatus(_A)
_A3ComSysTokenRingPortLineErrors_Type=Counter32
_A3ComSysTokenRingPortLineErrors_Object=MibTableColumn
a3ComSysTokenRingPortLineErrors=_A3ComSysTokenRingPortLineErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,8),_A3ComSysTokenRingPortLineErrors_Type())
a3ComSysTokenRingPortLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortLineErrors.setStatus(_A)
_A3ComSysTokenRingPortBurstErrors_Type=Counter32
_A3ComSysTokenRingPortBurstErrors_Object=MibTableColumn
a3ComSysTokenRingPortBurstErrors=_A3ComSysTokenRingPortBurstErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,9),_A3ComSysTokenRingPortBurstErrors_Type())
a3ComSysTokenRingPortBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortBurstErrors.setStatus(_A)
_A3ComSysTokenRingPortACErrors_Type=Counter32
_A3ComSysTokenRingPortACErrors_Object=MibTableColumn
a3ComSysTokenRingPortACErrors=_A3ComSysTokenRingPortACErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,10),_A3ComSysTokenRingPortACErrors_Type())
a3ComSysTokenRingPortACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortACErrors.setStatus(_A)
_A3ComSysTokenRingPortAbortTransErrors_Type=Counter32
_A3ComSysTokenRingPortAbortTransErrors_Object=MibTableColumn
a3ComSysTokenRingPortAbortTransErrors=_A3ComSysTokenRingPortAbortTransErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,11),_A3ComSysTokenRingPortAbortTransErrors_Type())
a3ComSysTokenRingPortAbortTransErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortAbortTransErrors.setStatus(_A)
_A3ComSysTokenRingPortInternalErrors_Type=Counter32
_A3ComSysTokenRingPortInternalErrors_Object=MibTableColumn
a3ComSysTokenRingPortInternalErrors=_A3ComSysTokenRingPortInternalErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,12),_A3ComSysTokenRingPortInternalErrors_Type())
a3ComSysTokenRingPortInternalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortInternalErrors.setStatus(_A)
_A3ComSysTokenRingPortLostFrameErrors_Type=Counter32
_A3ComSysTokenRingPortLostFrameErrors_Object=MibTableColumn
a3ComSysTokenRingPortLostFrameErrors=_A3ComSysTokenRingPortLostFrameErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,13),_A3ComSysTokenRingPortLostFrameErrors_Type())
a3ComSysTokenRingPortLostFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortLostFrameErrors.setStatus(_A)
_A3ComSysTokenRingPortReceiveCongestionErrors_Type=Counter32
_A3ComSysTokenRingPortReceiveCongestionErrors_Object=MibTableColumn
a3ComSysTokenRingPortReceiveCongestionErrors=_A3ComSysTokenRingPortReceiveCongestionErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,14),_A3ComSysTokenRingPortReceiveCongestionErrors_Type())
a3ComSysTokenRingPortReceiveCongestionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortReceiveCongestionErrors.setStatus(_A)
_A3ComSysTokenRingPortFrameCopiedErrors_Type=Counter32
_A3ComSysTokenRingPortFrameCopiedErrors_Object=MibTableColumn
a3ComSysTokenRingPortFrameCopiedErrors=_A3ComSysTokenRingPortFrameCopiedErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,15),_A3ComSysTokenRingPortFrameCopiedErrors_Type())
a3ComSysTokenRingPortFrameCopiedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortFrameCopiedErrors.setStatus(_A)
_A3ComSysTokenRingPortTokenErrors_Type=Counter32
_A3ComSysTokenRingPortTokenErrors_Object=MibTableColumn
a3ComSysTokenRingPortTokenErrors=_A3ComSysTokenRingPortTokenErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,16),_A3ComSysTokenRingPortTokenErrors_Type())
a3ComSysTokenRingPortTokenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortTokenErrors.setStatus(_A)
_A3ComSysTokenRingPortSoftErrors_Type=Counter32
_A3ComSysTokenRingPortSoftErrors_Object=MibTableColumn
a3ComSysTokenRingPortSoftErrors=_A3ComSysTokenRingPortSoftErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,17),_A3ComSysTokenRingPortSoftErrors_Type())
a3ComSysTokenRingPortSoftErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortSoftErrors.setStatus(_A)
_A3ComSysTokenRingPortHardErrors_Type=Counter32
_A3ComSysTokenRingPortHardErrors_Object=MibTableColumn
a3ComSysTokenRingPortHardErrors=_A3ComSysTokenRingPortHardErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,18),_A3ComSysTokenRingPortHardErrors_Type())
a3ComSysTokenRingPortHardErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortHardErrors.setStatus(_A)
_A3ComSysTokenRingPortTransmitBeacons_Type=Counter32
_A3ComSysTokenRingPortTransmitBeacons_Object=MibTableColumn
a3ComSysTokenRingPortTransmitBeacons=_A3ComSysTokenRingPortTransmitBeacons_Object((1,3,6,1,4,1,43,29,4,13,2,1,19),_A3ComSysTokenRingPortTransmitBeacons_Type())
a3ComSysTokenRingPortTransmitBeacons.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortTransmitBeacons.setStatus(_A)
_A3ComSysTokenRingPortLobeWires_Type=Counter32
_A3ComSysTokenRingPortLobeWires_Object=MibTableColumn
a3ComSysTokenRingPortLobeWires=_A3ComSysTokenRingPortLobeWires_Object((1,3,6,1,4,1,43,29,4,13,2,1,20),_A3ComSysTokenRingPortLobeWires_Type())
a3ComSysTokenRingPortLobeWires.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortLobeWires.setStatus(_A)
_A3ComSysTokenRingPortRemoves_Type=Counter32
_A3ComSysTokenRingPortRemoves_Object=MibTableColumn
a3ComSysTokenRingPortRemoves=_A3ComSysTokenRingPortRemoves_Object((1,3,6,1,4,1,43,29,4,13,2,1,21),_A3ComSysTokenRingPortRemoves_Type())
a3ComSysTokenRingPortRemoves.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortRemoves.setStatus(_A)
_A3ComSysTokenRingPortSingles_Type=Counter32
_A3ComSysTokenRingPortSingles_Object=MibTableColumn
a3ComSysTokenRingPortSingles=_A3ComSysTokenRingPortSingles_Object((1,3,6,1,4,1,43,29,4,13,2,1,22),_A3ComSysTokenRingPortSingles_Type())
a3ComSysTokenRingPortSingles.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortSingles.setStatus(_A)
_A3ComSysTokenRingPortFreqErrors_Type=Counter32
_A3ComSysTokenRingPortFreqErrors_Object=MibTableColumn
a3ComSysTokenRingPortFreqErrors=_A3ComSysTokenRingPortFreqErrors_Object((1,3,6,1,4,1,43,29,4,13,2,1,23),_A3ComSysTokenRingPortFreqErrors_Type())
a3ComSysTokenRingPortFreqErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortFreqErrors.setStatus(_A)
_A3ComSysTokenRingPortRingStatus_Type=Integer32
_A3ComSysTokenRingPortRingStatus_Object=MibTableColumn
a3ComSysTokenRingPortRingStatus=_A3ComSysTokenRingPortRingStatus_Object((1,3,6,1,4,1,43,29,4,13,2,1,24),_A3ComSysTokenRingPortRingStatus_Type())
a3ComSysTokenRingPortRingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysTokenRingPortRingStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComSysTokenRingPort':a3ComSysTokenRingPort,'a3ComSysTokenRingPortCount':a3ComSysTokenRingPortCount,'a3ComSysTokenRingPortTable':a3ComSysTokenRingPortTable,'a3ComSysTokenRingPortEntry':a3ComSysTokenRingPortEntry,_H:a3ComSysTokenRingPortIndex,'a3ComSysTokenRingPortIfIndex':a3ComSysTokenRingPortIfIndex,'a3ComSysTokenRingPortLabel':a3ComSysTokenRingPortLabel,'a3ComSysTokenRingPortInsertStatus':a3ComSysTokenRingPortInsertStatus,'a3ComSysTokenRingPortType':a3ComSysTokenRingPortType,'a3ComSysTokenRingPortMode':a3ComSysTokenRingPortMode,'a3ComSysTokenRingPortSpeed':a3ComSysTokenRingPortSpeed,'a3ComSysTokenRingPortLineErrors':a3ComSysTokenRingPortLineErrors,'a3ComSysTokenRingPortBurstErrors':a3ComSysTokenRingPortBurstErrors,'a3ComSysTokenRingPortACErrors':a3ComSysTokenRingPortACErrors,'a3ComSysTokenRingPortAbortTransErrors':a3ComSysTokenRingPortAbortTransErrors,'a3ComSysTokenRingPortInternalErrors':a3ComSysTokenRingPortInternalErrors,'a3ComSysTokenRingPortLostFrameErrors':a3ComSysTokenRingPortLostFrameErrors,'a3ComSysTokenRingPortReceiveCongestionErrors':a3ComSysTokenRingPortReceiveCongestionErrors,'a3ComSysTokenRingPortFrameCopiedErrors':a3ComSysTokenRingPortFrameCopiedErrors,'a3ComSysTokenRingPortTokenErrors':a3ComSysTokenRingPortTokenErrors,'a3ComSysTokenRingPortSoftErrors':a3ComSysTokenRingPortSoftErrors,'a3ComSysTokenRingPortHardErrors':a3ComSysTokenRingPortHardErrors,'a3ComSysTokenRingPortTransmitBeacons':a3ComSysTokenRingPortTransmitBeacons,'a3ComSysTokenRingPortLobeWires':a3ComSysTokenRingPortLobeWires,'a3ComSysTokenRingPortRemoves':a3ComSysTokenRingPortRemoves,'a3ComSysTokenRingPortSingles':a3ComSysTokenRingPortSingles,'a3ComSysTokenRingPortFreqErrors':a3ComSysTokenRingPortFreqErrors,'a3ComSysTokenRingPortRingStatus':a3ComSysTokenRingPortRingStatus})