_q='mbgMgmtNotificationGroup'
_p='mbgMgmtObjectsGroup'
_o='mbgMgmtTrapHeartbeat'
_n='mbgMgmtTrapNtpMainState'
_m='mbgMgmtNtpPeerJitter'
_l='mbgMgmtNtpPeerDispersion'
_k='mbgMgmtNtpPeerDelay'
_j='mbgMgmtNtpPeerOffset'
_i='mbgMgmtNtpPeerStateTime'
_h='mbgMgmtNtpPeerStateAssocId'
_g='mbgMgmtNtpPeerStateReach'
_f='mbgMgmtNtpPeerStateStratum'
_e='mbgMgmtNtpPeerStateRefId'
_d='mbgMgmtNtpPeerStateValid'
_c='mbgMgmtNtpRefclkJitter'
_b='mbgMgmtNtpRefclkDispersion'
_a='mbgMgmtNtpRefclkDelay'
_Z='mbgMgmtNtpRefclkOffset'
_Y='mbgMgmtNtpRefclkStateTime'
_X='mbgMgmtNtpRefclkStateAssocId'
_W='mbgMgmtNtpRefclkStateReach'
_V='mbgMgmtNtpRefclkStateStratum'
_U='mbgMgmtNtpRefclkStateRefId'
_T='mbgMgmtNtpRefclkStateValid'
_S='mbgMgmtNtpSysStateRootDispersion'
_R='mbgMgmtNtpSysStateRootDelay'
_Q='mbgMgmtNtpSysStateTime'
_P='mbgMgmtNtpSysStateAssocId'
_O='mbgMgmtNtpSysStateLeapIndicator'
_N='mbgMgmtNtpSysStateStratum'
_M='mbgMgmtNtpSysStateRefId'
_L='mbgMgmtNtpPeerStateIndex'
_K='not-accessible'
_J='mbgMgmtNtpRefclkStateIndex'
_I='mbgMgmtNtpSysStateMain'
_H='sysName'
_G='SNMPv2-MIB'
_F='ns'
_E='us'
_D='Integer32'
_C='read-only'
_B='MBG-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mbgSnmpRoot,=mibBuilder.importSymbols('MBG-SNMP-ROOT-MIB','mbgSnmpRoot')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mbgManagement=ModuleIdentity((1,3,6,1,4,1,5597,7))
if mibBuilder.loadTexts:mbgManagement.setRevisions(('2017-11-09 07:07',))
class NtpTimestamp(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(27,27));fixedLength=27
class YesNo(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
class NtpReach(TextualConvention,Integer32):status=_A;displayHint='o'
_MbgMgmtObjects_ObjectIdentity=ObjectIdentity
mbgMgmtObjects=_MbgMgmtObjects_ObjectIdentity((1,3,6,1,4,1,5597,7,1))
_MbgMgmtNtp_ObjectIdentity=ObjectIdentity
mbgMgmtNtp=_MbgMgmtNtp_ObjectIdentity((1,3,6,1,4,1,5597,7,1,1))
_MbgMgmtNtpConfig_ObjectIdentity=ObjectIdentity
mbgMgmtNtpConfig=_MbgMgmtNtpConfig_ObjectIdentity((1,3,6,1,4,1,5597,7,1,1,1))
_MbgMgmtNtpState_ObjectIdentity=ObjectIdentity
mbgMgmtNtpState=_MbgMgmtNtpState_ObjectIdentity((1,3,6,1,4,1,5597,7,1,1,2))
_MbgMgmtNtpSysState_ObjectIdentity=ObjectIdentity
mbgMgmtNtpSysState=_MbgMgmtNtpSysState_ObjectIdentity((1,3,6,1,4,1,5597,7,1,1,2,1))
class _MbgMgmtNtpSysStateMain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('init',0),('sync',1),('notSync',2),('stopped',3)))
_MbgMgmtNtpSysStateMain_Type.__name__=_D
_MbgMgmtNtpSysStateMain_Object=MibScalar
mbgMgmtNtpSysStateMain=_MbgMgmtNtpSysStateMain_Object((1,3,6,1,4,1,5597,7,1,1,2,1,1),_MbgMgmtNtpSysStateMain_Type())
mbgMgmtNtpSysStateMain.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateMain.setStatus(_A)
_MbgMgmtNtpSysStateRefId_Type=DisplayString
_MbgMgmtNtpSysStateRefId_Object=MibScalar
mbgMgmtNtpSysStateRefId=_MbgMgmtNtpSysStateRefId_Object((1,3,6,1,4,1,5597,7,1,1,2,1,2),_MbgMgmtNtpSysStateRefId_Type())
mbgMgmtNtpSysStateRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateRefId.setStatus(_A)
class _MbgMgmtNtpSysStateStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MbgMgmtNtpSysStateStratum_Type.__name__=_D
_MbgMgmtNtpSysStateStratum_Object=MibScalar
mbgMgmtNtpSysStateStratum=_MbgMgmtNtpSysStateStratum_Object((1,3,6,1,4,1,5597,7,1,1,2,1,3),_MbgMgmtNtpSysStateStratum_Type())
mbgMgmtNtpSysStateStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateStratum.setStatus(_A)
class _MbgMgmtNtpSysStateLeapIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('addSecond',1),('deleteSecond',2),('alarm',3)))
_MbgMgmtNtpSysStateLeapIndicator_Type.__name__=_D
_MbgMgmtNtpSysStateLeapIndicator_Object=MibScalar
mbgMgmtNtpSysStateLeapIndicator=_MbgMgmtNtpSysStateLeapIndicator_Object((1,3,6,1,4,1,5597,7,1,1,2,1,4),_MbgMgmtNtpSysStateLeapIndicator_Type())
mbgMgmtNtpSysStateLeapIndicator.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateLeapIndicator.setStatus(_A)
_MbgMgmtNtpSysStateAssocId_Type=Unsigned32
_MbgMgmtNtpSysStateAssocId_Object=MibScalar
mbgMgmtNtpSysStateAssocId=_MbgMgmtNtpSysStateAssocId_Object((1,3,6,1,4,1,5597,7,1,1,2,1,5),_MbgMgmtNtpSysStateAssocId_Type())
mbgMgmtNtpSysStateAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateAssocId.setStatus(_A)
_MbgMgmtNtpSysStateTime_Type=NtpTimestamp
_MbgMgmtNtpSysStateTime_Object=MibScalar
mbgMgmtNtpSysStateTime=_MbgMgmtNtpSysStateTime_Object((1,3,6,1,4,1,5597,7,1,1,2,1,6),_MbgMgmtNtpSysStateTime_Type())
mbgMgmtNtpSysStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateTime.setStatus(_A)
_MbgMgmtNtpSysStateRootDelay_Type=Integer32
_MbgMgmtNtpSysStateRootDelay_Object=MibScalar
mbgMgmtNtpSysStateRootDelay=_MbgMgmtNtpSysStateRootDelay_Object((1,3,6,1,4,1,5597,7,1,1,2,1,7),_MbgMgmtNtpSysStateRootDelay_Type())
mbgMgmtNtpSysStateRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateRootDelay.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateRootDelay.setUnits(_E)
_MbgMgmtNtpSysStateRootDispersion_Type=Integer32
_MbgMgmtNtpSysStateRootDispersion_Object=MibScalar
mbgMgmtNtpSysStateRootDispersion=_MbgMgmtNtpSysStateRootDispersion_Object((1,3,6,1,4,1,5597,7,1,1,2,1,8),_MbgMgmtNtpSysStateRootDispersion_Type())
mbgMgmtNtpSysStateRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateRootDispersion.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpSysStateRootDispersion.setUnits(_E)
_MbgMgmtNtpRefclkStates_ObjectIdentity=ObjectIdentity
mbgMgmtNtpRefclkStates=_MbgMgmtNtpRefclkStates_ObjectIdentity((1,3,6,1,4,1,5597,7,1,1,2,2))
_MbgMgmtNtpRefclkStateTable_Object=MibTable
mbgMgmtNtpRefclkStateTable=_MbgMgmtNtpRefclkStateTable_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1))
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateTable.setStatus(_A)
_MbgMgmtNtpRefclkStateTableEntry_Object=MibTableRow
mbgMgmtNtpRefclkStateTableEntry=_MbgMgmtNtpRefclkStateTableEntry_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1))
mbgMgmtNtpRefclkStateTableEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateTableEntry.setStatus(_A)
_MbgMgmtNtpRefclkStateIndex_Type=Unsigned32
_MbgMgmtNtpRefclkStateIndex_Object=MibTableColumn
mbgMgmtNtpRefclkStateIndex=_MbgMgmtNtpRefclkStateIndex_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,1),_MbgMgmtNtpRefclkStateIndex_Type())
mbgMgmtNtpRefclkStateIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateIndex.setStatus(_A)
_MbgMgmtNtpRefclkStateValid_Type=YesNo
_MbgMgmtNtpRefclkStateValid_Object=MibTableColumn
mbgMgmtNtpRefclkStateValid=_MbgMgmtNtpRefclkStateValid_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,2),_MbgMgmtNtpRefclkStateValid_Type())
mbgMgmtNtpRefclkStateValid.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateValid.setStatus(_A)
_MbgMgmtNtpRefclkStateRefId_Type=DisplayString
_MbgMgmtNtpRefclkStateRefId_Object=MibTableColumn
mbgMgmtNtpRefclkStateRefId=_MbgMgmtNtpRefclkStateRefId_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,3),_MbgMgmtNtpRefclkStateRefId_Type())
mbgMgmtNtpRefclkStateRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateRefId.setStatus(_A)
class _MbgMgmtNtpRefclkStateStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_MbgMgmtNtpRefclkStateStratum_Type.__name__=_D
_MbgMgmtNtpRefclkStateStratum_Object=MibTableColumn
mbgMgmtNtpRefclkStateStratum=_MbgMgmtNtpRefclkStateStratum_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,4),_MbgMgmtNtpRefclkStateStratum_Type())
mbgMgmtNtpRefclkStateStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateStratum.setStatus(_A)
_MbgMgmtNtpRefclkStateReach_Type=NtpReach
_MbgMgmtNtpRefclkStateReach_Object=MibTableColumn
mbgMgmtNtpRefclkStateReach=_MbgMgmtNtpRefclkStateReach_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,5),_MbgMgmtNtpRefclkStateReach_Type())
mbgMgmtNtpRefclkStateReach.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateReach.setStatus(_A)
_MbgMgmtNtpRefclkStateAssocId_Type=Integer32
_MbgMgmtNtpRefclkStateAssocId_Object=MibTableColumn
mbgMgmtNtpRefclkStateAssocId=_MbgMgmtNtpRefclkStateAssocId_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,6),_MbgMgmtNtpRefclkStateAssocId_Type())
mbgMgmtNtpRefclkStateAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateAssocId.setStatus(_A)
_MbgMgmtNtpRefclkStateTime_Type=NtpTimestamp
_MbgMgmtNtpRefclkStateTime_Object=MibTableColumn
mbgMgmtNtpRefclkStateTime=_MbgMgmtNtpRefclkStateTime_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,7),_MbgMgmtNtpRefclkStateTime_Type())
mbgMgmtNtpRefclkStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkStateTime.setStatus(_A)
_MbgMgmtNtpRefclkOffset_Type=Integer32
_MbgMgmtNtpRefclkOffset_Object=MibTableColumn
mbgMgmtNtpRefclkOffset=_MbgMgmtNtpRefclkOffset_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,8),_MbgMgmtNtpRefclkOffset_Type())
mbgMgmtNtpRefclkOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkOffset.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkOffset.setUnits(_F)
_MbgMgmtNtpRefclkDelay_Type=Integer32
_MbgMgmtNtpRefclkDelay_Object=MibTableColumn
mbgMgmtNtpRefclkDelay=_MbgMgmtNtpRefclkDelay_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,9),_MbgMgmtNtpRefclkDelay_Type())
mbgMgmtNtpRefclkDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkDelay.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkDelay.setUnits(_F)
_MbgMgmtNtpRefclkDispersion_Type=Integer32
_MbgMgmtNtpRefclkDispersion_Object=MibTableColumn
mbgMgmtNtpRefclkDispersion=_MbgMgmtNtpRefclkDispersion_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,10),_MbgMgmtNtpRefclkDispersion_Type())
mbgMgmtNtpRefclkDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkDispersion.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkDispersion.setUnits(_E)
_MbgMgmtNtpRefclkJitter_Type=Integer32
_MbgMgmtNtpRefclkJitter_Object=MibTableColumn
mbgMgmtNtpRefclkJitter=_MbgMgmtNtpRefclkJitter_Object((1,3,6,1,4,1,5597,7,1,1,2,2,1,1,11),_MbgMgmtNtpRefclkJitter_Type())
mbgMgmtNtpRefclkJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkJitter.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpRefclkJitter.setUnits(_E)
_MbgMgmtNtpPeerStates_ObjectIdentity=ObjectIdentity
mbgMgmtNtpPeerStates=_MbgMgmtNtpPeerStates_ObjectIdentity((1,3,6,1,4,1,5597,7,1,1,2,3))
_MbgMgmtNtpPeerStateTable_Object=MibTable
mbgMgmtNtpPeerStateTable=_MbgMgmtNtpPeerStateTable_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1))
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateTable.setStatus(_A)
_MbgMgmtNtpPeerStateTableEntry_Object=MibTableRow
mbgMgmtNtpPeerStateTableEntry=_MbgMgmtNtpPeerStateTableEntry_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1))
mbgMgmtNtpPeerStateTableEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateTableEntry.setStatus(_A)
_MbgMgmtNtpPeerStateIndex_Type=Unsigned32
_MbgMgmtNtpPeerStateIndex_Object=MibTableColumn
mbgMgmtNtpPeerStateIndex=_MbgMgmtNtpPeerStateIndex_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,1),_MbgMgmtNtpPeerStateIndex_Type())
mbgMgmtNtpPeerStateIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateIndex.setStatus(_A)
_MbgMgmtNtpPeerStateValid_Type=YesNo
_MbgMgmtNtpPeerStateValid_Object=MibTableColumn
mbgMgmtNtpPeerStateValid=_MbgMgmtNtpPeerStateValid_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,2),_MbgMgmtNtpPeerStateValid_Type())
mbgMgmtNtpPeerStateValid.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateValid.setStatus(_A)
_MbgMgmtNtpPeerStateRefId_Type=DisplayString
_MbgMgmtNtpPeerStateRefId_Object=MibTableColumn
mbgMgmtNtpPeerStateRefId=_MbgMgmtNtpPeerStateRefId_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,3),_MbgMgmtNtpPeerStateRefId_Type())
mbgMgmtNtpPeerStateRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateRefId.setStatus(_A)
class _MbgMgmtNtpPeerStateStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_MbgMgmtNtpPeerStateStratum_Type.__name__=_D
_MbgMgmtNtpPeerStateStratum_Object=MibTableColumn
mbgMgmtNtpPeerStateStratum=_MbgMgmtNtpPeerStateStratum_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,4),_MbgMgmtNtpPeerStateStratum_Type())
mbgMgmtNtpPeerStateStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateStratum.setStatus(_A)
_MbgMgmtNtpPeerStateReach_Type=NtpReach
_MbgMgmtNtpPeerStateReach_Object=MibTableColumn
mbgMgmtNtpPeerStateReach=_MbgMgmtNtpPeerStateReach_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,5),_MbgMgmtNtpPeerStateReach_Type())
mbgMgmtNtpPeerStateReach.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateReach.setStatus(_A)
_MbgMgmtNtpPeerStateAssocId_Type=Integer32
_MbgMgmtNtpPeerStateAssocId_Object=MibTableColumn
mbgMgmtNtpPeerStateAssocId=_MbgMgmtNtpPeerStateAssocId_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,6),_MbgMgmtNtpPeerStateAssocId_Type())
mbgMgmtNtpPeerStateAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateAssocId.setStatus(_A)
_MbgMgmtNtpPeerStateTime_Type=NtpTimestamp
_MbgMgmtNtpPeerStateTime_Object=MibTableColumn
mbgMgmtNtpPeerStateTime=_MbgMgmtNtpPeerStateTime_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,7),_MbgMgmtNtpPeerStateTime_Type())
mbgMgmtNtpPeerStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerStateTime.setStatus(_A)
_MbgMgmtNtpPeerOffset_Type=Integer32
_MbgMgmtNtpPeerOffset_Object=MibTableColumn
mbgMgmtNtpPeerOffset=_MbgMgmtNtpPeerOffset_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,8),_MbgMgmtNtpPeerOffset_Type())
mbgMgmtNtpPeerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerOffset.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpPeerOffset.setUnits(_F)
_MbgMgmtNtpPeerDelay_Type=Integer32
_MbgMgmtNtpPeerDelay_Object=MibTableColumn
mbgMgmtNtpPeerDelay=_MbgMgmtNtpPeerDelay_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,9),_MbgMgmtNtpPeerDelay_Type())
mbgMgmtNtpPeerDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerDelay.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpPeerDelay.setUnits(_F)
_MbgMgmtNtpPeerDispersion_Type=Integer32
_MbgMgmtNtpPeerDispersion_Object=MibTableColumn
mbgMgmtNtpPeerDispersion=_MbgMgmtNtpPeerDispersion_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,10),_MbgMgmtNtpPeerDispersion_Type())
mbgMgmtNtpPeerDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerDispersion.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpPeerDispersion.setUnits(_E)
_MbgMgmtNtpPeerJitter_Type=Integer32
_MbgMgmtNtpPeerJitter_Object=MibTableColumn
mbgMgmtNtpPeerJitter=_MbgMgmtNtpPeerJitter_Object((1,3,6,1,4,1,5597,7,1,1,2,3,1,1,11),_MbgMgmtNtpPeerJitter_Type())
mbgMgmtNtpPeerJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMgmtNtpPeerJitter.setStatus(_A)
if mibBuilder.loadTexts:mbgMgmtNtpPeerJitter.setUnits(_E)
_MbgMgmtNotifications_ObjectIdentity=ObjectIdentity
mbgMgmtNotifications=_MbgMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,5597,7,2))
_MbgMgmtTraps_ObjectIdentity=ObjectIdentity
mbgMgmtTraps=_MbgMgmtTraps_ObjectIdentity((1,3,6,1,4,1,5597,7,2,0))
_MbgMgmtConformance_ObjectIdentity=ObjectIdentity
mbgMgmtConformance=_MbgMgmtConformance_ObjectIdentity((1,3,6,1,4,1,5597,7,90))
_MbgMgmtCompliances_ObjectIdentity=ObjectIdentity
mbgMgmtCompliances=_MbgMgmtCompliances_ObjectIdentity((1,3,6,1,4,1,5597,7,90,1))
_MbgMgmtGroups_ObjectIdentity=ObjectIdentity
mbgMgmtGroups=_MbgMgmtGroups_ObjectIdentity((1,3,6,1,4,1,5597,7,90,2))
mbgMgmtObjectsGroup=ObjectGroup((1,3,6,1,4,1,5597,7,90,2,1))
mbgMgmtObjectsGroup.setObjects(*((_B,_I),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:mbgMgmtObjectsGroup.setStatus(_A)
mbgMgmtTrapNtpMainState=NotificationType((1,3,6,1,4,1,5597,7,2,0,1))
mbgMgmtTrapNtpMainState.setObjects(*((_B,_I),(_G,_H)))
if mibBuilder.loadTexts:mbgMgmtTrapNtpMainState.setStatus(_A)
mbgMgmtTrapHeartbeat=NotificationType((1,3,6,1,4,1,5597,7,2,0,2))
mbgMgmtTrapHeartbeat.setObjects((_G,_H))
if mibBuilder.loadTexts:mbgMgmtTrapHeartbeat.setStatus(_A)
mbgMgmtNotificationGroup=NotificationGroup((1,3,6,1,4,1,5597,7,90,2,2))
mbgMgmtNotificationGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:mbgMgmtNotificationGroup.setStatus(_A)
mbgMgmtCompliance=ModuleCompliance((1,3,6,1,4,1,5597,7,90,1,1))
mbgMgmtCompliance.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:mbgMgmtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NtpTimestamp':NtpTimestamp,'YesNo':YesNo,'NtpReach':NtpReach,'mbgManagement':mbgManagement,'mbgMgmtObjects':mbgMgmtObjects,'mbgMgmtNtp':mbgMgmtNtp,'mbgMgmtNtpConfig':mbgMgmtNtpConfig,'mbgMgmtNtpState':mbgMgmtNtpState,'mbgMgmtNtpSysState':mbgMgmtNtpSysState,_I:mbgMgmtNtpSysStateMain,_M:mbgMgmtNtpSysStateRefId,_N:mbgMgmtNtpSysStateStratum,_O:mbgMgmtNtpSysStateLeapIndicator,_P:mbgMgmtNtpSysStateAssocId,_Q:mbgMgmtNtpSysStateTime,_R:mbgMgmtNtpSysStateRootDelay,_S:mbgMgmtNtpSysStateRootDispersion,'mbgMgmtNtpRefclkStates':mbgMgmtNtpRefclkStates,'mbgMgmtNtpRefclkStateTable':mbgMgmtNtpRefclkStateTable,'mbgMgmtNtpRefclkStateTableEntry':mbgMgmtNtpRefclkStateTableEntry,_J:mbgMgmtNtpRefclkStateIndex,_T:mbgMgmtNtpRefclkStateValid,_U:mbgMgmtNtpRefclkStateRefId,_V:mbgMgmtNtpRefclkStateStratum,_W:mbgMgmtNtpRefclkStateReach,_X:mbgMgmtNtpRefclkStateAssocId,_Y:mbgMgmtNtpRefclkStateTime,_Z:mbgMgmtNtpRefclkOffset,_a:mbgMgmtNtpRefclkDelay,_b:mbgMgmtNtpRefclkDispersion,_c:mbgMgmtNtpRefclkJitter,'mbgMgmtNtpPeerStates':mbgMgmtNtpPeerStates,'mbgMgmtNtpPeerStateTable':mbgMgmtNtpPeerStateTable,'mbgMgmtNtpPeerStateTableEntry':mbgMgmtNtpPeerStateTableEntry,_L:mbgMgmtNtpPeerStateIndex,_d:mbgMgmtNtpPeerStateValid,_e:mbgMgmtNtpPeerStateRefId,_f:mbgMgmtNtpPeerStateStratum,_g:mbgMgmtNtpPeerStateReach,_h:mbgMgmtNtpPeerStateAssocId,_i:mbgMgmtNtpPeerStateTime,_j:mbgMgmtNtpPeerOffset,_k:mbgMgmtNtpPeerDelay,_l:mbgMgmtNtpPeerDispersion,_m:mbgMgmtNtpPeerJitter,'mbgMgmtNotifications':mbgMgmtNotifications,'mbgMgmtTraps':mbgMgmtTraps,_n:mbgMgmtTrapNtpMainState,_o:mbgMgmtTrapHeartbeat,'mbgMgmtConformance':mbgMgmtConformance,'mbgMgmtCompliances':mbgMgmtCompliances,'mbgMgmtCompliance':mbgMgmtCompliance,'mbgMgmtGroups':mbgMgmtGroups,_p:mbgMgmtObjectsGroup,_q:mbgMgmtNotificationGroup})