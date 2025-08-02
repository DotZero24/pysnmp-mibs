_Ae='fsFiberAntifakeSerialNumberDescGroup'
_Ad='fsFiberAntifakeIntfNameDescGroup'
_Ac='fsFiberMIBGroup'
_Ab='fsFiberChannel4TXpowerSign'
_Aa='fsFiberChannel3TXpowerSign'
_AZ='fsFiberChannel2TXpowerSign'
_AY='fsFiberChannel1TXpowerSign'
_AX='fsFiberTXpowerSign'
_AW='fsFiberChannel4RXpowerSign'
_AV='fsFiberChannel3RXpowerSign'
_AU='fsFiberChannel2RXpowerSign'
_AT='fsFiberChannel1RXpowerSign'
_AS='fsFiberRXpowerSign'
_AR='fsFiberChannel4TXpowerStatus'
_AQ='fsFiberChannel4TXpowerDecimalpart'
_AP='fsFiberChannel4TXpowerIntegerpart'
_AO='fsFiberChannel3TXpowerStatus'
_AN='fsFiberChannel3TXpowerDecimalpart'
_AM='fsFiberChannel3TXpowerIntegerpart'
_AL='fsFiberChannel2TXpowerStatus'
_AK='fsFiberChannel2TXpowerDecimalpart'
_AJ='fsFiberChannel2TXpowerIntegerpart'
_AI='fsFiberChannel1TXpowerStatus'
_AH='fsFiberChannel1TXpowerDecimalpart'
_AG='fsFiberChannel1TXpowerIntegerpart'
_AF='fsFiberTXpowerStatus'
_AE='fsFiberTXpowerDecimalpart'
_AD='fsFiberTXpowerIntegerpart'
_AC='fsFiberChannel4RXpowerStatus'
_AB='fsFiberChannel4RXpowertype'
_AA='fsFiberChannel4RXpowerDecimalpart'
_A9='fsFiberChannel4RXpowerIntegerpart'
_A8='fsFiberChannel3RXpowerStatus'
_A7='fsFiberChannel3RXpowertype'
_A6='fsFiberChannel3RXpowerDecimalpart'
_A5='fsFiberChannel3RXpowerIntegerpart'
_A4='fsFiberChannel2RXpowerStatus'
_A3='fsFiberChannel2RXpowertype'
_A2='fsFiberChannel2RXpowerDecimalpart'
_A1='fsFiberChannel2RXpowerIntegerpart'
_A0='fsFiberChannel1RXpowerStatus'
_z='fsFiberChannel1RXpowertype'
_y='fsFiberChannel1RXpowerDecimalpart'
_x='fsFiberChannel1RXpowerIntegerpart'
_w='fsFiberRXpowerStatus'
_v='fsFiberRXpowertype'
_u='fsFiberRXpowerDecimalpart'
_t='fsFiberRXpowerIntegerpart'
_s='fsFiberChannel4BiasStatus'
_r='fsFiberChannel4Bias'
_q='fsFiberChannel3BiasStatus'
_p='fsFiberChannel3Bias'
_o='fsFiberChannel2BiasStatus'
_n='fsFiberChannel2Bias'
_m='fsFiberChannel1BiasStatus'
_l='fsFiberChannel1Bias'
_k='fsFiberBiasStatus'
_j='fsFiberBias'
_i='fsFiberVoltageStatus'
_h='fsFiberVoltage'
_g='fsFiberTempStatus'
_f='fsFiberTemp'
_e='fsFiberSerialNumber'
_d='fsFiberDDMSupportStatus'
_c='fsFiberTransferDistanceCableAssembly'
_b='fsFiberTransferDistanceCopper'
_a='fsFiberTransferDistanceEBW50um'
_Z='fsFiberTransferDistance50umOM3'
_Y='fsFiberTransferDistance50um'
_X='fsFiberTransferDistance50umOM2'
_W='fsFiberTransferDistance62point5um'
_V='fsFiberTransferDistance62point5umOM1'
_U='fsFiberTransferDistanceSMF'
_T='fsFiberWavelength'
_S='fsFiberConnectorType'
_R='fsFiberTransceiverType'
_Q='fsFiberPortDescr'
_P='accessible-for-notify'
_O='fsFiberVendorPortIndex'
_N='fsFiberPortIndex'
_M='fsFiberAntifakeSerialNumberDesc'
_L='fsFiberAntifakeIntfNameDesc'
_K='oma'
_J='average'
_I='DisplayString'
_H='alarm'
_G='warning'
_F='ok'
_E='unknown'
_D='Integer32'
_C='FS-FIBER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TruthValue')
fsFiberMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,105))
if mibBuilder.loadTexts:fsFiberMIB.setRevisions(('2011-11-28 00:00',))
_FsFiberMIBObjects_ObjectIdentity=ObjectIdentity
fsFiberMIBObjects=_FsFiberMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,105,1))
_FsFiberTable_Object=MibTable
fsFiberTable=_FsFiberTable_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1))
if mibBuilder.loadTexts:fsFiberTable.setStatus(_A)
_FsFiberEntry_Object=MibTableRow
fsFiberEntry=_FsFiberEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1))
fsFiberEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:fsFiberEntry.setStatus(_A)
_FsFiberPortIndex_Type=IfIndex
_FsFiberPortIndex_Object=MibTableColumn
fsFiberPortIndex=_FsFiberPortIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,1),_FsFiberPortIndex_Type())
fsFiberPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsFiberPortIndex.setStatus(_A)
class _FsFiberPortDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsFiberPortDescr_Type.__name__=_I
_FsFiberPortDescr_Object=MibTableColumn
fsFiberPortDescr=_FsFiberPortDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,2),_FsFiberPortDescr_Type())
fsFiberPortDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberPortDescr.setStatus(_A)
class _FsFiberTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49)));namedValues=NamedValues(*((_E,1),('fiber100BASEGTSFP',2),('fiber100BASESXSFP',3),('fiber100BASELXSFP',4),('fiber100BASELHSFP',5),('fiber100BASEZXSFP',6),('fiber100CopperSFP',7),('fiber1000BASEGTSFP',8),('fiber1000BASESXSFP',9),('fiber1000BASELXSFP',10),('fiber1000BASELHSFP',11),('fiber1000BASEZXSFP',12),('fiber1000CopperSFP',13),('fiber10GCopperSFPPlus',14),('fiber10GBASESRSFPPlus',15),('fiber10GBASELRSFPPlus',16),('fiber10GBASEERSFPPlus',17),('fiber10GBASEZRSFPPlus',18),('fiber10GCopperXFP',19),('fiber10GBASESRXFP',20),('fiber10GBASELRXFP',21),('fiber10GBASEERXFP',22),('fiber10GBASEZRXFP',23),('fiber40GActiveCableQSFPPlus',24),('fiber40GLR4QSFPPlus',25),('fiber40GCopperQSFPPlus',26),('fiber40GSR4QSFPPlus',27),('fiber2500CopperSFP',28),('fiberFC16G',29),('fiberFC8G',30),('fiberFC4G',31),('fiberFC2G',32),('fiber10GActiveCableSFPPlus',33),('fiber40GER4QSFPPlus',34),('fiber40GZR4QSFPPlus',35),('fiber100GCABLEQSFP28',36),('fiber100GLR4QSFP28',37),('fiber100GSR4QSFP28',38),('fiber100GER4QSFP28',39),('fiber100GZR4QSFP28',40),('fiber100GCR4QSFP28',41),('fiber100GPSM4QSFP28',42),('fiber25GSRSFP28',43),('fiber25GLRSFP28',44),('fiber25GERSFP28',45),('fiber25GZRSFP28',46),('fiber25GCOPPERSFP28',47),('fiber25GACTIVECABLESFP28',48),('fiber100GiLR4QSFP28',49)))
_FsFiberTransceiverType_Type.__name__=_D
_FsFiberTransceiverType_Object=MibTableColumn
fsFiberTransceiverType=_FsFiberTransceiverType_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,3),_FsFiberTransceiverType_Type())
fsFiberTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransceiverType.setStatus(_A)
class _FsFiberConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('meaningless',0),('unknownorunspecified',1),('vendorspecific',2),('sc',3),('fiberChannelStyle1CopperConnector',4),('fiberChannelStyle2CopperConnector',5),('bncortnc',6),('fiberChannelCoaxialHeaders',7),('fiberJack',8),('lc',9),('mtrj',10),('mu',11),('sg',12),('opticalPigtail',13),('hssdcII',14),('copperPigtail',15),('mpo',16),('rj45',17),('noSparableConnector',18)))
_FsFiberConnectorType_Type.__name__=_D
_FsFiberConnectorType_Object=MibTableColumn
fsFiberConnectorType=_FsFiberConnectorType_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,4),_FsFiberConnectorType_Type())
fsFiberConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberConnectorType.setStatus(_A)
_FsFiberWavelength_Type=Integer32
_FsFiberWavelength_Object=MibTableColumn
fsFiberWavelength=_FsFiberWavelength_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,5),_FsFiberWavelength_Type())
fsFiberWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberWavelength.setStatus(_A)
_FsFiberTransferDistanceSMF_Type=Integer32
_FsFiberTransferDistanceSMF_Object=MibTableColumn
fsFiberTransferDistanceSMF=_FsFiberTransferDistanceSMF_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,6),_FsFiberTransferDistanceSMF_Type())
fsFiberTransferDistanceSMF.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistanceSMF.setStatus(_A)
_FsFiberTransferDistance62point5umOM1_Type=Integer32
_FsFiberTransferDistance62point5umOM1_Object=MibTableColumn
fsFiberTransferDistance62point5umOM1=_FsFiberTransferDistance62point5umOM1_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,7),_FsFiberTransferDistance62point5umOM1_Type())
fsFiberTransferDistance62point5umOM1.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistance62point5umOM1.setStatus(_A)
_FsFiberTransferDistance62point5um_Type=Integer32
_FsFiberTransferDistance62point5um_Object=MibTableColumn
fsFiberTransferDistance62point5um=_FsFiberTransferDistance62point5um_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,8),_FsFiberTransferDistance62point5um_Type())
fsFiberTransferDistance62point5um.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistance62point5um.setStatus(_A)
_FsFiberTransferDistance50umOM2_Type=Integer32
_FsFiberTransferDistance50umOM2_Object=MibTableColumn
fsFiberTransferDistance50umOM2=_FsFiberTransferDistance50umOM2_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,9),_FsFiberTransferDistance50umOM2_Type())
fsFiberTransferDistance50umOM2.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistance50umOM2.setStatus(_A)
_FsFiberTransferDistance50um_Type=Integer32
_FsFiberTransferDistance50um_Object=MibTableColumn
fsFiberTransferDistance50um=_FsFiberTransferDistance50um_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,10),_FsFiberTransferDistance50um_Type())
fsFiberTransferDistance50um.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistance50um.setStatus(_A)
_FsFiberTransferDistance50umOM3_Type=Integer32
_FsFiberTransferDistance50umOM3_Object=MibTableColumn
fsFiberTransferDistance50umOM3=_FsFiberTransferDistance50umOM3_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,11),_FsFiberTransferDistance50umOM3_Type())
fsFiberTransferDistance50umOM3.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistance50umOM3.setStatus(_A)
_FsFiberTransferDistanceEBW50um_Type=Integer32
_FsFiberTransferDistanceEBW50um_Object=MibTableColumn
fsFiberTransferDistanceEBW50um=_FsFiberTransferDistanceEBW50um_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,12),_FsFiberTransferDistanceEBW50um_Type())
fsFiberTransferDistanceEBW50um.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistanceEBW50um.setStatus(_A)
_FsFiberTransferDistanceCopper_Type=Integer32
_FsFiberTransferDistanceCopper_Object=MibTableColumn
fsFiberTransferDistanceCopper=_FsFiberTransferDistanceCopper_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,13),_FsFiberTransferDistanceCopper_Type())
fsFiberTransferDistanceCopper.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistanceCopper.setStatus(_A)
_FsFiberTransferDistanceCableAssembly_Type=Integer32
_FsFiberTransferDistanceCableAssembly_Object=MibTableColumn
fsFiberTransferDistanceCableAssembly=_FsFiberTransferDistanceCableAssembly_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,14),_FsFiberTransferDistanceCableAssembly_Type())
fsFiberTransferDistanceCableAssembly.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTransferDistanceCableAssembly.setStatus(_A)
_FsFiberDDMSupportStatus_Type=TruthValue
_FsFiberDDMSupportStatus_Object=MibTableColumn
fsFiberDDMSupportStatus=_FsFiberDDMSupportStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,15),_FsFiberDDMSupportStatus_Type())
fsFiberDDMSupportStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberDDMSupportStatus.setStatus(_A)
class _FsFiberSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsFiberSerialNumber_Type.__name__=_I
_FsFiberSerialNumber_Object=MibTableColumn
fsFiberSerialNumber=_FsFiberSerialNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,16),_FsFiberSerialNumber_Type())
fsFiberSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberSerialNumber.setStatus(_A)
_FsFiberTemp_Type=Integer32
_FsFiberTemp_Object=MibTableColumn
fsFiberTemp=_FsFiberTemp_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,17),_FsFiberTemp_Type())
fsFiberTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTemp.setStatus(_A)
class _FsFiberTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberTempStatus_Type.__name__=_D
_FsFiberTempStatus_Object=MibTableColumn
fsFiberTempStatus=_FsFiberTempStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,18),_FsFiberTempStatus_Type())
fsFiberTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTempStatus.setStatus(_A)
_FsFiberVoltage_Type=Integer32
_FsFiberVoltage_Object=MibTableColumn
fsFiberVoltage=_FsFiberVoltage_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,19),_FsFiberVoltage_Type())
fsFiberVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVoltage.setStatus(_A)
class _FsFiberVoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberVoltageStatus_Type.__name__=_D
_FsFiberVoltageStatus_Object=MibTableColumn
fsFiberVoltageStatus=_FsFiberVoltageStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,20),_FsFiberVoltageStatus_Type())
fsFiberVoltageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVoltageStatus.setStatus(_A)
_FsFiberBias_Type=Integer32
_FsFiberBias_Object=MibTableColumn
fsFiberBias=_FsFiberBias_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,21),_FsFiberBias_Type())
fsFiberBias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberBias.setStatus(_A)
class _FsFiberBiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberBiasStatus_Type.__name__=_D
_FsFiberBiasStatus_Object=MibTableColumn
fsFiberBiasStatus=_FsFiberBiasStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,22),_FsFiberBiasStatus_Type())
fsFiberBiasStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberBiasStatus.setStatus(_A)
_FsFiberChannel1Bias_Type=Integer32
_FsFiberChannel1Bias_Object=MibTableColumn
fsFiberChannel1Bias=_FsFiberChannel1Bias_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,23),_FsFiberChannel1Bias_Type())
fsFiberChannel1Bias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1Bias.setStatus(_A)
class _FsFiberChannel1BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel1BiasStatus_Type.__name__=_D
_FsFiberChannel1BiasStatus_Object=MibTableColumn
fsFiberChannel1BiasStatus=_FsFiberChannel1BiasStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,24),_FsFiberChannel1BiasStatus_Type())
fsFiberChannel1BiasStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1BiasStatus.setStatus(_A)
_FsFiberChannel2Bias_Type=Integer32
_FsFiberChannel2Bias_Object=MibTableColumn
fsFiberChannel2Bias=_FsFiberChannel2Bias_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,25),_FsFiberChannel2Bias_Type())
fsFiberChannel2Bias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2Bias.setStatus(_A)
class _FsFiberChannel2BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel2BiasStatus_Type.__name__=_D
_FsFiberChannel2BiasStatus_Object=MibTableColumn
fsFiberChannel2BiasStatus=_FsFiberChannel2BiasStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,26),_FsFiberChannel2BiasStatus_Type())
fsFiberChannel2BiasStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2BiasStatus.setStatus(_A)
_FsFiberChannel3Bias_Type=Integer32
_FsFiberChannel3Bias_Object=MibTableColumn
fsFiberChannel3Bias=_FsFiberChannel3Bias_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,27),_FsFiberChannel3Bias_Type())
fsFiberChannel3Bias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3Bias.setStatus(_A)
class _FsFiberChannel3BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel3BiasStatus_Type.__name__=_D
_FsFiberChannel3BiasStatus_Object=MibTableColumn
fsFiberChannel3BiasStatus=_FsFiberChannel3BiasStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,28),_FsFiberChannel3BiasStatus_Type())
fsFiberChannel3BiasStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3BiasStatus.setStatus(_A)
_FsFiberChannel4Bias_Type=Integer32
_FsFiberChannel4Bias_Object=MibTableColumn
fsFiberChannel4Bias=_FsFiberChannel4Bias_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,29),_FsFiberChannel4Bias_Type())
fsFiberChannel4Bias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4Bias.setStatus(_A)
class _FsFiberChannel4BiasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel4BiasStatus_Type.__name__=_D
_FsFiberChannel4BiasStatus_Object=MibTableColumn
fsFiberChannel4BiasStatus=_FsFiberChannel4BiasStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,30),_FsFiberChannel4BiasStatus_Type())
fsFiberChannel4BiasStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4BiasStatus.setStatus(_A)
_FsFiberRXpowerIntegerpart_Type=Integer32
_FsFiberRXpowerIntegerpart_Object=MibTableColumn
fsFiberRXpowerIntegerpart=_FsFiberRXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,31),_FsFiberRXpowerIntegerpart_Type())
fsFiberRXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberRXpowerIntegerpart.setStatus(_A)
_FsFiberRXpowerDecimalpart_Type=Integer32
_FsFiberRXpowerDecimalpart_Object=MibTableColumn
fsFiberRXpowerDecimalpart=_FsFiberRXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,32),_FsFiberRXpowerDecimalpart_Type())
fsFiberRXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberRXpowerDecimalpart.setStatus(_A)
class _FsFiberRXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3)))
_FsFiberRXpowertype_Type.__name__=_D
_FsFiberRXpowertype_Object=MibTableColumn
fsFiberRXpowertype=_FsFiberRXpowertype_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,33),_FsFiberRXpowertype_Type())
fsFiberRXpowertype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberRXpowertype.setStatus(_A)
class _FsFiberRXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberRXpowerStatus_Type.__name__=_D
_FsFiberRXpowerStatus_Object=MibTableColumn
fsFiberRXpowerStatus=_FsFiberRXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,34),_FsFiberRXpowerStatus_Type())
fsFiberRXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberRXpowerStatus.setStatus(_A)
_FsFiberChannel1RXpowerIntegerpart_Type=Integer32
_FsFiberChannel1RXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel1RXpowerIntegerpart=_FsFiberChannel1RXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,35),_FsFiberChannel1RXpowerIntegerpart_Type())
fsFiberChannel1RXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1RXpowerIntegerpart.setStatus(_A)
_FsFiberChannel1RXpowerDecimalpart_Type=Integer32
_FsFiberChannel1RXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel1RXpowerDecimalpart=_FsFiberChannel1RXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,36),_FsFiberChannel1RXpowerDecimalpart_Type())
fsFiberChannel1RXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1RXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel1RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3)))
_FsFiberChannel1RXpowertype_Type.__name__=_D
_FsFiberChannel1RXpowertype_Object=MibTableColumn
fsFiberChannel1RXpowertype=_FsFiberChannel1RXpowertype_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,37),_FsFiberChannel1RXpowertype_Type())
fsFiberChannel1RXpowertype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1RXpowertype.setStatus(_A)
class _FsFiberChannel1RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel1RXpowerStatus_Type.__name__=_D
_FsFiberChannel1RXpowerStatus_Object=MibTableColumn
fsFiberChannel1RXpowerStatus=_FsFiberChannel1RXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,38),_FsFiberChannel1RXpowerStatus_Type())
fsFiberChannel1RXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1RXpowerStatus.setStatus(_A)
_FsFiberChannel2RXpowerIntegerpart_Type=Integer32
_FsFiberChannel2RXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel2RXpowerIntegerpart=_FsFiberChannel2RXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,39),_FsFiberChannel2RXpowerIntegerpart_Type())
fsFiberChannel2RXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2RXpowerIntegerpart.setStatus(_A)
_FsFiberChannel2RXpowerDecimalpart_Type=Integer32
_FsFiberChannel2RXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel2RXpowerDecimalpart=_FsFiberChannel2RXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,40),_FsFiberChannel2RXpowerDecimalpart_Type())
fsFiberChannel2RXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2RXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel2RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3)))
_FsFiberChannel2RXpowertype_Type.__name__=_D
_FsFiberChannel2RXpowertype_Object=MibTableColumn
fsFiberChannel2RXpowertype=_FsFiberChannel2RXpowertype_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,41),_FsFiberChannel2RXpowertype_Type())
fsFiberChannel2RXpowertype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2RXpowertype.setStatus(_A)
class _FsFiberChannel2RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel2RXpowerStatus_Type.__name__=_D
_FsFiberChannel2RXpowerStatus_Object=MibTableColumn
fsFiberChannel2RXpowerStatus=_FsFiberChannel2RXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,42),_FsFiberChannel2RXpowerStatus_Type())
fsFiberChannel2RXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2RXpowerStatus.setStatus(_A)
_FsFiberChannel3RXpowerIntegerpart_Type=Integer32
_FsFiberChannel3RXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel3RXpowerIntegerpart=_FsFiberChannel3RXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,43),_FsFiberChannel3RXpowerIntegerpart_Type())
fsFiberChannel3RXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3RXpowerIntegerpart.setStatus(_A)
_FsFiberChannel3RXpowerDecimalpart_Type=Integer32
_FsFiberChannel3RXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel3RXpowerDecimalpart=_FsFiberChannel3RXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,44),_FsFiberChannel3RXpowerDecimalpart_Type())
fsFiberChannel3RXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3RXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel3RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3)))
_FsFiberChannel3RXpowertype_Type.__name__=_D
_FsFiberChannel3RXpowertype_Object=MibTableColumn
fsFiberChannel3RXpowertype=_FsFiberChannel3RXpowertype_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,45),_FsFiberChannel3RXpowertype_Type())
fsFiberChannel3RXpowertype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3RXpowertype.setStatus(_A)
class _FsFiberChannel3RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel3RXpowerStatus_Type.__name__=_D
_FsFiberChannel3RXpowerStatus_Object=MibTableColumn
fsFiberChannel3RXpowerStatus=_FsFiberChannel3RXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,46),_FsFiberChannel3RXpowerStatus_Type())
fsFiberChannel3RXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3RXpowerStatus.setStatus(_A)
_FsFiberChannel4RXpowerIntegerpart_Type=Integer32
_FsFiberChannel4RXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel4RXpowerIntegerpart=_FsFiberChannel4RXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,47),_FsFiberChannel4RXpowerIntegerpart_Type())
fsFiberChannel4RXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4RXpowerIntegerpart.setStatus(_A)
_FsFiberChannel4RXpowerDecimalpart_Type=Integer32
_FsFiberChannel4RXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel4RXpowerDecimalpart=_FsFiberChannel4RXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,48),_FsFiberChannel4RXpowerDecimalpart_Type())
fsFiberChannel4RXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4RXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel4RXpowertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3)))
_FsFiberChannel4RXpowertype_Type.__name__=_D
_FsFiberChannel4RXpowertype_Object=MibTableColumn
fsFiberChannel4RXpowertype=_FsFiberChannel4RXpowertype_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,49),_FsFiberChannel4RXpowertype_Type())
fsFiberChannel4RXpowertype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4RXpowertype.setStatus(_A)
class _FsFiberChannel4RXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel4RXpowerStatus_Type.__name__=_D
_FsFiberChannel4RXpowerStatus_Object=MibTableColumn
fsFiberChannel4RXpowerStatus=_FsFiberChannel4RXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,50),_FsFiberChannel4RXpowerStatus_Type())
fsFiberChannel4RXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4RXpowerStatus.setStatus(_A)
_FsFiberTXpowerIntegerpart_Type=Integer32
_FsFiberTXpowerIntegerpart_Object=MibTableColumn
fsFiberTXpowerIntegerpart=_FsFiberTXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,51),_FsFiberTXpowerIntegerpart_Type())
fsFiberTXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTXpowerIntegerpart.setStatus(_A)
_FsFiberTXpowerDecimalpart_Type=Integer32
_FsFiberTXpowerDecimalpart_Object=MibTableColumn
fsFiberTXpowerDecimalpart=_FsFiberTXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,52),_FsFiberTXpowerDecimalpart_Type())
fsFiberTXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTXpowerDecimalpart.setStatus(_A)
class _FsFiberTXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberTXpowerStatus_Type.__name__=_D
_FsFiberTXpowerStatus_Object=MibTableColumn
fsFiberTXpowerStatus=_FsFiberTXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,53),_FsFiberTXpowerStatus_Type())
fsFiberTXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTXpowerStatus.setStatus(_A)
_FsFiberChannel1TXpowerIntegerpart_Type=Integer32
_FsFiberChannel1TXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel1TXpowerIntegerpart=_FsFiberChannel1TXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,54),_FsFiberChannel1TXpowerIntegerpart_Type())
fsFiberChannel1TXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1TXpowerIntegerpart.setStatus(_A)
_FsFiberChannel1TXpowerDecimalpart_Type=Integer32
_FsFiberChannel1TXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel1TXpowerDecimalpart=_FsFiberChannel1TXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,55),_FsFiberChannel1TXpowerDecimalpart_Type())
fsFiberChannel1TXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1TXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel1TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel1TXpowerStatus_Type.__name__=_D
_FsFiberChannel1TXpowerStatus_Object=MibTableColumn
fsFiberChannel1TXpowerStatus=_FsFiberChannel1TXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,56),_FsFiberChannel1TXpowerStatus_Type())
fsFiberChannel1TXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1TXpowerStatus.setStatus(_A)
_FsFiberChannel2TXpowerIntegerpart_Type=Integer32
_FsFiberChannel2TXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel2TXpowerIntegerpart=_FsFiberChannel2TXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,57),_FsFiberChannel2TXpowerIntegerpart_Type())
fsFiberChannel2TXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2TXpowerIntegerpart.setStatus(_A)
_FsFiberChannel2TXpowerDecimalpart_Type=Integer32
_FsFiberChannel2TXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel2TXpowerDecimalpart=_FsFiberChannel2TXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,58),_FsFiberChannel2TXpowerDecimalpart_Type())
fsFiberChannel2TXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2TXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel2TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel2TXpowerStatus_Type.__name__=_D
_FsFiberChannel2TXpowerStatus_Object=MibTableColumn
fsFiberChannel2TXpowerStatus=_FsFiberChannel2TXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,59),_FsFiberChannel2TXpowerStatus_Type())
fsFiberChannel2TXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2TXpowerStatus.setStatus(_A)
_FsFiberChannel3TXpowerIntegerpart_Type=Integer32
_FsFiberChannel3TXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel3TXpowerIntegerpart=_FsFiberChannel3TXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,60),_FsFiberChannel3TXpowerIntegerpart_Type())
fsFiberChannel3TXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3TXpowerIntegerpart.setStatus(_A)
_FsFiberChannel3TXpowerDecimalpart_Type=Integer32
_FsFiberChannel3TXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel3TXpowerDecimalpart=_FsFiberChannel3TXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,61),_FsFiberChannel3TXpowerDecimalpart_Type())
fsFiberChannel3TXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3TXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel3TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel3TXpowerStatus_Type.__name__=_D
_FsFiberChannel3TXpowerStatus_Object=MibTableColumn
fsFiberChannel3TXpowerStatus=_FsFiberChannel3TXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,62),_FsFiberChannel3TXpowerStatus_Type())
fsFiberChannel3TXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3TXpowerStatus.setStatus(_A)
_FsFiberChannel4TXpowerIntegerpart_Type=Integer32
_FsFiberChannel4TXpowerIntegerpart_Object=MibTableColumn
fsFiberChannel4TXpowerIntegerpart=_FsFiberChannel4TXpowerIntegerpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,63),_FsFiberChannel4TXpowerIntegerpart_Type())
fsFiberChannel4TXpowerIntegerpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4TXpowerIntegerpart.setStatus(_A)
_FsFiberChannel4TXpowerDecimalpart_Type=Integer32
_FsFiberChannel4TXpowerDecimalpart_Object=MibTableColumn
fsFiberChannel4TXpowerDecimalpart=_FsFiberChannel4TXpowerDecimalpart_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,64),_FsFiberChannel4TXpowerDecimalpart_Type())
fsFiberChannel4TXpowerDecimalpart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4TXpowerDecimalpart.setStatus(_A)
class _FsFiberChannel4TXpowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_FsFiberChannel4TXpowerStatus_Type.__name__=_D
_FsFiberChannel4TXpowerStatus_Object=MibTableColumn
fsFiberChannel4TXpowerStatus=_FsFiberChannel4TXpowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,65),_FsFiberChannel4TXpowerStatus_Type())
fsFiberChannel4TXpowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4TXpowerStatus.setStatus(_A)
_FsFiberRXpowerSign_Type=Integer32
_FsFiberRXpowerSign_Object=MibTableColumn
fsFiberRXpowerSign=_FsFiberRXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,66),_FsFiberRXpowerSign_Type())
fsFiberRXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberRXpowerSign.setStatus(_A)
_FsFiberChannel1RXpowerSign_Type=Integer32
_FsFiberChannel1RXpowerSign_Object=MibTableColumn
fsFiberChannel1RXpowerSign=_FsFiberChannel1RXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,67),_FsFiberChannel1RXpowerSign_Type())
fsFiberChannel1RXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1RXpowerSign.setStatus(_A)
_FsFiberChannel2RXpowerSign_Type=Integer32
_FsFiberChannel2RXpowerSign_Object=MibTableColumn
fsFiberChannel2RXpowerSign=_FsFiberChannel2RXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,68),_FsFiberChannel2RXpowerSign_Type())
fsFiberChannel2RXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2RXpowerSign.setStatus(_A)
_FsFiberChannel3RXpowerSign_Type=Integer32
_FsFiberChannel3RXpowerSign_Object=MibTableColumn
fsFiberChannel3RXpowerSign=_FsFiberChannel3RXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,69),_FsFiberChannel3RXpowerSign_Type())
fsFiberChannel3RXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3RXpowerSign.setStatus(_A)
_FsFiberChannel4RXpowerSign_Type=Integer32
_FsFiberChannel4RXpowerSign_Object=MibTableColumn
fsFiberChannel4RXpowerSign=_FsFiberChannel4RXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,70),_FsFiberChannel4RXpowerSign_Type())
fsFiberChannel4RXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4RXpowerSign.setStatus(_A)
_FsFiberTXpowerSign_Type=Integer32
_FsFiberTXpowerSign_Object=MibTableColumn
fsFiberTXpowerSign=_FsFiberTXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,71),_FsFiberTXpowerSign_Type())
fsFiberTXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTXpowerSign.setStatus(_A)
_FsFiberChannel1TXpowerSign_Type=Integer32
_FsFiberChannel1TXpowerSign_Object=MibTableColumn
fsFiberChannel1TXpowerSign=_FsFiberChannel1TXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,72),_FsFiberChannel1TXpowerSign_Type())
fsFiberChannel1TXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1TXpowerSign.setStatus(_A)
_FsFiberChannel2TXpowerSign_Type=Integer32
_FsFiberChannel2TXpowerSign_Object=MibTableColumn
fsFiberChannel2TXpowerSign=_FsFiberChannel2TXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,73),_FsFiberChannel2TXpowerSign_Type())
fsFiberChannel2TXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2TXpowerSign.setStatus(_A)
_FsFiberChannel3TXpowerSign_Type=Integer32
_FsFiberChannel3TXpowerSign_Object=MibTableColumn
fsFiberChannel3TXpowerSign=_FsFiberChannel3TXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,74),_FsFiberChannel3TXpowerSign_Type())
fsFiberChannel3TXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3TXpowerSign.setStatus(_A)
_FsFiberChannel4TXpowerSign_Type=Integer32
_FsFiberChannel4TXpowerSign_Object=MibTableColumn
fsFiberChannel4TXpowerSign=_FsFiberChannel4TXpowerSign_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,75),_FsFiberChannel4TXpowerSign_Type())
fsFiberChannel4TXpowerSign.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4TXpowerSign.setStatus(_A)
_FsFiberRXpowerInteger_Type=Integer32
_FsFiberRXpowerInteger_Object=MibTableColumn
fsFiberRXpowerInteger=_FsFiberRXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,76),_FsFiberRXpowerInteger_Type())
fsFiberRXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberRXpowerInteger.setStatus(_A)
_FsFiberChannel1RXpowerInteger_Type=Integer32
_FsFiberChannel1RXpowerInteger_Object=MibTableColumn
fsFiberChannel1RXpowerInteger=_FsFiberChannel1RXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,77),_FsFiberChannel1RXpowerInteger_Type())
fsFiberChannel1RXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1RXpowerInteger.setStatus(_A)
_FsFiberChannel2RXpowerInteger_Type=Integer32
_FsFiberChannel2RXpowerInteger_Object=MibTableColumn
fsFiberChannel2RXpowerInteger=_FsFiberChannel2RXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,78),_FsFiberChannel2RXpowerInteger_Type())
fsFiberChannel2RXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2RXpowerInteger.setStatus(_A)
_FsFiberChannel3RXpowerInteger_Type=Integer32
_FsFiberChannel3RXpowerInteger_Object=MibTableColumn
fsFiberChannel3RXpowerInteger=_FsFiberChannel3RXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,79),_FsFiberChannel3RXpowerInteger_Type())
fsFiberChannel3RXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3RXpowerInteger.setStatus(_A)
_FsFiberChannel4RXpowerInteger_Type=Integer32
_FsFiberChannel4RXpowerInteger_Object=MibTableColumn
fsFiberChannel4RXpowerInteger=_FsFiberChannel4RXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,80),_FsFiberChannel4RXpowerInteger_Type())
fsFiberChannel4RXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4RXpowerInteger.setStatus(_A)
_FsFiberTXpowerInteger_Type=Integer32
_FsFiberTXpowerInteger_Object=MibTableColumn
fsFiberTXpowerInteger=_FsFiberTXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,81),_FsFiberTXpowerInteger_Type())
fsFiberTXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberTXpowerInteger.setStatus(_A)
_FsFiberChannel1TXpowerInteger_Type=Integer32
_FsFiberChannel1TXpowerInteger_Object=MibTableColumn
fsFiberChannel1TXpowerInteger=_FsFiberChannel1TXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,82),_FsFiberChannel1TXpowerInteger_Type())
fsFiberChannel1TXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel1TXpowerInteger.setStatus(_A)
_FsFiberChannel2TXpowerInteger_Type=Integer32
_FsFiberChannel2TXpowerInteger_Object=MibTableColumn
fsFiberChannel2TXpowerInteger=_FsFiberChannel2TXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,83),_FsFiberChannel2TXpowerInteger_Type())
fsFiberChannel2TXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel2TXpowerInteger.setStatus(_A)
_FsFiberChannel3TXpowerInteger_Type=Integer32
_FsFiberChannel3TXpowerInteger_Object=MibTableColumn
fsFiberChannel3TXpowerInteger=_FsFiberChannel3TXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,84),_FsFiberChannel3TXpowerInteger_Type())
fsFiberChannel3TXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel3TXpowerInteger.setStatus(_A)
_FsFiberChannel4TXpowerInteger_Type=Integer32
_FsFiberChannel4TXpowerInteger_Object=MibTableColumn
fsFiberChannel4TXpowerInteger=_FsFiberChannel4TXpowerInteger_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,1,1,85),_FsFiberChannel4TXpowerInteger_Type())
fsFiberChannel4TXpowerInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberChannel4TXpowerInteger.setStatus(_A)
_FsFiberVendorTable_Object=MibTable
fsFiberVendorTable=_FsFiberVendorTable_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2))
if mibBuilder.loadTexts:fsFiberVendorTable.setStatus(_A)
_FsFiberVendorEntry_Object=MibTableRow
fsFiberVendorEntry=_FsFiberVendorEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1))
fsFiberVendorEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:fsFiberVendorEntry.setStatus(_A)
_FsFiberVendorPortIndex_Type=IfIndex
_FsFiberVendorPortIndex_Object=MibTableColumn
fsFiberVendorPortIndex=_FsFiberVendorPortIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1,1),_FsFiberVendorPortIndex_Type())
fsFiberVendorPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVendorPortIndex.setStatus(_A)
_FsFiberVendorName_Type=DisplayString
_FsFiberVendorName_Object=MibTableColumn
fsFiberVendorName=_FsFiberVendorName_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1,2),_FsFiberVendorName_Type())
fsFiberVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVendorName.setStatus(_A)
_FsFiberVendorOUI_Type=DisplayString
_FsFiberVendorOUI_Object=MibTableColumn
fsFiberVendorOUI=_FsFiberVendorOUI_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1,3),_FsFiberVendorOUI_Type())
fsFiberVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVendorOUI.setStatus(_A)
_FsFiberVendorPN_Type=DisplayString
_FsFiberVendorPN_Object=MibTableColumn
fsFiberVendorPN=_FsFiberVendorPN_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1,4),_FsFiberVendorPN_Type())
fsFiberVendorPN.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVendorPN.setStatus(_A)
_FsFiberVendorRev_Type=DisplayString
_FsFiberVendorRev_Object=MibTableColumn
fsFiberVendorRev=_FsFiberVendorRev_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1,5),_FsFiberVendorRev_Type())
fsFiberVendorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVendorRev.setStatus(_A)
_FsFiberVendorDate_Type=DisplayString
_FsFiberVendorDate_Object=MibTableColumn
fsFiberVendorDate=_FsFiberVendorDate_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1,6),_FsFiberVendorDate_Type())
fsFiberVendorDate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVendorDate.setStatus(_A)
_FsFiberVendorEncoding_Type=DisplayString
_FsFiberVendorEncoding_Object=MibTableColumn
fsFiberVendorEncoding=_FsFiberVendorEncoding_Object((1,3,6,1,4,1,52642,1,1,10,2,105,1,2,1,7),_FsFiberVendorEncoding_Type())
fsFiberVendorEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFiberVendorEncoding.setStatus(_A)
_FsFiberAntifakeMIBTraps_ObjectIdentity=ObjectIdentity
fsFiberAntifakeMIBTraps=_FsFiberAntifakeMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,105,2))
class _FsFiberAntifakeIntfNameDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsFiberAntifakeIntfNameDesc_Type.__name__=_I
_FsFiberAntifakeIntfNameDesc_Object=MibScalar
fsFiberAntifakeIntfNameDesc=_FsFiberAntifakeIntfNameDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,105,2,1),_FsFiberAntifakeIntfNameDesc_Type())
fsFiberAntifakeIntfNameDesc.setMaxAccess(_P)
if mibBuilder.loadTexts:fsFiberAntifakeIntfNameDesc.setStatus(_A)
class _FsFiberAntifakeSerialNumberDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsFiberAntifakeSerialNumberDesc_Type.__name__=_I
_FsFiberAntifakeSerialNumberDesc_Object=MibScalar
fsFiberAntifakeSerialNumberDesc=_FsFiberAntifakeSerialNumberDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,105,2,2),_FsFiberAntifakeSerialNumberDesc_Type())
fsFiberAntifakeSerialNumberDesc.setMaxAccess(_P)
if mibBuilder.loadTexts:fsFiberAntifakeSerialNumberDesc.setStatus(_A)
_FsFiberMIBConformance_ObjectIdentity=ObjectIdentity
fsFiberMIBConformance=_FsFiberMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,105,3))
_FsFiberMIBCompliances_ObjectIdentity=ObjectIdentity
fsFiberMIBCompliances=_FsFiberMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,105,3,1))
_FsFiberMIBGroups_ObjectIdentity=ObjectIdentity
fsFiberMIBGroups=_FsFiberMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,105,3,2))
fsFiberMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,105,3,2,1))
fsFiberMIBGroup.setObjects(*((_C,_Q),(_C,_R),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_g),(_C,_h),(_C,_i),(_C,_j),(_C,_k),(_C,_l),(_C,_m),(_C,_n),(_C,_o),(_C,_p),(_C,_q),(_C,_r),(_C,_s),(_C,_t),(_C,_u),(_C,_v),(_C,_w),(_C,_x),(_C,_y),(_C,_z),(_C,_A0),(_C,_A1),(_C,_A2),(_C,_A3),(_C,_A4),(_C,_A5),(_C,_A6),(_C,_A7),(_C,_A8),(_C,_A9),(_C,_AA),(_C,_AB),(_C,_AC),(_C,_AD),(_C,_AE),(_C,_AF),(_C,_AG),(_C,_AH),(_C,_AI),(_C,_AJ),(_C,_AK),(_C,_AL),(_C,_AM),(_C,_AN),(_C,_AO),(_C,_AP),(_C,_AQ),(_C,_AR),(_C,_AS),(_C,_AT),(_C,_AU),(_C,_AV),(_C,_AW),(_C,_AX),(_C,_AY),(_C,_AZ),(_C,_Aa),(_C,_Ab)))
if mibBuilder.loadTexts:fsFiberMIBGroup.setStatus(_A)
fsFiberAntifakeIntfNameDescGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,105,3,2,2))
fsFiberAntifakeIntfNameDescGroup.setObjects((_C,_L))
if mibBuilder.loadTexts:fsFiberAntifakeIntfNameDescGroup.setStatus(_A)
fsFiberAntifakeSerialNumberDescGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,105,3,2,3))
fsFiberAntifakeSerialNumberDescGroup.setObjects((_C,_M))
if mibBuilder.loadTexts:fsFiberAntifakeSerialNumberDescGroup.setStatus(_A)
fsFiberAntifakeTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,105,2,3))
fsFiberAntifakeTrap.setObjects(*((_C,_L),(_C,_M)))
if mibBuilder.loadTexts:fsFiberAntifakeTrap.setStatus(_A)
fsFiberMIBConpliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,105,3,1,1))
fsFiberMIBConpliance.setObjects(*((_C,_Ac),(_C,_Ad),(_C,_Ae)))
if mibBuilder.loadTexts:fsFiberMIBConpliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsFiberMIB':fsFiberMIB,'fsFiberMIBObjects':fsFiberMIBObjects,'fsFiberTable':fsFiberTable,'fsFiberEntry':fsFiberEntry,_N:fsFiberPortIndex,_Q:fsFiberPortDescr,_R:fsFiberTransceiverType,_S:fsFiberConnectorType,_T:fsFiberWavelength,_U:fsFiberTransferDistanceSMF,_V:fsFiberTransferDistance62point5umOM1,_W:fsFiberTransferDistance62point5um,_X:fsFiberTransferDistance50umOM2,_Y:fsFiberTransferDistance50um,_Z:fsFiberTransferDistance50umOM3,_a:fsFiberTransferDistanceEBW50um,_b:fsFiberTransferDistanceCopper,_c:fsFiberTransferDistanceCableAssembly,_d:fsFiberDDMSupportStatus,_e:fsFiberSerialNumber,_f:fsFiberTemp,_g:fsFiberTempStatus,_h:fsFiberVoltage,_i:fsFiberVoltageStatus,_j:fsFiberBias,_k:fsFiberBiasStatus,_l:fsFiberChannel1Bias,_m:fsFiberChannel1BiasStatus,_n:fsFiberChannel2Bias,_o:fsFiberChannel2BiasStatus,_p:fsFiberChannel3Bias,_q:fsFiberChannel3BiasStatus,_r:fsFiberChannel4Bias,_s:fsFiberChannel4BiasStatus,_t:fsFiberRXpowerIntegerpart,_u:fsFiberRXpowerDecimalpart,_v:fsFiberRXpowertype,_w:fsFiberRXpowerStatus,_x:fsFiberChannel1RXpowerIntegerpart,_y:fsFiberChannel1RXpowerDecimalpart,_z:fsFiberChannel1RXpowertype,_A0:fsFiberChannel1RXpowerStatus,_A1:fsFiberChannel2RXpowerIntegerpart,_A2:fsFiberChannel2RXpowerDecimalpart,_A3:fsFiberChannel2RXpowertype,_A4:fsFiberChannel2RXpowerStatus,_A5:fsFiberChannel3RXpowerIntegerpart,_A6:fsFiberChannel3RXpowerDecimalpart,_A7:fsFiberChannel3RXpowertype,_A8:fsFiberChannel3RXpowerStatus,_A9:fsFiberChannel4RXpowerIntegerpart,_AA:fsFiberChannel4RXpowerDecimalpart,_AB:fsFiberChannel4RXpowertype,_AC:fsFiberChannel4RXpowerStatus,_AD:fsFiberTXpowerIntegerpart,_AE:fsFiberTXpowerDecimalpart,_AF:fsFiberTXpowerStatus,_AG:fsFiberChannel1TXpowerIntegerpart,_AH:fsFiberChannel1TXpowerDecimalpart,_AI:fsFiberChannel1TXpowerStatus,_AJ:fsFiberChannel2TXpowerIntegerpart,_AK:fsFiberChannel2TXpowerDecimalpart,_AL:fsFiberChannel2TXpowerStatus,_AM:fsFiberChannel3TXpowerIntegerpart,_AN:fsFiberChannel3TXpowerDecimalpart,_AO:fsFiberChannel3TXpowerStatus,_AP:fsFiberChannel4TXpowerIntegerpart,_AQ:fsFiberChannel4TXpowerDecimalpart,_AR:fsFiberChannel4TXpowerStatus,_AS:fsFiberRXpowerSign,_AT:fsFiberChannel1RXpowerSign,_AU:fsFiberChannel2RXpowerSign,_AV:fsFiberChannel3RXpowerSign,_AW:fsFiberChannel4RXpowerSign,_AX:fsFiberTXpowerSign,_AY:fsFiberChannel1TXpowerSign,_AZ:fsFiberChannel2TXpowerSign,_Aa:fsFiberChannel3TXpowerSign,_Ab:fsFiberChannel4TXpowerSign,'fsFiberRXpowerInteger':fsFiberRXpowerInteger,'fsFiberChannel1RXpowerInteger':fsFiberChannel1RXpowerInteger,'fsFiberChannel2RXpowerInteger':fsFiberChannel2RXpowerInteger,'fsFiberChannel3RXpowerInteger':fsFiberChannel3RXpowerInteger,'fsFiberChannel4RXpowerInteger':fsFiberChannel4RXpowerInteger,'fsFiberTXpowerInteger':fsFiberTXpowerInteger,'fsFiberChannel1TXpowerInteger':fsFiberChannel1TXpowerInteger,'fsFiberChannel2TXpowerInteger':fsFiberChannel2TXpowerInteger,'fsFiberChannel3TXpowerInteger':fsFiberChannel3TXpowerInteger,'fsFiberChannel4TXpowerInteger':fsFiberChannel4TXpowerInteger,'fsFiberVendorTable':fsFiberVendorTable,'fsFiberVendorEntry':fsFiberVendorEntry,_O:fsFiberVendorPortIndex,'fsFiberVendorName':fsFiberVendorName,'fsFiberVendorOUI':fsFiberVendorOUI,'fsFiberVendorPN':fsFiberVendorPN,'fsFiberVendorRev':fsFiberVendorRev,'fsFiberVendorDate':fsFiberVendorDate,'fsFiberVendorEncoding':fsFiberVendorEncoding,'fsFiberAntifakeMIBTraps':fsFiberAntifakeMIBTraps,_L:fsFiberAntifakeIntfNameDesc,_M:fsFiberAntifakeSerialNumberDesc,'fsFiberAntifakeTrap':fsFiberAntifakeTrap,'fsFiberMIBConformance':fsFiberMIBConformance,'fsFiberMIBCompliances':fsFiberMIBCompliances,'fsFiberMIBConpliance':fsFiberMIBConpliance,'fsFiberMIBGroups':fsFiberMIBGroups,_Ac:fsFiberMIBGroup,_Ad:fsFiberAntifakeIntfNameDescGroup,_Ae:fsFiberAntifakeSerialNumberDescGroup})