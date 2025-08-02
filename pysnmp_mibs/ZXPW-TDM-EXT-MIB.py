_J='zxPwTDMExtSlot'
_I='zxPwTDMExtShelf'
_H='zxPwTDMExtRack'
_G='zxPwIndex'
_F='ZXPW-STD-MIB'
_E='not-accessible'
_D='ZXPW-TDM-EXT-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxPwCTDM,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxPwCTDM')
IANAPwTypeTC,=mibBuilder.importSymbols('ZX-PWE3-MIB','IANAPwTypeTC')
zxPwIndex,=mibBuilder.importSymbols(_F,_G)
zxPwTDMExtMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,11))
class PwTDMCfgIndex(TextualConvention,Unsigned32):status=_A
_ZxPwTDMExtObjects_ObjectIdentity=ObjectIdentity
zxPwTDMExtObjects=_ZxPwTDMExtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,11,1))
_ZxPwTDMExtCardTable_Object=MibTable
zxPwTDMExtCardTable=_ZxPwTDMExtCardTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1))
if mibBuilder.loadTexts:zxPwTDMExtCardTable.setStatus(_A)
_ZxPwTDMExtCardEntry_Object=MibTableRow
zxPwTDMExtCardEntry=_ZxPwTDMExtCardEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1))
zxPwTDMExtCardEntry.setIndexNames((0,_D,_H),(0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:zxPwTDMExtCardEntry.setStatus(_A)
_ZxPwTDMExtRack_Type=Integer32
_ZxPwTDMExtRack_Object=MibTableColumn
zxPwTDMExtRack=_ZxPwTDMExtRack_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,1),_ZxPwTDMExtRack_Type())
zxPwTDMExtRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxPwTDMExtRack.setStatus(_A)
_ZxPwTDMExtShelf_Type=Integer32
_ZxPwTDMExtShelf_Object=MibTableColumn
zxPwTDMExtShelf=_ZxPwTDMExtShelf_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,2),_ZxPwTDMExtShelf_Type())
zxPwTDMExtShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxPwTDMExtShelf.setStatus(_A)
_ZxPwTDMExtSlot_Type=Integer32
_ZxPwTDMExtSlot_Object=MibTableColumn
zxPwTDMExtSlot=_ZxPwTDMExtSlot_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,3),_ZxPwTDMExtSlot_Type())
zxPwTDMExtSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxPwTDMExtSlot.setStatus(_A)
class _ZxPwTDMExtTDMType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,9)));namedValues=NamedValues(*(('udt',1),('sdtMaster',2),('sdtSlave',3),('unconfigured',9)))
_ZxPwTDMExtTDMType_Type.__name__=_C
_ZxPwTDMExtTDMType_Object=MibTableColumn
zxPwTDMExtTDMType=_ZxPwTDMExtTDMType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,4),_ZxPwTDMExtTDMType_Type())
zxPwTDMExtTDMType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtTDMType.setStatus(_A)
class _ZxPwTDMExtTransmitClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2),('throughTiming',3),('adaptive',4),('enhancedAdaptive',5),('differential',6),('lineTiming',7),('wanderOptimalAdaptive',8)))
_ZxPwTDMExtTransmitClockSource_Type.__name__=_C
_ZxPwTDMExtTransmitClockSource_Object=MibTableColumn
zxPwTDMExtTransmitClockSource=_ZxPwTDMExtTransmitClockSource_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,5),_ZxPwTDMExtTransmitClockSource_Type())
zxPwTDMExtTransmitClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtTransmitClockSource.setStatus(_A)
class _ZxPwTDMExtPrimaryClock_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxPwTDMExtPrimaryClock_Type.__name__=_C
_ZxPwTDMExtPrimaryClock_Object=MibTableColumn
zxPwTDMExtPrimaryClock=_ZxPwTDMExtPrimaryClock_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,6),_ZxPwTDMExtPrimaryClock_Type())
zxPwTDMExtPrimaryClock.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtPrimaryClock.setStatus(_A)
class _ZxPwTDMExtSecondaryClock_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxPwTDMExtSecondaryClock_Type.__name__=_C
_ZxPwTDMExtSecondaryClock_Object=MibTableColumn
zxPwTDMExtSecondaryClock=_ZxPwTDMExtSecondaryClock_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,7),_ZxPwTDMExtSecondaryClock_Type())
zxPwTDMExtSecondaryClock.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtSecondaryClock.setStatus(_A)
_ZxPwTDMExtPwType_Type=IANAPwTypeTC
_ZxPwTDMExtPwType_Object=MibTableColumn
zxPwTDMExtPwType=_ZxPwTDMExtPwType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,8),_ZxPwTDMExtPwType_Type())
zxPwTDMExtPwType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtPwType.setStatus(_A)
class _ZxPwTDMExtReferenceClockSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('packet',1),('line',2)))
_ZxPwTDMExtReferenceClockSource_Type.__name__=_C
_ZxPwTDMExtReferenceClockSource_Object=MibTableColumn
zxPwTDMExtReferenceClockSource=_ZxPwTDMExtReferenceClockSource_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,9),_ZxPwTDMExtReferenceClockSource_Type())
zxPwTDMExtReferenceClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtReferenceClockSource.setStatus(_A)
class _ZxPwTDMExtServiceClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internalClock',1),('e1Clock',2)))
_ZxPwTDMExtServiceClockSource_Type.__name__=_C
_ZxPwTDMExtServiceClockSource_Object=MibTableColumn
zxPwTDMExtServiceClockSource=_ZxPwTDMExtServiceClockSource_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,10),_ZxPwTDMExtServiceClockSource_Type())
zxPwTDMExtServiceClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtServiceClockSource.setStatus(_A)
_ZxPwTDMExtServiceClockE1No_Type=Integer32
_ZxPwTDMExtServiceClockE1No_Object=MibTableColumn
zxPwTDMExtServiceClockE1No=_ZxPwTDMExtServiceClockE1No_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,1,1,11),_ZxPwTDMExtServiceClockE1No_Type())
zxPwTDMExtServiceClockE1No.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtServiceClockE1No.setStatus(_A)
_ZxPwTDMExtTable_Object=MibTable
zxPwTDMExtTable=_ZxPwTDMExtTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,2))
if mibBuilder.loadTexts:zxPwTDMExtTable.setStatus(_A)
_ZxPwTDMExtEntry_Object=MibTableRow
zxPwTDMExtEntry=_ZxPwTDMExtEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,2,1))
zxPwTDMExtEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxPwTDMExtEntry.setStatus(_A)
_ZxPwTDMExtHWNo_Type=Integer32
_ZxPwTDMExtHWNo_Object=MibTableColumn
zxPwTDMExtHWNo=_ZxPwTDMExtHWNo_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,2,1,1),_ZxPwTDMExtHWNo_Type())
zxPwTDMExtHWNo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtHWNo.setStatus(_A)
_ZxPwTDMExtTSList_Type=DisplayString
_ZxPwTDMExtTSList_Object=MibTableColumn
zxPwTDMExtTSList=_ZxPwTDMExtTSList_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,2,1,2),_ZxPwTDMExtTSList_Type())
zxPwTDMExtTSList.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtTSList.setStatus(_A)
_ZxPwExtGenTDMCfgIndex_Type=PwTDMCfgIndex
_ZxPwExtGenTDMCfgIndex_Object=MibTableColumn
zxPwExtGenTDMCfgIndex=_ZxPwExtGenTDMCfgIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,2,1,3),_ZxPwExtGenTDMCfgIndex_Type())
zxPwExtGenTDMCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwExtGenTDMCfgIndex.setStatus(_A)
class _ZxPwTDMExtFramesPerPacket_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ZxPwTDMExtFramesPerPacket_Type.__name__=_C
_ZxPwTDMExtFramesPerPacket_Object=MibTableColumn
zxPwTDMExtFramesPerPacket=_ZxPwTDMExtFramesPerPacket_Object((1,3,6,1,4,1,3902,1015,1013,2,1,11,1,2,1,4),_ZxPwTDMExtFramesPerPacket_Type())
zxPwTDMExtFramesPerPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwTDMExtFramesPerPacket.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PwTDMCfgIndex':PwTDMCfgIndex,'zxPwTDMExtMIB':zxPwTDMExtMIB,'zxPwTDMExtObjects':zxPwTDMExtObjects,'zxPwTDMExtCardTable':zxPwTDMExtCardTable,'zxPwTDMExtCardEntry':zxPwTDMExtCardEntry,_H:zxPwTDMExtRack,_I:zxPwTDMExtShelf,_J:zxPwTDMExtSlot,'zxPwTDMExtTDMType':zxPwTDMExtTDMType,'zxPwTDMExtTransmitClockSource':zxPwTDMExtTransmitClockSource,'zxPwTDMExtPrimaryClock':zxPwTDMExtPrimaryClock,'zxPwTDMExtSecondaryClock':zxPwTDMExtSecondaryClock,'zxPwTDMExtPwType':zxPwTDMExtPwType,'zxPwTDMExtReferenceClockSource':zxPwTDMExtReferenceClockSource,'zxPwTDMExtServiceClockSource':zxPwTDMExtServiceClockSource,'zxPwTDMExtServiceClockE1No':zxPwTDMExtServiceClockE1No,'zxPwTDMExtTable':zxPwTDMExtTable,'zxPwTDMExtEntry':zxPwTDMExtEntry,'zxPwTDMExtHWNo':zxPwTDMExtHWNo,'zxPwTDMExtTSList':zxPwTDMExtTSList,'zxPwExtGenTDMCfgIndex':zxPwExtGenTDMCfgIndex,'zxPwTDMExtFramesPerPacket':zxPwTDMExtFramesPerPacket})