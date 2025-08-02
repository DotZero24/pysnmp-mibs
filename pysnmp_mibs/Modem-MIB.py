_AM='mdmDataCompressionGroup'
_AL='mdmErrorControlGroup'
_AK='mdmStatisticsGroup'
_AJ='mdmSignalConvertorGroup'
_AI='mdmCallControlGroup'
_AH='mdmDTEInterfaceGroup'
_AG='mdmLineInterfaceGroup'
_AF='mdmIDGroup'
_AE='mdmStatsErrorFrames'
_AD='mdmStatsResentFrames'
_AC='mdmStatsReceivedDataFrames'
_AB='mdmStatsSentDataFrames'
_AA='mdmStatsReceivedOctets'
_A9='mdmStatsSentOctets'
_A8='mdmStatsCompressionEfficiency'
_A7='mdmStatsCompressedConnections'
_A6='mdmStatsErrorControlledConnections'
_A5='mdmStatsGreaterThan14400Connections'
_A4='mdmStats2400To14400Connections'
_A3='mdmStats2400OrLessConnections'
_A2='mdmStatsRetrains'
_A1='mdmStatsOutgoingConnectionCompletions'
_A0='mdmStatsOutgoingConnectionFailures'
_z='mdmStatsFailedDialAttempts'
_y='mdmStatsIncomingConnectionCompletions'
_x='mdmStatsIncomingConnectionFailures'
_w='mdmStatsRingNoAnswers'
_v='mdmSCModulationSchemeUsed'
_u='mdmSCInitialLineTransmitRate'
_t='mdmSCInitialLineReceiveRate'
_s='mdmSCCurrentLineTransmitRate'
_r='mdmSCCurrentLineReceiveRate'
_q='mdmDCCompressionTypeUsed'
_p='mdmECErrorControlUsed'
_o='mdmCCStoredDialString'
_n='mdmCCConnectionFailReason'
_m='mdmCCCallDuration'
_l='mdmCCEscapeAction'
_k='mdmCCResultCodeEnable'
_j='mdmCCCallSetUpFailTimer'
_i='mdmCCRingsBeforeAnswer'
_h='mdmDTEInactivityTimeout'
_g='mdmDTESyncAsyncMode'
_f='mdmDTESyncTimingSource'
_e='mdmDTEActionDTROffToOn'
_d='mdmDTEActionDTROnToOff'
_c='mdmLineCapabilitiesEnableGranted'
_b='mdmLineCapabilitiesEnableRequested'
_a='mdmLineCapabilitiesID'
_Z='mdmLineState'
_Y='mdmLineCarrierLossTime'
_X='mdmIDProductDetails'
_W='mdmIDManufacturerOID'
_V='mdmStatsEntry'
_U='mdmSCEntry'
_T='mdmDCEntry'
_S='mdmECEntry'
_R='mdmCallControlEntry'
_Q='mdmDTEInterfaceEntry'
_P='mdmLineEntry'
_O='mdmCCStoredDialStringIndex'
_N='ignore'
_M='preferred'
_L='optional'
_K='mdmLineCapabilitiesIndex'
_J='unknown'
_I='disabled'
_H='not-accessible'
_G='DisplayString'
_F='mdmIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='Modem-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
mdmMIB=ModuleIdentity((1,3,6,1,2,1,38,1))
_MdmMib_ObjectIdentity=ObjectIdentity
mdmMib=_MdmMib_ObjectIdentity((1,3,6,1,2,1,38))
_MdmMIBObjects_ObjectIdentity=ObjectIdentity
mdmMIBObjects=_MdmMIBObjects_ObjectIdentity((1,3,6,1,2,1,38,1,1))
_MdmNumber_Type=Integer32
_MdmNumber_Object=MibScalar
mdmNumber=_MdmNumber_Object((1,3,6,1,2,1,38,1,1,1),_MdmNumber_Type())
mdmNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmNumber.setStatus(_A)
_MdmIDTable_Object=MibTable
mdmIDTable=_MdmIDTable_Object((1,3,6,1,2,1,38,1,1,2))
if mibBuilder.loadTexts:mdmIDTable.setStatus(_A)
_MdmIDEntry_Object=MibTableRow
mdmIDEntry=_MdmIDEntry_Object((1,3,6,1,2,1,38,1,1,2,1))
mdmIDEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:mdmIDEntry.setStatus(_A)
class _MdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MdmIndex_Type.__name__=_D
_MdmIndex_Object=MibTableColumn
mdmIndex=_MdmIndex_Object((1,3,6,1,2,1,38,1,1,2,1,1),_MdmIndex_Type())
mdmIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mdmIndex.setStatus(_A)
_MdmIDManufacturerOID_Type=ObjectIdentifier
_MdmIDManufacturerOID_Object=MibTableColumn
mdmIDManufacturerOID=_MdmIDManufacturerOID_Object((1,3,6,1,2,1,38,1,1,2,1,2),_MdmIDManufacturerOID_Type())
mdmIDManufacturerOID.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmIDManufacturerOID.setStatus(_A)
class _MdmIDProductDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_MdmIDProductDetails_Type.__name__=_G
_MdmIDProductDetails_Object=MibTableColumn
mdmIDProductDetails=_MdmIDProductDetails_Object((1,3,6,1,2,1,38,1,1,2,1,3),_MdmIDProductDetails_Type())
mdmIDProductDetails.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmIDProductDetails.setStatus(_A)
_MdmLineTable_Object=MibTable
mdmLineTable=_MdmLineTable_Object((1,3,6,1,2,1,38,1,1,3))
if mibBuilder.loadTexts:mdmLineTable.setStatus(_A)
_MdmLineEntry_Object=MibTableRow
mdmLineEntry=_MdmLineEntry_Object((1,3,6,1,2,1,38,1,1,3,1))
if mibBuilder.loadTexts:mdmLineEntry.setStatus(_A)
class _MdmLineCarrierLossTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_MdmLineCarrierLossTime_Type.__name__=_D
_MdmLineCarrierLossTime_Object=MibTableColumn
mdmLineCarrierLossTime=_MdmLineCarrierLossTime_Object((1,3,6,1,2,1,38,1,1,3,1,1),_MdmLineCarrierLossTime_Type())
mdmLineCarrierLossTime.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmLineCarrierLossTime.setStatus(_A)
class _MdmLineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('onHook',2),('offHook',3),('connected',4),('busiedOut',5),('reset',6)))
_MdmLineState_Type.__name__=_D
_MdmLineState_Object=MibTableColumn
mdmLineState=_MdmLineState_Object((1,3,6,1,2,1,38,1,1,3,1,2),_MdmLineState_Type())
mdmLineState.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmLineState.setStatus(_A)
_MdmLineCapabilitiesTable_Object=MibTable
mdmLineCapabilitiesTable=_MdmLineCapabilitiesTable_Object((1,3,6,1,2,1,38,1,1,4))
if mibBuilder.loadTexts:mdmLineCapabilitiesTable.setStatus(_A)
_MdmLineCapabilitiesEntry_Object=MibTableRow
mdmLineCapabilitiesEntry=_MdmLineCapabilitiesEntry_Object((1,3,6,1,2,1,38,1,1,4,1))
mdmLineCapabilitiesEntry.setIndexNames((0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:mdmLineCapabilitiesEntry.setStatus(_A)
_MdmLineCapabilitiesIndex_Type=Integer32
_MdmLineCapabilitiesIndex_Object=MibTableColumn
mdmLineCapabilitiesIndex=_MdmLineCapabilitiesIndex_Object((1,3,6,1,2,1,38,1,1,4,1,1),_MdmLineCapabilitiesIndex_Type())
mdmLineCapabilitiesIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mdmLineCapabilitiesIndex.setStatus(_A)
_MdmLineCapabilitiesID_Type=ObjectIdentifier
_MdmLineCapabilitiesID_Object=MibTableColumn
mdmLineCapabilitiesID=_MdmLineCapabilitiesID_Object((1,3,6,1,2,1,38,1,1,4,1,2),_MdmLineCapabilitiesID_Type())
mdmLineCapabilitiesID.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmLineCapabilitiesID.setStatus(_A)
class _MdmLineCapabilitiesEnableRequested_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_L,2),(_M,3)))
_MdmLineCapabilitiesEnableRequested_Type.__name__=_D
_MdmLineCapabilitiesEnableRequested_Object=MibTableColumn
mdmLineCapabilitiesEnableRequested=_MdmLineCapabilitiesEnableRequested_Object((1,3,6,1,2,1,38,1,1,4,1,3),_MdmLineCapabilitiesEnableRequested_Type())
mdmLineCapabilitiesEnableRequested.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmLineCapabilitiesEnableRequested.setStatus(_A)
class _MdmLineCapabilitiesEnableGranted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_L,2),(_M,3)))
_MdmLineCapabilitiesEnableGranted_Type.__name__=_D
_MdmLineCapabilitiesEnableGranted_Object=MibTableColumn
mdmLineCapabilitiesEnableGranted=_MdmLineCapabilitiesEnableGranted_Object((1,3,6,1,2,1,38,1,1,4,1,4),_MdmLineCapabilitiesEnableGranted_Type())
mdmLineCapabilitiesEnableGranted.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmLineCapabilitiesEnableGranted.setStatus(_A)
_MdmLineCapabilities_ObjectIdentity=ObjectIdentity
mdmLineCapabilities=_MdmLineCapabilities_ObjectIdentity((1,3,6,1,2,1,38,1,1,5))
_MdmLineCapabilitiesV21_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV21=_MdmLineCapabilitiesV21_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,1))
if mibBuilder.loadTexts:mdmLineCapabilitiesV21.setStatus(_A)
_MdmLineCapabilitiesV22_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV22=_MdmLineCapabilitiesV22_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,2))
if mibBuilder.loadTexts:mdmLineCapabilitiesV22.setStatus(_A)
_MdmLineCapabilitiesV22bis_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV22bis=_MdmLineCapabilitiesV22bis_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,3))
if mibBuilder.loadTexts:mdmLineCapabilitiesV22bis.setStatus(_A)
_MdmLineCapabilitiesV23CC_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV23CC=_MdmLineCapabilitiesV23CC_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,4))
if mibBuilder.loadTexts:mdmLineCapabilitiesV23CC.setStatus(_A)
_MdmLineCapabilitiesV23SC_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV23SC=_MdmLineCapabilitiesV23SC_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,5))
if mibBuilder.loadTexts:mdmLineCapabilitiesV23SC.setStatus(_A)
_MdmLineCapabilitiesV25bis_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV25bis=_MdmLineCapabilitiesV25bis_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,6))
if mibBuilder.loadTexts:mdmLineCapabilitiesV25bis.setStatus(_A)
_MdmLineCapabilitiesV26bis_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV26bis=_MdmLineCapabilitiesV26bis_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,7))
if mibBuilder.loadTexts:mdmLineCapabilitiesV26bis.setStatus(_A)
_MdmLineCapabilitiesV26ter_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV26ter=_MdmLineCapabilitiesV26ter_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,8))
if mibBuilder.loadTexts:mdmLineCapabilitiesV26ter.setStatus(_A)
_MdmLineCapabilitiesV27ter_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV27ter=_MdmLineCapabilitiesV27ter_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,9))
if mibBuilder.loadTexts:mdmLineCapabilitiesV27ter.setStatus(_A)
_MdmLineCapabilitiesV32_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV32=_MdmLineCapabilitiesV32_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,10))
if mibBuilder.loadTexts:mdmLineCapabilitiesV32.setStatus(_A)
_MdmLineCapabilitiesV32bis_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV32bis=_MdmLineCapabilitiesV32bis_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,11))
if mibBuilder.loadTexts:mdmLineCapabilitiesV32bis.setStatus(_A)
_MdmLineCapabilitiesV32terbo_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV32terbo=_MdmLineCapabilitiesV32terbo_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,12))
if mibBuilder.loadTexts:mdmLineCapabilitiesV32terbo.setStatus(_A)
_MdmLineCapabilitiesVFC_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesVFC=_MdmLineCapabilitiesVFC_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,13))
if mibBuilder.loadTexts:mdmLineCapabilitiesVFC.setStatus(_A)
_MdmLineCapabilitiesV34_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV34=_MdmLineCapabilitiesV34_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,14))
if mibBuilder.loadTexts:mdmLineCapabilitiesV34.setStatus(_A)
_MdmLineCapabilitiesV42_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV42=_MdmLineCapabilitiesV42_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,15))
if mibBuilder.loadTexts:mdmLineCapabilitiesV42.setStatus(_A)
_MdmLineCapabilitiesV42bis_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV42bis=_MdmLineCapabilitiesV42bis_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,16))
if mibBuilder.loadTexts:mdmLineCapabilitiesV42bis.setStatus(_A)
_MdmLineCapabilitiesMNP1_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP1=_MdmLineCapabilitiesMNP1_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,17))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP1.setStatus(_A)
_MdmLineCapabilitiesMNP2_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP2=_MdmLineCapabilitiesMNP2_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,18))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP2.setStatus(_A)
_MdmLineCapabilitiesMNP3_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP3=_MdmLineCapabilitiesMNP3_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,19))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP3.setStatus(_A)
_MdmLineCapabilitiesMNP4_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP4=_MdmLineCapabilitiesMNP4_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,20))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP4.setStatus(_A)
_MdmLineCapabilitiesMNP5_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP5=_MdmLineCapabilitiesMNP5_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,21))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP5.setStatus(_A)
_MdmLineCapabilitiesMNP6_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP6=_MdmLineCapabilitiesMNP6_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,22))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP6.setStatus(_A)
_MdmLineCapabilitiesMNP7_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP7=_MdmLineCapabilitiesMNP7_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,23))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP7.setStatus(_A)
_MdmLineCapabilitiesMNP8_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP8=_MdmLineCapabilitiesMNP8_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,24))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP8.setStatus(_A)
_MdmLineCapabilitiesMNP9_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP9=_MdmLineCapabilitiesMNP9_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,25))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP9.setStatus(_A)
_MdmLineCapabilitiesMNP10_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesMNP10=_MdmLineCapabilitiesMNP10_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,26))
if mibBuilder.loadTexts:mdmLineCapabilitiesMNP10.setStatus(_A)
_MdmLineCapabilitiesV29_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV29=_MdmLineCapabilitiesV29_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,27))
if mibBuilder.loadTexts:mdmLineCapabilitiesV29.setStatus(_A)
_MdmLineCapabilitiesV33_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesV33=_MdmLineCapabilitiesV33_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,28))
if mibBuilder.loadTexts:mdmLineCapabilitiesV33.setStatus(_A)
_MdmLineCapabilitiesBell208_ObjectIdentity=ObjectIdentity
mdmLineCapabilitiesBell208=_MdmLineCapabilitiesBell208_ObjectIdentity((1,3,6,1,2,1,38,1,1,5,29))
if mibBuilder.loadTexts:mdmLineCapabilitiesBell208.setStatus(_A)
_MdmDTEInterfaceTable_Object=MibTable
mdmDTEInterfaceTable=_MdmDTEInterfaceTable_Object((1,3,6,1,2,1,38,1,1,6))
if mibBuilder.loadTexts:mdmDTEInterfaceTable.setStatus(_A)
_MdmDTEInterfaceEntry_Object=MibTableRow
mdmDTEInterfaceEntry=_MdmDTEInterfaceEntry_Object((1,3,6,1,2,1,38,1,1,6,1))
if mibBuilder.loadTexts:mdmDTEInterfaceEntry.setStatus(_A)
class _MdmDTEActionDTROnToOff_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('escapeToCommandMode',2),('disconnectCall',3),('resetModem',4)))
_MdmDTEActionDTROnToOff_Type.__name__=_D
_MdmDTEActionDTROnToOff_Object=MibTableColumn
mdmDTEActionDTROnToOff=_MdmDTEActionDTROnToOff_Object((1,3,6,1,2,1,38,1,1,6,1,1),_MdmDTEActionDTROnToOff_Type())
mdmDTEActionDTROnToOff.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmDTEActionDTROnToOff.setStatus(_A)
class _MdmDTEActionDTROffToOn_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('enableDial',2),('autoAnswerEnable',3),('establishConnection',4)))
_MdmDTEActionDTROffToOn_Type.__name__=_D
_MdmDTEActionDTROffToOn_Object=MibTableColumn
mdmDTEActionDTROffToOn=_MdmDTEActionDTROffToOn_Object((1,3,6,1,2,1,38,1,1,6,1,2),_MdmDTEActionDTROffToOn_Type())
mdmDTEActionDTROffToOn.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmDTEActionDTROffToOn.setStatus(_A)
class _MdmDTESyncTimingSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('internal',1),('external',2),('loopback',3),('network',4)))
_MdmDTESyncTimingSource_Type.__name__=_D
_MdmDTESyncTimingSource_Object=MibTableColumn
mdmDTESyncTimingSource=_MdmDTESyncTimingSource_Object((1,3,6,1,2,1,38,1,1,6,1,3),_MdmDTESyncTimingSource_Type())
mdmDTESyncTimingSource.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmDTESyncTimingSource.setStatus(_A)
class _MdmDTESyncAsyncMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('async',1),('sync',2),('syncAfterDial',3)))
_MdmDTESyncAsyncMode_Type.__name__=_D
_MdmDTESyncAsyncMode_Object=MibTableColumn
mdmDTESyncAsyncMode=_MdmDTESyncAsyncMode_Object((1,3,6,1,2,1,38,1,1,6,1,4),_MdmDTESyncAsyncMode_Type())
mdmDTESyncAsyncMode.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmDTESyncAsyncMode.setStatus(_A)
class _MdmDTEInactivityTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MdmDTEInactivityTimeout_Type.__name__=_D
_MdmDTEInactivityTimeout_Object=MibTableColumn
mdmDTEInactivityTimeout=_MdmDTEInactivityTimeout_Object((1,3,6,1,2,1,38,1,1,6,1,5),_MdmDTEInactivityTimeout_Type())
mdmDTEInactivityTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmDTEInactivityTimeout.setStatus(_A)
_MdmCallControlTable_Object=MibTable
mdmCallControlTable=_MdmCallControlTable_Object((1,3,6,1,2,1,38,1,1,7))
if mibBuilder.loadTexts:mdmCallControlTable.setStatus(_A)
_MdmCallControlEntry_Object=MibTableRow
mdmCallControlEntry=_MdmCallControlEntry_Object((1,3,6,1,2,1,38,1,1,7,1))
if mibBuilder.loadTexts:mdmCallControlEntry.setStatus(_A)
class _MdmCCRingsBeforeAnswer_Type(Integer32):defaultValue=1
_MdmCCRingsBeforeAnswer_Type.__name__=_D
_MdmCCRingsBeforeAnswer_Object=MibTableColumn
mdmCCRingsBeforeAnswer=_MdmCCRingsBeforeAnswer_Object((1,3,6,1,2,1,38,1,1,7,1,1),_MdmCCRingsBeforeAnswer_Type())
mdmCCRingsBeforeAnswer.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmCCRingsBeforeAnswer.setStatus(_A)
class _MdmCCCallSetUpFailTimer_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MdmCCCallSetUpFailTimer_Type.__name__=_D
_MdmCCCallSetUpFailTimer_Object=MibTableColumn
mdmCCCallSetUpFailTimer=_MdmCCCallSetUpFailTimer_Object((1,3,6,1,2,1,38,1,1,7,1,2),_MdmCCCallSetUpFailTimer_Type())
mdmCCCallSetUpFailTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmCCCallSetUpFailTimer.setStatus(_A)
class _MdmCCResultCodeEnable_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('numericEnabled',2),('verboseEnabled',3)))
_MdmCCResultCodeEnable_Type.__name__=_D
_MdmCCResultCodeEnable_Object=MibTableColumn
mdmCCResultCodeEnable=_MdmCCResultCodeEnable_Object((1,3,6,1,2,1,38,1,1,7,1,3),_MdmCCResultCodeEnable_Type())
mdmCCResultCodeEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmCCResultCodeEnable.setStatus(_A)
class _MdmCCEscapeAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ignoreEscape',1),('hangUp',2),('enterCommandMode',3)))
_MdmCCEscapeAction_Type.__name__=_D
_MdmCCEscapeAction_Object=MibTableColumn
mdmCCEscapeAction=_MdmCCEscapeAction_Object((1,3,6,1,2,1,38,1,1,7,1,4),_MdmCCEscapeAction_Type())
mdmCCEscapeAction.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmCCEscapeAction.setStatus(_A)
_MdmCCCallDuration_Type=Integer32
_MdmCCCallDuration_Object=MibTableColumn
mdmCCCallDuration=_MdmCCCallDuration_Object((1,3,6,1,2,1,38,1,1,7,1,5),_MdmCCCallDuration_Type())
mdmCCCallDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmCCCallDuration.setStatus(_A)
class _MdmCCConnectionFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,10,11,20,30,31,32,33,40,41,42)));namedValues=NamedValues(*((_J,1),('other',2),('managementCommand',3),('inactivityTimeout',4),('mnpIncompatibility',5),('protocolError',6),('powerLoss',10),('equipmentFailure',11),('dtrDrop',20),('noDialTone',30),('lineBusy',31),('noAnswer',32),('voiceDetected',33),('carrierLost',40),('trainingFailed',41),('faxDetected',42)))
_MdmCCConnectionFailReason_Type.__name__=_D
_MdmCCConnectionFailReason_Object=MibTableColumn
mdmCCConnectionFailReason=_MdmCCConnectionFailReason_Object((1,3,6,1,2,1,38,1,1,7,1,6),_MdmCCConnectionFailReason_Type())
mdmCCConnectionFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmCCConnectionFailReason.setStatus(_A)
_MdmCCStoredDialStringTable_Object=MibTable
mdmCCStoredDialStringTable=_MdmCCStoredDialStringTable_Object((1,3,6,1,2,1,38,1,1,8))
if mibBuilder.loadTexts:mdmCCStoredDialStringTable.setStatus(_A)
_MdmCCStoredDialStringEntry_Object=MibTableRow
mdmCCStoredDialStringEntry=_MdmCCStoredDialStringEntry_Object((1,3,6,1,2,1,38,1,1,8,1))
mdmCCStoredDialStringEntry.setIndexNames((0,_B,_F),(0,_B,_O))
if mibBuilder.loadTexts:mdmCCStoredDialStringEntry.setStatus(_A)
class _MdmCCStoredDialStringIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MdmCCStoredDialStringIndex_Type.__name__=_D
_MdmCCStoredDialStringIndex_Object=MibTableColumn
mdmCCStoredDialStringIndex=_MdmCCStoredDialStringIndex_Object((1,3,6,1,2,1,38,1,1,8,1,1),_MdmCCStoredDialStringIndex_Type())
mdmCCStoredDialStringIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mdmCCStoredDialStringIndex.setStatus(_A)
class _MdmCCStoredDialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MdmCCStoredDialString_Type.__name__=_G
_MdmCCStoredDialString_Object=MibTableColumn
mdmCCStoredDialString=_MdmCCStoredDialString_Object((1,3,6,1,2,1,38,1,1,8,1,2),_MdmCCStoredDialString_Type())
mdmCCStoredDialString.setMaxAccess(_E)
if mibBuilder.loadTexts:mdmCCStoredDialString.setStatus(_A)
_MdmECTable_Object=MibTable
mdmECTable=_MdmECTable_Object((1,3,6,1,2,1,38,1,1,9))
if mibBuilder.loadTexts:mdmECTable.setStatus(_A)
_MdmECEntry_Object=MibTableRow
mdmECEntry=_MdmECEntry_Object((1,3,6,1,2,1,38,1,1,9,1))
if mibBuilder.loadTexts:mdmECEntry.setStatus(_A)
_MdmECErrorControlUsed_Type=ObjectIdentifier
_MdmECErrorControlUsed_Object=MibTableColumn
mdmECErrorControlUsed=_MdmECErrorControlUsed_Object((1,3,6,1,2,1,38,1,1,9,1,1),_MdmECErrorControlUsed_Type())
mdmECErrorControlUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmECErrorControlUsed.setStatus(_A)
_MdmDCTable_Object=MibTable
mdmDCTable=_MdmDCTable_Object((1,3,6,1,2,1,38,1,1,10))
if mibBuilder.loadTexts:mdmDCTable.setStatus(_A)
_MdmDCEntry_Object=MibTableRow
mdmDCEntry=_MdmDCEntry_Object((1,3,6,1,2,1,38,1,1,10,1))
if mibBuilder.loadTexts:mdmDCEntry.setStatus(_A)
_MdmDCCompressionTypeUsed_Type=ObjectIdentifier
_MdmDCCompressionTypeUsed_Object=MibTableColumn
mdmDCCompressionTypeUsed=_MdmDCCompressionTypeUsed_Object((1,3,6,1,2,1,38,1,1,10,1,1),_MdmDCCompressionTypeUsed_Type())
mdmDCCompressionTypeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmDCCompressionTypeUsed.setStatus(_A)
_MdmSCTable_Object=MibTable
mdmSCTable=_MdmSCTable_Object((1,3,6,1,2,1,38,1,1,11))
if mibBuilder.loadTexts:mdmSCTable.setStatus(_A)
_MdmSCEntry_Object=MibTableRow
mdmSCEntry=_MdmSCEntry_Object((1,3,6,1,2,1,38,1,1,11,1))
if mibBuilder.loadTexts:mdmSCEntry.setStatus(_A)
_MdmSCCurrentLineTransmitRate_Type=Integer32
_MdmSCCurrentLineTransmitRate_Object=MibTableColumn
mdmSCCurrentLineTransmitRate=_MdmSCCurrentLineTransmitRate_Object((1,3,6,1,2,1,38,1,1,11,1,1),_MdmSCCurrentLineTransmitRate_Type())
mdmSCCurrentLineTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmSCCurrentLineTransmitRate.setStatus(_A)
_MdmSCCurrentLineReceiveRate_Type=Integer32
_MdmSCCurrentLineReceiveRate_Object=MibTableColumn
mdmSCCurrentLineReceiveRate=_MdmSCCurrentLineReceiveRate_Object((1,3,6,1,2,1,38,1,1,11,1,2),_MdmSCCurrentLineReceiveRate_Type())
mdmSCCurrentLineReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmSCCurrentLineReceiveRate.setStatus(_A)
_MdmSCInitialLineTransmitRate_Type=Integer32
_MdmSCInitialLineTransmitRate_Object=MibTableColumn
mdmSCInitialLineTransmitRate=_MdmSCInitialLineTransmitRate_Object((1,3,6,1,2,1,38,1,1,11,1,3),_MdmSCInitialLineTransmitRate_Type())
mdmSCInitialLineTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmSCInitialLineTransmitRate.setStatus(_A)
_MdmSCInitialLineReceiveRate_Type=Integer32
_MdmSCInitialLineReceiveRate_Object=MibTableColumn
mdmSCInitialLineReceiveRate=_MdmSCInitialLineReceiveRate_Object((1,3,6,1,2,1,38,1,1,11,1,4),_MdmSCInitialLineReceiveRate_Type())
mdmSCInitialLineReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmSCInitialLineReceiveRate.setStatus(_A)
_MdmSCModulationSchemeUsed_Type=ObjectIdentifier
_MdmSCModulationSchemeUsed_Object=MibTableColumn
mdmSCModulationSchemeUsed=_MdmSCModulationSchemeUsed_Object((1,3,6,1,2,1,38,1,1,11,1,5),_MdmSCModulationSchemeUsed_Type())
mdmSCModulationSchemeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmSCModulationSchemeUsed.setStatus(_A)
_MdmStatsTable_Object=MibTable
mdmStatsTable=_MdmStatsTable_Object((1,3,6,1,2,1,38,1,1,12))
if mibBuilder.loadTexts:mdmStatsTable.setStatus(_A)
_MdmStatsEntry_Object=MibTableRow
mdmStatsEntry=_MdmStatsEntry_Object((1,3,6,1,2,1,38,1,1,12,1))
if mibBuilder.loadTexts:mdmStatsEntry.setStatus(_A)
_MdmStatsRingNoAnswers_Type=Counter32
_MdmStatsRingNoAnswers_Object=MibTableColumn
mdmStatsRingNoAnswers=_MdmStatsRingNoAnswers_Object((1,3,6,1,2,1,38,1,1,12,1,1),_MdmStatsRingNoAnswers_Type())
mdmStatsRingNoAnswers.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsRingNoAnswers.setStatus(_A)
_MdmStatsIncomingConnectionFailures_Type=Counter32
_MdmStatsIncomingConnectionFailures_Object=MibTableColumn
mdmStatsIncomingConnectionFailures=_MdmStatsIncomingConnectionFailures_Object((1,3,6,1,2,1,38,1,1,12,1,2),_MdmStatsIncomingConnectionFailures_Type())
mdmStatsIncomingConnectionFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsIncomingConnectionFailures.setStatus(_A)
_MdmStatsIncomingConnectionCompletions_Type=Counter32
_MdmStatsIncomingConnectionCompletions_Object=MibTableColumn
mdmStatsIncomingConnectionCompletions=_MdmStatsIncomingConnectionCompletions_Object((1,3,6,1,2,1,38,1,1,12,1,3),_MdmStatsIncomingConnectionCompletions_Type())
mdmStatsIncomingConnectionCompletions.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsIncomingConnectionCompletions.setStatus(_A)
_MdmStatsFailedDialAttempts_Type=Counter32
_MdmStatsFailedDialAttempts_Object=MibTableColumn
mdmStatsFailedDialAttempts=_MdmStatsFailedDialAttempts_Object((1,3,6,1,2,1,38,1,1,12,1,4),_MdmStatsFailedDialAttempts_Type())
mdmStatsFailedDialAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsFailedDialAttempts.setStatus(_A)
_MdmStatsOutgoingConnectionFailures_Type=Counter32
_MdmStatsOutgoingConnectionFailures_Object=MibTableColumn
mdmStatsOutgoingConnectionFailures=_MdmStatsOutgoingConnectionFailures_Object((1,3,6,1,2,1,38,1,1,12,1,5),_MdmStatsOutgoingConnectionFailures_Type())
mdmStatsOutgoingConnectionFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsOutgoingConnectionFailures.setStatus(_A)
_MdmStatsOutgoingConnectionCompletions_Type=Counter32
_MdmStatsOutgoingConnectionCompletions_Object=MibTableColumn
mdmStatsOutgoingConnectionCompletions=_MdmStatsOutgoingConnectionCompletions_Object((1,3,6,1,2,1,38,1,1,12,1,6),_MdmStatsOutgoingConnectionCompletions_Type())
mdmStatsOutgoingConnectionCompletions.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsOutgoingConnectionCompletions.setStatus(_A)
_MdmStatsRetrains_Type=Counter32
_MdmStatsRetrains_Object=MibTableColumn
mdmStatsRetrains=_MdmStatsRetrains_Object((1,3,6,1,2,1,38,1,1,12,1,7),_MdmStatsRetrains_Type())
mdmStatsRetrains.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsRetrains.setStatus(_A)
_MdmStats2400OrLessConnections_Type=Counter32
_MdmStats2400OrLessConnections_Object=MibTableColumn
mdmStats2400OrLessConnections=_MdmStats2400OrLessConnections_Object((1,3,6,1,2,1,38,1,1,12,1,8),_MdmStats2400OrLessConnections_Type())
mdmStats2400OrLessConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStats2400OrLessConnections.setStatus(_A)
_MdmStats2400To14400Connections_Type=Counter32
_MdmStats2400To14400Connections_Object=MibTableColumn
mdmStats2400To14400Connections=_MdmStats2400To14400Connections_Object((1,3,6,1,2,1,38,1,1,12,1,9),_MdmStats2400To14400Connections_Type())
mdmStats2400To14400Connections.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStats2400To14400Connections.setStatus(_A)
_MdmStatsGreaterThan14400Connections_Type=Counter32
_MdmStatsGreaterThan14400Connections_Object=MibTableColumn
mdmStatsGreaterThan14400Connections=_MdmStatsGreaterThan14400Connections_Object((1,3,6,1,2,1,38,1,1,12,1,10),_MdmStatsGreaterThan14400Connections_Type())
mdmStatsGreaterThan14400Connections.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsGreaterThan14400Connections.setStatus(_A)
_MdmStatsErrorControlledConnections_Type=Counter32
_MdmStatsErrorControlledConnections_Object=MibTableColumn
mdmStatsErrorControlledConnections=_MdmStatsErrorControlledConnections_Object((1,3,6,1,2,1,38,1,1,12,1,11),_MdmStatsErrorControlledConnections_Type())
mdmStatsErrorControlledConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsErrorControlledConnections.setStatus(_A)
_MdmStatsCompressedConnections_Type=Counter32
_MdmStatsCompressedConnections_Object=MibTableColumn
mdmStatsCompressedConnections=_MdmStatsCompressedConnections_Object((1,3,6,1,2,1,38,1,1,12,1,12),_MdmStatsCompressedConnections_Type())
mdmStatsCompressedConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsCompressedConnections.setStatus(_A)
class _MdmStatsCompressionEfficiency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MdmStatsCompressionEfficiency_Type.__name__=_D
_MdmStatsCompressionEfficiency_Object=MibTableColumn
mdmStatsCompressionEfficiency=_MdmStatsCompressionEfficiency_Object((1,3,6,1,2,1,38,1,1,12,1,13),_MdmStatsCompressionEfficiency_Type())
mdmStatsCompressionEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsCompressionEfficiency.setStatus(_A)
_MdmStatsSentOctets_Type=Counter32
_MdmStatsSentOctets_Object=MibTableColumn
mdmStatsSentOctets=_MdmStatsSentOctets_Object((1,3,6,1,2,1,38,1,1,12,1,14),_MdmStatsSentOctets_Type())
mdmStatsSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsSentOctets.setStatus(_A)
_MdmStatsReceivedOctets_Type=Counter32
_MdmStatsReceivedOctets_Object=MibTableColumn
mdmStatsReceivedOctets=_MdmStatsReceivedOctets_Object((1,3,6,1,2,1,38,1,1,12,1,15),_MdmStatsReceivedOctets_Type())
mdmStatsReceivedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsReceivedOctets.setStatus(_A)
_MdmStatsSentDataFrames_Type=Counter32
_MdmStatsSentDataFrames_Object=MibTableColumn
mdmStatsSentDataFrames=_MdmStatsSentDataFrames_Object((1,3,6,1,2,1,38,1,1,12,1,16),_MdmStatsSentDataFrames_Type())
mdmStatsSentDataFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsSentDataFrames.setStatus(_A)
_MdmStatsReceivedDataFrames_Type=Counter32
_MdmStatsReceivedDataFrames_Object=MibTableColumn
mdmStatsReceivedDataFrames=_MdmStatsReceivedDataFrames_Object((1,3,6,1,2,1,38,1,1,12,1,17),_MdmStatsReceivedDataFrames_Type())
mdmStatsReceivedDataFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsReceivedDataFrames.setStatus(_A)
_MdmStatsResentFrames_Type=Counter32
_MdmStatsResentFrames_Object=MibTableColumn
mdmStatsResentFrames=_MdmStatsResentFrames_Object((1,3,6,1,2,1,38,1,1,12,1,18),_MdmStatsResentFrames_Type())
mdmStatsResentFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsResentFrames.setStatus(_A)
_MdmStatsErrorFrames_Type=Counter32
_MdmStatsErrorFrames_Object=MibTableColumn
mdmStatsErrorFrames=_MdmStatsErrorFrames_Object((1,3,6,1,2,1,38,1,1,12,1,19),_MdmStatsErrorFrames_Type())
mdmStatsErrorFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:mdmStatsErrorFrames.setStatus(_A)
_MdmConformance_ObjectIdentity=ObjectIdentity
mdmConformance=_MdmConformance_ObjectIdentity((1,3,6,1,2,1,38,1,2))
_MdmCompliances_ObjectIdentity=ObjectIdentity
mdmCompliances=_MdmCompliances_ObjectIdentity((1,3,6,1,2,1,38,1,2,1))
_MdmGroups_ObjectIdentity=ObjectIdentity
mdmGroups=_MdmGroups_ObjectIdentity((1,3,6,1,2,1,38,1,2,2))
mdmIDEntry.registerAugmentions((_B,_P))
mdmLineEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions((_B,_Q))
mdmDTEInterfaceEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions((_B,_R))
mdmCallControlEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions((_B,_S))
mdmECEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions((_B,_T))
mdmDCEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions((_B,_U))
mdmSCEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions((_B,_V))
mdmStatsEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,1))
mdmIDGroup.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:mdmIDGroup.setStatus(_A)
mdmLineInterfaceGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,2))
mdmLineInterfaceGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:mdmLineInterfaceGroup.setStatus(_A)
mdmDTEInterfaceGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,3))
mdmDTEInterfaceGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:mdmDTEInterfaceGroup.setStatus(_A)
mdmCallControlGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,4))
mdmCallControlGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:mdmCallControlGroup.setStatus(_A)
mdmErrorControlGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,5))
mdmErrorControlGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:mdmErrorControlGroup.setStatus(_A)
mdmDataCompressionGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,6))
mdmDataCompressionGroup.setObjects((_B,_q))
if mibBuilder.loadTexts:mdmDataCompressionGroup.setStatus(_A)
mdmSignalConvertorGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,7))
mdmSignalConvertorGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:mdmSignalConvertorGroup.setStatus(_A)
mdmStatisticsGroup=ObjectGroup((1,3,6,1,2,1,38,1,2,2,8))
mdmStatisticsGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:mdmStatisticsGroup.setStatus(_A)
mdmCompliance=ModuleCompliance((1,3,6,1,2,1,38,1,2,1,1))
mdmCompliance.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:mdmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mdmMib':mdmMib,'mdmMIB':mdmMIB,'mdmMIBObjects':mdmMIBObjects,'mdmNumber':mdmNumber,'mdmIDTable':mdmIDTable,'mdmIDEntry':mdmIDEntry,_F:mdmIndex,_W:mdmIDManufacturerOID,_X:mdmIDProductDetails,'mdmLineTable':mdmLineTable,_P:mdmLineEntry,_Y:mdmLineCarrierLossTime,_Z:mdmLineState,'mdmLineCapabilitiesTable':mdmLineCapabilitiesTable,'mdmLineCapabilitiesEntry':mdmLineCapabilitiesEntry,_K:mdmLineCapabilitiesIndex,_a:mdmLineCapabilitiesID,_b:mdmLineCapabilitiesEnableRequested,_c:mdmLineCapabilitiesEnableGranted,'mdmLineCapabilities':mdmLineCapabilities,'mdmLineCapabilitiesV21':mdmLineCapabilitiesV21,'mdmLineCapabilitiesV22':mdmLineCapabilitiesV22,'mdmLineCapabilitiesV22bis':mdmLineCapabilitiesV22bis,'mdmLineCapabilitiesV23CC':mdmLineCapabilitiesV23CC,'mdmLineCapabilitiesV23SC':mdmLineCapabilitiesV23SC,'mdmLineCapabilitiesV25bis':mdmLineCapabilitiesV25bis,'mdmLineCapabilitiesV26bis':mdmLineCapabilitiesV26bis,'mdmLineCapabilitiesV26ter':mdmLineCapabilitiesV26ter,'mdmLineCapabilitiesV27ter':mdmLineCapabilitiesV27ter,'mdmLineCapabilitiesV32':mdmLineCapabilitiesV32,'mdmLineCapabilitiesV32bis':mdmLineCapabilitiesV32bis,'mdmLineCapabilitiesV32terbo':mdmLineCapabilitiesV32terbo,'mdmLineCapabilitiesVFC':mdmLineCapabilitiesVFC,'mdmLineCapabilitiesV34':mdmLineCapabilitiesV34,'mdmLineCapabilitiesV42':mdmLineCapabilitiesV42,'mdmLineCapabilitiesV42bis':mdmLineCapabilitiesV42bis,'mdmLineCapabilitiesMNP1':mdmLineCapabilitiesMNP1,'mdmLineCapabilitiesMNP2':mdmLineCapabilitiesMNP2,'mdmLineCapabilitiesMNP3':mdmLineCapabilitiesMNP3,'mdmLineCapabilitiesMNP4':mdmLineCapabilitiesMNP4,'mdmLineCapabilitiesMNP5':mdmLineCapabilitiesMNP5,'mdmLineCapabilitiesMNP6':mdmLineCapabilitiesMNP6,'mdmLineCapabilitiesMNP7':mdmLineCapabilitiesMNP7,'mdmLineCapabilitiesMNP8':mdmLineCapabilitiesMNP8,'mdmLineCapabilitiesMNP9':mdmLineCapabilitiesMNP9,'mdmLineCapabilitiesMNP10':mdmLineCapabilitiesMNP10,'mdmLineCapabilitiesV29':mdmLineCapabilitiesV29,'mdmLineCapabilitiesV33':mdmLineCapabilitiesV33,'mdmLineCapabilitiesBell208':mdmLineCapabilitiesBell208,'mdmDTEInterfaceTable':mdmDTEInterfaceTable,_Q:mdmDTEInterfaceEntry,_d:mdmDTEActionDTROnToOff,_e:mdmDTEActionDTROffToOn,_f:mdmDTESyncTimingSource,_g:mdmDTESyncAsyncMode,_h:mdmDTEInactivityTimeout,'mdmCallControlTable':mdmCallControlTable,_R:mdmCallControlEntry,_i:mdmCCRingsBeforeAnswer,_j:mdmCCCallSetUpFailTimer,_k:mdmCCResultCodeEnable,_l:mdmCCEscapeAction,_m:mdmCCCallDuration,_n:mdmCCConnectionFailReason,'mdmCCStoredDialStringTable':mdmCCStoredDialStringTable,'mdmCCStoredDialStringEntry':mdmCCStoredDialStringEntry,_O:mdmCCStoredDialStringIndex,_o:mdmCCStoredDialString,'mdmECTable':mdmECTable,_S:mdmECEntry,_p:mdmECErrorControlUsed,'mdmDCTable':mdmDCTable,_T:mdmDCEntry,_q:mdmDCCompressionTypeUsed,'mdmSCTable':mdmSCTable,_U:mdmSCEntry,_s:mdmSCCurrentLineTransmitRate,_r:mdmSCCurrentLineReceiveRate,_u:mdmSCInitialLineTransmitRate,_t:mdmSCInitialLineReceiveRate,_v:mdmSCModulationSchemeUsed,'mdmStatsTable':mdmStatsTable,_V:mdmStatsEntry,_w:mdmStatsRingNoAnswers,_x:mdmStatsIncomingConnectionFailures,_y:mdmStatsIncomingConnectionCompletions,_z:mdmStatsFailedDialAttempts,_A0:mdmStatsOutgoingConnectionFailures,_A1:mdmStatsOutgoingConnectionCompletions,_A2:mdmStatsRetrains,_A3:mdmStats2400OrLessConnections,_A4:mdmStats2400To14400Connections,_A5:mdmStatsGreaterThan14400Connections,_A6:mdmStatsErrorControlledConnections,_A7:mdmStatsCompressedConnections,_A8:mdmStatsCompressionEfficiency,_A9:mdmStatsSentOctets,_AA:mdmStatsReceivedOctets,_AB:mdmStatsSentDataFrames,_AC:mdmStatsReceivedDataFrames,_AD:mdmStatsResentFrames,_AE:mdmStatsErrorFrames,'mdmConformance':mdmConformance,'mdmCompliances':mdmCompliances,'mdmCompliance':mdmCompliance,'mdmGroups':mdmGroups,_AF:mdmIDGroup,_AG:mdmLineInterfaceGroup,_AH:mdmDTEInterfaceGroup,_AI:mdmCallControlGroup,_AL:mdmErrorControlGroup,_AM:mdmDataCompressionGroup,_AJ:mdmSignalConvertorGroup,_AK:mdmStatisticsGroup})