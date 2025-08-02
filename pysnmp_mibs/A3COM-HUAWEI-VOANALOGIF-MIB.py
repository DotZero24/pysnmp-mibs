_Q='h3cVoAIfEMTimerPortIndex'
_P='h3cVoAIfEMCfgPortIndex'
_O='h3cVoAIfFXOTimerPortIndex'
_N='h3cVoAIfFXOCfgPortIndex'
_M='h3cVoAIfFXSTimerPortIndex'
_L='simple'
_K='complex'
_J='h3cVoAIfFXSCfgPortIndex'
_I='h3cVoAIfCfgPortIndex'
_H='disable'
_G='enable'
_F='not-accessible'
_E='A3COM-HUAWEI-VOANALOGIF-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cVoice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cVoiceAnalogInterface=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,39,3))
if mibBuilder.loadTexts:h3cVoiceAnalogInterface.setRevisions(('2005-03-15 00:00',))
_H3cVoAnalogIfCommonObjects_ObjectIdentity=ObjectIdentity
h3cVoAnalogIfCommonObjects=_H3cVoAnalogIfCommonObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,3,1))
_H3cVoAnalogIfCommonCfgTable_Object=MibTable
h3cVoAnalogIfCommonCfgTable=_H3cVoAnalogIfCommonCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,1,1))
if mibBuilder.loadTexts:h3cVoAnalogIfCommonCfgTable.setStatus(_A)
_H3cVoAnalogIfCommonCfgEntry_Object=MibTableRow
h3cVoAnalogIfCommonCfgEntry=_H3cVoAnalogIfCommonCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,1,1,1))
h3cVoAnalogIfCommonCfgEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:h3cVoAnalogIfCommonCfgEntry.setStatus(_A)
_H3cVoAIfCfgPortIndex_Type=Integer32
_H3cVoAIfCfgPortIndex_Object=MibTableColumn
h3cVoAIfCfgPortIndex=_H3cVoAIfCfgPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,1,1,1,1),_H3cVoAIfCfgPortIndex_Type())
h3cVoAIfCfgPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoAIfCfgPortIndex.setStatus(_A)
class _H3cVoAIfCfgPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fxs',1),('fxo',2),('em',3)))
_H3cVoAIfCfgPortType_Type.__name__=_C
_H3cVoAIfCfgPortType_Object=MibTableColumn
h3cVoAIfCfgPortType=_H3cVoAIfCfgPortType_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,1,1,1,2),_H3cVoAIfCfgPortType_Type())
h3cVoAIfCfgPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfCfgPortType.setStatus(_A)
_H3cVoAIfCfgPortSubLine_Type=OctetString
_H3cVoAIfCfgPortSubLine_Object=MibTableColumn
h3cVoAIfCfgPortSubLine=_H3cVoAIfCfgPortSubLine_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,1,1,1,3),_H3cVoAIfCfgPortSubLine_Type())
h3cVoAIfCfgPortSubLine.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfCfgPortSubLine.setStatus(_A)
_H3cVoAnalogIfFXSObjects_ObjectIdentity=ObjectIdentity
h3cVoAnalogIfFXSObjects=_H3cVoAnalogIfFXSObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,3,2))
_H3cVoAnalogIfFXSCfgTable_Object=MibTable
h3cVoAnalogIfFXSCfgTable=_H3cVoAnalogIfFXSCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,1))
if mibBuilder.loadTexts:h3cVoAnalogIfFXSCfgTable.setStatus(_A)
_H3cVoAnalogIfFXSCfgEntry_Object=MibTableRow
h3cVoAnalogIfFXSCfgEntry=_H3cVoAnalogIfFXSCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,1,1))
h3cVoAnalogIfFXSCfgEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:h3cVoAnalogIfFXSCfgEntry.setStatus(_A)
_H3cVoAIfFXSCfgPortIndex_Type=Integer32
_H3cVoAIfFXSCfgPortIndex_Object=MibTableColumn
h3cVoAIfFXSCfgPortIndex=_H3cVoAIfFXSCfgPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,1,1,1),_H3cVoAIfFXSCfgPortIndex_Type())
h3cVoAIfFXSCfgPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoAIfFXSCfgPortIndex.setStatus(_A)
class _H3cVoAIfFXSCfgCidDisplay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cVoAIfFXSCfgCidDisplay_Type.__name__=_C
_H3cVoAIfFXSCfgCidDisplay_Object=MibTableColumn
h3cVoAIfFXSCfgCidDisplay=_H3cVoAIfFXSCfgCidDisplay_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,1,1,3),_H3cVoAIfFXSCfgCidDisplay_Type())
h3cVoAIfFXSCfgCidDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXSCfgCidDisplay.setStatus(_A)
class _H3cVoAIfFXSCfgCidSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cVoAIfFXSCfgCidSend_Type.__name__=_C
_H3cVoAIfFXSCfgCidSend_Object=MibTableColumn
h3cVoAIfFXSCfgCidSend=_H3cVoAIfFXSCfgCidSend_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,1,1,4),_H3cVoAIfFXSCfgCidSend_Type())
h3cVoAIfFXSCfgCidSend.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXSCfgCidSend.setStatus(_A)
class _H3cVoAIfFXSCfgCidType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_H3cVoAIfFXSCfgCidType_Type.__name__=_C
_H3cVoAIfFXSCfgCidType_Object=MibTableColumn
h3cVoAIfFXSCfgCidType=_H3cVoAIfFXSCfgCidType_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,1,1,5),_H3cVoAIfFXSCfgCidType_Type())
h3cVoAIfFXSCfgCidType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXSCfgCidType.setStatus(_A)
_H3cVoAIfFXSCfgSubLine_Type=OctetString
_H3cVoAIfFXSCfgSubLine_Object=MibTableColumn
h3cVoAIfFXSCfgSubLine=_H3cVoAIfFXSCfgSubLine_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,1,1,6),_H3cVoAIfFXSCfgSubLine_Type())
h3cVoAIfFXSCfgSubLine.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfFXSCfgSubLine.setStatus(_A)
_H3cVoAnalogIfFXSTimerTable_Object=MibTable
h3cVoAnalogIfFXSTimerTable=_H3cVoAnalogIfFXSTimerTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,3))
if mibBuilder.loadTexts:h3cVoAnalogIfFXSTimerTable.setStatus(_A)
_H3cVoAnalogIfFXSTimerEntry_Object=MibTableRow
h3cVoAnalogIfFXSTimerEntry=_H3cVoAnalogIfFXSTimerEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,3,1))
h3cVoAnalogIfFXSTimerEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:h3cVoAnalogIfFXSTimerEntry.setStatus(_A)
_H3cVoAIfFXSTimerPortIndex_Type=Integer32
_H3cVoAIfFXSTimerPortIndex_Object=MibTableColumn
h3cVoAIfFXSTimerPortIndex=_H3cVoAIfFXSTimerPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,3,1,1),_H3cVoAIfFXSTimerPortIndex_Type())
h3cVoAIfFXSTimerPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoAIfFXSTimerPortIndex.setStatus(_A)
class _H3cVoAIfFXSTimerDialInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_H3cVoAIfFXSTimerDialInterval_Type.__name__=_C
_H3cVoAIfFXSTimerDialInterval_Object=MibTableColumn
h3cVoAIfFXSTimerDialInterval=_H3cVoAIfFXSTimerDialInterval_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,3,1,4),_H3cVoAIfFXSTimerDialInterval_Type())
h3cVoAIfFXSTimerDialInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXSTimerDialInterval.setStatus(_A)
class _H3cVoAIfFXSTimerFirstDial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_H3cVoAIfFXSTimerFirstDial_Type.__name__=_C
_H3cVoAIfFXSTimerFirstDial_Object=MibTableColumn
h3cVoAIfFXSTimerFirstDial=_H3cVoAIfFXSTimerFirstDial_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,3,1,5),_H3cVoAIfFXSTimerFirstDial_Type())
h3cVoAIfFXSTimerFirstDial.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXSTimerFirstDial.setStatus(_A)
_H3cVoAIfFXSTimerRingBack_Type=Integer32
_H3cVoAIfFXSTimerRingBack_Object=MibTableColumn
h3cVoAIfFXSTimerRingBack=_H3cVoAIfFXSTimerRingBack_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,3,1,6),_H3cVoAIfFXSTimerRingBack_Type())
h3cVoAIfFXSTimerRingBack.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXSTimerRingBack.setStatus(_A)
_H3cVoAIfFXSTimerSubLine_Type=OctetString
_H3cVoAIfFXSTimerSubLine_Object=MibTableColumn
h3cVoAIfFXSTimerSubLine=_H3cVoAIfFXSTimerSubLine_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,2,3,1,7),_H3cVoAIfFXSTimerSubLine_Type())
h3cVoAIfFXSTimerSubLine.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfFXSTimerSubLine.setStatus(_A)
_H3cVoAnalogIfFXOObjects_ObjectIdentity=ObjectIdentity
h3cVoAnalogIfFXOObjects=_H3cVoAnalogIfFXOObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,3,3))
_H3cVoAnalogIfFXOCfgTable_Object=MibTable
h3cVoAnalogIfFXOCfgTable=_H3cVoAnalogIfFXOCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1))
if mibBuilder.loadTexts:h3cVoAnalogIfFXOCfgTable.setStatus(_A)
_H3cVoAnalogIfFXOCfgEntry_Object=MibTableRow
h3cVoAnalogIfFXOCfgEntry=_H3cVoAnalogIfFXOCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1))
h3cVoAnalogIfFXOCfgEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:h3cVoAnalogIfFXOCfgEntry.setStatus(_A)
_H3cVoAIfFXOCfgPortIndex_Type=Integer32
_H3cVoAIfFXOCfgPortIndex_Object=MibTableColumn
h3cVoAIfFXOCfgPortIndex=_H3cVoAIfFXOCfgPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,1),_H3cVoAIfFXOCfgPortIndex_Type())
h3cVoAIfFXOCfgPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoAIfFXOCfgPortIndex.setStatus(_A)
class _H3cVoAIfFXOCfgArea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('custom',1),('europe',2),('northmerica',3)))
_H3cVoAIfFXOCfgArea_Type.__name__=_C
_H3cVoAIfFXOCfgArea_Object=MibTableColumn
h3cVoAIfFXOCfgArea=_H3cVoAIfFXOCfgArea_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,4),_H3cVoAIfFXOCfgArea_Type())
h3cVoAIfFXOCfgArea.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOCfgArea.setStatus(_A)
class _H3cVoAIfFXOPreDialDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_H3cVoAIfFXOPreDialDelay_Type.__name__=_C
_H3cVoAIfFXOPreDialDelay_Object=MibTableColumn
h3cVoAIfFXOPreDialDelay=_H3cVoAIfFXOPreDialDelay_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,5),_H3cVoAIfFXOPreDialDelay_Type())
h3cVoAIfFXOPreDialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOPreDialDelay.setStatus(_A)
class _H3cVoAIfFXOCfgPortImpedance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*(('australia',1),('austria',2),('belgiumLong',3),('belgiumShort',4),('brazil',5),('germanSwiss',6),('china',7),('greece',8),('czechRepublic',9),('denmark',10),('eTSIHarmanized',11),('finland',12),('france',13),('hungary',14),('india',15),('italy',16),('japan',17),('korea',18),('mexico',19),('netherlands',20),('norway',21),('portugal',22),('slovakia',23),('spain',24),('sweden',25),('uk',26),('usLoadedLine',27),('usNonLoaded',28),('usSpecialService',29),('r550',30),('r600',31),('r650',32),('r700',33),('r750',34),('r800',35),('r850',36),('r900',37),('r950',38)))
_H3cVoAIfFXOCfgPortImpedance_Type.__name__=_C
_H3cVoAIfFXOCfgPortImpedance_Object=MibTableColumn
h3cVoAIfFXOCfgPortImpedance=_H3cVoAIfFXOCfgPortImpedance_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,6),_H3cVoAIfFXOCfgPortImpedance_Type())
h3cVoAIfFXOCfgPortImpedance.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOCfgPortImpedance.setStatus(_A)
class _H3cVoAIfFXOCfgCidEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cVoAIfFXOCfgCidEnable_Type.__name__=_C
_H3cVoAIfFXOCfgCidEnable_Object=MibTableColumn
h3cVoAIfFXOCfgCidEnable=_H3cVoAIfFXOCfgCidEnable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,7),_H3cVoAIfFXOCfgCidEnable_Type())
h3cVoAIfFXOCfgCidEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOCfgCidEnable.setStatus(_A)
class _H3cVoAnalogIfFXOCfgCidSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cVoAnalogIfFXOCfgCidSend_Type.__name__=_C
_H3cVoAnalogIfFXOCfgCidSend_Object=MibTableColumn
h3cVoAnalogIfFXOCfgCidSend=_H3cVoAnalogIfFXOCfgCidSend_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,8),_H3cVoAnalogIfFXOCfgCidSend_Type())
h3cVoAnalogIfFXOCfgCidSend.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAnalogIfFXOCfgCidSend.setStatus(_A)
class _H3cVoAIfFXOCfgCidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_H3cVoAIfFXOCfgCidType_Type.__name__=_C
_H3cVoAIfFXOCfgCidType_Object=MibTableColumn
h3cVoAIfFXOCfgCidType=_H3cVoAIfFXOCfgCidType_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,9),_H3cVoAIfFXOCfgCidType_Type())
h3cVoAIfFXOCfgCidType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOCfgCidType.setStatus(_A)
_H3cVoAIfFXOCfgSubLine_Type=OctetString
_H3cVoAIfFXOCfgSubLine_Object=MibTableColumn
h3cVoAIfFXOCfgSubLine=_H3cVoAIfFXOCfgSubLine_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,1,1,10),_H3cVoAIfFXOCfgSubLine_Type())
h3cVoAIfFXOCfgSubLine.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfFXOCfgSubLine.setStatus(_A)
_H3cVoAnalogIfFXOTimerTable_Object=MibTable
h3cVoAnalogIfFXOTimerTable=_H3cVoAnalogIfFXOTimerTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3))
if mibBuilder.loadTexts:h3cVoAnalogIfFXOTimerTable.setStatus(_A)
_H3cVoAnalogIfFXOTimerEntry_Object=MibTableRow
h3cVoAnalogIfFXOTimerEntry=_H3cVoAnalogIfFXOTimerEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1))
h3cVoAnalogIfFXOTimerEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:h3cVoAnalogIfFXOTimerEntry.setStatus(_A)
_H3cVoAIfFXOTimerPortIndex_Type=Integer32
_H3cVoAIfFXOTimerPortIndex_Object=MibTableColumn
h3cVoAIfFXOTimerPortIndex=_H3cVoAIfFXOTimerPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1,1),_H3cVoAIfFXOTimerPortIndex_Type())
h3cVoAIfFXOTimerPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoAIfFXOTimerPortIndex.setStatus(_A)
_H3cVoAIfFXOTimerDtmf_Type=Integer32
_H3cVoAIfFXOTimerDtmf_Object=MibTableColumn
h3cVoAIfFXOTimerDtmf=_H3cVoAIfFXOTimerDtmf_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1,2),_H3cVoAIfFXOTimerDtmf_Type())
h3cVoAIfFXOTimerDtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOTimerDtmf.setStatus(_A)
_H3cVoAIfFXOTimerDtmfInterval_Type=Integer32
_H3cVoAIfFXOTimerDtmfInterval_Object=MibTableColumn
h3cVoAIfFXOTimerDtmfInterval=_H3cVoAIfFXOTimerDtmfInterval_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1,3),_H3cVoAIfFXOTimerDtmfInterval_Type())
h3cVoAIfFXOTimerDtmfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOTimerDtmfInterval.setStatus(_A)
_H3cVoAIfFXOTimerDialInterval_Type=Integer32
_H3cVoAIfFXOTimerDialInterval_Object=MibTableColumn
h3cVoAIfFXOTimerDialInterval=_H3cVoAIfFXOTimerDialInterval_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1,4),_H3cVoAIfFXOTimerDialInterval_Type())
h3cVoAIfFXOTimerDialInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOTimerDialInterval.setStatus(_A)
_H3cVoAIfFXOTimerFirstDial_Type=Integer32
_H3cVoAIfFXOTimerFirstDial_Object=MibTableColumn
h3cVoAIfFXOTimerFirstDial=_H3cVoAIfFXOTimerFirstDial_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1,5),_H3cVoAIfFXOTimerFirstDial_Type())
h3cVoAIfFXOTimerFirstDial.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOTimerFirstDial.setStatus(_A)
_H3cVoAIfFXOTimerRingBack_Type=Integer32
_H3cVoAIfFXOTimerRingBack_Object=MibTableColumn
h3cVoAIfFXOTimerRingBack=_H3cVoAIfFXOTimerRingBack_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1,6),_H3cVoAIfFXOTimerRingBack_Type())
h3cVoAIfFXOTimerRingBack.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfFXOTimerRingBack.setStatus(_A)
_H3cVoAIfFXOTimerSubLine_Type=OctetString
_H3cVoAIfFXOTimerSubLine_Object=MibTableColumn
h3cVoAIfFXOTimerSubLine=_H3cVoAIfFXOTimerSubLine_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,3,3,1,7),_H3cVoAIfFXOTimerSubLine_Type())
h3cVoAIfFXOTimerSubLine.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfFXOTimerSubLine.setStatus(_A)
_H3cVoAnalogIfEMObjects_ObjectIdentity=ObjectIdentity
h3cVoAnalogIfEMObjects=_H3cVoAnalogIfEMObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,3,4))
_H3cVoAnalogIfEMCfgTable_Object=MibTable
h3cVoAnalogIfEMCfgTable=_H3cVoAnalogIfEMCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1))
if mibBuilder.loadTexts:h3cVoAnalogIfEMCfgTable.setStatus(_A)
_H3cVoAnalogIfEMCfgEntry_Object=MibTableRow
h3cVoAnalogIfEMCfgEntry=_H3cVoAnalogIfEMCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1))
h3cVoAnalogIfEMCfgEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:h3cVoAnalogIfEMCfgEntry.setStatus(_A)
_H3cVoAIfEMCfgPortIndex_Type=Integer32
_H3cVoAIfEMCfgPortIndex_Object=MibTableColumn
h3cVoAIfEMCfgPortIndex=_H3cVoAIfEMCfgPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1,1),_H3cVoAIfEMCfgPortIndex_Type())
h3cVoAIfEMCfgPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfEMCfgPortIndex.setStatus(_A)
class _H3cVoAIfEMCfgSignalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('delayDial',1),('immediateDial',2),('winkStart',3)))
_H3cVoAIfEMCfgSignalMode_Type.__name__=_C
_H3cVoAIfEMCfgSignalMode_Object=MibTableColumn
h3cVoAIfEMCfgSignalMode=_H3cVoAIfEMCfgSignalMode_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1,2),_H3cVoAIfEMCfgSignalMode_Type())
h3cVoAIfEMCfgSignalMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMCfgSignalMode.setStatus(_A)
class _H3cVoAIfEMCfgPhyParm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoWiresOperation',1),('fourWiresOperation',2)))
_H3cVoAIfEMCfgPhyParm_Type.__name__=_C
_H3cVoAIfEMCfgPhyParm_Object=MibTableColumn
h3cVoAIfEMCfgPhyParm=_H3cVoAIfEMCfgPhyParm_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1,3),_H3cVoAIfEMCfgPhyParm_Type())
h3cVoAIfEMCfgPhyParm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMCfgPhyParm.setStatus(_A)
class _H3cVoAIfEMCfgPhyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3),('type5',5)))
_H3cVoAIfEMCfgPhyType_Type.__name__=_C
_H3cVoAIfEMCfgPhyType_Object=MibTableColumn
h3cVoAIfEMCfgPhyType=_H3cVoAIfEMCfgPhyType_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1,4),_H3cVoAIfEMCfgPhyType_Type())
h3cVoAIfEMCfgPhyType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMCfgPhyType.setStatus(_A)
class _H3cVoAIfEMCfgTimeoutRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_H3cVoAIfEMCfgTimeoutRing_Type.__name__=_C
_H3cVoAIfEMCfgTimeoutRing_Object=MibTableColumn
h3cVoAIfEMCfgTimeoutRing=_H3cVoAIfEMCfgTimeoutRing_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1,5),_H3cVoAIfEMCfgTimeoutRing_Type())
h3cVoAIfEMCfgTimeoutRing.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMCfgTimeoutRing.setStatus(_A)
_H3cVoAIfEMCfgTimeoutWaitDigit_Type=Integer32
_H3cVoAIfEMCfgTimeoutWaitDigit_Object=MibTableColumn
h3cVoAIfEMCfgTimeoutWaitDigit=_H3cVoAIfEMCfgTimeoutWaitDigit_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1,6),_H3cVoAIfEMCfgTimeoutWaitDigit_Type())
h3cVoAIfEMCfgTimeoutWaitDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMCfgTimeoutWaitDigit.setStatus(_A)
_H3cVoAIfEMCfgSubLine_Type=OctetString
_H3cVoAIfEMCfgSubLine_Object=MibTableColumn
h3cVoAIfEMCfgSubLine=_H3cVoAIfEMCfgSubLine_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,1,1,7),_H3cVoAIfEMCfgSubLine_Type())
h3cVoAIfEMCfgSubLine.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfEMCfgSubLine.setStatus(_A)
_H3cVoAnalogIfEMTimerTable_Object=MibTable
h3cVoAnalogIfEMTimerTable=_H3cVoAnalogIfEMTimerTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3))
if mibBuilder.loadTexts:h3cVoAnalogIfEMTimerTable.setStatus(_A)
_H3cVoAnalogIfEMTimerEntry_Object=MibTableRow
h3cVoAnalogIfEMTimerEntry=_H3cVoAnalogIfEMTimerEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1))
h3cVoAnalogIfEMTimerEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:h3cVoAnalogIfEMTimerEntry.setStatus(_A)
_H3cVoAIfEMTimerPortIndex_Type=Integer32
_H3cVoAIfEMTimerPortIndex_Object=MibTableColumn
h3cVoAIfEMTimerPortIndex=_H3cVoAIfEMTimerPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,1),_H3cVoAIfEMTimerPortIndex_Type())
h3cVoAIfEMTimerPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfEMTimerPortIndex.setStatus(_A)
_H3cVoAIfEMTimerDtmf_Type=Integer32
_H3cVoAIfEMTimerDtmf_Object=MibTableColumn
h3cVoAIfEMTimerDtmf=_H3cVoAIfEMTimerDtmf_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,2),_H3cVoAIfEMTimerDtmf_Type())
h3cVoAIfEMTimerDtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerDtmf.setStatus(_A)
_H3cVoAIfEMTimerDtmfInterval_Type=Integer32
_H3cVoAIfEMTimerDtmfInterval_Object=MibTableColumn
h3cVoAIfEMTimerDtmfInterval=_H3cVoAIfEMTimerDtmfInterval_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,3),_H3cVoAIfEMTimerDtmfInterval_Type())
h3cVoAIfEMTimerDtmfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerDtmfInterval.setStatus(_A)
class _H3cVoAIfEMTimerSendWink_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_H3cVoAIfEMTimerSendWink_Type.__name__=_C
_H3cVoAIfEMTimerSendWink_Object=MibTableColumn
h3cVoAIfEMTimerSendWink=_H3cVoAIfEMTimerSendWink_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,5),_H3cVoAIfEMTimerSendWink_Type())
h3cVoAIfEMTimerSendWink.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerSendWink.setStatus(_A)
_H3cVoAIfEMTimerWinkRising_Type=Integer32
_H3cVoAIfEMTimerWinkRising_Object=MibTableColumn
h3cVoAIfEMTimerWinkRising=_H3cVoAIfEMTimerWinkRising_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,6),_H3cVoAIfEMTimerWinkRising_Type())
h3cVoAIfEMTimerWinkRising.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerWinkRising.setStatus(_A)
_H3cVoAIfEMTimerWinkHold_Type=Integer32
_H3cVoAIfEMTimerWinkHold_Object=MibTableColumn
h3cVoAIfEMTimerWinkHold=_H3cVoAIfEMTimerWinkHold_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,7),_H3cVoAIfEMTimerWinkHold_Type())
h3cVoAIfEMTimerWinkHold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerWinkHold.setStatus(_A)
_H3cVoAIfEMTimerDialoutDelay_Type=Integer32
_H3cVoAIfEMTimerDialoutDelay_Object=MibTableColumn
h3cVoAIfEMTimerDialoutDelay=_H3cVoAIfEMTimerDialoutDelay_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,8),_H3cVoAIfEMTimerDialoutDelay_Type())
h3cVoAIfEMTimerDialoutDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerDialoutDelay.setStatus(_A)
_H3cVoAIfEMTimerDelayRising_Type=Integer32
_H3cVoAIfEMTimerDelayRising_Object=MibTableColumn
h3cVoAIfEMTimerDelayRising=_H3cVoAIfEMTimerDelayRising_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,9),_H3cVoAIfEMTimerDelayRising_Type())
h3cVoAIfEMTimerDelayRising.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerDelayRising.setStatus(_A)
_H3cVoAIfEMTimerDelayHold_Type=Integer32
_H3cVoAIfEMTimerDelayHold_Object=MibTableColumn
h3cVoAIfEMTimerDelayHold=_H3cVoAIfEMTimerDelayHold_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,10),_H3cVoAIfEMTimerDelayHold_Type())
h3cVoAIfEMTimerDelayHold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAIfEMTimerDelayHold.setStatus(_A)
_H3cVoAIfEMTimerSubLine_Type=OctetString
_H3cVoAIfEMTimerSubLine_Object=MibTableColumn
h3cVoAIfEMTimerSubLine=_H3cVoAIfEMTimerSubLine_Object((1,3,6,1,4,1,43,45,1,10,2,39,3,4,3,1,11),_H3cVoAIfEMTimerSubLine_Type())
h3cVoAIfEMTimerSubLine.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoAIfEMTimerSubLine.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cVoiceAnalogInterface':h3cVoiceAnalogInterface,'h3cVoAnalogIfCommonObjects':h3cVoAnalogIfCommonObjects,'h3cVoAnalogIfCommonCfgTable':h3cVoAnalogIfCommonCfgTable,'h3cVoAnalogIfCommonCfgEntry':h3cVoAnalogIfCommonCfgEntry,_I:h3cVoAIfCfgPortIndex,'h3cVoAIfCfgPortType':h3cVoAIfCfgPortType,'h3cVoAIfCfgPortSubLine':h3cVoAIfCfgPortSubLine,'h3cVoAnalogIfFXSObjects':h3cVoAnalogIfFXSObjects,'h3cVoAnalogIfFXSCfgTable':h3cVoAnalogIfFXSCfgTable,'h3cVoAnalogIfFXSCfgEntry':h3cVoAnalogIfFXSCfgEntry,_J:h3cVoAIfFXSCfgPortIndex,'h3cVoAIfFXSCfgCidDisplay':h3cVoAIfFXSCfgCidDisplay,'h3cVoAIfFXSCfgCidSend':h3cVoAIfFXSCfgCidSend,'h3cVoAIfFXSCfgCidType':h3cVoAIfFXSCfgCidType,'h3cVoAIfFXSCfgSubLine':h3cVoAIfFXSCfgSubLine,'h3cVoAnalogIfFXSTimerTable':h3cVoAnalogIfFXSTimerTable,'h3cVoAnalogIfFXSTimerEntry':h3cVoAnalogIfFXSTimerEntry,_M:h3cVoAIfFXSTimerPortIndex,'h3cVoAIfFXSTimerDialInterval':h3cVoAIfFXSTimerDialInterval,'h3cVoAIfFXSTimerFirstDial':h3cVoAIfFXSTimerFirstDial,'h3cVoAIfFXSTimerRingBack':h3cVoAIfFXSTimerRingBack,'h3cVoAIfFXSTimerSubLine':h3cVoAIfFXSTimerSubLine,'h3cVoAnalogIfFXOObjects':h3cVoAnalogIfFXOObjects,'h3cVoAnalogIfFXOCfgTable':h3cVoAnalogIfFXOCfgTable,'h3cVoAnalogIfFXOCfgEntry':h3cVoAnalogIfFXOCfgEntry,_N:h3cVoAIfFXOCfgPortIndex,'h3cVoAIfFXOCfgArea':h3cVoAIfFXOCfgArea,'h3cVoAIfFXOPreDialDelay':h3cVoAIfFXOPreDialDelay,'h3cVoAIfFXOCfgPortImpedance':h3cVoAIfFXOCfgPortImpedance,'h3cVoAIfFXOCfgCidEnable':h3cVoAIfFXOCfgCidEnable,'h3cVoAnalogIfFXOCfgCidSend':h3cVoAnalogIfFXOCfgCidSend,'h3cVoAIfFXOCfgCidType':h3cVoAIfFXOCfgCidType,'h3cVoAIfFXOCfgSubLine':h3cVoAIfFXOCfgSubLine,'h3cVoAnalogIfFXOTimerTable':h3cVoAnalogIfFXOTimerTable,'h3cVoAnalogIfFXOTimerEntry':h3cVoAnalogIfFXOTimerEntry,_O:h3cVoAIfFXOTimerPortIndex,'h3cVoAIfFXOTimerDtmf':h3cVoAIfFXOTimerDtmf,'h3cVoAIfFXOTimerDtmfInterval':h3cVoAIfFXOTimerDtmfInterval,'h3cVoAIfFXOTimerDialInterval':h3cVoAIfFXOTimerDialInterval,'h3cVoAIfFXOTimerFirstDial':h3cVoAIfFXOTimerFirstDial,'h3cVoAIfFXOTimerRingBack':h3cVoAIfFXOTimerRingBack,'h3cVoAIfFXOTimerSubLine':h3cVoAIfFXOTimerSubLine,'h3cVoAnalogIfEMObjects':h3cVoAnalogIfEMObjects,'h3cVoAnalogIfEMCfgTable':h3cVoAnalogIfEMCfgTable,'h3cVoAnalogIfEMCfgEntry':h3cVoAnalogIfEMCfgEntry,_P:h3cVoAIfEMCfgPortIndex,'h3cVoAIfEMCfgSignalMode':h3cVoAIfEMCfgSignalMode,'h3cVoAIfEMCfgPhyParm':h3cVoAIfEMCfgPhyParm,'h3cVoAIfEMCfgPhyType':h3cVoAIfEMCfgPhyType,'h3cVoAIfEMCfgTimeoutRing':h3cVoAIfEMCfgTimeoutRing,'h3cVoAIfEMCfgTimeoutWaitDigit':h3cVoAIfEMCfgTimeoutWaitDigit,'h3cVoAIfEMCfgSubLine':h3cVoAIfEMCfgSubLine,'h3cVoAnalogIfEMTimerTable':h3cVoAnalogIfEMTimerTable,'h3cVoAnalogIfEMTimerEntry':h3cVoAnalogIfEMTimerEntry,_Q:h3cVoAIfEMTimerPortIndex,'h3cVoAIfEMTimerDtmf':h3cVoAIfEMTimerDtmf,'h3cVoAIfEMTimerDtmfInterval':h3cVoAIfEMTimerDtmfInterval,'h3cVoAIfEMTimerSendWink':h3cVoAIfEMTimerSendWink,'h3cVoAIfEMTimerWinkRising':h3cVoAIfEMTimerWinkRising,'h3cVoAIfEMTimerWinkHold':h3cVoAIfEMTimerWinkHold,'h3cVoAIfEMTimerDialoutDelay':h3cVoAIfEMTimerDialoutDelay,'h3cVoAIfEMTimerDelayRising':h3cVoAIfEMTimerDelayRising,'h3cVoAIfEMTimerDelayHold':h3cVoAIfEMTimerDelayHold,'h3cVoAIfEMTimerSubLine':h3cVoAIfEMTimerSubLine})