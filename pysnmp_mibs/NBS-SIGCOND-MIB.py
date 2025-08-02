_U='nbsSigCondVodPortIfIndex'
_T='nbsSigCondChannelIfIndex'
_S='nbsSigCondPortIfIndex'
_R='nbsSigCondRedundIfIndex'
_Q='nbsSigCondRamanIfIndex'
_P='nbsSigCondVoaChannelRangeIfIndex'
_O='nbsSigCondVoaPortIfIndex'
_N='nbsSigCondEqualizeDesiredMax'
_M='nbsSigCondEqualizeDesiredMin'
_L='nbsSigCondChannelTxPower'
_K='ifAlias'
_J='IF-MIB'
_I='nbsSigCondChannelCenterline'
_H='nbsSigCondEqualizeIfIndex'
_G='not-accessible'
_F='NbsTcMilliDb'
_E='read-write'
_D='Integer32'
_C='NBS-SIGCOND-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifAlias=mibBuilder.importSymbols(_J,'InterfaceIndex',_K)
NbsTcMHz,NbsTcMilliDb,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcMHz',_F,'nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsSigCondMib=ModuleIdentity((1,3,6,1,4,1,629,227))
_NbsSigCondVoaPortGrp_ObjectIdentity=ObjectIdentity
nbsSigCondVoaPortGrp=_NbsSigCondVoaPortGrp_ObjectIdentity((1,3,6,1,4,1,629,227,1))
if mibBuilder.loadTexts:nbsSigCondVoaPortGrp.setStatus(_A)
_NbsSigCondVoaPortTableSize_Type=Unsigned32
_NbsSigCondVoaPortTableSize_Object=MibScalar
nbsSigCondVoaPortTableSize=_NbsSigCondVoaPortTableSize_Object((1,3,6,1,4,1,629,227,1,1),_NbsSigCondVoaPortTableSize_Type())
nbsSigCondVoaPortTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVoaPortTableSize.setStatus(_A)
_NbsSigCondVoaPortTable_Object=MibTable
nbsSigCondVoaPortTable=_NbsSigCondVoaPortTable_Object((1,3,6,1,4,1,629,227,1,2))
if mibBuilder.loadTexts:nbsSigCondVoaPortTable.setStatus(_A)
_NbsSigCondVoaPortEntry_Object=MibTableRow
nbsSigCondVoaPortEntry=_NbsSigCondVoaPortEntry_Object((1,3,6,1,4,1,629,227,1,2,1))
nbsSigCondVoaPortEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:nbsSigCondVoaPortEntry.setStatus(_A)
_NbsSigCondVoaPortIfIndex_Type=InterfaceIndex
_NbsSigCondVoaPortIfIndex_Object=MibTableColumn
nbsSigCondVoaPortIfIndex=_NbsSigCondVoaPortIfIndex_Object((1,3,6,1,4,1,629,227,1,2,1,1),_NbsSigCondVoaPortIfIndex_Type())
nbsSigCondVoaPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsSigCondVoaPortIfIndex.setStatus(_A)
class _NbsSigCondVoaPortRxAttenuAdmin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVoaPortRxAttenuAdmin_Type.__name__=_D
_NbsSigCondVoaPortRxAttenuAdmin_Object=MibTableColumn
nbsSigCondVoaPortRxAttenuAdmin=_NbsSigCondVoaPortRxAttenuAdmin_Object((1,3,6,1,4,1,629,227,1,2,1,2),_NbsSigCondVoaPortRxAttenuAdmin_Type())
nbsSigCondVoaPortRxAttenuAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondVoaPortRxAttenuAdmin.setStatus(_A)
class _NbsSigCondVoaPortRxAttenuOper_Type(Integer32):defaultValue=0
_NbsSigCondVoaPortRxAttenuOper_Type.__name__=_D
_NbsSigCondVoaPortRxAttenuOper_Object=MibTableColumn
nbsSigCondVoaPortRxAttenuOper=_NbsSigCondVoaPortRxAttenuOper_Object((1,3,6,1,4,1,629,227,1,2,1,3),_NbsSigCondVoaPortRxAttenuOper_Type())
nbsSigCondVoaPortRxAttenuOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVoaPortRxAttenuOper.setStatus(_A)
class _NbsSigCondVoaPortTxAttenuAdmin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVoaPortTxAttenuAdmin_Type.__name__=_D
_NbsSigCondVoaPortTxAttenuAdmin_Object=MibTableColumn
nbsSigCondVoaPortTxAttenuAdmin=_NbsSigCondVoaPortTxAttenuAdmin_Object((1,3,6,1,4,1,629,227,1,2,1,4),_NbsSigCondVoaPortTxAttenuAdmin_Type())
nbsSigCondVoaPortTxAttenuAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondVoaPortTxAttenuAdmin.setStatus(_A)
class _NbsSigCondVoaPortTxAttenuOper_Type(Integer32):defaultValue=0
_NbsSigCondVoaPortTxAttenuOper_Type.__name__=_D
_NbsSigCondVoaPortTxAttenuOper_Object=MibTableColumn
nbsSigCondVoaPortTxAttenuOper=_NbsSigCondVoaPortTxAttenuOper_Object((1,3,6,1,4,1,629,227,1,2,1,5),_NbsSigCondVoaPortTxAttenuOper_Type())
nbsSigCondVoaPortTxAttenuOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVoaPortTxAttenuOper.setStatus(_A)
_NbsSigCondVoaChannelGrp_ObjectIdentity=ObjectIdentity
nbsSigCondVoaChannelGrp=_NbsSigCondVoaChannelGrp_ObjectIdentity((1,3,6,1,4,1,629,227,2))
if mibBuilder.loadTexts:nbsSigCondVoaChannelGrp.setStatus(_A)
_NbsSigCondVoaChannelRangeTableSize_Type=Unsigned32
_NbsSigCondVoaChannelRangeTableSize_Object=MibScalar
nbsSigCondVoaChannelRangeTableSize=_NbsSigCondVoaChannelRangeTableSize_Object((1,3,6,1,4,1,629,227,2,1),_NbsSigCondVoaChannelRangeTableSize_Type())
nbsSigCondVoaChannelRangeTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVoaChannelRangeTableSize.setStatus(_A)
_NbsSigCondVoaChannelRangeTable_Object=MibTable
nbsSigCondVoaChannelRangeTable=_NbsSigCondVoaChannelRangeTable_Object((1,3,6,1,4,1,629,227,2,2))
if mibBuilder.loadTexts:nbsSigCondVoaChannelRangeTable.setStatus(_A)
_NbsSigCondVoaChannelRangeEntry_Object=MibTableRow
nbsSigCondVoaChannelRangeEntry=_NbsSigCondVoaChannelRangeEntry_Object((1,3,6,1,4,1,629,227,2,2,1))
nbsSigCondVoaChannelRangeEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:nbsSigCondVoaChannelRangeEntry.setStatus(_A)
_NbsSigCondVoaChannelRangeIfIndex_Type=InterfaceIndex
_NbsSigCondVoaChannelRangeIfIndex_Object=MibTableColumn
nbsSigCondVoaChannelRangeIfIndex=_NbsSigCondVoaChannelRangeIfIndex_Object((1,3,6,1,4,1,629,227,2,2,1,1),_NbsSigCondVoaChannelRangeIfIndex_Type())
nbsSigCondVoaChannelRangeIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsSigCondVoaChannelRangeIfIndex.setStatus(_A)
class _NbsSigCondVoaChannelRangeMin_Type(NbsTcMilliDb):defaultValue=0
_NbsSigCondVoaChannelRangeMin_Type.__name__=_F
_NbsSigCondVoaChannelRangeMin_Object=MibTableColumn
nbsSigCondVoaChannelRangeMin=_NbsSigCondVoaChannelRangeMin_Object((1,3,6,1,4,1,629,227,2,2,1,2),_NbsSigCondVoaChannelRangeMin_Type())
nbsSigCondVoaChannelRangeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVoaChannelRangeMin.setStatus(_A)
class _NbsSigCondVoaChannelRangeMax_Type(NbsTcMilliDb):defaultValue=0
_NbsSigCondVoaChannelRangeMax_Type.__name__=_F
_NbsSigCondVoaChannelRangeMax_Object=MibTableColumn
nbsSigCondVoaChannelRangeMax=_NbsSigCondVoaChannelRangeMax_Object((1,3,6,1,4,1,629,227,2,2,1,3),_NbsSigCondVoaChannelRangeMax_Type())
nbsSigCondVoaChannelRangeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVoaChannelRangeMax.setStatus(_A)
class _NbsSigCondVoaChannelRangeIncr_Type(NbsTcMilliDb):defaultValue=0
_NbsSigCondVoaChannelRangeIncr_Type.__name__=_F
_NbsSigCondVoaChannelRangeIncr_Object=MibTableColumn
nbsSigCondVoaChannelRangeIncr=_NbsSigCondVoaChannelRangeIncr_Object((1,3,6,1,4,1,629,227,2,2,1,4),_NbsSigCondVoaChannelRangeIncr_Type())
nbsSigCondVoaChannelRangeIncr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVoaChannelRangeIncr.setStatus(_A)
_NbsSigCondRamanGrp_ObjectIdentity=ObjectIdentity
nbsSigCondRamanGrp=_NbsSigCondRamanGrp_ObjectIdentity((1,3,6,1,4,1,629,227,3))
if mibBuilder.loadTexts:nbsSigCondRamanGrp.setStatus(_A)
_NbsSigCondRamanTableSize_Type=Unsigned32
_NbsSigCondRamanTableSize_Object=MibScalar
nbsSigCondRamanTableSize=_NbsSigCondRamanTableSize_Object((1,3,6,1,4,1,629,227,3,1),_NbsSigCondRamanTableSize_Type())
nbsSigCondRamanTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondRamanTableSize.setStatus(_A)
_NbsSigCondRamanTable_Object=MibTable
nbsSigCondRamanTable=_NbsSigCondRamanTable_Object((1,3,6,1,4,1,629,227,3,2))
if mibBuilder.loadTexts:nbsSigCondRamanTable.setStatus(_A)
_NbsSigCondRamanEntry_Object=MibTableRow
nbsSigCondRamanEntry=_NbsSigCondRamanEntry_Object((1,3,6,1,4,1,629,227,3,2,1))
nbsSigCondRamanEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:nbsSigCondRamanEntry.setStatus(_A)
_NbsSigCondRamanIfIndex_Type=InterfaceIndex
_NbsSigCondRamanIfIndex_Object=MibTableColumn
nbsSigCondRamanIfIndex=_NbsSigCondRamanIfIndex_Object((1,3,6,1,4,1,629,227,3,2,1,1),_NbsSigCondRamanIfIndex_Type())
nbsSigCondRamanIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsSigCondRamanIfIndex.setStatus(_A)
_NbsSigCondRamanPumpPwrAdmin_Type=Integer32
_NbsSigCondRamanPumpPwrAdmin_Object=MibTableColumn
nbsSigCondRamanPumpPwrAdmin=_NbsSigCondRamanPumpPwrAdmin_Object((1,3,6,1,4,1,629,227,3,2,1,2),_NbsSigCondRamanPumpPwrAdmin_Type())
nbsSigCondRamanPumpPwrAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondRamanPumpPwrAdmin.setStatus(_A)
_NbsSigCondRamanPumpPwrOper_Type=Integer32
_NbsSigCondRamanPumpPwrOper_Object=MibTableColumn
nbsSigCondRamanPumpPwrOper=_NbsSigCondRamanPumpPwrOper_Object((1,3,6,1,4,1,629,227,3,2,1,3),_NbsSigCondRamanPumpPwrOper_Type())
nbsSigCondRamanPumpPwrOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondRamanPumpPwrOper.setStatus(_A)
_NbsSigCondEqualizeGrp_ObjectIdentity=ObjectIdentity
nbsSigCondEqualizeGrp=_NbsSigCondEqualizeGrp_ObjectIdentity((1,3,6,1,4,1,629,227,20))
if mibBuilder.loadTexts:nbsSigCondEqualizeGrp.setStatus(_A)
_NbsSigCondEqualizeTableSize_Type=Unsigned32
_NbsSigCondEqualizeTableSize_Object=MibScalar
nbsSigCondEqualizeTableSize=_NbsSigCondEqualizeTableSize_Object((1,3,6,1,4,1,629,227,20,1),_NbsSigCondEqualizeTableSize_Type())
nbsSigCondEqualizeTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondEqualizeTableSize.setStatus(_A)
_NbsSigCondEqualizeTable_Object=MibTable
nbsSigCondEqualizeTable=_NbsSigCondEqualizeTable_Object((1,3,6,1,4,1,629,227,20,2))
if mibBuilder.loadTexts:nbsSigCondEqualizeTable.setStatus(_A)
_NbsSigCondEqualizeEntry_Object=MibTableRow
nbsSigCondEqualizeEntry=_NbsSigCondEqualizeEntry_Object((1,3,6,1,4,1,629,227,20,2,1))
nbsSigCondEqualizeEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:nbsSigCondEqualizeEntry.setStatus(_A)
_NbsSigCondEqualizeIfIndex_Type=InterfaceIndex
_NbsSigCondEqualizeIfIndex_Object=MibTableColumn
nbsSigCondEqualizeIfIndex=_NbsSigCondEqualizeIfIndex_Object((1,3,6,1,4,1,629,227,20,2,1,1),_NbsSigCondEqualizeIfIndex_Type())
nbsSigCondEqualizeIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondEqualizeIfIndex.setStatus(_A)
class _NbsSigCondEqualizeState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),('disabled',2),('enabled',3)))
_NbsSigCondEqualizeState_Type.__name__=_D
_NbsSigCondEqualizeState_Object=MibTableColumn
nbsSigCondEqualizeState=_NbsSigCondEqualizeState_Object((1,3,6,1,4,1,629,227,20,2,1,10),_NbsSigCondEqualizeState_Type())
nbsSigCondEqualizeState.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondEqualizeState.setStatus(_A)
_NbsSigCondEqualizeLimitMin_Type=NbsTcMilliDb
_NbsSigCondEqualizeLimitMin_Object=MibTableColumn
nbsSigCondEqualizeLimitMin=_NbsSigCondEqualizeLimitMin_Object((1,3,6,1,4,1,629,227,20,2,1,11),_NbsSigCondEqualizeLimitMin_Type())
nbsSigCondEqualizeLimitMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondEqualizeLimitMin.setStatus(_A)
_NbsSigCondEqualizeLimitMax_Type=NbsTcMilliDb
_NbsSigCondEqualizeLimitMax_Object=MibTableColumn
nbsSigCondEqualizeLimitMax=_NbsSigCondEqualizeLimitMax_Object((1,3,6,1,4,1,629,227,20,2,1,12),_NbsSigCondEqualizeLimitMax_Type())
nbsSigCondEqualizeLimitMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondEqualizeLimitMax.setStatus(_A)
class _NbsSigCondEqualizeDesiredMin_Type(NbsTcMilliDb):defaultValue=-50000
_NbsSigCondEqualizeDesiredMin_Type.__name__=_F
_NbsSigCondEqualizeDesiredMin_Object=MibTableColumn
nbsSigCondEqualizeDesiredMin=_NbsSigCondEqualizeDesiredMin_Object((1,3,6,1,4,1,629,227,20,2,1,21),_NbsSigCondEqualizeDesiredMin_Type())
nbsSigCondEqualizeDesiredMin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondEqualizeDesiredMin.setStatus(_A)
class _NbsSigCondEqualizeDesiredMax_Type(NbsTcMilliDb):defaultValue=0
_NbsSigCondEqualizeDesiredMax_Type.__name__=_F
_NbsSigCondEqualizeDesiredMax_Object=MibTableColumn
nbsSigCondEqualizeDesiredMax=_NbsSigCondEqualizeDesiredMax_Object((1,3,6,1,4,1,629,227,20,2,1,22),_NbsSigCondEqualizeDesiredMax_Type())
nbsSigCondEqualizeDesiredMax.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondEqualizeDesiredMax.setStatus(_A)
class _NbsSigCondEqualizeDesiredVal_Type(NbsTcMilliDb):defaultValue=-25000
_NbsSigCondEqualizeDesiredVal_Type.__name__=_F
_NbsSigCondEqualizeDesiredVal_Object=MibTableColumn
nbsSigCondEqualizeDesiredVal=_NbsSigCondEqualizeDesiredVal_Object((1,3,6,1,4,1,629,227,20,2,1,23),_NbsSigCondEqualizeDesiredVal_Type())
nbsSigCondEqualizeDesiredVal.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondEqualizeDesiredVal.setStatus(_A)
_NbsSigCondRedundGrp_ObjectIdentity=ObjectIdentity
nbsSigCondRedundGrp=_NbsSigCondRedundGrp_ObjectIdentity((1,3,6,1,4,1,629,227,30))
if mibBuilder.loadTexts:nbsSigCondRedundGrp.setStatus(_A)
_NbsSigCondRedundTableSize_Type=Unsigned32
_NbsSigCondRedundTableSize_Object=MibScalar
nbsSigCondRedundTableSize=_NbsSigCondRedundTableSize_Object((1,3,6,1,4,1,629,227,30,1),_NbsSigCondRedundTableSize_Type())
nbsSigCondRedundTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondRedundTableSize.setStatus(_A)
_NbsSigCondRedundTable_Object=MibTable
nbsSigCondRedundTable=_NbsSigCondRedundTable_Object((1,3,6,1,4,1,629,227,30,2))
if mibBuilder.loadTexts:nbsSigCondRedundTable.setStatus(_A)
_NbsSigCondRedundEntry_Object=MibTableRow
nbsSigCondRedundEntry=_NbsSigCondRedundEntry_Object((1,3,6,1,4,1,629,227,30,2,1))
nbsSigCondRedundEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:nbsSigCondRedundEntry.setStatus(_A)
_NbsSigCondRedundIfIndex_Type=InterfaceIndex
_NbsSigCondRedundIfIndex_Object=MibTableColumn
nbsSigCondRedundIfIndex=_NbsSigCondRedundIfIndex_Object((1,3,6,1,4,1,629,227,30,2,1,1),_NbsSigCondRedundIfIndex_Type())
nbsSigCondRedundIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondRedundIfIndex.setStatus(_A)
_NbsSigCondRedundLimitMin_Type=NbsTcMilliDb
_NbsSigCondRedundLimitMin_Object=MibTableColumn
nbsSigCondRedundLimitMin=_NbsSigCondRedundLimitMin_Object((1,3,6,1,4,1,629,227,30,2,1,5),_NbsSigCondRedundLimitMin_Type())
nbsSigCondRedundLimitMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondRedundLimitMin.setStatus(_A)
_NbsSigCondRedundLimitMax_Type=NbsTcMilliDb
_NbsSigCondRedundLimitMax_Object=MibTableColumn
nbsSigCondRedundLimitMax=_NbsSigCondRedundLimitMax_Object((1,3,6,1,4,1,629,227,30,2,1,8),_NbsSigCondRedundLimitMax_Type())
nbsSigCondRedundLimitMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondRedundLimitMax.setStatus(_A)
_NbsSigCondRedundDesiredMin_Type=NbsTcMilliDb
_NbsSigCondRedundDesiredMin_Object=MibTableColumn
nbsSigCondRedundDesiredMin=_NbsSigCondRedundDesiredMin_Object((1,3,6,1,4,1,629,227,30,2,1,10),_NbsSigCondRedundDesiredMin_Type())
nbsSigCondRedundDesiredMin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondRedundDesiredMin.setStatus(_A)
_NbsSigCondRedundDesiredMax_Type=NbsTcMilliDb
_NbsSigCondRedundDesiredMax_Object=MibTableColumn
nbsSigCondRedundDesiredMax=_NbsSigCondRedundDesiredMax_Object((1,3,6,1,4,1,629,227,30,2,1,15),_NbsSigCondRedundDesiredMax_Type())
nbsSigCondRedundDesiredMax.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondRedundDesiredMax.setStatus(_A)
_NbsSigCondPortGrp_ObjectIdentity=ObjectIdentity
nbsSigCondPortGrp=_NbsSigCondPortGrp_ObjectIdentity((1,3,6,1,4,1,629,227,40))
if mibBuilder.loadTexts:nbsSigCondPortGrp.setStatus(_A)
_NbsSigCondPortTableSize_Type=Unsigned32
_NbsSigCondPortTableSize_Object=MibScalar
nbsSigCondPortTableSize=_NbsSigCondPortTableSize_Object((1,3,6,1,4,1,629,227,40,1),_NbsSigCondPortTableSize_Type())
nbsSigCondPortTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondPortTableSize.setStatus(_A)
_NbsSigCondPortTable_Object=MibTable
nbsSigCondPortTable=_NbsSigCondPortTable_Object((1,3,6,1,4,1,629,227,40,2))
if mibBuilder.loadTexts:nbsSigCondPortTable.setStatus(_A)
_NbsSigCondPortEntry_Object=MibTableRow
nbsSigCondPortEntry=_NbsSigCondPortEntry_Object((1,3,6,1,4,1,629,227,40,2,1))
nbsSigCondPortEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:nbsSigCondPortEntry.setStatus(_A)
_NbsSigCondPortIfIndex_Type=InterfaceIndex
_NbsSigCondPortIfIndex_Object=MibTableColumn
nbsSigCondPortIfIndex=_NbsSigCondPortIfIndex_Object((1,3,6,1,4,1,629,227,40,2,1,1),_NbsSigCondPortIfIndex_Type())
nbsSigCondPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsSigCondPortIfIndex.setStatus(_A)
_NbsSigCondPortRxPower_Type=Integer32
_NbsSigCondPortRxPower_Object=MibTableColumn
nbsSigCondPortRxPower=_NbsSigCondPortRxPower_Object((1,3,6,1,4,1,629,227,40,2,1,2),_NbsSigCondPortRxPower_Type())
nbsSigCondPortRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondPortRxPower.setStatus(_A)
_NbsSigCondPortTxPower_Type=Integer32
_NbsSigCondPortTxPower_Object=MibTableColumn
nbsSigCondPortTxPower=_NbsSigCondPortTxPower_Object((1,3,6,1,4,1,629,227,40,2,1,3),_NbsSigCondPortTxPower_Type())
nbsSigCondPortTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondPortTxPower.setStatus(_A)
_NbsSigCondPortReflection_Type=Integer32
_NbsSigCondPortReflection_Object=MibTableColumn
nbsSigCondPortReflection=_NbsSigCondPortReflection_Object((1,3,6,1,4,1,629,227,40,2,1,4),_NbsSigCondPortReflection_Type())
nbsSigCondPortReflection.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondPortReflection.setStatus(_A)
_NbsSigCondPortRxPowerMin_Type=Integer32
_NbsSigCondPortRxPowerMin_Object=MibTableColumn
nbsSigCondPortRxPowerMin=_NbsSigCondPortRxPowerMin_Object((1,3,6,1,4,1,629,227,40,2,1,5),_NbsSigCondPortRxPowerMin_Type())
nbsSigCondPortRxPowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondPortRxPowerMin.setStatus(_A)
_NbsSigCondPortRxPowerMax_Type=Integer32
_NbsSigCondPortRxPowerMax_Object=MibTableColumn
nbsSigCondPortRxPowerMax=_NbsSigCondPortRxPowerMax_Object((1,3,6,1,4,1,629,227,40,2,1,6),_NbsSigCondPortRxPowerMax_Type())
nbsSigCondPortRxPowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondPortRxPowerMax.setStatus(_A)
_NbsSigCondPortNoiseFigure_Type=Integer32
_NbsSigCondPortNoiseFigure_Object=MibTableColumn
nbsSigCondPortNoiseFigure=_NbsSigCondPortNoiseFigure_Object((1,3,6,1,4,1,629,227,40,2,1,7),_NbsSigCondPortNoiseFigure_Type())
nbsSigCondPortNoiseFigure.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondPortNoiseFigure.setStatus(_A)
_NbsSigCondChannelGrp_ObjectIdentity=ObjectIdentity
nbsSigCondChannelGrp=_NbsSigCondChannelGrp_ObjectIdentity((1,3,6,1,4,1,629,227,50))
if mibBuilder.loadTexts:nbsSigCondChannelGrp.setStatus(_A)
_NbsSigCondChannelTableSize_Type=Unsigned32
_NbsSigCondChannelTableSize_Object=MibScalar
nbsSigCondChannelTableSize=_NbsSigCondChannelTableSize_Object((1,3,6,1,4,1,629,227,50,1),_NbsSigCondChannelTableSize_Type())
nbsSigCondChannelTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondChannelTableSize.setStatus(_A)
_NbsSigCondChannelTable_Object=MibTable
nbsSigCondChannelTable=_NbsSigCondChannelTable_Object((1,3,6,1,4,1,629,227,50,2))
if mibBuilder.loadTexts:nbsSigCondChannelTable.setStatus(_A)
_NbsSigCondChannelEntry_Object=MibTableRow
nbsSigCondChannelEntry=_NbsSigCondChannelEntry_Object((1,3,6,1,4,1,629,227,50,2,1))
nbsSigCondChannelEntry.setIndexNames((0,_C,_T),(0,_C,_I))
if mibBuilder.loadTexts:nbsSigCondChannelEntry.setStatus(_A)
_NbsSigCondChannelIfIndex_Type=InterfaceIndex
_NbsSigCondChannelIfIndex_Object=MibTableColumn
nbsSigCondChannelIfIndex=_NbsSigCondChannelIfIndex_Object((1,3,6,1,4,1,629,227,50,2,1,1),_NbsSigCondChannelIfIndex_Type())
nbsSigCondChannelIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsSigCondChannelIfIndex.setStatus(_A)
_NbsSigCondChannelCenterline_Type=NbsTcMHz
_NbsSigCondChannelCenterline_Object=MibTableColumn
nbsSigCondChannelCenterline=_NbsSigCondChannelCenterline_Object((1,3,6,1,4,1,629,227,50,2,1,2),_NbsSigCondChannelCenterline_Type())
nbsSigCondChannelCenterline.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondChannelCenterline.setStatus(_A)
_NbsSigCondChannelRxPower_Type=NbsTcMilliDb
_NbsSigCondChannelRxPower_Object=MibTableColumn
nbsSigCondChannelRxPower=_NbsSigCondChannelRxPower_Object((1,3,6,1,4,1,629,227,50,2,1,11),_NbsSigCondChannelRxPower_Type())
nbsSigCondChannelRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondChannelRxPower.setStatus(_A)
_NbsSigCondChannelTxPower_Type=NbsTcMilliDb
_NbsSigCondChannelTxPower_Object=MibTableColumn
nbsSigCondChannelTxPower=_NbsSigCondChannelTxPower_Object((1,3,6,1,4,1,629,227,50,2,1,12),_NbsSigCondChannelTxPower_Type())
nbsSigCondChannelTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondChannelTxPower.setStatus(_A)
_NbsSigCondChannelTxAttenu_Type=NbsTcMilliDb
_NbsSigCondChannelTxAttenu_Object=MibTableColumn
nbsSigCondChannelTxAttenu=_NbsSigCondChannelTxAttenu_Object((1,3,6,1,4,1,629,227,50,2,1,14),_NbsSigCondChannelTxAttenu_Type())
nbsSigCondChannelTxAttenu.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondChannelTxAttenu.setStatus(_A)
_NbsSigCondChannelRxAttenu_Type=NbsTcMilliDb
_NbsSigCondChannelRxAttenu_Object=MibTableColumn
nbsSigCondChannelRxAttenu=_NbsSigCondChannelRxAttenu_Object((1,3,6,1,4,1,629,227,50,2,1,15),_NbsSigCondChannelRxAttenu_Type())
nbsSigCondChannelRxAttenu.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondChannelRxAttenu.setStatus(_A)
_NbsSigCondVodPortGrp_ObjectIdentity=ObjectIdentity
nbsSigCondVodPortGrp=_NbsSigCondVodPortGrp_ObjectIdentity((1,3,6,1,4,1,629,227,60))
if mibBuilder.loadTexts:nbsSigCondVodPortGrp.setStatus(_A)
_NbsSigCondVodPortTableSize_Type=Unsigned32
_NbsSigCondVodPortTableSize_Object=MibScalar
nbsSigCondVodPortTableSize=_NbsSigCondVodPortTableSize_Object((1,3,6,1,4,1,629,227,60,1),_NbsSigCondVodPortTableSize_Type())
nbsSigCondVodPortTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortTableSize.setStatus(_A)
_NbsSigCondVodPortTable_Object=MibTable
nbsSigCondVodPortTable=_NbsSigCondVodPortTable_Object((1,3,6,1,4,1,629,227,60,2))
if mibBuilder.loadTexts:nbsSigCondVodPortTable.setStatus(_A)
_NbsSigCondVodPortEntry_Object=MibTableRow
nbsSigCondVodPortEntry=_NbsSigCondVodPortEntry_Object((1,3,6,1,4,1,629,227,60,2,1))
nbsSigCondVodPortEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:nbsSigCondVodPortEntry.setStatus(_A)
_NbsSigCondVodPortIfIndex_Type=InterfaceIndex
_NbsSigCondVodPortIfIndex_Object=MibTableColumn
nbsSigCondVodPortIfIndex=_NbsSigCondVodPortIfIndex_Object((1,3,6,1,4,1,629,227,60,2,1,1),_NbsSigCondVodPortIfIndex_Type())
nbsSigCondVodPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsSigCondVodPortIfIndex.setStatus(_A)
class _NbsSigCondVodPortDispersionMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionMin_Type.__name__=_D
_NbsSigCondVodPortDispersionMin_Object=MibTableColumn
nbsSigCondVodPortDispersionMin=_NbsSigCondVodPortDispersionMin_Object((1,3,6,1,4,1,629,227,60,2,1,2),_NbsSigCondVodPortDispersionMin_Type())
nbsSigCondVodPortDispersionMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionMin.setStatus(_A)
class _NbsSigCondVodPortDispersionMax_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionMax_Type.__name__=_D
_NbsSigCondVodPortDispersionMax_Object=MibTableColumn
nbsSigCondVodPortDispersionMax=_NbsSigCondVodPortDispersionMax_Object((1,3,6,1,4,1,629,227,60,2,1,3),_NbsSigCondVodPortDispersionMax_Type())
nbsSigCondVodPortDispersionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionMax.setStatus(_A)
class _NbsSigCondVodPortDispersionAdmin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionAdmin_Type.__name__=_D
_NbsSigCondVodPortDispersionAdmin_Object=MibTableColumn
nbsSigCondVodPortDispersionAdmin=_NbsSigCondVodPortDispersionAdmin_Object((1,3,6,1,4,1,629,227,60,2,1,4),_NbsSigCondVodPortDispersionAdmin_Type())
nbsSigCondVodPortDispersionAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionAdmin.setStatus(_A)
class _NbsSigCondVodPortDispersionOper_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionOper_Type.__name__=_D
_NbsSigCondVodPortDispersionOper_Object=MibTableColumn
nbsSigCondVodPortDispersionOper=_NbsSigCondVodPortDispersionOper_Object((1,3,6,1,4,1,629,227,60,2,1,5),_NbsSigCondVodPortDispersionOper_Type())
nbsSigCondVodPortDispersionOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionOper.setStatus(_A)
_NbsSigCondVodPortDispersionGridOffsetCenter_Type=Integer32
_NbsSigCondVodPortDispersionGridOffsetCenter_Object=MibTableColumn
nbsSigCondVodPortDispersionGridOffsetCenter=_NbsSigCondVodPortDispersionGridOffsetCenter_Object((1,3,6,1,4,1,629,227,60,2,1,10),_NbsSigCondVodPortDispersionGridOffsetCenter_Type())
nbsSigCondVodPortDispersionGridOffsetCenter.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionGridOffsetCenter.setStatus(_A)
class _NbsSigCondVodPortDispersionGridOffsetMin_Type(Integer32):defaultValue=-100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionGridOffsetMin_Type.__name__=_D
_NbsSigCondVodPortDispersionGridOffsetMin_Object=MibTableColumn
nbsSigCondVodPortDispersionGridOffsetMin=_NbsSigCondVodPortDispersionGridOffsetMin_Object((1,3,6,1,4,1,629,227,60,2,1,11),_NbsSigCondVodPortDispersionGridOffsetMin_Type())
nbsSigCondVodPortDispersionGridOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionGridOffsetMin.setStatus(_A)
class _NbsSigCondVodPortDispersionGridOffsetMax_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionGridOffsetMax_Type.__name__=_D
_NbsSigCondVodPortDispersionGridOffsetMax_Object=MibTableColumn
nbsSigCondVodPortDispersionGridOffsetMax=_NbsSigCondVodPortDispersionGridOffsetMax_Object((1,3,6,1,4,1,629,227,60,2,1,12),_NbsSigCondVodPortDispersionGridOffsetMax_Type())
nbsSigCondVodPortDispersionGridOffsetMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionGridOffsetMax.setStatus(_A)
class _NbsSigCondVodPortDispersionGridOffsetStep_Type(Integer32):defaultValue=1
_NbsSigCondVodPortDispersionGridOffsetStep_Type.__name__=_D
_NbsSigCondVodPortDispersionGridOffsetStep_Object=MibTableColumn
nbsSigCondVodPortDispersionGridOffsetStep=_NbsSigCondVodPortDispersionGridOffsetStep_Object((1,3,6,1,4,1,629,227,60,2,1,13),_NbsSigCondVodPortDispersionGridOffsetStep_Type())
nbsSigCondVodPortDispersionGridOffsetStep.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionGridOffsetStep.setStatus(_A)
class _NbsSigCondVodPortDispersionGridOffsetExponent_Type(Integer32):defaultValue=9
_NbsSigCondVodPortDispersionGridOffsetExponent_Type.__name__=_D
_NbsSigCondVodPortDispersionGridOffsetExponent_Object=MibTableColumn
nbsSigCondVodPortDispersionGridOffsetExponent=_NbsSigCondVodPortDispersionGridOffsetExponent_Object((1,3,6,1,4,1,629,227,60,2,1,14),_NbsSigCondVodPortDispersionGridOffsetExponent_Type())
nbsSigCondVodPortDispersionGridOffsetExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionGridOffsetExponent.setStatus(_A)
class _NbsSigCondVodPortDispersionGridOffsetAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionGridOffsetAdmin_Type.__name__=_D
_NbsSigCondVodPortDispersionGridOffsetAdmin_Object=MibTableColumn
nbsSigCondVodPortDispersionGridOffsetAdmin=_NbsSigCondVodPortDispersionGridOffsetAdmin_Object((1,3,6,1,4,1,629,227,60,2,1,15),_NbsSigCondVodPortDispersionGridOffsetAdmin_Type())
nbsSigCondVodPortDispersionGridOffsetAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionGridOffsetAdmin.setStatus(_A)
class _NbsSigCondVodPortDispersionGridOffsetOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000,100000))
_NbsSigCondVodPortDispersionGridOffsetOper_Type.__name__=_D
_NbsSigCondVodPortDispersionGridOffsetOper_Object=MibTableColumn
nbsSigCondVodPortDispersionGridOffsetOper=_NbsSigCondVodPortDispersionGridOffsetOper_Object((1,3,6,1,4,1,629,227,60,2,1,16),_NbsSigCondVodPortDispersionGridOffsetOper_Type())
nbsSigCondVodPortDispersionGridOffsetOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSigCondVodPortDispersionGridOffsetOper.setStatus(_A)
_NbsSigCondTraps_ObjectIdentity=ObjectIdentity
nbsSigCondTraps=_NbsSigCondTraps_ObjectIdentity((1,3,6,1,4,1,629,227,200))
if mibBuilder.loadTexts:nbsSigCondTraps.setStatus(_A)
_NbsSigCondEvent_ObjectIdentity=ObjectIdentity
nbsSigCondEvent=_NbsSigCondEvent_ObjectIdentity((1,3,6,1,4,1,629,227,200,0))
if mibBuilder.loadTexts:nbsSigCondEvent.setStatus(_A)
nbsSigCondEventEqualizeOk=NotificationType((1,3,6,1,4,1,629,227,200,0,20))
nbsSigCondEventEqualizeOk.setObjects(*((_C,_H),(_J,_K),(_C,_I),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:nbsSigCondEventEqualizeOk.setStatus(_A)
nbsSigCondEventEqualizeTooLow=NotificationType((1,3,6,1,4,1,629,227,200,0,21))
nbsSigCondEventEqualizeTooLow.setObjects(*((_C,_H),(_J,_K),(_C,_I),(_C,_L),(_C,_M)))
if mibBuilder.loadTexts:nbsSigCondEventEqualizeTooLow.setStatus(_A)
nbsSigCondEventEqualizeTooHigh=NotificationType((1,3,6,1,4,1,629,227,200,0,22))
nbsSigCondEventEqualizeTooHigh.setObjects(*((_C,_H),(_J,_K),(_C,_I),(_C,_L),(_C,_N)))
if mibBuilder.loadTexts:nbsSigCondEventEqualizeTooHigh.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nbsSigCondMib':nbsSigCondMib,'nbsSigCondVoaPortGrp':nbsSigCondVoaPortGrp,'nbsSigCondVoaPortTableSize':nbsSigCondVoaPortTableSize,'nbsSigCondVoaPortTable':nbsSigCondVoaPortTable,'nbsSigCondVoaPortEntry':nbsSigCondVoaPortEntry,_O:nbsSigCondVoaPortIfIndex,'nbsSigCondVoaPortRxAttenuAdmin':nbsSigCondVoaPortRxAttenuAdmin,'nbsSigCondVoaPortRxAttenuOper':nbsSigCondVoaPortRxAttenuOper,'nbsSigCondVoaPortTxAttenuAdmin':nbsSigCondVoaPortTxAttenuAdmin,'nbsSigCondVoaPortTxAttenuOper':nbsSigCondVoaPortTxAttenuOper,'nbsSigCondVoaChannelGrp':nbsSigCondVoaChannelGrp,'nbsSigCondVoaChannelRangeTableSize':nbsSigCondVoaChannelRangeTableSize,'nbsSigCondVoaChannelRangeTable':nbsSigCondVoaChannelRangeTable,'nbsSigCondVoaChannelRangeEntry':nbsSigCondVoaChannelRangeEntry,_P:nbsSigCondVoaChannelRangeIfIndex,'nbsSigCondVoaChannelRangeMin':nbsSigCondVoaChannelRangeMin,'nbsSigCondVoaChannelRangeMax':nbsSigCondVoaChannelRangeMax,'nbsSigCondVoaChannelRangeIncr':nbsSigCondVoaChannelRangeIncr,'nbsSigCondRamanGrp':nbsSigCondRamanGrp,'nbsSigCondRamanTableSize':nbsSigCondRamanTableSize,'nbsSigCondRamanTable':nbsSigCondRamanTable,'nbsSigCondRamanEntry':nbsSigCondRamanEntry,_Q:nbsSigCondRamanIfIndex,'nbsSigCondRamanPumpPwrAdmin':nbsSigCondRamanPumpPwrAdmin,'nbsSigCondRamanPumpPwrOper':nbsSigCondRamanPumpPwrOper,'nbsSigCondEqualizeGrp':nbsSigCondEqualizeGrp,'nbsSigCondEqualizeTableSize':nbsSigCondEqualizeTableSize,'nbsSigCondEqualizeTable':nbsSigCondEqualizeTable,'nbsSigCondEqualizeEntry':nbsSigCondEqualizeEntry,_H:nbsSigCondEqualizeIfIndex,'nbsSigCondEqualizeState':nbsSigCondEqualizeState,'nbsSigCondEqualizeLimitMin':nbsSigCondEqualizeLimitMin,'nbsSigCondEqualizeLimitMax':nbsSigCondEqualizeLimitMax,_M:nbsSigCondEqualizeDesiredMin,_N:nbsSigCondEqualizeDesiredMax,'nbsSigCondEqualizeDesiredVal':nbsSigCondEqualizeDesiredVal,'nbsSigCondRedundGrp':nbsSigCondRedundGrp,'nbsSigCondRedundTableSize':nbsSigCondRedundTableSize,'nbsSigCondRedundTable':nbsSigCondRedundTable,'nbsSigCondRedundEntry':nbsSigCondRedundEntry,_R:nbsSigCondRedundIfIndex,'nbsSigCondRedundLimitMin':nbsSigCondRedundLimitMin,'nbsSigCondRedundLimitMax':nbsSigCondRedundLimitMax,'nbsSigCondRedundDesiredMin':nbsSigCondRedundDesiredMin,'nbsSigCondRedundDesiredMax':nbsSigCondRedundDesiredMax,'nbsSigCondPortGrp':nbsSigCondPortGrp,'nbsSigCondPortTableSize':nbsSigCondPortTableSize,'nbsSigCondPortTable':nbsSigCondPortTable,'nbsSigCondPortEntry':nbsSigCondPortEntry,_S:nbsSigCondPortIfIndex,'nbsSigCondPortRxPower':nbsSigCondPortRxPower,'nbsSigCondPortTxPower':nbsSigCondPortTxPower,'nbsSigCondPortReflection':nbsSigCondPortReflection,'nbsSigCondPortRxPowerMin':nbsSigCondPortRxPowerMin,'nbsSigCondPortRxPowerMax':nbsSigCondPortRxPowerMax,'nbsSigCondPortNoiseFigure':nbsSigCondPortNoiseFigure,'nbsSigCondChannelGrp':nbsSigCondChannelGrp,'nbsSigCondChannelTableSize':nbsSigCondChannelTableSize,'nbsSigCondChannelTable':nbsSigCondChannelTable,'nbsSigCondChannelEntry':nbsSigCondChannelEntry,_T:nbsSigCondChannelIfIndex,_I:nbsSigCondChannelCenterline,'nbsSigCondChannelRxPower':nbsSigCondChannelRxPower,_L:nbsSigCondChannelTxPower,'nbsSigCondChannelTxAttenu':nbsSigCondChannelTxAttenu,'nbsSigCondChannelRxAttenu':nbsSigCondChannelRxAttenu,'nbsSigCondVodPortGrp':nbsSigCondVodPortGrp,'nbsSigCondVodPortTableSize':nbsSigCondVodPortTableSize,'nbsSigCondVodPortTable':nbsSigCondVodPortTable,'nbsSigCondVodPortEntry':nbsSigCondVodPortEntry,_U:nbsSigCondVodPortIfIndex,'nbsSigCondVodPortDispersionMin':nbsSigCondVodPortDispersionMin,'nbsSigCondVodPortDispersionMax':nbsSigCondVodPortDispersionMax,'nbsSigCondVodPortDispersionAdmin':nbsSigCondVodPortDispersionAdmin,'nbsSigCondVodPortDispersionOper':nbsSigCondVodPortDispersionOper,'nbsSigCondVodPortDispersionGridOffsetCenter':nbsSigCondVodPortDispersionGridOffsetCenter,'nbsSigCondVodPortDispersionGridOffsetMin':nbsSigCondVodPortDispersionGridOffsetMin,'nbsSigCondVodPortDispersionGridOffsetMax':nbsSigCondVodPortDispersionGridOffsetMax,'nbsSigCondVodPortDispersionGridOffsetStep':nbsSigCondVodPortDispersionGridOffsetStep,'nbsSigCondVodPortDispersionGridOffsetExponent':nbsSigCondVodPortDispersionGridOffsetExponent,'nbsSigCondVodPortDispersionGridOffsetAdmin':nbsSigCondVodPortDispersionGridOffsetAdmin,'nbsSigCondVodPortDispersionGridOffsetOper':nbsSigCondVodPortDispersionGridOffsetOper,'nbsSigCondTraps':nbsSigCondTraps,'nbsSigCondEvent':nbsSigCondEvent,'nbsSigCondEventEqualizeOk':nbsSigCondEventEqualizeOk,'nbsSigCondEventEqualizeTooLow':nbsSigCondEventEqualizeTooLow,'nbsSigCondEventEqualizeTooHigh':nbsSigCondEventEqualizeTooHigh})