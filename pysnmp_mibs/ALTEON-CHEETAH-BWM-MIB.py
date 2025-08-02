_n='bwmStatPortTcrContractIndex'
_m='bwmStatPortTcrPortIndex'
_l='bwmStatPortTcContractIndex'
_k='bwmStatPortTcPortIndex'
_j='bwmStatTcrContractIndex'
_i='bwmStatTcContractIndex'
_h='bwmNewCfgContractGroupIndx'
_g='bwmCurCfgContractGroupIndx'
_f='bwmNewCfgContTimePolicyIndx'
_e='bwmNewCfgContTimePolicyContIndx'
_d='everyday'
_c='weekend'
_b='weekday'
_a='saturday'
_Z='friday'
_Y='thursday'
_X='wednesday'
_W='tuesday'
_V='monday'
_U='sunday'
_T='bwmCurCfgContTimePolicyIndx'
_S='bwmCurCfgContTimePolicyContIndx'
_R='bwmContractIndx'
_Q='bwmNewCfgContractIndx'
_P='reserved'
_O='regular'
_N='bwmCurCfgContractIndx'
_M='bwmNewCfgPolicyIndx'
_L='bwmCurCfgPolicyIndx'
_K='delete'
_J='other'
_I='read-write'
_H='ALTEON-CHEETAH-BWM-MIB'
_G='disabled'
_F='enabled'
_E='DisplayString'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aws_switch,=mibBuilder.importSymbols('ALTEON-ROOT-MIB','aws-switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
bwm=ModuleIdentity((1,3,6,1,4,1,1872,2,5,6))
if mibBuilder.loadTexts:bwm.setRevisions(('2009-08-05 00:00',))
_BwmConfigs_ObjectIdentity=ObjectIdentity
bwmConfigs=_BwmConfigs_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,1))
_BwmGeneralConfig_ObjectIdentity=ObjectIdentity
bwmGeneralConfig=_BwmGeneralConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,1,1))
class _BwmCurCfgGenState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('on',2),('off',3)))
_BwmCurCfgGenState_Type.__name__=_C
_BwmCurCfgGenState_Object=MibScalar
bwmCurCfgGenState=_BwmCurCfgGenState_Object((1,3,6,1,4,1,1872,2,5,6,1,1,1),_BwmCurCfgGenState_Type())
bwmCurCfgGenState.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenState.setStatus(_A)
class _BwmNewCfgGenState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('on',2),('off',3)))
_BwmNewCfgGenState_Type.__name__=_C
_BwmNewCfgGenState_Object=MibScalar
bwmNewCfgGenState=_BwmNewCfgGenState_Object((1,3,6,1,4,1,1872,2,5,6,1,1,2),_BwmNewCfgGenState_Type())
bwmNewCfgGenState.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenState.setStatus(_A)
class _BwmCurCfgGenEnforcePolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmCurCfgGenEnforcePolicy_Type.__name__=_C
_BwmCurCfgGenEnforcePolicy_Object=MibScalar
bwmCurCfgGenEnforcePolicy=_BwmCurCfgGenEnforcePolicy_Object((1,3,6,1,4,1,1872,2,5,6,1,1,3),_BwmCurCfgGenEnforcePolicy_Type())
bwmCurCfgGenEnforcePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenEnforcePolicy.setStatus(_A)
class _BwmNewCfgGenEnforcePolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmNewCfgGenEnforcePolicy_Type.__name__=_C
_BwmNewCfgGenEnforcePolicy_Object=MibScalar
bwmNewCfgGenEnforcePolicy=_BwmNewCfgGenEnforcePolicy_Object((1,3,6,1,4,1,1872,2,5,6,1,1,4),_BwmNewCfgGenEnforcePolicy_Type())
bwmNewCfgGenEnforcePolicy.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenEnforcePolicy.setStatus(_A)
class _BwmCurCfgGenSmtpUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_BwmCurCfgGenSmtpUser_Type.__name__=_E
_BwmCurCfgGenSmtpUser_Object=MibScalar
bwmCurCfgGenSmtpUser=_BwmCurCfgGenSmtpUser_Object((1,3,6,1,4,1,1872,2,5,6,1,1,5),_BwmCurCfgGenSmtpUser_Type())
bwmCurCfgGenSmtpUser.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenSmtpUser.setStatus(_A)
class _BwmNewCfgGenSmtpUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_BwmNewCfgGenSmtpUser_Type.__name__=_E
_BwmNewCfgGenSmtpUser_Object=MibScalar
bwmNewCfgGenSmtpUser=_BwmNewCfgGenSmtpUser_Object((1,3,6,1,4,1,1872,2,5,6,1,1,6),_BwmNewCfgGenSmtpUser_Type())
bwmNewCfgGenSmtpUser.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenSmtpUser.setStatus(_A)
class _BwmCurCfgGenEmailFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_BwmCurCfgGenEmailFrequency_Type.__name__=_C
_BwmCurCfgGenEmailFrequency_Object=MibScalar
bwmCurCfgGenEmailFrequency=_BwmCurCfgGenEmailFrequency_Object((1,3,6,1,4,1,1872,2,5,6,1,1,7),_BwmCurCfgGenEmailFrequency_Type())
bwmCurCfgGenEmailFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenEmailFrequency.setStatus(_A)
class _BwmNewCfgGenEmailFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_BwmNewCfgGenEmailFrequency_Type.__name__=_C
_BwmNewCfgGenEmailFrequency_Object=MibScalar
bwmNewCfgGenEmailFrequency=_BwmNewCfgGenEmailFrequency_Object((1,3,6,1,4,1,1872,2,5,6,1,1,8),_BwmNewCfgGenEmailFrequency_Type())
bwmNewCfgGenEmailFrequency.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenEmailFrequency.setStatus(_A)
class _BwmCurCfgGenIPUserLimit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_BwmCurCfgGenIPUserLimit_Type.__name__=_E
_BwmCurCfgGenIPUserLimit_Object=MibScalar
bwmCurCfgGenIPUserLimit=_BwmCurCfgGenIPUserLimit_Object((1,3,6,1,4,1,1872,2,5,6,1,1,9),_BwmCurCfgGenIPUserLimit_Type())
bwmCurCfgGenIPUserLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenIPUserLimit.setStatus(_A)
class _BwmNewCfgGenIPUserLimit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_BwmNewCfgGenIPUserLimit_Type.__name__=_E
_BwmNewCfgGenIPUserLimit_Object=MibScalar
bwmNewCfgGenIPUserLimit=_BwmNewCfgGenIPUserLimit_Object((1,3,6,1,4,1,1872,2,5,6,1,1,10),_BwmNewCfgGenIPUserLimit_Type())
bwmNewCfgGenIPUserLimit.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenIPUserLimit.setStatus(_A)
class _BwmCurCfgGenEmail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmCurCfgGenEmail_Type.__name__=_C
_BwmCurCfgGenEmail_Object=MibScalar
bwmCurCfgGenEmail=_BwmCurCfgGenEmail_Object((1,3,6,1,4,1,1872,2,5,6,1,1,11),_BwmCurCfgGenEmail_Type())
bwmCurCfgGenEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenEmail.setStatus(_A)
class _BwmNewCfgGenEmail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmNewCfgGenEmail_Type.__name__=_C
_BwmNewCfgGenEmail_Object=MibScalar
bwmNewCfgGenEmail=_BwmNewCfgGenEmail_Object((1,3,6,1,4,1,1872,2,5,6,1,1,12),_BwmNewCfgGenEmail_Type())
bwmNewCfgGenEmail.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenEmail.setStatus(_A)
_BwmCurCfgGenReport_Type=IpAddress
_BwmCurCfgGenReport_Object=MibScalar
bwmCurCfgGenReport=_BwmCurCfgGenReport_Object((1,3,6,1,4,1,1872,2,5,6,1,1,13),_BwmCurCfgGenReport_Type())
bwmCurCfgGenReport.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenReport.setStatus(_A)
_BwmNewCfgGenReport_Type=IpAddress
_BwmNewCfgGenReport_Object=MibScalar
bwmNewCfgGenReport=_BwmNewCfgGenReport_Object((1,3,6,1,4,1,1872,2,5,6,1,1,14),_BwmNewCfgGenReport_Type())
bwmNewCfgGenReport.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenReport.setStatus(_A)
_BwmCurCfgGenReportStr_Type=DisplayString
_BwmCurCfgGenReportStr_Object=MibScalar
bwmCurCfgGenReportStr=_BwmCurCfgGenReportStr_Object((1,3,6,1,4,1,1872,2,5,6,1,1,15),_BwmCurCfgGenReportStr_Type())
bwmCurCfgGenReportStr.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgGenReportStr.setStatus(_A)
_BwmNewCfgGenReportStr_Type=DisplayString
_BwmNewCfgGenReportStr_Object=MibScalar
bwmNewCfgGenReportStr=_BwmNewCfgGenReportStr_Object((1,3,6,1,4,1,1872,2,5,6,1,1,16),_BwmNewCfgGenReportStr_Type())
bwmNewCfgGenReportStr.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmNewCfgGenReportStr.setStatus(_A)
_BwmPolicyConfig_ObjectIdentity=ObjectIdentity
bwmPolicyConfig=_BwmPolicyConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,1,2))
_BwmPolicyTableMaxEnt_Type=Integer32
_BwmPolicyTableMaxEnt_Object=MibScalar
bwmPolicyTableMaxEnt=_BwmPolicyTableMaxEnt_Object((1,3,6,1,4,1,1872,2,5,6,1,2,1),_BwmPolicyTableMaxEnt_Type())
bwmPolicyTableMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmPolicyTableMaxEnt.setStatus(_A)
_BwmCurCfgPolicyTable_Object=MibTable
bwmCurCfgPolicyTable=_BwmCurCfgPolicyTable_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2))
if mibBuilder.loadTexts:bwmCurCfgPolicyTable.setStatus(_A)
_BwmCurCfgPolicyTableEntry_Object=MibTableRow
bwmCurCfgPolicyTableEntry=_BwmCurCfgPolicyTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1))
bwmCurCfgPolicyTableEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:bwmCurCfgPolicyTableEntry.setStatus(_A)
_BwmCurCfgPolicyIndx_Type=Integer32
_BwmCurCfgPolicyIndx_Object=MibTableColumn
bwmCurCfgPolicyIndx=_BwmCurCfgPolicyIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,1),_BwmCurCfgPolicyIndx_Type())
bwmCurCfgPolicyIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicyIndx.setStatus(_A)
class _BwmCurCfgPolicyTosIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BwmCurCfgPolicyTosIn_Type.__name__=_C
_BwmCurCfgPolicyTosIn_Object=MibTableColumn
bwmCurCfgPolicyTosIn=_BwmCurCfgPolicyTosIn_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,2),_BwmCurCfgPolicyTosIn_Type())
bwmCurCfgPolicyTosIn.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicyTosIn.setStatus(_A)
class _BwmCurCfgPolicyTosOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BwmCurCfgPolicyTosOut_Type.__name__=_C
_BwmCurCfgPolicyTosOut_Object=MibTableColumn
bwmCurCfgPolicyTosOut=_BwmCurCfgPolicyTosOut_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,3),_BwmCurCfgPolicyTosOut_Type())
bwmCurCfgPolicyTosOut.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicyTosOut.setStatus(_A)
class _BwmCurCfgPolicyHard_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmCurCfgPolicyHard_Type.__name__=_E
_BwmCurCfgPolicyHard_Object=MibTableColumn
bwmCurCfgPolicyHard=_BwmCurCfgPolicyHard_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,4),_BwmCurCfgPolicyHard_Type())
bwmCurCfgPolicyHard.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicyHard.setStatus(_A)
class _BwmCurCfgPolicySoft_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmCurCfgPolicySoft_Type.__name__=_E
_BwmCurCfgPolicySoft_Object=MibTableColumn
bwmCurCfgPolicySoft=_BwmCurCfgPolicySoft_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,5),_BwmCurCfgPolicySoft_Type())
bwmCurCfgPolicySoft.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicySoft.setStatus(_A)
class _BwmCurCfgPolicyResv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmCurCfgPolicyResv_Type.__name__=_E
_BwmCurCfgPolicyResv_Object=MibTableColumn
bwmCurCfgPolicyResv=_BwmCurCfgPolicyResv_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,6),_BwmCurCfgPolicyResv_Type())
bwmCurCfgPolicyResv.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicyResv.setStatus(_A)
class _BwmCurCfgPolicyBuffer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8192,128000))
_BwmCurCfgPolicyBuffer_Type.__name__=_C
_BwmCurCfgPolicyBuffer_Object=MibTableColumn
bwmCurCfgPolicyBuffer=_BwmCurCfgPolicyBuffer_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,7),_BwmCurCfgPolicyBuffer_Type())
bwmCurCfgPolicyBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicyBuffer.setStatus(_A)
class _BwmCurCfgPolicyUserLimit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmCurCfgPolicyUserLimit_Type.__name__=_E
_BwmCurCfgPolicyUserLimit_Object=MibTableColumn
bwmCurCfgPolicyUserLimit=_BwmCurCfgPolicyUserLimit_Object((1,3,6,1,4,1,1872,2,5,6,1,2,2,1,8),_BwmCurCfgPolicyUserLimit_Type())
bwmCurCfgPolicyUserLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgPolicyUserLimit.setStatus(_A)
_BwmNewCfgPolicyTable_Object=MibTable
bwmNewCfgPolicyTable=_BwmNewCfgPolicyTable_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3))
if mibBuilder.loadTexts:bwmNewCfgPolicyTable.setStatus(_A)
_BwmNewCfgPolicyTableEntry_Object=MibTableRow
bwmNewCfgPolicyTableEntry=_BwmNewCfgPolicyTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1))
bwmNewCfgPolicyTableEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:bwmNewCfgPolicyTableEntry.setStatus(_A)
_BwmNewCfgPolicyIndx_Type=Integer32
_BwmNewCfgPolicyIndx_Object=MibTableColumn
bwmNewCfgPolicyIndx=_BwmNewCfgPolicyIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,1),_BwmNewCfgPolicyIndx_Type())
bwmNewCfgPolicyIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgPolicyIndx.setStatus(_A)
class _BwmNewCfgPolicyTosIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BwmNewCfgPolicyTosIn_Type.__name__=_C
_BwmNewCfgPolicyTosIn_Object=MibTableColumn
bwmNewCfgPolicyTosIn=_BwmNewCfgPolicyTosIn_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,2),_BwmNewCfgPolicyTosIn_Type())
bwmNewCfgPolicyTosIn.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicyTosIn.setStatus(_A)
class _BwmNewCfgPolicyTosOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BwmNewCfgPolicyTosOut_Type.__name__=_C
_BwmNewCfgPolicyTosOut_Object=MibTableColumn
bwmNewCfgPolicyTosOut=_BwmNewCfgPolicyTosOut_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,3),_BwmNewCfgPolicyTosOut_Type())
bwmNewCfgPolicyTosOut.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicyTosOut.setStatus(_A)
class _BwmNewCfgPolicyHard_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmNewCfgPolicyHard_Type.__name__=_E
_BwmNewCfgPolicyHard_Object=MibTableColumn
bwmNewCfgPolicyHard=_BwmNewCfgPolicyHard_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,4),_BwmNewCfgPolicyHard_Type())
bwmNewCfgPolicyHard.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicyHard.setStatus(_A)
class _BwmNewCfgPolicySoft_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmNewCfgPolicySoft_Type.__name__=_E
_BwmNewCfgPolicySoft_Object=MibTableColumn
bwmNewCfgPolicySoft=_BwmNewCfgPolicySoft_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,5),_BwmNewCfgPolicySoft_Type())
bwmNewCfgPolicySoft.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicySoft.setStatus(_A)
class _BwmNewCfgPolicyResv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmNewCfgPolicyResv_Type.__name__=_E
_BwmNewCfgPolicyResv_Object=MibTableColumn
bwmNewCfgPolicyResv=_BwmNewCfgPolicyResv_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,6),_BwmNewCfgPolicyResv_Type())
bwmNewCfgPolicyResv.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicyResv.setStatus(_A)
class _BwmNewCfgPolicyBuffer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8192,128000))
_BwmNewCfgPolicyBuffer_Type.__name__=_C
_BwmNewCfgPolicyBuffer_Object=MibTableColumn
bwmNewCfgPolicyBuffer=_BwmNewCfgPolicyBuffer_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,7),_BwmNewCfgPolicyBuffer_Type())
bwmNewCfgPolicyBuffer.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicyBuffer.setStatus(_A)
class _BwmNewCfgPolicyDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BwmNewCfgPolicyDelete_Type.__name__=_C
_BwmNewCfgPolicyDelete_Object=MibTableColumn
bwmNewCfgPolicyDelete=_BwmNewCfgPolicyDelete_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,8),_BwmNewCfgPolicyDelete_Type())
bwmNewCfgPolicyDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicyDelete.setStatus(_A)
class _BwmNewCfgPolicyUserLimit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BwmNewCfgPolicyUserLimit_Type.__name__=_E
_BwmNewCfgPolicyUserLimit_Object=MibTableColumn
bwmNewCfgPolicyUserLimit=_BwmNewCfgPolicyUserLimit_Object((1,3,6,1,4,1,1872,2,5,6,1,2,3,1,9),_BwmNewCfgPolicyUserLimit_Type())
bwmNewCfgPolicyUserLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgPolicyUserLimit.setStatus(_A)
_BwmContractConfig_ObjectIdentity=ObjectIdentity
bwmContractConfig=_BwmContractConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,1,3))
_BwmContractTableMaxEnt_Type=Integer32
_BwmContractTableMaxEnt_Object=MibScalar
bwmContractTableMaxEnt=_BwmContractTableMaxEnt_Object((1,3,6,1,4,1,1872,2,5,6,1,3,1),_BwmContractTableMaxEnt_Type())
bwmContractTableMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmContractTableMaxEnt.setStatus(_A)
_BwmCurCfgContractTable_Object=MibTable
bwmCurCfgContractTable=_BwmCurCfgContractTable_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2))
if mibBuilder.loadTexts:bwmCurCfgContractTable.setStatus(_A)
_BwmCurCfgContractTableEntry_Object=MibTableRow
bwmCurCfgContractTableEntry=_BwmCurCfgContractTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1))
bwmCurCfgContractTableEntry.setIndexNames((0,_H,_N))
if mibBuilder.loadTexts:bwmCurCfgContractTableEntry.setStatus(_A)
_BwmCurCfgContractIndx_Type=Integer32
_BwmCurCfgContractIndx_Object=MibTableColumn
bwmCurCfgContractIndx=_BwmCurCfgContractIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,1),_BwmCurCfgContractIndx_Type())
bwmCurCfgContractIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractIndx.setStatus(_A)
class _BwmCurCfgContractName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BwmCurCfgContractName_Type.__name__=_E
_BwmCurCfgContractName_Object=MibTableColumn
bwmCurCfgContractName=_BwmCurCfgContractName_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,2),_BwmCurCfgContractName_Type())
bwmCurCfgContractName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractName.setStatus(_A)
class _BwmCurCfgContractState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmCurCfgContractState_Type.__name__=_C
_BwmCurCfgContractState_Object=MibTableColumn
bwmCurCfgContractState=_BwmCurCfgContractState_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,3),_BwmCurCfgContractState_Type())
bwmCurCfgContractState.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractState.setStatus(_A)
_BwmCurCfgContractPolicy_Type=Integer32
_BwmCurCfgContractPolicy_Object=MibTableColumn
bwmCurCfgContractPolicy=_BwmCurCfgContractPolicy_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,4),_BwmCurCfgContractPolicy_Type())
bwmCurCfgContractPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractPolicy.setStatus(_A)
class _BwmCurCfgContractPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BwmCurCfgContractPrec_Type.__name__=_C
_BwmCurCfgContractPrec_Object=MibTableColumn
bwmCurCfgContractPrec=_BwmCurCfgContractPrec_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,5),_BwmCurCfgContractPrec_Type())
bwmCurCfgContractPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractPrec.setStatus(_A)
class _BwmCurCfgContractUseTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmCurCfgContractUseTos_Type.__name__=_C
_BwmCurCfgContractUseTos_Object=MibTableColumn
bwmCurCfgContractUseTos=_BwmCurCfgContractUseTos_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,6),_BwmCurCfgContractUseTos_Type())
bwmCurCfgContractUseTos.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractUseTos.setStatus(_A)
class _BwmCurCfgContractHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmCurCfgContractHistory_Type.__name__=_C
_BwmCurCfgContractHistory_Object=MibTableColumn
bwmCurCfgContractHistory=_BwmCurCfgContractHistory_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,7),_BwmCurCfgContractHistory_Type())
bwmCurCfgContractHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractHistory.setStatus(_A)
class _BwmCurCfgContractShaping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BwmCurCfgContractShaping_Type.__name__=_C
_BwmCurCfgContractShaping_Object=MibTableColumn
bwmCurCfgContractShaping=_BwmCurCfgContractShaping_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,8),_BwmCurCfgContractShaping_Type())
bwmCurCfgContractShaping.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractShaping.setStatus(_A)
class _BwmCurCfgContractResizeTcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmCurCfgContractResizeTcp_Type.__name__=_C
_BwmCurCfgContractResizeTcp_Object=MibTableColumn
bwmCurCfgContractResizeTcp=_BwmCurCfgContractResizeTcp_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,9),_BwmCurCfgContractResizeTcp_Type())
bwmCurCfgContractResizeTcp.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractResizeTcp.setStatus(_A)
class _BwmCurCfgContractIpLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmCurCfgContractIpLimit_Type.__name__=_C
_BwmCurCfgContractIpLimit_Object=MibTableColumn
bwmCurCfgContractIpLimit=_BwmCurCfgContractIpLimit_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,10),_BwmCurCfgContractIpLimit_Type())
bwmCurCfgContractIpLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractIpLimit.setStatus(_A)
class _BwmCurCfgContractIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sip',1),('dip',2)))
_BwmCurCfgContractIpType_Type.__name__=_C
_BwmCurCfgContractIpType_Object=MibTableColumn
bwmCurCfgContractIpType=_BwmCurCfgContractIpType_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,11),_BwmCurCfgContractIpType_Type())
bwmCurCfgContractIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractIpType.setStatus(_A)
class _BwmCurCfgContractMonitorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BwmCurCfgContractMonitorMode_Type.__name__=_C
_BwmCurCfgContractMonitorMode_Object=MibTableColumn
bwmCurCfgContractMonitorMode=_BwmCurCfgContractMonitorMode_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,12),_BwmCurCfgContractMonitorMode_Type())
bwmCurCfgContractMonitorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractMonitorMode.setStatus(_A)
_BwmCurCfgContractGroup_Type=Integer32
_BwmCurCfgContractGroup_Object=MibTableColumn
bwmCurCfgContractGroup=_BwmCurCfgContractGroup_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,13),_BwmCurCfgContractGroup_Type())
bwmCurCfgContractGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractGroup.setStatus(_A)
class _BwmCurCfgContractMaxSess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_BwmCurCfgContractMaxSess_Type.__name__=_C
_BwmCurCfgContractMaxSess_Object=MibTableColumn
bwmCurCfgContractMaxSess=_BwmCurCfgContractMaxSess_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,15),_BwmCurCfgContractMaxSess_Type())
bwmCurCfgContractMaxSess.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractMaxSess.setStatus(_A)
class _BwmCurCfgContractRowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_BwmCurCfgContractRowType_Type.__name__=_C
_BwmCurCfgContractRowType_Object=MibTableColumn
bwmCurCfgContractRowType=_BwmCurCfgContractRowType_Object((1,3,6,1,4,1,1872,2,5,6,1,3,2,1,16),_BwmCurCfgContractRowType_Type())
bwmCurCfgContractRowType.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractRowType.setStatus(_A)
_BwmNewCfgContractTable_Object=MibTable
bwmNewCfgContractTable=_BwmNewCfgContractTable_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3))
if mibBuilder.loadTexts:bwmNewCfgContractTable.setStatus(_A)
_BwmNewCfgContractTableEntry_Object=MibTableRow
bwmNewCfgContractTableEntry=_BwmNewCfgContractTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1))
bwmNewCfgContractTableEntry.setIndexNames((0,_H,_Q))
if mibBuilder.loadTexts:bwmNewCfgContractTableEntry.setStatus(_A)
_BwmNewCfgContractIndx_Type=Integer32
_BwmNewCfgContractIndx_Object=MibTableColumn
bwmNewCfgContractIndx=_BwmNewCfgContractIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,1),_BwmNewCfgContractIndx_Type())
bwmNewCfgContractIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgContractIndx.setStatus(_A)
class _BwmNewCfgContractName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BwmNewCfgContractName_Type.__name__=_E
_BwmNewCfgContractName_Object=MibTableColumn
bwmNewCfgContractName=_BwmNewCfgContractName_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,2),_BwmNewCfgContractName_Type())
bwmNewCfgContractName.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractName.setStatus(_A)
class _BwmNewCfgContractState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmNewCfgContractState_Type.__name__=_C
_BwmNewCfgContractState_Object=MibTableColumn
bwmNewCfgContractState=_BwmNewCfgContractState_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,3),_BwmNewCfgContractState_Type())
bwmNewCfgContractState.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractState.setStatus(_A)
_BwmNewCfgContractPolicy_Type=Integer32
_BwmNewCfgContractPolicy_Object=MibTableColumn
bwmNewCfgContractPolicy=_BwmNewCfgContractPolicy_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,4),_BwmNewCfgContractPolicy_Type())
bwmNewCfgContractPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractPolicy.setStatus(_A)
class _BwmNewCfgContractDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BwmNewCfgContractDelete_Type.__name__=_C
_BwmNewCfgContractDelete_Object=MibTableColumn
bwmNewCfgContractDelete=_BwmNewCfgContractDelete_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,5),_BwmNewCfgContractDelete_Type())
bwmNewCfgContractDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractDelete.setStatus(_A)
class _BwmNewCfgContractPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BwmNewCfgContractPrec_Type.__name__=_C
_BwmNewCfgContractPrec_Object=MibTableColumn
bwmNewCfgContractPrec=_BwmNewCfgContractPrec_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,6),_BwmNewCfgContractPrec_Type())
bwmNewCfgContractPrec.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractPrec.setStatus(_A)
class _BwmNewCfgContractUseTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmNewCfgContractUseTos_Type.__name__=_C
_BwmNewCfgContractUseTos_Object=MibTableColumn
bwmNewCfgContractUseTos=_BwmNewCfgContractUseTos_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,7),_BwmNewCfgContractUseTos_Type())
bwmNewCfgContractUseTos.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractUseTos.setStatus(_A)
class _BwmNewCfgContractHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmNewCfgContractHistory_Type.__name__=_C
_BwmNewCfgContractHistory_Object=MibTableColumn
bwmNewCfgContractHistory=_BwmNewCfgContractHistory_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,8),_BwmNewCfgContractHistory_Type())
bwmNewCfgContractHistory.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractHistory.setStatus(_A)
class _BwmNewCfgContractShaping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BwmNewCfgContractShaping_Type.__name__=_C
_BwmNewCfgContractShaping_Object=MibTableColumn
bwmNewCfgContractShaping=_BwmNewCfgContractShaping_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,9),_BwmNewCfgContractShaping_Type())
bwmNewCfgContractShaping.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractShaping.setStatus(_A)
class _BwmNewCfgContractResizeTcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmNewCfgContractResizeTcp_Type.__name__=_C
_BwmNewCfgContractResizeTcp_Object=MibTableColumn
bwmNewCfgContractResizeTcp=_BwmNewCfgContractResizeTcp_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,10),_BwmNewCfgContractResizeTcp_Type())
bwmNewCfgContractResizeTcp.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractResizeTcp.setStatus(_A)
class _BwmNewCfgContractIpLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_BwmNewCfgContractIpLimit_Type.__name__=_C
_BwmNewCfgContractIpLimit_Object=MibTableColumn
bwmNewCfgContractIpLimit=_BwmNewCfgContractIpLimit_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,11),_BwmNewCfgContractIpLimit_Type())
bwmNewCfgContractIpLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractIpLimit.setStatus(_A)
class _BwmNewCfgContractIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sip',1),('dip',2)))
_BwmNewCfgContractIpType_Type.__name__=_C
_BwmNewCfgContractIpType_Object=MibTableColumn
bwmNewCfgContractIpType=_BwmNewCfgContractIpType_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,12),_BwmNewCfgContractIpType_Type())
bwmNewCfgContractIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractIpType.setStatus(_A)
class _BwmNewCfgContractMonitorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BwmNewCfgContractMonitorMode_Type.__name__=_C
_BwmNewCfgContractMonitorMode_Object=MibTableColumn
bwmNewCfgContractMonitorMode=_BwmNewCfgContractMonitorMode_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,13),_BwmNewCfgContractMonitorMode_Type())
bwmNewCfgContractMonitorMode.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractMonitorMode.setStatus(_A)
_BwmNewCfgContractGroup_Type=Integer32
_BwmNewCfgContractGroup_Object=MibTableColumn
bwmNewCfgContractGroup=_BwmNewCfgContractGroup_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,14),_BwmNewCfgContractGroup_Type())
bwmNewCfgContractGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgContractGroup.setStatus(_A)
class _BwmNewCfgContractMaxSess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_BwmNewCfgContractMaxSess_Type.__name__=_C
_BwmNewCfgContractMaxSess_Object=MibTableColumn
bwmNewCfgContractMaxSess=_BwmNewCfgContractMaxSess_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,16),_BwmNewCfgContractMaxSess_Type())
bwmNewCfgContractMaxSess.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractMaxSess.setStatus(_A)
class _BwmNewCfgContractRowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_BwmNewCfgContractRowType_Type.__name__=_C
_BwmNewCfgContractRowType_Object=MibTableColumn
bwmNewCfgContractRowType=_BwmNewCfgContractRowType_Object((1,3,6,1,4,1,1872,2,5,6,1,3,3,1,17),_BwmNewCfgContractRowType_Type())
bwmNewCfgContractRowType.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgContractRowType.setStatus(_A)
_BwmAvailableContractsTable_Object=MibTable
bwmAvailableContractsTable=_BwmAvailableContractsTable_Object((1,3,6,1,4,1,1872,2,5,6,1,3,4))
if mibBuilder.loadTexts:bwmAvailableContractsTable.setStatus(_A)
_BwmAvailableContractsTableEntry_Object=MibTableRow
bwmAvailableContractsTableEntry=_BwmAvailableContractsTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,3,4,1))
bwmAvailableContractsTableEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:bwmAvailableContractsTableEntry.setStatus(_A)
_BwmContractIndx_Type=Integer32
_BwmContractIndx_Object=MibTableColumn
bwmContractIndx=_BwmContractIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,3,4,1,1),_BwmContractIndx_Type())
bwmContractIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmContractIndx.setStatus(_A)
class _BwmContractName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BwmContractName_Type.__name__=_E
_BwmContractName_Object=MibTableColumn
bwmContractName=_BwmContractName_Object((1,3,6,1,4,1,1872,2,5,6,1,3,4,1,2),_BwmContractName_Type())
bwmContractName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmContractName.setStatus(_A)
_BwmContTimePolicyConfig_ObjectIdentity=ObjectIdentity
bwmContTimePolicyConfig=_BwmContTimePolicyConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,1,4))
_BwmContTimePolicyTableMaxEnt_Type=Integer32
_BwmContTimePolicyTableMaxEnt_Object=MibScalar
bwmContTimePolicyTableMaxEnt=_BwmContTimePolicyTableMaxEnt_Object((1,3,6,1,4,1,1872,2,5,6,1,4,1),_BwmContTimePolicyTableMaxEnt_Type())
bwmContTimePolicyTableMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmContTimePolicyTableMaxEnt.setStatus(_A)
_BwmCurCfgContTimePolicyTable_Object=MibTable
bwmCurCfgContTimePolicyTable=_BwmCurCfgContTimePolicyTable_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2))
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyTable.setStatus(_A)
_BwmCurCfgContTimePolicyTableEntry_Object=MibTableRow
bwmCurCfgContTimePolicyTableEntry=_BwmCurCfgContTimePolicyTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1))
bwmCurCfgContTimePolicyTableEntry.setIndexNames((0,_H,_S),(0,_H,_T))
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyTableEntry.setStatus(_A)
_BwmCurCfgContTimePolicyContIndx_Type=Integer32
_BwmCurCfgContTimePolicyContIndx_Object=MibTableColumn
bwmCurCfgContTimePolicyContIndx=_BwmCurCfgContTimePolicyContIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1,1),_BwmCurCfgContTimePolicyContIndx_Type())
bwmCurCfgContTimePolicyContIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyContIndx.setStatus(_A)
_BwmCurCfgContTimePolicyIndx_Type=Integer32
_BwmCurCfgContTimePolicyIndx_Object=MibTableColumn
bwmCurCfgContTimePolicyIndx=_BwmCurCfgContTimePolicyIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1,2),_BwmCurCfgContTimePolicyIndx_Type())
bwmCurCfgContTimePolicyIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyIndx.setStatus(_A)
class _BwmCurCfgContTimePolicyDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,8),(_c,9),(_d,10)))
_BwmCurCfgContTimePolicyDay_Type.__name__=_C
_BwmCurCfgContTimePolicyDay_Object=MibTableColumn
bwmCurCfgContTimePolicyDay=_BwmCurCfgContTimePolicyDay_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1,3),_BwmCurCfgContTimePolicyDay_Type())
bwmCurCfgContTimePolicyDay.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyDay.setStatus(_A)
class _BwmCurCfgContTimePolicyFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_BwmCurCfgContTimePolicyFrom_Type.__name__=_C
_BwmCurCfgContTimePolicyFrom_Object=MibTableColumn
bwmCurCfgContTimePolicyFrom=_BwmCurCfgContTimePolicyFrom_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1,4),_BwmCurCfgContTimePolicyFrom_Type())
bwmCurCfgContTimePolicyFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyFrom.setStatus(_A)
class _BwmCurCfgContTimePolicyTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_BwmCurCfgContTimePolicyTo_Type.__name__=_C
_BwmCurCfgContTimePolicyTo_Object=MibTableColumn
bwmCurCfgContTimePolicyTo=_BwmCurCfgContTimePolicyTo_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1,5),_BwmCurCfgContTimePolicyTo_Type())
bwmCurCfgContTimePolicyTo.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyTo.setStatus(_A)
_BwmCurCfgContTimePolicyPol_Type=Integer32
_BwmCurCfgContTimePolicyPol_Object=MibTableColumn
bwmCurCfgContTimePolicyPol=_BwmCurCfgContTimePolicyPol_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1,6),_BwmCurCfgContTimePolicyPol_Type())
bwmCurCfgContTimePolicyPol.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyPol.setStatus(_A)
class _BwmCurCfgContTimePolicyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BwmCurCfgContTimePolicyState_Type.__name__=_C
_BwmCurCfgContTimePolicyState_Object=MibTableColumn
bwmCurCfgContTimePolicyState=_BwmCurCfgContTimePolicyState_Object((1,3,6,1,4,1,1872,2,5,6,1,4,2,1,7),_BwmCurCfgContTimePolicyState_Type())
bwmCurCfgContTimePolicyState.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContTimePolicyState.setStatus(_A)
_BwmNewCfgContTimePolicyTable_Object=MibTable
bwmNewCfgContTimePolicyTable=_BwmNewCfgContTimePolicyTable_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3))
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyTable.setStatus(_A)
_BwmNewCfgContTimePolicyTableEntry_Object=MibTableRow
bwmNewCfgContTimePolicyTableEntry=_BwmNewCfgContTimePolicyTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1))
bwmNewCfgContTimePolicyTableEntry.setIndexNames((0,_H,_e),(0,_H,_f))
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyTableEntry.setStatus(_A)
_BwmNewCfgContTimePolicyContIndx_Type=Integer32
_BwmNewCfgContTimePolicyContIndx_Object=MibTableColumn
bwmNewCfgContTimePolicyContIndx=_BwmNewCfgContTimePolicyContIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,1),_BwmNewCfgContTimePolicyContIndx_Type())
bwmNewCfgContTimePolicyContIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyContIndx.setStatus(_A)
_BwmNewCfgContTimePolicyIndx_Type=Integer32
_BwmNewCfgContTimePolicyIndx_Object=MibTableColumn
bwmNewCfgContTimePolicyIndx=_BwmNewCfgContTimePolicyIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,2),_BwmNewCfgContTimePolicyIndx_Type())
bwmNewCfgContTimePolicyIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyIndx.setStatus(_A)
class _BwmNewCfgContTimePolicyDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,8),(_c,9),(_d,10)))
_BwmNewCfgContTimePolicyDay_Type.__name__=_C
_BwmNewCfgContTimePolicyDay_Object=MibTableColumn
bwmNewCfgContTimePolicyDay=_BwmNewCfgContTimePolicyDay_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,3),_BwmNewCfgContTimePolicyDay_Type())
bwmNewCfgContTimePolicyDay.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyDay.setStatus(_A)
class _BwmNewCfgContTimePolicyFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_BwmNewCfgContTimePolicyFrom_Type.__name__=_C
_BwmNewCfgContTimePolicyFrom_Object=MibTableColumn
bwmNewCfgContTimePolicyFrom=_BwmNewCfgContTimePolicyFrom_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,4),_BwmNewCfgContTimePolicyFrom_Type())
bwmNewCfgContTimePolicyFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyFrom.setStatus(_A)
class _BwmNewCfgContTimePolicyTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_BwmNewCfgContTimePolicyTo_Type.__name__=_C
_BwmNewCfgContTimePolicyTo_Object=MibTableColumn
bwmNewCfgContTimePolicyTo=_BwmNewCfgContTimePolicyTo_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,5),_BwmNewCfgContTimePolicyTo_Type())
bwmNewCfgContTimePolicyTo.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyTo.setStatus(_A)
_BwmNewCfgContTimePolicyPol_Type=Integer32
_BwmNewCfgContTimePolicyPol_Object=MibTableColumn
bwmNewCfgContTimePolicyPol=_BwmNewCfgContTimePolicyPol_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,6),_BwmNewCfgContTimePolicyPol_Type())
bwmNewCfgContTimePolicyPol.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyPol.setStatus(_A)
class _BwmNewCfgContTimePolicyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BwmNewCfgContTimePolicyState_Type.__name__=_C
_BwmNewCfgContTimePolicyState_Object=MibTableColumn
bwmNewCfgContTimePolicyState=_BwmNewCfgContTimePolicyState_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,7),_BwmNewCfgContTimePolicyState_Type())
bwmNewCfgContTimePolicyState.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyState.setStatus(_A)
class _BwmNewCfgContTimePolicyDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BwmNewCfgContTimePolicyDelete_Type.__name__=_C
_BwmNewCfgContTimePolicyDelete_Object=MibTableColumn
bwmNewCfgContTimePolicyDelete=_BwmNewCfgContTimePolicyDelete_Object((1,3,6,1,4,1,1872,2,5,6,1,4,3,1,8),_BwmNewCfgContTimePolicyDelete_Type())
bwmNewCfgContTimePolicyDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContTimePolicyDelete.setStatus(_A)
_BwmContractGroupConfig_ObjectIdentity=ObjectIdentity
bwmContractGroupConfig=_BwmContractGroupConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,1,5))
_BwmContractGroupTableMaxEnt_Type=Integer32
_BwmContractGroupTableMaxEnt_Object=MibScalar
bwmContractGroupTableMaxEnt=_BwmContractGroupTableMaxEnt_Object((1,3,6,1,4,1,1872,2,5,6,1,5,1),_BwmContractGroupTableMaxEnt_Type())
bwmContractGroupTableMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmContractGroupTableMaxEnt.setStatus(_A)
_BwmCurCfgContractGroupTable_Object=MibTable
bwmCurCfgContractGroupTable=_BwmCurCfgContractGroupTable_Object((1,3,6,1,4,1,1872,2,5,6,1,5,2))
if mibBuilder.loadTexts:bwmCurCfgContractGroupTable.setStatus(_A)
_BwmCurCfgContractGroupTableEntry_Object=MibTableRow
bwmCurCfgContractGroupTableEntry=_BwmCurCfgContractGroupTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,5,2,1))
bwmCurCfgContractGroupTableEntry.setIndexNames((0,_H,_g))
if mibBuilder.loadTexts:bwmCurCfgContractGroupTableEntry.setStatus(_A)
_BwmCurCfgContractGroupIndx_Type=Integer32
_BwmCurCfgContractGroupIndx_Object=MibTableColumn
bwmCurCfgContractGroupIndx=_BwmCurCfgContractGroupIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,5,2,1,1),_BwmCurCfgContractGroupIndx_Type())
bwmCurCfgContractGroupIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractGroupIndx.setStatus(_A)
_BwmCurCfgContractGroupContracts_Type=OctetString
_BwmCurCfgContractGroupContracts_Object=MibTableColumn
bwmCurCfgContractGroupContracts=_BwmCurCfgContractGroupContracts_Object((1,3,6,1,4,1,1872,2,5,6,1,5,2,1,2),_BwmCurCfgContractGroupContracts_Type())
bwmCurCfgContractGroupContracts.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractGroupContracts.setStatus(_A)
class _BwmCurCfgContractGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BwmCurCfgContractGroupName_Type.__name__=_E
_BwmCurCfgContractGroupName_Object=MibTableColumn
bwmCurCfgContractGroupName=_BwmCurCfgContractGroupName_Object((1,3,6,1,4,1,1872,2,5,6,1,5,2,1,3),_BwmCurCfgContractGroupName_Type())
bwmCurCfgContractGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmCurCfgContractGroupName.setStatus(_A)
_BwmNewCfgContractGroupTable_Object=MibTable
bwmNewCfgContractGroupTable=_BwmNewCfgContractGroupTable_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3))
if mibBuilder.loadTexts:bwmNewCfgContractGroupTable.setStatus(_A)
_BwmNewCfgContractGroupTableEntry_Object=MibTableRow
bwmNewCfgContractGroupTableEntry=_BwmNewCfgContractGroupTableEntry_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3,1))
bwmNewCfgContractGroupTableEntry.setIndexNames((0,_H,_h))
if mibBuilder.loadTexts:bwmNewCfgContractGroupTableEntry.setStatus(_A)
_BwmNewCfgContractGroupIndx_Type=Integer32
_BwmNewCfgContractGroupIndx_Object=MibTableColumn
bwmNewCfgContractGroupIndx=_BwmNewCfgContractGroupIndx_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3,1,1),_BwmNewCfgContractGroupIndx_Type())
bwmNewCfgContractGroupIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgContractGroupIndx.setStatus(_A)
_BwmNewCfgContractGroupContracts_Type=OctetString
_BwmNewCfgContractGroupContracts_Object=MibTableColumn
bwmNewCfgContractGroupContracts=_BwmNewCfgContractGroupContracts_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3,1,2),_BwmNewCfgContractGroupContracts_Type())
bwmNewCfgContractGroupContracts.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmNewCfgContractGroupContracts.setStatus(_A)
_BwmNewCfgContractGroupAddCont_Type=Integer32
_BwmNewCfgContractGroupAddCont_Object=MibTableColumn
bwmNewCfgContractGroupAddCont=_BwmNewCfgContractGroupAddCont_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3,1,3),_BwmNewCfgContractGroupAddCont_Type())
bwmNewCfgContractGroupAddCont.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractGroupAddCont.setStatus(_A)
_BwmNewCfgContractGroupRemCont_Type=Integer32
_BwmNewCfgContractGroupRemCont_Object=MibTableColumn
bwmNewCfgContractGroupRemCont=_BwmNewCfgContractGroupRemCont_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3,1,4),_BwmNewCfgContractGroupRemCont_Type())
bwmNewCfgContractGroupRemCont.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractGroupRemCont.setStatus(_A)
class _BwmNewCfgContractGroupDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BwmNewCfgContractGroupDelete_Type.__name__=_C
_BwmNewCfgContractGroupDelete_Object=MibTableColumn
bwmNewCfgContractGroupDelete=_BwmNewCfgContractGroupDelete_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3,1,5),_BwmNewCfgContractGroupDelete_Type())
bwmNewCfgContractGroupDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractGroupDelete.setStatus(_A)
class _BwmNewCfgContractGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BwmNewCfgContractGroupName_Type.__name__=_E
_BwmNewCfgContractGroupName_Object=MibTableColumn
bwmNewCfgContractGroupName=_BwmNewCfgContractGroupName_Object((1,3,6,1,4,1,1872,2,5,6,1,5,3,1,6),_BwmNewCfgContractGroupName_Type())
bwmNewCfgContractGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:bwmNewCfgContractGroupName.setStatus(_A)
_BwmContractGroupTableMaxCont_Type=Integer32
_BwmContractGroupTableMaxCont_Object=MibScalar
bwmContractGroupTableMaxCont=_BwmContractGroupTableMaxCont_Object((1,3,6,1,4,1,1872,2,5,6,1,5,4),_BwmContractGroupTableMaxCont_Type())
bwmContractGroupTableMaxCont.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmContractGroupTableMaxCont.setStatus(_A)
_BwmStats_ObjectIdentity=ObjectIdentity
bwmStats=_BwmStats_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,2))
_BwmStatTcTable_Object=MibTable
bwmStatTcTable=_BwmStatTcTable_Object((1,3,6,1,4,1,1872,2,5,6,2,1))
if mibBuilder.loadTexts:bwmStatTcTable.setStatus(_A)
_BwmStatTcEntry_Object=MibTableRow
bwmStatTcEntry=_BwmStatTcEntry_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1))
bwmStatTcEntry.setIndexNames((0,_H,_i))
if mibBuilder.loadTexts:bwmStatTcEntry.setStatus(_A)
_BwmStatTcContractIndex_Type=Integer32
_BwmStatTcContractIndex_Object=MibTableColumn
bwmStatTcContractIndex=_BwmStatTcContractIndex_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,1),_BwmStatTcContractIndex_Type())
bwmStatTcContractIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcContractIndex.setStatus(_A)
class _BwmStatTcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BwmStatTcName_Type.__name__=_E
_BwmStatTcName_Object=MibTableColumn
bwmStatTcName=_BwmStatTcName_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,2),_BwmStatTcName_Type())
bwmStatTcName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcName.setStatus(_A)
_BwmStatTcOutoct_Type=Counter32
_BwmStatTcOutoct_Object=MibTableColumn
bwmStatTcOutoct=_BwmStatTcOutoct_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,3),_BwmStatTcOutoct_Type())
bwmStatTcOutoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcOutoct.setStatus(_A)
_BwmStatTcOutdisoct_Type=Counter32
_BwmStatTcOutdisoct_Object=MibTableColumn
bwmStatTcOutdisoct=_BwmStatTcOutdisoct_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,4),_BwmStatTcOutdisoct_Type())
bwmStatTcOutdisoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcOutdisoct.setStatus(_A)
_BwmStatTcBufferUsed_Type=Integer32
_BwmStatTcBufferUsed_Object=MibTableColumn
bwmStatTcBufferUsed=_BwmStatTcBufferUsed_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,5),_BwmStatTcBufferUsed_Type())
bwmStatTcBufferUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcBufferUsed.setStatus(_A)
_BwmStatTcBufferMax_Type=Counter32
_BwmStatTcBufferMax_Object=MibTableColumn
bwmStatTcBufferMax=_BwmStatTcBufferMax_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,6),_BwmStatTcBufferMax_Type())
bwmStatTcBufferMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcBufferMax.setStatus(_A)
_BwmStatTcTotalPackets_Type=Counter32
_BwmStatTcTotalPackets_Object=MibTableColumn
bwmStatTcTotalPackets=_BwmStatTcTotalPackets_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,7),_BwmStatTcTotalPackets_Type())
bwmStatTcTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcTotalPackets.setStatus(_A)
_BwmStatTcSessRejected_Type=Counter32
_BwmStatTcSessRejected_Object=MibTableColumn
bwmStatTcSessRejected=_BwmStatTcSessRejected_Object((1,3,6,1,4,1,1872,2,5,6,2,1,1,8),_BwmStatTcSessRejected_Type())
bwmStatTcSessRejected.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcSessRejected.setStatus(_A)
_BwmStatTcrTable_Object=MibTable
bwmStatTcrTable=_BwmStatTcrTable_Object((1,3,6,1,4,1,1872,2,5,6,2,2))
if mibBuilder.loadTexts:bwmStatTcrTable.setStatus(_A)
_BwmStatTcrEntry_Object=MibTableRow
bwmStatTcrEntry=_BwmStatTcrEntry_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1))
bwmStatTcrEntry.setIndexNames((0,_H,_j))
if mibBuilder.loadTexts:bwmStatTcrEntry.setStatus(_A)
_BwmStatTcrContractIndex_Type=Integer32
_BwmStatTcrContractIndex_Object=MibTableColumn
bwmStatTcrContractIndex=_BwmStatTcrContractIndex_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,1),_BwmStatTcrContractIndex_Type())
bwmStatTcrContractIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrContractIndex.setStatus(_A)
class _BwmStatTcrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BwmStatTcrName_Type.__name__=_E
_BwmStatTcrName_Object=MibTableColumn
bwmStatTcrName=_BwmStatTcrName_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,2),_BwmStatTcrName_Type())
bwmStatTcrName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrName.setStatus(_A)
_BwmStatTcrRate_Type=Integer32
_BwmStatTcrRate_Object=MibTableColumn
bwmStatTcrRate=_BwmStatTcrRate_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,3),_BwmStatTcrRate_Type())
bwmStatTcrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrRate.setStatus(_A)
_BwmStatTcrOutoct_Type=Counter32
_BwmStatTcrOutoct_Object=MibTableColumn
bwmStatTcrOutoct=_BwmStatTcrOutoct_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,4),_BwmStatTcrOutoct_Type())
bwmStatTcrOutoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrOutoct.setStatus(_A)
_BwmStatTcrOutdisoct_Type=Counter32
_BwmStatTcrOutdisoct_Object=MibTableColumn
bwmStatTcrOutdisoct=_BwmStatTcrOutdisoct_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,5),_BwmStatTcrOutdisoct_Type())
bwmStatTcrOutdisoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrOutdisoct.setStatus(_A)
_BwmStatTcrBufferUsed_Type=Integer32
_BwmStatTcrBufferUsed_Object=MibTableColumn
bwmStatTcrBufferUsed=_BwmStatTcrBufferUsed_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,6),_BwmStatTcrBufferUsed_Type())
bwmStatTcrBufferUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrBufferUsed.setStatus(_A)
_BwmStatTcrBufferMax_Type=Counter32
_BwmStatTcrBufferMax_Object=MibTableColumn
bwmStatTcrBufferMax=_BwmStatTcrBufferMax_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,7),_BwmStatTcrBufferMax_Type())
bwmStatTcrBufferMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrBufferMax.setStatus(_A)
_BwmStatTcrTotalPackets_Type=Counter32
_BwmStatTcrTotalPackets_Object=MibTableColumn
bwmStatTcrTotalPackets=_BwmStatTcrTotalPackets_Object((1,3,6,1,4,1,1872,2,5,6,2,2,1,8),_BwmStatTcrTotalPackets_Type())
bwmStatTcrTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatTcrTotalPackets.setStatus(_A)
_BwmStatPortTcTable_Object=MibTable
bwmStatPortTcTable=_BwmStatPortTcTable_Object((1,3,6,1,4,1,1872,2,5,6,2,3))
if mibBuilder.loadTexts:bwmStatPortTcTable.setStatus(_A)
_BwmStatPortTcEntry_Object=MibTableRow
bwmStatPortTcEntry=_BwmStatPortTcEntry_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1))
bwmStatPortTcEntry.setIndexNames((0,_H,_k),(0,_H,_l))
if mibBuilder.loadTexts:bwmStatPortTcEntry.setStatus(_A)
_BwmStatPortTcPortIndex_Type=Integer32
_BwmStatPortTcPortIndex_Object=MibTableColumn
bwmStatPortTcPortIndex=_BwmStatPortTcPortIndex_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,1),_BwmStatPortTcPortIndex_Type())
bwmStatPortTcPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcPortIndex.setStatus(_A)
_BwmStatPortTcContractIndex_Type=Integer32
_BwmStatPortTcContractIndex_Object=MibTableColumn
bwmStatPortTcContractIndex=_BwmStatPortTcContractIndex_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,2),_BwmStatPortTcContractIndex_Type())
bwmStatPortTcContractIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcContractIndex.setStatus(_A)
class _BwmStatPortTcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BwmStatPortTcName_Type.__name__=_E
_BwmStatPortTcName_Object=MibTableColumn
bwmStatPortTcName=_BwmStatPortTcName_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,3),_BwmStatPortTcName_Type())
bwmStatPortTcName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcName.setStatus(_A)
_BwmStatPortTcOutoct_Type=Counter32
_BwmStatPortTcOutoct_Object=MibTableColumn
bwmStatPortTcOutoct=_BwmStatPortTcOutoct_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,4),_BwmStatPortTcOutoct_Type())
bwmStatPortTcOutoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcOutoct.setStatus(_A)
_BwmStatPortTcOutdisoct_Type=Counter32
_BwmStatPortTcOutdisoct_Object=MibTableColumn
bwmStatPortTcOutdisoct=_BwmStatPortTcOutdisoct_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,5),_BwmStatPortTcOutdisoct_Type())
bwmStatPortTcOutdisoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcOutdisoct.setStatus(_A)
_BwmStatPortTcBufferUsed_Type=Integer32
_BwmStatPortTcBufferUsed_Object=MibTableColumn
bwmStatPortTcBufferUsed=_BwmStatPortTcBufferUsed_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,6),_BwmStatPortTcBufferUsed_Type())
bwmStatPortTcBufferUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcBufferUsed.setStatus(_A)
_BwmStatPortTcBufferMax_Type=Counter32
_BwmStatPortTcBufferMax_Object=MibTableColumn
bwmStatPortTcBufferMax=_BwmStatPortTcBufferMax_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,7),_BwmStatPortTcBufferMax_Type())
bwmStatPortTcBufferMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcBufferMax.setStatus(_A)
_BwmStatPortTcTotalPackets_Type=Counter32
_BwmStatPortTcTotalPackets_Object=MibTableColumn
bwmStatPortTcTotalPackets=_BwmStatPortTcTotalPackets_Object((1,3,6,1,4,1,1872,2,5,6,2,3,1,8),_BwmStatPortTcTotalPackets_Type())
bwmStatPortTcTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcTotalPackets.setStatus(_A)
_BwmStatPortTcrTable_Object=MibTable
bwmStatPortTcrTable=_BwmStatPortTcrTable_Object((1,3,6,1,4,1,1872,2,5,6,2,4))
if mibBuilder.loadTexts:bwmStatPortTcrTable.setStatus(_A)
_BwmStatPortTcrEntry_Object=MibTableRow
bwmStatPortTcrEntry=_BwmStatPortTcrEntry_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1))
bwmStatPortTcrEntry.setIndexNames((0,_H,_m),(0,_H,_n))
if mibBuilder.loadTexts:bwmStatPortTcrEntry.setStatus(_A)
_BwmStatPortTcrPortIndex_Type=Integer32
_BwmStatPortTcrPortIndex_Object=MibTableColumn
bwmStatPortTcrPortIndex=_BwmStatPortTcrPortIndex_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,1),_BwmStatPortTcrPortIndex_Type())
bwmStatPortTcrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrPortIndex.setStatus(_A)
_BwmStatPortTcrContractIndex_Type=Integer32
_BwmStatPortTcrContractIndex_Object=MibTableColumn
bwmStatPortTcrContractIndex=_BwmStatPortTcrContractIndex_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,2),_BwmStatPortTcrContractIndex_Type())
bwmStatPortTcrContractIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrContractIndex.setStatus(_A)
class _BwmStatPortTcrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BwmStatPortTcrName_Type.__name__=_E
_BwmStatPortTcrName_Object=MibTableColumn
bwmStatPortTcrName=_BwmStatPortTcrName_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,3),_BwmStatPortTcrName_Type())
bwmStatPortTcrName.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrName.setStatus(_A)
_BwmStatPortTcrRate_Type=Integer32
_BwmStatPortTcrRate_Object=MibTableColumn
bwmStatPortTcrRate=_BwmStatPortTcrRate_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,4),_BwmStatPortTcrRate_Type())
bwmStatPortTcrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrRate.setStatus(_A)
_BwmStatPortTcrOutoct_Type=Counter32
_BwmStatPortTcrOutoct_Object=MibTableColumn
bwmStatPortTcrOutoct=_BwmStatPortTcrOutoct_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,5),_BwmStatPortTcrOutoct_Type())
bwmStatPortTcrOutoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrOutoct.setStatus(_A)
_BwmStatPortTcrOutdisoct_Type=Counter32
_BwmStatPortTcrOutdisoct_Object=MibTableColumn
bwmStatPortTcrOutdisoct=_BwmStatPortTcrOutdisoct_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,6),_BwmStatPortTcrOutdisoct_Type())
bwmStatPortTcrOutdisoct.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrOutdisoct.setStatus(_A)
_BwmStatPortTcrBufferUsed_Type=Integer32
_BwmStatPortTcrBufferUsed_Object=MibTableColumn
bwmStatPortTcrBufferUsed=_BwmStatPortTcrBufferUsed_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,7),_BwmStatPortTcrBufferUsed_Type())
bwmStatPortTcrBufferUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrBufferUsed.setStatus(_A)
_BwmStatPortTcrBufferMax_Type=Counter32
_BwmStatPortTcrBufferMax_Object=MibTableColumn
bwmStatPortTcrBufferMax=_BwmStatPortTcrBufferMax_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,8),_BwmStatPortTcrBufferMax_Type())
bwmStatPortTcrBufferMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrBufferMax.setStatus(_A)
_BwmStatPortTcrTotalPackets_Type=Counter32
_BwmStatPortTcrTotalPackets_Object=MibTableColumn
bwmStatPortTcrTotalPackets=_BwmStatPortTcrTotalPackets_Object((1,3,6,1,4,1,1872,2,5,6,2,4,1,9),_BwmStatPortTcrTotalPackets_Type())
bwmStatPortTcrTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bwmStatPortTcrTotalPackets.setStatus(_A)
class _BwmStatsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('clear',2)))
_BwmStatsClear_Type.__name__=_C
_BwmStatsClear_Object=MibScalar
bwmStatsClear=_BwmStatsClear_Object((1,3,6,1,4,1,1872,2,5,6,2,5),_BwmStatsClear_Type())
bwmStatsClear.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmStatsClear.setStatus(_A)
_BwmOpers_ObjectIdentity=ObjectIdentity
bwmOpers=_BwmOpers_ObjectIdentity((1,3,6,1,4,1,1872,2,5,6,3))
class _BwmOperSendSMTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('send',2)))
_BwmOperSendSMTP_Type.__name__=_C
_BwmOperSendSMTP_Object=MibScalar
bwmOperSendSMTP=_BwmOperSendSMTP_Object((1,3,6,1,4,1,1872,2,5,6,3,1),_BwmOperSendSMTP_Type())
bwmOperSendSMTP.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmOperSendSMTP.setStatus(_A)
class _BwmOperClearUsrEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('clear',2)))
_BwmOperClearUsrEntry_Type.__name__=_C
_BwmOperClearUsrEntry_Object=MibScalar
bwmOperClearUsrEntry=_BwmOperClearUsrEntry_Object((1,3,6,1,4,1,1872,2,5,6,3,2),_BwmOperClearUsrEntry_Type())
bwmOperClearUsrEntry.setMaxAccess(_I)
if mibBuilder.loadTexts:bwmOperClearUsrEntry.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'bwm':bwm,'bwmConfigs':bwmConfigs,'bwmGeneralConfig':bwmGeneralConfig,'bwmCurCfgGenState':bwmCurCfgGenState,'bwmNewCfgGenState':bwmNewCfgGenState,'bwmCurCfgGenEnforcePolicy':bwmCurCfgGenEnforcePolicy,'bwmNewCfgGenEnforcePolicy':bwmNewCfgGenEnforcePolicy,'bwmCurCfgGenSmtpUser':bwmCurCfgGenSmtpUser,'bwmNewCfgGenSmtpUser':bwmNewCfgGenSmtpUser,'bwmCurCfgGenEmailFrequency':bwmCurCfgGenEmailFrequency,'bwmNewCfgGenEmailFrequency':bwmNewCfgGenEmailFrequency,'bwmCurCfgGenIPUserLimit':bwmCurCfgGenIPUserLimit,'bwmNewCfgGenIPUserLimit':bwmNewCfgGenIPUserLimit,'bwmCurCfgGenEmail':bwmCurCfgGenEmail,'bwmNewCfgGenEmail':bwmNewCfgGenEmail,'bwmCurCfgGenReport':bwmCurCfgGenReport,'bwmNewCfgGenReport':bwmNewCfgGenReport,'bwmCurCfgGenReportStr':bwmCurCfgGenReportStr,'bwmNewCfgGenReportStr':bwmNewCfgGenReportStr,'bwmPolicyConfig':bwmPolicyConfig,'bwmPolicyTableMaxEnt':bwmPolicyTableMaxEnt,'bwmCurCfgPolicyTable':bwmCurCfgPolicyTable,'bwmCurCfgPolicyTableEntry':bwmCurCfgPolicyTableEntry,_L:bwmCurCfgPolicyIndx,'bwmCurCfgPolicyTosIn':bwmCurCfgPolicyTosIn,'bwmCurCfgPolicyTosOut':bwmCurCfgPolicyTosOut,'bwmCurCfgPolicyHard':bwmCurCfgPolicyHard,'bwmCurCfgPolicySoft':bwmCurCfgPolicySoft,'bwmCurCfgPolicyResv':bwmCurCfgPolicyResv,'bwmCurCfgPolicyBuffer':bwmCurCfgPolicyBuffer,'bwmCurCfgPolicyUserLimit':bwmCurCfgPolicyUserLimit,'bwmNewCfgPolicyTable':bwmNewCfgPolicyTable,'bwmNewCfgPolicyTableEntry':bwmNewCfgPolicyTableEntry,_M:bwmNewCfgPolicyIndx,'bwmNewCfgPolicyTosIn':bwmNewCfgPolicyTosIn,'bwmNewCfgPolicyTosOut':bwmNewCfgPolicyTosOut,'bwmNewCfgPolicyHard':bwmNewCfgPolicyHard,'bwmNewCfgPolicySoft':bwmNewCfgPolicySoft,'bwmNewCfgPolicyResv':bwmNewCfgPolicyResv,'bwmNewCfgPolicyBuffer':bwmNewCfgPolicyBuffer,'bwmNewCfgPolicyDelete':bwmNewCfgPolicyDelete,'bwmNewCfgPolicyUserLimit':bwmNewCfgPolicyUserLimit,'bwmContractConfig':bwmContractConfig,'bwmContractTableMaxEnt':bwmContractTableMaxEnt,'bwmCurCfgContractTable':bwmCurCfgContractTable,'bwmCurCfgContractTableEntry':bwmCurCfgContractTableEntry,_N:bwmCurCfgContractIndx,'bwmCurCfgContractName':bwmCurCfgContractName,'bwmCurCfgContractState':bwmCurCfgContractState,'bwmCurCfgContractPolicy':bwmCurCfgContractPolicy,'bwmCurCfgContractPrec':bwmCurCfgContractPrec,'bwmCurCfgContractUseTos':bwmCurCfgContractUseTos,'bwmCurCfgContractHistory':bwmCurCfgContractHistory,'bwmCurCfgContractShaping':bwmCurCfgContractShaping,'bwmCurCfgContractResizeTcp':bwmCurCfgContractResizeTcp,'bwmCurCfgContractIpLimit':bwmCurCfgContractIpLimit,'bwmCurCfgContractIpType':bwmCurCfgContractIpType,'bwmCurCfgContractMonitorMode':bwmCurCfgContractMonitorMode,'bwmCurCfgContractGroup':bwmCurCfgContractGroup,'bwmCurCfgContractMaxSess':bwmCurCfgContractMaxSess,'bwmCurCfgContractRowType':bwmCurCfgContractRowType,'bwmNewCfgContractTable':bwmNewCfgContractTable,'bwmNewCfgContractTableEntry':bwmNewCfgContractTableEntry,_Q:bwmNewCfgContractIndx,'bwmNewCfgContractName':bwmNewCfgContractName,'bwmNewCfgContractState':bwmNewCfgContractState,'bwmNewCfgContractPolicy':bwmNewCfgContractPolicy,'bwmNewCfgContractDelete':bwmNewCfgContractDelete,'bwmNewCfgContractPrec':bwmNewCfgContractPrec,'bwmNewCfgContractUseTos':bwmNewCfgContractUseTos,'bwmNewCfgContractHistory':bwmNewCfgContractHistory,'bwmNewCfgContractShaping':bwmNewCfgContractShaping,'bwmNewCfgContractResizeTcp':bwmNewCfgContractResizeTcp,'bwmNewCfgContractIpLimit':bwmNewCfgContractIpLimit,'bwmNewCfgContractIpType':bwmNewCfgContractIpType,'bwmNewCfgContractMonitorMode':bwmNewCfgContractMonitorMode,'bwmNewCfgContractGroup':bwmNewCfgContractGroup,'bwmNewCfgContractMaxSess':bwmNewCfgContractMaxSess,'bwmNewCfgContractRowType':bwmNewCfgContractRowType,'bwmAvailableContractsTable':bwmAvailableContractsTable,'bwmAvailableContractsTableEntry':bwmAvailableContractsTableEntry,_R:bwmContractIndx,'bwmContractName':bwmContractName,'bwmContTimePolicyConfig':bwmContTimePolicyConfig,'bwmContTimePolicyTableMaxEnt':bwmContTimePolicyTableMaxEnt,'bwmCurCfgContTimePolicyTable':bwmCurCfgContTimePolicyTable,'bwmCurCfgContTimePolicyTableEntry':bwmCurCfgContTimePolicyTableEntry,_S:bwmCurCfgContTimePolicyContIndx,_T:bwmCurCfgContTimePolicyIndx,'bwmCurCfgContTimePolicyDay':bwmCurCfgContTimePolicyDay,'bwmCurCfgContTimePolicyFrom':bwmCurCfgContTimePolicyFrom,'bwmCurCfgContTimePolicyTo':bwmCurCfgContTimePolicyTo,'bwmCurCfgContTimePolicyPol':bwmCurCfgContTimePolicyPol,'bwmCurCfgContTimePolicyState':bwmCurCfgContTimePolicyState,'bwmNewCfgContTimePolicyTable':bwmNewCfgContTimePolicyTable,'bwmNewCfgContTimePolicyTableEntry':bwmNewCfgContTimePolicyTableEntry,_e:bwmNewCfgContTimePolicyContIndx,_f:bwmNewCfgContTimePolicyIndx,'bwmNewCfgContTimePolicyDay':bwmNewCfgContTimePolicyDay,'bwmNewCfgContTimePolicyFrom':bwmNewCfgContTimePolicyFrom,'bwmNewCfgContTimePolicyTo':bwmNewCfgContTimePolicyTo,'bwmNewCfgContTimePolicyPol':bwmNewCfgContTimePolicyPol,'bwmNewCfgContTimePolicyState':bwmNewCfgContTimePolicyState,'bwmNewCfgContTimePolicyDelete':bwmNewCfgContTimePolicyDelete,'bwmContractGroupConfig':bwmContractGroupConfig,'bwmContractGroupTableMaxEnt':bwmContractGroupTableMaxEnt,'bwmCurCfgContractGroupTable':bwmCurCfgContractGroupTable,'bwmCurCfgContractGroupTableEntry':bwmCurCfgContractGroupTableEntry,_g:bwmCurCfgContractGroupIndx,'bwmCurCfgContractGroupContracts':bwmCurCfgContractGroupContracts,'bwmCurCfgContractGroupName':bwmCurCfgContractGroupName,'bwmNewCfgContractGroupTable':bwmNewCfgContractGroupTable,'bwmNewCfgContractGroupTableEntry':bwmNewCfgContractGroupTableEntry,_h:bwmNewCfgContractGroupIndx,'bwmNewCfgContractGroupContracts':bwmNewCfgContractGroupContracts,'bwmNewCfgContractGroupAddCont':bwmNewCfgContractGroupAddCont,'bwmNewCfgContractGroupRemCont':bwmNewCfgContractGroupRemCont,'bwmNewCfgContractGroupDelete':bwmNewCfgContractGroupDelete,'bwmNewCfgContractGroupName':bwmNewCfgContractGroupName,'bwmContractGroupTableMaxCont':bwmContractGroupTableMaxCont,'bwmStats':bwmStats,'bwmStatTcTable':bwmStatTcTable,'bwmStatTcEntry':bwmStatTcEntry,_i:bwmStatTcContractIndex,'bwmStatTcName':bwmStatTcName,'bwmStatTcOutoct':bwmStatTcOutoct,'bwmStatTcOutdisoct':bwmStatTcOutdisoct,'bwmStatTcBufferUsed':bwmStatTcBufferUsed,'bwmStatTcBufferMax':bwmStatTcBufferMax,'bwmStatTcTotalPackets':bwmStatTcTotalPackets,'bwmStatTcSessRejected':bwmStatTcSessRejected,'bwmStatTcrTable':bwmStatTcrTable,'bwmStatTcrEntry':bwmStatTcrEntry,_j:bwmStatTcrContractIndex,'bwmStatTcrName':bwmStatTcrName,'bwmStatTcrRate':bwmStatTcrRate,'bwmStatTcrOutoct':bwmStatTcrOutoct,'bwmStatTcrOutdisoct':bwmStatTcrOutdisoct,'bwmStatTcrBufferUsed':bwmStatTcrBufferUsed,'bwmStatTcrBufferMax':bwmStatTcrBufferMax,'bwmStatTcrTotalPackets':bwmStatTcrTotalPackets,'bwmStatPortTcTable':bwmStatPortTcTable,'bwmStatPortTcEntry':bwmStatPortTcEntry,_k:bwmStatPortTcPortIndex,_l:bwmStatPortTcContractIndex,'bwmStatPortTcName':bwmStatPortTcName,'bwmStatPortTcOutoct':bwmStatPortTcOutoct,'bwmStatPortTcOutdisoct':bwmStatPortTcOutdisoct,'bwmStatPortTcBufferUsed':bwmStatPortTcBufferUsed,'bwmStatPortTcBufferMax':bwmStatPortTcBufferMax,'bwmStatPortTcTotalPackets':bwmStatPortTcTotalPackets,'bwmStatPortTcrTable':bwmStatPortTcrTable,'bwmStatPortTcrEntry':bwmStatPortTcrEntry,_m:bwmStatPortTcrPortIndex,_n:bwmStatPortTcrContractIndex,'bwmStatPortTcrName':bwmStatPortTcrName,'bwmStatPortTcrRate':bwmStatPortTcrRate,'bwmStatPortTcrOutoct':bwmStatPortTcrOutoct,'bwmStatPortTcrOutdisoct':bwmStatPortTcrOutdisoct,'bwmStatPortTcrBufferUsed':bwmStatPortTcrBufferUsed,'bwmStatPortTcrBufferMax':bwmStatPortTcrBufferMax,'bwmStatPortTcrTotalPackets':bwmStatPortTcrTotalPackets,'bwmStatsClear':bwmStatsClear,'bwmOpers':bwmOpers,'bwmOperSendSMTP':bwmOperSendSMTP,'bwmOperClearUsrEntry':bwmOperClearUsrEntry})