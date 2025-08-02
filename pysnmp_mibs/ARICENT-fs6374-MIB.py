_b='fs6374DMSeqNum'
_a='fs6374LMSeqNum'
_Z='inferred'
_Y='direct'
_X='disabled'
_W='enabled'
_V='disable'
_U='enable'
_T='fs6374DMSessionId'
_S='fs6374LMSessionId'
_R='proActive'
_Q='onDemand'
_P='twoway'
_O='oneway'
_N='Fs6374TransmitStatus'
_M='FS6374TimeStampFormat'
_L='TruthValue'
_K='not-accessible'
_J='fs6374ServiceName'
_I='OctetString'
_H='fs6374ContextId'
_G='Unsigned32'
_F='milliseconds'
_E='Integer32'
_D='ARICENT-fs6374-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
fs6374MIB=ModuleIdentity((1,3,6,1,4,1,29601,2,107))
if mibBuilder.loadTexts:fs6374MIB.setRevisions(('2012-09-05 00:00',))
class FS6374Traps(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('none',0),('bTrapUnsupportedVersion',1),('bTrapUnsupportedControlCode',2),('bTrapUnsupportedDataFormat',3),('bTrapConnectionMismatch',4),('bTrapUnsupportedMandatoryTLVObject',5),('bTrapUnsupportedTimeStamp',6),('bTrapResponseTimeout',7),('bTrapResourceUnavailable',8),('bTrapTestAbort',9),('bTrapProactiveTestRestart',10),('bTrapUnsupportedQueryInterval',11)))
class FS6374TimeStampFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('timeStampFormatNull',0),('timeStampFormatSequence',1),('timeStampFormatNTP',2),('timeStampFormatIEEE1588',3)))
class Fs6374TransmitStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('start',1),('stop',2),('ready',3),('notReady',4)))
class FS6374TimeRepresentation(TextualConvention,OctetString):status=_A;displayHint='4d:4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class FS6374SuppTimeStampFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tsFormatNTP',1),('tsFormatIEEE1588',2)))
_Fs6374ServiceConfig_ObjectIdentity=ObjectIdentity
fs6374ServiceConfig=_Fs6374ServiceConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,107,1))
_Fs6374ServiceConfigTable_Object=MibTable
fs6374ServiceConfigTable=_Fs6374ServiceConfigTable_Object((1,3,6,1,4,1,29601,2,107,1,1))
if mibBuilder.loadTexts:fs6374ServiceConfigTable.setStatus(_A)
_Fs6374ServiceConfigEntry_Object=MibTableRow
fs6374ServiceConfigEntry=_Fs6374ServiceConfigEntry_Object((1,3,6,1,4,1,29601,2,107,1,1,1))
fs6374ServiceConfigEntry.setIndexNames((0,_D,_H),(0,_D,_J))
if mibBuilder.loadTexts:fs6374ServiceConfigEntry.setStatus(_A)
_Fs6374ContextId_Type=Unsigned32
_Fs6374ContextId_Object=MibTableColumn
fs6374ContextId=_Fs6374ContextId_Object((1,3,6,1,4,1,29601,2,107,1,1,1,1),_Fs6374ContextId_Type())
fs6374ContextId.setMaxAccess(_K)
if mibBuilder.loadTexts:fs6374ContextId.setStatus(_A)
class _Fs6374ServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Fs6374ServiceName_Type.__name__=_I
_Fs6374ServiceName_Object=MibTableColumn
fs6374ServiceName=_Fs6374ServiceName_Object((1,3,6,1,4,1,29601,2,107,1,1,1,2),_Fs6374ServiceName_Type())
fs6374ServiceName.setMaxAccess(_K)
if mibBuilder.loadTexts:fs6374ServiceName.setStatus(_A)
_Fs6374MplsPathType_Type=Integer32
_Fs6374MplsPathType_Object=MibTableColumn
fs6374MplsPathType=_Fs6374MplsPathType_Object((1,3,6,1,4,1,29601,2,107,1,1,1,3),_Fs6374MplsPathType_Type())
fs6374MplsPathType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374MplsPathType.setStatus(_A)
_Fs6374FwdTnlIdOrPwId_Type=Unsigned32
_Fs6374FwdTnlIdOrPwId_Object=MibTableColumn
fs6374FwdTnlIdOrPwId=_Fs6374FwdTnlIdOrPwId_Object((1,3,6,1,4,1,29601,2,107,1,1,1,4),_Fs6374FwdTnlIdOrPwId_Type())
fs6374FwdTnlIdOrPwId.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374FwdTnlIdOrPwId.setStatus(_A)
_Fs6374RevTnlId_Type=Unsigned32
_Fs6374RevTnlId_Object=MibTableColumn
fs6374RevTnlId=_Fs6374RevTnlId_Object((1,3,6,1,4,1,29601,2,107,1,1,1,5),_Fs6374RevTnlId_Type())
fs6374RevTnlId.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374RevTnlId.setStatus(_A)
class _Fs6374SrcIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Fs6374SrcIpAddr_Type.__name__=_I
_Fs6374SrcIpAddr_Object=MibTableColumn
fs6374SrcIpAddr=_Fs6374SrcIpAddr_Object((1,3,6,1,4,1,29601,2,107,1,1,1,6),_Fs6374SrcIpAddr_Type())
fs6374SrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374SrcIpAddr.setStatus(_A)
class _Fs6374DestIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Fs6374DestIpAddr_Type.__name__=_I
_Fs6374DestIpAddr_Object=MibTableColumn
fs6374DestIpAddr=_Fs6374DestIpAddr_Object((1,3,6,1,4,1,29601,2,107,1,1,1,7),_Fs6374DestIpAddr_Type())
fs6374DestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DestIpAddr.setStatus(_A)
class _Fs6374EncapType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('withGALHEADER',1),('withoutGALHEADER',2)))
_Fs6374EncapType_Type.__name__=_E
_Fs6374EncapType_Object=MibTableColumn
fs6374EncapType=_Fs6374EncapType_Object((1,3,6,1,4,1,29601,2,107,1,1,1,8),_Fs6374EncapType_Type())
fs6374EncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374EncapType.setStatus(_A)
class _Fs6374TrafficClass_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Fs6374TrafficClass_Type.__name__=_E
_Fs6374TrafficClass_Object=MibTableColumn
fs6374TrafficClass=_Fs6374TrafficClass_Object((1,3,6,1,4,1,29601,2,107,1,1,1,9),_Fs6374TrafficClass_Type())
fs6374TrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374TrafficClass.setStatus(_A)
_Fs6374RowStatus_Type=RowStatus
_Fs6374RowStatus_Object=MibTableColumn
fs6374RowStatus=_Fs6374RowStatus_Object((1,3,6,1,4,1,29601,2,107,1,1,1,10),_Fs6374RowStatus_Type())
fs6374RowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fs6374RowStatus.setStatus(_A)
class _Fs6374DyadicMeasurement_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_Fs6374DyadicMeasurement_Type.__name__=_E
_Fs6374DyadicMeasurement_Object=MibTableColumn
fs6374DyadicMeasurement=_Fs6374DyadicMeasurement_Object((1,3,6,1,4,1,29601,2,107,1,1,1,11),_Fs6374DyadicMeasurement_Type())
fs6374DyadicMeasurement.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DyadicMeasurement.setStatus(_A)
class _Fs6374TSFNegotiation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_Fs6374TSFNegotiation_Type.__name__=_E
_Fs6374TSFNegotiation_Object=MibTableColumn
fs6374TSFNegotiation=_Fs6374TSFNegotiation_Object((1,3,6,1,4,1,29601,2,107,1,1,1,12),_Fs6374TSFNegotiation_Type())
fs6374TSFNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374TSFNegotiation.setStatus(_A)
_Fs6374TSNegotiatedFormat_Type=Unsigned32
_Fs6374TSNegotiatedFormat_Object=MibTableColumn
fs6374TSNegotiatedFormat=_Fs6374TSNegotiatedFormat_Object((1,3,6,1,4,1,29601,2,107,1,1,1,13),_Fs6374TSNegotiatedFormat_Type())
fs6374TSNegotiatedFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374TSNegotiatedFormat.setStatus(_A)
class _Fs6374DyadicProactiveRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_Fs6374DyadicProactiveRole_Type.__name__=_E
_Fs6374DyadicProactiveRole_Object=MibTableColumn
fs6374DyadicProactiveRole=_Fs6374DyadicProactiveRole_Object((1,3,6,1,4,1,29601,2,107,1,1,1,14),_Fs6374DyadicProactiveRole_Type())
fs6374DyadicProactiveRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DyadicProactiveRole.setStatus(_A)
class _Fs6374QueryTransmitRetryCount_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_Fs6374QueryTransmitRetryCount_Type.__name__=_G
_Fs6374QueryTransmitRetryCount_Object=MibTableColumn
fs6374QueryTransmitRetryCount=_Fs6374QueryTransmitRetryCount_Object((1,3,6,1,4,1,29601,2,107,1,1,1,15),_Fs6374QueryTransmitRetryCount_Type())
fs6374QueryTransmitRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374QueryTransmitRetryCount.setStatus(_A)
class _Fs6374SessionIntervalQueryStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_Fs6374SessionIntervalQueryStatus_Type.__name__=_E
_Fs6374SessionIntervalQueryStatus_Object=MibTableColumn
fs6374SessionIntervalQueryStatus=_Fs6374SessionIntervalQueryStatus_Object((1,3,6,1,4,1,29601,2,107,1,1,1,16),_Fs6374SessionIntervalQueryStatus_Type())
fs6374SessionIntervalQueryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374SessionIntervalQueryStatus.setStatus(_A)
class _Fs6374MinReceptionIntervalInMilliseconds_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_Fs6374MinReceptionIntervalInMilliseconds_Type.__name__=_G
_Fs6374MinReceptionIntervalInMilliseconds_Object=MibTableColumn
fs6374MinReceptionIntervalInMilliseconds=_Fs6374MinReceptionIntervalInMilliseconds_Object((1,3,6,1,4,1,29601,2,107,1,1,1,17),_Fs6374MinReceptionIntervalInMilliseconds_Type())
fs6374MinReceptionIntervalInMilliseconds.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374MinReceptionIntervalInMilliseconds.setStatus(_A)
if mibBuilder.loadTexts:fs6374MinReceptionIntervalInMilliseconds.setUnits(_F)
_Fs6374ParamsConfig_ObjectIdentity=ObjectIdentity
fs6374ParamsConfig=_Fs6374ParamsConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,107,2))
_Fs6374ParamsConfigTable_Object=MibTable
fs6374ParamsConfigTable=_Fs6374ParamsConfigTable_Object((1,3,6,1,4,1,29601,2,107,2,1))
if mibBuilder.loadTexts:fs6374ParamsConfigTable.setStatus(_A)
_Fs6374ParamsConfigTableEntry_Object=MibTableRow
fs6374ParamsConfigTableEntry=_Fs6374ParamsConfigTableEntry_Object((1,3,6,1,4,1,29601,2,107,2,1,1))
fs6374ParamsConfigTableEntry.setIndexNames((0,_D,_H),(0,_D,_J))
if mibBuilder.loadTexts:fs6374ParamsConfigTableEntry.setStatus(_A)
class _Fs6374LMType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_Fs6374LMType_Type.__name__=_E
_Fs6374LMType_Object=MibTableColumn
fs6374LMType=_Fs6374LMType_Object((1,3,6,1,4,1,29601,2,107,2,1,1,1),_Fs6374LMType_Type())
fs6374LMType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMType.setStatus(_A)
class _Fs6374LMMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_Fs6374LMMethod_Type.__name__=_E
_Fs6374LMMethod_Object=MibTableColumn
fs6374LMMethod=_Fs6374LMMethod_Object((1,3,6,1,4,1,29601,2,107,2,1,1,2),_Fs6374LMMethod_Type())
fs6374LMMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMMethod.setStatus(_A)
class _Fs6374LMMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_Fs6374LMMode_Type.__name__=_E
_Fs6374LMMode_Object=MibTableColumn
fs6374LMMode=_Fs6374LMMode_Object((1,3,6,1,4,1,29601,2,107,2,1,1,3),_Fs6374LMMode_Type())
fs6374LMMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMMode.setStatus(_A)
class _Fs6374LMNoOfMessages_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Fs6374LMNoOfMessages_Type.__name__=_G
_Fs6374LMNoOfMessages_Object=MibTableColumn
fs6374LMNoOfMessages=_Fs6374LMNoOfMessages_Object((1,3,6,1,4,1,29601,2,107,2,1,1,4),_Fs6374LMNoOfMessages_Type())
fs6374LMNoOfMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMNoOfMessages.setStatus(_A)
class _Fs6374LMTimeIntervalInMilliseconds_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_Fs6374LMTimeIntervalInMilliseconds_Type.__name__=_G
_Fs6374LMTimeIntervalInMilliseconds_Object=MibTableColumn
fs6374LMTimeIntervalInMilliseconds=_Fs6374LMTimeIntervalInMilliseconds_Object((1,3,6,1,4,1,29601,2,107,2,1,1,5),_Fs6374LMTimeIntervalInMilliseconds_Type())
fs6374LMTimeIntervalInMilliseconds.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMTimeIntervalInMilliseconds.setStatus(_A)
if mibBuilder.loadTexts:fs6374LMTimeIntervalInMilliseconds.setUnits(_F)
class _Fs6374LMTimeStampFormat_Type(FS6374TimeStampFormat):defaultValue=3
_Fs6374LMTimeStampFormat_Type.__name__=_M
_Fs6374LMTimeStampFormat_Object=MibTableColumn
fs6374LMTimeStampFormat=_Fs6374LMTimeStampFormat_Object((1,3,6,1,4,1,29601,2,107,2,1,1,6),_Fs6374LMTimeStampFormat_Type())
fs6374LMTimeStampFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMTimeStampFormat.setStatus(_A)
class _Fs6374LMTransmitStatus_Type(Fs6374TransmitStatus):defaultValue=3
_Fs6374LMTransmitStatus_Type.__name__=_N
_Fs6374LMTransmitStatus_Object=MibTableColumn
fs6374LMTransmitStatus=_Fs6374LMTransmitStatus_Object((1,3,6,1,4,1,29601,2,107,2,1,1,7),_Fs6374LMTransmitStatus_Type())
fs6374LMTransmitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMTransmitStatus.setStatus(_A)
class _Fs6374DMType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_Fs6374DMType_Type.__name__=_E
_Fs6374DMType_Object=MibTableColumn
fs6374DMType=_Fs6374DMType_Object((1,3,6,1,4,1,29601,2,107,2,1,1,8),_Fs6374DMType_Type())
fs6374DMType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMType.setStatus(_A)
class _Fs6374DMMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_Fs6374DMMode_Type.__name__=_E
_Fs6374DMMode_Object=MibTableColumn
fs6374DMMode=_Fs6374DMMode_Object((1,3,6,1,4,1,29601,2,107,2,1,1,9),_Fs6374DMMode_Type())
fs6374DMMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMMode.setStatus(_A)
class _Fs6374DMTimeIntervalInMilliseconds_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_Fs6374DMTimeIntervalInMilliseconds_Type.__name__=_G
_Fs6374DMTimeIntervalInMilliseconds_Object=MibTableColumn
fs6374DMTimeIntervalInMilliseconds=_Fs6374DMTimeIntervalInMilliseconds_Object((1,3,6,1,4,1,29601,2,107,2,1,1,10),_Fs6374DMTimeIntervalInMilliseconds_Type())
fs6374DMTimeIntervalInMilliseconds.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMTimeIntervalInMilliseconds.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMTimeIntervalInMilliseconds.setUnits(_F)
class _Fs6374DMNoOfMessages_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Fs6374DMNoOfMessages_Type.__name__=_G
_Fs6374DMNoOfMessages_Object=MibTableColumn
fs6374DMNoOfMessages=_Fs6374DMNoOfMessages_Object((1,3,6,1,4,1,29601,2,107,2,1,1,11),_Fs6374DMNoOfMessages_Type())
fs6374DMNoOfMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMNoOfMessages.setStatus(_A)
class _Fs6374DMTimeStampFormat_Type(FS6374TimeStampFormat):defaultValue=3
_Fs6374DMTimeStampFormat_Type.__name__=_M
_Fs6374DMTimeStampFormat_Object=MibTableColumn
fs6374DMTimeStampFormat=_Fs6374DMTimeStampFormat_Object((1,3,6,1,4,1,29601,2,107,2,1,1,12),_Fs6374DMTimeStampFormat_Type())
fs6374DMTimeStampFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMTimeStampFormat.setStatus(_A)
class _Fs6374DMTransmitStatus_Type(Fs6374TransmitStatus):defaultValue=3
_Fs6374DMTransmitStatus_Type.__name__=_N
_Fs6374DMTransmitStatus_Object=MibTableColumn
fs6374DMTransmitStatus=_Fs6374DMTransmitStatus_Object((1,3,6,1,4,1,29601,2,107,2,1,1,13),_Fs6374DMTransmitStatus_Type())
fs6374DMTransmitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMTransmitStatus.setStatus(_A)
class _Fs6374CmbLMDMType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_Fs6374CmbLMDMType_Type.__name__=_E
_Fs6374CmbLMDMType_Object=MibTableColumn
fs6374CmbLMDMType=_Fs6374CmbLMDMType_Object((1,3,6,1,4,1,29601,2,107,2,1,1,14),_Fs6374CmbLMDMType_Type())
fs6374CmbLMDMType.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMType.setStatus(_A)
class _Fs6374CmbLMDMMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_Fs6374CmbLMDMMethod_Type.__name__=_E
_Fs6374CmbLMDMMethod_Object=MibTableColumn
fs6374CmbLMDMMethod=_Fs6374CmbLMDMMethod_Object((1,3,6,1,4,1,29601,2,107,2,1,1,15),_Fs6374CmbLMDMMethod_Type())
fs6374CmbLMDMMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMMethod.setStatus(_A)
class _Fs6374CmbLMDMMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_Fs6374CmbLMDMMode_Type.__name__=_E
_Fs6374CmbLMDMMode_Object=MibTableColumn
fs6374CmbLMDMMode=_Fs6374CmbLMDMMode_Object((1,3,6,1,4,1,29601,2,107,2,1,1,16),_Fs6374CmbLMDMMode_Type())
fs6374CmbLMDMMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMMode.setStatus(_A)
class _Fs6374CmbLMDMNoOfMessages_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Fs6374CmbLMDMNoOfMessages_Type.__name__=_G
_Fs6374CmbLMDMNoOfMessages_Object=MibTableColumn
fs6374CmbLMDMNoOfMessages=_Fs6374CmbLMDMNoOfMessages_Object((1,3,6,1,4,1,29601,2,107,2,1,1,17),_Fs6374CmbLMDMNoOfMessages_Type())
fs6374CmbLMDMNoOfMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMNoOfMessages.setStatus(_A)
class _Fs6374CmbLMDMTimeIntervalInMilliseconds_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_Fs6374CmbLMDMTimeIntervalInMilliseconds_Type.__name__=_G
_Fs6374CmbLMDMTimeIntervalInMilliseconds_Object=MibTableColumn
fs6374CmbLMDMTimeIntervalInMilliseconds=_Fs6374CmbLMDMTimeIntervalInMilliseconds_Object((1,3,6,1,4,1,29601,2,107,2,1,1,18),_Fs6374CmbLMDMTimeIntervalInMilliseconds_Type())
fs6374CmbLMDMTimeIntervalInMilliseconds.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMTimeIntervalInMilliseconds.setStatus(_A)
if mibBuilder.loadTexts:fs6374CmbLMDMTimeIntervalInMilliseconds.setUnits(_F)
class _Fs6374CmbLMDMTimeStampFormat_Type(FS6374TimeStampFormat):defaultValue=3
_Fs6374CmbLMDMTimeStampFormat_Type.__name__=_M
_Fs6374CmbLMDMTimeStampFormat_Object=MibTableColumn
fs6374CmbLMDMTimeStampFormat=_Fs6374CmbLMDMTimeStampFormat_Object((1,3,6,1,4,1,29601,2,107,2,1,1,19),_Fs6374CmbLMDMTimeStampFormat_Type())
fs6374CmbLMDMTimeStampFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMTimeStampFormat.setStatus(_A)
class _Fs6374CmbLMDMTransmitStatus_Type(Fs6374TransmitStatus):defaultValue=3
_Fs6374CmbLMDMTransmitStatus_Type.__name__=_N
_Fs6374CmbLMDMTransmitStatus_Object=MibTableColumn
fs6374CmbLMDMTransmitStatus=_Fs6374CmbLMDMTransmitStatus_Object((1,3,6,1,4,1,29601,2,107,2,1,1,20),_Fs6374CmbLMDMTransmitStatus_Type())
fs6374CmbLMDMTransmitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMTransmitStatus.setStatus(_A)
class _Fs6374DMPaddingSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_Fs6374DMPaddingSize_Type.__name__=_G
_Fs6374DMPaddingSize_Object=MibTableColumn
fs6374DMPaddingSize=_Fs6374DMPaddingSize_Object((1,3,6,1,4,1,29601,2,107,2,1,1,21),_Fs6374DMPaddingSize_Type())
fs6374DMPaddingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMPaddingSize.setStatus(_A)
class _Fs6374CmbLMDMPaddingSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9000))
_Fs6374CmbLMDMPaddingSize_Type.__name__=_G
_Fs6374CmbLMDMPaddingSize_Object=MibTableColumn
fs6374CmbLMDMPaddingSize=_Fs6374CmbLMDMPaddingSize_Object((1,3,6,1,4,1,29601,2,107,2,1,1,22),_Fs6374CmbLMDMPaddingSize_Type())
fs6374CmbLMDMPaddingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374CmbLMDMPaddingSize.setStatus(_A)
_Fs6374LMBuffer_ObjectIdentity=ObjectIdentity
fs6374LMBuffer=_Fs6374LMBuffer_ObjectIdentity((1,3,6,1,4,1,29601,2,107,3))
_Fs6374LMTable_Object=MibTable
fs6374LMTable=_Fs6374LMTable_Object((1,3,6,1,4,1,29601,2,107,3,1))
if mibBuilder.loadTexts:fs6374LMTable.setStatus(_A)
_Fs6374LMTableEntry_Object=MibTableRow
fs6374LMTableEntry=_Fs6374LMTableEntry_Object((1,3,6,1,4,1,29601,2,107,3,1,1))
fs6374LMTableEntry.setIndexNames((0,_D,_H),(0,_D,_J),(0,_D,_S),(0,_D,_a))
if mibBuilder.loadTexts:fs6374LMTableEntry.setStatus(_A)
_Fs6374LMSessionId_Type=Unsigned32
_Fs6374LMSessionId_Object=MibTableColumn
fs6374LMSessionId=_Fs6374LMSessionId_Object((1,3,6,1,4,1,29601,2,107,3,1,1,1),_Fs6374LMSessionId_Type())
fs6374LMSessionId.setMaxAccess(_K)
if mibBuilder.loadTexts:fs6374LMSessionId.setStatus(_A)
_Fs6374LMSeqNum_Type=Unsigned32
_Fs6374LMSeqNum_Object=MibTableColumn
fs6374LMSeqNum=_Fs6374LMSeqNum_Object((1,3,6,1,4,1,29601,2,107,3,1,1,2),_Fs6374LMSeqNum_Type())
fs6374LMSeqNum.setMaxAccess(_K)
if mibBuilder.loadTexts:fs6374LMSeqNum.setStatus(_A)
_Fs6374LMTxLossAtSenderEnd_Type=Unsigned32
_Fs6374LMTxLossAtSenderEnd_Object=MibTableColumn
fs6374LMTxLossAtSenderEnd=_Fs6374LMTxLossAtSenderEnd_Object((1,3,6,1,4,1,29601,2,107,3,1,1,3),_Fs6374LMTxLossAtSenderEnd_Type())
fs6374LMTxLossAtSenderEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMTxLossAtSenderEnd.setStatus(_A)
_Fs6374LMRxLossAtSenderEnd_Type=Unsigned32
_Fs6374LMRxLossAtSenderEnd_Object=MibTableColumn
fs6374LMRxLossAtSenderEnd=_Fs6374LMRxLossAtSenderEnd_Object((1,3,6,1,4,1,29601,2,107,3,1,1,4),_Fs6374LMRxLossAtSenderEnd_Type())
fs6374LMRxLossAtSenderEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMRxLossAtSenderEnd.setStatus(_A)
_Fs6374LMRxLossAtReceiverEnd_Type=Unsigned32
_Fs6374LMRxLossAtReceiverEnd_Object=MibTableColumn
fs6374LMRxLossAtReceiverEnd=_Fs6374LMRxLossAtReceiverEnd_Object((1,3,6,1,4,1,29601,2,107,3,1,1,5),_Fs6374LMRxLossAtReceiverEnd_Type())
fs6374LMRxLossAtReceiverEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMRxLossAtReceiverEnd.setStatus(_A)
_Fs6374LMMeasurementTimeTakenInMilliseconds_Type=FS6374TimeRepresentation
_Fs6374LMMeasurementTimeTakenInMilliseconds_Object=MibTableColumn
fs6374LMMeasurementTimeTakenInMilliseconds=_Fs6374LMMeasurementTimeTakenInMilliseconds_Object((1,3,6,1,4,1,29601,2,107,3,1,1,6),_Fs6374LMMeasurementTimeTakenInMilliseconds_Type())
fs6374LMMeasurementTimeTakenInMilliseconds.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMMeasurementTimeTakenInMilliseconds.setStatus(_A)
if mibBuilder.loadTexts:fs6374LMMeasurementTimeTakenInMilliseconds.setUnits(_F)
class _Fs6374LMTransmitResultOK_Type(TruthValue):defaultValue=1
_Fs6374LMTransmitResultOK_Type.__name__=_L
_Fs6374LMTransmitResultOK_Object=MibTableColumn
fs6374LMTransmitResultOK=_Fs6374LMTransmitResultOK_Object((1,3,6,1,4,1,29601,2,107,3,1,1,7),_Fs6374LMTransmitResultOK_Type())
fs6374LMTransmitResultOK.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMTransmitResultOK.setStatus(_A)
_Fs6374LMTestPktsCount_Type=Unsigned32
_Fs6374LMTestPktsCount_Object=MibTableColumn
fs6374LMTestPktsCount=_Fs6374LMTestPktsCount_Object((1,3,6,1,4,1,29601,2,107,3,1,1,8),_Fs6374LMTestPktsCount_Type())
fs6374LMTestPktsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMTestPktsCount.setStatus(_A)
_Fs6374DMBuffer_ObjectIdentity=ObjectIdentity
fs6374DMBuffer=_Fs6374DMBuffer_ObjectIdentity((1,3,6,1,4,1,29601,2,107,4))
_Fs6374DMTable_Object=MibTable
fs6374DMTable=_Fs6374DMTable_Object((1,3,6,1,4,1,29601,2,107,4,1))
if mibBuilder.loadTexts:fs6374DMTable.setStatus(_A)
_Fs6374DMTableEntry_Object=MibTableRow
fs6374DMTableEntry=_Fs6374DMTableEntry_Object((1,3,6,1,4,1,29601,2,107,4,1,1))
fs6374DMTableEntry.setIndexNames((0,_D,_H),(0,_D,_J),(0,_D,_T),(0,_D,_b))
if mibBuilder.loadTexts:fs6374DMTableEntry.setStatus(_A)
_Fs6374DMSessionId_Type=Unsigned32
_Fs6374DMSessionId_Object=MibTableColumn
fs6374DMSessionId=_Fs6374DMSessionId_Object((1,3,6,1,4,1,29601,2,107,4,1,1,1),_Fs6374DMSessionId_Type())
fs6374DMSessionId.setMaxAccess(_K)
if mibBuilder.loadTexts:fs6374DMSessionId.setStatus(_A)
_Fs6374DMSeqNum_Type=Unsigned32
_Fs6374DMSeqNum_Object=MibTableColumn
fs6374DMSeqNum=_Fs6374DMSeqNum_Object((1,3,6,1,4,1,29601,2,107,4,1,1,2),_Fs6374DMSeqNum_Type())
fs6374DMSeqNum.setMaxAccess(_K)
if mibBuilder.loadTexts:fs6374DMSeqNum.setStatus(_A)
_Fs6374DMDelayValue_Type=FS6374TimeRepresentation
_Fs6374DMDelayValue_Object=MibTableColumn
fs6374DMDelayValue=_Fs6374DMDelayValue_Object((1,3,6,1,4,1,29601,2,107,4,1,1,3),_Fs6374DMDelayValue_Type())
fs6374DMDelayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMDelayValue.setStatus(_A)
_Fs6374DMRTDelayValue_Type=FS6374TimeRepresentation
_Fs6374DMRTDelayValue_Object=MibTableColumn
fs6374DMRTDelayValue=_Fs6374DMRTDelayValue_Object((1,3,6,1,4,1,29601,2,107,4,1,1,4),_Fs6374DMRTDelayValue_Type())
fs6374DMRTDelayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMRTDelayValue.setStatus(_A)
_Fs6374DMIPDV_Type=FS6374TimeRepresentation
_Fs6374DMIPDV_Object=MibTableColumn
fs6374DMIPDV=_Fs6374DMIPDV_Object((1,3,6,1,4,1,29601,2,107,4,1,1,5),_Fs6374DMIPDV_Type())
fs6374DMIPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMIPDV.setStatus(_A)
_Fs6374DMPDV_Type=FS6374TimeRepresentation
_Fs6374DMPDV_Object=MibTableColumn
fs6374DMPDV=_Fs6374DMPDV_Object((1,3,6,1,4,1,29601,2,107,4,1,1,6),_Fs6374DMPDV_Type())
fs6374DMPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMPDV.setStatus(_A)
class _Fs6374DMTransmitResultOK_Type(TruthValue):defaultValue=1
_Fs6374DMTransmitResultOK_Type.__name__=_L
_Fs6374DMTransmitResultOK_Object=MibTableColumn
fs6374DMTransmitResultOK=_Fs6374DMTransmitResultOK_Object((1,3,6,1,4,1,29601,2,107,4,1,1,7),_Fs6374DMTransmitResultOK_Type())
fs6374DMTransmitResultOK.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMTransmitResultOK.setStatus(_A)
_Fs6374LMStats_ObjectIdentity=ObjectIdentity
fs6374LMStats=_Fs6374LMStats_ObjectIdentity((1,3,6,1,4,1,29601,2,107,5))
_Fs6374LMStatsTable_Object=MibTable
fs6374LMStatsTable=_Fs6374LMStatsTable_Object((1,3,6,1,4,1,29601,2,107,5,1))
if mibBuilder.loadTexts:fs6374LMStatsTable.setStatus(_A)
_Fs6374LMStatsTableEntry_Object=MibTableRow
fs6374LMStatsTableEntry=_Fs6374LMStatsTableEntry_Object((1,3,6,1,4,1,29601,2,107,5,1,1))
fs6374LMStatsTableEntry.setIndexNames((0,_D,_H),(0,_D,_J),(0,_D,_S))
if mibBuilder.loadTexts:fs6374LMStatsTableEntry.setStatus(_A)
_Fs6374LMStatsMplsType_Type=Integer32
_Fs6374LMStatsMplsType_Object=MibTableColumn
fs6374LMStatsMplsType=_Fs6374LMStatsMplsType_Object((1,3,6,1,4,1,29601,2,107,5,1,1,1),_Fs6374LMStatsMplsType_Type())
fs6374LMStatsMplsType.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsMplsType.setStatus(_A)
_Fs6374LMStatsFwdTnlIdOrPwId_Type=Unsigned32
_Fs6374LMStatsFwdTnlIdOrPwId_Object=MibTableColumn
fs6374LMStatsFwdTnlIdOrPwId=_Fs6374LMStatsFwdTnlIdOrPwId_Object((1,3,6,1,4,1,29601,2,107,5,1,1,2),_Fs6374LMStatsFwdTnlIdOrPwId_Type())
fs6374LMStatsFwdTnlIdOrPwId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsFwdTnlIdOrPwId.setStatus(_A)
_Fs6374LMStatsRevTnlId_Type=Unsigned32
_Fs6374LMStatsRevTnlId_Object=MibTableColumn
fs6374LMStatsRevTnlId=_Fs6374LMStatsRevTnlId_Object((1,3,6,1,4,1,29601,2,107,5,1,1,3),_Fs6374LMStatsRevTnlId_Type())
fs6374LMStatsRevTnlId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsRevTnlId.setStatus(_A)
class _Fs6374LMStatsSrcIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Fs6374LMStatsSrcIpAddr_Type.__name__=_I
_Fs6374LMStatsSrcIpAddr_Object=MibTableColumn
fs6374LMStatsSrcIpAddr=_Fs6374LMStatsSrcIpAddr_Object((1,3,6,1,4,1,29601,2,107,5,1,1,4),_Fs6374LMStatsSrcIpAddr_Type())
fs6374LMStatsSrcIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsSrcIpAddr.setStatus(_A)
class _Fs6374LMStatsDestIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Fs6374LMStatsDestIpAddr_Type.__name__=_I
_Fs6374LMStatsDestIpAddr_Object=MibTableColumn
fs6374LMStatsDestIpAddr=_Fs6374LMStatsDestIpAddr_Object((1,3,6,1,4,1,29601,2,107,5,1,1,5),_Fs6374LMStatsDestIpAddr_Type())
fs6374LMStatsDestIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsDestIpAddr.setStatus(_A)
_Fs6374LMStatsTrafficClass_Type=Integer32
_Fs6374LMStatsTrafficClass_Object=MibTableColumn
fs6374LMStatsTrafficClass=_Fs6374LMStatsTrafficClass_Object((1,3,6,1,4,1,29601,2,107,5,1,1,6),_Fs6374LMStatsTrafficClass_Type())
fs6374LMStatsTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsTrafficClass.setStatus(_A)
_Fs6374LMStatsMode_Type=Integer32
_Fs6374LMStatsMode_Object=MibTableColumn
fs6374LMStatsMode=_Fs6374LMStatsMode_Object((1,3,6,1,4,1,29601,2,107,5,1,1,7),_Fs6374LMStatsMode_Type())
fs6374LMStatsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsMode.setStatus(_A)
_Fs6374LMStatsMethod_Type=Integer32
_Fs6374LMStatsMethod_Object=MibTableColumn
fs6374LMStatsMethod=_Fs6374LMStatsMethod_Object((1,3,6,1,4,1,29601,2,107,5,1,1,8),_Fs6374LMStatsMethod_Type())
fs6374LMStatsMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsMethod.setStatus(_A)
_Fs6374LMStatsType_Type=Integer32
_Fs6374LMStatsType_Object=MibTableColumn
fs6374LMStatsType=_Fs6374LMStatsType_Object((1,3,6,1,4,1,29601,2,107,5,1,1,9),_Fs6374LMStatsType_Type())
fs6374LMStatsType.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsType.setStatus(_A)
_Fs6374LMStatsTimeStampFormat_Type=FS6374TimeStampFormat
_Fs6374LMStatsTimeStampFormat_Object=MibTableColumn
fs6374LMStatsTimeStampFormat=_Fs6374LMStatsTimeStampFormat_Object((1,3,6,1,4,1,29601,2,107,5,1,1,10),_Fs6374LMStatsTimeStampFormat_Type())
fs6374LMStatsTimeStampFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsTimeStampFormat.setStatus(_A)
_Fs6374LMStatsStartTime_Type=Unsigned32
_Fs6374LMStatsStartTime_Object=MibTableColumn
fs6374LMStatsStartTime=_Fs6374LMStatsStartTime_Object((1,3,6,1,4,1,29601,2,107,5,1,1,11),_Fs6374LMStatsStartTime_Type())
fs6374LMStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsStartTime.setStatus(_A)
_Fs6374LMStatsFarEndLossMin_Type=Unsigned32
_Fs6374LMStatsFarEndLossMin_Object=MibTableColumn
fs6374LMStatsFarEndLossMin=_Fs6374LMStatsFarEndLossMin_Object((1,3,6,1,4,1,29601,2,107,5,1,1,12),_Fs6374LMStatsFarEndLossMin_Type())
fs6374LMStatsFarEndLossMin.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsFarEndLossMin.setStatus(_A)
_Fs6374LMStatsFarEndLossMax_Type=Unsigned32
_Fs6374LMStatsFarEndLossMax_Object=MibTableColumn
fs6374LMStatsFarEndLossMax=_Fs6374LMStatsFarEndLossMax_Object((1,3,6,1,4,1,29601,2,107,5,1,1,13),_Fs6374LMStatsFarEndLossMax_Type())
fs6374LMStatsFarEndLossMax.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsFarEndLossMax.setStatus(_A)
_Fs6374LMStatsFarEndLossAvg_Type=Unsigned32
_Fs6374LMStatsFarEndLossAvg_Object=MibTableColumn
fs6374LMStatsFarEndLossAvg=_Fs6374LMStatsFarEndLossAvg_Object((1,3,6,1,4,1,29601,2,107,5,1,1,14),_Fs6374LMStatsFarEndLossAvg_Type())
fs6374LMStatsFarEndLossAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsFarEndLossAvg.setStatus(_A)
_Fs6374LMStatsNearEndLossMin_Type=Unsigned32
_Fs6374LMStatsNearEndLossMin_Object=MibTableColumn
fs6374LMStatsNearEndLossMin=_Fs6374LMStatsNearEndLossMin_Object((1,3,6,1,4,1,29601,2,107,5,1,1,15),_Fs6374LMStatsNearEndLossMin_Type())
fs6374LMStatsNearEndLossMin.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsNearEndLossMin.setStatus(_A)
_Fs6374LMStatsNearEndLossMax_Type=Unsigned32
_Fs6374LMStatsNearEndLossMax_Object=MibTableColumn
fs6374LMStatsNearEndLossMax=_Fs6374LMStatsNearEndLossMax_Object((1,3,6,1,4,1,29601,2,107,5,1,1,16),_Fs6374LMStatsNearEndLossMax_Type())
fs6374LMStatsNearEndLossMax.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsNearEndLossMax.setStatus(_A)
_Fs6374LMStatsNearEndLossAvg_Type=Unsigned32
_Fs6374LMStatsNearEndLossAvg_Object=MibTableColumn
fs6374LMStatsNearEndLossAvg=_Fs6374LMStatsNearEndLossAvg_Object((1,3,6,1,4,1,29601,2,107,5,1,1,17),_Fs6374LMStatsNearEndLossAvg_Type())
fs6374LMStatsNearEndLossAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsNearEndLossAvg.setStatus(_A)
_Fs6374LMStatsTxPktCount_Type=Unsigned32
_Fs6374LMStatsTxPktCount_Object=MibTableColumn
fs6374LMStatsTxPktCount=_Fs6374LMStatsTxPktCount_Object((1,3,6,1,4,1,29601,2,107,5,1,1,18),_Fs6374LMStatsTxPktCount_Type())
fs6374LMStatsTxPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsTxPktCount.setStatus(_A)
_Fs6374LMStatsRxPktCount_Type=Unsigned32
_Fs6374LMStatsRxPktCount_Object=MibTableColumn
fs6374LMStatsRxPktCount=_Fs6374LMStatsRxPktCount_Object((1,3,6,1,4,1,29601,2,107,5,1,1,19),_Fs6374LMStatsRxPktCount_Type())
fs6374LMStatsRxPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsRxPktCount.setStatus(_A)
_Fs6374LMStatsThroughputpercent_Type=OctetString
_Fs6374LMStatsThroughputpercent_Object=MibTableColumn
fs6374LMStatsThroughputpercent=_Fs6374LMStatsThroughputpercent_Object((1,3,6,1,4,1,29601,2,107,5,1,1,20),_Fs6374LMStatsThroughputpercent_Type())
fs6374LMStatsThroughputpercent.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsThroughputpercent.setStatus(_A)
class _Fs6374LMStatsResponseErrors_Type(Unsigned32):defaultValue=0
_Fs6374LMStatsResponseErrors_Type.__name__=_G
_Fs6374LMStatsResponseErrors_Object=MibTableColumn
fs6374LMStatsResponseErrors=_Fs6374LMStatsResponseErrors_Object((1,3,6,1,4,1,29601,2,107,5,1,1,21),_Fs6374LMStatsResponseErrors_Type())
fs6374LMStatsResponseErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsResponseErrors.setStatus(_A)
class _Fs6374LMStatsResponseTimeout_Type(Unsigned32):defaultValue=0
_Fs6374LMStatsResponseTimeout_Type.__name__=_G
_Fs6374LMStatsResponseTimeout_Object=MibTableColumn
fs6374LMStatsResponseTimeout=_Fs6374LMStatsResponseTimeout_Object((1,3,6,1,4,1,29601,2,107,5,1,1,22),_Fs6374LMStatsResponseTimeout_Type())
fs6374LMStatsResponseTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsResponseTimeout.setStatus(_A)
class _Fs6374LMStatsMeasurementOnGoing_Type(Integer32):defaultValue=0
_Fs6374LMStatsMeasurementOnGoing_Type.__name__=_E
_Fs6374LMStatsMeasurementOnGoing_Object=MibTableColumn
fs6374LMStatsMeasurementOnGoing=_Fs6374LMStatsMeasurementOnGoing_Object((1,3,6,1,4,1,29601,2,107,5,1,1,23),_Fs6374LMStatsMeasurementOnGoing_Type())
fs6374LMStatsMeasurementOnGoing.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMStatsMeasurementOnGoing.setStatus(_A)
class _Fs6374LMDyadicMeasurement_Type(Integer32):defaultValue=2
_Fs6374LMDyadicMeasurement_Type.__name__=_E
_Fs6374LMDyadicMeasurement_Object=MibTableColumn
fs6374LMDyadicMeasurement=_Fs6374LMDyadicMeasurement_Object((1,3,6,1,4,1,29601,2,107,5,1,1,24),_Fs6374LMDyadicMeasurement_Type())
fs6374LMDyadicMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMDyadicMeasurement.setStatus(_A)
_Fs6374LMRemoteSessionId_Type=Unsigned32
_Fs6374LMRemoteSessionId_Object=MibTableColumn
fs6374LMRemoteSessionId=_Fs6374LMRemoteSessionId_Object((1,3,6,1,4,1,29601,2,107,5,1,1,25),_Fs6374LMRemoteSessionId_Type())
fs6374LMRemoteSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMRemoteSessionId.setStatus(_A)
_Fs6374LMDyadicProactiveRole_Type=Integer32
_Fs6374LMDyadicProactiveRole_Object=MibTableColumn
fs6374LMDyadicProactiveRole=_Fs6374LMDyadicProactiveRole_Object((1,3,6,1,4,1,29601,2,107,5,1,1,26),_Fs6374LMDyadicProactiveRole_Type())
fs6374LMDyadicProactiveRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374LMDyadicProactiveRole.setStatus(_A)
class _Fs6374IsLMBufferSQIEnabled_Type(TruthValue):defaultValue=2
_Fs6374IsLMBufferSQIEnabled_Type.__name__=_L
_Fs6374IsLMBufferSQIEnabled_Object=MibTableColumn
fs6374IsLMBufferSQIEnabled=_Fs6374IsLMBufferSQIEnabled_Object((1,3,6,1,4,1,29601,2,107,5,1,1,27),_Fs6374IsLMBufferSQIEnabled_Type())
fs6374IsLMBufferSQIEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374IsLMBufferSQIEnabled.setStatus(_A)
_Fs6374DMStats_ObjectIdentity=ObjectIdentity
fs6374DMStats=_Fs6374DMStats_ObjectIdentity((1,3,6,1,4,1,29601,2,107,6))
_Fs6374DMStatsTable_Object=MibTable
fs6374DMStatsTable=_Fs6374DMStatsTable_Object((1,3,6,1,4,1,29601,2,107,6,1))
if mibBuilder.loadTexts:fs6374DMStatsTable.setStatus(_A)
_Fs6374DMStatsTableEntry_Object=MibTableRow
fs6374DMStatsTableEntry=_Fs6374DMStatsTableEntry_Object((1,3,6,1,4,1,29601,2,107,6,1,1))
fs6374DMStatsTableEntry.setIndexNames((0,_D,_H),(0,_D,_J),(0,_D,_T))
if mibBuilder.loadTexts:fs6374DMStatsTableEntry.setStatus(_A)
_Fs6374DMStatsMplsType_Type=Integer32
_Fs6374DMStatsMplsType_Object=MibTableColumn
fs6374DMStatsMplsType=_Fs6374DMStatsMplsType_Object((1,3,6,1,4,1,29601,2,107,6,1,1,1),_Fs6374DMStatsMplsType_Type())
fs6374DMStatsMplsType.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMplsType.setStatus(_A)
_Fs6374DMStatsFwdTnlIdOrPwId_Type=Unsigned32
_Fs6374DMStatsFwdTnlIdOrPwId_Object=MibTableColumn
fs6374DMStatsFwdTnlIdOrPwId=_Fs6374DMStatsFwdTnlIdOrPwId_Object((1,3,6,1,4,1,29601,2,107,6,1,1,2),_Fs6374DMStatsFwdTnlIdOrPwId_Type())
fs6374DMStatsFwdTnlIdOrPwId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsFwdTnlIdOrPwId.setStatus(_A)
_Fs6374DMStatsRevTnlId_Type=Unsigned32
_Fs6374DMStatsRevTnlId_Object=MibTableColumn
fs6374DMStatsRevTnlId=_Fs6374DMStatsRevTnlId_Object((1,3,6,1,4,1,29601,2,107,6,1,1,3),_Fs6374DMStatsRevTnlId_Type())
fs6374DMStatsRevTnlId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsRevTnlId.setStatus(_A)
class _Fs6374DMStatsSrcIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Fs6374DMStatsSrcIpAddr_Type.__name__=_I
_Fs6374DMStatsSrcIpAddr_Object=MibTableColumn
fs6374DMStatsSrcIpAddr=_Fs6374DMStatsSrcIpAddr_Object((1,3,6,1,4,1,29601,2,107,6,1,1,4),_Fs6374DMStatsSrcIpAddr_Type())
fs6374DMStatsSrcIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsSrcIpAddr.setStatus(_A)
class _Fs6374DMStatsDestIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Fs6374DMStatsDestIpAddr_Type.__name__=_I
_Fs6374DMStatsDestIpAddr_Object=MibTableColumn
fs6374DMStatsDestIpAddr=_Fs6374DMStatsDestIpAddr_Object((1,3,6,1,4,1,29601,2,107,6,1,1,5),_Fs6374DMStatsDestIpAddr_Type())
fs6374DMStatsDestIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsDestIpAddr.setStatus(_A)
_Fs6374DMStatsTrafficClass_Type=Integer32
_Fs6374DMStatsTrafficClass_Object=MibTableColumn
fs6374DMStatsTrafficClass=_Fs6374DMStatsTrafficClass_Object((1,3,6,1,4,1,29601,2,107,6,1,1,6),_Fs6374DMStatsTrafficClass_Type())
fs6374DMStatsTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsTrafficClass.setStatus(_A)
_Fs6374DMStatsMode_Type=Integer32
_Fs6374DMStatsMode_Object=MibTableColumn
fs6374DMStatsMode=_Fs6374DMStatsMode_Object((1,3,6,1,4,1,29601,2,107,6,1,1,7),_Fs6374DMStatsMode_Type())
fs6374DMStatsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMode.setStatus(_A)
_Fs6374DMStatsType_Type=Integer32
_Fs6374DMStatsType_Object=MibTableColumn
fs6374DMStatsType=_Fs6374DMStatsType_Object((1,3,6,1,4,1,29601,2,107,6,1,1,8),_Fs6374DMStatsType_Type())
fs6374DMStatsType.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsType.setStatus(_A)
_Fs6374DMStatsTimeStampFormat_Type=FS6374TimeStampFormat
_Fs6374DMStatsTimeStampFormat_Object=MibTableColumn
fs6374DMStatsTimeStampFormat=_Fs6374DMStatsTimeStampFormat_Object((1,3,6,1,4,1,29601,2,107,6,1,1,9),_Fs6374DMStatsTimeStampFormat_Type())
fs6374DMStatsTimeStampFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsTimeStampFormat.setStatus(_A)
_Fs6374DMStatsStartTime_Type=Unsigned32
_Fs6374DMStatsStartTime_Object=MibTableColumn
fs6374DMStatsStartTime=_Fs6374DMStatsStartTime_Object((1,3,6,1,4,1,29601,2,107,6,1,1,10),_Fs6374DMStatsStartTime_Type())
fs6374DMStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsStartTime.setStatus(_A)
_Fs6374DMStatsMinDelay_Type=FS6374TimeRepresentation
_Fs6374DMStatsMinDelay_Object=MibTableColumn
fs6374DMStatsMinDelay=_Fs6374DMStatsMinDelay_Object((1,3,6,1,4,1,29601,2,107,6,1,1,11),_Fs6374DMStatsMinDelay_Type())
fs6374DMStatsMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMinDelay.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMinDelay.setUnits(_F)
_Fs6374DMStatsMaxDelay_Type=FS6374TimeRepresentation
_Fs6374DMStatsMaxDelay_Object=MibTableColumn
fs6374DMStatsMaxDelay=_Fs6374DMStatsMaxDelay_Object((1,3,6,1,4,1,29601,2,107,6,1,1,12),_Fs6374DMStatsMaxDelay_Type())
fs6374DMStatsMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMaxDelay.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMaxDelay.setUnits(_F)
_Fs6374DMStatsAvgDelay_Type=FS6374TimeRepresentation
_Fs6374DMStatsAvgDelay_Object=MibTableColumn
fs6374DMStatsAvgDelay=_Fs6374DMStatsAvgDelay_Object((1,3,6,1,4,1,29601,2,107,6,1,1,13),_Fs6374DMStatsAvgDelay_Type())
fs6374DMStatsAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsAvgDelay.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsAvgDelay.setUnits(_F)
_Fs6374DMStatsMinRTDelay_Type=FS6374TimeRepresentation
_Fs6374DMStatsMinRTDelay_Object=MibTableColumn
fs6374DMStatsMinRTDelay=_Fs6374DMStatsMinRTDelay_Object((1,3,6,1,4,1,29601,2,107,6,1,1,14),_Fs6374DMStatsMinRTDelay_Type())
fs6374DMStatsMinRTDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMinRTDelay.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMinRTDelay.setUnits(_F)
_Fs6374DMStatsMaxRTDelay_Type=FS6374TimeRepresentation
_Fs6374DMStatsMaxRTDelay_Object=MibTableColumn
fs6374DMStatsMaxRTDelay=_Fs6374DMStatsMaxRTDelay_Object((1,3,6,1,4,1,29601,2,107,6,1,1,15),_Fs6374DMStatsMaxRTDelay_Type())
fs6374DMStatsMaxRTDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMaxRTDelay.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMaxRTDelay.setUnits(_F)
_Fs6374DMStatsAvgRTDelay_Type=FS6374TimeRepresentation
_Fs6374DMStatsAvgRTDelay_Object=MibTableColumn
fs6374DMStatsAvgRTDelay=_Fs6374DMStatsAvgRTDelay_Object((1,3,6,1,4,1,29601,2,107,6,1,1,16),_Fs6374DMStatsAvgRTDelay_Type())
fs6374DMStatsAvgRTDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsAvgRTDelay.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsAvgRTDelay.setUnits(_F)
_Fs6374DMStatsMinIPDV_Type=FS6374TimeRepresentation
_Fs6374DMStatsMinIPDV_Object=MibTableColumn
fs6374DMStatsMinIPDV=_Fs6374DMStatsMinIPDV_Object((1,3,6,1,4,1,29601,2,107,6,1,1,17),_Fs6374DMStatsMinIPDV_Type())
fs6374DMStatsMinIPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMinIPDV.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMinIPDV.setUnits(_F)
_Fs6374DMStatsMaxIPDV_Type=FS6374TimeRepresentation
_Fs6374DMStatsMaxIPDV_Object=MibTableColumn
fs6374DMStatsMaxIPDV=_Fs6374DMStatsMaxIPDV_Object((1,3,6,1,4,1,29601,2,107,6,1,1,18),_Fs6374DMStatsMaxIPDV_Type())
fs6374DMStatsMaxIPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMaxIPDV.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMaxIPDV.setUnits(_F)
_Fs6374DMStatsAvgIPDV_Type=FS6374TimeRepresentation
_Fs6374DMStatsAvgIPDV_Object=MibTableColumn
fs6374DMStatsAvgIPDV=_Fs6374DMStatsAvgIPDV_Object((1,3,6,1,4,1,29601,2,107,6,1,1,19),_Fs6374DMStatsAvgIPDV_Type())
fs6374DMStatsAvgIPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsAvgIPDV.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsAvgIPDV.setUnits(_F)
_Fs6374DMStatsMinPDV_Type=FS6374TimeRepresentation
_Fs6374DMStatsMinPDV_Object=MibTableColumn
fs6374DMStatsMinPDV=_Fs6374DMStatsMinPDV_Object((1,3,6,1,4,1,29601,2,107,6,1,1,20),_Fs6374DMStatsMinPDV_Type())
fs6374DMStatsMinPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMinPDV.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMinPDV.setUnits(_F)
_Fs6374DMStatsMaxPDV_Type=FS6374TimeRepresentation
_Fs6374DMStatsMaxPDV_Object=MibTableColumn
fs6374DMStatsMaxPDV=_Fs6374DMStatsMaxPDV_Object((1,3,6,1,4,1,29601,2,107,6,1,1,21),_Fs6374DMStatsMaxPDV_Type())
fs6374DMStatsMaxPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMaxPDV.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsMaxPDV.setUnits(_F)
_Fs6374DMStatsAvgPDV_Type=FS6374TimeRepresentation
_Fs6374DMStatsAvgPDV_Object=MibTableColumn
fs6374DMStatsAvgPDV=_Fs6374DMStatsAvgPDV_Object((1,3,6,1,4,1,29601,2,107,6,1,1,22),_Fs6374DMStatsAvgPDV_Type())
fs6374DMStatsAvgPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsAvgPDV.setStatus(_A)
if mibBuilder.loadTexts:fs6374DMStatsAvgPDV.setUnits(_F)
_Fs6374DMStatsTxPktCount_Type=Unsigned32
_Fs6374DMStatsTxPktCount_Object=MibTableColumn
fs6374DMStatsTxPktCount=_Fs6374DMStatsTxPktCount_Object((1,3,6,1,4,1,29601,2,107,6,1,1,23),_Fs6374DMStatsTxPktCount_Type())
fs6374DMStatsTxPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsTxPktCount.setStatus(_A)
_Fs6374DMStatsRxPktCount_Type=Unsigned32
_Fs6374DMStatsRxPktCount_Object=MibTableColumn
fs6374DMStatsRxPktCount=_Fs6374DMStatsRxPktCount_Object((1,3,6,1,4,1,29601,2,107,6,1,1,24),_Fs6374DMStatsRxPktCount_Type())
fs6374DMStatsRxPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsRxPktCount.setStatus(_A)
class _Fs6374DMStatsResponseErrors_Type(Unsigned32):defaultValue=0
_Fs6374DMStatsResponseErrors_Type.__name__=_G
_Fs6374DMStatsResponseErrors_Object=MibTableColumn
fs6374DMStatsResponseErrors=_Fs6374DMStatsResponseErrors_Object((1,3,6,1,4,1,29601,2,107,6,1,1,25),_Fs6374DMStatsResponseErrors_Type())
fs6374DMStatsResponseErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsResponseErrors.setStatus(_A)
class _Fs6374DMStatsResponseTimeout_Type(Unsigned32):defaultValue=0
_Fs6374DMStatsResponseTimeout_Type.__name__=_G
_Fs6374DMStatsResponseTimeout_Object=MibTableColumn
fs6374DMStatsResponseTimeout=_Fs6374DMStatsResponseTimeout_Object((1,3,6,1,4,1,29601,2,107,6,1,1,26),_Fs6374DMStatsResponseTimeout_Type())
fs6374DMStatsResponseTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsResponseTimeout.setStatus(_A)
class _Fs6374DMStatsMeasurementOnGoing_Type(Integer32):defaultValue=0
_Fs6374DMStatsMeasurementOnGoing_Type.__name__=_E
_Fs6374DMStatsMeasurementOnGoing_Object=MibTableColumn
fs6374DMStatsMeasurementOnGoing=_Fs6374DMStatsMeasurementOnGoing_Object((1,3,6,1,4,1,29601,2,107,6,1,1,27),_Fs6374DMStatsMeasurementOnGoing_Type())
fs6374DMStatsMeasurementOnGoing.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsMeasurementOnGoing.setStatus(_A)
class _Fs6374DMDyadicMeasurement_Type(Integer32):defaultValue=2
_Fs6374DMDyadicMeasurement_Type.__name__=_E
_Fs6374DMDyadicMeasurement_Object=MibTableColumn
fs6374DMDyadicMeasurement=_Fs6374DMDyadicMeasurement_Object((1,3,6,1,4,1,29601,2,107,6,1,1,28),_Fs6374DMDyadicMeasurement_Type())
fs6374DMDyadicMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMDyadicMeasurement.setStatus(_A)
_Fs6374DMRemoteSessionId_Type=Unsigned32
_Fs6374DMRemoteSessionId_Object=MibTableColumn
fs6374DMRemoteSessionId=_Fs6374DMRemoteSessionId_Object((1,3,6,1,4,1,29601,2,107,6,1,1,29),_Fs6374DMRemoteSessionId_Type())
fs6374DMRemoteSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMRemoteSessionId.setStatus(_A)
_Fs6374DMDyadicProactiveRole_Type=Integer32
_Fs6374DMDyadicProactiveRole_Object=MibTableColumn
fs6374DMDyadicProactiveRole=_Fs6374DMDyadicProactiveRole_Object((1,3,6,1,4,1,29601,2,107,6,1,1,30),_Fs6374DMDyadicProactiveRole_Type())
fs6374DMDyadicProactiveRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMDyadicProactiveRole.setStatus(_A)
_Fs6374DMStatsPaddingSize_Type=Unsigned32
_Fs6374DMStatsPaddingSize_Object=MibTableColumn
fs6374DMStatsPaddingSize=_Fs6374DMStatsPaddingSize_Object((1,3,6,1,4,1,29601,2,107,6,1,1,31),_Fs6374DMStatsPaddingSize_Type())
fs6374DMStatsPaddingSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374DMStatsPaddingSize.setStatus(_A)
class _Fs6374IsDMBufferSQIEnabled_Type(TruthValue):defaultValue=2
_Fs6374IsDMBufferSQIEnabled_Type.__name__=_L
_Fs6374IsDMBufferSQIEnabled_Object=MibTableColumn
fs6374IsDMBufferSQIEnabled=_Fs6374IsDMBufferSQIEnabled_Object((1,3,6,1,4,1,29601,2,107,6,1,1,32),_Fs6374IsDMBufferSQIEnabled_Type())
fs6374IsDMBufferSQIEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374IsDMBufferSQIEnabled.setStatus(_A)
_Fs6374Stats_ObjectIdentity=ObjectIdentity
fs6374Stats=_Fs6374Stats_ObjectIdentity((1,3,6,1,4,1,29601,2,107,7))
_Fs6374StatsTable_Object=MibTable
fs6374StatsTable=_Fs6374StatsTable_Object((1,3,6,1,4,1,29601,2,107,7,1))
if mibBuilder.loadTexts:fs6374StatsTable.setStatus(_A)
_Fs6374StatsTableEntry_Object=MibTableRow
fs6374StatsTableEntry=_Fs6374StatsTableEntry_Object((1,3,6,1,4,1,29601,2,107,7,1,1))
fs6374StatsTableEntry.setIndexNames((0,_D,_H),(0,_D,_J))
if mibBuilder.loadTexts:fs6374StatsTableEntry.setStatus(_A)
_Fs6374StatsLmmOut_Type=Unsigned32
_Fs6374StatsLmmOut_Object=MibTableColumn
fs6374StatsLmmOut=_Fs6374StatsLmmOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,1),_Fs6374StatsLmmOut_Type())
fs6374StatsLmmOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsLmmOut.setStatus(_A)
_Fs6374StatsLmmIn_Type=Unsigned32
_Fs6374StatsLmmIn_Object=MibTableColumn
fs6374StatsLmmIn=_Fs6374StatsLmmIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,2),_Fs6374StatsLmmIn_Type())
fs6374StatsLmmIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsLmmIn.setStatus(_A)
_Fs6374StatsLmrOut_Type=Unsigned32
_Fs6374StatsLmrOut_Object=MibTableColumn
fs6374StatsLmrOut=_Fs6374StatsLmrOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,3),_Fs6374StatsLmrOut_Type())
fs6374StatsLmrOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsLmrOut.setStatus(_A)
_Fs6374StatsLmrIn_Type=Unsigned32
_Fs6374StatsLmrIn_Object=MibTableColumn
fs6374StatsLmrIn=_Fs6374StatsLmrIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,4),_Fs6374StatsLmrIn_Type())
fs6374StatsLmrIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsLmrIn.setStatus(_A)
_Fs6374Stats1LmOut_Type=Unsigned32
_Fs6374Stats1LmOut_Object=MibTableColumn
fs6374Stats1LmOut=_Fs6374Stats1LmOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,5),_Fs6374Stats1LmOut_Type())
fs6374Stats1LmOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374Stats1LmOut.setStatus(_A)
_Fs6374Stats1LmIn_Type=Unsigned32
_Fs6374Stats1LmIn_Object=MibTableColumn
fs6374Stats1LmIn=_Fs6374Stats1LmIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,6),_Fs6374Stats1LmIn_Type())
fs6374Stats1LmIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374Stats1LmIn.setStatus(_A)
_Fs6374Stats1DmOut_Type=Unsigned32
_Fs6374Stats1DmOut_Object=MibTableColumn
fs6374Stats1DmOut=_Fs6374Stats1DmOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,7),_Fs6374Stats1DmOut_Type())
fs6374Stats1DmOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374Stats1DmOut.setStatus(_A)
_Fs6374Stats1DmIn_Type=Unsigned32
_Fs6374Stats1DmIn_Object=MibTableColumn
fs6374Stats1DmIn=_Fs6374Stats1DmIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,8),_Fs6374Stats1DmIn_Type())
fs6374Stats1DmIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374Stats1DmIn.setStatus(_A)
_Fs6374StatsDmmOut_Type=Unsigned32
_Fs6374StatsDmmOut_Object=MibTableColumn
fs6374StatsDmmOut=_Fs6374StatsDmmOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,9),_Fs6374StatsDmmOut_Type())
fs6374StatsDmmOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsDmmOut.setStatus(_A)
_Fs6374StatsDmmIn_Type=Unsigned32
_Fs6374StatsDmmIn_Object=MibTableColumn
fs6374StatsDmmIn=_Fs6374StatsDmmIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,10),_Fs6374StatsDmmIn_Type())
fs6374StatsDmmIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsDmmIn.setStatus(_A)
_Fs6374StatsDmrOut_Type=Unsigned32
_Fs6374StatsDmrOut_Object=MibTableColumn
fs6374StatsDmrOut=_Fs6374StatsDmrOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,11),_Fs6374StatsDmrOut_Type())
fs6374StatsDmrOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsDmrOut.setStatus(_A)
_Fs6374StatsDmrIn_Type=Unsigned32
_Fs6374StatsDmrIn_Object=MibTableColumn
fs6374StatsDmrIn=_Fs6374StatsDmrIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,12),_Fs6374StatsDmrIn_Type())
fs6374StatsDmrIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374StatsDmrIn.setStatus(_A)
_Fs6374StatsCmb1LmDmOut_Type=Unsigned32
_Fs6374StatsCmb1LmDmOut_Object=MibTableColumn
fs6374StatsCmb1LmDmOut=_Fs6374StatsCmb1LmDmOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,13),_Fs6374StatsCmb1LmDmOut_Type())
fs6374StatsCmb1LmDmOut.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374StatsCmb1LmDmOut.setStatus(_A)
_Fs6374StatsCmb1LmDmIn_Type=Unsigned32
_Fs6374StatsCmb1LmDmIn_Object=MibTableColumn
fs6374StatsCmb1LmDmIn=_Fs6374StatsCmb1LmDmIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,14),_Fs6374StatsCmb1LmDmIn_Type())
fs6374StatsCmb1LmDmIn.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374StatsCmb1LmDmIn.setStatus(_A)
_Fs6374StatsCmbLmmDmmOut_Type=Unsigned32
_Fs6374StatsCmbLmmDmmOut_Object=MibTableColumn
fs6374StatsCmbLmmDmmOut=_Fs6374StatsCmbLmmDmmOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,15),_Fs6374StatsCmbLmmDmmOut_Type())
fs6374StatsCmbLmmDmmOut.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374StatsCmbLmmDmmOut.setStatus(_A)
_Fs6374StatsCmbLmmDmmIn_Type=Unsigned32
_Fs6374StatsCmbLmmDmmIn_Object=MibTableColumn
fs6374StatsCmbLmmDmmIn=_Fs6374StatsCmbLmmDmmIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,16),_Fs6374StatsCmbLmmDmmIn_Type())
fs6374StatsCmbLmmDmmIn.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374StatsCmbLmmDmmIn.setStatus(_A)
_Fs6374StatsCmbLmrDmrOut_Type=Unsigned32
_Fs6374StatsCmbLmrDmrOut_Object=MibTableColumn
fs6374StatsCmbLmrDmrOut=_Fs6374StatsCmbLmrDmrOut_Object((1,3,6,1,4,1,29601,2,107,7,1,1,17),_Fs6374StatsCmbLmrDmrOut_Type())
fs6374StatsCmbLmrDmrOut.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374StatsCmbLmrDmrOut.setStatus(_A)
_Fs6374StatsCmbLmrDmrIn_Type=Unsigned32
_Fs6374StatsCmbLmrDmrIn_Object=MibTableColumn
fs6374StatsCmbLmrDmrIn=_Fs6374StatsCmbLmrDmrIn_Object((1,3,6,1,4,1,29601,2,107,7,1,1,18),_Fs6374StatsCmbLmrDmrIn_Type())
fs6374StatsCmbLmrDmrIn.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374StatsCmbLmrDmrIn.setStatus(_A)
_Fs6374SystemConfig_ObjectIdentity=ObjectIdentity
fs6374SystemConfig=_Fs6374SystemConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,107,8))
_Fs6374SystemConfigTable_Object=MibTable
fs6374SystemConfigTable=_Fs6374SystemConfigTable_Object((1,3,6,1,4,1,29601,2,107,8,1))
if mibBuilder.loadTexts:fs6374SystemConfigTable.setStatus(_A)
_Fs6374SystemConfigEntry_Object=MibTableRow
fs6374SystemConfigEntry=_Fs6374SystemConfigEntry_Object((1,3,6,1,4,1,29601,2,107,8,1,1))
fs6374SystemConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fs6374SystemConfigEntry.setStatus(_A)
class _Fs6374SystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_Fs6374SystemControl_Type.__name__=_E
_Fs6374SystemControl_Object=MibTableColumn
fs6374SystemControl=_Fs6374SystemControl_Object((1,3,6,1,4,1,29601,2,107,8,1,1,1),_Fs6374SystemControl_Type())
fs6374SystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374SystemControl.setStatus(_A)
class _Fs6374ModuleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_Fs6374ModuleStatus_Type.__name__=_E
_Fs6374ModuleStatus_Object=MibTableColumn
fs6374ModuleStatus=_Fs6374ModuleStatus_Object((1,3,6,1,4,1,29601,2,107,8,1,1,2),_Fs6374ModuleStatus_Type())
fs6374ModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374ModuleStatus.setStatus(_A)
_Fs6374DMBufferClear_Type=TruthValue
_Fs6374DMBufferClear_Object=MibTableColumn
fs6374DMBufferClear=_Fs6374DMBufferClear_Object((1,3,6,1,4,1,29601,2,107,8,1,1,3),_Fs6374DMBufferClear_Type())
fs6374DMBufferClear.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DMBufferClear.setStatus(_A)
_Fs6374LMBufferClear_Type=TruthValue
_Fs6374LMBufferClear_Object=MibTableColumn
fs6374LMBufferClear=_Fs6374LMBufferClear_Object((1,3,6,1,4,1,29601,2,107,8,1,1,4),_Fs6374LMBufferClear_Type())
fs6374LMBufferClear.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMBufferClear.setStatus(_A)
class _Fs6374DebugLevel_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fs6374DebugLevel_Type.__name__=_G
_Fs6374DebugLevel_Object=MibTableColumn
fs6374DebugLevel=_Fs6374DebugLevel_Object((1,3,6,1,4,1,29601,2,107,8,1,1,5),_Fs6374DebugLevel_Type())
fs6374DebugLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374DebugLevel.setStatus(_A)
_Fs6374TSFormatSupported_Type=FS6374SuppTimeStampFormat
_Fs6374TSFormatSupported_Object=MibTableColumn
fs6374TSFormatSupported=_Fs6374TSFormatSupported_Object((1,3,6,1,4,1,29601,2,107,8,1,1,6),_Fs6374TSFormatSupported_Type())
fs6374TSFormatSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fs6374TSFormatSupported.setStatus(_A)
_Fs6374Notifications_ObjectIdentity=ObjectIdentity
fs6374Notifications=_Fs6374Notifications_ObjectIdentity((1,3,6,1,4,1,29601,2,107,9))
_Fs6374NotificationsTable_Object=MibTable
fs6374NotificationsTable=_Fs6374NotificationsTable_Object((1,3,6,1,4,1,29601,2,107,9,1))
if mibBuilder.loadTexts:fs6374NotificationsTable.setStatus(_A)
_Fs6374NotificationsEntry_Object=MibTableRow
fs6374NotificationsEntry=_Fs6374NotificationsEntry_Object((1,3,6,1,4,1,29601,2,107,9,1,1))
fs6374NotificationsEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fs6374NotificationsEntry.setStatus(_A)
_Fs6374LMDMTrapControl_Type=FS6374Traps
_Fs6374LMDMTrapControl_Object=MibTableColumn
fs6374LMDMTrapControl=_Fs6374LMDMTrapControl_Object((1,3,6,1,4,1,29601,2,107,9,1,1,1),_Fs6374LMDMTrapControl_Type())
fs6374LMDMTrapControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fs6374LMDMTrapControl.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'FS6374Traps':FS6374Traps,_M:FS6374TimeStampFormat,_N:Fs6374TransmitStatus,'FS6374TimeRepresentation':FS6374TimeRepresentation,'FS6374SuppTimeStampFormat':FS6374SuppTimeStampFormat,'fs6374MIB':fs6374MIB,'fs6374ServiceConfig':fs6374ServiceConfig,'fs6374ServiceConfigTable':fs6374ServiceConfigTable,'fs6374ServiceConfigEntry':fs6374ServiceConfigEntry,_H:fs6374ContextId,_J:fs6374ServiceName,'fs6374MplsPathType':fs6374MplsPathType,'fs6374FwdTnlIdOrPwId':fs6374FwdTnlIdOrPwId,'fs6374RevTnlId':fs6374RevTnlId,'fs6374SrcIpAddr':fs6374SrcIpAddr,'fs6374DestIpAddr':fs6374DestIpAddr,'fs6374EncapType':fs6374EncapType,'fs6374TrafficClass':fs6374TrafficClass,'fs6374RowStatus':fs6374RowStatus,'fs6374DyadicMeasurement':fs6374DyadicMeasurement,'fs6374TSFNegotiation':fs6374TSFNegotiation,'fs6374TSNegotiatedFormat':fs6374TSNegotiatedFormat,'fs6374DyadicProactiveRole':fs6374DyadicProactiveRole,'fs6374QueryTransmitRetryCount':fs6374QueryTransmitRetryCount,'fs6374SessionIntervalQueryStatus':fs6374SessionIntervalQueryStatus,'fs6374MinReceptionIntervalInMilliseconds':fs6374MinReceptionIntervalInMilliseconds,'fs6374ParamsConfig':fs6374ParamsConfig,'fs6374ParamsConfigTable':fs6374ParamsConfigTable,'fs6374ParamsConfigTableEntry':fs6374ParamsConfigTableEntry,'fs6374LMType':fs6374LMType,'fs6374LMMethod':fs6374LMMethod,'fs6374LMMode':fs6374LMMode,'fs6374LMNoOfMessages':fs6374LMNoOfMessages,'fs6374LMTimeIntervalInMilliseconds':fs6374LMTimeIntervalInMilliseconds,'fs6374LMTimeStampFormat':fs6374LMTimeStampFormat,'fs6374LMTransmitStatus':fs6374LMTransmitStatus,'fs6374DMType':fs6374DMType,'fs6374DMMode':fs6374DMMode,'fs6374DMTimeIntervalInMilliseconds':fs6374DMTimeIntervalInMilliseconds,'fs6374DMNoOfMessages':fs6374DMNoOfMessages,'fs6374DMTimeStampFormat':fs6374DMTimeStampFormat,'fs6374DMTransmitStatus':fs6374DMTransmitStatus,'fs6374CmbLMDMType':fs6374CmbLMDMType,'fs6374CmbLMDMMethod':fs6374CmbLMDMMethod,'fs6374CmbLMDMMode':fs6374CmbLMDMMode,'fs6374CmbLMDMNoOfMessages':fs6374CmbLMDMNoOfMessages,'fs6374CmbLMDMTimeIntervalInMilliseconds':fs6374CmbLMDMTimeIntervalInMilliseconds,'fs6374CmbLMDMTimeStampFormat':fs6374CmbLMDMTimeStampFormat,'fs6374CmbLMDMTransmitStatus':fs6374CmbLMDMTransmitStatus,'fs6374DMPaddingSize':fs6374DMPaddingSize,'fs6374CmbLMDMPaddingSize':fs6374CmbLMDMPaddingSize,'fs6374LMBuffer':fs6374LMBuffer,'fs6374LMTable':fs6374LMTable,'fs6374LMTableEntry':fs6374LMTableEntry,_S:fs6374LMSessionId,_a:fs6374LMSeqNum,'fs6374LMTxLossAtSenderEnd':fs6374LMTxLossAtSenderEnd,'fs6374LMRxLossAtSenderEnd':fs6374LMRxLossAtSenderEnd,'fs6374LMRxLossAtReceiverEnd':fs6374LMRxLossAtReceiverEnd,'fs6374LMMeasurementTimeTakenInMilliseconds':fs6374LMMeasurementTimeTakenInMilliseconds,'fs6374LMTransmitResultOK':fs6374LMTransmitResultOK,'fs6374LMTestPktsCount':fs6374LMTestPktsCount,'fs6374DMBuffer':fs6374DMBuffer,'fs6374DMTable':fs6374DMTable,'fs6374DMTableEntry':fs6374DMTableEntry,_T:fs6374DMSessionId,_b:fs6374DMSeqNum,'fs6374DMDelayValue':fs6374DMDelayValue,'fs6374DMRTDelayValue':fs6374DMRTDelayValue,'fs6374DMIPDV':fs6374DMIPDV,'fs6374DMPDV':fs6374DMPDV,'fs6374DMTransmitResultOK':fs6374DMTransmitResultOK,'fs6374LMStats':fs6374LMStats,'fs6374LMStatsTable':fs6374LMStatsTable,'fs6374LMStatsTableEntry':fs6374LMStatsTableEntry,'fs6374LMStatsMplsType':fs6374LMStatsMplsType,'fs6374LMStatsFwdTnlIdOrPwId':fs6374LMStatsFwdTnlIdOrPwId,'fs6374LMStatsRevTnlId':fs6374LMStatsRevTnlId,'fs6374LMStatsSrcIpAddr':fs6374LMStatsSrcIpAddr,'fs6374LMStatsDestIpAddr':fs6374LMStatsDestIpAddr,'fs6374LMStatsTrafficClass':fs6374LMStatsTrafficClass,'fs6374LMStatsMode':fs6374LMStatsMode,'fs6374LMStatsMethod':fs6374LMStatsMethod,'fs6374LMStatsType':fs6374LMStatsType,'fs6374LMStatsTimeStampFormat':fs6374LMStatsTimeStampFormat,'fs6374LMStatsStartTime':fs6374LMStatsStartTime,'fs6374LMStatsFarEndLossMin':fs6374LMStatsFarEndLossMin,'fs6374LMStatsFarEndLossMax':fs6374LMStatsFarEndLossMax,'fs6374LMStatsFarEndLossAvg':fs6374LMStatsFarEndLossAvg,'fs6374LMStatsNearEndLossMin':fs6374LMStatsNearEndLossMin,'fs6374LMStatsNearEndLossMax':fs6374LMStatsNearEndLossMax,'fs6374LMStatsNearEndLossAvg':fs6374LMStatsNearEndLossAvg,'fs6374LMStatsTxPktCount':fs6374LMStatsTxPktCount,'fs6374LMStatsRxPktCount':fs6374LMStatsRxPktCount,'fs6374LMStatsThroughputpercent':fs6374LMStatsThroughputpercent,'fs6374LMStatsResponseErrors':fs6374LMStatsResponseErrors,'fs6374LMStatsResponseTimeout':fs6374LMStatsResponseTimeout,'fs6374LMStatsMeasurementOnGoing':fs6374LMStatsMeasurementOnGoing,'fs6374LMDyadicMeasurement':fs6374LMDyadicMeasurement,'fs6374LMRemoteSessionId':fs6374LMRemoteSessionId,'fs6374LMDyadicProactiveRole':fs6374LMDyadicProactiveRole,'fs6374IsLMBufferSQIEnabled':fs6374IsLMBufferSQIEnabled,'fs6374DMStats':fs6374DMStats,'fs6374DMStatsTable':fs6374DMStatsTable,'fs6374DMStatsTableEntry':fs6374DMStatsTableEntry,'fs6374DMStatsMplsType':fs6374DMStatsMplsType,'fs6374DMStatsFwdTnlIdOrPwId':fs6374DMStatsFwdTnlIdOrPwId,'fs6374DMStatsRevTnlId':fs6374DMStatsRevTnlId,'fs6374DMStatsSrcIpAddr':fs6374DMStatsSrcIpAddr,'fs6374DMStatsDestIpAddr':fs6374DMStatsDestIpAddr,'fs6374DMStatsTrafficClass':fs6374DMStatsTrafficClass,'fs6374DMStatsMode':fs6374DMStatsMode,'fs6374DMStatsType':fs6374DMStatsType,'fs6374DMStatsTimeStampFormat':fs6374DMStatsTimeStampFormat,'fs6374DMStatsStartTime':fs6374DMStatsStartTime,'fs6374DMStatsMinDelay':fs6374DMStatsMinDelay,'fs6374DMStatsMaxDelay':fs6374DMStatsMaxDelay,'fs6374DMStatsAvgDelay':fs6374DMStatsAvgDelay,'fs6374DMStatsMinRTDelay':fs6374DMStatsMinRTDelay,'fs6374DMStatsMaxRTDelay':fs6374DMStatsMaxRTDelay,'fs6374DMStatsAvgRTDelay':fs6374DMStatsAvgRTDelay,'fs6374DMStatsMinIPDV':fs6374DMStatsMinIPDV,'fs6374DMStatsMaxIPDV':fs6374DMStatsMaxIPDV,'fs6374DMStatsAvgIPDV':fs6374DMStatsAvgIPDV,'fs6374DMStatsMinPDV':fs6374DMStatsMinPDV,'fs6374DMStatsMaxPDV':fs6374DMStatsMaxPDV,'fs6374DMStatsAvgPDV':fs6374DMStatsAvgPDV,'fs6374DMStatsTxPktCount':fs6374DMStatsTxPktCount,'fs6374DMStatsRxPktCount':fs6374DMStatsRxPktCount,'fs6374DMStatsResponseErrors':fs6374DMStatsResponseErrors,'fs6374DMStatsResponseTimeout':fs6374DMStatsResponseTimeout,'fs6374DMStatsMeasurementOnGoing':fs6374DMStatsMeasurementOnGoing,'fs6374DMDyadicMeasurement':fs6374DMDyadicMeasurement,'fs6374DMRemoteSessionId':fs6374DMRemoteSessionId,'fs6374DMDyadicProactiveRole':fs6374DMDyadicProactiveRole,'fs6374DMStatsPaddingSize':fs6374DMStatsPaddingSize,'fs6374IsDMBufferSQIEnabled':fs6374IsDMBufferSQIEnabled,'fs6374Stats':fs6374Stats,'fs6374StatsTable':fs6374StatsTable,'fs6374StatsTableEntry':fs6374StatsTableEntry,'fs6374StatsLmmOut':fs6374StatsLmmOut,'fs6374StatsLmmIn':fs6374StatsLmmIn,'fs6374StatsLmrOut':fs6374StatsLmrOut,'fs6374StatsLmrIn':fs6374StatsLmrIn,'fs6374Stats1LmOut':fs6374Stats1LmOut,'fs6374Stats1LmIn':fs6374Stats1LmIn,'fs6374Stats1DmOut':fs6374Stats1DmOut,'fs6374Stats1DmIn':fs6374Stats1DmIn,'fs6374StatsDmmOut':fs6374StatsDmmOut,'fs6374StatsDmmIn':fs6374StatsDmmIn,'fs6374StatsDmrOut':fs6374StatsDmrOut,'fs6374StatsDmrIn':fs6374StatsDmrIn,'fs6374StatsCmb1LmDmOut':fs6374StatsCmb1LmDmOut,'fs6374StatsCmb1LmDmIn':fs6374StatsCmb1LmDmIn,'fs6374StatsCmbLmmDmmOut':fs6374StatsCmbLmmDmmOut,'fs6374StatsCmbLmmDmmIn':fs6374StatsCmbLmmDmmIn,'fs6374StatsCmbLmrDmrOut':fs6374StatsCmbLmrDmrOut,'fs6374StatsCmbLmrDmrIn':fs6374StatsCmbLmrDmrIn,'fs6374SystemConfig':fs6374SystemConfig,'fs6374SystemConfigTable':fs6374SystemConfigTable,'fs6374SystemConfigEntry':fs6374SystemConfigEntry,'fs6374SystemControl':fs6374SystemControl,'fs6374ModuleStatus':fs6374ModuleStatus,'fs6374DMBufferClear':fs6374DMBufferClear,'fs6374LMBufferClear':fs6374LMBufferClear,'fs6374DebugLevel':fs6374DebugLevel,'fs6374TSFormatSupported':fs6374TSFormatSupported,'fs6374Notifications':fs6374Notifications,'fs6374NotificationsTable':fs6374NotificationsTable,'fs6374NotificationsEntry':fs6374NotificationsEntry,'fs6374LMDMTrapControl':fs6374LMDMTrapControl})