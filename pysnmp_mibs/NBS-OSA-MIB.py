_T='nbsOsaChannelOSNRMax'
_S='nbsOsaChannelOSNRMin'
_R='nbsOsaChannelRxPowerMax'
_Q='nbsOsaChannelRxPowerMin'
_P='nbsOsaSpectrumWavelength'
_O='nbsOsaSpectrumIfIndex'
_N='nbsOsaPortIfIndex'
_M='nbsOsaChannelOSNROper'
_L='nbsOsaChannelRxPowerOper'
_K='nbsOsaChannelFrequencyNominal'
_J='read-write'
_I='nbsOsaChannelNumber'
_H='nbsOsaChannelBand'
_G='Integer32'
_F='ifAlias'
_E='IF-MIB'
_D='nbsOsaChannelIfIndex'
_C='read-only'
_B='current'
_A='NBS-OSA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifAlias=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
NbsCmmcChannelBand,=mibBuilder.importSymbols('NBS-CMMCENUM-MIB','NbsCmmcChannelBand')
NbsTcMHz,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcMHz','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsOsaMib=ModuleIdentity((1,3,6,1,4,1,629,207))
_NbsOsaPortGrp_ObjectIdentity=ObjectIdentity
nbsOsaPortGrp=_NbsOsaPortGrp_ObjectIdentity((1,3,6,1,4,1,629,207,1))
if mibBuilder.loadTexts:nbsOsaPortGrp.setStatus(_B)
_NbsOsaPortTableSize_Type=Unsigned32
_NbsOsaPortTableSize_Object=MibScalar
nbsOsaPortTableSize=_NbsOsaPortTableSize_Object((1,3,6,1,4,1,629,207,1,1),_NbsOsaPortTableSize_Type())
nbsOsaPortTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaPortTableSize.setStatus(_B)
_NbsOsaPortTable_Object=MibTable
nbsOsaPortTable=_NbsOsaPortTable_Object((1,3,6,1,4,1,629,207,1,2))
if mibBuilder.loadTexts:nbsOsaPortTable.setStatus(_B)
_NbsOsaPortEntry_Object=MibTableRow
nbsOsaPortEntry=_NbsOsaPortEntry_Object((1,3,6,1,4,1,629,207,1,2,1))
nbsOsaPortEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:nbsOsaPortEntry.setStatus(_B)
_NbsOsaPortIfIndex_Type=InterfaceIndex
_NbsOsaPortIfIndex_Object=MibTableColumn
nbsOsaPortIfIndex=_NbsOsaPortIfIndex_Object((1,3,6,1,4,1,629,207,1,2,1,2),_NbsOsaPortIfIndex_Type())
nbsOsaPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaPortIfIndex.setStatus(_B)
class _NbsOsaPortAttenuation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsOsaPortAttenuation_Type.__name__=_G
_NbsOsaPortAttenuation_Object=MibTableColumn
nbsOsaPortAttenuation=_NbsOsaPortAttenuation_Object((1,3,6,1,4,1,629,207,1,2,1,3),_NbsOsaPortAttenuation_Type())
nbsOsaPortAttenuation.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsOsaPortAttenuation.setStatus(_B)
class _NbsOsaPortChannels_Type(Integer32):defaultValue=0
_NbsOsaPortChannels_Type.__name__=_G
_NbsOsaPortChannels_Object=MibTableColumn
nbsOsaPortChannels=_NbsOsaPortChannels_Object((1,3,6,1,4,1,629,207,1,2,1,4),_NbsOsaPortChannels_Type())
nbsOsaPortChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaPortChannels.setStatus(_B)
_NbsOsaSpectrumGrp_ObjectIdentity=ObjectIdentity
nbsOsaSpectrumGrp=_NbsOsaSpectrumGrp_ObjectIdentity((1,3,6,1,4,1,629,207,2))
if mibBuilder.loadTexts:nbsOsaSpectrumGrp.setStatus(_B)
_NbsOsaSpectrumTableSize_Type=Unsigned32
_NbsOsaSpectrumTableSize_Object=MibScalar
nbsOsaSpectrumTableSize=_NbsOsaSpectrumTableSize_Object((1,3,6,1,4,1,629,207,2,1),_NbsOsaSpectrumTableSize_Type())
nbsOsaSpectrumTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaSpectrumTableSize.setStatus(_B)
_NbsOsaSpectrumTable_Object=MibTable
nbsOsaSpectrumTable=_NbsOsaSpectrumTable_Object((1,3,6,1,4,1,629,207,2,2))
if mibBuilder.loadTexts:nbsOsaSpectrumTable.setStatus(_B)
_NbsOsaSpectrumEntry_Object=MibTableRow
nbsOsaSpectrumEntry=_NbsOsaSpectrumEntry_Object((1,3,6,1,4,1,629,207,2,2,1))
nbsOsaSpectrumEntry.setIndexNames((0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:nbsOsaSpectrumEntry.setStatus(_B)
_NbsOsaSpectrumIfIndex_Type=InterfaceIndex
_NbsOsaSpectrumIfIndex_Object=MibTableColumn
nbsOsaSpectrumIfIndex=_NbsOsaSpectrumIfIndex_Object((1,3,6,1,4,1,629,207,2,2,1,2),_NbsOsaSpectrumIfIndex_Type())
nbsOsaSpectrumIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaSpectrumIfIndex.setStatus(_B)
_NbsOsaSpectrumWavelength_Type=Integer32
_NbsOsaSpectrumWavelength_Object=MibTableColumn
nbsOsaSpectrumWavelength=_NbsOsaSpectrumWavelength_Object((1,3,6,1,4,1,629,207,2,2,1,3),_NbsOsaSpectrumWavelength_Type())
nbsOsaSpectrumWavelength.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbsOsaSpectrumWavelength.setStatus(_B)
_NbsOsaSpectrumTimestamp_Type=TimeTicks
_NbsOsaSpectrumTimestamp_Object=MibTableColumn
nbsOsaSpectrumTimestamp=_NbsOsaSpectrumTimestamp_Object((1,3,6,1,4,1,629,207,2,2,1,4),_NbsOsaSpectrumTimestamp_Type())
nbsOsaSpectrumTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaSpectrumTimestamp.setStatus(_B)
_NbsOsaSpectrumRxPowerOper_Type=Integer32
_NbsOsaSpectrumRxPowerOper_Object=MibTableColumn
nbsOsaSpectrumRxPowerOper=_NbsOsaSpectrumRxPowerOper_Object((1,3,6,1,4,1,629,207,2,2,1,5),_NbsOsaSpectrumRxPowerOper_Type())
nbsOsaSpectrumRxPowerOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaSpectrumRxPowerOper.setStatus(_B)
_NbsOsaChannelGrp_ObjectIdentity=ObjectIdentity
nbsOsaChannelGrp=_NbsOsaChannelGrp_ObjectIdentity((1,3,6,1,4,1,629,207,3))
if mibBuilder.loadTexts:nbsOsaChannelGrp.setStatus(_B)
_NbsOsaChannelTableSize_Type=Unsigned32
_NbsOsaChannelTableSize_Object=MibScalar
nbsOsaChannelTableSize=_NbsOsaChannelTableSize_Object((1,3,6,1,4,1,629,207,3,1),_NbsOsaChannelTableSize_Type())
nbsOsaChannelTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelTableSize.setStatus(_B)
_NbsOsaChannelTable_Object=MibTable
nbsOsaChannelTable=_NbsOsaChannelTable_Object((1,3,6,1,4,1,629,207,3,2))
if mibBuilder.loadTexts:nbsOsaChannelTable.setStatus(_B)
_NbsOsaChannelEntry_Object=MibTableRow
nbsOsaChannelEntry=_NbsOsaChannelEntry_Object((1,3,6,1,4,1,629,207,3,2,1))
nbsOsaChannelEntry.setIndexNames((0,_A,_D),(0,_A,_K))
if mibBuilder.loadTexts:nbsOsaChannelEntry.setStatus(_B)
_NbsOsaChannelIfIndex_Type=InterfaceIndex
_NbsOsaChannelIfIndex_Object=MibTableColumn
nbsOsaChannelIfIndex=_NbsOsaChannelIfIndex_Object((1,3,6,1,4,1,629,207,3,2,1,1),_NbsOsaChannelIfIndex_Type())
nbsOsaChannelIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelIfIndex.setStatus(_B)
_NbsOsaChannelFrequencyNominal_Type=NbsTcMHz
_NbsOsaChannelFrequencyNominal_Object=MibTableColumn
nbsOsaChannelFrequencyNominal=_NbsOsaChannelFrequencyNominal_Object((1,3,6,1,4,1,629,207,3,2,1,2),_NbsOsaChannelFrequencyNominal_Type())
nbsOsaChannelFrequencyNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelFrequencyNominal.setStatus(_B)
_NbsOsaChannelBand_Type=NbsCmmcChannelBand
_NbsOsaChannelBand_Object=MibTableColumn
nbsOsaChannelBand=_NbsOsaChannelBand_Object((1,3,6,1,4,1,629,207,3,2,1,3),_NbsOsaChannelBand_Type())
nbsOsaChannelBand.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelBand.setStatus(_B)
_NbsOsaChannelNumber_Type=Integer32
_NbsOsaChannelNumber_Object=MibTableColumn
nbsOsaChannelNumber=_NbsOsaChannelNumber_Object((1,3,6,1,4,1,629,207,3,2,1,4),_NbsOsaChannelNumber_Type())
nbsOsaChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelNumber.setStatus(_B)
class _NbsOsaChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absent',1),('present',2)))
_NbsOsaChannelStatus_Type.__name__=_G
_NbsOsaChannelStatus_Object=MibTableColumn
nbsOsaChannelStatus=_NbsOsaChannelStatus_Object((1,3,6,1,4,1,629,207,3,2,1,5),_NbsOsaChannelStatus_Type())
nbsOsaChannelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelStatus.setStatus(_B)
_NbsOsaChannelTimestamp_Type=TimeTicks
_NbsOsaChannelTimestamp_Object=MibTableColumn
nbsOsaChannelTimestamp=_NbsOsaChannelTimestamp_Object((1,3,6,1,4,1,629,207,3,2,1,6),_NbsOsaChannelTimestamp_Type())
nbsOsaChannelTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelTimestamp.setStatus(_B)
_NbsOsaChannelFrequencyOper_Type=NbsTcMHz
_NbsOsaChannelFrequencyOper_Object=MibTableColumn
nbsOsaChannelFrequencyOper=_NbsOsaChannelFrequencyOper_Object((1,3,6,1,4,1,629,207,3,2,1,7),_NbsOsaChannelFrequencyOper_Type())
nbsOsaChannelFrequencyOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelFrequencyOper.setStatus(_B)
class _NbsOsaChannelRxPowerOper_Type(Integer32):defaultValue=-100000
_NbsOsaChannelRxPowerOper_Type.__name__=_G
_NbsOsaChannelRxPowerOper_Object=MibTableColumn
nbsOsaChannelRxPowerOper=_NbsOsaChannelRxPowerOper_Object((1,3,6,1,4,1,629,207,3,2,1,8),_NbsOsaChannelRxPowerOper_Type())
nbsOsaChannelRxPowerOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelRxPowerOper.setStatus(_B)
class _NbsOsaChannelRxPowerMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsOsaChannelRxPowerMin_Type.__name__=_G
_NbsOsaChannelRxPowerMin_Object=MibTableColumn
nbsOsaChannelRxPowerMin=_NbsOsaChannelRxPowerMin_Object((1,3,6,1,4,1,629,207,3,2,1,9),_NbsOsaChannelRxPowerMin_Type())
nbsOsaChannelRxPowerMin.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsOsaChannelRxPowerMin.setStatus(_B)
class _NbsOsaChannelRxPowerMax_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsOsaChannelRxPowerMax_Type.__name__=_G
_NbsOsaChannelRxPowerMax_Object=MibTableColumn
nbsOsaChannelRxPowerMax=_NbsOsaChannelRxPowerMax_Object((1,3,6,1,4,1,629,207,3,2,1,10),_NbsOsaChannelRxPowerMax_Type())
nbsOsaChannelRxPowerMax.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsOsaChannelRxPowerMax.setStatus(_B)
_NbsOsaChannelOSNROper_Type=Integer32
_NbsOsaChannelOSNROper_Object=MibTableColumn
nbsOsaChannelOSNROper=_NbsOsaChannelOSNROper_Object((1,3,6,1,4,1,629,207,3,2,1,11),_NbsOsaChannelOSNROper_Type())
nbsOsaChannelOSNROper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOsaChannelOSNROper.setStatus(_B)
class _NbsOsaChannelOSNRMin_Type(Integer32):defaultValue=1000
_NbsOsaChannelOSNRMin_Type.__name__=_G
_NbsOsaChannelOSNRMin_Object=MibTableColumn
nbsOsaChannelOSNRMin=_NbsOsaChannelOSNRMin_Object((1,3,6,1,4,1,629,207,3,2,1,12),_NbsOsaChannelOSNRMin_Type())
nbsOsaChannelOSNRMin.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsOsaChannelOSNRMin.setStatus(_B)
class _NbsOsaChannelOSNRMax_Type(Integer32):defaultValue=1000
_NbsOsaChannelOSNRMax_Type.__name__=_G
_NbsOsaChannelOSNRMax_Object=MibTableColumn
nbsOsaChannelOSNRMax=_NbsOsaChannelOSNRMax_Object((1,3,6,1,4,1,629,207,3,2,1,13),_NbsOsaChannelOSNRMax_Type())
nbsOsaChannelOSNRMax.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsOsaChannelOSNRMax.setStatus(_B)
_NbsOsaTraps_ObjectIdentity=ObjectIdentity
nbsOsaTraps=_NbsOsaTraps_ObjectIdentity((1,3,6,1,4,1,629,207,4))
if mibBuilder.loadTexts:nbsOsaTraps.setStatus(_B)
nbsOsaTrapPortChannelAdded=NotificationType((1,3,6,1,4,1,629,207,4,1))
nbsOsaTrapPortChannelAdded.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:nbsOsaTrapPortChannelAdded.setStatus(_B)
nbsOsaTrapPortChannelDropped=NotificationType((1,3,6,1,4,1,629,207,4,2))
nbsOsaTrapPortChannelDropped.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:nbsOsaTrapPortChannelDropped.setStatus(_B)
nbsOsaTrapPortRxPowerTooLow=NotificationType((1,3,6,1,4,1,629,207,4,3))
nbsOsaTrapPortRxPowerTooLow.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_Q),(_A,_L)))
if mibBuilder.loadTexts:nbsOsaTrapPortRxPowerTooLow.setStatus(_B)
nbsOsaTrapPortRxPowerOK=NotificationType((1,3,6,1,4,1,629,207,4,4))
nbsOsaTrapPortRxPowerOK.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_L)))
if mibBuilder.loadTexts:nbsOsaTrapPortRxPowerOK.setStatus(_B)
nbsOsaTrapPortRxPowerTooHigh=NotificationType((1,3,6,1,4,1,629,207,4,5))
nbsOsaTrapPortRxPowerTooHigh.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_R),(_A,_L)))
if mibBuilder.loadTexts:nbsOsaTrapPortRxPowerTooHigh.setStatus(_B)
nbsOsaTrapPortOSNRTooLow=NotificationType((1,3,6,1,4,1,629,207,4,6))
nbsOsaTrapPortOSNRTooLow.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_S),(_A,_M)))
if mibBuilder.loadTexts:nbsOsaTrapPortOSNRTooLow.setStatus(_B)
nbsOsaTrapPortOSNROk=NotificationType((1,3,6,1,4,1,629,207,4,7))
nbsOsaTrapPortOSNROk.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_M)))
if mibBuilder.loadTexts:nbsOsaTrapPortOSNROk.setStatus(_B)
nbsOsaTrapPortOSNRTooHigh=NotificationType((1,3,6,1,4,1,629,207,4,8))
nbsOsaTrapPortOSNRTooHigh.setObjects(*((_A,_D),(_E,_F),(_A,_H),(_A,_I),(_A,_T),(_A,_M)))
if mibBuilder.loadTexts:nbsOsaTrapPortOSNRTooHigh.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nbsOsaMib':nbsOsaMib,'nbsOsaPortGrp':nbsOsaPortGrp,'nbsOsaPortTableSize':nbsOsaPortTableSize,'nbsOsaPortTable':nbsOsaPortTable,'nbsOsaPortEntry':nbsOsaPortEntry,_N:nbsOsaPortIfIndex,'nbsOsaPortAttenuation':nbsOsaPortAttenuation,'nbsOsaPortChannels':nbsOsaPortChannels,'nbsOsaSpectrumGrp':nbsOsaSpectrumGrp,'nbsOsaSpectrumTableSize':nbsOsaSpectrumTableSize,'nbsOsaSpectrumTable':nbsOsaSpectrumTable,'nbsOsaSpectrumEntry':nbsOsaSpectrumEntry,_O:nbsOsaSpectrumIfIndex,_P:nbsOsaSpectrumWavelength,'nbsOsaSpectrumTimestamp':nbsOsaSpectrumTimestamp,'nbsOsaSpectrumRxPowerOper':nbsOsaSpectrumRxPowerOper,'nbsOsaChannelGrp':nbsOsaChannelGrp,'nbsOsaChannelTableSize':nbsOsaChannelTableSize,'nbsOsaChannelTable':nbsOsaChannelTable,'nbsOsaChannelEntry':nbsOsaChannelEntry,_D:nbsOsaChannelIfIndex,_K:nbsOsaChannelFrequencyNominal,_H:nbsOsaChannelBand,_I:nbsOsaChannelNumber,'nbsOsaChannelStatus':nbsOsaChannelStatus,'nbsOsaChannelTimestamp':nbsOsaChannelTimestamp,'nbsOsaChannelFrequencyOper':nbsOsaChannelFrequencyOper,_L:nbsOsaChannelRxPowerOper,_Q:nbsOsaChannelRxPowerMin,_R:nbsOsaChannelRxPowerMax,_M:nbsOsaChannelOSNROper,_S:nbsOsaChannelOSNRMin,_T:nbsOsaChannelOSNRMax,'nbsOsaTraps':nbsOsaTraps,'nbsOsaTrapPortChannelAdded':nbsOsaTrapPortChannelAdded,'nbsOsaTrapPortChannelDropped':nbsOsaTrapPortChannelDropped,'nbsOsaTrapPortRxPowerTooLow':nbsOsaTrapPortRxPowerTooLow,'nbsOsaTrapPortRxPowerOK':nbsOsaTrapPortRxPowerOK,'nbsOsaTrapPortRxPowerTooHigh':nbsOsaTrapPortRxPowerTooHigh,'nbsOsaTrapPortOSNRTooLow':nbsOsaTrapPortOSNRTooLow,'nbsOsaTrapPortOSNROk':nbsOsaTrapPortOSNROk,'nbsOsaTrapPortOSNRTooHigh':nbsOsaTrapPortOSNRTooHigh})