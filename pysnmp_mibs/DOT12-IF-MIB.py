_j='dot12StatsGroup'
_i='dot12ConfigGroup'
_h='dot12HCOutHighPriorityOctets'
_g='dot12HCInNormPriorityOctets'
_f='dot12HCInHighPriorityOctets'
_e='dot12TransitionIntoTrainings'
_d='dot12OutHighPriorityOctets'
_c='dot12OutHighPriorityFrames'
_b='dot12InNullAddressedFrames'
_a='dot12InDataErrors'
_Z='dot12InOversizeFrameErrors'
_Y='dot12InIPMErrors'
_X='dot12InNormPriorityOctets'
_W='dot12InNormPriorityFrames'
_V='dot12InHighPriorityOctets'
_U='dot12InHighPriorityFrames'
_T='dot12ControlMode'
_S='dot12CurrentFramingType'
_R='dot12Status'
_Q='dot12Commands'
_P='dot12LastTrainingConfig'
_O='dot12TrainingVersion'
_N='dot12DesiredPromiscStatus'
_M='dot12FramingCapability'
_L='dot12DesiredFramingType'
_K='frameTypeEither'
_J='OctetString'
_I='frameType88025'
_H='frameType88023'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='DOT12-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dot12MIB=ModuleIdentity((1,3,6,1,2,1,10,45))
_Dot12MIBObjects_ObjectIdentity=ObjectIdentity
dot12MIBObjects=_Dot12MIBObjects_ObjectIdentity((1,3,6,1,2,1,10,45,1))
_Dot12ConfigTable_Object=MibTable
dot12ConfigTable=_Dot12ConfigTable_Object((1,3,6,1,2,1,10,45,1,1))
if mibBuilder.loadTexts:dot12ConfigTable.setStatus(_A)
_Dot12ConfigEntry_Object=MibTableRow
dot12ConfigEntry=_Dot12ConfigEntry_Object((1,3,6,1,2,1,10,45,1,1,1))
dot12ConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot12ConfigEntry.setStatus(_A)
class _Dot12CurrentFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('frameTypeUnknown',3)))
_Dot12CurrentFramingType_Type.__name__=_D
_Dot12CurrentFramingType_Object=MibTableColumn
dot12CurrentFramingType=_Dot12CurrentFramingType_Object((1,3,6,1,2,1,10,45,1,1,1,1),_Dot12CurrentFramingType_Type())
dot12CurrentFramingType.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12CurrentFramingType.setStatus(_A)
class _Dot12DesiredFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_K,3)))
_Dot12DesiredFramingType_Type.__name__=_D
_Dot12DesiredFramingType_Object=MibTableColumn
dot12DesiredFramingType=_Dot12DesiredFramingType_Object((1,3,6,1,2,1,10,45,1,1,1,2),_Dot12DesiredFramingType_Type())
dot12DesiredFramingType.setMaxAccess(_E)
if mibBuilder.loadTexts:dot12DesiredFramingType.setStatus(_A)
class _Dot12FramingCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_K,3)))
_Dot12FramingCapability_Type.__name__=_D
_Dot12FramingCapability_Object=MibTableColumn
dot12FramingCapability=_Dot12FramingCapability_Object((1,3,6,1,2,1,10,45,1,1,1,3),_Dot12FramingCapability_Type())
dot12FramingCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12FramingCapability.setStatus(_A)
class _Dot12DesiredPromiscStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleAddressMode',1),('promiscuousMode',2)))
_Dot12DesiredPromiscStatus_Type.__name__=_D
_Dot12DesiredPromiscStatus_Object=MibTableColumn
dot12DesiredPromiscStatus=_Dot12DesiredPromiscStatus_Object((1,3,6,1,2,1,10,45,1,1,1,4),_Dot12DesiredPromiscStatus_Type())
dot12DesiredPromiscStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot12DesiredPromiscStatus.setStatus(_A)
class _Dot12TrainingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot12TrainingVersion_Type.__name__=_D
_Dot12TrainingVersion_Object=MibTableColumn
dot12TrainingVersion=_Dot12TrainingVersion_Object((1,3,6,1,2,1,10,45,1,1,1,5),_Dot12TrainingVersion_Type())
dot12TrainingVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12TrainingVersion.setStatus(_A)
class _Dot12LastTrainingConfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Dot12LastTrainingConfig_Type.__name__=_J
_Dot12LastTrainingConfig_Object=MibTableColumn
dot12LastTrainingConfig=_Dot12LastTrainingConfig_Object((1,3,6,1,2,1,10,45,1,1,1,6),_Dot12LastTrainingConfig_Type())
dot12LastTrainingConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12LastTrainingConfig.setStatus(_A)
class _Dot12Commands_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOp',1),('open',2),('reset',3),('close',4)))
_Dot12Commands_Type.__name__=_D
_Dot12Commands_Object=MibTableColumn
dot12Commands=_Dot12Commands_Object((1,3,6,1,2,1,10,45,1,1,1,7),_Dot12Commands_Type())
dot12Commands.setMaxAccess(_E)
if mibBuilder.loadTexts:dot12Commands.setStatus(_A)
class _Dot12Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6)));namedValues=NamedValues(*(('opened',1),('closed',2),('opening',3),('openFailure',5),('linkFailure',6)))
_Dot12Status_Type.__name__=_D
_Dot12Status_Object=MibTableColumn
dot12Status=_Dot12Status_Object((1,3,6,1,2,1,10,45,1,1,1,8),_Dot12Status_Type())
dot12Status.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12Status.setStatus(_A)
class _Dot12ControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('masterMode',1),('slaveMode',2),('learn',3)))
_Dot12ControlMode_Type.__name__=_D
_Dot12ControlMode_Object=MibTableColumn
dot12ControlMode=_Dot12ControlMode_Object((1,3,6,1,2,1,10,45,1,1,1,9),_Dot12ControlMode_Type())
dot12ControlMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dot12ControlMode.setStatus(_A)
_Dot12StatTable_Object=MibTable
dot12StatTable=_Dot12StatTable_Object((1,3,6,1,2,1,10,45,1,2))
if mibBuilder.loadTexts:dot12StatTable.setStatus(_A)
_Dot12StatEntry_Object=MibTableRow
dot12StatEntry=_Dot12StatEntry_Object((1,3,6,1,2,1,10,45,1,2,1))
dot12StatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot12StatEntry.setStatus(_A)
_Dot12InHighPriorityFrames_Type=Counter32
_Dot12InHighPriorityFrames_Object=MibTableColumn
dot12InHighPriorityFrames=_Dot12InHighPriorityFrames_Object((1,3,6,1,2,1,10,45,1,2,1,1),_Dot12InHighPriorityFrames_Type())
dot12InHighPriorityFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InHighPriorityFrames.setStatus(_A)
_Dot12InHighPriorityOctets_Type=Counter32
_Dot12InHighPriorityOctets_Object=MibTableColumn
dot12InHighPriorityOctets=_Dot12InHighPriorityOctets_Object((1,3,6,1,2,1,10,45,1,2,1,2),_Dot12InHighPriorityOctets_Type())
dot12InHighPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InHighPriorityOctets.setStatus(_A)
_Dot12InNormPriorityFrames_Type=Counter32
_Dot12InNormPriorityFrames_Object=MibTableColumn
dot12InNormPriorityFrames=_Dot12InNormPriorityFrames_Object((1,3,6,1,2,1,10,45,1,2,1,3),_Dot12InNormPriorityFrames_Type())
dot12InNormPriorityFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InNormPriorityFrames.setStatus(_A)
_Dot12InNormPriorityOctets_Type=Counter32
_Dot12InNormPriorityOctets_Object=MibTableColumn
dot12InNormPriorityOctets=_Dot12InNormPriorityOctets_Object((1,3,6,1,2,1,10,45,1,2,1,4),_Dot12InNormPriorityOctets_Type())
dot12InNormPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InNormPriorityOctets.setStatus(_A)
_Dot12InIPMErrors_Type=Counter32
_Dot12InIPMErrors_Object=MibTableColumn
dot12InIPMErrors=_Dot12InIPMErrors_Object((1,3,6,1,2,1,10,45,1,2,1,5),_Dot12InIPMErrors_Type())
dot12InIPMErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InIPMErrors.setStatus(_A)
_Dot12InOversizeFrameErrors_Type=Counter32
_Dot12InOversizeFrameErrors_Object=MibTableColumn
dot12InOversizeFrameErrors=_Dot12InOversizeFrameErrors_Object((1,3,6,1,2,1,10,45,1,2,1,6),_Dot12InOversizeFrameErrors_Type())
dot12InOversizeFrameErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InOversizeFrameErrors.setStatus(_A)
_Dot12InDataErrors_Type=Counter32
_Dot12InDataErrors_Object=MibTableColumn
dot12InDataErrors=_Dot12InDataErrors_Object((1,3,6,1,2,1,10,45,1,2,1,7),_Dot12InDataErrors_Type())
dot12InDataErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InDataErrors.setStatus(_A)
_Dot12InNullAddressedFrames_Type=Counter32
_Dot12InNullAddressedFrames_Object=MibTableColumn
dot12InNullAddressedFrames=_Dot12InNullAddressedFrames_Object((1,3,6,1,2,1,10,45,1,2,1,8),_Dot12InNullAddressedFrames_Type())
dot12InNullAddressedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12InNullAddressedFrames.setStatus(_A)
_Dot12OutHighPriorityFrames_Type=Counter32
_Dot12OutHighPriorityFrames_Object=MibTableColumn
dot12OutHighPriorityFrames=_Dot12OutHighPriorityFrames_Object((1,3,6,1,2,1,10,45,1,2,1,9),_Dot12OutHighPriorityFrames_Type())
dot12OutHighPriorityFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12OutHighPriorityFrames.setStatus(_A)
_Dot12OutHighPriorityOctets_Type=Counter32
_Dot12OutHighPriorityOctets_Object=MibTableColumn
dot12OutHighPriorityOctets=_Dot12OutHighPriorityOctets_Object((1,3,6,1,2,1,10,45,1,2,1,10),_Dot12OutHighPriorityOctets_Type())
dot12OutHighPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12OutHighPriorityOctets.setStatus(_A)
_Dot12TransitionIntoTrainings_Type=Counter32
_Dot12TransitionIntoTrainings_Object=MibTableColumn
dot12TransitionIntoTrainings=_Dot12TransitionIntoTrainings_Object((1,3,6,1,2,1,10,45,1,2,1,11),_Dot12TransitionIntoTrainings_Type())
dot12TransitionIntoTrainings.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12TransitionIntoTrainings.setStatus(_A)
_Dot12HCInHighPriorityOctets_Type=Counter64
_Dot12HCInHighPriorityOctets_Object=MibTableColumn
dot12HCInHighPriorityOctets=_Dot12HCInHighPriorityOctets_Object((1,3,6,1,2,1,10,45,1,2,1,12),_Dot12HCInHighPriorityOctets_Type())
dot12HCInHighPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12HCInHighPriorityOctets.setStatus(_A)
_Dot12HCInNormPriorityOctets_Type=Counter64
_Dot12HCInNormPriorityOctets_Object=MibTableColumn
dot12HCInNormPriorityOctets=_Dot12HCInNormPriorityOctets_Object((1,3,6,1,2,1,10,45,1,2,1,13),_Dot12HCInNormPriorityOctets_Type())
dot12HCInNormPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12HCInNormPriorityOctets.setStatus(_A)
_Dot12HCOutHighPriorityOctets_Type=Counter64
_Dot12HCOutHighPriorityOctets_Object=MibTableColumn
dot12HCOutHighPriorityOctets=_Dot12HCOutHighPriorityOctets_Object((1,3,6,1,2,1,10,45,1,2,1,14),_Dot12HCOutHighPriorityOctets_Type())
dot12HCOutHighPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dot12HCOutHighPriorityOctets.setStatus(_A)
_Dot12Conformance_ObjectIdentity=ObjectIdentity
dot12Conformance=_Dot12Conformance_ObjectIdentity((1,3,6,1,2,1,10,45,2))
_Dot12Compliances_ObjectIdentity=ObjectIdentity
dot12Compliances=_Dot12Compliances_ObjectIdentity((1,3,6,1,2,1,10,45,2,1))
_Dot12Groups_ObjectIdentity=ObjectIdentity
dot12Groups=_Dot12Groups_ObjectIdentity((1,3,6,1,2,1,10,45,2,2))
dot12ConfigGroup=ObjectGroup((1,3,6,1,2,1,10,45,2,2,1))
dot12ConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:dot12ConfigGroup.setStatus(_A)
dot12StatsGroup=ObjectGroup((1,3,6,1,2,1,10,45,2,2,2))
dot12StatsGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:dot12StatsGroup.setStatus(_A)
dot12Compliance=ModuleCompliance((1,3,6,1,2,1,10,45,2,1,1))
dot12Compliance.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:dot12Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dot12MIB':dot12MIB,'dot12MIBObjects':dot12MIBObjects,'dot12ConfigTable':dot12ConfigTable,'dot12ConfigEntry':dot12ConfigEntry,_S:dot12CurrentFramingType,_L:dot12DesiredFramingType,_M:dot12FramingCapability,_N:dot12DesiredPromiscStatus,_O:dot12TrainingVersion,_P:dot12LastTrainingConfig,_Q:dot12Commands,_R:dot12Status,_T:dot12ControlMode,'dot12StatTable':dot12StatTable,'dot12StatEntry':dot12StatEntry,_U:dot12InHighPriorityFrames,_V:dot12InHighPriorityOctets,_W:dot12InNormPriorityFrames,_X:dot12InNormPriorityOctets,_Y:dot12InIPMErrors,_Z:dot12InOversizeFrameErrors,_a:dot12InDataErrors,_b:dot12InNullAddressedFrames,_c:dot12OutHighPriorityFrames,_d:dot12OutHighPriorityOctets,_e:dot12TransitionIntoTrainings,_f:dot12HCInHighPriorityOctets,_g:dot12HCInNormPriorityOctets,_h:dot12HCOutHighPriorityOctets,'dot12Conformance':dot12Conformance,'dot12Compliances':dot12Compliances,'dot12Compliance':dot12Compliance,'dot12Groups':dot12Groups,_i:dot12ConfigGroup,_j:dot12StatsGroup})