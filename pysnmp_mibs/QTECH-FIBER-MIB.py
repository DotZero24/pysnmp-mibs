_AO='qtechFiberMIBGroup'
_AN='qtechFiberChannel4TXpowerStatus'
_AM='qtechFiberChannel4TXpowerDecimalpart'
_AL='qtechFiberChannel4TXpowerIntegerpart'
_AK='qtechFiberChannel3TXpowerStatus'
_AJ='qtechFiberChannel3TXpowerDecimalpart'
_AI='qtechFiberChannel3TXpowerIntegerpart'
_AH='qtechFiberChannel2TXpowerStatus'
_AG='qtechFiberChannel2TXpowerDecimalpart'
_AF='qtechFiberChannel2TXpowerIntegerpart'
_AE='qtechFiberChannel1TXpowerStatus'
_AD='qtechFiberChannel1TXpowerDecimalpart'
_AC='qtechFiberChannel1TXpowerIntegerpart'
_AB='qtechFiberTXpowerStatus'
_AA='qtechFiberTXpowerDecimalpart'
_A9='qtechFiberTXpowerIntegerpart'
_A8='qtechFiberChannel4RXpowerStatus'
_A7='qtechFiberChannel4RXpowertype'
_A6='qtechFiberChannel4RXpowerDecimalpart'
_A5='qtechFiberChannel4RXpowerIntegerpart'
_A4='qtechFiberChannel3RXpowerStatus'
_A3='qtechFiberChannel3RXpowertype'
_A2='qtechFiberChannel3RXpowerDecimalpart'
_A1='qtechFiberChannel3RXpowerIntegerpart'
_A0='qtechFiberChannel2RXpowerStatus'
_z='qtechFiberChannel2RXpowertype'
_y='qtechFiberChannel2RXpowerDecimalpart'
_x='qtechFiberChannel2RXpowerIntegerpart'
_w='qtechFiberChannel1RXpowerStatus'
_v='qtechFiberChannel1RXpowertype'
_u='qtechFiberChannel1RXpowerDecimalpart'
_t='qtechFiberChannel1RXpowerIntegerpart'
_s='qtechFiberRXpowerStatus'
_r='qtechFiberRXpowertype'
_q='qtechFiberRXpowerDecimalpart'
_p='qtechFiberRXpowerIntegerpart'
_o='qtechFiberChannel4BiasStatus'
_n='qtechFiberChannel4Bias'
_m='qtechFiberChannel3BiasStatus'
_l='qtechFiberChannel3Bias'
_k='qtechFiberChannel2BiasStatus'
_j='qtechFiberChannel2Bias'
_i='qtechFiberChannel1BiasStatus'
_h='qtechFiberChannel1Bias'
_g='qtechFiberBiasStatus'
_f='qtechFiberBias'
_e='qtechFiberVoltageStatus'
_d='qtechFiberVoltage'
_c='qtechFiberTempStatus'
_b='qtechFiberTemp'
_a='qtechFiberSerialNumber'
_Z='qtechFiberDDMSupportStatus'
_Y='qtechFiberTransferDistanceCableAssembly'
_X='qtechFiberTransferDistanceCopper'
_W='qtechFiberTransferDistanceEBW50um'
_V='qtechFiberTransferDistance50umOM3'
_U='qtechFiberTransferDistance50um'
_T='qtechFiberTransferDistance50umOM2'
_S='qtechFiberTransferDistance62point5um'
_R='qtechFiberTransferDistance62point5umOM1'
_Q='qtechFiberTransferDistanceSMF'
_P='qtechFiberWavelength'
_O='qtechFiberConnectorType'
_N='qtechFiberTransceiverType'
_M='qtechFiberPortDescr'
_L='qtechFiberPortIndex'
_K='DisplayString'
_J='oma'
_I='average'
_H='alarm'
_G='warning'
_F='ok'
_E='unknown'
_D='Integer32'
_C='read-only'
_B='QTECH-FIBER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention','TruthValue')
qtechFiberMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,105))
if mibBuilder.loadTexts:qtechFiberMIB.setRevisions(('2011-11-28 00:00',))
_QtechFiberMIBObjects_ObjectIdentity=ObjectIdentity
qtechFiberMIBObjects=_QtechFiberMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,105,1))
_QtechFiberTable_Object=MibTable
qtechFiberTable=_QtechFiberTable_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1))
if mibBuilder.loadTexts:qtechFiberTable.setStatus(_A)
_QtechFiberEntry_Object=MibTableRow
qtechFiberEntry=_QtechFiberEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1))
qtechFiberEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qtechFiberEntry.setStatus(_A)
_QtechFiberPortIndex_Type=IfIndex
_QtechFiberPortIndex_Object=MibTableColumn
qtechFiberPortIndex=_QtechFiberPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,1),_QtechFiberPortIndex_Type())
qtechFiberPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechFiberPortIndex.setStatus(_A)
class _QtechFiberPortDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechFiberPortDescr_Type.__name__=_K
_QtechFiberPortDescr_Object=MibTableColumn
qtechFiberPortDescr=_QtechFiberPortDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,2),_QtechFiberPortDescr_Type())
qtechFiberPortDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberPortDescr.setStatus(_A)
class _QtechFiberTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28)));namedValues=NamedValues(*((_E,1),('fiber100BASEGTSFP',2),('fiber100BASESXSFP',3),('fiber100BASELXSFP',4),('fiber100BASELHSFP',5),('fiber100BASEZXSFP',6),('fiber100CopperSFP',7),('fiber1000BASEGTSFP',8),('fiber1000BASESXSFP',9),('fiber1000BASELXSFP',10),('fiber1000BASELHSFP',11),('fiber1000BASEZXSFP',12),('fiber1000CopperSFP',13),('fiber10GCopperSFPPlus',14),('fiber10GBASESRSFPPlus',15),('fiber10GBASELRSFPPlus',16),('fiber10GBASEERSFPPlus',17),('fiber10GBASEZRSFPPlus',18),('fiber10GCopperXFP',19),('fiber10GBASESRXFP',20),('fiber10GBASELRXFP',21),('fiber10GBASEERXFP',22),('fiber10GBASEZRXFP',23),('fiber40GActiveCableQSFPPlus',24),('fiber40GLR4QSFPPlus',25),('fiber40GCopperQSFPPlus',26),('fiber40GSR4QSFPPlus',27),('fiber2500CopperSFP',28)))
_QtechFiberTransceiverType_Type.__name__=_D
_QtechFiberTransceiverType_Object=MibTableColumn
qtechFiberTransceiverType=_QtechFiberTransceiverType_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,3),_QtechFiberTransceiverType_Type())
qtechFiberTransceiverType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransceiverType.setStatus(_A)
class _QtechFiberConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('meaningless',0),('unknownorunspecified',1),('vendorspecific',2),('sc',3),('fiberChannelStyle1CopperConnector',4),('fiberChannelStyle2CopperConnector',5),('bncortnc',6),('fiberChannelCoaxialHeaders',7),('fiberJack',8),('lc',9),('mtrj',10),('mu',11),('sg',12),('opticalPigtail',13),('hssdcII',14),('copperPigtail',15),('mpo',16),('rj45',17),('noSparableConnector',18)))
_QtechFiberConnectorType_Type.__name__=_D
_QtechFiberConnectorType_Object=MibTableColumn
qtechFiberConnectorType=_QtechFiberConnectorType_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,4),_QtechFiberConnectorType_Type())
qtechFiberConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberConnectorType.setStatus(_A)
_QtechFiberWavelength_Type=Integer32
_QtechFiberWavelength_Object=MibTableColumn
qtechFiberWavelength=_QtechFiberWavelength_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,5),_QtechFiberWavelength_Type())
qtechFiberWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberWavelength.setStatus(_A)
_QtechFiberTransferDistanceSMF_Type=Integer32
_QtechFiberTransferDistanceSMF_Object=MibTableColumn
qtechFiberTransferDistanceSMF=_QtechFiberTransferDistanceSMF_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,6),_QtechFiberTransferDistanceSMF_Type())
qtechFiberTransferDistanceSMF.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistanceSMF.setStatus(_A)
_QtechFiberTransferDistance62point5umOM1_Type=Integer32
_QtechFiberTransferDistance62point5umOM1_Object=MibTableColumn
qtechFiberTransferDistance62point5umOM1=_QtechFiberTransferDistance62point5umOM1_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,7),_QtechFiberTransferDistance62point5umOM1_Type())
qtechFiberTransferDistance62point5umOM1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistance62point5umOM1.setStatus(_A)
_QtechFiberTransferDistance62point5um_Type=Integer32
_QtechFiberTransferDistance62point5um_Object=MibTableColumn
qtechFiberTransferDistance62point5um=_QtechFiberTransferDistance62point5um_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,8),_QtechFiberTransferDistance62point5um_Type())
qtechFiberTransferDistance62point5um.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistance62point5um.setStatus(_A)
_QtechFiberTransferDistance50umOM2_Type=Integer32
_QtechFiberTransferDistance50umOM2_Object=MibTableColumn
qtechFiberTransferDistance50umOM2=_QtechFiberTransferDistance50umOM2_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,9),_QtechFiberTransferDistance50umOM2_Type())
qtechFiberTransferDistance50umOM2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistance50umOM2.setStatus(_A)
_QtechFiberTransferDistance50um_Type=Integer32
_QtechFiberTransferDistance50um_Object=MibTableColumn
qtechFiberTransferDistance50um=_QtechFiberTransferDistance50um_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,10),_QtechFiberTransferDistance50um_Type())
qtechFiberTransferDistance50um.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistance50um.setStatus(_A)
_QtechFiberTransferDistance50umOM3_Type=Integer32
_QtechFiberTransferDistance50umOM3_Object=MibTableColumn
qtechFiberTransferDistance50umOM3=_QtechFiberTransferDistance50umOM3_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,11),_QtechFiberTransferDistance50umOM3_Type())
qtechFiberTransferDistance50umOM3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistance50umOM3.setStatus(_A)
_QtechFiberTransferDistanceEBW50um_Type=Integer32
_QtechFiberTransferDistanceEBW50um_Object=MibTableColumn
qtechFiberTransferDistanceEBW50um=_QtechFiberTransferDistanceEBW50um_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,12),_QtechFiberTransferDistanceEBW50um_Type())
qtechFiberTransferDistanceEBW50um.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistanceEBW50um.setStatus(_A)
_QtechFiberTransferDistanceCopper_Type=Integer32
_QtechFiberTransferDistanceCopper_Object=MibTableColumn
qtechFiberTransferDistanceCopper=_QtechFiberTransferDistanceCopper_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,13),_QtechFiberTransferDistanceCopper_Type())
qtechFiberTransferDistanceCopper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistanceCopper.setStatus(_A)
_QtechFiberTransferDistanceCableAssembly_Type=Integer32
_QtechFiberTransferDistanceCableAssembly_Object=MibTableColumn
qtechFiberTransferDistanceCableAssembly=_QtechFiberTransferDistanceCableAssembly_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,14),_QtechFiberTransferDistanceCableAssembly_Type())
qtechFiberTransferDistanceCableAssembly.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTransferDistanceCableAssembly.setStatus(_A)
_QtechFiberDDMSupportStatus_Type=TruthValue
_QtechFiberDDMSupportStatus_Object=MibTableColumn
qtechFiberDDMSupportStatus=_QtechFiberDDMSupportStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,15),_QtechFiberDDMSupportStatus_Type())
qtechFiberDDMSupportStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberDDMSupportStatus.setStatus(_A)
class _QtechFiberSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechFiberSerialNumber_Type.__name__=_K
_QtechFiberSerialNumber_Object=MibTableColumn
qtechFiberSerialNumber=_QtechFiberSerialNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,16),_QtechFiberSerialNumber_Type())
qtechFiberSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberSerialNumber.setStatus(_A)
_QtechFiberTemp_Type=Integer32
_QtechFiberTemp_Object=MibTableColumn
qtechFiberTemp=_QtechFiberTemp_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,17),_QtechFiberTemp_Type())
qtechFiberTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTemp.setStatus(_A)
class _QtechFiberTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberTempStatus_Type.__name__=_D
_QtechFiberTempStatus_Object=MibTableColumn
qtechFiberTempStatus=_QtechFiberTempStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,18),_QtechFiberTempStatus_Type())
qtechFiberTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTempStatus.setStatus(_A)
_QtechFiberVoltage_Type=Integer32
_QtechFiberVoltage_Object=MibTableColumn
qtechFiberVoltage=_QtechFiberVoltage_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,19),_QtechFiberVoltage_Type())
qtechFiberVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberVoltage.setStatus(_A)
class _QtechFiberVoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberVoltageStatus_Type.__name__=_D
_QtechFiberVoltageStatus_Object=MibTableColumn
qtechFiberVoltageStatus=_QtechFiberVoltageStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,20),_QtechFiberVoltageStatus_Type())
qtechFiberVoltageStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberVoltageStatus.setStatus(_A)
_QtechFiberBias_Type=Integer32
_QtechFiberBias_Object=MibTableColumn
qtechFiberBias=_QtechFiberBias_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,21),_QtechFiberBias_Type())
qtechFiberBias.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberBias.setStatus(_A)
class _QtechFiberBiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberBiasStatus_Type.__name__=_D
_QtechFiberBiasStatus_Object=MibTableColumn
qtechFiberBiasStatus=_QtechFiberBiasStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,22),_QtechFiberBiasStatus_Type())
qtechFiberBiasStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberBiasStatus.setStatus(_A)
_QtechFiberChannel1Bias_Type=Integer32
_QtechFiberChannel1Bias_Object=MibTableColumn
qtechFiberChannel1Bias=_QtechFiberChannel1Bias_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,23),_QtechFiberChannel1Bias_Type())
qtechFiberChannel1Bias.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1Bias.setStatus(_A)
class _QtechFiberChannel1BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel1BiasStatus_Type.__name__=_D
_QtechFiberChannel1BiasStatus_Object=MibTableColumn
qtechFiberChannel1BiasStatus=_QtechFiberChannel1BiasStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,24),_QtechFiberChannel1BiasStatus_Type())
qtechFiberChannel1BiasStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1BiasStatus.setStatus(_A)
_QtechFiberChannel2Bias_Type=Integer32
_QtechFiberChannel2Bias_Object=MibTableColumn
qtechFiberChannel2Bias=_QtechFiberChannel2Bias_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,25),_QtechFiberChannel2Bias_Type())
qtechFiberChannel2Bias.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2Bias.setStatus(_A)
class _QtechFiberChannel2BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel2BiasStatus_Type.__name__=_D
_QtechFiberChannel2BiasStatus_Object=MibTableColumn
qtechFiberChannel2BiasStatus=_QtechFiberChannel2BiasStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,26),_QtechFiberChannel2BiasStatus_Type())
qtechFiberChannel2BiasStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2BiasStatus.setStatus(_A)
_QtechFiberChannel3Bias_Type=Integer32
_QtechFiberChannel3Bias_Object=MibTableColumn
qtechFiberChannel3Bias=_QtechFiberChannel3Bias_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,27),_QtechFiberChannel3Bias_Type())
qtechFiberChannel3Bias.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3Bias.setStatus(_A)
class _QtechFiberChannel3BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel3BiasStatus_Type.__name__=_D
_QtechFiberChannel3BiasStatus_Object=MibTableColumn
qtechFiberChannel3BiasStatus=_QtechFiberChannel3BiasStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,28),_QtechFiberChannel3BiasStatus_Type())
qtechFiberChannel3BiasStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3BiasStatus.setStatus(_A)
_QtechFiberChannel4Bias_Type=Integer32
_QtechFiberChannel4Bias_Object=MibTableColumn
qtechFiberChannel4Bias=_QtechFiberChannel4Bias_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,29),_QtechFiberChannel4Bias_Type())
qtechFiberChannel4Bias.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4Bias.setStatus(_A)
class _QtechFiberChannel4BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel4BiasStatus_Type.__name__=_D
_QtechFiberChannel4BiasStatus_Object=MibTableColumn
qtechFiberChannel4BiasStatus=_QtechFiberChannel4BiasStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,30),_QtechFiberChannel4BiasStatus_Type())
qtechFiberChannel4BiasStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4BiasStatus.setStatus(_A)
_QtechFiberRXpowerIntegerpart_Type=Integer32
_QtechFiberRXpowerIntegerpart_Object=MibTableColumn
qtechFiberRXpowerIntegerpart=_QtechFiberRXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,31),_QtechFiberRXpowerIntegerpart_Type())
qtechFiberRXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberRXpowerIntegerpart.setStatus(_A)
_QtechFiberRXpowerDecimalpart_Type=Integer32
_QtechFiberRXpowerDecimalpart_Object=MibTableColumn
qtechFiberRXpowerDecimalpart=_QtechFiberRXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,32),_QtechFiberRXpowerDecimalpart_Type())
qtechFiberRXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberRXpowerDecimalpart.setStatus(_A)
class _QtechFiberRXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_QtechFiberRXpowertype_Type.__name__=_D
_QtechFiberRXpowertype_Object=MibTableColumn
qtechFiberRXpowertype=_QtechFiberRXpowertype_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,33),_QtechFiberRXpowertype_Type())
qtechFiberRXpowertype.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberRXpowertype.setStatus(_A)
class _QtechFiberRXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberRXpowerStatus_Type.__name__=_D
_QtechFiberRXpowerStatus_Object=MibTableColumn
qtechFiberRXpowerStatus=_QtechFiberRXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,34),_QtechFiberRXpowerStatus_Type())
qtechFiberRXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberRXpowerStatus.setStatus(_A)
_QtechFiberChannel1RXpowerIntegerpart_Type=Integer32
_QtechFiberChannel1RXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel1RXpowerIntegerpart=_QtechFiberChannel1RXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,35),_QtechFiberChannel1RXpowerIntegerpart_Type())
qtechFiberChannel1RXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1RXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel1RXpowerDecimalpart_Type=Integer32
_QtechFiberChannel1RXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel1RXpowerDecimalpart=_QtechFiberChannel1RXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,36),_QtechFiberChannel1RXpowerDecimalpart_Type())
qtechFiberChannel1RXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1RXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel1RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_QtechFiberChannel1RXpowertype_Type.__name__=_D
_QtechFiberChannel1RXpowertype_Object=MibTableColumn
qtechFiberChannel1RXpowertype=_QtechFiberChannel1RXpowertype_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,37),_QtechFiberChannel1RXpowertype_Type())
qtechFiberChannel1RXpowertype.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1RXpowertype.setStatus(_A)
class _QtechFiberChannel1RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel1RXpowerStatus_Type.__name__=_D
_QtechFiberChannel1RXpowerStatus_Object=MibTableColumn
qtechFiberChannel1RXpowerStatus=_QtechFiberChannel1RXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,38),_QtechFiberChannel1RXpowerStatus_Type())
qtechFiberChannel1RXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1RXpowerStatus.setStatus(_A)
_QtechFiberChannel2RXpowerIntegerpart_Type=Integer32
_QtechFiberChannel2RXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel2RXpowerIntegerpart=_QtechFiberChannel2RXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,39),_QtechFiberChannel2RXpowerIntegerpart_Type())
qtechFiberChannel2RXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2RXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel2RXpowerDecimalpart_Type=Integer32
_QtechFiberChannel2RXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel2RXpowerDecimalpart=_QtechFiberChannel2RXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,40),_QtechFiberChannel2RXpowerDecimalpart_Type())
qtechFiberChannel2RXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2RXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel2RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_QtechFiberChannel2RXpowertype_Type.__name__=_D
_QtechFiberChannel2RXpowertype_Object=MibTableColumn
qtechFiberChannel2RXpowertype=_QtechFiberChannel2RXpowertype_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,41),_QtechFiberChannel2RXpowertype_Type())
qtechFiberChannel2RXpowertype.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2RXpowertype.setStatus(_A)
class _QtechFiberChannel2RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel2RXpowerStatus_Type.__name__=_D
_QtechFiberChannel2RXpowerStatus_Object=MibTableColumn
qtechFiberChannel2RXpowerStatus=_QtechFiberChannel2RXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,42),_QtechFiberChannel2RXpowerStatus_Type())
qtechFiberChannel2RXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2RXpowerStatus.setStatus(_A)
_QtechFiberChannel3RXpowerIntegerpart_Type=Integer32
_QtechFiberChannel3RXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel3RXpowerIntegerpart=_QtechFiberChannel3RXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,43),_QtechFiberChannel3RXpowerIntegerpart_Type())
qtechFiberChannel3RXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3RXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel3RXpowerDecimalpart_Type=Integer32
_QtechFiberChannel3RXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel3RXpowerDecimalpart=_QtechFiberChannel3RXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,44),_QtechFiberChannel3RXpowerDecimalpart_Type())
qtechFiberChannel3RXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3RXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel3RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_QtechFiberChannel3RXpowertype_Type.__name__=_D
_QtechFiberChannel3RXpowertype_Object=MibTableColumn
qtechFiberChannel3RXpowertype=_QtechFiberChannel3RXpowertype_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,45),_QtechFiberChannel3RXpowertype_Type())
qtechFiberChannel3RXpowertype.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3RXpowertype.setStatus(_A)
class _QtechFiberChannel3RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel3RXpowerStatus_Type.__name__=_D
_QtechFiberChannel3RXpowerStatus_Object=MibTableColumn
qtechFiberChannel3RXpowerStatus=_QtechFiberChannel3RXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,46),_QtechFiberChannel3RXpowerStatus_Type())
qtechFiberChannel3RXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3RXpowerStatus.setStatus(_A)
_QtechFiberChannel4RXpowerIntegerpart_Type=Integer32
_QtechFiberChannel4RXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel4RXpowerIntegerpart=_QtechFiberChannel4RXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,47),_QtechFiberChannel4RXpowerIntegerpart_Type())
qtechFiberChannel4RXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4RXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel4RXpowerDecimalpart_Type=Integer32
_QtechFiberChannel4RXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel4RXpowerDecimalpart=_QtechFiberChannel4RXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,48),_QtechFiberChannel4RXpowerDecimalpart_Type())
qtechFiberChannel4RXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4RXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel4RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_QtechFiberChannel4RXpowertype_Type.__name__=_D
_QtechFiberChannel4RXpowertype_Object=MibTableColumn
qtechFiberChannel4RXpowertype=_QtechFiberChannel4RXpowertype_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,49),_QtechFiberChannel4RXpowertype_Type())
qtechFiberChannel4RXpowertype.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4RXpowertype.setStatus(_A)
class _QtechFiberChannel4RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel4RXpowerStatus_Type.__name__=_D
_QtechFiberChannel4RXpowerStatus_Object=MibTableColumn
qtechFiberChannel4RXpowerStatus=_QtechFiberChannel4RXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,50),_QtechFiberChannel4RXpowerStatus_Type())
qtechFiberChannel4RXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4RXpowerStatus.setStatus(_A)
_QtechFiberTXpowerIntegerpart_Type=Integer32
_QtechFiberTXpowerIntegerpart_Object=MibTableColumn
qtechFiberTXpowerIntegerpart=_QtechFiberTXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,51),_QtechFiberTXpowerIntegerpart_Type())
qtechFiberTXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTXpowerIntegerpart.setStatus(_A)
_QtechFiberTXpowerDecimalpart_Type=Integer32
_QtechFiberTXpowerDecimalpart_Object=MibTableColumn
qtechFiberTXpowerDecimalpart=_QtechFiberTXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,52),_QtechFiberTXpowerDecimalpart_Type())
qtechFiberTXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTXpowerDecimalpart.setStatus(_A)
class _QtechFiberTXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberTXpowerStatus_Type.__name__=_D
_QtechFiberTXpowerStatus_Object=MibTableColumn
qtechFiberTXpowerStatus=_QtechFiberTXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,53),_QtechFiberTXpowerStatus_Type())
qtechFiberTXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberTXpowerStatus.setStatus(_A)
_QtechFiberChannel1TXpowerIntegerpart_Type=Integer32
_QtechFiberChannel1TXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel1TXpowerIntegerpart=_QtechFiberChannel1TXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,54),_QtechFiberChannel1TXpowerIntegerpart_Type())
qtechFiberChannel1TXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1TXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel1TXpowerDecimalpart_Type=Integer32
_QtechFiberChannel1TXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel1TXpowerDecimalpart=_QtechFiberChannel1TXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,55),_QtechFiberChannel1TXpowerDecimalpart_Type())
qtechFiberChannel1TXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1TXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel1TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel1TXpowerStatus_Type.__name__=_D
_QtechFiberChannel1TXpowerStatus_Object=MibTableColumn
qtechFiberChannel1TXpowerStatus=_QtechFiberChannel1TXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,56),_QtechFiberChannel1TXpowerStatus_Type())
qtechFiberChannel1TXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel1TXpowerStatus.setStatus(_A)
_QtechFiberChannel2TXpowerIntegerpart_Type=Integer32
_QtechFiberChannel2TXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel2TXpowerIntegerpart=_QtechFiberChannel2TXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,57),_QtechFiberChannel2TXpowerIntegerpart_Type())
qtechFiberChannel2TXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2TXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel2TXpowerDecimalpart_Type=Integer32
_QtechFiberChannel2TXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel2TXpowerDecimalpart=_QtechFiberChannel2TXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,58),_QtechFiberChannel2TXpowerDecimalpart_Type())
qtechFiberChannel2TXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2TXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel2TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel2TXpowerStatus_Type.__name__=_D
_QtechFiberChannel2TXpowerStatus_Object=MibTableColumn
qtechFiberChannel2TXpowerStatus=_QtechFiberChannel2TXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,59),_QtechFiberChannel2TXpowerStatus_Type())
qtechFiberChannel2TXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel2TXpowerStatus.setStatus(_A)
_QtechFiberChannel3TXpowerIntegerpart_Type=Integer32
_QtechFiberChannel3TXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel3TXpowerIntegerpart=_QtechFiberChannel3TXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,60),_QtechFiberChannel3TXpowerIntegerpart_Type())
qtechFiberChannel3TXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3TXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel3TXpowerDecimalpart_Type=Integer32
_QtechFiberChannel3TXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel3TXpowerDecimalpart=_QtechFiberChannel3TXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,61),_QtechFiberChannel3TXpowerDecimalpart_Type())
qtechFiberChannel3TXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3TXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel3TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel3TXpowerStatus_Type.__name__=_D
_QtechFiberChannel3TXpowerStatus_Object=MibTableColumn
qtechFiberChannel3TXpowerStatus=_QtechFiberChannel3TXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,62),_QtechFiberChannel3TXpowerStatus_Type())
qtechFiberChannel3TXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel3TXpowerStatus.setStatus(_A)
_QtechFiberChannel4TXpowerIntegerpart_Type=Integer32
_QtechFiberChannel4TXpowerIntegerpart_Object=MibTableColumn
qtechFiberChannel4TXpowerIntegerpart=_QtechFiberChannel4TXpowerIntegerpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,63),_QtechFiberChannel4TXpowerIntegerpart_Type())
qtechFiberChannel4TXpowerIntegerpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4TXpowerIntegerpart.setStatus(_A)
_QtechFiberChannel4TXpowerDecimalpart_Type=Integer32
_QtechFiberChannel4TXpowerDecimalpart_Object=MibTableColumn
qtechFiberChannel4TXpowerDecimalpart=_QtechFiberChannel4TXpowerDecimalpart_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,64),_QtechFiberChannel4TXpowerDecimalpart_Type())
qtechFiberChannel4TXpowerDecimalpart.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4TXpowerDecimalpart.setStatus(_A)
class _QtechFiberChannel4TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_QtechFiberChannel4TXpowerStatus_Type.__name__=_D
_QtechFiberChannel4TXpowerStatus_Object=MibTableColumn
qtechFiberChannel4TXpowerStatus=_QtechFiberChannel4TXpowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,105,1,1,1,65),_QtechFiberChannel4TXpowerStatus_Type())
qtechFiberChannel4TXpowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFiberChannel4TXpowerStatus.setStatus(_A)
_QtechFiberMIBConformance_ObjectIdentity=ObjectIdentity
qtechFiberMIBConformance=_QtechFiberMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,105,2))
_QtechFiberMIBCompliances_ObjectIdentity=ObjectIdentity
qtechFiberMIBCompliances=_QtechFiberMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,105,2,1))
_QtechFiberMIBGroups_ObjectIdentity=ObjectIdentity
qtechFiberMIBGroups=_QtechFiberMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,105,2,2))
qtechFiberMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,105,2,2,1))
qtechFiberMIBGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:qtechFiberMIBGroup.setStatus(_A)
qtechFiberMIBConpliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,105,2,1,1))
qtechFiberMIBConpliance.setObjects((_B,_AO))
if mibBuilder.loadTexts:qtechFiberMIBConpliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechFiberMIB':qtechFiberMIB,'qtechFiberMIBObjects':qtechFiberMIBObjects,'qtechFiberTable':qtechFiberTable,'qtechFiberEntry':qtechFiberEntry,_L:qtechFiberPortIndex,_M:qtechFiberPortDescr,_N:qtechFiberTransceiverType,_O:qtechFiberConnectorType,_P:qtechFiberWavelength,_Q:qtechFiberTransferDistanceSMF,_R:qtechFiberTransferDistance62point5umOM1,_S:qtechFiberTransferDistance62point5um,_T:qtechFiberTransferDistance50umOM2,_U:qtechFiberTransferDistance50um,_V:qtechFiberTransferDistance50umOM3,_W:qtechFiberTransferDistanceEBW50um,_X:qtechFiberTransferDistanceCopper,_Y:qtechFiberTransferDistanceCableAssembly,_Z:qtechFiberDDMSupportStatus,_a:qtechFiberSerialNumber,_b:qtechFiberTemp,_c:qtechFiberTempStatus,_d:qtechFiberVoltage,_e:qtechFiberVoltageStatus,_f:qtechFiberBias,_g:qtechFiberBiasStatus,_h:qtechFiberChannel1Bias,_i:qtechFiberChannel1BiasStatus,_j:qtechFiberChannel2Bias,_k:qtechFiberChannel2BiasStatus,_l:qtechFiberChannel3Bias,_m:qtechFiberChannel3BiasStatus,_n:qtechFiberChannel4Bias,_o:qtechFiberChannel4BiasStatus,_p:qtechFiberRXpowerIntegerpart,_q:qtechFiberRXpowerDecimalpart,_r:qtechFiberRXpowertype,_s:qtechFiberRXpowerStatus,_t:qtechFiberChannel1RXpowerIntegerpart,_u:qtechFiberChannel1RXpowerDecimalpart,_v:qtechFiberChannel1RXpowertype,_w:qtechFiberChannel1RXpowerStatus,_x:qtechFiberChannel2RXpowerIntegerpart,_y:qtechFiberChannel2RXpowerDecimalpart,_z:qtechFiberChannel2RXpowertype,_A0:qtechFiberChannel2RXpowerStatus,_A1:qtechFiberChannel3RXpowerIntegerpart,_A2:qtechFiberChannel3RXpowerDecimalpart,_A3:qtechFiberChannel3RXpowertype,_A4:qtechFiberChannel3RXpowerStatus,_A5:qtechFiberChannel4RXpowerIntegerpart,_A6:qtechFiberChannel4RXpowerDecimalpart,_A7:qtechFiberChannel4RXpowertype,_A8:qtechFiberChannel4RXpowerStatus,_A9:qtechFiberTXpowerIntegerpart,_AA:qtechFiberTXpowerDecimalpart,_AB:qtechFiberTXpowerStatus,_AC:qtechFiberChannel1TXpowerIntegerpart,_AD:qtechFiberChannel1TXpowerDecimalpart,_AE:qtechFiberChannel1TXpowerStatus,_AF:qtechFiberChannel2TXpowerIntegerpart,_AG:qtechFiberChannel2TXpowerDecimalpart,_AH:qtechFiberChannel2TXpowerStatus,_AI:qtechFiberChannel3TXpowerIntegerpart,_AJ:qtechFiberChannel3TXpowerDecimalpart,_AK:qtechFiberChannel3TXpowerStatus,_AL:qtechFiberChannel4TXpowerIntegerpart,_AM:qtechFiberChannel4TXpowerDecimalpart,_AN:qtechFiberChannel4TXpowerStatus,'qtechFiberMIBConformance':qtechFiberMIBConformance,'qtechFiberMIBCompliances':qtechFiberMIBCompliances,'qtechFiberMIBConpliance':qtechFiberMIBConpliance,'qtechFiberMIBGroups':qtechFiberMIBGroups,_AO:qtechFiberMIBGroup})