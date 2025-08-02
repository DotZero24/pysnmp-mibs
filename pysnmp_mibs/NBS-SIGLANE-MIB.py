_S='read-write'
_R='nbsSigLaneLaneIndex'
_Q='nbsSigLaneLaneIfIndex'
_P='nbsSigLanePortIfIndex'
_O='DisplayString'
_N='NbsTcTemperature'
_M='NbsTcMicroAmp'
_L='OctetString'
_K='highAlarm'
_J='highWarning'
_I='ok'
_H='lowWarning'
_G='lowAlarm'
_F='NBS-SIGLANE-MIB'
_E='NbsTcMilliDb'
_D='notSupported'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
NbsCmmcChannelBand,=mibBuilder.importSymbols('NBS-CMMCENUM-MIB','NbsCmmcChannelBand')
NbsTcMHz,NbsTcMicroAmp,NbsTcMilliDb,NbsTcTemperature,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcMHz',_M,_E,_N,'nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention')
nbsSigLaneMib=ModuleIdentity((1,3,6,1,4,1,629,236))
_NbsSigLanePortGrp_ObjectIdentity=ObjectIdentity
nbsSigLanePortGrp=_NbsSigLanePortGrp_ObjectIdentity((1,3,6,1,4,1,629,236,10))
if mibBuilder.loadTexts:nbsSigLanePortGrp.setStatus(_A)
_NbsSigLanePortTable_Object=MibTable
nbsSigLanePortTable=_NbsSigLanePortTable_Object((1,3,6,1,4,1,629,236,10,1))
if mibBuilder.loadTexts:nbsSigLanePortTable.setStatus(_A)
_NbsSigLanePortEntry_Object=MibTableRow
nbsSigLanePortEntry=_NbsSigLanePortEntry_Object((1,3,6,1,4,1,629,236,10,1,1))
nbsSigLanePortEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:nbsSigLanePortEntry.setStatus(_A)
_NbsSigLanePortIfIndex_Type=InterfaceIndex
_NbsSigLanePortIfIndex_Object=MibTableColumn
nbsSigLanePortIfIndex=_NbsSigLanePortIfIndex_Object((1,3,6,1,4,1,629,236,10,1,1,1),_NbsSigLanePortIfIndex_Type())
nbsSigLanePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLanePortIfIndex.setStatus(_A)
class _NbsSigLanePortFacility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('fiber',2),('lambda',3)))
_NbsSigLanePortFacility_Type.__name__=_C
_NbsSigLanePortFacility_Object=MibTableColumn
nbsSigLanePortFacility=_NbsSigLanePortFacility_Object((1,3,6,1,4,1,629,236,10,1,1,10),_NbsSigLanePortFacility_Type())
nbsSigLanePortFacility.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLanePortFacility.setStatus(_A)
_NbsSigLanePortLanes_Type=Integer32
_NbsSigLanePortLanes_Object=MibTableColumn
nbsSigLanePortLanes=_NbsSigLanePortLanes_Object((1,3,6,1,4,1,629,236,10,1,1,20),_NbsSigLanePortLanes_Type())
nbsSigLanePortLanes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLanePortLanes.setStatus(_A)
_NbsSigLaneLaneGrp_ObjectIdentity=ObjectIdentity
nbsSigLaneLaneGrp=_NbsSigLaneLaneGrp_ObjectIdentity((1,3,6,1,4,1,629,236,20))
if mibBuilder.loadTexts:nbsSigLaneLaneGrp.setStatus(_A)
_NbsSigLaneLaneTable_Object=MibTable
nbsSigLaneLaneTable=_NbsSigLaneLaneTable_Object((1,3,6,1,4,1,629,236,20,1))
if mibBuilder.loadTexts:nbsSigLaneLaneTable.setStatus(_A)
_NbsSigLaneLaneEntry_Object=MibTableRow
nbsSigLaneLaneEntry=_NbsSigLaneLaneEntry_Object((1,3,6,1,4,1,629,236,20,1,1))
nbsSigLaneLaneEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:nbsSigLaneLaneEntry.setStatus(_A)
_NbsSigLaneLaneIfIndex_Type=InterfaceIndex
_NbsSigLaneLaneIfIndex_Object=MibTableColumn
nbsSigLaneLaneIfIndex=_NbsSigLaneLaneIfIndex_Object((1,3,6,1,4,1,629,236,20,1,1,1),_NbsSigLaneLaneIfIndex_Type())
nbsSigLaneLaneIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneIfIndex.setStatus(_A)
_NbsSigLaneLaneIndex_Type=Integer32
_NbsSigLaneLaneIndex_Object=MibTableColumn
nbsSigLaneLaneIndex=_NbsSigLaneLaneIndex_Object((1,3,6,1,4,1,629,236,20,1,1,2),_NbsSigLaneLaneIndex_Type())
nbsSigLaneLaneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneIndex.setStatus(_A)
_NbsSigLaneLaneFrequency_Type=NbsTcMHz
_NbsSigLaneLaneFrequency_Object=MibTableColumn
nbsSigLaneLaneFrequency=_NbsSigLaneLaneFrequency_Object((1,3,6,1,4,1,629,236,20,1,1,10),_NbsSigLaneLaneFrequency_Type())
nbsSigLaneLaneFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneFrequency.setStatus(_A)
class _NbsSigLaneLaneWavelengthX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,8))
_NbsSigLaneLaneWavelengthX_Type.__name__=_O
_NbsSigLaneLaneWavelengthX_Object=MibTableColumn
nbsSigLaneLaneWavelengthX=_NbsSigLaneLaneWavelengthX_Object((1,3,6,1,4,1,629,236,20,1,1,11),_NbsSigLaneLaneWavelengthX_Type())
nbsSigLaneLaneWavelengthX.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneWavelengthX.setStatus(_A)
_NbsSigLaneLaneChannelBand_Type=NbsCmmcChannelBand
_NbsSigLaneLaneChannelBand_Object=MibTableColumn
nbsSigLaneLaneChannelBand=_NbsSigLaneLaneChannelBand_Object((1,3,6,1,4,1,629,236,20,1,1,12),_NbsSigLaneLaneChannelBand_Type())
nbsSigLaneLaneChannelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneChannelBand.setStatus(_A)
_NbsSigLaneLaneChannelNumber_Type=Integer32
_NbsSigLaneLaneChannelNumber_Object=MibTableColumn
nbsSigLaneLaneChannelNumber=_NbsSigLaneLaneChannelNumber_Object((1,3,6,1,4,1,629,236,20,1,1,13),_NbsSigLaneLaneChannelNumber_Type())
nbsSigLaneLaneChannelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneChannelNumber.setStatus(_A)
class _NbsSigLaneLaneTxDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no',2),('yes',3)))
_NbsSigLaneLaneTxDisable_Type.__name__=_C
_NbsSigLaneLaneTxDisable_Object=MibTableColumn
nbsSigLaneLaneTxDisable=_NbsSigLaneLaneTxDisable_Object((1,3,6,1,4,1,629,236,20,1,1,14),_NbsSigLaneLaneTxDisable_Type())
nbsSigLaneLaneTxDisable.setMaxAccess(_S)
if mibBuilder.loadTexts:nbsSigLaneLaneTxDisable.setStatus(_A)
class _NbsSigLaneLaneFaultsCaps_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_NbsSigLaneLaneFaultsCaps_Type.__name__=_L
_NbsSigLaneLaneFaultsCaps_Object=MibTableColumn
nbsSigLaneLaneFaultsCaps=_NbsSigLaneLaneFaultsCaps_Object((1,3,6,1,4,1,629,236,20,1,1,15),_NbsSigLaneLaneFaultsCaps_Type())
nbsSigLaneLaneFaultsCaps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneFaultsCaps.setStatus(_A)
class _NbsSigLaneLaneFaultsOper_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_NbsSigLaneLaneFaultsOper_Type.__name__=_L
_NbsSigLaneLaneFaultsOper_Object=MibTableColumn
nbsSigLaneLaneFaultsOper=_NbsSigLaneLaneFaultsOper_Object((1,3,6,1,4,1,629,236,20,1,1,16),_NbsSigLaneLaneFaultsOper_Type())
nbsSigLaneLaneFaultsOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneFaultsOper.setStatus(_A)
class _NbsSigLaneLaneTxPowerLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_NbsSigLaneLaneTxPowerLevel_Type.__name__=_C
_NbsSigLaneLaneTxPowerLevel_Object=MibTableColumn
nbsSigLaneLaneTxPowerLevel=_NbsSigLaneLaneTxPowerLevel_Object((1,3,6,1,4,1,629,236,20,1,1,20),_NbsSigLaneLaneTxPowerLevel_Type())
nbsSigLaneLaneTxPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneTxPowerLevel.setStatus(_A)
class _NbsSigLaneLaneTxPower_Type(NbsTcMilliDb):defaultValue=-2147483648
_NbsSigLaneLaneTxPower_Type.__name__=_E
_NbsSigLaneLaneTxPower_Object=MibTableColumn
nbsSigLaneLaneTxPower=_NbsSigLaneLaneTxPower_Object((1,3,6,1,4,1,629,236,20,1,1,21),_NbsSigLaneLaneTxPower_Type())
nbsSigLaneLaneTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneTxPower.setStatus(_A)
class _NbsSigLaneLaneTxPowerAdmin_Type(NbsTcMilliDb):defaultValue=-2147483648
_NbsSigLaneLaneTxPowerAdmin_Type.__name__=_E
_NbsSigLaneLaneTxPowerAdmin_Object=MibTableColumn
nbsSigLaneLaneTxPowerAdmin=_NbsSigLaneLaneTxPowerAdmin_Object((1,3,6,1,4,1,629,236,20,1,1,22),_NbsSigLaneLaneTxPowerAdmin_Type())
nbsSigLaneLaneTxPowerAdmin.setMaxAccess(_S)
if mibBuilder.loadTexts:nbsSigLaneLaneTxPowerAdmin.setStatus(_A)
class _NbsSigLaneLaneRxPowerLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_NbsSigLaneLaneRxPowerLevel_Type.__name__=_C
_NbsSigLaneLaneRxPowerLevel_Object=MibTableColumn
nbsSigLaneLaneRxPowerLevel=_NbsSigLaneLaneRxPowerLevel_Object((1,3,6,1,4,1,629,236,20,1,1,30),_NbsSigLaneLaneRxPowerLevel_Type())
nbsSigLaneLaneRxPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneRxPowerLevel.setStatus(_A)
class _NbsSigLaneLaneRxPower_Type(NbsTcMilliDb):defaultValue=-2147483648
_NbsSigLaneLaneRxPower_Type.__name__=_E
_NbsSigLaneLaneRxPower_Object=MibTableColumn
nbsSigLaneLaneRxPower=_NbsSigLaneLaneRxPower_Object((1,3,6,1,4,1,629,236,20,1,1,31),_NbsSigLaneLaneRxPower_Type())
nbsSigLaneLaneRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneRxPower.setStatus(_A)
class _NbsSigLaneLaneBiasAmpsLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_NbsSigLaneLaneBiasAmpsLevel_Type.__name__=_C
_NbsSigLaneLaneBiasAmpsLevel_Object=MibTableColumn
nbsSigLaneLaneBiasAmpsLevel=_NbsSigLaneLaneBiasAmpsLevel_Object((1,3,6,1,4,1,629,236,20,1,1,40),_NbsSigLaneLaneBiasAmpsLevel_Type())
nbsSigLaneLaneBiasAmpsLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneBiasAmpsLevel.setStatus(_A)
class _NbsSigLaneLaneBiasAmps_Type(NbsTcMicroAmp):defaultValue=-1
_NbsSigLaneLaneBiasAmps_Type.__name__=_M
_NbsSigLaneLaneBiasAmps_Object=MibTableColumn
nbsSigLaneLaneBiasAmps=_NbsSigLaneLaneBiasAmps_Object((1,3,6,1,4,1,629,236,20,1,1,41),_NbsSigLaneLaneBiasAmps_Type())
nbsSigLaneLaneBiasAmps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneBiasAmps.setStatus(_A)
class _NbsSigLaneLaneLaserTempLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_NbsSigLaneLaneLaserTempLevel_Type.__name__=_C
_NbsSigLaneLaneLaserTempLevel_Object=MibTableColumn
nbsSigLaneLaneLaserTempLevel=_NbsSigLaneLaneLaserTempLevel_Object((1,3,6,1,4,1,629,236,20,1,1,50),_NbsSigLaneLaneLaserTempLevel_Type())
nbsSigLaneLaneLaserTempLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneLaserTempLevel.setStatus(_A)
class _NbsSigLaneLaneLaserTemp_Type(NbsTcTemperature):defaultValue=-2147483648
_NbsSigLaneLaneLaserTemp_Type.__name__=_N
_NbsSigLaneLaneLaserTemp_Object=MibTableColumn
nbsSigLaneLaneLaserTemp=_NbsSigLaneLaneLaserTemp_Object((1,3,6,1,4,1,629,236,20,1,1,51),_NbsSigLaneLaneLaserTemp_Type())
nbsSigLaneLaneLaserTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneLaserTemp.setStatus(_A)
_NbsSigLaneLaneEthTxAllOctets_Type=Counter64
_NbsSigLaneLaneEthTxAllOctets_Object=MibTableColumn
nbsSigLaneLaneEthTxAllOctets=_NbsSigLaneLaneEthTxAllOctets_Object((1,3,6,1,4,1,629,236,20,1,1,60),_NbsSigLaneLaneEthTxAllOctets_Type())
nbsSigLaneLaneEthTxAllOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneEthTxAllOctets.setStatus(_A)
_NbsSigLaneLaneEthTxAllFrames_Type=Counter64
_NbsSigLaneLaneEthTxAllFrames_Object=MibTableColumn
nbsSigLaneLaneEthTxAllFrames=_NbsSigLaneLaneEthTxAllFrames_Object((1,3,6,1,4,1,629,236,20,1,1,61),_NbsSigLaneLaneEthTxAllFrames_Type())
nbsSigLaneLaneEthTxAllFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneEthTxAllFrames.setStatus(_A)
_NbsSigLaneLaneEthRxAllOctets_Type=Counter64
_NbsSigLaneLaneEthRxAllOctets_Object=MibTableColumn
nbsSigLaneLaneEthRxAllOctets=_NbsSigLaneLaneEthRxAllOctets_Object((1,3,6,1,4,1,629,236,20,1,1,70),_NbsSigLaneLaneEthRxAllOctets_Type())
nbsSigLaneLaneEthRxAllOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneEthRxAllOctets.setStatus(_A)
_NbsSigLaneLaneEthRxAllFrames_Type=Counter64
_NbsSigLaneLaneEthRxAllFrames_Object=MibTableColumn
nbsSigLaneLaneEthRxAllFrames=_NbsSigLaneLaneEthRxAllFrames_Object((1,3,6,1,4,1,629,236,20,1,1,71),_NbsSigLaneLaneEthRxAllFrames_Type())
nbsSigLaneLaneEthRxAllFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigLaneLaneEthRxAllFrames.setStatus(_A)
_NbsSigLaneTraps_ObjectIdentity=ObjectIdentity
nbsSigLaneTraps=_NbsSigLaneTraps_ObjectIdentity((1,3,6,1,4,1,629,236,100))
if mibBuilder.loadTexts:nbsSigLaneTraps.setStatus(_A)
_NbsSigLaneTraps0_ObjectIdentity=ObjectIdentity
nbsSigLaneTraps0=_NbsSigLaneTraps0_ObjectIdentity((1,3,6,1,4,1,629,236,100,0))
if mibBuilder.loadTexts:nbsSigLaneTraps0.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'nbsSigLaneMib':nbsSigLaneMib,'nbsSigLanePortGrp':nbsSigLanePortGrp,'nbsSigLanePortTable':nbsSigLanePortTable,'nbsSigLanePortEntry':nbsSigLanePortEntry,_P:nbsSigLanePortIfIndex,'nbsSigLanePortFacility':nbsSigLanePortFacility,'nbsSigLanePortLanes':nbsSigLanePortLanes,'nbsSigLaneLaneGrp':nbsSigLaneLaneGrp,'nbsSigLaneLaneTable':nbsSigLaneLaneTable,'nbsSigLaneLaneEntry':nbsSigLaneLaneEntry,_Q:nbsSigLaneLaneIfIndex,_R:nbsSigLaneLaneIndex,'nbsSigLaneLaneFrequency':nbsSigLaneLaneFrequency,'nbsSigLaneLaneWavelengthX':nbsSigLaneLaneWavelengthX,'nbsSigLaneLaneChannelBand':nbsSigLaneLaneChannelBand,'nbsSigLaneLaneChannelNumber':nbsSigLaneLaneChannelNumber,'nbsSigLaneLaneTxDisable':nbsSigLaneLaneTxDisable,'nbsSigLaneLaneFaultsCaps':nbsSigLaneLaneFaultsCaps,'nbsSigLaneLaneFaultsOper':nbsSigLaneLaneFaultsOper,'nbsSigLaneLaneTxPowerLevel':nbsSigLaneLaneTxPowerLevel,'nbsSigLaneLaneTxPower':nbsSigLaneLaneTxPower,'nbsSigLaneLaneTxPowerAdmin':nbsSigLaneLaneTxPowerAdmin,'nbsSigLaneLaneRxPowerLevel':nbsSigLaneLaneRxPowerLevel,'nbsSigLaneLaneRxPower':nbsSigLaneLaneRxPower,'nbsSigLaneLaneBiasAmpsLevel':nbsSigLaneLaneBiasAmpsLevel,'nbsSigLaneLaneBiasAmps':nbsSigLaneLaneBiasAmps,'nbsSigLaneLaneLaserTempLevel':nbsSigLaneLaneLaserTempLevel,'nbsSigLaneLaneLaserTemp':nbsSigLaneLaneLaserTemp,'nbsSigLaneLaneEthTxAllOctets':nbsSigLaneLaneEthTxAllOctets,'nbsSigLaneLaneEthTxAllFrames':nbsSigLaneLaneEthTxAllFrames,'nbsSigLaneLaneEthRxAllOctets':nbsSigLaneLaneEthRxAllOctets,'nbsSigLaneLaneEthRxAllFrames':nbsSigLaneLaneEthRxAllFrames,'nbsSigLaneTraps':nbsSigLaneTraps,'nbsSigLaneTraps0':nbsSigLaneTraps0})