_K='nbsFanFanSpeed'
_J='DisplayString'
_I='Integer32'
_H='nbsFanFanStatus'
_G='nbsFanFanDescription'
_F='nbsFanFanIndex'
_E='nbsFanFanParentPartIndex'
_D='nbsFanFanParentIfIndex'
_C='read-only'
_B='current'
_A='NBS-FAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
NbsTcPartIndex,NbsTcStatusSimple,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcPartIndex','NbsTcStatusSimple','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
nbsFanMib=ModuleIdentity((1,3,6,1,4,1,629,226))
_NbsFanFanGrp_ObjectIdentity=ObjectIdentity
nbsFanFanGrp=_NbsFanFanGrp_ObjectIdentity((1,3,6,1,4,1,629,226,1))
if mibBuilder.loadTexts:nbsFanFanGrp.setStatus(_B)
_NbsFanFanTable_Object=MibTable
nbsFanFanTable=_NbsFanFanTable_Object((1,3,6,1,4,1,629,226,1,1))
if mibBuilder.loadTexts:nbsFanFanTable.setStatus(_B)
_NbsFanFanEntry_Object=MibTableRow
nbsFanFanEntry=_NbsFanFanEntry_Object((1,3,6,1,4,1,629,226,1,1,1))
nbsFanFanEntry.setIndexNames((0,_A,_D),(0,_A,_E),(0,_A,_F))
if mibBuilder.loadTexts:nbsFanFanEntry.setStatus(_B)
_NbsFanFanParentIfIndex_Type=InterfaceIndex
_NbsFanFanParentIfIndex_Object=MibTableColumn
nbsFanFanParentIfIndex=_NbsFanFanParentIfIndex_Object((1,3,6,1,4,1,629,226,1,1,1,1),_NbsFanFanParentIfIndex_Type())
nbsFanFanParentIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsFanFanParentIfIndex.setStatus(_B)
_NbsFanFanParentPartIndex_Type=NbsTcPartIndex
_NbsFanFanParentPartIndex_Object=MibTableColumn
nbsFanFanParentPartIndex=_NbsFanFanParentPartIndex_Object((1,3,6,1,4,1,629,226,1,1,1,2),_NbsFanFanParentPartIndex_Type())
nbsFanFanParentPartIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsFanFanParentPartIndex.setStatus(_B)
_NbsFanFanIndex_Type=Integer32
_NbsFanFanIndex_Object=MibTableColumn
nbsFanFanIndex=_NbsFanFanIndex_Object((1,3,6,1,4,1,629,226,1,1,1,3),_NbsFanFanIndex_Type())
nbsFanFanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsFanFanIndex.setStatus(_B)
class _NbsFanFanDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsFanFanDescription_Type.__name__=_J
_NbsFanFanDescription_Object=MibTableColumn
nbsFanFanDescription=_NbsFanFanDescription_Object((1,3,6,1,4,1,629,226,1,1,1,10),_NbsFanFanDescription_Type())
nbsFanFanDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsFanFanDescription.setStatus(_B)
_NbsFanFanStatus_Type=NbsTcStatusSimple
_NbsFanFanStatus_Object=MibTableColumn
nbsFanFanStatus=_NbsFanFanStatus_Object((1,3,6,1,4,1,629,226,1,1,1,30),_NbsFanFanStatus_Type())
nbsFanFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsFanFanStatus.setStatus(_B)
class _NbsFanFanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notSupported',1),('off',2),('low',3),('medium',4),('high',5)))
_NbsFanFanSpeed_Type.__name__=_I
_NbsFanFanSpeed_Object=MibTableColumn
nbsFanFanSpeed=_NbsFanFanSpeed_Object((1,3,6,1,4,1,629,226,1,1,1,40),_NbsFanFanSpeed_Type())
nbsFanFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsFanFanSpeed.setStatus(_B)
_NbsFanFanTableSize_Type=Integer32
_NbsFanFanTableSize_Object=MibScalar
nbsFanFanTableSize=_NbsFanFanTableSize_Object((1,3,6,1,4,1,629,226,1,2),_NbsFanFanTableSize_Type())
nbsFanFanTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsFanFanTableSize.setStatus(_B)
_NbsFanEventsGrp_ObjectIdentity=ObjectIdentity
nbsFanEventsGrp=_NbsFanEventsGrp_ObjectIdentity((1,3,6,1,4,1,629,226,100))
if mibBuilder.loadTexts:nbsFanEventsGrp.setStatus(_B)
_NbsFanEvents_ObjectIdentity=ObjectIdentity
nbsFanEvents=_NbsFanEvents_ObjectIdentity((1,3,6,1,4,1,629,226,100,0))
if mibBuilder.loadTexts:nbsFanEvents.setStatus(_B)
nbsFanTrapFanStatusBad=NotificationType((1,3,6,1,4,1,629,226,100,0,30))
nbsFanTrapFanStatusBad.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:nbsFanTrapFanStatusBad.setStatus(_B)
nbsFanTrapFanStatusOk=NotificationType((1,3,6,1,4,1,629,226,100,0,31))
nbsFanTrapFanStatusOk.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:nbsFanTrapFanStatusOk.setStatus(_B)
nbsFanTrapFanSpeedChanged=NotificationType((1,3,6,1,4,1,629,226,100,0,40))
nbsFanTrapFanSpeedChanged.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:nbsFanTrapFanSpeedChanged.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nbsFanMib':nbsFanMib,'nbsFanFanGrp':nbsFanFanGrp,'nbsFanFanTable':nbsFanFanTable,'nbsFanFanEntry':nbsFanFanEntry,_D:nbsFanFanParentIfIndex,_E:nbsFanFanParentPartIndex,_F:nbsFanFanIndex,_G:nbsFanFanDescription,_H:nbsFanFanStatus,_K:nbsFanFanSpeed,'nbsFanFanTableSize':nbsFanFanTableSize,'nbsFanEventsGrp':nbsFanEventsGrp,'nbsFanEvents':nbsFanEvents,'nbsFanTrapFanStatusBad':nbsFanTrapFanStatusBad,'nbsFanTrapFanStatusOk':nbsFanTrapFanStatusOk,'nbsFanTrapFanSpeedChanged':nbsFanTrapFanSpeedChanged})