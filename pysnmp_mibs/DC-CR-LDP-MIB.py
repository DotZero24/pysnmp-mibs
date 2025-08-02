_AC='dccrldpOptionalGroup'
_AB='dccrldpMandatoryGroup'
_AA='dccrldpPmPwFastUpstreamRelease'
_A9='dccrldpPmIngressReleaseDelay'
_A8='dccrldpPmWthdrwDownstreamLbl'
_A7='dccrldpPmImplicitXcVcFecs'
_A6='dccrldpPmLabelWithdrawDelay'
_A5='dccrldpPmRedundancySwitchIntvl'
_A4='dccrldpPmLdpEntityCreatePsiJoin'
_A3='dccrldpPmLdpEntityCreateNhrLdb'
_A2='dccrldpPmCheckOutSegIntfaceStat'
_A1='dccrldpPmPolicySupportFlags'
_A0='dccrldpPmSupportIpv6'
_z='dccrldpPmOutSegProgOrder'
_y='dccrldpPmAdjDwnHoldTime'
_x='dccrldpPmMaxPeerRecovery'
_w='dccrldpPmMaxPeerReconnect'
_v='dccrldpPmRecoveryTime'
_u='dccrldpPmReconnectTime'
_t='dccrldpPmRestartCapable'
_s='dccrldpPmOperStatus'
_r='dccrldpPmAdminStatus'
_q='dccrldpPmQueryFECSupported'
_p='dccrldpPmCrLdpSupported'
_o='dccrldpPmLdpSupported'
_n='dccrldpPmIprBufPoolSize'
_m='dccrldpPmAsNumber'
_l='dccrldpPmUseLdpFt'
_k='dccrldpPmLdpVersion'
_j='dccrldpPmLdpEntityReuse'
_i='dccrldpPmLdpEntityAutoStart'
_h='dccrldpPmLdpEntityAutoCreate'
_g='dccrldpSigBfdProviderIndex'
_f='dccrldpSigPathVecLimitTrapEnable'
_e='dccrldpSigSessThreshTrapEnable'
_d='dccrldpSigSessStatusTrapEnable'
_c='dccrldpSigUseIPv6Transport'
_b='dccrldpSigConformanceFlags'
_a='dccrldpSigUseI3Interface'
_Z='dccrldpSigOperStatus'
_Y='dccrldpSigAdminStatus'
_X='dccrldpSigAMBufPoolSize'
_W='dccrldpSigEMBufPoolSize'
_V='dccrldpSigSessionBufPoolSize'
_U='dccrldpPmLsrIndex'
_T='dccrldpSigSocketIfIndex'
_S='dccrldpSigLsrIndex'
_R='dccrldpSigPathManagerIndex'
_Q='dccrldpPmIndex'
_P='read-only'
_O='DcCrldpIndex'
_N='not-accessible'
_M='dccrldpSigIndex'
_L='InterfaceIndexOrZero'
_K='dccrldpPmRowStatus'
_J='dccrldpSigRowStatus'
_I='DcCrldpAdminStatus'
_H='Unsigned32'
_G='Bits'
_F='milliseconds'
_E='Integer32'
_D='TruthValue'
_C='read-create'
_B='DC-CR-LDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
dccrldp=ModuleIdentity((1,3,6,1,4,1,629,10,15))
if mibBuilder.loadTexts:dccrldp.setRevisions(('2014-12-21 00:00',))
class DcCrldpAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class DcCrldpOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),('goingUp',3),('goingDown',4),('actFailed',5)))
class DcCrldpIndex(TextualConvention,Unsigned32):status=_A
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_Opx_ObjectIdentity=ObjectIdentity
opx=_Opx_ObjectIdentity((1,3,6,1,4,1,629,10))
_DccrldpObjects_ObjectIdentity=ObjectIdentity
dccrldpObjects=_DccrldpObjects_ObjectIdentity((1,3,6,1,4,1,629,10,15,1))
_DccrldpSigTable_Object=MibTable
dccrldpSigTable=_DccrldpSigTable_Object((1,3,6,1,4,1,629,10,15,1,1))
if mibBuilder.loadTexts:dccrldpSigTable.setStatus(_A)
_DccrldpSigEntry_Object=MibTableRow
dccrldpSigEntry=_DccrldpSigEntry_Object((1,3,6,1,4,1,629,10,15,1,1,1))
dccrldpSigEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:dccrldpSigEntry.setStatus(_A)
_DccrldpSigIndex_Type=DcCrldpIndex
_DccrldpSigIndex_Object=MibTableColumn
dccrldpSigIndex=_DccrldpSigIndex_Object((1,3,6,1,4,1,629,10,15,1,1,1,1),_DccrldpSigIndex_Type())
dccrldpSigIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dccrldpSigIndex.setStatus(_A)
class _DccrldpSigPathManagerIndex_Type(DcCrldpIndex):defaultValue=0
_DccrldpSigPathManagerIndex_Type.__name__=_O
_DccrldpSigPathManagerIndex_Object=MibTableColumn
dccrldpSigPathManagerIndex=_DccrldpSigPathManagerIndex_Object((1,3,6,1,4,1,629,10,15,1,1,1,2),_DccrldpSigPathManagerIndex_Type())
dccrldpSigPathManagerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigPathManagerIndex.setStatus(_A)
class _DccrldpSigLsrIndex_Type(Unsigned32):defaultValue=0
_DccrldpSigLsrIndex_Type.__name__=_H
_DccrldpSigLsrIndex_Object=MibTableColumn
dccrldpSigLsrIndex=_DccrldpSigLsrIndex_Object((1,3,6,1,4,1,629,10,15,1,1,1,3),_DccrldpSigLsrIndex_Type())
dccrldpSigLsrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigLsrIndex.setStatus(_A)
class _DccrldpSigSocketIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_DccrldpSigSocketIfIndex_Type.__name__=_L
_DccrldpSigSocketIfIndex_Object=MibTableColumn
dccrldpSigSocketIfIndex=_DccrldpSigSocketIfIndex_Object((1,3,6,1,4,1,629,10,15,1,1,1,4),_DccrldpSigSocketIfIndex_Type())
dccrldpSigSocketIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigSocketIfIndex.setStatus(_A)
class _DccrldpSigSessionBufPoolSize_Type(Integer32):defaultValue=8
_DccrldpSigSessionBufPoolSize_Type.__name__=_E
_DccrldpSigSessionBufPoolSize_Object=MibTableColumn
dccrldpSigSessionBufPoolSize=_DccrldpSigSessionBufPoolSize_Object((1,3,6,1,4,1,629,10,15,1,1,1,5),_DccrldpSigSessionBufPoolSize_Type())
dccrldpSigSessionBufPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigSessionBufPoolSize.setStatus(_A)
class _DccrldpSigEMBufPoolSize_Type(Integer32):defaultValue=8
_DccrldpSigEMBufPoolSize_Type.__name__=_E
_DccrldpSigEMBufPoolSize_Object=MibTableColumn
dccrldpSigEMBufPoolSize=_DccrldpSigEMBufPoolSize_Object((1,3,6,1,4,1,629,10,15,1,1,1,6),_DccrldpSigEMBufPoolSize_Type())
dccrldpSigEMBufPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigEMBufPoolSize.setStatus(_A)
class _DccrldpSigAMBufPoolSize_Type(Integer32):defaultValue=8
_DccrldpSigAMBufPoolSize_Type.__name__=_E
_DccrldpSigAMBufPoolSize_Object=MibTableColumn
dccrldpSigAMBufPoolSize=_DccrldpSigAMBufPoolSize_Object((1,3,6,1,4,1,629,10,15,1,1,1,7),_DccrldpSigAMBufPoolSize_Type())
dccrldpSigAMBufPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigAMBufPoolSize.setStatus(_A)
class _DccrldpSigAdminStatus_Type(DcCrldpAdminStatus):defaultValue=1
_DccrldpSigAdminStatus_Type.__name__=_I
_DccrldpSigAdminStatus_Object=MibTableColumn
dccrldpSigAdminStatus=_DccrldpSigAdminStatus_Object((1,3,6,1,4,1,629,10,15,1,1,1,8),_DccrldpSigAdminStatus_Type())
dccrldpSigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigAdminStatus.setStatus(_A)
_DccrldpSigOperStatus_Type=DcCrldpOperStatus
_DccrldpSigOperStatus_Object=MibTableColumn
dccrldpSigOperStatus=_DccrldpSigOperStatus_Object((1,3,6,1,4,1,629,10,15,1,1,1,9),_DccrldpSigOperStatus_Type())
dccrldpSigOperStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:dccrldpSigOperStatus.setStatus(_A)
_DccrldpSigRowStatus_Type=RowStatus
_DccrldpSigRowStatus_Object=MibTableColumn
dccrldpSigRowStatus=_DccrldpSigRowStatus_Object((1,3,6,1,4,1,629,10,15,1,1,1,10),_DccrldpSigRowStatus_Type())
dccrldpSigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigRowStatus.setStatus(_A)
class _DccrldpSigUseI3Interface_Type(TruthValue):defaultValue=2
_DccrldpSigUseI3Interface_Type.__name__=_D
_DccrldpSigUseI3Interface_Object=MibTableColumn
dccrldpSigUseI3Interface=_DccrldpSigUseI3Interface_Object((1,3,6,1,4,1,629,10,15,1,1,1,11),_DccrldpSigUseI3Interface_Type())
dccrldpSigUseI3Interface.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigUseI3Interface.setStatus(_A)
class _DccrldpSigConformanceFlags_Type(Bits):defaultBinValue='0';namedValues=NamedValues(('maxPduLen',0))
_DccrldpSigConformanceFlags_Type.__name__=_G
_DccrldpSigConformanceFlags_Object=MibTableColumn
dccrldpSigConformanceFlags=_DccrldpSigConformanceFlags_Object((1,3,6,1,4,1,629,10,15,1,1,1,12),_DccrldpSigConformanceFlags_Type())
dccrldpSigConformanceFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigConformanceFlags.setStatus(_A)
class _DccrldpSigUseIPv6Transport_Type(TruthValue):defaultValue=2
_DccrldpSigUseIPv6Transport_Type.__name__=_D
_DccrldpSigUseIPv6Transport_Object=MibTableColumn
dccrldpSigUseIPv6Transport=_DccrldpSigUseIPv6Transport_Object((1,3,6,1,4,1,629,10,15,1,1,1,13),_DccrldpSigUseIPv6Transport_Type())
dccrldpSigUseIPv6Transport.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigUseIPv6Transport.setStatus(_A)
class _DccrldpSigSessStatusTrapEnable_Type(TruthValue):defaultValue=2
_DccrldpSigSessStatusTrapEnable_Type.__name__=_D
_DccrldpSigSessStatusTrapEnable_Object=MibTableColumn
dccrldpSigSessStatusTrapEnable=_DccrldpSigSessStatusTrapEnable_Object((1,3,6,1,4,1,629,10,15,1,1,1,14),_DccrldpSigSessStatusTrapEnable_Type())
dccrldpSigSessStatusTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigSessStatusTrapEnable.setStatus(_A)
class _DccrldpSigSessThreshTrapEnable_Type(TruthValue):defaultValue=2
_DccrldpSigSessThreshTrapEnable_Type.__name__=_D
_DccrldpSigSessThreshTrapEnable_Object=MibTableColumn
dccrldpSigSessThreshTrapEnable=_DccrldpSigSessThreshTrapEnable_Object((1,3,6,1,4,1,629,10,15,1,1,1,15),_DccrldpSigSessThreshTrapEnable_Type())
dccrldpSigSessThreshTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigSessThreshTrapEnable.setStatus(_A)
class _DccrldpSigPathVecLimitTrapEnable_Type(TruthValue):defaultValue=2
_DccrldpSigPathVecLimitTrapEnable_Type.__name__=_D
_DccrldpSigPathVecLimitTrapEnable_Object=MibTableColumn
dccrldpSigPathVecLimitTrapEnable=_DccrldpSigPathVecLimitTrapEnable_Object((1,3,6,1,4,1,629,10,15,1,1,1,16),_DccrldpSigPathVecLimitTrapEnable_Type())
dccrldpSigPathVecLimitTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigPathVecLimitTrapEnable.setStatus(_A)
class _DccrldpSigBfdProviderIndex_Type(Integer32):defaultValue=0
_DccrldpSigBfdProviderIndex_Type.__name__=_E
_DccrldpSigBfdProviderIndex_Object=MibTableColumn
dccrldpSigBfdProviderIndex=_DccrldpSigBfdProviderIndex_Object((1,3,6,1,4,1,629,10,15,1,1,1,17),_DccrldpSigBfdProviderIndex_Type())
dccrldpSigBfdProviderIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpSigBfdProviderIndex.setStatus(_A)
_DccrldpPmTable_Object=MibTable
dccrldpPmTable=_DccrldpPmTable_Object((1,3,6,1,4,1,629,10,15,1,2))
if mibBuilder.loadTexts:dccrldpPmTable.setStatus(_A)
_DccrldpPmEntry_Object=MibTableRow
dccrldpPmEntry=_DccrldpPmEntry_Object((1,3,6,1,4,1,629,10,15,1,2,1))
dccrldpPmEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:dccrldpPmEntry.setStatus(_A)
_DccrldpPmIndex_Type=DcCrldpIndex
_DccrldpPmIndex_Object=MibTableColumn
dccrldpPmIndex=_DccrldpPmIndex_Object((1,3,6,1,4,1,629,10,15,1,2,1,1),_DccrldpPmIndex_Type())
dccrldpPmIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dccrldpPmIndex.setStatus(_A)
class _DccrldpPmLsrIndex_Type(Unsigned32):defaultValue=0
_DccrldpPmLsrIndex_Type.__name__=_H
_DccrldpPmLsrIndex_Object=MibTableColumn
dccrldpPmLsrIndex=_DccrldpPmLsrIndex_Object((1,3,6,1,4,1,629,10,15,1,2,1,2),_DccrldpPmLsrIndex_Type())
dccrldpPmLsrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLsrIndex.setStatus(_A)
class _DccrldpPmLdpEntityAutoCreate_Type(TruthValue):defaultValue=1
_DccrldpPmLdpEntityAutoCreate_Type.__name__=_D
_DccrldpPmLdpEntityAutoCreate_Object=MibTableColumn
dccrldpPmLdpEntityAutoCreate=_DccrldpPmLdpEntityAutoCreate_Object((1,3,6,1,4,1,629,10,15,1,2,1,3),_DccrldpPmLdpEntityAutoCreate_Type())
dccrldpPmLdpEntityAutoCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLdpEntityAutoCreate.setStatus(_A)
class _DccrldpPmLdpEntityAutoStart_Type(TruthValue):defaultValue=1
_DccrldpPmLdpEntityAutoStart_Type.__name__=_D
_DccrldpPmLdpEntityAutoStart_Object=MibTableColumn
dccrldpPmLdpEntityAutoStart=_DccrldpPmLdpEntityAutoStart_Object((1,3,6,1,4,1,629,10,15,1,2,1,4),_DccrldpPmLdpEntityAutoStart_Type())
dccrldpPmLdpEntityAutoStart.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLdpEntityAutoStart.setStatus(_A)
class _DccrldpPmLdpEntityReuse_Type(TruthValue):defaultValue=1
_DccrldpPmLdpEntityReuse_Type.__name__=_D
_DccrldpPmLdpEntityReuse_Object=MibTableColumn
dccrldpPmLdpEntityReuse=_DccrldpPmLdpEntityReuse_Object((1,3,6,1,4,1,629,10,15,1,2,1,5),_DccrldpPmLdpEntityReuse_Type())
dccrldpPmLdpEntityReuse.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLdpEntityReuse.setStatus(_A)
class _DccrldpPmLdpVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('version1',1))
_DccrldpPmLdpVersion_Type.__name__=_E
_DccrldpPmLdpVersion_Object=MibTableColumn
dccrldpPmLdpVersion=_DccrldpPmLdpVersion_Object((1,3,6,1,4,1,629,10,15,1,2,1,6),_DccrldpPmLdpVersion_Type())
dccrldpPmLdpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLdpVersion.setStatus(_A)
class _DccrldpPmUseLdpFt_Type(TruthValue):defaultValue=2
_DccrldpPmUseLdpFt_Type.__name__=_D
_DccrldpPmUseLdpFt_Object=MibTableColumn
dccrldpPmUseLdpFt=_DccrldpPmUseLdpFt_Object((1,3,6,1,4,1,629,10,15,1,2,1,7),_DccrldpPmUseLdpFt_Type())
dccrldpPmUseLdpFt.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmUseLdpFt.setStatus(_A)
class _DccrldpPmAsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DccrldpPmAsNumber_Type.__name__=_E
_DccrldpPmAsNumber_Object=MibTableColumn
dccrldpPmAsNumber=_DccrldpPmAsNumber_Object((1,3,6,1,4,1,629,10,15,1,2,1,8),_DccrldpPmAsNumber_Type())
dccrldpPmAsNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmAsNumber.setStatus(_A)
class _DccrldpPmIprBufPoolSize_Type(Integer32):defaultValue=8
_DccrldpPmIprBufPoolSize_Type.__name__=_E
_DccrldpPmIprBufPoolSize_Object=MibTableColumn
dccrldpPmIprBufPoolSize=_DccrldpPmIprBufPoolSize_Object((1,3,6,1,4,1,629,10,15,1,2,1,9),_DccrldpPmIprBufPoolSize_Type())
dccrldpPmIprBufPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmIprBufPoolSize.setStatus(_A)
class _DccrldpPmLdpSupported_Type(TruthValue):defaultValue=2
_DccrldpPmLdpSupported_Type.__name__=_D
_DccrldpPmLdpSupported_Object=MibTableColumn
dccrldpPmLdpSupported=_DccrldpPmLdpSupported_Object((1,3,6,1,4,1,629,10,15,1,2,1,10),_DccrldpPmLdpSupported_Type())
dccrldpPmLdpSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLdpSupported.setStatus(_A)
class _DccrldpPmCrLdpSupported_Type(TruthValue):defaultValue=2
_DccrldpPmCrLdpSupported_Type.__name__=_D
_DccrldpPmCrLdpSupported_Object=MibTableColumn
dccrldpPmCrLdpSupported=_DccrldpPmCrLdpSupported_Object((1,3,6,1,4,1,629,10,15,1,2,1,11),_DccrldpPmCrLdpSupported_Type())
dccrldpPmCrLdpSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmCrLdpSupported.setStatus(_A)
class _DccrldpPmQueryFECSupported_Type(TruthValue):defaultValue=2
_DccrldpPmQueryFECSupported_Type.__name__=_D
_DccrldpPmQueryFECSupported_Object=MibTableColumn
dccrldpPmQueryFECSupported=_DccrldpPmQueryFECSupported_Object((1,3,6,1,4,1,629,10,15,1,2,1,12),_DccrldpPmQueryFECSupported_Type())
dccrldpPmQueryFECSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmQueryFECSupported.setStatus(_A)
class _DccrldpPmAdminStatus_Type(DcCrldpAdminStatus):defaultValue=1
_DccrldpPmAdminStatus_Type.__name__=_I
_DccrldpPmAdminStatus_Object=MibTableColumn
dccrldpPmAdminStatus=_DccrldpPmAdminStatus_Object((1,3,6,1,4,1,629,10,15,1,2,1,13),_DccrldpPmAdminStatus_Type())
dccrldpPmAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmAdminStatus.setStatus(_A)
_DccrldpPmOperStatus_Type=DcCrldpOperStatus
_DccrldpPmOperStatus_Object=MibTableColumn
dccrldpPmOperStatus=_DccrldpPmOperStatus_Object((1,3,6,1,4,1,629,10,15,1,2,1,14),_DccrldpPmOperStatus_Type())
dccrldpPmOperStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:dccrldpPmOperStatus.setStatus(_A)
_DccrldpPmRowStatus_Type=RowStatus
_DccrldpPmRowStatus_Object=MibTableColumn
dccrldpPmRowStatus=_DccrldpPmRowStatus_Object((1,3,6,1,4,1,629,10,15,1,2,1,15),_DccrldpPmRowStatus_Type())
dccrldpPmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmRowStatus.setStatus(_A)
class _DccrldpPmRestartCapable_Type(TruthValue):defaultValue=2
_DccrldpPmRestartCapable_Type.__name__=_D
_DccrldpPmRestartCapable_Object=MibTableColumn
dccrldpPmRestartCapable=_DccrldpPmRestartCapable_Object((1,3,6,1,4,1,629,10,15,1,2,1,16),_DccrldpPmRestartCapable_Type())
dccrldpPmRestartCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmRestartCapable.setStatus(_A)
class _DccrldpPmReconnectTime_Type(Integer32):defaultValue=60000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DccrldpPmReconnectTime_Type.__name__=_E
_DccrldpPmReconnectTime_Object=MibTableColumn
dccrldpPmReconnectTime=_DccrldpPmReconnectTime_Object((1,3,6,1,4,1,629,10,15,1,2,1,17),_DccrldpPmReconnectTime_Type())
dccrldpPmReconnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmReconnectTime.setStatus(_A)
if mibBuilder.loadTexts:dccrldpPmReconnectTime.setUnits(_F)
class _DccrldpPmRecoveryTime_Type(Integer32):defaultValue=180000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DccrldpPmRecoveryTime_Type.__name__=_E
_DccrldpPmRecoveryTime_Object=MibTableColumn
dccrldpPmRecoveryTime=_DccrldpPmRecoveryTime_Object((1,3,6,1,4,1,629,10,15,1,2,1,18),_DccrldpPmRecoveryTime_Type())
dccrldpPmRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmRecoveryTime.setStatus(_A)
if mibBuilder.loadTexts:dccrldpPmRecoveryTime.setUnits(_F)
class _DccrldpPmMaxPeerReconnect_Type(Integer32):defaultValue=180000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DccrldpPmMaxPeerReconnect_Type.__name__=_E
_DccrldpPmMaxPeerReconnect_Object=MibTableColumn
dccrldpPmMaxPeerReconnect=_DccrldpPmMaxPeerReconnect_Object((1,3,6,1,4,1,629,10,15,1,2,1,19),_DccrldpPmMaxPeerReconnect_Type())
dccrldpPmMaxPeerReconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmMaxPeerReconnect.setStatus(_A)
if mibBuilder.loadTexts:dccrldpPmMaxPeerReconnect.setUnits(_F)
class _DccrldpPmMaxPeerRecovery_Type(Integer32):defaultValue=240000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DccrldpPmMaxPeerRecovery_Type.__name__=_E
_DccrldpPmMaxPeerRecovery_Object=MibTableColumn
dccrldpPmMaxPeerRecovery=_DccrldpPmMaxPeerRecovery_Object((1,3,6,1,4,1,629,10,15,1,2,1,20),_DccrldpPmMaxPeerRecovery_Type())
dccrldpPmMaxPeerRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmMaxPeerRecovery.setStatus(_A)
if mibBuilder.loadTexts:dccrldpPmMaxPeerRecovery.setUnits(_F)
class _DccrldpPmAdjDwnHoldTime_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DccrldpPmAdjDwnHoldTime_Type.__name__=_E
_DccrldpPmAdjDwnHoldTime_Object=MibTableColumn
dccrldpPmAdjDwnHoldTime=_DccrldpPmAdjDwnHoldTime_Object((1,3,6,1,4,1,629,10,15,1,2,1,21),_DccrldpPmAdjDwnHoldTime_Type())
dccrldpPmAdjDwnHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmAdjDwnHoldTime.setStatus(_A)
if mibBuilder.loadTexts:dccrldpPmAdjDwnHoldTime.setUnits(_F)
class _DccrldpPmOutSegProgOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('default',0),('connFirst',1)))
_DccrldpPmOutSegProgOrder_Type.__name__=_E
_DccrldpPmOutSegProgOrder_Object=MibTableColumn
dccrldpPmOutSegProgOrder=_DccrldpPmOutSegProgOrder_Object((1,3,6,1,4,1,629,10,15,1,2,1,22),_DccrldpPmOutSegProgOrder_Type())
dccrldpPmOutSegProgOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmOutSegProgOrder.setStatus(_A)
class _DccrldpPmSupportIpv6_Type(TruthValue):defaultValue=2
_DccrldpPmSupportIpv6_Type.__name__=_D
_DccrldpPmSupportIpv6_Object=MibTableColumn
dccrldpPmSupportIpv6=_DccrldpPmSupportIpv6_Object((1,3,6,1,4,1,629,10,15,1,2,1,23),_DccrldpPmSupportIpv6_Type())
dccrldpPmSupportIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmSupportIpv6.setStatus(_A)
class _DccrldpPmPolicySupportFlags_Type(Bits):namedValues=NamedValues(*(('policySupported',0),('perFecOptimizationSupported',1),('suppressAddressPolicy',2),('policyForVCFECs',3)))
_DccrldpPmPolicySupportFlags_Type.__name__=_G
_DccrldpPmPolicySupportFlags_Object=MibTableColumn
dccrldpPmPolicySupportFlags=_DccrldpPmPolicySupportFlags_Object((1,3,6,1,4,1,629,10,15,1,2,1,24),_DccrldpPmPolicySupportFlags_Type())
dccrldpPmPolicySupportFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmPolicySupportFlags.setStatus(_A)
class _DccrldpPmCheckOutSegIntfaceStat_Type(TruthValue):defaultValue=2
_DccrldpPmCheckOutSegIntfaceStat_Type.__name__=_D
_DccrldpPmCheckOutSegIntfaceStat_Object=MibTableColumn
dccrldpPmCheckOutSegIntfaceStat=_DccrldpPmCheckOutSegIntfaceStat_Object((1,3,6,1,4,1,629,10,15,1,2,1,25),_DccrldpPmCheckOutSegIntfaceStat_Type())
dccrldpPmCheckOutSegIntfaceStat.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmCheckOutSegIntfaceStat.setStatus(_A)
class _DccrldpPmLdpEntityCreateNhrLdb_Type(TruthValue):defaultValue=1
_DccrldpPmLdpEntityCreateNhrLdb_Type.__name__=_D
_DccrldpPmLdpEntityCreateNhrLdb_Object=MibTableColumn
dccrldpPmLdpEntityCreateNhrLdb=_DccrldpPmLdpEntityCreateNhrLdb_Object((1,3,6,1,4,1,629,10,15,1,2,1,26),_DccrldpPmLdpEntityCreateNhrLdb_Type())
dccrldpPmLdpEntityCreateNhrLdb.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLdpEntityCreateNhrLdb.setStatus(_A)
class _DccrldpPmLdpEntityCreatePsiJoin_Type(TruthValue):defaultValue=2
_DccrldpPmLdpEntityCreatePsiJoin_Type.__name__=_D
_DccrldpPmLdpEntityCreatePsiJoin_Object=MibTableColumn
dccrldpPmLdpEntityCreatePsiJoin=_DccrldpPmLdpEntityCreatePsiJoin_Object((1,3,6,1,4,1,629,10,15,1,2,1,27),_DccrldpPmLdpEntityCreatePsiJoin_Type())
dccrldpPmLdpEntityCreatePsiJoin.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLdpEntityCreatePsiJoin.setStatus(_A)
class _DccrldpPmRedundancySwitchIntvl_Type(Integer32):defaultValue=20000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DccrldpPmRedundancySwitchIntvl_Type.__name__=_E
_DccrldpPmRedundancySwitchIntvl_Object=MibTableColumn
dccrldpPmRedundancySwitchIntvl=_DccrldpPmRedundancySwitchIntvl_Object((1,3,6,1,4,1,629,10,15,1,2,1,28),_DccrldpPmRedundancySwitchIntvl_Type())
dccrldpPmRedundancySwitchIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmRedundancySwitchIntvl.setStatus(_A)
if mibBuilder.loadTexts:dccrldpPmRedundancySwitchIntvl.setUnits(_F)
class _DccrldpPmLabelWithdrawDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000))
_DccrldpPmLabelWithdrawDelay_Type.__name__=_E
_DccrldpPmLabelWithdrawDelay_Object=MibTableColumn
dccrldpPmLabelWithdrawDelay=_DccrldpPmLabelWithdrawDelay_Object((1,3,6,1,4,1,629,10,15,1,2,1,29),_DccrldpPmLabelWithdrawDelay_Type())
dccrldpPmLabelWithdrawDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmLabelWithdrawDelay.setStatus(_A)
if mibBuilder.loadTexts:dccrldpPmLabelWithdrawDelay.setUnits('seconds')
class _DccrldpPmImplicitXcVcFecs_Type(TruthValue):defaultValue=2
_DccrldpPmImplicitXcVcFecs_Type.__name__=_D
_DccrldpPmImplicitXcVcFecs_Object=MibTableColumn
dccrldpPmImplicitXcVcFecs=_DccrldpPmImplicitXcVcFecs_Object((1,3,6,1,4,1,629,10,15,1,2,1,30),_DccrldpPmImplicitXcVcFecs_Type())
dccrldpPmImplicitXcVcFecs.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmImplicitXcVcFecs.setStatus(_A)
class _DccrldpPmWthdrwDownstreamLbl_Type(TruthValue):defaultValue=2
_DccrldpPmWthdrwDownstreamLbl_Type.__name__=_D
_DccrldpPmWthdrwDownstreamLbl_Object=MibTableColumn
dccrldpPmWthdrwDownstreamLbl=_DccrldpPmWthdrwDownstreamLbl_Object((1,3,6,1,4,1,629,10,15,1,2,1,31),_DccrldpPmWthdrwDownstreamLbl_Type())
dccrldpPmWthdrwDownstreamLbl.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmWthdrwDownstreamLbl.setStatus(_A)
class _DccrldpPmIngressReleaseDelay_Type(TruthValue):defaultValue=2
_DccrldpPmIngressReleaseDelay_Type.__name__=_D
_DccrldpPmIngressReleaseDelay_Object=MibTableColumn
dccrldpPmIngressReleaseDelay=_DccrldpPmIngressReleaseDelay_Object((1,3,6,1,4,1,629,10,15,1,2,1,32),_DccrldpPmIngressReleaseDelay_Type())
dccrldpPmIngressReleaseDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmIngressReleaseDelay.setStatus(_A)
class _DccrldpPmPwFastUpstreamRelease_Type(TruthValue):defaultValue=2
_DccrldpPmPwFastUpstreamRelease_Type.__name__=_D
_DccrldpPmPwFastUpstreamRelease_Object=MibTableColumn
dccrldpPmPwFastUpstreamRelease=_DccrldpPmPwFastUpstreamRelease_Object((1,3,6,1,4,1,629,10,15,1,2,1,33),_DccrldpPmPwFastUpstreamRelease_Type())
dccrldpPmPwFastUpstreamRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:dccrldpPmPwFastUpstreamRelease.setStatus(_A)
_DccrldpConformance_ObjectIdentity=ObjectIdentity
dccrldpConformance=_DccrldpConformance_ObjectIdentity((1,3,6,1,4,1,629,10,15,2))
_DccrldpCompliances_ObjectIdentity=ObjectIdentity
dccrldpCompliances=_DccrldpCompliances_ObjectIdentity((1,3,6,1,4,1,629,10,15,2,1))
_DccrldpGroups_ObjectIdentity=ObjectIdentity
dccrldpGroups=_DccrldpGroups_ObjectIdentity((1,3,6,1,4,1,629,10,15,2,2))
dccrldpMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,10,15,2,2,2))
dccrldpMandatoryGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_J),(_B,_U),(_B,_K)))
if mibBuilder.loadTexts:dccrldpMandatoryGroup.setStatus(_A)
dccrldpOptionalGroup=ObjectGroup((1,3,6,1,4,1,629,10,15,2,2,3))
dccrldpOptionalGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_J),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_K),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:dccrldpOptionalGroup.setStatus(_A)
dccrldpMibCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,15,2,1,1))
dccrldpMibCompliance.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:dccrldpMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_I:DcCrldpAdminStatus,'DcCrldpOperStatus':DcCrldpOperStatus,_O:DcCrldpIndex,'nbase':nbase,'opx':opx,'dccrldp':dccrldp,'dccrldpObjects':dccrldpObjects,'dccrldpSigTable':dccrldpSigTable,'dccrldpSigEntry':dccrldpSigEntry,_M:dccrldpSigIndex,_R:dccrldpSigPathManagerIndex,_S:dccrldpSigLsrIndex,_T:dccrldpSigSocketIfIndex,_V:dccrldpSigSessionBufPoolSize,_W:dccrldpSigEMBufPoolSize,_X:dccrldpSigAMBufPoolSize,_Y:dccrldpSigAdminStatus,_Z:dccrldpSigOperStatus,_J:dccrldpSigRowStatus,_a:dccrldpSigUseI3Interface,_b:dccrldpSigConformanceFlags,_c:dccrldpSigUseIPv6Transport,_d:dccrldpSigSessStatusTrapEnable,_e:dccrldpSigSessThreshTrapEnable,_f:dccrldpSigPathVecLimitTrapEnable,_g:dccrldpSigBfdProviderIndex,'dccrldpPmTable':dccrldpPmTable,'dccrldpPmEntry':dccrldpPmEntry,_Q:dccrldpPmIndex,_U:dccrldpPmLsrIndex,_h:dccrldpPmLdpEntityAutoCreate,_i:dccrldpPmLdpEntityAutoStart,_j:dccrldpPmLdpEntityReuse,_k:dccrldpPmLdpVersion,_l:dccrldpPmUseLdpFt,_m:dccrldpPmAsNumber,_n:dccrldpPmIprBufPoolSize,_o:dccrldpPmLdpSupported,_p:dccrldpPmCrLdpSupported,_q:dccrldpPmQueryFECSupported,_r:dccrldpPmAdminStatus,_s:dccrldpPmOperStatus,_K:dccrldpPmRowStatus,_t:dccrldpPmRestartCapable,_u:dccrldpPmReconnectTime,_v:dccrldpPmRecoveryTime,_w:dccrldpPmMaxPeerReconnect,_x:dccrldpPmMaxPeerRecovery,_y:dccrldpPmAdjDwnHoldTime,_z:dccrldpPmOutSegProgOrder,_A0:dccrldpPmSupportIpv6,_A1:dccrldpPmPolicySupportFlags,_A2:dccrldpPmCheckOutSegIntfaceStat,_A3:dccrldpPmLdpEntityCreateNhrLdb,_A4:dccrldpPmLdpEntityCreatePsiJoin,_A5:dccrldpPmRedundancySwitchIntvl,_A6:dccrldpPmLabelWithdrawDelay,_A7:dccrldpPmImplicitXcVcFecs,_A8:dccrldpPmWthdrwDownstreamLbl,_A9:dccrldpPmIngressReleaseDelay,_AA:dccrldpPmPwFastUpstreamRelease,'dccrldpConformance':dccrldpConformance,'dccrldpCompliances':dccrldpCompliances,'dccrldpMibCompliance':dccrldpMibCompliance,'dccrldpGroups':dccrldpGroups,_AB:dccrldpMandatoryGroup,_AC:dccrldpOptionalGroup})