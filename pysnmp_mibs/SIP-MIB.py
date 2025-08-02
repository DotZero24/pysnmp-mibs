_x='sipDxiStuff'
_w='sipIPApplicationsStuff'
_v='sipDS3PLCPStuff'
_u='sipDS1PLCPStuff'
_t='sipLevel2Stuff'
_s='sipLevel3Stuff'
_r='sipDxiHbpNoAcks'
_q='sipDxiOutTestFrames'
_p='sipDxiInTestFrames'
_o='sipDxiInAborts'
_n='sipDxiInErrors'
_m='sipDxiOutDiscards'
_l='sipDxiCrc'
_k='ipOverSMDSARPReq'
_j='ipOverSMDSLISGA'
_i='ipOverSMDSHA'
_h='sipDS3PLCPUASs'
_g='sipDS3PLCPAlarmState'
_f='sipDS3PLCPSEFSs'
_e='sipDS1PLCPUASs'
_d='sipDS1PLCPAlarmState'
_c='sipDS1PLCPSEFSs'
_b='sipL2EomsMIDErrors'
_a='sipL2BomOrSSMsMIDErrors'
_Z='sipL2MidCurrentlyActiveErrors'
_Y='sipL2SequenceNumberErrors'
_X='sipL2PayloadLengthErrors'
_W='sipL2HcsOrCRCErrors'
_V='sipL3PDUErrorTimeStamp'
_U='sipL3PDUErrorDA'
_T='sipL3PDUErrorSA'
_S='sipL3VersionSupport'
_R='incomingLOF'
_Q='receivedFarEndAlarm'
_P='noAlarm'
_O='ifIndex'
_N='IF-MIB'
_M='sipL3PDUErrorType'
_L='sipL3PDUErrorIndex'
_K='ipOverSMDSAddress'
_J='ipOverSMDSIndex'
_I='sipDS3PLCPIndex'
_H='sipDS1PLCPIndex'
_G='sipL2Index'
_F='sipL3Index'
_E='Integer32'
_D='deprecated'
_C='read-only'
_B='SIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_N,_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2','transmission')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
sipMIB=ModuleIdentity((1,3,6,1,2,1,36))
class SMDSAddress(TextualConvention,OctetString):status=_A;displayHint='1h:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class IfIndex(TextualConvention,Integer32):status=_A
_Sip_ObjectIdentity=ObjectIdentity
sip=_Sip_ObjectIdentity((1,3,6,1,2,1,10,31))
_SipL3Table_Object=MibTable
sipL3Table=_SipL3Table_Object((1,3,6,1,2,1,10,31,1))
if mibBuilder.loadTexts:sipL3Table.setStatus(_A)
_SipL3Entry_Object=MibTableRow
sipL3Entry=_SipL3Entry_Object((1,3,6,1,2,1,10,31,1,1))
sipL3Entry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:sipL3Entry.setStatus(_A)
_SipL3Index_Type=IfIndex
_SipL3Index_Object=MibTableColumn
sipL3Index=_SipL3Index_Object((1,3,6,1,2,1,10,31,1,1,1),_SipL3Index_Type())
sipL3Index.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3Index.setStatus(_A)
_SipL3ReceivedIndividualDAs_Type=Counter32
_SipL3ReceivedIndividualDAs_Object=MibTableColumn
sipL3ReceivedIndividualDAs=_SipL3ReceivedIndividualDAs_Object((1,3,6,1,2,1,10,31,1,1,2),_SipL3ReceivedIndividualDAs_Type())
sipL3ReceivedIndividualDAs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3ReceivedIndividualDAs.setStatus(_D)
_SipL3ReceivedGAs_Type=Counter32
_SipL3ReceivedGAs_Object=MibTableColumn
sipL3ReceivedGAs=_SipL3ReceivedGAs_Object((1,3,6,1,2,1,10,31,1,1,3),_SipL3ReceivedGAs_Type())
sipL3ReceivedGAs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3ReceivedGAs.setStatus(_D)
_SipL3UnrecognizedIndividualDAs_Type=Counter32
_SipL3UnrecognizedIndividualDAs_Object=MibTableColumn
sipL3UnrecognizedIndividualDAs=_SipL3UnrecognizedIndividualDAs_Object((1,3,6,1,2,1,10,31,1,1,4),_SipL3UnrecognizedIndividualDAs_Type())
sipL3UnrecognizedIndividualDAs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3UnrecognizedIndividualDAs.setStatus(_D)
_SipL3UnrecognizedGAs_Type=Counter32
_SipL3UnrecognizedGAs_Object=MibTableColumn
sipL3UnrecognizedGAs=_SipL3UnrecognizedGAs_Object((1,3,6,1,2,1,10,31,1,1,5),_SipL3UnrecognizedGAs_Type())
sipL3UnrecognizedGAs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3UnrecognizedGAs.setStatus(_D)
_SipL3SentIndividualDAs_Type=Counter32
_SipL3SentIndividualDAs_Object=MibTableColumn
sipL3SentIndividualDAs=_SipL3SentIndividualDAs_Object((1,3,6,1,2,1,10,31,1,1,6),_SipL3SentIndividualDAs_Type())
sipL3SentIndividualDAs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3SentIndividualDAs.setStatus(_D)
_SipL3SentGAs_Type=Counter32
_SipL3SentGAs_Object=MibTableColumn
sipL3SentGAs=_SipL3SentGAs_Object((1,3,6,1,2,1,10,31,1,1,7),_SipL3SentGAs_Type())
sipL3SentGAs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3SentGAs.setStatus(_D)
_SipL3Errors_Type=Counter32
_SipL3Errors_Object=MibTableColumn
sipL3Errors=_SipL3Errors_Object((1,3,6,1,2,1,10,31,1,1,8),_SipL3Errors_Type())
sipL3Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3Errors.setStatus(_D)
_SipL3InvalidSMDSAddressTypes_Type=Counter32
_SipL3InvalidSMDSAddressTypes_Object=MibTableColumn
sipL3InvalidSMDSAddressTypes=_SipL3InvalidSMDSAddressTypes_Object((1,3,6,1,2,1,10,31,1,1,9),_SipL3InvalidSMDSAddressTypes_Type())
sipL3InvalidSMDSAddressTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3InvalidSMDSAddressTypes.setStatus(_D)
_SipL3VersionSupport_Type=Integer32
_SipL3VersionSupport_Object=MibTableColumn
sipL3VersionSupport=_SipL3VersionSupport_Object((1,3,6,1,2,1,10,31,1,1,10),_SipL3VersionSupport_Type())
sipL3VersionSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3VersionSupport.setStatus(_A)
_SipL2Table_Object=MibTable
sipL2Table=_SipL2Table_Object((1,3,6,1,2,1,10,31,2))
if mibBuilder.loadTexts:sipL2Table.setStatus(_A)
_SipL2Entry_Object=MibTableRow
sipL2Entry=_SipL2Entry_Object((1,3,6,1,2,1,10,31,2,1))
sipL2Entry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:sipL2Entry.setStatus(_A)
_SipL2Index_Type=IfIndex
_SipL2Index_Object=MibTableColumn
sipL2Index=_SipL2Index_Object((1,3,6,1,2,1,10,31,2,1,1),_SipL2Index_Type())
sipL2Index.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2Index.setStatus(_A)
_SipL2ReceivedCounts_Type=Counter32
_SipL2ReceivedCounts_Object=MibTableColumn
sipL2ReceivedCounts=_SipL2ReceivedCounts_Object((1,3,6,1,2,1,10,31,2,1,2),_SipL2ReceivedCounts_Type())
sipL2ReceivedCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2ReceivedCounts.setStatus(_A)
_SipL2SentCounts_Type=Counter32
_SipL2SentCounts_Object=MibTableColumn
sipL2SentCounts=_SipL2SentCounts_Object((1,3,6,1,2,1,10,31,2,1,3),_SipL2SentCounts_Type())
sipL2SentCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2SentCounts.setStatus(_A)
_SipL2HcsOrCRCErrors_Type=Counter32
_SipL2HcsOrCRCErrors_Object=MibTableColumn
sipL2HcsOrCRCErrors=_SipL2HcsOrCRCErrors_Object((1,3,6,1,2,1,10,31,2,1,4),_SipL2HcsOrCRCErrors_Type())
sipL2HcsOrCRCErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2HcsOrCRCErrors.setStatus(_A)
_SipL2PayloadLengthErrors_Type=Counter32
_SipL2PayloadLengthErrors_Object=MibTableColumn
sipL2PayloadLengthErrors=_SipL2PayloadLengthErrors_Object((1,3,6,1,2,1,10,31,2,1,5),_SipL2PayloadLengthErrors_Type())
sipL2PayloadLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2PayloadLengthErrors.setStatus(_A)
_SipL2SequenceNumberErrors_Type=Counter32
_SipL2SequenceNumberErrors_Object=MibTableColumn
sipL2SequenceNumberErrors=_SipL2SequenceNumberErrors_Object((1,3,6,1,2,1,10,31,2,1,6),_SipL2SequenceNumberErrors_Type())
sipL2SequenceNumberErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2SequenceNumberErrors.setStatus(_A)
_SipL2MidCurrentlyActiveErrors_Type=Counter32
_SipL2MidCurrentlyActiveErrors_Object=MibTableColumn
sipL2MidCurrentlyActiveErrors=_SipL2MidCurrentlyActiveErrors_Object((1,3,6,1,2,1,10,31,2,1,7),_SipL2MidCurrentlyActiveErrors_Type())
sipL2MidCurrentlyActiveErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2MidCurrentlyActiveErrors.setStatus(_A)
_SipL2BomOrSSMsMIDErrors_Type=Counter32
_SipL2BomOrSSMsMIDErrors_Object=MibTableColumn
sipL2BomOrSSMsMIDErrors=_SipL2BomOrSSMsMIDErrors_Object((1,3,6,1,2,1,10,31,2,1,8),_SipL2BomOrSSMsMIDErrors_Type())
sipL2BomOrSSMsMIDErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2BomOrSSMsMIDErrors.setStatus(_A)
_SipL2EomsMIDErrors_Type=Counter32
_SipL2EomsMIDErrors_Object=MibTableColumn
sipL2EomsMIDErrors=_SipL2EomsMIDErrors_Object((1,3,6,1,2,1,10,31,2,1,9),_SipL2EomsMIDErrors_Type())
sipL2EomsMIDErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL2EomsMIDErrors.setStatus(_A)
_SipPLCP_ObjectIdentity=ObjectIdentity
sipPLCP=_SipPLCP_ObjectIdentity((1,3,6,1,2,1,10,31,3))
_SipDS1PLCPTable_Object=MibTable
sipDS1PLCPTable=_SipDS1PLCPTable_Object((1,3,6,1,2,1,10,31,3,1))
if mibBuilder.loadTexts:sipDS1PLCPTable.setStatus(_A)
_SipDS1PLCPEntry_Object=MibTableRow
sipDS1PLCPEntry=_SipDS1PLCPEntry_Object((1,3,6,1,2,1,10,31,3,1,1))
sipDS1PLCPEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:sipDS1PLCPEntry.setStatus(_A)
_SipDS1PLCPIndex_Type=IfIndex
_SipDS1PLCPIndex_Object=MibTableColumn
sipDS1PLCPIndex=_SipDS1PLCPIndex_Object((1,3,6,1,2,1,10,31,3,1,1,1),_SipDS1PLCPIndex_Type())
sipDS1PLCPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS1PLCPIndex.setStatus(_A)
_SipDS1PLCPSEFSs_Type=Counter32
_SipDS1PLCPSEFSs_Object=MibTableColumn
sipDS1PLCPSEFSs=_SipDS1PLCPSEFSs_Object((1,3,6,1,2,1,10,31,3,1,1,2),_SipDS1PLCPSEFSs_Type())
sipDS1PLCPSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS1PLCPSEFSs.setStatus(_A)
class _SipDS1PLCPAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
_SipDS1PLCPAlarmState_Type.__name__=_E
_SipDS1PLCPAlarmState_Object=MibTableColumn
sipDS1PLCPAlarmState=_SipDS1PLCPAlarmState_Object((1,3,6,1,2,1,10,31,3,1,1,3),_SipDS1PLCPAlarmState_Type())
sipDS1PLCPAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS1PLCPAlarmState.setStatus(_A)
_SipDS1PLCPUASs_Type=Counter32
_SipDS1PLCPUASs_Object=MibTableColumn
sipDS1PLCPUASs=_SipDS1PLCPUASs_Object((1,3,6,1,2,1,10,31,3,1,1,4),_SipDS1PLCPUASs_Type())
sipDS1PLCPUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS1PLCPUASs.setStatus(_A)
_SipDS3PLCPTable_Object=MibTable
sipDS3PLCPTable=_SipDS3PLCPTable_Object((1,3,6,1,2,1,10,31,3,2))
if mibBuilder.loadTexts:sipDS3PLCPTable.setStatus(_A)
_SipDS3PLCPEntry_Object=MibTableRow
sipDS3PLCPEntry=_SipDS3PLCPEntry_Object((1,3,6,1,2,1,10,31,3,2,1))
sipDS3PLCPEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:sipDS3PLCPEntry.setStatus(_A)
_SipDS3PLCPIndex_Type=IfIndex
_SipDS3PLCPIndex_Object=MibTableColumn
sipDS3PLCPIndex=_SipDS3PLCPIndex_Object((1,3,6,1,2,1,10,31,3,2,1,1),_SipDS3PLCPIndex_Type())
sipDS3PLCPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS3PLCPIndex.setStatus(_A)
_SipDS3PLCPSEFSs_Type=Counter32
_SipDS3PLCPSEFSs_Object=MibTableColumn
sipDS3PLCPSEFSs=_SipDS3PLCPSEFSs_Object((1,3,6,1,2,1,10,31,3,2,1,2),_SipDS3PLCPSEFSs_Type())
sipDS3PLCPSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS3PLCPSEFSs.setStatus(_A)
class _SipDS3PLCPAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
_SipDS3PLCPAlarmState_Type.__name__=_E
_SipDS3PLCPAlarmState_Object=MibTableColumn
sipDS3PLCPAlarmState=_SipDS3PLCPAlarmState_Object((1,3,6,1,2,1,10,31,3,2,1,3),_SipDS3PLCPAlarmState_Type())
sipDS3PLCPAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS3PLCPAlarmState.setStatus(_A)
_SipDS3PLCPUASs_Type=Counter32
_SipDS3PLCPUASs_Object=MibTableColumn
sipDS3PLCPUASs=_SipDS3PLCPUASs_Object((1,3,6,1,2,1,10,31,3,2,1,4),_SipDS3PLCPUASs_Type())
sipDS3PLCPUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDS3PLCPUASs.setStatus(_A)
_SmdsApplications_ObjectIdentity=ObjectIdentity
smdsApplications=_SmdsApplications_ObjectIdentity((1,3,6,1,2,1,10,31,4))
_IpOverSMDS_ObjectIdentity=ObjectIdentity
ipOverSMDS=_IpOverSMDS_ObjectIdentity((1,3,6,1,2,1,10,31,4,1))
_IpOverSMDSTable_Object=MibTable
ipOverSMDSTable=_IpOverSMDSTable_Object((1,3,6,1,2,1,10,31,4,1,1))
if mibBuilder.loadTexts:ipOverSMDSTable.setStatus(_A)
_IpOverSMDSEntry_Object=MibTableRow
ipOverSMDSEntry=_IpOverSMDSEntry_Object((1,3,6,1,2,1,10,31,4,1,1,1))
ipOverSMDSEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:ipOverSMDSEntry.setStatus(_A)
_IpOverSMDSIndex_Type=IfIndex
_IpOverSMDSIndex_Object=MibTableColumn
ipOverSMDSIndex=_IpOverSMDSIndex_Object((1,3,6,1,2,1,10,31,4,1,1,1,1),_IpOverSMDSIndex_Type())
ipOverSMDSIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipOverSMDSIndex.setStatus(_A)
_IpOverSMDSAddress_Type=IpAddress
_IpOverSMDSAddress_Object=MibTableColumn
ipOverSMDSAddress=_IpOverSMDSAddress_Object((1,3,6,1,2,1,10,31,4,1,1,1,2),_IpOverSMDSAddress_Type())
ipOverSMDSAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipOverSMDSAddress.setStatus(_A)
_IpOverSMDSHA_Type=SMDSAddress
_IpOverSMDSHA_Object=MibTableColumn
ipOverSMDSHA=_IpOverSMDSHA_Object((1,3,6,1,2,1,10,31,4,1,1,1,3),_IpOverSMDSHA_Type())
ipOverSMDSHA.setMaxAccess(_C)
if mibBuilder.loadTexts:ipOverSMDSHA.setStatus(_A)
_IpOverSMDSLISGA_Type=SMDSAddress
_IpOverSMDSLISGA_Object=MibTableColumn
ipOverSMDSLISGA=_IpOverSMDSLISGA_Object((1,3,6,1,2,1,10,31,4,1,1,1,4),_IpOverSMDSLISGA_Type())
ipOverSMDSLISGA.setMaxAccess(_C)
if mibBuilder.loadTexts:ipOverSMDSLISGA.setStatus(_A)
_IpOverSMDSARPReq_Type=SMDSAddress
_IpOverSMDSARPReq_Object=MibTableColumn
ipOverSMDSARPReq=_IpOverSMDSARPReq_Object((1,3,6,1,2,1,10,31,4,1,1,1,5),_IpOverSMDSARPReq_Type())
ipOverSMDSARPReq.setMaxAccess(_C)
if mibBuilder.loadTexts:ipOverSMDSARPReq.setStatus(_A)
_SmdsCarrierSelection_ObjectIdentity=ObjectIdentity
smdsCarrierSelection=_SmdsCarrierSelection_ObjectIdentity((1,3,6,1,2,1,10,31,5))
_SipErrorLog_ObjectIdentity=ObjectIdentity
sipErrorLog=_SipErrorLog_ObjectIdentity((1,3,6,1,2,1,10,31,6))
_SipL3PDUErrorTable_Object=MibTable
sipL3PDUErrorTable=_SipL3PDUErrorTable_Object((1,3,6,1,2,1,10,31,6,1))
if mibBuilder.loadTexts:sipL3PDUErrorTable.setStatus(_A)
_SipL3PDUErrorEntry_Object=MibTableRow
sipL3PDUErrorEntry=_SipL3PDUErrorEntry_Object((1,3,6,1,2,1,10,31,6,1,1))
sipL3PDUErrorEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:sipL3PDUErrorEntry.setStatus(_A)
_SipL3PDUErrorIndex_Type=IfIndex
_SipL3PDUErrorIndex_Object=MibTableColumn
sipL3PDUErrorIndex=_SipL3PDUErrorIndex_Object((1,3,6,1,2,1,10,31,6,1,1,1),_SipL3PDUErrorIndex_Type())
sipL3PDUErrorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3PDUErrorIndex.setStatus(_A)
class _SipL3PDUErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('erroredDAFieldFormat',1),('erroredSAFieldFormat',2),('invalidBAsizeFieldValue',3),('invalidHdrExtLength',4),('invalidHdrExtElementLength',5),('invalidHdrExtVersionElementPositionLenthOrValue',6),('invalidHdrExtCarSelectElementPositionLenghtValueOrFormat',7),('hePADError',8),('beTagMismatch',9),('baSizeFieldNotEqualToLengthField',10),('incorrectLength',11),('mriTimeout',12)))
_SipL3PDUErrorType_Type.__name__=_E
_SipL3PDUErrorType_Object=MibTableColumn
sipL3PDUErrorType=_SipL3PDUErrorType_Object((1,3,6,1,2,1,10,31,6,1,1,2),_SipL3PDUErrorType_Type())
sipL3PDUErrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3PDUErrorType.setStatus(_A)
_SipL3PDUErrorSA_Type=SMDSAddress
_SipL3PDUErrorSA_Object=MibTableColumn
sipL3PDUErrorSA=_SipL3PDUErrorSA_Object((1,3,6,1,2,1,10,31,6,1,1,3),_SipL3PDUErrorSA_Type())
sipL3PDUErrorSA.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3PDUErrorSA.setStatus(_A)
_SipL3PDUErrorDA_Type=SMDSAddress
_SipL3PDUErrorDA_Object=MibTableColumn
sipL3PDUErrorDA=_SipL3PDUErrorDA_Object((1,3,6,1,2,1,10,31,6,1,1,4),_SipL3PDUErrorDA_Type())
sipL3PDUErrorDA.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3PDUErrorDA.setStatus(_A)
_SipL3PDUErrorTimeStamp_Type=TimeStamp
_SipL3PDUErrorTimeStamp_Object=MibTableColumn
sipL3PDUErrorTimeStamp=_SipL3PDUErrorTimeStamp_Object((1,3,6,1,2,1,10,31,6,1,1,5),_SipL3PDUErrorTimeStamp_Type())
sipL3PDUErrorTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sipL3PDUErrorTimeStamp.setStatus(_A)
_SipMIBObjects_ObjectIdentity=ObjectIdentity
sipMIBObjects=_SipMIBObjects_ObjectIdentity((1,3,6,1,2,1,36,1))
_SipDxiTable_Object=MibTable
sipDxiTable=_SipDxiTable_Object((1,3,6,1,2,1,36,1,1))
if mibBuilder.loadTexts:sipDxiTable.setStatus(_A)
_SipDxiEntry_Object=MibTableRow
sipDxiEntry=_SipDxiEntry_Object((1,3,6,1,2,1,36,1,1,1))
sipDxiEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:sipDxiEntry.setStatus(_A)
class _SipDxiCrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crc16',1),('crc32',2)))
_SipDxiCrc_Type.__name__=_E
_SipDxiCrc_Object=MibTableColumn
sipDxiCrc=_SipDxiCrc_Object((1,3,6,1,2,1,36,1,1,1,1),_SipDxiCrc_Type())
sipDxiCrc.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDxiCrc.setStatus(_A)
_SipDxiOutDiscards_Type=Counter32
_SipDxiOutDiscards_Object=MibTableColumn
sipDxiOutDiscards=_SipDxiOutDiscards_Object((1,3,6,1,2,1,36,1,1,1,2),_SipDxiOutDiscards_Type())
sipDxiOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDxiOutDiscards.setStatus(_A)
_SipDxiInErrors_Type=Counter32
_SipDxiInErrors_Object=MibTableColumn
sipDxiInErrors=_SipDxiInErrors_Object((1,3,6,1,2,1,36,1,1,1,3),_SipDxiInErrors_Type())
sipDxiInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDxiInErrors.setStatus(_A)
_SipDxiInAborts_Type=Counter32
_SipDxiInAborts_Object=MibTableColumn
sipDxiInAborts=_SipDxiInAborts_Object((1,3,6,1,2,1,36,1,1,1,4),_SipDxiInAborts_Type())
sipDxiInAborts.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDxiInAborts.setStatus(_A)
_SipDxiInTestFrames_Type=Counter32
_SipDxiInTestFrames_Object=MibTableColumn
sipDxiInTestFrames=_SipDxiInTestFrames_Object((1,3,6,1,2,1,36,1,1,1,5),_SipDxiInTestFrames_Type())
sipDxiInTestFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDxiInTestFrames.setStatus(_A)
_SipDxiOutTestFrames_Type=Counter32
_SipDxiOutTestFrames_Object=MibTableColumn
sipDxiOutTestFrames=_SipDxiOutTestFrames_Object((1,3,6,1,2,1,36,1,1,1,6),_SipDxiOutTestFrames_Type())
sipDxiOutTestFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDxiOutTestFrames.setStatus(_A)
_SipDxiHbpNoAcks_Type=Counter32
_SipDxiHbpNoAcks_Object=MibTableColumn
sipDxiHbpNoAcks=_SipDxiHbpNoAcks_Object((1,3,6,1,2,1,36,1,1,1,7),_SipDxiHbpNoAcks_Type())
sipDxiHbpNoAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:sipDxiHbpNoAcks.setStatus(_A)
_SmdsConformance_ObjectIdentity=ObjectIdentity
smdsConformance=_SmdsConformance_ObjectIdentity((1,3,6,1,2,1,36,2))
_SmdsGroups_ObjectIdentity=ObjectIdentity
smdsGroups=_SmdsGroups_ObjectIdentity((1,3,6,1,2,1,36,2,1))
_SmdsCompliances_ObjectIdentity=ObjectIdentity
smdsCompliances=_SmdsCompliances_ObjectIdentity((1,3,6,1,2,1,36,2,2))
sipLevel3Stuff=ObjectGroup((1,3,6,1,2,1,36,2,1,1))
sipLevel3Stuff.setObjects(*((_B,_F),(_B,_S),(_B,_L),(_B,_M),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:sipLevel3Stuff.setStatus(_A)
sipLevel2Stuff=ObjectGroup((1,3,6,1,2,1,36,2,1,2))
sipLevel2Stuff.setObjects(*((_B,_G),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:sipLevel2Stuff.setStatus(_A)
sipDS1PLCPStuff=ObjectGroup((1,3,6,1,2,1,36,2,1,3))
sipDS1PLCPStuff.setObjects(*((_B,_H),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:sipDS1PLCPStuff.setStatus(_A)
sipDS3PLCPStuff=ObjectGroup((1,3,6,1,2,1,36,2,1,4))
sipDS3PLCPStuff.setObjects(*((_B,_I),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:sipDS3PLCPStuff.setStatus(_A)
sipIPApplicationsStuff=ObjectGroup((1,3,6,1,2,1,36,2,1,5))
sipIPApplicationsStuff.setObjects(*((_B,_J),(_B,_K),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:sipIPApplicationsStuff.setStatus(_A)
sipDxiStuff=ObjectGroup((1,3,6,1,2,1,36,2,1,6))
sipDxiStuff.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:sipDxiStuff.setStatus(_A)
smdsCompliance=ModuleCompliance((1,3,6,1,2,1,36,2,2,1))
smdsCompliance.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:smdsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SMDSAddress':SMDSAddress,'IfIndex':IfIndex,'sip':sip,'sipL3Table':sipL3Table,'sipL3Entry':sipL3Entry,_F:sipL3Index,'sipL3ReceivedIndividualDAs':sipL3ReceivedIndividualDAs,'sipL3ReceivedGAs':sipL3ReceivedGAs,'sipL3UnrecognizedIndividualDAs':sipL3UnrecognizedIndividualDAs,'sipL3UnrecognizedGAs':sipL3UnrecognizedGAs,'sipL3SentIndividualDAs':sipL3SentIndividualDAs,'sipL3SentGAs':sipL3SentGAs,'sipL3Errors':sipL3Errors,'sipL3InvalidSMDSAddressTypes':sipL3InvalidSMDSAddressTypes,_S:sipL3VersionSupport,'sipL2Table':sipL2Table,'sipL2Entry':sipL2Entry,_G:sipL2Index,'sipL2ReceivedCounts':sipL2ReceivedCounts,'sipL2SentCounts':sipL2SentCounts,_W:sipL2HcsOrCRCErrors,_X:sipL2PayloadLengthErrors,_Y:sipL2SequenceNumberErrors,_Z:sipL2MidCurrentlyActiveErrors,_a:sipL2BomOrSSMsMIDErrors,_b:sipL2EomsMIDErrors,'sipPLCP':sipPLCP,'sipDS1PLCPTable':sipDS1PLCPTable,'sipDS1PLCPEntry':sipDS1PLCPEntry,_H:sipDS1PLCPIndex,_c:sipDS1PLCPSEFSs,_d:sipDS1PLCPAlarmState,_e:sipDS1PLCPUASs,'sipDS3PLCPTable':sipDS3PLCPTable,'sipDS3PLCPEntry':sipDS3PLCPEntry,_I:sipDS3PLCPIndex,_f:sipDS3PLCPSEFSs,_g:sipDS3PLCPAlarmState,_h:sipDS3PLCPUASs,'smdsApplications':smdsApplications,'ipOverSMDS':ipOverSMDS,'ipOverSMDSTable':ipOverSMDSTable,'ipOverSMDSEntry':ipOverSMDSEntry,_J:ipOverSMDSIndex,_K:ipOverSMDSAddress,_i:ipOverSMDSHA,_j:ipOverSMDSLISGA,_k:ipOverSMDSARPReq,'smdsCarrierSelection':smdsCarrierSelection,'sipErrorLog':sipErrorLog,'sipL3PDUErrorTable':sipL3PDUErrorTable,'sipL3PDUErrorEntry':sipL3PDUErrorEntry,_L:sipL3PDUErrorIndex,_M:sipL3PDUErrorType,_T:sipL3PDUErrorSA,_U:sipL3PDUErrorDA,_V:sipL3PDUErrorTimeStamp,'sipMIB':sipMIB,'sipMIBObjects':sipMIBObjects,'sipDxiTable':sipDxiTable,'sipDxiEntry':sipDxiEntry,_l:sipDxiCrc,_m:sipDxiOutDiscards,_n:sipDxiInErrors,_o:sipDxiInAborts,_p:sipDxiInTestFrames,_q:sipDxiOutTestFrames,_r:sipDxiHbpNoAcks,'smdsConformance':smdsConformance,'smdsGroups':smdsGroups,_s:sipLevel3Stuff,_t:sipLevel2Stuff,_u:sipDS1PLCPStuff,_v:sipDS3PLCPStuff,_w:sipIPApplicationsStuff,_x:sipDxiStuff,'smdsCompliances':smdsCompliances,'smdsCompliance':smdsCompliance})